"""
Rutas API para calibración dinámica de umbrales YOLOv8 y muestreo (Sprint 2: HU11).
Permite ajustar en caliente confianza, IoU y FPS sin alterar código ni reiniciar el servidor.
"""

from typing import Optional
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

from app import db

router = APIRouter(prefix="/api/calibration", tags=["Calibración"])


class CalibrationUpdate(BaseModel):
    confidence: float = Field(
        ...,
        ge=0.10,
        le=0.95,
        description="Umbral de confianza mínima de detección para YOLOv8 (0.10 a 0.95)",
    )
    iou: float = Field(
        ...,
        ge=0.10,
        le=0.90,
        description="Umbral IoU de Supresión de No Máximos (NMS) (0.10 a 0.90)",
    )
    target_fps: float = Field(
        5.0,
        ge=1.0,
        le=30.0,
        description="Tasa de fotogramas objetivo para submuestreo temporal (1.0 a 30.0 FPS)",
    )
    changed_by: Optional[str] = Field("Jorge (TI)", description="Usuario o rol que aplica el cambio")
    note: Optional[str] = Field("Ajuste de parámetros en planta", description="Motivo técnico del ajuste")


@router.get("")
async def get_calibration():
    """Consulta la configuración actual de calibración del detector."""
    settings = db.get_calibration_settings()
    return {
        "status": "success",
        "settings": settings,
    }


@router.post("")
async def update_calibration(payload: CalibrationUpdate):
    """
    Aplica y persiste nuevos parámetros de calibración para YOLOv8 y muestreo.
    Valida límites numéricos y almacena el evento en la bitácora de auditoría.
    """
    try:
        updated = db.save_calibration_settings(
            confidence=payload.confidence,
            iou=payload.iou,
            target_fps=payload.target_fps,
            changed_by=payload.changed_by or "Jorge (TI)",
            note=payload.note or "Calibración manual de planta",
        )
        return {
            "status": "success",
            "message": "Parámetros de calibración actualizados y persistidos con éxito.",
            "settings": updated,
        }
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/reset")
async def reset_calibration(changed_by: str = "Jorge (TI)"):
    """Restaura los valores de fábrica predeterminados (Confidence 0.50, IoU 0.45, 5.0 FPS)."""
    defaults = db.reset_calibration_settings(changed_by=changed_by)
    return {
        "status": "success",
        "message": "Calibración restablecida a los valores predeterminados de fábrica.",
        "settings": defaults,
    }


@router.get("/history")
async def get_calibration_history(limit: int = 15):
    """Consulta el historial de auditoría de calibraciones realizadas."""
    history = db.get_calibration_audit_logs(limit=limit)
    return {
        "status": "success",
        "count": len(history),
        "history": history,
    }
