# Sprints de NewBit

Plan de 4 sprints. Fuentes: orden y sprint de cada HU en [Priorización MoSCoW + 100 puntos](../../../curso/semana-05-rsu-y-backlog/nuestras-entregas/Priorizacion_MoSCoW_100_Puntos_NewBit/Priorizacion_MoSCoW_100_Puntos_NewBit.md); lo construido en [`../../README.md`](../../README.md) (sección 2) y en el historial de git.

| Sprint | Estado | Historias (según el backlog MoSCoW) | Código |
|---|---|---|---|
| **1** | Completado (17/10/2026) | HU01 Cargar video · HU02 Extraer frames · HU03 Detectar operarios | `app/`, `ml/` |
| **2** | Completado (17/10/2026) | HU04 Descartar frames vacíos · HU05 Agrupar en clips · HU06 Descartar clips cortos · HU11 Calibrar umbral | `ml/`, `tests/` |
| **3** | Pendiente | HU07 Procesar con ConvLSTM · HU08 Clasificar y tipificar | — |
| **4** | Pendiente | HU09 Ver video con recuadro · HU10 Alerta de riesgo · HU12 Ver log de tiempos | — |

## Avance real a la fecha
- Sprints 1 y 2: **15 puntos de historia implementados** (hito de congelamiento al ~50 %, 17/10/2026), con 43 pruebas automatizadas según el README del proyecto. No ejecuté las pruebas al escribir esta ficha.
- Autor de los commits del código: EnnoAL. Detalle HU por HU: tabla de la sección 2 de [`../../README.md`](../../README.md).

## Inconsistencia a resolver
La **numeración de las HU no coincide** entre el backlog (p. ej. HU03 = Detectar operarios, HU05 = Agrupar clips) y la tabla del README del proyecto (HU03 = Catálogo web, HU05 = YOLOv8n). Los sprints asignados sí coinciden. Falta decidir cuál numeración es la canónica y alinear la otra.

## Ceremonias por sprint (por llenar)
Planificación · Revisión · Retrospectiva: aún no hay actas de sprint en el repo. Guardarlas aquí como `sprint-0N-revision.md` y `sprint-0N-retro.md`.
