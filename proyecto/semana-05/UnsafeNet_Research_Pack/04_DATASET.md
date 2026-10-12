# 04 — Dataset oficial

## 1. Identificación

**Nombre:** Video Dataset for Safe and Unsafe Behaviours  
**Autores:** Oğuzhan Önal, Emre Dandıl  
**Versión:** 1  
**Publicado:** 11 junio 2024  
**DOI:** `10.17632/xjmtb22pff.1`  
**Licencia:** CC BY 4.0

Fuente oficial:
https://data.mendeley.com/datasets/xjmtb22pff/1

Paper de documentación:
https://pmc.ncbi.nlm.nih.gov/articles/PMC11367630/

## 2. Origen

Fábrica:
**Kafaoğlu Metal Plastik Makine San. ve Tic. A.Ş.**

Ubicación:
**Eskişehir, Türkiye**

Periodo:
**5 noviembre 2022 – 13 diciembre 2022**

Duración:
- 39 días;
- aproximadamente 4,000 horas de video bruto.

## 3. Cámaras

| Propiedad | Valor |
|---|---|
| Cantidad | 2 |
| Marca | UNV |
| Modelo | IPC2122CR3-PF40-A |
| Resolución | 1920×1080 |
| FPS | 24 |
| Codec | H.264 |
| Formato | MP4 |

Las cámaras identificadas en el paper de datos son la **9** y la **14**, con áreas físicas distintas.

## 4. Clases

El dataset tiene 8 clases: cuatro seguras y cuatro inseguras.

| ID | Clase | Tipo | Definición operacional |
|---:|---|---|---|
| 0 | Safe Walkway Violation | Unsafe | caminar fuera del camino verde |
| 1 | Unauthorized Intervention | Unsafe | intervenir el panel sin el chaleco/condición de autorización definida |
| 2 | Opened Panel Cover | Unsafe | dejar el panel abierto después de intervención |
| 3 | Carrying Overload with Forklift | Unsafe | montacargas transporta 3 o más bloques |
| 4 | Safe Walkway | Safe | caminar dentro del camino verde |
| 5 | Authorized Intervention | Safe | intervención autorizada con la condición visual definida |
| 6 | Closed Panel Cover | Safe | panel cerrado después de intervención |
| 7 | Safe Carrying | Safe | montacargas transporta 2 bloques o menos |

## 5. Distribución train/test

| Clase | Train | Test | Total |
|---|---:|---:|---:|
| Safe Walkway Violation | 178 | 32 | 210 |
| Safe Walkway | 50 | 25 | 75 |
| Unauthorized Intervention | 97 | 11 | 108 |
| Authorized Intervention | 23 | 15 | 38 |
| Opened Panel Cover | 129 | 13 | 142 |
| Closed Panel Cover | 19 | 13 | 32 |
| Carrying Overload with Forklift | 48 | 8 | 56 |
| Safe Carrying | 22 | 8 | 30 |
| **Total** | **566** | **125** | **691** |

## 6. Duración de los clips

| Clase | Promedio | Mínimo | Máximo |
|---|---:|---:|---:|
| Safe Walkway Violation | 9.7 s | 4 s | 17 s |
| Safe Walkway | 9.2 s | 4 s | 20 s |
| Unauthorized Intervention | 10.2 s | 6 s | 20 s |
| Authorized Intervention | 8.6 s | 4 s | 15 s |
| Opened Panel Cover | 5.8 s | 2 s | 12 s |
| Closed Panel Cover | 4.6 s | 1 s | 10 s |
| Carrying Overload with Forklift | 6.9 s | 3 s | 13 s |
| Safe Carrying | 7.2 s | 2 s | 12 s |

## 7. Convención de archivos

Ejemplos documentados:

```text
0_tr1
0_tr2
0_te1
```

Patrón:

```text
<class_id>_tr<video_number>
<class_id>_te<video_number>
```

## 8. Importante: clips multiconducta

El paper del dataset dice que algunos clips pueden contener **más de un comportamiento**.

Esto explica por qué la arquitectura original añade un proceso posterior para separar el contenido antes de ConvLSTM.

## 9. Dataset de video vs dataset de YOLO

El dataset público es fundamentalmente un dataset de **videos**.

El paper original, en cambio, también utilizó un conjunto de **frames anotados con bounding boxes** para entrenar YOLOv4:

- 2,262 imágenes de entrenamiento;
- 329 imágenes de test;
- anotación con LabelImg.

Esas anotaciones de detección no deben asumirse automáticamente como disponibles dentro del paquete público de Mendeley.

### Consecuencia para nuestra réplica

Si queremos entrenar YOLO desde cero de forma fiel, probablemente tendremos que:

1. extraer frames;
2. definir las categorías de detección;
3. volver a anotar bounding boxes;
4. generar labels compatibles con YOLO.

Esto es uno de los principales costos de reproducción.

## 10. Licencia

Mendeley declara **CC BY 4.0**.

Esto permite reutilización y adaptación con atribución adecuada. Para cualquier entrega académica se debe citar:

- autores;
- DOI del dataset;
- paper de Unsafe-Net;
- paper de Data in Brief.
