# -*- coding: utf-8 -*-
"""Arma la entrega individual de la semana 9 en un solo PDF:
carátula + EGAP020 Registro de Stakeholders + FGAP080 Cronograma de Planificación de Lanzamiento.
Toma los PDF ya exportados de sus carpetas (si cambian, primero se regeneran allí y luego se corre esto).
Uso: python3 -I unir_entrega.py   (con el Python de .venv, que trae PyMuPDF)
"""
import os
import sys

sys.dont_write_bytecode = True
import pymupdf  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.basename(HERE)
ENTREGAS = os.path.dirname(HERE)
EGAP020 = os.path.join(ENTREGAS, "EGAP020_Registro_de_Stakeholders_NewBit", "EGAP020_Registro_de_Stakeholders_NewBit.pdf")
FGAP080 = os.path.join(ENTREGAS, "FGAP080_Cronograma_Lanzamiento_NewBit", "FGAP080_Cronograma_Lanzamiento_NewBit.pdf")
LOGO = os.path.abspath(os.path.join(ENTREGAS, "..", "..", "semana-06-producto-unidad-1", "nuestras-entregas",
                                    "Producto_Unidad_1_NewBit", "logo-uns.png"))
FUENTE = "/System/Library/Fonts/Supplemental/Arial.ttf"
FUENTE_N = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FUENTE_I = "/System/Library/Fonts/Supplemental/Arial Italic.ttf"

ALUMNO = "Lopez Yrribarren, Anthony Gabriel"
PROYECTO = ("PY-NB-001 – Sistema web con Visión Artificial para la detección de actos inseguros\n"
            "en áreas operativas de manufactura metalmecánica (NewBit)")


def caratula(doc, ancho, alto):
    pag = doc.new_page(width=ancho, height=alto)
    for nombre, ruta in (("ar", FUENTE), ("arb", FUENTE_N), ("ari", FUENTE_I)):
        pag.insert_font(fontname=nombre, fontfile=ruta)
    cx = ancho / 2
    y = 42
    if os.path.exists(LOGO):
        pag.insert_image(pymupdf.Rect(cx - 38, y, cx + 38, y + 76), filename=LOGO, keep_proportion=True)
        y += 88

    def linea(texto, tam, fuente="ar", color=(0, 0, 0), alto_linea=None):
        nonlocal y
        h = alto_linea or tam * 1.45 * (texto.count("\n") + 1)
        pag.insert_textbox(pymupdf.Rect(60, y, ancho - 60, y + h + 4), texto, fontname=fuente, fontsize=tam,
                           align=pymupdf.TEXT_ALIGN_CENTER, color=color)
        y += h

    rojo = (0.55, 0.12, 0.18)
    linea("UNIVERSIDAD NACIONAL DEL SANTA", 17, "arb", rojo)
    linea("Facultad de Ingeniería", 12, "arb")
    linea("Escuela Profesional de Ingeniería de Sistemas e Informática", 11.5)
    y += 14
    linea("Curso: Ingeniería de Software II", 12.5, "arb")
    linea("Actividad individual · Semana 9", 11.5)
    y += 12
    linea("EGAP020 – Registro de Stakeholders\nFGAP080 – Cronograma de Planificación de Lanzamiento", 15, "arb")
    y += 8
    linea(PROYECTO, 11, "ari")
    y += 18
    linea("Alumno", 11.5, "arb")
    linea(ALUMNO, 13)
    linea("Scrum Master y Developer · Grupo D3 (laboratorio D, equipo 3)", 10.5, color=(0.3, 0.3, 0.3))
    y += 12
    linea("Docente", 11.5, "arb")
    linea("Dr. Ing. Alfredo Daza Vergaray", 12)
    pag.insert_textbox(pymupdf.Rect(60, alto - 70, ancho - 60, alto - 30), "Nuevo Chimbote, Perú\nNoviembre de 2026",
                       fontname="ar", fontsize=11, align=pymupdf.TEXT_ALIGN_CENTER)
    pag.draw_line(pymupdf.Point(70, alto - 82), pymupdf.Point(ancho - 70, alto - 82), color=rojo, width=0.8)


def main():
    for ruta in (EGAP020, FGAP080):
        if not os.path.exists(ruta):
            raise SystemExit("Falta %s: genéralo primero en su carpeta." % ruta)
    a = pymupdf.open(EGAP020)
    b = pymupdf.open(FGAP080)
    r = a[0].rect
    out = pymupdf.open()
    caratula(out, r.width, r.height)
    out.insert_pdf(a)
    out.insert_pdf(b)
    out.set_toc([[1, "Carátula", 1],
                 [1, "EGAP020 – Registro de Stakeholders", 2],
                 [1, "FGAP080 – Cronograma de Planificación de Lanzamiento", 2 + len(a)]])
    out.set_metadata({"title": "Semana 9 – EGAP020 y FGAP080 – NewBit", "author": "Anthony Gabriel Lopez Yrribarren",
                      "subject": "Ingeniería de Software II – UNS – actividad individual", "creator": "unir_entrega.py"})
    destino = os.path.join(HERE, BASE + ".pdf")
    out.save(destino, garbage=3, deflate=True)
    print("OK:", destino, "·", len(out), "páginas (carátula + %d EGAP020 + %d FGAP080)" % (len(a), len(b)))


if __name__ == "__main__":
    main()
