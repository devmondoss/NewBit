"""
Pruebas automatizadas del motor de submuestreo temporal inteligente (Sprint 2: HU04 / Paso D-06).
Verifica cálculo de zancadas (stride), reducción de frames con OpenCV y endpoints API de métricas.
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
from ml.sampler import calculate_sample_stride, extract_sampled_frames


def create_test_video(path: Path, width=640, height=480, fps=24, frames=48):
    """Genera video sintético de 2.0 segundos a 24 FPS (48 frames totales)."""
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(str(path), fourcc, fps, (width, height))
    for i in range(frames):
        frame = np.full((height, width, 3), (i * 5) % 255, dtype=np.uint8)
        out.write(frame)
    out.release()


class TestSampler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        db.init_db()
        cls.client = TestClient(app)
        cls.temp_dir = tempfile.TemporaryDirectory()
        cls.temp_path = Path(cls.temp_dir.name)

        cls.sample_video = cls.temp_path / "sampler_clip.mp4"
        create_test_video(cls.sample_video, width=640, height=480, fps=24, frames=48)

        # Cargar video en la API para obtener registro en SQLite
        with open(cls.sample_video, "rb") as f:
            res = cls.client.post("/api/videos/upload", files={"file": ("sampler_clip.mp4", f, "video/mp4")})
        cls.video_data = res.json()["video"]
        cls.video_id = cls.video_data["id"]

    @classmethod
    def tearDownClass(cls):
        cls.temp_dir.cleanup()
        # Eliminar archivo crudo y frames
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

    def test_01_calculate_stride_math(self):
        """Verifica el cálculo matemático de la zancada de muestreo."""
        # 24 FPS a 6 FPS -> stride = 4 (24/6)
        self.assertEqual(calculate_sample_stride(24.0, 6.0), 4)

        # 24 FPS a 5 FPS -> stride = 5 (round(4.8) = 5)
        self.assertEqual(calculate_sample_stride(24.0, 5.0), 5)

        # 30 FPS a 5 FPS -> stride = 6 (30/5 = 6)
        self.assertEqual(calculate_sample_stride(30.0, 5.0), 6)

        # 30 FPS a 10 FPS -> stride = 3 (30/10 = 3)
        self.assertEqual(calculate_sample_stride(30.0, 10.0), 3)

        # target_fps >= original_fps -> stride = 1 (sin saltos)
        self.assertEqual(calculate_sample_stride(24.0, 30.0), 1)

        # Valores límite
        self.assertEqual(calculate_sample_stride(24.0, 0), 1)

    def test_02_extract_sampled_frames_reduction(self):
        """Verifica que el submuestreo de 48 frames a 6 FPS extraiga exactamente 12 frames (75% reducción)."""
        target_dir = self.temp_path / "sampled_frames"
        result = extract_sampled_frames(
            video_path=self.sample_video,
            output_dir=target_dir,
            target_fps=6.0,
            target_size=(640, 640),
        )

        self.assertEqual(result["original_frames"], 48)
        self.assertEqual(result["sampled_frames"], 12)
        self.assertEqual(result["stride"], 4)
        self.assertEqual(result["reduction_pct"], 75.0)
        self.assertEqual(len(result["frame_filenames"]), 12)
        self.assertEqual(len(result["timestamps"]), 12)

        # Comprobar resolución del frame guardado
        first_frame = cv2.imread(str(target_dir / result["frame_filenames"][0]))
        self.assertEqual(first_frame.shape, (640, 640, 3))

    def test_03_api_sample_endpoint(self):
        """Verifica el endpoint POST /api/videos/{video_id}/sample."""
        response = self.client.post(f"/api/videos/{self.video_id}/sample?target_fps=6.0")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "success")
        metrics = data["metrics"]
        self.assertEqual(metrics["sampled_frames"], 12)
        self.assertEqual(metrics["reduction_pct"], 75.0)

        # Verificar que la base de datos se actualizó con los valores de reducción
        updated_vid = db.get_video_by_id(self.video_id)
        self.assertEqual(updated_vid["sampled_frames_count"], 12)
        self.assertEqual(updated_vid["target_fps"], 6.0)
        self.assertEqual(updated_vid["reduction_pct"], 75.0)

    def test_04_api_get_sampling_metrics(self):
        """Verifica la consulta de métricas en GET /api/videos/{video_id}/sampling-metrics."""
        response = self.client.get(f"/api/videos/{self.video_id}/sampling-metrics")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "success")
        self.assertEqual(data["sampled_frames_count"], 12)
        self.assertEqual(data["reduction_pct"], 75.0)

    def test_05_api_sample_invalid_fps(self):
        """Verifica el rechazo con HTTP 400 ante target_fps inválido."""
        response = self.client.post(f"/api/videos/{self.video_id}/sample?target_fps=-5.0")
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
