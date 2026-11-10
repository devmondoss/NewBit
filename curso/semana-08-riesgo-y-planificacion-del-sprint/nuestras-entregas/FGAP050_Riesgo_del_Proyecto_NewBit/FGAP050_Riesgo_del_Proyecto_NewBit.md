# FGAP050 – Riesgo del Proyecto: NewBit (R-01, R-02 y R-03)

- **Archivos para entregar** (esta carpeta): `FGAP050_Riesgo_del_Proyecto_NewBit.docx` (editable) y `FGAP050_Riesgo_del_Proyecto_NewBit.pdf`: una ficha por riesgo (R-01, R-02 y R-03), una por página.
- **Formato:** el de los ejemplos del docente ([ejemplo 1](../../material-del-profe/riesgo-fgap050-ejemplo-1/riesgo-fgap050-ejemplo-1.md), [ejemplo 2](../../material-del-profe/riesgo-fgap050-ejemplo-2/riesgo-fgap050-ejemplo-2.md)); no llegó FGAP050 en blanco. Cada ficha es una página completa del formato (control de versiones, identificación, evaluación y tabla de escalas con lo elegido resaltado).
- **Generador:** `generar_fgap050.py` (usa `docx_nb.py` de la carpeta del FGAP110). PDF exportado con Pages (Word no acepta «guardar como» por AppleScript en esta Mac).
- **Fecha:** 02/11/2026 (inicio del Sprint 2) · **Versión:** 1.0 (Grupo D3).
- **Fuente de los riesgos:** sección «Riesgos generales del proyecto» del Acta (`FGAP010_Acta_Constitucion_NewBit.docx`, v2.0), la misma lista que la Tabla de riesgos del Producto de la Unidad I.

## Control de versiones
| Versión | Hecho por | Revisado por | Aprobado por | Fecha | Motivo |
|---|---|---|---|---|---|
| 1.0 | Developers (Anthony Lopez y Luis Salazar) | Anthony Lopez (Scrum Master) | Albert Chumacero (Product Owner) · **POR CONFIRMAR** | 02/11/2026 | Registro de los riesgos prioritarios al inicio del Sprint 2 |

**Código y nombre del proyecto:** PY-NB-001 – Sistema web con Visión Artificial para la detección de actos inseguros en áreas operativas de manufactura metalmecánica (NewBit)

## R-01 · Ajuste del modelo temporal (ConvLSTM)
| Campo | Contenido |
|---|---|
| **Descripción del riesgo** | El modelo ConvLSTM de NewBit podría no aprender a distinguir las conductas de la primera versión (tránsito fuera de la vía peatonal y panel eléctrico abierto, con sus casos seguros) con la longitud de secuencia, las capas y los hiperparámetros iniciales, o su ajuste podría necesitar más ciclos de entrenamiento de los que caben en los Sprints 2 y 3. Retrasaría HU07 y HU08 y comprometería el pipeline completo que exige el Acta. |
| **Causa raíz** | El equipo no ha entrenado antes un ConvLSTM y no tiene una línea base propia. La longitud de secuencia N depende de la ventana fija de HU05, que todavía no existe, y del submuestreo a 5 fps. Los datos vienen de una sola planta con dos cámaras y hay pocos ejemplos por clase (en el conjunto de prueba del artículo, 13 videos de panel abierto; Research Pack de Unsafe-Net). |
| **Trigger** | Al cerrar el *spike* de longitud de secuencia (T10, 10/11/2026), ninguna de las dos configuraciones de N supera en exactitud de validación al clasificador de la clase mayoritaria (línea base trivial), o la pérdida de validación no baja durante 5 épocas seguidas. |
| **Entregables afectados** | HU07 (Sprint 2 si se aprueba la SC-001; si no, Sprint 3) y HU08 (Sprint 3); modelo ConvLSTM entrenado y evaluado con métricas por clase (entregable clave del Acta); evaluación comparativa; HU09 y HU10, que dependen de HU08; demostración del incremento. |
| **Estimación de probabilidad** | 0,50 – Probable |
| **Estimación de impacto** | 0,80 – Muy alto |
| **Probabilidad por impacto** | 0,50 × 0,80 = **0,40** |
| **Tipo de riesgo** | **ALTO** |

## R-02 · Implementación propia del pipeline completo
| Campo | Contenido |
|---|---|
| **Descripción del riesgo** | El pipeline propio de NewBit (carga, extracción de frames, detección, descarte de frames vacíos, agrupamiento y tensor) podría tener defectos no detectados, porque la prueba integrada solo se hizo con un clip sintético y no hay revisión de pares registrada. Al probarlo con videos reales del dataset, las historias construidas podrían no cumplir sus criterios o la Definición de Terminado, y HU07 recibiría secuencias mal formadas. |
| **Causa raíz** | El código de las 7 HU de los Sprints 1 y 2 se escribió en un día (17/10/2026). El clip de prueba (`tests/fixtures`) usa la foto de muestra `zidane.jpg` de Ultralytics: muestra personas, no operarios, y no sirve como evidencia visual. No hay registro de la revisión de pares que exige el FGAP070. En macOS, un paquete `tests` de terceros tapa `proyecto-newbit/tests` y la prueba E2E no corre con el comando del README. |
| **Trigger** | La prueba integrada con un video real del dataset (T13, 12/11/2026) falla en algún paso; o, en la revisión manual de T11 (03/11; 20 frames con operario visible por video), más del 10 % queda sin caja «persona» (umbral propuesto); o al 11/11 la revisión de pares (T12) deja al menos una observación crítica sin resolver. |
| **Entregables afectados** | Incremento de los Sprints 1 y 2 (HU01–HU06 y HU11, 15 pts) y su aceptación por el PO; tensor de entrada de HU07; demostración en la revisión del Sprint 2; criterio de aprobación del Acta «reproducibilidad técnica». |
| **Estimación de probabilidad** | 0,50 – Probable |
| **Estimación de impacto** | 0,40 – Alto |
| **Probabilidad por impacto** | 0,50 × 0,40 = **0,20** |
| **Tipo de riesgo** | **MODERADO** |

## R-03 · GPU y tiempo de entrenamiento limitados
| Campo | Contenido |
|---|---|
| **Descripción del riesgo** | El entrenamiento de ConvLSTM podría no caber en el tiempo del sprint por falta de GPU propia o por las cuotas y desconexiones de Google Colab. Retrasaría HU07 y HU08 y reduciría el número de configuraciones que se pueden probar, lo que agrava R-01. |
| **Causa raíz** | La aplicación corre en CPU y no está documentado si los equipos del grupo tienen GPU NVIDIA (**POR CONFIRMAR**). El presupuesto de nube del Acta es acotado (S/ 80: 2 meses × S/ 40). Los videos y los tensores tienen que subirse a la nube antes de entrenar. |
| **Trigger** | En el *spike* T10 (10/11/2026), una época con el subconjunto de las dos conductas tarda más de 20 min (umbral propuesto: permite unas 20 épocas en una sesión), o se pierden 2 o más sesiones de Colab por cuota o desconexión en la misma semana. |
| **Entregables afectados** | HU07 y HU08; modelo ConvLSTM entrenado; comparación de tiempos de procesamiento del Acta; cronograma de los Sprints 2 y 3. |
| **Estimación de probabilidad** | 0,50 – Probable |
| **Estimación de impacto** | 0,40 – Alto |
| **Probabilidad por impacto** | 0,50 × 0,40 = **0,20** |
| **Tipo de riesgo** | **MODERADO** |

## Tabla de escalas (del docente)
| Probabilidad | Valor | Impacto | Valor | Tipo de riesgo | P × I |
|---|---|---|---|---|---|
| Muy improbable | 0,1 | Muy bajo | 0,05 | Muy alto | Mayor a 0,50 |
| Relativamente probable | 0,3 | Bajo | 0,10 | Alto | Menor a 0,50 |
| Probable | 0,5 | Moderado | 0,20 | Moderado | Menor a 0,30 |
| Muy probable | 0,7 | Alto | 0,40 | Bajo | Menor a 0,10 |
| Casi certeza | 0,9 | Muy alto | 0,80 | Muy bajo | Menor a 0,05 |

En cada ficha del Word se resaltan la probabilidad, el impacto y el tipo elegidos, como en el ejemplo del docente.

## Notas de trabajo (no van en el formato)

### Sustento de las estimaciones y respuesta prevista
| Riesgo | Sustento de P e I | Respuesta prevista (tareas de la EDT del Sprint 2) |
|---|---|---|
| R-01 | **P = 0,50 (probable):** primer ConvLSTM del equipo y sin línea base; el dataset es público y el artículo muestra que la tarea es abordable. **I = 0,80 (muy alto):** sin modelo temporal no hay pipeline completo ni métricas, que son criterios de aprobación del Acta. | **Mitigar.** Registro versionado de cada configuración y *spike* de dos valores de N (T10, 3 h, EDT FGAP110). Adelantar HU07 al Sprint 2 (SC-001, FGAP090) para que el Sprint 3 tenga holgura para un segundo ciclo de ajuste. **Plan B del Acta:** cierre con alcance reducido a una conducta, con su evaluación documentada. Dueño del riesgo: Product Owner; ejecutan: Developers; vigila: Scrum Master (Daily y retrospectiva). |
| R-02 | **P = 0,50 (probable):** nunca se probó con videos reales ni se revisó entre pares, aunque las 43 pruebas automatizadas pasan (20/10). **I = 0,40 (alto):** obliga a retrabajo dentro del sprint y retrasa la aceptación de 15 pts, pero no cambia el alcance. | **Mitigar (Acta: bibliotecas abiertas y revisión por pares).** T11: pipeline espacial con 5 videos del dataset (3 h). T12: revisión de pares registrada con la lista del FGAP070 (4 h). T13: prueba E2E con video real y corrección del import en macOS (3 h). Dueño: Product Owner; ejecutan: Developers; el Scrum Master registra el resultado de la revisión de pares. |
| R-03 | **P = 0,50 (probable):** depende de un servicio externo con cuotas y de hardware no confirmado. **I = 0,40 (alto):** retrasa el modelo temporal, pero hay alternativas (bajar resolución o N, menos épocas). | **Mitigar.** T14: entorno de entrenamiento en Colab con dependencias fijadas y checkpoint por época, para reanudar tras una desconexión (2 h). Medición del tiempo por época en T10. **Plan B:** reducir la resolución de entrada o N y entrenar solo con las dos conductas de la primera versión (Acta). Dueño: Product Owner; ejecuta: Luis Salazar. |

### Priorización de los 7 riesgos del Acta al 02/11/2026
Se hizo ficha de los riesgos con P × I ≥ 0,20 que necesitan tareas en el Sprint 2 (Guía del SBOK: backlog priorizado ajustado al riesgo).

| Código | Riesgo (Acta) | P | I | P × I | Tipo | Situación al 02/11/2026 | Tratamiento en el Sprint 2 |
|---|---|:-:|:-:|:-:|---|---|---|
| **R-01** | Ajuste del modelo temporal (longitud de secuencia, capas, hiperparámetros) | 0,50 | 0,80 | **0,40** | Alto | HU07 entra al Sprint 2 si se aprueba la SC-001; no hay línea base propia | Ficha y tarea T10 |
| **R-02** | Implementación propia del pipeline completo | 0,50 | 0,40 | **0,20** | Moderado | Prueba integrada solo con clip sintético; sin revisión de pares registrada | Ficha y tareas T11–T13 |
| **R-03** | GPU y tiempo de entrenamiento limitados | 0,50 | 0,40 | **0,20** | Moderado | El entrenamiento de ConvLSTM empieza en el Sprint 2; GPU local sin confirmar | Ficha y tarea T14 (medición en T10) |
| R-04 | Etiquetado de frames más lento de lo previsto | 0,30 | 0,20 | 0,06 | Bajo | En el Sprint 2 no se anotan frames a mano: se usa YOLOv8n preentrenado (clase «persona») | Se vigila; sin tareas |
| R-05 | Espacio en disco (30–50 GB entre videos, frames y checkpoints) | 0,30 | 0,20 | 0,06 | Bajo | Los tensores del split y los checkpoints empiezan a generarse en el Sprint 2 | Se vigila; checkpoints fuera de git |
| R-06 | Cambio de entorno: una planta y dos cámaras | 0,30 | 0,10 | 0,03 | Muy bajo | La adaptación a otras plantas está fuera del alcance de esta versión | Se acepta |
| R-07 | Equipo de tres; el Scrum Master también es Developer | 0,50 | 0,20 | 0,10 | Moderado | Anthony tiene 17 h de tareas en el Sprint 2 además de su rol de Scrum Master | Se vigila en cada Daily; *time-boxing* |

### Notas
- Los riesgos en negrita son los que tienen ficha (R-01, R-02 y R-03). Sus tareas de respuesta están en la EDT del Sprint 2 (FGAP110) y en el cronograma (FGAP130).
- La numeración R-01 a R-07 se asigna en este documento según el orden del Acta; el Acta no los numeraba.
- Los umbrales de los triggers (20 min por época, 10 % de frames sin detección) son **propuestas** del equipo: no hay métricas propias demostradas todavía.
- Según la Guía del SBOK, el Product Owner es el dueño de los riesgos y los Developers implementan las respuestas durante el sprint; el Scrum Master los vigila y los comunica. Los riesgos se reevalúan en cada planificación y retrospectiva.
- Aprobación del Product Owner de esta evaluación: **POR CONFIRMAR**.
- **Diferencia con el `.md` del Acta:** su resumen nombra los riesgos de otra forma («reproducibilidad de pesos», «iluminación y oclusiones», «transferibilidad de dominio»). Aquí se usa la lista del `.docx` del Acta (lo que se entregó), que coincide con el Producto de la Unidad I. Conviene corregir el resumen del `.md` del Acta.

## POR CONFIRMAR
1. **Aprobación del Product Owner** de las fichas y de la priorización.
2. **GPU NVIDIA en los equipos del grupo** (causa raíz de R-03).
3. Los umbrales de los triggers son propuestas; el PO puede ajustarlos en la planificación.
