# FGAP040 – Épicas de NewBit: versión del equipo

- **Archivos** (esta carpeta): `FGAP040_Epicas_NewBit_equipo.docx` y `.pdf`. Llegaron el 12/10/2026 con el nombre de la plantilla del docente (`FGAP040_Epicas_Proyecto_Retinopatia_Diabetica`), pero el **contenido es del equipo**. Se renombraron para no confundirlos con el ejemplo de `docs/semana-04/`.
- **Tipo:** transcripción de las épicas e historias (documento corto).
- **Otra versión:** `../FGAP040_Epicas_NewBit/`, armada antes (6 épicas por rol de usuario y 26 títulos de HU). **Esta versión del equipo es la que vale** para el proyecto.

## Proyecto
PY-NB-001 – NewBit: plataforma de Computer Vision que convierte cámaras existentes en sensores inteligentes configurables para operaciones industriales.

## Épicas
| ID | Épica | Rol | Debería… a fin de… |
|---|---|---|---|
| EP01 | Ingestión y preprocesamiento de video | Investigador | Cargar y normalizar secuencias de video → datos listos para extraer características |
| EP02 | Extracción espacial y filtrado inteligente (YOLOv4) | Investigador | Detectar sujetos y descartar frames irrelevantes → menos carga y secuencias más cortas |
| EP03 | Segmentación de secuencias temporales | Investigador | Agrupar frames filtrados en clips → una sola acción por clip |
| EP04 | Clasificación espacio-temporal (ConvLSTM) *(central)* | Investigador | Clasificar el clip con ConvLSTM → saber si la conducta es insegura |
| EP05 | Interfaz gráfica (GUI) y registro de validación | Evaluador del sistema | Ver el video con etiquetas y registrar alertas → validar resultados |
| EP06 | Administración, seguridad y trazabilidad | Administrador técnico | Gestionar parámetros y umbrales → controlar la experimentación |

## Historias de usuario (12)
- **EP01:** HU01 cargar un video industrial · HU02 fragmentarlo en frames.
- **EP02:** HU03 YOLOv4 identifica trabajadores por frame · HU04 descartar frames sin trabajadores.
- **EP03:** HU05 agrupar frames en clips de tamaño fijo · HU06 descartar clips sin tiempo mínimo de acción.
- **EP04:** HU07 procesar el clip con ConvLSTM · HU08 asignar la etiqueta "seguro" o "inseguro".
- **EP05:** HU09 ver el video en la GUI con un recuadro de color según el riesgo · HU10 activar una alerta ante una conducta insegura.
- **EP06:** HU11 modificar el umbral de confianza de YOLOv4 · HU12 ver el log de tiempos de procesamiento.

## Análisis
**Corregido el 12/10/2026** en el Word y el PDF, para que coincida con los demás entregables:
1. El código y el nombre pasan a PY-NB-001 con el título de la plataforma (antes: PY-NEWBIT-001 "NewBit para el reconocimiento espacio-temporal…").
2. Se quitan "el paper" y "la réplica": EP02 ahora dice "el primer gran aporte de NewBit", y EP05 y EP06 hablan de "el sistema".
3. Control de versiones: hecho por Anthony Lopez / Luis Salazar, revisado por Anthony Lopez (SM), aprobado por Albert Chumacero (PO), 12/10/2026. Se agregaron los nombres del equipo en la carátula.
4. EP06 usa un solo nombre: "Administración, seguridad y trazabilidad".

Siguen pendientes en la carátula: ciclo, aula, turno, fecha y firma. Los roles de las épicas (investigador, evaluador del sistema, administrador técnico) son distintos de los perfiles de FGAP030; se dejaron como los escribió el equipo.
