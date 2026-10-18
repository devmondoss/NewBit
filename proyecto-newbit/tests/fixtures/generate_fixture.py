"""
Generador del fixture de video para pruebas de integración de extremo a extremo (E2E) en NewBit.
Crea un clip representativo de CCTV de taller metalmecánico (24 FPS, 640x480) que contiene:
- Segmento A: 1.0s de tiempo muerto (nave vacía sin operarios)
- Segmento B: 2.5s de actividad operativa continua (operarios reales en la escena)
- Segmento C: 1.5s de tiempo muerto (operarios fuera del encuadre)
Total: 5.0 segundos (120 fotogramas).
"""

import cv2
import numpy as np
from pathlib import Path
from ultralytics.utils import ASSETS


def create_industrial_background(width: int = 640, height: int = 480) -> np.ndarray:
    """Crea una vista sintética del piso de un taller metalmecánico con pasarela de seguridad."""
    # Fondo base gris cemento industrial
    img = np.full((height, width, 3), (70, 75, 80), dtype=np.uint8)

    # Pasarela verde de seguridad (clase Safe Walkway de Kafaoğlu / Unsafe-Net)
    # Coordenadas X: 200 a 440
    cv2.rectangle(img, (200, 0), (440, height), (40, 110, 45), -1)

    # Franjas amarillas delimitadoras de seguridad
    for y in range(0, height, 40):
        cv2.line(img, (198, y), (198, y + 20), (0, 215, 255), 3)
        cv2.line(img, (442, y), (442, y + 20), (0, 215, 255), 3)

    # Rótulo de identificación de nave
    cv2.putText(
        img,
        "TALLER METALMECANICO - CAMARA CCTV 14",
        (20, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        (220, 220, 220),
        1,
        cv2.LINE_AA,
    )
    cv2.putText(
        img,
        "PASARELA PEATONAL SEGURA (KAFAOGLU)",
        (208, height - 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.42,
        (180, 255, 180),
        1,
        cv2.LINE_AA,
    )
    return img


def generate_sample_metalworking_clip(output_path: Path) -> Path:
    """Genera el clip de 5.0s con fases de tiempo muerto y presencia humana real."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    width, height = 640, 480
    fps = 24
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(str(output_path), fourcc, fps, (width, height))

    # Cargar imagen oficial de personas de Ultralytics (zidane.jpg)
    zidane_path = ASSETS / "zidane.jpg"
    person_img = cv2.imread(str(zidane_path))
    if person_img is None:
        raise FileNotFoundError(f"No se pudo cargar asset base en {zidane_path}")

    # Escalar imagen de persona para que quepa en el encuadre
    person_resized = cv2.resize(person_img, (320, 360))

    # 1. Fase Inicial: 1.0 segundo de tiempo muerto (24 frames vacíos)
    bg_empty = create_industrial_background(width, height)
    for _ in range(24):
        writer.write(bg_empty)

    # 2. Fase Activa: 2.5 segundos con operarios en nave (60 frames activos)
    for i in range(60):
        frame = create_industrial_background(width, height)
        # Componer a los operarios en la pasarela peatonal
        # y1: 80 a 440, x1: 160 a 480
        frame[80:440, 160:480] = person_resized
        # Marca de tiempo visual
        time_sec = round((24 + i) / 24, 2)
        cv2.putText(
            frame,
            f"ACTIVIDAD OPERARIA T: {time_sec}s",
            (20, 65),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (50, 220, 80),
            1,
            cv2.LINE_AA,
        )
        writer.write(frame)

    # 3. Fase Final: 1.5 segundos de tiempo muerto (36 frames vacíos)
    for _ in range(36):
        writer.write(bg_empty)

    writer.release()
    return output_path


if __name__ == "__main__":
    out_file = Path(__file__).resolve().parent / "sample_metalworking_clip.mp4"
    generate_sample_metalworking_clip(out_file)
    print(f"Fixture generado exitosamente en: {out_file}")
