"""
Motor de submuestreo temporal inteligente para NewBit (PY-NB-001).
Implementa reducción de tasa de fotogramas (FPS) con OpenCV para optimización
de la carga computacional previo a la inferencia espacial con YOLOv8 (Sprint 2: HU04).
"""

import shutil
from pathlib import Path
from typing import Dict, Any, List, Tuple
import cv2

from app import config


def calculate_sample_stride(original_fps: float, target_fps: float = 5.0) -> int:
    """
    Calcula la zancada (stride) o salto de fotogramas necesario para reducir
    la tasa de cuadros original al valor objetivo.
    Garantiza un stride mínimo de 1.
    """
    if original_fps <= 0 or target_fps <= 0:
        return 1
    if target_fps >= original_fps:
        return 1
    return max(1, round(original_fps / target_fps))


def extract_sampled_frames(
    video_path: Path | str,
    output_dir: Path | str,
    target_fps: float = 5.0,
    target_size: Tuple[int, int] = (640, 640),
) -> Dict[str, Any]:
    """
    Extrae únicamente los fotogramas clave correspondientes a la tasa objetivo,
    los normaliza a target_size (640x640 px) y calcula las métricas de reducción
    computacional obtenidas.
    """
    path = Path(video_path)
    out_dir = Path(output_dir)

    if not path.exists():
        raise FileNotFoundError(f"Archivo de video no encontrado: {path}")

    # Limpiar carpeta de frames previa si existiese
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    cap = cv2.VideoCapture(str(path))
    if not cap.isOpened():
        raise ValueError(f"No se pudo decodificar el video: {path.name}")

    try:
        original_fps = float(cap.get(cv2.CAP_PROP_FPS))
        if original_fps <= 0:
            original_fps = 24.0  # Fallback estándar

        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        stride = calculate_sample_stride(original_fps, target_fps)

        frame_idx = 0
        saved_idx = 0
        frame_filenames: List[str] = []
        timestamps: List[float] = []

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Conservar solo los fotogramas que coincidan con la zancada
            if frame_idx % stride == 0:
                saved_idx += 1
                timestamp_sec = round(frame_idx / original_fps, 2)

                # Normalización espacial a 640x640
                if target_size:
                    frame_norm = cv2.resize(frame, target_size, interpolation=cv2.INTER_AREA)
                else:
                    frame_norm = frame

                filename = f"frame_{saved_idx:06d}.jpg"
                dest_file = out_dir / filename
                cv2.imwrite(str(dest_file), frame_norm, [cv2.IMWRITE_JPEG_QUALITY, 95])

                frame_filenames.append(filename)
                timestamps.append(timestamp_sec)

            frame_idx += 1

        actual_total = frame_idx if frame_idx > 0 else total_frames
        reduction_pct = (
            round((1.0 - (saved_idx / actual_total)) * 100, 2)
            if actual_total > 0
            else 0.0
        )

        effective_fps = round(saved_idx / (actual_total / original_fps), 2) if actual_total > 0 else target_fps

        return {
            "original_frames": actual_total,
            "sampled_frames": saved_idx,
            "original_fps": round(original_fps, 2),
            "target_fps": target_fps,
            "effective_fps": effective_fps,
            "stride": stride,
            "reduction_pct": max(0.0, reduction_pct),
            "frame_filenames": frame_filenames,
            "timestamps": timestamps,
        }
    finally:
        cap.release()
