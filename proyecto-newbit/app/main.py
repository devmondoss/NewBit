"""
Servidor web principal de NewBit (PY-NB-001).
Capa FastAPI + Jinja2 + Tailwind para gestión de video y visualización de actos inseguros.
"""

from pathlib import Path
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
import torch

from app import config, db
from app.api import routes_videos


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Inicializar base de datos SQLite y directorios al arranque
    db.init_db()
    yield


app = FastAPI(
    title=f"{config.PROJECT_NAME} ({config.PROJECT_CODE})",
    description="Sistema web con Visión Artificial para la detección de actos inseguros en áreas operativas de manufactura metalmecánica",
    version=config.APP_VERSION,
    lifespan=lifespan,
)

# Montaje de archivos estáticos
app.mount("/static", StaticFiles(directory=str(config.STATIC_DIR)), name="static")

# Configuración del motor de plantillas Jinja2
templates = Jinja2Templates(directory=str(config.TEMPLATES_DIR))

# Inclusión de enrutadores API
app.include_router(routes_videos.router)


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
    """Página principal / Dashboard de NewBit con estadísticas dinámicas."""
    videos = db.get_all_videos()
    total_frames = sum(v["frame_count"] for v in videos)
    sampled_videos = [v for v in videos if v.get("reduction_pct", 0) > 0]
    avg_reduction = (
        round(sum(v["reduction_pct"] for v in sampled_videos) / len(sampled_videos), 1)
        if sampled_videos
        else 0.0
    )
    stats = {
        "total_videos": len(videos),
        "total_frames": total_frames,
        "avg_reduction": avg_reduction,
        "confidence": config.DEFAULT_YOLO_CONFIDENCE,
        "iou": config.DEFAULT_YOLO_IOU,
    }
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"stats": stats}
    )



@app.get("/videos", response_class=HTMLResponse)
async def videos_catalog_view(request: Request):
    """Catálogo web interactivo de videos con dropzone y tabla de estados (HU01 - HU03)."""
    videos = db.get_all_videos()
    total_frames = sum(v["frame_count"] for v in videos)
    sampled_videos = [v for v in videos if v.get("reduction_pct", 0) > 0]
    avg_reduction = (
        round(sum(v["reduction_pct"] for v in sampled_videos) / len(sampled_videos), 1)
        if sampled_videos
        else 0.0
    )
    stats = {
        "total_videos": len(videos),
        "total_frames": total_frames,
        "avg_reduction": avg_reduction,
        "confidence": config.DEFAULT_YOLO_CONFIDENCE,
        "iou": config.DEFAULT_YOLO_IOU,
    }
    return templates.TemplateResponse(
        request=request,
        name="videos_catalog.html",
        context={"videos": videos, "stats": stats}
    )




@app.get("/videos/{video_id}", response_class=HTMLResponse)
async def video_detail_view(request: Request, video_id: str):
    """Visor web HTML5 con ficha técnica de metadatos y visor de fotogramas (HU02)."""
    video = db.get_video_by_id(video_id)
    if not video:
        return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={
                "stats": {
                    "total_videos": 0,
                    "total_frames": 0,
                    "avg_reduction": 0.0,
                    "confidence": config.DEFAULT_YOLO_CONFIDENCE,
                    "iou": config.DEFAULT_YOLO_IOU,
                }
            },
            status_code=404
        )

    frames_dir = config.FRAMES_DIR / video_id
    frames = sorted([f.name for f in frames_dir.glob("*.jpg")]) if frames_dir.exists() else []

    return templates.TemplateResponse(
        request=request,
        name="video_detail.html",
        context={"video": video, "frames": frames}
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

