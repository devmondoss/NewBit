# -*- coding: utf-8 -*-
"""Genera el FGAP080 de NewBit (Cronograma de Planificación de Lanzamiento) con las tareas de cada sprint:
  1. FGAP080_Cronograma_Lanzamiento_NewBit.xml  -> proyecto de MS Project (MSPDI) con tareas, vínculos y recursos;
     se abre en MS Project (Archivo > Abrir > XML), ProjectLibre o herramientas/mini-project y se guarda como .mpp.
  2. Gantt_Lanzamiento_NewBit.png (vista resumen) y Gantt_Lanzamiento_NewBit_<n>.png (detalle por sprint),
     dibujados al estilo de la vista Diagrama de Gantt de MS Project.
  3. FGAP080_Cronograma_Lanzamiento_NewBit.docx -> el formato del docente con los Gantt; y su .md.
Uso: python3 -I generar_fgap080.py [--pdf]                 (desde plan_lanzamiento.py; reescribe también el XML)
     python3 -I generar_fgap080.py --xml X.xml [--pdf]     (desde el XML editado en Mini Project; no toca el XML)
--pdf exporta el Word a PDF con Pages (macOS).
"""
import argparse
import datetime as dt
import glob
import os
import subprocess
import sys
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape

sys.dont_write_bytecode = True  # no dejar __pycache__ en las carpetas de entregas
HERE = os.path.dirname(os.path.abspath(__file__))
FGAP110 = os.path.abspath(os.path.join(HERE, "..", "..", "..", "semana-08-riesgo-y-planificacion-del-sprint",
                                       "nuestras-entregas", "FGAP110_EDT_Sprint_02_NewBit"))
sys.path.insert(0, FGAP110)  # docx_nb.py (generador de Word del equipo)
sys.path.insert(0, HERE)
import plan_lanzamiento as P  # noqa: E402

BASE = "FGAP080_Cronograma_Lanzamiento_NewBit"
PNG = "Gantt_Lanzamiento_NewBit.png"
FECHA_DOC = "09/11/2026"
AUTOR = "Anthony Gabriel Lopez Yrribarren"  # actividad individual
VERSION = ["1.0", AUTOR, "Albert Chumacero – Product Owner", "Ricardo Salcedo – Sponsor", FECHA_DOC,
           "Cronograma de lanzamiento con las tareas de los 4 sprints"]
FERIADOS = None   # None = calendario del plan (feriados no descontados); lista = feriados del XML
DESDE_XML = None  # nombre del XML si el cronograma viene del editor
MAX_FILAS_PAGINA = 24


def proyecto(T):
    ini, fin, dur = P.proyecto(T)
    return ini, fin, dur - sum(1 for f in (FERIADOS or []) if ini <= f <= fin and f.weekday() < 5)


def texto_feriados():
    if FERIADOS:
        return "feriados descontados: %s." % ", ".join(f.strftime("%d/%m") for f in FERIADOS)
    return "los feriados del 08/10 y 08/12 no se descuentan, igual que en el Acta y el burndown."


def recursos_de(t):
    return [r.strip() for r in (t.get("resp") or "").split(";") if r.strip()]


# ---------------------------------------------------------------- 1. MSPDI (XML de MS Project)
def _dt(d, hora):
    return "%sT%s" % (d.isoformat(), hora)


def build_xml(T, path):
    ini, fin, dur = proyecto(T)
    wd = []
    for k in range(1, 8):  # 1 = domingo ... 7 = sábado
        if k in (1, 7):
            wd.append("<WeekDay><DayType>%d</DayType><DayWorking>0</DayWorking></WeekDay>" % k)
        else:
            wd.append("<WeekDay><DayType>%d</DayType><DayWorking>1</DayWorking><WorkingTimes>"
                      "<WorkingTime><FromTime>08:00:00</FromTime><ToTime>12:00:00</ToTime></WorkingTime>"
                      "<WorkingTime><FromTime>13:00:00</FromTime><ToTime>17:00:00</ToTime></WorkingTime>"
                      "</WorkingTimes></WeekDay>" % k)
    cal = ("<Calendars><Calendar><UID>1</UID><Name>Estándar</Name><IsBaseCalendar>1</IsBaseCalendar>"
           "<BaseCalendarUID>-1</BaseCalendarUID><WeekDays>%s</WeekDays></Calendar></Calendars>" % "".join(wd))

    def task(t, wbs):
        hito = t["tipo"] == "hito"
        x = ["<Task><UID>%d</UID><ID>%d</ID><Name>%s</Name><Type>1</Type><IsNull>0</IsNull>" % (t["id"], t["id"], escape(t["nombre"])),
             "<WBS>%s</WBS><OutlineNumber>%s</OutlineNumber><OutlineLevel>%d</OutlineLevel><Priority>500</Priority>" % (wbs, wbs, t["nivel"]),
             "<Start>%s</Start><Finish>%s</Finish>" % (_dt(t["ini"], "17:00:00" if hito else "08:00:00"), _dt(t["fin"], "17:00:00")),
             "<Duration>PT%dH0M0S</Duration><DurationFormat>7</DurationFormat>" % (t["dur"] * 8),
             "<Milestone>%d</Milestone><Summary>%d</Summary>" % (hito, t["tipo"] == "resumen")]
        if t.get("cini"):
            x.append("<ConstraintType>4</ConstraintType><ConstraintDate>%s</ConstraintDate>" % _dt(t["cini"], "08:00:00"))
        else:
            x.append("<ConstraintType>0</ConstraintType>")
        for p in t.get("pred", []):
            x.append("<PredecessorLink><PredecessorUID>%d</PredecessorUID><Type>1</Type><CrossProject>0</CrossProject>"
                     "<LinkLag>0</LinkLag><LagFormat>7</LagFormat></PredecessorLink>" % p)
        x.append("</Task>")
        return "".join(x)

    tasks = [task(dict(id=0, nombre="NewBit (PY-NB-001)", nivel=0, tipo="resumen", ini=ini, fin=fin, dur=dur), "0")]
    cont = []
    for t in T:
        cont = (cont + [0] * t["nivel"])[:t["nivel"]]
        cont[-1] += 1
        tasks.append(task(t, ".".join(map(str, cont))))
    nombres = []
    for t in T:
        for r in recursos_de(t):
            if r not in nombres:
                nombres.append(r)
    ruid = {r: i + 1 for i, r in enumerate(nombres)}
    res = "".join("<Resource><UID>%d</UID><ID>%d</ID><Name>%s</Name><Type>1</Type><IsNull>0</IsNull><MaxUnits>1.00</MaxUnits></Resource>"
                  % (ruid[r], ruid[r], escape(r)) for r in nombres)
    asig, k = [], 0
    for t in T:
        for r in recursos_de(t):
            k += 1
            asig.append("<Assignment><UID>%d</UID><TaskUID>%d</TaskUID><ResourceUID>%d</ResourceUID><Units>1</Units></Assignment>"
                        % (k, t["id"], ruid[r]))
    xml = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
           '<Project xmlns="http://schemas.microsoft.com/project">'
           "<SaveVersion>14</SaveVersion><Name>%s.xml</Name><Title>%s</Title><Author>%s</Author>"
           "<CreationDate>2026-11-09T08:00:00</CreationDate><ScheduleFromStart>1</ScheduleFromStart>"
           "<StartDate>%s</StartDate><FinishDate>%s</FinishDate><CalendarUID>1</CalendarUID>"
           "<DefaultStartTime>08:00:00</DefaultStartTime><DefaultFinishTime>17:00:00</DefaultFinishTime>"
           "<MinutesPerDay>480</MinutesPerDay><MinutesPerWeek>2400</MinutesPerWeek><DaysPerMonth>20</DaysPerMonth>"
           "<DefaultTaskType>1</DefaultTaskType><DurationFormat>7</DurationFormat>"
           "%s<Tasks>%s</Tasks><Resources>%s</Resources><Assignments>%s</Assignments></Project>\n") % (
        BASE, escape(P.PROYECTO), escape(AUTOR), _dt(ini, "08:00:00"), _dt(fin, "17:00:00"), cal, "".join(tasks), res, "".join(asig))
    with open(path, "w", encoding="utf-8") as f:
        f.write(xml)


# ---------------------------------------------------------------- lectura del XML (MSPDI) editado
def leer_xml(path):
    """Devuelve (tareas, feriados) con el mismo formato que plan_lanzamiento.calcular()."""
    ns = {"p": "http://schemas.microsoft.com/project"}
    raiz = ET.parse(path).getroot()
    tx = lambda e, n: (e.findtext("p:" + n, default="", namespaces=ns) or "").strip()  # noqa: E731
    fecha = lambda s: dt.date.fromisoformat(s[:10])  # noqa: E731
    feriados = set()
    for ex in raiz.findall("p:Calendars/p:Calendar/p:Exceptions/p:Exception", ns):
        if tx(ex, "DayWorking") == "0":
            tp = ex.find("p:TimePeriod", ns)
            a, b = fecha(tx(tp, "FromDate")), fecha(tx(tp, "ToDate"))
            while a <= b:
                feriados.add(a)
                a += dt.timedelta(days=1)
    rec = {tx(r, "UID"): tx(r, "Name") for r in raiz.findall("p:Resources/p:Resource", ns) if tx(r, "Name")}
    asig = {}
    for a in raiz.findall("p:Assignments/p:Assignment", ns):
        if tx(a, "ResourceUID") in rec:
            asig.setdefault(tx(a, "TaskUID"), []).append(rec[tx(a, "ResourceUID")])
    crudas = []
    for e in raiz.findall("p:Tasks/p:Task", ns):
        if tx(e, "UID") == "0" or tx(e, "IsNull") == "1" or tx(e, "OutlineLevel") in ("", "0"):
            continue
        dur = tx(e, "Duration")
        horas = float(dur[2:dur.index("H")]) if dur.startswith("PT") and "H" in dur else 0.0
        crudas.append(dict(uid=tx(e, "UID"), id=int(tx(e, "ID")), nombre=tx(e, "Name"), nivel=int(tx(e, "OutlineLevel")),
                           dur=int(round(horas / 8)), ini=fecha(tx(e, "Start")), fin=fecha(tx(e, "Finish")),
                           hito=tx(e, "Milestone") == "1", resp="; ".join(asig.get(tx(e, "UID"), [])),
                           pred_uids=[tx(l, "PredecessorUID") for l in e.findall("p:PredecessorLink", ns)]))
    por_uid = {t["uid"]: t for t in crudas}
    T = []
    for i, t in enumerate(crudas):
        resumen = i + 1 < len(crudas) and crudas[i + 1]["nivel"] > t["nivel"]
        T.append(dict(id=t["id"], nombre=t["nombre"], nivel=t["nivel"], dur=t["dur"], ini=t["ini"], fin=t["fin"], resp=t["resp"],
                      tipo="resumen" if resumen else ("hito" if t["hito"] or t["dur"] == 0 else "tarea"),
                      pred=[por_uid[u]["id"] for u in t["pred_uids"] if u in por_uid]))
    if not T:
        raise SystemExit("El XML no tiene tareas")
    return T, sorted(feriados)


# ---------------------------------------------------------------- 2. Gantt al estilo de MS Project
def paginas(T):
    """Vista resumen (niveles 1 y 2) + páginas de detalle formadas por grupos de nivel 1 completos."""
    resumen, padre = [], None
    for t in T:  # como el modelo: nivel 1 y, dentro de cada sprint, sus 3 fases
        if t["nivel"] == 1:
            padre = t
            resumen.append(t)
        elif t["nivel"] == 2 and padre["nombre"].startswith("Sprint"):
            resumen.append(t)
    grupos, actual = [], []
    for t in T:
        if t["nivel"] == 1 and actual:
            grupos.append(actual)
            actual = []
        actual.append(t)
    grupos.append(actual)
    detalle, pag = [], []
    for g in grupos:
        if pag and len(pag) + len(g) > MAX_FILAS_PAGINA:
            detalle.append(pag)
            pag = []
        pag = pag + g
    detalle.append(pag)
    return resumen, detalle


def titulo_pagina(filas):
    return " · ".join(t["nombre"].split(" · ")[0] for t in filas if t["nivel"] == 1)


def dibujar_gantt(filas, path, T, detalle=False):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Polygon, Rectangle

    plt.rcParams["font.family"] = "Arial"
    ini, fin, dur = proyecto(T)
    if not detalle:
        filas = [dict(nombre="NewBit (PY-NB-001)", nivel=0, tipo="resumen", ini=ini, fin=fin, dur=dur, pred=[], id=0, resp="")] + filas
    a0 = min(t["ini"] for t in filas)
    a1 = max(t["fin"] for t in filas)
    d0 = a0 - dt.timedelta(days=a0.weekday())
    d1 = a1 + dt.timedelta(days=(6 - a1.weekday()) + (8 if detalle else 1))
    dias = (d1 - d0).days
    x = lambda d: (d - d0).days  # noqa: E731
    n = len(filas)
    W_T, W_G = 9.4, 10.6
    fig = plt.figure(figsize=((W_T + W_G) * 0.62, 0.25 * (n + 2.6)), dpi=230)
    at = fig.add_axes([0, 0, W_T / (W_T + W_G), 1])
    ag = fig.add_axes([W_T / (W_T + W_G), 0, W_G / (W_T + W_G), 1])
    H = n + 2
    for ax in (at, ag):
        ax.set_ylim(H, 0)
        ax.axis("off")
    at.set_xlim(0, W_T)
    ag.set_xlim(0, dias)
    GRIS, BORDE, VERDE = "#E8E8E8", "#C8C8C8", "#4E8F3A"
    FS = 6.9
    cols = [("", 0.0, 0.42), ("Nombre de tarea", 0.42, 5.38), ("Duración", 5.8, 0.95),
            ("Comienzo", 6.75, 1.33), ("Fin", 8.08, 1.32)]
    at.add_patch(Rectangle((0, 0), W_T, 2, color=GRIS, lw=0))
    at.plot([0, W_T], [2, 2], color=VERDE, lw=1.6)
    for titulo, cx, cw in cols:
        at.text(cx + 0.07, 1.35, titulo, fontsize=FS + 0.3, fontweight="bold", va="center", color="#1F1F1F")
        at.plot([cx + cw, cx + cw], [0, H], color=BORDE, lw=0.5)
    for i, t in enumerate(filas):
        y = 2 + i + 0.5
        at.plot([0, W_T], [2 + i + 1, 2 + i + 1], color="#EDEDED", lw=0.4)
        fw = "bold" if t["tipo"] == "resumen" else "normal"
        at.text(0.21, y, str(t["id"]), fontsize=FS - 0.6, ha="center", va="center", color="#5A5A5A")
        at.text(0.5 + 0.22 * t["nivel"], y, t["nombre"], fontsize=FS, fontweight=fw, va="center", color="#1F1F1F")
        at.text(5.86, y, P.f_dur(t), fontsize=FS, fontweight=fw, va="center")
        at.text(6.81, y, P.f_ms(t["ini"]), fontsize=FS, fontweight=fw, va="center")
        at.text(8.14, y, P.f_ms(t["fin"]), fontsize=FS, fontweight=fw, va="center")
    # escala de tiempo
    ag.add_patch(Rectangle((0, 0), dias, 2, color=GRIS, lw=0))
    ag.plot([0, dias], [1, 1], color=BORDE, lw=0.5)
    ag.plot([0, dias], [2, 2], color=BORDE, lw=0.8)
    MESES = ["", "enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre",
             "octubre", "noviembre", "diciembre"]
    LETRA = "LMXJVSD"
    if detalle:  # semanas arriba, días abajo
        d = d0
        while d < d1:
            ag.plot([x(d), x(d)], [0, H], color=BORDE if d == d0 else "#D0D0D0", lw=0.6)
            ag.text(x(d) + 3.5, 0.5, "semana del %s" % d.strftime("%d/%m"), fontsize=FS - 0.2, ha="center", va="center")
            d += dt.timedelta(days=7)
        d = d0
        while d < d1:
            ag.text(x(d) + 0.5, 1.5, "%s%d" % (LETRA[d.weekday()], d.day), fontsize=FS - 1.6, ha="center", va="center")
            if d.weekday() >= 5 or d in (FERIADOS or []):
                ag.add_patch(Rectangle((x(d), 2), 1, n, color="#F2F2F2", lw=0, zorder=0))
            d += dt.timedelta(days=1)
    else:  # meses arriba, semanas abajo
        d = d0
        while d < d1:
            nxt = min(dt.date(d.year + (d.month == 12), d.month % 12 + 1, 1), d1)
            ag.plot([x(d), x(d)], [0, 1], color=BORDE, lw=0.5)
            ag.text((x(d) + x(nxt)) / 2, 0.5, "%s %d" % (MESES[d.month], d.year), fontsize=FS, ha="center", va="center")
            d = nxt
        d = d0
        while d < d1:
            ag.plot([x(d), x(d)], [1, H], color=BORDE if d == d0 else "#DADADA", lw=0.5)
            ag.text(x(d) + 3.5, 1.5, d.strftime("%d/%m"), fontsize=FS - 0.4, ha="center", va="center")
            ag.add_patch(Rectangle((x(d) + 5, 2), 2, n, color="#F2F2F2", lw=0, zorder=0))
            d += dt.timedelta(days=7)
    # barras
    pos = {}
    alto = 0.44
    for i, t in enumerate(filas):
        yc = 2 + i + 0.5
        a = x(t["ini"]) + 8 / 24.0
        b = x(t["fin"]) + 17 / 24.0
        if t["tipo"] == "resumen":
            ag.add_patch(Rectangle((a, yc - 0.12), b - a, 0.16, color="#262626", lw=0, zorder=3))
            k = 0.18 if detalle else 0.35
            for xx in (a, b):
                ag.add_patch(Polygon([(xx - k, yc - 0.12), (xx + k, yc - 0.12), (xx, yc + 0.28)], closed=True, color="#262626", lw=0, zorder=3))
        elif t["tipo"] == "hito":
            k = 0.25 if detalle else 0.42
            ag.add_patch(Polygon([(b, yc - 0.34), (b + k, yc), (b, yc + 0.34), (b - k, yc)], closed=True, color="#1F1F1F", zorder=4))
            ag.text(b + 2 * k, yc, t["fin"].strftime("%d/%m"), fontsize=FS - 0.4, va="center")
            a = b
        else:
            ag.add_patch(Rectangle((a, yc - alto / 2), b - a, alto, facecolor="#8DB4E2", edgecolor="#4A7EBB", lw=0.6, zorder=3))
            if detalle and t.get("resp"):  # nombres de los recursos junto a la barra, como MS Project
                ag.text(b + 0.25, yc, t["resp"].replace("; ", ", "), fontsize=FS - 1.0, va="center", color="#333333", zorder=5)
        pos[t["id"]] = (a, b, yc)
    # flechas de predecesoras (solo entre filas visibles)
    hueco = 0.18 if detalle else 0.35
    for t in filas:
        for p in t.get("pred", []):
            if p not in pos or t["id"] not in pos:
                continue
            _, b0, y0 = pos[p]
            a1_, _, y1 = pos[t["id"]]
            xm = b0 + hueco
            arriba = y1 > y0
            top = y1 - (0.34 if t["tipo"] == "hito" else alto / 2) * (1 if arriba else -1)
            if a1_ - xm > 0.3:
                ag.plot([b0, xm, xm], [y0, y0, y1], color="#2F5597", lw=0.6, zorder=2)
                ag.annotate("", xy=(a1_, y1), xytext=(xm, y1),
                            arrowprops=dict(arrowstyle="-|>", color="#2F5597", lw=0.6, mutation_scale=5), zorder=5)
            else:
                ag.plot([b0, xm], [y0, y0], color="#2F5597", lw=0.6, zorder=2)
                ag.annotate("", xy=(xm, top), xytext=(xm, y0),
                            arrowprops=dict(arrowstyle="-|>", color="#2F5597", lw=0.6, mutation_scale=5), zorder=5)
    fig.savefig(path, dpi=230, facecolor="white")
    plt.close(fig)


def build_pngs(T):
    for viejo in glob.glob(os.path.join(HERE, "Gantt_Lanzamiento_NewBit*.png")):
        os.remove(viejo)
    resumen, detalle = paginas(T)
    salida = [("Vista resumen (como el modelo del docente): fases de cada sprint", os.path.join(HERE, PNG))]
    dibujar_gantt(resumen, salida[0][1], T)
    for k, filas in enumerate(detalle, 1):
        ruta = os.path.join(HERE, "Gantt_Lanzamiento_NewBit_%d.png" % k)
        dibujar_gantt(filas, ruta, T, detalle=True)
        salida.append(("Detalle de tareas: %s" % titulo_pagina(filas), ruta))
    return salida


# ---------------------------------------------------------------- 3. Word (formato FGAP080)
def ancho_imagen(png, max_w=26.6, max_h=15.6):
    from PIL import Image
    w, h = Image.open(png).size
    return min(max_w, max_h * w / h)


def build_docx(path, imagenes, T):
    from docx_nb import Doc
    d = Doc(landscape=True, margins_cm=(1.4, 1.3, 1.2, 1.3), font="Verdana", size=16,
            header=[("FGAP080 - Cronograma de Planificación de Lanzamiento", {"size": 16, "align": "right", "after": 0})],
            footer=[("FGAP080 • %s • Ingeniería de Software II • UNS • Página {PAGE}" % AUTOR, {"size": 13, "align": "right"})],
            title="FGAP080 Cronograma de Planificación de Lanzamiento – NewBit",
            subject="Cronograma de lanzamiento con las tareas de los 4 sprints")
    rows = [[{"text": "**CONTROL DE VERSIONES**", "span": 6, "fill": "D9D9D9", "align": "center", "size": 18}],
            [{"text": "**//%s//**" % h, "fill": "F2F2F2", "align": "center", "size": 16}
             for h in ["Versión", "Hecho por", "Revisado por", "Aprobado por", "Fecha", "Motivo"]],
            [{"text": v, "align": "center", "size": 15} for v in VERSION]]
    d.table(rows, widths_rel=[0.8, 2.3, 2.3, 2.1, 1.1, 3.1], border="595959", sz=4, cell_margin=50)
    d.p("//CRONOGRAMA DE PLANIFICACIÓN DE LANZAMIENTO//", size=30, align="center", before=60, after=50, font="Arial")
    rows = [[{"text": "**CÓDIGO Y NOMBRE DEL PROYECTO**", "fill": "D9D9D9", "align": "center", "size": 16, "smallcaps": True}],
            [{"text": P.PROYECTO, "align": "center", "size": 15}]]
    d.table(rows, widths_rel=[1], border="595959", sz=4, cell_margin=60)
    ROJO, ROSA, ROJO_OSC, GRIS_C = "B5323F", "F3D3D7", "8B1E2D", "F7F7F7"

    def titulo_seccion(txt, antes=80):
        d.p("**%s**" % txt, size=19, color=ROJO_OSC, before=antes, after=40)

    # --- parámetros acordados de la liberación
    titulo_seccion("PARÁMETROS ACORDADOS DE LA LIBERACIÓN")
    d.table([[{"text": "**%s**" % k, "fill": "1F2A44", "color": "FFFFFF", "align": "center", "size": 15} for k, _ in P.PARAMETROS],
             [{"text": v, "align": "center", "size": 15, "fill": GRIS_C} for _, v in P.PARAMETROS]],
            widths_rel=[1, 1, 1, 1.5], border="BFC5CE", sz=4, cell_margin=50)
    # --- cronograma detallado de actividades (nivel 1, fases de cada sprint e historias de usuario)
    titulo_seccion("CRONOGRAMA DETALLADO DE ACTIVIDADES")
    cab = [{"text": "**%s**" % h, "fill": "1F2A44", "color": "FFFFFF", "align": a, "size": 14}
           for h, a in (("NOMBRE DE LA TAREA", "left"), ("DURACIÓN", "center"), ("COMIENZO", "center"), ("FIN", "center"),
                        ("RESULTADO / HITO VERIFICABLE", "left"))]
    filas = [cab]
    for t in T:
        if t["nivel"] == 4 or (t["nivel"] == 2 and t["tipo"] == "resumen" and False):
            continue
        n1 = t["nivel"] == 1
        hito = t["tipo"] == "hito"
        fill = ROSA if (n1 and t["nombre"].startswith("Sprint")) else ("FBE9EB" if hito else (None if not n1 else "EEF0F3"))
        color = ROJO_OSC if hito else None
        b = n1 or hito
        sangria = "   " * (t["nivel"] - 1)
        nombre = ("★ " if hito else "") + t["nombre"]
        fila = [{"text": sangria + (("**%s**" % nombre) if b else nombre), "fill": fill, "color": color, "size": 13},
                {"text": ("**%s**" if b else "%s") % ("Hito" if hito else P.f_dur(t).replace("días", "días háb.") if t["dur"] > 1 else P.f_dur(t)),
                 "fill": fill, "color": color, "align": "center", "size": 13},
                {"text": ("**%s**" if b else "%s") % t["ini"].strftime("%d/%m/%Y"), "fill": fill, "color": color, "align": "center", "size": 13},
                {"text": ("**%s**" if b else "%s") % t["fin"].strftime("%d/%m/%Y"), "fill": fill, "color": color, "align": "center", "size": 13},
                {"text": ("**%s**" if b else "%s") % P.resultado(t), "fill": fill, "color": color, "size": 13}]
        filas.append(fila)
    d.table(filas, widths_rel=[8.2, 1.9, 2.0, 2.0, 8.6], border="D5D9E0", sz=4, cell_margin=45, header_rows=1, keep_rows=True)
    # --- vista tipo Gantt por semanas (editable en Word)
    d.page_break()
    titulo_seccion("VISTA TIPO GANTT (RESUMEN EDITABLE POR SEMANAS)", antes=0)
    d.p("Celdas coloreadas = semana de trabajo. ★ = hito de lanzamiento o entrega. Las fechas exactas están en el cronograma detallado "
        "y en la vista de MS Project de las páginas siguientes.", size=13, after=40)
    ini, fin, _ = proyecto(T)
    lunes = ini - dt.timedelta(days=ini.weekday())
    semanas = []
    while lunes <= fin:
        semanas.append(lunes)
        lunes += dt.timedelta(days=7)
    MES = ["", "ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]

    def etiqueta(l):
        v = l + dt.timedelta(days=4)
        return ("%02d–%02d %s" % (l.day, v.day, MES[v.month])) if l.month == v.month else ("%02d %s–%02d %s" % (l.day, MES[l.month], v.day, MES[v.month]))
    filas = [[{"text": "**FASE / HITO**", "fill": "1F2A44", "color": "FFFFFF", "align": "center", "size": 12}] +
             [{"text": "**%s**" % etiqueta(l), "fill": "1F2A44", "color": "FFFFFF", "align": "center", "size": 11} for l in semanas]]
    for t in T:
        es_hu = t["nivel"] == 3
        es_sprint = t["nivel"] == 1 and t["nombre"].startswith("Sprint")
        es_hito = t["tipo"] == "hito"
        if not (t["nivel"] == 1 or es_hu or es_hito):
            continue
        nombre = t["nombre"].rsplit(" · ", 1)[0] if t["nombre"].endswith(" PH") else t["nombre"]
        if es_hu:
            nombre = "\u00a0\u00a0\u00a0" + nombre
        if es_sprint:
            nombre = nombre.split(" (")[0]
        fila = [{"text": ("**%s**" % nombre) if not es_hu else nombre, "size": 12, "fill": "EEF0F3" if t["nivel"] == 1 and not es_hito else None}]
        for k, l in enumerate(semanas):
            v = l + dt.timedelta(days=6)
            dentro = t["ini"] <= v and t["fin"] >= l
            if es_hito:
                fila.append({"text": "**★**" if dentro else "", "fill": ROJO_OSC if dentro else (GRIS_C if k % 2 else None),
                             "color": "FFFFFF", "align": "center", "size": 13})
            else:
                fila.append({"text": "", "size": 8, "fill": (ROJO if not es_hu else "E8A3AC") if dentro else (GRIS_C if k % 2 else None)})
        filas.append(fila)
    d.table(filas, widths_rel=[7.0] + [1.75] * len(semanas), border="D5D9E0", sz=4, cell_margin=8, header_rows=1, keep_rows=True)
    # --- condiciones de uso y vista de MS Project (misma página)
    d.page_break()
    titulo_seccion("CONDICIONES DE USO DEL CRONOGRAMA", antes=0)
    for c in P.CONDICIONES:
        d.bullet(c, size=13, after=20)
    titulo_seccion("CRONOGRAMA EN MS PROJECT", antes=70)
    titulo0, png0 = imagenes[0]
    d.p("**%s.** Archivo de MS Project: `%s.xml` (tareas, vínculos y recursos)." % (titulo0, BASE), size=13, after=30)
    d.image(png0, ancho_imagen(png0, max_h=11.8), after=20)
    for titulo, png in imagenes[1:]:
        d.page_break()
        d.p("**%s**" % titulo, size=15, after=40)
        d.image(png, ancho_imagen(png), after=20)
    d.save(path)


# ---------------------------------------------------------------- .md
def build_md(T, path, imagenes):
    ini, fin, dur = proyecto(T)
    L = ["# FGAP080 – Cronograma de Planificación de Lanzamiento: NewBit", ""]
    L.append("- **Archivos para entregar** (esta carpeta): `%s.pdf` y `%s.docx` (editable), más `%s.xml`, el proyecto de **MS Project** "
             "con tareas, vínculos y recursos. Para el `.mpp`, abrir el XML en MS Project (Archivo › Abrir › tipo «XML») y guardarlo como `.mpp`." % (BASE, BASE, BASE))
    L.append("- **Estructura:** la del [formato FGAP080 del docente](../../material-del-profe/lanzamiento-fgap080-formato/lanzamiento-fgap080-formato.md): "
             "control de versiones, código y nombre del proyecto y el cronograma de MS Project. Además trae las secciones del ejemplo desarrollado del docente. PDF de 8 páginas: "
             "(1–2) control de versiones, código, **parámetros de la liberación** y **cronograma detallado de actividades** con resultado verificable; "
             "(3) **vista tipo Gantt por semanas** (sprints, historias y hitos ★); (4) **condiciones de uso** y vista resumen de MS Project como el modelo; "
             "(5–8) **detalle de las tareas de cada sprint** en MS Project, con responsable y predecesoras.")
    L.append("- **Generador:** `generar_fgap080.py` lee `plan_lanzamiento.py` (fuente única; `verificar()` comprueba las fechas del Acta y del FGAP130, "
             "que cada predecesora termine antes, que nadie tenga dos tareas el mismo día y que todo quepa en su sprint) y produce el XML (MSPDI), "
             "los Gantt en PNG (matplotlib, al estilo de MS Project) y el Word con `docx_nb.py` del FGAP110. PDF exportado con Pages.")
    L.append("- **Fecha:** %s · **Versión:** 1.0 · **Actividad individual** de %s (Grupo D3, proyecto NewBit)." % (FECHA_DOC, AUTOR))
    if DESDE_XML:
        L.append("- **Fuente de esta versión:** `%s`, editado con [Mini Project](../../../../herramientas/mini-project/README.md) y regenerado el %s. "
                 "Las «decisiones tomadas» de abajo son las de la v1.0: si cambiaste el cronograma, revísalas." % (DESDE_XML, dt.date.today().strftime("%d/%m/%Y")))
    L.append("- **Calendario:** el del [Acta FGAP010 v2.0](../../../semana-02-scrum-y-acta/nuestras-entregas/FGAP010_Acta_Constitucion_NewBit/FGAP010_Acta_Constitucion_NewBit.md). "
             "El Sprint 2 usa las tareas y fechas del [FGAP130](../../../semana-08-riesgo-y-planificacion-del-sprint/nuestras-entregas/FGAP130_Cronograma_Sprint_02_NewBit/FGAP130_Cronograma_Sprint_02_NewBit.md) "
             "(02–13/11) sin las de la SC-001; los puntos por historia son los del [backlog](../../../semana-05-rsu-y-backlog/nuestras-entregas/Priorizacion_MoSCoW_100_Puntos_NewBit/Priorizacion_MoSCoW_100_Puntos_NewBit.md).")
    L.append("")
    for titulo, png in imagenes:
        L.append("**%s**" % titulo)
        L.append("")
        L.append("![%s](%s)" % (titulo, os.path.basename(png)))
        L.append("")
    L.append("## Control de versiones")
    L.append("| Versión | Hecho por | Revisado por | Aprobado por | Fecha | Motivo |")
    L.append("|---|---|---|---|---|---|")
    L.append("| " + " | ".join(VERSION) + " |")
    L.append("")
    L.append("## Cronograma de planificación de lanzamiento")
    L.append("**Código y nombre del proyecto:** %s" % P.PROYECTO)
    L.append("")
    L.append("### Parámetros acordados de la liberación")
    L.append("| " + " | ".join(k for k, _ in P.PARAMETROS) + " |")
    L.append("|" + "---|" * len(P.PARAMETROS))
    L.append("| " + " | ".join(v for _, v in P.PARAMETROS) + " |")
    L.append("")
    L.append("### Cronograma detallado (todas las filas del XML de MS Project)")
    L.append("En el Word y el PDF, el «Cronograma detallado de actividades» muestra hasta el nivel de historia de usuario con su resultado verificable; "
             "la «Vista tipo Gantt» marca por semanas cada sprint, cada historia y los hitos (★); las tareas técnicas se ven en las páginas de MS Project.")
    L.append("")
    L.append("| Id | Nombre de tarea | Duración | Comienzo | Fin | Predecesoras | Recursos | Resultado / hito verificable |")
    L.append("|---|---|---|---|---|---|---|---|")
    L.append("| 0 | **NewBit (PY-NB-001)** | **%d días** | **%s** | **%s** | | | |" % (dur, P.f_ms(ini), P.f_ms(fin)))
    for t in T:
        nom = t["nombre"]
        if t["tipo"] == "resumen":
            nom = "**%s**" % nom
        elif t["tipo"] == "hito":
            nom = "◆ " + nom
        nom = "&nbsp;&nbsp;&nbsp;" * (t["nivel"] - 1) + nom
        dur_s = ("**%s**" % P.f_dur(t)) if t["tipo"] == "resumen" else P.f_dur(t)
        L.append("| %d | %s | %s | %s | %s | %s | %s | %s |" % (t["id"], nom, dur_s, P.f_ms(t["ini"]), P.f_ms(t["fin"]),
                                                          ", ".join(map(str, t["pred"])) or "—", (t.get("resp") or "").replace("; ", " y "),
                                                          P.resultado(t) if t["nivel"] < 4 else ""))
    L.append("")
    L.append("Predecesoras fin → comienzo. Duración en días hábiles (lunes a viernes). PH = puntos de historia (5 h por PH, como en el burndown).")
    L.append("")
    L.append("## Decisiones tomadas (propuesta del equipo)")
    L.append("- **Sprints de 10 días hábiles** (2 semanas, como fija el Acta): día 1 Planificación y Estimación, días 2–9 Implementación y día 10 "
             "Revisión y Retrospectiva (el modelo del docente usa 3 + 20 + 2 días porque su ejemplo es de sprints de 25 días).")
    L.append("- **Tareas por historia de usuario:** cada sprint baja a tareas técnicas de 1 o 2 días con responsable, como en la EDT del Sprint 2 (FGAP110). "
             "Luis lleva datos y modelos (OpenCV, YOLOv8, tensores, ConvLSTM, métricas, API) y Anthony la web, la integración y las pruebas, "
             "según los roles del FGAP030. Cada historia cierra con pruebas y revisión de pares (DoD, FGAP070).")
    L.append("- **Sprint 1:** las tareas del Scrumboard del Sprint 1 (tablero Kanban, semana 5). **Sprint 2:** T01–T05 y T11–T14 del FGAP110/FGAP130 con sus fechas "
             "(T05 y T14 empiezan el día de la planificación, como en el FGAP130); las tareas T06–T10 dependen de la SC-001 (adelantar HU07), que el backlog deja "
             "en el Sprint 3, así que no entran. **Sprint 3:** cierre del arrastre de HU05 (como en el burndown), HU07 y HU08. **Sprint 4:** HU09, HU10 y HU12.")
    L.append("- **Lanzamiento 1 como hito (0 días) el 13/11**, en la revisión del Sprint 2: versión alfa del pipeline espacial (carga, frames, YOLO, filtrado y clips). "
             "El Acta pone los sprints seguidos, así que no hay hueco para un lanzamiento de 10 días como en el modelo.")
    L.append("- **Lanzamiento 2 (14–16/12) y Cierre (17–18/12)** reparten la semana de «Cierre y sustentación» del Acta, con sus tareas y el hito de entrega final.")
    if FERIADOS:
        L.append("- **Feriados descontados** (no laborables en el calendario del XML): " + ", ".join(f.strftime("%d/%m/%Y") for f in FERIADOS) + ".")
    else:
        L.append("- **Feriados no descontados:** " + "; ".join("%s, %s" % (f.strftime("%d/%m"), n) for f, n in P.FERIADOS_NO_DESCONTADOS) +
                 ". Mismo criterio que el Acta y el burndown. Si el equipo no trabaja esos días, se marcan como feriados (en MS Project o en Mini Project) y las fechas se recalculan solas.")
    L.append("")
    L.append("## Condiciones de uso del cronograma")
    for c in P.CONDICIONES:
        L.append("- " + c)
    L.append("")
    L.append("## Cómo pasarlo a MS Project")
    L.append("1. Con **MS Project (Windows)**: Archivo › Abrir › tipo «Formato XML» › `%s.xml` › «Como nuevo proyecto». Luego Guardar como `.mpp`." % BASE)
    L.append("2. En **Mac**: abrir el mismo XML con ProjectLibre (gratuito) o con Mini Project.")
    L.append("3. **Para editarlo sin MS Project:** `python3 herramientas/mini-project/servidor.py` abre [Mini Project](../../../../herramientas/mini-project/README.md); "
             "se abre este XML, se edita como en Project y el botón «Word/PDF» corre `generar_fgap080.py --xml … --pdf`, que rehace el Word, los PNG, el `.md` y el PDF.")
    L.append("")
    L.append("## Estado")
    L.append("Completo en Word y PDF, sin campos «POR CONFIRMAR». Lo único que no se puede hacer en Mac es el archivo `.mpp`: si el docente lo pide, "
             "se abre el XML en una PC con MS Project y se guarda como `.mpp` (el contenido ya está listo). Las tareas y fechas de los Sprints 3 y 4 "
             "son la planificación propuesta, no avance real.")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")


def exportar_pdf(docx, pdf):
    """Exporta el Word a PDF con Pages (macOS). Microsoft Word no sirve por los permisos de su sandbox."""
    guion = ('tell application "Pages Creator Studio"\n set d to open (POSIX file "%s")\n delay 3\n'
             ' export d to (POSIX file "%s") as PDF\n close d saving no\nend tell' % (docx, pdf))
    r = subprocess.run(["osascript", "-e", guion], capture_output=True, text=True, timeout=180)
    if r.returncode != 0:
        print("AVISO: no se pudo exportar el PDF con Pages:", r.stderr.strip())
        return False
    return True


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Genera el FGAP080 de NewBit")
    ap.add_argument("--xml", help="generar desde un XML de MS Project (p. ej. editado en Mini Project) en vez de plan_lanzamiento.py")
    ap.add_argument("--pdf", action="store_true", help="exportar también el PDF con Pages")
    a = ap.parse_args()
    if a.xml:
        T, FERIADOS = leer_xml(a.xml)
        DESDE_XML = os.path.basename(a.xml)
    else:
        T = P.verificar()
        build_xml(T, os.path.join(HERE, BASE + ".xml"))
    imagenes = build_pngs(T)
    build_docx(os.path.join(HERE, BASE + ".docx"), imagenes, T)
    build_md(T, os.path.join(HERE, BASE + ".md"), imagenes)
    print("Generados: %s.docx, %s.md y %d imágenes de Gantt%s" % (BASE, BASE, len(imagenes), "" if a.xml else " (y el XML desde plan_lanzamiento.py)"))
    if a.pdf:
        if exportar_pdf(os.path.join(HERE, BASE + ".docx"), os.path.join(HERE, BASE + ".pdf")):
            print("PDF exportado: %s.pdf" % BASE)
