# Presentación: Puño de cinco (*Fist of Five*)

- **Archivos** (esta carpeta):
  - `Presentacion_Fist_of_Five.html`: para presentar desde el navegador.
  - `Presentacion_Fist_of_Five.pptx`: editable en PowerPoint o Keynote, con notas del orador.
  - `Presentacion_Fist_of_Five.pdf`: exportado con Keynote, por si falla todo lo demás.
  - `generar_presentacion.js`: genera el HTML y el PPTX desde una sola definición, con las mismas posiciones en pulgadas.
  - `Carlito-*.woff2` (4): la fuente que el generador incrusta en el HTML. Carlito tiene licencia OFL y mide igual que Calibri.
- **Equipo:** **Grupo D3** (laboratorio D, equipo 3). En la portada van los 3 integrantes con su rol; el pie de cada diapositiva dice "Puño de cinco · Grupo D3".
- **Fecha:** 12/10/2026 · versión 1.2 · **8 diapositivas**, unos 12–14 min más una votación con el aula. Versión 1.3: los ejemplos usan **las épicas del equipo** (`../../semana-04/FGAP040_Epicas_NewBit_equipo/`).
- **Fuente teórica:** *Guía del SBOK*, 4.ª ed., **9.2.2.1 Métodos de estimación, pág. 193–195** (PDF 210–212). Resumen en [`docs/semana-05/Guia_SBOK_…`](../../../../docs/semana-05/Guia_SBOK_Fundamentos_de_Scrum_4ta_edicion/Guia_SBOK_Fundamentos_de_Scrum_4ta_edicion.md).
- **Estilo:** minimalista y propio, sin relación con el PPT de NewBit de la semana 3. Fondo blanco, tinta casi negra y acento naranja. Los votos usan rojo (no), ámbar (duda) y verde (sí). Las manos se dibujan con formas simples: en el PPT se pueden editar. Fuente: Calibri en el PPTX. En el HTML va Carlito **incrustada**, así que se ve igual sin internet y con los mismos cortes de línea que el PPTX.
- **POR CONFIRMAR con el docente:** duración, si es por equipo, si se puede votar con el aula y si hay que entregar el PPT.

## Diapositivas
| # | Título | Contenido | Expone |
|---|---|---|---|
| 1 | Puño de cinco | Portada: *Fist of Five*, Grupo D3 con los 3 integrantes y su rol, docente | Albert |
| 2 | Votar a la vez, con los dedos, del 1 al 5 | Qué es y sus dos usos: **estimar** (tamaño relativo) y **decidir** (nivel de acuerdo). Vota el Equipo Scrum; el PO solo aclara | Anthony |
| 3 | Qué significa cada dedo | Los 5 niveles de consenso del libro, con una mano por nivel + sugerencia del equipo | Anthony |
| 4 | Cómo se usa, en 4 pasos | Presentar → votar a la vez → los extremos explican → volver a votar o decidir | Luis |
| 5 | Ejemplo: HU07 «Procesar el clip con ConvLSTM» | Épica EP04. Estimar: ronda 1 (2 y 5), ronda 2 (4 y 4). Decidir: ¿HU07 entra completa al Sprint 3? → 2, 3, 2 → dividirla | Luis |
| 6 | Estimamos las 12 historias de NewBit | HU01–HU12 de nuestras épicas con el tamaño acordado (1–5); la EP04 es la más grande | Anthony |
| 7 | Decidimos en equipo qué entra a cada sprint | 3 votaciones de los tres: EP01 al Sprint 1 (5, 4, 5 → sí) · EP02 + EP03 al Sprint 2 (3, 4, 3 → sí, con revisión) · EP05 + EP06 al Sprint 4 (4, 5, 4 → sí) | Luis |
| 8 | ¿Cuándo usar el puño de cinco? | Comparación con Planning Poker, Wideband Delphi y Afinidad + idea clave + fuente APA | Albert |

**No vienen del libro (propuesta del equipo):** la lectura de los dedos como tamaño (1 = muy pequeña … 5 = muy grande), la sugerencia de la diapositiva 3 y los votos de las diapositivas 5–7, que son simulados. Los tamaños y el reparto por sprint siguen el plan del Acta (EP04 en el Sprint 3).

## Uso
- **HTML:** se abre en el navegador (es un solo archivo, funciona sin internet). **→ / espacio** avanza · **←** retrocede · **N** muestra las notas · **F** pantalla completa. En celular, se desliza.
- **Exportar el HTML a PDF:** con el botón **PDF** (o Ctrl/Cmd + P) → "Guardar como PDF". Sale una diapositiva por página, a 16:9 y con los colores y las manos. Si algo sale blanco, activar "Gráficos de fondo" en el diálogo de impresión.
- **PPT:** no hay que convertir el HTML. El `.pptx` ya está generado con las mismas posiciones; se verificó en Keynote comparando cada diapositiva con el HTML.
- **Para cambiar algo:** editar `generar_presentacion.js` y correr `node generar_presentacion.js <carpeta con node_modules/pptxgenjs@3.12.0>`. Se regeneran el HTML y el PPTX; el PDF se vuelve a exportar desde Keynote.
