# EGAP050 Solicitud de Cambio: ejemplo 2 (validar calidad técnica de imágenes, Retinopatía)

- **Fuente:** `solicitud-de-cambio-egap050-ejemplo-2.pdf` (llegó como `EGAP050_Solicitud_de_Cambio_Ejemplo_02_Retinopatia_UNS.pdf`). 2 págs., con capa de texto.
- **De quién:** docente. **Ejemplo desarrollado con caso y nombres ficticios (PY-DR001 Retinopatía), no del equipo.**
- **Semana:** 7 (llegó el 27/10/2026).
- **Tipo de `.md`:** Resumen (documento corto). La estructura del formato está en el [ejemplo 1](../solicitud-de-cambio-egap050-ejemplo-1/solicitud-de-cambio-egap050-ejemplo-1.md).

## Contenido del ejemplo
- **SC-002 / v1.0**, 26/10/2026, evaluada e incorporada al Product Backlog. La solicita una técnica de imágenes oftalmológicas y la evalúa la PO. Épicas EP02 y EP03; historias HU04 (cargar imagen) y HU06 (notificar imágenes no válidas).
- **Situación:** el sistema no avisa con claridad si la imagen está desenfocada, con poca luz o en un formato no admitido antes del análisis.
- **Cambio:** verificar la calidad técnica antes de enviar la imagen al modelo, con mensajes específicos y la opción de reemplazar el archivo. No incluye compra de cámaras ni diagnóstico automatizado.
- **Impacto:** 5 puntos de historia, sin alterar el Sprint Goal vigente y sin cambiar la arquitectura del modelo. Riesgo: rechazar imágenes clínicamente útiles (falsos positivos), mitigado con umbrales ajustables y validación con personal oftalmológico. Depende de HU04, HU06 y de los criterios técnicos de calidad.
- **Criterios de aceptación:** CA01–CA05 (formatos JPG/PNG, resolución mínima, mostrar el motivo y la opción de reemplazo, no enviar al modelo una imagen rechazada, casos de prueba de las alertas).
- **Decisión:** se crea la **HU22** «Validar calidad técnica de imágenes» con prioridad alta, como candidata a un sprint futuro.

## Para NewBit
El cambio es análogo a uno posible en NewBit: validar la calidad del video o del encuadre de la cámara antes de la inferencia. Si se usa como idea, hay que redactarlo con nuestras épicas, HU y sprints.
