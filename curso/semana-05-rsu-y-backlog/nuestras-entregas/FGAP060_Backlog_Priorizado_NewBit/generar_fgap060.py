# -*- coding: utf-8 -*-
"""Genera el FGAP060 (Backlog Priorizado del Producto) de NewBit:
  1. FGAP060_Backlog_Priorizado_NewBit.docx -> formato FGAP060 del docente (ejemplo Retinopatía v1.1), horizontal.
  2. FGAP060_Backlog_Priorizado_NewBit.md   -> resumen del repo con la tabla completa.
El PDF se exporta aparte con Pages (ver el .md).
Uso: python3 -I generar_fgap060.py   (escribe en esta carpeta)
Fuentes: FGAP040 v2.0 (épicas e HU), Priorización MoSCoW + 100 puntos v2.0 (prioridad, votos, orden,
dependencias y sprint), Tablero Kanban v2.0 y su versión actualizada al 20/10/2026 (puntos, criterios y estado),
FGAP090 (SC-001) y FGAP050 v1.1 (R-01 a R-04 y R-08, los de P × I ≥ 0,20).
"""
import os
import sys

sys.dont_write_bytecode = True  # no dejar __pycache__ en las carpetas de entregas
HERE = os.path.dirname(os.path.abspath(__file__))
FGAP110 = os.path.abspath(os.path.join(HERE, "..", "..", "..", "semana-08-riesgo-y-planificacion-del-sprint",
                                       "nuestras-entregas", "FGAP110_EDT_Sprint_02_NewBit"))
sys.path.insert(0, FGAP110)  # docx_nb.py (generador de Word del equipo)
from docx_nb import Doc, md_from_markup  # noqa: E402

BASE = "FGAP060_Backlog_Priorizado_NewBit"
PROYECTO = ("PY-NB-001 – Sistema web con Visión Artificial para la detección de actos inseguros "
            "en áreas operativas de manufactura metalmecánica (NewBit)")
HECHO = "Equipo Scrum (Grupo D3)"
REVISA = "Anthony Lopez – Scrum Master"
APRUEBA = "Albert Chumacero – Product Owner"
VERSIONES = [
    ["1.0", HECHO, REVISA, APRUEBA, "12/10/2026", "Versión original del backlog priorizado"],
    ["1.1", HECHO, REVISA, APRUEBA, "09/11/2026", "Backlog actualizado con SC-001 y riesgos del FGAP050"],
]

# MoSCoW -> escala del ejemplo del docente (Alta/Media/Baja)
NIVEL = {"Must": "Alta", "Should": "Media", "Could": "Baja"}
NOMBRE_MOSCOW = {"Must": "Must have", "Should": "Should have", "Could": "Could have"}

# Épicas en el orden del FGAP040. Cada HU: id, título, MoSCoW, orden final, votos (de 300), PH, sprint, observaciones.
EPICAS = [
    dict(id="EP01", nombre="Ingestión y preprocesamiento de video", prio="Alta (Must have)", rol="Administrador de la plataforma (Jorge Ponce, TI)",
         hus=[
             ("HU01", "Cargar video industrial (.mp4/.avi)", "Must", 1, 19, 1, 1,
              "Sin dependencias. Criterios: acepta .mp4 y .avi (otro formato da error validado) y muestra duración, resolución y FPS. "
              "Estado: construida; pendiente de aceptación del PO."),
             ("HU02", "Extraer frames normalizados", "Must", 2, 20, 2, 1,
              "Depende de HU01. Criterios: frames numerados en secuencia y normalizados al tamaño de entrada de YOLOv8. "
              "Estado: construida; pendiente de aceptación del PO."),
         ]),
    dict(id="EP02", nombre="Extracción espacial y detección de operarios (YOLOv8)", prio="Alta (Must have)", rol="Supervisora de SST (Mariana Torres)",
         hus=[
             ("HU03", "Detectar operarios con YOLOv8", "Must", 3, 37, 4, 1,
              "Depende de HU02. Criterios: cajas de la clase «persona» con su confianza y vista previa del frame. "
              "Estado: construida; pendiente de aceptación del PO y de la prueba con videos reales del dataset (R-02)."),
         ]),
    dict(id="EP03", nombre="Segmentación y reducción de secuencias temporales", prio="Alta (Must have)", rol="Administrador (Jorge Ponce) y Supervisora de SST (Mariana Torres)",
         hus=[
             ("HU04", "Descartar frames sin operarios", "Must", 4, 28, 2, 2,
              "Depende de HU03. Criterios: excluye los frames sin detección y registra frames entrantes, conservados y % de reducción. "
              "Estado: construida; evidencia con videos reales en la tarea T01 del Sprint 2."),
             ("HU05", "Agrupar frames activos en clips", "Must", 5, 25, 3, 2,
              "Depende de HU04 y habilita HU07. Criterios: secuencias de N frames consecutivos (N configurable) y tensor compatible con ConvLSTM. "
              "Estado: en progreso; faltan la ventana fija de N y el tensor (T02 y T03 del Sprint 2)."),
             ("HU06", "Descartar clips cortos", "Should", 11, 12, 2, 2,
              "Depende de HU05. Va en el Sprint 2 pese a su orden porque filtra los clips antes de entrenar ConvLSTM. "
              "Criterios: descarta clips bajo la duración mínima y registra cuántos. Estado: construida; umbral por alinear con N (T04)."),
         ]),
    dict(id="EP04", nombre="Clasificación espacio-temporal de actos (ConvLSTM)", prio="Alta (Must have)", rol="Supervisora de SST (Mariana Torres)",
         hus=[
             ("HU07", "Procesar clips con ConvLSTM", "Must", 6, 47, 5, 3,
              "Depende de HU05 (tensor). Criterios: inferencia sobre el split oficial de prueba y vector de probabilidades normalizado por secuencia. "
              "La SC-001 (adelantarla al Sprint 2) fue rechazada por el PO. Riesgos R-01 y R-03. Estado: por hacer."),
             ("HU08", "Clasificar y tipificar la conducta", "Must", 7, 38, 3, 3,
              "Depende de HU07. Criterios: etiqueta segura/insegura y tipo de conducta (pasarela peatonal o tablero de control) por clip; "
              "Accuracy, Precision, Recall y F1 por clase. Estado: por hacer."),
         ]),
    dict(id="EP05", nombre="Interfaz de monitoreo y visualización de alertas", prio="Alta (Must have)", rol="Operadora de monitoreo (Lucía Ramos)",
         hus=[
             ("HU09", "Ver video con recuadro de riesgo", "Must", 8, 30, 4, 4,
              "Depende de HU08. Criterios: recuadro verde (seguro) o rojo (inseguro) sobre el video; reproducir, pausar y revisar clips. "
              "Estado: por hacer."),
             ("HU10", "Alerta de conducta insegura", "Should", 9, 21, 2, 4,
              "Depende de HU08. Criterios: alerta visual y sonora; guarda el evento con fecha, momento del video, clip y probabilidad. "
              "Estado: por hacer."),
         ]),
    dict(id="EP06", nombre="Administración, calibración y trazabilidad", prio="Media (Should y Could have)", rol="Administrador (Jorge Ponce) y Gerente de operaciones (Ricardo Salcedo)",
         hus=[
             ("HU11", "Calibrar umbral de confianza de YOLOv8", "Could", 12, 8, 1, 2,
              "Depende de HU03. Va en el Sprint 2 pese a su orden porque calibra el detector de HU03 y el filtro de HU04. "
              "Criterios: umbral de 0,0 a 1,0 desde la interfaz, validado y registrado en el log. Estado: construida; verificación con video real (T05)."),
             ("HU12", "Ver log de tiempos y aceleración", "Should", 10, 15, 2, 4,
              "Depende de HU04. Criterios: tiempos por fase (ingesta, YOLOv8, ConvLSTM) y comparación del tiempo total con y sin reducción. "
              "Estado: por hacer."),
         ]),
]

SCS = [
    ("SC-001", "Adelantar HU07 (ConvLSTM) al Sprint 2", "Alta (propuesta de los Developers)",
     "5 (los de HU07; no agrega puntos)", "No aplica: rechazada (HU07 sigue en el Sprint 3)",
     "FGAP090 del 02/11/2026. **Rechazada para el Sprint 2** por el PO el 02/11/2026: el compromiso subía de 8 a 13 PH frente a una "
     "velocidad objetivo de 8, HU01–HU03 aún no están aceptadas y R-01 es alto. El backlog no cambia. Solo se aprueba T14 (entorno de "
     "Colab, R-03) en el Sprint 2; el análisis de HU07 se reutiliza en la planificación del Sprint 3 (16/11)."),
]

RIESGOS = [
    ("R-01", "Ajuste del modelo temporal (ConvLSTM)", "Alta (P × I = 0,40; riesgo alto)",
     "Sin PH (respuesta: T10, 3 h)", "3",
     "Afecta HU07 y HU08 (y por ellas HU09 y HU10). Respuesta: mitigar con un //spike// de dos valores de N y registro de experimentos (T10); "
     "al rechazarse la SC-001 no se ejecuta en el Sprint 2 y pasa a la planificación del Sprint 3, junto con HU07. "
     "Plan B del Acta: cerrar con una sola conducta."),
    ("R-02", "Implementación propia del pipeline completo", "Media (P × I = 0,20; riesgo moderado)",
     "Sin PH (respuesta: T11–T13, 10 h)", "2",
     "Afecta HU01–HU06 y HU11 (15 PH) y su aceptación por el PO. Respuesta: pipeline con 5 videos reales (T11), revisión de pares "
     "registrada (T12) y prueba E2E con video real (T13)."),
    ("R-03", "GPU y tiempo de entrenamiento limitados", "Media (P × I = 0,20; riesgo moderado)",
     "Sin PH (respuesta: T14, 2 h)", "2 y 3",
     "Afecta HU07 y HU08. Respuesta: entorno de entrenamiento en Google Colab con checkpoint por época (T14), aprobado en el Sprint 2 "
     "como preparación del Sprint 3. Plan B: bajar la resolución o N."),
    ("R-08", "Privacidad de los videos de operarios", "Media (P × I = 0,24; riesgo moderado)",
     "Sin PH (criterio nuevo y tarea de acceso)", "2 y 4",
     "Afecta HU01, HU09 y HU10. Respuesta: criterio de privacidad en HU10 (sin reconocimiento facial ni datos que identifiquen al "
     "trabajador), tarea de control de acceso a videos y clips en el Sprint 4 e ítem nuevo en la DoD. Responsable: Anthony Lopez."),
    ("R-04", "Desbalance de clases y etiquetas de los clips", "Media (P × I = 0,20; riesgo moderado)",
     "Sin PH (criterio nuevo en HU05)", "3",
     "Afecta HU05, HU07 y HU08. Respuesta: conteo de clips por clase en HU05 (tarea 3.04), métricas por clase y F1 macro en el "
     "entrenamiento y la evaluación (3.06 y 3.10). Responsable: Luis Salazar."),
]

NOTA = ("**Nota:** el Product Owner ordena el Product Backlog. La prioridad viene de MoSCoW (Must = Alta, Should = Media, "
        "Could = Baja) y el orden, de la votación de 100 puntos por integrante (300 votos), ajustado por las dependencias del pipeline. "
        "Los puntos de historia se estimaron con Puño de cinco (escala de 1 a 5). Sprints de dos semanas: S1 19/10–30/10, "
        "S2 02/11–13/11, S3 16/11–27/11 y S4 30/11–11/12/2026. «Construida» = código y pruebas automatizadas listos (43/43 pruebas, "
        "verificado el 20/10/2026), pendiente de la aceptación del PO en la revisión del sprint. Fuera del alcance (Won't have): cámaras "
        "RTSP en vivo 24/7, alertas físicas (balizas o sirenas) y reconocimiento facial. Del FGAP050 v1.1 entran los riesgos con "
        "P × I ≥ 0,20 (acción en el backlog); R-05, R-06, R-07 y R-09 se mitigan dentro de tareas y eventos ya planificados.")

GRIS = "D9D9D9"
BORDE = "808080"


def total_ph():
    return sum(h[5] for e in EPICAS for h in e["hus"])


def ph_por_sprint():
    d = {}
    for e in EPICAS:
        for h in e["hus"]:
            d[h[6]] = d.get(h[6], 0) + h[5]
    return d


def epica_ph(e):
    return sum(h[5] for h in e["hus"])


def epica_sprints(e):
    s = sorted({h[6] for h in e["hus"]})
    return " y ".join(str(x) for x in s)


def prio_hu(h):
    return "%s (%s)\nOrden %d · %d votos" % (NIVEL[h[2]], NOMBRE_MOSCOW[h[2]], h[3], h[4])


def build_docx(path):
    d = Doc(landscape=True, margins_cm=(1.9, 1.6, 1.4, 1.6), font="Verdana", size=16,
            header=[("FGAP060 - Backlog Priorizado del Producto", {"size": 16, "align": "right", "after": 0,
                                                                  "border_bottom": "808080"})],
            footer=[("FGAP060 • NewBit • Grupo D3 • Ingeniería de Software II • UNS • Página {PAGE}", {"size": 13, "align": "right"})],
            title="FGAP060 Backlog Priorizado del Producto – NewBit",
            subject="Backlog priorizado del producto del proyecto PY-NB-001 (Grupo D3)")
    # Control de versiones
    rows = [[{"text": "**CONTROL DE VERSIONES**", "span": 6, "fill": GRIS, "align": "center", "size": 18}],
            [{"text": "**//%s//**" % h, "align": "center", "size": 16}
             for h in ["Versión", "Hecho por", "Revisado por", "Aprobado por", "Fecha", "Motivo"]]]
    for v in VERSIONES:
        rows.append([{"text": x, "align": "center", "size": 18, "font": "Times New Roman"} for x in v])
    d.table(rows, widths_cm=[1.6, 3.4, 4.0, 4.4, 2.1, 5.6], border=BORDE, sz=6, cell_margin=50)
    d.p("//BACKLOG PRIORIZADO DEL PRODUCTO//", size=32, align="center", before=200, after=200, shadow=True)
    rows = [[{"text": "**CÓDIGO Y NOMBRE DEL PROYECTO**", "fill": GRIS, "align": "center", "size": 18, "smallcaps": True}],
            [{"text": PROYECTO, "size": 20, "font": "Times New Roman"}]]
    d.table(rows, widths_cm=[15.5], border=BORDE, sz=6, cell_margin=60)
    d.spacer(12)

    # Tabla del backlog (columnas del formato)
    cab = {"fill": GRIS, "align": "center", "size": 15, "font": "Arial", "b": True, "valign": "top"}
    rows = [[dict(cab, text="ÉPICAS\nHISTORIAS DE USUARIO,\nSOLICITUDES DE CAMBIO\nO RIESGOS"),
             dict(cab, text="PRIORIDAD"),
             dict(cab, text="ESTIMACIÓN DE TAMAÑO\n(PUNTOS DE HISTORIA)"),
             dict(cab, text="COMPROMETIDA PARA SPRINT\nNÚMERO"),
             dict(cab, text="OBSERVACIONES")]]
    cel = {"size": 15, "font": "Arial", "valign": "top"}
    grupo = dict(cel, fill="F2F2F2", keep_next=True)
    for e in EPICAS:
        rows.append([dict(grupo, text="**%s – %s**" % (e["id"], e["nombre"])),
                     dict(grupo, text=e["prio"]),
                     dict(grupo, text="%d" % epica_ph(e), align="center"),
                     dict(grupo, text=epica_sprints(e), align="center"),
                     dict(grupo, text="Rol de negocio: %s." % e["rol"])])
        for h in e["hus"]:
            rows.append([dict(cel, text="**%s – %s**" % (h[0], h[1])),
                         dict(cel, text=prio_hu(h)),
                         dict(cel, text=str(h[5]), align="center"),
                         dict(cel, text=str(h[6]), align="center"),
                         dict(cel, text=h[7])])
    sp = ph_por_sprint()
    rows.append([dict(cel, text="**Total del Product Backlog: 12 HU**", fill="F2F2F2"),
                 dict(cel, text="8 Must · 3 Should · 1 Could", fill="F2F2F2"),
                 dict(cel, text="**%d**" % total_ph(), align="center", fill="F2F2F2"),
                 dict(cel, text="1 a 4", align="center", fill="F2F2F2"),
                 dict(cel, text="Por sprint: S1 %d PH · S2 %d PH · S3 %d PH · S4 %d PH." % (sp[1], sp[2], sp[3], sp[4]), fill="F2F2F2")])
    anchos = [5.3, 3.6, 3.0, 2.9, 11.7]
    d.table(rows, widths_cm=anchos, border=BORDE, sz=4, cell_margin=70, header_rows=1)
    # Solicitudes de cambio y riesgos: en una hoja aparte, con la misma cabecera (Pages no respeta
    # «mantener con el siguiente» y dejaba la fila «Riesgos» sola al pie de la hoja 2).
    d.page_break()
    rows = [rows[0]]
    rows.append([dict(grupo, text="**Solicitudes de cambio**"), dict(grupo, text=""), dict(grupo, text=""),
                 dict(grupo, text=""), dict(grupo, text="Formato FGAP090.")])
    for s in SCS:
        rows.append([dict(cel, text="**%s – %s**" % (s[0], s[1])), dict(cel, text=s[2]),
                     dict(cel, text=s[3], align="center"), dict(cel, text=s[4], align="center"), dict(cel, text=s[5])])
    # Riesgos
    rows.append([dict(grupo, text="**Riesgos**"), dict(grupo, text=""), dict(grupo, text=""),
                 dict(grupo, text=""), dict(grupo, text="Fichas del FGAP050; tareas de respuesta en la EDT del Sprint 2 (FGAP110).")])
    for r in RIESGOS:
        rows.append([dict(cel, text="**%s – %s**" % (r[0], r[1])), dict(cel, text=r[2]),
                     dict(cel, text=r[3], align="center"), dict(cel, text=r[4], align="center"), dict(cel, text=r[5])])
    d.table(rows, widths_cm=anchos, border=BORDE, sz=4, cell_margin=70, header_rows=1)
    d.p(NOTA, size=17, font="Times New Roman", before=120, after=0)
    d.save(path)


def _c(x):
    return md_from_markup(x).replace("\n", "<br>")


def build_md(path):
    sp = ph_por_sprint()
    L = ["# FGAP060 – Backlog Priorizado del Producto: NewBit", ""]
    L.append("- **Archivos para entregar** (esta carpeta): `%s.docx` (editable) y `%s.pdf` (horizontal)." % (BASE, BASE))
    L.append("- **Formato:** el del [ejemplo del docente](../../material-del-profe/backlog-priorizado-ejemplo-retinopatia/"
             "backlog-priorizado-ejemplo-retinopatia.md) (Retinopatía, v1.1 corregida): encabezado «FGAP060 - Backlog Priorizado del "
             "Producto», control de versiones, título en cursiva, código y nombre del proyecto, tabla con las columnas **Épicas / Historias "
             "de usuario, solicitudes de cambio o riesgos · Prioridad · Estimación de tamaño (puntos de historia) · Comprometida para Sprint "
             "número · Observaciones** (filas de épica seguidas de sus HU) y nota final. Página A4 horizontal; Verdana, Arial y Times New Roman como el ejemplo.")
    L.append("- **Generador:** `generar_fgap060.py` (datos en las listas `EPICAS`, `SCS` y `RIESGOS`) produce el Word con `docx_nb.py` del "
             "[FGAP110](../../../semana-08-riesgo-y-planificacion-del-sprint/nuestras-entregas/FGAP110_EDT_Sprint_02_NewBit/FGAP110_EDT_Sprint_02_NewBit.md) "
             "y este `.md`. Regenerar: `python3 -I generar_fgap060.py`. PDF exportado con Pages (Word no acepta «guardar como» por AppleScript en esta Mac).")
    L.append("- **Semana:** 5 (el FGAP060 es el paso 5 de la secuencia de avances FGAP010 → FGAP090). Versión 1.0 del 12/10/2026 y 1.1 del "
             "09/11/2026, que agrega la solicitud de cambio y los riesgos.")
    L.append("- **Fuentes:**")
    L.append("  - Épicas e HU: [FGAP040 v2.0](../../../semana-04-justificacion-y-epicas/nuestras-entregas/FGAP040_Epicas_NewBit/FGAP040_Epicas_NewBit.md).")
    L.append("  - Prioridad MoSCoW, votos, orden final, dependencias y sprint: [Priorización MoSCoW + 100 puntos](../Priorizacion_MoSCoW_100_Puntos_NewBit/"
             "Priorizacion_MoSCoW_100_Puntos_NewBit.md).")
    L.append("  - Puntos de historia y criterios: [Tablero Kanban](../Tablero_Kanban_NewBit/Tablero_Kanban_NewBit.md); estado y fechas de los sprints: "
             "[Tablero Kanban actualizado al 20/10](../../../semana-06-producto-unidad-1/nuestras-entregas/Tablero_Kanban_NewBit_Actualizado/"
             "Tablero_Kanban_NewBit_Actualizado.md) y [estado de los sprints](../../../../proyecto-newbit/gestion/sprints/README.md).")
    L.append("  - SC-001: [FGAP090](../../../semana-07-gestion-del-cambio/nuestras-entregas/FGAP090_Solicitud_de_Cambio_NewBit/"
             "FGAP090_Solicitud_de_Cambio_NewBit.md). Riesgos: [FGAP050 v1.1](../../../semana-08-riesgo-y-planificacion-del-sprint/"
             "nuestras-entregas/FGAP050_Riesgo_del_Proyecto_NewBit/FGAP050_Riesgo_del_Proyecto_NewBit.md). Tareas T01–T14: "
             "[EDT del Sprint 2 (FGAP110)](../../../semana-08-riesgo-y-planificacion-del-sprint/nuestras-entregas/FGAP110_EDT_Sprint_02_NewBit/"
             "FGAP110_EDT_Sprint_02_NewBit.md).")
    L.append("")
    L.append("## Control de versiones")
    L.append("| Versión | Hecho por | Revisado por | Aprobado por | Fecha | Motivo |")
    L.append("|---|---|---|---|---|---|")
    for v in VERSIONES:
        L.append("| " + " | ".join(v) + " |")
    L.append("")
    L.append("## Backlog priorizado del producto")
    L.append("**Código y nombre del proyecto:** %s" % PROYECTO)
    L.append("")
    L.append("| Épicas / Historias de usuario, solicitudes de cambio o riesgos | Prioridad | Estimación de tamaño (PH) | "
             "Comprometida para Sprint número | Observaciones |")
    L.append("|---|---|:---:|:---:|---|")
    for e in EPICAS:
        L.append("| **%s – %s** | %s | %d | %s | Rol de negocio: %s. |" % (e["id"], e["nombre"], e["prio"], epica_ph(e),
                                                                     epica_sprints(e), e["rol"]))
        for h in e["hus"]:
            L.append("| %s – %s | %s | %d | %d | %s |" % (h[0], h[1], _c(prio_hu(h)), h[5], h[6], _c(h[7])))
    L.append("| **Total del Product Backlog: 12 HU** | 8 Must · 3 Should · 1 Could | **%d** | 1 a 4 | Por sprint: S1 %d PH · S2 %d PH · "
             "S3 %d PH · S4 %d PH. |" % (total_ph(), sp[1], sp[2], sp[3], sp[4]))
    L.append("| **Solicitudes de cambio** | | | | Formato FGAP090. |")
    for s in SCS:
        L.append("| %s – %s | %s | %s | %s | %s |" % (s[0], s[1], s[2], s[3], s[4], _c(s[5])))
    L.append("| **Riesgos** | | | | Fichas del FGAP050; tareas de respuesta en la EDT del Sprint 2 (FGAP110). |")
    for r in RIESGOS:
        L.append("| %s – %s | %s | %s | %s | %s |" % (r[0], r[1], r[2], r[3], r[4], _c(r[5])))
    L.append("")
    L.append(md_from_markup(NOTA))
    L.append("")
    L.append("**Conteo de filas:** 6 épicas, 12 HU (31 PH), 1 fila de total, 1 solicitud de cambio (SC-001) y 5 riesgos (R-01, R-02, R-03, R-04 y R-08).")
    L.append("")
    L.append("## Decisiones tomadas (criterio del equipo)")
    L.append("- **Prioridad:** el ejemplo del docente usa Alta/Media/Baja y el equipo priorizó con MoSCoW. Se tradujo Must → Alta, Should → Media, "
             "Could → Baja, dejando el término MoSCoW entre paréntesis y, debajo, el **orden final** y los **votos** (de 300) de la priorización, "
             "para que el orden del PO se lea en la misma columna.")
    L.append("- **Orden de las filas:** como el ejemplo, agrupadas por épica (EP01 a EP06) y con las HU en su número; el orden de prioridad se lee "
             "en la columna Prioridad (orden 1 a 12). Prioridad de la épica = la más alta de sus HU (EP06: Should y Could → Media).")
    L.append("- **Filas de épica con datos:** el ejemplo las deja vacías; aquí llevan la suma de PH y los sprints de sus HU, como permiten las "
             "instrucciones de llenado («estimación del tamaño de la Épica…»), y el rol de negocio del FGAP040 en Observaciones.")
    L.append("- **Sprint de HU06 y HU11:** van en el Sprint 2 aunque tienen el orden 11 y 12, por la regla de dependencias de la priorización "
             "MoSCoW (HU06 filtra los clips antes de entrenar ConvLSTM; HU11 calibra el detector de HU03 y el filtro de HU04). Se explica en su fila.")
    L.append("- **SC-001 rechazada; HU07 sigue en el Sprint 3.** Se siguió el `.md` del FGAP090 (versión del 09/11/2026): el PO la rechazó para el "
             "Sprint 2 el 02/11/2026 y solo aprobó T14. Por eso su columna Sprint dice «No aplica: rechazada», la fila de HU07 no cambia y la "
             "respuesta a R-01 (T10) pasa al Sprint 3. La SC se mantiene en el backlog como registro de la decisión, como pide el formato "
             "(«solicitudes de cambio o riesgos»). Al empezar esta tarea el FGAP090 decía «pendiente de decisión del PO»; cambió durante el trabajo.")
    L.append("- **Estimación de SC y riesgos:** la SC-001 no agrega puntos (son los 5 PH de HU07). Los riesgos no se estiman en PH: se escribió "
             "«Sin PH» y las horas de sus tareas de respuesta de la EDT del Sprint 2 (T10 3 h, T11–T13 10 h, T14 2 h).")
    L.append("- **Prioridad de los riesgos:** sale de P × I del FGAP050 (alto → Alta; moderado → Media). Entran los riesgos del FGAP050 v1.1 con "
             "P × I ≥ 0,20 (R-01, R-02, R-03, R-04 y R-08), que según su regla de priorización requieren acción en el backlog; los demás se mencionan en la nota.")
    L.append("- **Estado en Observaciones:** el real según el Tablero Kanban actualizado y el estado de los sprints (última verificación: 20/10/2026): "
             "HU01–HU04, HU06 y HU11 **construidas, por aceptar** (no hay acta de revisión del Sprint 1); HU05 **en progreso**; el resto **por hacer**. "
             "No se usaron los estados del burndown porque son **datos simulados para clase**. «Construida» no es «Terminada»: falta la aceptación del PO.")
    L.append("- **Fechas de los sprints:** las del Acta (S1 19/10–30/10, S2 02/11–13/11, S3 16/11–27/11, S4 30/11–11/12), como en el Kanban "
             "actualizado; el Kanban de la semana 5 decía 01/11, 15/11 y 29/11.")
    L.append("- **Numeración de las HU:** se usa la del FGAP040 y la priorización MoSCoW (p. ej. HU03 = Detectar operarios, HU05 = Agrupar en clips). "
             "La tabla del `proyecto-newbit/README.md` usa otra numeración (HU03 = Catálogo web, HU05 = YOLOv8n); los sprints coinciden. "
             "Falta alinear ese README (no se tocó en esta entrega).")
    L.append("- **Won't have:** no son filas del backlog; se dejaron en la nota final (RTSP en vivo, alertas físicas, reconocimiento facial), "
             "como en la priorización MoSCoW y el Acta.")
    L.append("- **Instrucciones de llenado del ejemplo omitidas:** son la guía para los alumnos y no aportan en la entrega llenada (mismo criterio "
             "que el EGAP020). Se agregó un pie de página con «Página N» y la cabecera de la tabla se repite en cada hoja. Las solicitudes de cambio y los riesgos van en la hoja 3, con la misma "
             "cabecera, para que el bloque «Riesgos» no quede separado de sus filas.")
    L.append("")
    L.append("## Estado")
    L.append("Completo: sin campos «POR CONFIRMAR» en el Word ni en el PDF. Si el PO cambia su decisión sobre la SC-001 o acepta HU en una revisión, "
             "se actualizan `EPICAS`, `SCS` o `RIESGOS`, se agrega la versión 1.2 en `VERSIONES` y se regenera.")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")


if __name__ == "__main__":
    assert total_ph() == 31, total_ph()
    assert ph_por_sprint() == {1: 7, 2: 8, 3: 8, 4: 8}, ph_por_sprint()
    assert sum(h[4] for e in EPICAS for h in e["hus"]) == 300
    build_docx(os.path.join(HERE, BASE + ".docx"))
    build_md(os.path.join(HERE, BASE + ".md"))
    print("OK:", BASE + ".docx", BASE + ".md")
