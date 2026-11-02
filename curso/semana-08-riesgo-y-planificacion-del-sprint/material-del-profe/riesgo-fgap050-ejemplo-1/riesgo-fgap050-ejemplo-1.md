# FGAP050 Riesgo del Proyecto: ejemplo 1 (desempeño del modelo con otras cámaras, Retinopatía)

- **Fuente:** `riesgo-fgap050-ejemplo-1.pdf` (llegó como `FGAP050_Riesgo_del_Proyecto_Ejemplo_Resuelto_UNS.pdf`). 1 pág., con capa de texto.
- **De quién:** docente. **Ejemplo resuelto con datos ficticios (IA-RD-2026-02 Retinopatía), no del equipo.**
- **Semana:** 8. Se agregó al repo el 02/11/2026; el pie dice «Ejemplo académico para la semana 8».
- **Tipo de `.md`:** Resumen (documento corto). Incluye completa la tabla de escalas, que es la clave para llenar el formato.

## Estructura del formato FGAP050
Control de versiones · **Código y nombre del proyecto** · **Código del riesgo** · **Identificación del riesgo:** descripción, causa raíz, trigger (señal de que el riesgo está por ocurrir) y entregables afectados · **Evaluación del riesgo:** estimación de probabilidad, estimación de impacto, probabilidad × impacto y tipo de riesgo · tabla de escalas.

No llegó el FGAP050 en blanco: este ejemplo trae todos los campos y la escala.

## Contenido del ejemplo (R-03)
- **Versión:** v1.0, 02/11/2026. La hizo el equipo Scrum, la revisó el SM y la aprobó la PO. Motivo: «Registro inicial del riesgo».
- **Riesgo:** el modelo de clasificación pierde desempeño con imágenes de otras cámaras o con otra iluminación. Eso trae clasificaciones incorrectas y retrasa la validación del prototipo.
- **Causa raíz:** los datos de entrenamiento no cubren la variación de cámara, foco e iluminación, y no se planificó un piloto temprano con otras fuentes ni criterios de calidad.
- **Trigger:** en un piloto con otra fuente, la **Macro-F1 cae ≥ 0,15** frente al test inicial, o sube el porcentaje de imágenes rechazadas por calidad.
- **Entregables afectados:** modelo de 5 niveles, API de inferencia, carga de imágenes, reporte de evaluación y demostración del incremento.
- **Evaluación:** probabilidad 0,70 (muy probable) × impacto 0,80 (muy alto) = **0,56 → MUY ALTO**.

## Tabla de escalas (igual en los dos ejemplos)
| Probabilidad | Valor | Impacto | Valor | Tipo de riesgo | P × I |
|---|---|---|---|---|---|
| Muy improbable | 0,1 | Muy bajo | 0,05 | Muy alto | > 0,50 |
| Relativamente probable | 0,3 | Bajo | 0,10 | Alto | < 0,50 |
| Probable | 0,5 | Moderado | 0,20 | Moderado | < 0,30 |
| Muy probable | 0,7 | Alto | 0,40 | Bajo | < 0,10 |
| Casi certeza | 0,9 | Muy alto | 0,80 | Muy bajo | < 0,05 |

La escala de impacto no es lineal: duplica en cada nivel.

## Para NewBit
Es el riesgo análogo más directo para NewBit. Un modelo entrenado con el dataset de Önal y Dandıl puede rendir peor con las cámaras y la iluminación de un taller real. El trigger se mide con una métrica concreta comparada contra la línea base; en NewBit no hay métricas propias demostradas todavía, así que el umbral tendría que quedar como **propuesta**.
