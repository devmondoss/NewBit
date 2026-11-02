# Casos ilustrados de gestión del cambio (4 ejemplos paso a paso): texto completo

> Texto completo extraído del PDF (capa de texto). Las ilustraciones no se transcriben.

<!-- pág. 1 -->
UNIVERSIDAD NACIONAL DEL SANTA | INGENIERÍA DE SOFTWARE II CUADERNO DE CASOS ILUSTRADOS Semana 07 · Gestión del Cambio en Scrum | Cuatro ejemplos paso a paso para el aula Fuente principal: SCRUMstudy, Guía de los fundamentos de Scrum (Guía del SBOK®), 4.ª edición, capítulo 6, pp. 101– 118.
Objetivo. Disponer de cuatro casos diferentes para explicar, resolver en equipos y registrar en el formato FGAP090 (Solicitud de Cambio). Cada ejemplo incluye situación, análisis, decisión, criterios de aceptación, diagramas y solución orientadora.
Atención. Los nombres, datos, prioridades, esfuerzos y decisiones son ficticios. No sustituya políticas reales, legislación aplicable ni decisiones de un entorno clínico. Los diagramas son originales y didácticos; representan propuestas de flujo, no gráficos extraídos del libro.
Tipo de decisión Aprobado y programado después Caso Aprendizaje central
1. Consentimiento Backlog vs. sprint en curso
2. Versión de modelo Aprobado tras analizar impacto Dependencias y trazabilidad
3. Exposición indebida Atención crítica y contención Seguridad, comunicación y excepción
4. Rediseño estético Rechazado / reconsiderable Valor y autoridad proporcional Cómo utilizar este material en clase Antes del taller. Proyecte el diagrama 1 de cada caso sin mostrar todavía la respuesta; entregue el FGAP090 en blanco y asigne roles (solicitante, PO, Scrum Master, equipo).
Durante el taller. Permita 5 minutos de lectura, 15 de análisis FGAP090, 10 de deliberación y 5 de exposición por caso. Puede distribuir un caso diferente a cada equipo para reducir tiempo.
Evaluación. Solicite evidencias de problema/causa/consecuencia, solicitud precisa, valor, impactos, autoridad, prioridad y tratamiento. Al corregir, contraste los campos del formato con los criterios de aceptación.
SEMANA 07 · SCRUM — CAMBIO | Dr. Alfredo Daza Vergaray

<!-- pág. 2 -->
UNIVERSIDAD NACIONAL DEL SANTA | INGENIERÍA DE SOFTWARE II CASO 1 · Consentimiento antes de subir imágenes Situación inicial. El equipo desarrolla la visualización de resultados en Sprint 2. En la revisión del flujo, el personal de admisión propone que el usuario confirme su autorización antes de cargar fotografías de retina.
Decisión esperada. Aprobado para el Product Backlog; propuesto para Sprint 3, sin alterar de inmediato Sprint 2.
Figura 1.1. Visualización del flujo y puntos de decisión del caso 1.
1. Desarrollo guiado paso a paso Paso Acción que realiza el equipo y justificación
1. Recepción Registrar la necesidad textual y quién la plantea; separar causa y consecuencia.
2. Valor PO contrasta urgencia y valor con el sprint actual; valida alcance mínimo.
3. Impacto Equipo estima 8 puntos y enumera UI, backend, pruebas y dependencias.
4. Decisión Aprobar para Product Backlog; priorizar por encima del cambio visual; no asumir implementación inmediata.
5. Integración Crear historia y criterios; programar cuando el Sprint Planning siguiente confirme capacidad.
6. Verificación Probar rechazo y aceptación de consentimiento y presentar demostración al usuario.
SEMANA 07 · SCRUM — CAMBIO | Dr. Alfredo Daza Vergaray

<!-- pág. 3 -->
UNIVERSIDAD NACIONAL DEL SANTA | INGENIERÍA DE SOFTWARE II
2. Representación visual del cambio Figura 1.2. Segunda vista del caso: prioridades, dependencias o alternativas.
3. Ejemplo de diligenciamiento FGAP090 Campo del FGAP090 Ejemplo resuelto Código de proyecto / solicitud RDA-2026 · SC-011 Control de versiones Versión 1.0 · Preparado: Equipo Scrum (ficticio) · Revisión:
PO · Fecha: 26/10/2026 · Motivo: presentación inicial Problema o situación actual Problema: el flujo actual permite que el operador pase directamente a la carga sin una confirmación explícita dentro del sistema. Causa: la historia original describía solo la carga técnica. Consecuencia: falta trazabilidad funcional de la autorización en el prototipo.
Añadir una pantalla de confirmación y un registro de estado (acepta/no acepta) asociado a la carga, con mensaje Descripción detallada del cambio comprensible, responsable funcional definido y pruebas para impedir la carga si la confirmación no existe.
Razón de la solicitud El proceso simulado necesita una señal verificable de consentimiento en el prototipo. Alternativas: correo externo (poco integrado) o casilla sin registro (baja trazabilidad). Si no se realiza, el flujo permanece incompleto frente a la necesidad del usuario.
Refinar historia y aceptación; modificar interfaz y lógica de Efectos a corto plazo carga; agregar pruebas. No interrumpir automáticamente la meta comprometida del Sprint 2.
Efectos a largo plazo Mayor trazabilidad funcional y mayor trabajo de mantenimiento de eventos y textos informativos. Verificar retención y acceso según políticas que realmente correspondan.
El módulo de auditoría deberá consumir el estado de Otros proyectos / programas / portafolios confirmación; puede impactar manual de uso y validación del prototipo.
Efectos extraempresariales Operadores y usuarios reciben una secuencia de interacción diferente; revisar con el patrocinador el texto, sin afirmar cumplimiento normativo por sí solo.
SEMANA 07 · SCRUM — CAMBIO | Dr. Alfredo Daza Vergaray

<!-- pág. 4 -->
UNIVERSIDAD NACIONAL DEL SANTA | INGENIERÍA DE SOFTWARE II No recopilar imágenes reales de pacientes para la práctica;
Observaciones adicionales usar fotografías sintéticas o de prueba. Toda estimación del caso es simulada.
Revisión y resultado Fecha de ejemplo: 26/10/2026 · Evaluación: PO con equipo · Aprobado para el Product Backlog; propuesto para Sprint 3, sin alterar de inmediato Sprint 2.
Responsable de aplicar / informar Solicitante: representante del hospital ficticio. PO: Lucía Rojas. Scrum Master: Iván Cruz. Equipo: grupo académico.
Estimación / contexto 8 puntos de historia estimados académicamente; impacto:
UI, servicio de carga, persistencia y pruebas.
4. Criterios comprobables para validar el resultado
• Dado un usuario sin confirmación, al intentar cargar, el sistema no inicia la carga.
• La interfaz distingue aceptación y no aceptación y guarda el estado en el prototipo.
• La nueva lógica pasa pruebas de regresión de carga y navegación.
5. Pregunta para alumnos y respuesta docente Pregunta. ¿Qué cambia en el Product Backlog y por qué no se debe imponer el desarrollo durante el Sprint 2?
Respuesta fundamentada. Se crea o refina la historia de consentimiento con criterios verificables; el PO prioriza y el equipo estima. El Sprint Goal actual mantiene su foco salvo decisión extraordinaria justificada.
6. Actividad breve de aplicación en su propio proyecto Cada grupo propone un cambio análogo en su proyecto de inteligencia artificial, diligencia FGAP090, identifica si debe aprobarse, rechazarse o diferirse y justifica en qué sprint sería razonable atenderlo. Presenta en 2 minutos el impacto técnico y la decisión.
SEMANA 07 · SCRUM — CAMBIO | Dr. Alfredo Daza Vergaray

<!-- pág. 5 -->
UNIVERSIDAD NACIONAL DEL SANTA | INGENIERÍA DE SOFTWARE II CASO 2 · Trazabilidad de la versión del modelo de IA Situación inicial. El sistema ya calcula resultados de prueba con un modelo de clasificación de retinopatía diabética. Un especialista solicita conocer exactamente qué versión generó cada inferencia en una demo.
Decisión esperada. Aprobada para refinamiento y próxima planificación, condicionada a pruebas de trazabilidad.
Figura 2.1. Visualización del flujo y puntos de decisión del caso 2.
1. Desarrollo guiado paso a paso Paso Acción que realiza el equipo y justificación
1. Solicitar Especialista registra imposibilidad de identificar versión del resultado.
2. Delimitar PO precisa qué metadato se necesita y quién puede visualizarlo.
3. Impactar Equipo traza cambios en BD, API, interfaz y pruebas automatizadas.
4. Decidir Aprobar para backlog y estimar como nueva historia o dividirla por entregables verificables.
5. Implementar En sprint seleccionado: migración, cambio API, UI y prueba de regresión.
6. Validar Demostrar consulta de dos resultados de prueba con versiones distintas.
SEMANA 07 · SCRUM — CAMBIO | Dr. Alfredo Daza Vergaray

<!-- pág. 6 -->
UNIVERSIDAD NACIONAL DEL SANTA | INGENIERÍA DE SOFTWARE II
2. Representación visual del cambio Figura 2.2. Segunda vista del caso: prioridades, dependencias o alternativas.
3. Ejemplo de diligenciamiento FGAP090 Campo del FGAP090 Ejemplo resuelto Código de proyecto / solicitud RDA-2026 · SC-012 Control de versiones Versión 1.0 · Preparado: Equipo Scrum (ficticio) · Revisión:
PO · Fecha: 26/10/2026 · Motivo: presentación inicial Problema o situación actual Problema: la salida visible solo contiene categoría y fecha.
Causa: el backend guarda el resultado sin identificador de modelo. Consecuencia: resulta difícil comparar ejecuciones al actualizar pesos.
Agregar model_version a cada registro de inferencia, mostrarlo en una sección autorizada del reporte y registrar Descripción detallada del cambio datos mínimos de auditoría. El cambio debe abarcar base de datos, API, interfaz y pruebas.
Razón de la solicitud La trazabilidad técnica ayuda a investigar resultados generados por distintas versiones. Una anotación manual en archivo separado es frágil; sin cambio, no queda vinculación entre resultado y modelo.
Diseñar migración de base de datos, modificar contrato API, Efectos a corto plazo actualizar vista de resultados y agregar pruebas de compatibilidad. Estimar esfuerzo antes de elegir sprint.
Efectos a largo plazo Permite reproducibilidad operativa condicionada a conservar artefactos y configuraciones de los modelos; añade costo de gestión de versiones.
El módulo de reportes y las exportaciones podrían Otros proyectos / programas / portafolios consumir el nuevo campo; coordinar contrato con equipo de datos si es otro proyecto.
Efectos extraempresariales Especialistas autorizados verán metadatos de la inferencia.
No implica por sí solo validez clínica o mejora automática de desempeño.
Observaciones adicionales Emplear nombres de modelos y ejemplos totalmente simulados. Guardar acceso según roles del prototipo.
Revisión y resultado Fecha de ejemplo: 26/10/2026 · Evaluación: PO con equipo SEMANA 07 · SCRUM — CAMBIO | Dr. Alfredo Daza Vergaray

<!-- pág. 7 -->
UNIVERSIDAD NACIONAL DEL SANTA | INGENIERÍA DE SOFTWARE II · Aprobada para refinamiento y próxima planificación, condicionada a pruebas de trazabilidad.
Responsable de aplicar / informar Solicitante: Dra. Elena Soria (ficticia). PO: Lucía Rojas.
Scrum Master: Iván Cruz. Equipo: desarrollo e IA.
Estimación / contexto 13 puntos académicos; dependencias principales: esquema BD, servicio de inferencia, presentación y pruebas.
4. Criterios comprobables para validar el resultado
• Cada registro nuevo almacena model_version al generar una inferencia de prueba.
• Solo un rol autorizado puede consultar la versión desde el detalle del resultado.
• Una actualización de modelo no sobrescribe el identificador de inferencias anteriores.
5. Pregunta para alumnos y respuesta docente Pregunta. ¿Qué ocurriría si el equipo estima solo el tiempo de añadir una etiqueta en la interfaz?
Respuesta fundamentada. La estimación sería incompleta porque debe persistirse el metadato y transportarse por API, ajustar permisos y comprobar los resultados históricos.
6. Actividad breve de aplicación en su propio proyecto Cada grupo propone un cambio análogo en su proyecto de inteligencia artificial, diligencia FGAP090, identifica si debe aprobarse, rechazarse o diferirse y justifica en qué sprint sería razonable atenderlo. Presenta en 2 minutos el impacto técnico y la decisión.
SEMANA 07 · SCRUM — CAMBIO | Dr. Alfredo Daza Vergaray

<!-- pág. 8 -->
UNIVERSIDAD NACIONAL DEL SANTA | INGENIERÍA DE SOFTWARE II CASO 3 · Corrección crítica por exposición indebida en un prototipo Situación inicial. Durante las pruebas del sistema ficticio, un integrante descubre que un usuario de prueba puede consultar una imagen cargada bajo otra cuenta. Hay una demostración prevista para el final del sprint.
Decisión esperada. Contener el defecto, bloquear liberación afectada y acordar un plan de corrección prioritario.
Figura 3.1. Visualización del flujo y puntos de decisión del caso 3.
1. Desarrollo guiado paso a paso Paso Acción que realiza el equipo y justificación
1. Detectar QA reproduce acceso indebido con dos usuarios de prueba ficticios.
2. Contener Equipo evita la liberación de la funcionalidad afectada y registra el defecto.
3. Analizar Se determina la causa técnica y se evalúa el Sprint Goal y el plan de demostración.
4. Decidir PO y equipo acuerdan corrección prioritaria y comunican impacto; escalan si supera tolerancias.
5. Corregir Añadir autorización en backend y pruebas negativas y de regresión.
6. Validar QA confirma aislamiento; solo después se considera liberar el incremento corregido.
SEMANA 07 · SCRUM — CAMBIO | Dr. Alfredo Daza Vergaray

<!-- pág. 9 -->
UNIVERSIDAD NACIONAL DEL SANTA | INGENIERÍA DE SOFTWARE II
2. Representación visual del cambio Figura 3.2. Segunda vista del caso: prioridades, dependencias o alternativas.
3. Ejemplo de diligenciamiento FGAP090 Campo del FGAP090 Ejemplo resuelto Código de proyecto / solicitud RDA-2026 · SC-013 Control de versiones Versión 1.0 · Preparado: Equipo Scrum (ficticio) · Revisión:
PO · Fecha: 26/10/2026 · Motivo: presentación inicial Problema o situación actual Problema: autorización insuficiente al consultar archivos de prueba. Causa probable por investigar: filtro de acceso por identificador no validado en el endpoint. Consecuencia: acceso cruzado no autorizado en el prototipo.
Impedir inmediatamente el acceso indebido, revisar permisos por usuario y rol, añadir pruebas negativas de Descripción detallada del cambio autorización, documentar impacto y decidir si la meta y la demostración deben ajustarse.
Razón de la solicitud La protección básica de archivos del prototipo es más importante que presentar una nueva función defectuosa.
Alternativa de ignorar alerta es inaceptable; sustituir imágenes sin corregir control de acceso no soluciona la causa.
Suspender exposición pública de la función afectada;
Efectos a corto plazo reproducir con cuentas ficticias; identificar fallo; corregir y volver a probar antes de liberar.
Efectos a largo plazo Reforzar pruebas de seguridad, revisar control de permisos y mejorar revisión técnica; puede exigir reestimación de otras historias.
Otros proyectos / programas / portafolios Si comparte servicio de archivos con otro prototipo, alertar al responsable y revisar efecto en ese sistema.
Efectos extraempresariales En simulación no hay pacientes reales. Si sucediera en operación real, requeriría activar procedimientos institucionales y obligaciones aplicables; no se inventan normas ni plazos.
Observaciones adicionales No introducir información sanitaria real. Caso didáctico sobre seguridad y priorización, no sobre diagnósticos SEMANA 07 · SCRUM — CAMBIO | Dr. Alfredo Daza Vergaray

<!-- pág. 10 -->
UNIVERSIDAD NACIONAL DEL SANTA | INGENIERÍA DE SOFTWARE II médicos.
Revisión y resultado Fecha de ejemplo: 26/10/2026 · Evaluación: PO con equipo · Contener el defecto, bloquear liberación afectada y acordar un plan de corrección prioritario.
Responsable de aplicar / informar Detector: miembro de QA. PO: Lucía Rojas. Scrum Master:
Iván Cruz. Equipo: backend, frontend y pruebas.
Estimación / contexto Esfuerzo incierto hasta reproducir defecto. Se registran impacto, urgencia, contención y plan de pruebas.
4. Criterios comprobables para validar el resultado
• Una cuenta de prueba A no puede consultar imágenes de la cuenta B.
• Las respuestas del API son correctas ante usuario autenticado no autorizado.
• La prueba de regresión confirma que los accesos autorizados siguen funcionando.
5. Pregunta para alumnos y respuesta docente Pregunta. ¿Debe esperarse tranquilamente al siguiente sprint sin ninguna acción?
Respuesta fundamentada. No. Debe contenerse el problema y evitar liberaciones inseguras; luego se analiza la corrección con transparencia. La prioridad de seguridad no elimina necesidad de registrar y comunicar el efecto en el sprint.
6. Actividad breve de aplicación en su propio proyecto Cada grupo propone un cambio análogo en su proyecto de inteligencia artificial, diligencia FGAP090, identifica si debe aprobarse, rechazarse o diferirse y justifica en qué sprint sería razonable atenderlo. Presenta en 2 minutos el impacto técnico y la decisión.
SEMANA 07 · SCRUM — CAMBIO | Dr. Alfredo Daza Vergaray

<!-- pág. 11 -->
UNIVERSIDAD NACIONAL DEL SANTA | INGENIERÍA DE SOFTWARE II CASO 4 · Solicitud estética no prioritaria y escalamiento proporcional Situación inicial. Un representante propone cambiar todos los colores, animaciones y pantallas de inicio del dashboard mientras varios usuarios requieren exportar un informe accesible y existe trabajo de pruebas pendiente.
Decisión esperada. Rechazada en este ciclo como cambio independiente; reconsiderar solo ante evidencia de valor.
Figura 4.1. Visualización del flujo y puntos de decisión del caso 4.
1. Desarrollo guiado paso a paso Paso Acción que realiza el equipo y justificación
1. Recibir Registrar propuesta estética completa y el beneficio alegado.
2. Aclarar Preguntar qué problema real resuelve; recopilar evidencia de usuarios.
3. Comparar PO contrasta valor con reporte accesible, pruebas y otras historias.
4. Decidir Rechazar por ahora el rediseño global; guardar justificación.
5. Comunicar Explicar decisión sin descalificar solicitante y ofrecer evaluación de usabilidad.
6. Escalar solo si aplica Si existe política transversal de identidad, verificar alcance con programa/portafolio.
SEMANA 07 · SCRUM — CAMBIO | Dr. Alfredo Daza Vergaray

<!-- pág. 12 -->
UNIVERSIDAD NACIONAL DEL SANTA | INGENIERÍA DE SOFTWARE II
2. Representación visual del cambio Figura 4.2. Segunda vista del caso: prioridades, dependencias o alternativas.
3. Ejemplo de diligenciamiento FGAP090 Campo del FGAP090 Ejemplo resuelto Código de proyecto / solicitud RDA-2026 · SC-014 Control de versiones Versión 1.0 · Preparado: Equipo Scrum (ficticio) · Revisión:
PO · Fecha: 26/10/2026 · Motivo: presentación inicial Problema o situación actual Problema señalado: apariencia percibida como poco moderna; no existe evidencia de que impida completar tareas. Causa: preferencia estética del solicitante.
Consecuencia de aceptarlo ahora: desviar tiempo de una necesidad funcional más valiosa.
Rediseñar paleta cromática, transiciones de pantalla e Descripción detallada del cambio iconografía del panel. Se solicita prioridad máxima sin datos de usuarios.
Razón de la solicitud Se busca satisfacción visual, pero no se presentaron resultados de pruebas de usabilidad. Alternativa recomendada: medir problemas reales y proponer correcciones puntuales de accesibilidad.
Si se aceptara, implicaría rediseño y regresiones visuales;
Efectos a corto plazo distraería del reporte accesible. Al rechazar no se modifica Sprint 2 ni se crea trabajo comprometido.
Efectos a largo plazo Se puede replantear el diseño si un estudio de usabilidad identifica errores observables o barreras. Mantener un registro de la solicitud y su decisión.
Si el diseño corporativo es un estándar transversal Otros proyectos / programas / portafolios compartido entre proyectos, la revisión podría necesitar coordinación de programa; no ocurre automáticamente.
Efectos extraempresariales No se identifican efectos regulatorios ni con proveedores en el caso ficticio. Usuarios podrían ver una interfaz distinta solo si se aprueba en el futuro.
Rechazo justificado por falta de evidencia de valor relativo;
Observaciones adicionales no equivale a despreciar la experiencia del usuario. Si afecta accesibilidad, reabrir con nuevos datos.
SEMANA 07 · SCRUM — CAMBIO | Dr. Alfredo Daza Vergaray

<!-- pág. 13 -->
UNIVERSIDAD NACIONAL DEL SANTA | INGENIERÍA DE SOFTWARE II Revisión y resultado Fecha de ejemplo: 26/10/2026 · Evaluación: PO con equipo · Rechazada en este ciclo como cambio independiente; reconsiderar solo ante evidencia de valor.
Responsable de aplicar / informar Solicitante: representante comercial ficticio. PO: Lucía Rojas. Scrum Master: Iván Cruz. Equipo: UI/UX y desarrollo.
Estimación / contexto Estimada de forma orientativa: 21 puntos si fuera un rediseño completo, sujeta a refinamiento.
4. Criterios comprobables para validar el resultado
• No se modifica el Sprint Backlog actual por esta solicitud.
• FGAP090 contiene decisión, motivo y condiciones para reconsiderarla.
• Una futura nueva solicitud debe señalar un problema verificable y sus criterios de aceptación.
5. Pregunta para alumnos y respuesta docente Pregunta. ¿Es correcto rechazar una solicitud planteada por un alto directivo?
Respuesta fundamentada. Puede ser correcto cuando la autoridad de decisión lo permite y se argumenta por valor, riesgo y dependencias. Si supera la autoridad del PO, se escala según reglas de gobernanza, no por jerarquía informal.
6. Actividad breve de aplicación en su propio proyecto Cada grupo propone un cambio análogo en su proyecto de inteligencia artificial, diligencia FGAP090, identifica si debe aprobarse, rechazarse o diferirse y justifica en qué sprint sería razonable atenderlo. Presenta en 2 minutos el impacto técnico y la decisión.
SEMANA 07 · SCRUM — CAMBIO | Dr. Alfredo Daza Vergaray

<!-- pág. 14 -->
UNIVERSIDAD NACIONAL DEL SANTA | INGENIERÍA DE SOFTWARE II Plantilla de cotejo para el docente Criterio Puntuación sugerida Evidencia observable Claridad del cambio 20 % Describe qué, por qué, alcance y solicitante sin ambigüedad Justificación / valor 20 % Compara alternativas y consecuencias de no hacer el cambio Impactos 25 % Analiza corto/largo plazo y dependencias técnicas y externas Tratamiento Scrum y roles 25 % Distingue Product Backlog y sprint; autoridad, aceptación y decisión Presentación y trazabilidad 10 % FGAP090 completo, legible, consistente y expuesto Relación con el material base Libro SBOK®, 4.ª edición, capítulo 6 «Cambio»: 6.3 solicitudes aprobadas/no aprobadas; 6.4 flexibilidad y estabilidad; 6.5 integración de cambios y refinamiento; 6.6 programas y portafolios; 6.7 responsabilidades; 6.8 comparación con gestión tradicional.
Sílabo UNS 2026-II, Semana 07: “Scrum – Cambio”; evidencia requerida: “Solicitud de Cambio desarrollada”. Las actividades usan los apartados reales del formato FGAP090 entregado por el docente.
SEMANA 07 · SCRUM — CAMBIO | Dr. Alfredo Daza Vergaray
