# Contexto del curso – Ingeniería de Software II

Resumen para consulta rápida. Cada semana tiene su carpeta en `docs/semana-XX/` y dentro **una carpeta por archivo** (original + `.md` del mismo nombre). El trabajo del equipo (proyecto Unsafe-Net) va aparte, en `proyecto/` en la raíz del repo.

## Datos del curso
- **Asignatura:** Ingeniería de Software II · Escuela de Ing. de Sistemas e Informática · Facultad de Ingeniería · Universidad Nacional del Santa (UNS)
- **Semestre:** 2026-II · **Docente:** Dr. Ing. Alfredo Daza Vergaray
- **Enfoque:** Scrum aplicado a un proyecto de software del equipo. Los documentos de gestión se entregan en formatos con código (EGAP/FGAP).
- **Libro base:** *Guía de los Fundamentos de Scrum (Guía del SBOK®)*, 4.ª ed., SCRUMstudy (2022). El docente basa sus clases en él. Ficha, capítulos y dónde está cada formato: `semana-05/Guia_SBOK_Fundamentos_de_Scrum_4ta_edicion/`.

## Calendario y material por semana
| Semana | Fechas | Qué se vio / pidió | Material (`docs/…`) |
|---|---|---|---|
| 1 | 14–20/09 | Sin actividad | `semana-01/README.md` |
| 2 | 21–27/09 | **Principios de Scrum** (teoría + actividad). **Acta de Constitución** (EGAP010) | `semana-02/`: principios Scrum, plantilla y ejemplo de Acta |
| 3 | 28/09–04/10 | **Roles y Prototipos** (FGAP030/EGAP030). Tareas: infografía de 12 pasos, PPT de presentación y diagrama de flujo de la arquitectura | `semana-03/`: plantilla y ejemplo de Roles |
| 4 | 05–11/10 | **Laboratorio 4:** Justificación del proyecto (EGAP015) y Épicas e historias de usuario (FGAP040) | `semana-04/`: formato de Justificación y Épicas de ejemplo |
| **5** | **12–18/10 (actual)** | **Responsabilidad Social Universitaria (RSU):** Reglamento UNS (Res. 448-2023-CU-R-UNS) y dos proyectos RSU de ejemplo (instrucción **por confirmar**). **Secuencia de avances:** hoja de ruta de formatos FGAP010 → FGAP090 | `semana-05/`: reglamento, ejemplos RSU, secuencia, FGAP070, **libro base (Guía del SBOK)** |

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
El avance de cada entregable **para NewBit** se sigue en [`proyecto/README.md`](../proyecto/README.md). Aquí queda qué pide el curso y si hay algo hecho.

| Entregable | Semana | Estado |
|---|---|---|
| 1 · Acta de Constitución (FGAP/EGAP010) | 2 | Hecha para VIGIA (proyecto anterior); **rehacer para NewBit** |
| Cuadro comparativo de principios de Scrum | 2 | Sin evidencia |
| 2 · Registro de Stakeholders (FGAP020) | 5 (en la secuencia) | **Nuevo; sin formato ni ejemplo en el repo** |
| 3 · Roles y Prototipos (FGAP/EGAP030) | 3 | Hecho para VIGIA; **rehacer para NewBit** |
| Infografía de 12 pasos del proyecto | 3 | Hecha en HTML para VIGIA; rehacer o adaptar |
| Justificación del proyecto (EGAP015) | 4 | **Pendiente** |
| 4 · Épicas e historias de usuario (FGAP040) | 4 | **Pendiente** |
| Proyecto de RSU (Anexo 1 del reglamento) | 5 | **Por confirmar** si se pide y cuándo |
| 5 · Backlog priorizado (FGAP060) | 5 (en la secuencia) | Pendiente; sin formato aún |
| 5 · Criterios de Terminado (FGAP070) | 5 | Pendiente; **ejemplo recibido** (`semana-05/FGAP070_…/`) |
| 6 · Sprints (planificación, revisión, retrospectiva) | – | Pendiente |
| 7 · Cierre del Proyecto (FGAP090) | – | Al final |

## Dudas para el docente
1. Cómo se evalúa un equipo de **3 personas** (PO + SM/Developer + Developer) si el ejemplo asume 1 PO + 1 SM + 3 developers.
2. Si cambia el proyecto, qué entregables ya hechos (Acta, Roles) hay que rehacer.
3. `NightWatch_Protocol_Propuesta.pdf` (en `semana-04/Formato_Justificacion_…/`) es en realidad el formato de Justificación: duplicado del `.docx`; renombrar o descartar.
4. **RSU (semana 5):** ¿hay que redactar un proyecto de RSU propio (Anexo 1)? ¿solo el diseño o también ejecutarlo e informar (Anexo 2)? ¿debe relacionarse con el proyecto del curso? ¿fecha de entrega?
5. **Secuencia (semana 5):** pedir el formato **FGAP020 (Registro de Stakeholders)**, FGAP060 y FGAP070. ¿Hay diferencia entre EGAP y FGAP? ¿Existen FGAP050 y FGAP080?
