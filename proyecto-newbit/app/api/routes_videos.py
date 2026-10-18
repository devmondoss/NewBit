"""
Rutas API para ingesta y consulta de videos (Sprint 1: HU01).
Permite subida de archivos .mp4/.avi, validación técnica y persistencia de metadatos.
"""

import uuid
import shutil
import aiofiles
from pathlib import Path
from fastapi import APIRouter, UploadFile, File, HTTPException, status
from fastapi.responses import JSONResponse, FileResponse


from app import config, db
from ml.video_processor import validate_video_file, get_video_metadata, extract_frames

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


@router.get("/{video_id}/stream")
async def stream_video(video_id: str):
    """Transmite el archivo de video para su reproducción en el reproductor HTML5."""
    video = db.get_video_by_id(video_id)
    if not video:
        raise HTTPException(status_code=404, detail="Video no encontrado.")

    video_path = Path(video["filepath"])
    if not video_path.exists():
        raise HTTPException(status_code=404, detail="El archivo físico de video no existe en disco.")

    return FileResponse(
        path=str(video_path),
        media_type="video/mp4",
        filename=video["filename"],
    )


@router.post("/{video_id}/extract-frames")
async def extract_video_frames(video_id: str, max_frames: int | None = None):
    """
    Dispara la fragmentación del video en fotogramas normalizados (640x640)
    y los almacena en storage/frames/{video_id}/.
    """
    video = db.get_video_by_id(video_id)
    if not video:
        raise HTTPException(status_code=404, detail="Video no encontrado.")

    video_path = Path(video["filepath"])
    output_dir = config.FRAMES_DIR / video_id

    try:
        frames = extract_frames(
            video_path=video_path,
            output_dir=output_dir,
            target_size=config.TARGET_FRAME_SIZE,
            max_frames=max_frames,
        )
        # Actualizar estado en la base de datos
        db.update_video_status(video_id, "frames_extracted")
        return {
            "status": "success",
            "message": f"Se extrajeron {len(frames)} fotogramas normalizados a 640x640.",
            "total_frames_extracted": len(frames),
            "target_resolution": f"{config.TARGET_FRAME_SIZE[0]}x{config.TARGET_FRAME_SIZE[1]}",
            "frames": frames[:50],  # Devolver muestra de nombres
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error durante la extracción de frames: {str(e)}")


@router.get("/{video_id}/frames")
async def list_video_frames(video_id: str):
    """Lista los fotogramas extraídos existentes para un video."""
    video = db.get_video_by_id(video_id)
    if not video:
        raise HTTPException(status_code=404, detail="Video no encontrado.")

    frames_dir = config.FRAMES_DIR / video_id
    if not frames_dir.exists():
        return {"status": "success", "count": 0, "frames": []}

    frames = sorted([f.name for f in frames_dir.glob("*.jpg")])
    return {
        "status": "success",
        "count": len(frames),
        "frames": frames,
    }


@router.get("/{video_id}/frames/{filename}")
async def get_single_frame(video_id: str, filename: str):
    """Sirve la imagen JPEG de un fotograma individual normalizado."""
    frame_path = config.FRAMES_DIR / video_id / filename
    if not frame_path.exists():
        raise HTTPException(status_code=404, detail="Fotograma no encontrado.")

    return FileResponse(path=str(frame_path), media_type="image/jpeg")


@router.delete("/{video_id}")
async def delete_video(video_id: str):
    """
    Elimina un video del catálogo y limpia todos sus artefactos en disco:
    archivo original en storage/uploads/, fotogramas en storage/frames/{id}/
    y registro en base de datos.
    """
    video = db.get_video_by_id(video_id)
    if not video:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Video con ID '{video_id}' no encontrado en el catálogo.",
        )

    # 1. Eliminar archivo original en uploads/
    raw_path = Path(video["filepath"])
    if raw_path.exists():
        try:
            raw_path.unlink()
        except Exception:
            pass

    # 2. Eliminar carpeta de fotogramas extraídos en frames/
    frames_dir = config.FRAMES_DIR / video_id
    if frames_dir.exists():
        try:
            shutil.rmtree(frames_dir)
        except Exception:
            pass

    # 3. Eliminar posibles archivos de salida procesados en outputs/
    for output_file in config.OUTPUTS_DIR.glob(f"{video_id}_*"):
        try:
            output_file.unlink()
        except Exception:
            pass

    # 4. Eliminar registro en base de datos
    db.delete_video_record(video_id)

    return {
        "status": "success",
        "message": f"Video '{video['original_name']}' ({video_id}) y sus recursos fueron eliminados correctamente.",
    }


