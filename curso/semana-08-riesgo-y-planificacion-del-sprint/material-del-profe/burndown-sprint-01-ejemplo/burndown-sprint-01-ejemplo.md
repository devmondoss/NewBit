# Burndown del Sprint 01: ejemplo editable con fórmulas (Retinopatía)

- **Fuente:** `burndown-sprint-01-ejemplo.xlsx` (llegó como `Burndown_Sprint01_Editable_Con_Formulas.xlsx`). Excel con 3 hojas y un gráfico de líneas.
- **De quién:** docente. Las propiedades del archivo indican «ALFREDO DAZA VERGARAY - Docente UNS». **Ejemplo con datos simulados (PY-RD-001 Retinopatía), no del equipo.**
- **Semana:** 8, porque se agregó al repo el 02/11/2026 con el resto del material. **El archivo fue creado el 27/10/2026**, así que pudo llegar en la semana 7; si fue así, moverlo a `semana-07-gestion-del-cambio/`.
- **Tipo de `.md`:** Resumen + fórmulas (se leyeron todas las celdas).

## Hojas
**1. Resumen.** «Sprint 01, avance y burndown». Sprint de 2 semanas (10 jornadas hábiles) con HU01, HU02 y HU03.

| Indicador | Fórmula | Valor del ejemplo |
|---|---|---|
| Puntos comprometidos | `SUM(Historias!C6:C8)` | 18 |
| Días hábiles | fijo | 10 |
| Puntos aceptados | `SUMIF(Estado="Terminada"; Puntos)` | 10 |
| Puntos pendientes | comprometidos − aceptados | 8 |
| Cumplimiento | aceptados / comprometidos | 55,6 % |
| Velocidad observada (PH/sprint) | = aceptados | 10 |
| Horas consumidas | `SUM(Historias!G6:G8)` | 60 |

«Lectura docente»: se terminan 2 de 3 historias (10 de 18 puntos). HU03 conserva sus 8 puntos porque **no cumple la Definición de Terminado**.

**2. Historias** (solo se editan «Día de aceptación» y «Estado»):

| HU | Entregable | PH | Día de aceptación | Estado | Horas previstas | Horas consumidas | Observaciones |
|---|---|---|---|---|---|---|---|
| HU01 | Iniciar sesión | 5 | 4 | Terminada | 16 | 18 | Autenticación probada |
| HU02 | Registrar usuario | 5 | 8 | Terminada | 16 | 19 | Alta por admin de prueba |
| HU03 | Asignar roles y permisos | 8 | — | En curso | 28 | 23 | Dos pruebas de acceso fallan; NO terminada |
| **Total** | | **18** | | | **60** | **60** | |

**3. Burndown.** Tabla por día hábil (0–10) con las columnas Ideal pendiente, Real pendiente, Puntos aceptados, Brecha y Evento, más un gráfico de líneas «Ideal vs. Real».
- **Ideal** = compromiso × (1 − día / días hábiles), es decir, 18 → 0 en línea recta.
- **Real** = compromiso − puntos de HU **terminadas** con día de aceptación ≤ día. En el ejemplo: 18 hasta el día 3, 13 del día 4 al 7 (HU01 aceptada) y 8 del día 8 al 10 (HU02 aceptada).
- **Brecha** = real − ideal.
- Regla: **solo se descuentan puntos de historias terminadas**. El trabajo parcial no baja la curva.

## Para NewBit
Sirve de plantilla para el burndown de nuestros sprints: se reemplazan las HU, los puntos y los días de aceptación. Hay que usar datos reales. En el repo, los Sprints 1 y 2 de NewBit están «construidos, por aceptar» ([sprints](../../../../proyecto-newbit/gestion/sprints/README.md)): mientras el PO no acepte ninguna historia, la curva real no baja.
