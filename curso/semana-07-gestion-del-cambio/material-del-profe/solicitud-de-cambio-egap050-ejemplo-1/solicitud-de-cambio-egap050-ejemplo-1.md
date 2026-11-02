# EGAP050 Solicitud de Cambio: ejemplo 1 (informe PDF de la evaluación, Retinopatía)

- **Fuente:** `solicitud-de-cambio-egap050-ejemplo-1.pdf` (llegó como `EGAP050_Solicitud_de_Cambio_Ejemplo_Retinopatia_UNS.pdf`). 2 págs., con capa de texto.
- **De quién:** docente. **Ejemplo desarrollado con caso y nombres ficticios (PY-DR001 Retinopatía), no del equipo.**
- **Semana:** 7 (llegó el 27/10/2026). El documento dice «Segunda unidad – Semana 7: Scrum – Cambio».
- **Tipo de `.md`:** Resumen (documento corto).

## Estructura del formato EGAP050
Encabezado (asignatura, docente, unidad/semana, proyecto, empresa cliente/desarrolladora) · **1. Control e identificación** (código/versión, fecha/estado, solicitante, responsable de evaluar, épicas y HU relacionadas) · **2. Descripción y justificación** (situación actual, cambio solicitado, justificación/valor, alcance/exclusiones) · **3. Análisis de impacto** (alcance, tiempo/esfuerzo, costo, calidad/seguridad, riesgos, dependencias) · **4. Criterios de aceptación propuestos** · **5. Evaluación, decisión y seguimiento** (evaluación de Developers, decisión del PO, planificación, responsables, estado y evidencia).

## Contenido del ejemplo
- **SC-001 / v1.0**, 26/10/2026, evaluada e incorporada al Product Backlog. La solicita un médico oftalmólogo y la evalúa la PO. Épicas EP03 y EP04; historias HU08 y HU09.
- **Cambio:** botón «Generar informe PDF» en el detalle de la evaluación, con paciente, fecha, imagen, clasificación, confianza y la advertencia de uso como apoyo clínico. No incluye envío por correo ni diagnóstico autónomo.
- **Impacto:** 8 puntos de historia, sin compra de licencias y sin comprometer el sprint en curso. Riesgo: exposición de datos sensibles, mitigada con autorización por rol. Depende de HU08 y HU09.
- **Criterios de aceptación:** CA01–CA05 (solo usuarios autorizados, datos correctos, leyenda de apoyo clínico, no generar el informe si está incompleto, no mezclar pacientes).
- **Decisión:** se crea la **HU21** en el backlog con prioridad media-alta, como candidata a un sprint futuro. No entra automáticamente en el sprint actual.
- Nota final: «Scrum no exige un comité formal de control de cambios.»

## Notas
- El docente usa dos formatos para la solicitud de cambio: **EGAP050**, más detallado y con criterios de aceptación, y **FGAP090**, el formato en blanco para alumnos. Falta confirmar cuál se entrega; el material de la semana pide el FGAP090.
- Segundo ejemplo en el mismo formato: [ejemplo 2](../solicitud-de-cambio-egap050-ejemplo-2/solicitud-de-cambio-egap050-ejemplo-2.md).
