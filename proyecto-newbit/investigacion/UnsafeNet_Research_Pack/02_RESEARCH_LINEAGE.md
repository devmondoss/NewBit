# 02 — Genealogía de la investigación

## 1. La línea de investigación

Unsafe-Net es la culminación de varios años de trabajo de Oğuzhan Önal y Emre Dandıl sobre visión computacional aplicada a seguridad laboral.

### Línea temporal

| Año / fecha | Hito | Relevancia |
|---|---|---|
| 2019 | Proyecto BAP `2019-02.BŞEÜ.01-03` | Financia la línea de investigación |
| 2021 | Paper YOLOv4 para seguridad laboral | Antecedente directo centrado en detección |
| 2022 | Captura de video industrial | Base de datos real de la fábrica |
| 2023-10-20 | Envío de Unsafe-Net | Inicio del proceso editorial |
| 2024-04-18 | Aceptación | Paper aceptado |
| 2024-05-04 | Publicación online | Unsafe-Net disponible en Springer |
| 2024-06-11 | Dataset en Mendeley | Se publica el dataset |
| 2024-08 | Data in Brief | Paper específico de documentación del dataset |
| 2024-09-25 | Tesis doctoral | Önal presenta la tesis que integra la línea |
| 2025 | Volumen 84 de la revista | Referencia bibliográfica final del paper |
| 2025 | Solicitud de patente `2025/001387` | Continuidad tecnológica institucional |
| 2026 | Reutilizaciones modernas | FiftyOne, NVIDIA Cosmos y otros trabajos derivados |

## 2. Antecedente 2021

**Título:** *Object Detection for Safe Working Environments using YOLOv4 Deep Learning Model*

Autores: Oğuzhan Önal y Emre Dandıl.

El trabajo anterior usa YOLOv4 para monitorear elementos relacionados con seguridad y EPP. Reporta:

- mAP: 91.18%
- precision: 0.89
- recall: 0.91
- F1: 0.90

Su importancia no está solo en las métricas: demuestra que la línea comenzó en **detección espacial** antes de evolucionar a reconocimiento temporal.

Fuente:
https://dergipark.org.tr/en/pub/ejosat/article/951733

## 3. Evolución conceptual

```text
2021
detección de objetos / EPP
        ↓
limitación: un frame no describe una acción
        ↓
2022
captura de video real
        ↓
2024
YOLOv4 + ConvLSTM
        ↓
detección + comprensión temporal
        ↓
Unsafe-Net
```

## 4. Paper principal

**Título:** *Unsafe-Net: YOLO v4 and ConvLSTM based computer vision system for real-time detection of unsafe behaviours in workplace*

Autores:
- Oğuzhan Önal
- Emre Dandıl

Revista:
- *Multimedia Tools and Applications*
- publicación online: 4 mayo 2024
- volumen 84, 2025
- páginas 34967–34993
- DOI: `10.1007/s11042-024-19276-8`

Fuente:
https://link.springer.com/article/10.1007/s11042-024-19276-8

## 5. Tesis doctoral

**Título original:** *Endüstriyel ortamlarda güvensiz davranışların video üzerinden tespiti için yeni bir derin öğrenme modeli geliştirilmesi*

**Título inglés:** *Development of a new deep learning model for video detection of unsafe behaviors in industrial environments*

Autor:
- Oğuzhan Önal

Asesor:
- Emre Dandıl

La tesis documenta dos grandes etapas:

1. identificación de EPP con YOLO;
2. desarrollo de Unsafe-Net con YOLOv4 + ConvLSTM.

La tesis confirma que la segunda etapa utiliza 39 días de video y reporta los mismos resultados centrales de Unsafe-Net.

Fuente:
https://acikkaynak.bilecik.edu.tr/items/a55c58c5-1408-4ac3-a052-f861f59a985e/full

## 6. Dataset y paper de datos

El dataset se publica como:

**Video Dataset for Safe and Unsafe Behaviours**

DOI:
`10.17632/xjmtb22pff.1`

El paper de datos se publica en *Data in Brief*:

**Video dataset for the detection of safe and unsafe behaviours in workplaces**

- Vol. 56
- Article 110791
- DOI: `10.1016/j.dib.2024.110791`

Fuentes:
- https://data.mendeley.com/datasets/xjmtb22pff/1
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11367630/

## 7. Solicitud de patente

El portafolio oficial de Bilecik Şeyh Edebali University lista:

- solicitud: `2025/001387`
- inventores/titulares listados: Emre Dandıl y Oğuzhan Önal
- título relativo a un método y sistema de deep learning para detectar comportamientos inseguros mediante cámaras de seguridad.

Fuente:
https://bilecik.edu.tr/dosya/13821_5d76_13821_09cb_Patent%20portfoy%C3%BC.pdf%20SON.pdf

**Precaución:** la existencia de la solicitud no equivale a afirmar que la patente fue concedida.

## 8. Ecosistema posterior

### FiftyOne / Voxel51

El dataset está empaquetado para exploración desde FiftyOne/Hugging Face.

Esto facilita:
- inspección visual;
- filtrado de muestras;
- análisis de metadata;
- experimentación.

Fuente:
https://docs.voxel51.com/dataset_zoo/datasets_hf/safe_and_unsafe_behaviours.html

### NVIDIA Cosmos

En 2026, NVIDIA publica una receta que reutiliza el problema y el dataset con un Video Language Model.

Esto sirve para estudiar la evolución del problema, pero:

> **no es parte de Unsafe-Net original.**

Fuente:
https://github.com/nvidia-cosmos/cosmos-cookbook/blob/main/docs/recipes/inference/reason2/worker_safety/inference.md
