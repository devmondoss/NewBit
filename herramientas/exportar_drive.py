# -*- coding: utf-8 -*-
"""Arma la carpeta para subir al Drive del curso: una carpeta por semana, nombres claros y numerados,
PDF a la vista y editables (Word, PowerPoint, Excel, XML de MS Project) en una subcarpeta, más un índice
«00 - LEEME» en PDF para que el equipo encuentre todo rápido.

Uso:  .venv/bin/python -I herramientas/exportar_drive.py [carpeta_destino]
      (por defecto: ~/Desktop/NewBit - Entregas (Drive), y también deja un .zip al lado)
Se vuelve a correr cada vez que cambia una entrega: la carpeta de destino se reemplaza entera.
Para agregar una entrega nueva, se añade una fila a ENTREGAS.
"""
import datetime as dt
import os
import shutil
import sys

sys.dont_write_bytecode = True
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
DESTINO = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser("~/Desktop/NewBit - Entregas (Drive)")

SEMANAS = {
    2: ("semana-02-scrum-y-acta", "Semana 02 - Scrum y Acta (21-27 sep)"),
    3: ("semana-03-roles-y-prototipos", "Semana 03 - Roles y Prototipos (28 sep-04 oct)"),
    4: ("semana-04-justificacion-y-epicas", "Semana 04 - Justificación y Épicas (05-11 oct)"),
    5: ("semana-05-rsu-y-backlog", "Semana 05 - RSU y Backlog (12-18 oct)"),
    6: ("semana-06-producto-unidad-1", "Semana 06 - Producto de la Unidad I (19-25 oct)"),
    7: ("semana-07-gestion-del-cambio", "Semana 07 - Gestión del cambio (26 oct-01 nov)"),
    8: ("semana-08-riesgo-y-planificacion-del-sprint", "Semana 08 - Riesgo y planificación del sprint (02-08 nov)"),
    9: ("semana-09-stakeholders-y-lanzamiento", "Semana 09 - Stakeholders y lanzamiento (09-15 nov)"),
}

# (semana, carpeta de la entrega, nombre para el Drive, archivos a la vista, editables, grupal/individual, de qué trata)
ENTREGAS = [
    (2, "FGAP010_Acta_Constitucion_NewBit", "FGAP010 - Acta de Constitución", ["FGAP010_Acta_Constitucion_NewBit.pdf"], ["FGAP010_Acta_Constitucion_NewBit.docx"], "Grupal", "Problema, objetivos, alcance, equipo, presupuesto e hitos del proyecto."),
    (2, "Cuadro_Principios_Scrum_NewBit", "Cuadro de principios de Scrum", ["Cuadro_Principios_Scrum_NewBit.pdf"], ["Cuadro_Principios_Scrum_NewBit.pptx"], "Grupal", "Los 6 principios de Scrum con ejemplos de NewBit."),
    (3, "FGAP030_Roles_y_Prototipos_NewBit", "FGAP030 - Roles y Prototipos", ["FGAP030_Roles_y_Prototipos_NewBit.pdf"], ["FGAP030_Roles_y_Prototipos_NewBit.docx"], "Grupal", "Roles del sistema y prototipos de las pantallas."),
    (3, "Diagrama_Arquitectura_NewBit", "Diagrama de arquitectura", ["Diagrama_Arquitectura_NewBit.pdf"], [], "Grupal", "Cómo funciona NewBit: del video a la alerta."),
    (3, "PPT_Presentacion_NewBit", "Presentación de NewBit", ["PPT_Presentacion_NewBit.pdf"], ["PPT_Presentacion_NewBit.pptx"], "Grupal", "Presentación del proyecto (12 diapositivas)."),
    (3, "Infografias_NewBit", "Infografía - 12 pasos del proyecto", ["01-pasos-proyecto.pdf"], [], "Grupal", "Los 12 pasos del proyecto en una infografía."),
    (4, "EGAP015_Justificacion_NewBit", "EGAP015 - Justificación", ["EGAP015_Justificacion_NewBit.pdf"], ["EGAP015_Justificacion_NewBit.docx"], "Grupal", "Por qué conviene el proyecto: valor, costos y viabilidad."),
    (4, "FGAP040_Epicas_NewBit", "FGAP040 - Épicas e historias de usuario", ["FGAP040_Epicas_NewBit.pdf"], ["FGAP040_Epicas_NewBit.docx"], "Grupal", "6 épicas y 12 historias de usuario."),
    (5, "FGAP060_Backlog_Priorizado_NewBit", "FGAP060 - Backlog Priorizado del Producto", ["FGAP060_Backlog_Priorizado_NewBit.pdf"], ["FGAP060_Backlog_Priorizado_NewBit.docx"], "Grupal", "Historias con prioridad, puntos y sprint; cambio SC-001 y riesgos."),
    (5, "FGAP070_Criterios_de_Terminado_NewBit", "FGAP070 - Criterios de Terminado", ["FGAP070_Criterios_de_Terminado_NewBit.pdf"], ["FGAP070_Criterios_de_Terminado_NewBit.docx"], "Grupal", "Definición de terminado (DoD) del equipo."),
    (5, "Priorizacion_MoSCoW_100_Puntos_NewBit", "Priorización MoSCoW y 100 puntos", ["Priorizacion_MoSCoW_100_Puntos_NewBit.pdf"], ["Priorizacion_MoSCoW_100_Puntos_NewBit.pptx"], "Grupal", "Votación del equipo para ordenar las 12 historias."),
    (5, "Presentacion_Fist_of_Five", "Estimación con Puño de cinco", ["Presentacion_Fist_of_Five.pdf"], ["Presentacion_Fist_of_Five.pptx"], "Grupal", "Estimación de las historias en puntos."),
    (5, "Tablero_Kanban_NewBit", "Tablero Kanban", ["Tablero_Kanban_NewBit.pdf"], ["Tablero_Kanban_NewBit.pptx"], "Grupal", "Backlog con criterios y Scrumboard del Sprint 1."),
    (5, "Proyecto_RSU_NewBit", "Proyecto RSU - Seguridad laboral asistida por IA", ["Proyecto_RSU_NewBit.pdf"], ["Proyecto_RSU_NewBit.docx"], "Grupal", "Propuesta de taller RSU (Anexo 1 del reglamento UNS), 05/12/2026."),
    (6, "Producto_Unidad_1_NewBit", "Producto de la Unidad I - Informe", ["Producto_Unidad_1_NewBit.pdf"], [], "Grupal", "Informe de la Unidad I (APA 7, 40 págs.)."),
    (6, "PPT_Producto_Unidad_1_NewBit", "Producto de la Unidad I - Presentación", ["PPT_Producto_Unidad_1_NewBit.pdf"], ["PPT_Producto_Unidad_1_NewBit.pptx"], "Grupal", "Presentación de la Unidad I (30 láminas)."),
    (6, "Tablero_Kanban_NewBit_Actualizado", "Tablero Kanban actualizado", ["Tablero_Kanban_NewBit_Actualizado.pdf"], ["Tablero_Kanban_NewBit_Actualizado.pptx"], "Grupal", "Estado del backlog y de los sprints al 20/10."),
    (7, "FGAP090_Solicitud_de_Cambio_NewBit", "FGAP090 - Solicitud de Cambio", ["FGAP090_Solicitud_de_Cambio_NewBit.pdf"], ["FGAP090_Solicitud_de_Cambio_NewBit.docx"], "Grupal", "SC-001: adelantar HU07 al Sprint 2 (no aprobada por el PO)."),
    (7, "EGAP050_Solicitud_de_Cambio_NewBit", "EGAP050 - Solicitud de Cambio", ["EGAP050_Solicitud_de_Cambio_NewBit.pdf"], ["EGAP050_Solicitud_de_Cambio_NewBit.docx"], "Grupal", "La misma SC-001 en el segundo formato del docente."),
    (8, "FGAP050_Riesgo_del_Proyecto_NewBit", "FGAP050 - Riesgo del Proyecto", ["FGAP050_Riesgo_del_Proyecto_NewBit.pdf"], ["FGAP050_Riesgo_del_Proyecto_NewBit.docx"], "Grupal", "9 riesgos con matriz P×I, respuesta, responsable y guion de 3 minutos."),
    (8, "FGAP110_EDT_Sprint_02_NewBit", "FGAP110 - EDT del Sprint 02", ["FGAP110_EDT_Sprint_02_NewBit.pdf"], ["FGAP110_EDT_Sprint_02_NewBit.docx"], "Grupal", "Historias del Sprint 2 desglosadas en tareas con horas."),
    (8, "FGAP130_Cronograma_Sprint_02_NewBit", "FGAP130 - Cronograma del Sprint 02", ["FGAP130_Cronograma_Sprint_02_NewBit.pdf"], ["FGAP130_Cronograma_Sprint_02_NewBit.docx"], "Grupal", "Gantt por día del Sprint 2 (02-13/11)."),
    (8, "Burndown_Sprint_NewBit", "Burndown de los sprints",
     ["Burndown_Sprint01_NewBit.xlsx", "Burndown_Sprint02_NewBit.xlsx", "Burndown_Sprint03_NewBit.xlsx", "Burndown_Sprint04_NewBit.xlsx"], [], "Grupal",
     "Burndown en Excel de los 4 sprints (datos simulados para clase)."),
    (9, "Entrega_Semana09_Lopez_Yrribarren", "ENTREGA INDIVIDUAL - Stakeholders y Cronograma de Lanzamiento", ["Entrega_Semana09_Lopez_Yrribarren.pdf"], [], "Individual (Anthony Lopez)", "PDF único con carátula: EGAP020 + FGAP080 (11 págs.)."),
    (9, "EGAP020_Registro_de_Stakeholders_NewBit", "EGAP020 - Registro de Stakeholders", ["EGAP020_Registro_de_Stakeholders_NewBit.pdf"], ["EGAP020_Registro_de_Stakeholders_NewBit.docx"], "Individual (Anthony Lopez)", "10 interesados con identificación y evaluación."),
    (9, "FGAP080_Cronograma_Lanzamiento_NewBit", "FGAP080 - Cronograma de Planificación de Lanzamiento", ["FGAP080_Cronograma_Lanzamiento_NewBit.pdf"],
     ["FGAP080_Cronograma_Lanzamiento_NewBit.docx", "FGAP080_Cronograma_Lanzamiento_NewBit.xml"], "Individual (Anthony Lopez)",
     "Los 4 sprints con 80 tareas, Gantt por semanas y archivo de MS Project (.xml)."),
]

LO_QUE_VIENE = [
    ("16-27 nov", "Sprint 3: HU05 (cierre), HU07 y HU08 - modelo ConvLSTM", "EDT y cronograma del Sprint 3 (FGAP110/FGAP130), burndown"),
    ("30 nov-11 dic", "Sprint 4: HU09, HU10 y HU12 - video con recuadro, alertas y log", "EDT y cronograma del Sprint 4, burndown"),
    ("05 dic", "Taller RSU «Seguridad laboral asistida por IA» (si se aprueba)", "Proyecto RSU de la semana 5"),
    ("14-16 dic", "Lanzamiento 2: versión final y sustentación", "Demo, manual de usuario"),
    ("17-18 dic", "Cierre del proyecto: lecciones aprendidas y acta de cierre", "Formato de cierre (código por confirmar)"),
]


def copiar():
    if os.path.exists(DESTINO):
        assert os.path.basename(DESTINO).startswith("NewBit - Entregas"), "Destino inesperado: %s" % DESTINO
        shutil.rmtree(DESTINO)
    os.makedirs(DESTINO)
    faltan, filas = [], []
    contador = {}
    for sem, carpeta, nombre, vista, editables, tipo, que in ENTREGAS:
        base_repo, nombre_sem = SEMANAS[sem]
        origen = os.path.join(REPO, "curso", base_repo, "nuestras-entregas", carpeta)
        dest_sem = os.path.join(DESTINO, nombre_sem)
        os.makedirs(dest_sem, exist_ok=True)
        contador[sem] = contador.get(sem, 0) + 1
        n = contador[sem]
        copiados = []
        for k, arch in enumerate(vista):
            src = os.path.join(origen, arch)
            if not os.path.exists(src):
                faltan.append(src)
                continue
            ext = os.path.splitext(arch)[1]
            sufijo = "" if len(vista) == 1 else " - Sprint %02d" % (k + 1)
            nuevo = "%02d - %s%s%s" % (n, nombre, sufijo, ext)
            shutil.copy2(src, os.path.join(dest_sem, nuevo))
            copiados.append(nuevo)
        for arch in editables:
            src = os.path.join(origen, arch)
            if not os.path.exists(src):
                faltan.append(src)
                continue
            os.makedirs(os.path.join(dest_sem, "editables"), exist_ok=True)
            ext = os.path.splitext(arch)[1]
            extra = " (MS Project)" if ext == ".xml" else ""
            shutil.copy2(src, os.path.join(dest_sem, "editables", "%02d - %s%s%s" % (n, nombre, extra, ext)))
        filas.append((sem, nombre_sem, "%02d - %s" % (n, nombre), tipo, que))
    return filas, faltan


def leeme(filas):
    hoy = dt.date.today().strftime("%d/%m/%Y")
    css = ("body{font-family:sans-serif;font-size:9.5pt;color:#1f1f1f} h1{font-size:17pt;color:#8B1E2D;margin:0} "
           "h2{font-size:12pt;color:#1F2A44;margin:10pt 0 4pt 0} p{margin:2pt 0} "
           "table{border-collapse:collapse;width:100%} th{background:#1F2A44;color:white;text-align:left;padding:3pt;font-size:9pt} "
           "td{border-bottom:0.5pt solid #ccc;padding:2.5pt 3pt;vertical-align:top;font-size:9pt} .s{background:#EEF0F3;font-weight:bold}")
    h = ["<html><head><style>%s</style></head><body>" % css,
         "<h1>NewBit · Entregas del curso Ingeniería de Software II</h1>",
         "<p><b>Universidad Nacional del Santa · 2026-II · Docente: Dr. Ing. Alfredo Daza Vergaray</b></p>",
         "<p>Grupo D3 (laboratorio D, equipo 3): Albert Chumacero Chávarry (Product Owner) · Anthony Lopez Yrribarren (Scrum Master y Developer) · "
         "Luis Salazar Diaz (Developer). Proyecto PY-NB-001: sistema web con visión artificial para detectar actos inseguros en talleres metalmecánicos.</p>",
         "<h2>Cómo está ordenado</h2>",
         "<p>Una carpeta por <b>semana en que el profe pidió la tarea</b>. Dentro, los PDF numerados en orden (lo que se revisa); "
         "en <b>editables/</b> están los Word, PowerPoint y el archivo de MS Project por si hay que corregir algo. "
         "Las entregas de la semana 9 son <b>individuales</b>; las demás, del grupo. Actualizado el %s.</p>" % hoy,
         "<h2>Índice de entregas</h2>",
         "<table><tr><th>Archivo</th><th>Tipo</th><th>De qué trata</th></tr>"]
    actual = None
    for sem, nombre_sem, archivo, tipo, que in filas:
        if nombre_sem != actual:
            h.append('<tr><td class="s" colspan="3">%s</td></tr>' % nombre_sem)
            actual = nombre_sem
        h.append("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (archivo, tipo, que))
    h.append("</table><h2>Lo que viene (quedan unas 6 semanas)</h2>"
             "<table><tr><th>Cuándo</th><th>Qué</th><th>Documentos esperados</th></tr>")
    for a, b, c in LO_QUE_VIENE:
        h.append("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (a, b, c))
    h.append("</table><p style='color:#666;margin-top:6pt'>Fuente: repositorio NewBit (github.com/devmondoss/NewBit). "
             "Esta carpeta se genera con herramientas/exportar_drive.py.</p></body></html>")
    import pymupdf
    ruta = os.path.join(DESTINO, "00 - LEEME - Índice de entregas.pdf")
    story = pymupdf.Story(html="".join(h))
    writer = pymupdf.DocumentWriter(ruta)
    mediabox = pymupdf.paper_rect("a4")
    area = mediabox + (36, 36, -36, -36)
    mas = True
    while mas:
        dev = writer.begin_page(mediabox)
        mas, _ = story.place(area)
        story.draw(dev)
        writer.end_page()
    writer.close()
    return ruta


if __name__ == "__main__":
    filas, faltan = copiar()
    ruta = leeme(filas)
    zipbase = DESTINO
    shutil.make_archive(zipbase, "zip", os.path.dirname(DESTINO), os.path.basename(DESTINO))
    n_pdf = sum(1 for r, _, fs in os.walk(DESTINO) for f in fs if not r.endswith("editables"))
    print("Listo: %s (%d archivos a la vista, más editables) y %s.zip" % (DESTINO, n_pdf, zipbase))
    if faltan:
        print("FALTAN %d archivos:" % len(faltan))
        for f in faltan:
            print("  -", os.path.relpath(f, REPO))
