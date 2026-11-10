# -*- coding: utf-8 -*-
"""Genera el EGAP020 (Registro de Stakeholders) de NewBit:
  1. EGAP020_Registro_de_Stakeholders_NewBit.docx -> formato EGAP020 del docente (ejemplo BigFarma), horizontal.
  2. EGAP020_Registro_de_Stakeholders_NewBit.md   -> resumen del repo con la tabla completa.
El PDF se exporta aparte con Pages (ver el .md).
Uso: python3 -I generar_egap020.py   (escribe en esta carpeta)
Fuentes de los datos: Acta FGAP010 v2.0 (lista de interesados clave), FGAP030 v2.0 (roles y prototipos)
y FGAP040 v2.0 (historias de usuario). Contactos de la empresa: simulados (dominio .example), como en el ejemplo del docente.
Actividad individual: hecha por Anthony Gabriel Lopez Yrribarren.
"""
import os
import sys

sys.dont_write_bytecode = True  # no dejar __pycache__ en las carpetas de entregas
HERE = os.path.dirname(os.path.abspath(__file__))
FGAP110 = os.path.abspath(os.path.join(HERE, "..", "..", "..", "semana-08-riesgo-y-planificacion-del-sprint",
                                       "nuestras-entregas", "FGAP110_EDT_Sprint_02_NewBit"))
sys.path.insert(0, FGAP110)  # docx_nb.py (generador de Word del equipo)
from docx_nb import Doc, md_from_markup  # noqa: E402

BASE = "EGAP020_Registro_de_Stakeholders_NewBit"
FECHA_DOC = "09/11/2026"
PROYECTO = ("PY-NB-001 – Sistema web con Visión Artificial para la detección de actos inseguros "
            "en áreas operativas de manufactura metalmecánica (NewBit)")
AUTOR = "Anthony Gabriel Lopez Yrribarren"  # actividad individual
VERSION = ["1.0", AUTOR, "Albert Chumacero – Product Owner",
           "Ricardo Salcedo – Sponsor", FECHA_DOC, "Versión original"]

EMP = "Empresa metalmecánica (caso académico)"
UBI_EMP = "Nuevo Chimbote"
UBI_UNS = "Chimbote (UNS)"
PC = "{PC}"

# Cada stakeholder: nombre, empresa y puesto, ubicación, rol, contacto, requisitos, expectativas,
# influencia, áreas de mayor interés. Las listas se muestran como párrafos separados (como BigFarma).
S = [
    dict(nombre="Ricardo Salcedo Paredes", empresa=EMP + " – Gerente General", ubic=UBI_EMP,
         rol="Sponsor", contacto="rsalcedo@metalmecanica.example · Anexo 101",
         req=["Autorizar el proyecto y aprobar sus recursos (S/ 20,768) y el cronograma 05/10–18/12/2026.",
              "Ver el log de tiempos y el ahorro de cómputo (HU12)."],
         exp=["Cifras claras sobre conductas inseguras por tipo y zona para decidir recursos, capacitaciones "
              "y la ampliación a nuevas conductas."],
         infl="Alta",
         areas=["Inicio (Acta y recursos)", "Lanzamiento 2 y cierre"]),
    dict(nombre="Mariana Torres Cárdenas", empresa=EMP + " – Supervisora de SST", ubic=UBI_EMP,
         rol="Stakeholder (usuaria clave, SST)", contacto="mtorres@metalmecanica.example · Anexo 102",
         req=["Definir qué conductas importan: tránsito fuera de la vía peatonal y panel eléctrico abierto.",
              "Detección y clasificación segura/insegura con clip de evidencia (HU03, HU05–HU08)."],
         exp=["Enterarse de una conducta insegura cuando aún puede intervenir y saber en qué zonas se repite, "
              "sin revisar horas de video."],
         infl="Media",
         areas=["Sprint 3: clasificación ConvLSTM (HU07, HU08)", "Validación de alertas (Sprint 4)"]),
    dict(nombre="Jorge Ponce Aguilar", empresa=EMP + " – Analista de TI (administrador de la plataforma)",
         ubic=UBI_EMP, rol="Stakeholder técnico (TI)", contacto="jponce@metalmecanica.example · Anexo 103",
         req=["Cargar videos .mp4/.avi y obtener frames (HU01, HU02).",
              "Ajustar el umbral de confianza desde la interfaz, sin tocar código (HU11).",
              "Revisar infraestructura, almacenamiento y seguridad de la información."],
         exp=["Procesamiento sin intervención manual, con mensajes de error claros e historial de cambios."],
         infl="Media",
         areas=["Sprints 1 y 2: ingesta, filtrado y calibración", "Sprint 4: log de procesamiento (HU12)"]),
    dict(nombre="César Vásquez Lozano", empresa=EMP + " – Supervisor de turno de operaciones", ubic=UBI_EMP,
         rol="Stakeholder (usuario operativo)", contacto="cvasquez@metalmecanica.example · Anexo 104",
         req=["Consultar las alertas de su área con hora, ubicación, tipo de conducta y clip."],
         exp=["Saber rápido qué pasó, dónde y cuándo, en una pantalla sencilla y sin recibir la misma alerta "
              "varias veces."],
         infl="Baja",
         areas=["Sprint 4: interfaz y alertas (HU09, HU10)"]),
    dict(nombre="Lucía Ramos Villena", empresa=EMP + " – Operadora de la central de monitoreo", ubic=UBI_EMP,
         rol="Stakeholder (usuaria operativa)", contacto="lramos@metalmecanica.example · Anexo 105",
         req=["Alerta visual y sonora con hora y evidencia (RF-07, HU10).",
              "Video con recuadro de riesgo verde/rojo (HU09)."],
         exp=["Que NewBit le señale solo lo importante y le permita confirmar o descartar una alerta en un clic."],
         infl="Baja",
         areas=["Sprint 4: interfaz de monitoreo y alertas (HU09, HU10)"]),
    dict(nombre="Trabajadores de planta (operarios)", empresa=EMP + " – Operarios del taller", ubic=UBI_EMP,
         rol="Stakeholder (personas observadas)",
         contacto="Por medio de la Supervisora de SST (Anexo 102)",
         req=["Privacidad por diseño: sin reconocimiento facial ni identificación de trabajadores."],
         exp=["Que las alertas sirvan para prevenir actos inseguros; aportan contexto operativo y validan su utilidad."],
         infl="Baja",
         areas=["Definición de conductas (Inicio)", "Validación de alertas (Sprint 4)"]),
    dict(nombre="Dr. Alfredo Daza Vergaray", empresa="UNS – Docente de Ingeniería de Software II", ubic=UBI_UNS,
         rol="Stakeholder académico (revisor)", contacto="Aula virtual del curso Ingeniería de Software II (UNS)",
         req=["Entregables de gestión en los formatos del curso y coherentes con Scrum.",
              "Demostración de NewBit e informe técnico."],
         exp=["Proyecto reproducible, con métricas por clase y sin afirmar resultados no demostrados."],
         infl="Alta",
         areas=["Revisión de entregables de cada semana", "Lanzamiento 2 y sustentación (14–18/12)"]),
    dict(nombre="Albert Sebastian Chumacero Chávarry", empresa="UNS – Estudiante, Grupo D3", ubic=UBI_UNS,
         rol="Product Owner", contacto="Grupo D3 · aula virtual del curso (UNS)",
         req=["Backlog priorizado (12 HU, 31 puntos) con criterios de aceptación.",
              "Aceptar o rechazar los incrementos de cada sprint."],
         exp=["Incrementos que aporten valor en cada revisión, sin cambiar el alcance sin acuerdo del Sponsor."],
         infl="Alta",
         areas=["Todas"]),
    dict(nombre="Anthony Gabriel Lopez Yrribarren", empresa="UNS – Estudiante, Grupo D3", ubic=UBI_UNS,
         rol="Scrum Master y Developer", contacto="Grupo D3 · aula virtual del curso (UNS)",
         req=["Facilitar los eventos Scrum y eliminar impedimentos.",
              "Implementar interfaz, registro, integración del pipeline y pruebas."],
         exp=["Cumplir los 4 sprints en fecha pese al doble rol, con time-boxing y revisión de pares."],
         infl="Media",
         areas=["Todas", "Sprint 4: interfaz, registro y alertas"]),
    dict(nombre="Luis Fernando Salazar Diaz", empresa="UNS – Estudiante, Grupo D3", ubic=UBI_UNS,
         rol="Equipo Scrum (Developer)", contacto="Grupo D3 · aula virtual del curso (UNS)",
         req=["Dataset de Önal y Dandıl (2024) con su split oficial y atribución CC BY 4.0.",
              "GPU suficiente para entrenar (Colab o local)."],
         exp=["Modelos YOLOv8 y ConvLSTM entrenados y evaluados con métricas por clase y resultados reproducibles."],
         infl="Media",
         areas=["Sprints 1 a 3: datos, YOLOv8 y ConvLSTM"]),
]

NOTA = ("**Nota:** la empresa metalmecánica es un caso académico: los nombres y cargos de sus representantes son "
        "ficticios para fines de modelado, como declara el Acta FGAP010 v2.0, y no se usa video privado de sus instalaciones. "
        "Influencia potencial = capacidad de afectar las decisiones del proyecto (Alta/Media/Baja), no la importancia de la persona. "
        "Los contactos de la empresa son simulados (dominio reservado .example y anexos internos), como en el ejemplo del docente.")

GRIS = "D9D9D9"
GRIS_CAB = "E7E6E6"
BORDE = "595959"


def build_docx(path):
    d = Doc(landscape=True, margins_cm=(1.9, 1.6, 1.4, 1.6), font="Verdana", size=16,
            header=[("EGAP020 - Registro de Stakeholders", {"size": 16, "align": "right", "after": 0,
                                                            "border_bottom": "808080"})],
            footer=[("EGAP020 • Anthony Gabriel Lopez Yrribarren • Ingeniería de Software II • UNS • Página {PAGE}", {"size": 13, "align": "right"})],
            title="EGAP020 Registro de Stakeholders – NewBit",
            subject="Registro de stakeholders del proyecto PY-NB-001 (Grupo D3)")
    # Control de versiones
    rows = [[{"text": "**CONTROL DE VERSIONES**", "span": 6, "fill": GRIS, "align": "center", "size": 18}],
            [{"text": "**//%s//**" % h, "align": "center", "size": 16}
             for h in ["Versión", "Hecho por", "Revisado por", "Aprobado por", "Fecha", "Motivo"]],
            [{"text": v, "align": "center", "size": 18, "font": "Arial"} for v in VERSION]]
    d.table(rows, widths_cm=[1.7, 3.6, 4.3, 4.3, 2.0, 3.1], border=BORDE, sz=4, cell_margin=50)
    d.p("//REGISTRO DE STAKEHOLDERS//", size=32, align="center", before=160, after=160, shadow=True)
    rows = [[{"text": "**CÓDIGO Y NOMBRE DEL PROYECTO**", "fill": GRIS, "align": "center", "size": 18, "smallcaps": True}],
            [{"text": PROYECTO, "align": "center", "size": 18, "font": "Arial"}]]
    d.table(rows, widths_cm=[19.0], border=BORDE, sz=4, cell_margin=60)
    d.spacer(10)
    # Registro
    cab = {"fill": GRIS_CAB, "align": "center", "size": 14, "font": "Tahoma", "b": True}
    rows = [[dict(cab, text="INFORMACIÓN DE IDENTIFICACIÓN", span=5),
             dict(cab, text="INFORMACIÓN DE EVALUACIÓN", span=4)],
            [dict(cab, text=t) for t in ["NOMBRE", "EMPRESA Y PUESTO", "UBICA-\nCIÓN", "ROL EN EL PROYECTO",
                                         "INFORMACIÓN\nDE CONTACTO", "REQUISITOS PRINCIPALES",
                                         "EXPECTATIVAS PRINCIPALES", "INFLUENCIA\nPOTENCIAL",
                                         "ÁREAS DE MAYOR INTERÉS"]]]
    cel = {"align": "center", "size": 15, "font": "Tahoma"}
    for s in S:
        rows.append([
            dict(cel, text=s["nombre"], font="Arial", size=17),
            dict(cel, text=s["empresa"], font="Arial", size=16),
            dict(cel, text=s["ubic"]),
            dict(cel, text=s["rol"]),
            dict(cel, text=s["contacto"]),
            dict(cel, paras=s["req"], after=50),
            dict(cel, paras=s["exp"], after=50),
            dict(cel, text=s["infl"]),
            dict(cel, paras=s["areas"], after=80),
        ])
    d.table(rows, widths_cm=[2.5, 3.1, 1.75, 2.3, 2.5, 4.6, 4.0, 2.0, 3.0], border=BORDE, sz=4,
            cell_margin=70, header_rows=2)  # sin cantSplit: con tblHeader, Pages manda toda la tabla a la pág. 2
    d.p(NOTA, size=13, before=60, after=0)
    d.save(path)


def _md_cell(x):
    if isinstance(x, list):
        return "<br>".join(md_from_markup(i) for i in x)
    return md_from_markup(x)


def build_md(path):
    L = ["# EGAP020 – Registro de Stakeholders: NewBit", ""]
    L.append("- **Archivos para entregar** (esta carpeta): `%s.docx` (editable) y `%s.pdf` (2 págs., horizontal)." % (BASE, BASE))
    L.append("- **Estructura:** la del [formato EGAP020 del docente](../../material-del-profe/stakeholders-egap020-ejemplo-bigfarma/"
             "stakeholders-egap020-ejemplo-bigfarma.md) (ejemplo BigFarma, versión «alumnos»): encabezado «EGAP020 - Registro de "
             "Stakeholders», control de versiones, título, código y nombre del proyecto y la tabla con dos grupos de columnas: "
             "**información de identificación** (nombre · empresa y puesto · ubicación · rol en el proyecto · información de contacto) e "
             "**información de evaluación** (requisitos principales · expectativas principales · influencia potencial · áreas de mayor interés). "
             "Se imitó su aspecto: Verdana/Tahoma/Arial, encabezados en gris claro, cursivas de cabecera y título en cursiva.")
    L.append("- **Generador:** `generar_egap020.py` (datos en una sola lista) produce el Word con `docx_nb.py` del "
             "[FGAP110](../../../semana-08-riesgo-y-planificacion-del-sprint/nuestras-entregas/FGAP110_EDT_Sprint_02_NewBit/FGAP110_EDT_Sprint_02_NewBit.md) "
             "y este `.md`. PDF exportado con Pages.")
    L.append("- **Fecha:** %s · **Versión:** 1.0 · **Actividad individual** de %s (Grupo D3, proyecto NewBit)." % (FECHA_DOC, AUTOR))
    L.append("- **Fuentes:** [Acta FGAP010 v2.0](../../../semana-02-scrum-y-acta/nuestras-entregas/FGAP010_Acta_Constitucion_NewBit/"
             "FGAP010_Acta_Constitucion_NewBit.md) (lista de interesados clave, requisitos, alcance, riesgos y criterios), "
             "[FGAP030 v2.0](../../../semana-03-roles-y-prototipos/nuestras-entregas/FGAP030_Roles_y_Prototipos_NewBit/"
             "FGAP030_Roles_y_Prototipos_NewBit.md) (roles, prototipos y lo que cada persona busca) y "
             "[FGAP040 v2.0](../../../semana-04-justificacion-y-epicas/nuestras-entregas/FGAP040_Epicas_NewBit/FGAP040_Epicas_NewBit.md) "
             "(historias de usuario por rol).")
    L.append("")
    L.append("## Control de versiones")
    L.append("| Versión | Hecho por | Revisado por | Aprobado por | Fecha | Motivo |")
    L.append("|---|---|---|---|---|---|")
    L.append("| " + " | ".join(md_from_markup(v) for v in VERSION) + " |")
    L.append("")
    L.append("## Registro de stakeholders")
    L.append("**Código y nombre del proyecto:** %s" % PROYECTO)
    L.append("")
    L.append("| Nombre | Empresa y puesto | Ubicación | Rol en el proyecto | Información de contacto | Requisitos principales | "
             "Expectativas principales | Influencia potencial | Áreas de mayor interés |")
    L.append("|---|---|---|---|---|---|---|---|---|")
    for s in S:
        L.append("| " + " | ".join(_md_cell(s[k]) for k in
                                   ("nombre", "empresa", "ubic", "rol", "contacto", "req", "exp", "infl", "areas")) + " |")
    L.append("")
    L.append(md_from_markup(NOTA))
    L.append("")
    L.append("**Resumen:** 10 stakeholders (9 personas y 1 grupo). Influencia **Alta**: Sponsor, docente y Product Owner · "
             "**Media**: Supervisora de SST, TI, Scrum Master y Developer · **Baja**: operadora de monitoreo, supervisor de turno y operarios.")
    L.append("")
    L.append("## Decisiones tomadas (criterio del equipo)")
    L.append("- **Relación con el FGAP020 v1.0:** el Producto de la Unidad I (semana 6) ya traía un registro de interesados propio, sin plantilla del docente. "
             "Este EGAP020 lo pasa al formato oficial con los mismos 10 interesados y el mismo poder, y agrega lo que pide el formato: empresa y puesto, "
             "ubicación, contacto, requisitos y áreas de mayor interés.")
    L.append("- **Quiénes entran:** los 8 interesados clave del Acta (equipo Scrum, Sponsor, SST, TI, docente y «supervisores y trabajadores "
             "de planta»). Ese último grupo se separó en **César Vásquez** (supervisor de turno) y **Lucía Ramos** (operadora de monitoreo), "
             "que son personas del FGAP030 y usuarios del backlog (Lucía: HU09, HU10), y en una fila de grupo para los **operarios observados**, "
             "porque el requisito de privacidad (sin reconocimiento facial) los protege a ellos.")
    L.append("- **Personas y empresa ficticias:** el Acta dice que el Sponsor, SST y TI son ficticios y que la empresa es un caso propuesto. "
             "Se dejó escrito en la columna «Empresa y puesto» («caso académico») y en la nota bajo la tabla, como pide el ejemplo de Retinopatía "
             "(no presentar datos ficticios como reales).")
    L.append("- **Cargo del Sponsor: Gerente General**, como dicen el Word del Acta y el prototipo del FGAP030. El resumen `.md` del Acta y el "
             "rol de usuario del FGAP030 lo llaman «Gerente de operaciones»; se usó el cargo del documento entregado.")
    L.append("- **Ubicación:** Nuevo Chimbote para la empresa (el FGAP030 ubica ahí la empresa de Jorge Ponce) y Chimbote (UNS) para el docente y el equipo.")
    L.append("- **Contactos:** los de la empresa son **simulados**, con el dominio reservado `.example` y anexos internos, igual que el ejemplo "
             "de Retinopatía del docente; así el registro queda completo sin inventar datos reales. El docente y el equipo se contactan por el aula "
             "virtual del curso (no se publican correos personales). A los operarios se llega por la Supervisora de SST.")
    L.append("- **Influencia:** según las condiciones del ejemplo de Retinopatía, es la capacidad de afectar decisiones (Alta/Media/Baja). "
             "Se tomó la misma valoración de **poder** del [FGAP020 v1.0](../../../semana-06-producto-unidad-1/nuestras-entregas/Producto_Unidad_1_NewBit/"
             "Producto_Unidad_1_NewBit.md) (sección 4.3 del Producto de la Unidad I, con matriz de poder e interés) para no contradecirlo: "
             "**Alta** para quienes aprueban, aceptan o pueden cancelar (Sponsor, docente y PO; el Acta da la cancelación al Sponsor y al docente); "
             "**Media** para SST y TI, que validan y revisan pero no aprueban, y para los dos Developers (el SM incluido); **Baja** para la operadora, "
             "el supervisor de turno y los operarios. En BigFarma el SM figura con «Alta»; aquí se mantuvo lo ya entregado.")
    L.append("- **Áreas de mayor interés:** la fase del proyecto que más le importa a cada uno, con los nombres del "
             "[FGAP080](../FGAP080_Cronograma_Lanzamiento_NewBit/FGAP080_Cronograma_Lanzamiento_NewBit.md) (Inicio, Sprints 1–4, Lanzamiento 2, Cierre).")
    L.append("- **No se incluyó** a los autores del dataset (Önal y Dandıl, 2024): no participan ni conocen el proyecto. Su licencia CC BY 4.0 "
             "sí condiciona el trabajo, así que la atribución quedó como requisito en la fila de Luis Salazar (datos y modelos).")
    L.append("- **Instrucciones de llenado omitidas:** el ejemplo BigFarma las trae al final porque es la plantilla para los alumnos; "
             "en la entrega llenada no aportan nada y alargan el documento. Se conservó lo que importa de ellas: la escala de influencia y "
             "las «áreas de mayor interés» como fase del proyecto.")
    L.append("- **Cabecera de la tabla repetida** en cada página (en el ejemplo no se repite) para que la segunda hoja se lea sola.")
    L.append("")
    L.append("## Estado")
    L.append("Completo: sin campos «POR CONFIRMAR» en el Word ni en el PDF. Si el docente pide los correos institucionales reales del equipo "
             "o las instrucciones de llenado, se cambian en la lista `S` o en `build_docx` y se regenera.")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")


if __name__ == "__main__":
    build_docx(os.path.join(HERE, BASE + ".docx"))
    build_md(os.path.join(HERE, BASE + ".md"))
    print("OK:", BASE + ".docx", BASE + ".md")
