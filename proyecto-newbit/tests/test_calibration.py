"""
Pruebas automatizadas de calibración dinámica de umbrales YOLOv8 (Sprint 2: HU11 / Paso D-07).
Verifica persistencia de umbrales, validación de rangos, bitácora de auditoría y renderizado web.
"""

import sys
import unittest
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from fastapi.testclient import TestClient
from app.main import app
from app import db


class TestCalibration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        db.init_db()
        cls.client = TestClient(app)
        db.reset_calibration_settings(changed_by="Test Setup")

    @classmethod
    def tearDownClass(cls):
        db.reset_calibration_settings(changed_by="Test TearDown")

    def test_01_get_calibration_defaults(self):
        """Verifica que la API retorne los umbrales predeterminados de fábrica."""
        response = self.client.get("/api/calibration")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "success")
        settings = data["settings"]
        self.assertAlmostEqual(settings["confidence"], 0.50, places=2)
        self.assertAlmostEqual(settings["iou"], 0.45, places=2)
        self.assertAlmostEqual(settings["target_fps"], 5.0, places=1)

    def test_02_update_calibration_valid(self):
        """Verifica el guardado y auditoría de nuevos umbrales dentro de rangos válidos."""
        payload = {
            "confidence": 0.65,
            "iou": 0.50,
            "target_fps": 8.0,
            "changed_by": "Mariana (SST)",
            "note": "Ajuste de prueba para nave de corte",
        }
        response = self.client.post("/api/calibration", json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "success")
        settings = data["settings"]
        self.assertAlmostEqual(settings["confidence"], 0.65, places=2)
        self.assertAlmostEqual(settings["iou"], 0.50, places=2)
        self.assertAlmostEqual(settings["target_fps"], 8.0, places=1)

        # Verificar que el log de auditoría registró el cambio
        res_history = self.client.get("/api/calibration/history")
        self.assertEqual(res_history.status_code, 200)
        history = res_history.json()["history"]
        self.assertGreaterEqual(len(history), 1)
        latest = history[0]
        self.assertEqual(latest["changed_by"], "Mariana (SST)")
        self.assertAlmostEqual(latest["confidence"], 0.65, places=2)

    def test_03_update_calibration_invalid_ranges(self):
        """Verifica el rechazo con HTTP 422 ante umbrales fuera de los límites físicos."""
        # Confianza > 0.95
        res1 = self.client.post("/api/calibration", json={"confidence": 1.2, "iou": 0.45, "target_fps": 5.0})
        self.assertEqual(res1.status_code, 422)

        # Confianza < 0.10
        res2 = self.client.post("/api/calibration", json={"confidence": 0.05, "iou": 0.45, "target_fps": 5.0})
        self.assertEqual(res2.status_code, 422)

        # IoU > 0.90
        res3 = self.client.post("/api/calibration", json={"confidence": 0.50, "iou": 0.98, "target_fps": 5.0})
        self.assertEqual(res3.status_code, 422)

        # FPS > 30.0
        res4 = self.client.post("/api/calibration", json={"confidence": 0.50, "iou": 0.45, "target_fps": 60.0})
        self.assertEqual(res4.status_code, 422)

    def test_04_reset_calibration(self):
        """Verifica la restauración a los valores predeterminados de fábrica."""
        # Primero cambiamos a un valor distinto
        self.client.post("/api/calibration", json={"confidence": 0.80, "iou": 0.60, "target_fps": 10.0})

        # Ejecutamos reset
        res_reset = self.client.post("/api/calibration/reset")
        self.assertEqual(res_reset.status_code, 200)
        data = res_reset.json()
        settings = data["settings"]
        self.assertAlmostEqual(settings["confidence"], 0.50, places=2)
        self.assertAlmostEqual(settings["iou"], 0.45, places=2)
        self.assertAlmostEqual(settings["target_fps"], 5.0, places=1)

    def test_05_web_calibration_page(self):
        """Verifica que la página HTML /calibration cargue los controles, sliders y script."""
        response = self.client.get("/calibration")
        self.assertEqual(response.status_code, 200)
        self.assertIn("slider-confidence", response.text)
        self.assertIn("slider-iou", response.text)
        self.assertIn("slider-fps", response.text)
        self.assertIn("calibration.js", response.text)
        self.assertIn("Bitácora de Auditoría", response.text)


if __name__ == "__main__":
    unittest.main()
