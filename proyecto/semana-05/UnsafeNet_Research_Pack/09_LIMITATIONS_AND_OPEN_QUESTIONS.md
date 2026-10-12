# 09 — Limitaciones, inconsistencias y preguntas abiertas

Este archivo es deliberadamente crítico. Es el registro de todo aquello que **no debemos maquillar**.

## 1. Limitaciones declaradas por los autores

### Una sola fábrica

El dataset proviene de un único entorno industrial.

Consecuencia:
- baja evidencia de generalización entre dominios.

### Solo dos cámaras

Hay poca variedad de:
- ángulos;
- iluminación;
- distancias;
- backgrounds.

### Solo cuatro conductas inseguras

El espacio de riesgos industriales es muchísimo mayor.

### Falsos positivos en YOLO

Los autores reconocen FPs en algunas clases y recomiendan más datos.

### Piloto corto

Se recomienda repetir el despliegue durante un periodo mayor.

## 2. Inconsistencia: 4 vs 8 clases YOLO

El paper especifica `number of classes = 4`, pero simultáneamente:

- el dataset tiene 8 clases;
- el texto habla de detección safe + unsafe;
- se describen métricas/AP de categorías seguras e inseguras.

**Estado:** no resuelto.

No hay código oficial público conocido para inspeccionar la configuración real.

## 3. Inconsistencia: “32 videos” vs 64

El paper enumera:

- 32 Walkway Violation
- 11 Unauthorized
- 13 Opened Panel
- 8 Forklift Overload

Suma:
**64**

y después confirma resultados sobre 64.

Sin embargo, una frase menciona “a total of 32 videos passing through YOLOv4”.

**Interpretación más probable:** error editorial.

**Regla:** documentarlo; no borrarlo silenciosamente.

## 4. 1–20 s vs 3–18 s

El paper del dataset documenta clips entre **1 y 20 s**.

El experimento Unsafe-Net describe los 64 clips de prueba inseguros como de **3 a 18 s**.

Esto no es necesariamente contradicción:
- el primero describe todo el dataset;
- el segundo, un subconjunto concreto.

## 5. 39 días vs 19 + 20 días

La adquisición completa abarca 39 días.

El paper separa:

- 5–23 noviembre: periodo inicial / construcción de datos / baseline;
- 24 noviembre–13 diciembre: periodo de sistema instalado.

Por eso “39 días” no debe interpretarse como “todo ese video se usó de la misma manera para entrenar”.

## 6. 0.14 s

No es latencia total.

Es la etapa de reconocimiento temporal una vez el clip ya fue reducido.

## 7. 95.81%

Es macro-average de accuracies por clase.

62/64 produce una micro-accuracy distinta.

Siempre especificar qué agregación usamos.

## 8. 75%

Es reducción observada de conductas registradas en un before/after.

No es reducción demostrada de accidentes.

## 9. Falta de código oficial

No se ha identificado un repositorio oficial público de los autores con:

- scripts;
- weights;
- config YOLO;
- entrenamiento ConvLSTM;
- segmentación de acciones;
- GUI;
- firmware del Arduino.

Consecuencia:
la réplica es una **reconstrucción**.

## 10. Falta de labels de detección fácilmente reutilizables

El dataset público está orientado a clips de video.

Para replicar exactamente el detector hay que verificar si las anotaciones de 2,262/329 frames están disponibles por separado. No debe suponerse.

## 11. Hiperparámetros incompletos de ConvLSTM

Pendientes de confirmación:
- optimizer;
- LR;
- epochs;
- batch;
- frame size;
- fixed sequence length;
- padding/truncation;
- random seed;
- Dense dimensions.

## 12. Segmentación temporal

El paper explica el concepto de separar acciones, pero no publica un algoritmo detallado suficientemente reproducible para responder:

- ¿cuántos frames consecutivos hacen una acción?
- ¿cómo se unen detecciones separadas?
- ¿qué gap temporal corta un evento?
- ¿qué threshold se usa para conservar?
- ¿cómo se trata una detección intermitente?

Este es uno de los puntos que nuestra réplica deberá especificar explícitamente.

## 13. Domain shift

Un modelo entrenado en:
- líneas verdes concretas;
- vestimenta específica;
- panel específico;
- bloques y montacargas específicos;

puede aprender correlaciones del escenario y no una noción general de “seguridad”.

La investigación es válida dentro de su dominio, pero no debe venderse como inteligencia industrial universal.

## 14. Riesgo de leakage

En una réplica hay que evitar que clips casi consecutivos del mismo evento/turno aparezcan en train y test si eso genera información redundante.

Idealmente se debe:
- respetar el split oficial;
- registrar origen temporal/cámara;
- evitar crear nuevos splits aleatorios sin justificación.

## 15. Lista de preguntas pendientes

- [ ] ¿Existen públicamente los labels YOLO originales?
- [ ] ¿Existen weights oficiales?
- [ ] ¿Cuál fue el optimizer ConvLSTM?
- [ ] ¿Cuál fue el learning rate?
- [ ] ¿Cuál fue la longitud fija de secuencia?
- [ ] ¿Cuál fue el resize exacto de frames para ConvLSTM?
- [ ] ¿Cómo implementaron exactamente la segmentación temporal?
- [ ] ¿Qué threshold YOLO activaba conservación de frame?
- [ ] ¿Qué stack/framework exacto se usó para ConvLSTM?
- [ ] ¿El firmware del Arduino fue publicado?
- [ ] ¿La solicitud de patente 2025/001387 avanzó a concesión?
