# Burndown de NewBit: un libro por sprint, en el formato del docente (DATOS SIMULADOS PARA CLASE)

> **DATOS SIMULADOS PARA CLASE.** Los Sprints 1 y 2 de NewBit están construidos (17/10/2026) y **por aceptar**: el Product Owner todavía no registró la aceptación de ninguna HU ([estado de los sprints](../../../../proyecto-newbit/gestion/sprints/README.md)). Por eso los días de aceptación, los estados finales, las horas consumidas y las observaciones de los libros son una **simulación ilustrativa**: el Sprint 1 como cierre simulado y los Sprints 2 a 4 como proyección simulada. No son resultados reales. Las HU, sus puntos y su sprint sí son los del backlog oficial.

- **Archivos para entregar** (esta carpeta), uno por sprint, todos con la misma estructura:
  - `Burndown_Sprint01_NewBit.xlsx` · `Burndown_Sprint02_NewBit.xlsx` · `Burndown_Sprint03_NewBit.xlsx` · `Burndown_Sprint04_NewBit.xlsx`
  - No hay PDF.
- **Tipo:** Burndown del sprint en Excel, en el **mismo formato del [ejemplo del docente](../../material-del-profe/burndown-sprint-01-ejemplo/burndown-sprint-01-ejemplo.md)** (Retinopatía): 3 hojas (`Resumen`, `Historias`, `Burndown`), mismas filas, columnas, fórmulas, fuentes, colores, anchos y un gráfico de líneas ideal vs. real. Como el formato es de un solo sprint, hay un libro por sprint.
- **Fecha de elaboración:** 02/11/2026 · Versión 1.0 (Grupo D3).
- **Proyecto:** `PY-NB-001`, Plataforma NewBit. 12 HU y 31 puntos de historia (PH), según [FGAP040](../../../semana-04-justificacion-y-epicas/nuestras-entregas/FGAP040_Epicas_NewBit/FGAP040_Epicas_NewBit.md) y la [Priorización MoSCoW](../../../semana-05-rsu-y-backlog/nuestras-entregas/Priorizacion_MoSCoW_100_Puntos_NewBit/Priorizacion_MoSCoW_100_Puntos_NewBit.md). Definición de Terminado: [FGAP070](../../../semana-05-rsu-y-backlog/nuestras-entregas/FGAP070_Criterios_de_Terminado_NewBit/FGAP070_Criterios_de_Terminado_NewBit.md).

## Control de versiones
| Versión | Fecha | Elaborado por | Revisado por | Aprobado por | Motivo |
|---|---|---|---|---|---|
| 1.0 | 02/11/2026 | Equipo de Desarrollo (Anthony Lopez y Luis Fernando Salazar Diaz) | Anthony Lopez (Scrum Master) | Albert Chumacero (Product Owner): **pendiente** | Burndown de los 4 sprints con tiempos estimados para 2 developers |

## Equipo y capacidad: 3 personas, 2 developers
- **Albert Sebastian Chumacero Chávarry:** Product Owner. **No desarrolla**: aporta 0 h a la capacidad de desarrollo.
- **Anthony Gabriel Lopez Yrribarren:** Scrum Master y Developer. Desarrolla menos que Luis porque se le descuenta su tiempo de Scrum Master.
- **Luis Fernando Salazar Diaz:** Developer.

La capacidad se explica aquí y **no** va en los Excel (el formato del docente no tiene hoja de capacidad). Las «Horas previstas» de cada HU en `Historias` son **números escritos a mano** (como en el original) que salen de las cuentas de abajo: PH × alcance × 5 h/PH. Si cambian los supuestos, hay que volver a escribirlas.

## HU del Sprint 02 con sus horas previstas
Para cuadrar con la EDT del Sprint 02 (FGAP110). Libro: `Burndown_Sprint02_NewBit.xlsx`. Sprint 02: 02/11 a 13/11/2026. Horas previstas = PH × 5 h/PH.

| HU | Entregable | PH | **Horas previstas** | Estado simulado | Día de aceptación (simulado) |
|---|---|:---:|:---:|---|:---:|
| HU04 | Descartar frames vacíos | 2 | **10,0 h** | Terminada | 4 |
| HU05 | Agrupar en clips | 3 | **15,0 h** | En curso (no cumple la DoD; pasa al Sprint 3) | — |
| HU06 | Descartar clips cortos | 2 | **10,0 h** | Terminada | 8 |
| HU11 | Calibrar umbral (confidence) | 1 | **5,0 h** | Terminada | 6 |
| **Total Sprint 02** | | **8** | **40,0 h** | 5 de 8 PH aceptados | |

- Las **40,0 h** caben en la capacidad neta del sprint (**49,5 h**): holgura de 9,5 h y uso previsto del 80,8 %.
- Si la EDT del Sprint 02 reparte las tareas técnicas con otras horas, los totales por HU (10 / 15 / 10 / 5) y el total (40 h) deben cuadrar con esta tabla, o bien se cambia el h/PH en estas cuentas y se reescriben las «Horas previstas».
- Las 6,0 h previstas para cerrar HU05 en el Sprint 3 (40 % del trabajo) no entran en la EDT del Sprint 02.
- Horas consumidas simuladas del Sprint 02: 38,5 h (HU04 11,0 · HU05 11,0 · HU06 12,0 · HU11 4,5).

## Estructura de cada libro (igual al ejemplo del docente)
| Hoja | Contenido |
|---|---|
| `Resumen` | Título «SPRINT 0N · AVANCE Y BURNDOWN · NEWBIT», subtítulo «PY-NB-001 · Datos simulados para clase · HU… · 2 semanas / 10 jornadas hábiles», 7 indicadores (puntos comprometidos, días hábiles, puntos aceptados, puntos pendientes, cumplimiento, velocidad observada, horas consumidas), «LECTURA DOCENTE» y la nota de matriz de datos editable |
| `Historias` | 8 columnas: HU · Entregable · Puntos PH · Día de aceptación · Estado · Horas previstas · Horas consumidas · Observaciones, con fila TOTAL. Solo se editan «Día de aceptación» y «Estado» (lista: Terminada, En curso, Pendiente) |
| `Burndown` | Día hábil 0 a 10 con Ideal pendiente, Real pendiente, Puntos aceptados, Brecha y Evento; nota de fórmulas; un gráfico de líneas «Puntos pendientes durante el Sprint 0N» (ideal vs. real) |

- **Fórmulas:** las mismas del docente, con los rangos ajustados al número de filas de Historias (3 filas en los Sprints 1, 3 y 4; 4 filas en el Sprint 2). Ideal = compromiso × (1 − día / días hábiles). Real = compromiso − suma de PH de las HU «Terminada» con día de aceptación ≤ día. **Solo bajan las HU terminadas.** Brecha = real − ideal. El «Evento» es texto escrito a mano, igual que en el original.
- **Adaptaciones frente al original:** títulos con NewBit y el sprint; el rótulo «Datos simulados para clase» en la línea de subtítulo (y en el título de `Historias` y `Burndown`); dato «—» en «Día de aceptación» de la HU que no se acepta; la etiqueta «LECTURA DOCENTE» se conserva del formato, y el texto bajo ella es una lectura simulada del equipo; nota de arrastre en `Burndown` de los Sprints 2 y 3.

## Parámetros de capacidad
| Parámetro | Valor | Justificación |
|---|---|---|
| Días hábiles por sprint | 10 | 2 semanas (Acta FGAP010) |
| Luis: horas/día dedicadas al proyecto | 3,5 h | Estudiante con otras materias: 3 a 4 h efectivas; punto medio |
| Anthony: horas/día dedicadas al proyecto | 3,5 h | Misma carga académica que Luis |
| Anthony: horas/día de Scrum Master fuera de ceremonias | 0,75 h | Quitar impedimentos, mantener tablero y backlog, coordinar con el PO; se resta de su desarrollo |
| Albert (PO): horas/día de desarrollo | 0 h | El PO no desarrolla (dedica ~0,5 h/día al rol de PO, informativo) |
| Planificación del sprint (día 1) | 2 h por developer | Equipo pequeño y backlog ya estimado |
| Daily Scrum | 15 min por día | Reunión diaria de 15 minutos |
| Revisión del sprint (último día) | 1 h por developer | Demo al PO y aceptación |
| Retrospectiva (último día) | 1 h por developer | Después de la revisión |
| Uso máximo recomendado de la capacidad | 85 % | Colchón del 15 % para imprevistos académicos (parciales, otros cursos) |

**Ceremonias por developer y sprint:** 2 h + (15 min × 10 días = 2,5 h) + 1 h + 1 h = **6,5 h**.

### Horas por punto de historia (h/PH): 5,0 h
| Componente | h/PH | Qué incluye |
|---|:---:|---|
| Análisis y construcción | 2,5 | Diseño, codificación e integración (OpenCV, ultralytics/YOLOv8, FastAPI, ConvLSTM) |
| Pruebas (pytest unitarias + prueba integrada) | 1,0 | Exigidas por la DoD (FGAP070) |
| Revisión cruzada entre Developers | 0,5 | Exigida por la DoD |
| Documentación y evidencia de la DoD | 0,5 | README, evidencia, métricas y versión de pesos |
| Contingencia (reproceso y aprendizaje) | 0,5 | Cerca del 10 % del total |
| **Total** | **5,0** | |

**Por qué 5 h/PH:** queda en el extremo alto del rango de 3 a 5 h/PH porque la DoD de NewBit exige pruebas, revisión de pares y documentación en cada historia. Un punto de historia son 5 h; por ejemplo, HU07 (5 PH) son 25 h. Es un **supuesto de planificación**, no una medición: se recalibra con la velocidad observada en la retrospectiva del Sprint 1.

## Capacidad de un sprint (tabla por persona)
| Persona | Horas dedicadas | (−) Scrum Master | (−) Ceremonias | **Horas netas de desarrollo** |
|---|:---:|:---:|:---:|:---:|
| Luis (Developer) | 35,0 | 0,0 | 6,5 | **28,5** |
| Anthony (SM + Developer) | 35,0 | 7,5 | 6,5 | **21,0** |
| Albert (Product Owner) | 0,0 | 0,0 | 0,0 | **0,0** |
| **Equipo** | | | | **49,5** |

- **Capacidad máxima:** 49,5 h ÷ 5 h/PH = 9 PH.
- **Velocidad objetivo:** 49,5 h × 85 % ÷ 5 h/PH = 8,4, redondeado hacia abajo = **8 PH por sprint**.
- **Feriado del 08/12/2026:** es feriado nacional y cae en el Sprint 4. El calendario fija 10 días hábiles por sprint y no se descontó. Si el equipo no trabaja ese día, se pierden 5,75 h (Luis 3,25 h + Anthony 2,5 h): la capacidad del Sprint 4 baja a 43,75 h, las 40 h previstas siguen cabiendo, pero el uso sube al 91 % y la velocidad objetivo baja a 7 PH.

## Las 12 HU por sprint (13 filas, por el arrastre de HU05)
Horas previstas = PH × alcance × 5 h/PH. «Día» = día hábil de aceptación (simulado).

| Sprint | HU | Entregable | PH | Horas previstas | Horas consumidas (simuladas) | Estado (simulado) | Día |
|:---:|---|---|:---:|:---:|:---:|---|:---:|
| 1 | HU01 | Cargar video (.mp4/.avi) | 1 | 5,0 | 5,5 | Terminada | 3 |
| 1 | HU02 | Extraer frames | 2 | 10,0 | 11,5 | Terminada | 5 |
| 1 | HU03 | Detectar operarios (YOLOv8) | 4 | 20,0 | 24,0 | Terminada | 9 |
| 2 | HU04 | Descartar frames vacíos | 2 | 10,0 | 11,0 | Terminada | 4 |
| 2 | HU05 | Agrupar en clips | 3 | 15,0 | 11,0 | **En curso** (no cumple la DoD) | — |
| 2 | HU06 | Descartar clips cortos | 2 | 10,0 | 12,0 | Terminada | 8 |
| 2 | HU11 | Calibrar umbral (confidence) | 1 | 5,0 | 4,5 | Terminada | 6 |
| 3 | HU05 (arrastre) | Agrupar en clips (cierre) | 3 | 6,0 (alcance 40 %) | 7,0 | Terminada | 4 |
| 3 | HU07 | Procesar con ConvLSTM | 5 | 25,0 | 27,5 | Terminada | 7 |
| 3 | HU08 | Clasificar y tipificar la conducta | 3 | 15,0 | 12,5 | Terminada | 10 |
| 4 | HU09 | Ver video con recuadro de riesgo | 4 | 20,0 | 22,0 | Terminada | 8 |
| 4 | HU10 | Alerta de riesgo con evidencia | 2 | 10,0 | 9,0 | Terminada | 9 |
| 4 | HU12 | Ver log de tiempos de procesamiento | 2 | 10,0 | 11,5 | Terminada | 5 |

### Regla del arrastre (HU05)
HU05 es el caso de una historia que **no cumple la Definición de Terminado** al cerrar su sprint. En la realidad, HU05 agrupa secuencias continuas de longitud variable, pero le falta la ventana fija de N frames y el tensor de entrada de ConvLSTM ([estado de los sprints](../../../../proyecto-newbit/gestion/sprints/README.md)). Por eso, en la simulación:
1. En el **Sprint 2** queda «En curso» con sus **3 PH sin descontar**: la curva real del burndown no baja y el sprint cierra con 3 PH pendientes (cumplimiento 5/8 = 62,5 %).
2. Se vuelve a comprometer en el **Sprint 3** (fila «HU05 (arrastre)» en `Historias`), con solo el 40 % del trabajo por hacer (6 h).
3. Sus 3 PH cuentan como **aceptados y como velocidad una sola vez, en el sprint donde se termina de verdad (Sprint 3)**. Por eso el compromiso del Sprint 3 es de 11 PH (8 propios + 3 de HU05) y la suma de los compromisos de los 4 sprints (34 PH) supera al backlog (31 PH) en esos 3 PH.

## Resumen por sprint (simulado)
Los indicadores de puntos y horas consumidas salen de la hoja `Resumen` de cada libro. Las horas previstas, la capacidad y los usos de capacidad se calculan con las cuentas de este documento (no están en el Excel).

| Indicador | Sprint 1 | Sprint 2 | Sprint 3 | Sprint 4 | Total proyecto |
|---|:---:|:---:|:---:|:---:|:---:|
| Fechas | 19/10–30/10 | 02/11–13/11 | 16/11–27/11 | 30/11–11/12 | 19/10–11/12 |
| Tipo de dato | Cierre simulado | Proyección simulada | Proyección simulada | Proyección simulada | Simulado |
| Puntos comprometidos (PH) | 7 | 8 | 11 (8 + 3 de HU05) | 8 | 31 (34 con arrastre) |
| Puntos aceptados (PH) | 7 | 5 | 11 | 8 | 31 |
| Puntos pendientes (PH) | 0 | 3 | 0 | 0 | 0 |
| Cumplimiento | 100 % | 62,5 % | 100 % | 100 % | 100 % |
| Velocidad observada (PH) | 7 | 5 | 11 | 8 | 7,75 (promedio) |
| Velocidad objetivo (PH) | 8 | 8 | 8 | 8 | 8 |
| Horas previstas | 35,0 | 40,0 | 46,0 | 40,0 | 161,0 |
| Horas consumidas | 41,0 | 38,5 | 47,0 | 42,5 | 169,0 |
| Capacidad neta (h) | 49,5 | 49,5 | 49,5 | 49,5 | 198,0 |
| Uso previsto de la capacidad | 70,7 % | 80,8 % | 92,9 % | 80,8 % | 81,3 % |
| Uso consumido de la capacidad | 82,8 % | 77,8 % | 94,9 % | 85,9 % | 85,4 % |
| Horas previstas ≤ capacidad | OK | OK | OK | OK | 4 de 4 OK |
| PH comprometidos ≤ velocidad objetivo | OK | OK | ATENCIÓN (11 > 8) | OK | 3 de 4 OK |

**Lectura (con los datos simulados):**
- **Sprint 1:** se aceptan las 3 historias (días 3, 5 y 9). HU03 tarda más por un fallo con video real que se corrige antes de la prueba integrada.
- **Sprint 2:** se aceptan HU04, HU11 y HU06 (5 de 8 PH). HU05 queda «En curso» y pasa al Sprint 3.
- **Sprint 3:** es el más riesgoso. Con el arrastre, compromete 11 PH frente a una velocidad objetivo de 8 PH. Las 46 h previstas caben en 49,5 h (93 %), pero sin colchón. HU08 se acepta recién el día 10.
- **Sprint 4:** se aceptan HU12, HU09 y HU10 (8 de 8 PH). Con el feriado del 08/12 descontado queda ajustado.
- La velocidad del Sprint 3 (11 PH) incluye trabajo hecho en parte en el Sprint 2. Para planificar conviene el promedio de los 4 sprints (7,75 PH).

### Curva real pendiente por día (día 0 a 10)
| Sprint | Real pendiente |
|---|---|
| 1 (7 PH) | 7, 7, 7, 6, 6, 4, 4, 4, 4, 0, 0 |
| 2 (8 PH) | 8, 8, 8, 8, 6, 6, 5, 5, 3, 3, 3 |
| 3 (11 PH) | 11, 11, 11, 11, 8, 8, 8, 3, 3, 3, 0 |
| 4 (8 PH) | 8, 8, 8, 8, 8, 6, 6, 6, 2, 0, 0 |

## Notas de uso y límites
- **Qué es real y qué es simulado:** son reales las 12 HU, sus puntos, su sprint, las fechas de los sprints y la DoD. Es simulado todo lo demás: la dedicación por persona (supuesto de planificación), los días de aceptación, los estados, las horas consumidas y las observaciones.
- **Numeración de las HU:** se usa la del backlog (FGAP040). La tabla del README del proyecto numera distinto algunas HU; está pendiente de resolver ([estado de los sprints](../../../../proyecto-newbit/gestion/sprints/README.md)).
- **Recalcular:** cada libro se calcula al abrirlo en Excel. Para usarlo con datos reales basta cambiar «Día de aceptación» y «Estado» en `Historias` cuando el PO acepte cada HU (y las horas consumidas, que son datos de entrada).
- **Aprobación del PO:** pendiente. El Product Owner todavía no validó este documento ni aceptó ninguna HU.
