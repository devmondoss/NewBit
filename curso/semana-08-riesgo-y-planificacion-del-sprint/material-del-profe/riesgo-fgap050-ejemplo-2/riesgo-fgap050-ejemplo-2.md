# FGAP050 Riesgo del Proyecto: ejemplo 2 (acceso no autorizado a imágenes, Retinopatía)

- **Fuente:** `riesgo-fgap050-ejemplo-2.pdf` (llegó como `FGAP050_Segundo_Ejemplo_Riesgo_Privacidad_Imagenes_UNS.pdf`). 1 pág., con capa de texto.
- **De quién:** docente. **Ejemplo resuelto con datos ficticios (IA-RD-2026-02 Retinopatía), no del equipo.**
- **Semana:** 8. Se agregó al repo el 02/11/2026; el pie dice «Ejemplo académico para la semana 8».
- **Tipo de `.md`:** Resumen (documento corto). La estructura del formato y la tabla de escalas están en el [ejemplo 1](../riesgo-fgap050-ejemplo-1/riesgo-fgap050-ejemplo-1.md).

## Contenido del ejemplo (R-04)
- **Versión:** v1.0, 02/11/2026. La hizo el equipo Scrum, la revisó el SM y la aprobó la PO. Motivo: «Registro inicial del riesgo».
- **Riesgo:** acceso no autorizado a imágenes de retina y resultados de pacientes en el intercambio entre la interfaz, la API y el almacenamiento. Consecuencias: pérdida de confidencialidad, incidentes de seguridad y suspensión del piloto.
- **Causa raíz:** faltan las pruebas de control de acceso por roles y la verificación de permisos sobre archivos. Hay rutas de descarga sin proteger y el almacenamiento privado no está validado.
- **Trigger:** en pruebas de seguridad, una petición **sin sesión válida recibe HTTP 200** sobre una imagen o reporte protegido, o se detecta una URL pública de almacenamiento. Eso es señal para detener el piloto.
- **Entregables afectados:** autenticación, API de descarga y consulta, repositorio privado de imágenes, informe de resultados, pruebas de seguridad y versión demostrable del sprint.
- **Evaluación:** probabilidad 0,50 (probable) × impacto 0,80 (muy alto) = **0,40 → ALTO**.

## Para NewBit
El riesgo análogo en NewBit es la exposición de videos de operarios, que son datos personales del personal de planta. El trigger del ejemplo es verificable con una prueba automática (HTTP 200 sin sesión), y conviene que los triggers de NewBit también lo sean.
