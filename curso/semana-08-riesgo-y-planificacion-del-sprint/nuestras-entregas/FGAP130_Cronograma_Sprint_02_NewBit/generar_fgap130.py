# -*- coding: utf-8 -*-
"""Genera FGAP130_Cronograma_Sprint_02_NewBit.docx y su .md a partir de plan_sprint02.py
(las mismas tareas e IDs de la EDT FGAP110). Uso: python3 generar_fgap130.py <carpeta_salida>
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
# docx_nb.py y plan_sprint02.py viven en la carpeta del FGAP110 (fuente única)
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "FGAP110_EDT_Sprint_02_NewBit")))
sys.path.insert(0, HERE)
import plan_sprint02 as P  # noqa: E402
from docx_nb import Doc, md_from_markup  # noqa: E402

BASE = "FGAP130_Cronograma_Sprint_02_NewBit"
ROJO = "8B1E2D"
COLOR = {"HU": ("8B1E2D", "E9B9C0"), "SC": ("8B1E2D", "E9B9C0"), "R": ("8B1E2D", "E9B9C0")}
FRANJA_FUERA = "F7ECEE"
CLARO = "FAFAFA"
HITO_AZUL = "1F5F99"

VERSION = ["1.0", "Developers (Anthony Lopez y Luis Salazar)", "Anthony Lopez – Scrum Master",
           "Albert Chumacero – Product Owner · {PC}", "02/11/2026", "Cronograma inicial del Sprint 02"]

NOTAS = [
    "**Mismas tareas que la EDT.** T01–T14 y sus horas son las del FGAP110 del Sprint 02 (fuente común: `plan_sprint02.py`).",
    "**Dos Developers, máximo 2 tareas por día.** Cada día hay como mucho una tarea de Luis y una de Anthony (tabla de asignación diaria). "
    "Albert Chumacero (Product Owner) no desarrolla: refina el backlog, aclara criterios y acepta o rechaza en la revisión.",
    "**Ceremonias (no son tareas):** planificación el 02/11; Daily de 15 min cada día; revisión y retrospectiva el 13/11. Por eso el primer y el último día tienen poca carga.",
    "**SC-001 es condicional.** Las filas de SC-001 (T06–T09), R-01 (T10) y R-03 (T14) dependen de que el Product Owner apruebe la solicitud de cambio (FGAP090): {PC}. "
    "Si la rechaza, el cronograma queda con T01–T05 y T11–T13 y el hito no cambia.",
    "**Regla de corte (FGAP090):** si el 10/11 se activa el trigger de R-01 o de R-03 (T10), HU07 vuelve al Product Backlog y T08–T09 no se ejecutan.",
    "Duraciones en días hábiles (lunes a viernes). Fechas, dependencias y horas son una **estimación** de la planificación, no un avance real.",
]


def tarea_de(persona, dia):
    """Tarea de una persona en un día (T12: Luis el primer día y Anthony el segundo)."""
    for t in P.TAREAS:
        if t[6] <= dia <= t[6] + t[7] - 1:
            quien = (P.L if dia == t[6] else P.A) if t[0] == "T12" else t[4]
            if quien == persona:
                return t[0]
    return "—"


def build_docx(path):
    d = Doc(landscape=True, margins_cm=(1.3, 1.2, 1.1, 1.2), font="Georgia", size=15,
            header=[("\tFGAP130 – CRONOGRAMA DEL SPRINT  |  NewBit (PY-NB-001)", {"size": 13, "color": ROJO, "b": True, "tab_cm": (27.2, "right"), "after": 0})],
            footer=[("FGAP130 • Ingeniería de Software II • UNS • Grupo D3 • Página {PAGE}", {"size": 13, "color": ROJO, "align": "right"})],
            title="FGAP130 Cronograma del Sprint 02 – NewBit", subject="Cronograma del Sprint 02 del Grupo D3")
    d.p("UNIVERSIDAD NACIONAL DEL SANTA", size=26, b=True, color=ROJO, align="center", after=0)
    d.p("Ingeniería de Software II  •  Docente: Dr. Alfredo Daza Vergaray", size=16, align="center", after=60)
    rows = [[{"text": "**CONTROL DE VERSIONES**", "span": 6, "fill": "D9DDE3", "align": "center"}],
            [{"text": "**%s**" % h, "fill": "EEF0F3", "align": "center", "size": 14} for h in ["Versión", "Hecho por", "Revisado por", "Aprobado por", "Fecha", "Motivo"]],
            [{"text": v, "align": "center", "size": 14} for v in VERSION]]
    d.table(rows, widths_rel=[0.7, 2.4, 2.0, 2.4, 1.0, 2.4], border="BFC5CE", sz=4, cell_margin=50)
    d.p("CRONOGRAMA DEL SPRINT", size=30, b=True, i=True, color="1F2A44", align="center", before=60, after=60)
    rows = [[{"text": "**CÓDIGO Y NOMBRE DEL PROYECTO**", "fill": "D9DDE3", "align": "center", "size": 14},
             {"text": "**SPRINT NÚMERO**", "fill": "D9DDE3", "align": "center", "size": 14}],
            [{"text": P.PROYECTO, "size": 14}, {"text": "**%s**  |  02–13 de noviembre de 2026" % P.SPRINT, "align": "center", "size": 14}]]
    d.table(rows, widths_rel=[3.2, 1.1], border="BFC5CE", sz=4, cell_margin=50)
    d.p("**Objetivo del sprint:** " + P.OBJETIVO, size=15, after=60)
    # --- Gantt ---------------------------------------------------------
    w_fixed = [7.35, 1.45, 1.65, 1.4, 1.9]
    w_day = (27.3 - sum(w_fixed)) / 10.0
    widths = w_fixed + [w_day] * 10
    hdr1 = [{"text": "**Nombre de tarea / Historia**", "fill": "D9DDE3", "vmerge": "restart", "align": "center", "size": 13},
            {"text": "**Duración**", "fill": "D9DDE3", "vmerge": "restart", "align": "center", "size": 13},
            {"text": "**Comienzo**", "fill": "D9DDE3", "vmerge": "restart", "align": "center", "size": 13},
            {"text": "**Fin**", "fill": "D9DDE3", "vmerge": "restart", "align": "center", "size": 13},
            {"text": "**Predecesora**", "fill": "D9DDE3", "vmerge": "restart", "align": "center", "size": 13}]
    hdr1 += [{"text": "**%s**" % dl, "fill": "D9DDE3", "align": "center", "size": 13} for dl, _ in P.DIAS]
    hdr2 = [{"text": "", "fill": "D9DDE3", "vmerge": "cont"} for _ in range(5)]
    hdr2 += [{"text": "**%s**" % df, "fill": "D9DDE3", "align": "center", "size": 12} for _, df in P.DIAS]
    rows = [hdr1, hdr2]
    for n in P.NODOS:
        oscuro, banda = COLOR[n["tipo"]]
        ini, fin = P.span_nodo(n["id"])
        dur = fin - ini + 1
        etiqueta = "%s · %s" % (n["id"], n["titulo"])
        r = [{"text": "**%s**" % etiqueta, "fill": oscuro, "color": "FFFFFF", "size": 13},
             {"text": "**%d %s**" % (dur, "día" if dur == 1 else "días"), "fill": banda, "align": "center", "size": 13},
             {"text": "**%s**" % P.fecha(ini), "fill": banda, "align": "center", "size": 13},
             {"text": "**%s**" % P.fecha(fin), "fill": banda, "align": "center", "size": 13},
             {"text": "", "fill": banda}]
        r += [{"text": "", "fill": banda if ini <= k <= fin else FRANJA_FUERA} for k in range(1, 11)]
        rows.append(r)
        for t in P.tareas_de(n["id"]):
            a, b = t[6], t[6] + t[7] - 1
            r = [{"text": "%s · %s" % (t[0], t[2]), "size": 13},
                 {"text": "%d %s" % (t[7], "día" if t[7] == 1 else "días"), "align": "center", "size": 13},
                 {"text": P.fecha(a), "align": "center", "size": 13},
                 {"text": P.fecha(b), "align": "center", "size": 13},
                 {"text": ", ".join(t[8]) or "—", "align": "center", "size": 13}]
            r += [{"text": "**▬**" if a <= k <= b else "", "fill": "A3283A" if a <= k <= b else None, "color": "FFFFFF", "align": "center", "size": 12}
                  for k in range(1, 11)]
            rows.append(r)
    nombre, dia, pred = P.HITO
    r = [{"text": "**◆ %s**" % nombre, "size": 13}, {"text": "Hito", "align": "center", "size": 13},
         {"text": P.fecha(dia), "align": "center", "size": 13}, {"text": P.fecha(dia), "align": "center", "size": 13},
         {"text": ", ".join(pred), "align": "center", "size": 13}]
    r += [{"text": "**◆**" if k == dia else "", "fill": HITO_AZUL if k == dia else None, "color": "FFFFFF", "align": "center", "size": 15} for k in range(1, 11)]
    rows.append(r)
    d.table(rows, widths_cm=widths, border="BFC5CE", sz=4, cell_margin=40, header_rows=2, keep_rows=True)
    d.p("**Leyenda:** Barras rojas: tareas programadas  •  Franja rosa: historia de usuario, solicitud de cambio o riesgo (nodo de la EDT)  •  Rombo azul: hito  •  "
        "Días hábiles (lunes a viernes).", size=13, after=20)
    d.p("**Nota:** tareas e IDs de la EDT del Sprint 02 (FGAP110); fechas, dependencias y duraciones son estimaciones de la planificación. Dos Developers (Luis Salazar y "
        "Anthony Lopez): como máximo 2 tareas en paralelo por día; el PO no desarrolla. {PC}: aprobación del PO y decisión sobre SC-001 (si la rechaza, salen T06–T10 y T14).",
        size=13, after=0)
    d.save(path)
    return tarea_de


def build_md(path, tarea_de):
    L = []
    L.append("# FGAP130 – Cronograma del Sprint 02: NewBit")
    L.append("")
    L.append("- **Archivos para entregar** (esta carpeta): `%s.docx` (editable) y `%s.pdf`." % (BASE, BASE))
    L.append("- **Estructura:** la del [ejemplo FGAP130 del docente](../../material-del-profe/cronograma-del-sprint-fgap130-ejemplo/cronograma-del-sprint-fgap130-ejemplo.md) "
             "(no llegó formato en blanco): control de versiones, proyecto y sprint, objetivo, Gantt con duración, comienzo, fin y predecesora, e hito de revisión.")
    L.append("- **Generador:** `generar_fgap130.py`, que lee `plan_sprint02.py` y `docx_nb.py` de la carpeta del FGAP110 (la misma fuente de tareas de la EDT). El Gantt es una tabla de Word editable (celdas coloreadas). PDF exportado con Pages.")
    L.append("- **Fecha:** 02/11/2026 · **Versión:** 1.0 (Grupo D3).")
    L.append("- **Coherencia:** mismas tareas, IDs y horas que la [EDT del Sprint 02 (FGAP110)](../FGAP110_EDT_Sprint_02_NewBit/FGAP110_EDT_Sprint_02_NewBit.md).")
    L.append("")
    L.append("## Control de versiones")
    L.append("| Versión | Hecho por | Revisado por | Aprobado por | Fecha | Motivo |")
    L.append("|---|---|---|---|---|---|")
    L.append("| " + " | ".join(md_from_markup(v) for v in VERSION) + " |")
    L.append("")
    L.append("## Cronograma del sprint")
    L.append("| Código y nombre del proyecto | Sprint número |")
    L.append("|---|---|")
    L.append("| %s | %s (02–13/11/2026, 10 días hábiles) |" % (P.PROYECTO, P.SPRINT))
    L.append("")
    L.append("**Objetivo del sprint:** " + P.OBJETIVO)
    L.append("")
    cab = "| Nombre de tarea / Historia | Duración | Comienzo | Fin | Predecesora | " + " | ".join("%s %s" % x for x in P.DIAS) + " |"
    L.append(cab)
    L.append("|---|---|---|---|---|" + "|".join([":-:"] * 10) + "|")
    for n in P.NODOS:
        ini, fin = P.span_nodo(n["id"])
        dur = fin - ini + 1
        L.append("| **%s · %s** | **%d %s** | **%s** | **%s** | | %s |" % (
            n["id"], n["titulo"], dur, "día" if dur == 1 else "días", P.fecha(ini), P.fecha(fin),
            " | ".join("░" if ini <= k <= fin else "" for k in range(1, 11))))
        for t in P.tareas_de(n["id"]):
            a, b = t[6], t[6] + t[7] - 1
            L.append("| %s · %s | %d %s | %s | %s | %s | %s |" % (
                t[0], t[2], t[7], "día" if t[7] == 1 else "días", P.fecha(a), P.fecha(b), ", ".join(t[8]) or "—",
                " | ".join("█" if a <= k <= b else "" for k in range(1, 11))))
    nombre, dia, pred = P.HITO
    L.append("| **◆ %s** | Hito | %s | %s | %s | %s |" % (nombre, P.fecha(dia), P.fecha(dia), ", ".join(pred),
                                                     " | ".join("◆" if k == dia else "" for k in range(1, 11))))
    L.append("")
    L.append("Leyenda: █ tarea programada · ░ duración del nodo de la EDT (historia, solicitud de cambio o riesgo) · ◆ hito · días hábiles de lunes a viernes. "
             "En el Word, como en el ejemplo del docente: barras rojas, franja rosa y rombo azul.")
    L.append("")
    L.append("## Notas de trabajo (no van en el formato)")
    L.append("")
    L.append("### Asignación diaria por Developer (máximo 2 tareas en paralelo)")
    L.append("| Developer | " + " | ".join("%s %s" % x for x in P.DIAS) + " | Horas |")
    L.append("|---|" + "|".join([":-:"] * 10) + "|:-:|")
    for persona, horas in ((P.L, 26), (P.A, 17)):
        L.append("| %s | %s | %d h |" % (persona, " | ".join(tarea_de(persona, k) for k in range(1, 11)), horas))
    L.append("| Tareas en paralelo | %s | 43 h |" % " | ".join(str(sum(1 for p in (P.L, P.A) if tarea_de(p, k) != "—")) for k in range(1, 11)))
    L.append("")
    L.append("### Notas")
    for t in NOTAS:
        L.append("- " + md_from_markup(t))
    L.append("")
    L.append("## POR CONFIRMAR")
    L.append("1. **Aprobación del Product Owner** del cronograma (control de versiones).")
    L.append("2. **Decisión del PO sobre SC-001** (FGAP090): si la rechaza, salen T06–T10 y T14.")
    L.append("3. **Dataset completo descargado** y **acceso a GPU en Colab** (supuestos de T05, T06, T08, T10, T11 y T14).")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "."
    os.makedirs(out, exist_ok=True)
    P.verificar()
    build_docx(os.path.join(out, BASE + ".docx"))
    build_md(os.path.join(out, BASE + ".md"), tarea_de)
    print("ok", out)
