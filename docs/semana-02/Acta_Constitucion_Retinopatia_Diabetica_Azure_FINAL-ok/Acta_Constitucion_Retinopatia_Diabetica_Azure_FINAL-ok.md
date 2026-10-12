# EGAP010 – Acta de Constitución: Retinopatía Diabética (Azure)

- **Fuente:** `Acta_Constitucion_Retinopatia_Diabetica_Azure_FINAL-ok.pdf` (4 págs.)
- **Semana:** 2 · **Tipo:** ejemplo del docente (proyecto Retinopatía) · **Versión 1 – 21/09/2026** ("Versión inicial")
- **Hecho por:** Equipo del proyecto · **Revisado:** Docente/asesor · **Aprobado:** Sponsor/responsable

## Código y nombre
**PY-RD-001 – Sistema web con Deep Learning para predecir la retinopatía diabética en el Hospital III de EsSalud Chimbote**

## Visión
El Hospital III de EsSalud Chimbote requiere fortalecer el apoyo a la detección de signos de retinopatía diabética en pacientes con diabetes, facilitando el análisis oportuno de imágenes de fondo de ojo y la priorización de casos para evaluación especializada. Es una herramienta de **apoyo a la decisión clínica**, sin sustituir el diagnóstico del profesional.

## Requisitos

### Funcionales
1. Registrar usuarios por rol (administrador, profesional de salud, usuario autorizado).
2. Registrar/identificar al paciente con código interno, respetando protección de datos.
3. Cargar imágenes de fondo de ojo en formatos admitidos.
4. Validar calidad y formato básico antes de enviar al modelo.
5. Ejecutar el modelo de Deep Learning para estimar la clase/nivel de retinopatía.
6. Mostrar predicción, nivel de confianza y advertencia de uso como apoyo.
7. Consultar historial de evaluaciones autorizadas.
8. Generar reportes de evaluaciones y resultados.
9. Administrador gestiona usuarios, roles y parámetros.
10. Trazabilidad básica de accesos y operaciones relevantes.

### No funcionales
- Interfaz web clara, usable y responsiva (computadoras y tablets).
- HTTPS/TLS en despliegue.
- Contraseñas almacenadas de forma segura; acceso por roles.
- Confidencialidad de datos e imágenes según políticas aplicables.
- Métricas del modelo: accuracy, sensibilidad, especificidad, Macro-F1, AUC y/o QWK según el esquema.
- Tiempo de respuesta de la predicción medido y documentado.
- Respaldo y recuperación de la información almacenada.
- Código, modelo y documentación versionados (trazabilidad y reproducibilidad).

## Alcance
Análisis, diseño, desarrollo y validación de un **prototipo** de sistema web con modelo de Deep Learning. Gestión con **Scrum**, entregas incrementales por sprint.

### Límites
- Prototipo académico/tecnológico; no sustituye el diagnóstico médico.
- Sin validación clínica formal ni certificación como dispositivo médico (salvo proceso específico de la institución).
- Sin integración inicial con historia clínica electrónica ni otros sistemas.
- Solo datos/imágenes con autorización, licencia o base legítima.
- El modelo se limita a las clases definidas en el dataset y protocolo.
- No incluye cámaras de fondo de ojo ni infraestructura clínica.

### Entregables clave
Acta · Product Backlog priorizado e historias de usuario · documento de requisitos y criterios de aceptación · dataset preparado y documentado (train/val/test) · modelo entrenado, evaluado y versionado · prototipo web integrado · evidencias de pruebas (funcionales, desempeño, modelo) · manual de usuario y documentación técnica · informe final y demo.

## Riesgos generales
- Dificultad para obtener imágenes clínicas suficientes, autorizadas y bien etiquetadas.
- Desbalance entre clases de retinopatía.
- Variabilidad de calidad, iluminación, resolución o procedencia.
- Sobreajuste / desempeño insuficiente en imágenes distintas al entrenamiento.
- Falta de capacidad computacional para entrenar o inferir.
- Retrasos en autorizaciones institucionales/éticas/acceso a datos.
- Exposición de datos sensibles sin controles de seguridad y privacidad.
- Cambios de alcance o poca disponibilidad de usuarios clínicos.
- Integración tardía modelo ↔ sistema web.

## Cronograma de hitos
| Hito | Fecha |
|---|---|
| Inicio y aprobación del Acta | 21/09/2026 |
| Product Backlog y requisitos priorizados | 28/09/2026 |
| Preparación y análisis del dataset | 12/10/2026 |
| Primer modelo Deep Learning entrenado | 26/10/2026 |
| Evaluación y selección del modelo | 09/11/2026 |
| Prototipo web integrado con el modelo | 23/11/2026 |
| Pruebas y ajustes finales | 07/12/2026 |
| Informe, manuales y presentación final | 14/12/2026 |
| Cierre del proyecto | 18/12/2026 |

Las fechas son una propuesta para el semestre 2026-II; deben reemplazarse por las oficiales del curso y el plan de sprints.

## Recursos financieros (piloto ~6 meses)
| Concepto | Monto |
|---|---|
| Equipo Scrum: PO + Scrum Master + 3 Developers | S/ 72,000 |
| Azure Machine Learning / GPU | S/ 1,000 |
| Azure App Service | S/ 520 |
| Azure SQL Database | S/ 510 |
| Azure Blob Storage | S/ 180 |
| Azure Monitor, Key Vault y transferencia | S/ 610 |
| Dominio y servicios complementarios | S/ 300 |
| Datos / licencias | S/ 0 (inicialmente) |
| Contingencia de infraestructura Azure | S/ 310 |
| **Total estimado** | **S/ 75,430** |

Estimación referencial: la GPU solo se usa en entrenamiento/pruebas; los costos deben cotizarse antes de implementar.

## Interesados clave
Sponsor/responsable institucional · Product Owner · Equipo Scrum · Docente/asesor · Representante del Hospital III EsSalud Chimbote · Oftalmólogos/personal clínico autorizado (validación) · Área de TI · Responsable de protección de datos / comité de ética · Pacientes (beneficiarios indirectos, datos con protección especial). **Todos los nombres están "por completar".**

## Requisitos de aprobación
Culminado técnicamente cuando: entregables aceptados, flujo carga→predicción funcionando, modelo evaluado con conjunto de prueba **sin fuga de datos**, métricas y limitaciones documentadas, y pruebas funcionales y de seguridad ejecutadas. Acepta el docente/asesor + Product Owner. Un uso institucional o clínico exige además autorizaciones del hospital e instancias competentes.

## Criterios de culminación
- **Cierre normal:** entregables presentados y aceptados, repositorio y documentación al día, resultados/limitaciones registrados, retrospectiva de cierre.
- **Cancelación/replanteo:** sin acceso legítimo a datos, restricciones institucionales o éticas, modelo no validable de forma técnicamente aceptable, o cambio de prioridad del sponsor/docente (documentando estado y razones).

## Product Owner
Nombre: *[por completar]* · Reporta a: *[sponsor por completar]* · Autoridad: prioriza el Product Backlog y acepta/rechaza incrementos según criterios acordados.

## Sponsor
Nombre/entidad/cargo: *[por completar]* · Fecha: 21/09/2026.

## Análisis

- **Es el ejemplo del docente (proyecto Retinopatía), no el proyecto del equipo.** Sirve de modelo para el Acta propia: ver `archivo/vigia-industrial/semana-02/Acta_Constitucion_VIGIA_Industrial_SIDERPERU/Acta_Constitucion_VIGIA_Industrial_SIDERPERU.md`. Los campos "[por completar]" (PO, sponsor, interesados) son placeholders que el docente deja para que cada equipo los llene.
- **Estructura que hay que replicar:** código y nombre · visión · requisitos (funcionales y no funcionales) · alcance, límites y entregables · riesgos · hitos · recursos financieros · interesados · requisitos de aprobación · criterios de culminación · Product Owner · sponsor.
- **Buenas prácticas que marca:** separar "resultado experimental" de "autorización de uso real"; límites explícitos; el PO debe ser una persona, no un comité; métricas con umbral fijado tras revisar el dataset; cronograma ajustado a las fechas oficiales.
- **Cuentas verificadas:** 72,000 + 1,000 + 520 + 510 + 180 + 610 + 300 + 0 + 310 = S/ 75,430. El equipo Scrum es ~95 % del costo.
- **Comparación con el Acta de VIGIA:** el Acta del equipo cubre las mismas secciones y agrega responsables por riesgo, fechas de inicio y fin por sprint, umbrales de aceptación concretos, retención de datos y modelo de caja (dedicación valorizada vs desembolso).
