# Diagrama de arquitectura de NewBit: "Cómo funciona" (HTML y PDF)

- **Archivos:** `Diagrama_Arquitectura_NewBit.html` (interactivo para navegador) y `Diagrama_Arquitectura_NewBit.pdf` (exportado para entrega formal e impresión).
- **Tarea:** diagrama de flujo de la arquitectura de la semana 3.
- **Fecha:** 12/10/2026 (act. 17/10/2026) · versión 2.0 · coherente con el Acta (RF-01…RF-07, 2 conductas, 4 sprints, YOLOv8), Roles (5 perfiles) y Épicas.

## Contenido
1. **Encabezado:** NewBit + título formal `PY-NB-001 – Sistema web con Visión Artificial para la detección de actos inseguros en áreas operativas de manufactura metalmecánica`, Scrum en 4 sprints, UNS 2026-II.
2. **Flujo principal (7 etapas):** video MP4 → detección espacial YOLOv8 → selección de fotogramas → secuencias → clasificación ConvLSTM → alerta con evidencia → validación humana y registro. Cada etapa indica su requisito (RF) y el rol que interviene.
3. **Conductas:** tránsito fuera de la vía peatonal y panel eléctrico abierto, con sus casos seguros de contraste.
4. **Entrenamiento y evaluación:** dataset público (CC BY 4.0) → anotación → inferencia espacial YOLOv8 → ConvLSTM → evaluación → modelos versionados.
5. **Paneles:** quién usa NewBit (5 roles del taller metalmecánico), qué se construye en cada sprint (HU11 en Sprint 2), y tecnología y principios (Python, FastAPI, OpenCV, YOLOv8, ConvLSTM).

## Notas
- Responsivo: 7 columnas en pantalla grande, 2 en tablet y 1 en celular. Para presentar, abrirlo a pantalla completa en una laptop.
- No incluye cifras de desempeño: las metas se fijan con la línea base del Sprint 3.
