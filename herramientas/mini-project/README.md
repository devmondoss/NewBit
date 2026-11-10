# Mini Project: editor de cronogramas tipo MS Project (localhost)

Editor web local para hacer y modificar cronogramas cuando no hay MS Project (p. ej. en Mac). Trabaja directamente con el **XML de MS Project (formato MSPDI)**: lo que guardas aquí se abre en MS Project o ProjectLibre y desde allí se guarda como `.mpp`.

## Cómo abrirlo
```bash
python3 herramientas/mini-project/servidor.py
```
- Abre el navegador en `http://127.0.0.1:8780/`. Si ese puerto está ocupado, usa el siguiente libre y lo muestra en la terminal.
- Para abrir un archivo al iniciar: `--abrir <ruta del .xml relativa al repo>`. Para no abrir el navegador: `--sin-navegador`. Para otro puerto: `--puerto 8800`.
- Solo usa la biblioteca estándar de Python. El servidor escucha solo en `127.0.0.1`, solo lee y escribe `.xml` dentro del repo y rechaza peticiones de otras páginas. Se cierra con Ctrl+C.

## Qué hace
| Función | Cómo |
|---|---|
| Tabla como MS Project | Id · Nombre de tarea · Duración · Comienzo · Fin · Predecesoras · Nombres de los recursos (separados por «;»). Se edita escribiendo en la celda; Enter o ↑/↓ confirma y mueve. |
| Programación automática | Vínculos **fin → comienzo** con retraso opcional (`3+2d`), días laborables de lunes a viernes, **feriados** (botón Proyecto) y resúmenes calculados con sus subtareas. Mismo cálculo que MS Project para estos casos. |
| Fijar una fecha | Escribir en «Comienzo» o arrastrar la barra crea la restricción «no comenzar antes de» (icono 📌). Para quitarla, borrar la celda. |
| Cambiar la duración | Escribirla (`5`, `5 días`, `2 sem`), editar el Fin o arrastrar el borde derecho de la barra. `0` = hito (◆). |
| Estructura | Botones Sangría/Anular (Alt+Shift+→/←), Subir/Bajar (Alt+Shift+↑/↓), Insertar (tecla Insert), Hito, Eliminar (Supr), contraer y expandir resúmenes (▼). |
| Vincular | Seleccionar varias filas (Shift o Ctrl/Cmd + clic en el número) y pulsar «Vincular»: quedan en cadena. |
| Gantt | Barras, resúmenes, hitos, flechas de predecesoras, fines de semana y feriados sombreados, línea de hoy y zoom (de semanas a días). |
| Deshacer | Ctrl+Z / Ctrl+Y (hasta 200 pasos). |
| Guardar | Ctrl+S guarda el `.xml`. «Guardar como» pide una ruta dentro del repo. |
| PNG | Descarga la vista (tabla + Gantt) como imagen. |
| Word/PDF | Guarda y ejecuta el `generar_*.py` de la carpeta del XML con `--xml <archivo> --pdf` (ver la convención de abajo). |

## Convención para el botón Word/PDF
Si en la carpeta del `.xml` hay un `generar_<formato>.py` que acepta `--xml <archivo>` (y opcionalmente `--pdf`), el botón lo ejecuta con el Python de `.venv`. Ejemplo: [`generar_fgap080.py`](../../curso/semana-09-stakeholders-y-lanzamiento/nuestras-entregas/FGAP080_Cronograma_Lanzamiento_NewBit/generar_fgap080.py) rehace el Word del FGAP080, el Gantt en PNG, el `.md` y el PDF (con Pages) a partir del XML editado. Para un formato nuevo (otro cronograma, otro sprint), se copia ese generador y se ajusta el encabezado.

## Límites
- Solo vínculos fin → comienzo. Los otros tipos (CC, FF, CF) se leen como fin → comienzo y se avisa en la barra de estado.
- Duraciones en días enteros. Los recursos son solo nombres asignados (se guardan como recursos y asignaciones de MS Project); sin costos, nivelación ni línea base.
- Se probó el cálculo de fechas y la ida y vuelta del XML con el FGAP080 de 80 filas: mismas fechas, vínculos y recursos que `plan_lanzamiento.py`. **No se ha probado todavía abrir sus XML en MS Project**: la primera vez, comprobar que las fechas coinciden.

## Archivos
`servidor.py` (servidor local y API) · `index.html` · `estilos.css` · `app.js` (cálculo, Gantt y lectura y escritura del MSPDI).
