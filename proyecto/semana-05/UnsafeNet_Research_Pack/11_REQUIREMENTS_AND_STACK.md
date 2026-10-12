# 11 — Requisitos técnicos y stack

## 1. Stack original confirmado

### Machine Learning
- YOLOv4
- ConvLSTM

### Aplicación
- Python
- PyQt Designer

### Hardware de alerta
- ESP8266
- Arduino Uno
- salida audible
- salida visual

### Datos
- video MP4 H.264
- 1920×1080
- 24 FPS

## 2. Stack recomendado para la réplica

> Esto es una decisión de réplica, no necesariamente el stack exacto original.

### Lenguaje
- Python 3.10/3.11

### Video
- OpenCV
- FFmpeg

### Deep learning
Una de:
- TensorFlow/Keras para ConvLSTM;
- PyTorch si el equipo prefiere implementar ConvLSTM allí.

Para máxima cercanía conceptual:
- Keras `ConvLSTM2D` simplifica la reconstrucción.

### YOLOv4
Opciones:

#### A. Darknet
Más fiel históricamente.

Pros:
- cercano al modelo original.

Contras:
- setup más pesado;
- CUDA/NVIDIA más cómodo.

#### B. implementación PyTorch compatible con YOLOv4
Más fácil de integrar, pero debe documentarse como adaptación de implementación.

## 3. Hardware mínimo de curso

### Desarrollo/preprocesamiento
- CPU moderna
- 16 GB RAM recomendado
- SSD

### Entrenamiento
Recomendado:
- GPU NVIDIA con CUDA

Alternativa:
- Google Colab / notebook con GPU.

ConvLSTM con dataset reducido puede entrenarse en hardware moderado.

## 4. Espacio en disco

El dataset de video distribuido por terceros ronda varios GB y la extracción de frames puede multiplicar el uso.

Planificar al menos:

- dataset;
- frames;
- labels;
- checkpoints;
- clips reducidos;
- resultados.

Recomendación práctica:
**30–50 GB libres** para trabajar cómodamente.

## 5. Dependencias sugeridas

```text
python
opencv-python
numpy
pandas
scikit-learn
matplotlib
tensorflow
ffmpeg
tqdm
pyyaml
```

Y, según implementación YOLO:
- Darknet/CUDA/cuDNN;
o
- PyTorch + librería YOLOv4 elegida.

## 6. Herramientas de anotación

Original:
- LabelImg

Para mantener fidelidad:
- usar LabelImg.

Formato típico YOLO:

```text
class x_center y_center width height
```

normalizado a 0–1.

## 7. Requisitos funcionales

### RF-01
El sistema debe aceptar clips MP4.

### RF-02
Debe ejecutar detección frame a frame.

### RF-03
Debe conservar frames relevantes según una regla explícita.

### RF-04
Debe agrupar frames en secuencias.

### RF-05
Debe clasificar la secuencia.

### RF-06
Debe registrar:
- archivo;
- clase;
- confidence;
- tiempo;
- cantidad de frames original;
- cantidad conservada.

### RF-07
Debe generar una salida visible de alerta/detección.

## 8. Requisitos no funcionales

- reproducibilidad;
- logs;
- configuración versionada;
- separación train/test;
- ejecución determinista cuando sea posible;
- checkpoints;
- métricas por clase;
- no modificar el test set para “mejorar” resultados.

## 9. Estructura de configuración

```yaml
experiment:
  id: exp_001
  seed: 42

dataset:
  classes: 4
  split: official

detector:
  architecture: yolov4
  input_size: 416
  confidence_threshold: TBD

segmenter:
  max_gap_frames: TBD

convlstm:
  filters: [4, 8, 14, 16]
  kernel_size: [3, 3]
  dropout: 0.2

evaluation:
  macro_accuracy: true
  micro_accuracy: true
  confusion_matrix: true
```

Los `TBD` existen a propósito: representan parámetros que deben elegirse y documentarse porque no están completamente fijados por la publicación.
