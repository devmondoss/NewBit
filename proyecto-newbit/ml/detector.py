"""
Módulo de inferencia espacial con YOLOv8 para NewBit (PY-NB-001).
Carga el modelo ligero YOLOv8n, detecta operarios (clase person de COCO),
calcula cajas delimitadoras y genera fotogramas anotados para el filtrado espacial (HU05).
"""

from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple
import cv2
import numpy as np
from ultralytics import YOLO

from app import config, db


class YOLOv8Detector:
    _instance: Optional["YOLOv8Detector"] = None
    _model: Optional[YOLO] = None

    def __init__(self, model_path: Optional[Path | str] = None):
        """Inicializa el detector cargando los pesos de YOLOv8n."""
        path = Path(model_path or config.YOLO_MODEL_PATH)
        if not path.exists():
            # Si el peso no está en weights/, Ultralytics lo descargará
            self.model = YOLO("yolov8n.pt")
        else:
            self.model = YOLO(str(path))

    @classmethod
    def get_instance(cls) -> "YOLOv8Detector":
        """Patrón singleton para evitar recargar el modelo en memoria en cada petición."""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def detect_frame(
        self,
        image: np.ndarray | str | Path,
        conf: Optional[float] = None,
        iou: Optional[float] = None,
        target_classes: Optional[List[int]] = None,
    ) -> Dict[str, Any]:
        """
        Ejecuta la inferencia sobre un único fotograma buscando operarios (clase 0: person).
        Retorna las coordenadas de bounding boxes, confianzas y etiquetas.
        """
        # Si no se especifican umbrales, se consultan los valores activos en SQLite (HU11)
        if conf is None or iou is None:
            calib = db.get_calibration_settings()
            conf = conf if conf is not None else calib["confidence"]
            iou = iou if iou is not None else calib["iou"]

        if target_classes is None:
            target_classes = [0]  # Clase 0: person (operario en taller)

        results = self.model.predict(
            source=image,
            conf=conf,
            iou=iou,
            classes=target_classes,
            verbose=False,
        )

        detections = []
        if results and len(results) > 0:
            boxes = results[0].boxes
            if boxes is not None and len(boxes) > 0:
                xyxy = boxes.xyxy.cpu().numpy()
                confs = boxes.conf.cpu().numpy()
                cls_ids = boxes.cls.cpu().numpy().astype(int)

                for box, score, cid in zip(xyxy, confs, cls_ids):
                    detections.append({
                        "box": [round(float(coord), 1) for coord in box],
                        "confidence": round(float(score), 2),
                        "class_id": int(cid),
                        "label": "operario",
                    })

        return {
            "has_detections": len(detections) > 0,
            "detections_count": len(detections),
            "detections": detections,
            "conf_used": conf,
            "iou_used": iou,
        }

    def draw_bounding_boxes(
        self, image: np.ndarray, detections: List[Dict[str, Any]]
    ) -> np.ndarray:
        """
        Dibuja los recuadros delimitadores y etiquetas sobre una copia del fotograma con OpenCV.
        Estilo visual: recuadro azul/esmeralda, etiqueta con fondo translúcido y porcentaje.
        """
        annotated = image.copy()

        for det in detections:
            x1, y1, x2, y2 = [int(v) for v in det["box"]]
            conf_pct = int(det["confidence"] * 100)
            label = f"operario: {conf_pct}%"

            # Color verde esmeralda para presencia humana detectada en BGR: (50, 180, 80)
            color = (80, 180, 50)
            thickness = 2
            cv2.rectangle(annotated, (x1, y1), (x2, y2), color, thickness)

            # Fondo para la etiqueta de texto
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 0.45
            font_thickness = 1
            (text_w, text_h), baseline = cv2.getTextSize(label, font, font_scale, font_thickness)

            tag_y1 = max(0, y1 - text_h - 6)
            tag_y2 = y1
            tag_x2 = min(annotated.shape[1], x1 + text_w + 8)

            cv2.rectangle(annotated, (x1, tag_y1), (tag_x2, tag_y2), color, -1)
            cv2.putText(
                annotated,
                label,
                (x1 + 4, tag_y2 - 3),
                font,
                font_scale,
                (255, 255, 255),
                font_thickness,
                cv2.LINE_AA,
            )

        return annotated

    def process_video_frames(
        self,
        video_id: str,
        conf: Optional[float] = None,
        iou: Optional[float] = None,
    ) -> Dict[str, Any]:
        """
        Escanea todos los fotogramas del video en storage/frames/{video_id}/,
        genera las versiones anotadas con bounding boxes en annotated/ y
        clasifica fotogramas activos vs. inactivos (filtro espacial de Unsafe-Net).
        """
        frames_dir = config.FRAMES_DIR / video_id
        if not frames_dir.exists():
            raise FileNotFoundError(f"No se encontraron fotogramas extraídos para el video {video_id}.")

        annotated_dir = frames_dir / "annotated"
        annotated_dir.mkdir(parents=True, exist_ok=True)

        # Buscar todos los JPG principales (ignorando la subcarpeta annotated)
        frame_files = sorted([f for f in frames_dir.glob("*.jpg") if f.is_file()])
        if not frame_files:
            raise ValueError(f"No hay fotogramas disponibles en {frames_dir}.")

        total_frames = len(frame_files)
        active_frames = []
        inactive_frames = []
        total_detections_count = 0
        detections_by_frame = {}
        annotated_filenames = []

        for frame_file in frame_files:
            img = cv2.imread(str(frame_file))
            if img is None:
                continue

            det_result = self.detect_frame(img, conf=conf, iou=iou)
            has_person = det_result["has_detections"]
            num_persons = det_result["detections_count"]
            total_detections_count += num_persons

            # Dibujar bounding boxes (incluso si no hay operarios devuelve copia limpia)
            annotated_img = self.draw_bounding_boxes(img, det_result["detections"])

            out_annotated_file = annotated_dir / frame_file.name
            cv2.imwrite(str(out_annotated_file), annotated_img, [cv2.IMWRITE_JPEG_QUALITY, 95])

            annotated_filenames.append(frame_file.name)
            detections_by_frame[frame_file.name] = det_result["detections"]

            if has_person:
                active_frames.append(frame_file.name)
            else:
                inactive_frames.append(frame_file.name)

        active_ratio_pct = (
            round((len(active_frames) / total_frames) * 100, 2)
            if total_frames > 0
            else 0.0
        )
        empty_ratio_pct = round(100.0 - active_ratio_pct, 2)

        meta_result = {
            "video_id": video_id,
            "total_frames_analyzed": total_frames,
            "active_frames_count": len(active_frames),
            "inactive_frames_count": len(inactive_frames),
            "total_detections_count": total_detections_count,
            "active_ratio_pct": active_ratio_pct,
            "spatial_filter_reduction_pct": empty_ratio_pct,
            "active_frames": active_frames,
            "inactive_frames": inactive_frames,
            "annotated_filenames": annotated_filenames,
            "detections_by_frame": detections_by_frame,
        }

        # Persistir resumen en detections.json para consumo rápido por sequence_grouper
        try:
            import json
            meta_path = frames_dir / "detections.json"
            with open(meta_path, "w", encoding="utf-8") as f:
                json.dump(meta_result, f, indent=2)
        except Exception:
            pass

        return meta_result

