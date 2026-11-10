# -*- coding: utf-8 -*-
"""Genera FGAP110_EDT_Sprint_02_NewBit.docx y su .md sobre una COPIA del formato del docente.

Uso: python3 generar_fgap110.py <formato_convertido.docx> <carpeta_salida>
  <formato_convertido.docx>: copia de `edt-del-sprint-fgap110-formato.doc` convertida a .docx
  (Pages > Exportar > Word). El .doc original del docente no se modifica.
Requiere plan_sprint02.py, dibujar_edt.py y docx_nb.py en la misma carpeta.
"""
import os
import re
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import plan_sprint02 as P  # noqa: E402
import dibujar_edt  # noqa: E402
from docx_nb import Doc, run_xml, md_from_markup  # noqa: E402

BASE = "FGAP110_EDT_Sprint_02_NewBit"
FILL = {"HU": "DCE3F0", "SC": "FCE9D2", "R": "F6DADF"}
ETQ = {"HU": "Historia de usuario", "SC": "Solicitud de cambio", "R": "Riesgo"}

VERSION = ["1.0", "Developers (Anthony Lopez y Luis Salazar)", "Anthony Lopez (Scrum Master)",
           "Albert Chumacero (Product Owner) · {PC}", "02/11/2026", "Creación de la EDT del Sprint 02"]

CAPACIDAD = [
    "**Equipo:** 3 personas y **2 Developers**. Albert Chumacero es Product Owner y no desarrolla; Anthony Lopez es Scrum Master y Developer; Luis Salazar es Developer.",
    "**Capacidad de referencia (estimación):** Luis ≈ 4 h/día y Anthony ≈ 3,5 h/día, menos ≈ 0,5 h/día de labores de Scrum Master; descontadas las ceremonias "
    "(planificación 2 h, Daily 15 min, revisión 1,5 h y retrospectiva 1 h ≈ 7 h por persona) quedan ≈ 33 h (Luis) + ≈ 23 h (Anthony) = **≈ 56 h** para tareas.",
    "**Carga planificada:** **43 h** (≈ 77 %): Luis 26 h y Anthony 17 h. **Nunca hay más de 2 tareas en paralelo por día** (una por Developer); la revisión de pares (T12) la hace Luis el 10/11 y Anthony el 11/11. Ver el cronograma FGAP130.",
]

NOTAS = [
    "**SC-001 es condicional.** El nodo SC-001 (T06–T09) y las respuestas a R-01 (T10) y R-03 (T14) existen porque se propone adelantar HU07 (FGAP090). "
    "Si el Product Owner rechaza la solicitud, salen del sprint y quedan 22 h (T01–T05 y T11–T13). Decisión del PO: {PC}.",
    "**HU01–HU03 (Sprint 1):** construidas el 17/10 y sin aceptar; no hay acta de la revisión del Sprint 1 (30/10). No tienen tareas nuevas: su verificación con videos "
    "del dataset (T11) y su revisión de pares (T12) cuelgan del riesgo R-02. Si el PO las presenta en la revisión del Sprint 2: {PC}.",
    "**HU04, HU06 y HU11** ya están construidas (17/10/2026); sus tareas son de evidencia y ajuste para que el PO pueda aceptarlas con sus criterios y con la Definición de Terminado (FGAP070).",
    "**Numeración:** HU según el Product Backlog (FGAP040 y priorización MoSCoW). La tabla de la sección 2 del README del proyecto usa otra numeración; falta alinearla.",
    "**Supuestos:** el dataset completo de Önal y Dandıl (2024) está descargado en el equipo de trabajo ({PC}) y hay acceso a GPU en Google Colab ({PC}).",
    "Las horas son **estimaciones** del equipo hechas en la planificación; no son horas consumidas.",
]


def fill_empty_cells(row_xml, values):
    """Inserta un run en el párrafo vacío de cada celda de la fila."""
    cells = re.findall(r"<w:tc>.*?</w:tc>", row_xml, flags=re.S)
    assert len(cells) == len(values), (len(cells), len(values))
    new = row_xml
    for c, v in zip(cells, values):
        runs = "".join(run_xml(t, p, "Verdana", 15) for t, p in __import__("docx_nb").runs_from_markup(v, {"size": 15}))
        assert "<w:p/>" in c
        c2 = c.replace("<w:p/>", '<w:p><w:pPr><w:spacing w:before="0" w:after="0"/><w:jc w:val="center"/></w:pPr>%s</w:p>' % runs, 1)
        new = new.replace(c, c2, 1)
    return new


def scale_table(tbl, factor):
    tbl = re.sub(r'(<w:gridCol w:w=")(\d+)(")', lambda m: "%s%d%s" % (m.group(1), round(int(m.group(2)) * factor), m.group(3)), tbl)
    tbl = re.sub(r'(<w:tcW w:type="dxa" w:w=")(\d+)(")', lambda m: "%s%d%s" % (m.group(1), round(int(m.group(2)) * factor), m.group(3)), tbl)
    tbl = re.sub(r'(<w:tblW w:w=")(\d+)(")', lambda m: "%s%d%s" % (m.group(1), round(int(m.group(2)) * factor), m.group(3)), tbl)
    return tbl


HISTORIA = {
    "HU04": "Como Administrador de la plataforma (Jorge), quiero que el sistema descarte automáticamente los fotogramas sin trabajadores detectados, para optimizar la carga computacional y eliminar tiempo muerto.",
    "HU05": "Como Supervisora de SST (Mariana), quiero agrupar los frames activos filtrados en clips de tamaño fijo, para estructurar la entrada al modelo de inferencia temporal.",
    "HU06": "Como Supervisora de SST (Mariana), quiero descartar clips que no cumplan con una ventana de tiempo mínima de acción, para evitar alertas falsas por movimientos fugaces.",
    "HU11": "Como Administrador de la plataforma (Jorge), quiero modificar el umbral de confianza (confidence) de YOLOv8 desde la interfaz de configuración sin alterar código, para calibrar la sensibilidad del filtrado espacial según la iluminación de la nave.",
    "SC-001": "Adelantar HU07 al Sprint 2 (FGAP090). HU07: como Supervisora de SST (Mariana), quiero procesar el clip segmentado mediante ConvLSTM, para extraer características de movimiento y dependencias temporales. Entra solo si el PO aprueba la solicitud ({PC}).",
    "R-01": "Riesgo del FGAP050 (P × I = 0,40, alto): el modelo ConvLSTM podría no aprender a distinguir las conductas con la configuración inicial. Respuesta: mitigar con un //spike// y un registro de experimentos.",
    "R-02": "Riesgo del FGAP050 (P × I = 0,20, moderado): defectos no detectados en el pipeline propio, probado solo con un clip sintético y sin revisión de pares. Respuesta: verificación con videos reales, revisión de pares y prueba E2E; cubre también el cierre de HU01–HU03.",
    "R-03": "Riesgo del FGAP050 (P × I = 0,20, moderado): falta de GPU propia o cortes de Google Colab. Respuesta: entorno de entrenamiento reanudable, con checkpoint por época.",
}
ETQ_MAY = {"HU": "HISTORIA DE USUARIO", "SC": "SOLICITUD DE CAMBIO", "R": "RIESGO"}
ROJO = "8B1E2D"

NOTA_FINAL = ("**Total del Sprint 02: 43 h** (historias de usuario 12 h · SC-001 16 h · riesgos 15 h). Dos Developers, Luis Salazar y Anthony Lopez, con un máximo de 2 tareas "
              "en paralelo por día (Albert Chumacero es PO y no desarrolla). {PC}: aprobación del PO y decisión sobre SC-001 (si la rechaza, salen T06–T10 y T14).")


def objetivo_xml():
    d = Doc(landscape=True, font="Verdana", size=15)
    d.p("**Objetivo del sprint:** " + P.OBJETIVO, size=15, before=0, after=0)
    return "".join(d.body)


def detalle_xml():
    """Página de detalle con la disposición del ejemplo del docente: por nodo, su enunciado y la tabla ID · tarea técnica · estimación."""
    d = Doc(landscape=True, margins_cm=(2.0, 2.0, 1.8, 2.0), font="Verdana", size=15)
    d.page_break()
    d.p("DETALLE DE LA EDT: HISTORIAS DE USUARIO, SOLICITUD DE CAMBIO Y RIESGOS → TAREAS TÉCNICAS", size=22, b=True, color="1F2A44", align="center", after=60)
    d.p("Los identificadores T01–T14 coinciden con los del diagrama. Las tareas se estiman en la planificación del sprint; las horas son estimaciones del equipo, no horas consumidas.",
        size=15, after=80)
    for n in P.NODOS:
        pts = "" if n["pts"] is None else (" · %d pt" % n["pts"] if n["pts"] == 1 else " · %d pts" % n["pts"])
        d.p("%s · %s%s · %d h" % (n["id"], ETQ_MAY[n["tipo"]], pts, P.horas_nodo(n["id"])), size=18, b=True, color=ROJO, before=80, after=20, keep_next=True)
        d.p("//%s//" % HISTORIA[n["id"]], size=14, after=40, keep_next=True)
        rows = [[{"text": "**ID**", "fill": "E1E4E8", "size": 13}, {"text": "**TAREA TÉCNICA (¿QUÉ IMPLEMENTAR?)**", "fill": "E1E4E8", "size": 13},
                 {"text": "**EST.**", "fill": "E1E4E8", "size": 13}]]
        for t in P.tareas_de(n["id"]):
            rows.append([{"text": t[0], "size": 14}, {"text": t[3], "size": 14}, {"text": "%d h" % t[5], "size": 14}])
        d.table(rows, widths_rel=[0.7, 10.5, 0.9], border="BFC5CE", sz=4, keep_rows=True)
    d.p(NOTA_FINAL, size=14, before=100, after=0)
    return "".join(d.body)


def build_docx(base_docx, out_docx, png):
    zin = zipfile.ZipFile(base_docx)
    files = {n: zin.read(n) for n in zin.namelist()}
    x = files["word/document.xml"].decode("utf-8")
    # 1) página horizontal (como los ejemplos del docente) y márgenes
    x = x.replace('<w:pgSz w:w="11900" w:h="16840" w:orient="portrait"/>', '<w:pgSz w:w="16840" w:h="11900" w:orient="landscape"/>')
    x = re.sub(r'<w:pgMar [^>]*/>', '<w:pgMar w:top="1134" w:right="1134" w:bottom="1020" w:left="1134" w:header="567" w:footer="567"/>', x)
    # 2) tablas al ancho útil y llenado de celdas
    tbls = re.findall(r"<w:tbl>.*?</w:tbl>", x, flags=re.S)
    assert len(tbls) == 2
    t1 = scale_table(tbls[0], 14400 / 8611.0)
    rows = re.findall(r"<w:tr>.*?</w:tr>", t1, flags=re.S)
    t1 = t1.replace(rows[2], fill_empty_cells(rows[2], VERSION))
    t2 = scale_table(tbls[1], 14400 / 8657.0)
    rows = re.findall(r"<w:tr>.*?</w:tr>", t2, flags=re.S)
    t2 = t2.replace(rows[1], fill_empty_cells(rows[1], [P.PROYECTO, "**%s** (%s)" % (P.SPRINT, P.SPRINT_FECHAS)]))
    x = x.replace(tbls[0], t1).replace(tbls[1], t2)
    # 3) árbol de la EDT en lugar de la imagen modelo
    from PIL import Image
    im = Image.open(png)
    cx = int(21.6 * 360000)
    cy = int(cx * im.size[1] / im.size[0])
    x = re.sub(r'<wp:extent cx="\d+" cy="\d+"/>', '<wp:extent cx="%d" cy="%d"/>' % (cx, cy), x, count=1)
    x = re.sub(r'<a:ext cx="\d+" cy="\d+"/>', '<a:ext cx="%d" cy="%d"/>' % (cx, cy), x, count=1)
    x = x.replace('descr="image.png"', 'descr="EDT del Sprint 02 de NewBit"')
    files["word/media/image1.png"] = open(png, "rb").read()
    # 4) dejar un solo párrafo vacío entre la tabla del proyecto y el árbol, para que todo quepa en la pág. 1
    i_tbl = x.find(t2) + len(t2)
    i_img = x.rfind("<w:p>", 0, x.find("<w:drawing"))
    entre = x[i_tbl:i_img]
    vacios = re.findall(r"<w:p>(?:(?!</w:p>).)*?</w:p>|<w:p/>", entre, flags=re.S)
    assert all("<w:t" not in v for v in vacios), "se esperaban solo párrafos vacíos"
    x = x[:i_tbl] + (vacios[0] if vacios else "") + x[i_img:]
    # 5) detalle después del árbol
    idx = x.find("</w:drawing>")
    idx = x.find("</w:p>", idx) + len("</w:p>")
    x = x[:idx] + objetivo_xml() + detalle_xml() + x[idx:]
    files["word/document.xml"] = x.encode("utf-8")
    # 6) pie de página con identificación y número
    d = Doc(font="Verdana", size=13)
    files["word/footer1.xml"] = d._hf_xml("ftr", [("NewBit (PY-NB-001) · Grupo D3 · EDT del Sprint 02 · Página {PAGE}",
                                                   {"size": 13, "color": "808080", "align": "center"})]).encode("utf-8")
    with zipfile.ZipFile(out_docx, "w", zipfile.ZIP_DEFLATED) as z:
        for n, data in files.items():
            z.writestr(n, data)


def build_md(path):
    L = []
    L.append("# FGAP110 – EDT del Sprint 02: NewBit")
    L.append("")
    L.append("- **Archivos para entregar** (esta carpeta): `%s.docx` (editable) y `%s.pdf`." % (BASE, BASE))
    L.append("- **Base:** una **copia** del formato del docente [`edt-del-sprint-fgap110-formato.doc`](../../material-del-profe/edt-del-sprint-fgap110-formato/edt-del-sprint-fgap110-formato.md) "
             "(convertida a .docx con Pages; el original no se tocó). Para regenerar: exportar con Pages una copia del `.doc` como Word y correr `python3 generar_fgap110.py <copia.docx> .`. Se conservan su encabezado, el control de versiones, el título y la tabla de proyecto; "
             "la imagen modelo se reemplazó por el árbol de NewBit y la hoja pasó a horizontal, como en los ejemplos del docente.")
    L.append("- **Generadores:** `generar_fgap110.py` (documento y este `.md`), `dibujar_edt.py` (árbol `EDT_Sprint_02_arbol.png`) y `plan_sprint02.py` "
             "(fuente única de nodos y tareas, compartida con el FGAP130; `python3 plan_sprint02.py` verifica IDs, predecesoras y máximo 2 tareas por día) y `docx_nb.py` "
             "(generador mínimo de .docx que usan también el FGAP050, el FGAP130 y el FGAP090). PDF exportado con Pages (Word no acepta «guardar como» por AppleScript en esta Mac).")
    L.append("- **Fecha:** 02/11/2026 (inicio del Sprint 2) · **Versión:** 1.0 (Grupo D3).")
    L.append("- **Coherencia:** las tareas T01–T14 son las mismas del [cronograma FGAP130](../FGAP130_Cronograma_Sprint_02_NewBit/FGAP130_Cronograma_Sprint_02_NewBit.md); "
             "el nodo SC-001 viene de la [solicitud de cambio FGAP090](../../../semana-07-gestion-del-cambio/nuestras-entregas/FGAP090_Solicitud_de_Cambio_NewBit/FGAP090_Solicitud_de_Cambio_NewBit.md) "
             "y los nodos R-01, R-02 y R-03, del [FGAP050](../FGAP050_Riesgo_del_Proyecto_NewBit/FGAP050_Riesgo_del_Proyecto_NewBit.md).")
    L.append("")
    L.append("## Control de versiones")
    L.append("| Versión | Hecha por | Revisada por | Aprobada por | Fecha | Motivo |")
    L.append("|---|---|---|---|---|---|")
    L.append("| " + " | ".join(md_from_markup(v) for v in VERSION) + " |")
    L.append("")
    L.append("## Estructura de descomposición del trabajo (EDT) del sprint")
    L.append("| Código y nombre del proyecto | Sprint número |")
    L.append("|---|---|")
    L.append("| %s | %s (%s) |" % (P.PROYECTO, P.SPRINT, P.SPRINT_FECHAS))
    L.append("")
    L.append("**Objetivo del Sprint 02:** " + P.OBJETIVO)
    L.append("")
    L.append("### Árbol (nivel 1 → 2 → 3)")
    L.append("```text")
    L.append("PY-NB-001 · NewBit · Sprint Nro. 02 (02–13/11/2026) · 43 h")
    for i, n in enumerate(P.NODOS):
        ult = i == len(P.NODOS) - 1
        pts = "" if n["pts"] is None else (" · %d pt" % n["pts"] if n["pts"] == 1 else " · %d pts" % n["pts"])
        L.append("%s %s %s · %s%s · %d h" % ("└──" if ult else "├──", ETQ[n["tipo"]], n["id"], n["titulo"], pts, P.horas_nodo(n["id"])))
        ts = P.tareas_de(n["id"])
        for j, t in enumerate(ts):
            L.append("%s   %s %s %s (%d h)" % (" " if ult else "│", "└──" if j == len(ts) - 1 else "├──", t[0], t[2], t[5]))
    L.append("```")
    L.append("")
    L.append("### Enunciado de cada nodo (como en la página de detalle del Word)")
    L.append("| Nodo | Enunciado |")
    L.append("|---|---|")
    for n in P.NODOS:
        L.append("| %s · %s | %s |" % (n["id"], ETQ[n["tipo"]], md_from_markup(HISTORIA[n["id"]])))
    L.append("")
    L.append("**Nota del documento:** " + md_from_markup(NOTA_FINAL))
    L.append("")
    L.append("### Detalle de tareas técnicas")
    L.append("| Nodo | ID | Tarea técnica (entregable verificable) | Responsable (propuesto) | Fechas | Predecesoras | Horas |")
    L.append("|---|---|---|---|---|---|:---:|")
    for n in P.NODOS:
        for t in P.tareas_de(n["id"]):
            ini, fin = t[6], t[6] + t[7] - 1
            fechas = P.fecha(ini) if ini == fin else "%s–%s" % (P.fecha(ini), P.fecha(fin))
            L.append("| %s | **%s** | %s | %s | %s | %s | %d |" % (n["id"], t[0], t[3], t[4], fechas, ", ".join(t[8]) or "—", t[5]))
    L.append("")
    L.append("### Horas por nodo (para cuadrar con el burndown)")
    L.append("| Nodo | Tipo | Pts | Tareas | Horas |")
    L.append("|---|---|:---:|---|:---:|")
    for n in P.NODOS:
        L.append("| %s · %s | %s | %s | %s | %d |" % (n["id"], n["titulo"], ETQ[n["tipo"]], n["pts"] if n["pts"] else "—",
                                                  ", ".join(t[0] for t in P.tareas_de(n["id"])), P.horas_nodo(n["id"])))
    L.append("| **Total** | | **13** | T01–T14 | **%d** |" % sum(t[5] for t in P.TAREAS))
    L.append("")
    L.append("Historias del backlog del Sprint 2 (HU04, HU05, HU06, HU11): 12 h · SC-001 (HU07): 16 h · riesgos (R-01, R-02, R-03): 15 h. "
             "Por persona: Luis 26 h (incluye 2 h de T12) y Anthony 17 h (incluye 2 h de T12).")
    L.append("")
    L.append("## Notas de trabajo (no van en el formato)")
    L.append("")
    L.append("### Capacidad del equipo y paralelismo")
    for t in CAPACIDAD:
        L.append("- " + md_from_markup(t))
    L.append("")
    L.append("### Notas")
    for t in NOTAS:
        L.append("- " + md_from_markup(t))
    L.append("")
    L.append("## POR CONFIRMAR")
    L.append("1. **Aprobación del Product Owner** de la EDT (control de versiones) y **decisión sobre SC-001**: si la rechaza, salen T06–T10 y T14 (quedan 22 h).")
    L.append("2. Si el PO presenta **HU01–HU03** para aceptación en la revisión del Sprint 2.")
    L.append("3. **Dataset completo descargado** en el equipo de trabajo y **acceso a GPU en Colab**.")
    L.append("4. La capacidad (≈ 56 h) es una estimación de referencia; si el burndown usa otra, prevalece la que acuerde el equipo en la planificación.")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")


if __name__ == "__main__":
    base_docx = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else "."
    os.makedirs(out, exist_ok=True)
    png = os.path.join(out, "EDT_Sprint_02_arbol.png")
    dibujar_edt.main(png)
    P.verificar()
    build_docx(base_docx, os.path.join(out, BASE + ".docx"), png)
    build_md(os.path.join(out, BASE + ".md"))
    print("ok", out)
