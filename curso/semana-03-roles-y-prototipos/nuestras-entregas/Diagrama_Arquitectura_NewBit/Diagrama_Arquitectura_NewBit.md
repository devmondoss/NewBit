# Diagrama de arquitectura de NewBit: "Cómo funciona" (HTML)

- **Archivo:** `Diagrama_Arquitectura_NewBit.html` (esta carpeta). Se abre con doble clic en el navegador; no necesita internet salvo la tipografía Inter, que tiene respaldo del sistema.
- **Tarea:** diagrama de flujo de la arquitectura de la semana 3. Reemplaza las infografías de VIGIA (`descartado/vigia-industrial/semana-03/infografias/`) para el proyecto actual.
- **Fecha:** 12/10/2026 · coherente con el Acta (RF-01…RF-07, 2 conductas, 4 sprints), Roles (5 perfiles) y Épicas.

## Contenido
1. **Encabezado:** NewBit + título de la plataforma + PY-NB-001, Scrum en 4 sprints, UNS 2026-II.
2. **Flujo principal (7 etapas):** video MP4 → detección YOLOv4 → selección de frames → secuencias → clasificación ConvLSTM → alerta con evidencia → validación humana y registro. Cada etapa indica su requisito (RF) y el rol que interviene.
3. **Conductas:** tránsito fuera de la vía peatonal y panel eléctrico abierto, con sus casos seguros de contraste.
4. **Entrenamiento y evaluación:** dataset público (CC BY 4.0) → anotación → YOLOv4 → ConvLSTM → evaluación (directa vs pipeline) → modelos versionados, que alimentan las etapas 02 y 05.
5. **Paneles:** quién usa NewBit (5 roles), qué se construye en cada sprint, y tecnología y principios (la conducta y no el frame, validación humana, privacidad, reproducibilidad).

## Notas
- Responsivo: 7 columnas en pantalla grande, 2 en tablet y 1 en celular. Para presentar, abrirlo a pantalla completa en una laptop.
- No incluye cifras de desempeño: las metas se fijan con la línea base del Sprint 3.
