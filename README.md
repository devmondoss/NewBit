# NewBit – Ingeniería de Software II (UNS, 2026-II)

Repositorio del **Grupo D3** (laboratorio D, equipo 3): **Albert Sebastian Chumacero Chávarry** (Product Owner), **Anthony Gabriel Lopez Yrribarren** (Scrum Master y Developer) y **Luis Fernando Salazar Diaz** (Developer).  
Proyecto: **PY-NB-001 – Sistema web con Visión Artificial para la detección de actos inseguros en áreas operativas de manufactura metalmecánica** (Nombre comercial: **NewBit**).

## Dónde está cada cosa
```
NewBit/
├── curso/                         ← TODO LO DE CLASE
│   ├── README.md                  calendario y temas por semana
│   ├── contexto-del-curso.md      convenciones del profe y lista de entregables
│   ├── libro-guia-sbok/           libro base del profe (Guía del SBOK, 4.ª ed.)
│   └── semana-XX-<tema>/
│       ├── material-del-profe/    lo que mandó el profe (formatos, ejemplos, reglamentos)
│       └── nuestras-entregas/     lo que entregamos esa semana (Word, PDF, PPT…)
├── proyecto-newbit/               ← EL PROYECTO EN SÍ (no va por semanas)
│   ├── README.md                  estado, decisiones y hoja de ruta de entregables
│   └── investigacion/             paper Unsafe-Net, research pack, guía de investigación
│                                  (el código va aquí en monorepo: app/, ml/)
├── descartado/                    ← solo consulta: proyecto anterior (VIGIA) y borradores obsoletos
├── herramientas/                  ← utilitarios de mantenimiento y automatización
│   ├── indice-de-archivos.md      cada PDF/Word/PPT → su resumen .md
│   ├── package.json               manifiesto NPM para generadores de PPTX/HTML
│   ├── verificar-indice.ps1       verificador nativo PowerShell (Windows)
│   └── verificar-indice.sh        verificador Bash (Linux / Git Bash)
└── CLAUDE.md                      instrucciones para asistentes y pair-programming
```

## Semanas
| Semana | Fechas | Tema | Carpeta |
|---|---|---|---|
| 1 | 14–20/09 | Sin actividad | — |
| 2 | 21–27/09 | Principios de Scrum · Acta de Constitución | [`curso/semana-02-scrum-y-acta/`](curso/semana-02-scrum-y-acta/) |
| 3 | 28/09–04/10 | Roles y Prototipos · infografía · PPT · diagrama | [`curso/semana-03-roles-y-prototipos/`](curso/semana-03-roles-y-prototipos/) |
| 4 | 05–11/10 | Justificación · Épicas e historias | [`curso/semana-04-justificacion-y-epicas/`](curso/semana-04-justificacion-y-epicas/) |
| **5** | **12–18/10 (actual)** | RSU · Secuencia de avances · Criterios de terminado · Puño de cinco · Kanban · Priorización | [`curso/semana-05-rsu-y-backlog/`](curso/semana-05-rsu-y-backlog/) |

## Reglas para agregar contenido
1. **¿Lo mandó el profe?** → `curso/semana-XX-<tema>/material-del-profe/` (la semana es la de llegada). Si es de todo el curso, como el libro, va directo en `curso/`. Actualizar [`curso/README.md`](curso/README.md) y [`curso/contexto-del-curso.md`](curso/contexto-del-curso.md).
2. **¿Es una tarea que entregamos?** → `curso/semana-XX-<tema>/nuestras-entregas/` (la semana en que se pidió). Actualizar [`proyecto-newbit/README.md`](proyecto-newbit/README.md).
3. **¿Es investigación o código del proyecto?** → `proyecto-newbit/`.
4. **Todo PDF, Word, PPT o imagen lleva su `.md`** en una carpeta con el mismo nombre (`<nombre>/<nombre>.pdf` + `<nombre>/<nombre>.md`), con una fila en [`herramientas/indice-de-archivos.md`](herramientas/indice-de-archivos.md). Comprobar con `herramientas/verificar-indice.sh`.
5. BigFarma, Retinopatía Diabética y los proyectos RSU de 2025 son **ejemplos del profe**, no nuestros.
6. No afirmar resultados no demostrados; marcar como **propuesta** lo que sea diseño nuevo.
