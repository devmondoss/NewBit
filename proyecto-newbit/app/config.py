"""
Configuración centralizada de NewBit (PY-NB-001).
Define rutas del monorepo, parámetros de almacenamiento y umbrales por defecto.
"""

from pathlib import Path

# Rutas base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent
APP_DIR = BASE_DIR / "app"
TEMPLATES_DIR = APP_DIR / "templates"
STATIC_DIR = APP_DIR / "static"

# Capa de Machine Learning y pesos
ML_DIR = BASE_DIR / "ml"
WEIGHTS_DIR = ML_DIR / "weights"
YOLO_MODEL_PATH = WEIGHTS_DIR / "yolov8n.pt"

# Almacenamiento local de medios
STORAGE_DIR = BASE_DIR / "storage"
UPLOADS_DIR = STORAGE_DIR / "uploads"
FRAMES_DIR = STORAGE_DIR / "frames"
OUTPUTS_DIR = STORAGE_DIR / "outputs"

# Asegurar existencia de directorios operativos
for directory in [UPLOADS_DIR, FRAMES_DIR, OUTPUTS_DIR, WEIGHTS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# Parámetros de ingesta y validación (HU01)
ALLOWED_EXTENSIONS = {".mp4", ".avi"}
MAX_UPLOAD_SIZE_MB = 100
MAX_UPLOAD_BYTES = MAX_UPLOAD_SIZE_MB * 1024 * 1024

# Parámetros de detección y calibración (HU03, HU11)
DEFAULT_YOLO_CONFIDENCE = 0.50
DEFAULT_YOLO_IOU = 0.45
TARGET_FRAME_SIZE = (640, 640)

# Parámetros de muestreo y filtrado temporal (HU04, HU06)
DEFAULT_SAMPLE_FPS = 5
MIN_ACTION_DURATION_SEC = 1.0

# Metadatos del proyecto
PROJECT_CODE = "PY-NB-001"
PROJECT_NAME = "NewBit"
APP_VERSION = "1.0.0-mvp"
ACADEMIC_CONTEXT = "Ingeniería de Software II (UNS) - Grupo D3"
DOMAIN_CONTEXT = "Taller de manufactura metalmecánica / Dataset Kafaoğlu"
