# -*- coding: utf-8 -*-
"""Plan de lanzamiento de NewBit (FGAP080), con las tareas detalladas de cada sprint.
Fuente única para el XML de MS Project, los Gantt (PNG), el Word y el .md.

Calendario del Acta (FGAP010 v2.0): Fase de Inicio 05–16/10 · 4 sprints de 2 semanas (19/10–11/12/2026)
· Cierre y sustentación 14–18/12/2026. Cada sprint: día 1 = Planificación y Estimación, días 2–9 =
Implementación (tareas por historia de usuario), día 10 = Revisión y Retrospectiva (modelo del docente).
Historias por sprint: backlog MoSCoW (semana 5). Horas por historia: burndown (5 h por punto de historia).
Sprint 2 = tareas T01–T14 del FGAP110/FGAP130 que no dependen de la SC-001, con las mismas fechas.
Responsables: Luis = datos y modelos; Anthony = web, integración y pruebas (FGAP030). Como máximo
una tarea por persona por día (2 Developers). Grupo D3, 09/11/2026.
"""
import datetime as dt

PROYECTO_COD = "PY-NB-001"
PROYECTO = ("PY-NB-001 – Sistema web con Visión Artificial para la detección de actos inseguros en áreas "
            "operativas de manufactura metalmecánica (NewBit)")
INICIO = dt.date(2026, 10, 5)

# El Acta fija sprints de 10 días hábiles sin descontar feriados (igual que el burndown).
FERIADOS_NO_DESCONTADOS = [(dt.date(2026, 10, 8), "Combate de Angamos (Fase de Inicio)"),
                           (dt.date(2026, 12, 8), "Inmaculada Concepción (Sprint 4)")]

L, A, LA = "Luis Salazar", "Anthony Lopez", "Luis Salazar; Anthony Lopez"
EQ = "Equipo Scrum"

# ---------------------------------------------------------------------------------------------
# Sprints: (nombre, tema, lunes de inicio, grupos). Cada grupo = (título del grupo, [tareas]).
# Tarea = (clave, nombre, responsable, día del sprint (1–10), duración en días, predecesoras (claves)).
SPRINTS = [
    ("Sprint 1", "Ingesta y detección (HU01–HU03)", dt.date(2026, 10, 19), [
        ("HU01 · Cargar video (.mp4/.avi) · 1 PH", [
            ("1.01", "Pantalla de carga con validación .mp4/.avi", A, 2, 1, []),
            ("1.02", "Extraer metadatos del video (duración, resolución, fps)", A, 3, 1, ["1.01"]),
        ]),
        ("HU02 · Extraer frames · 2 PH", [
            ("1.03", "Decodificar con OpenCV y muestrear a 5 fps", L, 2, 2, []),
            ("1.04", "Redimensionar y guardar los frames en orden", L, 4, 1, ["1.03"]),
            ("1.05", "Flujo web carga → extracción con estado del proceso", A, 4, 2, ["1.02"]),
        ]),
        ("HU03 · Detectar operarios (YOLOv8) · 4 PH", [
            ("1.06", "Integrar YOLOv8n: clase «person» por frame", L, 5, 2, ["1.04"]),
            ("1.07", "Dibujar recuadros y guardar detecciones por frame", A, 7, 1, ["1.06", "1.05"]),
            ("1.08", "Pruebas unitarias de frames y detección", L, 7, 1, ["1.06"]),
            ("1.09", "Prueba integrada: carga → frames → detección", A, 8, 1, ["1.07", "1.08"]),
            ("1.10", "Revisión de pares y documentación (DoD, FGAP070)", LA, 9, 1, ["1.09"]),
        ]),
    ]),
    ("Sprint 2", "Filtrado y clips (HU04, HU05, HU06, HU11)", dt.date(2026, 11, 2), [
        ("HU04 · Descartar frames vacíos · 2 PH", [
            ("T01", "Evidencia de reducción de frames con videos reales", A, 6, 1, ["T11"]),
        ]),
        ("HU05 · Agrupar en clips · 3 PH", [
            ("T02", "Ventana fija de N frames (N y paso configurables)", L, 3, 2, []),
            ("T03", "Tensor de entrada de ConvLSTM y pruebas", L, 5, 1, ["T02"]),
        ]),
        ("HU06 · Descartar clips cortos · 2 PH", [
            ("T04", "Umbral de duración mínima alineado con N", A, 5, 1, ["T02"]),
        ]),
        ("HU11 · Calibrar umbral de confianza · 1 PH", [
            ("T05", "Verificar la calibración con un video real", A, 1, 1, []),
        ]),
        ("Riesgos R-02 y R-03 (FGAP050)", [
            ("T14", "Entorno de entrenamiento en Colab con checkpoints", L, 1, 1, []),
            ("T11", "Pipeline espacial con 5 videos reales del dataset", L, 2, 1, []),
            ("T12", "Revisión de pares registrada (lista del FGAP070)", LA, 7, 2, ["T03", "T04"]),
            ("T13", "Prueba E2E con video real y suite completa", A, 9, 1, ["T12"]),
        ]),
    ]),
    ("Sprint 3", "Modelo temporal ConvLSTM (HU05, HU07, HU08)", dt.date(2026, 11, 16), [
        ("HU05 · Agrupar en clips (cierre del arrastre) · 3 PH", [
            ("3.01", "Tensor con la N elegida y pruebas unitarias", L, 2, 1, []),
            ("3.02", "Revisión de pares y cierre de HU05 con la DoD", A, 4, 1, ["3.01"]),
        ]),
        ("HU07 · Procesar con ConvLSTM · 5 PH", [
            ("3.03", "Arquitectura ConvLSTM base (config. y semilla fijas)", A, 2, 2, []),
            ("3.04", "Tensores del split oficial (entrenamiento y prueba)", L, 3, 1, ["3.01"]),
            ("3.05", "Spike: dos valores de N y registro de experimentos", L, 4, 1, ["3.03", "3.04"]),
            ("3.06", "Entrenamiento base en Colab con checkpoint por época", L, 5, 2, ["3.05"]),
            ("3.07", "Salida: vector de probabilidades por secuencia", A, 5, 2, ["3.03"]),
            ("3.08", "Inferencia en el split de prueba y métricas por clase", L, 7, 1, ["3.06", "3.07"]),
        ]),
        ("HU08 · Clasificar y tipificar la conducta · 3 PH", [
            ("3.09", "Clasificar seguro/inseguro y tipificar la conducta", A, 7, 2, ["3.07"]),
            ("3.10", "Umbral de decisión y matriz de confusión por conducta", L, 8, 1, ["3.08"]),
            ("3.11", "Prueba E2E video → clase y revisión de pares", LA, 9, 1, ["3.09", "3.10"]),
        ]),
    ]),
    ("Sprint 4", "Visualización y alertas (HU09, HU10, HU12)", dt.date(2026, 11, 30), [
        ("HU09 · Ver video con recuadro de riesgo · 4 PH", [
            ("4.01", "Servicio (API) con clase y confianza por clip", L, 2, 2, []),
            ("4.02", "Reproductor de video con las detecciones por frame", A, 2, 2, []),
            ("4.03", "Recuadro verde/rojo sincronizado con la clase de HU08", A, 4, 2, ["4.01", "4.02"]),
        ]),
        ("HU10 · Alerta de riesgo con evidencia · 2 PH", [
            ("4.04", "Regla de alerta: hora, clip y frame de evidencia", L, 4, 2, ["4.01"]),
            ("4.05", "Panel de alertas visual y sonoro; confirmar o descartar", A, 6, 2, ["4.03", "4.04"]),
        ]),
        ("HU12 · Ver log de tiempos de procesamiento · 2 PH", [
            ("4.06", "Registrar tiempos por etapa y % de frames descartados", L, 6, 1, ["4.04"]),
            ("4.07", "Vista del log de tiempos y métricas de aceleración", L, 7, 2, ["4.06"]),
            ("4.08", "Prueba de usabilidad con el flujo de la operadora", A, 8, 1, ["4.05"]),
            ("4.09", "Prueba E2E con videos del dataset y revisión de pares", LA, 9, 1, ["4.07", "4.08"]),
        ]),
    ]),
]

INICIO_TAREAS = [  # Fase de Inicio (Acta): (clave, nombre, responsable, comienzo, duración)
    ("0.01", "Justificación y épicas (EGAP015, FGAP040)", EQ, dt.date(2026, 10, 5), 5),
    ("0.02", "Backlog priorizado, estimación y DoD (MoSCoW, FGAP070)", EQ, dt.date(2026, 10, 12), 5),
]
LANZ2_TAREAS = [
    ("L2.1", "Despliegue de demostración y manual de usuario", LA, dt.date(2026, 12, 14), 2),
    ("L2.2", "Sustentación final ante el docente y el Sponsor", EQ, dt.date(2026, 12, 16), 1),
]
CIERRE_TAREAS = [
    ("C.1", "Retrospectiva del proyecto y lecciones aprendidas", EQ, dt.date(2026, 12, 17), 1),
    ("C.2", "Acta de cierre y repositorio final", EQ, dt.date(2026, 12, 18), 1),
]


# ---------------------------------------------------------------------------------------------
def habil_siguiente(d):
    while d.weekday() >= 5:
        d += dt.timedelta(days=1)
    return d


def sumar_habiles(d, n):
    """Último día de un bloque de n días hábiles que empieza en d (n >= 1)."""
    d = habil_siguiente(d)
    k = 1
    while k < n:
        d += dt.timedelta(days=1)
        if d.weekday() < 5:
            k += 1
    return d


def habiles(a, b):
    n, d = 0, a
    while d <= b:
        n += d.weekday() < 5
        d += dt.timedelta(days=1)
    return n


def dias_sprint(lunes):
    """Los 10 días hábiles de un sprint (índice 1..10)."""
    out, d = [], lunes
    while len(out) < 10:
        if d.weekday() < 5:
            out.append(d)
        d += dt.timedelta(days=1)
    return out


def calcular():
    """Lista de filas como en MS Project: id, nombre, nivel, tipo (resumen/tarea/hito), dur, ini, fin,
    pred (ids), resp y cini (fecha «no comenzar antes de», o None si la fijan las predecesoras)."""
    T, clave_id = [], {}

    def fila(nombre, nivel, tipo="tarea", ini=None, dur=None, resp="", preds=(), clave=None):
        t = dict(id=len(T) + 1, nombre=nombre, nivel=nivel, tipo=tipo, resp=resp, _preds=list(preds))
        if ini is not None:
            t["ini"] = ini
            t["dur"] = dur
            t["fin"] = ini if dur == 0 else sumar_habiles(ini, dur)
        T.append(t)
        if clave:
            clave_id[clave] = t["id"]
        return t

    fila("Inicio del Proyecto", 1, "resumen")
    for clave, nombre, resp, ini, dur in INICIO_TAREAS:
        fila(nombre, 2, ini=ini, dur=dur, resp=resp, clave=clave, preds=[INICIO_TAREAS[0][0]] if clave != "0.01" else [])
    previo = INICIO_TAREAS[-1][0]
    for n, (s, tema, lunes, grupos) in enumerate(SPRINTS, 1):
        D = dias_sprint(lunes)
        fila("%s · %s" % (s, tema), 1, "resumen")
        fila("Planificación y Estimación del Sprint", 2, ini=D[0], dur=1, resp=EQ, preds=[previo], clave="P%d" % n)
        fila("Implementación del Sprint", 2, "resumen")
        ultimas = []
        for titulo, tareas in grupos:
            fila(titulo, 3, "resumen")
            for clave, nombre, resp, dia, dur, preds in tareas:
                fila("%s · %s" % (clave, nombre), 4, ini=D[dia - 1], dur=dur, resp=resp, preds=preds, clave=clave)
                ultimas.append((D[dia - 1 + dur - 1], clave))
        fin_impl = max(f for f, _ in ultimas)
        fila("Revisión y Retrospectiva del Sprint", 2, ini=D[9], dur=1, resp=EQ,
             preds=[c for f, c in ultimas if f == fin_impl], clave="R%d" % n)
        previo = "R%d" % n
        if n == 2:
            fila("Lanzamiento 1 · Versión alfa: video → clips de operarios", 1, "hito", ini=D[9], dur=0,
                 preds=["R2"], clave="L1")
            previo = "L1"
    fila("Lanzamiento 2 · Versión final y sustentación", 1, "resumen")
    for k, (clave, nombre, resp, ini, dur) in enumerate(LANZ2_TAREAS):
        fila(nombre, 2, ini=ini, dur=dur, resp=resp, clave=clave, preds=[previo])
        previo = clave
    fila("Entrega final del prototipo", 2, "hito", ini=LANZ2_TAREAS[-1][3], dur=0, preds=[previo], clave="L2")
    previo = "L2"
    fila("Cierre del Proyecto", 1, "resumen")
    for clave, nombre, resp, ini, dur in CIERRE_TAREAS:
        fila(nombre, 2, ini=ini, dur=dur, resp=resp, clave=clave, preds=[previo])
        previo = clave

    # predecesoras → ids; restricción «no comenzar antes de» si las predecesoras no fijan el comienzo
    por_id = {t["id"]: t for t in T}
    for t in T:
        t["pred"] = [clave_id[c] for c in t.pop("_preds")]
    for t in T:
        if t["tipo"] == "resumen":
            continue
        if t["pred"]:
            fin_pred = max(por_id[p]["fin"] for p in t["pred"])
            esperado = fin_pred if t["tipo"] == "hito" else habil_siguiente(fin_pred + dt.timedelta(days=1))
            t["cini"] = None if esperado == t["ini"] else t["ini"]
        else:
            t["cini"] = t["ini"]
    # resúmenes
    for i, t in enumerate(T):
        if t["tipo"] != "resumen":
            continue
        hijas = []
        for u in T[i + 1:]:
            if u["nivel"] <= t["nivel"]:
                break
            if u["tipo"] != "resumen":
                hijas.append(u)
        t["ini"] = min(u["ini"] for u in hijas)
        t["fin"] = max(u["fin"] for u in hijas)
        t["dur"] = habiles(t["ini"], t["fin"])
        t["pred"], t["cini"] = [], None
    return T


def proyecto(T):
    ini = min(t["ini"] for t in T)
    fin = max(t["fin"] for t in T)
    return ini, fin, habiles(ini, fin)


DIAS = ["lun", "mar", "mié", "jue", "vie", "sáb", "dom"]


def f_ms(d):
    """Fecha al estilo de MS Project en español: 'lun 19/10/26'."""
    return "%s %s" % (DIAS[d.weekday()], d.strftime("%d/%m/%y"))


def f_dur(t):
    n = t["dur"]
    return "%d %s" % (n, "día" if n == 1 else "días")


def verificar():
    T = calcular()
    por_id = {t["id"]: t for t in T}
    D = dt.date
    top = {t["nombre"].split(" · ")[0]: t for t in T if t["nivel"] == 1}
    assert (top["Inicio del Proyecto"]["ini"], top["Inicio del Proyecto"]["fin"]) == (D(2026, 10, 5), D(2026, 10, 16))
    assert (top["Sprint 1"]["ini"], top["Sprint 1"]["fin"]) == (D(2026, 10, 19), D(2026, 10, 30))
    assert (top["Sprint 2"]["ini"], top["Sprint 2"]["fin"]) == (D(2026, 11, 2), D(2026, 11, 13))  # = FGAP130
    assert (top["Sprint 3"]["ini"], top["Sprint 3"]["fin"]) == (D(2026, 11, 16), D(2026, 11, 27))
    assert (top["Sprint 4"]["ini"], top["Sprint 4"]["fin"]) == (D(2026, 11, 30), D(2026, 12, 11))
    assert top["Lanzamiento 1"]["ini"] == D(2026, 11, 13)
    assert top["Cierre del Proyecto"]["fin"] == D(2026, 12, 18)
    for t in T:
        for p in t["pred"]:  # toda predecesora termina antes de que empiece la sucesora (fin → comienzo)
            q = por_id[p]
            assert q["fin"] < t["ini"] or (t["tipo"] == "hito" and q["fin"] <= t["ini"]), (q["nombre"], t["nombre"])
    # 2 Developers: como máximo una tarea por persona por día dentro de los sprints
    carga = {}
    for t in T:
        if t["nivel"] != 4:
            continue
        d = t["ini"]
        while d <= t["fin"]:
            if d.weekday() < 5:
                for p in t["resp"].split("; "):
                    assert (p, d) not in carga, ("doble tarea", p, d, t["nombre"], carga.get((p, d)))
                    carga[(p, d)] = t["nombre"]
            d += dt.timedelta(days=1)
    # las tareas de implementación caben en los días 2–9 (salvo el Sprint 2, que replica el FGAP130 y usa el día 1)
    for s, _, lunes, grupos in SPRINTS:
        D_ = dias_sprint(lunes)
        for _, tareas in grupos:
            for clave, nombre, resp, dia, dur, preds in tareas:
                assert dia + dur - 1 <= 9, (s, clave)
    return T


if __name__ == "__main__":
    T = verificar()
    for t in T:
        print("%3d %s%-62s %-8s %s  %s  pred=%-12s %s%s" % (
            t["id"], "  " * (t["nivel"] - 1), t["nombre"][:62], f_dur(t), f_ms(t["ini"]), f_ms(t["fin"]),
            ",".join(map(str, t["pred"])), t["resp"], "  📌" if t.get("cini") else ""))
    print(proyecto(T), len(T), "filas")


# ---------------------------------------------------------------------------------------------
# Datos del formato desarrollado (como el ejemplo FGAP080 del docente): parámetros de la liberación,
# resultado o hito verificable de cada fila y condiciones de uso del cronograma.
PARAMETROS = [
    ("Responsable de priorización", "Product Owner: Albert Chumacero"),
    ("Duración de cada sprint", "10 días hábiles (2 semanas)"),
    ("Ventana del proyecto", "05/10/2026 – 18/12/2026"),
    ("Alcance de las liberaciones", "Prototipo académico con videos del dataset público; sin instalación en planta"),
]

RESULTADOS = [  # (prefijo del nombre de la tarea, resultado o hito verificable); gana el primer prefijo que coincide
    ("Inicio del Proyecto", "Acta, roles, justificación, épicas y backlog aprobados."),
    ("Justificación y épicas", "EGAP015 y FGAP040 con 12 historias de usuario."),
    ("Backlog priorizado", "Backlog MoSCoW (31 PH), estimación y DoD (FGAP070)."),
    ("Sprint 1", "Carga de video, frames y detección de operarios."),
    ("Sprint 2", "Pipeline espacial con filtrado, clips y calibración."),
    ("Sprint 3", "ConvLSTM entrenado: clase segura/insegura con métricas."),
    ("Sprint 4", "Video con recuadro de riesgo, alertas y log de tiempos."),
    ("HU01", "Sube .mp4/.avi y muestra duración, resolución y fps."),
    ("HU02", "Frames a 5 fps guardados en orden."),
    ("HU03", "Recuadros de operarios (YOLOv8n) en cada frame."),
    ("HU04", "% de frames vacíos descartados, medido con videos reales."),
    ("HU05 · Agrupar en clips (cierre", "HU05 aceptada con la DoD (tensor con la N elegida)."),
    ("HU05", "Clips de N frames y tensor de entrada de ConvLSTM."),
    ("HU06", "Clips cortos descartados con el umbral alineado a N."),
    ("HU11", "Umbral de confianza ajustable y registrado."),
    ("Riesgos R-02", "Pipeline con videos reales, revisión de pares y E2E."),
    ("HU07", "Vector de probabilidades por secuencia en el split de prueba."),
    ("HU08", "Clase segura/insegura y tipo de conducta; matriz de confusión."),
    ("HU09", "Video con recuadro verde/rojo según la clase."),
    ("HU10", "Alerta con hora y evidencia; confirmar o descartar."),
    ("HU12", "Log de tiempos por etapa y ahorro de cómputo."),
    ("Planificación y Estimación", "Meta del sprint y tareas estimadas."),
    ("Implementación del Sprint", "Historias implementadas con pruebas y revisión de pares."),
    ("Revisión y Retrospectiva", "Demo al PO, historias aceptadas y acuerdos de mejora."),
    ("Lanzamiento 1", "Demo alfa: video → clips de operarios."),
    ("Lanzamiento 2", "Prototipo final, manual y sustentación."),
    ("Despliegue de demostración", "Demo desplegada y manual de usuario."),
    ("Sustentación final", "Presentación final ante el docente y el Sponsor."),
    ("Entrega final del prototipo", "Incremento final aceptado."),
    ("Cierre del Proyecto", "Lecciones aprendidas, acta de cierre y repositorio."),
    ("Retrospectiva del proyecto", "Lecciones aprendidas registradas."),
    ("Acta de cierre", "Acta de cierre y repositorio final publicados."),
]

CONDICIONES = [
    "Días hábiles de lunes a viernes. El Acta fija sprints de 2 semanas sin descontar los feriados del 08/10 (Fase de Inicio) "
    "y del 08/12 (Sprint 4); si el equipo no trabaja esos días, se marcan como no laborables y las fechas se recalculan.",
    "Lanzamiento 1: demostración alfa interna del pipeline espacial con videos del dataset público (Önal y Dandıl, 2024; CC BY 4.0). "
    "Lanzamiento 2: entrega académica final del prototipo. Ninguno autoriza su uso en una planta real sin validación ni permisos.",
    "Las tareas de los Sprints 3 y 4 son planificación: se revisan en la Planificación de cada sprint y en cada revisión, como pide Scrum.",
    "Si el Product Owner aprueba una solicitud de cambio (FGAP090), por ejemplo la SC-001 que adelanta HU07, se actualiza este cronograma con una nueva versión.",
]


def resultado(t):
    for prefijo, texto in RESULTADOS:
        if t["nombre"].startswith(prefijo):
            return texto
    return ""
