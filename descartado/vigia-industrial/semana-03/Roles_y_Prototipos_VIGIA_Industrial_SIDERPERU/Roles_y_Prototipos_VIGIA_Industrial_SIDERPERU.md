# EGAP030 – Roles y Prototipos: VIGIA Industrial (SIDERPERU)

- **Fuente:** `Roles_y_Prototipos_VIGIA_Industrial_SIDERPERU.docx`
- **Semana:** 3 · **Tipo:** **entregable del equipo**
- **Versión 1.0 – 28/09/2026** · "Versión inicial" · Hecho por Luis Fernando Elias Salazar Diaz / Anthony Lopez Yrribarren · Revisado por Valeria Rojas Medina · Aprobado por Ricardo Salcedo Paredes
- **Proyecto:** PY-CV-001 – VIGIA Industrial (Computer Vision que convierte cámaras existentes en sensores inteligentes configurables). Primer caso: SIDERPERU.
- *Perfiles y aprobadores ficticios. La proficiencia indicada es la esperada tras la capacitación inicial.*

## Roles

| Rol | Frecuencia | Experticia | Comput. | Software | Meta |
|---|---|---|---|---|---|
| Administrador de la plataforma | Diaria y cuando haya soporte | Alto (infraestructura, redes, cámaras IP) | Alto | Alto | Configurar cámaras, zonas y reglas; gestionar usuarios y permisos; verificar conectividad y resolver incidencias |
| Supervisor de SST | Diaria, al inicio del turno y ante cada alerta | Alto (EPP, prevención) | Medio | Medio | Revisar eventos de casco/chaleco e ingresos a zonas restringidas; confirmar o descartar; priorizar inspecciones |
| Supervisor de turno de operaciones | Diaria durante su turno | Alto (procedimientos, circulación) | Medio | Medio | Consultar alertas de sus zonas, revisar evidencias, registrar la validación del evento |
| Analista de operaciones y mejora continua | 3 veces por semana y cierre semanal | Alto (indicadores, procesos) | Alto | Medio | Comparar eventos por zona, horario y tipo; exportar reportes; identificar recurrencias; priorizar el backlog |
| Gerente de operaciones | Semanal y en reuniones de seguimiento | Alto (gestión industrial) | Medio | **Bajo** | Consultar tendencias y reportes consolidados; decidir sobre recursos o ampliaciones |

## Prototipos (personas)
- **Jorge Ponce Aguilar** (Administrador) – 35 años, analista de TI, Nuevo Chimbote, esposa e hijo. Redes, cámaras IP, administración de sistemas. Quiere mantener disponibles las 4 cámaras y ajustar reglas **sin modificar código**; necesita mensajes de error claros e historial de cambios.
- **Mariana Torres Cárdenas** (Supervisora SST) – 32 años, Chimbote, pareja e hija. Combina recorridos de planta con reportes; maneja hojas de cálculo y protocolos de EPP. Quiere ver **recurrencias por zona sin revisar horas de video**; necesita evidencias legibles, filtros simples y alertas desde computadora o tablet.
- **Carlos Mendoza Rivas** (Supervisor de turno) – 40 años, turnos rotativos, esposa y dos hijos. Quiere saber rápido **dónde ocurrió el evento** y evitar alertas repetidas; permiso de supervisor **limitado a sus zonas**; interfaz sencilla con hora, ubicación y evidencia.
- **Valeria Rojas Medina** (Analista / Product Owner) – 34 años, soltera, coordinadora de mejora operativa. Quiere indicadores consistentes para evaluar el piloto. Permiso de **consulta**: su rol de PO no implica administrar cámaras ni modificar evidencias.
- **Ricardo Salcedo Paredes** (Gerente / sponsor) – 48 años, esposa, dos hijos universitarios. Quiere ver qué zonas concentran eventos y si la plataforma aporta información útil; **reportes breves con cifras claras**, sin configurar reglas ni revisar alertas.

## Análisis

- **Coherente con el Acta:** los 5 perfiles se corresponden con los 3 roles del sistema del Acta: *administrador* (Jorge), *supervisor* (Mariana, Carlos; Carlos con alcance limitado a sus zonas), *consulta* (Valeria, Ricardo). Las personas coinciden con los interesados nombrados en el Acta (TI, SST, PO, sponsor), y el supervisor de turno cubre a los "supervisores y trabajadores" de las zonas piloto.
- **Requisitos de diseño que se deducen** (útiles para las épicas e historias): permisos por zona para el supervisor de turno; evidencia legible y filtros simples; alertas por correo y en panel (Acta); reportes CSV y vistas breves para la gerencia; registro de cambios de configuración (el admin lo pide); evitar alertas repetidas (deduplicación y cooldown).
- **Perfiles que habría que cuidar en UX:** el *gerente* (software **bajo**) y los supervisores (medio) → interfaz sencilla y reportes cortos; el *admin* (alto) → configuración avanzada de zonas y reglas.
- **Conexión con el discovery:** los 4 usuarios del discovery (Supervisor SST, Supervisor operativo, Jefatura/analítica SST, Administrador técnico) se mantienen y se suma el **gerente de operaciones**.
- **Detalles a pulir:** (1) código `PY-CV-001` vs `PY-001` del Acta; (2) varios nombres se parecen a los del ejemplo del docente (Carlos Mendoza Ríos → Carlos Mendoza Rivas; Mariana Ruiz Campos → Mariana Torres Cárdenas): conviene diferenciarlos para que no parezca copia; (3) la Valeria "analista" y la Valeria "Product Owner" son la misma persona con permiso de consulta: está bien, pero hay que dejar claro en el backlog que prioriza sin tener permisos de administración.
