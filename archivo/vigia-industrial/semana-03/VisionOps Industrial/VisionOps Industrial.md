# Presentación del equipo – VisionOps Industrial / New Bit

- **Fuente:** `VisionOps Industrial.pptx` (15 diapositivas, modificado el 28/09/2026)
- **Semana:** 3 · **Tipo:** presentación del proyecto propio del equipo
- **Autores en portada:** Anthony Lopez Yrribarren · Salazar Diaz Luis Fernando · Curso: Software Engineering · Lean + Kanban + Scrum · Caso piloto: SIDERPERU


## Diapositiva 1

- PRODUCT DISCOVERY · MVP · V0.1
- New Bit
- Una plataforma de Computer Vision que convierte cámaras existentes en sensores inteligentes configurables para operaciones industriales.
- Caso piloto · Seguridad industrial · SIDERPERU
- Curso · Software Engineering · Lean + Kanban + Scrum
- Estudiantes · Anthony Lopez Yrribarren · Salazar Diaz Luis Fernando

## Diapositiva 2

- 01 · PROBLEMA
- Una brecha entre ocurrir y enterarse
- Normativa
- La ley exige verificar
- La Ley N.° 29783 obliga a entregar EPP adecuado y a verificar su uso efectivo, no solo a entregarlo.
- Proceso actual
- La inspección no escala
- Inspecciones, auditorías y reportes en SSMA cubren momentos, no todo el turno ni todos los puntos.
- Tecnología actual
- La cámara graba, no alerta
- El CCTV produce horas de video, pero ningún evento listo para que alguien actúe a tiempo.
- El reto no es “detectar objetos con IA”: es cubrir un vacío operativo de supervisión continua.
- Fuentes: Ley N.° 29783 · SIDERPERU, Reporte de Sostenibilidad 2023

## Diapositiva 3

- 02 · SOLUCIÓN PROPUESTA
- Convertir video en eventos accionables
- Mundo real
- Cámara
- Detección + tracking
- Regla de negocio
- Evento único + evidencia
- Supervisor actúa
- Núcleo genérico: Camera → Detector → Track → Zone → Rule → Event → Action. El EPP es el primer caso de uso.
- DECISIÓN DE ALCANCE
- 1 cámara · 1 zona · 1 regla
- «Persona entra en zona operacional sin casco requerido». Si ese evento no lleva a una acción útil, no se escala.
- LO QUE NO ES
- No reemplaza el sistema SST
- Se integra antes del registro en SSMA: entrega evidencia y alerta; la decisión sigue siendo humana.
- VisionOps Industrial · Solución

## Diapositiva 4

- 02 · SOLUCIÓN — LÓGICA DEL EVENTO
- Un evento, no un frame
- Detecta
- YOLO localiza personas y cascos en cada frame.
- Sigue
- ByteTrack mantiene un ID temporal por persona entre frames.
- Evalúa
- ¿Ese ID está dentro del polígono y sin casco durante la ventana mínima de N segundos?
- Emite
- Un único evento con snapshot; el cooldown evita duplicados.
- evento.json · ejemplo
```json
{
  "camera": "cam-01",
  "zone": "zona-operacional-A",
  "rule": "casco_requerido",
  "track_id": 17,
  "timestamp": "2026-10-12T09:41:07",
  "confidence": 0.87,
  "snapshot": "evt_0192.jpg"
}
```
- Cada evento es trazable y auditable: hora, cámara, zona, regla, confianza y evidencia.
- Valores del JSON ilustrativos

## Diapositiva 5

- 03 · CLIENTES Y BENEFICIARIOS
- Quién adopta, usa y se beneficia
- CLIENTE
- SIDERPERU (piloto)
- Valida el caso real: cámaras, zonas y su proceso SST existente.
- USUARIO
- Supervisor SST
- Ve dónde y cuándo ocurre una condición insegura sin mirar video.
- USUARIO
- Supervisor operativo
- Se entera a tiempo de lo que requiere intervención en su zona.
- USUARIO
- Jefatura / analítica SST
- Prioriza controles con eventos por zona, tipo y recurrencia.
- USUARIO
- Administrador técnico
- Configura cámaras, zonas y reglas sin reescribir el sistema.
- BENEFICIARIO
- Trabajadores
- Directos y tercerizados: menos exposición y revisión humana.
- BENEFICIARIO
- Comité SST y auditoría
- Evidencia trazable: hora, cámara, zona, regla y captura.
- FUTURO
- Otras plantas industriales
- Mismo núcleo para zonas restringidas, montacargas o permanencia.
- Cliente · Usuario · Beneficiario · Futuro

## Diapositiva 6

- 04 · ARQUITECTURA DE LA SOLUCIÓN
- Una cadena simple, de extremo a extremo
- Percepción y reglas (Python) → servicio y visualización
- Fuente
- Webcam · MP4
- RTSP después
- Captura
- OpenCV
- Lee frames
- Detección
- YOLO nano
- Persona · casco
- Tracking
- ByteTrack
- ID por persona
- Reglas
- Zona + regla
- N s + cooldown
- API
- FastAPI
- Recibe eventos
- Datos
- PostgreSQL
- + snapshots
- Interfaz
- Next.js
- Dashboard
- Usuario
- Supervisor
- Revisa y decide
- Acción
- Proceso SST
- Registro SSMA
- Deliberadamente simple: una cámara, Docker Compose local, sin Kafka ni Kubernetes. Mismo patrón que NVIDIA DeepStream: fuente → inferencia → tracking → analytics → evento.

## Diapositiva 7

- 04 · STACK TECNOLÓGICO
- Demo hoy, ruta clara para escalar
| Capa | Demo universitaria (MVP) | Escalado posterior |
|---|---|---|
| Video | OpenCV / FFmpeg | GStreamer / DeepStream |
| Detector | Ultralytics YOLO nano | TensorRT / modelo optimizado |
| Tracking | ByteTrack | DeepStream tracker / BoT-SORT |
| Reglas | Python: zonas + condiciones + cooldown | Servicio de reglas configurable |
| API | FastAPI | API + event bus si el volumen lo exige |
| Datos | PostgreSQL | PostgreSQL + object storage |
| Frontend | Next.js | Mismo frontend, multi-site / multi-tenant |
| Deploy | Docker Compose local | Edge node (p. ej. Jetson Orin Nano) + cloud |
- Hardware demo: laptop 16 GB RAM · webcam 720p o MP4 · GPU opcional

## Diapositiva 8

- 05 · MODELO YOLO — DATOS
- ¿Con qué datos se entrena?
- Fuente 1 · Construction-PPE
- 1,416
- imágenes · 11 clases
- Dataset público de Ultralytics, punto de partida. Para el MVP usamos 3 clases: persona, casco y sin casco.
- Fuente 2 · Planta objetivo
- In situ
- ángulo · luz · EPP real
- Capturas propias desde la cámara real, en distintos turnos y con el casco usado en planta. Etiquetado en CVAT o Label Studio.
- Fuente 3 · Set de prueba
- ≥ 30
- escenarios controlados
- Con y sin casco, oclusión, distancia y entradas a la zona. Separado del entrenamiento: mide eventos, no frames.
- Por qué no basta el dataset público: un modelo entrenado en construcción puede fallar en siderurgia (domain shift). El público acelera; los datos locales validan.
- Sin reconocimiento facial · capturas con aviso previo de videovigilancia

## Diapositiva 9

- 05 · MODELO YOLO — ENTRENAMIENTO
- Cómo se entrena y se valida
- Paso 1
- Base
- YOLO nano con pesos preentrenados en COCO.
- Paso 2
- Fine-tuning 1
- Construction-PPE, 3 clases, 640 px; aumentos de brillo, blur y flip.
- Paso 3
- Fine-tuning 2
- Se suman imágenes locales para corregir el domain shift.
- Paso 4
- Calibración
- Umbral por clase, ventana de N frames y cooldown.
- Paso 5
- Evaluación
- mAP por clase y precisión / recall por evento en los 30 escenarios.
- Dónde corre
- GPU para entrenar, laptop para inferir
- Entrenamos en GPU (local o en la nube). La demo infiere en CPU o Apple Silicon; luego se exporta a ONNX / TensorRT para edge.
- Qué medimos
- Modelo ≠ producto
- mAP@0.5 dice si el detector ve cascos. Precisión y recall por evento dicen si el supervisor recibe alertas confiables.
- Hiperparámetros iniciales: propuesta del equipo, ajustables

## Diapositiva 10

- 06 · CRITERIOS DE ÉXITO DEL MVP
- Cómo sabremos que funciona
- ≥ 80%
- Eventos accionables
- según el usuario evaluador
- ≤ 5 s
- Latencia
- de la regla al dashboard
- ≥ 90%
- Precisión de evento
- en un set de ≥ 30 escenarios
- ≥ 85%
- Recall de evento
- en el mismo set de prueba
- Evento por persona y regla
- durante el cooldown
- 30 min
- Estabilidad
- continuos sin caída, una fuente
- Objetivos de demo para validar el loop, no SLA de producción

## Diapositiva 11

- 06 · PLAN DE TRABAJO
- Discovery primero, luego 4 sprints
- Discovery
- Entender
- Mapa del proceso, 2+ entrevistas y pain priorizado.
- Sprint 1
- Ver
- Video → detección de persona y casco.
- Sprint 2
- Razonar
- Tracking + zona + regla con deduplicación.
- Sprint 3
- Persistir
- FastAPI, PostgreSQL, evidencia y contrato de evento.
- Sprint 4
- Mostrar y medir
- Dashboard, pruebas end-to-end, métricas y feedback.
- GO
- Evento frecuente con detección tardía, cámara viable y acción concreta.
- PIVOT
- Otro problema visual duele más: zonas, montacargas, permanencia.
- STOP
- El evento no lleva a acción o la cámara no puede ver la condición.
- Fuera del MVP: reconocimiento facial · chat IA · app móvil · 15 clases de EPP · Kafka / Kubernetes · sanciones automáticas.
- Lean evita construir lo equivocado · Scrum organiza la construcción

## Diapositiva 12

- 07 · SCRUM — CÓMO LO EJECUTAMOS
- Sprints de 2 semanas, ritmo fijo
- PRODUCT OWNER
- Anthony Lopez Yrribarren
- Prioriza el backlog por valor y valida con SST / operaciones.
- SCRUM MASTER
- Salazar Diaz Luis Fernando
- Facilita los eventos, cuida el WIP y remueve bloqueos.
- DEVELOPERS
- Ambos
- Visión, backend y frontend, con revisión cruzada de código.
- Día 1 · 2 h
- Sprint Planning
- Objetivo del sprint e historias que entran, estimadas en puntos.
- Diario · 15 min
- Daily
- Qué hice, qué haré, bloqueos. Presencial o por chat.
- Último día · 1 h
- Sprint Review
- Demo end-to-end ante el usuario evaluador y el docente.
- Último día · 30 min
- Retrospectiva
- Una mejora concreta que entra al siguiente sprint.
- Artefactos: Product Backlog (US-01 a US-06) · Sprint Backlog en tablero Kanban (Por hacer · En curso · Revisión · Hecho) · Incremento que cumple la DoD.
- Duración y roles: propuesta del equipo

## Diapositiva 13

- 07 · SCRUM — PRODUCT BACKLOG
- Seis historias que sostienen el loop
| ID | Como… | Quiero… | Criterio de aceptación | Sprint |
|---|---|---|---|---|
| US-01 | Administrador | registrar una fuente de video | Procesa MP4/webcam y reporta estado | S1 |
| US-02 | Supervisor | definir una zona y el EPP requerido | Zona guardada, editable y con regla | S2 |
| US-03 | Supervisor | detectar persona sin casco en la zona | Evento solo si persiste la ventana | S1–S2 |
| US-04 | Supervisor | un único evento con evidencia | Sin duplicados; snapshot + metadata | S2–S3 |
| US-05 | Supervisor | revisar el historial de eventos | Filtra por fecha, cámara, zona, regla | S4 |
| US-06 | Equipo | medir precisión, recall y latencia | Reporte de métricas reproducible | S4 |
- Entrada al backlog: una hipótesis solo se vuelve historia con evidencia de discovery y un criterio de aceptación.
- Priorización: primero lo que cierra el loop cámara → evento → acción; lo decorativo espera.
- Backlog semilla, deliberadamente corto

## Diapositiva 14

- 07 · SCRUM — SPRINT A SPRINT
- Qué entrega y cómo se valida cada sprint
- Sprint 1 · sem. 1–2
- El modelo ve
- US-01 · US-03
- Entregable
- Video → detecciones de persona y casco en demo controlada.
- Se valida con
- mAP por clase en el set de validación.
- Sprint 2 · sem. 3–4
- El sistema razona
- US-02 · US-03 · US-04
- Entregable
- Tracking + zona + regla con evento local deduplicado.
- Se valida con
- 5–10 eventos de prueba revisados por el usuario.
- Sprint 3 · sem. 5–6
- El evento persiste
- US-04
- Entregable
- FastAPI + PostgreSQL + snapshot y contrato de evento.
- Se valida con
- Evento consultable vía API en ≤ 5 s.
- Sprint 4 · sem. 7–8
- El supervisor decide
- US-05 · US-06
- Entregable
- Dashboard, pruebas end-to-end y reporte de métricas.
- Se valida con
- ≥ 30 escenarios, 30 min estables y feedback.
- Cada Review alimenta el siguiente Planning · semanas contadas tras el discovery

## Diapositiva 15

- CONCLUSIÓN
- Evento correcto. · A tiempo. · Accionable.
- Todo feature que no mejore una de estas tres propiedades queda fuera del MVP.
- Gracias · ¿Preguntas?

## Análisis

- **Es la presentación del discovery del equipo** (v0.1): problema, solución, usuarios, arquitectura, stack, datos y entrenamiento de YOLO, criterios de éxito, plan, Scrum, backlog (US-01 a US-06) y sprints. Reúne lo del discovery PDF y añade el plan de entrenamiento, los eventos Scrum y la asignación de roles.
- **Alcance de esta presentación: 1 cámara · 1 zona · 1 regla (casco), 4 sprints, 2 semanas por sprint.** El Acta VIGIA (semana 2) amplía el alcance a 4 cámaras, 8 zonas, 3 reglas y 6 sprints; ver `archivo/vigia-industrial/semana-02/Acta_Constitucion_VIGIA_Industrial_SIDERPERU/Acta_Constitucion_VIGIA_Industrial_SIDERPERU.md`. La presentación quedó como "primer experimento", no como alcance contractual.
- **Roles distintos al Acta:** aquí Anthony es Product Owner y Luis Scrum Master; el Acta pone como Product Owner a Valeria Rojas Medina (interesada ficticia de SIDERPERU) y a ambos como equipo ejecutor, sin Scrum Master formal. Conviene unificar.
- **Nombre:** "New Bit" en la portada, "VisionOps Industrial" en el pie de varias diapositivas y "VIGIA Industrial" en el Acta y los Roles.
- Detalle técnico completo de esta cadena en `archivo/vigia-industrial/semana-03/04-arquitectura-tecnica.md`.
