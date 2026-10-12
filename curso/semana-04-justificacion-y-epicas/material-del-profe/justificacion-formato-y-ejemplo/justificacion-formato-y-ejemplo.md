# EGAP015 – Justificación del Proyecto (Laboratorio 4, Actividad 1)

- **Fuente:** `justificacion-formato-y-ejemplo.pdf` (6 págs.) y su versión Word `justificacion-formato-y-ejemplo.docx` (mismo contenido)
- **Semana:** 4 (actual; Laboratorio 4, junto con las Épicas) · **Tipo:** guía + formato + ejemplo resuelto del docente
- **Duración de la actividad:** 70 min · en equipo · el docente puede pedir sustentación oral de cualquier apartado

> ⚠️ **El nombre del PDF no coincide con su contenido** (el `.docx` sí se llama como el formato). "NightWatch Protocol Propuesta" no aparece en el documento: es el formato EGAP015 con el ejemplo de Retinopatía Diabética. Probablemente es el mismo archivo con otro nombre; el `.docx` es la versión editable y su Parte I sigue **sin llenar**.

## Instrucciones de la actividad
- Coherente con el Acta: **mismo nombre, alcance, organización beneficiaria y equipo Scrum**.
- Explicar *por qué* es necesario el proyecto, no solo qué funciones tiene.
- Cinco perspectivas: **tecnológica, operativa, económica, social y académica**.
- Económica: detallar gastos y **verificar que el total coincida con el Acta**.
- Beneficios realistas y medibles; **no atribuir resultados aún no demostrados**.
- Redacción formal, técnica y propia (no copiar el ejemplo).
- Revisar coherencia: problema → justificación → beneficios → viabilidad.

## Formato (10 apartados)
1. Datos generales (código, nombre, organización, PO, SM, 3 Developers).
2. Situación o necesidad.
3. Justificación tecnológica (valor de la tecnología, no solo nombres).
4. Justificación operativa (usuarios, facilidad de uso, disponibilidad, proceso actual).
5. Justificación económica (costo, componentes, beneficios; sin afirmar ahorro sin evidencia).
6. Justificación social/clínica (sin afirmar beneficios clínicos no demostrados; apoyo, no sustituto).
7. Justificación académica y formativa.
8. Beneficios esperados (tangibles e intangibles).
9. Viabilidad inicial (técnica, operativa, económica, restricciones).
10. Conclusión (un párrafo que integre necesidad, valor, viabilidad y alcance).

## Ejemplo desarrollado: PY-RD-001 (Retinopatía Diabética)

**Datos:** Scrum, equipo 1 PO + 1 SM + 3 Developers; web + modelo de Deep Learning + Microsoft Azure.

**Necesidad:** fortalecer el análisis oportuno de imágenes de fondo de ojo y facilitar la identificación de posibles signos que requieran evaluación especializada; herramienta de apoyo a la decisión, no sustituto del diagnóstico.

**Tecnológica:** Deep Learning aprende patrones visuales de las clases del dataset; la web da un flujo único (cargar → predecir → ver → trazar); Azure da cómputo bajo demanda sin comprar infraestructura física.

**Operativa:** interfaz web centralizada (usuarios, carga, modelo, resultado, consulta); permite que PO y usuarios revisen incrementos por sprint. Depende de usuarios autorizados, reglas de acceso claras e imágenes permitidas.

**Económica – S/ 75,430 (6 meses):**

| Concepto | Detalle | Monto |
|---|---|---|
| Equipo Scrum | PO + SM + 3 Developers | S/ 72,000 |
| Azure ML / GPU | Entrenamiento y pruebas, bajo demanda, no 24/7 | S/ 1,000 |
| Azure App Service | Hosting web/API | S/ 520 |
| Azure SQL Database | Usuarios, resultados, trazabilidad, metadatos | S/ 510 |
| Azure Blob Storage | Imágenes, archivos del modelo, respaldos | S/ 180 |
| Azure Monitor, Key Vault, transferencia | Monitoreo, secretos, datos | S/ 610 |
| Dominio y complementarios | Despliegue | S/ 300 |
| Datos / licencias | Datos públicos o autorizados sin costo | S/ 0 |
| Contingencia Azure | Variación de consumo | S/ 310 |
| **Total** | | **S/ 75,430** |

~95 % del presupuesto es el equipo Scrum. No incluye cámara retinal, integración con HCE, certificación como dispositivo médico ni validación clínica formal. Montos referenciales, no cotización.

**Social/clínica:** beneficiarios potenciales: personal que evalúa y, indirectamente, pacientes. El prototipo **no** es evidencia de beneficio clínico ni autorización asistencial.

**Académica:** integra Scrum, backlog, historias de usuario, criterios de aceptación, pruebas, riesgos, trazabilidad, web, IA, datos, seguridad y cloud.

**Beneficios tangibles:** prototipo web integrado con modelo · flujo carga/proceso/visualización · modelo entrenado, evaluado y versionado con métricas · backlog, historias, pruebas, manuales, documentación · infraestructura cloud de piloto.
**Intangibles:** experiencia en desarrollo incremental con IA · comprensión de requisitos/riesgos/seguridad en dominio sensible · trabajo colaborativo y decisiones por valor.

**Viabilidad:** técnica (si hay dataset autorizado, cómputo y herramientas) · operativa (PO y usuarios disponibles, reglas de acceso) · económica (S/ 75,430; revisar si cambia duración, GPU o alcance) · restricciones (sin HCE, cámaras, certificación ni validación clínica).

**Conclusión:** se justifica ejecutar el piloto con entregas incrementales, siempre que haya uso autorizado de datos, control de consumo de infraestructura y se mantenga que el modelo es apoyo tecnológico y no reemplaza el diagnóstico.

### Lista de verificación del alumno
¿Explica por qué y no solo qué? · ¿Coincide con la visión del Acta? · ¿La tecnológica explica valor y no solo herramientas? · ¿El costo coincide con el Acta? · ¿Los beneficios no exceden el alcance? · ¿Se diferencia prototipo de solución clínica certificada? · ¿Se mantiene 1 PO + 1 SM + 3 Developers? · ¿La conclusión demuestra necesidad, valor y viabilidad?

## Análisis

- **Es el ejemplo del docente (Retinopatía).** El formato propio de VIGIA (Parte I) **sigue sin llenar**: es una entrega pendiente. El borrador de `descartado/` está escrito para Retinopatía y **no sirve** para el proyecto del equipo.
- **Reglas de oro del formato:** explicar *por qué* y no solo qué; no prometer beneficios no demostrados ni ahorros sin evidencia; el total económico debe coincidir con el Acta; mismo nombre, alcance, organización y equipo que el Acta.
- **Datos del Acta de VIGIA para llenar cada apartado** (`descartado/vigia-industrial/semana-02/Acta_Constitucion_VIGIA_Industrial_SIDERPERU/Acta_Constitucion_VIGIA_Industrial_SIDERPERU.md`):

| Apartado | Material disponible |
|---|---|
| 1. Datos generales | PY-001 VIGIA Industrial · SIDERPERU (caso propuesto) · PO Valeria Rojas Medina · equipo de 2: Luis Fernando Elias Salazar Diaz y Anthony Lopez Yrribarren (no hay 3 developers ni SM formal: confirmar con el docente) |
| 2. Necesidad | Brecha entre "ocurrió" y "se enteraron"; inspecciones no cubren todo el turno; el CCTV graba pero no alerta; Ley 29783 exige verificar el uso efectivo del EPP (discovery, diap. 2) |
| 3. Tecnológica | YOLO nano + ByteTrack + reglas por zona → eventos; nodo local de inferencia; web con panel, alertas y reportes; justificar por el valor, no por nombres |
| 4. Operativa | Supervisores de SST y de turno, analista, gerente y admin (Roles); piloto en modo observación; 2 zonas, 4 cámaras, hasta 10 usuarios |
| 5. Económica | **S/ 30,820** = 26,800 + 4,020 de contingencia; S/ 20,800 son dedicación valorizada; **caja máxima S/ 10,020**. No afirmar ahorro: el Acta no lo demuestra |
| 6. Social | Trabajadores directos y tercerizados; privacidad (sin reconocimiento facial, retención 30/180 días); sin sanciones automáticas |
| 7. Académica | Scrum (6 sprints), backlog, historias, visión por computadora, web, datos, pruebas, seguridad |
| 8. Beneficios | Tangibles: MVP, dataset, modelos, informe del piloto, manuales. Intangibles: criterio de eventos accionables, trazabilidad |
| 9. Viabilidad | Técnica: 4 flujos ≥ 5 fps · Operativa: acceso a planta y a cámaras · Económica: S/ 30,820 · Restricciones: sin acceso a planta no se acredita el piloto |
| 10. Conclusión | Integrar necesidad, valor, viabilidad y alcance en un párrafo |

- **Puntos a cuidar en la defensa oral:** el docente puede pedir sustentar cualquier apartado; los números del apartado 5 deben salir del Acta y no del ejemplo.
