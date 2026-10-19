# NewBit – contexto del repositorio

Repositorio del curso **Ingeniería de Software II** (UNS, 2026-II) y del proyecto del equipo. **Equipo Scrum (3):** Albert Sebastian Chumacero Chávarry (Product Owner), Anthony Gabriel Lopez Yrribarren (Scrum Master y Developer) y Luis Fernando Salazar Diaz (Developer). **Grupo D3** (laboratorio D, equipo 3). Proyecto en **4 sprints**. Monorepo: lo de clase en `curso/`, el proyecto en `proyecto-newbit/`.

Antes de responder, lee:
- `README.md` — mapa del repo, calendario y reglas para agregar contenido.
- `curso/contexto-del-curso.md` — calendario por semanas, qué enseñó cada una, convenciones del docente y entregables.
- `proyecto-newbit/README.md` — **proyecto vigente: NewBit** — plataforma de Computer Vision que convierte cámaras existentes en sensores inteligentes configurables para operaciones industriales. **Investigación base: Unsafe-Net** (conductas inseguras con YOLO + ConvLSTM, elegida el 05/10/2026); "Unsafe-Net" no es el nombre del proyecto. Estado de entregables y decisiones abiertas. Ficha: `proyecto-newbit/investigacion/NewBit_Top3_ComputerVision_SeguridadIndustrial/NewBit_Top3_ComputerVision_SeguridadIndustrial.md`.
- `descartado/vigia-industrial/CONTEXTO-PROYECTO.md` — proyecto anterior (VIGIA Industrial / NewBit). Solo referencia.

Estructura (reorganizada el 12/10/2026):
- `curso/` — **todo lo de clase**. Índice de semanas: `curso/README.md`.
  - `curso/semana-XX-<tema>/material-del-profe/` — **solo material del docente** (**una carpeta por archivo** con el mismo nombre: original + `<mismo nombre>.md`). Nombres cortos en minúsculas (p. ej. `acta-ejemplo-retinopatia/`).
  - `curso/semana-XX-<tema>/nuestras-entregas/<ENTREGABLE>/` — **tareas del curso** hechas para NewBit, **en la semana en que se pidieron** (`.docx`/`.pdf`/`.pptx`/`.html` + `.md`). Conservan su nombre de entrega (p. ej. `FGAP010_Acta_Constitucion_NewBit`). Los Word se editan directo (descomprimir → editar `word/document.xml` → comprimir); lo pendiente va resaltado en amarillo con "POR CONFIRMAR".
  - `curso/referencias/` — libro base del docente (`libro-guia-sbok/`) y lecturas generales (vale para todas las semanas).
- `proyecto-newbit/` — **el proyecto en sí, no va por semanas**: `README.md` (estado, decisiones, hoja de ruta de entregables) e `investigacion/` (Top 3, guía de investigación, UnsafeNet Research Pack). El código, cuando exista, va aquí (p. ej. `ml/`, `app/`).
- `descartado/` — proyecto anterior (VIGIA) y borradores que no se usan.
- `herramientas/` — `indice-de-archivos.md` y `verificar-indice.sh`.

Ahorro de tokens (importante):
- **Nunca abrir un PDF/DOCX/PPTX/imagen si tiene `.md`.** Buscarlo en `herramientas/indice-de-archivos.md` y leer ese `.md`. Abrir el original solo si el `.md` dice que algo no está cubierto o el usuario lo pide.
- Orden de lectura: `README.md` → `curso/contexto-del-curso.md` o `proyecto-newbit/README.md` → el `.md` puntual. No leer semanas enteras.
- Todo archivo nuevo no-Markdown lleva un `.md`, pero **con el mínimo de lectura**:
  - **Largo, normativo o escaneado** (reglamentos, resoluciones, papers, decks largos): **no leerlo entero ni escanear página por página**. Una pasada: portada, índice y 1–2 páginas clave. Escribir una **ficha rápida** (qué es, de quién, para qué sirve, estructura en una línea, 3–5 puntos clave) y marcar "Ficha rápida: no leído completo".
  - **Corto o formato a llenar** (plantilla EGAP/FGAP, infografía de 1 página): resumen o transcripción.
  - Guardarlo en **su propia carpeta con el mismo nombre del archivo** (sin extensión) dentro de `material-del-profe/` o `nuestras-entregas/` de la semana: `<nombre>/<nombre>.pdf` + `<nombre>/<nombre>.md`. Mismo documento en PDF y Word → misma carpeta, un `.md`.
  - Agregar su fila a `herramientas/indice-de-archivos.md` y correr `herramientas/verificar-indice.sh`.

Reglas:
- Los documentos de **Retinopatía Diabética**, **BigFarma** y los **proyectos RSU de 2025** son **ejemplos/plantillas del docente**, no del equipo.
- **Semanas:** 1 = 14–20/09 (sin actividad) · 2 = 21–27/09 (Scrum, Acta) · 3 = 28/09–04/10 (Roles, infografía) · 4 = 05–11/10 (Justificación y Épicas) · **5 = 12–18/10, actual (RSU y Secuencia de avances FGAP010→FGAP090)**. Cada semana empieza el lunes; la semana de un archivo se decide por su fecha de llegada.
- Material nuevo del docente → `curso/semana-XX-<tema>/material-del-profe/` (crear la carpeta de la semana con su tema si no existe) + actualizar `curso/README.md`, `curso/contexto-del-curso.md` y la tabla del `README.md` raíz. Tareas del equipo → `curso/semana-XX-<tema>/nuestras-entregas/`; investigación o código → `proyecto-newbit/`. En ambos casos actualizar `proyecto-newbit/README.md`.
- No afirmar resultados no demostrados; marcar como propuesta lo que sea diseño nuevo.
