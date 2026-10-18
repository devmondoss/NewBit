"""
Pruebas automatizadas del motor de inferencia espacial YOLOv8n (Sprint 2: HU05 / Paso D-08).
Verifica carga del detector, inferencia sobre fotogramas, dibujo de bounding boxes y endpoints API.
"""

import sys
import unittest
import tempfile
import cv2
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from fastapi.testclient import TestClient
from app.main import app
from app import config, db
from ml.detector import YOLOv8Detector


def create_synthetic_frame(width: int = 640, height: int = 640) -> np.ndarray:
    """Genera un fotograma sintético RGB de prueba."""
    img = np.full((height, width, 3), 120, dtype=np.uint8)
    cv2.putText(
        img,
        "TEST FRAME",
        (50, 300),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.5,
        (255, 255, 255),
        2,
        cv2.LINE_AA,
    )
    return img


class TestDetector(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        db.init_db()
        cls.client = TestClient(app)
        cls.temp_dir = tempfile.TemporaryDirectory()
        cls.temp_path = Path(cls.temp_dir.name)

        # Generar video sintético de 24 FPS y 24 fotogramas (1 segundo)
        cls.sample_video = cls.temp_path / "detector_test_clip.mp4"
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        out = cv2.VideoWriter(str(cls.sample_video), fourcc, 24, (640, 480))
        for i in range(24):
            frame = np.full((480, 640, 3), (i * 10) % 255, dtype=np.uint8)
            out.write(frame)
        out.release()

        # Cargar video en la API para obtener registro en SQLite
        with open(cls.sample_video, "rb") as f:
            res = cls.client.post(
                "/api/videos/upload",
                files={"file": ("detector_test_clip.mp4", f, "video/mp4")},
            )
        cls.video_data = res.json()["video"]
        cls.video_id = cls.video_data["id"]

        # Ejecutar submuestreo para generar fotogramas base en storage/frames/{id}
        cls.client.post(f"/api/videos/{cls.video_id}/sample?target_fps=5.0")

    @classmethod
    def tearDownClass(cls):
        cls.temp_dir.cleanup()
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
        db.delete_video_record(cls.video_id)

    def test_01_singleton_pattern(self):
        """Verifica que YOLOv8Detector funcione como singleton reutilizable."""
        det1 = YOLOv8Detector.get_instance()
        det2 = YOLOv8Detector.get_instance()
        self.assertIs(det1, det2)
        self.assertIsNotNone(det1.model)

    def test_02_detect_frame_structure(self):
        """Verifica la estructura del resultado de detección sobre un fotograma."""
        detector = YOLOv8Detector.get_instance()
        frame = create_synthetic_frame()
        res = detector.detect_frame(frame, conf=0.5, iou=0.45)

        self.assertIn("has_detections", res)
        self.assertIn("detections_count", res)
        self.assertIn("detections", res)
        self.assertIn("conf_used", res)
        self.assertIn("iou_used", res)
        self.assertEqual(res["conf_used"], 0.5)
        self.assertEqual(res["iou_used"], 0.45)
        self.assertIsInstance(res["detections"], list)

    def test_03_draw_bounding_boxes(self):
        """Verifica que el dibujo de bounding boxes preserve dimensiones y retorne imagen válida."""
        detector = YOLOv8Detector.get_instance()
        frame = create_synthetic_frame(640, 640)
        dummy_detections = [
            {
                "box": [100.0, 100.0, 300.0, 450.0],
                "confidence": 0.89,
                "class_id": 0,
                "label": "operario",
            }
        ]
        annotated = detector.draw_bounding_boxes(frame, dummy_detections)
        self.assertEqual(annotated.shape, frame.shape)
        # Debe haber píxeles verdes esmeralda dibujados (color de detección: 80, 180, 50)
        self.assertTrue(np.any(annotated[:, :, 1] == 180))

    def test_04_process_video_frames_batch(self):
        """Verifica el procesamiento por lote de fotogramas y la creación de la carpeta annotated/."""
        detector = YOLOv8Detector.get_instance()
        metrics = detector.process_video_frames(self.video_id, conf=0.3, iou=0.45)

        self.assertEqual(metrics["video_id"], self.video_id)
        self.assertGreater(metrics["total_frames_analyzed"], 0)
        self.assertEqual(
            metrics["total_frames_analyzed"],
            metrics["active_frames_count"] + metrics["inactive_frames_count"],
        )
        self.assertIn("spatial_filter_reduction_pct", metrics)

        annotated_dir = config.FRAMES_DIR / self.video_id / "annotated"
        self.assertTrue(annotated_dir.exists())
        annotated_files = list(annotated_dir.glob("*.jpg"))
        self.assertEqual(len(annotated_files), metrics["total_frames_analyzed"])

    def test_05_api_detect_endpoint(self):
        """Verifica el endpoint POST /api/videos/{video_id}/detect y la persistencia en DB."""
        response = self.client.post(
            f"/api/videos/{self.video_id}/detect?conf=0.35&iou=0.45"
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "success")
        self.assertIn("metrics", data)

        # Verificar actualización en SQLite
        video = db.get_video_by_id(self.video_id)
        self.assertEqual(video["status"], "detected")
        self.assertIsNotNone(video["active_frames_count"])
        self.assertIsNotNone(video["detected_workers_count"])

    def test_06_api_get_annotated_frame(self):
        """Verifica que el endpoint GET /api/videos/{video_id}/annotated-frames/{filename} sirva la imagen."""
        annotated_dir = config.FRAMES_DIR / self.video_id / "annotated"
        annotated_files = sorted([f.name for f in annotated_dir.glob("*.jpg")])
        self.assertTrue(len(annotated_files) > 0)

        first_frame = annotated_files[0]
        res = self.client.get(
            f"/api/videos/{self.video_id}/annotated-frames/{first_frame}"
        )
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.headers["content-type"], "image/jpeg")

    def test_07_api_annotated_frame_not_found(self):
        """Verifica código 404 al solicitar un fotograma anotado inexistente."""
        res = self.client.get(
            f"/api/videos/{self.video_id}/annotated-frames/non_existent_frame.jpg"
        )
        self.assertEqual(res.status_code, 404)

    def test_08_api_detections_summary(self):
        """Verifica el endpoint GET /api/videos/{video_id}/detections."""
        res = self.client.get(f"/api/videos/{self.video_id}/detections")
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data["status"], "success")
        self.assertEqual(data["video_id"], self.video_id)
        self.assertGreater(data["annotated_frames_count"], 0)
        self.assertEqual(len(data["annotated_frames"]), data["annotated_frames_count"])


if __name__ == "__main__":
    unittest.main()
