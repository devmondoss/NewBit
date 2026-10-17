"""
Pruebas automatizadas del visor HTML5 y extracción de frames (Sprint 1: HU02 / Paso D-04).
Verifica normalización de resolución a 640x640, streaming de video y renderizado de la ficha técnica.
"""

import sys
import unittest
import tempfile
import shutil
import numpy as np
import cv2
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from fastapi.testclient import TestClient
from app.main import app
from app import config, db
from ml.video_processor import extract_frames


def create_test_video(path: Path, width=320, height=240, fps=24, frames=24):
    """Crea un clip pequeño (1.0 s) con resolución no estándar (320x240) para verificar normalización."""
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(str(path), fourcc, fps, (width, height))
    for i in range(frames):
        frame = np.full((height, width, 3), (i * 10) % 255, dtype=np.uint8)
        cv2.putText(frame, f"F:{i}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        out.write(frame)
    out.release()


class TestVideoViewer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        db.init_db()
        cls.client = TestClient(app)
        cls.temp_dir = tempfile.TemporaryDirectory()
        cls.temp_path = Path(cls.temp_dir.name)

        # Generar video sintético
        cls.raw_video_path = cls.temp_path / "clip_planta.mp4"
        create_test_video(cls.raw_video_path, width=320, height=240, fps=24, frames=24)

        # Subir video para obtener video_id registrado
        with open(cls.raw_video_path, "rb") as f:
            res = cls.client.post("/api/videos/upload", files={"file": ("clip_planta.mp4", f, "video/mp4")})
        cls.video_data = res.json()["video"]
        cls.video_id = cls.video_data["id"]

    @classmethod
    def tearDownClass(cls):
        cls.temp_dir.cleanup()
        # Limpiar archivo en storage/uploads y storage/frames
        vid_record = db.get_video_by_id(cls.video_id)
        if vid_record and Path(vid_record["filepath"]).exists():
            try:
                Path(vid_record["filepath"]).unlink()
            except Exception:
                pass
        frames_dir = config.FRAMES_DIR / cls.video_id
        if frames_dir.exists():
            shutil.rmtree(frames_dir)
        db.delete_video_record(cls.video_id)

    def test_01_extract_frames_normalization(self):
        """Verifica que OpenCV extraiga y normalice todos los frames a 640x640."""
        target_dir = self.temp_path / "extracted_frames"
        frames = extract_frames(
            video_path=self.raw_video_path,
            output_dir=target_dir,
            target_size=(640, 640),
        )
        self.assertEqual(len(frames), 24)
        self.assertEqual(frames[0], "frame_000001.jpg")

        # Comprobar que la imagen guardada tenga dimensiones 640x640
        sample_img = cv2.imread(str(target_dir / frames[0]))
        self.assertEqual(sample_img.shape, (640, 640, 3))

    def test_02_api_extract_frames_endpoint(self):
        """Verifica el endpoint POST /api/videos/{video_id}/extract-frames."""
        response = self.client.post(f"/api/videos/{self.video_id}/extract-frames")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "success")
        self.assertEqual(data["total_frames_extracted"], 24)
        self.assertEqual(data["target_resolution"], "640x640")

        # Verificar que el estado del video en base de datos se actualizó
        updated_video = db.get_video_by_id(self.video_id)
        self.assertEqual(updated_video["status"], "frames_extracted")

    def test_03_api_stream_video(self):
        """Verifica que el endpoint de streaming entregue el video con media_type video/mp4."""
        response = self.client.get(f"/api/videos/{self.video_id}/stream")
        self.assertEqual(response.status_code, 200)
        self.assertIn("video/mp4", response.headers["content-type"])

    def test_04_api_get_frame_image(self):
        """Verifica que se pueda consultar la imagen JPEG de un fotograma extraído."""
        response = self.client.get(f"/api/videos/{self.video_id}/frames/frame_000001.jpg")
        self.assertEqual(response.status_code, 200)
        self.assertIn("image/jpeg", response.headers["content-type"])

    def test_05_web_video_detail_page(self):
        """Verifica que la vista HTML /videos/{video_id} renderice la ficha técnica y reproductor."""
        response = self.client.get(f"/videos/{self.video_id}")
        self.assertEqual(response.status_code, 200)
        self.assertIn("clip_planta.mp4", response.text)
        self.assertIn("Ficha Técnica", response.text)
        self.assertIn("video-player", response.text)
        self.assertIn("640 × 640 px", response.text)


if __name__ == "__main__":
    unittest.main()
