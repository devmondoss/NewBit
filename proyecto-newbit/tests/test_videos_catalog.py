"""
Pruebas automatizadas del catálogo de videos y gestión de estados (Sprint 1: HU03 / Paso D-05).
Verifica renderizado de la tabla de catálogo, zona dropzone y borrado seguro de recursos.
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


def create_test_video(path: Path, width=320, height=240, fps=24, frames=24):
    """Genera un archivo MP4 pequeño para validación."""
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(str(path), fourcc, fps, (width, height))
    for i in range(frames):
        frame = np.full((height, width, 3), (i * 10) % 255, dtype=np.uint8)
        out.write(frame)
    out.release()


class TestVideosCatalog(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        db.init_db()
        cls.client = TestClient(app)
        cls.temp_dir = tempfile.TemporaryDirectory()
        cls.temp_path = Path(cls.temp_dir.name)
        cls.sample_video = cls.temp_path / "catalog_clip.mp4"
        create_test_video(cls.sample_video, width=320, height=240, fps=24, frames=24)

    @classmethod
    def tearDownClass(cls):
        cls.temp_dir.cleanup()

    def test_01_catalog_page_renders(self):
        """Verifica que la ruta GET /videos devuelva HTTP 200 y contenga la dropzone y scripts."""
        response = self.client.get("/videos")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Catálogo de Videos", response.text)
        self.assertIn("dropzone", response.text)
        self.assertIn("upload.js", response.text)

    def test_02_upload_and_display_in_catalog(self):
        """Sube un video y verifica que aparezca listado en la tabla de /videos."""
        with open(self.sample_video, "rb") as f:
            res_upload = self.client.post(
                "/api/videos/upload",
                files={"file": ("catalog_clip.mp4", f, "video/mp4")},
            )
        self.assertEqual(res_upload.status_code, 201)
        video_data = res_upload.json()["video"]
        video_id = video_data["id"]

        # Consultar la tabla de catálogo
        response_catalog = self.client.get("/videos")
        self.assertEqual(response_catalog.status_code, 200)
        self.assertIn("catalog_clip.mp4", response_catalog.text)
        self.assertIn(video_id, response_catalog.text)
        self.assertIn("Pendiente", response_catalog.text)

        # Extraer frames para verificar cambio de estado
        res_extract = self.client.post(f"/api/videos/{video_id}/extract-frames")
        self.assertEqual(res_extract.status_code, 200)

        response_catalog_updated = self.client.get("/videos")
        self.assertIn("Frames Listos", response_catalog_updated.text)

        # Probar eliminación segura
        res_delete = self.client.delete(f"/api/videos/{video_id}")
        self.assertEqual(res_delete.status_code, 200)
        self.assertEqual(res_delete.json()["status"], "success")

        # Verificar que el registro ya no existe en SQLite
        self.assertIsNone(db.get_video_by_id(video_id))

        # Verificar que la carpeta de frames y archivo crudo se eliminaron
        raw_file = Path(video_data["filepath"])
        frames_dir = config.FRAMES_DIR / video_id
        self.assertFalse(raw_file.exists())
        self.assertFalse(frames_dir.exists())

    def test_03_delete_nonexistent_video(self):
        """Verifica que intentar eliminar un video inexistente retorne HTTP 404."""
        response = self.client.delete("/api/videos/nonexistent_id_999")
        self.assertEqual(response.status_code, 404)
        self.assertIn("no encontrado", response.json()["detail"])


if __name__ == "__main__":
    unittest.main()
