# 08 — Despliegue real, GUI y piloto

## 1. El proyecto no terminó en un notebook

Los autores desplegaron un sistema operativo en la fábrica.

Componentes:

```text
Cámaras
↓
YOLOv4
↓
ConvLSTM
↓
Python application
├── PyQt GUI
├── reports
├── logs
└── control de alerta
        ↓ Wi-Fi
      ESP8266
        ↓
     Arduino Uno
      ├── alerta sonora
      └── alerta visual
```

## 2. GUI

Tecnologías:
- Python
- PyQt Designer

Funciones reportadas:
- iniciar/detener sistema;
- observar actividades inseguras;
- abrir reportes;
- activar/controlar sistema de alerta.

## 3. Registro

Cuando ocurre un comportamiento inseguro:

- se genera un reporte de texto;
- se registra información del evento;
- se puede acceder desde la GUI.

El paper no publica un esquema completo de base de datos; no debemos inventarlo.

## 4. Electrónica

Comunicación:

```text
software → Wi-Fi → ESP8266 → Arduino Uno
```

El Arduino dispara:
- aviso visual;
- aviso audible.

## 5. Diseño de campo

### Periodo anterior a instalación

**5–23 noviembre 2022**

Un experto de seguridad contabilizó:
**518 conductas inseguras**

en las cuatro clases.

### Periodo posterior

Los trabajadores fueron informados del sistema.

**24 noviembre–13 diciembre 2022**

Se registraron:
**134 conductas inseguras**

Reducción observada:
aproximadamente **75%**.

## 6. Qué significa y qué no significa el 75%

### Sí puede decirse

> Durante el periodo posterior a la instalación se observaron aproximadamente 75% menos ocurrencias de las cuatro conductas inseguras registradas.

### No puede decirse

- “el sistema reduce 75% los accidentes”;
- “Unsafe-Net evita 75% de lesiones”;
- “se demostró causalmente una reducción del 75%”;
- “tendrá el mismo efecto en cualquier fábrica”.

## 7. Diseño experimental limitado

No es un ensayo controlado aleatorizado.

Entre “antes” y “después” ocurren cambios importantes:

- se instala el sistema;
- los empleados son informados;
- saben que existe alerta;
- pueden modificar su conducta por observación/conciencia;
- no hay grupo control descrito.

Por tanto, el resultado es valioso como **pilot field evidence**, pero no como prueba causal fuerte.

## 8. Validación humana

El especialista de seguridad revisó resultados.

El paper reporta un caso en el que:

```text
Opened Panel Cover
→ clasificado como Unauthorized Intervention
```

Esto muestra que la evaluación en campo también incluyó revisión humana.
