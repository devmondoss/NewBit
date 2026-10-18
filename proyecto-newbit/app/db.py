"""
Capa de persistencia ligera con SQLite para NewBit (PY-NB-001).
Gestiona el catálogo de videos, metadatos técnicos y estados de procesamiento.
"""

import sqlite3
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Dict, Any
from app import config

DB_PATH = config.STORAGE_DIR / "newbit.db"


def get_connection() -> sqlite3.Connection:
    """Crea una conexión con la base de datos SQLite con soporte para diccionarios."""
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    """Inicializa la estructura de tablas del catálogo de videos si no existen."""
    config.STORAGE_DIR.mkdir(parents=True, exist_ok=True)
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS videos (
                id TEXT PRIMARY KEY,
                filename TEXT NOT NULL,
                original_name TEXT NOT NULL,
                filepath TEXT NOT NULL,
                file_size_mb REAL NOT NULL,
                duration_sec REAL NOT NULL,
                fps REAL NOT NULL,
                frame_count INTEGER NOT NULL,
                width INTEGER NOT NULL,
                height INTEGER NOT NULL,
                codec TEXT,
                status TEXT NOT NULL DEFAULT 'uploaded',
                sampled_frames_count INTEGER DEFAULT 0,
                target_fps REAL DEFAULT 0.0,
                reduction_pct REAL DEFAULT 0.0,
                detected_workers_count INTEGER DEFAULT 0,
                active_frames_count INTEGER DEFAULT 0,
                processed_video_path TEXT,
                processed_duration_sec REAL DEFAULT 0.0,
                processed_frame_count INTEGER DEFAULT 0,
                created_at TEXT NOT NULL
            )
            """
        )

        # Migración segura de columnas si la tabla ya existía
        cursor.execute("PRAGMA table_info(videos)")
        existing_cols = {row["name"] for row in cursor.fetchall()}
        if "sampled_frames_count" not in existing_cols:
            cursor.execute("ALTER TABLE videos ADD COLUMN sampled_frames_count INTEGER DEFAULT 0")
        if "target_fps" not in existing_cols:
            cursor.execute("ALTER TABLE videos ADD COLUMN target_fps REAL DEFAULT 0.0")
        if "reduction_pct" not in existing_cols:
            cursor.execute("ALTER TABLE videos ADD COLUMN reduction_pct REAL DEFAULT 0.0")
        if "detected_workers_count" not in existing_cols:
            cursor.execute("ALTER TABLE videos ADD COLUMN detected_workers_count INTEGER DEFAULT 0")
        if "active_frames_count" not in existing_cols:
            cursor.execute("ALTER TABLE videos ADD COLUMN active_frames_count INTEGER DEFAULT 0")
        if "processed_video_path" not in existing_cols:
            cursor.execute("ALTER TABLE videos ADD COLUMN processed_video_path TEXT")
        if "processed_duration_sec" not in existing_cols:
            cursor.execute("ALTER TABLE videos ADD COLUMN processed_duration_sec REAL DEFAULT 0.0")
        if "processed_frame_count" not in existing_cols:
            cursor.execute("ALTER TABLE videos ADD COLUMN processed_frame_count INTEGER DEFAULT 0")



        # Tabla de configuración del sistema (HU11)
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS settings (
                key TEXT PRIMARY KEY,
                value TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
            """
        )

        # Tabla de auditoría de calibración (HU11)
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS calibration_audit (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                confidence REAL NOT NULL,
                iou REAL NOT NULL,
                target_fps REAL NOT NULL,
                changed_by TEXT NOT NULL,
                created_at TEXT NOT NULL,
                note TEXT
            )
            """
        )

        conn.commit()




def save_video_record(record: Dict[str, Any]) -> Dict[str, Any]:
    """Inserta o actualiza un registro de video en la base de datos."""
    if "created_at" not in record:
        record["created_at"] = datetime.now().isoformat()

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO videos (
                id, filename, original_name, filepath, file_size_mb,
                duration_sec, fps, frame_count, width, height, codec, status, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                status = excluded.status,
                duration_sec = excluded.duration_sec,
                fps = excluded.fps,
                frame_count = excluded.frame_count
            """,
            (
                record["id"],
                record["filename"],
                record["original_name"],
                record["filepath"],
                record["file_size_mb"],
                record["duration_sec"],
                record["fps"],
                record["frame_count"],
                record["width"],
                record["height"],
                record.get("codec", "unknown"),
                record.get("status", "uploaded"),
                record["created_at"],
            ),
        )
        conn.commit()
    return record


def get_video_by_id(video_id: str) -> Optional[Dict[str, Any]]:
    """Recupera la ficha técnica y estado de un video por su identificador único."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM videos WHERE id = ?", (video_id,))
        row = cursor.fetchone()
        return dict(row) if row else None


def get_all_videos() -> List[Dict[str, Any]]:
    """Obtiene la lista completa de videos registrados ordenados por fecha descendente."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM videos ORDER BY created_at DESC")
        rows = cursor.fetchall()
        return [dict(r) for r in rows]


def update_video_status(video_id: str, status: str) -> bool:
    """Actualiza el estado de procesamiento del video ('uploaded', 'processing', 'completed', 'error')."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE videos SET status = ? WHERE id = ?", (status, video_id))
        conn.commit()
        return cursor.rowcount > 0


def delete_video_record(video_id: str) -> bool:
    """Elimina el registro de un video en el catálogo."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
        conn.commit()
        return cursor.rowcount > 0


def update_sampling_metrics(
    video_id: str, sampled_count: int, target_fps: float, reduction_pct: float
) -> bool:
    """Actualiza las métricas de submuestreo y tasa de reducción en la base de datos."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE videos
            SET sampled_frames_count = ?,
                target_fps = ?,
                reduction_pct = ?,
                status = 'frames_extracted'
            WHERE id = ?
            """,
            (sampled_count, target_fps, reduction_pct, video_id),
        )
        conn.commit()
        return cursor.rowcount > 0


def update_detection_metrics(
    video_id: str, active_frames: int, total_detections: int
) -> bool:
    """Actualiza las métricas de detección de operarios y frames activos (HU05)."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE videos
            SET active_frames_count = ?,
                detected_workers_count = ?,
                status = 'detected'
            WHERE id = ?
            """,
            (active_frames, total_detections, video_id),
        )
        conn.commit()
        return cursor.rowcount > 0


def update_processed_video_metrics(
    video_id: str,
    processed_path: str,
    duration_sec: float,
    frame_count: int,
) -> bool:
    """Actualiza el video procesado y su estado final a 'completed' (HU06)."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE videos
            SET processed_video_path = ?,
                processed_duration_sec = ?,
                processed_frame_count = ?,
                status = 'completed'
            WHERE id = ?
            """,
            (processed_path, duration_sec, frame_count, video_id),
        )
        conn.commit()
        return cursor.rowcount > 0




# =========================================================================
# FUNCIONES DE CALIBRACIÓN DINÁMICA DE DETECTOR Y SISTEMA (HU11)
# =========================================================================

def get_calibration_settings() -> Dict[str, Any]:
    """Recupera la configuración activa de calibración o inicializa valores de fábrica."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT key, value, updated_at FROM settings WHERE key IN ('confidence', 'iou', 'target_fps')")
        rows = cursor.fetchall()
        settings_map = {row["key"]: row["value"] for row in rows}

    now_iso = datetime.now().isoformat()
    confidence = float(settings_map.get("confidence", config.DEFAULT_YOLO_CONFIDENCE))
    iou = float(settings_map.get("iou", config.DEFAULT_YOLO_IOU))
    target_fps = float(settings_map.get("target_fps", config.DEFAULT_SAMPLE_FPS))
    updated_at = settings_map.get("updated_at", now_iso)

    return {
        "confidence": confidence,
        "iou": iou,
        "target_fps": target_fps,
        "updated_at": updated_at,
    }


def save_calibration_settings(
    confidence: float,
    iou: float,
    target_fps: float = 5.0,
    changed_by: str = "Jorge (TI)",
    note: str = "Ajuste de parámetros de detección en planta",
) -> Dict[str, Any]:
    """Valida, persiste y registra en auditoría los nuevos umbrales de calibración."""
    if not (0.10 <= confidence <= 0.95):
        raise ValueError(f"El umbral de confianza debe estar entre 0.10 y 0.95 (recibido: {confidence}).")
    if not (0.10 <= iou <= 0.90):
        raise ValueError(f"El umbral IoU debe estar entre 0.10 y 0.90 (recibido: {iou}).")
    if not (1.0 <= target_fps <= 30.0):
        raise ValueError(f"La tasa objetivo debe estar entre 1.0 y 30.0 FPS (recibido: {target_fps}).")

    now_iso = datetime.now().isoformat()

    with get_connection() as conn:
        cursor = conn.cursor()
        for key, val in [("confidence", str(confidence)), ("iou", str(iou)), ("target_fps", str(target_fps))]:
            cursor.execute(
                """
                INSERT INTO settings (key, value, updated_at) VALUES (?, ?, ?)
                ON CONFLICT(key) DO UPDATE SET value = excluded.value, updated_at = excluded.updated_at
                """,
                (key, val, now_iso),
            )

        # Registro en la bitácora de auditoría
        cursor.execute(
            """
            INSERT INTO calibration_audit (confidence, iou, target_fps, changed_by, created_at, note)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (confidence, iou, target_fps, changed_by, now_iso, note),
        )
        conn.commit()

    return {
        "confidence": confidence,
        "iou": iou,
        "target_fps": target_fps,
        "updated_at": now_iso,
    }


def reset_calibration_settings(changed_by: str = "Jorge (TI)") -> Dict[str, Any]:
    """Restaura los parámetros de calibración a los valores predeterminados de fábrica."""
    return save_calibration_settings(
        confidence=config.DEFAULT_YOLO_CONFIDENCE,
        iou=config.DEFAULT_YOLO_IOU,
        target_fps=config.DEFAULT_SAMPLE_FPS,
        changed_by=changed_by,
        note="Restauración a valores predeterminados de fábrica",
    )


def get_calibration_audit_logs(limit: int = 10) -> List[Dict[str, Any]]:
    """Consulta el historial de auditoría de calibración ordenado de más reciente a más antiguo."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM calibration_audit ORDER BY created_at DESC LIMIT ?", (limit,)
        )
        rows = cursor.fetchall()
        return [dict(r) for r in rows]


