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

