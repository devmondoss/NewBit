# Unsafe-Net Research Pack

> **Propósito:** documentación técnica y académica para iniciar una réplica educativa, a menor escala, de **Unsafe-Net**, el sistema de visión computacional de Oğuzhan Önal y Emre Dandıl para detectar comportamientos inseguros en entornos industriales.

## 1. Contexto del proyecto

El proceso previo del equipo fue:

**revisión amplia de papers → Top 20 → Top 3 → selección final: Unsafe-Net**

A partir de esta carpeta, Unsafe-Net se trata como la **investigación base**. Las otras investigaciones del Top 3 quedan únicamente como literatura relacionada o benchmarks, no como parte del sistema que se pretende replicar.

La intención **no es afirmar novedad científica** ni presentar el sistema como una invención propia. El objetivo es:

1. comprender con precisión la investigación original;
2. reconstruir su lógica de extremo a extremo;
3. identificar qué partes son reproducibles con la información pública;
4. detectar vacíos e inconsistencias;
5. diseñar una réplica académica pequeña y trazable.

## 2. Clasificación rápida

- **Área:** Inteligencia Artificial
- **Disciplina:** Computer Vision
- **Subárea:** Video Understanding / Human Action Recognition
- **Técnica principal:** Deep Learning
- **Etapa espacial:** Object Detection con YOLOv4
- **Etapa temporal:** ConvLSTM
- **Dominio:** Occupational Health & Safety
- **Sector:** industria / manufactura
- **Nicho:** detección automática de comportamientos inseguros desde video de vigilancia industrial

Una forma precisa de describirlo es:

> **Sistema de reconocimiento espacio-temporal de comportamientos inseguros mediante visión computacional para seguridad industrial.**

## 3. Idea central de Unsafe-Net

Unsafe-Net no intenta clasificar cada frame de una cámara como si fuera una fotografía independiente.

La arquitectura busca:

```text
video industrial
    ↓
YOLOv4
    ↓
detección + selección de frames relevantes
    ↓
eliminación de frames seguros/irrelevantes
    ↓
segmentación en clips con una sola acción
    ↓
ConvLSTM
    ↓
clasificación temporal de la conducta insegura
    ↓
GUI + registro
    ↓
alerta visual y sonora
```

La aportación central del paper es que **filtrar el video antes del modelo temporal reduce el tamaño efectivo de la secuencia y mejora velocidad y desempeño de clasificación**.

## 4. Índice de documentos

| Archivo | Contenido |
|---|---|
| [01_SCOPE_AND_TAXONOMY.md](01_SCOPE_AND_TAXONOMY.md) | Qué es Unsafe-Net, qué no es, categoría, nicho y alcance |
| [02_RESEARCH_LINEAGE.md](02_RESEARCH_LINEAGE.md) | Antecedentes, paper 2021, tesis, paper 2024/2025, dataset y patente |
| [03_ORIGINAL_SYSTEM_ARCHITECTURE.md](03_ORIGINAL_SYSTEM_ARCHITECTURE.md) | Arquitectura completa del sistema original |
| [04_DATASET.md](04_DATASET.md) | Dataset, cámaras, clases, splits, duraciones, licencia y estructura |
| [05_YOLOV4_STAGE.md](05_YOLOV4_STAGE.md) | Etapa YOLOv4, etiquetado, frame filtering y datos publicados |
| [06_CONVLSTM_STAGE.md](06_CONVLSTM_STAGE.md) | ConvLSTM, arquitectura, entradas y clasificación temporal |
| [07_EXPERIMENTS_AND_RESULTS.md](07_EXPERIMENTS_AND_RESULTS.md) | Métricas, resultados, tiempos y análisis del 95.81% |
| [08_DEPLOYMENT_AND_FIELD_PILOT.md](08_DEPLOYMENT_AND_FIELD_PILOT.md) | GUI, Arduino, ESP8266, alertas y piloto industrial |
| [09_LIMITATIONS_AND_OPEN_QUESTIONS.md](09_LIMITATIONS_AND_OPEN_QUESTIONS.md) | Limitaciones, inconsistencias y cabos sueltos reales |
| [10_SMALL_SCALE_REPLICATION.md](10_SMALL_SCALE_REPLICATION.md) | Plan recomendado de réplica educativa |
| [11_REQUIREMENTS_AND_STACK.md](11_REQUIREMENTS_AND_STACK.md) | Hardware, software, dependencias y estructura del repo |
| [12_EXPERIMENT_PLAN.md](12_EXPERIMENT_PLAN.md) | Experimentos, métricas, criterios de éxito y trazabilidad |
| [13_REFERENCES.md](13_REFERENCES.md) | Fuentes canónicas, enlaces y jerarquía de evidencia |
| [14_GLOSSARY.md](14_GLOSSARY.md) | Glosario técnico |

## 5. Convención de evidencia

En esta documentación se usan cuatro niveles:

- **[FUENTE PRIMARIA]**: afirmado directamente por el paper, tesis o dataset oficial.
- **[FUENTE OFICIAL]**: repositorio universitario, Mendeley, portafolio de patentes u otra publicación institucional.
- **[DERIVADO]**: material de terceros que reutiliza el dataset o la idea.
- **[RÉPLICA PROPUESTA]**: decisión nuestra para construir una versión educativa; no debe atribuirse a los autores.

Esto es importante porque **no todo lo que hoy existe alrededor del dataset pertenece a Unsafe-Net original**.

## 6. Fuentes canónicas

- Paper principal: https://link.springer.com/article/10.1007/s11042-024-19276-8
- Dataset oficial: https://data.mendeley.com/datasets/xjmtb22pff/1
- Paper del dataset: https://pmc.ncbi.nlm.nih.gov/articles/PMC11367630/
- Tesis doctoral de Oğuzhan Önal: https://acikkaynak.bilecik.edu.tr/items/a55c58c5-1408-4ac3-a052-f861f59a985e/full
- Antecedente YOLOv4 de 2021: https://dergipark.org.tr/en/pub/ejosat/article/951733

## 7. Regla de oro del proyecto

> **No rellenar con suposiciones los parámetros que los autores no publicaron.**

Una réplica académica puede adaptar componentes, pero cada adaptación debe estar explícitamente marcada como tal.
