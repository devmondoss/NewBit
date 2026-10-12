# Priorización del backlog de NewBit: MoSCoW y método de los 100 puntos

- **Actividad (semana 5, en clase):** priorizar las historias con **MoSCoW** y con el **método de los 100 puntos**. Es la segunda de las dos actividades; la primera, la estimación con el puño de cinco, está en `../Presentacion_Fist_of_Five/`. Se entrega en **PDF** subido al Drive del curso.
- **Archivos** (esta carpeta):
  - `Priorizacion_MoSCoW_100_Puntos_NewBit.pdf`: **el que se sube**, exportado con Keynote.
  - `.pptx`: editable, con notas del orador.
  - `.html`: para presentar desde el navegador.
  - `generar_priorizacion.js`: genera el HTML y el PPTX desde los mismos datos.
  - `Carlito-*.woff2`: fuente incrustada en el HTML.
- **Base:** las 12 HU de la versión del equipo del FGAP040 (`../../../semana-04-justificacion-y-epicas/nuestras-entregas/FGAP040_Epicas_NewBit_equipo/`). Los "No tendrá" salen del "Fuera de alcance" del Acta (FGAP010). Teoría: *Guía del SBOK*, 4.5.2 y 8.5.2.1, pp. 76–78 y 169.
- **Fecha:** 12/10/2026 · versión 1.0 · Grupo D3 · 6 páginas.
- **Votación:** los tres integrantes repartieron sus 100 puntos en clase el 12/10/2026. Si se corrige algún voto, se edita en `generar_priorizacion.js` (campo `v`) y se regenera.

## Páginas
| # | Título | Contenido |
|---|---|---|
| 1 | Priorización | Portada del Grupo D3 |
| 2 | Dos métodos del SBOK para priorizar | MoSCoW: 4 grupos con su significado · 100 puntos: 4 pasos |
| 3 | Paso 1 · MoSCoW | 4 columnas con las historias: 8 Must, 3 Should, 1 Could, 3 Won't (del Acta) |
| 4 | Paso 2 · 100 puntos por integrante | Tabla de votos de Albert, Anthony y Luis, con total y barras; cada uno suma 100 |
| 5 | Paso 3 · Resultado | Backlog final: MoSCoW, puntos, dependencia y sprint |
| 6 | Qué aprendimos | 3 conclusiones + fuente APA |

## Datos
| HU | Historia | MoSCoW | Albert | Anthony | Luis | Total | Orden final | Depende de | Sprint |
|---|---|---|---|---|---|---|---|---|---|
| HU07 | Procesar con ConvLSTM | Must | 15 | 14 | 18 | **47** | 6 | HU05 | 3 |
| HU08 | Etiquetar el clip | Must | 14 | 12 | 12 | **38** | 7 | HU07 | 3 |
| HU03 | Detectar trabajadores | Must | 12 | 12 | 13 | **37** | 3 | HU02 | 1 |
| HU09 | Ver video con recuadro | Must | 13 | 9 | 8 | **30** | 8 | HU08 | 4 |
| HU04 | Descartar frames vacíos | Must | 8 | 10 | 10 | **28** | 4 | HU03 | 2 |
| HU05 | Agrupar en clips | Must | 6 | 9 | 10 | **25** | 5 | HU04 | 2 |
| HU10 | Alerta insegura | Should | 10 | 6 | 5 | **21** | 9 | HU08 | 4 |
| HU02 | Extraer frames | Must | 5 | 8 | 7 | **20** | 2 | HU01 | 1 |
| HU01 | Cargar video | Must | 6 | 8 | 5 | **19** | 1 | — | 1 |
| HU12 | Ver log de tiempos | Should | 6 | 5 | 4 | **15** | 10 | HU04 | 4 |
| HU06 | Descartar clips cortos | Should | 3 | 4 | 5 | **12** | 11 | HU05 | 2 |
| HU11 | Ajustar umbral | Could | 2 | 3 | 3 | **8** | 12 | HU03 | 2 |
| | **Suma** | | 100 | 100 | 100 | 300 | | | |

**Won't (fuera de alcance del Acta):** cámaras en vivo · alertas físicas en planta · reconocimiento facial.

**Regla de combinación:**
1. MoSCoW define el grupo.
2. Los 100 puntos ordenan dentro del grupo.
3. Las dependencias fijan el orden de ejecución: por eso las Must siguen el flujo HU01 → HU09.

El orden final es el mismo que el del **tablero Kanban** (`../Tablero_Kanban_NewBit/`, actualizado a la versión 1.1).
