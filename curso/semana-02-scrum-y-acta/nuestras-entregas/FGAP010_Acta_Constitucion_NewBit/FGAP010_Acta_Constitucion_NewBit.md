# FGAP010 – Acta de Constitución: NewBit (versión 1.0)

- **Archivos para entregar** (esta carpeta): `FGAP010_Acta_Constitucion_NewBit.pdf` (5 págs., exportado con Pages; para subir al Drive) y `FGAP010_Acta_Constitucion_NewBit.docx` (editable). Formato EGAP/FGAP010 del docente; se usó como plantilla el Acta de VIGIA (mismas tablas, encabezado y estilos).
- **Fecha:** 12/10/2026 · **Estado:** completa, **sin pendientes** (decisiones confirmadas por el equipo el 12/10).
- **Enfoque de redacción:** NewBit se presenta como proyecto propio. Unsafe-Net no se menciona; solo se cita el **dataset** (autores, DOI y licencia CC BY 4.0), porque su licencia exige atribución y en una revisión académica los datos ajenos deben citarse.

## Resumen
| Sección | Contenido |
|---|---|
| Código y nombre | PY-NB-001 – NewBit: plataforma de Computer Vision que convierte cámaras existentes en sensores inteligentes configurables para operaciones industriales |
| Visión | Cámaras existentes → sensores inteligentes; primera capacidad: detectar conductas inseguras con YOLOv4 + ConvLSTM y alertar en segundos; vigilancia continua para el supervisor de SST; apoya la decisión humana; privacidad por diseño |
| Requisitos | RF-01…RF-07 + no funcionales (reproducibilidad, split oficial, métricas por clase, atribución CC BY 4.0, sin reconocimiento facial) |
| Alcance | 2 conductas: tránsito fuera de la vía peatonal y panel eléctrico abierto (arquitectura preparada para más) · dataset de Mendeley citado · comparación clasificación directa vs pipeline completo |
| Fuera de alcance | Instalación en planta, cámaras en vivo, alertas físicas, reconocimiento facial, certificación de SST |
| Riesgos | 7: ajuste del modelo temporal, implementación propia, GPU, etiquetado, disco, cambio de entorno, SM que también es Developer |
| Hitos | Inicio 05–16/10 · **4 sprints** (19/10–11/12) · cierre 14–18/12/2026 |
| Presupuesto | **S/ 20,768**: Albert 100 h × S/ 40, Anthony 200 h × S/ 38, Luis 200 h × S/ 35 (S/ 18,600) + S/ 280 de gasto + 10 % de contingencia |
| Interesados | Albert Sebastian Chumacero Chávarry (PO), Anthony Gabriel Lopez Yrribarren (SM + Dev), Luis Fernando Salazar Diaz (Dev); Sponsor Ricardo Salcedo, SST Mariana Torres y TI Jorge Ponce (ficticios); docente; supervisores y trabajadores |
| Aprobación | 6 criterios técnicos (pipeline completo, etapas separadas, reducción de frames, comparación, documentación, reproducibilidad); metas fijadas con la línea base del Sprint 3 |
| Culminación | Normal · alcance reducido (1 conducta) · cancelación |
| PO / Sponsor | Albert Sebastian Chumacero Chávarry / Ricardo Salcedo Paredes, SIDERPERU (caso académico) |

## Análisis
- Primer entregable de la secuencia. Los formatos siguientes deben repetir **el mismo nombre, alcance, equipo y presupuesto (S/ 20,768)**.
- Si el docente pregunta por la base técnica, el enfoque YOLO + ConvLSTM y el dataset vienen de la literatura (Önal y Dandıl, 2024). Conviene citarlos como antecedente en la Justificación (EGAP015).
- Se corrigieron dos defectos heredados de la plantilla: los títulos grises de 5 tablas ahora ocupan todo el ancho, y la columna Fecha del control de versiones es más ancha (Pages la ocultaba).
- El encabezado dice "EGAP010", heredado de la plantilla; la Secuencia de avances lo llama FGAP010.
