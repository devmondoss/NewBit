# Proyecto: Unsafe-Net (en definición)

Proyecto vigente del equipo para el curso, elegido el **05/10/2026**: detección de **conductas inseguras** en video industrial con **YOLO + ConvLSTM**, a partir del artículo *Unsafe-Net* (Önal y Dandıl, 2024).

- **Equipo (2):** Anthony Lopez Yrribarren · Luis Fernando Elias Salazar Diaz.
- **Ficha y análisis del artículo:** [semana-04/NewBit_Top3_ComputerVision_SeguridadIndustrial/NewBit_Top3_ComputerVision_SeguridadIndustrial.md](semana-04/NewBit_Top3_ComputerVision_SeguridadIndustrial/NewBit_Top3_ComputerVision_SeguridadIndustrial.md).
- **Material del curso** (plantillas y ejemplos del docente): [`../docs/`](../docs/README.md). **Proyecto anterior** (VIGIA Industrial): [`../archivo/vigia-industrial/`](../archivo/vigia-industrial/README.md).

## Cómo se ordena esta carpeta
- `semana-XX/`: lo que el equipo produce cada semana del curso (**una carpeta por archivo**, con el original y su `.md` del mismo nombre; los documentos escritos por el equipo van como `.md` sueltos). Misma numeración de semanas que `docs/`.
- Cuando empiece el código, va **dentro de esta carpeta** (por ejemplo `ml/` para el modelo y `app/` para la web/API); así el repo funciona como monorepo: curso en `docs/`, proyecto (docs + código) en `proyecto/`.
- Todo lo que sea diseño propio se marca como **propuesta**. Las cifras del artículo (95.81 %, 0.14 s, 518 → 134) no son resultados nuestros.

## Hoja de ruta: entregables aplicados a Unsafe-Net
Sigue la **Secuencia de avances** del docente ([`docs/semana-05/SECUENCIA DE AVANCES/SECUENCIA DE AVANCES.md`](../docs/semana-05/SECUENCIA DE AVANCES/SECUENCIA DE AVANCES.md)). Plantilla o ejemplo de cada paso en `docs/semana-XX/`.

| Paso | Formato | Plantilla / ejemplo | Estado para Unsafe-Net |
|---|---|---|---|
| 1 | FGAP010 Acta de Constitución | `docs/semana-02/` | Pendiente (la de VIGIA sirve de base) — **es la base de todo lo demás** |
| 2 | FGAP020 Registro de Stakeholders | — (no recibido) | Pendiente; pedir formato al docente |
| 3 | FGAP030 Roles y Prototipos | `docs/semana-03/` | Pendiente (la de VIGIA sirve de base) |
| 4 | FGAP040 Épicas | `docs/semana-04/FGAP040_…/` | Pendiente; depende del Acta |
| 5 | FGAP060 Backlog priorizado · FGAP070 Criterios de Terminado | FGAP060: no recibido · FGAP070: `docs/semana-05/FGAP070_…/` | Pendiente; el FGAP070 ya tiene ejemplo y su análisis dice cómo adaptarlo |
| 6 | Sprints: planificación → implementación → revisión → retrospectiva | — | Aún no empieza |
| 7 | FGAP090 Cierre del Proyecto | — | Al final |

**Fuera de la secuencia, también pedidos:**
| Documento | Plantilla / ejemplo | Estado |
|---|---|---|
| EGAP015 Justificación (semana 4) | `docs/semana-04/Formato_Justificacion_…/` | Pendiente; depende del Acta |
| Infografía de 12 pasos (semana 3) | — | Pendiente (las de VIGIA están en `archivo/`) |
| Proyecto de RSU, Anexo 1 (semana 5) | `docs/semana-05/README.md` (reglamento + ejemplos) | **Por confirmar** con el docente; idea de tema en `docs/semana-05/README.md` |

## Decisiones
Base: [UnsafeNet Research Pack](semana-05/UnsafeNet_Research_Pack/UnsafeNet_Research_Pack.md) (12/10). Las marcadas *propuesta* faltan confirmarlas entre el equipo.

| # | Decisión | Estado |
|---|---|---|
| 1 | Conductas | *Propuesta:* **Safe Walkway Violation + Opened Panel Cover**, ampliable a las 4 inseguras |
| 2 | Fuente del video | **Resuelto:** dataset público de Mendeley (CC BY 4.0, 691 clips, split oficial). Confirmar tamaño y licencia en el enlace |
| 3 | Réplica fiel o propia | *Propuesta:* **réplica pequeña fiel (nivel B)**: YOLOv4 filtra frames → ConvLSTM; comparar con el baseline; GUI simple y alerta simulada |
| 4 | Dónde entrenar | *Propuesta:* Colab o GPU NVIDIA local; 30–50 GB libres en disco |
| 5 | Nombre del proyecto y del Scrum Team | **Abierta** (el curso asume 1 PO + 1 SM + 3 Developers) |
| 6 | Organización del caso, interesados, contexto peruano y costos | **Abierta:** falta investigar (puntos E–G de la guía) |

## Por semana
| Semana | Fechas | Qué hizo el equipo |
|---|---|---|
| 4 | 05–11/10 | Elección de Unsafe-Net: [Ficha y análisis](semana-04/NewBit_Top3_ComputerVision_SeguridadIndustrial/NewBit_Top3_ComputerVision_SeguridadIndustrial.md) (el PDF original está en la misma carpeta) |
| 5 | 12–18/10 | [Guía de investigación](semana-05/guia-investigacion-unsafe-net.md) (qué investigar para cerrar las decisiones y redactar los formatos) · [UnsafeNet Research Pack](semana-05/UnsafeNet_Research_Pack/UnsafeNet_Research_Pack.md) (investigación del equipo: dataset, arquitectura, plan de réplica) |
