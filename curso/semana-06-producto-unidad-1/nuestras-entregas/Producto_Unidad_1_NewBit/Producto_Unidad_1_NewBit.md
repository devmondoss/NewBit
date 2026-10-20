# Producto de la Unidad I: NewBit (informe en LaTeX, APA 7) · versión 3

- **Archivos** (esta carpeta): `Producto_Unidad_1_NewBit.pdf` (39 págs., para entregar), `Producto_Unidad_1_NewBit.tex` (fuente) y `logo-uns.png` (sello de la UNS para la carátula, tomado del material del docente).
- **Semana:** 6 (pedido el 19/10/2026). **Estructura pedida:** carátula, índice, introducción, antecedentes, marco teórico, desarrollo con todos los formatos (semanas 2 a 5) y referencias. La PPT está en [`PPT_Producto_Unidad_1_NewBit`](../PPT_Producto_Unidad_1_NewBit/PPT_Producto_Unidad_1_NewBit.md).
- **Compilar:** `tectonic Producto_Unidad_1_NewBit.tex` (o XeLaTeX). Incrusta como figuras los PDF reales de las entregas (rutas relativas a `curso/semana-0X/...`): no mover esas carpetas.
- **Enfoque (v2):** todo anclado a la **Guía SBOK** con número de página: cada entregable se vincula al proceso que lo produce y a sus salidas obligatorias. Presenta la idea y su evolución, y no adelanta métricas propias del modelo.
- **v3 (20/10/2026):** agrega el **estado real del producto** (sección 4.8). El alcance de los sprints 1 y 2 (7 HU, 15/31 pts, etapa espacial) se construyó el 17/10. El equipo lo verificó el 20/10: 43/43 pruebas y flujo completo en la app con un clip sintético. Hay una tabla por HU frente a sus criterios de aceptación y otra de los criterios de terminado (FGAP070) cumplidos y pendientes. Cierra con una **propuesta** de reordenamiento (adelantar el Sprint 3), que decide el PO. También se actualizaron las figuras de secuencia, arquitectura y plan de sprints (lo construido va en verde), un objetivo específico más y una fila de la tabla de entregables (proceso 10.1).

## Contenido
| Sección | Qué tiene |
|---|---|
| Carátula, índices | Sello UNS · índice general · 22 tablas · 9 figuras |
| 1. Introducción | Problema, propuesta, objetivo general y 5 específicos (incluye el enfoque Scrum y el estado real) |
| 2. Antecedentes | 3 internacionales (Önal y Dandıl) y 4 nacionales verificados (PUCP, UNSA, UCV, UPN), con tabla síntesis |
| 3. Marco teórico | **3.1 Scrum según la Guía SBOK:** principios (tabla con pág.), aspectos, roles, 19 procesos en 5 fases (tabla), reuniones y time-boxes (tabla) · requisitos ágiles · priorización y estimación · SST · YOLO · ConvLSTM · métricas |
| 4. Desarrollo | Tabla entregable ↔ proceso SBOK · evolución VIGIA → NewBit · **Semana 2:** cuadro de principios (figura) y FGAP010 · **Semana 3:** FGAP030, infografía (figura en dos partes), diagrama de arquitectura (figura) · **Semana 4:** EGAP015, FGAP040 · **Semana 5:** FGAP060, puño de cinco, Scrumboard del Sprint 1 (figura), FGAP070 · **Semana 6:** FGAP020 y definición de listo · planificación de la liberación: arquitectura, plan de sprints y ciclo de cada sprint · **4.8 Estado del primer incremento al 20/10/2026:** HU de S1–S2 frente a sus criterios, criterios de terminado y propuesta de reordenamiento |
| Referencias | 23 en APA 7 |

## Decisiones tomadas al redactar (revisar)
- **Hechos para este producto (semana 6):** FGAP020, **definición de listo** y planificación de la liberación (una liberación guiada por fecha, 14–18/12). Son salidas obligatorias del SBOK que faltaban; están marcadas como propuesta.
- **Cronograma:** fechas del acta (S1 19–30/10…); el tablero Kanban dice 01/11 como fin del S1 y se aclara en una nota que prevalece el acta.
- **César Vásquez:** «área de mecanizado»; el FGAP030 entregado dice «zona de laminación».
- **Unsafe-Net** citado como 2025 (volumen 84), según APA 7.
- **Escuela:** «Escuela Profesional de Ingeniería de Sistemas e Informática» (POR CONFIRMAR).
- **Estado del incremento (v3):** las historias de S1–S2 figuran como «hechas, por aceptar», porque el SBOK solo las da por aceptadas en la revisión del sprint con el PO (p. 248). HU05 figura «en cierre»: agrupa secuencias continuas, pero le faltan la ventana fija de N fotogramas y el tensor de ConvLSTM que piden sus criterios. Además, la prueba integrada se hizo con un clip sintético y la revisión de pares no está registrada.
