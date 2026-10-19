# Conversión de PDF a Markdown

Scripts con los que se convirtieron los libros y diapositivas del curso (19/10/2026). Solo usan lo que trae macOS (PDFKit y el OCR de Vision) y Python 3; no hay que instalar nada.

| Script | Para qué |
|---|---|
| `ocr.swift` | OCR de un rango de páginas: `swift ocr.swift <pdf> <desde> <hasta> <salida.md>`. Para PDF escaneados y diapositivas (~2 s por página). |
| `txt.swift` | Extrae la capa de texto de un PDF que ya tiene texto: `swift txt.swift <pdf> <salida.md>`. |
| `limpiar.py` | Limpia y da formato: `sbok` (parte la Guía del SBOK por capítulos), `libro` (libro con texto) o `diapos` (una sección por diapositiva). |

Ejemplo (SBOK completo): `swift ocr.swift ../../curso/referencias/libro-guia-sbok/libro-guia-sbok.pdf 1 413 /tmp/sbok.md` y luego `python3 limpiar.py sbok /tmp/sbok.md ../../curso/referencias/libro-guia-sbok/texto-completo`.
