"""
Pruebas automatizadas del motor de agrupamiento temporal y síntesis de video (Sprint 2: HU06 / Paso D-09).
Verifica agrupamiento de secuencias continuas, descarte de acciones fugaces < 1.0s y renderizado MP4.
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
from ml.sequence_grouper import (
    extract_frame_number,
    group_active_sequences,
    render_processed_video,
)


def create_dummy_frame_file(path: Path, width: int = 640, height: int = 640, label: str = ""):
    """Crea una imagen JPEG sintética en la ruta especificada."""
    img = np.full((height, width, 3), 150, dtype=np.uint8)
    if label:
        cv2.putText(
            img, label, (40, 200), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2
        )
    cv2.imwrite(str(path), img)


class TestSequenceGrouper(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        db.init_db()
        cls.client = TestClient(app)
        cls.temp_dir = tempfile.TemporaryDirectory()
        cls.temp_path = Path(cls.temp_dir.name)

        # Generar video sintético de 24 FPS y 48 frames (2.0 segundos)
        cls.sample_video = cls.temp_path / "grouper_test_clip.mp4"
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        out = cv2.VideoWriter(str(cls.sample_video), fourcc, 24, (640, 480))
        for i in range(48):
            frame = np.full((480, 640, 3), (i * 5) % 255, dtype=np.uint8)
            out.write(frame)
        out.release()

        # Ingestar video en la API
        with open(cls.sample_video, "rb") as f:
            res = cls.client.post(
                "/api/videos/upload",
                files={"file": ("grouper_test_clip.mp4", f, "video/mp4")},
            )
        cls.video_data = res.json()["video"]
        cls.video_id = cls.video_data["id"]

        # Submuestrear a 5.0 FPS para tener fotogramas base
        cls.client.post(f"/api/videos/{cls.video_id}/sample?target_fps=5.0")

        # Asegurar existencia de carpeta annotated con fotogramas válidos
        annotated_dir = config.FRAMES_DIR / cls.video_id / "annotated"
        annotated_dir.mkdir(parents=True, exist_ok=True)
        for i in range(1, 11):
            frame_name = f"frame_{i:06d}.jpg"
            create_dummy_frame_file(annotated_dir / frame_name, label=f"Annotated {i}")

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
        processed_file = config.OUTPUTS_DIR / f"{cls.video_id}_processed.mp4"
        if processed_file.exists():
            try:
                processed_file.unlink()
            except Exception:
                pass
        db.delete_video_record(cls.video_id)

    def test_01_extract_frame_number(self):
        """Verifica la extracción numérica de nombres de archivo de fotogramas."""
        self.assertEqual(extract_frame_number("frame_000005.jpg"), 5)
        self.assertEqual(extract_frame_number("frame_000128.jpg"), 128)
        self.assertEqual(extract_frame_number("clip_42_annotated.jpg"), 42)
        self.assertEqual(extract_frame_number("no_numbers.jpg"), 0)

    def test_02_group_active_sequences_filter_transient(self):
        """
        Verifica que se agrupen secuencias continuas y se descarten movimientos fugaces < 1.0s (HU06).
        A 5 FPS, 1.0 segundo = 5 fotogramas mínimos requeridos.
        """
        # Secuencia 1: 7 fotogramas continuos (1.4s) -> ACEPTADA
        seq1 = [f"frame_{i:06d}.jpg" for i in range(1, 8)]
        # Secuencia 2: 2 fotogramas fugaces (0.4s) -> DESCARTADA (falso positivo)
        seq2 = ["frame_000020.jpg", "frame_000021.jpg"]
        # Secuencia 3: 5 fotogramas continuos (1.0s justo) -> ACEPTADA
        seq3 = [f"frame_{i:06d}.jpg" for i in range(35, 40)]

        all_active = seq1 + seq2 + seq3
        accepted, discarded = group_active_sequences(
            all_active, fps=5.0, min_duration_sec=1.0, max_gap_frames=1
        )

        self.assertEqual(len(accepted), 2)
        self.assertEqual(len(discarded), 1)
        self.assertEqual(accepted[0], seq1)
        self.assertEqual(accepted[1], seq3)
        self.assertEqual(discarded[0], seq2)

    def test_03_group_empty_input(self):
        """Verifica que entradas vacías retornen tuplas vacías con gracia."""
        accepted, discarded = group_active_sequences([])
        self.assertEqual(accepted, [])
        self.assertEqual(discarded, [])

    def test_04_render_processed_video_opencv(self):
        """Verifica que OpenCV ensamble el MP4 reproducible en storage/outputs/."""
        selected_frames = [f"frame_{i:06d}.jpg" for i in range(1, 8)]
        res = render_processed_video(
            video_id=self.video_id,
            selected_frames=selected_frames,
            fps=5.0,
            target_size=(640, 640),
        )

        out_path = Path(res["output_filepath"])
        self.assertTrue(out_path.exists())
        self.assertGreater(out_path.stat().st_size, 0)
        self.assertEqual(res["processed_frame_count"], 7)
        self.assertEqual(res["processed_duration_sec"], 1.4)

        # Verificar integridad del MP4 generado con VideoCapture
        cap = cv2.VideoCapture(str(out_path))
        self.assertTrue(cap.isOpened())
        ret, frame = cap.read()
        self.assertTrue(ret)
        self.assertEqual((frame.shape[1], frame.shape[0]), (640, 640))
        cap.release()

    def test_05_api_group_and_render_endpoint(self):
        """Verifica el endpoint POST /api/videos/{video_id}/group-and-render."""
        import json
        frames_dir = config.FRAMES_DIR / self.video_id
        annotated_dir = frames_dir / "annotated"
        annotated_dir.mkdir(parents=True, exist_ok=True)
        active_list = [f"frame_{i:06d}.jpg" for i in range(1, 9)]
        for f_name in active_list:
            create_dummy_frame_file(annotated_dir / f_name, label=f"Worker {f_name}")

        with open(frames_dir / "detections.json", "w", encoding="utf-8") as f:
            json.dump({
                "video_id": self.video_id,
                "active_frames": active_list,
                "inactive_frames": [],
                "total_detections_count": 8,
            }, f)

        response = self.client.post(
            f"/api/videos/{self.video_id}/group-and-render?min_duration=0.5"
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "success")
        self.assertIn("result", data)
        self.assertEqual(data["result"]["status"], "completed")

        # Verificar que SQLite tenga el video en 'completed'
        video = db.get_video_by_id(self.video_id)
        self.assertEqual(video["status"], "completed")
        self.assertIsNotNone(video["processed_video_path"])
        self.assertGreater(video["processed_frame_count"], 0)


    def test_06_api_stream_processed_video(self):
        """Verifica que el endpoint GET /api/videos/{video_id}/processed-stream sirva el MP4."""
        response = self.client.get(f"/api/videos/{self.video_id}/processed-stream")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["content-type"], "video/mp4")

    def test_07_api_stream_nonexistent_processed_video(self):
        """Verifica HTTP 404 al solicitar streaming de un video procesado inexistente."""
        response = self.client.get("/api/videos/non_existent_id/processed-stream")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
