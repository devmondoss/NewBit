"""
Módulo de procesamiento y análisis de video para NewBit (PY-NB-001).
Implementa validación de contenedores multimedia y extracción de metadatos con OpenCV.
"""

from pathlib import Path
from typing import Dict, Any
import cv2

from app import config


def validate_video_file(filename: str, file_size_bytes: int) -> None:
    """
    Valida que el archivo cumpla con los formatos permitidos (.mp4, .avi)
    y no exceda el tamaño máximo configurado (100 MB).
    Lanza ValueError si alguna regla de negocio no se cumple.
    """
    suffix = Path(filename).suffix.lower()
    if suffix not in config.ALLOWED_EXTENSIONS:
        allowed_list = ", ".join(sorted(config.ALLOWED_EXTENSIONS))
        raise ValueError(
            f"Formato no permitido: '{suffix}'. Solo se aceptan archivos {allowed_list}."
        )

    if file_size_bytes > config.MAX_UPLOAD_BYTES:
        max_mb = config.MAX_UPLOAD_SIZE_MB
        actual_mb = round(file_size_bytes / (1024 * 1024), 2)
        raise ValueError(
            f"El archivo excede el tamaño máximo permitido de {max_mb} MB (tamaño recibido: {actual_mb} MB)."
        )


def get_video_metadata(video_path: Path | str) -> Dict[str, Any]:
    """
    Inspecciona el archivo de video con OpenCV y extrae su ficha técnica:
    ancho, alto, FPS, conteo de fotogramas, duración en segundos y códec.
    """
    path = Path(video_path)
    if not path.exists():
        raise FileNotFoundError(f"El archivo de video no existe en disco: {path}")

    cap = cv2.VideoCapture(str(path))
    if not cap.isOpened():
        raise ValueError(
            f"OpenCV no pudo decodificar el archivo '{path.name}'. Contenedor dañado o códec incompatible."
        )

    try:
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = float(cap.get(cv2.CAP_PROP_FPS))
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        # Cálculo de duración exacta
        duration_sec = round(frame_count / fps, 2) if fps > 0 else 0.0

        # Decodificación de FourCC del códec
        fourcc_int = int(cap.get(cv2.CAP_PROP_FOURCC))
        codec_chars = "".join([chr((fourcc_int >> (8 * i)) & 0xFF) for i in range(4)])
        codec = codec_chars.strip() if codec_chars.isprintable() else "H264"

        file_size_bytes = path.stat().st_size
        file_size_mb = round(file_size_bytes / (1024 * 1024), 2)

        return {
            "width": width,
            "height": height,
            "fps": round(fps, 2),
            "frame_count": frame_count,
            "duration_sec": duration_sec,
            "codec": codec if codec else "H264",
            "file_size_mb": file_size_mb,
        }
    finally:
        cap.release()


def extract_frames(
    video_path: Path | str,
    output_dir: Path | str,
    target_size: tuple = (640, 640),
    max_frames: int | None = None,
) -> list[str]:
    """
    Decodifica el video con OpenCV, normaliza cada fotograma al tamaño
    requerido por YOLOv8 (640x640) y los guarda secuencialmente como imágenes JPEG.
    Retorna la lista de nombres de archivo generados.
    """
    path = Path(video_path)
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    if not path.exists():
        raise FileNotFoundError(f"Video no encontrado: {path}")

    cap = cv2.VideoCapture(str(path))
    if not cap.isOpened():
        raise ValueError(f"No se pudo abrir el video para extraer fotogramas: {path.name}")

    extracted_files = []
    frame_idx = 0

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame_idx += 1
            if max_frames and frame_idx > max_frames:
                break

            # Normalización dimensional a target_size (640x640)
            if target_size:
                frame_resized = cv2.resize(frame, target_size, interpolation=cv2.INTER_AREA)
            else:
                frame_resized = frame

            filename = f"frame_{frame_idx:06d}.jpg"
            dest_frame_path = out_dir / filename

            # Guardar con calidad JPEG óptima (95%)
            cv2.imwrite(str(dest_frame_path), frame_resized, [cv2.IMWRITE_JPEG_QUALITY, 95])
            extracted_files.append(filename)

        return extracted_files
    finally:
        cap.release()

