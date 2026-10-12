# 12 — Plan experimental y evaluación

## 1. Objetivo experimental

Evaluar si el pipeline:

```text
YOLO filtering + ConvLSTM
```

mejora la clasificación y la velocidad frente a:

```text
ConvLSTM sobre video sin reducción
```

## 2. Experimento 0 — sanity check

Objetivo:
verificar que el dataset se carga correctamente.

Medir:
- número de clips;
- clases;
- FPS;
- resolución;
- duración;
- archivos corruptos.

Salida:
`dataset_audit.csv`

## 3. Experimento 1 — baseline temporal

Input:
clips originales.

Modelo:
ConvLSTM.

Métricas:
- macro accuracy;
- micro accuracy;
- precision/recall/F1;
- confusion matrix;
- tiempo por clip.

## 4. Experimento 2 — detector

Input:
frames anotados.

Modelo:
YOLOv4.

Métricas:
- precision;
- recall;
- AP;
- mAP@0.5;
- FPs;
- inference time.

## 5. Experimento 3 — reducción

Input:
videos.

Proceso:
YOLO + reglas de selección.

Métricas:

```text
frame_reduction_ratio =
1 - kept_frames / original_frames
```

y:

```text
duration_reduction_ratio =
1 - reduced_duration / original_duration
```

También:
- pérdida de eventos;
- clips vacíos;
- fragmentación excesiva.

## 6. Experimento 4 — Unsafe-Net reducido

Input:
clips filtrados.

Modelo:
ConvLSTM.

Comparar con baseline:

| Métrica | Baseline | Filtered | Delta |
|---|---:|---:|---:|
| Macro Acc |  |  |  |
| Micro Acc |  |  |  |
| Macro F1 |  |  |  |
| Avg inference |  |  |  |
| Avg duration |  |  |  |

## 7. Experimento 5 — ablation

Si hay tiempo:

### A
ConvLSTM raw

### B
Uniform frame sampling + ConvLSTM

### C
YOLO filtering + ConvLSTM

Esto permite distinguir si la mejora viene de:
- simplemente usar menos frames;
o
- seleccionar frames semánticamente relevantes.

## 8. Métricas mínimas

### Clasificación
- accuracy macro;
- accuracy micro;
- macro F1;
- per-class recall;
- confusion matrix.

### Eficiencia
- tiempo detector;
- tiempo ConvLSTM;
- end-to-end time;
- frames procesados;
- reducción temporal.

### Robustez
- errores por clase;
- clips sin predicción;
- clips multiacción;
- sensibilidad al threshold.

## 9. Reporting honesto

Nunca reportar solo el mejor run.

Registrar:
- seed;
- hardware;
- versión de librerías;
- parámetros;
- timestamp;
- commit hash;
- checkpoint.

## 10. Criterios de éxito de una réplica educativa

No es necesario alcanzar 95.81%.

La réplica puede considerarse exitosa si:

1. implementa el pipeline completo;
2. logra separar etapa espacial y temporal;
3. demuestra cuantitativamente reducción de secuencia;
4. compara baseline vs filtered;
5. explica discrepancias con el paper;
6. documenta decisiones no especificadas;
7. puede reproducir sus propios resultados.

## 11. Reproducibilidad

Cada ejecución debería producir:

```text
runs/<experiment_id>/
├── config.yaml
├── metrics.json
├── confusion_matrix.png
├── training_curve.png
├── logs.txt
└── predictions.csv
```

## 12. Preguntas para discusión académica

- ¿La reducción mejora por eliminar ruido o por introducir conocimiento de clase?
- ¿YOLO está aprendiendo acciones o proxies visuales?
- ¿El sistema generaliza a otra cámara?
- ¿Las clases dependen demasiado del layout?
- ¿Qué ocurre cuando hay más de una acción simultánea?
- ¿La métrica de clip es suficiente para producción?
- ¿Cómo cambia el desempeño si se usa una arquitectura moderna?
