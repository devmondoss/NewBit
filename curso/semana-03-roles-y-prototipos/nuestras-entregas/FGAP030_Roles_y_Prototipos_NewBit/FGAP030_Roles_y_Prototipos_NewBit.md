# FGAP030 – Roles y Prototipos: NewBit (Versión Oficial Normalizada)

- **Archivos para entregar** (esta carpeta): `FGAP030_Roles_y_Prototipos_NewBit.pdf` (2 págs.) y `FGAP030_Roles_y_Prototipos_NewBit.docx` (editable).
- **Formato:** Formato oficial FGAP030 del docente (tablas de perfiles de usuario, matriz de competencias y arquetipos *User Persona*).
- **Fecha de normalización:** 17/10/2026 · versión 2.0 (Grupo D3).
- **Coherencia total con el Acta (FGAP010) y Épicas (FGAP040):** Mismo código **PY-NB-001**, título oficial, equipo ejecutor (Anthony Lopez, Luis Salazar, Albert Chumacero), entorno de **Taller de Manufactura Metalmecánica** y las 2 conductas priorizadas (pasarela peatonal y panel de máquina abierto).

## Roles de Usuario y Arquetipos (Personas)
| Rol | Persona (Arquetipo) | Frecuencia | Experticia | Comput. | Software | Meta principal en NewBit |
|---|---|---|---|---|---|---|
| **Administrador de la plataforma** | Jorge Ponce Aguilar (35, TI) | Diaria / al ingresar lotes | Alto | Alto | Alto | Cargar secuencias de video (.mp4/.avi), calibrar umbrales de confianza de YOLOv8 (HU11), auditar métricas de rendimiento y gestionar accesos (EP01, EP03, EP06). |
| **Supervisora de SST** | Mariana Torres Cárdenas (32) | Diaria y por inspección | Alto | Medio | Medio | Evaluar detecciones y secuencias temporales, verificar diagnósticos de actos inseguros (HU03, HU05, HU06, HU08), tipificar conductas y planificar medidas preventivas en planta. |
| **Supervisor de turno** | César Vásquez Lozano (41) | Diaria, en su turno | Alto | Medio | Medio | Revisar incidencias reportadas en su área de taller, verificar la corrección física de los actos observados y registrar acciones inmediatas en piso. |
| **Operadora de monitoreo** | Lucía Ramos Villena (29) | Durante el procesamiento de lotes | Medio | Alto | Alto | Monitorear el procesamiento visual en la interfaz, atender notificaciones inmediatas ante conductas inseguras detectadas en los clips y descartar falsos positivos (EP05, HU09, HU10). |
| **Gerente de operaciones (Sponsor)** | Ricardo Salcedo Paredes (48) | Semanal / mensual | Alto | Medio | Bajo | Consultar indicadores consolidados de seguridad, evaluar tiempos y ahorro de procesamiento (HU12) y respaldar la viabilidad operativa y asignación presupuestal. |

## Análisis y Trazabilidad con el Backlog
1. **Resolución de Ambigüedad Operativa:** Se normalizó la descripción de la operadora **Lucía Ramos**: su función se sincroniza con el alcance formal del Acta, supervisando la bandeja de procesamiento por lotes y respondiendo a los eventos críticos arrojados por los modelos sobre los videos cargados, sin exigir transmisión continua RTSP.
2. **Trazabilidad 100% Cerrada:** Los 5 perfiles son los actores directos de las 6 épicas y 12 historias del backlog oficial [FGAP040](file:///c:/Users/luisf/OneDrive/Escritorio/Proyectos/IngSoftware/NewBit/curso/semana-04-justificacion-y-epicas/nuestras-entregas/FGAP040_Epicas_NewBit/FGAP040_Epicas_NewBit.md).
3. **Entorno de Aplicación:** El contexto de taller metalmecánico (tornos, fresadoras, prensas mecánicas, pasillos peatonales señalizados y tableros eléctricos) encaja con naturalidad en el día a día de Jorge, Mariana, César y Lucía.
