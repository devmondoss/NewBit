# NewBit (PY-NB-001)

> **Sistema web con Visión Artificial para la detección de actos inseguros en áreas operativas de manufactura metalmecánica.**  
> Basado en la arquitectura bi-etápica de *Unsafe-Net* (Önal y Dandıl, 2024).

---

## 1. Identidad y Contexto del Proyecto

* **Código de Proyecto:** `PY-NB-001`
* **Curso:** Ingeniería de Software II (Semestre 2026-II) · Universidad Nacional del Santa (UNS)
* **Docente Asignado:** Prof. Dr. Alfredo Daza Vergaray
* **Equipo Scrum (Grupo D3):**
  * **Product Owner:** Albert Sebastian Chumacero Chávarry
  * **Scrum Master & Developer:** Anthony Gabriel Lopez Yrribarren
  * **Developer:** Luis Fernando Salazar Diaz
* **Dominio de Aplicación:** Taller de manufactura metalmecánica (mecanizado con tornos, fresadoras, taladros de columna y pasarelas de seguridad peatonal).
* **Dataset Base:** *Video Dataset for Safe and Unsafe Behaviours* (Kafaoğlu Metal Plastik Makine San. ve Tic. A.Ş. / Mendeley Data, DOI: `10.17632/xjmtb22pff.1`).
* **Investigación Base:** *Unsafe-Net: A Two-Stage Spatial-Temporal Convolutional Architecture for Unsafe Human Action Recognition in Industrial CCTV Videos* (Önal & Dandıl, 2024).

---

## 2. Resumen del Incremento MVP (Sprints 1 y 2 – 15 Puntos de Historia)

El proyecto se encuentra en el **hito de congelamiento de software (~50% del Product Backlog total)**, habiendo implementado el 100% de los puntos de historia asignados a los Sprints 1 y 2 (15 SP) correspondientes a la **Etapa 1 de Unsafe-Net** (Filtro espacio-temporal inteligente):

| Épica | Historia de Usuario | Rol de Negocio (FGAP030) | SP | Sprint | Estado | Descripción Técnica y Funcional |
|---|---|---|:---:|:---:|:---:|---|
| **EP01** | **HU01: Ingestión y validación de video** | Jorge Ponce (TI Planta) | 3 | S1 | **Completado** | Subida multipart `.mp4`/`.avi` ($\le 100$ MB), validación OpenCV de FPS, resolución, duración y registro en SQLite. |
| **EP01** | **HU02: Extracción y visor HTML5** | Jorge Ponce (TI Planta) | 2 | S1 | **Completado** | Normalización de fotogramas a $640\times 640$ px, streaming HTTP y ficha técnica de metadatos (FGAP040). |
| **EP01** | **HU03: Catálogo web interactivo** | Lucía Ramos (Monitoreo) | 2 | S1 | **Completado** | Interfaz con Dropzone Drag & Drop, barra de progreso XHR en tiempo real, tabla de estados y borrado seguro de archivos. |
| **EP03** | **HU04: Submuestreo temporal inteligente** | Jorge Ponce (TI Planta) | 2 | S2 | **Completado** | Algoritmo con OpenCV para reducir de 24–30 FPS a 5.0 FPS, logrando **75% a 85% de reducción** en fotogramas a procesar. |
| **EP06** | **HU11: Calibración dinámica de umbrales** | Jorge Ponce (TI Planta) | 2 | S2 | **Completado** | Interfaz web con sliders para ajustar confianza ($0.10–0.95$) e IoU ($0.10–0.90$) en caliente con bitácora de auditoría en SQLite. |
| **EP02** | **HU05: Inferencia espacial con YOLOv8n** | Mariana Torres (Supervisora SST) | 2 | S2 | **Completado** | Patrón singleton para `yolov8n.pt`, filtrado de clase `person` (operarios), renderizado de bounding boxes verde esmeralda y separación de tiempo muerto. |
| **EP03** | **HU06: Agrupamiento temporal y clip final** | Mariana Torres (Supervisora SST) | 2 | S2 | **Completado** | Agrupador de secuencias continuas con descarte de acciones fugaces ($< 1.0$ s) y ensamblado de clip final en `storage/outputs/`. |

---

## 3. Arquitectura del Monorepo

El repositorio sigue un esquema de monorepo 100% en Python, separando la lógica web, la inferencia de visión computacional y el almacenamiento de medios:

```text
NewBit/
├── .venv/                              # Entorno virtual de Python 3.12+ (excluido de git)
├── run.bat                             # Script de arranque de un clic para Windows (Batch)
├── run.ps1                             # Script de arranque nativo para Windows (PowerShell)
├── ROADMAP_REESTRUCTURACION_NEWBIT.md  # Hoja de ruta canónica de gobernanza y auditoría
├── curso/                              # Entregables de gestión académica (Semanas 2 a 5)
└── proyecto-newbit/                    # Código fuente del software
    ├── app/                            # Capa de aplicación web (FastAPI)
    │   ├── api/                        # Controladores y rutas REST
    │   │   ├── routes_videos.py        # Endpoints de ingesta, streaming y catálogo (HU01-HU03)
    │   │   ├── routes_calibration.py   # Endpoints de calibración y auditoría (HU11)
    │   │   └── routes_processing.py    # Endpoints de inferencia YOLOv8 y agrupamiento (HU05-HU06)
    │   ├── templates/                  # Plantillas responsivas Jinja2 + Tailwind CSS
    │   │   ├── base.html               # Estructura visual compartida y navegación
    │   │   ├── index.html              # Dashboard analítico con métricas en tiempo real
    │   │   ├── videos_catalog.html     # Catálogo con Dropzone interactiva
    │   │   ├── video_detail.html       # Reproductor HTML5 dual y ficha técnica
    │   │   └── calibration.html        # Panel de sintonía fina de umbrales
    │   ├── static/                     # Archivos estáticos (CSS personalizado, JS interactivo)
    │   ├── config.py                   # Parámetros globales y límites de almacenamiento
    │   ├── db.py                       # Capa de persistencia relacional ligera con SQLite
    │   └── main.py                     # Instancia principal de la aplicación FastAPI
    ├── ml/                             # Módulos de Machine Learning y Visión Artificial
    │   ├── weights/                    # Binarios de modelos neuronales (yolov8n.pt)
    │   ├── video_processor.py          # Extracción y validación técnica con OpenCV
    │   ├── sampler.py                  # Motor de submuestreo inteligente de zancada temporal
    │   ├── detector.py                 # Inferencia con YOLOv8n y dibujo de bounding boxes
    │   └── sequence_grouper.py         # Agrupamiento de secuencias y renderizado MP4
    ├── storage/                        # Almacenamiento local estructurado (ignorado en git)
    │   ├── uploads/                    # Videos originales subidos por los usuarios
    │   ├── frames/                     # Fotogramas normalizados (640x640) y anotados
    │   └── outputs/                    # Clips finales filtrados procesados por la Etapa 1
    ├── tests/                          # Suite completa de pruebas automatizadas
    │   ├── fixtures/                   # Generador y clips sintéticos representativos
    │   ├── test_environment.py         # Comprobación de librerías y stack
    │   ├── test_server_base.py         # Salud técnica de endpoints y renderizado
    │   ├── test_video_ingestion.py     # Validación técnica de ingesta (HU01)
    │   ├── test_video_viewer.py        # Ficha técnica y streaming (HU02)
    │   ├── test_videos_catalog.py      # Catálogo y borrado seguro (HU03)
    │   ├── test_sampler.py             # Submuestreo inteligente de frames (HU04)
    │   ├── test_calibration.py         # Calibración dinámica y auditoría (HU11)
    │   ├── test_detector.py            # Inferencia espacial con YOLOv8n (HU05)
    │   ├── test_sequence_grouper.py    # Agrupamiento temporal y síntesis MP4 (HU06)
    │   └── test_e2e_pipeline.py        # Prueba de integración de extremo a extremo
    ├── investigacion/                  # Research Pack y fichas técnicas de Unsafe-Net
    └── requirements.txt                # Dependencias fijadas y verificadas
```

---

## 4. Requisitos del Sistema

* **Sistema Operativo:** Windows 10/11, Linux (Ubuntu 20.04+) o macOS (Apple Silicon compatible).
* **Python:** Versión `3.10`, `3.11` o `3.12` (verificado en Python 3.12.10).
* **Aceleración de Hardware:** Inferencia por defecto optimizada para **CPU** (~25–40 ms por frame con YOLOv8n). Compatible automáticamente con **GPU NVIDIA CUDA** si está disponible mediante PyTorch.
* **Espacio en Disco:** Mínimo 500 MB libres para almacenamiento temporal de fotogramas y base de datos SQLite.

---

## 5. Guía Rápida de Instalación y Despliegue

### Opción A: Inicio con un solo clic (Windows)
En la raíz del proyecto, ejecuta mediante consola o doble clic:
```cmd
run.bat
```
O desde PowerShell:
```powershell
.\run.ps1 -OpenBrowser
```

### Opción B: Instalación Manual por Comandos

1. **Clonar el repositorio y situarse en la raíz:**
   ```bash
   git clone https://github.com/devmondoss/NewBit.git
   cd NewBit
   ```

2. **Crear y activar el entorno virtual:**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. **Instalar dependencias de Python:**
   ```bash
   pip install --upgrade pip
   pip install -r proyecto-newbit/requirements.txt
   ```

4. **Lanzar el servidor web local:**
   ```bash
   uvicorn app.main:app --app-dir proyecto-newbit --host 127.0.0.1 --port 8000 --reload
   ```

---

## 6. Mapa de Navegación y Endpoints

Una vez iniciado el servidor, accede a las siguientes vistas en tu navegador:

| Módulo / Vista | URL Local | Descripción |
|---|---|---|
| **Dashboard Principal** | `http://127.0.0.1:8000/` | Visión ejecutiva con métricas acumuladas, total de frames, % de ahorro temporal y estado del modelo. |
| **Catálogo de Videos** | `http://127.0.0.1:8000/videos` | Zona Drag & Drop para cargar clips `.mp4`/`.avi`, tabla de estados de procesamiento y acciones rápidas. |
| **Ficha Técnica y Visor Dual** | `http://127.0.0.1:8000/videos/{id}` | Reproductor HTML5 nativo, barra de submuestreo, inferencia YOLOv8, galería de detecciones y reproductor del clip final procesado. |
| **Panel de Calibración** | `http://127.0.0.1:8000/calibration` | Sliders interactivos para calibrar umbrales de confianza e IoU en caliente con bitácora de auditoría. |
| **Documentación OpenAPI (Swagger)** | `http://127.0.0.1:8000/docs` | Explorador interactivo de todas las rutas y especificaciones de la API REST. |
| **Especificación Redoc** | `http://127.0.0.1:8000/redoc` | Documentación técnica alternativa para desarrolladores. |

---

## 7. Ejecución de Pruebas Automatizadas

NewBit cuenta con una cobertura integral de pruebas unitarias, de integración y extremo a extremo (E2E). Para ejecutar la suite completa de **43 pruebas**:

```powershell
# Ejecutar todas las pruebas con reporte detallado
.\.venv\Scripts\python.exe -m unittest discover -s proyecto-newbit/tests -v
```

Resultado esperado:
```text
Ran 43 tests in ~4.5s
OK
```

Para ejecutar una prueba específica:
```powershell
# Prueba de Extremo a Extremo (E2E) con clip de taller metalmecánico
.\.venv\Scripts\python.exe -m unittest proyecto-newbit/tests/test_e2e_pipeline.py -v

# Pruebas del detector YOLOv8n
.\.venv\Scripts\python.exe -m unittest proyecto-newbit/tests/test_detector.py -v
```

---

## 8. Trazabilidad con la Guía SBOK y Entregables del Curso

Los entregables de gestión ágil aprobados se encuentran normalizados en la carpeta [`curso/`](../curso/README.md):

* **Semana 2:** Acta de Constitución (`FGAP010`) y Cuadro Comparativo de Principios de Scrum (`Cuadro_Principios_Scrum_NewBit`).
* **Semana 3:** Registro de Roles y Prototipos (`FGAP030`), Presentación del Proyecto (`PPT_Presentacion_NewBit`) y Diagrama de Arquitectura.
* **Semana 4:** Justificación Técnica y Presupuestaria (`EGAP015`) y Catálogo Canónico de Épicas (`FGAP040`).
* **Semana 5:** Tablero Kanban oficial de 12 HU (`Tablero_Kanban_NewBit`), Priorización MoSCoW (`Priorizacion_MoSCoW_100_Puntos_NewBit`), Presentación Puño de Cinco (`Presentacion_Fist_of_Five`) y Criterios de Terminado (`FGAP070`).
* **Hoja de Ruta Canónica:** [`ROADMAP_REESTRUCTURACION_NEWBIT.md`](../ROADMAP_REESTRUCTURACION_NEWBIT.md).

---

## 9. Licencia y Créditos

Este proyecto es de uso académico y de investigación en la Universidad Nacional del Santa (UNS).  
El dataset de entrenamiento y evaluación se utiliza bajo licencia **Creative Commons Attribution 4.0 International (CC BY 4.0)**:  
> Önal, O., & Dandıl, E. (2024). *Video Dataset for Safe and Unsafe Behaviours in Metalworking Manufacturing*. Mendeley Data, V1, doi: 10.17632/xjmtb22pff.1.
