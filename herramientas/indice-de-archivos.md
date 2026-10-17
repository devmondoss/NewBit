# Índice de archivos

**Regla:** cada PDF, Word, PowerPoint o imagen vive en **su propia carpeta, con el mismo nombre**, junto a `<mismo nombre>.md`. Para consultar algo se lee el `.md`; el original solo si el `.md` dice que falta algo. Comprobar con `herramientas/verificar-indice.sh`.

Tipos de `.md`:
- **Ficha rápida:** documento largo o escaneado; solo se hojeó. Es el tipo por defecto para documentos largos.
- **Resumen:** contenido útil (estructura, datos, cifras), no cada palabra.
- **Transcripción:** todo el texto; solo para documentos cortos o formatos a llenar.

Rutas relativas a la raíz del repo. `S2…S5` = `curso/semana-02-scrum-y-acta`, `curso/semana-03-roles-y-prototipos`, `curso/semana-04-justificacion-y-epicas`, `curso/semana-05-rsu-y-backlog`.

## Curso: material del profe (`S*/material-del-profe/`)
| Semana | Carpeta | Tipo de `.md` | De qué trata |
|---|---|---|---|
| todas | `curso/libro-guia-sbok/` | Ficha rápida (escaneado, 413 págs.) + resumen de épicas, backlog, aceptación, prioridad y estimación | **Libro base del curso:** Guía del SBOK, 4.ª ed. (SCRUMstudy); dónde está cada formato |
| 2 | `principios-de-scrum/` | Resumen | Teoría de Scrum, 30 diapositivas |
| 2 | `acta-formato-y-ejemplo-bigfarma/` | Resumen | Formato del Acta con ejemplo BigFarma (2018) |
| 2 | `acta-ejemplo-retinopatia/` | Resumen | Acta de ejemplo (Retinopatía) |
| 3 | `roles-formato-en-blanco/` | Resumen | Formato de Roles en blanco |
| 3 | `roles-ejemplo-bigfarma/` | Resumen | Roles de ejemplo (BigFarma) |
| 3 | `roles-ejemplo-retinopatia/` | Resumen | Roles de ejemplo (Retinopatía) |
| 4 | `justificacion-formato-y-ejemplo/` (DOCX + PDF, mismo contenido) | Resumen | Formato EGAP015 de Justificación + ejemplo |
| 4 | `epicas-ejemplo-retinopatia/` (PDF + DOCX) | Resumen | Épicas de ejemplo (Retinopatía) |
| 5 | `secuencia-de-avances/` | Transcripción | Hoja de ruta FGAP010 → FGAP090 |
| 5 | `criterios-de-terminado-ejemplo-retinopatia/` | Transcripción (1 pág.) | FGAP070 Criterios de Terminado, ejemplo Retinopatía |
| 5 | `rsu-resolucion-448-2023/` | Resumen | Resolución 448-2023 que aprueba el reglamento RSU |
| 5 | `rsu-reglamento-uns/` | Resumen detallado (escaneado; no reabrir) | Reglamento RSU de la UNS + anexos |
| 5 | `rsu-ejemplo-1-charla-tecnologia/` | Resumen | Ejemplo RSU: charla vocacional |
| 5 | `rsu-ejemplo-2-ajedrez-con-ia/` | Resumen | Ejemplo RSU: ajedrez con IA |

## Curso: nuestras entregas (`S*/nuestras-entregas/`)
| Semana | Carpeta | Tipo de `.md` | De qué trata |
|---|---|---|---|
| 2 | `FGAP010_Acta_Constitucion_NewBit/` | Resumen | Acta de NewBit, versión 1.0 completa (DOCX + PDF) |
| 2 | `Cuadro_Principios_Scrum_NewBit/` | Resumen | Cuadro comparativo de los 6 principios de Scrum con ejemplos de NewBit (PPTX + PDF) |
| 3 | `FGAP030_Roles_y_Prototipos_NewBit/` | Resumen | Roles y Prototipos de NewBit, versión 1.0 (DOCX + PDF) |
| 3 | `Diagrama_Arquitectura_NewBit/` | Resumen | Diagrama "Cómo funciona" de NewBit (HTML) |
| 3 | `PPT_Presentacion_NewBit/` | Resumen | PPT de presentación de NewBit (PPTX + PDF), 12 diapositivas |
| 3 | `Infografias_NewBit/` (HTML, CSS, fotos) | `Infografias_NewBit.md` | 12 pasos y metodología de NewBit; página web, excepción a la regla de una carpeta por archivo |
| 4 | `EGAP015_Justificacion_NewBit/` | Resumen | Justificación de NewBit, versión 2.0 (DOCX + PDF) |
| 4 | `FGAP040_Epicas_NewBit/` | Transcripción | **Épicas canónicas del equipo** (6 épicas, 12 HU con roles de planta normalizados y YOLOv8) |
| 5 | `Presentacion_Fist_of_Five/` | Resumen | Estimación con el Puño de cinco aplicada a las historias (HTML + PPTX + PDF + generador, 8 diapositivas) |
| 5 | `Priorizacion_MoSCoW_100_Puntos_NewBit/` | Resumen + datos | Priorización con MoSCoW y 100 puntos de las 12 HU (PDF + PPTX + HTML + generador) |
| 5 | `Tablero_Kanban_NewBit/` | Resumen + backlog completo | Tablero Kanban: 12 HU con criterios, prioridad, puntos y sprint; Scrumboard del Sprint 1 (HTML + PPTX + PDF + generador) |

## Proyecto (`proyecto-newbit/investigacion/`)
| Carpeta | Tipo de `.md` | De qué trata |
|---|---|---|
| `NewBit_Top3_ComputerVision_SeguridadIndustrial/` | Resumen (solo Unsafe-Net) | Top 3 investigaciones; ficha y análisis de Unsafe-Net |
| `UnsafeNet_Research_Pack/` (zip + 15 `.md` ya descomprimidos) | Ficha rápida + los `.md` originales | Investigación del equipo: dataset, arquitectura, plan de réplica |
| `guia-investigacion-unsafe-net.md` (sin original) | — | Qué investigar para cerrar las decisiones |

## Descartado (`descartado/`)
| Carpeta | Tipo de `.md` | De qué trata |
|---|---|---|
| `vigia-industrial/semana-02/VisionOps_Lean_Kanban_Scrum_v01/` | Resumen | Discovery del MVP de VIGIA |
| `vigia-industrial/semana-02/Acta_Constitucion_VIGIA_Industrial_SIDERPERU/` | Resumen | Acta de VIGIA |
| `vigia-industrial/semana-03/NewBit_Arquitectura_Proyecto/` | Resumen | Arquitectura conceptual, 24 diapositivas |
| `vigia-industrial/semana-03/VisionOps Industrial/` | Resumen | Presentación del equipo, 15 diapositivas |
| `vigia-industrial/semana-03/Roles_y_Prototipos_VIGIA_Industrial_SIDERPERU/` | Resumen | Roles de VIGIA |
| `vigia-industrial/semana-03/referencias/infografia-referencia-pasos-vc/` | Resumen | Imagen de referencia: pasos de Computer Vision |
| `vigia-industrial/semana-03/referencias/referencia-metodologia-investigacion/` | Resumen | Imagen de referencia: metodología de investigación |
| `vigia-industrial/semana-03/referencias/referencia-tabla-tecnologias/` | Resumen | Imagen de referencia: comparativa de tecnologías |
| `vigia-industrial/semana-03/04-arquitectura-tecnica.md` (sin original) | — | Documento escrito por el equipo |
| `vigia-industrial/semana-03/infografias/` (HTML, CSS, fotos) | `CREDITOS.md` | Página web de VIGIA; excepción a la regla de una carpeta por archivo |
| `borrador-justificacion-retinopatia.md` (sin original) | — | Borrador de Justificación escrito para el ejemplo de Retinopatía; no es del equipo |
| `epicas-26-hu-obsoletas/` | Histórico | Borrador preliminar de 26 HU con roles genéricos de laboratorio (reemplazado por FGAP040 canónico de 12 HU) |
