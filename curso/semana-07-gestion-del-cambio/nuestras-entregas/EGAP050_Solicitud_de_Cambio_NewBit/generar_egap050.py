# -*- coding: utf-8 -*-
"""Genera el EGAP050 (Solicitud de Cambio) de NewBit, con la misma solicitud SC-001 del FGAP090:
  1. EGAP050_Solicitud_de_Cambio_NewBit.docx -> formato EGAP050 del docente (ejemplos 1 y 2, Retinopatía).
  2. EGAP050_Solicitud_de_Cambio_NewBit.md   -> resumen del repo con el contenido completo.
El PDF se exporta aparte con Pages (ver el .md).
Uso: python3 -I generar_egap050.py   (escribe en esta carpeta)
Fuentes: FGAP090 SC-001 (misma solicitud, impactos y decisión), FGAP040 (épicas e HU), priorización MoSCoW,
FGAP050 (R-01 a R-03), FGAP110/FGAP130 (tareas T01–T14 del Sprint 2) y burndown (velocidad objetivo, arrastre de HU05).
"""
import os
import sys

sys.dont_write_bytecode = True  # no dejar __pycache__ en las carpetas de entregas
HERE = os.path.dirname(os.path.abspath(__file__))
FGAP110 = os.path.abspath(os.path.join(HERE, "..", "..", "..", "semana-08-riesgo-y-planificacion-del-sprint",
                                       "nuestras-entregas", "FGAP110_EDT_Sprint_02_NewBit"))
sys.path.insert(0, FGAP110)  # docx_nb.py (generador de Word del equipo)
from docx_nb import Doc, md_from_markup  # noqa: E402

BASE = "EGAP050_Solicitud_de_Cambio_NewBit"
FECHA_DOC = "02/11/2026"  # la del FGAP090 (formato pedido en la semana 7; decisión en la planificación del Sprint 2)

VERSION = ["1.0", "Developers (Anthony Lopez y Luis Salazar)", "Anthony Lopez (SM)",
           "Albert Chumacero (PO)", FECHA_DOC, "Registro de la solicitud y decisión del PO"]

ENCABEZADO = [
    ("Asignatura / semestre", "Ingeniería de Software II / 2026-II"),
    ("Docente", "Dr. Alfredo Daza Vergaray"),
    ("Unidad / semana", "Segunda unidad – Semana 7: Scrum – Cambio"),
    ("Proyecto", "PY-NB-001 – Sistema web con Visión Artificial para la detección de actos inseguros en áreas "
                 "operativas de manufactura metalmecánica (NewBit)"),
    ("Empresa cliente / desarrolladora", "Taller de manufactura metalmecánica (caso académico) / Grupo D3 – equipo NewBit (UNS)"),
    ("Equipo Scrum", "Albert Chumacero (Product Owner) · Anthony Lopez (Scrum Master y Developer) · Luis Salazar (Developer)"),
]

S1 = [  # 1. Control e identificación
    ("Código / versión", "SC-001 / 1.0"),
    ("Fecha / estado", "02/11/2026 / Evaluada; **no aprobada para el Sprint 2** por el Product Owner. HU07 se mantiene en el "
                       "Sprint 3 del Product Backlog."),
    ("Solicitante", "Luis Salazar y Anthony Lopez – Developers (Grupo D3)"),
    ("Responsable de evaluar", "Albert Sebastian Chumacero Chávarry – Product Owner (facilita: Anthony Lopez, Scrum Master)"),
    ("Épicas relacionadas", "EP04 – Clasificación espacio-temporal de actos (ConvLSTM); EP03 – Segmentación y reducción de "
                            "secuencias temporales (aporta la entrada del modelo)"),
    ("Historias relacionadas", "HU07 – Procesar el clip segmentado mediante ConvLSTM (objeto del cambio); HU05 – Agrupar los "
                               "frames activos en clips (dependencia); HU08 – Clasificar y tipificar la conducta (sucesora)"),
]

S2 = [  # 2. Descripción y justificación del cambio
    ("Situación actual",
     "Las HU del Sprint 2 (HU04, HU05, HU06 y HU11; 8 pts) están construidas desde el 17/10/2026, salvo la ventana fija de N "
     "frames y el tensor de entrada de HU05; las 7 HU de los Sprints 1 y 2 pasan 43/43 pruebas automatizadas (20/10) y aún no "
     "tienen aceptación del PO. Con el plan vigente, el Sprint 2 tiene 22 h de tareas frente a ≈ 56 h de capacidad de los dos "
     "Developers, mientras HU07 (ConvLSTM, 5 pts), la historia de mayor riesgo técnico, sigue en el Sprint 3 (16–27/11)."),
    ("Cambio solicitado",
     "Adelantar HU07 «Procesar el clip segmentado mediante ConvLSTM» (EP04, //Must//, 5 pts) del Sprint 3 al Sprint 2 "
     "(02–13/11), sin cambiar su texto, sus criterios de aceptación ni sus puntos. Se descompondría en T06–T09 de la EDT del "
     "Sprint 2 (16 h), más las respuestas a R-01 y R-03 (T10 y T14; 5 h), con una regla de corte: si el 10/11 se activa el "
     "trigger de R-01 o de R-03, HU07 vuelve al Product Backlog para el Sprint 3."),
    ("Justificación / valor",
     "Ordenar el trabajo por valor, riesgo y dependencias: HU07 es //Must//, concentra la mayor incertidumbre técnica y su "
     "dependencia (HU05) se completa en el mismo sprint. Daría una primera evidencia del modelo temporal en la revisión del "
     "Sprint 2 y holgura en el Sprint 3 para un segundo ciclo de ajuste y para HU08. Sin el cambio, ConvLSTM empieza el 16/11 "
     "y, si el primer entrenamiento falla, queda una sola semana antes del Sprint 4. Alternativas descartadas por el equipo: "
     "adelantar también HU08 (supera la capacidad y necesita un modelo entrenado) o la interfaz HU09 (depende de HU08)."),
    ("Alcance / exclusiones",
     "Incluye tensores del split oficial, arquitectura ConvLSTM base, entrenamiento con checkpoint, inferencia sobre el split "
     "oficial de prueba y prueba de integración HU05 → HU07. No incluye la clasificación y tipificación final (HU08), las "
     "métricas por clase ni la interfaz y las alertas (HU09 y HU10); no cambia el alcance del Acta, las 12 HU ni los 31 pts."),
]

S3 = [  # 3. Análisis de impacto (estimación académica)
    ("Alcance",
     "Solo cambiaría el sprint de HU07 (3 → 2): S1 7 · S2 8 → 13 · S3 8 → 3 · S4 8 pts (total 31). Sin cambios en el alcance "
     "del Acta ni en la separación modular espacial/temporal. **Impacto en el backlog tras la decisión: ninguno** (HU07 sigue "
     "en el Sprint 3)."),
    ("Tiempo / esfuerzo",
     "HU07 mantiene 5 pts. El Sprint 2 pasaría de 8 a 13 pts, por encima de la velocidad objetivo de 8 pts por sprint, y de "
     "22 h a 43 h de tareas (≈ 77 % de ≈ 56 h): T06–T09 (16 h), T10 (3 h) y T14 (2 h). Sin cambios en el Sprint 4 ni en la "
     "liberación (14–18/12). Se evalúa en la planificación del Sprint 2, sin alterar un sprint en curso."),
    ("Costo",
     "Sin costo adicional: las 21 h ya están presupuestadas en el Acta (≈ S/ 762 con sus tarifas) y solo se adelantaría la "
     "partida de GPU en la nube (S/ 80). Sin compra de licencias: bibliotecas abiertas y Google Colab."),
    ("Calidad / seguridad",
     "HU07 debe cumplir sus criterios y la Definición de Terminado (FGAP070): prueba de integración HU05 → HU07, revisión de "
     "pares, configuración versionada con semilla fija y suite completa en verde. Se mantienen el split oficial y la atribución "
     "CC BY 4.0 del dataset (Önal y Dandıl, 2024), sin reconocimiento facial."),
    ("Riesgos",
     "R-01, ajuste del modelo temporal (exposición 0,40, alta): //spike// de dos valores de N y registro versionado (T10). "
     "R-03, GPU y tiempo de entrenamiento (0,20): entorno en Colab con checkpoint por época (T14). R-02, pipeline propio: "
     "evidencia con videos reales del dataset (T11–T13). Si un trigger se activara el 10/11, se aplicaría la regla de corte."),
    ("Dependencias",
     "HU07 necesita el tensor de entrada de HU05 (T02–T03), que aún no cumple la DoD, y los videos del dataset verificados en "
     "T11. HU07 destraba la cadena HU08 → HU09/HU10. Requiere acceso a GPU en Google Colab y el dataset completo descargado."),
]

CRITERIOS = [
    "CA01. Con el tensor de HU05, el modelo ConvLSTM ejecuta la inferencia espacio-temporal sobre el split oficial de prueba del dataset.",
    "CA02. Por cada secuencia se obtiene un vector de probabilidades normalizado (suma 1) sobre las clases definidas.",
    "CA03. La prueba de integración HU05 → HU07 verifica la forma del tensor y una salida por secuencia, y la suite automatizada pasa completa.",
    "CA04. La configuración (N, capas, hiperparámetros) queda versionada con semilla fija y el checkpoint guardado, para reproducir la inferencia.",
    "CA05. El código de entrenamiento e inferencia tiene revisión de pares registrada, sin observaciones críticas abiertas.",
    "CA06. El Product Backlog, el Tablero Kanban, la EDT, el cronograma y el burndown muestran HU07 en el sprint que decida el PO.",
]

S5 = [  # 5. Evaluación, decisión y seguimiento
    ("Evaluación de Developers",
     "Técnicamente viable y dentro de la capacidad en horas del Sprint 2 (43 h de ≈ 56 h), con la regla de corte del 10/11. "
     "Se propuso la arquitectura base (T07), los tensores del split oficial (T06), un //spike// de dos valores de N (T10) antes "
     "de entrenar (T08) y la prueba de integración (T09)."),
    ("Decisión del Product Owner",
     "**No aprobada para el Sprint 2** (Albert Chumacero, 02/11/2026, planificación del Sprint 2). Motivos: el compromiso "
     "subiría de 8 a 13 pts frente a una velocidad objetivo de 8 pts; HU05, de la que depende HU07, aún no cumple la DoD (le "
     "faltan la ventana fija de N y el tensor de entrada); HU01–HU03 aún no están aceptadas y el Sprint 2 debe dejar primero evidencia con videos reales (T11–T13); "
     "y R-01 tiene exposición alta (0,40). HU07 se mantiene en el Sprint 3."),
    ("Planificación",
     "Sprint 2: solo se ejecuta T14 (entorno de entrenamiento en Colab, respuesta a R-03; 2 h, Luis Salazar); T06–T10 no se "
     "ejecutan y el sprint queda con 24 h (T01–T05, T11–T14). HU07 se planifica en el Sprint 3 (16–27/11) y reutiliza el "
     "análisis de esta solicitud (tareas, horas y riesgos)."),
    ("Responsables",
     "Product Owner: decisión y orden del Product Backlog. Developers: Luis Salazar ejecuta T14; Luis Salazar y Anthony Lopez "
     "estiman HU07 en la planificación del Sprint 3. Scrum Master (Anthony Lopez): facilita e informa la decisión al equipo, "
     "al Sponsor (Ricardo Salcedo) y a SST (Mariana Torres), usuaria de HU07."),
    ("Estado y evidencia",
     "Solicitud evaluada y cerrada para el Sprint 2; registrada también en el FGAP090 (SC-001). Product Backlog sin cambios. "
     "Evidencia: esta solicitud, el entorno de Colab de T14 y, en el Sprint 3, HU07 con sus criterios CA01–CA06 en la revisión."),
]

NOTA = ("//Nota: caso académico; la empresa y los interesados de negocio son ficticios (Acta FGAP010 v2.0). Las horas, puntos y costos "
        "son estimaciones del equipo, no resultados. Scrum no exige un comité formal de control de cambios: decide el Product Owner.//")

ROJO = "C00000"
AZUL = "4F81BD"
BORDE = "000000"
W = [5.4, 12.0]  # rótulo | contenido (cm)


def tabla(d, filas):
    rows = [[{"text": "**%s**" % k, "valign": "top"}, {"text": v, "valign": "top"}] for k, v in filas]
    d.table(rows, widths_cm=W, border=BORDE, sz=4, cell_margin=60, keep_rows=True)


def seccion(d, titulo):
    d.p("**%s**" % titulo, size=26, color=AZUL, before=140, after=40, keep_next=True)


def build_docx(path):
    d = Doc(landscape=False, margins_cm=(2.0, 1.8, 1.8, 1.8), font="Arial", size=17,
            header=[("**UNIVERSIDAD NACIONAL DEL SANTA  |  INGENIERÍA DE SOFTWARE II**", {"size": 17, "align": "right", "after": 0})],
            footer=[("EGAP050 | Grupo D3 – NewBit | UNS – 2026-II | Pág. {PAGE}", {"size": 17, "align": "center"})],
            title="EGAP050 Solicitud de Cambio SC-001 – NewBit",
            subject="Solicitud de cambio SC-001 del proyecto PY-NB-001 (Grupo D3)")
    d.p("**UNIVERSIDAD NACIONAL DEL SANTA**", size=32, color=ROJO, align="center", before=0, after=60)
    d.p("Facultad de Ingeniería | Escuela Profesional de Ingeniería de Sistemas e Informática", size=17, align="center", after=200)
    d.p("**FORMATO EGAP050 – SOLICITUD DE CAMBIO**", size=24, align="center", after=160)
    tabla(d, ENCABEZADO)
    # Control de versiones (lo pide el curso en todas las entregas; el ejemplo EGAP050 no lo trae)
    seccion(d, "Control de versiones")
    cab = [{"text": "**%s**" % h, "align": "center", "fill": "D9D9D9"} for h in
           ["Versión", "Hecho por", "Revisado por", "Aprobado por", "Fecha", "Motivo"]]
    d.table([cab, [{"text": v, "align": "center"} for v in VERSION]],
            widths_cm=[1.6, 3.9, 2.7, 3.0, 2.0, 4.2], border=BORDE, sz=4, cell_margin=60)
    seccion(d, "1. Control e identificación")
    tabla(d, S1)
    seccion(d, "2. Descripción y justificación del cambio")
    tabla(d, S2)
    seccion(d, "3. Análisis de impacto (estimación académica)")
    tabla(d, S3)
    seccion(d, "4. Criterios de aceptación propuestos")
    for c in CRITERIOS:
        d.bullet(c, after=20)
    seccion(d, "5. Evaluación, decisión y seguimiento")
    tabla(d, S5)
    d.p(NOTA, size=15, before=0, after=0)
    d.save(path)


def build_md(path):
    def tab(filas):
        out = ["| Campo | Contenido |", "|---|---|"]
        out += ["| %s | %s |" % (k, md_from_markup(v)) for k, v in filas]
        return out
    sem08 = "../../../semana-08-riesgo-y-planificacion-del-sprint/nuestras-entregas/"
    L = ["# EGAP050 – Solicitud de Cambio: NewBit (SC-001, adelantar HU07 al Sprint 2 · no aprobada)", ""]
    L.append("- **Archivos para entregar** (esta carpeta): `%s.docx` (editable) y `%s.pdf` (3 págs., A4 vertical)." % (BASE, BASE))
    L.append("- **Formato:** EGAP050 del docente ([ejemplo 1](../../material-del-profe/solicitud-de-cambio-egap050-ejemplo-1/"
             "solicitud-de-cambio-egap050-ejemplo-1.md) y [ejemplo 2](../../material-del-profe/solicitud-de-cambio-egap050-ejemplo-2/"
             "solicitud-de-cambio-egap050-ejemplo-2.md), Retinopatía). Se copiaron sus secciones y su diseño: encabezado "
             "«UNIVERSIDAD NACIONAL DEL SANTA | INGENIERÍA DE SOFTWARE II», nombre de la universidad en rojo, facultad y escuela, "
             "título «FORMATO EGAP050 – SOLICITUD DE CAMBIO», tabla de datos del curso y del proyecto, secciones 1–5 numeradas con "
             "títulos en azul, tablas de dos columnas (rótulo en negrita | contenido), criterios CA en viñetas, nota final en cursiva "
             "y pie «EGAP050 | … | UNS – 2026-II».")
    L.append("- **Generador:** `generar_egap050.py` produce el Word con `docx_nb.py` del [FGAP110](%sFGAP110_EDT_Sprint_02_NewBit/"
             "FGAP110_EDT_Sprint_02_NewBit.md) y este `.md`. PDF exportado con Pages (Word no acepta «guardar como» por AppleScript)." % sem08)
    L.append("- **Fecha:** %s (la del FGAP090; el formato es de la semana 7 y la decisión se tomó en la planificación del Sprint 2) · "
             "**Versión:** 1.0 (Grupo D3)." % FECHA_DOC)
    L.append("- **Estado:** completo, sin «POR CONFIRMAR». La SC-001 está **no aprobada para el Sprint 2** por el Product Owner "
             "(02/11/2026): HU07 sigue en el Sprint 3.")
    L.append("")
    L.append("## Relación con el FGAP090")
    L.append("Es la **misma solicitud SC-001** del [FGAP090](../FGAP090_Solicitud_de_Cambio_NewBit/FGAP090_Solicitud_de_Cambio_NewBit.md) "
             "(solicitantes, cambio, cifras de impacto, riesgos y decisión del PO), escrita en el formato EGAP050, que es más corto y "
             "agrega dos cosas que el FGAP090 no tiene: **épicas e historias relacionadas** y **criterios de aceptación propuestos** "
             "(CA01–CA06). Equivalencias: «Definición del problema» → Situación actual · «Descripción detallada» → Cambio solicitado y "
             "Alcance/exclusiones · «Razón» → Justificación/valor · «Efectos en el proyecto / otros proyectos / extra empresariales» → "
             "sección 3 · «Revisión de la solicitud» → sección 5. Trazabilidad: tareas T01–T14 de la [EDT (FGAP110)](%s"
             "FGAP110_EDT_Sprint_02_NewBit/FGAP110_EDT_Sprint_02_NewBit.md) y del [cronograma (FGAP130)](%sFGAP130_Cronograma_Sprint_02_NewBit/"
             "FGAP130_Cronograma_Sprint_02_NewBit.md); riesgos del [FGAP050](%sFGAP050_Riesgo_del_Proyecto_NewBit/"
             "FGAP050_Riesgo_del_Proyecto_NewBit.md); velocidad objetivo y arrastre de HU05 del [burndown](%sBurndown_Sprint_NewBit/"
             "Burndown_Sprint_NewBit.md)." % (sem08, sem08, sem08, sem08))
    L.append("")
    L.append("## Control de versiones")
    L.append("| Versión | Hecho por | Revisado por | Aprobado por | Fecha | Motivo |")
    L.append("|---|---|---|---|---|---|")
    L.append("| " + " | ".join(VERSION) + " |")
    L.append("")
    L.append("## Formato EGAP050 – Solicitud de cambio")
    L += tab(ENCABEZADO)
    L.append("")
    L.append("### 1. Control e identificación")
    L += tab(S1)
    L.append("")
    L.append("### 2. Descripción y justificación del cambio")
    L += tab(S2)
    L.append("")
    L.append("### 3. Análisis de impacto (estimación académica)")
    L += tab(S3)
    L.append("")
    L.append("### 4. Criterios de aceptación propuestos")
    L += ["- " + c for c in CRITERIOS]
    L.append("")
    L.append("### 5. Evaluación, decisión y seguimiento")
    L += tab(S5)
    L.append("")
    L.append(md_from_markup(NOTA))
    L.append("")
    L.append("## Decisiones y supuestos (no van en el formato)")
    L.append("- **Decisión del PO:** el FGAP090 dejaba la decisión pendiente; el coordinador del equipo la fijó el 09/11/2026 como "
             "**no aprobada para el Sprint 2**, con fecha de decisión 02/11/2026 (planificación del Sprint 2), para que todos los "
             "documentos queden completos y coherentes. Si el PO decide otra cosa, se emite una versión 1.1 de este EGAP050 y del FGAP090.")
    L.append("- **Motivos de la decisión:** 13 pts frente a una velocidad objetivo de 8 pts por sprint (burndown: 5 h/PH); HU05 sin la "
             "ventana fija de N ni el tensor de entrada, así que no cumple la DoD (en el burndown pasa al Sprint 3 como arrastre); "
             "R-01 con exposición 0,40 (FGAP050). La capacidad en horas sí alcanzaba (43 h de ≈ 56 h); el PO decidió por puntos, "
             "DoD y riesgo, no por horas.")
    L.append("- **Horas del Sprint 2 tras la decisión:** 24 h = 22 h de T01–T05 y T11–T13 + 2 h de T14, que sí se ejecuta porque "
             "prepara el entrenamiento del Sprint 3 (respuesta a R-03). Coincide con la «carga real: 24 h» del FGAP110 y el FGAP130.")
    L.append("- **Secciones 2 y 3 en condicional:** describen la solicitud tal como la presentaron los Developers (lo que pasaría si se "
             "aprobaba); el efecto real en el backlog se dice en «Alcance» (sección 3) y en la sección 5.")
    L.append("- **Criterios de aceptación:** CA01–CA02 son los dos criterios de HU07 del Product Backlog (Tablero Kanban, semana 5); "
             "CA03–CA05 salen de las tareas T09 y T12 y de la DoD (FGAP070); CA06 es de gestión del cambio. Se aplican cuando HU07 se "
             "ejecute en el Sprint 3.")
    L.append("- **Agregados al diseño del ejemplo:** fila «Equipo Scrum» en la tabla del encabezado, tabla de **control de versiones** "
             "(la pide el curso en cada entrega) y número de página en el pie. El título no lleva «(EJEMPLO DESARROLLADO)».")
    L.append("- **Diferencias de diseño:** A4 (el ejemplo es carta), columnas de 5,4 cm y 12 cm en vez de mitades (el contenido de NewBit "
             "es más largo) y títulos de sección en Arial azul (el ejemplo usa Calibri, que no está instalado en la Mac donde se exporta).")
    L.append("- **Empresa cliente:** el Acta la presenta como taller metalmecánico ficticio (caso académico); la desarrolladora es el Grupo D3.")
    L.append("- **Supuestos:** dataset completo descargado (se verifica en T11) y acceso a GPU en Google Colab (se prepara en T14).")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")


if __name__ == "__main__":
    build_docx(os.path.join(HERE, BASE + ".docx"))
    build_md(os.path.join(HERE, BASE + ".md"))
    print("ok", HERE)
