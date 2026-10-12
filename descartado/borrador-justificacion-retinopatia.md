> ⚠️ **Revisar antes de usar.** Este borrador (que no escribí yo) justifica el proyecto **Retinopatía Diabética**, que es el **ejemplo del docente**. El proyecto real del equipo es **VIGIA Industrial / NewBit (SIDERPERU)**. Para llenar la justificación propia, usar la tabla de datos del Acta VIGIA en `curso/semana-04-justificacion-y-epicas/material-del-profe/justificacion-formato-y-ejemplo/justificacion-formato-y-ejemplo.md`. Se conserva aquí por si se quiere reaprovechar la redacción o la estructura.

# EGAP015 – Justificación del Proyecto (borrador propio del equipo)

- **Estado:** borrador en Markdown. Después se pasa al `.docx` `justificacion-formato-y-ejemplo.docx`, Parte I.
- **Proyecto:** PY-RD-001 (Retinopatía Diabética), el mismo del Acta. NewBit no entra aquí (ver `CLAUDE.md`).
- **Fuentes:** Acta EGAP010 (`curso/semana-02-scrum-y-acta/material-del-profe/acta-ejemplo-retinopatia/acta-ejemplo-retinopatia.md`), Épicas FGAP040 y el formato (`curso/semana-04-justificacion-y-epicas/material-del-profe/`).
- Los campos marcados **[COMPLETAR]** son datos que el repo no tiene. Hay que llenarlos antes de pasar al formato.

---

## 1. Datos generales del proyecto

| Campo | Respuesta |
|---|---|
| Código del proyecto | PY-RD-001 |
| Nombre del proyecto | Sistema web con Deep Learning para predecir la retinopatía diabética en el Hospital III de EsSalud Chimbote |
| Organización / área beneficiaria | Hospital III de EsSalud Chimbote. Ver nota 1 sobre el área o servicio. |
| Product Owner | **[COMPLETAR]**. El Acta exige una persona identificada, no un comité. |
| Scrum Master | **[COMPLETAR]** |
| Developers (3) | **[COMPLETAR]**, **[COMPLETAR]**, **[COMPLETAR]** |

Notas:
1. El Acta no precisa el área del hospital (oftalmología o endocrinología). Se sugiere "Servicio de Oftalmología, Hospital III EsSalud Chimbote" si el equipo lo confirma.
2. Enfoque de gestión: Scrum, con 1 PO, 1 SM y 3 Developers.
3. El Acta dice "predecir". Se mantiene el verbo del Acta para conservar la coherencia.

---

## 2. Situación o necesidad que justifica el proyecto

La retinopatía diabética es una complicación ocular de la diabetes. Suele avanzar sin síntomas visibles en sus etapas iniciales. Por eso depende de que las imágenes de fondo de ojo se revisen a tiempo para decidir qué pacientes necesitan evaluación especializada.

En el Hospital III de EsSalud Chimbote esa revisión recae en un número limitado de profesionales. Estos deben atender muchas imágenes y también priorizar los casos con posibles signos de la enfermedad. Además, el registro de evaluaciones, resultados e historial puede estar disperso o sin trazabilidad. **[VERIFICAR con el hospital: no hay datos del proceso actual en el repo. Redactar como situación general hasta tener entrevista o evidencia.]**

Si no se fortalece este apoyo, el riesgo es que la identificación de casos sospechosos se retrase o se haga sin criterios uniformes. También quedaría poca trazabilidad de qué se evaluó y con qué resultado.

El proyecto propone un **prototipo académico de apoyo a la decisión clínica**. Integra el análisis automatizado de imágenes con un entorno web para usuarios autorizados. No sustituye el diagnóstico del profesional de salud.

---

## 3. Justificación tecnológica

- **Deep Learning.** El problema es de clasificación de imágenes de fondo de ojo. Las redes neuronales convolucionales aprenden patrones visuales (lesiones, hemorragias, exudados) a partir de ejemplos etiquetados. Reglas escritas a mano no lo logran con esa variabilidad. El modelo se limita a las clases del dataset y del protocolo de evaluación.
- **Aplicación web.** Una interfaz web evita instalar software en cada equipo del hospital. Funciona en computadoras y tablets y da un flujo único: cargar imagen, validar calidad, predecir, mostrar nivel y confianza, y registrar la evaluación con trazabilidad.
- **Microsoft Azure.** El entrenamiento necesita GPU solo en periodos puntuales. Con cómputo bajo demanda no hace falta comprar infraestructura física. Además, los servicios gestionados (base de datos, almacenamiento, monitoreo, gestión de secretos) reducen el trabajo de operación de un equipo de cinco personas.
- **Control de calidad del modelo.** Se medirán accuracy, sensibilidad, especificidad, Macro-F1, AUC y/o QWK, con evaluación sin fuga de datos. Así el valor del modelo se demuestra con métricas y no se supone. Los umbrales aceptables aún no están definidos y se fijarán tras analizar el dataset.

---

## 4. Justificación operativa

- **Usuarios.** Técnico de imágenes (carga), oftalmólogo (interpreta), jefe de servicio (consulta reportes), médico general (consulta resultados) y administrador del sistema. Los roles salen del documento EGAP030.
- **Flujo.** El sistema reúne en un solo lugar acceso por rol, registro del paciente con código interno, carga de imagen, resultado con advertencia de uso como apoyo, historial y reportes. Esto hace verificable el proceso durante el piloto.
- **Facilidad de uso y disponibilidad.** La interfaz debe ser clara y responsiva. El despliegue usa HTTPS y se mide el tiempo de respuesta de la predicción.
- **Gestión del avance.** Con Scrum, el Product Owner y los usuarios participantes revisan incrementos cada sprint y ajustan prioridades antes de seguir.
- **Cambios necesarios.** Se requieren usuarios autorizados, reglas de acceso definidas, imágenes con uso permitido y disponibilidad del PO y de personal clínico para validar.
- **Alcance operativo.** No hay integración con la historia clínica electrónica ni con cámaras de fondo de ojo. La carga de imágenes es manual.

---

## 5. Justificación económica

**Presupuesto referencial del piloto de 6 meses: S/ 75,430.** Es el monto del Acta y coincide con ella.

| Concepto | Detalle / finalidad | Periodo | Monto (S/) |
|---|---|---|---|
| Equipo Scrum | PO + SM + 3 Developers: gestión del backlog, desarrollo web y backend, integración y componente de Deep Learning | 6 meses | 72,000 |
| Azure Machine Learning / GPU | Entrenamiento, experimentación y pruebas del modelo, bajo demanda | Entrenamiento y pruebas | 1,000 |
| Azure App Service | Hosting de la aplicación web y la API | 6 meses | 520 |
| Azure SQL Database | Usuarios, resultados, trazabilidad y metadatos autorizados | 6 meses | 510 |
| Azure Blob Storage | Imágenes, archivos del modelo y respaldos | 6 meses | 180 |
| Azure Monitor, Key Vault y transferencia | Monitoreo, secretos y transferencia de datos | 6 meses | 610 |
| Dominio y servicios complementarios | Despliegue del prototipo | Proyecto | 300 |
| Datos / licencias | Datos públicos o autorizados, sin costo de adquisición | Inicialmente | 0 |
| Contingencia de infraestructura Azure | Variación de consumo cloud | Proyecto | 310 |
| **Total** | | | **75,430** |

Verificación: 72,000 + 1,000 + 520 + 510 + 180 + 610 + 300 + 0 + 310 = **75,430**.

- El equipo Scrum es aproximadamente el 95 % del presupuesto. La infraestructura cloud pesa poco porque la GPU se usa solo en entrenamiento y pruebas.
- **No incluye** cámara retinal, integración con HCE, certificación como dispositivo médico, validación clínica formal ni licencias de datos clínicos adicionales.
- Los montos son estimaciones referenciales, no cotizaciones. Se revisarán si cambia la duración, el uso de GPU o el alcance.

**Beneficios económicos esperados:** este es un proyecto académico. La inversión se justifica por el prototipo, la infraestructura de piloto, el aprendizaje y la validación técnica. **No se afirma ahorro económico**: no hay datos de costos del proceso actual ni evidencia de reducción de gasto. Un posible ahorro futuro solo podría evaluarse después de una validación en el entorno real.

---

## 6. Justificación social / clínica

- **Beneficiarios directos potenciales:** profesionales del Hospital III que evalúan imágenes de fondo de ojo y personal que gestiona los registros.
- **Beneficiarios indirectos potenciales:** pacientes con diabetes, si en el futuro la herramienta se valida y ayuda a priorizar la evaluación especializada.
- **Valor que podría aportar:** una herramienta de apoyo que organiza las evaluaciones y señala casos con posibles signos para revisión profesional. Es un valor potencial, no demostrado.
- **Límites:**
  - El prototipo no es evidencia de beneficio clínico.
  - No cuenta con autorización asistencial.
  - No reemplaza el diagnóstico médico.
  - Un uso institucional o clínico real exige validación clínica y autorizaciones del hospital y de las instancias competentes.
- **Protección de datos.** Las imágenes y los datos de pacientes son sensibles. Se usará código interno del paciente, acceso por roles, HTTPS y trazabilidad de accesos. Solo se usarán datos con autorización, licencia o base legítima.

---

## 7. Justificación académica y formativa

El proyecto integra, en un caso realista, lo visto en Ingeniería de Software II:

- **Scrum:** roles, Product Backlog, épicas e historias de usuario, sprints, revisión y retrospectiva.
- **Requisitos:** criterios de aceptación y trazabilidad Acta → Épicas → Historias.
- **Desarrollo web:** backend, frontend y base de datos.
- **Inteligencia artificial:** preparación de datos, entrenamiento, evaluación y versionado de un modelo.
- **Pruebas:** funcionales, de desempeño y de modelo.
- **Seguridad y privacidad** en un dominio sensible.
- **Computación en la nube:** despliegue y control de costos en Azure.
- **Gestión de riesgos y documentación técnica.**
- **Trabajo colaborativo** y toma de decisiones por valor.

---

## 8. Beneficios esperados

**Tangibles (productos observables):**
- Prototipo web integrado con el modelo, con el flujo carga → validación → predicción → resultado → historial.
- Dataset preparado y documentado (train/val/test).
- Modelo entrenado, evaluado y versionado, con métricas y limitaciones documentadas.
- Product Backlog priorizado, historias de usuario, criterios de aceptación y evidencias de pruebas.
- Manual de usuario, documentación técnica, informe final y demo.
- Infraestructura cloud de piloto en Azure.

**Intangibles (cualitativos):**
- Experiencia en desarrollo incremental de un sistema con IA.
- Comprensión de requisitos, riesgos y seguridad en un dominio sensible.
- Capacidad de trabajo colaborativo bajo Scrum.
- Base técnica para una eventual validación clínica futura, sin asumirla.

---

## 9. Viabilidad inicial

| Aspecto | Respuesta |
|---|---|
| **Técnica** | Viable si se consigue un dataset autorizado y etiquetado en cantidad suficiente (hito 12/10) y hay cómputo con GPU y herramientas de Deep Learning. Riesgos: desbalance de clases, calidad variable de imágenes y sobreajuste. Se mitigan con evaluación sin fuga de datos y métricas por clase. |
| **Operativa** | Viable si el PO y los usuarios participantes están disponibles para revisar cada sprint y hay reglas de acceso definidas. Hoy el PO, el sponsor y los interesados **no tienen nombre**. |
| **Económica** | El presupuesto de S/ 75,430 es consistente con el Acta. Se revisa si cambia la duración, el consumo de GPU o el alcance. Costos referenciales, por cotizar. |
| **Restricciones principales** | Prototipo académico. Sin HCE, sin cámaras de fondo de ojo, sin certificación como dispositivo médico y sin validación clínica formal. Solo datos autorizados. El modelo se limita a las clases del dataset. Cronograma 21/09 a 18/12/2026. |

---

## 10. Conclusión de la justificación

Se recomienda ejecutar PY-RD-001 como piloto académico. La retinopatía diabética exige revisar a tiempo las imágenes de fondo de ojo, y un prototipo que combine un modelo de Deep Learning con una plataforma web trazable puede mostrar de forma verificable cómo apoyar esa revisión. El presupuesto de S/ 75,430 se concentra en el equipo Scrum y usa Azure bajo demanda, sin comprar infraestructura. Es viable técnica y operativamente mientras se cuente con datos autorizados, control del consumo de nube y disponibilidad del Product Owner y de los usuarios. El alcance se limita a un prototipo de apoyo: no incluye HCE, certificación ni validación clínica, y no sustituye el diagnóstico profesional. Los beneficios clínicos o económicos solo podrían afirmarse después de una validación posterior.

---

## Análisis

- **Coherencia con el Acta:** el código, el nombre, el verbo "predecir", el equipo (1 PO + 1 SM + 3 Dev), el presupuesto y los límites son los mismos del Acta. La suma se recalculó y da S/ 75,430.
- **No es copia del ejemplo del docente.** Mantiene la estructura y las cifras del Acta, porque deben coincidir. El texto es propio y aporta cosas que el ejemplo no tiene, como los roles reales del EGAP030, los riesgos del dataset y el vínculo con las épicas.
- **Pendientes antes de pasar al formato:**
  1. Nombres de PO, SM y los 3 Developers.
  2. Área o servicio del hospital.
  3. Datos del proceso actual en el hospital. Sin ellos, el apartado 2 queda como situación general, sin cifras.
- **Apartados que más probablemente se sustenten oralmente:** 5 (por qué ~95 % es el equipo y por qué no se afirma ahorro) y 6 (por qué no se afirma beneficio clínico).
- **Riesgo de redacción:** no escribir cifras de prevalencia ni de reducción de tiempos sin cita. El repo no las trae.
