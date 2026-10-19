"""Convierte la salida de OCR/texto (con marcadores <!-- pág. PDF N -->) en Markdown legible.

uso:
  limpiar.py sbok <ocr.md> <carpeta_salida>
  limpiar.py libro <txt.md> <salida.md> <título>
  limpiar.py diapos <ocr.md> <salida.md> <título>
"""
import re
import sys
from pathlib import Path

MARCA = re.compile(r'<!-- pág\. PDF (\d+) -->')


def paginas(texto):
    partes = MARCA.split(texto)
    return [(int(partes[i]), partes[i + 1].strip('\n').split('\n')) for i in range(1, len(partes), 2)]


def unir_parrafos(lineas):
    """Une líneas cortadas por el ancho de página; respeta viñetas, títulos y líneas vacías."""
    out = []
    for l in lineas:
        l = l.rstrip()
        if not l.strip():
            if out and out[-1] != '':
                out.append('')
            continue
        prev = out[-1] if out else ''
        es_bloque = l.lstrip().startswith(('#', '•', '\uf0b7', '-', '*', '|', '<!--')) or re.match(r'^\s*\d+[.)]\s', l)
        if prev and not prev.startswith(('#', '<!--', '|')) and not es_bloque:
            if prev.endswith('-') and not prev.endswith(' -') and l[:1].islower():
                out[-1] = prev[:-1] + l.lstrip()
                continue
            if not re.search(r'[.:;?!»”)]$', prev) or l[:1].islower():
                out[-1] = prev + ' ' + l.lstrip()
                continue
        out.append(l.replace('\uf0b7', '•'))
    return out


# ----------------------------------------------------------------------------- SBOK
CAPITULOS = [  # (archivo, título, pág. libro inicial)
    ('01-introduccion', 'Capítulo 1. Introducción', 1),
    ('02-principios', 'Capítulo 2. Principios', 21),
    ('03-organizacion', 'Capítulo 3. Organización', 41),
    ('04-justificacion-del-negocio', 'Capítulo 4. Justificación del negocio', 67),
    ('05-calidad', 'Capítulo 5. Calidad', 87),
    ('06-cambio', 'Capítulo 6. Cambio', 101),
    ('07-riesgo', 'Capítulo 7. Riesgo', 119),
    ('08-inicio', 'Capítulo 8. Inicio', 135),
    ('09-planificacion-y-estimacion', 'Capítulo 9. Planificación y estimación', 181),
    ('10-implementacion', 'Capítulo 10. Implementación', 217),
    ('11-revision-y-retrospectiva', 'Capítulo 11. Revisión y retrospectiva', 241),
    ('12-liberacion', 'Capítulo 12. Liberación', 257),
    ('13-escalamiento-grandes-proyectos', 'Capítulo 13. Escalamiento de Scrum para grandes proyectos', 271),
    ('14-escalamiento-para-la-empresa', 'Capítulo 14. Escalamiento de Scrum para la empresa', 295),
    ('15-apendices-y-referencias', 'Apéndices A, B y C y referencias', 333),
    ('16-glosario', 'Glosario', 355),
    ('17-indice-tematico', 'Índice temático', 392),
]
DESFASE = 17  # pág. PDF = pág. libro + 17


def limpiar_pagina_sbok(lineas, cap_num):
    res = []
    for l in lineas:
        s = l.strip()
        if 'SCRUMstudy' in s and ('©' in s or 'Guía de los fundamentos' in s):
            continue  # pie de página
        if re.fullmatch(r'\d{1,2}\s*[-–]\s*[A-ZÁÉÍÓÚÑ ,]+', s):
            continue  # encabezado de capítulo ("1- PRINCIPIOS")
        if re.fullmatch(r'[A-ZÁÉÍÓÚÑ ,]+\s*[-–]\s*\d{1,2}', s):
            continue
        if cap_num and s == str(cap_num):
            continue  # pestaña lateral con el número de capítulo
        if re.fullmatch(r'\d{1,3}', s) and not res:
            continue
        res.append(s)
    # Número de sección en su propia línea + título en la siguiente -> encabezado
    out, i = [], 0
    while i < len(res):
        s = res[i]
        m = re.fullmatch(r'(\d{1,2}(?:\.\d+){1,4})\.?', s)
        if m and i + 1 < len(res) and res[i + 1] and not re.match(r'^\d', res[i + 1]):
            nivel = min(2 + m.group(1).count('.'), 6)
            out += ['', '#' * nivel + f' {m.group(1)} {res[i + 1]}', '']
            i += 2
            continue
        m = re.fullmatch(r'(\d{1,2}(?:\.\d+){1,4})\s+(\D.{2,80})', s)
        if m and len(s) < 90 and not s.endswith('.'):
            nivel = min(2 + m.group(1).count('.'), 6)
            out += ['', '#' * nivel + f' {m.group(1)} {m.group(2)}', '']
            i += 1
            continue
        out.append(s)
        i += 1
    return out


def sbok(ocr, carpeta):
    pags = dict(paginas(Path(ocr).read_text(encoding='utf-8')))
    carpeta = Path(carpeta)
    carpeta.mkdir(parents=True, exist_ok=True)
    ultima = max(pags)
    tramos = [('00-preliminares', 'Preliminares: portada, créditos e índice general', 1 - DESFASE)] + CAPITULOS
    for k, (arch, titulo, inicio_libro) in enumerate(tramos):
        ini_pdf = inicio_libro + DESFASE
        fin_pdf = (tramos[k + 1][2] + DESFASE - 1) if k + 1 < len(tramos) else ultima
        cap_num = int(arch[:2]) if arch[:2].isdigit() and 1 <= int(arch[:2]) <= 14 else None
        cuerpo = []
        for p in range(ini_pdf, fin_pdf + 1):
            if p not in pags:
                continue
            libro = p - DESFASE
            cuerpo += ['', f'<!-- pág. libro {libro} · PDF {p} -->' if libro >= 1 else f'<!-- pág. PDF {p} -->']
            cuerpo += [l for l in limpiar_pagina_sbok(pags[p], cap_num) if l != str(libro)]
        cab = [f'# Guía del SBOK, 4.ª ed. · {titulo}', '',
               f'> Páginas del libro {max(inicio_libro, 1) if inicio_libro >= 1 else "—"}–{fin_pdf - DESFASE} (PDF {ini_pdf}–{fin_pdf}). '
               'Texto obtenido por OCR de la copia escaneada: puede tener errores menores; '
               'las figuras y tablas gráficas no se transcriben (solo su texto). '
               'Fuente: SCRUMstudy (2022). *Guía de los fundamentos de Scrum (Guía SBOK)*, 4.ª ed. VMEdu.', '']
        texto = '\n'.join(cab + unir_parrafos(cuerpo)).strip() + '\n'
        texto = re.sub(r'\n{3,}', '\n\n', texto)
        (carpeta / f'{arch}.md').write_text(texto, encoding='utf-8')
        print(f'{arch}.md  PDF {ini_pdf}-{fin_pdf}  {len(texto):,} car.')


# ----------------------------------------------------------------------------- otros
def libro(fuente, salida, titulo):
    out = [f'# {titulo}', '', '> Texto completo extraído del PDF (capa de texto). Las ilustraciones no se transcriben.', '']
    for p, lineas in paginas(Path(fuente).read_text(encoding='utf-8')):
        lineas = [l for l in lineas if not re.fullmatch(r'\s*\d{1,3}\s*', l)]  # número de página
        lineas = [l for l in lineas if not re.match(r'\s*2005-2018 – ScrumManager', l)]  # pie de página
        lineas = [re.sub(r'^\s*[\uf06e\uf0b7\uf0a7]\s*', '• ', l) for l in lineas]  # viñetas
        if lineas and lineas[0].strip() in ('Ingeniería de requisitos ágil', 'Formación Scrum Manager', 'ScrumManager: Información'):
            lineas = lineas[1:]  # encabezado repetido
        out += ['', f'<!-- pág. {p} -->'] + lineas
    texto = re.sub(r'\n{3,}', '\n\n', '\n'.join(unir_parrafos(out)).strip() + '\n')
    Path(salida).write_text(texto, encoding='utf-8')
    print(salida, f'{len(texto):,} car.')


def diapos(fuente, salida, titulo):
    out = [f'# {titulo}', '', '> Texto completo por OCR de cada diapositiva (incluye el texto dentro de imágenes y diagramas). '
           'El orden de lectura sigue la posición en la diapositiva; los diagramas pierden su forma.', '']
    for p, lineas in paginas(Path(fuente).read_text(encoding='utf-8')):
        lineas = [l.strip() for l in lineas if l.strip()]
        out += ['', f'## Diapositiva {p}', ''] + lineas
    texto = re.sub(r'\n{3,}', '\n\n', '\n'.join(out).strip() + '\n')
    Path(salida).write_text(texto, encoding='utf-8')
    print(salida, f'{len(texto):,} car.')


if __name__ == '__main__':
    modo = sys.argv[1]
    if modo == 'sbok':
        sbok(sys.argv[2], sys.argv[3])
    elif modo == 'libro':
        libro(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        diapos(sys.argv[2], sys.argv[3], sys.argv[4])
