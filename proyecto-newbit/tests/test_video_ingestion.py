"""
Pruebas automatizadas de ingesta y validación de video (Sprint 1: HU01 / Paso D-03).
Verifica validación de formato, extracción de metadatos con OpenCV y endpoints API.
"""

import sys
import unittest
import tempfile
import numpy as np
import cv2
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from fastapi.testclient import TestClient
from app.main import app
from app import config, db
from ml.video_processor import validate_video_file, get_video_metadata


def create_synthetic_video(output_path: Path, width=640, height=480, fps=24, total_frames=48):
    """Genera un archivo de video sintético real con OpenCV para pruebas (duración = 2.0 s)."""
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(str(output_path), fourcc, fps, (width, height))
    for i in range(total_frames):
        # Crear frame con gradiente de color para simular movimiento
        frame = np.full((height, width, 3), (i * 5) % 255, dtype=np.uint8)
        # Dibujar una figura geométrica de prueba
        cv2.circle(frame, (width // 2, height // 2), 50, (0, 255, 0), -1)
        out.write(frame)
    out.release()


class TestVideoIngestion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        db.init_db()
        cls.client = TestClient(app)
        cls.temp_dir = tempfile.TemporaryDirectory()
        cls.temp_path = Path(cls.temp_dir.name)
        cls.test_video_path = cls.temp_path / "test_clip.mp4"
        create_synthetic_video(cls.test_video_path, width=640, height=480, fps=24, total_frames=48)
        cls.created_video_ids = []

    @classmethod
    def tearDownClass(cls):
        cls.temp_dir.cleanup()
        # Limpiar videos subidos durante las pruebas
        for vid_id in cls.created_video_ids:
            record = db.get_video_by_id(vid_id)
            if record and Path(record["filepath"]).exists():
                try:
                    Path(record["filepath"]).unlink()
                except Exception:
                    pass
            db.delete_video_record(vid_id)

    def test_01_format_validation(self):
        """Valida que solo se acepten extensiones .mp4 y .avi."""
        # Extensiones válidas (no deben lanzar excepción)
        validate_video_file("camara1.mp4", 1024)
        validate_video_file("nave_central.avi", 2048)

        # Extensiones inválidas (deben lanzar ValueError)
        with self.assertRaises(ValueError):
            validate_video_file("archivo.txt", 100)
        with self.assertRaises(ValueError):
            validate_video_file("payload.exe", 100)

    def test_02_size_validation(self):
        """Valida que no se permitan archivos que superen los 100 MB."""
        # 10 MB permitido
        validate_video_file("video.mp4", 10 * 1024 * 1024)

        # 101 MB prohibido
        with self.assertRaises(ValueError):
            validate_video_file("video_pesado.mp4", 101 * 1024 * 1024)

    def test_03_opencv_metadata_extraction(self):
        """Verifica que OpenCV extraiga duración, FPS, resolución y conteo exacto de frames."""
        metadata = get_video_metadata(self.test_video_path)
        self.assertEqual(metadata["width"], 640)
        self.assertEqual(metadata["height"], 480)
        self.assertEqual(metadata["fps"], 24.0)
        self.assertEqual(metadata["frame_count"], 48)
        self.assertEqual(metadata["duration_sec"], 2.0)
        self.assertGreater(metadata["file_size_mb"], 0.0)

    def test_04_api_upload_valid_video(self):
        """Verifica el endpoint POST /api/videos/upload con un archivo de video real."""
        with open(self.test_video_path, "rb") as f:
            response = self.client.post(
                "/api/videos/upload",
                files={"file": ("test_clip.mp4", f, "video/mp4")},
            )

        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertEqual(data["status"], "success")
        video = data["video"]
        self.assertEqual(video["original_name"], "test_clip.mp4")
        self.assertEqual(video["duration_sec"], 2.0)
        self.assertEqual(video["fps"], 24.0)
        self.assertEqual(video["frame_count"], 48)
        self.assertEqual(video["width"], 640)
        self.assertEqual(video["height"], 480)
        self.assertEqual(video["status"], "uploaded")

        self.created_video_ids.append(video["id"])

    def test_05_api_upload_invalid_extension(self):
        """Verifica que el endpoint rechace extensiones no admitidas con HTTP 400."""
        response = self.client.post(
            "/api/videos/upload",
            files={"file": ("informe.pdf", b"fake-pdf-content", "application/pdf")},
        )
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertIn("Formato no permitido", data["detail"])

    def test_06_api_list_and_get_video(self):
        """Verifica la consulta de catálogo en GET /api/videos y GET /api/videos/{id}."""
        # Listado general
        response_list = self.client.get("/api/videos")
        self.assertEqual(response_list.status_code, 200)
        data_list = response_list.json()
        self.assertGreaterEqual(data_list["count"], 1)

        # Consulta individual
        vid_id = self.created_video_ids[0]
        response_get = self.client.get(f"/api/videos/{vid_id}")
        self.assertEqual(response_get.status_code, 200)
        data_get = response_get.json()
        self.assertEqual(data_get["video"]["id"], vid_id)


if __name__ == "__main__":
    unittest.main()
