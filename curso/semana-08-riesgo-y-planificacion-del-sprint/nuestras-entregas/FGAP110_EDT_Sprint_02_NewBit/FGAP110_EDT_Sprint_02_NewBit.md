# FGAP110 – EDT del Sprint 02: NewBit

- **Archivos para entregar** (esta carpeta): `FGAP110_EDT_Sprint_02_NewBit.docx` (editable) y `FGAP110_EDT_Sprint_02_NewBit.pdf`.
- **Base:** una **copia** del formato del docente [`edt-del-sprint-fgap110-formato.doc`](../../material-del-profe/edt-del-sprint-fgap110-formato/edt-del-sprint-fgap110-formato.md) (convertida a .docx con Pages; el original no se tocó). Para regenerar: exportar con Pages una copia del `.doc` como Word y correr `python3 generar_fgap110.py <copia.docx> .`. Se conservan su encabezado, el control de versiones, el título y la tabla de proyecto; la imagen modelo se reemplazó por el árbol de NewBit y la hoja pasó a horizontal, como en los ejemplos del docente.
- **Generadores:** `generar_fgap110.py` (documento y este `.md`), `dibujar_edt.py` (árbol `EDT_Sprint_02_arbol.png`) y `plan_sprint02.py` (fuente única de nodos y tareas, compartida con el FGAP130; `python3 plan_sprint02.py` verifica IDs, predecesoras y máximo 2 tareas por día) y `docx_nb.py` (generador mínimo de .docx que usan también el FGAP050, el FGAP130 y el FGAP090). PDF exportado con Pages (Word no acepta «guardar como» por AppleScript en esta Mac).
- **Fecha:** 02/11/2026 (inicio del Sprint 2) · **Versión:** 1.0 (Grupo D3).
- **Coherencia:** las tareas T01–T14 son las mismas del [cronograma FGAP130](../FGAP130_Cronograma_Sprint_02_NewBit/FGAP130_Cronograma_Sprint_02_NewBit.md); el nodo SC-001 viene de la [solicitud de cambio FGAP090](../../../semana-07-gestion-del-cambio/nuestras-entregas/FGAP090_Solicitud_de_Cambio_NewBit/FGAP090_Solicitud_de_Cambio_NewBit.md) y los nodos R-01, R-02 y R-03, del [FGAP050](../FGAP050_Riesgo_del_Proyecto_NewBit/FGAP050_Riesgo_del_Proyecto_NewBit.md).

## Control de versiones
| Versión | Hecha por | Revisada por | Aprobada por | Fecha | Motivo |
|---|---|---|---|---|---|
| 1.0 | Developers (Anthony Lopez y Luis Salazar) | Anthony Lopez (Scrum Master) | Albert Chumacero (Product Owner) | 02/11/2026 | Creación de la EDT del Sprint 02 |

## Estructura de descomposición del trabajo (EDT) del sprint
| Código y nombre del proyecto | Sprint número |
|---|---|
| PY-NB-001 – Sistema web con Visión Artificial para la detección de actos inseguros en áreas operativas de manufactura metalmecánica (NewBit) | 02 (02 al 13 de noviembre de 2026; 10 días hábiles) |

**Objetivo del Sprint 02:** Cerrar con videos reales del dataset la etapa espacial del Sprint 2 (HU04, HU05, HU06 y HU11) y, si el Product Owner aprueba la SC-001, obtener la primera inferencia de ConvLSTM (HU07) sobre el split oficial de prueba.

### Árbol (nivel 1 → 2 → 3)
```text
PY-NB-001 · NewBit · Sprint Nro. 02 (02–13/11/2026) · 43 h
├── Historia de usuario HU04 · Descartar frames vacíos · 2 pts · 1 h
│   └── T01 Evidencia de reducción con videos reales (1 h)
├── Historia de usuario HU05 · Agrupar en clips · 3 pts · 9 h
│   ├── T02 Ventana fija de N frames (5 h)
│   └── T03 Tensor de entrada de ConvLSTM y pruebas (4 h)
├── Historia de usuario HU06 · Descartar clips cortos · 2 pts · 1 h
│   └── T04 Umbral mínimo alineado con N (1 h)
├── Historia de usuario HU11 · Calibrar umbral (confidence) · 1 pt · 1 h
│   └── T05 Verificar calibración con video real (1 h)
├── Solicitud de cambio SC-001 · Adelantar HU07 (ConvLSTM) · 5 pts · 16 h
│   ├── T06 Tensores del split oficial (3 h)
│   ├── T07 Arquitectura ConvLSTM base (6 h)
│   ├── T08 Entrenamiento base e inferencia (6 h)
│   └── T09 Prueba de integración HU05–HU07 (1 h)
├── Riesgo R-01 · Ajuste del modelo temporal · 3 h
│   └── T10 Spike de N y registro de experimentos (3 h)
├── Riesgo R-02 · Implementación propia del pipeline · 10 h
│   ├── T11 Pipeline espacial con 5 videos reales (3 h)
│   ├── T12 Revisión de pares registrada (4 h)
│   └── T13 Prueba E2E con video real (3 h)
└── Riesgo R-03 · GPU y tiempo de entrenamiento · 2 h
    └── T14 Entorno de entrenamiento en Colab (2 h)
```

### Enunciado de cada nodo (como en la página de detalle del Word)
| Nodo | Enunciado |
|---|---|
| HU04 · Historia de usuario | Como Administrador de la plataforma (Jorge), quiero que el sistema descarte automáticamente los fotogramas sin trabajadores detectados, para optimizar la carga computacional y eliminar tiempo muerto. |
| HU05 · Historia de usuario | Como Supervisora de SST (Mariana), quiero agrupar los frames activos filtrados en clips de tamaño fijo, para estructurar la entrada al modelo de inferencia temporal. |
| HU06 · Historia de usuario | Como Supervisora de SST (Mariana), quiero descartar clips que no cumplan con una ventana de tiempo mínima de acción, para evitar alertas falsas por movimientos fugaces. |
| HU11 · Historia de usuario | Como Administrador de la plataforma (Jorge), quiero modificar el umbral de confianza (confidence) de YOLOv8 desde la interfaz de configuración sin alterar código, para calibrar la sensibilidad del filtrado espacial según la iluminación de la nave. |
| SC-001 · Solicitud de cambio | Adelantar HU07 al Sprint 2 (FGAP090). HU07: como Supervisora de SST (Mariana), quiero procesar el clip segmentado mediante ConvLSTM, para extraer características de movimiento y dependencias temporales. No aprobada por el PO el 02/11/2026: HU07 se hace en el Sprint 3. |
| R-01 · Riesgo | Riesgo del FGAP050 (P × I = 0,40, alto): el modelo ConvLSTM podría no aprender a distinguir las conductas con la configuración inicial. Respuesta: mitigar con un *spike* y un registro de experimentos. |
| R-02 · Riesgo | Riesgo del FGAP050 (P × I = 0,20, moderado): defectos no detectados en el pipeline propio, probado solo con un clip sintético y sin revisión de pares. Respuesta: verificación con videos reales, revisión de pares y prueba E2E; cubre también el cierre de HU01–HU03. |
| R-03 · Riesgo | Riesgo del FGAP050 (P × I = 0,20, moderado): falta de GPU propia o cortes de Google Colab. Respuesta: entorno de entrenamiento reanudable, con checkpoint por época. |

**Nota del documento:** **Total del Sprint 02: 43 h** (historias de usuario 12 h · SC-001 16 h · riesgos 15 h). Dos Developers, Luis Salazar y Anthony Lopez, con un máximo de 2 tareas en paralelo por día (Albert Chumacero es PO y no desarrolla). SC-001 no aprobada (02/11/2026): T06–T10 no se ejecutan y la carga real es de 24 h.

### Detalle de tareas técnicas
| Nodo | ID | Tarea técnica (entregable verificable) | Responsable (propuesto) | Fechas | Predecesoras | Horas |
|---|---|---|---|---|---|:---:|
| HU04 | **T01** | Registrar, con los 5 videos del dataset de T11, los frames entrantes, los conservados y el % de reducción (criterio 2 de HU04). | Anthony Lopez | 09/11 | T11 | 1 |
| HU05 | **T02** | Ventana fija de N frames consecutivos sobre las secuencias activas, con N y paso configurables (criterio 1 de HU05). | Luis Salazar | 04/11–05/11 | — | 5 |
| HU05 | **T03** | Tensor de entrada de ConvLSTM (clips × N × alto × ancho × canales), normalizado y guardado con su índice; pruebas unitarias de la ventana y del tensor (criterio 2 de HU05). | Luis Salazar | 06/11 | T02 | 4 |
| HU06 | **T04** | Alinear el umbral de duración mínima con la ventana N (un solo parámetro de configuración) y verificar en el log el conteo de clips descartados. | Anthony Lopez | 06/11 | T02 | 1 |
| HU11 | **T05** | Verificar con un video del dataset el efecto de dos umbrales de confianza en los frames conservados y su registro en la bitácora de auditoría. | Anthony Lopez | 02/11 | — | 1 |
| SC-001 | **T06** | Generar con el pipeline (YOLOv8 → HU04 → HU05) los tensores del split oficial de entrenamiento y prueba de las dos conductas y sus casos seguros. | Luis Salazar | 09/11 | T03 | 3 |
| SC-001 | **T07** | Implementar la arquitectura ConvLSTM base, con configuración versionada y semilla fija. | Anthony Lopez | 03/11–05/11 | — | 6 |
| SC-001 | **T08** | Entrenar la configuración elegida, guardar el checkpoint e inferir sobre el split oficial de prueba con un vector de probabilidades normalizado por secuencia (criterios 1 y 2 de HU07). | Luis Salazar | 11/11–12/11 | T10, T14 | 6 |
| SC-001 | **T09** | Prueba de integración HU05 → HU07 (forma del tensor, una salida por secuencia y probabilidades que suman 1) y revisión de pares del código de T08 (la hace Anthony antes de la revisión del sprint). | Luis Salazar | 13/11 | T08 | 1 |
| R-01 | **T10** | Spike: entrenamientos cortos con dos valores de N, registro versionado de cada configuración y del tiempo por época; se elige la configuración base. Mide los triggers de R-01 y R-03. | Anthony Lopez | 10/11 | T06, T07 | 3 |
| R-02 | **T11** | Ejecutar carga, frames, YOLOv8 y descarte con 5 videos del dataset y revisar a mano la detección de operarios (evidencia de HU01–HU03 y trigger de R-02). | Luis Salazar | 03/11 | — | 3 |
| R-02 | **T12** | Revisión de pares registrada con la lista del FGAP070: Luis revisa el código de Anthony (10/11) y Anthony el de Luis (11/11); se cierran las observaciones críticas. | Luis Salazar y Anthony Lopez | 10/11–11/11 | T03, T04, T06, T07 | 4 |
| R-02 | **T13** | Agregar un video real del dataset a la prueba E2E, corregir el conflicto del paquete `tests` en macOS y ejecutar la suite completa. | Anthony Lopez | 12/11 | T12 | 3 |
| R-03 | **T14** | Preparar el entorno de entrenamiento en Google Colab: dependencias fijadas, datos montados y checkpoint por época para reanudar tras una desconexión. | Luis Salazar | 02/11 | — | 2 |

### Horas por nodo (para cuadrar con el burndown)
| Nodo | Tipo | Pts | Tareas | Horas |
|---|---|:---:|---|:---:|
| HU04 · Descartar frames vacíos | Historia de usuario | 2 | T01 | 1 |
| HU05 · Agrupar en clips | Historia de usuario | 3 | T02, T03 | 9 |
| HU06 · Descartar clips cortos | Historia de usuario | 2 | T04 | 1 |
| HU11 · Calibrar umbral (confidence) | Historia de usuario | 1 | T05 | 1 |
| SC-001 · Adelantar HU07 (ConvLSTM) | Solicitud de cambio | 5 | T06, T07, T08, T09 | 16 |
| R-01 · Ajuste del modelo temporal | Riesgo | — | T10 | 3 |
| R-02 · Implementación propia del pipeline | Riesgo | — | T11, T12, T13 | 10 |
| R-03 · GPU y tiempo de entrenamiento | Riesgo | — | T14 | 2 |
| **Total** | | **13** | T01–T14 | **43** |

Historias del backlog del Sprint 2 (HU04, HU05, HU06, HU11): 12 h · SC-001 (HU07): 16 h · riesgos (R-01, R-02, R-03): 15 h. Por persona: Luis 26 h (incluye 2 h de T12) y Anthony 17 h (incluye 2 h de T12).

## Notas de trabajo (no van en el formato)

### Capacidad del equipo y paralelismo
- **Equipo:** 3 personas y **2 Developers**. Albert Chumacero es Product Owner y no desarrolla; Anthony Lopez es Scrum Master y Developer; Luis Salazar es Developer.
- **Capacidad de referencia (estimación):** Luis ≈ 4 h/día y Anthony ≈ 3,5 h/día, menos ≈ 0,5 h/día de labores de Scrum Master; descontadas las ceremonias (planificación 2 h, Daily 15 min, revisión 1,5 h y retrospectiva 1 h ≈ 7 h por persona) quedan ≈ 33 h (Luis) + ≈ 23 h (Anthony) = **≈ 56 h** para tareas.
- **Carga planificada:** **43 h** (≈ 77 %): Luis 26 h y Anthony 17 h. **Nunca hay más de 2 tareas en paralelo por día** (una por Developer); la revisión de pares (T12) la hace Luis el 10/11 y Anthony el 11/11. Ver el cronograma FGAP130.

### Notas
- **SC-001 no aprobada.** El nodo SC-001 (T06–T09) y la respuesta a R-01 (T10) se planificaron porque se propuso adelantar HU07 (FGAP090), pero el Product Owner no la aprobó el 02/11/2026 (FGAP090): T06–T10 no se ejecutan, HU07 queda en el Sprint 3 y la carga real del sprint es de 24 h (T01–T05 y T11–T14). T14 (entorno de Colab, R-03) sí se ejecuta como preparación del Sprint 3.
- **HU01–HU03 (Sprint 1):** construidas el 17/10 y sin aceptar; no hay acta de la revisión del Sprint 1 (30/10). No tienen tareas nuevas: su verificación con videos del dataset (T11) y su revisión de pares (T12) cuelgan del riesgo R-02. El PO las revisa en la revisión del Sprint 2 (13/11).
- **HU04, HU06 y HU11** ya están construidas (17/10/2026); sus tareas son de evidencia y ajuste para que el PO pueda aceptarlas con sus criterios y con la Definición de Terminado (FGAP070).
- **Numeración:** HU según el Product Backlog (FGAP040 y priorización MoSCoW). La tabla de la sección 2 del README del proyecto usa otra numeración; falta alinearla.
- **Supuestos:** el dataset completo de Önal y Dandıl (2024) está descargado en el equipo de trabajo (se verifica en T11) y hay acceso a GPU en Google Colab (se prepara en T14).
- Las horas son **estimaciones** del equipo hechas en la planificación; no son horas consumidas.

## Decisión registrada
1. **SC-001 no aprobada** por el PO el 02/11/2026: T06–T10 no se ejecutan; HU07 queda en el Sprint 3; T14 sí se ejecuta. Carga real del sprint: 24 h.
2. **HU01–HU03** se revisan en la revisión del Sprint 2 (13/11), con la evidencia de T11 y T12.
3. **Supuestos:** dataset completo descargado (se verifica en T11) y acceso a GPU en Colab (se prepara en T14).
4. La capacidad (≈ 56 h) es una estimación de referencia; si el burndown usa otra, prevalece la que acuerde el equipo en la planificación.
