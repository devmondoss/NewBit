# FGAP070 – Criterios de Terminado (ejemplo Retinopatía)

- **Original:** `FGAP070_Formato_Original_Completado_Retinopatia.pdf` (1 pág., con texto) · **Semana:** 5 (llegó el 12/10/2026) · **Tipo:** formato del docente **completado con el ejemplo** de Retinopatía. Este MD recoge todo su contenido.
- **En la secuencia de avances:** paso 5 (junto con FGAP060 Backlog priorizado).

## Contenido
- **Control de versiones:** 1.0 · hecho por el equipo del proyecto · revisado por el Scrum Master · aprobado por el Product Owner · 12/10/2026 · versión inicial del ejemplo.
- **Proyecto:** PY-RD-001 – Sistema web con Deep Learning para predecir la retinopatía diabética en el Hospital III de EsSalud Chimbote.
- **Concepto (texto del formato):** los Criterios de Terminado son reglas que se aplican a **todas** las historias de usuario; eliminan la ambigüedad de los requisitos y mantienen las normas de calidad.

| Campo del formato | Ejemplo resuelto |
|---|---|
| Código completo | CT-RD-001 – Definición de Terminado del incremento |
| Prueba unitaria | Componentes nuevos o modificados con pruebas unitarias ejecutadas y registradas; las fallas bloqueantes se corrigen antes de dar por terminado |
| Prueba integrada | Flujo interfaz web ↔ API ↔ almacenamiento ↔ servicio de inferencia; entradas válidas, errores controlados y permisos |
| Revisión cruzada (pares) | Otro Developer revisa código, pruebas, seguridad y legibilidad; los hallazgos críticos se resuelven |
| Certificación | No se exige certificación clínica ni de dispositivo médico (prototipo académico); no afirmar que el modelo está validado clínicamente |
| Documentación | Historias y criterios de aceptación actualizados; instrucciones de uso y despliegue; pruebas registradas; **para IA:** versión del dataset, preprocesamiento, modelo y métricas |
| Aprobaciones técnicas | Los Developers verifican pruebas, integración, seguridad, ausencia de defectos críticos y que el incremento esté disponible en el entorno de demostración |
| Aprobaciones administrativas | El PO verifica los criterios de aceptación; su aceptación **no sustituye** la Definición de Terminado |
| Otras | No usar datos sin autorización; proteger accesos y registros; la predicción es orientativa; trazabilidad y respaldo |

**Aplicación:** son comunes a todas las historias del Product Backlog; cada historia conserva además sus propios criterios de aceptación. Los Developers son responsables de cumplirlos.

## Análisis
- Es la **Definition of Done** de Scrum: aplica a todo el backlog, a diferencia de los **criterios de aceptación**, que son de cada historia. Hay que mantener esa diferencia en el entregable propio.
- **Para Unsafe-Net se adapta casi campo por campo:**
  - **Prueba integrada:** video → YOLO → ConvLSTM → GUI/alerta.
  - **Documentación de IA:** versión del dataset de Mendeley, split oficial, frames anotados, pesos del modelo y métricas por clase. Encaja con el plan experimental del Research Pack.
  - **Certificación:** prototipo académico, sin certificación de SST, sin afirmar que reduce accidentes.
  - **Otras:** atribución de la licencia CC BY 4.0, alertas orientativas con un humano que valida, y nada de reconocimiento facial.
- **Revisión cruzada con 2 personas:** cada uno revisa el código del otro. Sirve como argumento para la duda pendiente con el docente sobre el tamaño del equipo.
- Depende del Acta (código PY-…) y conviene hacerlo junto con el FGAP060 (Backlog), que todavía no llega.
