# Guía de investigación – Unsafe-Net

- **Fecha:** 12/10/2026 (semana 5) · **Para:** Anthony y Luis Fernando.
- **Objetivo:** reunir lo mínimo para cerrar las decisiones abiertas y redactar los formatos (Acta, Stakeholders, Roles, Épicas, Justificación). No hace falta investigar todo: cada bloque dice **qué traer**.
- **Cómo entregarlo:** pegar notas o archivos en `proyecto/investigacion/`; cada archivo en su carpeta con su `.md` (ficha rápida si es largo).

> **Estado (12/10):** A, B y C quedan cubiertos por `UnsafeNet_Research_Pack/` (dataset público en Mendeley; plan de réplica nivel B); D está cubierto en parte (stack y hardware en sus archivos 11 y 12). **Faltan E, F y G.**

## Prioridad 1 – Decide si el proyecto es viable (hacer primero)

### A. El artículo original
Hasta ahora solo se leyó un PDF que lo resume, no el artículo.
- **Conseguirlo:** *Unsafe-Net: YOLO v4 and ConvLSTM based computer vision system for real-time detection of unsafe behaviours in workplace* — Önal y Dandıl, *Multimedia Tools and Applications*, DOI `10.1007/s11042-024-19276-8`. Probar: Google Scholar, ResearchGate (pedirlo a los autores), biblioteca/VPN de la UNS, el docente.
- **Anotar:**
  - Qué detecta YOLOv4 exactamente (clases) y cómo elige los frames que pasan al ConvLSTM.
  - ConvLSTM: cuántos frames por clip, resolución de entrada, capas, épocas, optimizador.
  - Dataset: cuántos clips por conducta, duración de cada clip, cómo etiquetaron, división train/test.
  - Resultados **por clase** (no solo el 95.81 % promedio), falsos positivos, hardware y FPS.
  - Cómo hicieron el piloto y la validación con el experto.
  - **¿Publicaron código o dataset?** (buscar en el artículo, GitHub y Papers with Code).
- **Traer:** el PDF + respuestas a esa lista.

### B. Los datos de video (mayor riesgo)
Sin video etiquetado por conducta no hay proyecto. Buscar tres caminos y traer pros y contras de cada uno:
1. **Dataset público:** buscar "unsafe behavior dataset video", "worker unsafe action recognition dataset", "forklift dataset", "construction worker action recognition dataset", "pedestrian walkway violation dataset". Para cada uno: enlace, licencia, ¿es video o solo imágenes?, clases, tamaño, ¿está etiquetado por acción?
2. **Grabación propia simulada:** ¿hay un taller o laboratorio en la UNS donde grabar escenas actuadas (cruzar una zona marcada, abrir un tablero)? ¿Cuántos voluntarios? Consentimiento escrito.
3. **Planta real** (Chimbote: siderurgia, pesqueras, construcción): ¿hay algún contacto? ¿permitirían grabar o compartir video?
- **Traer:** tabla de opciones + cuál parece realista.

### C. Qué conductas detectar (alcance)
Las 4 del artículo: Safe Walkway Violation · Unauthorized Intervention · Opened Panel Cover · Carrying Overload with Forklift.
- Para cada una: ¿se puede conseguir o grabar video de ella? ¿cómo se ve en cámara? ¿cuánto dura?
- Propuesta a validar: empezar con **1–2 conductas** (p. ej. invasión de zona peatonal y panel abierto, que se pueden simular) y dejar el resto fuera de alcance.
- **Traer:** las conductas elegidas, con una definición de una línea cada una ("se considera X cuando…").

## Prioridad 2 – Diseño técnico

### D. Tecnología
- **Alternativas actuales** a YOLOv4 + ConvLSTM: YOLOv8/YOLO11 + tracking (ByteTrack) + clasificador temporal (LSTM sobre esqueleto/pose, 3D-CNN, X3D, SlowFast, VideoMAE). Para 2–3 opciones: dificultad, si hay código listo, GPU que necesita.
- **Dónde entrenar:** Google Colab, Kaggle (GPU gratis, límites de horas), PC propia (¿qué GPU tienen?), nube de pago (costo por hora).
- **Etiquetado de video:** CVAT o Label Studio; cuánto tarda etiquetar 1 hora de video.
- **Traer:** opción recomendada + dónde se entrena + herramienta de etiquetado.

## Prioridad 3 – Para los formatos del curso

### E. Contexto y justificación (Acta, Justificación)
- Estadísticas de accidentes de trabajo en Perú (MTPE, notificaciones de accidentes; año más reciente) y, si existe, de Áncash.
- Marco legal: Ley 29783 de Seguridad y Salud en el Trabajo; Ley 29733 de Protección de Datos Personales (videovigilancia de trabajadores).
- **Organización del caso:** ¿empresa real o caso propuesto? (El Acta de VIGIA usó SIDERPERU como caso propuesto.)
- 3–5 trabajos parecidos para "Antecedentes" (título, año, qué hicieron, resultado), en APA.
- **Traer:** cifras con fuente y enlace, y la organización elegida.

### F. Interesados y roles (FGAP020, FGAP030)
- ¿Quién usaría el sistema? (supervisor de SST, jefe de planta, operario, administrador de TI). ¿Quién decide y quién paga?
- Si pueden, una conversación corta con alguien de SST (aunque sea un conocido) sobre qué conductas les preocupan y qué harían con una alerta.
- **Traer:** lista de interesados con su interés en el proyecto, y 3–4 roles de usuario.

### G. Costos (Acta, Justificación)
- Cámara IP o webcam, GPU en nube por hora, hosting, dominio.
- **Traer:** precios con enlace (en soles si se puede).

## Al terminar
Con A–C se cierran las decisiones; con D–G se redactan los formatos. Siguiente paso: una **ficha de definición** de 1 página (nombre, problema, alcance, conductas, datos, stack, equipo) de la que salen todos los formatos.
