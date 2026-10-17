# FGAP070 – Criterios de Terminado: NewBit (Versión Oficial Normalizada)

- **Archivos para entregar** (esta carpeta): `FGAP070_Criterios_de_Terminado_NewBit.docx` (editable) y `FGAP070_Criterios_de_Terminado_NewBit.pdf`.
- **Tipo:** Formato oficial de Criterios de Terminado (*Definition of Done* – DoD) aplicable transversalmente a todas las Historias de Usuario del Product Backlog.
- **Fecha de elaboración:** 17/10/2026 · Versión 1.0 (Grupo D3).
- **Control de versiones:** Elaborado por el Equipo de Desarrollo (Anthony Lopez y Luis Fernando Salazar Diaz) · Revisado por el Scrum Master (Anthony Lopez) · Aprobado por el Product Owner (Albert Chumacero).
- **Marco de referencia:** SBOK Guide / Secuencia de avances de proyectos de software (UNS, Ing. de Software II - Dr. Alfredo Daza Vergaray).

---

## 1. Identificación del Proyecto
* **Código del Proyecto:** `PY-NB-001`
* **Nombre del Proyecto:** Sistema web con Visión Artificial para la detección de actos inseguros en áreas operativas de manufactura metalmecánica
* **Producto:** Plataforma NewBit
* **Código del Estándar:** `CT-NB-001 – Definición de Terminado del Incremento de Software NewBit`
* **Área de Aplicación:** Taller metalmecánico de mecanizado y torneado (referencia experimental: dataset de Kafaoğlu Metal Plastik, Eskişehir; Önal & Dandıl, 2024).

---

## 2. Concepto y Marco de Calidad
Los **Criterios de Terminado (Definition of Done - DoD)** constituyen el conjunto formal de acuerdos técnicos, requisitos de aseguramiento de la calidad y validaciones metodológicas que se aplican a **todas** las historias de usuario del Product Backlog (FGAP040 / FGAP060).

> **Distinción clave:**  
> A diferencia de los *Criterios de Aceptación* (que son individuales y definidos por el Product Owner para cada historia específica), la *Definición de Terminado* es común y obligatoria para todo el backlog. Garantiza que ningún incremento sea entregado con deuda técnica, fallas de seguridad, código no probado o documentación incompleta.

---

## 3. Matriz Canónica de Criterios de Terminado (FGAP070)

| Campo del Formato | Definición de Terminado Oficial (NewBit - PY-NB-001) |
|---|---|
| **Código completo** | `CT-NB-001 – Definición de Terminado del incremento de Visión Artificial (Plataforma NewBit)` |
| **Prueba unitaria** | Componentes y módulos nuevos o modificados (ingesta de video, validación de formatos `.mp4`/`.avi`, submuestreo de fotogramas vía OpenCV, calibración dinámica de umbrales IoU/confianza y pipeline de detección YOLOv8) con pruebas unitarias automatizadas ejecutadas y registradas vía `pytest`; todas las fallas bloqueantes o de regresión deben corregirse al 100% antes de dar por terminada la historia. |
| **Prueba integrada** | Flujo completo e integrado verificado de extremo a extremo: Interfaz web de monitoreo (`FastAPI` + `Jinja2`/`Tailwind`) $\leftrightarrow$ API REST de carga $\leftrightarrow$ Almacenamiento local estructurado (`storage/uploads/`, `storage/frames/`, `storage/outputs/`) $\leftrightarrow$ Motor de inferencia espacial YOLOv8; manejo robusto de excepciones (videos corruptos, archivos no soportados, parámetros fuera de rango) y codificación de salida H.264 reproducible en navegadores modernos. |
| **Revisión cruzada (pares)** | Revisión técnica de código obligatoria entre Developers (Luis Fernando Salazar Diaz y Anthony Lopez) mediante inspección de pares; verificación de legibilidad, arquitectura modular limpia, apego al estándar PEP 8, ausencia de credenciales embebidas y optimización de latencia en CPU/GPU; resolución formal de observaciones críticas antes de la aprobación del incremento. |
| **Certificación** | Prototipo de software académico y experimental desarrollado en el marco del curso Ingeniería de Software II (UNS); no constituye una certificación oficial de Seguridad y Salud en el Trabajo (SST) bajo la Ley N° 29783 ni sustituye la supervisión humana del Jefe de Taller, Prevencionista o Supervisor de Seguridad. |
| **Documentación** | Historias de usuario (FGAP040) y criterios de aceptación actualizados con evidencia de validación; manual técnico de instalación y archivo `README.md` al día; para los modelos de Visión Artificial: trazabilidad del dataset de Mendeley (Önal & Dandıl, 2024), registro de versión de pesos (`yolov8n.pt`), hiperparámetros de calibración (confianza 0.50, IoU 0.45) y registro de métricas de desempeño (mAP@50, FPS). |
| **Aprobaciones técnicas** | El Equipo de Desarrollo (Developers) certifica la ejecución exitosa de la suite de pruebas, la integración continua sin errores de sintaxis o ejecución, ausencia de defectos de severidad alta/bloqueante y la disponibilidad funcional del incremento en el entorno de demostración web local (`http://127.0.0.1:8000`). |
| **Aprobaciones administrativas** | El Product Owner (Albert Chumacero) inspecciona y valida el cumplimiento individual de los criterios de aceptación de cada Historia de Usuario en el evento de Sprint Review; su aceptación administrativa valida el valor de negocio, pero no sustituye ni flexibiliza la Definición de Terminado técnica. |
| **Otras (Ética, Privacidad y Gobernanza)** | Cumplimiento estricto de la licencia CC BY 4.0 del dataset de referencia; protección de la privacidad operativa (el sistema analiza posturas corporales, trayectorias y zonas de proximidad peligrosa a tornos/fresadoras, prohibiendo expresamente la biometría o reconocimiento facial); las alertas emitidas son de carácter preventivo y orientativo; respaldo periódico y trazable en el repositorio GitHub oficial. |

---

## 4. Responsabilidades y Aplicabilidad en el Flujo Scrum

1. **Responsabilidad de los Developers:**  
   Los desarrolladores (Luis Salazar y Anthony Lopez) son los garantes de la calidad técnica. Ninguna Historia de Usuario puede pasar a la columna `Done` del Tablero Kanban sin cumplir la totalidad de los criterios técnicos (pruebas, revisión por pares, integración y documentación).
2. **Rol del Scrum Master:**  
   Anthony Lopez supervisa que el equipo no reduzca los estándares de calidad ante presiones de tiempo y gestiona cualquier impedimento que dificulte el cumplimiento de la DoD.
3. **Rol del Product Owner:**  
   Albert Chumacero verifica en la Sprint Review que el incremento resuelva la necesidad operativa de planta antes de firmar la aceptación del Sprint.

---

## 5. Control de Aprobación y Firmas

| Rol | Nombre | Firma / Estado |
|---|---|---|
| **Product Owner** | Albert Chumacero | Aprobado |
| **Scrum Master & Developer** | Anthony Lopez | Aprobado |
| **Developer** | Luis Fernando Salazar Diaz | Aprobado |
