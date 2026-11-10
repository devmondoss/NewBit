# -*- coding: utf-8 -*-
"""Plan del Sprint 02 de NewBit: fuente única de nodos y tareas para la EDT (FGAP110) y el cronograma (FGAP130).
Horas = estimación del equipo (propuesta), no resultados. Grupo D3, 02/11/2026.
"""

PROYECTO = ("PY-NB-001 – Sistema web con Visión Artificial para la detección de actos inseguros en áreas "
            "operativas de manufactura metalmecánica (NewBit)")
SPRINT = "02"
SPRINT_FECHAS = "02 al 13 de noviembre de 2026; 10 días hábiles"
OBJETIVO = ("Cerrar con videos reales del dataset la etapa espacial del Sprint 2 (HU04, HU05, HU06 y HU11) y, si el "
            "Product Owner aprueba la SC-001, obtener la primera inferencia de ConvLSTM (HU07) sobre el split oficial de prueba.")

# Días hábiles del sprint (índice 1..10)
DIAS = [("L", "02/11"), ("M", "03/11"), ("M", "04/11"), ("J", "05/11"), ("V", "06/11"),
        ("L", "09/11"), ("M", "10/11"), ("M", "11/11"), ("J", "12/11"), ("V", "13/11")]

L = "Luis Salazar"
A = "Anthony Lopez"

# Nodos de nivel 2 de la EDT (orden del árbol, de izquierda a derecha)
NODOS = [
    {"id": "HU04", "tipo": "HU", "titulo": "Descartar frames vacíos", "pts": 2, "nota": "Construida el 17/10; falta evidencia con videos reales."},
    {"id": "HU05", "tipo": "HU", "titulo": "Agrupar en clips", "pts": 3, "nota": "Falta la ventana fija de N frames y el tensor de ConvLSTM."},
    {"id": "HU06", "tipo": "HU", "titulo": "Descartar clips cortos", "pts": 2, "nota": "Construida; se alinea con la ventana N."},
    {"id": "HU11", "tipo": "HU", "titulo": "Calibrar umbral (confidence)", "pts": 1, "nota": "Construida; falta evidencia con video real."},
    {"id": "SC-001", "tipo": "SC", "titulo": "Adelantar HU07 (ConvLSTM)", "pts": 5, "nota": "No aprobada por el PO (02/11/2026): HU07 queda en el Sprint 3."},
    {"id": "R-01", "tipo": "R", "titulo": "Ajuste del modelo temporal", "pts": None, "nota": "P×I 0,40 · Alto (FGAP050)."},
    {"id": "R-02", "tipo": "R", "titulo": "Implementación propia del pipeline", "pts": None, "nota": "P×I 0,20 · Moderado (FGAP050)."},
    {"id": "R-03", "tipo": "R", "titulo": "GPU y tiempo de entrenamiento", "pts": None, "nota": "P×I 0,20 · Moderado (FGAP050)."},
]

# Tareas: id, nodo, corto (árbol/Gantt), detalle (tabla), responsable, horas, día de inicio, duración (días), predecesoras
TAREAS = [
    ("T01", "HU04", "Evidencia de reducción con videos reales",
     "Registrar, con los 5 videos del dataset de T11, los frames entrantes, los conservados y el % de reducción (criterio 2 de HU04).", A, 1, 6, 1, ["T11"]),
    ("T02", "HU05", "Ventana fija de N frames",
     "Ventana fija de N frames consecutivos sobre las secuencias activas, con N y paso configurables (criterio 1 de HU05).", L, 5, 3, 2, []),
    ("T03", "HU05", "Tensor de entrada de ConvLSTM y pruebas",
     "Tensor de entrada de ConvLSTM (clips × N × alto × ancho × canales), normalizado y guardado con su índice; pruebas unitarias de la ventana y del tensor (criterio 2 de HU05).", L, 4, 5, 1, ["T02"]),
    ("T04", "HU06", "Umbral mínimo alineado con N",
     "Alinear el umbral de duración mínima con la ventana N (un solo parámetro de configuración) y verificar en el log el conteo de clips descartados.", A, 1, 5, 1, ["T02"]),
    ("T05", "HU11", "Verificar calibración con video real",
     "Verificar con un video del dataset el efecto de dos umbrales de confianza en los frames conservados y su registro en la bitácora de auditoría.", A, 1, 1, 1, []),
    ("T06", "SC-001", "Tensores del split oficial",
     "Generar con el pipeline (YOLOv8 → HU04 → HU05) los tensores del split oficial de entrenamiento y prueba de las dos conductas y sus casos seguros.", L, 3, 6, 1, ["T03"]),
    ("T07", "SC-001", "Arquitectura ConvLSTM base",
     "Implementar la arquitectura ConvLSTM base, con configuración versionada y semilla fija.", A, 6, 2, 3, []),
    ("T08", "SC-001", "Entrenamiento base e inferencia",
     "Entrenar la configuración elegida, guardar el checkpoint e inferir sobre el split oficial de prueba con un vector de probabilidades normalizado por secuencia (criterios 1 y 2 de HU07).", L, 6, 8, 2, ["T10", "T14"]),
    ("T09", "SC-001", "Prueba de integración HU05–HU07",
     "Prueba de integración HU05 → HU07 (forma del tensor, una salida por secuencia y probabilidades que suman 1) y revisión de pares del código de T08 "
     "(la hace Anthony antes de la revisión del sprint).", L, 1, 10, 1, ["T08"]),
    ("T10", "R-01", "Spike de N y registro de experimentos",
     "Spike: entrenamientos cortos con dos valores de N, registro versionado de cada configuración y del tiempo por época; se elige la configuración base. Mide los triggers de R-01 y R-03.", A, 3, 7, 1, ["T06", "T07"]),
    ("T11", "R-02", "Pipeline espacial con 5 videos reales",
     "Ejecutar carga, frames, YOLOv8 y descarte con 5 videos del dataset y revisar a mano la detección de operarios (evidencia de HU01–HU03 y trigger de R-02).", L, 3, 2, 1, []),
    ("T12", "R-02", "Revisión de pares registrada",
     "Revisión de pares registrada con la lista del FGAP070: Luis revisa el código de Anthony (10/11) y Anthony el de Luis (11/11); se cierran las observaciones críticas.", L + " y " + A, 4, 7, 2, ["T03", "T04", "T06", "T07"]),
    ("T13", "R-02", "Prueba E2E con video real",
     "Agregar un video real del dataset a la prueba E2E, corregir el conflicto del paquete `tests` en macOS y ejecutar la suite completa.", A, 3, 9, 1, ["T12"]),
    ("T14", "R-03", "Entorno de entrenamiento en Colab",
     "Preparar el entorno de entrenamiento en Google Colab: dependencias fijadas, datos montados y checkpoint por época para reanudar tras una desconexión.", L, 2, 1, 1, []),
]

HITO = ("Hito · Revisión del Sprint 02", 10, ["T09", "T13"])


def tareas_de(nodo):
    return [t for t in TAREAS if t[1] == nodo]


def horas_nodo(nodo):
    return sum(t[5] for t in tareas_de(nodo))


def fecha(dia):
    return DIAS[dia - 1][1]


def span_nodo(nodo):
    ts = tareas_de(nodo)
    ini = min(t[6] for t in ts)
    fin = max(t[6] + t[7] - 1 for t in ts)
    return ini, fin


def verificar():
    """Comprueba IDs correlativos, predecesoras y que no haya más de 2 tareas por día ni 2 tareas de una persona el mismo día."""
    ids = [t[0] for t in TAREAS]
    assert ids == ["T%02d" % i for i in range(1, len(TAREAS) + 1)], ids
    # orden correlativo por nodo
    orden = [n["id"] for n in NODOS]
    assert [orden.index(t[1]) for t in TAREAS] == sorted(orden.index(t[1]) for t in TAREAS)
    fin = {t[0]: t[6] + t[7] - 1 for t in TAREAS}
    for t in TAREAS:
        for p in t[8]:
            assert fin[p] < t[6], (t[0], p)
    for d in range(1, 11):
        activas = [t for t in TAREAS if t[6] <= d <= t[6] + t[7] - 1]
        assert len(activas) <= 2, (d, [t[0] for t in activas])
    # una tarea por persona y día (T12 la hace Luis el 1.er día y Anthony el 2.º)
    carga = {}
    for t in TAREAS:
        for d in range(t[6], t[6] + t[7]):
            if t[0] == "T12":
                who = [L] if d == t[6] else [A]
            else:
                who = [t[4]]
            for w in who:
                carga.setdefault((w, d), []).append(t[0])
    for k, v in carga.items():
        assert len(v) == 1, (k, v)
    return sum(t[5] for t in TAREAS)


if __name__ == "__main__":
    total = verificar()
    print("total h", total)
    for n in NODOS:
        print(n["id"], horas_nodo(n["id"]), span_nodo(n["id"]))
    for who in (L, A):
        h = sum(t[5] for t in TAREAS if t[4] == who) + (2 if True else 0)
        print(who, h)
