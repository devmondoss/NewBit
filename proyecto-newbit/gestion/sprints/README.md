# Sprints de NewBit

Plan de 4 sprints. Fuentes: orden y sprint de cada HU en [Priorización MoSCoW + 100 puntos](../../../curso/semana-05-rsu-y-backlog/nuestras-entregas/Priorizacion_MoSCoW_100_Puntos_NewBit/Priorizacion_MoSCoW_100_Puntos_NewBit.md); lo construido en [`../../README.md`](../../README.md) (sección 2) y en el historial de git.

| Sprint | Estado | Historias (según el backlog MoSCoW) | Código |
|---|---|---|---|
| **1** | Construido (17/10/2026), por aceptar | HU01 Cargar video · HU02 Extraer frames · HU03 Detectar operarios | `app/`, `ml/` |
| **2** | Construido (17/10/2026), por aceptar; HU05 en cierre | HU04 Descartar frames vacíos · HU05 Agrupar en clips · HU06 Descartar clips cortos · HU11 Calibrar umbral | `ml/`, `tests/` |
| **3** | Pendiente | HU07 Procesar con ConvLSTM · HU08 Clasificar y tipificar | — |
| **4** | Pendiente | HU09 Ver video con recuadro · HU10 Alerta de riesgo · HU12 Ver log de tiempos | — |

## Avance real a la fecha
- Sprints 1 y 2: **15 puntos de historia implementados** (hito de congelamiento al ~50 %, 17/10/2026).
- **Verificado el 20/10/2026:**
  - **43/43 pruebas pasan**, incluida la E2E.
  - En una copia aislada de la app, el flujo completo funcionó: subir, 24→5 fps, detectar, descartar vacíos y generar un clip de 5 s → 2,4 s.
  - En macOS, un paquete `tests` de terceros en `.venv/site-packages` tapa `proyecto-newbit/tests`, y `test_e2e_pipeline` falla al importar con el comando del README. No es un fallo del código.
- **Lo que falta para que el PO las acepte** (criterios de aceptación y FGAP070):
  - **HU05:** agrupa secuencias continuas de longitud variable. Le faltan la ventana fija de N frames y el tensor de entrada de ConvLSTM, así que se cierra con HU07.
  - **Prueba integrada:** solo se hizo con un clip **sintético** (`tests/fixtures`). El clip pega la foto de muestra `zidane.jpg` de Ultralytics, con personas reales y no operarios, así que no sirve como evidencia visual. Falta probar con los videos del dataset de Önal y Dandıl.
  - **Revisión de pares:** no hay registro.
  - **Aceptación del PO:** queda para la revisión del sprint.
- El estado está en el Producto de la Unidad I v3 (sección 4.8) y en la PPT v4 (láminas 26–29). Reordenar los sprints para adelantar el Sprint 3 es solo una **propuesta**; la decide el PO.
- Autor de los commits del código: EnnoAL. Detalle HU por HU: tabla de la sección 2 de [`../../README.md`](../../README.md).

## Inconsistencia a resolver
La **numeración de las HU no coincide** entre el backlog (p. ej. HU03 = Detectar operarios, HU05 = Agrupar clips) y la tabla del README del proyecto (HU03 = Catálogo web, HU05 = YOLOv8n). Los sprints asignados sí coinciden. Falta decidir cuál numeración es la canónica y alinear la otra.

## Ceremonias por sprint (por llenar)
Planificación · Revisión · Retrospectiva: aún no hay actas de sprint en el repo. Guardarlas aquí como `sprint-0N-revision.md` y `sprint-0N-retro.md`.
