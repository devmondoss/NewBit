# -*- coding: utf-8 -*-
"""Dibuja el árbol de la EDT del Sprint 02 (PNG) a partir de plan_sprint02.py.
Uso: python3 dibujar_edt.py <salida.png>
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import plan_sprint02 as P  # noqa: E402

FD = "/System/Library/Fonts/Supplemental/"
S = 3  # factor de escala (px por unidad)


def font(bold, size):
    return ImageFont.truetype(FD + ("Verdana Bold.ttf" if bold else "Verdana.ttf"), int(size * S))


COL = {"HU": ("1F3864", "Historia de usuario"), "SC": ("B45309", "Solicitud de cambio"), "R": ("9B2335", "Riesgo")}


def hexrgb(h):
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def wrap(draw, text, f, maxw):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=f) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def box(draw, x, y, w, h, fill, outline, shadow=True, width=1):
    if shadow:
        draw.rectangle([x + 3 * S, y + 3 * S, x + w + 3 * S, y + h + 3 * S], fill=(190, 190, 190))
    draw.rectangle([x, y, x + w, y + h], fill=fill, outline=outline, width=width * S)


def main(out):
    n = len(P.NODOS)
    colw = 118  # unidades
    gap = 8
    W = (colw * n + gap * (n - 1) + 24)
    H = 420
    img = Image.new("RGB", (W * S, H * S), "white")
    d = ImageDraw.Draw(img)
    negro = (30, 30, 30)
    # raíz
    rw, rh = 420, 42
    rx, ry = (W - rw) / 2, 8
    box(d, rx * S, ry * S, rw * S, rh * S, hexrgb("2D3748"), negro)
    f1 = font(True, 13)
    f2 = font(False, 9.5)
    t1 = "PY-NB-001 · NewBit · Sprint Nro. %s" % P.SPRINT
    t2 = "02–13/11/2026 · 43 h estimadas · Developers: Luis Salazar y Anthony Lopez"
    d.text(((W / 2) * S, (ry + 15) * S), t1, font=f1, fill="white", anchor="mm")
    d.text(((W / 2) * S, (ry + 31) * S), t2, font=f2, fill=(230, 230, 230), anchor="mm")
    # bus
    bus_y = ry + rh + 12
    d.line([(W / 2) * S, (ry + rh) * S, (W / 2) * S, bus_y * S], fill=negro, width=S)
    x0 = 12
    centers = [x0 + i * (colw + gap) + colw / 2 for i in range(n)]
    d.line([centers[0] * S, bus_y * S, centers[-1] * S, bus_y * S], fill=negro, width=S)
    ny = bus_y + 10
    fT = font(True, 10.5)
    fS = font(False, 8.5)
    fTask = font(False, 8.6)
    fTaskB = font(True, 8.6)
    fCab = font(False, 7.6)
    # alto común de los nodos de nivel 2 según el título más largo
    titulos = [wrap(d, "%s · %s" % (nd["id"], nd["titulo"]), fT, (colw - 10) * S) for nd in P.NODOS]
    maxl = max(len(t) for t in titulos)
    nh = 12 + 13 * maxl + 24
    max_y = 0
    for i, nodo in enumerate(P.NODOS):
        cx = centers[i]
        x = cx - colw / 2
        d.line([cx * S, bus_y * S, cx * S, ny * S], fill=negro, width=S)
        color, etiqueta = COL[nodo["tipo"]]
        box(d, x * S, ny * S, colw * S, nh * S, hexrgb(color), negro)
        d.text((cx * S, (ny + 8) * S), etiqueta, font=fCab, fill=(255, 235, 200) if nodo["tipo"] != "HU" else (200, 215, 240), anchor="mm")
        yy = ny + 20
        for ln in titulos[i]:
            d.text((cx * S, yy * S), ln, font=fT, fill="white", anchor="mm")
            yy += 13
        pie = (("%d pt · " if nodo["pts"] == 1 else "%d pts · ") % nodo["pts"] if nodo["pts"] else "") + "%d h" % P.horas_nodo(nodo["id"])
        d.text((cx * S, (ny + nh - 8) * S), pie, font=fS, fill=(235, 235, 235), anchor="mm")
        # tareas
        tareas = P.tareas_de(nodo["id"])
        ty = ny + nh + 10
        lx = x + 7
        last_mid = None
        for t in tareas:
            tx = x + 16
            tw = colw - 18
            txt = "%s %s" % (t[0], t[2])
            tl = wrap(d, txt, fTask, (tw - 8) * S)
            th = 10 + 11.2 * len(tl) + 11
            box(d, tx * S, ty * S, tw * S, th * S, (255, 255, 255), negro)
            yy = ty + 9
            for k, ln in enumerate(tl):
                if k == 0:
                    idt = t[0]
                    d.text(((tx + 4) * S, yy * S), idt, font=fTaskB, fill=negro, anchor="lm")
                    off = d.textlength(idt + " ", font=fTaskB) / S
                    d.text(((tx + 4 + off) * S, yy * S), ln[len(idt) + 1:], font=fTask, fill=negro, anchor="lm")
                else:
                    d.text(((tx + 4) * S, yy * S), ln, font=fTask, fill=negro, anchor="lm")
                yy += 11.2
            quien = "Luis" if t[4] == P.L else ("Anthony" if t[4] == P.A else "Luis y Anthony")
            d.text(((tx + 4) * S, (ty + th - 7.5) * S), "%d h · %s" % (t[5], quien), font=font(False, 7.4), fill=(90, 90, 90), anchor="lm")
            mid = ty + th / 2
            d.line([lx * S, mid * S, tx * S, mid * S], fill=negro, width=S)
            last_mid = mid
            ty += th + 8
        max_y = max(max_y, ty)
        if last_mid:
            d.line([lx * S, (ny + nh) * S, lx * S, last_mid * S], fill=negro, width=S)
    H = max_y + 22
    # leyenda
    ly = H - 10
    lx = 12
    for tipo in ("HU", "SC", "R"):
        color, etiqueta = COL[tipo]
        d.rectangle([lx * S, (ly - 4) * S, (lx + 10) * S, (ly + 4) * S], fill=hexrgb(color), outline=negro)
        d.text(((lx + 14) * S, ly * S), etiqueta, font=font(False, 8.2), fill=negro, anchor="lm")
        lx += 14 + d.textlength(etiqueta, font=font(False, 8.2)) / S + 16
    d.text((lx * S, ly * S), "Tareas T01–T14 numeradas en forma correlativa en todo el sprint · horas = estimación del equipo · "
           "SC-001 no aprobada por el PO (02/11): T06–T10 no se ejecutan", font=font(False, 8.2), fill=(70, 70, 70), anchor="lm")
    # recortar alto sobrante
    bbox = Image.eval(img.convert("L"), lambda v: 255 - v).getbbox()
    img = img.crop((0, 0, W * S, min(H * S, bbox[3] + 8 * S) if False else (H + 2) * S))
    img.save(out, dpi=(300, 300))
    print("ok", img.size)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "edt_sprint02.png")
