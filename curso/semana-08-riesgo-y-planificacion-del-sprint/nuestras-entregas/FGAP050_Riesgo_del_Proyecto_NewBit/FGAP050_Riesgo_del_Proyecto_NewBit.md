# FGAP050 – Riesgo del Proyecto: NewBit (v1.1, 9 riesgos)

- **Archivos para entregar** (esta carpeta): `FGAP050_Riesgo_del_Proyecto_NewBit.docx` (editable) y `FGAP050_Riesgo_del_Proyecto_NewBit.pdf` (11 páginas).
- **Qué cumple:** la **actividad calificada de la semana 8** (lámina 39 de la [clase de riesgo en Scrum](../../material-del-profe/riesgo-en-scrum-diapositivas/riesgo-en-scrum-diapositivas.md)): 9 riesgos concretos (3 técnicos, 4 de datos y 2 de gestión), escala explícita y exposición P × I, priorización con vínculo al backlog, respuesta (mitigación, responsable, fecha, trigger y evidencia de control) y guion de 3 minutos del riesgo más crítico (R-01).
- **Estructura del PDF:** pág. 1 criterios de evaluación, regla de priorización y matriz P × I · pág. 2 priorización y vínculo con las historias de usuario (HU01–HU12) · págs. 3–10 una ficha por riesgo (R-01, R-02, R-03, R-04, R-06, R-07, R-08 y R-09) · pág. 11 guion de 3 minutos. R-05 (bajo) no tiene ficha: se acepta y se vigila.
- **Formato:** el de los ejemplos del docente ([ejemplo 1](../../material-del-profe/riesgo-fgap050-ejemplo-1/riesgo-fgap050-ejemplo-1.md), [ejemplo 2](../../material-del-profe/riesgo-fgap050-ejemplo-2/riesgo-fgap050-ejemplo-2.md)). Cada ficha conserva control de versiones, identificación y evaluación con la escala del formato (en una tira por fila, con el nivel elegido resaltado) y agrega «Respuesta al riesgo».
- **Generador:** `generar_fgap050.py` (usa `docx_nb.py` de la carpeta del FGAP110). PDF exportado con Pages (Word no acepta «guardar como» por AppleScript en esta Mac).
- **Fecha:** 09/11/2026 · **Versión:** 1.1 (Grupo D3). La v1.0 (02/11/2026) tenía 3 fichas (R-01 a R-03).

## Control de versiones
| Versión | Hecho por | Revisado por | Aprobado por | Fecha | Motivo |
|---|---|---|---|---|---|
| 1.0 | Developers (Anthony Lopez y Luis Salazar) | Anthony Lopez (Scrum Master) | Albert Chumacero (Product Owner) | 02/11/2026 | Registro de los riesgos prioritarios al inicio del Sprint 2 |
| 1.1 | Developers (Anthony Lopez y Luis Salazar) | Anthony Lopez (Scrum Master) | Albert Chumacero (Product Owner) | 09/11/2026 | Se amplía a 9 riesgos y se agrega priorización, respuesta y comunicación (actividad de la semana 8) |

**Código y nombre del proyecto:** PY-NB-001 – Sistema web con Visión Artificial para la detección de actos inseguros en áreas operativas de manufactura metalmecánica (NewBit)

## Criterios de evaluación
Escala numérica del formato del docente; el criterio de cada nivel lo fija el equipo para NewBit.

| Probabilidad | Valor | Cuándo se elige en NewBit | Impacto | Valor | Cuándo se elige en NewBit | Tipo de riesgo | P × I |
|---|:-:|---|---|:-:|---|---|---|
| Muy improbable | 0,1 | No hay indicios en NewBit ni en proyectos parecidos. | Muy bajo | 0,05 | No afecta historias, fechas ni criterios del Acta. | Muy alto | Mayor a 0,50 |
| Relativamente probable | 0,3 | Pasa en proyectos parecidos, pero en NewBit la causa raíz no está presente todavía. | Bajo | 0,10 | Retrabajo menor dentro de una tarea, sin mover fechas. | Alto | Menor a 0,50 |
| Probable | 0,5 | La causa raíz está presente en NewBit, sin señales de que el riesgo ya empezó. | Moderado | 0,20 | Retrasa una tarea o una HU, pero el sprint se cumple. | Moderado | Menor a 0,30 |
| Muy probable | 0,7 | La causa raíz está presente y ya hay una señal parcial en el proyecto. | Alto | 0,40 | Una HU no cumple la DoD en su sprint (arrastre) o un criterio del Acta se cumple solo en parte. | Bajo | Menor a 0,10 |
| Casi certeza | 0,9 | El trigger está a punto de cumplirse. | Muy alto | 0,80 | Pone en riesgo un entregable clave del Acta (pipeline completo, modelo con métricas) o el lanzamiento. | Muy bajo | Menor a 0,05 |

**Regla de priorización y respuesta**
- **P × I ≥ 0,20 → acción en el backlog:** tarea en el Sprint Backlog o criterio de aceptación nuevo en una HU, con responsable y fecha. Aplica a R-01, R-08, R-02, R-04 y R-03.
- **0,10 ≤ P × I < 0,20 → mitigar dentro de lo planificado:** tareas o eventos Scrum ya previstos, sin ítem nuevo; se vigila en la Daily. Aplica a R-07, R-06 y R-09.
- **P × I < 0,10 → aceptar y vigilar:** R-05.
- Exposición = P × I, de mayor a menor; en un empate va primero la fecha de control más cercana. El PO es el dueño de los riesgos; el responsable de cada ficha ejecuta la respuesta; el Scrum Master vigila los triggers en la Daily y actualiza el registro (Guía del SBOK, cap. 7).

## Matriz de exposición P × I
| Probabilidad \ Impacto | Muy bajo (0,05) | Bajo (0,10) | Moderado (0,20) | Alto (0,40) | Muy alto (0,80) |
|---|:-:|:-:|:-:|:-:|:-:|
| Casi certeza (0,9) | 0,045 | 0,09 | 0,18 | 0,36 | 0,72 |
| Muy probable (0,7) | 0,035 | 0,07 | 0,14 **R-07** | 0,28 | 0,56 |
| Probable (0,5) | 0,025 | 0,05 | 0,10 **R-09** | 0,20 **R-02 · R-03 · R-04** | 0,40 **R-01** |
| Relativamente probable (0,3) | 0,015 | 0,03 | 0,06 **R-05** | 0,12 **R-06** | 0,24 **R-08** |
| Muy improbable (0,1) | 0,005 | 0,01 | 0,02 | 0,04 | 0,08 |

## Priorización y vínculo con el backlog
| N.º | Código | Riesgo | Categoría | P | I | P × I | Tipo | Respuesta | Acción en el backlog (HU / tarea) | Responsable | Fecha de control |
|:-:|---|---|---|:-:|:-:|:-:|---|---|---|---|---|
| 1 | **R-01** | Ajuste del modelo temporal (ConvLSTM) | Técnico | 0,50 | 0,80 | **0,40** | Alto | Mitigar | **Sí:** 3.05, 3.06 y 3.08 (HU07); regla de corte | Luis Salazar (Developer, datos y modelos). Dueño del riesgo: Albert Chumacero (PO). | 19/11/2026 (*spike*) · 24/11/2026 (control final y decisión del plan B) |
| 2 | **R-08** | Privacidad de los videos de operarios | Datos | 0,30 | 0,80 | **0,24** | Moderado | Mitigar y evitar | **Sí:** Criterio nuevo en HU10 (4.04); tarea nueva de acceso; DoD | Anthony Lopez (Developer, web e integración). | 13/11/2026 (primera verificación) · 04/12/2026 (HU10) · 14/12/2026 (demostración) |
| 3 | **R-02** | Implementación propia del pipeline completo | Técnico | 0,50 | 0,40 | **0,20** | Moderado | Mitigar | **Sí:** T11, T12 y T13 (Sprint 2) | Anthony Lopez (Developer, integración y pruebas); T11 la ejecuta Luis Salazar. | 12/11/2026 (T13) · control en la revisión del Sprint 2 (13/11/2026) |
| 4 | **R-04** | Desbalance de clases y etiquetas de los clips | Datos | 0,50 | 0,40 | **0,20** | Moderado | Mitigar | **Sí:** Criterio nuevo en HU05 (3.04); 3.06 y 3.10 | Luis Salazar (Developer, datos y modelos). | 18/11/2026 (conteo de clips) · 25/11/2026 (métricas por clase) |
| 5 | **R-03** | GPU y tiempo de entrenamiento limitados | Técnico | 0,50 | 0,40 | **0,20** | Moderado | Mitigar | **Sí:** T14 (Sprint 2); 3.05 y 3.06 (HU07) | Luis Salazar (Developer, datos y modelos). | 19/11/2026 (medición del tiempo por época) · 23/11/2026 (fin del entrenamiento base) |
| 6 | **R-07** | Capacidad del equipo: Scrum Master con doble rol | Gestión | 0,70 | 0,20 | **0,14** | Moderado | Mitigar | No es ítem nuevo: planificación del Sprint 3 | Anthony Lopez (Scrum Master). | 16/11/2026 (planificación del Sprint 3) y en cada Daily |
| 7 | **R-06** | Iluminación, oclusiones y cambio de dominio | Datos | 0,30 | 0,40 | **0,12** | Moderado | Mitigar con trabajo ya planificado | No es ítem nuevo: T05, T01 y 3.08 | Luis Salazar (Developer, datos y modelos); la calibración de T05 y T01 la ejecuta Anthony Lopez. | 09/11/2026 (T01) · 24/11/2026 (métricas por cámara) |
| 8 | **R-09** | Decisiones y aceptación del Product Owner a destiempo | Gestión | 0,50 | 0,20 | **0,10** | Moderado | Mitigar | No es ítem nuevo: revisión y planificación | Albert Chumacero (Product Owner); el Scrum Master agenda y registra. | 13/11/2026 (revisión del Sprint 2) |
| 9 | **R-05** | Espacio en disco (30–50 GB entre videos, frames y checkpoints) | Datos | 0,30 | 0,20 | **0,06** | Bajo | Aceptar y vigilar | No: se acepta y se vigila | Luis Salazar. | En cada revisión de sprint (13/11 y 27/11/2026) |

**Por qué van al backlog:** los cinco riesgos con P × I ≥ 0,20 afectan historias que todavía no se aceptan (HU05, HU07, HU08 y HU10) o la aceptación de las ya construidas (HU01–HU06 y HU11). Si la respuesta no se vuelve tarea o criterio de aceptación con fecha, no entra en la capacidad del sprint ni se verifica en la revisión.

## Vínculo con las historias de usuario
Riesgos en orden de prioridad; en negrita los que generan acción en el backlog (P × I ≥ 0,20).

| HU | Historia de usuario | Sprint | Riesgos que la afectan | Respuesta que recibe la historia |
|---|---|---|---|---|
| HU01 | Cargar video (.mp4/.avi) | 1 | **R-08** · **R-02** · R-09 | Cierre con T11 y T12 (R-02) y aceptación formal el 13/11 (R-09); medios fuera de git (R-08). |
| HU02 | Extraer frames | 1 | **R-08** · **R-02** · R-09 | Cierre con T11 y T12 (R-02) y aceptación formal el 13/11 (R-09). |
| HU03 | Detectar operarios (YOLOv8) | 1 | **R-08** · **R-02** · R-06 · R-09 | Revisión manual de la detección en T11 (R-02, R-06); aceptación formal el 13/11 (R-09). |
| HU04 | Descartar frames vacíos | 2 | **R-02** · R-06 · R-09 | Evidencia con videos reales en T01: frames con operario que se pierden (R-02, R-06). |
| HU05 | Agrupar en clips | 2 (cierre en 3) | **R-02** · **R-04** · R-07 · R-09 | Criterio de aceptación nuevo: conteo de clips por clase y split, tarea 3.04 (R-04). |
| HU06 | Descartar clips cortos | 2 | **R-02** · **R-04** · R-09 | Duración mínima alineada con N (T04) sin vaciar la clase menor; ventanas con solapamiento (R-04). |
| HU07 | Procesar con ConvLSTM | 3 | **R-01** · **R-02** · **R-04** · **R-03** · R-07 | 3.05 *spike* de N, 3.06 entrenamiento con checkpoint y pesos por clase, 3.08 métricas por clase y por cámara (R-01, R-03, R-04, R-06). |
| HU08 | Clasificar y tipificar la conducta | 3 | **R-01** · **R-04** · **R-03** · R-07 · R-06 | 3.10 matriz de confusión y F1 por conducta (R-04); alcance mínimo acordado (R-07); plan B a una conducta (R-01). |
| HU09 | Ver video con recuadro de riesgo | 4 | **R-01** · **R-08** · R-07 | Depende de HU08 (R-01); reproducción solo en 127.0.0.1 o con autenticación (R-08). |
| HU10 | Alerta de riesgo con evidencia | 4 | **R-01** · **R-08** · R-07 | Criterio de aceptación nuevo: captura con rostros difuminados y datos mínimos, tarea 4.04 (R-08). |
| HU11 | Calibrar umbral de confianza | 2 | **R-02** · R-06 · R-09 | T05 con video real y umbral por cámara (R-06). |
| HU12 | Ver log de tiempos de procesamiento | 4 | **R-03** · R-07 | Tiempo por época y por etapa en el registro de experimentos (R-03). |

## Fichas

### R-01 · Ajuste del modelo temporal (ConvLSTM) (Técnico · prioridad 1 de 9)
| Campo | Contenido |
|---|---|
| **Descripción del riesgo** | El modelo ConvLSTM de NewBit podría no aprender a distinguir las conductas de la primera versión (tránsito fuera de la vía peatonal y panel eléctrico abierto, con sus casos seguros) con la longitud de secuencia, las capas y los hiperparámetros iniciales, o su ajuste podría necesitar más ciclos de entrenamiento de los que caben en el Sprint 3 (16–27/11). Retrasaría HU07 y HU08 y comprometería el pipeline completo que exige el Acta. |
| **Causa raíz** | El equipo no ha entrenado antes un ConvLSTM y no tiene una línea base propia. La longitud de secuencia N depende de la ventana fija de HU05, que al 09/11 no está implementada, y del submuestreo a 5 fps. Los datos vienen de una sola planta con dos cámaras y hay pocos ejemplos por clase (13 videos de panel abierto en el split de prueba). El PO rechazó adelantar HU07 al Sprint 2 (SC-001, FGAP090): se entrena recién en el Sprint 3. |
| **Trigger** | Al cerrar el *spike* de longitud de secuencia (tarea 3.05, 19/11/2026), ninguna de las dos configuraciones de N supera en F1 macro de validación a la línea base trivial (clase mayoritaria), o la pérdida de validación no baja durante 5 épocas seguidas en el entrenamiento base (3.06). Activa el plan B: en la inferencia de prueba (3.08, 24/11) una conducta insegura queda con F1 menor a 0,50. |
| **Entregables afectados (HU)** | **HU07** (Sprint 3) y **HU08** (Sprint 3); modelo ConvLSTM entrenado y evaluado con métricas por clase (entregable clave del Acta); evaluación comparativa; **HU09** y **HU10**, que dependen de HU08; demostración del incremento. |
| **Probabilidad × impacto** | 0,50 (Probable) × 0,80 (Muy alto) = **0,40** → **ALTO** |
| **Sustento** | **P = 0,50 (probable):** la causa raíz está presente (primer ConvLSTM del equipo, sin línea base), pero el dataset es público y el artículo muestra que la tarea es abordable. **I = 0,80 (muy alto):** sin modelo temporal no hay pipeline completo ni métricas, criterios de aprobación del Acta. |
| **Estrategia y mitigación** | **Mitigar.** *Spike* con dos valores de N y registro versionado de cada configuración (semilla fija); entrenamiento base con checkpoint por época; métricas por clase desde el primer entrenamiento. **Plan B del Acta:** si se activa el trigger del 24/11, el PO reduce el alcance a una conducta y se entrega con su evaluación documentada, sin bajar la DoD. |
| **Acción en el backlog** | **Sí (HU07, Sprint 3):** tareas 3.05 *spike* de N (19/11), 3.06 entrenamiento base en Colab (20–23/11) y 3.08 inferencia y métricas por clase (24/11). Regla de corte del plan B registrada para la decisión del PO (24/11). |
| **Responsable** | Luis Salazar (Developer, datos y modelos). Dueño del riesgo: Albert Chumacero (PO). |
| **Fecha** | 19/11/2026 (*spike*) · 24/11/2026 (control final y decisión del plan B) |
| **Evidencia de control** | Registro versionado de experimentos (configuración, semilla, N, F1 macro y pérdida por época); métricas por clase del 24/11; acta de la decisión del PO si se aplica el plan B. |

### R-02 · Implementación propia del pipeline completo (Técnico · prioridad 3 de 9)
| Campo | Contenido |
|---|---|
| **Descripción del riesgo** | El pipeline propio de NewBit (carga, extracción de frames, detección, descarte de frames vacíos, agrupamiento y tensor) podría tener defectos no detectados, porque la prueba integrada solo se hizo con un clip sintético y no hay revisión de pares registrada. Al probarlo con videos reales del dataset, las historias construidas podrían no cumplir sus criterios o la Definición de Terminado, y HU07 recibiría secuencias mal formadas. |
| **Causa raíz** | El código de las 7 HU de los Sprints 1 y 2 se escribió en un día (17/10/2026). El clip de prueba (`tests/fixtures`) usa la foto de muestra `zidane.jpg` de Ultralytics: muestra personas, no operarios, y no sirve como evidencia visual. No hay registro de la revisión de pares que exige el FGAP070. En macOS, un paquete `tests` de terceros tapa `proyecto-newbit/tests` y la prueba E2E no corre con el comando del README. |
| **Trigger** | La prueba integrada con un video real del dataset (T13, 12/11/2026) falla en algún paso; o, en la revisión manual de T11 (20 frames con operario visible por video), más del 10 % queda sin caja «persona»; o al 11/11 la revisión de pares (T12) deja al menos una observación crítica sin resolver. |
| **Entregables afectados (HU)** | Incremento de los Sprints 1 y 2 (**HU01–HU06** y **HU11**, 15 PH) y su aceptación por el PO; tensor de entrada de **HU07**; demostración en la revisión del Sprint 2; criterio de aprobación del Acta «reproducibilidad técnica». |
| **Probabilidad × impacto** | 0,50 (Probable) × 0,40 (Alto) = **0,20** → **MODERADO** |
| **Sustento** | **P = 0,50 (probable):** nunca se probó con videos reales ni se revisó entre pares, aunque las 43 pruebas automatizadas pasan (20/10). **I = 0,40 (alto):** obliga a retrabajo y puede dejar una HU sin cumplir la DoD en su sprint, pero no cambia el alcance. |
| **Estrategia y mitigación** | **Mitigar** (Acta: bibliotecas abiertas y revisión por pares). Probar el pipeline espacial con 5 videos reales y revisar a mano la detección; revisión de pares cruzada con la lista del FGAP070; prueba E2E con un video real y corrección del conflicto del paquete `tests` en macOS. |
| **Acción en el backlog** | **Sí (Sprint 2, nodo R-02 de la EDT):** T11 pipeline espacial con 5 videos reales (03/11), T12 revisión de pares registrada (10–11/11) y T13 prueba E2E con video real (12/11). Cubren también el cierre de HU01–HU03. |
| **Responsable** | Anthony Lopez (Developer, integración y pruebas); T11 la ejecuta Luis Salazar. |
| **Fecha** | 12/11/2026 (T13) · control en la revisión del Sprint 2 (13/11/2026) |
| **Evidencia de control** | Tabla de la revisión manual de T11 (frames con operario y cajas detectadas por video); registro de la revisión de pares con la lista del FGAP070; salida de `pytest` con la suite completa y el video real. |

### R-03 · GPU y tiempo de entrenamiento limitados (Técnico · prioridad 5 de 9)
| Campo | Contenido |
|---|---|
| **Descripción del riesgo** | El entrenamiento de ConvLSTM podría no caber en el tiempo del sprint por falta de GPU propia o por las cuotas y desconexiones de Google Colab. Retrasaría HU07 y HU08 y reduciría el número de configuraciones que se pueden probar, lo que agrava R-01. |
| **Causa raíz** | La aplicación corre en CPU y el equipo no tiene GPU NVIDIA propia para entrenar: la Mac del Scrum Master no admite CUDA y no hay otra GPU registrada en el proyecto, así que se entrena en Google Colab. El presupuesto de nube del Acta es acotado (S/ 80: 2 meses × S/ 40). Los videos y los tensores tienen que subirse a la nube antes de entrenar. |
| **Trigger** | En el *spike* (3.05, 19/11/2026), una época con el subconjunto de las dos conductas tarda más de 20 min (con eso caben unas 20 épocas en una sesión), o se pierden 2 o más sesiones de Colab por cuota o desconexión en la misma semana. |
| **Entregables afectados (HU)** | **HU07** y **HU08**; modelo ConvLSTM entrenado; comparación de tiempos de procesamiento del Acta (**HU12**); cronograma del Sprint 3. |
| **Probabilidad × impacto** | 0,50 (Probable) × 0,40 (Alto) = **0,20** → **MODERADO** |
| **Sustento** | **P = 0,50 (probable):** depende de un servicio externo con cuotas y no hay GPU propia. **I = 0,40 (alto):** retrasa el modelo temporal y puede dejar HU07 sin terminar en el Sprint 3, pero hay alternativas (bajar resolución o N, menos épocas). |
| **Estrategia y mitigación** | **Mitigar.** Entorno de entrenamiento en Colab con dependencias fijadas y checkpoint por época, para reanudar tras una desconexión; medir el tiempo por época en el *spike*. **Plan B:** bajar la resolución de entrada o N y entrenar solo con las dos conductas de la primera versión (Acta); si hace falta, usar el presupuesto de nube del Acta. |
| **Acción en el backlog** | **Sí:** T14 entorno de entrenamiento en Colab (Sprint 2, 02/11) y, en HU07 (Sprint 3), medición del tiempo por época en 3.05 (19/11) y checkpoint por época en 3.06 (20–23/11). |
| **Responsable** | Luis Salazar (Developer, datos y modelos). |
| **Fecha** | 19/11/2026 (medición del tiempo por época) · 23/11/2026 (fin del entrenamiento base) |
| **Evidencia de control** | Cuaderno de Colab versionado con las dependencias fijadas; checkpoints por época en la carpeta privada del equipo; tiempo por época en el registro de experimentos. |

### R-04 · Desbalance de clases y etiquetas de los clips (Datos · prioridad 4 de 9)
| Campo | Contenido |
|---|---|
| **Descripción del riesgo** | Las clases del dataset están desbalanceadas y sus etiquetas son por video. Al cortar cada video en ventanas de N frames (HU05) y descartar las cortas (HU06), algunas clases seguras podrían quedarse con muy pocos clips, y algunas ventanas heredarían una etiqueta que no muestran (clips con más de una conducta). El modelo podría responder casi siempre la conducta mayoritaria y las métricas por clase de HU08 no serían válidas. |
| **Causa raíz** | En el split oficial de entrenamiento hay 178 videos de tránsito fuera de la vía frente a 50 de tránsito seguro, y 129 de panel abierto frente a 19 de panel cerrado (6,8 a 1). Los clips de panel cerrado duran 4,6 s en promedio (mínimo 1 s), cerca del umbral mínimo de HU06. El dataset etiqueta por video y su artículo advierte que algunos clips tienen más de una conducta. NewBit no reetiqueta frames a mano. |
| **Trigger** | Al generar los clips del split oficial con la N elegida (3.04, 18/11/2026), una clase queda con menos de 15 clips de entrenamiento o la razón entre la clase mayor y la menor de una misma conducta supera 10 a 1; o, en una muestra de 20 ventanas por clase, más del 20 % no muestra la conducta de su etiqueta. |
| **Entregables afectados (HU)** | **HU05** (ventana y tensor), **HU06** (duración mínima), **HU07** (entrenamiento) y **HU08** (métricas por clase y matriz de confusión); requisitos del Acta «split oficial de validación» y «métricas por clase». |
| **Probabilidad × impacto** | 0,50 (Probable) × 0,40 (Alto) = **0,20** → **MODERADO** |
| **Sustento** | **P = 0,50 (probable):** el desbalance ya está en el dataset (causa raíz presente), pero todavía no se sabe cuántos clips deja la ventana N. **I = 0,40 (alto):** un modelo sesgado obliga a reentrenar y deja HU08 sin métricas válidas en su sprint. |
| **Estrategia y mitigación** | **Mitigar.** Contar los clips por clase y por split antes de entrenar; ponderar la pérdida por clase (o sobremuestrear la clase menor) solo en entrenamiento, sin tocar el split de prueba; ventanas con solapamiento (paso menor que N) en los videos cortos; revisar a mano 20 ventanas por clase; reportar F1 macro y por clase, no solo exactitud. |
| **Acción en el backlog** | **Sí:** criterio de aceptación nuevo en **HU05** (conteo de clips por clase y split, tarea 3.04, 18/11); pesos por clase en 3.06 (**HU07**); matriz de confusión y F1 por conducta en 3.10 (**HU08**, 25/11). |
| **Responsable** | Luis Salazar (Developer, datos y modelos). |
| **Fecha** | 18/11/2026 (conteo de clips) · 25/11/2026 (métricas por clase) |
| **Evidencia de control** | Tabla de clips por clase y split en el registro de experimentos; muestra revisada de 20 ventanas por clase; matriz de confusión y F1 por clase en el informe de HU08. |

### R-05 · Espacio en disco (30–50 GB entre videos, frames y checkpoints) (Datos · prioridad 9 de 9) — sin ficha en el PDF
| Campo | Contenido |
|---|---|
| **Trigger** | Quedan menos de 10 GB libres en el equipo que procesa los videos. |
| **Probabilidad × impacto** | 0,30 (Relativamente probable) × 0,20 (Moderado) = **0,06** → **BAJO** |
| **Sustento** | **P = 0,30:** los tensores y los checkpoints empiezan a generarse en el Sprint 3. **I = 0,20:** retrasa una tarea; se resuelve borrando frames intermedios. |
| **Estrategia y mitigación** | **Aceptar y vigilar.** Checkpoints, tensores y medios fuera de git (`.gitignore` ya los excluye); borrar los frames intermedios después de generar los tensores. |
| **Acción en el backlog** | No (riesgo bajo). |
| **Responsable** | Luis Salazar. |
| **Fecha** | En cada revisión de sprint (13/11 y 27/11/2026) |
| **Evidencia de control** | Espacio libre anotado en la revisión del sprint. |

### R-06 · Iluminación, oclusiones y cambio de dominio (Datos · prioridad 7 de 9)
| Campo | Contenido |
|---|---|
| **Descripción del riesgo** | YOLOv8n preentrenado podría no detectar a operarios con poca luz, a contraluz, lejos de la cámara o tapados por máquinas. HU04 descartaría esos frames como vacíos y se perdería justo el tramo con la conducta (falso negativo). Además, el modelo se entrena con una sola planta y dos cámaras: con otra cámara u otra iluminación podría rendir peor. |
| **Causa raíz** | El detector no se reentrenó con imágenes del taller (no hay anotaciones propias). El dataset viene de una sola fábrica con dos cámaras fijas (1920 × 1080, 24 fps) y los frames se reducen a 640 × 640, lo que achica a los operarios lejanos. Hay un solo umbral de confianza para todas las cámaras. |
| **Trigger** | En la evidencia con 5 videos reales (T01, 09/11/2026), un video pierde más del 20 % de los frames con operario visible; o, en las métricas de prueba (3.08, 24/11), el recall de la clase insegura en una cámara es 0,15 o más menor que en la otra. |
| **Entregables afectados (HU)** | **HU03** (detección), **HU04** (descarte de frames), **HU11** (calibración del umbral) y **HU08** (métricas); criterio del Acta «reducción de frames ≥ 60 %» sin perder la conducta. |
| **Probabilidad × impacto** | 0,30 (Relativamente probable) × 0,40 (Alto) = **0,12** → **MODERADO** |
| **Sustento** | **P = 0,30 (relativamente probable):** pasa en proyectos parecidos y el dataset declara pocas cámaras, pero las cámaras de prueba son las mismas del entrenamiento. **I = 0,40 (alto):** los falsos negativos atacan el valor central del producto y obligan a recalibrar. |
| **Estrategia y mitigación** | **Mitigar con trabajo ya planificado.** Calibrar el umbral de confianza por cámara con HU11; medir en T01 los frames con operario visible que se descartan; reportar las métricas por cámara. **Aceptar** la generalización a otras plantas: está fuera del alcance de esta versión y se declara en el informe. |
| **Acción en el backlog** | **Dentro de tareas ya planificadas:** T05 y T01 (Sprint 2) y desglose por cámara en 3.08 (HU07, 24/11). No se crea una HU nueva. |
| **Responsable** | Luis Salazar (Developer, datos y modelos); la calibración de T05 y T01 la ejecuta Anthony Lopez. |
| **Fecha** | 09/11/2026 (T01) · 24/11/2026 (métricas por cámara) |
| **Evidencia de control** | Tabla de frames con operario visible frente a frames conservados por video (T01); bitácora de calibración de HU11 con el umbral de cada cámara; métricas por cámara en el informe. |

### R-07 · Capacidad del equipo: Scrum Master con doble rol (Gestión · prioridad 6 de 9)
| Campo | Contenido |
|---|---|
| **Descripción del riesgo** | El equipo tiene tres personas y solo dos desarrollan. Anthony es Scrum Master y Developer: si sus tareas de desarrollo se atrasan, podría descuidar la facilitación (Daily, impedimentos, registro de riesgos), o al revés. El Sprint 3 concentra el cierre de HU05, HU07 y HU08, el tramo más incierto del proyecto. |
| **Causa raíz** | Capacidad neta por sprint de 49,5 h: Luis 28,5 h y Anthony 21 h, después de 7,5 h de Scrum Master y 6,5 h de eventos. El plan del Sprint 3 usa 46 h (93 %) y compromete 11 PH frente a una velocidad objetivo de 8 PH. El Product Owner no desarrolla. |
| **Trigger** | En la Daily, una tarea del Sprint 3 pasa 2 días hábiles sin avance, o la curva real del burndown queda 2 días seguidos más de 20 % por encima de la ideal; o en una semana no se registran las Daily o la actualización de este registro. |
| **Entregables afectados (HU)** | Sprint 3 (**HU05**, **HU07** y **HU08**) y su revisión del 27/11; Sprint 4 (**HU09**, **HU10** y **HU12**); burndown y FGAP050 al día. |
| **Probabilidad × impacto** | 0,70 (Muy probable) × 0,20 (Moderado) = **0,14** → **MODERADO** |
| **Sustento** | **P = 0,70 (muy probable):** la causa raíz está presente y ya hay una señal: el Sprint 3 está planificado al 93 % de la capacidad. **I = 0,20 (moderado):** retrasa tareas, pero el PO puede reordenar el alcance del sprint sin tocar el Acta. |
| **Estrategia y mitigación** | **Mitigar.** *Time-boxing* del trabajo de Scrum Master (7,5 h por sprint, ya descontadas); reparto fijo: Luis lidera datos y modelos, Anthony web, integración y pruebas; en la planificación del Sprint 3 el PO ordena el trabajo (cierre de HU05 y HU07 primero) y acuerda un alcance mínimo de HU08; se recalcula la capacidad con la velocidad real del Sprint 2. |
| **Acción en el backlog** | **Dentro de los eventos Scrum:** orden del Sprint Backlog y alcance mínimo de HU08 en la planificación del Sprint 3 (16/11). No se crea una HU nueva. |
| **Responsable** | Anthony Lopez (Scrum Master). |
| **Fecha** | 16/11/2026 (planificación del Sprint 3) y en cada Daily |
| **Evidencia de control** | Burndown actualizado cada día; horas por persona en el Scrumboard; acta de la retrospectiva del Sprint 2 (13/11) con la velocidad real. |

### R-08 · Privacidad de los videos de operarios (Datos · prioridad 2 de 9)
| Campo | Contenido |
|---|---|
| **Descripción del riesgo** | Los videos que procesa NewBit muestran a operarios identificables (rostro, ropa, puesto). Los videos subidos, los frames, los clips y las capturas de evidencia de las alertas (HU10) podrían quedar expuestos: en el repositorio, en carpetas compartidas para entrenar en la nube o en la demostración, si la aplicación se publica sin control de acceso. Sería un tratamiento indebido de datos personales y rompería el requisito de privacidad por diseño del Acta. |
| **Causa raíz** | La aplicación no tiene inicio de sesión ni roles: hoy está protegida solo porque corre en 127.0.0.1. Los datos de entrenamiento se suben a Google Drive para Colab (R-03). HU10 guardará capturas de evidencia y no tiene un criterio de privacidad. Hay borrado de videos, pero no plazo de retención. En una planta real, la imagen de un trabajador es un dato personal (Ley N.° 29733, Perú). |
| **Trigger** | `git ls-files` muestra un video, frame o clip fuera de `tests/fixtures`; una carpeta de Drive del proyecto tiene acceso «cualquier persona con el enlace»; o, al preparar la demostración (14/12/2026), una petición desde otra máquina a `/api/videos/{id}/stream` responde HTTP 200 sin sesión. |
| **Entregables afectados (HU)** | **HU01–HU03** (carga y almacenamiento), **HU09** (reproducción), **HU10** (capturas de evidencia), despliegue de demostración y manual; requisitos del Acta «sin reconocimiento facial» y privacidad por diseño; atribución CC BY 4.0 del dataset. |
| **Probabilidad × impacto** | 0,30 (Relativamente probable) × 0,80 (Muy alto) = **0,24** → **MODERADO** |
| **Sustento** | **P = 0,30 (relativamente probable):** pasa en proyectos parecidos; en NewBit los medios ya están fuera de git y la aplicación es local. **I = 0,80 (muy alto):** una fuga de imágenes de trabajadores detendría la demostración y rompería un requisito del Acta. |
| **Estrategia y mitigación** | **Mitigar y evitar.** Revisar `git ls-files` en cada revisión de pares (ítem nuevo de la DoD); compartir la carpeta de Drive solo con los tres miembros; en HU10, guardar solo el recuadro, la hora y la clase, con los rostros difuminados; no publicar la aplicación fuera de 127.0.0.1 sin autenticación; borrar videos y frames procesados en el cierre del proyecto (18/12). |
| **Acción en el backlog** | **Sí:** criterio de aceptación nuevo en **HU10** (captura con rostros difuminados y datos mínimos, tarea 4.04, 03–04/12); tarea nueva del Sprint 4: control de acceso de la demostración antes del despliegue (14/12); ítem nuevo de la DoD (FGAP070). |
| **Responsable** | Anthony Lopez (Developer, web e integración). |
| **Fecha** | 13/11/2026 (primera verificación) · 04/12/2026 (HU10) · 14/12/2026 (demostración) |
| **Evidencia de control** | Salida de `git ls-files` sin medios en el registro de la revisión de pares; captura de permisos de la carpeta de Drive; prueba de HU10 con un rostro difuminado; prueba de acceso sin sesión con HTTP 401 antes de la demostración. |

### R-09 · Decisiones y aceptación del Product Owner a destiempo (Gestión · prioridad 8 de 9)
| Campo | Contenido |
|---|---|
| **Descripción del riesgo** | Las decisiones del Product Owner (aceptar historias, resolver solicitudes de cambio, recortar alcance) podrían llegar tarde. Si la revisión del Sprint 2 cierra sin aceptar formalmente las historias de los Sprints 1 y 2, el Sprint 3 empezaría sin saber qué está terminado, y el plan B de R-01 se decidiría cuando ya no hay margen. |
| **Causa raíz** | Al 09/11 no hay acta de la revisión del Sprint 1: HU01–HU03 están construidas pero sin aceptación formal. La decisión del PO sobre la SC-001 (02/11) recién quedó escrita en el FGAP090 el 09/11. El PO no desarrolla y las decisiones se toman por mensajes, sin un registro. |
| **Trigger** | Una decisión pedida al PO en la Daily o por mensaje pasa más de 2 días hábiles sin respuesta; o la revisión del Sprint 2 (13/11/2026) cierra sin un acta con cada historia aceptada o rechazada. |
| **Entregables afectados (HU)** | Aceptación de **HU01–HU06** y **HU11** (15 PH); registro de las solicitudes de cambio (FGAP090); planificación del Sprint 3; plan B de R-01. |
| **Probabilidad × impacto** | 0,50 (Probable) × 0,20 (Moderado) = **0,10** → **MODERADO** |
| **Sustento** | **P = 0,50 (probable):** la causa raíz está presente (aceptaciones sin acta). **I = 0,20 (moderado):** retrasa la planificación y la aceptación, pero el PO puede resolver en la revisión sin cambiar el Acta. |
| **Estrategia y mitigación** | **Mitigar.** Acta de la revisión de cada sprint con aceptado o rechazado por historia; registro de decisiones del PO en el repositorio (fecha, decisión, motivo); el Scrum Master pone las decisiones pendientes como primer punto de la Daily; el PO aprueba por adelantado la regla de corte de R-01. |
| **Acción en el backlog** | **Dentro de los eventos Scrum:** revisión del Sprint 2 (13/11) y planificación del Sprint 3 (16/11). No se crea una HU nueva. |
| **Responsable** | Albert Chumacero (Product Owner); el Scrum Master agenda y registra. |
| **Fecha** | 13/11/2026 (revisión del Sprint 2) |
| **Evidencia de control** | Acta de la revisión del Sprint 2 con el estado de cada historia; registro de decisiones del PO con fecha (como la de la SC-001 en el FGAP090). |

## Comunicación: guion de 3 minutos (R-01)
- **Riesgo:** R-01 · Ajuste del modelo temporal (ConvLSTM) · P × I = 0,40 · ALTO (prioridad 1 de 9)
- **Presenta:** Anthony Lopez (Scrum Master). Luis Salazar responde las preguntas técnicas y Albert Chumacero (PO) confirma el plan B.
- **Ante quién y cuándo:** Docente y compañeros (actividad de la semana 8) y en la revisión del Sprint 2 (13/11/2026) ante el PO.
- **Apoyo visual:** Matriz P × I (página 1), tabla de priorización (página 2) y ficha R-01 (página 3) de este documento.

| Tiempo | Bloque | Qué se dice |
|---|---|---|
| 0:00–0:20 | Apertura | «Soy Anthony Lopez, Scrum Master de NewBit. De los nueve riesgos que registramos, voy a explicar el más crítico, el R-01: el ajuste del modelo temporal ConvLSTM. Es el único con exposición alta.» |
| 0:20–0:50 | Qué es el riesgo | «NewBit trabaja en dos etapas. YOLOv8 detecta a los operarios y descarta los frames vacíos; después, ConvLSTM mira una secuencia de frames y decide si la conducta es segura o insegura: caminar fuera de la vía peatonal o dejar abierto el panel eléctrico. El riesgo es que ConvLSTM no aprenda a distinguir esas conductas con la configuración inicial, o que ajustarlo tome más entrenamientos de los que caben en el Sprint 3, del 16 al 27 de noviembre. Todavía no es un problema: es un evento incierto que estamos vigilando.» |
| 0:50–1:20 | Por qué es el más crítico | «Usamos la escala del formato. Probabilidad 0,5, probable: es el primer ConvLSTM que entrena el equipo, no tenemos línea base propia y la ventana de N frames de HU05 aún no está terminada. Impacto 0,8, muy alto: sin modelo temporal no hay pipeline completo ni métricas por clase, que son criterios de aprobación del Acta, y se caen HU07, HU08 y lo que depende de ellas, HU09 y HU10. Probabilidad por impacto: 0,40, riesgo alto. Ningún otro riesgo pasa de 0,24.» |
| 1:20–1:50 | Señal de alerta | «No vamos a esperar al final del sprint para enterarnos. Hay dos señales medibles. La primera, el 19 de noviembre, al cerrar el *spike* con dos longitudes de secuencia: si ninguna supera en F1 macro a una línea base que siempre responde la clase mayoritaria, o si la pérdida de validación no baja en cinco épocas seguidas. La segunda, el 24 de noviembre: si en el split de prueba una conducta insegura queda con F1 menor a 0,50.» |
| 1:50–2:25 | Respuesta y evidencia | «La respuesta es mitigar, y está en el backlog como tareas de HU07, no como buena intención. El responsable es Luis Salazar: hace el *spike* el 19, entrena en Colab con checkpoint por época del 20 al 23, lo que también controla el riesgo de GPU, R-03, y registra cada configuración con semilla fija. La evidencia de control es ese registro de experimentos y las métricas por clase del 24 de noviembre.» |
| 2:25–2:50 | Plan B | «Si se activa la señal, aplicamos el plan B del Acta: el Product Owner, Albert Chumacero, reduce el alcance a una sola conducta y la entregamos con su evaluación documentada, en vez de presentar dos conductas a medias. Así protegemos la Definición de Terminado.» |
| 2:50–3:00 | Cierre | «En resumen: el riesgo está identificado, medido, tiene responsable, fecha y una salida acordada. Lo revisamos en cada Daily y lo actualizamos en este registro. Gracias.» |

**Mensaje clave: el riesgo más crítico de NewBit es que el modelo temporal no aprenda a tiempo; lo medimos el 19 y el 24 de noviembre, lo mitiga Luis Salazar con tareas de HU07 y, si falla, el PO reduce el alcance a una conducta.**

## Notas de trabajo (no van en el formato)

### Cambios respecto de la v1.0 (02/11/2026)
- **Códigos estables:** R-01 a R-07 conservan el código de la tabla de priorización de la v1.0. R-04 pasó de «etiquetado de frames más lento» a «desbalance de clases y etiquetas de los clips» (el riesgo real de datos: el dataset etiqueta por video y está desbalanceado). R-06 pasó de «cambio de entorno: una planta y dos cámaras» (0,03) a «iluminación, oclusiones y cambio de dominio» (0,12): ahora incluye las fallas de detección dentro del dataset, que sí están en el alcance (HU03, HU04, HU11). R-07 sube de 0,10 a 0,14 por el Sprint 3 planificado al 93 %. **R-08 (privacidad)** y **R-09 (decisiones del PO)** son nuevos.
- **R-01 y R-03 pasan al Sprint 3:** el plan de lanzamiento ([FGAP080 v1.0, 09/11](../../../semana-09-stakeholders-y-lanzamiento/nuestras-entregas/FGAP080_Cronograma_Lanzamiento_NewBit/FGAP080_Cronograma_Lanzamiento_NewBit.md)) deja HU07 en el Sprint 3 y el FGAP090 registra que el PO rechazó la SC-001 para el Sprint 2 (02/11); por eso el //spike// de R-01 es la tarea 3.05 (19/11, Luis) y no la T10 del Sprint 2 (10/11, Anthony) del FGAP110/FGAP130, que no se ejecuta. T14 (Colab, R-03) sí queda en el Sprint 2. El trigger de R-01 cambia de «exactitud» a «F1 macro», por el desbalance de R-04.
- **Se quitó todo «POR CONFIRMAR» del Word y del PDF** (aprobación del PO y GPU de R-03). Los supuestos quedan abajo.
- Riesgos del resumen del `.md` del Acta: «reproducibilidad de pesos» queda dentro de R-01 y R-02 (semilla fija, configuración versionada, revisión de pares); «iluminación y oclusiones» y «transferibilidad de dominio» están en R-06; «espacio en disco» es R-05; «SM con doble rol» es R-07.
- Fechas del Sprint 3 (16–27/11): día 3 = 18/11, día 4 = 19/11, días 5–6 = 20 y 23/11, día 7 = 24/11, día 8 = 25/11 (tareas 3.04–3.10 del FGAP080). Sprint 4: tarea 4.04 = 03–04/12; despliegue de demostración L2.1 = 14/12; cierre C.2 = 18/12.

### Supuestos (no van en el formato)
1. **Aprobación del PO:** la v1.0 y la v1.1 figuran aprobadas por Albert Chumacero (PO), como pide la entrega; no hay en el repo un acta firmada.
2. **GPU (R-03):** se asume que el equipo no tiene GPU NVIDIA propia (la aplicación corre en CPU, la Mac del SM no admite CUDA y no hay otra GPU registrada); el plan entrena en Google Colab. Si un integrante tiene GPU NVIDIA, baja la probabilidad de R-03.
3. **Umbrales de los triggers** (20 min por época, 10 % y 20 % de frames perdidos, F1 < 0,50, 15 clips, 10 a 1, 0,15 de recall, 2 días hábiles, 10 GB): criterios del equipo, no mediciones; se recalibran con los datos de cada sprint.
4. **Resultados de T11 y T14** (03/11 y 02/11): al 09/11 no hay registro en el repo; el documento no afirma que se hicieron ni su resultado.
5. **Acciones nuevas en el backlog** (criterio de conteo de clips en HU05, criterio de privacidad en HU10, tarea de control de acceso del Sprint 4, ítem de `git ls-files` en la DoD): son respuestas propuestas en este registro; hay que llevarlas al backlog, al FGAP070 y al FGAP080 en su próxima versión.
6. **Datos del dataset** (178/50, 129/19, 13 videos de panel abierto en prueba, 4,6 s promedio de panel cerrado, clips con varias conductas): [Research Pack, 04_DATASET](../../../../proyecto-newbit/investigacion/UnsafeNet_Research_Pack/04_DATASET.md). Capacidad y uso del Sprint 3: [burndown](../Burndown_Sprint_NewBit/Burndown_Sprint_NewBit.md) (plan, no medición).
7. **Ley N.° 29733** (Ley de Protección de Datos Personales del Perú): se cita como marco de R-08; no se hizo un análisis legal.
