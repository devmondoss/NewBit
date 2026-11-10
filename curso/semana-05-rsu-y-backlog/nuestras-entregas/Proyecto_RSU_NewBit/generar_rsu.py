# -*- coding: utf-8 -*-
"""Genera la propuesta de proyecto de RSU del Grupo D3 (NewBit):
  1. Proyecto_RSU_NewBit.docx -> formato del Anexo N° 1 del Reglamento de RSU de la UNS
     (Res. N° 448-2023-CU-R-UNS), con la presentación de los dos ejemplos 2025 del docente:
     carátula con logo, índice, índice de tablas, secciones I–VIII, tablas APA y anexos.
  2. Proyecto_RSU_NewBit.md   -> resumen del repo (estructura seguida, supuestos y decisiones).
El PDF se exporta aparte con Pages (ver el .md).

Uso:  ../../../../.venv/bin/python -I generar_rsu.py
  Si ya existe Proyecto_RSU_NewBit.pdf y está PyMuPDF, el índice toma de ahí los números de página
  (primera pasada: generar -> exportar PDF; segunda pasada: generar -> exportar otra vez).
Propuesta (diseño nuevo): no hay convenios, instituciones con nombre propio ni resultados.
"""
import os
import re
import sys
import zipfile

sys.dont_write_bytecode = True  # no dejar __pycache__ en las carpetas de entregas
HERE = os.path.dirname(os.path.abspath(__file__))
FGAP110 = os.path.abspath(os.path.join(HERE, "..", "..", "..", "semana-08-riesgo-y-planificacion-del-sprint",
                                       "nuestras-entregas", "FGAP110_EDT_Sprint_02_NewBit"))
sys.path.insert(0, FGAP110)  # docx_nb.py (generador de Word del equipo)
from docx_nb import Doc, md_from_markup  # noqa: E402

BASE = "Proyecto_RSU_NewBit"
LOGO = os.path.abspath(os.path.join(HERE, "..", "..", "..", "semana-06-producto-unidad-1", "nuestras-entregas",
                                    "Producto_Unidad_1_NewBit", "logo-uns.png"))
TITULO = ("Seguridad laboral asistida por inteligencia artificial: taller de prevención de actos inseguros "
          "para trabajadores de talleres metalmecánicos de Chimbote y Nuevo Chimbote")
DOCENTE = "Dr. Ing. Alfredo Daza Vergaray"
ORCID_DOCENTE = "orcid.org/0000-0002-2259-1070"  # el que figura en los ejemplos del docente
ESTUDIANTES = [
    ("Chumacero Chávarry, Albert Sebastian",
     "Coordinación con el docente responsable y con los talleres convocados; inscripción de participantes, "
     "logística y presupuesto. Conduce el módulo 1 (actos y condiciones inseguras)."),
    ("Lopez Yrribarren, Anthony Gabriel",
     "Selección de los videos del conjunto de datos público, preparación y conducción de la demostración "
     "del prototipo NewBit (módulos 2 y 3)."),
    ("Salazar Diaz, Luis Fernando",
     "Diseño, aplicación y análisis de los instrumentos de evaluación; conduce el módulo 4 (privacidad y uso "
     "responsable) y redacta el informe final."),
]
N_BENEF = 30
FONT = "Times New Roman"
SZ = 24          # 12 pt (medios puntos)
SZ_T = 20        # 10 pt en tablas
LINE = 360       # interlineado 1,5
TEXT_W = 15.0    # ancho útil en cm (A4 con márgenes de 3 cm a izquierda y derecha)
GRIS = "D9D9D9"
BARRA = "1F3864"
HITO = "C00000"
BORDE = "7F7F7F"

# --------------------------------------------------------------------------------------------
# Contenido (una sola fuente para el Word y el .md)
# --------------------------------------------------------------------------------------------
LEGAL = [
    "La **Ley N.° 30220, Ley Universitaria** (Congreso de la República del Perú, 2014), define en su artículo 124 la "
    "responsabilidad social universitaria como la gestión ética y eficaz del impacto que la universidad genera en la "
    "sociedad al ejercer sus funciones académicas, de investigación y de extensión, y la reconoce como fundamento de "
    "la vida universitaria.",
    "El **Reglamento de Proyectos e Informes de RSU y Extensión Cultural de la UNS**, aprobado por la Resolución "
    "N.° 448-2023-CU-R-UNS (Universidad Nacional del Santa, 2023), exige que los proyectos estén vinculados al campo "
    "de la profesión (art. 6.6), que generen impacto social o educativo (art. 6.7) y reconoce como actividad la "
    "difusión de conocimientos tecnológicos socialmente útiles (art. 7.3). Este documento sigue su Anexo N.° 1.",
    "La **Ley N.° 29783, Ley de Seguridad y Salud en el Trabajo** (Congreso de la República del Perú, 2011b), y su "
    "reglamento, el Decreto Supremo N.° 005-2012-TR (Ministerio de Trabajo y Promoción del Empleo, 2012), establecen "
    "en su título preliminar los principios de prevención y de información y capacitación. El taller complementa, "
    "sin reemplazarla, la capacitación que corresponde al empleador.",
    "La **Ley N.° 29733, Ley de Protección de Datos Personales** (Congreso de la República del Perú, 2011a), protege "
    "la imagen que permite identificar a una persona. Por eso el taller no graba a los participantes ni aplica "
    "reconocimiento facial: la demostración usa solo videos de un conjunto de datos público con licencia CC BY 4.0.",
    "El proyecto se alinea con la **Agenda 2030** (Naciones Unidas, 2015): meta 8.8 del ODS 8, que pide promover "
    "entornos de trabajo seguros y sin riesgos para todos los trabajadores, y meta 4.4 del ODS 4, sobre las "
    "competencias técnicas que necesitan jóvenes y adultos para acceder a un trabajo decente.",
]

IMPORTANCIA = [
    "**Por qué.** En un taller metalmecánico conviven tornos, fresadoras, taladros, tableros eléctricos y pasillos de "
    "circulación. Muchos incidentes no empiezan con una falla de la máquina, sino con una conducta: cruzar fuera de la "
    "vía peatonal demarcada o dejar abierto el panel eléctrico de un equipo. Son actos que se repiten porque se "
    "vuelven costumbre y porque la supervisión es intermitente. Al mismo tiempo, empiezan a llegar a la industria "
    "sistemas de cámaras con inteligencia artificial (IA) que prometen detectar esas conductas. Si los trabajadores "
    "no saben qué hacen y qué no hacen estos sistemas, aparecen dos riesgos: rechazarlos como simple vigilancia o "
    "confiar en ellos más de lo debido.",
    "**Para qué.** Para que trabajadores, supervisores y aprendices reconozcan dos actos inseguros frecuentes, "
    "conozcan las medidas preventivas y entiendan, con un ejemplo concreto, cómo la visión por computadora puede "
    "apoyar a la persona que supervisa la seguridad sin sustituir su criterio ni invadir la privacidad. Para los "
    "estudiantes colaboradores, el taller pone en valor lo aprendido en la carrera (art. 6.6 del reglamento): "
    "visión por computadora, ingeniería de software y ética en el uso de datos, aplicadas al proyecto NewBit que "
    "desarrollan en el curso Ingeniería de Software II.",
    "**Vinculación con el proyecto del curso.** NewBit (código PY-NB-001) es la plataforma de Computer Vision que el "
    "equipo construye con Scrum para convertir cámaras existentes en sensores inteligentes configurables para "
    "operaciones industriales. Su primera capacidad, basada en la investigación Unsafe-Net (Önal y Dandıl, 2025), "
    "busca detectar actos inseguros en videos de manufactura metalmecánica. El proyecto de RSU no es parte del "
    "producto de software ni de su presupuesto: es la difusión de ese conocimiento a la comunidad.",
]

ANTECEDENTES = [
    "Önal y Dandıl (2021) aplicaron el detector YOLOv4 para reconocer elementos de seguridad y equipos de protección "
    "personal en entornos de trabajo, con un mAP de 91,18 %, una precisión de 0,89 y una sensibilidad de 0,91. El "
    "estudio muestra el punto de partida de esta línea de investigación: la detección cuadro por cuadro de objetos "
    "relacionados con la seguridad. Un solo fotograma, sin embargo, no basta para describir una acción.",
    "Esa limitación motivó Unsafe-Net (Önal y Dandıl, 2025), un sistema de dos etapas para detectar conductas "
    "inseguras en una fábrica. En la primera etapa, YOLOv4 identifica los fotogramas relevantes y reduce cada clip; "
    "en la segunda, una red ConvLSTM clasifica la secuencia. Con 39 días de video grabado por dos cámaras IP en una "
    "planta metalmecánica y de plásticos de Turquía, los autores reportan una exactitud promedio por clase de "
    "85,78 % sin reducción de fotogramas y de 95,81 % con el sistema completo, además de un piloto en planta "
    "validado por un experto en seguridad y salud en el trabajo.",
    "El conjunto de datos de ese estudio se describe en Önal y Dandıl (2024b) y se publica en Mendeley Data con "
    "licencia CC BY 4.0 (Önal y Dandıl, 2024a). Contiene 691 clips en ocho clases: cuatro conductas inseguras, entre "
    "ellas el tránsito fuera de la vía peatonal y la tapa de panel abierta, y sus cuatro contrapartes seguras. Para "
    "este proyecto es clave: permite mostrar actos inseguros reales sin grabar a ningún trabajador.",
    "En el Perú, Machaca Arcana (2019), en la Universidad Nacional de San Agustín de Arequipa, desarrolló un sistema "
    "que reconoce eventos anómalos en videos de cámaras de vigilancia mediante redes convolucionales que detectan "
    "personas y analizan sus acciones y patrones de movimiento. Es un antecedente nacional cercano porque trabaja con "
    "video y con acciones, no con imágenes aisladas.",
    "Paucara Guadalupe y Rodríguez Enciso (2024), en la Universidad César Vallejo, propusieron un sistema basado en "
    "aprendizaje profundo para detectar el uso correcto del casco. Con un diseño de preprueba y posprueba concluyeron "
    "que el sistema identifica el casco con mayor exactitud que la supervisión convencional. Su aporte metodológico "
    "es el mismo que adopta este proyecto: medir el efecto de la intervención comparando la situación antes y "
    "después.",
    "Como antecedente propio, el equipo tiene implementada la primera etapa del prototipo NewBit (sprints 1 y 2 del "
    "curso): carga y validación de videos, reducción de fotogramas, detección de personas con YOLOv8 (Jocher et al., "
    "2023) y armado del clip con los tramos relevantes, con pruebas automatizadas. La clasificación de la conducta "
    "con ConvLSTM está planificada para el sprint 3; el taller solo mostrará lo que esté terminado y probado a la "
    "fecha de ejecución.",
]

PROBLEMATICA = [
    "La actividad industrial de Chimbote y Nuevo Chimbote, ligada a la pesca, la siderurgia y la construcción "
    "naval, se apoya en una red de talleres metalmecánicos de distinto tamaño que fabrican y reparan piezas y "
    "equipos. En muchos de ellos la seguridad depende de inspecciones intermitentes y la capacitación suele "
    "centrarse en el uso de equipos de protección personal. Las conductas que exponen al trabajador, como "
    "transitar fuera de la vía peatonal o dejar abierto el panel eléctrico de una máquina, se toleran cuando "
    "“no pasa nada”, y las cámaras que algunos talleres ya tienen se revisan solo después de un incidente.",
    "A esto se suma un vacío de información sobre la IA aplicada a la seguridad laboral. Los trabajadores rara vez "
    "tienen un espacio para ver de forma práctica qué puede detectar una cámara inteligente, qué no puede detectar y "
    "cómo se protege su privacidad. Sin esa información, una herramienta preventiva puede percibirse como un "
    "instrumento de control o sanción.",
    "El equipo no dispone de un diagnóstico cuantitativo local de esta situación. Por eso el cuestionario de entrada "
    "del taller servirá como línea base del grupo atendido, y la comparación con el cuestionario de salida permitirá "
    "describir el cambio en sus conocimientos y percepciones, sin generalizarlo a todo el sector.",
]

OBJ_GENERAL = (
    "Fortalecer la cultura de prevención de actos inseguros en %d trabajadores, supervisores y aprendices de "
    "talleres metalmecánicos de Chimbote y Nuevo Chimbote, mediante un taller que muestre cómo la visión por "
    "computadora puede apoyar la supervisión de la seguridad laboral con respeto a la privacidad." % N_BENEF)
OBJ_ESPECIFICOS = [
    "Explicar la diferencia entre acto y condición insegura y las medidas preventivas para dos actos frecuentes "
    "en el taller: el tránsito fuera de la vía peatonal y el panel eléctrico abierto.",
    "Demostrar el prototipo NewBit con videos del conjunto de datos público de Önal y Dandıl (2024a), sin grabar a "
    "los participantes ni usar reconocimiento facial.",
    "Promover el uso responsable de la IA en el trabajo: la herramienta apoya la decisión de la persona que "
    "supervisa, no la reemplaza ni sirve para sancionar.",
    "Medir el cambio en conocimientos y percepciones de los participantes comparando un cuestionario de entrada "
    "y otro de salida, y recoger su satisfacción con el taller.",
]

METODOS = [
    "**Diseño preexperimental con preprueba y posprueba en un solo grupo**, con enfoque mixto: cuantitativo para "
    "comparar los puntajes del cuestionario antes y después del taller, y cualitativo para registrar preguntas, "
    "comentarios y sugerencias de los participantes.",
    "**Método expositivo-dialogado:** presentación breve de cada tema seguida de preguntas y ejemplos del propio "
    "trabajo de los participantes.",
    "**Método demostrativo:** uso en vivo del prototipo NewBit en una computadora portátil, sin conexión a cámaras "
    "reales, con videos del conjunto de datos público.",
    "**Estudio de casos con video:** los participantes analizan clips de conductas seguras e inseguras y comparan "
    "su juicio con el resultado del sistema.",
]
TECNICAS = [
    "**Expositivas:** presentaciones con apoyo audiovisual y lenguaje sencillo, sin tecnicismos innecesarios.",
    "**Demostrativas:** recorrido guiado por el prototipo: carga del video, fotogramas seleccionados, personas "
    "detectadas y clip resultante.",
    "**Participativas:** ejercicio «¿Seguro o inseguro?» en grupos de cinco y ronda de preguntas.",
    "**Evaluativas:** cuestionario de entrada y salida (Anexo A) y encuesta de satisfacción.",
    "**Observación:** registro de las preguntas frecuentes y de las dudas sobre privacidad para el informe final.",
]
PROCEDIMIENTOS = [
    "Presentar el proyecto al Departamento Académico y al Comité de RSU de la Facultad para su aval y aprobación; el "
    "taller se ejecuta después de la resolución de autorización (arts. 11–16 del reglamento).",
    "Convocar a los participantes visitando talleres metalmecánicos de Chimbote y Nuevo Chimbote y difundiendo una "
    "invitación digital; inscribirlos con la ficha del Anexo B hasta completar %d cupos." % N_BENEF,
    "Preparar el material: presentación, guía de bolsillo impresa y selección de ocho clips del conjunto de datos "
    "(tránsito fuera de la vía peatonal y panel abierto, con sus contrapartes seguras). Probar el prototipo en la "
    "computadora del taller sin depender de internet.",
    "Revisar con el docente responsable los instrumentos de evaluación y el guion de la sesión.",
    "Ejecutar el taller según el programa de la Tabla 2.",
    "Tabular los cuestionarios: puntaje promedio de entrada y de salida, porcentaje de aciertos por pregunta y "
    "resultados de la encuesta de satisfacción.",
    "Elaborar el informe final con el Anexo N.° 2 del reglamento dentro de los 15 días posteriores al taller "
    "(art. 18).",
]
PROGRAMA = [  # hora, módulo, contenido, responsable
    ("09:00–09:15", "Inicio", "Registro de asistencia, consentimiento informado y cuestionario de entrada.",
     "Albert Chumacero · Luis Salazar"),
    ("09:15–09:50", "Módulo 1", "Actos y condiciones inseguras en el taller metalmecánico; vía peatonal y panel "
     "eléctrico; principios de prevención de la Ley N.° 29783.", "Albert Chumacero"),
    ("09:50–10:25", "Módulo 2", "¿Cómo «ve» una cámara inteligente? Fotogramas, detección de personas y "
     "reconocimiento de una acción en el tiempo, explicados con ejemplos.", "Anthony Lopez"),
    ("10:25–10:40", "Pausa", "Refrigerio.", "Equipo"),
    ("10:40–11:20", "Módulo 3", "Demostración del prototipo NewBit con videos del conjunto de datos público y "
     "ejercicio «¿Seguro o inseguro?».", "Anthony Lopez"),
    ("11:20–11:45", "Módulo 4", "Privacidad y uso responsable: sin reconocimiento facial, decisión humana, límites "
     "y errores posibles del sistema; Ley N.° 29733.", "Luis Salazar"),
    ("11:45–12:00", "Cierre", "Cuestionario de salida, encuesta de satisfacción, entrega de la guía de bolsillo y "
     "de las constancias.", "Equipo y docente responsable"),
]
BENEFICIOS = [
    "**Participantes:** reconocen dos actos inseguros frecuentes y sus medidas preventivas, y conocen qué puede y "
    "qué no puede hacer una cámara con IA.",
    "**Talleres convocados:** cuentan con trabajadores sensibilizados y con una guía de bolsillo para reforzar la "
    "prevención en su puesto.",
    "**Estudiantes colaboradores:** aplican lo aprendido en la carrera y en el proyecto NewBit a un problema real "
    "de su entorno (arts. 6.3 y 6.6 del reglamento).",
    "**Universidad:** cumple su función de responsabilidad social y estrecha el vínculo con el sector productivo "
    "local (art. 6.5).",
    "**Sociedad:** se difunde un conocimiento tecnológico socialmente útil (art. 7.3) orientado a entornos de "
    "trabajo más seguros.",
]
INSTRUMENTOS = [
    "**Cuestionario de entrada y salida** (Anexo A): ocho preguntas de opción múltiple sobre actos inseguros y "
    "uso de la IA, y tres afirmaciones de percepción con escala de cinco puntos. Es el mismo antes y después.",
    "**Encuesta de satisfacción:** cinco afirmaciones con escala de cinco puntos y una pregunta abierta.",
    "**Ficha de inscripción y consentimiento informado** (Anexo B) y **lista de asistencia**.",
    "**Guía de observación:** registro de preguntas frecuentes y dudas sobre privacidad.",
    "**Recursos de la sesión:** presentación, computadora portátil con el prototipo NewBit, ocho clips del "
    "conjunto de datos público, proyector del aula y guía de bolsillo impresa.",
    "**Registro fotográfico** general del evento, solo con consentimiento y sin primeros planos; no se graba "
    "video de los participantes ni se procesa su imagen con el prototipo.",
]
INDICADORES = [  # objetivo, indicador, instrumento, meta propuesta
    ("OE1", "Puntaje promedio en las preguntas 1–4 (actos inseguros)", "Cuestionario de entrada y salida",
     "Mayor en la salida que en la entrada"),
    ("OE2", "Participantes que identifican correctamente los clips del ejercicio", "Ejercicio «¿Seguro o "
     "inseguro?» y preguntas 5–6", "Al menos 70 % en la salida"),
    ("OE3", "Participantes que reconocen que la IA apoya y no reemplaza la decisión humana", "Preguntas 7–8 y "
     "afirmaciones de percepción", "Al menos 80 % en la salida"),
    ("OE4", "Asistencia y satisfacción", "Lista de asistencia y encuesta de satisfacción",
     "Al menos 25 asistentes; al menos 80 % «de acuerdo» o «totalmente de acuerdo»"),
]
SEMANAS = ["Sem. 1\n16–22/11", "Sem. 2\n23–29/11", "Sem. 3\n30/11–06/12", "Sem. 4\n07–15/12"]
CRONOGRAMA = [  # actividad, responsable, semanas activas, hito
    ("Presentación del proyecto, aval del Comité de RSU y trámite de la resolución", "Equipo y docente", [1], None),
    ("Planificación detallada y reserva del aula", "A. Chumacero", [1], None),
    ("Convocatoria e inscripción de participantes", "A. Chumacero", [1, 2], None),
    ("Elaboración del material y selección de clips del conjunto de datos", "A. Lopez", [2], None),
    ("Elaboración y revisión de los instrumentos de evaluación", "L. Salazar", [2], None),
    ("Ensayo general de la demostración del prototipo", "A. Lopez", [3], None),
    ("Ejecución del taller (sábado 05/12/2026, 09:00–12:00)", "Equipo", [], 3),
    ("Tabulación y análisis de los cuestionarios", "L. Salazar", [4], None),
    ("Informe final (Anexo N.° 2) y entrega a la DECRS", "Equipo y docente", [4], None),
]
PRESUPUESTO = [  # rubro, detalle, cantidad, unitario
    ("Materiales", "Impresión de cuestionarios de entrada y salida y encuestas", 90, 0.10),
    ("Materiales", "Fichas de inscripción y consentimiento", 30, 0.10),
    ("Materiales", "Guía de bolsillo a color (díptico)", 30, 1.00),
    ("Materiales", "Lapiceros para los participantes", 30, 0.50),
    ("Materiales", "Constancias de participación en cartulina", 30, 1.00),
    ("Logística", "Refrigerio (30 participantes, 3 estudiantes y el docente)", 34, 3.50),
    ("Logística", "Movilidad local del equipo (convocatoria y día del taller)", 9, 5.00),
    ("Otros", "Imprevistos (aprox. 5 %)", 1, 13.00),
]
SIN_COSTO = [
    "Computadoras portátiles de los estudiantes colaboradores.",
    "Prototipo NewBit, desarrollado por el equipo en el curso Ingeniería de Software II.",
    "Conjunto de datos de Önal y Dandıl (2024a), de uso libre con atribución (licencia CC BY 4.0).",
    "Aula y proyector de la Facultad de Ingeniería de la UNS.",
]
ESTRATEGIAS = [
    "**Coordinación:** reuniones semanales del equipo y revisión de avances con el docente responsable; "
    "comunicación con los talleres convocados para fijar la asistencia.",
    "**Convocatoria y difusión:** visitas a talleres metalmecánicos de Chimbote y Nuevo Chimbote e invitación "
    "digital con fecha, hora, lugar y contenido del taller. Se prioriza a quienes trabajan en planta.",
    "**Participación:** sesión práctica, con el ejercicio de clips en grupos, ejemplos del propio trabajo de los "
    "participantes y tiempo para preguntas.",
    "**Certificación:** constancia de participación para cada asistente, firmada por el docente responsable.",
    "**Ética y privacidad:** consentimiento informado; respuestas anónimas en los cuestionarios; sin grabación de "
    "video ni reconocimiento facial; atribución del conjunto de datos según su licencia CC BY 4.0.",
    "**Contingencia:** si la resolución de autorización no se emite a tiempo, la fecha del taller se reprograma en "
    "coordinación con la DECRS (art. 16), sin cambiar el resto del plan. Si falla el equipo de cómputo, la "
    "demostración se hace con los clips ya procesados y guardados en una memoria USB.",
    "**Sostenibilidad:** la presentación y la guía de bolsillo quedan disponibles para los talleres participantes, "
    "y el equipo ofrece repetir el taller con otros grupos en un semestre siguiente.",
]
REFERENCIAS = [
    "Congreso de la República del Perú. (2011a, 3 de julio). //Ley N.° 29733, Ley de Protección de Datos "
    "Personales//. Diario Oficial El Peruano.",
    "Congreso de la República del Perú. (2011b, 20 de agosto). //Ley N.° 29783, Ley de Seguridad y Salud en el "
    "Trabajo//. Diario Oficial El Peruano.",
    "Congreso de la República del Perú. (2014, 9 de julio). //Ley N.° 30220, Ley Universitaria//. Diario Oficial "
    "El Peruano.",
    "Jocher, G., Chaurasia, A. y Qiu, J. (2023). //Ultralytics YOLOv8// (Versión 8.0.0) [Software]. "
    "https://github.com/ultralytics/ultralytics",
    "Machaca Arcana, L. A. (2019). //Reconocimiento de eventos anómalos en videos obtenidos de cámaras de "
    "vigilancia, usando redes convolucionales// [Tesis de licenciatura, Universidad Nacional de San Agustín de "
    "Arequipa]. Repositorio Institucional UNSA. http://repositorio.unsa.edu.pe/handle/UNSA/10849",
    "Ministerio de Trabajo y Promoción del Empleo. (2012, 25 de abril). //Decreto Supremo N.° 005-2012-TR, "
    "Reglamento de la Ley N.° 29783, Ley de Seguridad y Salud en el Trabajo//. Diario Oficial El Peruano.",
    "Naciones Unidas. (2015). //Transformar nuestro mundo: la Agenda 2030 para el Desarrollo Sostenible// "
    "(A/RES/70/1). https://undocs.org/es/A/RES/70/1",
    "Önal, O. y Dandıl, E. (2021). Object detection for safe working environments using YOLOv4 deep learning "
    "model. //Avrupa Bilim ve Teknoloji Dergisi//, (26), 343–351. https://doi.org/10.31590/ejosat.951733",
    "Önal, O. y Dandıl, E. (2024a). //Video dataset for safe and unsafe behaviours// (Versión 1) [Conjunto de "
    "datos]. Mendeley Data. https://doi.org/10.17632/xjmtb22pff.1",
    "Önal, O. y Dandıl, E. (2024b). Video dataset for the detection of safe and unsafe behaviours in workplaces. "
    "//Data in Brief//, //56//, Artículo 110791. https://doi.org/10.1016/j.dib.2024.110791",
    "Önal, O. y Dandıl, E. (2025). Unsafe-Net: YOLO v4 and ConvLSTM based computer vision system for real-time "
    "detection of unsafe behaviours in workplace. //Multimedia Tools and Applications//, //84//, 34967–34993. "
    "https://doi.org/10.1007/s11042-024-19276-8",
    "Paucara Guadalupe, C. E. R. y Rodríguez Enciso, S. P. (2024). //Sistema inteligente basado en deep learning "
    "para la detección del uso correcto de equipos de protección personal// [Tesis de licenciatura, Universidad "
    "César Vallejo]. Repositorio Digital Institucional UCV. https://hdl.handle.net/20.500.12692/149042",
    "Universidad Nacional del Santa. (2023). //Reglamento de proyectos e informes de responsabilidad social "
    "universitaria y extensión cultural// (aprobado por Resolución N.° 448-2023-CU-R-UNS). Dirección de Extensión "
    "Cultural y Responsabilidad Social.",
]
CUESTIONARIO = [  # pregunta, opciones (la correcta va primero en la clave, el orden impreso es otro)
    ("¿Cuál de estas situaciones es un **acto** inseguro y no una condición insegura?",
     ["a) Un piso con aceite derramado.", "b) Un trabajador que cruza la nave fuera de la vía peatonal.",
      "c) Una máquina sin guarda de protección de fábrica."]),
    ("¿Para qué sirve la vía peatonal demarcada en un taller?",
     ["a) Para separar el paso de las personas de las zonas de máquinas y de transporte de carga.",
      "b) Solo para orientar a los visitantes.", "c) Para guardar materiales cuando falta espacio."]),
    ("Si al terminar un ajuste el panel eléctrico de una máquina queda abierto, el principal riesgo es:",
     ["a) Que se ensucie el panel.", "b) Contacto eléctrico o manipulación por personal no autorizado.",
      "c) Que la máquina consuma más energía."]),
    ("Según la Ley N.° 29783, el principio de prevención significa que:",
     ["a) Se actúa solo después de un accidente.",
      "b) Se deben evitar los riesgos antes de que causen daño.",
      "c) La seguridad depende solo de cada trabajador."]),
    ("¿Qué hace una cámara con visión por computadora como la del prototipo mostrado?",
     ["a) Analiza las imágenes para detectar personas y reconocer ciertas conductas.",
      "b) Lee los pensamientos del trabajador.", "c) Reemplaza al supervisor de seguridad."]),
    ("¿Por qué el sistema necesita una secuencia de fotogramas y no una sola foto?",
     ["a) Porque una acción ocurre en el tiempo y una foto no la describe completa.",
      "b) Porque las fotos ocupan más espacio.", "c) No la necesita: una foto basta."]),
    ("Cuando el sistema marca una posible conducta insegura, lo correcto es que:",
     ["a) Se sancione automáticamente al trabajador.",
      "b) Una persona revise el caso y decida qué medida preventiva tomar.",
      "c) Se ignore la alerta."]),
    ("En el prototipo mostrado, ¿se identifica a cada trabajador por su rostro?",
     ["a) Sí, siempre.", "b) No: no usa reconocimiento facial; trabaja con la conducta, no con la identidad.",
      "c) Solo de noche."]),
]
PERCEPCION = [
    "Puedo reconocer cuándo un compañero comete un acto inseguro en el taller.",
    "Una cámara con IA puede ayudar a prevenir accidentes en mi lugar de trabajo.",
    "Entiendo cómo se protege mi privacidad cuando se usa una cámara con IA.",
]
CLAVE = "1 b · 2 a · 3 b · 4 b · 5 a · 6 a · 7 b · 8 b"

# --------------------------------------------------------------------------------------------
# Índice: (nivel, texto en el índice, clave de búsqueda en el PDF)
# --------------------------------------------------------------------------------------------
TOC = []
TABLAS = []


def total_presupuesto():
    return round(sum(c * u for _, _, c, u in PRESUPUESTO), 2)


def soles(x):
    return "S/ {:,.2f}".format(x)


def recolectar():
    """Pasada en seco: devuelve (títulos del índice, títulos de tablas) sin escribir nada."""
    TOC.clear()
    TABLAS.clear()
    _contenido(Rsu({}), dry=True)
    toc, tablas = list(TOC), list(TABLAS)
    TOC.clear()
    TABLAS.clear()
    return toc, tablas


def leer_paginas(pdf):
    """Busca cada título del índice en el PDF ya exportado y devuelve {clave: página}."""
    try:
        import pymupdf
    except Exception:
        return {}
    if not os.path.exists(pdf):
        return {}
    toc, tablas = recolectar()
    doc = pymupdf.open(pdf)
    textos = [re.sub(r"\s+", "", p.get_text()) for p in doc]
    inicio = next((i for i, t in enumerate(textos) if "DISEÑODELPROYECTO" in t), 0)
    pags = {}
    for _, _, clave in toc + tablas + [(1, "Anexos", "Anexos")]:
        k = re.sub(r"\s+", "", clave)
        for j in range(inicio, len(textos)):
            if k in textos[j]:
                pags[clave] = j + 1
                break
    return pags


class Rsu:
    def __init__(self, paginas):
        self.d = Doc(margins_cm=(2.5, 3.0, 2.5, 3.0), font=FONT, size=SZ,
                     header=None,
                     footer=[("{PAGE}", {"size": 20, "align": "right"})],
                     title="Proyecto RSU – NewBit (Grupo D3)",
                     subject="Proyecto de Responsabilidad Social Universitaria del Grupo D3 (UNS, 2026-II)")
        self.pag = paginas
        self.ntab = 0

    # bloques de texto -----------------------------------------------------------------------
    def P(self, text, **kw):
        kw.setdefault("align", "both")
        kw.setdefault("line", LINE)
        kw.setdefault("after", 120)
        self.d.p(text, **kw)

    def B(self, text, num=None):
        if num is None:
            self.d.bullet(text, line=LINE, align="both", after=60)
        else:
            self.d.body.append(self.d.para_xml(text, indent_cm=0.9, hanging_cm=0.6, tab_cm=0.9, prefix="%s\t" % num,
                                               line=LINE, align="both", after=60))

    def H1(self, num, text, new_page=False):
        self.d.p("**%s %s**" % (num, text), before=240, after=120, keep_next=True, line=LINE,
                 page_break_before=new_page)
        TOC.append((1, "%s %s" % (num, text), "%s %s" % (num, text)))

    def H2(self, num, text):
        self.d.p("**%s %s**" % (num, text), before=120, after=60, keep_next=True, line=LINE)
        TOC.append((2, "%s %s" % (num, text), "%s %s" % (num, text)))

    def H3(self, num, text):
        self.d.p("**//%s %s//**" % (num, text), before=60, after=60, keep_next=True, line=LINE, indent_cm=0.6)
        TOC.append((3, "%s %s" % (num, text), "%s %s" % (num, text)))

    def caption(self, title):
        self.ntab += 1
        self.d.p("**Tabla %d**" % self.ntab, before=120, after=0, keep_next=True)
        self.d.p("//%s//" % title, after=80)
        TABLAS.append((0, "Tabla %d. %s" % (self.ntab, title), title))
        return self.ntab

    def nota(self, text="Elaboración propia."):
        self.d.p("//Nota.// " + text, size=20, after=160)

    def table(self, rows, widths, **kw):
        kw.setdefault("border", BORDE)
        kw.setdefault("sz", 4)
        kw.setdefault("font_size", SZ_T)
        kw.setdefault("cell_margin", 80)
        # sin tblHeader: con encabezado repetido, Pages manda la tabla entera a la página siguiente
        self.d.table(rows, widths_cm=widths, **kw)

    def toc_line(self, level, text, key):
        ind = {0: 0.0, 1: 0.0, 2: 0.6, 3: 1.2}[level]
        num = str(self.pag.get(key, ""))
        x = self.d.para_xml("%s\t%s" % (text, num), b=(level == 1), indent_cm=ind, tab_cm=(TEXT_W, "right"),
                            after=40, line=300)
        x = x.replace('<w:tab w:val="right"', '<w:tab w:val="right" w:leader="dot"')
        self.d.body.append(x)


def build_docx(path, paginas):
    toc, tablas = recolectar()
    r = Rsu(paginas)
    _caratula(r)
    _indice(r, toc, tablas)
    _contenido(r)
    r.d.save(path)
    _primera_pagina_sin_numero(path)
    return toc, tablas


def _caratula(r):
    d = r.d
    for t in ["UNIVERSIDAD NACIONAL DEL SANTA", "FACULTAD DE INGENIERÍA",
              "ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS E INFORMÁTICA"]:
        d.p("**%s**" % t, size=28 if t.startswith("UNIV") else 26, align="center", after=140)
    d.spacer(10)
    d.image(LOGO, 4.2, after=360)
    d.p("**PROYECTO DE RESPONSABILIDAD SOCIAL Y EXTENSIÓN CULTURAL**", size=28, align="center", after=240)
    d.p("**%s**" % TITULO, size=26, align="center", after=480, line=300)
    d.p("**COLABORADORES:**", align="center", after=120)
    for n, _ in ESTUDIANTES:
        d.p(n, align="center", after=60)
    d.p("Grupo D3 · Ingeniería de Software II", align="center", after=360, i=True, size=22)
    d.p("**DOCENTE RESPONSABLE:**", align="center", after=120)
    d.p("%s (%s)" % (DOCENTE, ORCID_DOCENTE), align="center", after=480)
    d.p("**NUEVO CHIMBOTE – PERÚ**", align="center", after=100)
    d.p("**2026-II**", align="center", after=0)
    d.page_break()


def _indice(r, toc, tablas):
    d = r.d
    d.p("**Índice**", size=28, align="center", after=200)
    for lvl, text, key in toc:
        r.toc_line(lvl, text, key)
    r.toc_line(1, "Anexos", "Anexos")
    d.p("**Índice de tablas**", size=28, align="center", before=360, after=200)
    for _, text, key in tablas:
        r.toc_line(0, text, key)
    d.page_break()


def _contenido(r, dry=False):
    d = r.d
    d.p("**DISEÑO DEL PROYECTO DE RESPONSABILIDAD SOCIAL Y EXTENSIÓN CULTURAL**", size=26, align="center",
        after=120, line=LINE)
    d.p("**%s**" % TITULO, align="center", after=240, line=LINE)

    # I. Datos generales
    r.H1("I.", "Datos generales")
    r.H2("1.1.", "Facultad a la que pertenece el docente responsable del proyecto")
    r.P("Facultad de Ingeniería.", indent_cm=0.6)
    r.H2("1.2.", "Departamento académico donde está adscrito el docente responsable del proyecto")
    r.P("Departamento Académico de Ingeniería Civil y Sistemas.", indent_cm=0.6)
    r.H2("1.3.", "Nombres y apellidos del docente responsable del proyecto")
    r.P("%s (%s)." % (DOCENTE, ORCID_DOCENTE), indent_cm=0.6)
    r.H2("1.4.", "Nombres y apellidos de los docentes corresponsables del proyecto")
    r.P("No se consignan. El artículo 9 del reglamento admite hasta cinco docentes corresponsables, pero no los "
        "exige; el proyecto se ejecuta con el docente responsable.", indent_cm=0.6)
    r.H2("1.5.", "Nombres y apellidos de los estudiantes colaboradores")
    r.P("Estudiantes del curso Ingeniería de Software II (semestre 2026-II) de la Escuela Profesional de Ingeniería "
        "de Sistemas e Informática, Grupo D3. La Tabla 1 resume la función de cada uno.", indent_cm=0.6)
    r.caption("Estudiantes colaboradores y funciones en el proyecto")
    rows = [[{"text": "**Apellidos y nombres**", "fill": GRIS, "align": "center"},
             {"text": "**Función en el proyecto de RSU**", "fill": GRIS, "align": "center"}]]
    for n, f in ESTUDIANTES:
        rows.append([{"text": n}, {"text": f, "align": "both"}])
    r.table(rows, [5.0, 10.0])
    r.nota()
    r.H2("1.6.", "Unidad de desarrollo del proyecto")
    r.P("Aula de la Facultad de Ingeniería de la Universidad Nacional del Santa, campus de Nuevo Chimbote, con "
        "participantes de talleres metalmecánicos de Chimbote y Nuevo Chimbote convocados por el equipo.",
        indent_cm=0.6)
    r.H2("1.7.", "Número de beneficiarios del proyecto")
    r.P("%d participantes: trabajadores operativos, supervisores o encargados de seguridad y aprendices de talleres "
        "metalmecánicos de Chimbote y Nuevo Chimbote." % N_BENEF, indent_cm=0.6)
    r.H2("1.8.", "Duración del proyecto")
    r.P("30 días calendario, que incluyen un taller presencial de tres horas.", indent_cm=0.6)
    r.H2("1.9.", "Fecha de inicio y término")
    r.P("Inicio: 16 de noviembre de 2026.\nTaller: sábado 5 de diciembre de 2026, de 9:00 a 12:00 horas.\n"
        "Término: 15 de diciembre de 2026.", indent_cm=0.6)

    # II. Justificación
    r.H1("II.", "Justificación")
    r.H2("2.1.", "Justificación legal")
    for t in LEGAL:
        r.P(t)
    r.H2("2.2.", "Importancia (por qué y para qué)")
    for t in IMPORTANCIA:
        r.P(t)
    r.H2("2.3.", "Antecedentes")
    for t in ANTECEDENTES:
        r.P(t)

    # III. Problemática
    r.H1("III.", "Presentación de la problemática a resolver")
    r.H2("3.1.", "Caracterización de la problemática")
    for t in PROBLEMATICA:
        r.P(t)
    r.H2("3.2.", "Objetivos")
    r.H3("3.2.1.", "General")
    r.P(OBJ_GENERAL)
    r.H3("3.2.2.", "Específicos")
    for k, t in enumerate(OBJ_ESPECIFICOS, 1):
        r.B(t, num="OE%d." % k)

    # IV. Metodología
    r.H1("IV.", "Metodología")
    r.H2("4.1.", "Métodos a usar en la ejecución de la actividad")
    for t in METODOS:
        r.B(t)
    r.H2("4.2.", "Técnicas")
    for t in TECNICAS:
        r.B(t)
    r.H2("4.3.", "Procedimientos e instrumentos a utilizar")
    r.P("**Procedimientos.** El proyecto sigue estos pasos:", after=60)
    for k, t in enumerate(PROCEDIMIENTOS, 1):
        r.B(t, num="%d." % k)
    r.P("**Programa del taller.** La sesión dura tres horas y se organiza en cuatro módulos (Tabla 2). Los "
        "instrumentos que se usan en cada paso se describen en el apartado 4.5.", before=120)
    r.caption("Programa del taller del 5 de diciembre de 2026")
    rows = [[{"text": "**%s**" % h, "fill": GRIS, "align": "center"} for h in
             ["Hora", "Módulo", "Contenido", "Responsable"]]]
    for h, m, c, resp in PROGRAMA:
        rows.append([{"text": h, "align": "center"}, {"text": m, "align": "center"},
                     {"text": c, "align": "both"}, {"text": resp, "align": "center"}])
    r.table(rows, [2.3, 1.9, 7.6, 3.2])
    r.nota("Elaboración propia. Los videos de la demostración provienen de Önal y Dandıl (2024a).")
    r.H2("4.4.", "Número de beneficiarios del proyecto")
    r.P("Se atenderá a **%d participantes** de talleres metalmecánicos de Chimbote y Nuevo Chimbote, la misma "
        "cifra del apartado 1.7. Los beneficios esperados son:" % N_BENEF, after=60)
    for t in BENEFICIOS:
        r.B(t)
    r.H2("4.5.", "Instrumentos")
    for t in INSTRUMENTOS:
        r.B(t)
    r.P("La Tabla 3 relaciona cada objetivo específico con su indicador, su instrumento y la meta que el equipo se "
        "propone. Las metas son propuestas; los valores alcanzados se informarán en el informe final.", before=120)
    r.caption("Indicadores de evaluación del taller")
    rows = [[{"text": "**%s**" % h, "fill": GRIS, "align": "center"} for h in
             ["Objetivo", "Indicador", "Instrumento", "Meta propuesta"]]]
    for o, ind, ins, meta in INDICADORES:
        rows.append([{"text": o, "align": "center"}, {"text": ind}, {"text": ins}, {"text": meta}])
    r.table(rows, [1.8, 5.0, 4.4, 3.8])
    r.nota()

    # V. Cronograma
    r.H1("V.", "Cronograma de actividades")
    r.P("El cronograma se presenta como diagrama de Gantt por semanas (Tabla 4). Las barras indican la semana en "
        "que se realiza cada actividad y la celda roja marca el día del taller. La ejecución queda sujeta a la "
        "resolución de autorización (art. 16 del reglamento).")
    r.caption("Cronograma de actividades del proyecto (diagrama de Gantt)")
    rows = [[{"text": "**N.°**", "fill": GRIS, "align": "center"},
             {"text": "**Actividad**", "fill": GRIS, "align": "center"},
             {"text": "**Responsable**", "fill": GRIS, "align": "center"}] +
            [{"text": s, "b": True, "fill": GRIS, "align": "center", "size": 18} for s in SEMANAS]]
    for k, (act, resp, sem, hito) in enumerate(CRONOGRAMA, 1):
        row = [{"text": str(k), "align": "center"}, {"text": act}, {"text": resp, "align": "center", "size": 18}]
        for s in range(1, 5):
            if hito == s:
                row.append({"text": "**05/12**", "fill": HITO, "color": "FFFFFF", "align": "center", "size": 18})
            elif s in sem:
                row.append({"text": "", "fill": BARRA})
            else:
                row.append({"text": ""})
        rows.append(row)
    r.table(rows, [0.9, 6.3, 2.4, 1.35, 1.35, 1.35, 1.35])
    r.nota("Elaboración propia. Semanas de 2026; la semana 4 incluye hasta el martes 15 de diciembre, fecha de "
           "término del proyecto.")

    # VI. Presupuesto y financiamiento
    r.H1("VI.", "Presupuesto y financiamiento")
    r.H2("6.1.", "Presupuesto")
    r.P("La Tabla 5 detalla los gastos del proyecto. Es un presupuesto independiente del proyecto de software "
        "NewBit y no se suma a él.")
    r.caption("Presupuesto del proyecto")
    rows = [[{"text": "**%s**" % h, "fill": GRIS, "align": "center"} for h in
             ["Rubro", "Detalle", "Cant.", "Costo unit. (S/)", "Subtotal (S/)"]]]
    for rub, det, c, u in PRESUPUESTO:
        rows.append([{"text": rub, "align": "center"}, {"text": det}, {"text": str(c), "align": "center"},
                     {"text": "%.2f" % u, "align": "right"}, {"text": "%.2f" % (c * u), "align": "right"}])
    rows.append([{"text": "**Total**", "span": 4, "align": "right", "fill": GRIS},
                 {"text": "**%.2f**" % total_presupuesto(), "align": "right", "fill": GRIS}])
    r.table(rows, [2.3, 7.1, 1.4, 2.1, 2.1])
    r.nota()
    r.P("Además se emplean, sin costo para el proyecto, estos recursos existentes:", after=60)
    for t in SIN_COSTO:
        r.B(t)
    r.H2("6.2.", "Financiamiento")
    tot = total_presupuesto()
    r.P("El proyecto se financia con **recursos propios** de los tres estudiantes colaboradores, que aportan %s "
        "cada uno para cubrir el total de %s." % (soles(tot / 3), soles(tot)))

    # VII. Estrategias
    r.H1("VII.", "Estrategias")
    r.P("Para asegurar el cumplimiento de los objetivos se aplicarán las siguientes estrategias:", after=60)
    for t in ESTRATEGIAS:
        r.B(t)

    # VIII. Referencias
    r.H1("VIII.", "Referencias bibliográficas", new_page=True)
    for t in REFERENCIAS:
        d.p(t, indent_cm=1.27, hanging_cm=1.27, line=LINE, after=120, align="left")

    # Anexos
    d.page_break()
    d.p("**Anexos**", size=26, align="center", after=200)
    d.p("**Anexo A. Cuestionario de entrada y salida**", after=60)
    d.p("Se aplica el mismo cuestionario al inicio y al final del taller. Es anónimo: solo se pide un código de "
        "participante para emparejar ambas hojas.", align="both", after=80, size=22)
    d.p("Código de participante: ________    Momento:  ☐ Entrada   ☐ Salida", after=120, size=22)
    d.p("**Parte 1. Marque la respuesta correcta.**", after=60, size=22)
    for k, (q, ops) in enumerate(CUESTIONARIO, 1):
        d.p("%d. %s" % (k, q), after=20, size=22, keep_next=True)
        for o in ops:
            d.p(o, indent_cm=0.6, after=0, size=22, keep_next=(o != ops[-1]))
        d.spacer(2)
    d.p("**Parte 2. Indique su grado de acuerdo** (1 = totalmente en desacuerdo; 5 = totalmente de acuerdo).",
        before=80, after=60, size=22, keep_next=True)
    rows = [[{"text": "**Afirmación**", "fill": GRIS, "align": "center"}] +
            [{"text": "**%d**" % k, "fill": GRIS, "align": "center"} for k in range(1, 6)]]
    for a in PERCEPCION:
        rows.append([{"text": a}] + [{"text": "☐", "align": "center"} for _ in range(5)])
    r.table(rows, [10.0, 1.0, 1.0, 1.0, 1.0, 1.0])
    d.p("//Clave de respuestas (solo para el equipo):// " + CLAVE + ".", size=20, after=200)
    d.p("**Anexo B. Ficha de inscripción y consentimiento informado**", before=200, after=80, keep_next=True)
    rows = [[{"text": "**Datos del participante**", "fill": GRIS, "span": 2}],
            [{"text": "Nombres y apellidos"}, {"text": ""}],
            [{"text": "Ocupación"}, {"text": "☐ Operario   ☐ Supervisor o encargado de seguridad   ☐ Aprendiz"}],
            [{"text": "Años de experiencia en taller"}, {"text": ""}],
            [{"text": "Teléfono (opcional)"}, {"text": ""}],
            [{"text": "**Consentimiento**", "fill": GRIS, "span": 2}],
            [{"text": "Acepto participar en el taller «%s». Sé que mis respuestas a los cuestionarios son anónimas y "
                      "se usarán solo con fines académicos; que no se grabará video de los participantes ni se usará "
                      "reconocimiento facial; y que las fotografías generales del evento no mostrarán mi rostro en "
                      "primer plano. Puedo retirarme en cualquier momento." % TITULO, "span": 2, "align": "both"}],
            [{"text": "Firma: ______________________"}, {"text": "Fecha: ____/____/2026"}]]
    r.table(rows, [5.0, 10.0])


def _primera_pagina_sin_numero(path):
    """Carátula sin número de página: añade <w:titlePg/> (pie de primera página vacío)."""
    tmp = path + ".tmp"
    with zipfile.ZipFile(path) as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "word/document.xml":
                data = data.replace(b'<w:cols w:space="708"/></w:sectPr>',
                                    b'<w:cols w:space="708"/><w:titlePg/></w:sectPr>')
            zout.writestr(item, data)
    os.replace(tmp, path)


# --------------------------------------------------------------------------------------------
# .md del repo
# --------------------------------------------------------------------------------------------
def build_md(path, paginas, n_pags):
    m = md_from_markup
    L = []
    L.append("# Proyecto de RSU – Grupo D3 (NewBit): propuesta")
    L.append("")
    L.append("- **Archivos para entregar** (esta carpeta): `%s.pdf`%s y `%s.docx` (editable). "
             "Generador: `generar_rsu.py` (usa `docx_nb.py` del FGAP110 de la semana 8)."
             % (BASE, " (%d págs.)" % n_pags if n_pags else "", BASE))
    L.append("- **Semana:** 5 (el docente envió el reglamento y los ejemplos el 12/10/2026) · **elaborado:** 09/11/2026 · "
             "**Tipo:** proyecto de Responsabilidad Social Universitaria con el **Anexo N.° 1** del "
             "[reglamento de RSU de la UNS](../../material-del-profe/rsu-reglamento-uns/rsu-reglamento-uns.md) "
             "(Res. 448-2023-CU-R-UNS).")
    L.append("- **Estado:** **propuesta** (diseño nuevo). No se ha presentado al Comité de RSU, no tiene resolución "
             "y no se ha ejecutado: no hay resultados. Word y PDF completos, sin «POR CONFIRMAR»; los supuestos "
             "están solo en este `.md`.")
    L.append("")
    L.append("**Título:** %s." % TITULO)
    L.append("")
    L.append("## Estructura seguida")
    L.append("Secciones, numeración y presentación de los dos ejemplos del docente "
             "([ejemplo 1](../../material-del-profe/rsu-ejemplo-1-charla-tecnologia/rsu-ejemplo-1-charla-tecnologia.md), "
             "[ejemplo 2](../../material-del-profe/rsu-ejemplo-2-ajedrez-con-ia/rsu-ejemplo-2-ajedrez-con-ia.md)): "
             "carátula con logo, índice, índice de tablas, «Diseño del proyecto…», secciones I–VIII, tablas en "
             "APA (número, título en cursiva, «Nota. Elaboración propia.»), Times New Roman 12, interlineado 1,5, "
             "A4 vertical con márgenes de 2,5/3 cm (los del ejemplo 2).")
    L.append("")
    L.append("| Parte del documento | Anexo N.° 1 del reglamento / ejemplos | Contenido |")
    L.append("|---|---|---|")
    filas = [
        ("Carátula", "Ejemplos 1 y 2", "UNS, Facultad, Escuela, logo, título, 3 colaboradores, docente responsable, Nuevo Chimbote, 2026-II"),
        ("Índice e índice de tablas", "Ejemplos 1 y 2", "Con número de página (tomado del PDF exportado)"),
        ("I. Datos generales (1.1–1.9)", "Anexo 1, punto 1", "Facultad de Ingeniería · Dpto. de Ing. Civil y Sistemas · %s · sin corresponsables · Tabla 1 con los 3 estudiantes y su función · aula de la Facultad de Ingeniería (campus Nuevo Chimbote) · %d beneficiarios · 30 días (16/11–15/12/2026), taller el sáb. 05/12/2026" % (DOCENTE, N_BENEF)),
        ("II. Justificación (2.1–2.3)", "Anexo 1, punto 2", "Legal: Ley 30220 (art. 124), reglamento RSU (arts. 6.6, 6.7, 7.3), Ley 29783 y D.S. 005-2012-TR, Ley 29733, ODS 8.8 y 4.4 · Importancia: por qué, para qué y vínculo con NewBit · Antecedentes: 6 párrafos (Önal y Dandıl 2021, 2025, 2024a/b; Machaca 2019; Paucara y Rodríguez 2024; prototipo NewBit)"),
        ("III. Problemática y objetivos", "Anexo 1, punto 3", "Caracterización sin cifras locales (el cuestionario de entrada es la línea base) · 1 objetivo general · 4 específicos (OE1–OE4)"),
        ("IV. Metodología (4.1–4.5)", "Anexo 1, punto 4", "Preexperimental pre/post de un grupo, enfoque mixto · técnicas · 7 procedimientos · Tabla 2: programa del taller (4 módulos, 3 h) · beneficios por grupo · instrumentos · Tabla 3: indicadores con meta **propuesta**"),
        ("V. Cronograma", "Anexo 1, punto 5", "Tabla 4: Gantt real (barras sombreadas por semana y el hito del 05/12 en rojo), no una tabla de X"),
        ("VI. Presupuesto y financiamiento", "Anexo 1, punto 6", "Tabla 5: %s · recursos sin costo · recursos propios (%s por estudiante)" % (soles(total_presupuesto()), soles(total_presupuesto() / 3))),
        ("VII. Estrategias", "Anexo 1, punto 7", "Coordinación, convocatoria, participación, certificación, ética y privacidad, contingencia, sostenibilidad"),
        ("VIII. Referencias", "Anexo 1, punto 8 + APA (disposición complementaria)", "%d referencias en APA 7" % len(REFERENCIAS)),
        ("Anexos A y B", "No están en los ejemplos (agregado)", "A: cuestionario de entrada y salida (8 preguntas + 3 de percepción, con clave) · B: ficha de inscripción y consentimiento"),
    ]
    for f in filas:
        L.append("| %s | %s | %s |" % f)
    L.append("")
    L.append("## Resumen del contenido")
    L.append("- **Actividad:** taller presencial de 3 h (sáb. 05/12/2026, 9:00–12:00) para %d trabajadores, supervisores "
             "y aprendices de talleres metalmecánicos de Chimbote y Nuevo Chimbote. Cuatro módulos: actos y condiciones "
             "inseguras (tránsito fuera de la vía peatonal y panel eléctrico abierto) · cómo «ve» una cámara inteligente · "
             "demostración del prototipo NewBit con clips del dataset público (Önal y Dandıl, 2024a; CC BY 4.0) y ejercicio "
             "«¿Seguro o inseguro?» · privacidad y uso responsable." % N_BENEF)
    L.append("- **Objetivo general:** " + m(OBJ_GENERAL))
    L.append("- **Medición:** mismo cuestionario antes y después (Anexo A) + encuesta de satisfacción. Metas propuestas "
             "en la Tabla 3; no hay resultados porque no se ha ejecutado.")
    L.append("- **Funciones:** Albert Chumacero coordina, convoca y conduce el módulo 1; Anthony Lopez prepara y conduce "
             "la demostración (módulos 2 y 3); Luis Salazar se encarga de los instrumentos, el módulo 4 y el informe.")
    L.append("- **Presupuesto:** %s (materiales, refrigerio para 34 personas, movilidad e imprevistos), con recursos "
             "propios. Es aparte de los S/ 20,768 del proyecto de software PY-NB-001." % soles(total_presupuesto()))
    L.append("")
    L.append("**Cronograma (Tabla 4):**")
    L.append("")
    L.append("| N.° | Actividad | Responsable | " + " | ".join(s.replace("\n", " ") for s in SEMANAS) + " |")
    L.append("|---|---|---|---|---|---|---|")
    for k, (act, resp, sem, hito) in enumerate(CRONOGRAMA, 1):
        cel = []
        for s in range(1, 5):
            cel.append("◆ 05/12" if hito == s else ("■" if s in sem else ""))
        L.append("| %d | %s | %s | %s |" % (k, act, resp, " | ".join(cel)))
    L.append("")
    L.append("## Supuestos y decisiones (solo aquí, no en el Word)")
    sup = [
        "**Es una propuesta.** El docente envió el reglamento y los ejemplos en la semana 5 sin una instrucción escrita "
        "(ver `curso/contexto-del-curso.md`). Si pide otro formato, otra fecha o que no se ejecute, se ajusta en las "
        "constantes del generador y se regenera.",
        "**Beneficiarios genéricos:** no hay convenio ni taller con nombre propio. Se escribió «talleres metalmecánicos "
        "de Chimbote y Nuevo Chimbote convocados por el equipo». La cifra de %d es una meta de convocatoria, igual en "
        "1.7 y 4.4 (el ejemplo 2 tenía cifras distintas)." % N_BENEF,
        "**Unidad de desarrollo:** un aula de la Facultad de Ingeniería de la UNS (campus Nuevo Chimbote), porque tiene "
        "proyector y no exige permiso de una empresa. Supone que la Escuela presta el aula un sábado.",
        "**Fechas:** proyecto del 16/11 al 15/12/2026 (30 días, como los ejemplos), taller el sáb. 05/12, después del "
        "Lanzamiento 1 (13/11) y del fin planificado del Sprint 3 (27/11), y antes del cierre del curso (18/12). El "
        "informe cabe en los 15 días del art. 18. **Riesgo real:** el art. 16 prohíbe ejecutar sin resolución del "
        "VRAC, y una semana para aval, aprobación y resolución es poco; el documento lo cubre con la estrategia de "
        "contingencia (reprogramar con la DECRS).",
        "**Qué se mostrará del prototipo:** solo lo terminado y probado a la fecha. Hoy (09/11) está la etapa 1 "
        "(ingesta, submuestreo, detección de personas con YOLOv8n, clip). La clasificación con ConvLSTM es del Sprint 3; "
        "si no está lista, el ejercicio usa las etiquetas del dataset. No se citan métricas propias.",
        "**Privacidad:** sin grabación de video ni reconocimiento facial; fotos generales solo con consentimiento. Es "
        "coherente con el Acta (fuera de alcance: reconocimiento facial) y con la Ley 29733.",
        "**Docentes corresponsables:** ninguno. Los ejemplos repiten al Dr. Daza como responsable y corresponsable; el "
        "reglamento los trata como roles distintos y no exige corresponsables.",
        "**Departamento académico y ORCID del docente:** tomados de los ejemplos del docente. No se pusieron correos ni "
        "códigos de los estudiantes para no inventarlos (los ejemplos los traen; se pueden añadir en `ESTUDIANTES`).",
        "**Presupuesto:** precios de mercado local estimados (impresión S/ 0,10 por hoja, refrigerio S/ 3,50, pasaje "
        "S/ 5,00). Los ejemplos tenían S/ 85 y S/ 120; aquí sube por el refrigerio y las constancias para 30 personas.",
        "**Caracterización:** sin estadísticas locales de accidentes (no hay una fuente verificada en el repo). La "
        "mención de la pesca, la siderurgia y la construcción naval de Chimbote es contexto general, sin cifras.",
        "**Funciones de cada estudiante y metas de la Tabla 3:** propuestas del documento; el equipo puede cambiarlas.",
        "**Anexos A y B:** no están en los ejemplos; se agregaron porque la metodología se apoya en esos instrumentos.",
    ]
    for s in sup:
        L.append("- " + s)
    L.append("")
    L.append("## Cómo regenerar")
    L.append("1. `/Users/anthony/Documents/Projects/NewBit/.venv/bin/python -I generar_rsu.py` (escribe el `.docx` y este `.md`).")
    L.append("2. Exportar el PDF con Pages (AppleScript: `open` del `.docx` y `export … as PDF`).")
    L.append("3. Volver a correr el generador y exportar otra vez: el índice toma los números de página del PDF.")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")


if __name__ == "__main__":
    pdf = os.path.join(HERE, BASE + ".pdf")
    pags = leer_paginas(pdf)
    toc, tablas = build_docx(os.path.join(HERE, BASE + ".docx"), pags)
    n = 0
    if os.path.exists(pdf):
        try:
            import pymupdf
            n = len(pymupdf.open(pdf))
        except Exception:
            n = 0
    build_md(os.path.join(HERE, BASE + ".md"), pags, n)
    print("OK:", BASE + ".docx", BASE + ".md", "· páginas en el índice:", len(pags), "/", len(toc) + len(tablas) + 1)
