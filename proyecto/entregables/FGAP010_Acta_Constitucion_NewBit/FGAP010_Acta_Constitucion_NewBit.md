# FGAP010 – Acta de Constitución: NewBit (borrador 1.0)

- **Archivo para entregar:** `FGAP010_Acta_Constitucion_NewBit.docx` (esta carpeta). Formato EGAP/FGAP010 del docente; se usó como plantilla el Acta de VIGIA (mismas tablas, encabezado y estilos).
- **Fecha:** 12/10/2026 · **Estado:** borrador para revisar con el equipo. Lo pendiente está **resaltado en amarillo** con "POR CONFIRMAR" dentro del Word.
- **Fuentes del contenido:** `../../semana-05/UnsafeNet_Research_Pack/` (requisitos RF-01…RF-07 del archivo 11, criterios de éxito del 12, alcance del 10, dataset del 04) y decisiones de `proyecto/README.md`.

## Resumen de lo que dice
| Sección | Contenido |
|---|---|
| Código y nombre | PY-NB-001 – NewBit: plataforma de Computer Vision que convierte cámaras existentes en sensores inteligentes configurables para operaciones industriales |
| Visión | NewBit, plataforma de Computer Vision para operaciones industriales; primera capacidad: detectar conductas inseguras replicando a pequeña escala la investigación Unsafe-Net (YOLOv4 filtra frames → ConvLSTM clasifica) con interfaz, registro y alerta; apoyo al supervisor de SST, no lo reemplaza |
| Requisitos | RF-01…RF-07 + no funcionales (reproducibilidad, split oficial, métricas por clase, CC BY 4.0, sin reconocimiento facial) |
| Alcance | 2 conductas (Safe Walkway Violation, Opened Panel Cover), dataset de Mendeley, comparación línea base vs YOLOv4 + ConvLSTM |
| Fuera de alcance | Planta real, cámaras en vivo, hardware de alerta, reconocimiento facial, certificación de SST, perseguir el 95.81 % |
| Riesgos | Parámetros incompletos, sin código oficial, GPU, etiquetado, disco, cambio de dominio, SM que también es Developer |
| Hitos | Acta 05–16/10 · **4 sprints** de 2 semanas (19/10–11/12) · entrega y cierre 14–18/12/2026 |
| Presupuesto | **S/ 19,558** (S/ 17,500 de horas valorizadas: Albert 100 h, Anthony 200 h y Luis 200 h, a S/ 35; S/ 280 de gasto en efectivo; 10 % de contingencia) |
| Interesados | Equipo Scrum real: Albert Sebastian Chumacero Chávarry (PO), Anthony Gabriel Lopez Yrribarren (SM + Dev), Luis Fernando Salazar Diaz (Dev). Ficticios del caso: Sponsor Ricardo Salcedo, SST Mariana Torres, TI Jorge Ponce. Docente, supervisores y trabajadores |
| Aprobación | Los 7 criterios de éxito de la réplica (pipeline completo, comparación, reproducibilidad…); no se exige el 95.81 % |
| Culminación | Normal · con alcance reducido (1 conducta) · cancelación |
| PO / Sponsor | Albert Sebastian Chumacero Chávarry / Ricardo Salcedo Paredes, SIDERPERU (caso propuesto) |

## POR CONFIRMAR (marcado en amarillo en el Word)
1. Conductas (2, o las 4).
2. Fechas, según el calendario del semestre.
3. Tarifas y precios.
4. Organización del caso (SIDERPERU propuesta) y si se mantienen los interesados ficticios de VIGIA (Sponsor, SST, TI).

Resuelto el 12/10: equipo de 3 con roles definidos, 4 sprints y nombre **NewBit** (título tomado de las presentaciones de la semana 3: `archivo/vigia-industrial/semana-03/`).

## Análisis
- Primer entregable de la secuencia (paso 1). Roles, Épicas, Justificación y Criterios de Terminado deben repetir **el mismo nombre, alcance, equipo y presupuesto**.
- El presupuesto bajó de S/ 30,820 (VIGIA) a S/ 19,558 porque no hay hardware de planta ni instalación: el dataset es público y el cómputo se alquila por horas.
- Código PY-NB-001, siguiendo la convención del docente (PY-RD-001 en el ejemplo). "Unsafe-Net" aparece solo como investigación base, no como nombre del proyecto.
- Encabezado: dice "EGAP010" (heredado de la plantilla); la Secuencia de avances lo llama FGAP010. Cambiarlo si el docente lo pide.
