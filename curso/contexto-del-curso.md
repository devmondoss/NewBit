# Contexto del curso – Ingeniería de Software II

Resumen para consulta rápida. Cada semana tiene su carpeta `semana-XX-<tema>/` con `material-del-profe/` (lo que mandó el docente) y `nuestras-entregas/` (lo que entregó el Grupo D3); dentro, **una carpeta por archivo** (original + `.md` del mismo nombre). La investigación y el código del proyecto NewBit van aparte, en `../proyecto-newbit/`.

## Datos del curso
- **Asignatura:** Ingeniería de Software II · Escuela de Ing. de Sistemas e Informática · Facultad de Ingeniería · Universidad Nacional del Santa (UNS)
- **Semestre:** 2026-II · **Docente:** Dr. Ing. Alfredo Daza Vergaray
- **Enfoque:** Scrum aplicado a un proyecto de software del equipo. Los documentos de gestión se entregan en formatos con código (EGAP/FGAP).
- **Libro base:** *Guía de los Fundamentos de Scrum (Guía del SBOK®)*, 4.ª ed., SCRUMstudy (2022). El docente basa sus clases en él. Ficha, capítulos y dónde está cada formato: `referencias/libro-guia-sbok/`.

## Calendario y material por semana
| Semana | Fechas | Qué se vio / pidió | Material del profe |
|---|---|---|---|
| 1 | 14–20/09 | Sin actividad | — |
| 2 | 21–27/09 | **Principios de Scrum** (teoría + actividad). **Acta de Constitución** (EGAP010) | `semana-02-scrum-y-acta/material-del-profe/`: principios Scrum, plantilla y ejemplo de Acta |
| 3 | 28/09–04/10 | **Roles y Prototipos** (FGAP030/EGAP030). Tareas: infografía de 12 pasos, PPT de presentación y diagrama de flujo de la arquitectura | `semana-03-roles-y-prototipos/material-del-profe/`: plantilla y ejemplo de Roles |
| 4 | 05–11/10 | **Laboratorio 4:** Justificación del proyecto (EGAP015) y Épicas e historias de usuario (FGAP040) | `semana-04-justificacion-y-epicas/material-del-profe/`: formato de Justificación y Épicas de ejemplo |
| 5 | 12–18/10 | **Responsabilidad Social Universitaria (RSU):** Reglamento UNS (Res. 448-2023-CU-R-UNS) y dos proyectos RSU de ejemplo (instrucción **por confirmar**). **Secuencia de avances:** hoja de ruta de formatos FGAP010 → FGAP090 | `semana-05-rsu-y-backlog/material-del-profe/`: reglamento, ejemplos RSU, secuencia, FGAP070, **libro base (Guía del SBOK)**, clase de Justificación de negocio (12/10), FGAP060 de ejemplo. Lecturas generales (19/10) en `curso/`: Historias de usuario (Scrum Manager) y EXIN Agile Scrum Master sesiones 1–2 |
| **6** | **19–25/10 (actual)** | **Producto de la Unidad I:** informe con carátula, índice, introducción, antecedentes, marco teórico, desarrollo (todos los formatos) y referencias, más PPT (pedido por mensaje el 19/10) | Sin archivo: el pedido está transcrito en `semana-06-producto-unidad-1/README.md` |

## Qué enseñó cada semana
- **Semana 2 – Scrum:** control empírico (transparencia, inspección, adaptación), autoorganización, colaboración, priorización por valor (valor · riesgo · dependencias), time-boxing (sprint 1–4 semanas; daily 15 min), desarrollo iterativo (épicas → historias), Scrum vs cascada. Actividad: cuadro comparativo de los principios con un ejemplo práctico (sin evidencia de entrega en el repo).
- **Semana 2 – Acta (EGAP010):** 12 secciones: código y nombre · visión · requisitos · alcance, límites y entregables · riesgos · cronograma de hitos · recursos financieros · interesados · requisitos de aprobación · criterios de culminación · Product Owner · sponsor.
- **Semana 3 – Roles y Prototipos:** personas (user personas): rol, frecuencia de uso, experticia con el tema, proficiencia con computadoras y con el software, metas y prototipo (quién es, qué hace, estilo de vida).
- **Semana 4 – Justificación (EGAP015):** 10 apartados: datos generales · necesidad · justificación tecnológica, operativa, económica, social/clínica y académica · beneficios (tangibles e intangibles) · viabilidad · conclusión. **Épicas (FGAP040):** épicas con "Como [rol], yo debería… a fin de…" y su relación con historias de usuario.
- **Semana 5 – RSU:** el reglamento de la UNS exige que los proyectos de RSU estén ligados a la carrera (Art. 6.6), tengan 1 docente responsable + hasta 8 estudiantes colaboradores (Art. 9), no se ejecuten sin resolución (Art. 16), se informen en ≤ 15 días (Art. 18) y usen APA. Estructura del proyecto (Anexo 1): datos generales · justificación (legal, importancia, antecedentes) · problemática y objetivos · metodología · cronograma (Gantt) · presupuesto · estrategias · referencias. Los ejemplos son talleres de ~1 mes en colegios de Nuevo Chimbote, 30–40 beneficiarios, < S/ 150, con encuesta pre/post.
- **Semana 5 – Secuencia de avances:** el proyecto sigue 7 pasos: FGAP010 Acta → **FGAP020 Registro de Stakeholders** → FGAP030 Roles y Prototipos → FGAP040 Épicas → FGAP060 Backlog priorizado + FGAP070 Criterios de Terminado → Sprints (planificación, implementación, revisión, retrospectiva) → FGAP090 Cierre. La Justificación (EGAP015) no figura en la secuencia.
- **Semana 5 – FGAP070 Criterios de Terminado:** la Definition of Done común a todas las historias: prueba unitaria, prueba integrada, revisión por pares, certificación (aquí: no aplica, no afirmar validación), documentación (para IA: dataset, preprocesamiento, modelo, métricas), aprobaciones técnicas (Developers) y administrativas (PO; no sustituye la DoD), otras.

## Ejemplos y plantillas del docente
Los archivos de **BigFarma** (Acta, Roles, de 2018), de **Retinopatía Diabética** (Acta, Roles, Justificación, Épicas) y los dos **proyectos RSU de 2025** (semana 5) son **ejemplos del docente**, no del equipo. Las instrucciones de los labs lo dicen: *revise el ejemplo, desarrolle lo de su propio proyecto, no copie el ejemplo*.

## Convenciones del docente
- **Épica:** "Como [rol], yo debería [requerimiento], a fin de [beneficio]". **Historia:** "Como [rol], quiero [funcionalidad], para [beneficio]"; no demasiado general.
- Mantener coherencia entre documentos: Acta → Roles → Justificación → Épicas → Product Backlog; mismo nombre, alcance, organización y equipo.
- No afirmar beneficios, ahorros ni resultados que no estén demostrados. Si el presupuesto aparece en la Justificación, debe coincidir con el Acta.
- El docente puede pedir que cualquier integrante sustente oralmente cualquier apartado.
- El ejemplo asume un Scrum Team de **1 Product Owner + 1 Scrum Master + 3 Developers**.

## Entregables que pide el curso
El avance de cada entregable **para NewBit** se sigue en [`proyecto-newbit/README.md`](../proyecto-newbit/README.md) y en la hoja de ruta central [`roadmap-reestructuracion.md`](../proyecto-newbit/gestion/roadmap-reestructuracion.md). Estado actual consolidado:

| Entregable | Semana | Estado para NewBit |
|---|---|---|
| 1 · Acta de Constitución (FGAP/EGAP010) | 2 | **Completada v2.0:** [`semana-02/FGAP010_Acta_Constitucion_NewBit/`](semana-02-scrum-y-acta/nuestras-entregas/FGAP010_Acta_Constitucion_NewBit/FGAP010_Acta_Constitucion_NewBit.md) (dominio taller metalmecánico, YOLOv8, S/ 20,768) |
| Cuadro comparativo de principios de Scrum | 2 | **Completado v2.0:** [`semana-02/Cuadro_Principios_Scrum_NewBit/`](semana-02-scrum-y-acta/nuestras-entregas/Cuadro_Principios_Scrum_NewBit/Cuadro_Principios_Scrum_NewBit.md) (ejemplos adaptados y HU11 sincronizada en Sprint 2) |
| 2 · Registro de Stakeholders (FGAP020) | 6 | **v1.0 dentro del Producto de la Unidad I** (sección 4.3), sin plantilla oficial del docente |
| 3 · Roles y Prototipos (FGAP/EGAP030) | 3 | **Completado v2.0:** [`semana-03/FGAP030_Roles_y_Prototipos_NewBit/`](semana-03-roles-y-prototipos/nuestras-entregas/FGAP030_Roles_y_Prototipos_NewBit/FGAP030_Roles_y_Prototipos_NewBit.md) (5 perfiles de planta aprobados) |
| Diagrama de arquitectura y PPT NewBit | 3 | **Completado v1.0:** [`semana-03/Diagrama_Arquitectura_NewBit/`](semana-03-roles-y-prototipos/nuestras-entregas/Diagrama_Arquitectura_NewBit/Diagrama_Arquitectura_NewBit.md) y [`semana-03/PPT_Presentacion_NewBit/`](semana-03-roles-y-prototipos/nuestras-entregas/PPT_Presentacion_NewBit/PPT_Presentacion_NewBit.md) |
| Infografía de 12 pasos del proyecto | 3 | **Completada v1.0:** [`semana-03/Infografias_NewBit/`](semana-03-roles-y-prototipos/nuestras-entregas/Infografias_NewBit/Infografias_NewBit.md) (página web HTML/CSS con metodología del proyecto) |
| Justificación del proyecto (EGAP015) | 4 | **Completada v2.0:** [`semana-04/EGAP015_Justificacion_NewBit/`](semana-04-justificacion-y-epicas/nuestras-entregas/EGAP015_Justificacion_NewBit/EGAP015_Justificacion_NewBit.md) (S/ 20,768, viabilidad técnica, citas Önal & Dandıl 2024) |
| 4 · Épicas e historias de usuario (FGAP040) | 4 | **Completado v2.0 canónico:** [`semana-04/FGAP040_Epicas_NewBit/`](semana-04-justificacion-y-epicas/nuestras-entregas/FGAP040_Epicas_NewBit/FGAP040_Epicas_NewBit.md) (6 épicas, 12 HU con roles de planta reales) |
| Proyecto de RSU (Anexo 1 del reglamento) | 5 | **Por confirmar** si se pide y cuándo formalizarlo ante el docente |
| 5 · Backlog priorizado (FGAP060) | 5 (secuencia) | **Completado v2.0:** [`semana-05/Tablero_Kanban_NewBit/`](semana-05-rsu-y-backlog/nuestras-entregas/Tablero_Kanban_NewBit/Tablero_Kanban_NewBit.md) y [`semana-05/Priorizacion_MoSCoW_100_Puntos_NewBit/`](semana-05-rsu-y-backlog/nuestras-entregas/Priorizacion_MoSCoW_100_Puntos_NewBit/Priorizacion_MoSCoW_100_Puntos_NewBit.md) |
| Estimación: Puño de cinco (Fist of Five) | 5 | **Completada v2.0:** [`semana-05/Presentacion_Fist_of_Five/`](semana-05-rsu-y-backlog/nuestras-entregas/Presentacion_Fist_of_Five/Presentacion_Fist_of_Five.md) (8 diapositivas con votación de las 12 HU) |
| 5 · Criterios de Terminado (FGAP070) | 5 | **Completado v1.0:** [`semana-05/FGAP070_Criterios_de_Terminado_NewBit/`](semana-05-rsu-y-backlog/nuestras-entregas/FGAP070_Criterios_de_Terminado_NewBit/FGAP070_Criterios_de_Terminado_NewBit.md) (DoD canónica en Word, PDF y MD) |
| 6 · Sprints (planificación, implementación, revisión) | – | **En desarrollo activo:** alcance de código enfocado en Sprint 1 y Sprint 2 (15 puntos de historia) |
| **Producto de la Unidad I** (informe + PPT) | 6 | **Completado v2.0:** [`semana-06/Producto_Unidad_1_NewBit/`](semana-06-producto-unidad-1/nuestras-entregas/Producto_Unidad_1_NewBit/Producto_Unidad_1_NewBit.md) (LaTeX, APA 7, 37 págs., anclado a la Guía SBOK, desarrollo semana por semana) y [`semana-06/PPT_Producto_Unidad_1_NewBit/`](semana-06-producto-unidad-1/nuestras-entregas/PPT_Producto_Unidad_1_NewBit/PPT_Producto_Unidad_1_NewBit.md) (PowerPoint editable, 19 diap.). Incluye **FGAP020 v1.0**, **definición de listo** y planificación de la liberación |
| 7 · Cierre del Proyecto (FGAP090) | – | Previsto para el final del semestre |

## Precisiones y Consultas para el Docente
1. **Composición del equipo (3 integrantes):** El Scrum Team está conformado por Albert Chumacero (PO), Anthony Lopez (SM y Developer) y Luis Salazar (Developer). Las estimaciones y compromisos de sprint están calibrados para esta capacidad.
2. **Pivote metodológico cerrado:** La transición de VIGIA (acería pesada) a NewBit (taller metalmecánico con visión artificial offline y dataset Mendeley) ha quedado 100% normalizada en todos los formatos FGAP/EGAP.
3. **RSU (semana 5):** Mantener en consulta si se requerirá redactar un proyecto de RSU independiente o si se vinculará con la difusión de seguridad laboral asistida por IA.
4. **Secuencia documental:** Continuar usando la estructura canónica FGAP010 → FGAP030 → FGAP040 → FGAP060/070, asegurando consistencia de datos en cada revisión.
