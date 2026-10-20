"""Genera los íconos de línea de la presentación (SVG 24×24, trazo 1.6) y los convierte a PNG.

uso: python3 generar_iconos.py   (desde esta carpeta; usa herramientas/conversion-pdf/svg2png_lote.swift)
"""
import os, subprocess, tempfile

COLORES = {"ink": "#1A1A1A", "gris": "#8A8984", "azul": "#3E63DD", "ambar": "#C2410C", "verde": "#2F855A"}
ICONOS = {  # nombre: (trazos SVG, colores que usa la presentación)
    "alerta": ('<path d="M6 16v-5a6 6 0 0 1 12 0v5l1.5 2h-15z"/><path d="M10 20.5a2 2 0 0 0 4 0"/>', ['azul', 'ink']),
    "buscar": ('<circle cx="10.5" cy="10.5" r="6"/><path d="M15 15l5 5"/>', ['ink']),
    "calendario": ('<rect x="4" y="5" width="16" height="15" rx="2"/><path d="M4 10h16M9 3v4M15 3v4"/>', ['azul']),
    "capas": ('<path d="M12 4l8 4-8 4-8-4z"/><path d="M4 12l8 4 8-4M4 16l8 4 8-4"/>', ['ink']),
    "ciclo": ('<path d="M20 12a8 8 0 1 1-2.3-5.7"/><path d="M20 4v4h-4"/>', ['azul']),
    "dinero": ('<rect x="3" y="6" width="18" height="12" rx="2"/><circle cx="12" cy="12" r="2.5"/>', ['ink']),
    "equipo": ('<circle cx="9" cy="8" r="3"/><path d="M3.5 19c.9-3 3-4.5 5.5-4.5s4.6 1.5 5.5 4.5"/><circle cx="17" cy="9" r="2.5"/><path d="M16 14.6c2 .2 3.6 1.6 4.4 4.4"/>', ['azul']),
    "escudo": ('<path d="M12 3l7 3v5c0 4.5-3 8-7 10-4-2-7-5.5-7-10V6z"/><path d="M9 12l2 2 4-4"/>', ['azul']),
    "grafico": ('<path d="M4 20h16"/><path d="M7 16v-4M12 16V8M17 16v-7"/>', ['azul']),
    "libro": ('<path d="M5 4h9a3 3 0 0 1 3 3v13H8a3 3 0 0 1-3-3z"/><path d="M5 17a3 3 0 0 1 3-3h9"/>', ['ink']),
    "lista": ('<path d="M9 6h11M9 12h11M9 18h11"/><path d="M4.5 6h.01M4.5 12h.01M4.5 18h.01"/>', ['azul']),
    "mano": ('<path d="M8 13V6.5a1.5 1.5 0 0 1 3 0V11M11 10V5a1.5 1.5 0 0 1 3 0v6M14 10.5V7a1.5 1.5 0 0 1 3 0v6.5c0 4-2.5 7-6 7-2.5 0-4-1.5-5.5-4L4 14a1.5 1.5 0 0 1 2.4-1.8L8 14"/>', ['ink']),
    "no": ('<circle cx="12" cy="12" r="8.5"/><path d="M9 9l6 6M15 9l-6 6"/>', ['gris']),
    "objetivo": ('<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r="1"/>', ['ink']),
    "persona": ('<circle cx="12" cy="8" r="3.5"/><path d="M5 20c1.2-3.6 4-5.5 7-5.5s5.8 1.9 7 5.5"/>', ['ink']),
    "reloj": ('<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>', ['azul', 'ink', 'ambar']),
    "riesgo": ('<path d="M12 4l9 16H3z"/><path d="M12 10v4M12 17h.01"/>', ['ambar']),
    "secuencia": ('<rect x="3" y="7" width="12" height="10" rx="1.5"/><path d="M18 8.5v7M21 10v4"/>', ['ink']),
    "seguro": ('<circle cx="12" cy="12" r="8.5"/><path d="M8.5 12l2.5 2.5 4.5-5"/>', ['azul', 'verde']),
    "tablero": ('<rect x="5" y="3" width="14" height="18" rx="1.5"/><path d="M12.5 7l-3 5h4l-3 5"/>', ['ink']),
    "via": ('<path d="M7 21l3-18M17 21l-3-18"/><path d="M12 6v2M12 11v2M12 16v2"/>', ['ink']),
    "video": ('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M10 9.5v5l4.5-2.5z"/>', ['ink']),
}

aqui = os.path.dirname(os.path.abspath(__file__))
destino = os.path.join(aqui, "img", "iconos")
conversor = os.path.join(aqui, "..", "..", "..", "..", "herramientas", "conversion-pdf", "svg2png_lote.swift")
with tempfile.TemporaryDirectory() as tmp:
    for nombre, (trazos, colores) in ICONOS.items():
        for c in colores:
            with open(os.path.join(tmp, f"{nombre}-{c}.svg"), "w") as f:
                f.write(f'<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" '
                        f'stroke="{COLORES[c]}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{trazos}</svg>')
    os.makedirs(destino, exist_ok=True)
    subprocess.run(["swift", conversor, tmp, destino, "192"], check=True)
print("Íconos en", destino)
