# -*- coding: utf-8 -*-
"""Genera FGAP090_Solicitud_de_Cambio_NewBit.docx y su .md (Grupo D3, NewBit).
Disposición del formato FGAP090 del docente y de su ejemplo resuelto: control de versiones, título,
tabla de proyecto y código, y una tabla continua con un encabezado gris por campo y una fila por línea.
Uso: python3 generar_fgap090.py <carpeta_salida>
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
for p in (HERE, os.path.join(HERE, "..", "..", "..", "semana-08-riesgo-y-planificacion-del-sprint",
                             "nuestras-entregas", "FGAP110_EDT_Sprint_02_NewBit")):
    sys.path.insert(0, os.path.abspath(p))
from docx_nb import Doc, md_from_markup  # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else "."
BASE = "FGAP090_Solicitud_de_Cambio_NewBit"
GRIS = "D9D9D9"
FC = "Arial"  # letra del contenido, como en el ejemplo resuelto

PROYECTO = ("PY-NB-001 | NewBit: Sistema web con Visión Artificial para la detección de actos inseguros "
            "en áreas operativas de manufactura metalmecánica")
CODIGO_SC = "SC-001"

VERSIONES = ["1.0", "Developers (Anthony Lopez y Luis Salazar)", "Anthony Lopez (SM)",
             "Albert Chumacero (PO) · {PC}", "02/11/2026", "Registro inicial de la solicitud de cambio"]

PROBLEMA = [
    "**Problema:** el plan de sprints del Product Backlog ya no refleja el avance real. Las HU del Sprint 2 (HU04, HU05, HU06 y HU11; 8 pts) están construidas "
    "desde el 17/10/2026, salvo la ventana fija de N frames y el tensor de HU05, mientras HU07 (ConvLSTM, 5 pts), la más incierta, sigue en el Sprint 3 (16–27/11).",
    "**Situación:** las 7 HU de los Sprints 1 y 2 (15 de 31 pts) se construyeron el 17/10/2026 y pasan 43/43 pruebas automatizadas (20/10). El PO no ha aceptado ninguna.",
    "**Pendientes reales:** HU05 sin ventana fija de N ni tensor de ConvLSTM; prueba integrada solo con un clip sintético (falta con los videos del dataset de "
    "Önal y Dandıl, 2024); sin registro de la revisión de pares.",
    "**Hallazgo de planificación (estimación):** sin el cambio, el Sprint 2 tiene 22 h de tareas frente a ≈ 56 h disponibles de los dos Developers.",
    "**Causas:** se estimó en puntos antes de que existiera código; la etapa espacial avanzó rápido al reutilizar OpenCV y Ultralytics YOLOv8; el backlog no se "
    "refinó tras el congelamiento del 17/10; ConvLSTM se planificó entero en un solo sprint, sin un experimento previo.",
    "**Consecuencias:** ≈ 34 h ociosas en el Sprint 2; toda la incertidumbre técnica concentrada en el Sprint 3; sin holgura si falla el primer entrenamiento "
    "(riesgo R-01); peligran el criterio «pipeline completo» del Acta y el cierre con las dos conductas.",
]

DESCRIPCION = [
    "**QUÉ:** adelantar la HU07 «Procesar el clip segmentado mediante ConvLSTM» (EP04, //Must//, 5 pts) del Sprint 3 al Sprint 2, sin cambiar su texto, sus "
    "criterios (inferencia sobre el split oficial de prueba; vector de probabilidades normalizado por secuencia) ni sus puntos.",
    "**Resto del backlog:** HU04, HU05, HU06 y HU11 siguen en el Sprint 2 (HU05 aporta el tensor de entrada de HU07); HU08 sigue en el Sprint 3; HU09, HU10 y HU12, "
    "en el Sprint 4. Se mantienen 12 HU y 31 pts.",
    "**QUIÉN:** solicitan los Developers (Luis Salazar y Anthony Lopez); facilita el Scrum Master (Anthony Lopez); evalúa y decide el Product Owner (Albert "
    "Chumacero); se informa al Sponsor (Ricardo Salcedo) y se consulta a SST (Mariana Torres), usuaria de HU07.",
    "**CÓMO:** el PO la revisa en la planificación del Sprint 2; si la aprueba, mueve HU07 al Sprint 2 en el Product Backlog y el Tablero Kanban, y el equipo la "
    "descompone en T06–T09 de la EDT (16 h), más las respuestas a R-01 y R-03 (T10 y T14; 5 h).",
    "**Regla de corte:** si el 10/11 se activa el trigger de R-01 o de R-03, el SM avisa al PO y HU07 vuelve al Product Backlog para el Sprint 3, sin afectar a "
    "HU04, HU05, HU06 y HU11.",
    "**CUÁNDO:** decisión el 02/11/2026, en la planificación del Sprint 2; ejecución del 03/11 al 13/11; aceptación o rechazo en la revisión del 13/11. No altera un sprint en curso.",
    "**DÓNDE:** Product Backlog y Tablero Kanban; EDT, cronograma y burndown del Sprint 2; código en `proyecto-newbit/ml/` y `tests/`; entrenamiento en Google Colab.",
]

RAZON = [
    "**Motivo:** priorizar por valor, riesgo y dependencias (Guía del SBOK): HU07 es //Must//, es la de mayor riesgo técnico y su dependencia (HU05) se completa en el mismo sprint.",
    "**Valor esperado:** una primera evidencia del modelo temporal en la revisión del Sprint 2 y holgura en el Sprint 3 para un segundo ciclo de ajuste y para HU08.",
    "**Alternativa A:** mantener el plan del Acta. Descartada: el Sprint 2 usaría ≈ 39 % de la capacidad y el riesgo seguiría concentrado en el Sprint 3.",
    "**Alternativa B:** adelantar HU07 y HU08 (8 pts). Descartada: supera la capacidad (43 h + 15–20 h > ≈ 56 h) y HU08 necesita un modelo ya entrenado.",
    "**Alternativa C:** adelantar la interfaz (HU09). Descartada: depende de HU08 y no reduce la incertidumbre principal.",
    "**Alternativa D:** solo un //spike// de ConvLSTM, sin historia. Se usa en parte, como respuesta a R-01 (T10), porque por sí solo no entrega un incremento aceptable.",
    "**Se elige** adelantar solo HU07: usa la capacidad libre en la historia de mayor riesgo, cabe en la capacidad (43 h de ≈ 56 h) y no cambia la fecha de liberación.",
    "**Sin el cambio:** ConvLSTM empieza el 16/11; si el primer entrenamiento falla, queda una sola semana efectiva antes del Sprint 4 y crece la probabilidad de cerrar con una sola conducta.",
]

CORTO = [
    "Sprint 2: compromiso de 8 a 13 pts; tareas de 22 h a 43 h (≈ 77 % de ≈ 56 h).",
    "Tareas nuevas: T06–T09 (HU07, 16 h), T10 (R-01, 3 h) y T14 (R-03, 2 h).",
    "Sin costo adicional: 21 h ya presupuestadas en el Acta (≈ S/ 762 valorizados); se adelanta la partida de GPU en la nube (S/ 80).",
    "Máximo 2 tareas en paralelo por día (2 Developers); más carga para Luis (26 h).",
    "Calidad: HU07 debe cumplir la DoD (T09: integración y revisión de pares de T08; T12).",
    "Se actualizan Product Backlog, Kanban, EDT, cronograma y burndown del Sprint 2.",
]
LARGO = [
    "El Sprint 3 queda con HU08 (3 pts) y holgura para ajustar ConvLSTM; su uso lo decide el PO ({PC}).",
    "Sin cambios en el Sprint 4, la liberación (14–18/12) ni la duración de los sprints.",
    "La línea base formal sigue en el Sprint 3, pero con un modelo ya probado de punta a punta.",
    "Baja la probabilidad de cerrar con alcance reducido (una sola conducta).",
    "La cadena HU05 → HU07 → HU08 → HU09/HU10 se destraba antes.",
    "Sin efecto en el nivel de servicio: prototipo académico, sin operación en planta.",
]

OTROS = [
    "**Programas/portafolios:** NewBit no pertenece a ninguno; no afecta a otros proyectos del curso.",
    "**Operaciones del equipo:** el uso de GPU en Colab empieza dos semanas antes; tensores y checkpoints ocupan disco (riesgo del Acta: 30–50 GB) y quedan fuera de git.",
    "**Repositorio:** módulo nuevo del modelo temporal en `ml/` y sus pruebas en `tests/`; la suite debe seguir pasando completa.",
    "**Dependencias:** HU07 usa el tensor de HU05 (T03) y los videos verificados en T11.",
    "**Gestión del curso:** se actualizan la EDT, el cronograma y el burndown del Sprint 2.",
]

EXTRA = [
    "**Usuarios** (caso académico: SST, Mariana Torres; monitoreo, Lucía Ramos): ven antes una primera salida del modelo (probabilidades por secuencia), sin métricas ni alertas.",
    "**Clientes / Sponsor** (Ricardo Salcedo): sin cambios en alcance, costo ni fecha de liberación.",
    "**Proveedores:** Google Colab (cuotas y disponibilidad de GPU); las bibliotecas abiertas no cambian.",
    "**Dataset** (Mendeley Data; Önal y Dandıl, 2024; CC BY 4.0): se mantiene la atribución y el split oficial, sin modificar el conjunto de prueba.",
    "**Gobierno / normativa:** sin cambios; sin reconocimiento facial; NewBit no certifica SST (Ley 29783).",
    "**Mercado:** sin efecto (prototipo académico).",
]

OBSERVACIONES = [
    "**Estimación:** HU07 mantiene 5 pts; 16 h de tareas (T06–T09) y 5 h de respuesta a riesgos (T10 y T14). Son estimaciones del equipo, no resultados.",
    "**Product Backlog impactado:** solo HU07 cambia de sprint (3 → 2). Puntos por sprint: S1 7 · S2 8 → 13 · S3 8 → 3 · S4 8 (total 31).",
    "**Solicitud ≠ cambio aprobado:** hasta la decisión del PO, HU07 sigue en el Sprint 3. Si se rechaza, T06–T10 y T14 salen del Sprint 2 (quedan 22 h).",
    "**HU01–HU03:** construidas y sin aceptar (no hay acta de la revisión del Sprint 1); su cierre depende de T11 y T12 (R-02). Presentación en la revisión del Sprint 2: {PC}.",
    "**Numeración:** HU según el Product Backlog (FGAP040); la tabla del README del proyecto usa otra y falta alinearla.",
    "**Supuestos:** dataset completo descargado ({PC}) y acceso a GPU en Colab ({PC}). Riesgos relacionados: R-01, R-02 y R-03 (FGAP050).",
]

REVISION = [
    ["Fecha de revisión", "02/11/2026, en la planificación del Sprint 2 ({PC})"],
    ["Efectuada por", "Albert Sebastian Chumacero Chávarry, Product Owner"],
    ["Resultados de revisión (aprobada/rechazada)", "**Propuesta del equipo: APROBAR e incorporar HU07 al Sprint 2.** Decisión del PO: {PC}."],
    ["Responsable de aplicar/informar", "Aplican Luis Salazar (tensores, entrenamiento e inferencia) y Anthony Lopez (arquitectura y pruebas); el PO reordena el Product Backlog; informa Anthony Lopez (SM)."],
    ["Observaciones especiales", "Condición propuesta: regla de corte del 10/11; los criterios de aceptación de HU07 no cambian."],
]


def build_docx(path):
    d = Doc(landscape=False, margins_cm=(2.3, 2.5, 2.0, 2.5), font=FC, size=16,
            header=[("FGAP090 - Solicitud de Cambio", {"size": 16, "align": "right", "border_bottom": "808080", "after": 0, "font": "Verdana"})],
            footer=[("NewBit (PY-NB-001) · Grupo D3 · Ingeniería de Software II · UNS", {"size": 13, "color": "808080", "align": "center"})],
            title="FGAP090 Solicitud de Cambio SC-001 – NewBit", subject="Solicitud de cambio del Grupo D3")
    V = "Verdana"
    rows = [[{"text": "**CONTROL DE VERSIONES**", "span": 6, "fill": GRIS, "align": "center", "size": 16, "font": V}],
            [{"text": "**//%s//**" % h, "fill": GRIS, "align": "center", "size": 15, "font": V} for h in
             ["Versión", "Hecho por", "Revisado por", "Aprobado por", "Fecha", "Motivo"]],
            [{"text": c, "size": 14} for c in VERSIONES]]
    d.table(rows, widths_rel=[0.9, 2.0, 1.4, 1.8, 1.2, 2.3], border="000000", sz=6, cell_margin=50)
    d.p("SOLICITUD DE CAMBIO", size=36, i=True, align="center", before=240, after=200, font=V, shadow=True)
    rows = [[{"text": "**Código y Nombre del Proyecto**", "fill": GRIS, "align": "center", "smallcaps": True, "font": V},
             {"text": "**Código de la Solicitud de Cambio**", "fill": GRIS, "align": "center", "smallcaps": True, "font": V}],
            [{"text": "**%s**" % PROYECTO}, {"text": "**%s**" % CODIGO_SC}]]
    d.table(rows, widths_rel=[2.75, 1.25], border="000000", sz=6, cell_margin=50)
    d.spacer(8)

    # Tabla continua: 3 columnas (rótulo de la revisión | resto de la mitad izquierda | mitad derecha)
    W = [4.5, 3.5, 8.0]

    def cab(titulo, instruccion=""):
        txt = "**%s**" % titulo + ((" //%s//" % instruccion) if instruccion else "")
        return [{"text": txt, "span": 3, "fill": GRIS, "smallcaps": True, "size": 16, "font": V, "keep_next": True}]

    def lineas(items):
        return [[{"text": t, "span": 3}] for t in items]

    rows = []
    rows.append(cab("Definición del Problema o Situación Actual:",
                    "Defina y acote el problema que se va a resolver, distinguiendo el problema de sus causas y de sus consecuencias."))
    rows += lineas(PROBLEMA)
    rows.append(cab("Descripción detallada del Cambio Solicitado:",
                    "Especifique con claridad el cambio solicitado, precisando el qué, quién, cómo, cuándo y dónde."))
    rows += lineas(DESCRIPCION)
    grupos = [rows]
    rows = []
    rows.append(cab("Razón por la que se solicita el cambio:",
                    "Especifique con claridad por qué motivos o razones solicita el cambio, por qué motivos elige este curso de acción y no otro alternativo, y qué sucedería si el cambio no se realiza."))
    rows += lineas(RAZON)
    rows.append(cab("Efectos en el Proyecto:",
                    "Definir el efecto del cambio solicitado a corto o largo plazo en el proyecto, sus entregables, sus productos, el nivel de servicio, la calidad, etc."))
    rows.append([{"text": "**//En el corto plazo//**", "span": 2, "smallcaps": True, "font": V, "size": 15, "keep_next": True},
                 {"text": "**//En el largo plazo//**", "smallcaps": True, "font": V, "size": 15, "keep_next": True}])
    for k in range(max(len(CORTO), len(LARGO))):
        rows.append([{"text": CORTO[k] if k < len(CORTO) else "", "span": 2}, {"text": LARGO[k] if k < len(LARGO) else ""}])
    rows.append(cab("Efectos en otros proyectos, programas, portafolios u operaciones"))
    rows += lineas(OTROS)
    grupos.append(rows)
    rows = []
    rows.append(cab("Efectos extra empresariales en clientes, mercados, proveedores, gobierno, etc."))
    rows += lineas(EXTRA)
    rows.append(cab("Observaciones y Comentarios adicionales"))
    rows += lineas(OBSERVACIONES)
    rows.append(cab("Revisión de la Solicitud de Cambios"))
    for k, v in REVISION:
        rows.append([{"text": "//%s//" % k, "smallcaps": True, "font": V, "size": 15},
                     {"text": v, "span": 2}])
    grupos.append(rows)
    # Una tabla por página, para que ningún encabezado gris quede separado de sus filas
    for k, g in enumerate(grupos):
        if k:
            d.page_break()
        d.table(g, widths_cm=W, border="000000", sz=4, cell_margin=34, keep_rows=True)
    d.save(path)


def build_md(path):
    def lst(items):
        return ["- " + md_from_markup(t) for t in items]
    L = []
    L.append("# FGAP090 – Solicitud de Cambio: NewBit (SC-001, adelantar HU07 al Sprint 2)")
    L.append("")
    L.append("- **Archivos para entregar** (esta carpeta): `%s.docx` (editable) y `%s.pdf`." % (BASE, BASE))
    L.append("- **Formato:** FGAP090 del docente ([formato en blanco](../../material-del-profe/solicitud-de-cambio-fgap090-formato/solicitud-de-cambio-fgap090-formato.md)), "
             "con la disposición de su [ejemplo resuelto](../../material-del-profe/solicitud-de-cambio-fgap090-ejemplo/solicitud-de-cambio-fgap090-ejemplo.md): "
             "los mismos campos, en el mismo orden, con una línea por fila.")
    L.append("- **Generador:** `generar_fgap090.py` (usa `docx_nb.py`, que está en la carpeta del FGAP110 de la semana 8). El PDF se exportó con Pages: Word no acepta «guardar como» por AppleScript en esta Mac.")
    L.append("- **Fecha:** 02/11/2026 (el formato se pidió en la semana 7) · **Versión:** 1.0 (Grupo D3).")
    L.append("- **Estado:** propuesta del equipo. **La decisión del Product Owner está POR CONFIRMAR.**")
    L.append("- **Trazabilidad:** el cambio es el nodo SC-001 de la [EDT del Sprint 2 (FGAP110)](../../../semana-08-riesgo-y-planificacion-del-sprint/nuestras-entregas/FGAP110_EDT_Sprint_02_NewBit/FGAP110_EDT_Sprint_02_NewBit.md) "
             "y del [cronograma (FGAP130)](../../../semana-08-riesgo-y-planificacion-del-sprint/nuestras-entregas/FGAP130_Cronograma_Sprint_02_NewBit/FGAP130_Cronograma_Sprint_02_NewBit.md); "
             "sus riesgos están en el [FGAP050](../../../semana-08-riesgo-y-planificacion-del-sprint/nuestras-entregas/FGAP050_Riesgo_del_Proyecto_NewBit/FGAP050_Riesgo_del_Proyecto_NewBit.md).")
    L.append("")
    L.append("## Control de versiones")
    L.append("| Versión | Hecho por | Revisado por | Aprobado por | Fecha | Motivo |")
    L.append("|---|---|---|---|---|---|")
    L.append("| " + " | ".join(md_from_markup(c) for c in VERSIONES) + " |")
    L.append("")
    L.append("## Solicitud de cambio")
    L.append("| Código y nombre del proyecto | Código de la solicitud de cambio |")
    L.append("|---|---|")
    L.append("| %s | **%s** |" % (PROYECTO, CODIGO_SC))
    L.append("")
    L.append("### Definición del problema o situación actual")
    L += lst(PROBLEMA)
    L.append("")
    L.append("### Descripción detallada del cambio solicitado")
    L += lst(DESCRIPCION)
    L.append("")
    L.append("### Razón por la que se solicita el cambio")
    L += lst(RAZON)
    L.append("")
    L.append("### Efectos en el proyecto")
    L.append("| En el corto plazo | En el largo plazo |")
    L.append("|---|---|")
    for k in range(max(len(CORTO), len(LARGO))):
        L.append("| %s | %s |" % (md_from_markup(CORTO[k]) if k < len(CORTO) else "", md_from_markup(LARGO[k]) if k < len(LARGO) else ""))
    L.append("")
    L.append("### Efectos en otros proyectos, programas, portafolios u operaciones")
    L += lst(OTROS)
    L.append("")
    L.append("### Efectos extra empresariales en clientes, mercados, proveedores, gobierno, etc.")
    L += lst(EXTRA)
    L.append("")
    L.append("### Observaciones y comentarios adicionales")
    L += lst(OBSERVACIONES)
    L.append("")
    L.append("### Revisión de la solicitud de cambios")
    L.append("| Campo | Contenido |")
    L.append("|---|---|")
    for k, v in REVISION:
        L.append("| %s | %s |" % (k, md_from_markup(v)))
    L.append("")
    L.append("## Notas de trabajo (no van en el formato)")
    L.append("")
    L.append("**Product Backlog impactado (detalle).** Fuente: FGAP040 y priorización MoSCoW + 100 puntos.")
    L.append("")
    L.append("| HU | Historia | Pts | Sprint antes | Sprint después |")
    L.append("|---|---|:-:|:-:|:-:|")
    for r in [("HU01", "Cargar video", 1, 1, 1), ("HU02", "Extraer frames", 2, 1, 1), ("HU03", "Detectar operarios (YOLOv8)", 4, 1, 1),
              ("HU04", "Descartar frames vacíos", 2, 2, 2), ("HU05", "Agrupar en clips", 3, 2, 2), ("HU06", "Descartar clips cortos", 2, 2, 2),
              ("HU11", "Calibrar umbral", 1, 2, 2), ("HU07", "Procesar con ConvLSTM", 5, 3, "**2**"), ("HU08", "Clasificar y tipificar", 3, 3, 3),
              ("HU09", "Ver video con recuadro", 4, 4, 4), ("HU10", "Alerta de riesgo", 2, 4, 4), ("HU12", "Ver log de tiempos", 2, 4, 4)]:
        L.append("| %s | %s | %s | %s | %s |" % r)
    L.append("")
    L.append("**Cómo cubre la plantilla de cotejo del docente.**")
    L.append("")
    L.append("| Criterio (peso) | Dónde está |")
    L.append("|---|---|")
    L.append("| Claridad del cambio (20 %) | QUÉ, QUIÉN, CÓMO, CUÁNDO y DÓNDE; solicitante (Developers) y decisor (PO) explícitos; alcance limitado a HU07 sin cambiar sus criterios |")
    L.append("| Justificación / valor (20 %) | Motivo, valor esperado, alternativas A–D descartadas con su razón y qué pasa sin el cambio |")
    L.append("| Impactos (25 %) | Corto y largo plazo, horas y costo, dependencias (HU05 → HU07 → HU08), riesgos R-01 a R-03, proveedores y dataset |")
    L.append("| Tratamiento Scrum y roles (25 %) | Se decide en la planificación, sin tocar un sprint en curso; decide el PO; facilita e informa el SM; regla de corte; aceptación en la revisión con criterios y DoD |")
    L.append("| Presentación y trazabilidad (10 %) | Campos del FGAP090 en orden, Product Backlog impactado en Observaciones, vínculo con FGAP050, FGAP110 y FGAP130 |")
    L.append("")
    L.append("**Capacidad usada en las cifras (estimación):** ≈ 56 h por sprint para los dos Developers (Luis ≈ 4 h/día; Anthony ≈ 3,5 h/día menos 0,5 h/día de labores de SM; "
             "ceremonias ≈ 7 h por persona). Albert es PO y no desarrolla. Costo valorizado con las tarifas del Acta (Luis S/ 35/h, Anthony S/ 38/h).")
    L.append("")
    L.append("## POR CONFIRMAR")
    L.append("1. **Decisión del Product Owner** (Albert Chumacero) sobre SC-001 y su aprobación del documento.")
    L.append("2. **Fecha de la revisión:** se propone el 02/11/2026, en la planificación del Sprint 2.")
    L.append("3. **HU01–HU03:** si el PO las presenta para aceptación en la revisión del Sprint 2 (no hay acta de la revisión del Sprint 1).")
    L.append("4. **Uso de la holgura del Sprint 3:** lo decide el PO en el refinamiento.")
    L.append("5. **Dataset completo descargado** y **acceso a GPU en Colab**.")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    build_docx(os.path.join(OUT, BASE + ".docx"))
    build_md(os.path.join(OUT, BASE + ".md"))
    print("ok", OUT)
