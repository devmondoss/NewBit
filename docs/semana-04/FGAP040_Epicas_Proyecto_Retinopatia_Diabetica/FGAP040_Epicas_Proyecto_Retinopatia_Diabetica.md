# FGAP040 – Épicas del Proyecto e Historias de Usuario (Laboratorio 4)

- **Fuente:** `FGAP040_Epicas_Proyecto_Retinopatia_Diabetica.pdf` (3 págs.) y su versión editable `.docx` (contenido idéntico)
- **Semana:** 4 (actual) · **Tipo:** guía de laboratorio + épicas de ejemplo del docente (proyecto Retinopatía)
- **Versión 1.0** · Equipo del proyecto / Scrum Master / Product Owner · **04/10/2026** · "Versión inicial"
- **Curso:** Ingeniería de Software II · UNS · Dr. Alfredo Daza Vergaray · 70 minutos

## Instrucciones del laboratorio
- Revisar el ejemplo de épicas/HU del docente; **desarrollar las del propio proyecto** (no copiar).
- Cada épica = funcionalidad grande que agrupa varias historias.
- Formato de épica: **"Como [rol], yo debería [requerimiento], a fin de [beneficio]"**.
- Formato de historia: **"Como [rol], quiero [funcionalidad], para [beneficio]"**; evitar historias demasiado generales.
- Mantener coherencia **Acta de Constitución → Épicas → Historias de Usuario**.
- El equipo debe poder explicar la relación entre cada épica y sus historias.

## Proyecto
**PY-RD-001 – Sistema web con Deep Learning para predecir la retinopatía diabética en el Hospital III de EsSalud Chimbote**

## Épicas

| ID | Nombre | Rol | Debería… | A fin de… |
|---|---|---|---|---|
| EP01 | Gestión de acceso y usuarios | Administrador del sistema | Gestionar acceso, roles y permisos | Que solo el personal autorizado use las funciones y vea la información permitida |
| EP02 | Gestión de pacientes | Profesional de salud autorizado | Registrar, consultar y actualizar la información básica del paciente con código interno | Asociar correctamente las evaluaciones retinales y mantener organizado el proceso |
| EP03 | Evaluación de retinopatía diabética con Deep Learning *(épica central)* | Profesional de salud autorizado | Cargar y procesar una imagen de fondo de ojo con el modelo | Obtener una predicción del nivel de retinopatía como apoyo a la evaluación profesional |
| EP04 | Gestión de resultados e historial de evaluaciones | Profesional de salud autorizado | Consultar resultados e historial | Revisar cada evaluación y dar seguimiento a los registros autorizados |
| EP05 | Reportes y apoyo al seguimiento | Profesional de salud autorizado | Generar y consultar reportes de evaluaciones | Contar con información organizada para seguimiento y análisis |
| EP06 | Administración, seguridad y trazabilidad | Administrador del sistema | Supervisar parámetros, accesos y operaciones relevantes | Mantener seguridad, trazabilidad y control básico |

## Relación épicas → historias de usuario (propuesta inicial, 22 HU)

| Épica | Historias |
|---|---|
| EP01 Gestión de acceso y usuarios | HU01 Iniciar sesión · HU02 Registrar usuario · HU03 Asignar rol/permisos · HU04 Recuperar contraseña |
| EP02 Gestión de pacientes | HU05 Registrar paciente · HU06 Buscar/consultar paciente · HU07 Actualizar información autorizada |
| EP03 Evaluación con Deep Learning | HU08 Cargar imagen · HU09 Validar imagen · HU10 Procesar con Deep Learning · HU11 Mostrar nivel predicho · HU12 Mostrar confianza/advertencia |
| EP04 Resultados e historial | HU13 Consultar historial · HU14 Visualizar detalle de evaluación · HU15 Consultar resultados anteriores |
| EP05 Reportes | HU16 Generar reporte · HU17 Filtrar información · HU18 Exportar reporte, si corresponde |
| EP06 Administración y trazabilidad | HU19 Consultar accesos · HU20 Consultar operaciones · HU21 Gestionar parámetros · HU22 Verificar respaldos |

**Nota del docente:** las épicas no son una sola historia ni se ejecutan completas en un sprint; una épica puede abarcar varios sprints. Las historias mostradas son un punto de partida: deben **redactarse formalmente, priorizarse en el Product Backlog y distribuirse entre sprints** según valor, dependencias y capacidad.

## Análisis

- **Es el ejemplo del docente (Retinopatía).** La tarea del laboratorio es redactar las épicas e historias de **VIGIA**; ese entregable **todavía no existe en el repo**.
- **Cómo está armado el ejemplo (patrón a copiar, no el contenido):** 6 épicas, una por macro-función; la épica central (EP03) es el corazón del producto; cada épica lleva "Para entenderla mejor" con ejemplos de historias; las historias son solo títulos que luego deben formalizarse, priorizarse y repartirse entre sprints. La trazabilidad Acta → Épicas es completa: cada requisito funcional del Acta cae en una épica.
- **Punto de partida para VIGIA (borrador a validar por el equipo)**, derivado del Acta VIGIA y del backlog semilla US-01 a US-06:

| Épica | Qué cubre | Origen en el Acta / backlog |
|---|---|---|
| EP01 Cámaras y fuentes de video | Registrar cámaras RTSP, verificar conexión y estado | RF1 · US-01 |
| EP02 Zonas y reglas | Editor de zonas poligonales, horarios, reglas, confianza y permanencia | RF1–RF2 · US-02 |
| EP03 Detección y generación de eventos *(central)* | Casco, chaleco, zona restringida; tracking; evento único con evidencia y supresión de duplicados | RF2–RF3 · US-03, US-04 |
| EP04 Revisión de eventos | Ver evidencia, confirmar o descartar, historial con filtros | RF3 · US-05 |
| EP05 Alertas | Panel en tiempo casi real y correo | RF4 |
| EP06 Indicadores y reportes | Métricas por período, zona y tipo; exportar CSV | RF4 · US-06 |
| EP07 Usuarios, roles y auditoría | Admin, supervisor (limitado a zonas) y consulta; registro de cambios | RF5 |
| EP08 Datos y modelo *(técnica)* | Dataset, etiquetado, entrenamiento y evaluación por clase | Entregable 3 · Sprints 2–3 |
| EP09 Seguridad, respaldo y retención | HTTPS, cifrado de evidencias, respaldo y restauración, retención 30/180 días | RNF |

- **Notas:** EP08 no es una funcionalidad de usuario, pero es trabajo central del backlog; los roles de las épicas deben salir del documento de Roles de VIGIA (admin, supervisor de SST, supervisor de turno, analista, gerente).
