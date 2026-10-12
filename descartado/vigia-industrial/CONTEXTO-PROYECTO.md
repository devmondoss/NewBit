# Contexto del proyecto – VIGIA Industrial / NewBit

> ⚠️ **EN CAMBIO.** El equipo está cambiando de proyecto (05/10/2026). Todo lo de esta carpeta corresponde al proyecto **anterior** y puede quedar desactualizado. No se profundiza hasta que se defina el nuevo.

**Es el proyecto del equipo para el curso.** Tres nombres para lo mismo: *VisionOps Industrial* (discovery), *NewBit* (arquitectura y repo), *VIGIA Industrial* (Acta y Roles formales).

## En una línea
Plataforma de Computer Vision que convierte cámaras existentes en sensores configurables: **video → eventos operativos correctos, a tiempo y accionables**. El EPP es solo el primer caso de uso.

## Equipo e interesados (ficticios salvo el equipo)
- **Equipo ejecutor (2):** Luis Fernando Elias Salazar Diaz (líder, Computer Vision, datos) · Anthony Lopez Yrribarren (full stack, integración, seguridad, pruebas).
- **Interesados ficticios del caso:** Valeria Rojas Medina (PO propuesta) · Ricardo Salcedo Paredes (sponsor propuesto, gerente de operaciones) · Mariana Torres Cárdenas (SST) · Jorge Ponce Aguilar (TI). No expresan vínculo real con SIDERPERU.

## Alcance formal (Acta, 21/09/2026)
- **4 cámaras IP por RTSP, hasta 8 zonas poligonales** con horarios y reglas configurables desde la web.
- **3 reglas del MVP:** ausencia de casco, ausencia de chaleco, ingreso a zona restringida. Fuera: lentes, guantes, reconocimiento facial, control de maquinaria, integración con ERP.
- Alertas en panel y por correo; indicadores y **CSV**; roles administrador / supervisor / consulta; auditoría de cambios.
- Calidad: 4 flujos a ≥ 5 fps; latencia p95 ≤ 5 s; disponibilidad ≥ 95 % en un piloto de 2 semanas; HTTPS, evidencias cifradas, respaldo diario; retención 30 días (evidencias) y 180 días (métricas).
- Aceptación propuesta: precisión ≥ 90 % y sensibilidad ≥ 85 % por tipo de evento, con ≥ 100 positivos por tipo y 10 h de video negativo; evaluación por eventos con tolerancia de 2 s; datos separados por secuencia y día.
- **Presupuesto:** S/ 30,820 (26,800 + 15 % contingencia); S/ 20,800 son dedicación valorizada; **caja máxima S/ 10,020**.
- **Cronograma:** preparación 21/09–02/10 · S1 05–16/10 · S2 19–30/10 · S3 02–13/11 · S4 16–27/11 · S5 30/11–11/12 · S6 piloto 14–25/12 · ajustes 28/12–06/01 · cierre 07–08/01/2027.
- Piloto en modo observación; sin acceso a planta no se acredita el piloto industrial.

## Primer experimento (discovery y presentación)
**1 cámara · 1 zona · 1 regla** ("persona en zona sin casco durante N s"). Queda como primera iteración; el Acta lo amplía a 4/8/3. Si el evento no lleva a una acción útil del supervisor, no se escala (gate GO / PIVOT / STOP).

## Decisiones técnicas
- Núcleo agnóstico: `Camera → Detector → Track → Zone → Rule → Event → Action`; no reemplaza el sistema SST (SIDERPERU usa SSMA).
- **Cadena:** Fuente (webcam/MP4/RTSP) → Captura (OpenCV) → Detección (YOLO nano) → Tracking (ByteTrack) → Reglas (zona + N s + cooldown) → API (FastAPI) → Datos (PostgreSQL + snapshots) → Interfaz (Next.js) → Supervisor → Acción (SSMA). Docker Compose, sin Kafka ni Kubernetes.
- **Modelo:** YOLO nano con COCO → fine-tuning Construction-PPE (1,416 imágenes) → fine-tuning con imágenes locales; clases del experimento: persona, casco, sin casco (el Acta añade chaleco).
- **Se evalúa el evento, no el frame.** Privacidad: sin reconocimiento facial, snapshots y no video continuo, humano en el loop.

## Estado y vacíos
- Estamos en el **Sprint 1** (05–16/10): requisitos, cámaras, arquitectura y protocolo de datos (inventario de cámaras, matriz de zonas).
- **Sin evidencia** de la validación de acceso al piloto (hito del 02/10) ni de entrevistas de discovery.
- La arquitectura técnica (`descartado/vigia-industrial/semana-03/04-arquitectura-tecnica.md`) está escrita para el experimento 1-1-1; faltan chaleco, zona restringida, multi-cámara en paralelo, correo y CSV.
- Esquema de BD, API y latencia propuestos; pendientes de aprobar (7 decisiones abiertas en su §13).

## Dónde está cada cosa
- Semana 2: `descartado/vigia-industrial/semana-02/` → discovery (`01`), Acta VIGIA (`02`)
- Semana 3: `descartado/vigia-industrial/semana-03/` → arquitectura conceptual (`01`), presentación del equipo (`02`), Roles VIGIA (`03`), arquitectura técnica (`04`), `infografias/` (3 páginas HTML con fotos reales) y `referencias/`
- Semana 4: `curso/semana-04-justificacion-y-epicas/material-del-profe/` → Justificación y Épicas (curso); trabajo del Sprint 1 del proyecto
