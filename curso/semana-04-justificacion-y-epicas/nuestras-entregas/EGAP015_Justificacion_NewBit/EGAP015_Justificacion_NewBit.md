# EGAP015 – Justificación del Proyecto: NewBit (Versión Oficial Normalizada)

- **Archivos para entregar** (esta carpeta): `EGAP015_Justificacion_NewBit.pdf` (3 págs.) y `EGAP015_Justificacion_NewBit.docx`.
- **Formato:** Las 10 secciones oficiales del EGAP015 del docente (datos generales, necesidad, justificación tecnológica, operativa, económica, social, académica, beneficios, viabilidad y conclusión).
- **Fecha de normalización:** 17/10/2026 · versión 2.0 (Grupo D3).
- **Coherencia matemática y conceptual:** Mismo código **PY-NB-001**, título oficial canónico, entorno de **taller de manufactura metalmecánica**, equipo Scrum y presupuesto exacto de **S/ 20,768**.

## Resumen Ejecutivo de la Justificación
| Sección del Formato | Contenido Normalizado |
|---|---|
| **1. Datos generales** | **PY-NB-001 – Sistema web con Visión Artificial para la detección de actos inseguros en áreas operativas de manufactura metalmecánica** *(NewBit)* · Taller de Manufactura Metalmecánica / Maestranza Industrial (caso académico), área SST · PO Albert Chumacero, SM Anthony Lopez, Developers Anthony Lopez y Luis Salazar · Scrum, 4 sprints de 2 semanas. |
| **2. Situación o necesidad** | En naves metalmecánicas (tornos, prensas, ensamblaje), las inspecciones de SST son intermitentes y las cámaras de seguridad graban pasivamente sin emitir alertas. Los actos inseguros (invasión de pasillos peatonales demarcados y manipulación de tableros eléctricos de máquinas dejándolos abiertos) se identifican tardíamente. Cumplimiento proactivo de la Ley 29783. |
| **3. Justificación tecnológica** | Arquitectura híbrida en dos etapas: **YOLOv8** como detector espacial modernizado de alta velocidad para extraer operarios en frames, seguido de un filtro de reducción temporal que descarta hasta el 75% de fotogramas inactivos, y **ConvLSTM** para capturar dependencias temporales y clasificar el acto. Entorno 100% Python/FastAPI con OpenCV y dataset público validado (Önal y Dandıl, 2024, CC BY 4.0). |
| **4. Justificación operativa** | Flujo de trabajo dividido entre roles reales (FGAP030): Jorge (TI) administra la ingesta y umbrales, Mariana (SST) analiza incidentes tipificados y Lucía (Monitoreo) supervisa las alertas arrojadas por los lotes procesados. Interfaz web intuitiva que asiste y fortalece la decisión humana sin pretender reemplazar a los inspectores. |
| **5. Justificación económica** | **S/ 20,768** en estricta coincidencia con el Acta (FGAP010). Desglose: dedicación valorizada del equipo Scrum (Albert 100 h a S/ 40, Anthony 200 h a S/ 38, Luis 200 h a S/ 35 = S/ 18,600) + S/ 280 gastos directos de hosting/cloud + S/ 1,888 (10% contingencia). No se prometen ahorros económicos ficticios sin sustento empírico. |
| **6. Justificación social / SST** | Prevención de accidentes graves y atrapamientos en naves de mecanizado; cultura de seguridad preventiva; protección de datos y privacidad por diseño (sin reconocimiento facial ni seguimiento biométrico fuera del horario de labor). |
| **7. Justificación académica** | Aplicación rigurosa de Scrum según SBOK (4.ª ed.), ingeniería de requisitos, visión artificial con Deep Learning, desarrollo web estructurado, pruebas cruzadas y ética en IA. |
| **8. Beneficios esperados** | **Tangibles:** Plataforma web funcional, pipeline de reducción de frames integrado, detector YOLOv8 calibrado, reportes de auditoría y métricas. **Intangibles:** Reducción de fatiga de revisión visual en SST y mayor disciplina operativa en pasillos seguros. |
| **9. Viabilidad inicial** | Técnica, operativa y económica confirmada. Se declaran explícitamente las restricciones del prototipo: procesamiento por lotes de archivos de video (.mp4/.avi) y evaluación sobre 2 conductas priorizadas. |
| **10. Conclusión** | El proyecto es técnica y económicamente viable, aborda una necesidad crítica en talleres de manufactura con una solución tecnológica moderna y respeta los estándares del curso. |

## Análisis y Conformidad con la Rúbrica
- **Coherencia de Costos:** Coincidencia matemática absoluta con el Acta: el monto de **S/ 20,768** es idéntico al céntimo en ambos documentos.
- **Fundamentación Científica y Ética:** Se incluye formalmente como antecedente y fuente de validación el trabajo de Önal y Dandıl (2024) y la licencia CC BY 4.0, garantizando transparencia académica ante el docente.
