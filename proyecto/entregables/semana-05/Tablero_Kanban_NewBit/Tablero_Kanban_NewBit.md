# Tablero Kanban de NewBit: historias con criterios de aceptación, prioridad y estimación

- **Tarea (semana 5):** tablero Kanban con criterios de aceptación, prioridad y estimación. El docente no dejó formato; este es el del equipo.
- **Archivos** (esta carpeta):
  - `Tablero_Kanban_NewBit.html`: para presentar desde el navegador. Es un solo archivo y funciona sin internet. **→** avanza, **N** muestra las notas y **PDF** exporta.
  - `Tablero_Kanban_NewBit.pptx`: editable, con notas del orador.
  - `Tablero_Kanban_NewBit.pdf`: exportado con Keynote.
  - `generar_tablero.js`: genera el HTML y el PPTX desde los mismos datos.
  - `Carlito-*.woff2`: fuente incrustada en el HTML.
- **Base:** historias de la **versión del equipo del FGAP040** (`../../semana-04/FGAP040_Epicas_NewBit_equipo/`), que tiene 6 épicas y 12 HU. Teoría de la *Guía del SBOK*: 8.5 backlog priorizado, 9.1 criterios de aceptación, 9.2 estimación y 9.3.3 Scrumboard. Resumen en [`docs/semana-05/Guia_SBOK_…`](../../../../docs/semana-05/Guia_SBOK_Fundamentos_de_Scrum_4ta_edicion/Guia_SBOK_Fundamentos_de_Scrum_4ta_edicion.md).
- **Origen de los datos:** la prioridad sale de la actividad MoSCoW + 100 puntos (`../Priorizacion_MoSCoW_100_Puntos_NewBit/`) y la estimación, del puño de cinco; ambas votadas por el equipo el 12/10/2026. Los criterios de aceptación y las tareas del Sprint 1 los redactó el equipo.
- **Fecha:** 12/10/2026 · versión 1.1 · Grupo D3 · 6 diapositivas.

## Diapositivas
| # | Título | Contenido | Expone |
|---|---|---|---|
| 1 | Tablero Kanban | Portada del Grupo D3 | Albert |
| 2 | Product Backlog priorizado | Las 12 HU ordenadas: prioridad MoSCoW, puntos y sprint | Albert |
| 3 | Criterios de aceptación (1/2) | Tarjetas HU01–HU06: historia, 2 criterios, prioridad y puntos | Anthony |
| 4 | Criterios de aceptación (2/2) | Tarjetas HU07–HU12 | Luis |
| 5 | Tablero del Sprint 1 (Scrumboard) | Filas = HU01–HU03; sus tareas en Por hacer / En progreso / En prueba / Terminada (SBOK fig. 9-10), al inicio del sprint | Luis |
| 6 | Cómo priorizamos y estimamos | Valor + riesgo + dependencias y MoSCoW (8 Must, 3 Should, 1 Could) · puño de cinco (1–5) · plan de 4 sprints de unos 8 puntos | Anthony |

## Product Backlog
Escalas:
- **Prioridad:** MoSCoW + método de los 100 puntos + dependencias (ver `../Priorizacion_MoSCoW_100_Puntos_NewBit/`).
- **Estimación:** puntos de 1 a 5 con el puño de cinco (1 = muy pequeña, 5 = muy grande).

Sprints de 2 semanas: S1 19/10–01/11 · S2 02/11–15/11 · S3 16/11–29/11 · S4 30/11–11/12.

| # | HU | Historia (texto del FGAP040) | Criterios de aceptación | Prioridad | Pts | Sprint |
|---|---|---|---|---|---|---|
| 1 | HU01 | Como investigador, quiero cargar un archivo de video industrial al sistema, para iniciar el flujo de análisis. | Acepta .mp4 y .avi; otro formato muestra un mensaje de error · Muestra nombre, duración y resolución del video cargado | Must | 1 | 1 |
| 2 | HU02 | Como investigador, quiero que el sistema fragmente el video en fotogramas individuales (frames), para prepararlos para la inferencia espacial. | Guarda los frames numerados y en el orden del video · Los redimensiona al tamaño de entrada de YOLOv4 | Must | 2 | 1 |
| 3 | HU03 | Como investigador, quiero que YOLOv4 identifique la presencia de trabajadores en cada frame, para localizar dónde ocurre la acción. | Devuelve por frame las cajas de «persona» con su confianza · Un frame de prueba se ve con las cajas dibujadas | Must | 4 | 1 |
| 4 | HU04 | Como investigador, quiero que el sistema descarte automáticamente los fotogramas sin trabajadores detectados, para no saturar al modelo temporal con datos inútiles. | Los frames sin personas no pasan a la siguiente etapa · Registra cuántos frames entraron y cuántos se descartaron | Must | 2 | 2 |
| 5 | HU05 | Como investigador, quiero agrupar los frames filtrados en clips de tamaño fijo, para estructurar la entrada al formato requerido por la red temporal. | Todos los clips tienen N frames consecutivos (N configurable) · La salida tiene la forma de entrada que espera ConvLSTM | Must | 3 | 2 |
| 6 | HU07 | Como investigador, quiero procesar el clip segmentado mediante ConvLSTM, para que la red extraiga las características de movimiento y tiempo. | Entrena con el split oficial y guarda pesos y métricas · Recibe un clip y devuelve una probabilidad por clase | Must | 5 | 3 |
| 7 | HU08 | Como investigador, quiero que el modelo asigne una etiqueta de comportamiento "seguro" o "inseguro", para obtener el resultado de la clasificación. | Cada clip queda etiquetado con su probabilidad · Reporta accuracy, precision, recall y F1 del set de prueba (sin metas inventadas) | Must | 3 | 3 |
| 8 | HU09 | Como evaluador del sistema, quiero ver el video reproduciéndose en la GUI con un recuadro de color indicando el riesgo, para validar visualmente la inferencia. | El recuadro es verde (seguro) o rojo (inseguro) por tramo · Funciona con los videos del conjunto de prueba | Must | 4 | 4 |
| 9 | HU10 | Como evaluador del sistema, quiero que se active una alerta al clasificar una conducta insegura, para comprobar el mecanismo de respuesta del modelo base. | Una conducta insegura dispara un aviso visual y sonoro · Cada alerta se guarda con hora, video y probabilidad | Should | 2 | 4 |
| 10 | HU12 | Como administrador técnico, quiero visualizar el log de tiempos de procesamiento, para evaluar si el filtrado realmente mejora la velocidad del sistema. | Muestra el tiempo de cada etapa del procesamiento · Compara el mismo video con y sin filtrado | Should | 2 | 4 |
| 11 | HU06 | Como investigador, quiero descartar clips que no cumplan con el tiempo mínimo de acción, para evitar predicciones falsas por falta de contexto. | Los clips con menos frames que el mínimo se descartan · Registra cuántos clips se descartaron | Should | 2 | 2 |
| 12 | HU11 | Como administrador técnico, quiero modificar el umbral de confianza (confidence) de YOLOv4 desde la configuración, para calibrar la sensibilidad del filtrado espacial. | El umbral se cambia en la configuración, sin tocar código · Rechaza valores fuera de 0–1 y anota el cambio en el log | Could | 1 | 2 |

**Totales:** 31 puntos · S1 7 · S2 8 · S3 8 · S4 8. HU11 es Could pero entra en el Sprint 2 por dependencia: es pequeña y calibra el filtrado de HU03–HU04.

**Tareas del Sprint 1:**
- HU01: pantalla de carga · validar formato · ver datos del video.
- HU02: extraer frames · redimensionar frames · guardar en orden.
- HU03: instalar YOLOv4 · detectar personas · probar con 1 video.

## Notas
- **En las diapositivas**, las historias se resumieron para que quepan en la tarjeta. El texto completo es el de la tabla de arriba, igual al FGAP040.
- **Criterios de aceptación ≠ Definición de terminado.** Los criterios son por historia; la DoD es común a todas y va en el FGAP070, que sigue pendiente.
- **Si algo cambia**, se editan los datos en `generar_tablero.js` y se regenera. Esta tabla sirve de borrador del **FGAP060 Backlog priorizado** cuando llegue el formato.
- **Para regenerar:** `node generar_tablero.js <carpeta con node_modules/pptxgenjs@3.12.0>`. El PDF se vuelve a exportar desde Keynote.
