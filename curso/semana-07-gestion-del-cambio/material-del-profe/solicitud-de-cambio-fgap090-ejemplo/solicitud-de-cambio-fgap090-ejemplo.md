# FGAP090 Solicitud de Cambio: ejemplo resuelto (control de calidad de imágenes, Retinopatía)

- **Fuente:** `solicitud-de-cambio-fgap090-ejemplo.pdf` (llegó como `FGAP090_Ejemplo_Resuelto_Control_Calidad_Imagenes_Retinopatia.pdf`). 2 págs., con capa de texto.
- **De quién:** docente. **Ejemplo académico con datos ficticios (proyecto PR-IA-07 RetinaVis), no del equipo.**
- **Semana:** 7 (llegó el 27/10/2026; el documento tiene fecha 26/10/2026).
- **Tipo de `.md`:** Resumen (documento corto).

## Contenido
- **Control de versiones:** v1.0, hecho por Ana Rojas (analista), revisado por Luis Salinas (SM) y aprobado por Dra. Elena Vega (PO), 26/10/2026, «Registro inicial del cambio».
- **Proyecto / código:** PR-IA-07 RetinaVis: Sistema web con Deep Learning para retinopatía diabética · **SC-007-2026**.
- **Problema:** el módulo de carga acepta fotos borrosas, oscuras o de baja resolución. En una prueba simulada, 18 de 60 imágenes tuvieron calidad insuficiente. Causa: no hay controles automáticos ni indicaciones previas a la inferencia. Consecuencia: retrabajo, resultados no interpretables y demoras.
- **Cambio (qué, quién, cómo, cuándo y dónde):** control preliminar de calidad antes del modelo de IA. Lo implementa el equipo, el SM facilita y el PO prioriza y valida. Se verifican formato y resolución y se detectan desenfoque y exposición con umbrales ajustables. Se hace en el siguiente sprint (02–13/11/2026), en la pantalla de carga y en la API.
- **Razón:** advertir antes de la inferencia y permitir repetir la captura. Alternativas descartadas: A, revisión manual (más tiempo y carga), y B, exigir solo un tamaño de archivo (no detecta desenfoque ni exposición). Se elige la validación automática, con revisión manual para los casos límite. Si no se hace el cambio, siguen llegando fotos inapropiadas.
- **Efectos en el proyecto:**
  - Corto plazo: validación en la interfaz y la API, criterios de aceptación, 32 h (S/ 960), priorizar HU-18 y HU-19 sin alterar el sprint actual, y demostración del aviso.
  - Largo plazo: menos imágenes deficientes y menos retrabajo, umbrales ajustables, y la decisión clínica sigue en manos del profesional.
- **Efectos en otros proyectos y en operaciones:** el módulo de reportes recibe el estado de calidad, la API gana una bandera «requiere nueva captura» y se actualiza la guía de captura. No cambia el objetivo funcional.
- **Efectos extra empresariales:** usuarios, clientes, proveedores, normativa (acceso y manejo reservado de imágenes), mercado y gobierno. Casi todo «sin cambios» por ser un caso académico.
- **Observaciones:** estimación de 8 puntos de historia y 32 h (S/ 960). Tras la aprobación, el PO reordena el Product Backlog y el sprint en curso no se toca.
- **Revisión:** 26/10/2026, Dra. Elena Vega (PO). **APROBADA** para refinamiento y planificación del siguiente sprint. Aplica el equipo e informa el SM. Condición: validar los umbrales con el usuario.

## Para NewBit
Es el modelo más directo para nuestro FGAP090: cada campo está respondido con datos concretos, con alternativas comparadas, horas, costo e historias nuevas. En NewBit el cambio equivalente tendría que tocar nuestras propias HU y sprints, sin copiar este caso.
