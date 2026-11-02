# FGAP130 Cronograma del Sprint: ejemplo Sprint 02 (Retinopatía)

- **Fuente:** `cronograma-del-sprint-fgap130-ejemplo.pdf` (llegó como `FGAP130_Cronograma_Sprint_02_Ejemplo_Resuelto_UNS.pdf`). 1 pág., con capa de texto; diagrama de Gantt.
- **De quién:** Dr. Alfredo Daza Vergaray. **Ejemplo académico con datos simulados (SWRD-2026 Retinopatía), no del equipo.**
- **Semana:** 8 (se agregó al repo el 02/11/2026; el documento tiene fecha 02/11/2026).
- **Tipo de `.md`:** Transcripción de la tabla (sin las barras del Gantt). No llegó el FGAP130 en blanco.

## Estructura del formato FGAP130
Control de versiones · **Código y nombre del proyecto** · **Sprint número** (con fechas) · **Objetivo del sprint** · tabla Gantt con las columnas **Nombre de tarea / Historia · Duración · Comienzo · Fin · Predecesora** y una columna por día hábil (L–V) · leyenda.

## Transcripción
- **Versión:** v1.0, 02/11/2026. La hizo el equipo Scrum (ficticio), la revisó Ana Torres (SM) y la aprobó Carlos Rojas (PO). Motivo: «Cronograma inicial del Sprint 02».
- **Sprint 02:** 02–13/11/2026 (10 días hábiles). **Objetivo:** acceso autenticado, carga validada de imágenes y vista inicial de resultados en un entorno de prueba.

| Tarea / Historia | Duración | Comienzo | Fin | Predecesora |
|---|---|---|---|---|
| **HU-01 · Acceso seguro** | 6 días | 02/11 | 09/11 | |
| T01 · Criterios de acceso | 1 día | 02/11 | 02/11 | — |
| T02 · Interfaz de inicio de sesión | 2 días | 03/11 | 04/11 | T01 |
| T03 · API de autenticación JWT | 3 días | 03/11 | 05/11 | T01 |
| T04 · Integración y pruebas de acceso | 2 días | 06/11 | 09/11 | T02, T03 |
| **HU-02 · Carga validada de imágenes** | 7 días | 04/11 | 12/11 | |
| T05 · Reglas de formato y tamaño | 2 días | 04/11 | 05/11 | — |
| T06 · Pantalla de carga de imagen | 3 días | 06/11 | 10/11 | T05 |
| T07 · API de carga y metadatos | 3 días | 06/11 | 10/11 | T05 |
| T08 · Pruebas de validación | 2 días | 11/11 | 12/11 | T06, T07 |
| **HU-03 · Visualización de resultados** | 5 días | 09/11 | 13/11 | |
| T09 · Endpoint de inferencia | 2 días | 09/11 | 10/11 | T03 |
| T10 · Vista inicial de resultados | 2 días | 11/11 | 12/11 | T09 |
| T11 · Pruebas de aceptación | 1 día | 13/11 | 13/11 | T08, T10 |
| ◆ **Hito · Revisión del Sprint** | Hito | 13/11 | 13/11 | T11 |

**Leyenda:** barras rojas = tareas · franja rosa = historia de usuario · rombo azul = hito · días hábiles de lunes a viernes. **Nota del docente:** fechas, dependencias y estimaciones son simuladas; el Gantt es editable y cada equipo debe adaptarlo a las historias y tareas reales de su sprint.

## Notas
- Las tareas de este cronograma (T01–T11) **no coinciden** con las del [FGAP110 del Sprint 02](../edt-del-sprint-fgap110-ejemplo-sprint-02/edt-del-sprint-fgap110-ejemplo-sprint-02.md) (T01–T12), aunque los dos ejemplos son del mismo sprint. En NewBit, la EDT y el cronograma del mismo sprint deben usar las mismas tareas.
- El cronograma termina en el hito de la revisión del sprint. Las dependencias entre historias se marcan con predecesoras entre tareas; por ejemplo, T09 depende de T03.
