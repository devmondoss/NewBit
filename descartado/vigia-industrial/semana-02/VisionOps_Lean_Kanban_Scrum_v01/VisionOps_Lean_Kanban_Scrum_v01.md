# VisionOps Industrial – Product Discovery v0.1 (base de NewBit)

- **Fuente:** `VisionOps_Lean_Kanban_Scrum_v01.pdf` (10 págs.)
- **Fecha:** 21/09/2026 · v0.1 · Lean Discovery + Kanban + Scrum · caso piloto seguridad industrial / SIDERPERU
- **Semana:** 2 · **Tipo:** discovery del proyecto propio del equipo.
- **Nombres:** este es el mismo proyecto que luego se llama **NewBit** (arquitectura, repo) y **VIGIA Industrial** (Acta y Roles formales). El Acta posterior amplía el alcance: ver `descartado/vigia-industrial/semana-02/Acta_Constitucion_VIGIA_Industrial_SIDERPERU/Acta_Constitucion_VIGIA_Industrial_SIDERPERU.md`.

## Tesis
No construir "un detector de cascos". Construir una **capa configurable que convierta video en eventos operativos accionables**. El EPP es el primer caso de uso, no el producto.

## Resumen ejecutivo
- El problema relevante no es "detectar objetos con IA" sino un **vacío operativo**: la supervisión humana e inspecciones periódicas no escalan para vigilancia continua de EPP; las cámaras producen video, no eventos accionables.
- La **Ley 29783 (SST)** obliga al empleador a dar EPP adecuado y a **verificar su uso efectivo**.
- SIDERPERU describe públicamente: inspecciones planeadas, registro de actos/condiciones subestándar en software **SSMA**, auditorías e investigación de incidentes. **No** hay información pública sobre cuántas cámaras tienen, quién las monitorea ni si se usan para EPP.
- El MVP **no reemplaza** el sistema SST: se integra antes del registro, observa una fuente, aplica una regla y genera **un evento con evidencia** para que el supervisor decida.
- **Primer experimento:** una cámara, una zona, una regla: *"persona entra en zona operacional sin casco requerido"*. Si no genera acción útil, no hay razón para escalar.

## Qué dice la evidencia
- **Obligación:** el cumplimiento de EPP es control operativo, no solo entrega de equipos (Ley 29783; El Peruano 2022).
- **SIDERPERU (Reporte 2023):** SSMA, inspecciones generales/de pre-uso/del Comité SST, auditorías, investigación de accidentes, matrices IPER (actualizables tras incidentes). **2024:** 100 % de cobertura de salud y seguridad (directos y tercerizados) y **-90 %** en tasa de gravedad vs 2023. Declara "Seguridad en primer lugar" y una estrategia digital (procesos, tecnología, data/analítica). Esto no prueba que haya monitoreo automático por cámaras.
- **Literatura de CV para EPP:** la supervisión manual continua es difícil; los sistemas reales sufren por iluminación, oclusión, fondos complejos, objetos pequeños, ángulos y *domain shift*. El reto es la cadena **percepción → razonamiento → evento → acción**, no solo un buen mAP.

## Preguntas de discovery (qué se sabe y qué no)

| Pregunta | Respuesta | Confianza | Falta validar |
|---|---|---|---|
| ¿Cómo supervisan el EPP hoy? | Inspecciones, auditorías, SSMA; no hay evidencia de verificación automatizada | Alta (proceso público) / media (día a día) | Quién inspecciona, frecuencia, % de turno cubierto |
| ¿Cuántas cámaras? | Sin dato público | Abierta | Inventario: área, tipo, resolución, RTSP/ONVIF, FPS, ubicación |
| ¿Quién las observa? | Sin dato público | Abierta | Seguridad patrimonial, SST, operaciones o tercero |
| ¿Monitoreo continuo o forense? | No afirmable | Abierta | En vivo vs revisión; pantallas por operador |
| ¿Cómo se enteran de un incumplimiento? | Vía SSMA, inspecciones, auditorías | Media-alta | Ejemplo real reciente |
| ¿Cuánto tardan en detectar y actuar? | Sin métrica pública | Abierta | Medir **T_detect** (ocurrencia→detección) y **T_action** (detección→acción) |
| ¿Qué pasa con la información? | SSMA registra y trata; accidentes activan investigación/IPER | Alta (proceso) | Tratamiento específico de un acto subestándar por EPP |
| ¿Dolor principal? | Posible brecha de continuidad/escala; no atribuible sin entrevista | Hipótesis crítica | Puede ser otro (zonas, montacargas, tiempos) |

**Hallazgo más importante:** ya existe un proceso para registrar y tratar hallazgos; el producto debe **generar eventos confiables que alimenten ese proceso**, no otro sistema de SST.

## Problema y usuarios
**Problem statement:** el cumplimiento de seguridad depende de inspecciones, observación y reportes que no cubren todos los puntos y momentos; el video solo no genera un evento listo para actuar → brecha entre "lo que ocurrió" y "cuándo alguien se enteró".

| Usuario | Job To Be Done | Señal de valor |
|---|---|---|
| Supervisor SST | Saber dónde/cuándo hay condición insegura sin ver video continuo | Revisa un evento con evidencia y decide |
| Supervisor operativo | Detectar condición que requiere intervención en su zona | Menor tiempo ocurrencia→conocimiento |
| Jefatura / analítica SST | Entender recurrencia, zonas, tipos de desvío | Prioriza controles con eventos estructurados |
| Administrador técnico | Configurar cámaras, zonas y reglas sin reescribir el sistema | Mismo núcleo para otra zona/caso |

## Hipótesis de solución
Si una transmisión de cámara se convierte automáticamente en eventos relevantes (detección + tracking + zonas + reglas), un supervisor puede detectar incumplimientos sin observar video continuo.
**Abstracción:** `Camera → Detector → Track → Zone → Rule → Event → Action`. El núcleo no debe "saber qué es un casco": evalúa objetos, zonas, atributos y reglas (reutilizable para zonas restringidas, persona–montacargas, permanencia, conteos).

## MVP
1. Registrar fuente de video (MP4 o webcam; RTSP después).
2. Detectar persona y casco con modelo ligero.
3. ID temporal por persona (tracking).
4. Zona virtual (polígono) + regla de cumplimiento.
5. **Un único evento** cuando una persona tracked entra a la zona sin casco durante una ventana mínima.
6. Guardar timestamp, cámara, zona, regla, confidence y captura de evidencia.
7. Dashboard e historial básico.

**Anti-features (fuera por ahora):** reconocimiento facial/biometría · chat o copiloto IA · heatmaps decorativos · app móvil nativa · 15 clases de EPP en el Sprint 1 · Kafka/Kubernetes/microservicios · decisiones disciplinarias automáticas.

## Criterios de éxito (objetivos de demo, no SLA)
| Dimensión | Métrica |
|---|---|
| Valor | ≥ 80 % de eventos considerados "accionables" |
| Latencia | Evento visible ≤ 5 s tras cumplirse la regla |
| Duplicados | Máx. 1 evento por persona/regla durante el cooldown |
| Precisión de evento | ≥ 90 % en ≥ 30 escenarios controlados |
| Recall de evento | ≥ 85 % en el mismo set |
| Estabilidad | 30 min continuos sin caída |
| Trazabilidad | Cada evento con timestamp, cámara, zona, regla y evidencia |

## Lean + Kanban + Scrum
Scrum organiza la construcción; Lean evita construir lo equivocado; Kanban hace visible el discovery y limita WIP. **Regla:** una hipótesis no es Product Backlog Item hasta tener evidencia suficiente.

**Tablero de discovery (WIP):** Hipótesis (sin límite) → Investigando (2) → Evidencia (2) → Decisión (2) → Ready for Backlog (3).

**Hipótesis iniciales (riesgo):** la supervisión actual no cubre todo (Alto) · existe al menos un evento que merece detección casi inmediata (Alto) · captura + contexto es evidencia útil (Medio) · el usuario acepta alertas si no hay duplicados ni falsos positivos (Alto) · EPP es el mejor wedge inicial (Alto).

## Product Backlog semilla
| ID | Historia | Criterio principal |
|---|---|---|
| US-01 | Como administrador, registrar una fuente de video | Procesa MP4/webcam y reporta estado |
| US-02 | Como supervisor, definir una zona y el EPP requerido | Zona editable, regla asociada |
| US-03 | Como supervisor, detectar persona sin casco al entrar a la zona | Evento solo si la condición persiste la ventana configurada |
| US-04 | Como supervisor, recibir un único evento con evidencia y contexto | Sin duplicados en cooldown; snapshot + metadata |
| US-05 | Como supervisor, revisar historial | Filtra por fecha, cámara, zona y regla |
| US-06 | Como equipo, medir precisión, recall, duplicados y latencia | Reporte/dashboard reproducible |

**Sprints:** Discovery (mapa del proceso, 2+ entrevistas, pain priorizado, criterio de éxito) → S1 video→detección persona/casco → S2 tracking+zona+regla+evento local+dedup → S3 FastAPI+PostgreSQL+evidencia+contrato de evento → S4 dashboard+pruebas e2e+métricas+feedback.

**Definition of Done:** cumple criterios de aceptación con prueba reproducible · integrado en rama principal con revisión · demostrable de extremo a extremo (no solo mocks) · errores y limitaciones documentados · aporta evidencia de valor o aprendizaje.

## Stack y hardware
| Capa | Demo universitaria | Escalado |
|---|---|---|
| Video | OpenCV / FFmpeg | GStreamer / DeepStream |
| Detector | Ultralytics YOLO nano | TensorRT / modelo optimizado |
| Tracking | ByteTrack | DeepStream tracker / ByteTrack / BoT-SORT |
| Reglas | Python (zonas, condiciones, cooldown) | Servicio de reglas configurable |
| API | FastAPI | API + event bus si el volumen lo exige |
| Datos | PostgreSQL | PostgreSQL + object storage |
| Frontend | Next.js | Multi-site / multi-tenant |
| Deploy | Docker Compose local | Edge node + cloud |

**Hardware mínimo:** laptop/desktop moderno, 16 GB RAM · webcam 720p o MP4 · 10 GB libres · GPU no obligatoria con modelo nano. **Recomendado:** IP camera 1080p con RTSP, SSD, Ethernet; edge físico: Jetson Orin Nano Super (hasta 67 INT8 TOPS, 8 GB).
**Dataset de arranque:** Ultralytics *Construction-PPE* (1,416 imágenes, 11 clases); sirve para empezar, la validación real exige imágenes del entorno objetivo.

## Riesgos
| Riesgo | Control |
|---|---|
| Falsos positivos (casco oculto un frame) | Ventana temporal + tracking + N frames + cooldown; evaluar evento, no frame |
| Oclusión / distancia | Cámara bien ubicada, ROI, modelo adaptado, threshold por clase |
| Iluminación | Muestras locales, pruebas por condición, IR si corresponde |
| Domain shift (construcción → siderurgia) | Fine-tuning con datos representativos, evaluación por zona |
| Alert fatigue | Solo eventos accionables, severidad, dedup, rate limits |
| Cámara inadecuada | Auditar cámara antes de culpar al modelo |
| Privacidad | Minimización, acceso restringido, propósito, retención, aviso previo |
| Automatización punitiva | Apoyo con revisión humana antes de decisiones disciplinarias |

## Privacidad y cumplimiento
En Perú, la videovigilancia de personas identificables es tratamiento de datos personales (ANPD, Directiva 01-2020-JUS/DGTAIPD; carteles visibles; proporcionalidad en control laboral). En el MVP: sin reconocimiento facial · preferir snapshots a video continuo · propósito seguridad/prevención (no productividad) · acceso por roles, logs y retención configurable · aviso de videovigilancia antes de pruebas con personas · sin sanción automática.

## Plan de validación
**Entrevista mínima con SST/Operaciones (10 preguntas):** última vez que detectaron a alguien sin EPP y cómo se enteraron · inspecciones por turno y quién las hace · qué queda sin cobertura · qué se registra en SSMA · qué requiere intervención inmediata · cámaras en la zona (resolución, ubicación, acceso al stream, política) · quién las ve y para qué · tiempo típico desvío→acción · nivel de falso positivo que haría abandonar la alerta · qué situación repetitiva les gustaría detectar si no fuera EPP.

**Gate de decisión:**
- **GO:** evento frecuente/crítico con detección tardía + cámara/fuente viable + acción concreta posterior + falsos positivos alcanzables.
- **PIVOT:** si EPP ya está controlado pero otro problema visual duele más (zonas, persona–montacargas, permanencia, conteo, tiempos).
- **STOP:** si el evento no lleva a acción, el usuario no confía en la evidencia o la cámara no puede observar la condición.

## Conclusión del documento
No justifica una plataforma enorme desde el inicio; justifica probar un componente concreto: **observaciones visuales → eventos operativos confiables**. El hueco no es "otro software SST" sino automatizar la detección donde hoy depende de observación o reporte. Debe confirmarse con usuarios. El producto debe ganar por tres cosas: **evento correcto, a tiempo y accionable**.

**Anexo A (Mermaid):** `Problema/Hipótesis → Experimento → ¿Validado? → (No) Descartar/Reformular → Hipótesis · (Sí) Product Backlog → Sprint Planning → Sprint → Incremento → Validación con usuario → Hipótesis`.

**Referencias:** [1] Ley 29783 · [2] El Peruano 2022 (EPP) · [3] SIDERPERU Reporte 2023 · [4] SIDERPERU Reporte 2024 · [5] SIDERPERU Transformación Digital · [6] Procedia CS 245 (2024), YOLOv5 PPE · [7] AI Review (2024/25), revisión sistemática CV-PPE · [8] Computers 14(8) 312 (2025), diseño centrado en usuario · [9] NVIDIA DeepStream · [10] Ultralytics Construction-PPE · [11] NVIDIA Jetson Orin Nano Super · [12] ANPD Directiva 01-2020 · [13] ANPD/MINJUSDH criterios de videovigilancia.

## Análisis

- **Fortaleza principal:** honestidad epistémica. Distingue hechos públicos, inferencias y vacíos, y marca como "hipótesis por validar" lo que no se sabe de SIDERPERU. Los dos tiempos a medir (**T_detect** y **T_action**) dan línea base para demostrar valor.
- **Lo más accionable:** la regla "una hipótesis no entra al backlog sin evidencia" más el gate GO/PIVOT/STOP. El **discovery (entrevistas) aún está pendiente**; hoy el valor del producto es hipótesis.
- **Riesgo estructural:** casi todo el éxito depende de acceso a un usuario real y a una cámara viable; el documento reconoce que el dataset de construcción puede fallar en siderurgia (*domain shift*).
- **Métricas ambiciosas pero medibles:** precisión ≥ 90 %, recall ≥ 85 % se miden sobre *eventos* en ≥ 30 escenarios, no sobre mAP; correcto para el objetivo.
- **Relación con el curso:** es el proyecto que el equipo desarrolla para Ingeniería de Software II; usa Scrum (backlog, sprints, DoD) e historias de usuario según lo visto en la semana 2.
- **Alcance:** el MVP aquí es 1 cámara · 1 zona · 1 regla (casco). El Acta VIGIA lo amplía a 4 cámaras, 8 zonas y 3 reglas (casco, chaleco, zona restringida); este MVP queda como primer experimento.
