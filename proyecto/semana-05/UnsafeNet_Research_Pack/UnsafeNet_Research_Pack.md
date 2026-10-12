# UnsafeNet Research Pack – ficha rápida

- **Original:** `UnsafeNet_Research_Pack.zip` (30 KB), ya descomprimido en esta misma carpeta: 15 `.md` + `MANIFEST.json`. No hay que volver a abrir el zip.
- **Fecha:** 12/10/2026 (semana 5) · **Autor:** el equipo (investigación propia) · **Tipo:** ficha rápida; se hojearon README, dataset (04), alcance (01), réplica (10) y hardware (11).
- **Entrada al pack:** [README.md](README.md) (índice de los 14 documentos y convención de evidencia).

## Qué es
Documentación para hacer una **réplica educativa, a pequeña escala, de Unsafe-Net** (Önal y Dandıl). No pretende novedad científica: entender el sistema original, ver qué se puede reproducir con lo publicado y diseñar una réplica trazable. Marca cada afirmación como **[FUENTE PRIMARIA]**, **[FUENTE OFICIAL]**, **[DERIVADO]** o **[RÉPLICA PROPUESTA]**.

## Dónde buscar cada cosa
| Necesito… | Archivo |
|---|---|
| Qué es y qué no es; pregunta de réplica | `01_SCOPE_AND_TAXONOMY.md` |
| Paper 2021, tesis, paper 2024, dataset, patente | `02_RESEARCH_LINEAGE.md` |
| Arquitectura original (adquisición → YOLOv4 → reducción → ConvLSTM → GUI → alerta) | `03_ORIGINAL_SYSTEM_ARCHITECTURE.md` |
| Dataset: clases, clips, splits, licencia | `04_DATASET.md` |
| Detalles de YOLOv4 y ConvLSTM | `05_…`, `06_…` |
| Resultados (95.81 %, tiempos) y piloto (75 %) | `07_…`, `08_…` |
| Inconsistencias del paper y preguntas abiertas | `09_LIMITATIONS_AND_OPEN_QUESTIONS.md` |
| **Plan de réplica recomendado** | `10_SMALL_SCALE_REPLICATION.md` |
| Stack, hardware, **requisitos RF-01…RF-07** | `11_REQUIREMENTS_AND_STACK.md` |
| Experimentos y métricas | `12_EXPERIMENT_PLAN.md` |
| Enlaces y glosario | `13_REFERENCES.md`, `14_GLOSSARY.md` |

## Datos clave
- **Hay dataset público:** *Video Dataset for Safe and Unsafe Behaviours*, Mendeley Data, DOI `10.17632/xjmtb22pff.1`, **CC BY 4.0** (11/06/2024). Fábrica en Eskişehir (Turquía), 39 días, ~4,000 h de video bruto.
- **8 clases** (4 inseguras + sus 4 contrapartes seguras) y **691 clips** (566 de entrenamiento y 125 de prueba, con el split oficial), de unos 5–10 s en promedio.
- **No hay código oficial** y los hiperparámetros del ConvLSTM están incompletos (09).
- **Pregunta de réplica recomendada:** ¿seleccionar frames con YOLO antes del ConvLSTM mejora la clasificación y reduce el tiempo frente a usar ConvLSTM directo sobre los clips?
- **Nivel recomendado: B, réplica pequeña fiel.** Consiste en:
  - 2–4 clases inseguras, reanotando una muestra de frames con LabelImg;
  - YOLOv4 para filtrar frames → ConvLSTM;
  - comparar con el baseline;
  - una GUI simple con alerta simulada.
  - Si falta tiempo: **Safe Walkway Violation + Opened Panel Cover**.
- **Hardware:** GPU NVIDIA o Colab, 16 GB de RAM y **30–50 GB libres** en disco.

## Análisis
- **Resuelve el mayor riesgo:** existía la duda de dónde sacar el video. El dataset es público y su licencia permite usarlo con atribución, así que no hace falta una planta real ni grabar escenas.
- **Cierra varias decisiones abiertas** (ver `proyecto/README.md`):
  - conductas: 2, ampliables a 4;
  - datos: dataset de Mendeley con su split oficial;
  - enfoque: réplica fiel de nivel B, sin modernizar componentes salvo que se declare;
  - entrenamiento: Colab o una GPU local.
- **Sirve directo para los formatos:**
  - Épicas y Backlog: los requisitos RF-01…RF-07 (11) y el pipeline (10).
  - Justificación: los antecedentes (02) y las limitaciones (09).
  - Acta: el alcance y los criterios de éxito (10, 12).
- **Cuidado:**
  - El 95.81 % y la baja del 75 % son resultados **de los autores**; el propio pack aclara qué se puede afirmar y qué no (08).
  - Las cifras de esta ficha vienen del pack y **no se verificaron contra Mendeley**. Conviene abrir el enlace del dataset una vez para confirmar el tamaño y la licencia antes de escribir el Acta.
- **Pendiente** (lo que el pack no cubre de la guía de investigación):
  - contexto peruano: estadísticas, Ley 29783 y Ley 29733;
  - la organización del caso;
  - los interesados reales;
  - los costos en soles.
