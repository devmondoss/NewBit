# Herramientas

Archivos para mantener el repo en orden. No son del curso ni del proyecto.

- [`indice-de-archivos.md`](indice-de-archivos.md): lista de cada PDF, Word, PPT o imagen del repo con el `.md` que lo resume. Claude lo lee en vez de abrir los originales, para ahorrar tiempo.
- [`mini-project/`](mini-project/README.md): **editor de cronogramas tipo MS Project en localhost** (`python3 herramientas/mini-project/servidor.py`). Abre y guarda el XML de MS Project (MSPDI), calcula fechas con vínculos y feriados, dibuja el Gantt y con un botón rehace el Word/PDF del formato (p. ej. FGAP080).
- `verificar-indice.sh`: revisa que todo archivo que no es `.md` tenga su `.md` en una carpeta con el mismo nombre. Uso: `herramientas/verificar-indice.sh`.
