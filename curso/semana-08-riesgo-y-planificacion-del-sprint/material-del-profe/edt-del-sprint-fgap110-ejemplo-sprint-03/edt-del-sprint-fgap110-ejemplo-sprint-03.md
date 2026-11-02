# FGAP110 EDT del Sprint: ejemplo Sprint 03 (historial, reportes PDF y auditoría, Retinopatía)

- **Fuente:** `edt-del-sprint-fgap110-ejemplo-sprint-03.pdf` (llegó como `FGAP110_EDT_Sprint_03_Historial_Reportes_Auditoria_UNS.pdf`). 2 págs.: diagrama jerárquico y detalle.
- **De quién:** docente. **Ejemplo académico con datos ficticios (ISW2-IA-2026 Retinopatía), no del equipo.**
- **Semana:** 8 (se agregó al repo el 02/11/2026; el documento tiene fecha 16/11/2026, la del inicio de su sprint).
- **Tipo de `.md`:** Resumen. La estructura es la misma del [ejemplo del Sprint 02](../edt-del-sprint-fgap110-ejemplo-sprint-02/edt-del-sprint-fgap110-ejemplo-sprint-02.md).

## Contenido
- **Sprint 03:** 16 al 27 de noviembre de 2026. **Objetivo:** consultar el historial de evaluaciones, generar reportes PDF y registrar acciones para auditoría de forma segura.

| HU | Tareas técnicas (estimación) | Total |
|---|---|---|
| **HU-04** Consultar historial de evaluaciones de un paciente | T01 entidades Evaluación, PacienteRef y relaciones (5 h) · T02 GET /evaluaciones con filtros y paginación (7 h) · T03 tabla con fecha, resultado y filtros (6 h) · T04 probar orden, filtros y permisos (5 h) | 23 h |
| **HU-05** Descargar reporte de evaluación en PDF | T05 plantilla PDF (4 h) · T06 servicio que genera el PDF (7 h) · T07 botón Descargar y errores (4 h) · T08 validar contenido, formato y autorización (5 h) | 20 h |
| **HU-06** (auditor) Revisar quién consultó o descargó | T09 tabla de auditoría con usuario, acción y hora (4 h) · T10 registrar eventos de consulta y descarga (6 h) · T11 consulta de auditoría solo para el rol autorizado (5 h) · T12 probar permisos, integridad y consulta (5 h) | 20 h |
| | | **63 h** |

- La numeración de tareas **se reinicia en T01 en cada sprint**.
- El criterio de aceptación de la historia se comprueba solo cuando sus tareas entregan una funcionalidad usable y validada.

## Para NewBit
Muestra cómo se ve la EDT de un sprint posterior. Para NewBit correspondería a los sprints 3 y 4 (ConvLSTM y clasificación; video con recuadro, alertas y log).
