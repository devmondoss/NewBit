"""
Servidor web principal de NewBit (PY-NB-001).
Capa FastAPI + Jinja2 + Tailwind para gestión de video y visualización de actos inseguros.
"""

from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
import torch

from app import config

app = FastAPI(
    title=f"{config.PROJECT_NAME} ({config.PROJECT_CODE})",
    description="Sistema web con Visión Artificial para la detección de actos inseguros en áreas operativas de manufactura metalmecánica",
    version=config.APP_VERSION,
)

# Montaje de archivos estáticos
app.mount("/static", StaticFiles(directory=str(config.STATIC_DIR)), name="static")

# Configuración del motor de plantillas Jinja2
templates = Jinja2Templates(directory=str(config.TEMPLATES_DIR))


@app.get("/api/health")
async def health_check():
    """Endpoint de comprobación de salud técnica del servidor."""
    cuda_available = torch.cuda.is_available()
    device = torch.cuda.get_device_name(0) if cuda_available else "CPU (Standard)"
    return {
        "status": "ok",
        "app": config.PROJECT_NAME,
        "code": config.PROJECT_CODE,
        "version": config.APP_VERSION,
        "academic_context": config.ACADEMIC_CONTEXT,
        "domain": config.DOMAIN_CONTEXT,
        "device": device,
        "weights_present": config.YOLO_MODEL_PATH.exists(),
    }


@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    """Página principal / Dashboard de NewBit."""
    # En D-02 suministramos estadísticas base; en D-05 se dinamizan con la base de datos/almacenamiento
    stats = {
        "total_videos": len(list(config.UPLOADS_DIR.glob("*.*"))),
        "total_frames": len(list(config.FRAMES_DIR.glob("*/*.*"))),
        "avg_reduction": 0.0,
        "confidence": config.DEFAULT_YOLO_CONFIDENCE,
        "iou": config.DEFAULT_YOLO_IOU,
    }
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"stats": stats}
    )


@app.get("/videos", response_class=HTMLResponse)
async def videos_catalog_placeholder(request: Request):
    """Ruta preliminar para el catálogo de videos (se completa en D-05)."""
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "stats": {
                "total_videos": len(list(config.UPLOADS_DIR.glob("*.*"))),
                "total_frames": len(list(config.FRAMES_DIR.glob("*/*.*"))),
                "avg_reduction": 0.0,
                "confidence": config.DEFAULT_YOLO_CONFIDENCE,
                "iou": config.DEFAULT_YOLO_IOU,
            }
        }
    )


@app.get("/calibration", response_class=HTMLResponse)
async def calibration_placeholder(request: Request):
    """Ruta preliminar para calibración de umbrales (se completa en D-07)."""
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "stats": {
                "total_videos": len(list(config.UPLOADS_DIR.glob("*.*"))),
                "total_frames": len(list(config.FRAMES_DIR.glob("*/*.*"))),
                "avg_reduction": 0.0,
                "confidence": config.DEFAULT_YOLO_CONFIDENCE,
                "iou": config.DEFAULT_YOLO_IOU,
            }
        }
    )

