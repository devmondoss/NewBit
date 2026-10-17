# Priorización del backlog de NewBit: MoSCoW y método de los 100 puntos (Versión Oficial Normalizada)

- **Actividad (Semana 5):** Priorización formal de historias de usuario combinando el agrupamiento cualitativo **MoSCoW** (SBOK 4.5.2) con la ponderación cuantitativa de los **100 puntos por integrante** (SBOK 8.5.2.1).
- **Archivos** (esta carpeta):
  - `Priorizacion_MoSCoW_100_Puntos_NewBit.pdf`: Documento formal exportado para el Drive del curso.
  - `Priorizacion_MoSCoW_100_Puntos_NewBit.pptx`: Presentación editable con notas de orador en 6 páginas/diapositivas.
  - `Priorizacion_MoSCoW_100_Puntos_NewBit.html`: Vista web interactiva sin conexión.
  - `generar_priorizacion.js`: Script generador de las diapositivas y tablas.
  - `Carlito-*.woff2`: Fuentes integradas en el visualizador HTML.
- **Base:** 12 historias de usuario del backlog oficial [FGAP040](file:///c:/Users/luisf/OneDrive/Escritorio/Proyectos/IngSoftware/NewBit/curso/semana-04-justificacion-y-epicas/nuestras-entregas/FGAP040_Epicas_NewBit/FGAP040_Epicas_NewBit.md) normalizadas con los roles de planta de [FGAP030](file:///c:/Users/luisf/OneDrive/Escritorio/Proyectos/IngSoftware/NewBit/curso/semana-03-roles-y-prototipos/nuestras-entregas/FGAP030_Roles_y_Prototipos_NewBit/FGAP030_Roles_y_Prototipos_NewBit.md).
- **Fecha de normalización:** 17/10/2026 · Versión 2.0 (Grupo D3) · 6 páginas.
- **Proyecto:** `PY-NB-001 – Sistema web con Visión Artificial para la detección de actos inseguros en áreas operativas de manufactura metalmecánica` *(NewBit)*.

## Estructura del Documento
| # | Título | Contenido |
|---|---|---|
| 1 | Portada | Identificación oficial del Grupo D3, título del proyecto y miembros del equipo Scrum |
| 2 | Métodos del SBOK | Fundamentación teórica: MoSCoW (4 categorías) y Regla de los 100 puntos (consenso por valor) |
| 3 | Paso 1 · Clasificación MoSCoW | 8 Must have (núcleo operativo), 3 Should have, 1 Could have, 3 Won't have (alcance excluido) |
| 4 | Paso 2 · Votación 100 Puntos | Votación individual de Albert (PO), Anthony (SM/Dev) y Luis (Dev), sumando exactamente 100 pts c/u |
| 5 | Paso 3 · Resultado y Orden | Backlog consolidado con orden final, dependencias técnicas y asignación a Sprints |
| 6 | Conclusiones | Síntesis metodológica, lecciones aprendidas de priorización y referencia bibliográfica APA |

---

## Matriz de Priorización Consolidada
*Votación real del equipo (100 puntos por integrante = 300 puntos totales):*

| HU | Historia de Usuario Resumida | Rol de Negocio | MoSCoW | Albert | Anthony | Luis | Total Votos | Orden Final | Depende de | Sprint |
|---|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **HU07** | Procesar con ConvLSTM | Mariana (SST) | **Must** | 15 | 14 | 18 | **47** | **6** | HU05 | **3** |
| **HU08** | Clasificar y tipificar | Mariana (SST) | **Must** | 14 | 12 | 12 | **38** | **7** | HU07 | **3** |
| **HU03** | Detectar operarios (YOLOv8) | Mariana (SST) | **Must** | 12 | 12 | 13 | **37** | **3** | HU02 | **1** |
| **HU09** | Ver video con recuadro | Lucía (Monitoreo) | **Must** | 13 | 9 | 8 | **30** | **8** | HU08 | **4** |
| **HU04** | Descartar frames vacíos | Jorge (TI) | **Must** | 8 | 10 | 10 | **28** | **4** | HU03 | **2** |
| **HU05** | Agrupar en clips | Mariana (SST) | **Must** | 6 | 9 | 10 | **25** | **5** | HU04 | **2** |
| **HU10** | Alerta de riesgo | Lucía (Monitoreo) | **Should** | 10 | 6 | 5 | **21** | **9** | HU08 | **4** |
| **HU02** | Extraer frames | Jorge (TI) | **Must** | 5 | 8 | 7 | **20** | **2** | HU01 | **1** |
| **HU01** | Cargar video (.mp4/.avi) | Jorge (TI) | **Must** | 6 | 8 | 5 | **19** | **1** | — | **1** |
| **HU12** | Ver log de tiempos | Ricardo / Jorge | **Should** | 6 | 5 | 4 | **15** | **10** | HU04 | **4** |
| **HU06** | Descartar clips cortos | Mariana (SST) | **Should** | 3 | 4 | 5 | **12** | **11** | HU05 | **2** |
| **HU11** | Calibrar umbral (confidence) | Jorge (TI) | **Could** | 2 | 3 | 3 | **8** | **12** | HU03 | **2** |
| | **Suma Total de Puntos** | | | **100** | **100** | **100** | **300** | | | |

**Won't have (Fuera de Alcance formal según Acta FGAP010):**
* Conexión a cámaras RTSP en vivo 24/7 en planta.
* Alertas físicas (balizas sonoras/sirenas cableadas en maquinaria).
* Reconocimiento facial o identificación biométrica individual de operarios.

---

## Regla Metodológica de Dependencias (Por qué HU11 y HU06 entran en Sprint 2)
1. **Agrupación MoSCoW:** Establece el nivel de criticidad para el valor del negocio.
2. **Puntos Ponderados (100 pts):** Ordena la importancia relativa de las historias dentro de cada grupo MoSCoW.
3. **Resolución de Dependencias Técnicas (Pipeline Arquitectural):**
   * Aunque **HU11** (calibración de umbral) obtuvo prioridad *Could have* (8 pts, puesto #12), se incorpora al **Sprint 2** porque calibra directamente al detector espacial de HU03 y permite afinar el descarte de frames inactivos de HU04. Postergarla al Sprint 4 impediría calibrar las pruebas del Sprint 2 y 3.
   * Del mismo modo, **HU06** (*Should have*, 12 pts, puesto #11) se ejecuta en el **Sprint 2** porque filtra clips insuficientes antes de que el modelo temporal ConvLSTM sea entrenado y evaluado en el Sprint 3.
