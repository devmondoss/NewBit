# FGAP010 – Acta de Constitución: NewBit (Versión Oficial Normalizada)

- **Archivos para entregar** (esta carpeta): `FGAP010_Acta_Constitucion_NewBit.pdf` (5 págs.) y `FGAP010_Acta_Constitucion_NewBit.docx` (editable). Formato FGAP010 del docente.
- **Fecha de normalización:** 17/10/2026 · **Versión:** 2.0 (Grupo D3).
- **Estado:** Completa y normalizada según Decisiones D-01, D-02 y D-03.
- **Enfoque de redacción:** Proyecto presentado bajo el marco de desarrollo de software formal de la UNS. La inferencia espacial se moderniza a **YOLOv8** y se cita con rigor el dataset público de referencia (Önal y Dandıl, 2024, DOI `10.17632/xjmtb22pff.1`, licencia CC BY 4.0).

## Resumen Ejecutivo
| Sección | Contenido Normalizado |
|---|---|
| **Código y nombre** | **PY-NB-001 – Sistema web con Visión Artificial para la detección de actos inseguros en áreas operativas de manufactura metalmecánica** *(Plataforma NewBit)* |
| **Visión** | Transformar el registro pasivo de cámaras de videovigilancia de talleres de manufactura en un sistema de detección temprana de actos inseguros; primera capacidad: detección espacial de operarios con YOLOv8 y clasificación temporal con ConvLSTM a partir de lotes de video industrial; apoyo a la decisión del supervisor de SST; privacidad por diseño. |
| **Requisitos** | RF-01 a RF-07 (carga de videos, extracción de frames, inferencia espacial, filtrado inteligente, clasificación temporal, alertas y auditoría) + Requisitos no funcionales (reproducibilidad, split oficial de validación, métricas por clase, atribución CC BY 4.0, sin reconocimiento facial). |
| **Alcance** | 2 conductas de riesgo priorizadas: tránsito fuera de la vía peatonal y panel de máquina/control abierto (arquitectura extensible a más actos); procesamiento sobre clips de video en formatos .mp4 y .avi; evaluación comparativa (clasificación directa vs. pipeline con reducción de frames). |
| **Fuera de alcance** | Instalación física en planta, cámaras en vivo vía RTSP continuo, actuadores/alertas físicas en planta, reconocimiento facial de trabajadores, certificación médica o regulatoria formal de SST. |
| **Riesgos** | 7 riesgos identificados: ajuste del modelo temporal, reproducibilidad de pesos, consumo de GPU/recursos, iluminación y oclusiones en taller, espacio en disco para frames, transferibilidad de dominio y Scrum Master con doble rol (SM + Developer). |
| **Hitos del Cronograma** | Fase de Inicio (05–16/10) · **4 Sprints** de 2 semanas (19/10–11/12/2026) · Cierre y sustentación (14–18/12/2026). |
| **Presupuesto** | **S/ 20,768**: Albert 100 h × S/ 40 (S/ 4,000), Anthony 200 h × S/ 38 (S/ 7,600), Luis 200 h × S/ 35 (S/ 7,000) $\rightarrow$ Subtotal RRHH: S/ 18,600 + Gastos directos operativos: S/ 280 + Contingencia (10%): S/ 1,888. |
| **Interesados clave** | **Equipo Scrum:** Albert Chumacero (PO), Anthony Lopez (SM + Dev), Luis Salazar (Dev). **Interesados de negocio:** Ricardo Salcedo (Gerente de Operaciones / Sponsor), Mariana Torres (Supervisora de SST), Jorge Ponce (Administrador TI), Lucía Ramos (Operadora de Monitoreo). **Académicos:** Dr. Ing. Alfredo Daza Vergaray (Docente). |
| **Criterios de Aprobación** | Pipeline completo integrado, separación modular espacial/temporal, demostración de reducción de frames ($\ge 60\%$), reproducibilidad técnica y documentación de métricas (Accuracy, Precision, Recall, F1). |
| **Criterios de Culminación** | Cumplimiento de criterios de aceptación del Backlog en los 4 sprints; cierre formal con entrega del incremento de software probado. |
| **Product Owner / Sponsor** | Albert Sebastian Chumacero Chávarry (PO) / Ricardo Salcedo Paredes (Gerente de Operaciones, Taller de Manufactura Metalmecánica / Maestranza Industrial, caso académico). |

## Análisis y Coherencia
- Primer entregable de la secuencia del curso (FGAP010). Todos los formatos siguientes ([FGAP030](file:///c:/Users/luisf/OneDrive/Escritorio/Proyectos/IngSoftware/NewBit/curso/semana-03-roles-y-prototipos/nuestras-entregas/FGAP030_Roles_y_Prototipos_NewBit/FGAP030_Roles_y_Prototipos_NewBit.md), [EGAP015](file:///c:/Users/luisf/OneDrive/Escritorio/Proyectos/IngSoftware/NewBit/curso/semana-04-justificacion-y-epicas/nuestras-entregas/EGAP015_Justificacion_NewBit/EGAP015_Justificacion_NewBit.md), [FGAP040](file:///c:/Users/luisf/OneDrive/Escritorio/Proyectos/IngSoftware/NewBit/curso/semana-04-justificacion-y-epicas/nuestras-entregas/FGAP040_Epicas_NewBit/FGAP040_Epicas_NewBit.md)) mantienen **el mismo código (PY-NB-001), título, entorno de manufactura metalmecánica, equipo y presupuesto idéntico (S/ 20,768)**.
- El alcance técnico declara con honestidad académica el procesamiento de videos por lotes, garantizando que el software desarrollado sea 100% defendible sin simular conectividad RTSP que no existe.
