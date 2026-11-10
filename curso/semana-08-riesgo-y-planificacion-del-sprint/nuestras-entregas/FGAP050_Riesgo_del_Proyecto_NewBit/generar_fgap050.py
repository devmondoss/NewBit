# -*- coding: utf-8 -*-
"""Genera FGAP050_Riesgo_del_Proyecto_NewBit.docx (v1.1) y su .md.

v1.1 (09/11/2026): registro de 9 riesgos (técnicos, de datos y de gestión) con criterios de escala,
matriz P × I, priorización vinculada al backlog, una ficha por riesgo con su respuesta (mitigación,
responsable, fecha, trigger y evidencia de control) y el guion de 3 minutos del riesgo más crítico.
Actividad calificada de la semana 8 (lámina 39 de la clase de riesgo en Scrum).

Uso: python3 generar_fgap050.py <carpeta_salida>
"""
import os
import sys

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
# docx_nb.py vive en la carpeta del FGAP110 (fuente única)
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "FGAP110_EDT_Sprint_02_NewBit")))
from docx_nb import Doc, md_from_markup  # noqa: E402

BASE = "FGAP050_Riesgo_del_Proyecto_NewBit"
ROJO = "8B1E2D"
GRIS = "E1E4E8"
GRIS2 = "F3F4F6"
ROSA = "F9E1E3"
BORDE = "9AA1AB"
COLOR_TIPO = {"Muy alto": "F2A7AE", "Alto": "F8CFA4", "Moderado": "FBEDAE", "Bajo": "D7EDCF", "Muy bajo": "EDF6E8"}

PROYECTO = ("PY-NB-001 – Sistema web con Visión Artificial para la detección de actos inseguros en áreas operativas "
            "de manufactura metalmecánica (NewBit)")
HECHO = "Developers (Anthony Lopez y Luis Salazar)"
REVISADO = "Anthony Lopez (Scrum Master)"
APROBADO = "Albert Chumacero (Product Owner)"
VERSIONES = [
    ["1.0", HECHO, REVISADO, APROBADO, "02/11/2026", "Registro de los riesgos prioritarios al inicio del Sprint 2"],
    ["1.1", HECHO, REVISADO, APROBADO, "09/11/2026",
     "Se amplía a 9 riesgos y se agrega priorización, respuesta y comunicación (actividad de la semana 8)"],
]
FECHA = "09/11/2026"

PROB = [("Muy improbable", 0.1), ("Relativamente probable", 0.3), ("Probable", 0.5), ("Muy probable", 0.7), ("Casi certeza", 0.9)]
IMP = [("Muy bajo", 0.05), ("Bajo", 0.10), ("Moderado", 0.20), ("Alto", 0.40), ("Muy alto", 0.80)]
TIPO = [("Muy alto", "Mayor a 0,50"), ("Alto", "Menor a 0,50"), ("Moderado", "Menor a 0,30"), ("Bajo", "Menor a 0,10"), ("Muy bajo", "Menor a 0,05")]

# Criterios explícitos de cada nivel, aplicados a NewBit (la escala numérica es la del formato del docente)
CRIT_P = [
    "No hay indicios en NewBit ni en proyectos parecidos.",
    "Pasa en proyectos parecidos, pero en NewBit la causa raíz no está presente todavía.",
    "La causa raíz está presente en NewBit, sin señales de que el riesgo ya empezó.",
    "La causa raíz está presente y ya hay una señal parcial en el proyecto.",
    "El trigger está a punto de cumplirse.",
]
CRIT_I = [
    "No afecta historias, fechas ni criterios del Acta.",
    "Retrabajo menor dentro de una tarea, sin mover fechas.",
    "Retrasa una tarea o una HU, pero el sprint se cumple.",
    "Una HU no cumple la DoD en su sprint (arrastre) o un criterio del Acta se cumple solo en parte.",
    "Pone en riesgo un entregable clave del Acta (pipeline completo, modelo con métricas) o el lanzamiento.",
]


def r4(v):
    return round(v + 1e-12, 4)


def tipo_de(pi):
    pi = r4(pi)
    if pi > 0.50:
        return "Muy alto"
    if pi >= 0.30:
        return "Alto"
    if pi >= 0.10:
        return "Moderado"
    if pi >= 0.05:
        return "Bajo"
    return "Muy bajo"


def num(v):
    v = r4(v)
    txt = "%.2f" % v if abs(v * 100 - round(v * 100)) < 1e-6 else "%.3f" % v
    return txt.replace(".", ",")


def pname(p):
    return [n for n, v in PROB if abs(v - p) < 1e-9][0]


def iname(i):
    return [n for n, v in IMP if abs(v - i) < 1e-9][0]


L = "Luis Salazar"
A = "Anthony Lopez"
PO = "Albert Chumacero"

# ---------------------------------------------------------------------------------------------
# Registro de riesgos. "ficha": True = tiene ficha completa del formato.
RIESGOS = [
    {
        "cod": "R-01", "hu": [7, 8, 9, 10], "nombre": "Ajuste del modelo temporal (ConvLSTM)", "cat": "Técnico", "p": 0.5, "i": 0.8, "ficha": True,
        "desc": "El modelo ConvLSTM de NewBit podría no aprender a distinguir las conductas de la primera versión (tránsito fuera de la vía peatonal y panel "
                "eléctrico abierto, con sus casos seguros) con la longitud de secuencia, las capas y los hiperparámetros iniciales, o su ajuste podría necesitar "
                "más ciclos de entrenamiento de los que caben en el Sprint 3 (16–27/11). Retrasaría HU07 y HU08 y comprometería el pipeline completo que exige el Acta.",
        "causa": "El equipo no ha entrenado antes un ConvLSTM y no tiene una línea base propia. La longitud de secuencia N depende de la ventana fija de HU05, que "
                 "al 09/11 no está implementada, y del submuestreo a 5 fps. Los datos vienen de una sola planta con dos cámaras y hay pocos ejemplos por clase "
                 "(13 videos de panel abierto en el split de prueba). El PO rechazó adelantar HU07 al Sprint 2 (SC-001, FGAP090): se entrena recién en el Sprint 3.",
        "trigger": "Al cerrar el //spike// de longitud de secuencia (tarea 3.05, 19/11/2026), ninguna de las dos configuraciones de N supera en F1 macro de "
                   "validación a la línea base trivial (clase mayoritaria), o la pérdida de validación no baja durante 5 épocas seguidas en el entrenamiento base "
                   "(3.06). Activa el plan B: en la inferencia de prueba (3.08, 24/11) una conducta insegura queda con F1 menor a 0,50.",
        "entregables": "**HU07** (Sprint 3) y **HU08** (Sprint 3); modelo ConvLSTM entrenado y evaluado con métricas por clase (entregable clave del Acta); "
                       "evaluación comparativa; **HU09** y **HU10**, que dependen de HU08; demostración del incremento.",
        "sustento": "**P = 0,50 (probable):** la causa raíz está presente (primer ConvLSTM del equipo, sin línea base), pero el dataset es público y el artículo "
                    "muestra que la tarea es abordable. **I = 0,80 (muy alto):** sin modelo temporal no hay pipeline completo ni métricas, criterios de aprobación del Acta.",
        "estrategia": "**Mitigar.** //Spike// con dos valores de N y registro versionado de cada configuración (semilla fija); entrenamiento base con checkpoint por "
                      "época; métricas por clase desde el primer entrenamiento. **Plan B del Acta:** si se activa el trigger del 24/11, el PO reduce el alcance a "
                      "una conducta y se entrega con su evaluación documentada, sin bajar la DoD.",
        "backlog": "**Sí (HU07, Sprint 3):** tareas 3.05 //spike// de N (19/11), 3.06 entrenamiento base en Colab (20–23/11) y 3.08 inferencia y métricas por "
                   "clase (24/11). Regla de corte del plan B registrada para la decisión del PO (24/11).",
        "resp": "Luis Salazar (Developer, datos y modelos). Dueño del riesgo: Albert Chumacero (PO).",
        "fecha": "19/11/2026 (//spike//) · 24/11/2026 (control final y decisión del plan B)",
        "evidencia": "Registro versionado de experimentos (configuración, semilla, N, F1 macro y pérdida por época); métricas por clase del 24/11; "
                     "acta de la decisión del PO si se aplica el plan B.",
        "resumen_accion": "3.05, 3.06 y 3.08 (HU07); regla de corte",
    },
    {
        "cod": "R-02", "hu": [1, 2, 3, 4, 5, 6, 7, 11], "nombre": "Implementación propia del pipeline completo", "cat": "Técnico", "p": 0.5, "i": 0.4, "ficha": True,
        "desc": "El pipeline propio de NewBit (carga, extracción de frames, detección, descarte de frames vacíos, agrupamiento y tensor) podría tener defectos no "
                "detectados, porque la prueba integrada solo se hizo con un clip sintético y no hay revisión de pares registrada. Al probarlo con videos reales del "
                "dataset, las historias construidas podrían no cumplir sus criterios o la Definición de Terminado, y HU07 recibiría secuencias mal formadas.",
        "causa": "El código de las 7 HU de los Sprints 1 y 2 se escribió en un día (17/10/2026). El clip de prueba (`tests/fixtures`) usa la foto de muestra `zidane.jpg` "
                 "de Ultralytics: muestra personas, no operarios, y no sirve como evidencia visual. No hay registro de la revisión de pares que exige el FGAP070. "
                 "En macOS, un paquete `tests` de terceros tapa `proyecto-newbit/tests` y la prueba E2E no corre con el comando del README.",
        "trigger": "La prueba integrada con un video real del dataset (T13, 12/11/2026) falla en algún paso; o, en la revisión manual de T11 (20 frames con "
                   "operario visible por video), más del 10 % queda sin caja «persona»; o al 11/11 la revisión de pares (T12) deja al menos una observación "
                   "crítica sin resolver.",
        "entregables": "Incremento de los Sprints 1 y 2 (**HU01–HU06** y **HU11**, 15 PH) y su aceptación por el PO; tensor de entrada de **HU07**; demostración en "
                       "la revisión del Sprint 2; criterio de aprobación del Acta «reproducibilidad técnica».",
        "sustento": "**P = 0,50 (probable):** nunca se probó con videos reales ni se revisó entre pares, aunque las 43 pruebas automatizadas pasan (20/10). "
                    "**I = 0,40 (alto):** obliga a retrabajo y puede dejar una HU sin cumplir la DoD en su sprint, pero no cambia el alcance.",
        "estrategia": "**Mitigar** (Acta: bibliotecas abiertas y revisión por pares). Probar el pipeline espacial con 5 videos reales y revisar a mano la detección; "
                      "revisión de pares cruzada con la lista del FGAP070; prueba E2E con un video real y corrección del conflicto del paquete `tests` en macOS.",
        "backlog": "**Sí (Sprint 2, nodo R-02 de la EDT):** T11 pipeline espacial con 5 videos reales (03/11), T12 revisión de pares registrada (10–11/11) y "
                   "T13 prueba E2E con video real (12/11). Cubren también el cierre de HU01–HU03.",
        "resp": "Anthony Lopez (Developer, integración y pruebas); T11 la ejecuta Luis Salazar.",
        "fecha": "12/11/2026 (T13) · control en la revisión del Sprint 2 (13/11/2026)",
        "evidencia": "Tabla de la revisión manual de T11 (frames con operario y cajas detectadas por video); registro de la revisión de pares con la lista "
                     "del FGAP070; salida de `pytest` con la suite completa y el video real.",
        "resumen_accion": "T11, T12 y T13 (Sprint 2)",
    },
    {
        "cod": "R-03", "hu": [7, 8, 12], "nombre": "GPU y tiempo de entrenamiento limitados", "cat": "Técnico", "p": 0.5, "i": 0.4, "ficha": True,
        "desc": "El entrenamiento de ConvLSTM podría no caber en el tiempo del sprint por falta de GPU propia o por las cuotas y desconexiones de Google Colab. "
                "Retrasaría HU07 y HU08 y reduciría el número de configuraciones que se pueden probar, lo que agrava R-01.",
        "causa": "La aplicación corre en CPU y el equipo no tiene GPU NVIDIA propia para entrenar: la Mac del Scrum Master no admite CUDA y no hay otra GPU "
                 "registrada en el proyecto, así que se entrena en Google Colab. El presupuesto de nube del Acta es acotado (S/ 80: 2 meses × S/ 40). "
                 "Los videos y los tensores tienen que subirse a la nube antes de entrenar.",
        "trigger": "En el //spike// (3.05, 19/11/2026), una época con el subconjunto de las dos conductas tarda más de 20 min (con eso caben unas 20 épocas "
                   "en una sesión), o se pierden 2 o más sesiones de Colab por cuota o desconexión en la misma semana.",
        "entregables": "**HU07** y **HU08**; modelo ConvLSTM entrenado; comparación de tiempos de procesamiento del Acta (**HU12**); cronograma del Sprint 3.",
        "sustento": "**P = 0,50 (probable):** depende de un servicio externo con cuotas y no hay GPU propia. **I = 0,40 (alto):** retrasa el modelo temporal "
                    "y puede dejar HU07 sin terminar en el Sprint 3, pero hay alternativas (bajar resolución o N, menos épocas).",
        "estrategia": "**Mitigar.** Entorno de entrenamiento en Colab con dependencias fijadas y checkpoint por época, para reanudar tras una desconexión; "
                      "medir el tiempo por época en el //spike//. **Plan B:** bajar la resolución de entrada o N y entrenar solo con las dos conductas de "
                      "la primera versión (Acta); si hace falta, usar el presupuesto de nube del Acta.",
        "backlog": "**Sí:** T14 entorno de entrenamiento en Colab (Sprint 2, 02/11) y, en HU07 (Sprint 3), medición del tiempo por época en 3.05 (19/11) y "
                   "checkpoint por época en 3.06 (20–23/11).",
        "resp": "Luis Salazar (Developer, datos y modelos).",
        "fecha": "19/11/2026 (medición del tiempo por época) · 23/11/2026 (fin del entrenamiento base)",
        "evidencia": "Cuaderno de Colab versionado con las dependencias fijadas; checkpoints por época en la carpeta privada del equipo; tiempo por época "
                     "en el registro de experimentos.",
        "resumen_accion": "T14 (Sprint 2); 3.05 y 3.06 (HU07)",
    },
    {
        "cod": "R-04", "hu": [5, 6, 7, 8], "nombre": "Desbalance de clases y etiquetas de los clips", "cat": "Datos", "p": 0.5, "i": 0.4, "ficha": True,
        "desc": "Las clases del dataset están desbalanceadas y sus etiquetas son por video. Al cortar cada video en ventanas de N frames (HU05) y descartar las "
                "cortas (HU06), algunas clases seguras podrían quedarse con muy pocos clips, y algunas ventanas heredarían una etiqueta que no muestran (clips con "
                "más de una conducta). El modelo podría responder casi siempre la conducta mayoritaria y las métricas por clase de HU08 no serían válidas.",
        "causa": "En el split oficial de entrenamiento hay 178 videos de tránsito fuera de la vía frente a 50 de tránsito seguro, y 129 de panel abierto frente a "
                 "19 de panel cerrado (6,8 a 1). Los clips de panel cerrado duran 4,6 s en promedio (mínimo 1 s), cerca del umbral mínimo de HU06. El dataset "
                 "etiqueta por video y su artículo advierte que algunos clips tienen más de una conducta. NewBit no reetiqueta frames a mano.",
        "trigger": "Al generar los clips del split oficial con la N elegida (3.04, 18/11/2026), una clase queda con menos de 15 clips de entrenamiento o la "
                   "razón entre la clase mayor y la menor de una misma conducta supera 10 a 1; o, en una muestra de 20 ventanas por clase, más del 20 % no "
                   "muestra la conducta de su etiqueta.",
        "entregables": "**HU05** (ventana y tensor), **HU06** (duración mínima), **HU07** (entrenamiento) y **HU08** (métricas por clase y matriz de confusión); "
                       "requisitos del Acta «split oficial de validación» y «métricas por clase».",
        "sustento": "**P = 0,50 (probable):** el desbalance ya está en el dataset (causa raíz presente), pero todavía no se sabe cuántos clips deja la ventana N. "
                    "**I = 0,40 (alto):** un modelo sesgado obliga a reentrenar y deja HU08 sin métricas válidas en su sprint.",
        "estrategia": "**Mitigar.** Contar los clips por clase y por split antes de entrenar; ponderar la pérdida por clase (o sobremuestrear la clase menor) "
                      "solo en entrenamiento, sin tocar el split de prueba; ventanas con solapamiento (paso menor que N) en los videos cortos; revisar a "
                      "mano 20 ventanas por clase; reportar F1 macro y por clase, no solo exactitud.",
        "backlog": "**Sí:** criterio de aceptación nuevo en **HU05** (conteo de clips por clase y split, tarea 3.04, 18/11); pesos por clase en 3.06 (**HU07**); "
                   "matriz de confusión y F1 por conducta en 3.10 (**HU08**, 25/11).",
        "resp": "Luis Salazar (Developer, datos y modelos).",
        "fecha": "18/11/2026 (conteo de clips) · 25/11/2026 (métricas por clase)",
        "evidencia": "Tabla de clips por clase y split en el registro de experimentos; muestra revisada de 20 ventanas por clase; matriz de confusión y F1 "
                     "por clase en el informe de HU08.",
        "resumen_accion": "Criterio nuevo en HU05 (3.04); 3.06 y 3.10",
    },
    {
        "cod": "R-05", "hu": [], "nombre": "Espacio en disco (30–50 GB entre videos, frames y checkpoints)", "cat": "Datos", "p": 0.3, "i": 0.2, "ficha": False,
        "sustento": "**P = 0,30:** los tensores y los checkpoints empiezan a generarse en el Sprint 3. **I = 0,20:** retrasa una tarea; se resuelve borrando "
                    "frames intermedios.",
        "trigger": "Quedan menos de 10 GB libres en el equipo que procesa los videos.",
        "estrategia": "**Aceptar y vigilar.** Checkpoints, tensores y medios fuera de git (`.gitignore` ya los excluye); borrar los frames intermedios después "
                      "de generar los tensores.",
        "backlog": "No (riesgo bajo).",
        "resp": "Luis Salazar.",
        "fecha": "En cada revisión de sprint (13/11 y 27/11/2026)",
        "evidencia": "Espacio libre anotado en la revisión del sprint.",
        "resumen_accion": "No: se acepta y se vigila",
    },
    {
        "cod": "R-06", "hu": [3, 4, 8, 11], "nombre": "Iluminación, oclusiones y cambio de dominio", "cat": "Datos", "p": 0.3, "i": 0.4, "ficha": True,
        "desc": "YOLOv8n preentrenado podría no detectar a operarios con poca luz, a contraluz, lejos de la cámara o tapados por máquinas. HU04 descartaría esos "
                "frames como vacíos y se perdería justo el tramo con la conducta (falso negativo). Además, el modelo se entrena con una sola planta y dos "
                "cámaras: con otra cámara u otra iluminación podría rendir peor.",
        "causa": "El detector no se reentrenó con imágenes del taller (no hay anotaciones propias). El dataset viene de una sola fábrica con dos cámaras fijas "
                 "(1920 × 1080, 24 fps) y los frames se reducen a 640 × 640, lo que achica a los operarios lejanos. Hay un solo umbral de confianza para "
                 "todas las cámaras.",
        "trigger": "En la evidencia con 5 videos reales (T01, 09/11/2026), un video pierde más del 20 % de los frames con operario visible; o, en las métricas "
                   "de prueba (3.08, 24/11), el recall de la clase insegura en una cámara es 0,15 o más menor que en la otra.",
        "entregables": "**HU03** (detección), **HU04** (descarte de frames), **HU11** (calibración del umbral) y **HU08** (métricas); criterio del Acta "
                       "«reducción de frames ≥ 60 %» sin perder la conducta.",
        "sustento": "**P = 0,30 (relativamente probable):** pasa en proyectos parecidos y el dataset declara pocas cámaras, pero las cámaras de prueba son "
                    "las mismas del entrenamiento. **I = 0,40 (alto):** los falsos negativos atacan el valor central del producto y obligan a recalibrar.",
        "estrategia": "**Mitigar con trabajo ya planificado.** Calibrar el umbral de confianza por cámara con HU11; medir en T01 los frames con operario "
                      "visible que se descartan; reportar las métricas por cámara. **Aceptar** la generalización a otras plantas: está fuera del alcance "
                      "de esta versión y se declara en el informe.",
        "backlog": "**Dentro de tareas ya planificadas:** T05 y T01 (Sprint 2) y desglose por cámara en 3.08 (HU07, 24/11). No se crea una HU nueva.",
        "resp": "Luis Salazar (Developer, datos y modelos); la calibración de T05 y T01 la ejecuta Anthony Lopez.",
        "fecha": "09/11/2026 (T01) · 24/11/2026 (métricas por cámara)",
        "evidencia": "Tabla de frames con operario visible frente a frames conservados por video (T01); bitácora de calibración de HU11 con el umbral de "
                     "cada cámara; métricas por cámara en el informe.",
        "resumen_accion": "No es ítem nuevo: T05, T01 y 3.08",
    },
    {
        "cod": "R-07", "hu": [5, 7, 8, 9, 10, 12], "nombre": "Capacidad del equipo: Scrum Master con doble rol", "cat": "Gestión", "p": 0.7, "i": 0.2, "ficha": True,
        "desc": "El equipo tiene tres personas y solo dos desarrollan. Anthony es Scrum Master y Developer: si sus tareas de desarrollo se atrasan, podría "
                "descuidar la facilitación (Daily, impedimentos, registro de riesgos), o al revés. El Sprint 3 concentra el cierre de HU05, HU07 y HU08, el "
                "tramo más incierto del proyecto.",
        "causa": "Capacidad neta por sprint de 49,5 h: Luis 28,5 h y Anthony 21 h, después de 7,5 h de Scrum Master y 6,5 h de eventos. El plan del Sprint 3 "
                 "usa 46 h (93 %) y compromete 11 PH frente a una velocidad objetivo de 8 PH. El Product Owner no desarrolla.",
        "trigger": "En la Daily, una tarea del Sprint 3 pasa 2 días hábiles sin avance, o la curva real del burndown queda 2 días seguidos más de 20 % por "
                   "encima de la ideal; o en una semana no se registran las Daily o la actualización de este registro.",
        "entregables": "Sprint 3 (**HU05**, **HU07** y **HU08**) y su revisión del 27/11; Sprint 4 (**HU09**, **HU10** y **HU12**); burndown y FGAP050 al día.",
        "sustento": "**P = 0,70 (muy probable):** la causa raíz está presente y ya hay una señal: el Sprint 3 está planificado al 93 % de la capacidad. "
                    "**I = 0,20 (moderado):** retrasa tareas, pero el PO puede reordenar el alcance del sprint sin tocar el Acta.",
        "estrategia": "**Mitigar.** //Time-boxing// del trabajo de Scrum Master (7,5 h por sprint, ya descontadas); reparto fijo: Luis lidera datos y modelos, "
                      "Anthony web, integración y pruebas; en la planificación del Sprint 3 el PO ordena el trabajo (cierre de HU05 y HU07 primero) y acuerda "
                      "un alcance mínimo de HU08; se recalcula la capacidad con la velocidad real del Sprint 2.",
        "backlog": "**Dentro de los eventos Scrum:** orden del Sprint Backlog y alcance mínimo de HU08 en la planificación del Sprint 3 (16/11). No se crea una HU nueva.",
        "resp": "Anthony Lopez (Scrum Master).",
        "fecha": "16/11/2026 (planificación del Sprint 3) y en cada Daily",
        "evidencia": "Burndown actualizado cada día; horas por persona en el Scrumboard; acta de la retrospectiva del Sprint 2 (13/11) con la velocidad real.",
        "resumen_accion": "No es ítem nuevo: planificación del Sprint 3",
    },
    {
        "cod": "R-08", "hu": [1, 2, 3, 9, 10], "nombre": "Privacidad de los videos de operarios", "cat": "Datos", "p": 0.3, "i": 0.8, "ficha": True,
        "desc": "Los videos que procesa NewBit muestran a operarios identificables (rostro, ropa, puesto). Los videos subidos, los frames, los clips y las "
                "capturas de evidencia de las alertas (HU10) podrían quedar expuestos: en el repositorio, en carpetas compartidas para entrenar en la nube "
                "o en la demostración, si la aplicación se publica sin control de acceso. Sería un tratamiento indebido de datos personales y rompería el "
                "requisito de privacidad por diseño del Acta.",
        "causa": "La aplicación no tiene inicio de sesión ni roles: hoy está protegida solo porque corre en 127.0.0.1. Los datos de entrenamiento se suben a "
                 "Google Drive para Colab (R-03). HU10 guardará capturas de evidencia y no tiene un criterio de privacidad. Hay borrado de videos, pero no "
                 "plazo de retención. En una planta real, la imagen de un trabajador es un dato personal (Ley N.° 29733, Perú).",
        "trigger": "`git ls-files` muestra un video, frame o clip fuera de `tests/fixtures`; una carpeta de Drive del proyecto tiene acceso «cualquier persona "
                   "con el enlace»; o, al preparar la demostración (14/12/2026), una petición desde otra máquina a `/api/videos/{id}/stream` responde "
                   "HTTP 200 sin sesión.",
        "entregables": "**HU01–HU03** (carga y almacenamiento), **HU09** (reproducción), **HU10** (capturas de evidencia), despliegue de demostración y manual; "
                       "requisitos del Acta «sin reconocimiento facial» y privacidad por diseño; atribución CC BY 4.0 del dataset.",
        "sustento": "**P = 0,30 (relativamente probable):** pasa en proyectos parecidos; en NewBit los medios ya están fuera de git y la aplicación es local. "
                    "**I = 0,80 (muy alto):** una fuga de imágenes de trabajadores detendría la demostración y rompería un requisito del Acta.",
        "estrategia": "**Mitigar y evitar.** Revisar `git ls-files` en cada revisión de pares (ítem nuevo de la DoD); compartir la carpeta de Drive solo con "
                      "los tres miembros; en HU10, guardar solo el recuadro, la hora y la clase, con los rostros difuminados; no publicar la aplicación fuera "
                      "de 127.0.0.1 sin autenticación; borrar videos y frames procesados en el cierre del proyecto (18/12).",
        "backlog": "**Sí:** criterio de aceptación nuevo en **HU10** (captura con rostros difuminados y datos mínimos, tarea 4.04, 03–04/12); tarea nueva del "
                   "Sprint 4: control de acceso de la demostración antes del despliegue (14/12); ítem nuevo de la DoD (FGAP070).",
        "resp": "Anthony Lopez (Developer, web e integración).",
        "fecha": "13/11/2026 (primera verificación) · 04/12/2026 (HU10) · 14/12/2026 (demostración)",
        "evidencia": "Salida de `git ls-files` sin medios en el registro de la revisión de pares; captura de permisos de la carpeta de Drive; prueba de HU10 "
                     "con un rostro difuminado; prueba de acceso sin sesión con HTTP 401 antes de la demostración.",
        "resumen_accion": "Criterio nuevo en HU10 (4.04); tarea nueva de acceso; DoD",
    },
    {
        "cod": "R-09", "hu": [1, 2, 3, 4, 5, 6, 11], "nombre": "Decisiones y aceptación del Product Owner a destiempo", "cat": "Gestión", "p": 0.5, "i": 0.2, "ficha": True,
        "desc": "Las decisiones del Product Owner (aceptar historias, resolver solicitudes de cambio, recortar alcance) podrían llegar tarde. Si la revisión del "
                "Sprint 2 cierra sin aceptar formalmente las historias de los Sprints 1 y 2, el Sprint 3 empezaría sin saber qué está terminado, y el plan B "
                "de R-01 se decidiría cuando ya no hay margen.",
        "causa": "Al 09/11 no hay acta de la revisión del Sprint 1: HU01–HU03 están construidas pero sin aceptación formal. La decisión del PO sobre la SC-001 (02/11) "
                 "recién quedó escrita en el FGAP090 el 09/11. El PO no desarrolla y las decisiones se toman por mensajes, sin un registro.",
        "trigger": "Una decisión pedida al PO en la Daily o por mensaje pasa más de 2 días hábiles sin respuesta; o la revisión del Sprint 2 (13/11/2026) cierra "
                   "sin un acta con cada historia aceptada o rechazada.",
        "entregables": "Aceptación de **HU01–HU06** y **HU11** (15 PH); registro de las solicitudes de cambio (FGAP090); planificación del Sprint 3; plan B de R-01.",
        "sustento": "**P = 0,50 (probable):** la causa raíz está presente (aceptaciones sin acta). **I = 0,20 (moderado):** retrasa la planificación y la "
                    "aceptación, pero el PO puede resolver en la revisión sin cambiar el Acta.",
        "estrategia": "**Mitigar.** Acta de la revisión de cada sprint con aceptado o rechazado por historia; registro de decisiones del PO en el repositorio "
                      "(fecha, decisión, motivo); el Scrum Master pone las decisiones pendientes como primer punto de la Daily; el PO aprueba por adelantado "
                      "la regla de corte de R-01.",
        "backlog": "**Dentro de los eventos Scrum:** revisión del Sprint 2 (13/11) y planificación del Sprint 3 (16/11). No se crea una HU nueva.",
        "resp": "Albert Chumacero (Product Owner); el Scrum Master agenda y registra.",
        "fecha": "13/11/2026 (revisión del Sprint 2)",
        "evidencia": "Acta de la revisión del Sprint 2 con el estado de cada historia; registro de decisiones del PO con fecha (como la de la SC-001 en el FGAP090).",
        "resumen_accion": "No es ítem nuevo: revisión y planificación",
    },
]
# Historias de usuario del backlog (numeración del FGAP040) con su sprint y la respuesta que reciben
HISTORIAS = [
    (1, "Cargar video (.mp4/.avi)", "1", "Cierre con T11 y T12 (R-02) y aceptación formal el 13/11 (R-09); medios fuera de git (R-08)."),
    (2, "Extraer frames", "1", "Cierre con T11 y T12 (R-02) y aceptación formal el 13/11 (R-09)."),
    (3, "Detectar operarios (YOLOv8)", "1", "Revisión manual de la detección en T11 (R-02, R-06); aceptación formal el 13/11 (R-09)."),
    (4, "Descartar frames vacíos", "2", "Evidencia con videos reales en T01: frames con operario que se pierden (R-02, R-06)."),
    (5, "Agrupar en clips", "2 (cierre en 3)", "Criterio de aceptación nuevo: conteo de clips por clase y split, tarea 3.04 (R-04)."),
    (6, "Descartar clips cortos", "2", "Duración mínima alineada con N (T04) sin vaciar la clase menor; ventanas con solapamiento (R-04)."),
    (7, "Procesar con ConvLSTM", "3", "3.05 //spike// de N, 3.06 entrenamiento con checkpoint y pesos por clase, 3.08 métricas por clase y por cámara (R-01, R-03, R-04, R-06)."),
    (8, "Clasificar y tipificar la conducta", "3", "3.10 matriz de confusión y F1 por conducta (R-04); alcance mínimo acordado (R-07); plan B a una conducta (R-01)."),
    (9, "Ver video con recuadro de riesgo", "4", "Depende de HU08 (R-01); reproducción solo en 127.0.0.1 o con autenticación (R-08)."),
    (10, "Alerta de riesgo con evidencia", "4", "Criterio de aceptación nuevo: captura con rostros difuminados y datos mínimos, tarea 4.04 (R-08)."),
    (11, "Calibrar umbral de confianza", "2", "T05 con video real y umbral por cámara (R-06)."),
    (12, "Ver log de tiempos de procesamiento", "4", "Tiempo por época y por etapa en el registro de experimentos (R-03)."),
]

for _r in RIESGOS:
    _r["pi"] = r4(_r["p"] * _r["i"])
    _r["tipo"] = tipo_de(_r["pi"])

# Prioridad: exposición (P × I) de mayor a menor; en empate, la fecha de control más cercana.
ORDEN = ["R-01", "R-08", "R-02", "R-04", "R-03", "R-07", "R-06", "R-09", "R-05"]
BY = {r["cod"]: r for r in RIESGOS}
assert sorted(ORDEN) == sorted(BY)
assert all(BY[ORDEN[k]]["pi"] >= BY[ORDEN[k + 1]]["pi"] for k in range(len(ORDEN) - 1))
PRIO = {c: k + 1 for k, c in enumerate(ORDEN)}

REGLA = [
    "**P × I ≥ 0,20 → acción en el backlog:** tarea en el Sprint Backlog o criterio de aceptación nuevo en una HU, con responsable y fecha. "
    "Aplica a R-01, R-08, R-02, R-04 y R-03.",
    "**0,10 ≤ P × I < 0,20 → mitigar dentro de lo planificado:** tareas o eventos Scrum ya previstos, sin ítem nuevo; se vigila en la Daily. "
    "Aplica a R-07, R-06 y R-09.",
    "**P × I < 0,10 → aceptar y vigilar:** R-05.",
]

# ---------------------------------------------------------------------------------------------
# Guion de 3 minutos (riesgo más crítico: R-01)
GUION_META = [
    ("Riesgo", "R-01 · Ajuste del modelo temporal (ConvLSTM) · P × I = 0,40 · ALTO (prioridad 1 de 9)"),
    ("Presenta", "Anthony Lopez (Scrum Master). Luis Salazar responde las preguntas técnicas y Albert Chumacero (PO) confirma el plan B."),
    ("Ante quién y cuándo", "Docente y compañeros (actividad de la semana 8) y en la revisión del Sprint 2 (13/11/2026) ante el PO."),
    ("Apoyo visual", "Matriz P × I (página 1), tabla de priorización (página 2) y ficha R-01 (página 3) de este documento."),
]
GUION = [
    ("0:00–0:20", "Apertura",
     "«Soy Anthony Lopez, Scrum Master de NewBit. De los nueve riesgos que registramos, voy a explicar el más crítico, el R-01: el ajuste del modelo "
     "temporal ConvLSTM. Es el único con exposición alta.»"),
    ("0:20–0:50", "Qué es el riesgo",
     "«NewBit trabaja en dos etapas. YOLOv8 detecta a los operarios y descarta los frames vacíos; después, ConvLSTM mira una secuencia de frames y decide "
     "si la conducta es segura o insegura: caminar fuera de la vía peatonal o dejar abierto el panel eléctrico. El riesgo es que ConvLSTM no aprenda a "
     "distinguir esas conductas con la configuración inicial, o que ajustarlo tome más entrenamientos de los que caben en el Sprint 3, del 16 al 27 de "
     "noviembre. Todavía no es un problema: es un evento incierto que estamos vigilando.»"),
    ("0:50–1:20", "Por qué es el más crítico",
     "«Usamos la escala del formato. Probabilidad 0,5, probable: es el primer ConvLSTM que entrena el equipo, no tenemos línea base propia y la ventana de "
     "N frames de HU05 aún no está terminada. Impacto 0,8, muy alto: sin modelo temporal no hay pipeline completo ni métricas por clase, que son criterios "
     "de aprobación del Acta, y se caen HU07, HU08 y lo que depende de ellas, HU09 y HU10. Probabilidad por impacto: 0,40, riesgo alto. Ningún otro riesgo "
     "pasa de 0,24.»"),
    ("1:20–1:50", "Señal de alerta",
     "«No vamos a esperar al final del sprint para enterarnos. Hay dos señales medibles. La primera, el 19 de noviembre, al cerrar el //spike// con dos "
     "longitudes de secuencia: si ninguna supera en F1 macro a una línea base que siempre responde la clase mayoritaria, o si la pérdida de validación no "
     "baja en cinco épocas seguidas. La segunda, el 24 de noviembre: si en el split de prueba una conducta insegura queda con F1 menor a 0,50.»"),
    ("1:50–2:25", "Respuesta y evidencia",
     "«La respuesta es mitigar, y está en el backlog como tareas de HU07, no como buena intención. El responsable es Luis Salazar: hace el //spike// el 19, "
     "entrena en Colab con checkpoint por época del 20 al 23, lo que también controla el riesgo de GPU, R-03, y registra cada configuración con semilla "
     "fija. La evidencia de control es ese registro de experimentos y las métricas por clase del 24 de noviembre.»"),
    ("2:25–2:50", "Plan B",
     "«Si se activa la señal, aplicamos el plan B del Acta: el Product Owner, Albert Chumacero, reduce el alcance a una sola conducta y la entregamos con su "
     "evaluación documentada, en vez de presentar dos conductas a medias. Así protegemos la Definición de Terminado.»"),
    ("2:50–3:00", "Cierre",
     "«En resumen: el riesgo está identificado, medido, tiene responsable, fecha y una salida acordada. Lo revisamos en cada Daily y lo actualizamos en "
     "este registro. Gracias.»"),
]
MENSAJE = ("Mensaje clave: el riesgo más crítico de NewBit es que el modelo temporal no aprenda a tiempo; lo medimos el 19 y el 24 de noviembre, "
           "lo mitiga Luis Salazar con tareas de HU07 y, si falla, el PO reduce el alcance a una conducta.")


# ---------------------------------------------------------------------------------------------
def encabezado(d, texto):
    d.p(texto, size=13, b=True, color=ROJO, after=60)


def control(d):
    rows = [[{"text": "**CONTROL DE VERSIONES**", "span": 6, "fill": GRIS, "align": "center", "size": 13}],
            [{"text": "**%s**" % h, "fill": GRIS2, "align": "center", "size": 12} for h in ["Versión", "Hecho por", "Revisado por", "Aprobado por", "Fecha", "Motivo"]]]
    for v in VERSIONES:
        rows.append([{"text": x, "align": "center", "size": 12} for x in v])
    d.table(rows, widths_cm=[1.4, 3.8, 3.2, 3.6, 1.9, 7.6], border=BORDE, sz=4, cell_margin=50, keep_rows=True)


def tabla_proyecto(d, derecha_titulo, derecha_valor, size_val=18):
    cab = {"fill": GRIS, "align": "center", "size": 13}
    rows = [[dict(cab, text="**CÓDIGO Y NOMBRE DEL PROYECTO**"), dict(cab, text="**%s**" % derecha_titulo)],
            [{"text": PROYECTO, "size": 13}, {"text": derecha_valor, "align": "center", "size": size_val}]]
    d.table(rows, widths_rel=[1.55, 1], border=BORDE, sz=4, cell_margin=50)


def pagina_criterios(d):
    encabezado(d, "GRUPO D3 · NEWBIT · REGISTRO DE RIESGOS DEL PROYECTO · VERSIÓN 1.1 (%s)" % FECHA)
    control(d)
    d.p("RIESGO DEL PROYECTO", size=30, b=True, align="center", before=30, after=0)
    d.p("Registro de riesgos: criterios de evaluación, matriz de exposición y priorización", size=16, i=True, align="center", after=40)
    tabla_proyecto(d, "RIESGOS IDENTIFICADOS",
                   "**9** · 3 técnicos, 4 de datos y 2 de gestión · 8 con ficha (R-05 es bajo y se acepta)", size_val=13)
    # Criterios de escala explícitos
    h = {"fill": GRIS, "align": "center", "size": 12}
    rows = [[dict(h, text="**CRITERIOS DE EVALUACIÓN (escala numérica del formato FGAP050; el criterio de cada nivel lo fija el equipo para NewBit)**", span=8)],
            [dict(h, text="**PROBABILIDAD**"), dict(h, text="**VALOR**"), dict(h, text="**CUÁNDO SE ELIGE EN NEWBIT**"),
             dict(h, text="**IMPACTO**"), dict(h, text="**VALOR**"), dict(h, text="**CUÁNDO SE ELIGE EN NEWBIT**"),
             dict(h, text="**TIPO DE RIESGO**"), dict(h, text="**P × I**")]]
    for k in range(5):
        tp = TIPO[k][0]
        rows.append([{"text": "**%s**" % PROB[k][0], "size": 12}, {"text": ("%.1f" % PROB[k][1]).replace(".", ","), "align": "center", "size": 12},
                     {"text": CRIT_P[k], "size": 12},
                     {"text": "**%s**" % IMP[k][0], "size": 12}, {"text": num(IMP[k][1]), "align": "center", "size": 12},
                     {"text": CRIT_I[k], "size": 12},
                     {"text": "**%s**" % tp, "fill": COLOR_TIPO[tp], "size": 12}, {"text": TIPO[k][1], "fill": COLOR_TIPO[tp], "align": "center", "size": 12}])
    d.table(rows, widths_rel=[1.25, 0.5, 2.6, 0.85, 0.55, 2.9, 0.9, 0.95], border=BORDE, sz=4, keep_rows=True, cell_margin=50)
    rows = [[{"text": "**REGLA DE PRIORIZACIÓN Y RESPUESTA**", "fill": GRIS, "align": "center", "size": 12}]]
    rows.append([{"paras": ["• " + t for t in REGLA] + [
        "• **Exposición = probabilidad × impacto.** Se ordena de mayor a menor; en un empate va primero el riesgo con la fecha de control más cercana.",
        "• **Roles (Guía del SBOK, cap. 7):** el Product Owner es el dueño de los riesgos; el responsable de cada ficha ejecuta la respuesta; el Scrum Master "
        "vigila los triggers en la Daily y actualiza este registro en cada planificación, revisión y retrospectiva. Los umbrales de los triggers los fija el "
        "equipo para esta versión y se recalibran con los datos de cada sprint."], "size": 12}])
    d.table(rows, widths_rel=[1], border=BORDE, sz=4, cell_margin=60)
    matriz(d)


def matriz(d):
    h = {"fill": GRIS, "align": "center", "size": 12}
    rows = [[dict(h, text="**MATRIZ DE EXPOSICIÓN P × I (en cada celda: valor y riesgos ubicados)**", span=6)],
            [dict(h, text="**Probabilidad \\ Impacto**")] + [dict(h, text="**%s (%s)**" % (n, num(v))) for n, v in IMP]]
    for pn, pv in reversed(PROB):
        row = [{"text": "**%s (%s)**" % (pn, ("%.1f" % pv).replace(".", ",")), "fill": GRIS2, "size": 12}]
        for inn, iv in IMP:
            pi = r4(pv * iv)
            cods = [r["cod"] for r in RIESGOS if abs(r["p"] - pv) < 1e-9 and abs(r["i"] - iv) < 1e-9]
            txt = num(pi) + ("   **%s**" % " · ".join(cods) if cods else "")
            row.append({"text": txt, "fill": COLOR_TIPO[tipo_de(pi)], "align": "center", "size": 13 if cods else 12})
        rows.append(row)
    d.table(rows, widths_rel=[1.5, 1, 1, 1, 1, 1], border=BORDE, sz=4, keep_rows=True, cell_margin=50)


def pagina_priorizacion(d):
    d.page_break()
    encabezado(d, "GRUPO D3 · NEWBIT · PRIORIZACIÓN DE LOS 9 RIESGOS Y VÍNCULO CON LAS HISTORIAS DE USUARIO (%s)" % FECHA)
    h = {"fill": GRIS, "align": "center", "size": 12}
    rows = [[dict(h, text="**PRIORIZACIÓN Y VÍNCULO CON EL BACKLOG (orden por exposición)**", span=10)],
            [dict(h, text="**N.º**"), dict(h, text="**Código**"), dict(h, text="**Riesgo**"), dict(h, text="**Categoría**"),
             dict(h, text="**P × I**"), dict(h, text="**Tipo**"), dict(h, text="**Respuesta**"),
             dict(h, text="**¿Acción en el backlog? (HU / tarea)**"), dict(h, text="**Responsable**"), dict(h, text="**Fecha de control**")]]
    for c in ORDEN:
        r = BY[c]
        estr = r["estrategia"].split("**")[1].rstrip(".") if r["estrategia"].startswith("**") else ""
        rows.append([{"text": str(PRIO[c]), "align": "center", "size": 12}, {"text": "**%s**" % c, "align": "center", "size": 12},
                     {"text": r["nombre"], "size": 12}, {"text": r["cat"], "align": "center", "size": 12},
                     {"text": "%s × %s = **%s**" % (num(r["p"]), num(r["i"]), num(r["pi"])), "align": "center", "size": 12},
                     {"text": "**%s**" % r["tipo"], "fill": COLOR_TIPO[r["tipo"]], "align": "center", "size": 12},
                     {"text": estr, "size": 12},
                     {"text": ("**Sí:** " if r["pi"] >= 0.20 else "") + r["resumen_accion"], "size": 12},
                     {"text": r["resp"].split(" (")[0].split(".")[0].split(";")[0], "size": 12},
                     {"text": r["fecha"].split(" (")[0].split(" ·")[0], "align": "center", "size": 12}])
    d.table(rows, widths_rel=[0.35, 0.55, 2.4, 0.7, 1.15, 0.75, 1.3, 2.3, 1.15, 0.85], border=BORDE, sz=4, keep_rows=True, cell_margin=50)
    d.p("**Por qué estas acciones van al backlog:** los cinco riesgos con P × I ≥ 0,20 afectan historias que todavía no se aceptan (HU05, HU07, HU08 y HU10) "
        "o la aceptación de las ya construidas (HU01–HU06 y HU11). Si su respuesta no se vuelve tarea o criterio de aceptación con fecha, no entra en la "
        "capacidad del sprint ni se puede verificar en la revisión. R-01 es el más crítico (único ALTO): su explicación de 3 minutos está en la última página.",
        size=12, before=40, after=80)
    rows = [[dict(h, text="**VÍNCULO CON LAS HISTORIAS DE USUARIO (backlog FGAP040; riesgos en orden de prioridad)**", span=5)],
            [dict(h, text="**HU**"), dict(h, text="**Historia de usuario**"), dict(h, text="**Sprint**"),
             dict(h, text="**Riesgos que la afectan**"), dict(h, text="**Respuesta que recibe la historia**")]]
    for n, tit, sp, acc in HISTORIAS:
        rows.append([{"text": "**HU%02d**" % n, "align": "center", "size": 12}, {"text": tit, "size": 12}, {"text": sp, "align": "center", "size": 12},
                     {"text": riesgos_de_hu(n), "size": 12}, {"text": acc, "size": 12}])
    d.table(rows, widths_rel=[0.45, 1.9, 0.75, 1.6, 6.3], border=BORDE, sz=4, keep_rows=True, cell_margin=50)


def riesgos_de_hu(n):
    return " · ".join(("**%s**" if BY[c]["pi"] >= 0.20 else "%s") % c for c in ORDEN if n in BY[c]["hu"])


def ficha(d, r):
    d.page_break()
    encabezado(d, "GRUPO D3 · NEWBIT · REGISTRO DE RIESGOS v1.1 (%s) · CATEGORÍA: %s · PRIORIDAD %d DE 9" % (FECHA, r["cat"].upper(), PRIO[r["cod"]]))
    control(d)
    d.p("RIESGO DEL PROYECTO", size=26, b=True, align="center", before=20, after=20)
    tabla_proyecto(d, "CÓDIGO DEL RIESGO", "**%s**" % r["cod"])
    filas = [("DESCRIPCIÓN DEL RIESGO", "Describir detalladamente el riesgo identificado en el proyecto.", "**%s.** %s" % (r["nombre"], r["desc"])),
             ("CAUSA RAÍZ", "Describir las causas subyacentes que ocasionan el riesgo.", r["causa"]),
             ("TRIGGER", "Describir el evento o situación que indicaría la aparición inminente de un riesgo.", r["trigger"]),
             ("ENTREGABLES AFECTADOS", "Describir el entregable afectado por el riesgo (historias de usuario vinculadas en negrita).", r["entregables"])]
    rows = [[{"text": "**IDENTIFICACIÓN DEL RIESGO**", "span": 2, "fill": GRIS, "align": "center", "size": 13}]]
    for t, ins, v in filas:
        rows.append([{"paras": ["**%s**" % t, "//%s//" % ins], "fill": GRIS2, "size": 11}, {"text": v, "size": 12}])
    d.table(rows, widths_rel=[1, 3.3], border=BORDE, sz=4, keep_rows=True, cell_margin=50)
    # Evaluación: escala del formato en una tira por fila, con el nivel elegido resaltado
    h = {"fill": GRIS, "align": "center", "size": 12}
    rows = [[dict(h, text="**EVALUACIÓN DEL RIESGO** (escala del formato; se resalta el nivel elegido)", span=7)]]
    rp = [{"text": "**ESTIMACIÓN DE PROBABILIDAD**", "fill": GRIS2, "size": 11}]
    for n, v in PROB:
        sel = abs(v - r["p"]) < 1e-9
        rp.append({"text": ("**%s – %s**" if sel else "%s – %s") % (("%.1f" % v).replace(".", ","), n), "fill": ROSA if sel else None, "align": "center", "size": 11})
    rp.append({"text": "**%s – %s**" % (num(r["p"]), pname(r["p"])), "align": "center", "size": 13})
    ri = [{"text": "**ESTIMACIÓN DE IMPACTO**", "fill": GRIS2, "size": 11}]
    for n, v in IMP:
        sel = abs(v - r["i"]) < 1e-9
        ri.append({"text": ("**%s – %s**" if sel else "%s – %s") % (num(v), n), "fill": ROSA if sel else None, "align": "center", "size": 11})
    ri.append({"text": "**%s – %s**" % (num(r["i"]), iname(r["i"])), "align": "center", "size": 13})
    rt = [{"text": "**PROBABILIDAD POR IMPACTO Y TIPO DE RIESGO**", "fill": GRIS2, "size": 11}]
    for n, rango in reversed(TIPO):
        sel = n == r["tipo"]
        rt.append({"text": ("**%s (%s)**" if sel else "%s (%s)") % (n, rango.replace("Mayor a ", "> ").replace("Menor a ", "< ")),
                   "fill": ROSA if sel else None, "align": "center", "size": 11})
    rt.append({"text": "**%s × %s = %s → %s**" % (num(r["p"]), num(r["i"]), num(r["pi"]), r["tipo"].upper()), "align": "center", "size": 13,
               "fill": COLOR_TIPO[r["tipo"]]})
    rs = [{"text": "**SUSTENTO**", "fill": GRIS2, "size": 11}, {"text": r["sustento"], "span": 6, "size": 11}]
    rows += [rp, ri, rt, rs]
    d.table(rows, widths_rel=[1.15, 0.85, 0.85, 0.85, 0.85, 0.85, 1.6], border=BORDE, sz=4, keep_rows=True, cell_margin=45)
    # Respuesta
    rows = [[{"text": "**RESPUESTA AL RIESGO**", "span": 4, "fill": GRIS, "align": "center", "size": 13}],
            [{"text": "**ESTRATEGIA Y MITIGACIÓN**", "fill": GRIS2, "size": 11}, {"text": r["estrategia"], "span": 3, "size": 12}],
            [{"text": "**ACCIÓN EN EL BACKLOG (HU / TAREA)**", "fill": GRIS2, "size": 11}, {"text": r["backlog"], "span": 3, "size": 12}],
            [{"text": "**RESPONSABLE**", "fill": GRIS2, "size": 11}, {"text": r["resp"], "size": 12},
             {"text": "**FECHA**", "fill": GRIS2, "size": 11, "align": "center"}, {"text": r["fecha"], "size": 12}],
            [{"text": "**EVIDENCIA DE CONTROL**", "fill": GRIS2, "size": 11}, {"text": r["evidencia"], "span": 3, "size": 12}]]
    d.table(rows, widths_rel=[1, 1.65, 0.38, 1.27], border=BORDE, sz=4, keep_rows=True, cell_margin=50)


def pagina_guion(d):
    d.page_break()
    encabezado(d, "GRUPO D3 · NEWBIT · COMUNICACIÓN DEL RIESGO MÁS CRÍTICO (%s)" % FECHA)
    d.p("COMUNICACIÓN: GUION DE 3 MINUTOS", size=26, b=True, align="center", before=20, after=40)
    rows = [[{"text": "**%s**" % k.upper(), "fill": GRIS2, "size": 12}, {"text": v, "size": 12}] for k, v in GUION_META]
    d.table(rows, widths_rel=[1, 5], border=BORDE, sz=4, cell_margin=50)
    h = {"fill": GRIS, "align": "center", "size": 12}
    rows = [[dict(h, text="**TIEMPO**"), dict(h, text="**BLOQUE**"), dict(h, text="**QUÉ SE DICE (texto para leer en voz alta, unas 430 palabras)**")]]
    for t, b, txt in GUION:
        rows.append([{"text": "**%s**" % t, "align": "center", "size": 12}, {"text": "**%s**" % b, "size": 12}, {"text": txt, "size": 16}])
    d.table(rows, widths_rel=[0.75, 1.1, 8], border=BORDE, sz=4, keep_rows=True, cell_margin=70)
    d.p("**%s**" % MENSAJE, size=15, before=80, after=0, shade=ROSA)


def build_docx(path):
    d = Doc(landscape=True, margins_cm=(1.2, 1.5, 1.0, 1.5), font="Georgia", size=14,
            header=[("UNIVERSIDAD NACIONAL DEL SANTA  |  INGENIERÍA DE SOFTWARE II\tFGAP050 – Riesgo del Proyecto",
                     {"size": 13, "color": ROJO, "b": True, "tab_cm": (26.6, "right"), "after": 0})],
            footer=[("Universidad Nacional del Santa · Grupo D3 · NewBit (PY-NB-001) · Semana 8 · Página {PAGE}",
                     {"size": 13, "color": "707070", "align": "center"})],
            title="FGAP050 Riesgo del Proyecto – NewBit (v1.1)",
            subject="Registro de 9 riesgos con evaluación, priorización, respuesta y comunicación – Grupo D3")
    pagina_criterios(d)
    pagina_priorizacion(d)
    for c in sorted(BY):
        if BY[c]["ficha"]:
            ficha(d, BY[c])
    pagina_guion(d)
    d.save(path)


# ---------------------------------------------------------------------------------------------
def md_cell(t):
    return md_from_markup(t).replace("|", "\\|")


def build_md(path, n_paginas=None):
    out = []
    w = out.append
    w("# FGAP050 – Riesgo del Proyecto: NewBit (v1.1, 9 riesgos)")
    w("")
    w("- **Archivos para entregar** (esta carpeta): `%s.docx` (editable) y `%s.pdf`%s." % (
        BASE, BASE, " (%d páginas)" % n_paginas if n_paginas else ""))
    w("- **Qué cumple:** la **actividad calificada de la semana 8** (lámina 39 de la [clase de riesgo en Scrum](../../material-del-profe/riesgo-en-scrum-diapositivas/riesgo-en-scrum-diapositivas.md)): "
      "9 riesgos concretos (3 técnicos, 4 de datos y 2 de gestión), escala explícita y exposición P × I, priorización con vínculo al backlog, respuesta "
      "(mitigación, responsable, fecha, trigger y evidencia de control) y guion de 3 minutos del riesgo más crítico (R-01).")
    w("- **Estructura del PDF:** pág. 1 criterios de evaluación, regla de priorización y matriz P × I · pág. 2 priorización y vínculo con las historias de usuario (HU01–HU12) · págs. 3–10 una ficha "
      "por riesgo (R-01, R-02, R-03, R-04, R-06, R-07, R-08 y R-09) · pág. 11 guion de 3 minutos. R-05 (bajo) no tiene ficha: se acepta y se vigila.")
    w("- **Formato:** el de los ejemplos del docente ([ejemplo 1](../../material-del-profe/riesgo-fgap050-ejemplo-1/riesgo-fgap050-ejemplo-1.md), "
      "[ejemplo 2](../../material-del-profe/riesgo-fgap050-ejemplo-2/riesgo-fgap050-ejemplo-2.md)). Cada ficha conserva control de versiones, identificación y "
      "evaluación con la escala del formato (en una tira por fila, con el nivel elegido resaltado) y agrega «Respuesta al riesgo».")
    w("- **Generador:** `generar_fgap050.py` (usa `docx_nb.py` de la carpeta del FGAP110). PDF exportado con Pages (Word no acepta «guardar como» por AppleScript en esta Mac).")
    w("- **Fecha:** %s · **Versión:** 1.1 (Grupo D3). La v1.0 (02/11/2026) tenía 3 fichas (R-01 a R-03)." % FECHA)
    w("")
    w("## Control de versiones")
    w("| Versión | Hecho por | Revisado por | Aprobado por | Fecha | Motivo |")
    w("|---|---|---|---|---|---|")
    for v in VERSIONES:
        w("| " + " | ".join(md_cell(x) for x in v) + " |")
    w("")
    w("**Código y nombre del proyecto:** " + PROYECTO)
    w("")
    w("## Criterios de evaluación")
    w("Escala numérica del formato del docente; el criterio de cada nivel lo fija el equipo para NewBit.")
    w("")
    w("| Probabilidad | Valor | Cuándo se elige en NewBit | Impacto | Valor | Cuándo se elige en NewBit | Tipo de riesgo | P × I |")
    w("|---|:-:|---|---|:-:|---|---|---|")
    for k in range(5):
        w("| %s | %s | %s | %s | %s | %s | %s | %s |" % (PROB[k][0], ("%.1f" % PROB[k][1]).replace(".", ","), CRIT_P[k], IMP[k][0], num(IMP[k][1]),
                                                     CRIT_I[k], TIPO[k][0], TIPO[k][1]))
    w("")
    w("**Regla de priorización y respuesta**")
    for t in REGLA:
        w("- " + md_from_markup(t))
    w("- Exposición = P × I, de mayor a menor; en un empate va primero la fecha de control más cercana. El PO es el dueño de los riesgos; el responsable de "
      "cada ficha ejecuta la respuesta; el Scrum Master vigila los triggers en la Daily y actualiza el registro (Guía del SBOK, cap. 7).")
    w("")
    w("## Matriz de exposición P × I")
    w("| Probabilidad \\ Impacto | " + " | ".join("%s (%s)" % (n, num(v)) for n, v in IMP) + " |")
    w("|---|" + ":-:|" * 5)
    for pn, pv in reversed(PROB):
        cells = []
        for inn, iv in IMP:
            pi = r4(pv * iv)
            cods = [r["cod"] for r in RIESGOS if abs(r["p"] - pv) < 1e-9 and abs(r["i"] - iv) < 1e-9]
            cells.append(num(pi) + (" **%s**" % " · ".join(cods) if cods else ""))
        w("| %s (%s) | %s |" % (pn, ("%.1f" % pv).replace(".", ","), " | ".join(cells)))
    w("")
    w("## Priorización y vínculo con el backlog")
    w("| N.º | Código | Riesgo | Categoría | P | I | P × I | Tipo | Respuesta | Acción en el backlog (HU / tarea) | Responsable | Fecha de control |")
    w("|:-:|---|---|---|:-:|:-:|:-:|---|---|---|---|---|")
    for c in ORDEN:
        r = BY[c]
        estr = r["estrategia"].split("**")[1].rstrip(".")
        w("| %d | **%s** | %s | %s | %s | %s | **%s** | %s | %s | %s | %s | %s |" % (
            PRIO[c], c, r["nombre"], r["cat"], num(r["p"]), num(r["i"]), num(r["pi"]), r["tipo"], estr,
            ("**Sí:** " if r["pi"] >= 0.20 else "") + md_cell(r["resumen_accion"]), md_cell(r["resp"]), md_cell(r["fecha"])))
    w("")
    w("**Por qué van al backlog:** los cinco riesgos con P × I ≥ 0,20 afectan historias que todavía no se aceptan (HU05, HU07, HU08 y HU10) o la aceptación de "
      "las ya construidas (HU01–HU06 y HU11). Si la respuesta no se vuelve tarea o criterio de aceptación con fecha, no entra en la capacidad del sprint ni se "
      "verifica en la revisión.")
    w("")
    w("## Vínculo con las historias de usuario")
    w("Riesgos en orden de prioridad; en negrita los que generan acción en el backlog (P × I ≥ 0,20).")
    w("")
    w("| HU | Historia de usuario | Sprint | Riesgos que la afectan | Respuesta que recibe la historia |")
    w("|---|---|---|---|---|")
    for n, tit, sp, acc in HISTORIAS:
        w("| HU%02d | %s | %s | %s | %s |" % (n, tit, sp, riesgos_de_hu(n), md_cell(acc)))
    w("")
    w("## Fichas")
    for c in sorted(BY):
        r = BY[c]
        w("")
        w("### %s · %s (%s · prioridad %d de 9)%s" % (c, r["nombre"], r["cat"], PRIO[c], "" if r["ficha"] else " — sin ficha en el PDF"))
        w("| Campo | Contenido |")
        w("|---|---|")
        if r["ficha"]:
            w("| **Descripción del riesgo** | %s |" % md_cell(r["desc"]))
            w("| **Causa raíz** | %s |" % md_cell(r["causa"]))
        w("| **Trigger** | %s |" % md_cell(r["trigger"]))
        if r["ficha"]:
            w("| **Entregables afectados (HU)** | %s |" % md_cell(r["entregables"]))
        w("| **Probabilidad × impacto** | %s (%s) × %s (%s) = **%s** → **%s** |" % (num(r["p"]), pname(r["p"]), num(r["i"]), iname(r["i"]), num(r["pi"]), r["tipo"].upper()))
        w("| **Sustento** | %s |" % md_cell(r["sustento"]))
        w("| **Estrategia y mitigación** | %s |" % md_cell(r["estrategia"]))
        w("| **Acción en el backlog** | %s |" % md_cell(r["backlog"]))
        w("| **Responsable** | %s |" % md_cell(r["resp"]))
        w("| **Fecha** | %s |" % md_cell(r["fecha"]))
        w("| **Evidencia de control** | %s |" % md_cell(r["evidencia"]))
    w("")
    w("## Comunicación: guion de 3 minutos (R-01)")
    for k, v in GUION_META:
        w("- **%s:** %s" % (k, v))
    w("")
    w("| Tiempo | Bloque | Qué se dice |")
    w("|---|---|---|")
    for t, b, txt in GUION:
        w("| %s | %s | %s |" % (t, b, md_cell(txt)))
    w("")
    w("**%s**" % MENSAJE)
    w("")
    w("## Notas de trabajo (no van en el formato)")
    w("")
    w("### Cambios respecto de la v1.0 (02/11/2026)")
    w("- **Códigos estables:** R-01 a R-07 conservan el código de la tabla de priorización de la v1.0. R-04 pasó de «etiquetado de frames más lento» a "
      "«desbalance de clases y etiquetas de los clips» (el riesgo real de datos: el dataset etiqueta por video y está desbalanceado). R-06 pasó de «cambio de "
      "entorno: una planta y dos cámaras» (0,03) a «iluminación, oclusiones y cambio de dominio» (0,12): ahora incluye las fallas de detección dentro del "
      "dataset, que sí están en el alcance (HU03, HU04, HU11). R-07 sube de 0,10 a 0,14 por el Sprint 3 planificado al 93 %. **R-08 (privacidad)** y "
      "**R-09 (decisiones del PO)** son nuevos.")
    w("- **R-01 y R-03 pasan al Sprint 3:** el plan de lanzamiento ([FGAP080 v1.0, 09/11](../../../semana-09-stakeholders-y-lanzamiento/nuestras-entregas/FGAP080_Cronograma_Lanzamiento_NewBit/FGAP080_Cronograma_Lanzamiento_NewBit.md)) "
      "deja HU07 en el Sprint 3 y el FGAP090 registra que el PO rechazó la SC-001 para el Sprint 2 (02/11); por eso el //spike// de R-01 es la tarea 3.05 (19/11, Luis) "
      "y no la T10 del Sprint 2 (10/11, Anthony) del FGAP110/FGAP130, que no se ejecuta. T14 (Colab, R-03) sí queda en el Sprint 2. El trigger de R-01 cambia de «exactitud» a «F1 macro», por el desbalance de R-04.")
    w("- **Se quitó todo «POR CONFIRMAR» del Word y del PDF** (aprobación del PO y GPU de R-03). Los supuestos quedan abajo.")
    w("- Riesgos del resumen del `.md` del Acta: «reproducibilidad de pesos» queda dentro de R-01 y R-02 (semilla fija, configuración versionada, revisión de "
      "pares); «iluminación y oclusiones» y «transferibilidad de dominio» están en R-06; «espacio en disco» es R-05; «SM con doble rol» es R-07.")
    w("- Fechas del Sprint 3 (16–27/11): día 3 = 18/11, día 4 = 19/11, días 5–6 = 20 y 23/11, día 7 = 24/11, día 8 = 25/11 (tareas 3.04–3.10 del FGAP080). "
      "Sprint 4: tarea 4.04 = 03–04/12; despliegue de demostración L2.1 = 14/12; cierre C.2 = 18/12.")
    w("")
    w("### Supuestos (no van en el formato)")
    w("1. **Aprobación del PO:** la v1.0 y la v1.1 figuran aprobadas por Albert Chumacero (PO), como pide la entrega; no hay en el repo un acta firmada.")
    w("2. **GPU (R-03):** se asume que el equipo no tiene GPU NVIDIA propia (la aplicación corre en CPU, la Mac del SM no admite CUDA y no hay otra GPU registrada); "
      "el plan entrena en Google Colab. Si un integrante tiene GPU NVIDIA, baja la probabilidad de R-03.")
    w("3. **Umbrales de los triggers** (20 min por época, 10 % y 20 % de frames perdidos, F1 < 0,50, 15 clips, 10 a 1, 0,15 de recall, 2 días hábiles, 10 GB): "
      "criterios del equipo, no mediciones; se recalibran con los datos de cada sprint.")
    w("4. **Resultados de T11 y T14** (03/11 y 02/11): al 09/11 no hay registro en el repo; el documento no afirma que se hicieron ni su resultado.")
    w("5. **Acciones nuevas en el backlog** (criterio de conteo de clips en HU05, criterio de privacidad en HU10, tarea de control de acceso del Sprint 4, ítem "
      "de `git ls-files` en la DoD): son respuestas propuestas en este registro; hay que llevarlas al backlog, al FGAP070 y al FGAP080 en su próxima versión.")
    w("6. **Datos del dataset** (178/50, 129/19, 13 videos de panel abierto en prueba, 4,6 s promedio de panel cerrado, clips con varias conductas): "
      "[Research Pack, 04_DATASET](../../../../proyecto-newbit/investigacion/UnsafeNet_Research_Pack/04_DATASET.md). Capacidad y uso del Sprint 3: "
      "[burndown](../Burndown_Sprint_NewBit/Burndown_Sprint_NewBit.md) (plan, no medición).")
    w("7. **Ley N.° 29733** (Ley de Protección de Datos Personales del Perú): se cita como marco de R-08; no se hizo un análisis legal.")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "."
    npag = int(sys.argv[2]) if len(sys.argv) > 2 else None
    os.makedirs(out, exist_ok=True)
    build_docx(os.path.join(out, BASE + ".docx"))
    build_md(os.path.join(out, BASE + ".md"), npag)
    print("ok", out)
