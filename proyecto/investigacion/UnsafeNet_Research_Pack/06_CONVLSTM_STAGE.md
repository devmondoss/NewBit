# 06 — Etapa ConvLSTM

## 1. Rol

ConvLSTM recibe los fragmentos reducidos generados después de YOLOv4 y clasifica el comportamiento inseguro.

Las cuatro clases finales son:

1. Safe Walkway Violation
2. Unauthorized Intervention
3. Opened Panel Cover
4. Carrying Overload with Forklift

## 2. Por qué ConvLSTM

Una CNN normal modela estructura espacial.

Una LSTM modela secuencias.

ConvLSTM integra convoluciones dentro de la dinámica recurrente para conservar estructura espacial mientras aprende dependencias temporales.

Conceptualmente:

```text
frame_t + estado_t-1
        ↓
convoluciones dentro de gates LSTM
        ↓
estado_t
        ↓
secuencia espacio-temporal
```

## 3. Arquitectura publicada

El paper describe **4 bloques** formados por:

```text
ConvLSTM
→ MaxPooling
→ Dropout
```

Filtros:

| Bloque | Filtros |
|---|---:|
| 1 | 4 |
| 2 | 8 |
| 3 | 14 |
| 4 | 16 |

Parámetros explícitos:

- `kernel_size = (3, 3)`
- `pool_size = (1, 2, 2)`
- `dropout = 0.2`
- activation: `tanh`

Al final:

```text
Flatten
→ Dense
→ clase
```

## 4. Datos utilizados

Para la clasificación temporal:

- train: **452 videos**
- test: **64 videos**

El test está formado por:

| Clase | Test |
|---|---:|
| Safe Walkway Violation | 32 |
| Unauthorized Intervention | 11 |
| Opened Panel Cover | 13 |
| Carrying Overload with Forklift | 8 |
| **Total** | **64** |

## 5. Dos experimentos

### A. ConvLSTM sin reducción previa

Se procesa el clip completo.

Resultado promedio reportado:
**85.78% Acc**

### B. Unsafe-Net = YOLOv4 + ConvLSTM

Se reduce el video antes del modelo temporal.

Resultado promedio reportado:
**95.81% Acc**

Esta comparación es el experimento más importante del paper.

## 6. Confusiones principales

Con Unsafe-Net:

- Walkway Violation: todos los test correctamente clasificados;
- Forklift Overload: todos correctamente clasificados;
- Unauthorized Intervention: 1 error;
- Opened Panel Cover: 1 error.

Los errores son entre:

```text
Unauthorized Intervention
↔
Opened Panel Cover
```

Esto tiene sentido visual porque ambas acciones ocurren en una zona de intervención/panel.

## 7. Parámetros NO suficientemente documentados

No debemos inventar:

- optimizer exacto;
- learning rate;
- scheduler;
- batch size de ConvLSTM;
- número exacto de epochs;
- estrategia exacta de padding/truncation;
- resolución exacta de cada frame al entrar en ConvLSTM;
- unidades exactas de la(s) Dense final(es);
- seed;
- criterio exacto de early stopping;
- augmentations temporales.

Algunas de estas cosas podrían aparecer con más detalle en la tesis, pero no deben darse por conocidas hasta verificar cada una.

## 8. Decisión para la réplica

Si un hiperparámetro no está documentado, nuestra implementación debe registrar:

```yaml
source: replica_decision
reason: not specified by original authors
value: ...
```

Esto mantiene honestidad y reproducibilidad.
