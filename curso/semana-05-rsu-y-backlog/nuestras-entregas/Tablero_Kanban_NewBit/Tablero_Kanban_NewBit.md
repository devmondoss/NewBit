# Tablero Kanban de NewBit: historias con criterios de aceptación, prioridad y estimación (Versión Oficial Normalizada)

- **Tarea (Semana 5):** Tablero Kanban con criterios de aceptación, prioridad y estimación según los procesos 8.5, 9.1, 9.2 y 9.3 del SBOK (4.ª ed.).
- **Archivos** (esta carpeta):
  - `Tablero_Kanban_NewBit.html`: Para presentar interactivamente desde el navegador (funciona sin conexión).
  - `Tablero_Kanban_NewBit.pptx`: Presentación editable con notas de orador en 6 diapositivas.
  - `Tablero_Kanban_NewBit.pdf`: Exportación para entrega formal.
  - `generar_tablero.js`: Generador de diapositivas en Node.js a partir de los datos unificados.
  - `Carlito-*.woff2`: Fuentes integradas en el visualizador HTML.
- **Base:** 12 historias de usuario del backlog oficial [FGAP040](file:///c:/Users/luisf/OneDrive/Escritorio/Proyectos/IngSoftware/NewBit/curso/semana-04-justificacion-y-epicas/nuestras-entregas/FGAP040_Epicas_NewBit/FGAP040_Epicas_NewBit.md) normalizadas con los roles de planta de [FGAP030](file:///c:/Users/luisf/OneDrive/Escritorio/Proyectos/IngSoftware/NewBit/curso/semana-03-roles-y-prototipos/nuestras-entregas/FGAP030_Roles_y_Prototipos_NewBit/FGAP030_Roles_y_Prototipos_NewBit.md).
- **Fecha de normalización:** 17/10/2026 · Versión 2.0 (Grupo D3) · 6 diapositivas.
- **Proyecto:** `PY-NB-001 – Sistema web con Visión Artificial para la detección de actos inseguros en áreas operativas de manufactura metalmecánica` *(NewBit)*.

## Diapositivas
| # | Título | Contenido | Responsable |
|---|---|---|---|
| 1 | Tablero Kanban | Portada oficial del Grupo D3 con título y roles | Albert (PO) |
| 2 | Product Backlog priorizado | 12 HU ordenadas por prioridad MoSCoW, puntos de historia y sprint | Albert (PO) |
| 3 | Criterios de aceptación (1/2) | Tarjetas HU01–HU06: historia de usuario, criterios de aceptación, prioridad y puntos | Anthony (SM/Dev) |
| 4 | Criterios de aceptación (2/2) | Tarjetas HU07–HU12 con criterios, rol asignado y estimación | Luis (Dev) |
| 5 | Tablero del Sprint 1 (Scrumboard) | Historias HU01–HU03 desglosadas en tareas (Por hacer / En progreso / En prueba / Terminada) | Luis (Dev) |
| 6 | Cómo priorizamos y estimamos | Metodología SBOK: Valor + riesgo + dependencias, MoSCoW (8 Must, 3 Should, 1 Could) y Puño de cinco (31 pts) | Anthony (SM/Dev) |

---

## Product Backlog Oficial (12 HU · 31 Puntos)
**Escalas aplicadas:**
* **Prioridad:** Combinación MoSCoW + 100 puntos ponderados + dependencias técnicas de pipeline.
* **Estimación:** Puntos de historia relativos de 1 a 5 mediante la técnica *Puño de cinco* (SBOK 9.2.2.1).
* **Distribución de Sprints (2 semanas cada uno):** S1 (19/10–01/11, 7 pts) · S2 (02/11–15/11, 8 pts) · S3 (16/11–29/11, 8 pts) · S4 (30/11–11/12, 8 pts).

| # | HU | Historia de Usuario Oficial (Texto del FGAP040) | Criterios de Aceptación Verificables | Prioridad | Pts | Sprint |
|---|---|---|---|---|:---:|:---:|
| 1 | **HU01** | Como Administrador de la plataforma (Jorge), quiero cargar un archivo de video industrial (.mp4 o .avi) al sistema, para iniciar el flujo de procesamiento visual. | • Acepta formatos .mp4 y .avi; otros formatos arrojan error validado.<br>• Muestra nombre del archivo, duración exacta, resolución y FPS. | **Must** | 1 | **1** |
| 2 | **HU02** | Como Administrador de la plataforma (Jorge), quiero que el sistema fragmente el video en fotogramas individuales (frames) normalizados, para prepararlos para la inferencia espacial. | • Extrae y almacena fotogramas numerados secuencialmente.<br>• Normaliza las dimensiones de imagen al tamaño requerido por YOLOv8. | **Must** | 2 | **1** |
| 3 | **HU03** | Como Supervisora de SST (Mariana), quiero que el sistema detecte la presencia de operarios en cada frame mediante YOLOv8, para localizar las zonas donde se desarrollan actividades humanas en el taller. | • Infiere cajas delimitadoras de la clase «persona» con confianza asociada.<br>• Muestra vista previa del frame con cajas y porcentajes superpuestos. | **Must** | 4 | **1** |
| 4 | **HU04** | Como Administrador de la plataforma (Jorge), quiero que el sistema descarte automáticamente los fotogramas sin trabajadores detectados, para optimizar la carga computacional y eliminar tiempo muerto. | • Los fotogramas sin detecciones positivas son excluidos de la secuencia.<br>• Registra en log: total de frames entrantes vs. conservados y % de reducción. | **Must** | 2 | **2** |
| 5 | **HU05** | Como Supervisora de SST (Mariana), quiero agrupar los frames activos filtrados en clips de tamaño fijo, para estructurar la entrada al modelo de inferencia temporal. | • Genera secuencias continuas de N frames consecutivos (configurable).<br>• Estructura tensor de entrada compatible con el clasificador ConvLSTM. | **Must** | 3 | **2** |
| 6 | **HU07** | Como Supervisora de SST (Mariana), quiero procesar el clip segmentado mediante ConvLSTM, para extraer características de movimiento y dependencias temporales. | • Ejecuta inferencia espacio-temporal sobre el split oficial de prueba.<br>• Arroja vector de probabilidades normalizado para cada secuencia. | **Must** | 5 | **3** |
| 7 | **HU08** | Como Supervisora de SST (Mariana), quiero que el modelo clasifique el comportamiento como seguro o inseguro y tipifique la conducta (pasarela peatonal o tablero de control), para registrar el diagnóstico claro del acto en planta. | • Asigna etiqueta de riesgo y tipo de conducta observada por clip.<br>• Computa métricas formales: Accuracy, Precision, Recall y F1 por clase. | **Must** | 3 | **3** |
| 8 | **HU09** | Como Operadora de monitoreo (Lucía), quiero visualizar el video reproduciéndose en la interfaz con un recuadro de color indicando el nivel de riesgo (verde: seguro, rojo: riesgo), para validar visualmente la inferencia. | • Recuadro dinámico superpuesto en verde (seguro) y rojo (inseguro).<br>• Permite reproducir, pausar y revisar clips de video del lote cargado. | **Must** | 4 | **4** |
| 9 | **HU10** | Como Operadora de monitoreo (Lucía), quiero que se active una alerta inmediata ante una conducta insegura con registro de hora y captura de evidencia, para intervenir oportunamente. | • Dispara notificación visual y sonora destacada ante actos inseguros.<br>• Persiste evento con fecha, timestamp en video, clip y probabilidad. | **Should** | 2 | **4** |
| 10 | **HU12** | Como Gerente de operaciones (Ricardo) y Administrador (Jorge), quiero visualizar el log de tiempos de procesamiento y métricas de aceleración, para evaluar la eficiencia técnica y el ahorro de cómputo obtenido. | • Presenta tiempos discriminados por fase (ingesta, YOLOv8, ConvLSTM).<br>• Despliega comparativa de tiempo total con reducción vs. sin reducción. | **Should** | 2 | **4** |
| 11 | **HU06** | Como Supervisora de SST (Mariana), quiero descartar clips que no cumplan con una ventana de tiempo mínima de acción, para evitar alertas falsas por movimientos fugaces. | • Clips con duración inferior al umbral temporal mínimo son descartados.<br>• Registra cantidad de fragmentos descartados por duración insuficiente. | **Should** | 2 | **2** |
| 12 | **HU11** | Como Administrador de la plataforma (Jorge), quiero modificar el umbral de confianza (confidence) de YOLOv8 desde la interfaz de configuración sin alterar código, para calibrar la sensibilidad del filtrado espacial según la iluminación de la nave. | • Ajuste de umbral mediante interfaz gráfica (rango 0.0 a 1.0).<br>• Validación de límites numéricos y registro del cambio en log de auditoría. | **Could** | 1 | **2** |

---

## Tareas Detalladas del Sprint 1 (Alcance Inmediato de Luis Salazar)
* **HU01 (Carga de Video):** Pantalla web de carga con validación de extensiones `.mp4`/`.avi` $\rightarrow$ Extractor de metadatos (duración, resolución, fps).
* **HU02 (Extracción de Frames):** Módulo de decodificación OpenCV $\rightarrow$ Redimensionamiento estándar $\rightarrow$ Guardado secuencial en directorio de trabajo.
* **HU03 (Detección YOLOv8):** Integración de `ultralytics` (`yolov8n.pt`) $\rightarrow$ Inferencia de la clase `person` por fotograma $\rightarrow$ Renderizado de bounding boxes de prueba.

## Coherencia y Reglas del Backlog
1. **Asignación de HU11 al Sprint 2:** HU11 es clasificada como *Could have* por MoSCoW, pero se implementa en el Sprint 2 por dependencia técnica ineludible: calibra el detector de HU03 y el filtro de HU04.
2. **Criterios de Aceptación vs. DoD:** Los criterios detallados en esta tabla son específicos de cada historia; la Definition of Done (DoD) común a todo el incremento se rige bajo los estándares de calidad del FGAP070.
