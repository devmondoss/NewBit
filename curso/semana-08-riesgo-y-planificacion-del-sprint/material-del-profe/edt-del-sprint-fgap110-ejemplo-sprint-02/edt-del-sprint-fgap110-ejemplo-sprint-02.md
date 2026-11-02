# FGAP110 EDT del Sprint: ejemplo Sprint 02 (acceso, carga de imagen y resultado, Retinopatía)

- **Fuente:** `edt-del-sprint-fgap110-ejemplo-sprint-02.pdf` (llegó como `FGAP110_EDT_Sprint_02_Historias_y_Tareas_Tecnicas_UNS.pdf`). 2 págs.: pág. 1 con el diagrama jerárquico y pág. 2 con el detalle.
- **De quién:** docente. **Ejemplo académico con datos ficticios (ISW2-IA-2026 Retinopatía), no del equipo.**
- **Semana:** 8 (se agregó al repo el 02/11/2026; el documento tiene fecha 02/11/2026).
- **Tipo de `.md`:** Resumen. El diagrama de la pág. 1 no se transcribe porque sus identificadores (T01–T12) son los mismos de la pág. 2.

## Contenido
- **Versión:** v1.0, 02/11/2026. La hizo el equipo Scrum IA-02, la revisó el SM y la aprobó el PO. Motivo: «Creación de la EDT del Sprint 02».
- **Sprint 02:** 2 al 13 de noviembre de 2026. **Objetivo:** flujo funcional de acceso, carga de imagen y visualización de un resultado de clasificación de prueba.

| HU | Tareas técnicas (estimación) | Total |
|---|---|---|
| **HU-01** Iniciar sesión con credenciales | T01 tablas Usuario y Rol + migraciones (4 h) · T02 API de login y sesión (6 h) · T03 formulario de acceso y validaciones (5 h) · T04 pruebas de credenciales y roles (4 h) | 19 h |
| **HU-02** Cargar imagen de retina | T05 validar extensión, formato, tamaño y errores (4 h) · T06 almacenamiento con identificador seguro (5 h) · T07 endpoint POST /imagenes (6 h) · T08 vista previa y mensajes (5 h) | 20 h |
| **HU-03** Ver resultado de clasificación | T09 integrar inferencia con modelo de prueba (7 h) · T10 endpoint POST /predicciones (6 h) · T11 pantalla de clase y confianza (5 h) · T12 probar flujo imagen → inferencia → pantalla (6 h) | 24 h |
| | | **63 h** |

- **Idea central (pág. 2):** la historia expresa una necesidad del usuario con un beneficio observable. La tarea técnica descompone el trabajo de ingeniería para cumplirla; por ejemplo, «cargar imagen» = validaciones + almacenamiento + API + vista previa. Cada historia tiene varias tareas, y todas deben producir algo verificable.
- Las horas son ilustrativas y se estiman en la planificación del sprint.

## Para NewBit
Cada HU de NewBit se descompone en 3–4 tareas técnicas: datos o modelo, API o pipeline, interfaz y prueba. Las tareas llevan horas, no puntos de historia.
