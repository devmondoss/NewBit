# Proyecto: NewBit

**NewBit** — Plataforma de Computer Vision que convierte cámaras existentes en sensores inteligentes configurables para operaciones industriales. Código: **PY-NB-001**.

**Investigación base** (elegida el **05/10/2026**), cuya réplica es la primera capacidad de NewBit: detección de **conductas inseguras** en video industrial con **YOLO + ConvLSTM**, a partir del artículo *Unsafe-Net* (Önal y Dandıl, 2024).

- **Equipo Scrum (3):** Albert Sebastian Chumacero Chávarry — **Product Owner** · Anthony Gabriel Lopez Yrribarren — **Scrum Master y Developer** · Luis Fernando Salazar Diaz — **Developer**.
- **Duración:** **4 sprints** de dos semanas (19/10–11/12/2026), más el inicio (05–16/10) y el cierre (14–18/12).
- **Ficha y análisis del artículo:** [investigacion/NewBit_Top3_ComputerVision_SeguridadIndustrial/NewBit_Top3_ComputerVision_SeguridadIndustrial.md](investigacion/NewBit_Top3_ComputerVision_SeguridadIndustrial/NewBit_Top3_ComputerVision_SeguridadIndustrial.md).
- **Material del curso** (plantillas y ejemplos del docente): [`../docs/`](../docs/README.md). **Proyecto anterior** (VIGIA Industrial): [`../archivo/vigia-industrial/`](../archivo/vigia-industrial/README.md).

## Cómo se ordena esta carpeta
- `investigacion/`: **contexto del proyecto** que no pertenece a ninguna semana: ficha del Top 3, guía de investigación y UnsafeNet Research Pack (una carpeta por archivo, con su `.md`).
- `entregables/semana-XX/`: las **tareas del curso** hechas para NewBit, **ordenadas por la semana en que se pidieron** (una carpeta por entregable, con su `.md`).
- Cuando empiece el código, va **dentro de esta carpeta** (por ejemplo `ml/` para el modelo y `app/` para la web/API); así el repo funciona como monorepo: curso en `docs/`, proyecto (docs + código) en `proyecto/`.
- Todo lo que sea diseño propio se marca como **propuesta**. Las cifras del artículo (95.81 %, 0.14 s, 518 → 134) no son resultados nuestros.

## Hoja de ruta: entregables de NewBit
Sigue la **Secuencia de avances** del docente ([`docs/semana-05/SECUENCIA DE AVANCES/SECUENCIA DE AVANCES.md`](../docs/semana-05/SECUENCIA DE AVANCES/SECUENCIA DE AVANCES.md)). Plantilla o ejemplo de cada paso en `docs/semana-XX/`.

| Paso | Formato | Plantilla / ejemplo | Estado para NewBit |
|---|---|---|---|
| 1 | FGAP010 Acta de Constitución | `docs/semana-02/` | **Versión 1.0 completa** (12/10, sin pendientes): [`entregables/semana-02/FGAP010_Acta_Constitucion_NewBit/`](entregables/semana-02/FGAP010_Acta_Constitucion_NewBit/FGAP010_Acta_Constitucion_NewBit.md) |
| 2 | FGAP020 Registro de Stakeholders | — (no recibido) | Pendiente; pedir formato al docente |
| 3 | FGAP030 Roles y Prototipos | `docs/semana-03/` | **Versión 1.0 completa** (12/10): [`entregables/semana-03/FGAP030_Roles_y_Prototipos_NewBit/`](entregables/semana-03/FGAP030_Roles_y_Prototipos_NewBit/FGAP030_Roles_y_Prototipos_NewBit.md) — 5 roles con persona y foto |
| 4 | FGAP040 Épicas | `docs/semana-04/FGAP040_…/` | **Versión 1.0** (12/10): [`entregables/semana-04/FGAP040_Epicas_NewBit/`](entregables/semana-04/FGAP040_Epicas_NewBit/FGAP040_Epicas_NewBit.md): 6 épicas, 26 HU; falta la carátula (ciclo, aula, turno) |
| 5 | FGAP060 Backlog priorizado · FGAP070 Criterios de Terminado | FGAP060: no recibido · FGAP070: `docs/semana-05/FGAP070_…/` | Pendiente; el FGAP070 ya tiene ejemplo y su análisis dice cómo adaptarlo |
| 6 | Sprints: planificación → implementación → revisión → retrospectiva | — | Aún no empieza |
| 7 | FGAP090 Cierre del Proyecto | — | Al final |

**Fuera de la secuencia, también pedidos:**
| Documento | Plantilla / ejemplo | Estado |
|---|---|---|
| EGAP015 Justificación (semana 4) | `docs/semana-04/Formato_Justificacion_…/` | **Versión 1.0** (12/10): [`entregables/semana-04/EGAP015_Justificacion_NewBit/`](entregables/semana-04/EGAP015_Justificacion_NewBit/EGAP015_Justificacion_NewBit.md) |
| Diagrama de arquitectura / cómo funciona (semana 3) | — | **Versión 1.0 en HTML** (12/10): [`entregables/semana-03/Diagrama_Arquitectura_NewBit/`](entregables/semana-03/Diagrama_Arquitectura_NewBit/Diagrama_Arquitectura_NewBit.md) |
| PPT de presentación del proyecto (semana 3) | — | **Versión 1.0** (12/10): [`entregables/semana-03/PPT_Presentacion_NewBit/`](entregables/semana-03/PPT_Presentacion_NewBit/PPT_Presentacion_NewBit.md): 10 diapositivas con notas del orador |
| Infografía de 12 pasos + metodología (semana 3) | ejemplos del docente | **Versión 1.0 en HTML** (12/10): [`entregables/semana-03/Infografias_NewBit/`](entregables/semana-03/Infografias_NewBit/Infografias_NewBit.md), con fotos reales de Wikimedia |
| Proyecto de RSU, Anexo 1 (semana 5) | `docs/semana-05/README.md` (reglamento + ejemplos) | **Por confirmar** con el docente; idea de tema en `docs/semana-05/README.md` |
| Presentación de una técnica de estimación: **Puño de cinco** (semana 5) | Guía del SBOK, pág. 193–195 | **Versión 1.2** (12/10): [`entregables/semana-05/Presentacion_Fist_of_Five/`](entregables/semana-05/Presentacion_Fist_of_Five/Presentacion_Fist_of_Five.md): HTML + PPTX + PDF, 6 diapositivas con notas; confirmar formato con el docente |

## Decisiones
Base: [UnsafeNet Research Pack](investigacion/UnsafeNet_Research_Pack/UnsafeNet_Research_Pack.md) (12/10). Las marcadas *propuesta* faltan confirmarlas entre el equipo.

| # | Decisión | Estado |
|---|---|---|
| 1 | Conductas | *Propuesta:* **Safe Walkway Violation + Opened Panel Cover**, ampliable a las 4 inseguras |
| 2 | Fuente del video | **Resuelto:** dataset público de Mendeley (CC BY 4.0, 691 clips, split oficial). Confirmar tamaño y licencia en el enlace |
| 3 | Réplica fiel o propia | *Propuesta:* **réplica pequeña fiel (nivel B)**: YOLOv4 filtra frames → ConvLSTM; comparar con el baseline; GUI simple y alerta simulada |
| 4 | Dónde entrenar | *Propuesta:* Colab o GPU NVIDIA local; 30–50 GB libres en disco |
| 5 | Scrum Team y sprints | **Resuelto (12/10):** PO Albert Chumacero · SM + Dev Anthony Lopez · Dev Luis Salazar; 4 sprints. **Nombre: NewBit** (PY-NB-001) |
| 6 | Organización del caso, interesados, contexto peruano y costos | **Abierta:** falta investigar (puntos E–G de la guía) |

## Historial
| Semana | Fechas | Qué hizo el equipo |
|---|---|---|
| 4 | 05–11/10 | Elección de Unsafe-Net: [Ficha y análisis](investigacion/NewBit_Top3_ComputerVision_SeguridadIndustrial/NewBit_Top3_ComputerVision_SeguridadIndustrial.md) (el PDF original está en la misma carpeta) |
| 5 | 12–18/10 | [Guía de investigación](investigacion/guia-investigacion-unsafe-net.md) (qué investigar para cerrar las decisiones y redactar los formatos) · [UnsafeNet Research Pack](investigacion/UnsafeNet_Research_Pack/UnsafeNet_Research_Pack.md) (investigación del equipo: dataset, arquitectura, plan de réplica) |
