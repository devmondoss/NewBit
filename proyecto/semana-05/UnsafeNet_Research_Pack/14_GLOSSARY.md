# 14 — Glosario

## Action Recognition
Clasificación de una acción usando una secuencia temporal, no únicamente una imagen.

## AP — Average Precision
Área resumida bajo la relación precision-recall para una clase.

## mAP — Mean Average Precision
Promedio de AP entre clases de detección.

## Bounding Box
Rectángulo que localiza un objeto/región en una imagen.

## CNN
Convolutional Neural Network. Extrae patrones espaciales.

## ConvLSTM
Arquitectura recurrente donde las operaciones internas incluyen convoluciones, permitiendo modelar secuencias preservando estructura espacial.

## Deep Learning
Familia de métodos de aprendizaje basados en redes neuronales profundas.

## Frame
Una imagen individual de un video.

## Frame Filtering
Proceso de conservar/eliminar frames según relevancia.

En Unsafe-Net es parte esencial de la arquitectura.

## Human Action Recognition
Área de computer vision dedicada a identificar acciones humanas desde imágenes o video.

## IoU — Intersection over Union
Solapamiento entre bounding box predicha y ground truth.

## LSTM
Long Short-Term Memory. Red recurrente diseñada para dependencias temporales.

## Macro Accuracy
Promedio de la accuracy calculada independientemente por clase.

El 95.81% reportado por Unsafe-Net corresponde a esta lógica de promediado.

## Micro Accuracy
Correctos totales / muestras totales.

En el test final de Unsafe-Net, 62/64 ≈ 96.88%.

## Object Detection
Localiza y clasifica objetos/regiones dentro de una imagen.

## Occupational Health and Safety
Seguridad y salud ocupacional.

## PPE / EPP
Personal Protective Equipment / Equipo de Protección Personal.

Unsafe-Net no es solo PPE detection.

## Temporal Segmentation
División de un video en fragmentos que representan acciones/eventos específicos.

## Video Understanding
Conjunto de técnicas que buscan extraer significado de secuencias de video.

## YOLOv4
Detector one-stage usado por Unsafe-Net para localizar contenido y reducir los clips antes de ConvLSTM.

## Domain Shift
Caída de desempeño cuando un modelo entrenado en un entorno se aplica a otro con distribución visual distinta.

## False Positive
El sistema detecta algo que no corresponde a la clase/evento real.

## Ground Truth
Etiqueta considerada referencia correcta para entrenamiento/evaluación.

## Ablation Study
Experimento que elimina o cambia componentes para medir qué parte produce la mejora.
