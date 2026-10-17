# FGAP040 – Épicas del Proyecto: NewBit (Versión Oficial Normalizada)

- **Archivos para entregar** (esta carpeta): `FGAP040_Epicas_NewBit.docx` (editable) y `FGAP040_Epicas_NewBit.pdf`.
- **Tipo:** Catálogo oficial de 6 épicas y 12 historias de usuario con trazabilidad completa a los roles de negocio de FGAP030.
- **Fecha de normalización:** 17/10/2026 · versión 2.0 (equipo Grupo D3).
- **Control de versiones:** Elaborado por Anthony Lopez / Luis Salazar · Revisado por Anthony Lopez (Scrum Master) · Aprobado por Albert Chumacero (Product Owner).
- **Versión anterior archivada:** La propuesta preliminar de 26 títulos sin criterios ni priorización fue archivada en [`descartado/epicas-26-hu-obsoletas/`](../../../../descartado/epicas-26-hu-obsoletas/).

## Proyecto
**PY-NB-001 – Sistema web con Visión Artificial para la detección de actos inseguros en áreas operativas de manufactura metalmecánica**  
*(Plataforma NewBit)*

## Épicas del Proyecto
| ID | Épica | Rol de Negocio (FGAP030) | Debería… a fin de… |
|---|---|---|---|
| **EP01** | Ingestión y preprocesamiento de video | Administrador de la plataforma (Jorge Ponce Aguilar - TI) | Cargar y estandarizar secuencias de video en formatos .mp4 y .avi $\rightarrow$ disponer de datos ordenados para el análisis visual. |
| **EP02** | Extracción espacial y detección de operarios (YOLOv8) | Supervisora de SST (Mariana Torres Cárdenas) | Detectar automáticamente la presencia de trabajadores en los fotogramas $\rightarrow$ focalizar el análisis en áreas con presencia humana activa. |
| **EP03** | Segmentación y reducción de secuencias temporales | Administrador de la plataforma (Jorge Ponce Aguilar - TI) | Filtrar fotogramas vacíos y agrupar fotogramas activos en clips estandarizados $\rightarrow$ reducir la carga computacional y preparar secuencias temporales. |
| **EP04** | Clasificación espacio-temporal de actos (ConvLSTM) | Supervisora de SST (Mariana Torres Cárdenas) | Evaluar las secuencias temporales mediante redes recurrentes convolucionales $\rightarrow$ diagnosticar y tipificar actos inseguros en la nave. |
| **EP05** | Interfaz de monitoreo y visualización de alertas | Operadora de monitoreo (Lucía Ramos Villena) | Visualizar videos analizados con delimitación de riesgo y recibir alertas oportunas $\rightarrow$ intervenir rápidamente ante eventos de peligro. |
| **EP06** | Administración, calibración y trazabilidad | Administrador de la plataforma (Jorge) / Gerente de operaciones (Ricardo) | Calibrar parámetros de detección y auditar logs de rendimiento $\rightarrow$ garantizar la exactitud operativa y el control del sistema. |

---

## Historias de Usuario (12 HU)

### Épica EP01: Ingestión y preprocesamiento de video
* **HU01:** Como Administrador de la plataforma (Jorge), quiero cargar un archivo de video industrial (.mp4 o .avi) al sistema, para iniciar el flujo de procesamiento visual.
* **HU02:** Como Administrador de la plataforma (Jorge), quiero que el sistema fragmente el video en fotogramas individuales (frames) normalizados, para prepararlos para la inferencia espacial.

### Épica EP02: Extracción espacial y detección de operarios (YOLOv8)
* **HU03:** Como Supervisora de SST (Mariana), quiero que el sistema detecte la presencia de operarios en cada frame mediante YOLOv8, para localizar las zonas donde se desarrollan actividades humanas en el taller.

### Épica EP03: Segmentación y reducción de secuencias temporales
* **HU04:** Como Administrador de la plataforma (Jorge), quiero que el sistema descarte automáticamente los fotogramas sin trabajadores detectados, para optimizar la carga computacional y eliminar tiempo muerto.
* **HU05:** Como Supervisora de SST (Mariana), quiero agrupar los frames activos filtrados en clips de tamaño fijo, para estructurar la entrada al modelo de inferencia temporal.
* **HU06:** Como Supervisora de SST (Mariana), quiero descartar clips que no cumplan con una ventana de tiempo mínima de acción, para evitar alertas falsas por movimientos fugaces.

### Épica EP04: Clasificación espacio-temporal de actos (ConvLSTM)
* **HU07:** Como Supervisora de SST (Mariana), quiero procesar el clip segmentado mediante ConvLSTM, para extraer características de movimiento y dependencias temporales.
* **HU08:** Como Supervisora de SST (Mariana), quiero que el modelo clasifique el comportamiento como seguro o inseguro y tipifique la conducta (pasarela peatonal o tablero de control), para registrar el diagnóstico claro del acto en planta.

### Épica EP05: Interfaz de monitoreo y visualización de alertas
* **HU09:** Como Operadora de monitoreo (Lucía), quiero visualizar el video reproduciéndose en la interfaz con un recuadro de color indicando el nivel de riesgo (verde: seguro, rojo: riesgo), para validar visualmente la inferencia.
* **HU10:** Como Operadora de monitoreo (Lucía), quiero que se active una alerta inmediata ante una conducta insegura con registro de hora y captura de evidencia, para intervenir oportunamente.

### Épica EP06: Administración, calibración y trazabilidad
* **HU11:** Como Administrador de la plataforma (Jorge), quiero modificar el umbral de confianza (confidence) de YOLOv8 desde la interfaz de configuración sin alterar código, para calibrar la sensibilidad del filtrado espacial según la iluminación de la nave.
* **HU12:** Como Gerente de operaciones (Ricardo) y Administrador (Jorge), quiero visualizar el log de tiempos de procesamiento y métricas de aceleración, para evaluar la eficiencia técnica y el ahorro de cómputo obtenido.

---

## Trazabilidad y Coherencia con el Marco del Curso
1. **Alineación con FGAP030 (Roles):** Cada una de las 12 historias está asignada a los usuarios reales del taller definidos en el documento de Roles y Prototipos, eliminando la figura académica de "investigador/evaluador".
2. **Distribución por Sprints (31 puntos totales):**
   * **Sprint 1 (7 pts):** HU01 (1 pt), HU02 (2 pts), HU03 (4 pts) — *Ingesta y detección espacial*.
   * **Sprint 2 (8 pts):** HU04 (2 pts), HU05 (3 pts), HU06 (2 pts), HU11 (1 pt) — *Filtrado inteligente, secuencias y calibración*.
   * **Sprint 3 (8 pts):** HU07 (5 pts), HU08 (3 pts) — *Inferencia temporal y diagnóstico*.
   * **Sprint 4 (8 pts):** HU09 (4 pts), HU10 (2 pts), HU12 (2 pts) — *Visualización, alertas y métricas*.
3. **Calibración de Umbral (HU11):** Queda formalizada en el **Sprint 2** para calibrar el detector espacial en conjunto con HU03 y HU04, resolviendo la discrepancia con el Cuadro de Principios Scrum.
