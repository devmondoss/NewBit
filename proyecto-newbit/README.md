# Proyecto: NewBit

**NewBit** — Plataforma de Computer Vision que convierte cámaras existentes en sensores inteligentes configurables para operaciones industriales. Código: **PY-NB-001**.

**Investigación base** (elegida el **05/10/2026**), cuya réplica es la primera capacidad de NewBit: detección de **conductas inseguras** en video industrial con **YOLO + ConvLSTM**, a partir del artículo *Unsafe-Net* (Önal y Dandıl, 2024).

- **Grupo D3** (laboratorio D, equipo 3). **Equipo Scrum (3):** Albert Sebastian Chumacero Chávarry — **Product Owner** · Anthony Gabriel Lopez Yrribarren — **Scrum Master y Developer** · Luis Fernando Salazar Diaz — **Developer**.
- **Duración:** **4 sprints** de dos semanas (19/10–11/12/2026), más el inicio (05–16/10) y el cierre (14–18/12).
- **Ficha y análisis del artículo:** [investigacion/NewBit_Top3_ComputerVision_SeguridadIndustrial/NewBit_Top3_ComputerVision_SeguridadIndustrial.md](investigacion/NewBit_Top3_ComputerVision_SeguridadIndustrial/NewBit_Top3_ComputerVision_SeguridadIndustrial.md).
- **Lo de clase** (material del profe y nuestras entregas, por semana): [`../curso/`](../curso/README.md). **Proyecto anterior** (VIGIA Industrial): [`../descartado/vigia-industrial/`](../descartado/vigia-industrial/README.md).

## Cómo se ordena esta carpeta
- `investigacion/`: **contexto del proyecto** que no pertenece a ninguna semana: ficha del Top 3, guía de investigación y UnsafeNet Research Pack (una carpeta por archivo, con su `.md`).
- Las **tareas del curso** hechas para NewBit (Acta, Roles, Épicas…) **no están aquí**: van en `../curso/semana-XX-<tema>/nuestras-entregas/`, junto al material del profe de esa semana. La tabla de abajo enlaza cada una.
- Cuando empiece el código, va **dentro de esta carpeta** (por ejemplo `ml/` para el modelo y `app/` para la web/API); así el repo funciona como monorepo: curso en `curso/`, proyecto (docs + código) en `proyecto-newbit/`.
- Todo lo que sea diseño propio se marca como **propuesta**. Las cifras del artículo (95.81 %, 0.14 s, 518 → 134) no son resultados nuestros.

## Hoja de ruta: entregables de NewBit
Sigue la **Secuencia de avances** del docente ([`curso/semana-05-rsu-y-backlog/material-del-profe/secuencia-de-avances/secuencia-de-avances.md`](../curso/semana-05-rsu-y-backlog/material-del-profe/secuencia-de-avances/secuencia-de-avances.md)). Plantilla o ejemplo de cada paso en `../curso/semana-XX-<tema>/material-del-profe/`.

| Paso | Formato | Plantilla / ejemplo | Estado para NewBit |
|---|---|---|---|
| 1 | FGAP010 Acta de Constitución | `curso/semana-02-scrum-y-acta/material-del-profe/` | **Versión 2.0 completa** (17/10): [`../curso/semana-02-scrum-y-acta/nuestras-entregas/FGAP010_Acta_Constitucion_NewBit/`](../curso/semana-02-scrum-y-acta/nuestras-entregas/FGAP010_Acta_Constitucion_NewBit/FGAP010_Acta_Constitucion_NewBit.md) (taller metalmecánico, YOLOv8, S/ 20,768) |
| 2 | FGAP020 Registro de Stakeholders | — (no recibido) | Pendiente de plantilla docente; roles e interesados clave detallados en FGAP010 y FGAP030 |
| 3 | FGAP030 Roles y Prototipos | `curso/semana-03-roles-y-prototipos/material-del-profe/` | **Versión 2.0 completa** (17/10): [`../curso/semana-03-roles-y-prototipos/nuestras-entregas/FGAP030_Roles_y_Prototipos_NewBit/`](../curso/semana-03-roles-y-prototipos/nuestras-entregas/FGAP030_Roles_y_Prototipos_NewBit/FGAP030_Roles_y_Prototipos_NewBit.md) — 5 perfiles de planta aprobados |
| 4 | FGAP040 Épicas | `curso/semana-04-justificacion-y-epicas/material-del-profe/epicas-ejemplo-retinopatia/` | **Versión 2.0 canónica del equipo** (17/10): [`../curso/semana-04-justificacion-y-epicas/nuestras-entregas/FGAP040_Epicas_NewBit/`](../curso/semana-04-justificacion-y-epicas/nuestras-entregas/FGAP040_Epicas_NewBit/FGAP040_Epicas_NewBit.md): 6 épicas, 12 HU con roles de planta reales (versión preliminar de 26 HU archivada en `descartado/epicas-26-hu-obsoletas/`) |
| 5 | FGAP060 Backlog priorizado · FGAP070 Criterios de Terminado | FGAP060: no recibido · FGAP070: `curso/semana-05-rsu-y-backlog/material-del-profe/criterios-de-terminado-ejemplo-retinopatia/` | **Versión 2.0 completa** (17/10): Tablero Kanban, criterios DoD y priorización MoSCoW sincronizados en [`../curso/semana-05-rsu-y-backlog/nuestras-entregas/Tablero_Kanban_NewBit/`](../curso/semana-05-rsu-y-backlog/nuestras-entregas/Tablero_Kanban_NewBit/Tablero_Kanban_NewBit.md) |
| 6 | Sprints: planificación → implementación → revisión → retrospectiva | — | En desarrollo activo del incremento MVP (Sprints 1 y 2, 15 puntos de historia) |
| 7 | FGAP090 Cierre del Proyecto | — | Al final del semestre |

**Fuera de la secuencia, también pedidos:**
| Documento | Plantilla / ejemplo | Estado |
|---|---|---|
| Cuadro comparativo de los principios de Scrum (semana 2) | `curso/semana-02-scrum-y-acta/material-del-profe/principios-de-scrum/` | **Versión 2.0** (17/10): [`../curso/semana-02-scrum-y-acta/nuestras-entregas/Cuadro_Principios_Scrum_NewBit/`](../curso/semana-02-scrum-y-acta/nuestras-entregas/Cuadro_Principios_Scrum_NewBit/Cuadro_Principios_Scrum_NewBit.md): 6 principios con ejemplos de NewBit y HU11 en Sprint 2 |
| EGAP015 Justificación (semana 4) | `curso/semana-04-justificacion-y-epicas/material-del-profe/justificacion-formato-y-ejemplo/` | **Versión 2.0** (17/10): [`../curso/semana-04-justificacion-y-epicas/nuestras-entregas/EGAP015_Justificacion_NewBit/`](../curso/semana-04-justificacion-y-epicas/nuestras-entregas/EGAP015_Justificacion_NewBit/EGAP015_Justificacion_NewBit.md): presupuesto S/ 20,768, viabilidad técnica, citas Önal & Dandıl 2024 |
| Diagrama de arquitectura / cómo funciona (semana 3) | — | **Versión 1.0 en HTML** (12/10): [`../curso/semana-03-roles-y-prototipos/nuestras-entregas/Diagrama_Arquitectura_NewBit/`](../curso/semana-03-roles-y-prototipos/nuestras-entregas/Diagrama_Arquitectura_NewBit/Diagrama_Arquitectura_NewBit.md) |
| PPT de presentación del proyecto (semana 3) | — | **Versión 1.0** (12/10): [`../curso/semana-03-roles-y-prototipos/nuestras-entregas/PPT_Presentacion_NewBit/`](../curso/semana-03-roles-y-prototipos/nuestras-entregas/PPT_Presentacion_NewBit/PPT_Presentacion_NewBit.md): 12 diapositivas con notas del orador |
| Infografía de 12 pasos + metodología (semana 3) | ejemplos del docente | **Versión 1.0 en HTML** (12/10): [`../curso/semana-03-roles-y-prototipos/nuestras-entregas/Infografias_NewBit/`](../curso/semana-03-roles-y-prototipos/nuestras-entregas/Infografias_NewBit/Infografias_NewBit.md), con fotos reales de Wikimedia |
| Proyecto de RSU, Anexo 1 (semana 5) | `curso/semana-05-rsu-y-backlog/README.md` (reglamento + ejemplos) | **Por confirmar** con el docente |
| Presentación de una técnica de estimación: **Puño de cinco** (semana 5) | Guía del SBOK, pág. 193–195 | **Versión 2.0** (17/10): [`../curso/semana-05-rsu-y-backlog/nuestras-entregas/Presentacion_Fist_of_Five/`](../curso/semana-05-rsu-y-backlog/nuestras-entregas/Presentacion_Fist_of_Five/Presentacion_Fist_of_Five.md): HTML + PPTX + PDF, **8 diapositivas** con notas sincronizadas con el Backlog canónico |
| Tablero Kanban con criterios de aceptación, prioridad y estimación (semana 5) | Guía del SBOK 8.5, 9.1–9.3 (sin formato del docente) | **Versión 2.0** (17/10): [`../curso/semana-05-rsu-y-backlog/nuestras-entregas/Tablero_Kanban_NewBit/`](../curso/semana-05-rsu-y-backlog/nuestras-entregas/Tablero_Kanban_NewBit/Tablero_Kanban_NewBit.md): HTML + PPTX + PDF, 6 diapositivas; 12 HU canónicas, 31 puntos en 4 sprints |
| Priorización con **MoSCoW y 100 puntos** (semana 5, actividad de clase) | Guía del SBOK 4.5.2 y 8.5.2.1, pp. 76–78 y 169 | **Versión 2.0** (17/10): [`../curso/semana-05-rsu-y-backlog/nuestras-entregas/Priorizacion_MoSCoW_100_Puntos_NewBit/`](../curso/semana-05-rsu-y-backlog/nuestras-entregas/Priorizacion_MoSCoW_100_Puntos_NewBit/Priorizacion_MoSCoW_100_Puntos_NewBit.md): PDF + PPTX + HTML, 6 páginas |

## Decisiones
Base: [UnsafeNet Research Pack](investigacion/UnsafeNet_Research_Pack/UnsafeNet_Research_Pack.md) y [`ROADMAP_REESTRUCTURACION_NEWBIT.md`](../../ROADMAP_REESTRUCTURACION_NEWBIT.md).

| # | Decisión | Estado |
|---|---|---|
| 1 | Conductas | *Propuesta:* **Safe Walkway Violation + Opened Panel Cover**, ampliable a las 4 inseguras del dataset |
| 2 | Fuente del video | **Resuelto:** dataset público de Mendeley (CC BY 4.0, 691 clips, split oficial de Kafaoğlu Metal Plastik) |
| 3 | Réplica fiel o propia | **Resuelto (D-03):** Stack unificado 100% Python con **FastAPI** + Jinja2/Tailwind + OpenCV. Detector espacial modernizado a **YOLOv8n** (`ultralytics`), ingesta de clips .mp4 en lote y arquitectura en monorepo (`app/` y `ml/`). Alcance MVP: Sprints 1 y 2 (15 puntos). |
| 4 | Dónde entrenar | *Propuesta:* Inferencia local en CPU/GPU; entrenamiento en Google Colab o GPU NVIDIA local |
| 5 | Scrum Team y sprints | **Resuelto (12/10):** PO Albert Chumacero · SM + Dev Anthony Lopez · Dev Luis Salazar; 4 sprints de 2 semanas. **Nombre: NewBit** (PY-NB-001) |
| 6 | Organización del caso, interesados, contexto peruano y costos | **Resuelto (D-01/D-02):** Caso de estudio: taller de manufactura metalmecánica / mecanizado industrial. 5 perfiles de planta aprobados en FGAP030. Presupuesto formal consolidado: **S/ 20,768** (FGAP010 y EGAP015). |

## Historial
| Semana | Fechas | Qué hizo el equipo |
|---|---|---|
| 4 | 05–11/10 | Elección de Unsafe-Net: [Ficha y análisis](investigacion/NewBit_Top3_ComputerVision_SeguridadIndustrial/NewBit_Top3_ComputerVision_SeguridadIndustrial.md) (el PDF original está en la misma carpeta) |
| 5 | 12–18/10 | [Guía de investigación](investigacion/guia-investigacion-unsafe-net.md) (qué investigar para cerrar las decisiones y redactar los formatos) · [UnsafeNet Research Pack](investigacion/UnsafeNet_Research_Pack/UnsafeNet_Research_Pack.md) (investigación del equipo: dataset, arquitectura, plan de réplica) |
