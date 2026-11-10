# -*- coding: utf-8 -*-
"""Generador mínimo de .docx (WordprocessingML a mano, sin python-docx).

Marcado de texto admitido en cualquier cadena:
  **negrita**   //cursiva//   `código`   {PC}  -> «POR CONFIRMAR» resaltado en amarillo
  {PC:texto}    -> «texto» resaltado en amarillo (negrita)
Grupo D3 · NewBit · Ingeniería de Software II (UNS, 2026-II).
"""
import os
import re
import zipfile
from xml.sax.saxutils import escape

EMU_CM = 360000
TW_CM = 567  # twips por cm (aprox.)

TOKEN = re.compile(r"(\*\*.+?\*\*|//.+?//|`.+?`|\{PC(?::[^}]*)?\})")


def runs_from_markup(text, base):
    """Devuelve una lista de (texto, props) a partir del marcado."""
    out = []
    pos = 0
    for m in TOKEN.finditer(text):
        if m.start() > pos:
            out.append((text[pos:m.start()], dict(base)))
        tok = m.group(0)
        pr = dict(base)
        if tok.startswith("**"):
            pr["b"] = True
            inner = tok[2:-2]
            # permitir {PC} dentro de negrita
            for t, p2 in runs_from_markup(inner, pr):
                out.append((t, p2))
            pos = m.end()
            continue
        elif tok.startswith("//"):
            pr["i"] = True
            for t, p2 in runs_from_markup(tok[2:-2], pr):
                out.append((t, p2))
            pos = m.end()
            continue
        elif tok.startswith("`"):
            pr["code"] = True
            inner = tok[1:-1]
        else:  # {PC} o {PC:texto}
            pr["hl"] = True
            pr["b"] = True
            inner = tok[4:-1] if tok.startswith("{PC:") else "POR CONFIRMAR"
        out.append((inner, pr))
        pos = m.end()
    if pos < len(text):
        out.append((text[pos:], dict(base)))
    return out


def md_from_markup(text):
    """Convierte el marcado al Markdown de los .md del repo."""
    text = re.sub(r"\{PC:([^}]*)\}", r"**\1**", text)
    text = text.replace("{PC}", "**POR CONFIRMAR**")
    text = re.sub(r"//(.+?)//", r"*\1*", text)
    return text


def run_xml(t, pr, font, size):
    rpr = []
    f = "Courier New" if pr.get("code") else pr.get("font", font)
    rpr.append('<w:rFonts w:ascii="%s" w:hAnsi="%s" w:cs="%s" w:eastAsia="%s"/>' % (f, f, f, f))
    if pr.get("b"):
        rpr.append("<w:b/><w:bCs/>")
    if pr.get("i"):
        rpr.append("<w:i/><w:iCs/>")
    if pr.get("caps"):
        rpr.append("<w:caps/>")
    if pr.get("smallcaps"):
        rpr.append("<w:smallCaps/>")
    if pr.get("shadow"):
        rpr.append("<w:shadow/>")
    if pr.get("color"):
        rpr.append('<w:color w:val="%s"/>' % pr["color"])
    sz = pr.get("size", size)
    if pr.get("code"):
        sz = max(sz - 1, 12)
    rpr.append('<w:sz w:val="%d"/><w:szCs w:val="%d"/>' % (sz, sz))
    if pr.get("hl"):
        rpr.append('<w:highlight w:val="yellow"/>')
    rpr.append('<w:lang w:val="es-PE"/>')
    parts = []
    lines = t.split("\n")
    for k, line in enumerate(lines):
        if k:
            parts.append("<w:br/>")
        segs = line.split("\t")
        for j, seg in enumerate(segs):
            if j:
                parts.append("<w:tab/>")
            if seg:
                parts.append('<w:t xml:space="preserve">%s</w:t>' % escape(seg))
    return "<w:r><w:rPr>%s</w:rPr>%s</w:r>" % ("".join(rpr), "".join(parts))


class Doc:
    def __init__(self, landscape=False, margins_cm=(1.8, 1.6, 1.6, 1.6), font="Verdana",
                 size=17, header=None, footer=None, title="", subject=""):
        # size en medios puntos (17 = 8,5 pt)
        self.landscape = landscape
        self.margins = margins_cm  # top, right, bottom, left
        self.font = font
        self.size = size
        self.header = header  # lista de (texto marcado, alineación)
        self.footer = footer
        self.body = []
        self.media = []  # (nombre, ruta)
        self.title = title
        self.subject = subject

    # --- medidas -------------------------------------------------------
    @property
    def page_w_tw(self):
        return 16838 if self.landscape else 11906

    @property
    def page_h_tw(self):
        return 11906 if self.landscape else 16838

    @property
    def text_w_tw(self):
        return self.page_w_tw - int((self.margins[1] + self.margins[3]) * TW_CM)

    # --- bloques -------------------------------------------------------
    def para_xml(self, text, size=None, b=False, i=False, color=None, align=None, before=0,
                 after=60, shade=None, font=None, keep_next=False, caps=False, smallcaps=False,
                 line=None, indent_cm=None, hanging_cm=None, border_bottom=None, page_break_before=False,
                 tab_cm=None, prefix=None, shadow=False):
        base = {"size": size or self.size}
        if b:
            base["b"] = True
        if i:
            base["i"] = True
        if color:
            base["color"] = color
        if font:
            base["font"] = font
        if caps:
            base["caps"] = True
        if smallcaps:
            base["smallcaps"] = True
        if shadow:
            base["shadow"] = True
        ppr = []
        if keep_next:
            ppr.append("<w:keepNext/>")
        if page_break_before:
            ppr.append("<w:pageBreakBefore/>")
        if border_bottom:
            ppr.append('<w:pBdr><w:bottom w:val="single" w:sz="6" w:space="1" w:color="%s"/></w:pBdr>' % border_bottom)
        if shade:
            ppr.append('<w:shd w:val="clear" w:color="auto" w:fill="%s"/>' % shade)
        if tab_cm is not None:
            pos, kind = (tab_cm if isinstance(tab_cm, tuple) else (tab_cm, "left"))
            ppr.append('<w:tabs><w:tab w:val="%s" w:pos="%d"/></w:tabs>' % (kind, int(pos * TW_CM)))
        sp = '<w:spacing w:before="%d" w:after="%d"' % (before, after)
        if line:
            sp += ' w:line="%d" w:lineRule="auto"' % line
        ppr.append(sp + "/>")
        if indent_cm is not None or hanging_cm is not None:
            ind = '<w:ind w:left="%d"' % int((indent_cm or 0) * TW_CM)
            if hanging_cm:
                ind += ' w:hanging="%d"' % int(hanging_cm * TW_CM)
            ppr.append(ind + "/>")
        if align:
            ppr.append('<w:jc w:val="%s"/>' % align)
        runs = "".join(run_xml(t, p, self.font, self.size) for t, p in runs_from_markup(text, base))
        if prefix:
            runs = run_xml(prefix, {"size": base["size"]}, self.font, self.size) + runs
        return "<w:p><w:pPr>%s</w:pPr>%s</w:p>" % ("".join(ppr), runs)

    def p(self, text, **kw):
        self.body.append(self.para_xml(text, **kw))

    def bullet(self, text, level=0, **kw):
        kw.setdefault("after", 30)
        ind = 0.45 + 0.45 * level
        self.body.append(self.para_xml(text, indent_cm=ind, hanging_cm=0.3, tab_cm=ind, prefix="•\t", **kw))

    def page_break(self):
        self.body.append('<w:p><w:r><w:br w:type="page"/></w:r></w:p>')

    def spacer(self, pts=4):
        self.body.append('<w:p><w:pPr><w:spacing w:before="0" w:after="0" w:line="%d" w:lineRule="exact"/></w:pPr></w:p>' % (pts * 20))

    def image(self, path, width_cm, align="center", after=60):
        from PIL import Image
        im = Image.open(path)
        w, h = im.size
        cx = int(width_cm * EMU_CM)
        cy = int(cx * h / w)
        idx = len(self.media) + 1
        name = "image%d%s" % (idx, os.path.splitext(path)[1])
        self.media.append((name, path))
        rid = "rIdImg%d" % idx
        xml = (
            '<w:p><w:pPr><w:spacing w:before="0" w:after="%d"/><w:jc w:val="%s"/></w:pPr><w:r><w:drawing>'
            '<wp:inline distT="0" distB="0" distL="0" distR="0"><wp:extent cx="%d" cy="%d"/>'
            '<wp:docPr id="%d" name="Imagen %d"/><wp:cNvGraphicFramePr><a:graphicFrameLocks noChangeAspect="1"/></wp:cNvGraphicFramePr>'
            '<a:graphic><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
            '<pic:pic><pic:nvPicPr><pic:cNvPr id="%d" name="%s"/><pic:cNvPicPr/></pic:nvPicPr>'
            '<pic:blipFill><a:blip r:embed="%s"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
            '<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="%d" cy="%d"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr>'
            '</pic:pic></a:graphicData></a:graphic></wp:inline></w:drawing></w:r></w:p>'
        ) % (after, align, cx, cy, 100 + idx, idx, 100 + idx, name, rid, cx, cy)
        self.body.append(xml)

    def table(self, rows, widths_cm=None, widths_rel=None, border="808080", sz=4, font_size=None,
              cell_margin=60, header_rows=0, align="center", fixed=True, keep_rows=False, inner_h=None):
        """rows: lista de filas; cada celda es str o dict con claves:
        text (marcado) | paras (lista de str), fill, b, i, color, align, span, vmerge ('restart'|'cont'),
        size, valign, smallcaps."""
        total = self.text_w_tw
        if widths_cm:
            widths = [int(w * TW_CM) for w in widths_cm]
        else:
            rel = widths_rel or [1] * max(len(r) for r in rows)
            s = float(sum(rel))
            widths = [int(total * r / s) for r in rel]
        fs = font_size or self.size
        out = ['<w:tbl><w:tblPr><w:tblW w:w="%d" w:type="dxa"/><w:jc w:val="%s"/>' % (sum(widths), align)]
        out.append('<w:tblBorders>' + "".join(
            '<w:%s w:val="single" w:sz="%d" w:space="0" w:color="%s"/>' % (
                e, sz if not (e == "insideH" and inner_h) else 4, inner_h if (e == "insideH" and inner_h) else border)
            for e in ("top", "left", "bottom", "right", "insideH", "insideV")) + '</w:tblBorders>')
        if fixed:
            out.append('<w:tblLayout w:type="fixed"/>')
        out.append('<w:tblCellMar><w:top w:w="%d" w:type="dxa"/><w:left w:w="%d" w:type="dxa"/>'
                   '<w:bottom w:w="%d" w:type="dxa"/><w:right w:w="%d" w:type="dxa"/></w:tblCellMar>' % (
                       cell_margin // 2, cell_margin, cell_margin // 2, cell_margin))
        out.append('</w:tblPr><w:tblGrid>' + "".join('<w:gridCol w:w="%d"/>' % w for w in widths) + '</w:tblGrid>')
        for ri, row in enumerate(rows):
            trpr = ""
            if ri < header_rows:
                trpr += "<w:tblHeader/>"
            if keep_rows:
                trpr += "<w:cantSplit/>"
            out.append("<w:tr>%s" % ("<w:trPr>%s</w:trPr>" % trpr if trpr else ""))
            ci = 0
            for cell in row:
                if isinstance(cell, str):
                    cell = {"text": cell}
                span = cell.get("span", 1)
                w = sum(widths[ci:ci + span])
                tcpr = ['<w:tcW w:w="%d" w:type="dxa"/>' % w]
                if span > 1:
                    tcpr.append('<w:gridSpan w:val="%d"/>' % span)
                if cell.get("vmerge") == "restart":
                    tcpr.append('<w:vMerge w:val="restart"/>')
                elif cell.get("vmerge") == "cont":
                    tcpr.append('<w:vMerge/>')
                if cell.get("top_border"):
                    tcpr.append('<w:tcBorders><w:top w:val="single" w:sz="6" w:space="0" w:color="%s"/></w:tcBorders>' % cell["top_border"])
                if cell.get("noborder"):
                    tcpr.append('<w:tcBorders>' + "".join('<w:%s w:val="nil"/>' % e for e in ("top", "left", "bottom", "right")) + '</w:tcBorders>')
                if cell.get("fill"):
                    tcpr.append('<w:shd w:val="clear" w:color="auto" w:fill="%s"/>' % cell["fill"])
                tcpr.append('<w:vAlign w:val="%s"/>' % cell.get("valign", "center"))
                paras = cell.get("paras") or [cell.get("text", "")]
                pxml = []
                for k, ptxt in enumerate(paras):
                    bullet = False
                    if isinstance(ptxt, str) and ptxt.startswith("• "):
                        bullet = True
                        ptxt = ptxt[2:]
                    x = self.para_xml(ptxt, size=cell.get("size", fs), b=cell.get("b", False),
                                      i=cell.get("i", False), color=cell.get("color"),
                                      align=cell.get("align"), before=0,
                                      after=cell.get("after", 20 if k < len(paras) - 1 else 0),
                                      smallcaps=cell.get("smallcaps", False), font=cell.get("font"),
                                      keep_next=cell.get("keep_next", False),
                                      indent_cm=0.3 if bullet else None, hanging_cm=0.3 if bullet else None,
                                      tab_cm=0.3 if bullet else None, prefix="•\t" if bullet else None)
                    pxml.append(x)
                out.append("<w:tc><w:tcPr>%s</w:tcPr>%s</w:tc>" % ("".join(tcpr), "".join(pxml)))
                ci += span
            out.append("</w:tr>")
        out.append("</w:tbl>")
        self.body.append("".join(out))
        # párrafo mínimo tras la tabla
        self.body.append('<w:p><w:pPr><w:spacing w:before="0" w:after="0" w:line="120" w:lineRule="exact"/></w:pPr></w:p>')

    # --- ensamblado ----------------------------------------------------
    def _hf_xml(self, tag, items):
        ns = ('xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
              'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"')
        paras = []
        for it in items or []:
            text, kw = it[0], (it[1] if len(it) > 1 else {})
            x = self.para_xml(text, **kw)
            if "{PAGE}" in x:
                fld = ('</w:t></w:r><w:r><w:fldChar w:fldCharType="begin"/></w:r><w:r><w:instrText xml:space="preserve"> PAGE </w:instrText></w:r>'
                       '<w:r><w:fldChar w:fldCharType="separate"/></w:r><w:r><w:t>1</w:t></w:r><w:r><w:fldChar w:fldCharType="end"/></w:r><w:r><w:t xml:space="preserve">')
                x = x.replace("{PAGE}", fld)
            paras.append(x)
        return '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:%s %s>%s</w:%s>' % (tag, ns, "".join(paras) or "<w:p/>", tag)

    def save(self, path):
        W = self.page_w_tw
        H = self.page_h_tw
        t, r, b, l = [int(m * TW_CM) for m in self.margins]
        sect = ('<w:sectPr><w:headerReference w:type="default" r:id="rIdH1"/><w:footerReference w:type="default" r:id="rIdF1"/>'
                '<w:pgSz w:w="%d" w:h="%d"%s/><w:pgMar w:top="%d" w:right="%d" w:bottom="%d" w:left="%d" w:header="425" w:footer="425" w:gutter="0"/>'
                '<w:cols w:space="708"/></w:sectPr>') % (W, H, ' w:orient="landscape"' if self.landscape else "", t, r, b, l)
        doc = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
               '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
               'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
               'xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" '
               'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
               'xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">'
               '<w:body>%s%s</w:body></w:document>') % ("".join(self.body), sect)
        styles = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                  '<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
                  '<w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="{f}" w:hAnsi="{f}" w:cs="{f}" w:eastAsia="{f}"/>'
                  '<w:sz w:val="{s}"/><w:szCs w:val="{s}"/><w:lang w:val="es-PE"/></w:rPr></w:rPrDefault>'
                  '<w:pPrDefault><w:pPr><w:spacing w:after="60" w:line="252" w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults>'
                  '<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:qFormat/></w:style>'
                  '<w:style w:type="table" w:default="1" w:styleId="TableNormal"><w:name w:val="Normal Table"/>'
                  '<w:tblPr><w:tblInd w:w="0" w:type="dxa"/><w:tblCellMar><w:top w:w="0" w:type="dxa"/><w:left w:w="108" w:type="dxa"/>'
                  '<w:bottom w:w="0" w:type="dxa"/><w:right w:w="108" w:type="dxa"/></w:tblCellMar></w:tblPr></w:style>'
                  '</w:styles>').replace("{f}", self.font).replace("{s}", str(self.size))
        settings = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                    '<w:settings xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
                    '<w:zoom w:percent="100"/><w:defaultTabStop w:val="708"/><w:characterSpacingControl w:val="doNotCompress"/>'
                    '<w:compat><w:compatSetting w:name="compatibilityMode" w:uri="http://schemas.microsoft.com/office/word" w:val="15"/></w:compat>'
                    '</w:settings>')
        rels = ['<Relationship Id="rIdS" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>',
                '<Relationship Id="rIdSet" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/settings" Target="settings.xml"/>',
                '<Relationship Id="rIdH1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/header" Target="header1.xml"/>',
                '<Relationship Id="rIdF1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/>']
        for k, (name, _) in enumerate(self.media, 1):
            rels.append('<Relationship Id="rIdImg%d" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/%s"/>' % (k, name))
        drels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                 '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">%s</Relationships>' % "".join(rels))
        ct = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
              '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
              '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
              '<Default Extension="xml" ContentType="application/xml"/>'
              '<Default Extension="png" ContentType="image/png"/>'
              '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
              '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
              '<Override PartName="/word/settings.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml"/>'
              '<Override PartName="/word/header1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml"/>'
              '<Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>'
              '<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>'
              '<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>'
              '</Types>')
        rootrels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                    '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
                    '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>'
                    '<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>'
                    '</Relationships>')
        core = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
                'xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" '
                'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
                '<dc:title>%s</dc:title><dc:subject>%s</dc:subject><dc:creator>Grupo D3 (NewBit) - UNS</dc:creator>'
                '<cp:lastModifiedBy>Grupo D3</cp:lastModifiedBy>'
                '<dcterms:created xsi:type="dcterms:W3CDTF">2026-11-02T09:00:00Z</dcterms:created>'
                '<dcterms:modified xsi:type="dcterms:W3CDTF">2026-11-02T09:00:00Z</dcterms:modified>'
                '</cp:coreProperties>') % (escape(self.title), escape(self.subject))
        app = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
               '<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties">'
               '<Application>Microsoft Office Word</Application></Properties>')
        with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
            z.writestr("[Content_Types].xml", ct)
            z.writestr("_rels/.rels", rootrels)
            z.writestr("docProps/core.xml", core)
            z.writestr("docProps/app.xml", app)
            z.writestr("word/document.xml", doc)
            z.writestr("word/styles.xml", styles)
            z.writestr("word/settings.xml", settings)
            z.writestr("word/_rels/document.xml.rels", drels)
            z.writestr("word/header1.xml", self._hf_xml("hdr", self.header))
            z.writestr("word/footer1.xml", self._hf_xml("ftr", self.footer))
            for name, src in self.media:
                z.write(src, "word/media/" + name)
