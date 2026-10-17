"""
Rutas API para ingesta y consulta de videos (Sprint 1: HU01).
Permite subida de archivos .mp4/.avi, validación técnica y persistencia de metadatos.
"""

import uuid
import aiofiles
from pathlib import Path
from fastapi import APIRouter, UploadFile, File, HTTPException, status
from fastapi.responses import JSONResponse

from app import config, db
from ml.video_processor import validate_video_file, get_video_metadata

router = APIRouter(prefix="/api/videos", tags=["Videos"])


@router.post("/upload", status_code=status.HTTP_201_CREATED)
async def upload_video(file: UploadFile = File(...)):
    """
    Recibe un archivo de video industrial (.mp4 o .avi), valida su formato y tamaño,
    lo persiste en storage/uploads/, extrae sus metadatos con OpenCV y registra el video.
    """
    if not file.filename:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se proporcionó ningún nombre de archivo.",
        )

    # 1. Validación de extensión preliminar
    try:
        validate_video_file(file.filename, 0)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    # 2. Generación de identificador único y ruta segura
    video_id = str(uuid.uuid4())[:8]
    clean_name = Path(file.filename).name.replace(" ", "_")
    saved_filename = f"{video_id}_{clean_name}"
    dest_path = config.UPLOADS_DIR / saved_filename

    # 3. Guardado en disco controlando tamaño máximo
    bytes_written = 0
    try:
        async with aiofiles.open(dest_path, "wb") as out_file:
            while chunk := await file.read(1024 * 1024):  # 1 MB por bloque
                bytes_written += len(chunk)
                if bytes_written > config.MAX_UPLOAD_BYTES:
                    raise ValueError(
                        f"El archivo supera el límite de {config.MAX_UPLOAD_SIZE_MB} MB."
                    )
                await out_file.write(chunk)
    except Exception as e:
        if dest_path.exists():
            dest_path.unlink()  # Limpiar archivo parcial en caso de error
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Fallo durante la carga del archivo: {str(e)}",
        )

    # 4. Extracción de metadatos con OpenCV
    try:
        metadata = get_video_metadata(dest_path)
    except Exception as e:
        if dest_path.exists():
            dest_path.unlink()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error al analizar el video con OpenCV: {str(e)}",
        )

    # 5. Persistencia en SQLite
    record = {
        "id": video_id,
        "filename": saved_filename,
        "original_name": file.filename,
        "filepath": str(dest_path),
        "file_size_mb": metadata["file_size_mb"],
        "duration_sec": metadata["duration_sec"],
        "fps": metadata["fps"],
        "frame_count": metadata["frame_count"],
        "width": metadata["width"],
        "height": metadata["height"],
        "codec": metadata["codec"],
        "status": "uploaded",
    }
    db.save_video_record(record)

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "status": "success",
            "message": "Video cargado y analizado con éxito.",
            "video": record,
        },
    )


@router.get("")
async def list_videos():
    """Retorna la lista completa de videos registrados en el catálogo."""
    videos = db.get_all_videos()
    return {
        "status": "success",
        "count": len(videos),
        "videos": videos,
    }


@router.get("/{video_id}")
async def get_video(video_id: str):
    """Consulta la ficha técnica detallada de un video por ID."""
    video = db.get_video_by_id(video_id)
    if not video:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Video con ID '{video_id}' no encontrado en el catálogo.",
        )
    return {
        "status": "success",
        "video": video,
    }
