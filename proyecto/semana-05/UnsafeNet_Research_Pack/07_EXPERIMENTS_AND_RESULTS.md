# 07 — Experimentos y resultados

## 1. Hardware original

Workstation reportada:

- 2× NVIDIA GeForce GTX 1080
- Intel Core i9-9900
- 16 GB RAM
- HDD 3 TB
- SSD 500 GB

## 2. Resultado de YOLOv4

- 2,262 imágenes train;
- 329 imágenes test;
- input 416×416;
- mAP test: **95.66%** a IoU 0.5;
- test de 329 imágenes: ~14 s.

Los autores indican que Safe Carrying fue particularmente difícil por la similitud visual con Forklift Overload.

## 3. Resultado de ConvLSTM vs Unsafe-Net

### Sin frame reduction

Accuracy promedio por clases:
**85.78%**

### Con YOLOv4 + ConvLSTM

Accuracy promedio por clases:
**95.81%**

## 4. Por qué 95.81% y no 96.88%

El paper dice que, de 64 clips, **62 fueron correctamente clasificados**.

Si calculamos micro-accuracy:

```text
62 / 64 = 96.875%
```

Pero el paper reporta 95.81%.

Esto se explica porque promedia la accuracy de las cuatro clases:

```text
Walkway Violation      32/32 = 100.00%
Unauthorized           10/11 =  90.91%
Opened Panel           12/13 =  92.31%
Forklift Overload       8/8  = 100.00%

macro average = 95.805% ≈ 95.81%
```

No es necesariamente una contradicción: son dos formas distintas de agregar la métrica.

### Para nuestra réplica

Debemos reportar ambas:

- **micro accuracy**
- **macro accuracy**

y además:
- precision por clase;
- recall por clase;
- F1 por clase;
- confusion matrix.

## 5. Comparación de errores

A partir de los conteos descritos:

### ConvLSTM sin reducción

Errores reportados:
- Walkway Violation: 1
- Unauthorized Intervention: 2
- Opened Panel Cover: 3
- Forklift Overload: 1

Promedio por clase ≈ 85.78%.

### Unsafe-Net

Errores:
- Walkway Violation: 0
- Unauthorized Intervention: 1
- Opened Panel Cover: 1
- Forklift Overload: 0

## 6. Reducción de tiempo

### Video original del test

Promedio:
**7.72 s**

### Después del filtrado

Promedio:
**1.87 s**

### Tiempo de reconocimiento

ConvLSTM sin reducción:
**0.58 s**

Unsafe-Net después de reducción:
**0.14 s**

## 7. Cuidado con “0.14 s”

0.14 s es el tiempo de **action recognition sobre el clip ya reducido**.

No es la latencia total cámara → alerta.

El paper añade un ejemplo:

- YOLO tarda ~1.2 s en reducir un clip de 3 s a 1 s;
- ConvLSTM tarda ~0.14 s;
- estimación total: ~1.34 s.

Por tanto, en informes:

### Incorrecto

> Unsafe-Net tiene una latencia end-to-end de 0.14 segundos.

### Correcto

> La etapa temporal reporta 0.14 s de reconocimiento promedio una vez reducido el clip; el paper estima aproximadamente 1.34 s en un ejemplo que incluye la reducción YOLO.

## 8. Qué demuestra realmente el experimento

El paper aporta evidencia de que, **en este dataset y este entorno**, la reducción previa:

- disminuye longitud de los clips;
- reduce tiempo de clasificación;
- mejora la accuracy macro.

No demuestra automáticamente que el mismo incremento ocurra en otra fábrica.
