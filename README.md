# NewBit – Ingeniería de Software II (UNS, 2026-II)

Repositorio del equipo **Anthony Lopez Yrribarren** y **Luis Fernando Elias Salazar Diaz**. Separa lo que manda el docente de lo que hace el equipo.

```
NewBit/
├── INDICE-ARCHIVOS.md     Cada PDF/DOCX/PPTX/imagen → el .md que lo reemplaza (leer este primero)
├── scripts/verificar-indice.sh  Avisa si algún archivo no tiene .md
├── docs/                    Material del curso (lo que envía el docente), por semana
│   ├── README.md            Índice de semanas
│   ├── CONTEXTO-CURSO.md    Calendario, convenciones del docente, entregables
│   └── semana-XX/<archivo>/ Una carpeta por archivo: original + <archivo>.md
├── proyecto/                Proyecto vigente: Unsafe-Net (documentos del equipo y, luego, código)
│   ├── README.md            Estado, entregables aplicados al proyecto, decisiones abiertas
│   └── semana-XX/
└── archivo/
    └── vigia-industrial/    Proyecto anterior (VIGIA / NewBit / VisionOps). Solo referencia
```

## Calendario
| Semana | Fechas | Curso (`docs/`) | Proyecto (`proyecto/`) |
|---|---|---|---|
| 1 | 14–20/09 | Sin actividad | — |
| 2 | 21–27/09 | Scrum · Acta | (VIGIA, en `archivo/`) |
| 3 | 28/09–04/10 | Roles y Prototipos · infografía | (VIGIA, en `archivo/`) |
| 4 | 05–11/10 | Justificación · Épicas | Elección de Unsafe-Net |
| **5** | **12–18/10 (actual)** | RSU (reglamento + ejemplos) · Secuencia de avances FGAP010 → FGAP090 · FGAP070 (ejemplo) | — |

## Reglas para agregar contenido
1. **¿Lo mandó el docente?** → `docs/semana-XX/` (semana según la fecha de llegada). Original en ``, resumen en `.md` con sección **Análisis**, y actualizar `docs/README.md` y `docs/CONTEXTO-CURSO.md`.
   **Todo archivo que no sea `.md` (PDF, Word, PowerPoint, imagen) necesita su `.md`**: si es largo o escaneado, solo una **ficha rápida** tras hojearlo (no se transcribe); si es corto o un formato a llenar, resumen y una fila en `INDICE-ARCHIVOS.md`. Va en **su propia carpeta con el mismo nombre**: `semana-XX/<nombre>/` con el original y `<nombre>.md`. Comprobar con `scripts/verificar-indice.sh`.
2. **¿Lo hizo el equipo?** → `proyecto/semana-XX/` y actualizar `proyecto/README.md`.
3. BigFarma, Retinopatía Diabética y los proyectos RSU de 2025 son **ejemplos del docente**, no del equipo.
4. No afirmar resultados no demostrados; marcar como **propuesta** lo que sea diseño nuevo.
