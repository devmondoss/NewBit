# FGAP130 – Cronograma del Sprint 02: NewBit

- **Archivos para entregar** (esta carpeta): `FGAP130_Cronograma_Sprint_02_NewBit.docx` (editable) y `FGAP130_Cronograma_Sprint_02_NewBit.pdf`.
- **Estructura:** la del [ejemplo FGAP130 del docente](../../material-del-profe/cronograma-del-sprint-fgap130-ejemplo/cronograma-del-sprint-fgap130-ejemplo.md) (no llegó formato en blanco): control de versiones, proyecto y sprint, objetivo, Gantt con duración, comienzo, fin y predecesora, e hito de revisión.
- **Generador:** `generar_fgap130.py`, que lee `plan_sprint02.py` y `docx_nb.py` de la carpeta del FGAP110 (la misma fuente de tareas de la EDT). El Gantt es una tabla de Word editable (celdas coloreadas). PDF exportado con Pages.
- **Fecha:** 02/11/2026 · **Versión:** 1.0 (Grupo D3).
- **Coherencia:** mismas tareas, IDs y horas que la [EDT del Sprint 02 (FGAP110)](../FGAP110_EDT_Sprint_02_NewBit/FGAP110_EDT_Sprint_02_NewBit.md).

## Control de versiones
| Versión | Hecho por | Revisado por | Aprobado por | Fecha | Motivo |
|---|---|---|---|---|---|
| 1.0 | Developers (Anthony Lopez y Luis Salazar) | Anthony Lopez – Scrum Master | Albert Chumacero – Product Owner · **POR CONFIRMAR** | 02/11/2026 | Cronograma inicial del Sprint 02 |

## Cronograma del sprint
| Código y nombre del proyecto | Sprint número |
|---|---|
| PY-NB-001 – Sistema web con Visión Artificial para la detección de actos inseguros en áreas operativas de manufactura metalmecánica (NewBit) | 02 (02–13/11/2026, 10 días hábiles) |

**Objetivo del sprint:** Cerrar con videos reales del dataset la etapa espacial del Sprint 2 (HU04, HU05, HU06 y HU11) y, si el Product Owner aprueba la SC-001, obtener la primera inferencia de ConvLSTM (HU07) sobre el split oficial de prueba.

| Nombre de tarea / Historia | Duración | Comienzo | Fin | Predecesora | L 02/11 | M 03/11 | M 04/11 | J 05/11 | V 06/11 | L 09/11 | M 10/11 | M 11/11 | J 12/11 | V 13/11 |
|---|---|---|---|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **HU04 · Descartar frames vacíos** | **1 día** | **09/11** | **09/11** | |  |  |  |  |  | ░ |  |  |  |  |
| T01 · Evidencia de reducción con videos reales | 1 día | 09/11 | 09/11 | T11 |  |  |  |  |  | █ |  |  |  |  |
| **HU05 · Agrupar en clips** | **3 días** | **04/11** | **06/11** | |  |  | ░ | ░ | ░ |  |  |  |  |  |
| T02 · Ventana fija de N frames | 2 días | 04/11 | 05/11 | — |  |  | █ | █ |  |  |  |  |  |  |
| T03 · Tensor de entrada de ConvLSTM y pruebas | 1 día | 06/11 | 06/11 | T02 |  |  |  |  | █ |  |  |  |  |  |
| **HU06 · Descartar clips cortos** | **1 día** | **06/11** | **06/11** | |  |  |  |  | ░ |  |  |  |  |  |
| T04 · Umbral mínimo alineado con N | 1 día | 06/11 | 06/11 | T02 |  |  |  |  | █ |  |  |  |  |  |
| **HU11 · Calibrar umbral (confidence)** | **1 día** | **02/11** | **02/11** | | ░ |  |  |  |  |  |  |  |  |  |
| T05 · Verificar calibración con video real | 1 día | 02/11 | 02/11 | — | █ |  |  |  |  |  |  |  |  |  |
| **SC-001 · Adelantar HU07 (ConvLSTM)** | **9 días** | **03/11** | **13/11** | |  | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ |
| T06 · Tensores del split oficial | 1 día | 09/11 | 09/11 | T03 |  |  |  |  |  | █ |  |  |  |  |
| T07 · Arquitectura ConvLSTM base | 3 días | 03/11 | 05/11 | — |  | █ | █ | █ |  |  |  |  |  |  |
| T08 · Entrenamiento base e inferencia | 2 días | 11/11 | 12/11 | T10, T14 |  |  |  |  |  |  |  | █ | █ |  |
| T09 · Prueba de integración HU05–HU07 | 1 día | 13/11 | 13/11 | T08 |  |  |  |  |  |  |  |  |  | █ |
| **R-01 · Ajuste del modelo temporal** | **1 día** | **10/11** | **10/11** | |  |  |  |  |  |  | ░ |  |  |  |
| T10 · Spike de N y registro de experimentos | 1 día | 10/11 | 10/11 | T06, T07 |  |  |  |  |  |  | █ |  |  |  |
| **R-02 · Implementación propia del pipeline** | **8 días** | **03/11** | **12/11** | |  | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ |  |
| T11 · Pipeline espacial con 5 videos reales | 1 día | 03/11 | 03/11 | — |  | █ |  |  |  |  |  |  |  |  |
| T12 · Revisión de pares registrada | 2 días | 10/11 | 11/11 | T03, T04, T06, T07 |  |  |  |  |  |  | █ | █ |  |  |
| T13 · Prueba E2E con video real | 1 día | 12/11 | 12/11 | T12 |  |  |  |  |  |  |  |  | █ |  |
| **R-03 · GPU y tiempo de entrenamiento** | **1 día** | **02/11** | **02/11** | | ░ |  |  |  |  |  |  |  |  |  |
| T14 · Entorno de entrenamiento en Colab | 1 día | 02/11 | 02/11 | — | █ |  |  |  |  |  |  |  |  |  |
| **◆ Hito · Revisión del Sprint 02** | Hito | 13/11 | 13/11 | T09, T13 |  |  |  |  |  |  |  |  |  | ◆ |

Leyenda: █ tarea programada · ░ duración del nodo de la EDT (historia, solicitud de cambio o riesgo) · ◆ hito · días hábiles de lunes a viernes. En el Word, como en el ejemplo del docente: barras rojas, franja rosa y rombo azul.

## Notas de trabajo (no van en el formato)

### Asignación diaria por Developer (máximo 2 tareas en paralelo)
| Developer | L 02/11 | M 03/11 | M 04/11 | J 05/11 | V 06/11 | L 09/11 | M 10/11 | M 11/11 | J 12/11 | V 13/11 | Horas |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Luis Salazar | T14 | T11 | T02 | T02 | T03 | T06 | T12 | T08 | T08 | T09 | 26 h |
| Anthony Lopez | T05 | T07 | T07 | T07 | T04 | T01 | T10 | T12 | T13 | — | 17 h |
| Tareas en paralelo | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 43 h |

### Notas
- **Mismas tareas que la EDT.** T01–T14 y sus horas son las del FGAP110 del Sprint 02 (fuente común: `plan_sprint02.py`).
- **Dos Developers, máximo 2 tareas por día.** Cada día hay como mucho una tarea de Luis y una de Anthony (tabla de asignación diaria). Albert Chumacero (Product Owner) no desarrolla: refina el backlog, aclara criterios y acepta o rechaza en la revisión.
- **Ceremonias (no son tareas):** planificación el 02/11; Daily de 15 min cada día; revisión y retrospectiva el 13/11. Por eso el primer y el último día tienen poca carga.
- **SC-001 es condicional.** Las filas de SC-001 (T06–T09), R-01 (T10) y R-03 (T14) dependen de que el Product Owner apruebe la solicitud de cambio (FGAP090): **POR CONFIRMAR**. Si la rechaza, el cronograma queda con T01–T05 y T11–T13 y el hito no cambia.
- **Regla de corte (FGAP090):** si el 10/11 se activa el trigger de R-01 o de R-03 (T10), HU07 vuelve al Product Backlog y T08–T09 no se ejecutan.
- Duraciones en días hábiles (lunes a viernes). Fechas, dependencias y horas son una **estimación** de la planificación, no un avance real.

## POR CONFIRMAR
1. **Aprobación del Product Owner** del cronograma (control de versiones).
2. **Decisión del PO sobre SC-001** (FGAP090): si la rechaza, salen T06–T10 y T14.
3. **Dataset completo descargado** y **acceso a GPU en Colab** (supuestos de T05, T06, T08, T10, T11 y T14).
