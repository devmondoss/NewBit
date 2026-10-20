# Tablero Kanban de NewBit, actualizado al 20/10/2026

- **Qué es:** el tablero Kanban de la semana 5 ([`Tablero_Kanban_NewBit`](../../../semana-05-rsu-y-backlog/nuestras-entregas/Tablero_Kanban_NewBit/Tablero_Kanban_NewBit.md)) con el **estado real al 20/10/2026**. El original queda como se entregó: el informe de la Unidad I lo usa como plan (Figura 6).
- **Archivos** (esta carpeta):
  - `Tablero_Kanban_NewBit_Actualizado.pptx`: editable, 7 diapositivas con notas del orador.
  - `Tablero_Kanban_NewBit_Actualizado.pdf`: exportado con Keynote.
  - `Tablero_Kanban_NewBit_Actualizado.html`: se presenta en el navegador, sin conexión.
  - `generar_tablero.js` (copia adaptada del generador de la semana 5) y `Carlito-*.woff2`.
- **Regenerar:** `node generar_tablero.js <carpeta con node_modules/pptxgenjs@3.12.0>`. El PDF se vuelve a exportar desde Keynote o PowerPoint.
- **Base del estado:**
  - 43/43 pruebas automatizadas y flujo completo en la app (clip sintético), verificados el 20/10.
  - Código del 17/10 (historial de git).
  - Detalle en el Producto de la Unidad I, sección 4.8.

## Cambios frente a la semana 5
| # | Diapositiva | Cambio |
|---|---|---|
| 1 | Portada | «Actualizado al 20/10/2026» |
| 2 | Product Backlog priorizado | Nueva columna **Estado**: 6 «Terminada*», HU05 «En progreso» y 5 «Por hacer». *Terminada = falta la aceptación del PO en la revisión del sprint |
| 3–4 | Criterios de aceptación | Sin cambios |
| 5 | Tablero del Sprint 1 | Las 9 tareas de HU01–HU03 pasan a **Terminada** |
| 6 | **Nueva:** historias del Sprint 2, adelantadas | HU04, HU06 y HU11 terminadas. HU05: «agrupar seguidos» terminada; «ventana fija de N» y «tensor de ConvLSTM» por hacer |
| 7 | Cómo priorizamos y estimamos | S1 y S2 en verde, marcados «construido»; total con 15 de 31 puntos construidos |

- **Fechas:** se pasan a las del acta (S1 19/10–30/10, S2 02/11–13/11, S3 16/11–27/11, S4 30/11–11/12). El original decía 01/11, 15/11 y 29/11.
- **Tareas de las HU del Sprint 2:** el original no las tenía. Se definieron a partir de lo que hace el código.
