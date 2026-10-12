# FGAP030 – Roles y Prototipos: NewBit (versión 1.0)

- **Archivos para entregar** (esta carpeta): `FGAP030_Roles_y_Prototipos_NewBit.pdf` (2 págs., exportado con Pages) y `FGAP030_Roles_y_Prototipos_NewBit.docx` (editable).
- **Plantilla:** Roles y Prototipos de VIGIA (formato FGAP030 del docente; mismas tablas, encabezado y fotos). **Fecha:** 12/10/2026.
- **Coherencia con el Acta:** mismo código PY-NB-001, nombre, equipo (hecho por Anthony Lopez / Luis Salazar, revisado por el PO Albert Chumacero, aprobado por el Sponsor Ricardo Salcedo), SIDERPERU como caso y las 2 conductas.

## Roles de usuario de NewBit
| Rol | Persona | Frecuencia | Experticia | Comput. | Software | Meta principal |
|---|---|---|---|---|---|---|
| Administrador de la plataforma | Jorge Ponce Aguilar (35, TI) | Diaria / al cargar videos | Alto | Alto | Alto | Cargar videos, configurar la selección de frames y el umbral, gestionar usuarios |
| Supervisora de SST | Mariana Torres Cárdenas (32) | Diaria y ante cada alerta | Alto | Medio | Medio | Revisar alertas y evidencia, confirmar o descartar, priorizar inspecciones |
| Supervisor de turno | César Vásquez Lozano (41) | Diaria, en su turno | Alto | Medio | Medio | Ver alertas de su área, corregir en el momento, registrar la acción |
| Operadora de monitoreo | Lucía Ramos Villena (29) | Permanente en su turno | Medio | Alto | Alto | Atender alertas al instante, avisar al supervisor, marcar falsas alarmas |
| Gerente de operaciones (Sponsor) | Ricardo Salcedo Paredes (48) | Semanal | Alto | Medio | **Bajo** | Reportes breves por tipo, zona y semana; decidir recursos y ampliaciones |

## Análisis
- **Cambios frente a VIGIA:** las metas ahora giran en torno a las 2 conductas (vía peatonal, panel abierto) y a las alertas. La "analista" Valeria sale, porque el PO ahora es Albert, del equipo. Se agrega la **operadora de monitoreo**. El supervisor de turno pasa a llamarse **César Vásquez Lozano**: el nombre anterior se parecía al del ejemplo del docente.
- **Requisitos de diseño que se deducen** (para las Épicas): confirmar o descartar una alerta en un clic; clip de evidencia corto; filtros por zona, tipo y fecha; deduplicación de alertas; reportes breves para gerencia; configuración sin código e historial de cambios para el administrador; marcar falsas alarmas.
- **A revisar:** la operadora "atiende alertas en tiempo real", pero el Acta deja fuera las cámaras en vivo (en esta versión se procesan clips MP4). Se puede leer como el uso objetivo del producto; si el docente lo observa, cambiar a "cuando el sistema procesa los videos".
- **Fotos:** reutilizadas del documento de VIGIA; confirmar su origen o licencia antes de una entrega pública.
