# EGAP030 – Roles y Prototipos: Retinopatía Diabética

- **Fuente:** `EGAP030_Roles_y_Prototipos_Retinopatia_Diabetica.docx`
- **Semana:** 3 (documento fechado 27/09/2026; va con el laboratorio de Roles) · **Tipo:** ejemplo del docente (proyecto Retinopatía)
- **Versión 1** · Hecho por Equipo Scrum · Revisado por Scrum Master · Aprobado por Product Owner · "Versión académica"

## Proyecto
**PY-DR001 – Sistema web con Deep Learning para la detección y clasificación de retinopatía diabética para VisionSalud S.A.C.**

## Roles

| Rol | Frecuencia | Experticia | Comput. | Software | Meta |
|---|---|---|---|---|---|
| Médico oftalmólogo | Diario | Alto | Medio | Medio | Analizar imágenes de fondo de ojo y consultar la predicción del grado como apoyo clínico |
| Técnico de imágenes oftalmológicas | Diario | Alto | Medio | Medio | Registrar pacientes y cargar imágenes con la calidad requerida |
| Administrador del sistema | Diario | Alto | Alto | Alto | Administrar usuarios, permisos, parámetros, disponibilidad e incidencias |
| Jefe del Servicio de Oftalmología | Semanal | Alto | Medio | **Bajo** | Supervisar el uso clínico y consultar información consolidada |
| Médico general / profesional derivante | Semanal | Medio | Medio | **Bajo** | Consultar resultados y apoyar la derivación a oftalmología |

## Prototipos (personas)
- **Dr. Carlos Mendoza Ríos** – oftalmólogo, 8 años de experiencia en retina; usa sistemas clínicos, IA a nivel intermedio. Quiere cargar/revisar imágenes, ver la clasificación y una explicación que apoye su criterio.
- **Ana Torres Salazar** – técnica de imágenes, 4 años capturando fondo de ojo, trabaja L–S. Quiere identificar rápido al paciente, cargar sin pasos innecesarios y recibir mensajes claros cuando una imagen no se pueda procesar.
- **Ing. Luis Paredes Vega** – administrador de TI, 6 años en soporte, bases de datos, seguridad y nube. Crea/desactiva cuentas, asigna permisos, supervisa disponibilidad y coordina incidencias con **DeepVision Solutions S.A.C.** Busca solución segura, estable y mantenible.
- **Dra. Patricia León Castro** – jefa del servicio, +12 años de experiencia. Revisa periódicamente funcionamiento, resultados y reportes; le importa que la herramienta **no reemplace el juicio clínico**.
- **Dra. Mariana Ruiz Campos** – médica general con pacientes crónicos (diabetes), no es especialista en retina. Prefiere interfaces simples, términos comprensibles y acceso rápido.

*Nota del documento: nombres, empresas y perfiles son ficticios, con fines académicos.*

## Análisis

- **Es un ejemplo del docente (fechado 27/09/2026), no el entregable del equipo.** El entregable propio es `archivo/vigia-industrial/semana-03/Roles_y_Prototipos_VIGIA_Industrial_SIDERPERU/Roles_y_Prototipos_VIGIA_Industrial_SIDERPERU.md`.
- **Qué enseña:** cada rol se concreta en una persona creíble con frecuencia de uso, tres niveles de proficiencia y metas; sirve para decidir UX y prioridades. Los roles de menor proficiencia con el software (jefe de servicio, médico general) piden interfaces simples.
- **Inconsistencias internas del ejemplo** (no afectan al equipo, pero conviene no replicarlas): código `PY-DR001` aquí vs `PY-RD-001` en el Acta y las Épicas de ejemplo; organización *VisionSalud S.A.C.* aquí vs *Hospital III de EsSalud Chimbote* allá; "detección y clasificación" vs "predecir". En VIGIA, usar un solo código y nombre en todos los documentos.
- Los nombres de este ejemplo (p. ej. Carlos Mendoza, Mariana) tienen parecido con los de los perfiles de VIGIA: diferenciarlos.
