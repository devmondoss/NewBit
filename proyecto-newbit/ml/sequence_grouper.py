"""
Módulo de agrupamiento temporal de secuencias y renderizado de video para NewBit (PY-NB-001).
Implementa HU05 (agrupamiento de frames activos) y HU06 (descarte de acciones fugaces < 1.0s),
generando el clip final condensado en storage/outputs/{video_id}_processed.mp4.
"""

import re
import cv2
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional
import numpy as np

from app import config, db


def extract_frame_number(filename: str) -> int:
    """Extrae el índice numérico secuencial del nombre del fotograma (e.g., 'frame_000015.jpg' -> 15)."""
    match = re.search(r"\d+", filename)
    return int(match.group()) if match else 0


def group_active_sequences(
    active_frame_filenames: List[str],
    fps: float = 5.0,
    min_duration_sec: float = 1.0,
    max_gap_frames: int = 1,
) -> Tuple[List[List[str]], List[List[str]]]:
    """
    Agrupa los fotogramas activos con presencia de operarios en secuencias temporales continuas (HU05).
    Descarta aquellas secuencias cuya duración acumulada sea menor a min_duration_sec (HU06).

    Retorna:
        Tuple: (accepted_sequences, discarded_transient_sequences)
    """
    if not active_frame_filenames:
        return [], []

    # 1. Ordenar fotogramas por su índice numérico
    sorted_frames = sorted(active_frame_filenames, key=extract_frame_number)

    # 2. Agrupamiento en bloques contiguos (permitiendo una tolerancia de max_gap_frames)
    raw_sequences: List[List[str]] = []
    current_seq: List[str] = [sorted_frames[0]]

    for i in range(1, len(sorted_frames)):
        prev_idx = extract_frame_number(current_seq[-1])
        curr_idx = extract_frame_number(sorted_frames[i])

        if curr_idx - prev_idx <= (max_gap_frames + 1):
            current_seq.append(sorted_frames[i])
        else:
            raw_sequences.append(current_seq)
            current_seq = [sorted_frames[i]]

    if current_seq:
        raw_sequences.append(current_seq)

    # 3. Filtrado por ventana temporal mínima (HU06: descarte de falsos positivos o movimientos fugaces)
    # A 5 FPS, 1.0 segundo equivale a un mínimo de 5 fotogramas
    min_frames_required = max(1, int(round(fps * min_duration_sec)))

    accepted_sequences: List[List[str]] = []
    discarded_sequences: List[List[str]] = []

    for seq in raw_sequences:
        if len(seq) >= min_frames_required:
            accepted_sequences.append(seq)
        else:
            discarded_sequences.append(seq)

    return accepted_sequences, discarded_sequences


def render_processed_video(
    video_id: str,
    selected_frames: List[str],
    fps: float = 5.0,
    target_size: Tuple[int, int] = (640, 640),
) -> Dict[str, Any]:
    """
    Ensambla los fotogramas anotados seleccionados en un archivo de video final MP4
    utilizando OpenCV y lo persiste en storage/outputs/{video_id}_processed.mp4.
    """
    config.OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
    out_filename = f"{video_id}_processed.mp4"
    out_path = config.OUTPUTS_DIR / out_filename

    frames_dir = config.FRAMES_DIR / video_id
    annotated_dir = frames_dir / "annotated"

    # Preferir frames anotados con bounding boxes, con fallback a frames crudos
    base_dir = annotated_dir if annotated_dir.exists() else frames_dir

    if not selected_frames:
        raise ValueError("No se proporcionaron fotogramas para ensamblar el video procesado.")

    width, height = target_size
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(str(out_path), fourcc, fps, (width, height))

    if not writer.isOpened():
        raise RuntimeError(f"No se pudo inicializar el codificador de video OpenCV para {out_path}.")

    frames_written = 0
    for frame_name in selected_frames:
        frame_file = base_dir / frame_name
        if not frame_file.exists():
            continue

        img = cv2.imread(str(frame_file))
        if img is None:
            continue

        if (img.shape[1], img.shape[0]) != (width, height):
            img = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)

        writer.write(img)
        frames_written += 1

    writer.release()

    if frames_written == 0:
        if out_path.exists():
            out_path.unlink()
        raise RuntimeError("No se pudo escribir ningún fotograma válido en el video de salida.")

    processed_duration_sec = round(frames_written / fps, 2)
    file_size_mb = round(out_path.stat().st_size / (1024 * 1024), 3)

    return {
        "video_id": video_id,
        "output_filename": out_filename,
        "output_filepath": str(out_path),
        "processed_frame_count": frames_written,
        "processed_duration_sec": processed_duration_sec,
        "fps": fps,
        "file_size_mb": file_size_mb,
        "width": width,
        "height": height,
    }


def execute_sequence_pipeline(
    video_id: str,
    fps: Optional[float] = None,
    min_duration_sec: float = 1.0,
) -> Dict[str, Any]:
    """
    Ejecuta el pipeline completo de agrupamiento temporal y síntesis de video (HU05 / HU06).
    Lee las detecciones del video, filtra secuencias y genera el MP4 en storage/outputs/.
    """
    video = db.get_video_by_id(video_id)
    if not video:
        raise ValueError(f"Video {video_id} no encontrado en la base de datos.")

    if fps is None:
        fps = video.get("target_fps") or config.DEFAULT_SAMPLE_FPS
        if fps <= 0:
            fps = config.DEFAULT_SAMPLE_FPS

    # Recuperar fotogramas anotados en storage/frames/{video_id}/annotated/
    frames_dir = config.FRAMES_DIR / video_id
    annotated_dir = frames_dir / "annotated"
    if not annotated_dir.exists():
        raise FileNotFoundError(
            f"No se encontraron fotogramas anotados para el video {video_id}. "
            "Ejecute la detección espacial (HU05) primero."
        )

    # Identificar cuáles frames tienen presencia de operarios
    detections_file = frames_dir / "detections.json"
    active_frames = None
    if detections_file.exists():
        try:
            import json
            with open(detections_file, "r", encoding="utf-8") as f:
                det_data = json.load(f)
                active_frames = det_data.get("active_frames")
        except Exception:
            active_frames = None

    if active_frames is None:
        from ml.detector import YOLOv8Detector
        detector = YOLOv8Detector.get_instance()
        det_metrics = detector.process_video_frames(video_id=video_id)
        active_frames = det_metrics["active_frames"]

    if not active_frames:
        db.update_processed_video_metrics(
            video_id=video_id,
            processed_path="",
            duration_sec=0.0,
            frame_count=0,
        )
        return {
            "video_id": video_id,
            "status": "empty_activity",
            "message": "No se detectó actividad de operarios en el video.",
            "total_sequences_found": 0,
            "accepted_sequences_count": 0,
            "discarded_sequences_count": 0,
            "processed_frame_count": 0,
            "processed_duration_sec": 0.0,
            "time_reduction_pct": 100.0,
        }

    # Agrupamiento y descarte de secuencias fugaces (HU05 / HU06)
    accepted_seqs, discarded_seqs = group_active_sequences(
        active_frame_filenames=active_frames,
        fps=fps,
        min_duration_sec=min_duration_sec,
    )

    if not accepted_seqs:
        db.update_processed_video_metrics(
            video_id=video_id,
            processed_path="",
            duration_sec=0.0,
            frame_count=0,
        )
        return {
            "video_id": video_id,
            "status": "transient_activity_discarded",
            "message": (
                f"Se detectaron {len(discarded_seqs)} secuencias activas pero todas fueron "
                f"descartadas por durar menos de {min_duration_sec}s (movimientos fugaces - HU06)."
            ),
            "total_sequences_found": len(discarded_seqs),
            "accepted_sequences_count": 0,
            "discarded_sequences_count": len(discarded_seqs),
            "processed_frame_count": 0,
            "processed_duration_sec": 0.0,
            "time_reduction_pct": 100.0,
        }


    # Aplanar los fotogramas seleccionados de todas las secuencias aceptadas
    consolidated_frames = [f for seq in accepted_seqs for f in seq]

    # Renderizar el video consolidado en storage/outputs/
    render_result = render_processed_video(
        video_id=video_id,
        selected_frames=consolidated_frames,
        fps=fps,
        target_size=config.TARGET_FRAME_SIZE,
    )

    # Calcular ahorro de tiempo muerto respecto al video original
    original_duration = video["duration_sec"]
    processed_duration = render_result["processed_duration_sec"]
    time_saved_sec = max(0.0, original_duration - processed_duration)
    time_reduction_pct = (
        round((time_saved_sec / original_duration) * 100, 2)
        if original_duration > 0
        else 0.0
    )

    # Actualizar métricas y estado en base de datos SQLite
    db.update_processed_video_metrics(
        video_id=video_id,
        processed_path=render_result["output_filepath"],
        duration_sec=processed_duration,
        frame_count=render_result["processed_frame_count"],
    )

    return {
        "video_id": video_id,
        "status": "completed",
        "output_filename": render_result["output_filename"],
        "output_filepath": render_result["output_filepath"],
        "total_sequences_found": len(accepted_seqs) + len(discarded_seqs),
        "accepted_sequences_count": len(accepted_seqs),
        "discarded_sequences_count": len(discarded_seqs),
        "processed_frame_count": render_result["processed_frame_count"],
        "processed_duration_sec": processed_duration,
        "original_duration_sec": original_duration,
        "time_reduction_pct": time_reduction_pct,
        "file_size_mb": render_result["file_size_mb"],
    }
