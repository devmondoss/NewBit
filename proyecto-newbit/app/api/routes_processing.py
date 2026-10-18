"""
Rutas API para procesamiento espacial e inferencia con YOLOv8 (Sprint 2: HU05).
Ejecuta la detección de operarios, genera bounding boxes y sirve fotogramas anotados.
"""

from pathlib import Path
from typing import Optional
from fastapi import APIRouter, HTTPException, status, Query
from fastapi.responses import JSONResponse, FileResponse

from app import config, db
from ml.detector import YOLOv8Detector

router = APIRouter(prefix="/api/videos", tags=["Procesamiento e Inferencia"])


@router.post("/{video_id}/detect")
async def detect_workers_in_video(
    video_id: str,
    conf: Optional[float] = Query(None, ge=0.05, le=1.0, description="Umbral de confianza YOLOv8"),
    iou: Optional[float] = Query(None, ge=0.05, le=1.0, description="Umbral de IoU (NMS)"),
):
    """
    Ejecuta el filtrado espacial mediante YOLOv8n sobre los fotogramas del video (HU05).
    Detecta operarios (clase person), dibuja bounding boxes, persiste imágenes anotadas
    en storage/frames/{video_id}/annotated/ y actualiza las métricas en la base de datos.
    """
    video = db.get_video_by_id(video_id)
    if not video:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Video con ID '{video_id}' no encontrado en el sistema.",
        )

    frames_dir = config.FRAMES_DIR / video_id
    if not frames_dir.exists() or not any(frames_dir.glob("*.jpg")):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se encontraron fotogramas extraídos o submuestreados. Ejecute la extracción/submuestreo primero.",
        )

    # Actualizar estado a processing
    db.update_video_status(video_id, "processing")

    try:
        detector = YOLOv8Detector.get_instance()
        metrics = detector.process_video_frames(video_id=video_id, conf=conf, iou=iou)

        # Actualizar base de datos con las métricas de detección
        db.update_detection_metrics(
            video_id=video_id,
            active_frames=metrics["active_frames_count"],
            total_detections=metrics["total_detections_count"],
        )

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "status": "success",
                "message": (
                    f"Detección completada: {metrics['active_frames_count']} frames con operarios "
                    f"de {metrics['total_frames_analyzed']} analizados ({metrics['active_ratio_pct']}% activos)."
                ),
                "metrics": metrics,
            },
        )
    except Exception as e:
        db.update_video_status(video_id, "error")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Fallo durante la detección espacial con YOLOv8: {str(e)}",
        )


@router.get("/{video_id}/annotated-frames/{filename}")
async def get_annotated_frame(video_id: str, filename: str):
    """Sirve la imagen JPEG de un fotograma anotado con bounding boxes de operarios."""
    annotated_path = config.FRAMES_DIR / video_id / "annotated" / filename

    # Prevenir ataques de Path Traversal
    try:
        resolved = annotated_path.resolve()
        expected_dir = (config.FRAMES_DIR / video_id / "annotated").resolve()
        if not str(resolved).startswith(str(expected_dir)):
            raise HTTPException(status_code=400, detail="Ruta de archivo no autorizada.")
    except Exception:
        raise HTTPException(status_code=400, detail="Ruta de fotograma inválida.")

    if not resolved.exists() or not resolved.is_file():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"El fotograma anotado '{filename}' no existe.",
        )

    return FileResponse(path=str(resolved), media_type="image/jpeg")


@router.get("/{video_id}/detections")
async def get_video_detections_summary(video_id: str):
    """Obtiene el resumen de detecciones espaciales y lista de fotogramas anotados."""
    video = db.get_video_by_id(video_id)
    if not video:
        raise HTTPException(status_code=404, detail="Video no encontrado.")

    annotated_dir = config.FRAMES_DIR / video_id / "annotated"
    annotated_files = []
    if annotated_dir.exists():
        annotated_files = sorted([f.name for f in annotated_dir.glob("*.jpg") if f.is_file()])

    return {
        "status": "success",
        "video_id": video_id,
        "active_frames_count": video.get("active_frames_count", 0),
        "detected_workers_count": video.get("detected_workers_count", 0),
        "annotated_frames_count": len(annotated_files),
        "annotated_frames": annotated_files,
    }
