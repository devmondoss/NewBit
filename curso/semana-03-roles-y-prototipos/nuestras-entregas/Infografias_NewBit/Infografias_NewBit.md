# Infografías de NewBit (HTML, estilo de los ejemplos del docente)

- **Abrir:** `index.html` en el navegador. Páginas: `01-pasos-proyecto.html` (12 pasos) y `02-metodologia.html` (metodología de I+D, 8 bloques). Estilos en `estilos.css`; fotos en `assets/`.
- **Tarea:** infografía de la semana 3, en el estilo de las dos imágenes de ejemplo que compartió el docente (paneles numerados de colores, fotos con anotaciones y diagramas). Reemplaza a las de VIGIA.
- **Fecha:** 12/10/2026 · coherente con Acta, Roles, Épicas, Justificación, PPT y diagrama.
- **Todo es editable** (HTML y CSS): no son imágenes generadas con IA. Las fotos son **reales, de Wikimedia Commons, con licencia libre** (CC BY, CC BY-SA o dominio público). Los créditos están al pie de cada página.
- Las cajas de detección, la vía peatonal verde, los mapas de calor, las barras y la matriz de confusión **son ilustraciones** (marcadas así), no salidas de un modelo.

## 01 · Doce pasos
Problema → objetivo y variables → pipeline (foto de almacén con persona fuera de vía y montacargas) → tecnología (marcada como propuesta donde aplica) → entrenamiento → implementación (7 pasos) → analítica → metodología de validación → validación técnica y experta → evaluación comparativa A (ConvLSTM directo) vs B (YOLOv4 + ConvLSTM) → análisis → conclusiones. Al pie: estructura del proyecto y tecnología.

## 02 · Metodología
1 entrada de datos · 2 preprocesamiento · 3 arquitectura (rama YOLOv4: CSPDarknet53, SPP+PAN, head; rama ConvLSTM) · 4 selección de frames · 5 motor de eventos y alertas · 6 pérdidas y entrenamiento (clips por clase del dataset: 210 / 75 / 142 / 32, tomados del Research Pack, sin verificar contra Mendeley) · 7 XAI con Grad-CAM (propuesta) · 8 evaluación.

## Fotos (`assets/`)
Nuevas: `almacen-barandas`, `montacargas-pasillo`, `centro-distribucion`, `electricista-panel`, `panel-control-cerrado`. Reutilizadas de VIGIA: `camara-domo`, `camara-bullet`, `monitor-cctv`, `montacargas-casco`, `cabina-cascos`, `planta-chalecos-cascos`. Autores y licencias: al pie de cada HTML.

## Exportar
Imprimir → Guardar como PDF (A3 vertical), o captura de página completa.
