"""
Prueba de integración de extremo a extremo (E2E) para NewBit (PY-NB-001 / Paso D-10).
Ejecuta el ciclo de vida completo del MVP (Sprints 1 y 2 – 15 Puntos de Historia):
Ingesta -> Submuestreo -> Calibración -> Detección YOLOv8 -> Agrupamiento Temporal -> Síntesis MP4.
Utiliza un video de prueba de CCTV de taller metalmecánico representativo de Kafaoğlu et al.
"""

import sys
import unittest
import cv2
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from fastapi.testclient import TestClient
from app.main import app
from app import config, db
from tests.fixtures.generate_fixture import generate_sample_metalworking_clip


class TestE2EPipeline(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        db.init_db()
        cls.client = TestClient(app)

        # 1. Asegurar existencia del fixture de video de taller metalmecánico
        cls.fixture_path = (
            Path(__file__).resolve().parent / "fixtures" / "sample_metalworking_clip.mp4"
        )
        if not cls.fixture_path.exists():
            generate_sample_metalworking_clip(cls.fixture_path)

        cls.video_id = None

    @classmethod
    def tearDownClass(cls):
        # Limpieza completa de artefactos generados en la prueba E2E
        if cls.video_id:
            vid = db.get_video_by_id(cls.video_id)
            if vid and Path(vid["filepath"]).exists():
                try:
                    Path(vid["filepath"]).unlink()
                except Exception:
                    pass

            frames_dir = config.FRAMES_DIR / cls.video_id
            if frames_dir.exists():
                import shutil
                shutil.rmtree(frames_dir)

            out_video = config.OUTPUTS_DIR / f"{cls.video_id}_processed.mp4"
            if out_video.exists():
                try:
                    out_video.unlink()
                except Exception:
                    pass

            db.delete_video_record(cls.video_id)

    def test_e2e_full_lifecycle(self):
        """Ejecuta secuencialmente todas las etapas del pipeline de Unsafe-Net."""

        # -------------------------------------------------------------
        # 1. Comprobación de salud técnica del servidor
        # -------------------------------------------------------------
        health_res = self.client.get("/api/health")
        self.assertEqual(health_res.status_code, 200)
        health_data = health_res.json()
        self.assertEqual(health_data["status"], "ok")
        self.assertEqual(health_data["code"], config.PROJECT_CODE)
        self.assertTrue(health_data["weights_present"])

        # -------------------------------------------------------------
        # 2. HU01: Ingesta de video y extracción de metadatos con OpenCV
        # -------------------------------------------------------------
        with open(self.fixture_path, "rb") as f:
            upload_res = self.client.post(
                "/api/videos/upload",
                files={"file": ("cctv_nave14_kafaoglu.mp4", f, "video/mp4")},
            )
        self.assertEqual(upload_res.status_code, 201)
        upload_data = upload_res.json()
        self.assertEqual(upload_data["status"], "success")

        video_record = upload_data["video"]
        TestE2EPipeline.video_id = video_record["id"]
        vid_id = self.video_id

        # Verificar metadatos técnicos auténticos extraídos con OpenCV
        self.assertEqual(video_record["fps"], 24.0)
        self.assertEqual(video_record["duration_sec"], 5.0)
        self.assertEqual(video_record["frame_count"], 120)
        self.assertEqual(video_record["width"], 640)
        self.assertEqual(video_record["height"], 480)
        self.assertEqual(video_record["status"], "uploaded")

        # -------------------------------------------------------------
        # 3. HU02 / HU03: Vista web del catálogo y ficha técnica
        # -------------------------------------------------------------
        catalog_res = self.client.get("/videos")
        self.assertEqual(catalog_res.status_code, 200)
        self.assertIn("cctv_nave14_kafaoglu.mp4", catalog_res.text)

        detail_res = self.client.get(f"/videos/{vid_id}")
        self.assertEqual(detail_res.status_code, 200)
        self.assertIn(vid_id, detail_res.text)
        self.assertIn("Ficha Técnica", detail_res.text)

        # -------------------------------------------------------------
        # 4. HU04: Submuestreo inteligente de frames (reducción a 5.0 FPS)
        # -------------------------------------------------------------
        sample_res = self.client.post(f"/api/videos/{vid_id}/sample?target_fps=5.0")
        self.assertEqual(sample_res.status_code, 200)
        sample_data = sample_res.json()
        self.assertEqual(sample_data["status"], "success")

        metrics = sample_data["metrics"]
        self.assertEqual(metrics["stride"], 5)  # round(24 / 5) = 5
        self.assertEqual(metrics["sampled_frames"], 24)  # 120 frames / 5 = 24
        self.assertEqual(metrics["reduction_pct"], 80.0)  # 80% ahorro temporal

        # Verificar fotogramas normalizados en disco a 640x640
        frames_dir = config.FRAMES_DIR / vid_id
        saved_frames = sorted(list(frames_dir.glob("*.jpg")))
        self.assertEqual(len(saved_frames), 24)

        first_frame = cv2.imread(str(saved_frames[0]))
        self.assertEqual((first_frame.shape[1], first_frame.shape[0]), (640, 640))

        # -------------------------------------------------------------
        # 5. HU11: Calibración dinámica de umbrales YOLOv8
        # -------------------------------------------------------------
        calib_res = self.client.post(
            "/api/calibration",
            json={
                "confidence": 0.35,
                "iou": 0.45,
                "target_fps": 5.0,
                "changed_by": "Jorge (TI Planta)",
                "note": "Calibración operativa para cámara 14 de taller",
            },
        )
        self.assertEqual(calib_res.status_code, 200)
        active_calib = db.get_calibration_settings()
        self.assertEqual(active_calib["confidence"], 0.35)
        self.assertEqual(active_calib["iou"], 0.45)

        # -------------------------------------------------------------
        # 6. HU05: Inferencia espacial con YOLOv8n (detección de operarios)
        # -------------------------------------------------------------
        detect_res = self.client.post(f"/api/videos/{vid_id}/detect")
        self.assertEqual(detect_res.status_code, 200)
        detect_data = detect_res.json()
        self.assertEqual(detect_data["status"], "success")

        det_metrics = detect_data["metrics"]
        self.assertEqual(det_metrics["total_frames_analyzed"], 24)
        # Debe haber detectado presencia humana en la fase activa del fixture
        self.assertGreater(det_metrics["active_frames_count"], 0)
        self.assertGreater(det_metrics["inactive_frames_count"], 0)
        self.assertGreater(det_metrics["total_detections_count"], 0)

        # Verificar persistencia en base de datos
        db_video = db.get_video_by_id(vid_id)
        self.assertEqual(db_video["status"], "detected")
        self.assertEqual(db_video["active_frames_count"], det_metrics["active_frames_count"])
        self.assertEqual(db_video["detected_workers_count"], det_metrics["total_detections_count"])

        # Verificar que se generaron las imágenes con bounding boxes
        annotated_dir = frames_dir / "annotated"
        annotated_imgs = list(annotated_dir.glob("*.jpg"))
        self.assertEqual(len(annotated_imgs), 24)

        # -------------------------------------------------------------
        # 7. HU06: Agrupamiento temporal y renderizado de clip filtrado
        # -------------------------------------------------------------
        render_res = self.client.post(
            f"/api/videos/{vid_id}/group-and-render?min_duration=1.0"
        )
        self.assertEqual(render_res.status_code, 200)
        render_data = render_res.json()
        self.assertEqual(render_data["status"], "success")

        pipeline_result = render_data["result"]
        self.assertEqual(pipeline_result["status"], "completed")
        self.assertGreater(pipeline_result["processed_frame_count"], 0)
        self.assertLess(
            pipeline_result["processed_duration_sec"],
            video_record["duration_sec"],
        )
        self.assertGreater(pipeline_result["time_reduction_pct"], 0.0)

        # -------------------------------------------------------------
        # 8. Verificación de salida MP4 y streaming HTTP
        # -------------------------------------------------------------
        out_mp4_path = Path(pipeline_result["output_filepath"])
        self.assertTrue(out_mp4_path.exists())
        self.assertGreater(out_mp4_path.stat().st_size, 0)

        # Validar reproducibilidad con OpenCV
        cap = cv2.VideoCapture(str(out_mp4_path))
        self.assertTrue(cap.isOpened(), "El video MP4 de salida debe ser reproducible.")
        ret, read_frame = cap.read()
        self.assertTrue(ret, "Debe poder leerse al menos el primer fotograma del MP4.")
        self.assertEqual((read_frame.shape[1], read_frame.shape[0]), (640, 640))
        cap.release()

        # Streaming HTTP
        stream_res = self.client.get(f"/api/videos/{vid_id}/processed-stream")
        self.assertEqual(stream_res.status_code, 200)
        self.assertEqual(stream_res.headers["content-type"], "video/mp4")

        # -------------------------------------------------------------
        # 9. Verificación de estado final en SQLite y Dashboard
        # -------------------------------------------------------------
        final_video = db.get_video_by_id(vid_id)
        self.assertEqual(final_video["status"], "completed")
        self.assertEqual(final_video["processed_video_path"], str(out_mp4_path))
        self.assertEqual(
            final_video["processed_frame_count"], pipeline_result["processed_frame_count"]
        )

        final_detail_res = self.client.get(f"/videos/{vid_id}")
        self.assertEqual(final_detail_res.status_code, 200)
        self.assertIn("Clip Procesado Final", final_detail_res.text)
        self.assertIn("Descargar Clip MP4", final_detail_res.text)


if __name__ == "__main__":
    unittest.main()
