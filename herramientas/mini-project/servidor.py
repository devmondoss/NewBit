# -*- coding: utf-8 -*-
"""Mini Project: editor de cronogramas al estilo de MS Project, en localhost.

Lee y escribe proyectos en formato MSPDI (el XML de MS Project), así que el mismo archivo
se abre luego en MS Project o ProjectLibre y se guarda como .mpp.

Uso:   python3 herramientas/mini-project/servidor.py            (abre el navegador)
       python3 herramientas/mini-project/servidor.py --puerto 8800 --sin-navegador
Solo usa la biblioteca estándar. Escucha solo en 127.0.0.1 y solo toca archivos .xml/.png
dentro del repo. Grupo D3 · NewBit · Ingeniería de Software II (UNS, 2026-II).
"""
import argparse
import json
import os
import socket
import subprocess
import sys
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(AQUI, "..", ".."))
IGNORAR = {".git", ".venv", "node_modules", "__pycache__", ".claude", "descartado"}
ESTATICOS = {"/": ("index.html", "text/html; charset=utf-8"),
             "/app.js": ("app.js", "text/javascript; charset=utf-8"),
             "/estilos.css": ("estilos.css", "text/css; charset=utf-8")}


def ruta_segura(rel, extensiones=(".xml",)):
    """Convierte una ruta relativa al repo en absoluta y comprueba que no se salga del repo."""
    if not rel:
        raise ValueError("Falta la ruta")
    p = os.path.abspath(os.path.join(REPO, rel))
    if os.path.commonpath([p, REPO]) != REPO:
        raise ValueError("La ruta sale del repositorio")
    if not p.lower().endswith(extensiones):
        raise ValueError("Solo se permiten archivos %s" % ", ".join(extensiones))
    return p


def es_mspdi(p):
    try:
        with open(p, "rb") as f:
            cabeza = f.read(600)
        return b"schemas.microsoft.com/project" in cabeza
    except OSError:
        return False


def listar_proyectos():
    out = []
    for raiz, dirs, archivos in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in IGNORAR and not d.startswith(".")]
        for a in archivos:
            if a.lower().endswith(".xml"):
                p = os.path.join(raiz, a)
                if es_mspdi(p):
                    out.append({"ruta": os.path.relpath(p, REPO), "modificado": os.path.getmtime(p)})
    out.sort(key=lambda x: -x["modificado"])
    return out


def python_del_repo():
    for c in (os.path.join(REPO, ".venv", "bin", "python"), os.path.join(REPO, ".venv", "Scripts", "python.exe")):
        if os.path.exists(c):
            return c
    return sys.executable


def generadores_de(xml_abs):
    """Scripts generar_*.py de la carpeta del XML que aceptan --xml (convención del repo)."""
    carpeta = os.path.dirname(xml_abs)
    out = []
    for a in sorted(os.listdir(carpeta)):
        if a.startswith("generar_") and a.endswith(".py"):
            with open(os.path.join(carpeta, a), encoding="utf-8") as f:
                if "--xml" in f.read():
                    out.append(os.path.join(carpeta, a))
    return out


class Manejador(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):  # silencio salvo errores
        if args and str(args[1]).startswith(("4", "5")):
            sys.stderr.write("%s\n" % (fmt % args))

    def _json(self, obj, codigo=200):
        datos = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(codigo)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(datos)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(datos)

    def _cuerpo(self):
        n = int(self.headers.get("Content-Length") or 0)
        if n > 20 * 1024 * 1024:
            raise ValueError("Archivo demasiado grande")
        return self.rfile.read(n)

    def _mismo_origen(self):
        # evita que otra página del navegador escriba en el repo (CSRF)
        origen = self.headers.get("Origin")
        return origen is None or urlparse(origen).hostname in ("127.0.0.1", "localhost")

    def do_GET(self):
        u = urlparse(self.path)
        try:
            if u.path in ESTATICOS:
                nombre, tipo = ESTATICOS[u.path]
                with open(os.path.join(AQUI, nombre), "rb") as f:
                    datos = f.read()
                self.send_response(200)
                self.send_header("Content-Type", tipo)
                self.send_header("Content-Length", str(len(datos)))
                self.send_header("Cache-Control", "no-store")
                self.end_headers()
                self.wfile.write(datos)
            elif u.path == "/api/proyectos":
                self._json({"repo": REPO, "proyectos": listar_proyectos()})
            elif u.path == "/api/abrir":
                rel = parse_qs(u.query).get("ruta", [""])[0]
                p = ruta_segura(rel)
                with open(p, encoding="utf-8") as f:
                    xml = f.read()
                self._json({"ruta": os.path.relpath(p, REPO), "xml": xml,
                            "generadores": [os.path.basename(g) for g in generadores_de(p)]})
            else:
                self.send_error(404)
        except (ValueError, OSError) as e:
            self._json({"error": str(e)}, 400)

    def do_POST(self):
        u = urlparse(self.path)
        if not self._mismo_origen():
            return self._json({"error": "Origen no permitido"}, 403)
        try:
            datos = json.loads(self._cuerpo().decode("utf-8"))
            if u.path == "/api/guardar":
                p = ruta_segura(datos.get("ruta"))
                if os.path.exists(p) and not datos.get("sobrescribir", True):
                    return self._json({"error": "Ya existe", "existe": True}, 409)
                os.makedirs(os.path.dirname(p), exist_ok=True)
                tmp = p + ".tmp"
                with open(tmp, "w", encoding="utf-8", newline="\n") as f:
                    f.write(datos["xml"])
                os.replace(tmp, p)
                self._json({"ok": True, "ruta": os.path.relpath(p, REPO),
                            "generadores": [os.path.basename(g) for g in generadores_de(p)]})
            elif u.path == "/api/generar":
                p = ruta_segura(datos.get("ruta"))
                gens = generadores_de(p)
                if not gens:
                    return self._json({"error": "No hay un generar_*.py con --xml en la carpeta de este proyecto"}, 400)
                args = [python_del_repo(), "-I", gens[0], "--xml", p]
                if datos.get("pdf"):
                    args.append("--pdf")
                r = subprocess.run(args, cwd=os.path.dirname(p), capture_output=True, text=True, timeout=300)
                self._json({"ok": r.returncode == 0, "script": os.path.basename(gens[0]),
                            "salida": (r.stdout + r.stderr)[-4000:]}, 200 if r.returncode == 0 else 500)
            else:
                self.send_error(404)
        except subprocess.TimeoutExpired:
            self._json({"error": "El generador tardó demasiado"}, 500)
        except (ValueError, OSError, KeyError, json.JSONDecodeError) as e:
            self._json({"error": str(e)}, 400)


def puerto_libre(preferido):
    for p in range(preferido, preferido + 30):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(("127.0.0.1", p)) != 0:
                return p
    raise SystemExit("No hay puertos libres entre %d y %d" % (preferido, preferido + 29))


def main():
    ap = argparse.ArgumentParser(description="Mini Project: editor de cronogramas MSPDI en localhost")
    ap.add_argument("--puerto", type=int, default=8780)
    ap.add_argument("--sin-navegador", action="store_true")
    ap.add_argument("--abrir", help="ruta (relativa al repo) del .xml a abrir al iniciar")
    a = ap.parse_args()
    puerto = puerto_libre(a.puerto)
    srv = ThreadingHTTPServer(("127.0.0.1", puerto), Manejador)
    url = "http://127.0.0.1:%d/" % puerto + (("#" + a.abrir) if a.abrir else "")
    print("Mini Project en %s  (Ctrl+C para salir)" % url)
    print("Repositorio: %s" % REPO)
    if not a.sin_navegador:
        threading.Timer(0.6, lambda: webbrowser.open(url)).start()
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nListo.")


if __name__ == "__main__":
    main()
