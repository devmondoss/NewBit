# NewBit – Arquitectura del Proyecto (presentación)

- **Fuente:** `NewBit_Arquitectura_Proyecto.pptx` (24 diapositivas)
- **Semana:** 3 · **Tipo:** presentación de arquitectura derivada de `archivo/vigia-industrial/semana-02/VisionOps_Lean_Kanban_Scrum_v01/VisionOps_Lean_Kanban_Scrum_v01.md` (cada diapositiva cita sus páginas)
- **Subtítulo:** *Una plataforma de Computer Vision que convierte cámaras existentes en sensores inteligentes configurables para operaciones industriales.* Arquitectura · MVP · Stack · Validación · Roadmap.
- **Etiquetas:** Computer Vision · Industrial · Event-driven

## 1–3. Visión, problema y usuarios
- NewBit **no es un detector de cascos**: es una capa configurable entre cámaras y operaciones. Entrada: cámaras existentes, webcam, MP4, RTSP después. Inteligencia: detección + tracking + zonas + reglas. Salida: eventos únicos con evidencia y metadata.
- **Tesis:** el valor no está en ver cajas de detección sino en transformar video en eventos correctos, a tiempo y accionables.
- **Problema:** tener CCTV no equivale a detección operacional continua; hay una brecha entre "lo que ocurrió" y "cuándo alguien se enteró". Oportunidad: usar cámaras existentes como infraestructura sensorial **sin reemplazar** el sistema SST.
- **Usuarios:** Supervisor SST, Supervisor operativo, Jefatura/analítica SST, Administrador técnico.

## 4. Abstracción central
`CAMERA → DETECTOR → TRACK → ZONE → RULE → EVENT → ACTION`. El núcleo entiende objetos, tracks, zonas y reglas, **no "casco"**. Un nuevo caso (EPP, zonas restringidas, persona–montacargas, permanencia, conteos) = otra regla/zona/clases, no rehacer backend, BD ni dashboard.

## 5–6. Arquitectura end-to-end y módulos
Flujo: Webcam/MP4 (RTSP después) → OpenCV/FFmpeg → YOLO → ByteTrack → Zone + Rule Engine → Event Engine + Snapshot → FastAPI → PostgreSQL → Next.js Dashboard.
1. Capturar frames · 2. Inferir objetos · 3. Mantener IDs temporales · 4. Evaluar zona + condición · 5. Deduplicar y emitir evento · 6. Persistir + visualizar.

| # | Módulo | Responsabilidad | Tecnología |
|---|---|---|---|
| 01 | Video Ingestion | Abre la fuente, normaliza frames, expone estado de cámara | OpenCV / FFmpeg |
| 02 | Detection | Detecta clases relevantes por frame | YOLO nano o equivalente |
| 03 | Tracking | ID temporal por objeto/persona | ByteTrack |
| 04 | Zone Engine | Determina si un track entra, sale o permanece en una ROI | Polígonos + geometría |
| 05 | Rule Engine | Combina clase, zona, tiempo y atributos | Python configurable |
| 06 | Event Engine | Persistencia, dedup y cooldown; crea evidencia | Contrato de evento |
| 07 | API / Data / UI | Persiste, consulta y presenta | FastAPI + PostgreSQL + Next.js |

## 7. Ingestión de video
MVP: archivo MP4, webcam 720p, procesamiento local, estado de la fuente. Después: IP 1080p, RTSP, Ethernet estable, GStreamer/DeepStream.
Contrato interno **propuesto** (no está en el documento base): `FramePacket = { camera_id, timestamp, frame, width, height, fps, source_status }`.

## 8. Detección
El detector responde "qué hay en el frame" (clase + bbox + confidence); **todavía no es un evento**. Modelo inicial: Ultralytics YOLO nano; dataset de arranque Construction-PPE (1,416 imágenes, 11 clases) que acelera pero no valida el entorno final. Límites: iluminación, oclusión, objetos pequeños, domain shift. Regla: **evaluar eventos, no frames aislados**.

## 9. Tracking
Sin tracking cada frame parece una persona nueva; con ByteTrack un mismo ID acumula contexto y tiempo. Habilita **persistencia temporal, cooldown por track/regla y deduplicación**. El MVP exige un único evento por persona/regla durante el cooldown.

## 10. Zonas y Rule Engine
Zona = polígono virtual asociado a una cámara. Regla = objeto/atributo + zona + ventana temporal + condición + cooldown. Resultado true/false por track.
Ejemplo piloto: `track.class = person` ∧ `inside(zone_A)` ∧ `helmet = false` ∧ `duration ≥ T` → **EVENT**.

## 11. Event Engine
Condición activa → ventana temporal → cooldown/dedup → snapshot + metadata → evento persistido.
Contrato mínimo: `timestamp, camera_id, zone_id, rule_id, track_id, confidence, snapshot_uri, status` (*track_id* y *status* son propuestas de implementación).

## 12–13. Backend, API, datos y dashboard
- Entidades: Camera, Zone, Rule, Event, Evidence. Operaciones API: registrar fuente, guardar/editar zona, asociar regla, consultar eventos, filtrar historial. Metadata en PostgreSQL; snapshots separados a futuro (object storage).
- Dashboard (mockup conceptual): pestañas Eventos · Cámaras · Zonas · Reglas · Historial; lista de eventos recientes (ej. "Zona A · Sin casco · Regla EPP-01"); configuración, operación (evidencia y contexto) e historial filtrable por fecha, cámara, zona y regla.

## 14–16. Despliegue y evolución
- **MVP:** laptop/desktop con Docker Compose (CV Engine + FastAPI + PostgreSQL + Next.js), 16 GB RAM, webcam 720p o MP4, GPU no obligatoria, red no crítica.
- **Escalado:** DeepStream/GStreamer, TensorRT, ByteTrack/BoT-SORT, servicio de reglas configurable, event bus si el volumen lo exige, PostgreSQL + object storage, edge node + cloud. **Principio:** mover complejidad solo cuando el volumen lo justifique.

## 17–19. MVP, piloto y validación
- **Entra:** fuente MP4/webcam · persona y casco con modelo ligero · ID temporal · zona + regla · evento único con ventana y cooldown · metadata + evidencia + historial.
- **No entra:** biometría · chat IA · heatmaps sin decisión · app móvil · 15 clases de EPP en S1 · Kafka/K8s/microservicios · decisiones disciplinarias automáticas. Criterio: todo feature debe mejorar corrección, oportunidad o accionabilidad del evento.
- **Piloto:** "persona entra en zona operacional sin casco requerido y la condición persiste la ventana mínima" (cámara → YOLO → ByteTrack → Zone → Rule → Event → supervisor). Si no genera acción útil, no se escala.
- **Validación:** valor ≥ 80 % · latencia ≤ 5 s · ≤ 1 evento por persona/regla en cooldown · precisión ≥ 90 % (≥ 30 escenarios) · recall ≥ 85 % · estabilidad 30 min. La métrica principal es el **desempeño del evento completo, no el mAP**.

## 20–21. Riesgos y privacidad
- Riesgos y controles: falsos positivos (ventana + tracking + N frames + cooldown) · oclusión/distancia (ROI, cámara adecuada) · iluminación (muestras locales, IR) · domain shift (fine-tuning) · alert fatigue (severidad, dedup, rate limits) · cámara inadecuada (auditar antes de culpar al modelo).
- Gobernanza: sin biometría · minimización (snapshots, no video continuo) · propósito seguridad/prevención · roles, logs, retención configurable · aviso de videovigilancia · **humano en el loop** (nunca sanción automática). ANPD tiene directiva específica.

## 22–23. Plan de construcción y roadmap
Discovery → S1 (video → persona/casco) → S2 (tracking + zona + regla + evento + dedup) → S3 (FastAPI + PostgreSQL + evidencia + contrato) → S4 (dashboard + e2e + métricas + feedback). DoD: criterios cumplidos, prueba reproducible, código integrado, demo e2e, limitaciones documentadas, evidencia de valor/aprendizaje.
**Roadmap:** MVP (1 cámara · 1 zona · 1 regla) → v2 (múltiples cámaras y reglas) → v3 (edge node + almacenamiento de evidencia) → v4 (multi-site / multi-tenant).

## 24. Referencias
Mismas 13 del discovery (Ley 29783, El Peruano, reportes SIDERPERU 2023/2024, papers de PPE, NVIDIA, Ultralytics, ANPD). Nota: el documento base "VISIONOPS INDUSTRIAL | Product Discovery v0.1" fue **renombrado NEWBIT**.

## Análisis

- **Es una traducción fiel del discovery a arquitectura**, con aportes propios claramente marcados como propuestas (FramePacket, `track_id`/`status` del evento).
- **Decisión de diseño más importante:** el núcleo es agnóstico del caso de uso (cámara → detector → track → zona → regla → evento). Es lo que lo diferencia de "un detector de cascos" y lo hace escalable; también es el mayor riesgo de sobre-ingeniería si se construye antes de validar la primera regla.
- **Camino de menor riesgo:** el plan de 4 sprints construye primero percepción, luego lógica, luego producto; el riesgo (falsos positivos/dedup) se ataca en S2, antes de tener UI.
- **Vacíos:** sin diagramas de datos (esquema de BD), sin contratos de API ni estimación de FPS/latencia por etapa; la meta de ≤ 5 s de latencia no está desglosada por módulo. El discovery con usuarios sigue pendiente y condiciona todo.
