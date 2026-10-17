"""
Pruebas automatizadas de la base del servidor web FastAPI (Paso D-02).
Verifica endpoints, renderizado de plantillas y estructura del monorepo.
"""

import sys
import unittest
from pathlib import Path

# Agregar directorio 'proyecto-newbit' al sys.path para importación limpia
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from fastapi.testclient import TestClient
from app.main import app
from app import config


class TestServerBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    def test_health_endpoint(self):
        """Verifica que el endpoint /api/health devuelva metadatos correctos."""
        response = self.client.get("/api/health")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["app"], "NewBit")
        self.assertEqual(data["code"], "PY-NB-001")
        self.assertIn("device", data)
        self.assertTrue(data["weights_present"])

    def test_index_dashboard(self):
        """Verifica que la página principal renderice el HTML con la identidad oficial."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("NewBit", response.text)
        self.assertIn("PY-NB-001", response.text)
        self.assertIn("Manufactura Metalmecánica", response.text)
        self.assertIn("YOLOv8", response.text)

    def test_storage_directories_exist(self):
        """Verifica que las rutas operativas de storage y pesos existan en disco."""
        self.assertTrue(config.UPLOADS_DIR.exists())
        self.assertTrue(config.FRAMES_DIR.exists())
        self.assertTrue(config.OUTPUTS_DIR.exists())
        self.assertTrue(config.WEIGHTS_DIR.exists())
        self.assertTrue(config.YOLO_MODEL_PATH.exists())


if __name__ == "__main__":
    unittest.main()
