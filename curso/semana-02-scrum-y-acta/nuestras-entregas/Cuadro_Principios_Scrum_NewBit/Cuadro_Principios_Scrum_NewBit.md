# Cuadro comparativo: principios de Scrum aplicados a NewBit (Versión Normalizada)

- **Archivos** (esta carpeta): `Cuadro_Principios_Scrum_NewBit.pptx` (editable, con notas del orador) y `.pdf`. 3 diapositivas en 16:9.
- **Tarea:** Actividad de la semana 2: explicar cada principio con palabras propias y armar un **cuadro comparativo** con su significado y un **ejemplo práctico**, con íconos y colores en diseño claro.
- **Fecha de normalización:** 17/10/2026 · versión 2.0 · los ejemplos usan el proyecto real NewBit: 4 sprints, épicas EP01–EP06 del equipo, roles del equipo Scrum y el entorno de taller de manufactura metalmecánica.

## Contenido Normalizado
| # | Principio | Palabras clave | Ejemplo en NewBit |
|---|---|---|---|
| 1 | **Control del proceso empírico** | Transparencia · Inspección · Adaptación | Tablero Kanban compartido visible para todo el equipo; **calibración del umbral de confianza (HU11) en el Sprint 2** para adaptar el filtrado espacial a la luz del taller; inspección de métricas de ConvLSTM en la revisión del Sprint 3. |
| 2 | **Autoorganización** | Autoasignación · Responsabilidad · Iniciativa | Luis asume el núcleo de visión e inferencia (EP02–EP04) y Anthony la integración web, APIs y pruebas (EP01, EP05); quien culmina una historia apoya en la siguiente tarea del Sprint Backlog. |
| 3 | **Colaboración** | Conciencia · Articulación · Apropiación | El PO (Albert) aclara criterios de aceptación con los perfiles de usuario; revisión cruzada de código entre Developers (Anthony y Luis); Mariana (SST) valida la exactitud de los recuadros de alerta. |
| 4 | **Priorización basada en el valor** | Valor · Riesgo · Dependencias | EP01 primero (ingesta obligatoria); **HU11 entra en el Sprint 2 por dependencia técnica** (calibra el descarte de frames de HU03/HU04); EP04 (núcleo temporal) en el Sprint 3; HU12 (logs y auditoría) al Sprint 4. |
| 5 | **Time-boxing** | Tiempo fijo · Foco · Ritmo | 4 sprints de 2 semanas de duración fija; Daily Standup de 15 minutos; sesiones de Sprint Planning de 4 horas como máximo por iteración (2 h por semana de sprint según SBOK 9.3). |
| 6 | **Desarrollo iterativo** | Incrementos · Épicas $\rightarrow$ historias · Retroalimentación | Un incremento funcional entregable por sprint: S1 ingesta y detección YOLOv8; S2 filtrado inteligente y clips; S3 inferencia temporal ConvLSTM; S4 panel web de alertas y auditoría; todos revisados por el PO. |

Diapositiva 1: portada con los 6 íconos y el equipo. Diapositivas 2 y 3: el cuadro comparativo con 3 principios en cada una.

## Análisis y Coherencia
- Se elimina la discrepancia histórica que ubicaba erróneamente HU11 en el Sprint 4: **HU11 queda formalizada en el Sprint 2**, en estricta sincronía con el Tablero Kanban, la Priorización MoSCoW y el FGAP040 del equipo.
- Se actualiza la tecnología de inferencia espacial a **YOLOv8** y se ratifica el tiempo de time-boxing de 4 sprints de 2 semanas acordado en el Acta (FGAP010).
