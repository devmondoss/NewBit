# -*- coding: utf-8 -*-
"""Genera FGAP050_Riesgo_del_Proyecto_NewBit.docx (una ficha por riesgo + priorización) y su .md.
Uso: python3 generar_fgap050.py <carpeta_salida>
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
# docx_nb.py y plan_sprint02.py viven en la carpeta del FGAP110 (fuente única)
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "FGAP110_EDT_Sprint_02_NewBit")))
sys.path.insert(0, HERE)
from docx_nb import Doc, md_from_markup  # noqa: E402

BASE = "FGAP050_Riesgo_del_Proyecto_NewBit"
ROJO = "8B1E2D"
GRIS = "E1E4E8"
GRIS2 = "F3F4F6"
ROSA = "F9E1E3"

PROYECTO = ("PY-NB-001 – Sistema web con Visión Artificial para la detección de actos inseguros en áreas operativas "
            "de manufactura metalmecánica (NewBit)")
VERSION = ["1.0", "Developers (Anthony Lopez y Luis Salazar)", "Anthony Lopez (Scrum Master)",
           "Albert Chumacero (Product Owner) · {PC}", "02/11/2026", "Registro de los riesgos prioritarios al inicio del Sprint 2"]

PROB = [("Muy improbable", 0.1), ("Relativamente probable", 0.3), ("Probable", 0.5), ("Muy probable", 0.7), ("Casi certeza", 0.9)]
IMP = [("Muy bajo", 0.05), ("Bajo", 0.10), ("Moderado", 0.20), ("Alto", 0.40), ("Muy alto", 0.80)]
TIPO = [("Muy alto", "Mayor a 0,50"), ("Alto", "Menor a 0,50"), ("Moderado", "Menor a 0,30"), ("Bajo", "Menor a 0,10"), ("Muy bajo", "Menor a 0,05")]


def tipo_de(pi):
    if pi > 0.50:
        return "Muy alto"
    if pi >= 0.30:
        return "Alto"
    if pi >= 0.10:
        return "Moderado"
    if pi >= 0.05:
        return "Bajo"
    return "Muy bajo"


def num(v):
    return ("%.2f" % v).replace(".", ",")


RIESGOS = [
    {
        "cod": "R-01", "nombre": "Ajuste del modelo temporal (ConvLSTM)", "p": 0.5, "i": 0.8,
        "desc": "El modelo ConvLSTM de NewBit podría no aprender a distinguir las conductas de la primera versión (tránsito fuera de la vía peatonal y panel "
                "eléctrico abierto, con sus casos seguros) con la longitud de secuencia, las capas y los hiperparámetros iniciales, o su ajuste podría necesitar "
                "más ciclos de entrenamiento de los que caben en los Sprints 2 y 3. Retrasaría HU07 y HU08 y comprometería el pipeline completo que exige el Acta.",
        "causa": "El equipo no ha entrenado antes un ConvLSTM y no tiene una línea base propia. La longitud de secuencia N depende de la ventana fija de HU05, que "
                 "todavía no existe, y del submuestreo a 5 fps. Los datos vienen de una sola planta con dos cámaras y hay pocos ejemplos por clase (en el conjunto "
                 "de prueba del artículo, 13 videos de panel abierto; Research Pack de Unsafe-Net).",
        "trigger": "Al cerrar el //spike// de longitud de secuencia (T10, 10/11/2026), ninguna de las dos configuraciones de N supera en exactitud de validación "
                   "al clasificador de la clase mayoritaria (línea base trivial), o la pérdida de validación no baja durante 5 épocas seguidas.",
        "entregables": "HU07 (Sprint 2 si se aprueba la SC-001; si no, Sprint 3) y HU08 (Sprint 3); modelo ConvLSTM entrenado y evaluado con métricas por clase "
                       "(entregable clave del Acta); evaluación comparativa; HU09 y HU10, que dependen de HU08; demostración del incremento.",
        "sustento": "**P = 0,50 (probable):** primer ConvLSTM del equipo y sin línea base; el dataset es público y el artículo muestra que la tarea es abordable. "
                    "**I = 0,80 (muy alto):** sin modelo temporal no hay pipeline completo ni métricas, que son criterios de aprobación del Acta.",
        "respuesta": "**Mitigar.** Registro versionado de cada configuración y //spike// de dos valores de N (T10, 3 h, EDT FGAP110). Adelantar HU07 al Sprint 2 "
                     "(SC-001, FGAP090) para que el Sprint 3 tenga holgura para un segundo ciclo de ajuste. **Plan B del Acta:** cierre con alcance reducido a una "
                     "conducta, con su evaluación documentada. Dueño del riesgo: Product Owner; ejecutan: Developers; vigila: Scrum Master (Daily y retrospectiva).",
    },
    {
        "cod": "R-02", "nombre": "Implementación propia del pipeline completo", "p": 0.5, "i": 0.4,
        "desc": "El pipeline propio de NewBit (carga, extracción de frames, detección, descarte de frames vacíos, agrupamiento y tensor) podría tener defectos no "
                "detectados, porque la prueba integrada solo se hizo con un clip sintético y no hay revisión de pares registrada. Al probarlo con videos reales del "
                "dataset, las historias construidas podrían no cumplir sus criterios o la Definición de Terminado, y HU07 recibiría secuencias mal formadas.",
        "causa": "El código de las 7 HU de los Sprints 1 y 2 se escribió en un día (17/10/2026). El clip de prueba (`tests/fixtures`) usa la foto de muestra `zidane.jpg` "
                 "de Ultralytics: muestra personas, no operarios, y no sirve como evidencia visual. No hay registro de la revisión de pares que exige el FGAP070. "
                 "En macOS, un paquete `tests` de terceros tapa `proyecto-newbit/tests` y la prueba E2E no corre con el comando del README.",
        "trigger": "La prueba integrada con un video real del dataset (T13, 12/11/2026) falla en algún paso; o, en la revisión manual de T11 (03/11; 20 frames con "
                   "operario visible por video), más del 10 % queda sin caja «persona» (umbral propuesto); o al 11/11 la revisión de pares (T12) deja al menos "
                   "una observación crítica sin resolver.",
        "entregables": "Incremento de los Sprints 1 y 2 (HU01–HU06 y HU11, 15 pts) y su aceptación por el PO; tensor de entrada de HU07; demostración en la "
                       "revisión del Sprint 2; criterio de aprobación del Acta «reproducibilidad técnica».",
        "sustento": "**P = 0,50 (probable):** nunca se probó con videos reales ni se revisó entre pares, aunque las 43 pruebas automatizadas pasan (20/10). "
                    "**I = 0,40 (alto):** obliga a retrabajo dentro del sprint y retrasa la aceptación de 15 pts, pero no cambia el alcance.",
        "respuesta": "**Mitigar (Acta: bibliotecas abiertas y revisión por pares).** T11: pipeline espacial con 5 videos del dataset (3 h). T12: revisión de pares "
                     "registrada con la lista del FGAP070 (4 h). T13: prueba E2E con video real y corrección del import en macOS (3 h). Dueño: Product Owner; "
                     "ejecutan: Developers; el Scrum Master registra el resultado de la revisión de pares.",
    },
    {
        "cod": "R-03", "nombre": "GPU y tiempo de entrenamiento limitados", "p": 0.5, "i": 0.4,
        "desc": "El entrenamiento de ConvLSTM podría no caber en el tiempo del sprint por falta de GPU propia o por las cuotas y desconexiones de Google Colab. "
                "Retrasaría HU07 y HU08 y reduciría el número de configuraciones que se pueden probar, lo que agrava R-01.",
        "causa": "La aplicación corre en CPU y no está documentado si los equipos del grupo tienen GPU NVIDIA ({PC}). El presupuesto de nube del Acta es acotado "
                 "(S/ 80: 2 meses × S/ 40). Los videos y los tensores tienen que subirse a la nube antes de entrenar.",
        "trigger": "En el //spike// T10 (10/11/2026), una época con el subconjunto de las dos conductas tarda más de 20 min (umbral propuesto: permite unas 20 épocas "
                   "en una sesión), o se pierden 2 o más sesiones de Colab por cuota o desconexión en la misma semana.",
        "entregables": "HU07 y HU08; modelo ConvLSTM entrenado; comparación de tiempos de procesamiento del Acta; cronograma de los Sprints 2 y 3.",
        "sustento": "**P = 0,50 (probable):** depende de un servicio externo con cuotas y de hardware no confirmado. **I = 0,40 (alto):** retrasa el modelo "
                    "temporal, pero hay alternativas (bajar resolución o N, menos épocas).",
        "respuesta": "**Mitigar.** T14: entorno de entrenamiento en Colab con dependencias fijadas y checkpoint por época, para reanudar tras una desconexión "
                     "(2 h). Medición del tiempo por época en T10. **Plan B:** reducir la resolución de entrada o N y entrenar solo con las dos conductas de la "
                     "primera versión (Acta). Dueño: Product Owner; ejecuta: Luis Salazar.",
    },
]

RESUMEN = [
    # cod, riesgo del Acta, P, I, situación al 02/11, tratamiento
    ("R-01", "Ajuste del modelo temporal (longitud de secuencia, capas, hiperparámetros)", 0.5, 0.8,
     "HU07 entra al Sprint 2 si se aprueba la SC-001; no hay línea base propia", "Ficha y tarea T10"),
    ("R-02", "Implementación propia del pipeline completo", 0.5, 0.4,
     "Prueba integrada solo con clip sintético; sin revisión de pares registrada", "Ficha y tareas T11–T13"),
    ("R-03", "GPU y tiempo de entrenamiento limitados", 0.5, 0.4,
     "El entrenamiento de ConvLSTM empieza en el Sprint 2; GPU local sin confirmar", "Ficha y tarea T14 (medición en T10)"),
    ("R-04", "Etiquetado de frames más lento de lo previsto", 0.3, 0.2,
     "En el Sprint 2 no se anotan frames a mano: se usa YOLOv8n preentrenado (clase «persona»)", "Se vigila; sin tareas"),
    ("R-05", "Espacio en disco (30–50 GB entre videos, frames y checkpoints)", 0.3, 0.2,
     "Los tensores del split y los checkpoints empiezan a generarse en el Sprint 2", "Se vigila; checkpoints fuera de git"),
    ("R-06", "Cambio de entorno: una planta y dos cámaras", 0.3, 0.1,
     "La adaptación a otras plantas está fuera del alcance de esta versión", "Se acepta"),
    ("R-07", "Equipo de tres; el Scrum Master también es Developer", 0.5, 0.2,
     "Anthony tiene 17 h de tareas en el Sprint 2 además de su rol de Scrum Master", "Se vigila en cada Daily; //time-boxing//"),
]


def control(d):
    rows = [[{"text": "**CONTROL DE VERSIONES**", "span": 6, "fill": GRIS, "align": "center"}],
            [{"text": "**%s**" % h, "fill": GRIS2, "align": "center", "size": 13} for h in ["Versión", "Hecho por", "Revisado por", "Aprobado por", "Fecha", "Motivo"]],
            [{"text": v, "align": "center", "size": 13} for v in VERSION]]
    d.table(rows, widths_cm=[1.6, 3.6, 3.2, 3.8, 2.0, 3.6], border="9AA1AB", sz=4, cell_margin=50)


def ficha(d, r, primera):
    if not primera:
        d.page_break()
    d.p("GRUPO D3 · NEWBIT · RIESGOS PRIORITARIOS AL INICIO DEL SPRINT 2 (02/11/2026)", size=13, b=True, color=ROJO, after=60)
    control(d)
    d.p("RIESGO DEL PROYECTO", size=30, b=True, align="center", before=40, after=40)
    cab = {"fill": GRIS, "align": "center", "size": 14}
    rows = [[dict(cab, text="**CÓDIGO Y NOMBRE DEL PROYECTO**"), dict(cab, text="**CÓDIGO DEL RIESGO**")],
            [{"text": PROYECTO, "size": 14}, {"text": "**%s**" % r["cod"], "align": "center", "size": 18}]]
    d.table(rows, widths_rel=[1.55, 1], border="9AA1AB", sz=4)
    filas = [("DESCRIPCIÓN DEL RIESGO", "Describir detalladamente el riesgo identificado en el proyecto.", "**%s.** %s" % (r["nombre"], r["desc"])),
             ("CAUSA RAÍZ", "Describir las causas subyacentes que ocasionan el riesgo.", r["causa"]),
             ("TRIGGER", "Describir el evento o situación que indicaría la aparición inminente de un riesgo.", r["trigger"]),
             ("ENTREGABLES AFECTADOS", "Describir el entregable afectado por el riesgo.", r["entregables"])]
    rows = [[{"text": "**IDENTIFICACIÓN DEL RIESGO**", "span": 2, "fill": GRIS, "align": "center", "size": 15}]]
    for t, ins, v in filas:
        rows.append([{"paras": ["**%s**" % t, "//%s//" % ins], "fill": GRIS2, "size": 13},
                     {"text": v, "size": 14}])
    d.table(rows, widths_rel=[1, 2.35], border="9AA1AB", sz=4, keep_rows=True)
    pi = r["p"] * r["i"]
    tp = tipo_de(pi)
    pname = [n for n, v in PROB if abs(v - r["p"]) < 1e-9][0]
    iname = [n for n, v in IMP if abs(v - r["i"]) < 1e-9][0]
    rows = [[{"text": "**EVALUACIÓN DEL RIESGO**", "span": 4, "fill": GRIS, "align": "center", "size": 15}],
            [dict(cab, text="**ESTIMACIÓN DE PROBABILIDAD**"), dict(cab, text="**ESTIMACIÓN DE IMPACTO**"),
             dict(cab, text="**PROBABILIDAD POR IMPACTO**"), dict(cab, text="**TIPO DE RIESGO**")],
            [{"text": "**%s – %s**" % (num(r["p"]), pname), "align": "center", "size": 16},
             {"text": "**%s – %s**" % (num(r["i"]), iname), "align": "center", "size": 16},
             {"text": "**%s × %s = %s**" % (num(r["p"]), num(r["i"]), num(pi)), "align": "center", "size": 16},
             {"text": "**%s (%s)**" % (tp.upper(), [x[1] for x in TIPO if x[0] == tp][0].replace("Mayor a ", "> ").replace("Menor a ", "< ")), "align": "center", "size": 16}]]
    d.table(rows, widths_rel=[1, 1, 1, 1], border="9AA1AB", sz=4, keep_rows=True)
    # tabla de escalas con la probabilidad, el impacto y el tipo elegidos resaltados (como en el ejemplo)
    rows = [[{"text": "**%s**" % h, "fill": GRIS, "align": "center", "size": 12} for h in
             ["PROBABILIDAD", "VALOR NUMÉRICO", "IMPACTO", "VALOR NUMÉRICO", "TIPO DE RIESGO", "PROBABILIDAD × IMPACTO"]]]
    for k in range(5):
        fp = ROSA if abs(PROB[k][1] - r["p"]) < 1e-9 else None
        fi = ROSA if abs(IMP[k][1] - r["i"]) < 1e-9 else None
        ft = ROSA if TIPO[k][0] == tp else None
        rows.append([{"text": PROB[k][0], "fill": fp, "size": 12}, {"text": ("%.1f" % PROB[k][1]).replace(".", ","), "fill": fp, "align": "center", "size": 12},
                     {"text": IMP[k][0], "fill": fi, "size": 12}, {"text": num(IMP[k][1]), "fill": fi, "align": "center", "size": 12},
                     {"text": TIPO[k][0], "fill": ft, "size": 12}, {"text": TIPO[k][1], "fill": ft, "align": "center", "size": 12}])
    d.table(rows, widths_rel=[1.6, 0.8, 1.4, 0.8, 1.4, 1.6], border="9AA1AB", sz=4, keep_rows=True)


def build_docx(path):
    d = Doc(landscape=True, margins_cm=(1.3, 1.5, 1.1, 1.5), font="Georgia", size=15,
            header=[("UNIVERSIDAD NACIONAL DEL SANTA  |  INGENIERÍA DE SOFTWARE II\tFGAP050 – Riesgo del Proyecto",
                     {"size": 13, "color": ROJO, "b": True, "tab_cm": (26.6, "right"), "after": 0})],
            footer=[("Universidad Nacional del Santa · Grupo D3 · NewBit (PY-NB-001) · Semana 8 · Página {PAGE}",
                     {"size": 13, "color": "707070", "align": "center"})],
            title="FGAP050 Riesgo del Proyecto – NewBit", subject="Riesgos prioritarios del Grupo D3 al inicio del Sprint 2")
    for k, r in enumerate(RIESGOS):
        ficha(d, r, k == 0)
    d.p("{PC}: aprobación del Product Owner de las tres fichas; GPU NVIDIA en los equipos del grupo (R-03). P e I son estimaciones del equipo "
        "y los umbrales de los triggers, propuestas.", size=13, i=True, before=80, after=0)
    d.save(path)


NOTAS = [
    "Los riesgos en negrita son los que tienen ficha (R-01, R-02 y R-03). Sus tareas de respuesta están en la EDT del Sprint 2 (FGAP110) y en el cronograma (FGAP130).",
    "La numeración R-01 a R-07 se asigna en este documento según el orden del Acta; el Acta no los numeraba.",
    "Los umbrales de los triggers (20 min por época, 10 % de frames sin detección) son **propuestas** del equipo: no hay métricas propias demostradas todavía.",
    "Según la Guía del SBOK, el Product Owner es el dueño de los riesgos y los Developers implementan las respuestas durante el sprint; el Scrum Master los vigila y "
    "los comunica. Los riesgos se reevalúan en cada planificación y retrospectiva.",
    "Aprobación del Product Owner de esta evaluación: {PC}.",
]


def build_md(path):
    L = []
    L.append("# FGAP050 – Riesgo del Proyecto: NewBit (R-01, R-02 y R-03)")
    L.append("")
    L.append("- **Archivos para entregar** (esta carpeta): `%s.docx` (editable) y `%s.pdf`: una ficha por riesgo (R-01, R-02 y R-03), una por página." % (BASE, BASE))
    L.append("- **Formato:** el de los ejemplos del docente ([ejemplo 1](../../material-del-profe/riesgo-fgap050-ejemplo-1/riesgo-fgap050-ejemplo-1.md), "
             "[ejemplo 2](../../material-del-profe/riesgo-fgap050-ejemplo-2/riesgo-fgap050-ejemplo-2.md)); no llegó FGAP050 en blanco. "
             "Cada ficha es una página completa del formato (control de versiones, identificación, evaluación y tabla de escalas con lo elegido resaltado).")
    L.append("- **Generador:** `generar_fgap050.py` (usa `docx_nb.py` de la carpeta del FGAP110). PDF exportado con Pages (Word no acepta «guardar como» por AppleScript en esta Mac).")
    L.append("- **Fecha:** 02/11/2026 (inicio del Sprint 2) · **Versión:** 1.0 (Grupo D3).")
    L.append("- **Fuente de los riesgos:** sección «Riesgos generales del proyecto» del Acta (`FGAP010_Acta_Constitucion_NewBit.docx`, v2.0), la misma lista que la Tabla de riesgos del Producto de la Unidad I.")
    L.append("")
    L.append("## Control de versiones")
    L.append("| Versión | Hecho por | Revisado por | Aprobado por | Fecha | Motivo |")
    L.append("|---|---|---|---|---|---|")
    L.append("| " + " | ".join(md_from_markup(v) for v in VERSION) + " |")
    L.append("")
    L.append("**Código y nombre del proyecto:** " + PROYECTO)
    L.append("")
    for r in RIESGOS:
        pi = r["p"] * r["i"]
        tp = tipo_de(pi)
        pname = [n for n, v in PROB if abs(v - r["p"]) < 1e-9][0]
        iname = [n for n, v in IMP if abs(v - r["i"]) < 1e-9][0]
        L.append("## %s · %s" % (r["cod"], r["nombre"]))
        L.append("| Campo | Contenido |")
        L.append("|---|---|")
        L.append("| **Descripción del riesgo** | %s |" % md_from_markup(r["desc"]))
        L.append("| **Causa raíz** | %s |" % md_from_markup(r["causa"]))
        L.append("| **Trigger** | %s |" % md_from_markup(r["trigger"]))
        L.append("| **Entregables afectados** | %s |" % md_from_markup(r["entregables"]))
        L.append("| **Estimación de probabilidad** | %s – %s |" % (num(r["p"]), pname))
        L.append("| **Estimación de impacto** | %s – %s |" % (num(r["i"]), iname))
        L.append("| **Probabilidad por impacto** | %s × %s = **%s** |" % (num(r["p"]), num(r["i"]), num(pi)))
        L.append("| **Tipo de riesgo** | **%s** |" % tp.upper())
        L.append("")
    L.append("## Tabla de escalas (del docente)")
    L.append("| Probabilidad | Valor | Impacto | Valor | Tipo de riesgo | P × I |")
    L.append("|---|---|---|---|---|---|")
    for k in range(5):
        L.append("| %s | %s | %s | %s | %s | %s |" % (PROB[k][0], ("%.1f" % PROB[k][1]).replace(".", ","), IMP[k][0], num(IMP[k][1]), TIPO[k][0], TIPO[k][1]))
    L.append("")
    L.append("En cada ficha del Word se resaltan la probabilidad, el impacto y el tipo elegidos, como en el ejemplo del docente.")
    L.append("")
    L.append("## Notas de trabajo (no van en el formato)")
    L.append("")
    L.append("### Sustento de las estimaciones y respuesta prevista")
    L.append("| Riesgo | Sustento de P e I | Respuesta prevista (tareas de la EDT del Sprint 2) |")
    L.append("|---|---|---|")
    for r in RIESGOS:
        L.append("| %s | %s | %s |" % (r["cod"], md_from_markup(r["sustento"]), md_from_markup(r["respuesta"])))
    L.append("")
    L.append("### Priorización de los 7 riesgos del Acta al 02/11/2026")
    L.append("Se hizo ficha de los riesgos con P × I ≥ 0,20 que necesitan tareas en el Sprint 2 (Guía del SBOK: backlog priorizado ajustado al riesgo).")
    L.append("")
    L.append("| Código | Riesgo (Acta) | P | I | P × I | Tipo | Situación al 02/11/2026 | Tratamiento en el Sprint 2 |")
    L.append("|---|---|:-:|:-:|:-:|---|---|---|")
    for c, n, p, i, s, t in RESUMEN:
        pi = p * i
        L.append("| %s | %s | %s | %s | %s | %s | %s | %s |" % ("**%s**" % c if pi >= 0.2 else c, n, num(p), num(i), "**%s**" % num(pi) if pi >= 0.2 else num(pi), tipo_de(pi), s, md_from_markup(t)))
    L.append("")
    L.append("### Notas")
    for t in NOTAS:
        L.append("- " + md_from_markup(t))
    L.append("- **Diferencia con el `.md` del Acta:** su resumen nombra los riesgos de otra forma («reproducibilidad de pesos», «iluminación y oclusiones», «transferibilidad de dominio»). "
             "Aquí se usa la lista del `.docx` del Acta (lo que se entregó), que coincide con el Producto de la Unidad I. Conviene corregir el resumen del `.md` del Acta.")
    L.append("")
    L.append("## POR CONFIRMAR")
    L.append("1. **Aprobación del Product Owner** de las fichas y de la priorización.")
    L.append("2. **GPU NVIDIA en los equipos del grupo** (causa raíz de R-03).")
    L.append("3. Los umbrales de los triggers son propuestas; el PO puede ajustarlos en la planificación.")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "."
    os.makedirs(out, exist_ok=True)
    build_docx(os.path.join(out, BASE + ".docx"))
    build_md(os.path.join(out, BASE + ".md"))
    print("ok", out)
