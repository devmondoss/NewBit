# NewBit – contexto del repositorio

Repositorio del curso **Ingeniería de Software II** (UNS, 2026-II) y del proyecto del equipo. **Equipo Scrum (3):** Albert Sebastian Chumacero Chávarry (Product Owner), Anthony Gabriel Lopez Yrribarren (Scrum Master y Developer) y Luis Fernando Salazar Diaz (Developer). Proyecto en **4 sprints**. Monorepo: curso y proyecto van separados.

Antes de responder, lee:
- `README.md` — mapa del repo, calendario y reglas para agregar contenido.
- `docs/CONTEXTO-CURSO.md` — calendario por semanas, qué enseñó cada una, convenciones del docente y entregables.
- `proyecto/README.md` — **proyecto vigente: NewBit** — plataforma de Computer Vision que convierte cámaras existentes en sensores inteligentes configurables para operaciones industriales. **Investigación base: Unsafe-Net** (conductas inseguras con YOLO + ConvLSTM, elegida el 05/10/2026); "Unsafe-Net" no es el nombre del proyecto. Estado de entregables y decisiones abiertas. Ficha: `proyecto/investigacion/NewBit_Top3_ComputerVision_SeguridadIndustrial/NewBit_Top3_ComputerVision_SeguridadIndustrial.md`.
- `archivo/vigia-industrial/CONTEXTO-PROYECTO.md` — proyecto anterior (VIGIA Industrial / NewBit). Solo referencia.

Estructura:
- `docs/semana-XX/` — **solo material del docente** (**una carpeta por archivo** con el mismo nombre: original + `<mismo nombre>.md`). Índice: `docs/README.md`.
- `proyecto/entregables/<FORMATO>_…/` — formatos del curso llenados para NewBit (`.docx` + `.md`). Se editan directo en el Word (descomprimir → editar `word/document.xml` → comprimir); lo pendiente va resaltado en amarillo con "POR CONFIRMAR".
- `proyecto/investigacion/` — **contexto del proyecto, no va por semanas** (Top 3, guía de investigación, UnsafeNet Research Pack). Todo lo que sea investigación o contexto del proyecto va aquí. El código, cuando exista, va dentro de `proyecto/` (p. ej. `ml/`, `app/`).
- `archivo/` — proyectos descartados.

Ahorro de tokens (importante):
- **Nunca abrir un PDF/DOCX/PPTX/imagen si tiene `.md`.** Buscarlo en `INDICE-ARCHIVOS.md` y leer ese `.md`. Abrir el original solo si el `.md` dice que algo no está cubierto o el usuario lo pide.
- Orden de lectura: `README.md` → `docs/CONTEXTO-CURSO.md` o `proyecto/README.md` → el `.md` puntual. No leer semanas enteras.
- Todo archivo nuevo no-Markdown lleva un `.md`, pero **con el mínimo de lectura**:
  - **Largo, normativo o escaneado** (reglamentos, resoluciones, papers, decks largos): **no leerlo entero ni escanear página por página**. Una pasada: portada, índice y 1–2 páginas clave. Escribir una **ficha rápida** (qué es, de quién, para qué sirve, estructura en una línea, 3–5 puntos clave) y marcar "Ficha rápida: no leído completo".
  - **Corto o formato a llenar** (plantilla EGAP/FGAP, infografía de 1 página): resumen o transcripción.
  - Guardarlo en **su propia carpeta con el mismo nombre del archivo** (sin extensión) dentro de la semana: `semana-XX/<nombre>/<nombre>.pdf` + `semana-XX/<nombre>/<nombre>.md`. Mismo documento en PDF y Word → misma carpeta, un `.md`.
  - Agregar su fila a `INDICE-ARCHIVOS.md` y correr `scripts/verificar-indice.sh`.

Reglas:
- Los documentos de **Retinopatía Diabética**, **BigFarma** y los **proyectos RSU de 2025** son **ejemplos/plantillas del docente**, no del equipo.
- **Semanas:** 1 = 14–20/09 (sin actividad) · 2 = 21–27/09 (Scrum, Acta) · 3 = 28/09–04/10 (Roles, infografía) · 4 = 05–11/10 (Justificación y Épicas) · **5 = 12–18/10, actual (RSU y Secuencia de avances FGAP010→FGAP090)**. Cada semana empieza el lunes; la semana de un archivo se decide por su fecha de llegada.
- Material nuevo del docente → `docs/semana-XX/` + actualizar `docs/README.md`, `docs/CONTEXTO-CURSO.md` y la tabla del `README.md` raíz. Trabajo del equipo → `proyecto/entregables/` (formatos) o `proyecto/investigacion/` (contexto) + actualizar `proyecto/README.md`.
- No afirmar resultados no demostrados; marcar como propuesta lo que sea diseño nuevo.
