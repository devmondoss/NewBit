# 05 — Etapa YOLOv4

## 1. Función dentro de Unsafe-Net

YOLOv4 no es el clasificador final del comportamiento.

Su función principal es actuar como **selector espacial y temporal**:

1. detectar contenido relacionado con las conductas;
2. identificar frames potencialmente relevantes;
3. descartar frames seguros o sin interés;
4. reducir la longitud del clip;
5. preparar secuencias más limpias para ConvLSTM.

## 2. Arquitectura mencionada

El paper describe la estructura estándar de YOLOv4:

```text
CSPDarknet53
    ↓
SPP + PAN
    ↓
YOLO head
```

- **Backbone:** CSPDarknet53
- **Neck:** Spatial Pyramid Pooling + Path Aggregation Network
- **Head:** predicción de bounding boxes y clases

## 3. Datos anotados

Para YOLOv4, los autores extrajeron frames del video y anotaron:

- 2,262 imágenes train;
- 329 imágenes test.

Herramienta:
- LabelImg.

El ground truth fue creado con participación de un especialista de seguridad ocupacional de la fábrica.

Las etiquetas incluyen la geometría YOLO típica:

- centro x;
- centro y;
- width;
- height.

## 4. Configuración publicada

| Parámetro | Valor reportado |
|---|---|
| Input | 416×416 |
| Batch size | 65 |
| Subdivisions | 32 |
| GPU | 2 |
| IoU de evaluación | 0.5 |
| Test images | 329 |
| Tiempo de test | ~14 s |
| mAP test | 95.66% |

## 5. Inconsistencia importante: 4 vs 8 clases

El texto del paper dice que la configuración de entrenamiento tenía:

> `number of classes = 4`

Sin embargo, otras secciones describen detecciones y AP para clases seguras e inseguras, es decir, un universo de 8 categorías.

También se indica que se eliminan frames correspondientes a:

- 4 clases seguras;
- contenido irrelevante;

y se conservan los frames de las 4 clases inseguras.

### Interpretación correcta

No debemos resolver esta contradicción inventando.

Para una réplica hay que registrar:

- **Hecho:** el paper imprime `number of classes = 4` en la sección de configuración.
- **Hecho:** el paper analiza detecciones de clases safe + unsafe y menciona desempeño para más categorías.
- **Estado:** inconsistencia editorial/técnica no resuelta sin el `.cfg`, pesos y código originales.

## 6. Frame filtering

La parte esencial del método es:

```python
for frame in video:
    detections = yolo(frame)

    if contains_relevant_unsafe_pattern(detections):
        keep(frame)
    else:
        discard(frame)
```

Este pseudocódigo es conceptual; no es código publicado por los autores.

## 7. Ejemplo del paper

Un clip:

- entrada: 3.5 s;
- 105 frames;
- contiene varias acciones;

después del filtrado:

- 40 frames;
- 1.33 s;

y luego se separa en tres segmentos con una acción por segmento.

## 8. Riesgo de reproducción

El paper no libera un repositorio oficial conocido con:

- configuración exacta de Darknet;
- archivo `.cfg`;
- anchors;
- pesos originales;
- script de filtrado;
- reglas exactas que unen detecciones en segmentos.

Por eso la reproducción de YOLO es **reconstrucción metodológica**, no copia bit-a-bit.

## 9. Qué medir en nuestra réplica

Para esta etapa:

- precision;
- recall;
- AP/mAP;
- falsos positivos por clase;
- frames conservados / frames originales;
- reducción de duración;
- tiempo de procesamiento por clip;
- porcentaje de frames eliminados.

La métrica más importante para reproducir la tesis del paper es:

> **cuánto reduce YOLO la secuencia sin eliminar la evidencia necesaria para el clasificador temporal.**
