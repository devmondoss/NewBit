// Genera PPT_Producto_Unidad_1_NewBit.pptx: presentación del Producto de la Unidad I de NewBit.
// Uso: node generar_ppt.js [carpeta_con_node_modules]   (requiere pptxgenjs@3.12.0)
// Coordenadas en pulgadas sobre 10 × 5.625 (16:9). Mismo contenido y cifras que el informe
// Producto_Unidad_1_NewBit.pdf; las páginas citadas son de la Guía SBOK (SCRUMstudy, 2022).
const path = require("path");
const modDir = process.argv[2];
const pptxgen = require(modDir ? path.join(modDir, "node_modules", "pptxgenjs") : "pptxgenjs");

const OUT = path.join(__dirname, "PPT_Producto_Unidad_1_NewBit.pptx");
const IMG = (f) => path.join(__dirname, "img", f);
const FONT = "Calibri";
const C = {
  ink: "1F2937", muted: "6B7280", line: "E5E7EB", soft: "F3F4F6", white: "FFFFFF",
  blue: "1D4ED8", blueSoft: "DBEAFE", green: "047857", greenSoft: "D1FAE5",
  amber: "B45309", amberSoft: "FEF3C7",
};

const pptx = new pptxgen();
pptx.layout = "LAYOUT_16x9";
pptx.author = "Grupo D3 · Ingeniería de Software II · UNS";
pptx.title = "NewBit · Producto de la Unidad I";

// ---------- primitivas ----------
let nro = 0;
function nueva(titulo, notas) {
  const s = pptx.addSlide();
  nro += 1;
  s.background = { color: C.white };
  if (titulo) {
    s.addText(titulo, { x: 0.5, y: 0.28, w: 9, h: 0.55, fontFace: FONT, fontSize: 24, bold: true, color: C.ink, margin: 0 });
    s.addShape(pptx.ShapeType.rect, { x: 0.5, y: 0.88, w: 0.55, h: 0.05, fill: { color: C.blue }, line: { color: C.blue } });
    s.addText("NewBit · Producto de la Unidad I · Grupo D3", { x: 0.5, y: 5.25, w: 6, h: 0.25, fontFace: FONT, fontSize: 9, color: C.muted, margin: 0 });
    s.addText(String(nro), { x: 8.9, y: 5.25, w: 0.6, h: 0.25, fontFace: FONT, fontSize: 9, color: C.muted, align: "right", margin: 0 });
  }
  if (notas) s.addNotes(notas);
  return s;
}
const T = (s, txt, x, y, w, h, o = {}) =>
  s.addText(txt, { x, y, w, h, fontFace: FONT, fontSize: 13, color: C.ink, valign: "top", margin: 0, ...o });
function caja(s, x, y, w, h, color, fondo, o = {}) {
  s.addShape(pptx.ShapeType.roundRect, { x, y, w, h, rectRadius: 0.06, fill: { color: fondo }, line: { color, width: 1 }, ...o });
}
function flecha(s, x1, y1, x2, y2) {
  s.addShape(pptx.ShapeType.line, { x: Math.min(x1, x2), y: Math.min(y1, y2), w: Math.abs(x2 - x1), h: Math.abs(y2 - y1),
    flipH: x2 < x1, flipV: y2 < y1, line: { color: C.muted, width: 1.25, endArrowType: "triangle" } });
}
// Cada viñeta es un texto o una lista de fragmentos (ver rico); cada una es un párrafo.
function vinetas(s, items, x, y, w, h, size = 14, gap = 6) {
  const runs = [];
  items.forEach((it, i) => {
    const partes = typeof it === "string" ? [{ text: it, options: {} }] : it;
    partes.forEach((p, k) => runs.push({ text: p.text, options: {
      color: C.ink, ...p.options,
      ...(k === 0 ? { bullet: { code: "25CF", indent: 14 }, paraSpaceAfter: gap } : {}),
      ...(k === partes.length - 1 && i < items.length - 1 ? { breakLine: true } : {}),
    } }));
  });
  s.addText(runs, { x, y, w, h, fontFace: FONT, fontSize: size, valign: "top", margin: 0 });
}
// Texto con partes en negrita: "**negrita** normal"
const rico = (str, base = {}) => str.split(/(\*\*[^*]+\*\*)/).filter(Boolean).map((p) =>
  p.startsWith("**") ? { text: p.slice(2, -2), options: { ...base, bold: true } } : { text: p, options: base });
// Tabla sobria: encabezado en negrita con línea inferior y filas separadas por líneas finas.
function tabla(s, filas, x, y, w, colW, size = 11, o = {}) {
  const sin = { type: "none" }, fina = { type: "solid", pt: 0.5, color: C.line }, gruesa = { type: "solid", pt: 1, color: C.ink };
  const rows = filas.map((f, i) => f.map((celda) => {
    const c = typeof celda === "string" ? { text: celda } : celda;
    return { text: c.text, options: {
      bold: i === 0 || c.bold, color: i === 0 ? C.ink : (c.color || C.ink), fill: c.fill ? { color: c.fill } : undefined,
      border: [i === 0 ? gruesa : sin, sin, i === 0 ? gruesa : (i === filas.length - 1 ? gruesa : fina), sin],
      align: c.align || "left", valign: "top", fontSize: size, fontFace: FONT, margin: [3, 5, 3, 5] } };
  }));
  s.addTable(rows, { x, y, w, colW, autoPage: false, ...o });
}
function imagen(s, archivo, x, y, w, h, pxW, pxH) {
  const r = Math.min(w / pxW, h / pxH), iw = pxW * r, ih = pxH * r;
  s.addImage({ path: IMG(archivo), x: x + (w - iw) / 2, y: y + (h - ih) / 2, w: iw, h: ih });
  s.addShape(pptx.ShapeType.rect, { x: x + (w - iw) / 2, y: y + (h - ih) / 2, w: iw, h: ih, fill: { type: "none" }, line: { color: C.line, width: 0.75 } });
}
const fuente = (s, txt) => T(s, txt, 0.5, 4.98, 9, 0.25, { fontSize: 9, color: C.muted });

// ---------- 1. Portada ----------
{
  const s = nueva(null, "Presentación del Producto de la Unidad I. Presenta: Albert (PO). Mencionar el código del proyecto y que todo el trabajo sigue la Guía SBOK.");
  s.addShape(pptx.ShapeType.rect, { x: 0, y: 0, w: 0.22, h: 5.625, fill: { color: C.blue }, line: { color: C.blue } });
  s.addImage({ path: IMG("logo-uns.png"), x: 0.6, y: 0.45, w: 0.92, h: 1.2 });
  T(s, [{ text: "UNIVERSIDAD NACIONAL DEL SANTA", options: { bold: true, breakLine: true } },
    { text: "Facultad de Ingeniería · Escuela Profesional de Ingeniería de Sistemas e Informática", options: { breakLine: true } },
    { text: "Ingeniería de Software II · Producto de la Unidad I" }],
    1.7, 0.62, 7.8, 0.9, { fontSize: 12, color: C.muted });
  T(s, "NewBit", 0.6, 1.85, 8.8, 0.85, { fontSize: 46, bold: true });
  T(s, "Sistema web con visión artificial para la detección de actos inseguros en áreas operativas de manufactura metalmecánica",
    0.6, 2.7, 8.6, 0.75, { fontSize: 17 });
  T(s, "Código del proyecto: PY-NB-001", 0.6, 3.45, 6, 0.3, { fontSize: 12, color: C.muted });
  T(s, [{ text: "Grupo D3", options: { bold: true, breakLine: true } },
    { text: "Albert Chumacero Chávarry · ", options: {} }, { text: "Product Owner", options: { italic: true, breakLine: true } },
    { text: "Anthony Lopez Yrribarren · ", options: {} }, { text: "Scrum Master y Developer", options: { italic: true, breakLine: true } },
    { text: "Luis Salazar Diaz · ", options: {} }, { text: "Developer", options: { italic: true } }],
    0.6, 3.95, 5.2, 1.2, { fontSize: 12 });
  T(s, [{ text: "Docente", options: { bold: true, breakLine: true } },
    { text: "Dr. Ing. Alfredo Daza Vergaray", options: { breakLine: true } },
    { text: "Nuevo Chimbote, octubre de 2026", options: { color: C.muted } }],
    6.0, 3.95, 3.6, 1.0, { fontSize: 12 });
}

// ---------- 2. Problema ----------
{
  const s = nueva("El problema: el acto inseguro se detecta tarde",
    "Contexto: muchos accidentes nacen de una conducta, no de una falla del equipo. La supervisión es intermitente y el video no se revisa. Cerrar con la pregunta que guía el proyecto.");
  vinetas(s, [
    rico("En un taller metalmecánico, muchos accidentes nacen de una **conducta**: cruzar fuera de la vía peatonal o dejar abierto un tablero (Heinrich, 1931)."),
    rico("La supervisión de SST es **intermitente**: el inspector recorre la planta por turnos."),
    rico("Las cámaras graban horas de video que **casi nadie revisa**."),
    rico("La Ley N.º 29783 exige un enfoque **preventivo** (Congreso de la República del Perú, 2011)."),
  ], 0.5, 1.25, 5.3, 3.6, 14, 10);
  caja(s, 6.15, 1.35, 3.35, 2.4, C.line, C.soft);
  T(s, "PREGUNTA QUE GUÍA EL PROYECTO", 6.35, 1.55, 3.0, 0.3, { fontSize: 9, color: C.muted, bold: true });
  T(s, "¿Cómo convertir el video que ya se graba en evidencia oportuna de actos inseguros, sin vigilar a las personas?",
    6.35, 1.9, 3.0, 1.7, { fontSize: 15, bold: true });
}

// ---------- 3. Propuesta ----------
{
  const s = nueva("La propuesta: NewBit",
    "Explicar el flujo en cuatro pasos. El sistema no reemplaza a la persona de SST: le entrega evidencia para que decida.");
  const pasos = [
    ["Video grabado", "clips .mp4 / .avi por lotes", C.muted, C.soft],
    ["YOLOv8", "detecta operarios y descarta fotogramas sin actividad", C.blue, C.blueSoft],
    ["ConvLSTM", "clasifica la secuencia como conducta segura o insegura", C.amber, C.amberSoft],
    ["Alerta con evidencia", "la persona de SST confirma o descarta", C.green, C.greenSoft],
  ];
  pasos.forEach(([t, d, col, fondo], i) => {
    const x = 0.5 + i * 2.32;
    caja(s, x, 1.3, 1.95, 1.45, col, fondo);
    T(s, t, x + 0.1, 1.42, 1.75, 0.35, { fontSize: 14, bold: true, align: "center" });
    T(s, d, x + 0.1, 1.82, 1.75, 0.85, { fontSize: 11, color: C.muted, align: "center" });
    if (i < 3) flecha(s, x + 1.97, 2.02, x + 2.3, 2.02);
  });
  [["Dos conductas", "Tránsito fuera de la vía peatonal y tablero eléctrico abierto."],
   ["Base científica", "Unsafe-Net (Önal y Dandıl, 2025) y su conjunto de datos público, CC BY 4.0."],
   ["Privacidad por diseño", "Sin reconocimiento facial ni identificación de personas."]].forEach(([t, d], i) => {
    const x = 0.5 + i * 3.05;
    T(s, t, x, 3.25, 2.85, 0.3, { fontSize: 14, bold: true, color: C.blue });
    T(s, d, x, 3.6, 2.85, 0.9, { fontSize: 12 });
  });
}

// ---------- 4. Evolución ----------
{
  const s = nueva("Cómo evolucionó la propuesta",
    "Principio de control empírico aplicado antes del primer sprint: inspeccionar y adaptar. Cada versión resolvió un problema concreto de la anterior.");
  const v = [
    ["SEMANAS 2–3", "VIGIA Industrial", "Casco, chaleco e ingreso a zonas en 4 cámaras en vivo.", "Problema", "detectaba objetos, no conductas, y dependía de un piloto en planta sin garantizar.", C.muted, C.soft, C.amber],
    ["SEMANA 4 · 05/10", "Elección de Unsafe-Net", "Se comparan tres investigaciones y se elige la que reconoce conductas en el tiempo.", "Ganancia", "conjunto de datos público: desaparece el mayor riesgo.", C.blue, C.blueSoft, C.green],
    ["SEMANA 5", "NewBit normalizado", "Taller metalmecánico, video por lotes, YOLOv8 + ConvLSTM, 12 historias con criterios y roles de planta.", "Resultado", "formatos coherentes entre sí.", C.green, C.greenSoft, C.green],
  ];
  v.forEach(([sem, t, d, et, r, col, fondo, colEt], i) => {
    const x = 0.5 + i * 3.08;
    caja(s, x, 1.25, 2.8, 2.75, col, fondo);
    T(s, sem, x + 0.15, 1.38, 2.5, 0.25, { fontSize: 9, color: C.muted, bold: true });
    T(s, t, x + 0.15, 1.62, 2.5, 0.35, { fontSize: 15, bold: true });
    T(s, d, x + 0.15, 2.0, 2.5, 0.95, { fontSize: 11 });
    T(s, [{ text: et + ": ", options: { bold: true, color: colEt } }, { text: r }], x + 0.15, 2.95, 2.5, 0.95, { fontSize: 11 });
    if (i < 2) flecha(s, x + 2.82, 2.62, x + 3.06, 2.62);
  });
  T(s, rico("Se conservó en las tres versiones: **sin reconocimiento facial**, **decisión final humana** y **evaluar el evento completo**, no el fotograma."),
    0.5, 4.3, 9, 0.6, { fontSize: 13 });
}

// ---------- 5. Antecedentes ----------
{
  const s = nueva("Antecedentes: de objetos en imágenes a conductas en video",
    "Los nacionales detectan objetos (sobre todo EPP) en imágenes. Unsafe-Net reconoce conductas en video: ahí se ubica NewBit. Las cifras no son comparables entre sí.");
  tabla(s, [
    ["Autor (año)", "Técnica", "Unidad", "Resultado reportado"],
    ["Önal y Dandıl (2021), Turquía", "YOLOv4, detección de EPP", "Imagen", "mAP 91.18 %"],
    [{ text: "Önal y Dandıl (2025), Turquía", bold: true }, { text: "YOLOv4 + ConvLSTM, conductas inseguras", bold: true }, { text: "Video", bold: true }, { text: "Exactitud por clase 95.81 %", bold: true }],
    ["Gutiérrez Torres (2022), PUCP", "VGG-16, ResNet-18, Inception-V3", "Imagen", "Exactitud 84 %"],
    ["Machaca Arcana (2019), UNSA", "Redes convolucionales, eventos anómalos", "Video", "—"],
    ["Paucara y Rodríguez (2024), UCV", "Aprendizaje profundo, detección de casco", "Imagen", "Mejor que el método convencional"],
    ["León y León (2024), UPN", "YOLOv8, mascarilla y gorro", "Imagen", "Validación 96.57 %"],
  ], 0.5, 1.2, 9, [2.75, 3.0, 0.9, 2.35], 11);
  fuente(s, "Cada cifra corresponde al conjunto de datos de su autor; no son comparables entre sí. Referencias completas en el informe (APA 7).");
}

// ---------- 6. Scrum: principios y aspectos ----------
{
  const s = nueva("Scrum según la Guía SBOK: principios y aspectos",
    "La guía organiza Scrum en principios, aspectos y procesos (p. 9). Los principios no se negocian; aspectos y procesos se adaptan. Cada aspecto tiene un formato en NewBit.");
  T(s, "Seis principios (obligatorios)", 0.5, 1.15, 4.4, 0.3, { fontSize: 14, bold: true, color: C.blue });
  const pr = [["Control del proceso empírico", "22"], ["Autoorganización", "27"], ["Colaboración", "29"],
    ["Priorización basada en valor", "33"], ["Time-boxing", "35"], ["Desarrollo iterativo", "38"]];
  pr.forEach(([p, pag], i) => {
    const y = 1.55 + i * 0.52;
    caja(s, 0.5, y, 4.4, 0.42, C.blue, C.blueSoft);
    T(s, `${i + 1}. ${p}`, 0.65, y + 0.08, 3.5, 0.3, { fontSize: 13 });
    T(s, `p. ${pag}`, 4.15, y + 0.1, 0.65, 0.3, { fontSize: 10, color: C.muted, align: "right" });
  });
  T(s, "Cinco aspectos y su formato en NewBit", 5.3, 1.15, 4.2, 0.3, { fontSize: 14, bold: true, color: C.amber });
  tabla(s, [
    ["Aspecto (cap.)", "Formato que lo concreta"],
    ["Organización (3)", "FGAP020 · FGAP030"],
    ["Justificación del negocio (4)", "EGAP015"],
    ["Calidad (5)", "FGAP070 · definición de listo"],
    ["Cambio (6)", "Control de versiones de cada formato"],
    ["Riesgo (7)", "Riesgos del acta (FGAP010)"],
  ], 5.3, 1.55, 4.2, [2.0, 2.2], 12);
  fuente(s, "Fuente: SCRUMstudy (2022), pp. 9 y 21–134.");
}

// ---------- 7. Roles y procesos ----------
{
  const s = nueva("Roles y procesos de Scrum",
    "Tres roles principales sin jerarquía entre ellos (p. 42). La guía recomienda 6 a 10 miembros (p. 50); somos 3 y el SM también desarrolla, riesgo registrado en el acta. 19 procesos en 5 fases (p. 15).");
  const roles = [
    ["Product Owner", "Albert", "Maximiza el valor; voz del cliente; prioriza el backlog y acepta o rechaza historias."],
    ["Scrum Master", "Anthony", "Facilita, enseña Scrum y elimina impedimentos; es un par del equipo, no un jefe."],
    ["Equipo Scrum", "Anthony y Luis", "Entiende los requerimientos, estima las historias y crea los entregables."],
  ];
  roles.forEach(([r, q, d], i) => {
    const y = 1.2 + i * 1.12;
    caja(s, 0.5, y, 4.0, 1.0, C.blue, C.blueSoft);
    T(s, [{ text: r, options: { bold: true } }, { text: "  ·  " + q, options: { color: C.muted } }], 0.65, y + 0.1, 3.7, 0.3, { fontSize: 13 });
    T(s, d, 0.65, y + 0.42, 3.75, 0.55, { fontSize: 11 });
  });
  tabla(s, [
    ["Fase (cap.)", "Procesos", "En NewBit"],
    ["Inicio (8)", "1–6: visión, SM e interesados, equipo, épicas, backlog, liberación", "Unidad I"],
    ["Planificación y estimación (9)", "7–12: crear y estimar historias, comprometer, tareas, backlog del sprint", "7–8 en la Unidad I; 9–12 en cada sprint"],
    ["Implementación (10)", "13–15: entregables, Daily Standup, refinar backlog", "Durante cada sprint"],
    ["Revisión y retrospectiva (11)", "16–17: demostrar y validar, retrospectiva", "Al cierre de cada sprint"],
    ["Liberación (12)", "18–19: enviar entregables, retrospectiva de la liberación", "Cierre (FGAP090)"],
  ], 4.75, 1.2, 4.75, [1.35, 2.15, 1.25], 9.5);
  fuente(s, "Fuente: SCRUMstudy (2022), pp. 15, 42–44 y 50.");
}

// ---------- 8. Time-boxes ----------
{
  const s = nueva("Reuniones de Scrum y sus time-boxes",
    "Reglas de la guía (pp. 35–37) aplicadas a sprints de dos semanas. Daily: tres preguntas.");
  tabla(s, [
    ["Reunión", "Regla de la Guía SBOK", "En NewBit", "Para qué"],
    ["Sprint", "1 a 4 semanas", { text: "2 semanas", bold: true }, "Iteración que produce un incremento revisable"],
    ["Planificación del sprint", "2 h por semana de sprint", { text: "4 h", bold: true }, "Comprometer historias, identificar y estimar tareas"],
    ["Daily Standup", "15 min al día", { text: "15 min", bold: true }, "¿Qué hice?, ¿qué haré?, ¿qué impedimentos tengo?"],
    ["Revisión del sprint", "1 h por semana de sprint", { text: "2 h", bold: true }, "Demostrar el incremento; el PO acepta o rechaza"],
    ["Retrospectiva del sprint", "1 h por semana de sprint", { text: "2 h", bold: true }, "Acordar mejoras accionables"],
  ], 0.5, 1.25, 9, [2.1, 2.2, 1.2, 3.5], 13);
  fuente(s, "Fuente: SCRUMstudy (2022), pp. 35–37.");
}

// ---------- 9. Entregables ↔ procesos ----------
{
  const s = nueva("Entregables de la Unidad I y su proceso en la Guía SBOK",
    "Cada formato del curso es la salida de un proceso de la guía. Al contrastarlos aparecieron tres salidas obligatorias sin formato: FGAP020, definición de listo y planificación de la liberación; se completaron en la semana 6.");
  tabla(s, [
    ["Sem.", "Entregable", "Proceso SBOK (pág.)", "Salida obligatoria que aporta"],
    ["2", "Cuadro de principios · FGAP010 Acta", "Cap. 2 (21–40) · 8.1 (139–144)", "PO identificado; declaración de la visión"],
    ["3", "FGAP030 Roles y prototipos", "8.3 (151–156) · 8.4 (158–164)", "Equipo Scrum identificado; personajes"],
    ["3", "Infografía, diagrama y presentación", "Apoyo a 8.1 (141–144)", "Visión comunicada a los interesados"],
    ["4", "EGAP015 Justificación", "Cap. 4 (67–86) · entrada de 8.1", "Caso de negocio del proyecto"],
    ["4", "FGAP040 Épicas e historias", "8.4 · 9.1 (185–189)", "Historias y criterios de aceptación"],
    ["5", "FGAP060 · Puño de cinco · Kanban", "8.5 (166–172) · 9.2 · 9.3", "Backlog priorizado; estimaciones; Scrumboard"],
    ["5", "FGAP070 Criterios de terminado", "8.5 (172) · 5.4.3 (92)", "Criterios de terminado"],
    [{ text: "6", color: C.amber }, { text: "FGAP020 · Definición de listo", color: C.amber }, { text: "8.2 (145–150) · 8.5 (92)", color: C.amber }, { text: "Interesados identificados; definición de listo", color: C.amber }],
    [{ text: "6", color: C.amber }, { text: "Planificación de la liberación", color: C.amber }, { text: "8.6 (173–178)", color: C.amber }, { text: "Cronograma de liberación; duración del sprint", color: C.amber }],
  ], 0.5, 1.15, 9, [0.5, 2.85, 2.45, 3.2], 10);
  fuente(s, "En ámbar, lo elaborado en la semana 6 para completar la fase de inicio. Fuente: SCRUMstudy (2022).");
}

// ---------- 10. Semana 2 ----------
{
  const s = nueva("Semana 2 · Principios de Scrum y acta de constitución",
    "Cuadro comparativo: cada principio con un ejemplo de NewBit. Acta (proceso 8.1): alcance, fuera de alcance, presupuesto y cronograma.");
  imagen(s, "cuadro-principios.png", 0.5, 1.2, 4.6, 2.6, 2112, 1188);
  T(s, "Cuadro comparativo de los principios (extracto)", 0.5, 3.85, 4.6, 0.3, { fontSize: 10, color: C.muted, align: "center" });
  T(s, "FGAP010 · Acta (proceso 8.1)", 5.4, 1.2, 4.1, 0.3, { fontSize: 14, bold: true, color: C.blue });
  vinetas(s, [
    rico("**Alcance:** dos conductas y sus casos seguros; conjunto de datos público con su división oficial."),
    rico("**Fuera del alcance:** planta, cámaras en vivo, reconocimiento facial y certificación de SST."),
    rico("**Presupuesto:** S/ 20 768 (S/ 18 600 de dedicación valorizada, S/ 280 en efectivo y 10 % de contingencia)."),
    rico("**Cronograma:** 05/10 al 18/12/2026, cuatro sprints de dos semanas."),
    rico("**Siete riesgos** con respuesta; el mayor, ajustar el modelo temporal."),
  ], 5.4, 1.6, 4.1, 3.3, 12, 6);
}

// ---------- 11. Semana 3: roles ----------
{
  const s = nueva("Semana 3 · Roles y prototipos (FGAP030)",
    "Los personajes son la salida obligatoria del proceso 8.4 (p. 164). Cada necesidad se convierte en una historia: HU10 responde a Lucía; HU09, a Mariana.");
  tabla(s, [
    ["Rol (persona)", "Uso", "Qué necesita de NewBit"],
    ["Administrador de la plataforma (Jorge Ponce, TI)", "Diario, al ingresar lotes", "Cargar videos y calibrar umbrales sin tocar código"],
    ["Supervisora de SST (Mariana Torres)", "Diario y ante cada alerta", "Alertas con clip de evidencia para confirmar o descartar"],
    ["Supervisor de turno (César Vásquez)", "Diario, en su turno", "Saber qué pasó, dónde y cuándo, sin alertas repetidas"],
    ["Operadora de monitoreo (Lucía Ramos)", "Permanente en su turno", "Ver solo lo importante y confirmar en un clic"],
    ["Gerente general y sponsor (Ricardo Salcedo)", "Semanal", "Reportes por tipo, zona y semana para decidir recursos"],
  ], 0.5, 1.2, 9, [3.3, 1.9, 3.8], 12);
  fuente(s, "Perfiles ficticios de un caso académico. Fuente del concepto de personajes: SCRUMstudy (2022), p. 164.");
}

// ---------- 12. Semana 3: visión ----------
{
  const s = nueva("Semana 3 · Infografía y diagrama de arquitectura",
    "Piezas para la reunión de la visión del proyecto (8.1). Se muestran como se entregaron: aún decían YOLOv4; en la semana 5 pasó a YOLOv8.");
  imagen(s, "infografia-pasos-1-6.png", 0.5, 1.15, 4.4, 3.7, 1680, 1440);
  imagen(s, "diagrama-arquitectura.png", 5.1, 1.15, 4.4, 3.7, 1224, 982);
  T(s, "Infografía «Pasos para desarrollar NewBit» (pasos 1 a 6)", 0.5, 4.88, 4.4, 0.25, { fontSize: 9, color: C.muted, align: "center" });
  T(s, "Diagrama de arquitectura: flujo principal en siete etapas", 5.1, 4.88, 4.4, 0.25, { fontSize: 9, color: C.muted, align: "center" });
}

// ---------- 13. Semana 4 ----------
{
  const s = nueva("Semana 4 · Justificación y épicas",
    "La justificación es el caso de negocio, entrada obligatoria de 8.1 (p. 141). Épicas (8.4) e historias (9.1) siguen el recorrido del dato.");
  T(s, "EGAP015 · Justificación", 0.5, 1.15, 3.6, 0.3, { fontSize: 14, bold: true, color: C.blue });
  vinetas(s, [
    rico("**Necesidad:** inspecciones intermitentes y cámaras que no alertan."),
    rico("**Tecnológica:** YOLOv8 + ConvLSTM con software abierto."),
    rico("**Operativa:** apoya al supervisor, no lo reemplaza."),
    rico("**Económica:** S/ 20 768, igual al acta."),
    rico("No se prometen ahorros ni reducción de accidentes sin evidencia."),
  ], 0.5, 1.55, 3.6, 3.3, 12, 5);
  T(s, "FGAP040 · Seis épicas, doce historias", 4.4, 1.15, 5.1, 0.3, { fontSize: 14, bold: true, color: C.blue });
  const ep = [
    ["EP01", "Ingestión y preprocesamiento", "HU01–HU02", C.blue, C.blueSoft],
    ["EP02", "Detección de operarios (YOLOv8)", "HU03", C.blue, C.blueSoft],
    ["EP03", "Segmentación y reducción", "HU04–HU06", C.blue, C.blueSoft],
    ["EP04", "Clasificación con ConvLSTM", "HU07–HU08", C.amber, C.amberSoft],
    ["EP05", "Monitoreo y alertas", "HU09–HU10", C.amber, C.amberSoft],
    ["EP06", "Calibración y trazabilidad", "HU11–HU12", C.muted, C.soft],
  ];
  ep.forEach(([id, t, h, col, fondo], i) => {
    const x = 4.4 + (i % 2) * 2.6, y = 1.55 + Math.floor(i / 2) * 1.08;
    caja(s, x, y, 2.45, 0.95, col, fondo);
    T(s, [{ text: id + " ", options: { bold: true } }, { text: t }], x + 0.1, y + 0.08, 2.25, 0.55, { fontSize: 11.5 });
    T(s, h, x + 0.1, y + 0.62, 2.25, 0.25, { fontSize: 10, color: C.muted });
  });
}

// ---------- 14. Semana 5: backlog ----------
{
  const s = nueva("Semana 5 · Backlog priorizado (FGAP060)",
    "Proceso 8.5: un único documento ordenado por valor, riesgo y dependencias. Tres pasos: MoSCoW, 100 puntos por integrante y dependencias. HU11 y HU06 se adelantan al Sprint 2.");
  const filas = [["HU", "Historia", "MoSCoW", "100 pts", "Sprint (pts)"],
    ["HU01", "Cargar video", "Must", "19", "1 (1)"], ["HU02", "Extraer fotogramas", "Must", "20", "1 (2)"],
    ["HU03", "Detectar operarios", "Must", "37", "1 (4)"], ["HU04", "Descartar fotogramas vacíos", "Must", "28", "2 (2)"],
    ["HU05", "Agrupar en clips", "Must", "25", "2 (3)"], ["HU06", "Descartar clips cortos", "Should", "12", "2 (2)"],
    ["HU11", "Calibrar umbral", "Could", "8", "2 (1)"], ["HU07", "Procesar con ConvLSTM", "Must", "47", "3 (5)"],
    ["HU08", "Clasificar y tipificar", "Must", "38", "3 (3)"], ["HU09", "Ver video con recuadro", "Must", "30", "4 (4)"],
    ["HU10", "Alerta de riesgo", "Should", "21", "4 (2)"], ["HU12", "Ver log de tiempos", "Should", "15", "4 (2)"]]
    .map((f, i) => i === 0 ? f : f.map((c, j) => (j >= 2 ? { text: c, align: "center" } : c)));
  tabla(s, filas, 0.5, 1.1, 5.6, [0.7, 2.4, 0.85, 0.75, 0.9], 9.5);
  T(s, "Tres criterios, en orden", 6.4, 1.15, 3.1, 0.3, { fontSize: 14, bold: true, color: C.blue });
  vinetas(s, [
    rico("**MoSCoW:** 8 Must, 3 Should, 1 Could."),
    rico("**100 puntos** por integrante (300 en total)."),
    rico("**Dependencias** del pipeline."),
  ], 6.4, 1.55, 3.1, 1.3, 12, 5);
  T(s, rico("HU11 y HU06 se adelantan al Sprint 2: calibran y filtran antes de entrenar el modelo temporal.\n**31 puntos:** 7 · 8 · 8 · 8 por sprint."),
    6.4, 2.95, 3.1, 1.6, { fontSize: 12 });
}

// ---------- 15. Semana 5: estimación, Kanban y DoD ----------
{
  const s = nueva("Semana 5 · Estimación, Scrumboard y criterios de terminado",
    "Estimación (9.2) con el puño de cinco: 1 = muy pequeña, 5 = muy grande. Scrumboard (9.3) del Sprint 1: tareas propuestas. DoD (8.5): obligatoria para toda historia.");
  imagen(s, "scrumboard-sprint1.png", 0.5, 1.15, 5.2, 2.95, 1584, 891);
  T(s, "Scrumboard propuesto para el Sprint 1 (tablero Kanban)", 0.5, 4.12, 5.2, 0.25, { fontSize: 9, color: C.muted, align: "center" });
  T(s, "Puño de cinco (9.2)", 6.0, 1.15, 3.5, 0.3, { fontSize: 14, bold: true, color: C.blue });
  T(s, "Tamaño relativo de 1 a 5 dedos; los extremos explican y se vuelve a votar. Total: 31 puntos; la EP04 es la más grande.",
    6.0, 1.5, 3.5, 1.0, { fontSize: 11.5 });
  T(s, "Criterios de terminado (FGAP070)", 6.0, 2.6, 3.5, 0.3, { fontSize: 14, bold: true, color: C.blue });
  vinetas(s, ["Pruebas unitarias e integradas", "Revisión de pares entre Developers", "Documentación de datos, pesos y métricas",
    "Aprobación técnica y del PO", "Ética: CC BY 4.0, sin biometría"], 6.0, 2.95, 3.5, 2.0, 11, 3);
}

// ---------- 16. Semana 6 ----------
{
  const s = nueva("Semana 6 · Registro de interesados y definición de listo",
    "FGAP020 (proceso 8.2): no había formato del docente; se elaboró desde el acta y FGAP030. Definición de listo (8.5, p. 92): propuesta que se validará en la planificación del Sprint 1.");
  const X0 = 0.75, Y0 = 1.25, W = 4.4, H = 3.4;
  s.addShape(pptx.ShapeType.rect, { x: X0 + W / 2, y: Y0, w: W / 2, h: H / 2, fill: { color: C.blueSoft }, line: { color: C.blueSoft } });
  s.addShape(pptx.ShapeType.rect, { x: X0, y: Y0 + H / 2, w: W / 2, h: H / 2, fill: { color: C.soft }, line: { color: C.soft } });
  s.addShape(pptx.ShapeType.rect, { x: X0, y: Y0, w: W, h: H, fill: { type: "none" }, line: { color: C.muted, width: 0.75 } });
  s.addShape(pptx.ShapeType.line, { x: X0 + W / 2, y: Y0, w: 0, h: H, line: { color: C.muted, width: 0.5, dashType: "dash" } });
  s.addShape(pptx.ShapeType.line, { x: X0, y: Y0 + H / 2, w: W, h: 0, line: { color: C.muted, width: 0.5, dashType: "dash" } });
  [["MANTENER SATISFECHO", X0 + 0.08, Y0 + 0.06, "left"], ["GESTIONAR DE CERCA", X0 + W / 2, Y0 + 0.06, "right"],
   ["MONITOREAR", X0 + 0.08, Y0 + H - 0.28, "left"], ["MANTENER INFORMADO", X0 + W / 2, Y0 + H - 0.28, "right"]].forEach(([t, x, y, al]) =>
    T(s, t, x, y, W / 2 - 0.12, 0.22, { fontSize: 8, bold: true, color: C.muted, align: al }));
  const pts = [[3.9, 5.6, "Sponsor"], [9.0, 6.2, "Docente"], [8.6, 5.5, "Product Owner"], [8.8, 4.8, "Scrum Master y Developer"],
    [7.6, 4.0, "SST y TI"], [8.8, 2.6, "Operadora de monitoreo"], [8.2, 1.8, "Supervisor de turno"], [3.9, 1.6, "Trabajadores"]];
  pts.forEach(([ix, iy, t]) => {
    const x = X0 + (ix / 10) * W, y = Y0 + H - (iy / 7) * H;
    s.addShape(pptx.ShapeType.ellipse, { x: x - 0.05, y: y - 0.05, w: 0.1, h: 0.1, fill: { color: C.blue }, line: { color: C.blue } });
    T(s, t, x - 2.05, y - 0.11, 1.95, 0.22, { fontSize: 9, align: "right" });
  });
  T(s, "Interés →", X0, Y0 + H + 0.05, W, 0.25, { fontSize: 10, color: C.muted, align: "center" });
  T(s, "Poder ↑", X0 - 0.62, Y0 + H / 2 - 0.12, 0.6, 0.25, { fontSize: 10, color: C.muted });
  T(s, "Definición de listo (propuesta)", 5.6, 1.2, 3.9, 0.3, { fontSize: 14, bold: true, color: C.amber });
  T(s, "Una historia entra a un sprint cuando…", 5.6, 1.55, 3.9, 0.3, { fontSize: 11, color: C.muted });
  vinetas(s, ["Tiene rol, funcionalidad y beneficio, y el PO la explicó.", "Tiene criterios de aceptación verificables.",
    "Sus dependencias están resueltas o planificadas.", "Está estimada y cabe en un sprint de dos semanas.",
    "Se conocen los datos que necesita (clips y etiquetas)."], 5.6, 1.9, 3.9, 3.0, 12, 6);
}

// ---------- 17. Arquitectura ----------
{
  const s = nueva("Arquitectura propuesta",
    "Actualiza el diagrama de la semana 3 con YOLOv8n y el sprint de cada etapa. Separar etapas permite evaluarlas por su cuenta y medir cuánto aporta la reducción de fotogramas, como exige el acta.");
  const arriba = [["Carga y validación", "RF-01 · Sprint 1"], ["Fotogramas normalizados", "Sprint 1"],
    ["Detección de operarios (YOLOv8n)", "RF-02 · Sprint 1"], ["Reducción y clips", "RF-03, RF-04 · Sprint 2"]];
  const abajo = [["Confirmación por SST", "decisión humana", C.muted, C.soft], ["Alerta visual y sonora", "RF-07 · Sprint 4", C.amber, C.amberSoft],
    ["Registro de la detección", "RF-06 · Sprint 3", C.amber, C.amberSoft], ["Clasificación de la conducta (ConvLSTM)", "RF-05 · Sprint 3", C.amber, C.amberSoft]];
  const bw = 1.9, gap = 0.37, x0 = 0.75;
  T(s, "Etapa espacial", x0, 1.12, 4 * bw + 3 * gap, 0.25, { fontSize: 11, bold: true, color: C.blue, align: "center" });
  arriba.forEach(([t, d], i) => {
    const x = x0 + i * (bw + gap);
    caja(s, x, 1.42, bw, 1.15, C.blue, C.blueSoft);
    T(s, t, x + 0.08, 1.52, bw - 0.16, 0.6, { fontSize: 12, bold: true, align: "center" });
    T(s, d, x + 0.08, 2.15, bw - 0.16, 0.3, { fontSize: 9.5, color: C.muted, align: "center" });
    if (i < 3) flecha(s, x + bw + 0.02, 2.0, x + bw + gap - 0.02, 2.0);
  });
  const xr = x0 + 3 * (bw + gap) + bw / 2;
  flecha(s, xr, 2.59, xr, 3.08);
  abajo.forEach(([t, d, col, fondo], i) => {
    const x = x0 + i * (bw + gap);
    caja(s, x, 3.1, bw, 1.15, col, fondo);
    T(s, t, x + 0.08, 3.2, bw - 0.16, 0.6, { fontSize: 12, bold: true, align: "center" });
    T(s, d, x + 0.08, 3.83, bw - 0.16, 0.3, { fontSize: 9.5, color: C.muted, align: "center" });
    if (i > 0) flecha(s, x - 0.02, 3.68, x - gap + 0.02, 3.68);
  });
  T(s, "Etapa temporal y salida", x0, 4.32, 4 * bw + 3 * gap, 0.25, { fontSize: 11, bold: true, color: C.amber, align: "center" });
  fuente(s, "Adapta Unsafe-Net (Önal y Dandıl, 2025), con YOLOv8n en lugar de YOLOv4.");
}

// ---------- 18. Plan de sprints ----------
{
  const s = nueva("Planificación de la liberación y de los sprints",
    "Proceso 8.6 (p. 178): duración del sprint de dos semanas y una liberación guiada por fecha, 14–18/12. El Sprint 3 concentra el mayor riesgo técnico; las metas se fijan con su línea base.");
  const dia = 0.085, x0 = 2.6, y0 = 1.35;
  [[0, "05 oct"], [14, "19 oct"], [28, "02 nov"], [42, "16 nov"], [56, "30 nov"], [70, "14 dic"]].forEach(([d, t]) => {
    s.addShape(pptx.ShapeType.line, { x: x0 + d * dia, y: y0, w: 0, h: 2.05, line: { color: C.line, width: 0.75 } });
    T(s, t, x0 + d * dia - 0.4, y0 - 0.25, 0.8, 0.22, { fontSize: 9, color: C.muted, align: "center" });
  });
  [["Inicio", "FGAP010 a FGAP070", 0, 11, C.muted, C.soft], ["Sprint 1", "EP01, EP02 · 7 pts", 14, 25, C.blue, C.blueSoft],
   ["Sprint 2", "EP03 y HU11 · 8 pts", 28, 39, C.blue, C.blueSoft], ["Sprint 3", "EP04 · 8 pts", 42, 53, C.amber, C.amberSoft],
   ["Sprint 4", "EP05 y HU12 · 8 pts", 56, 67, C.amber, C.amberSoft], ["Cierre", "FGAP090", 70, 74, C.muted, C.soft]].forEach(([n, d, a, b, col, fondo], i) => {
    const y = y0 + 0.08 + i * 0.32;
    s.addShape(pptx.ShapeType.roundRect, { x: x0 + a * dia, y, w: (b - a) * dia, h: 0.22, rectRadius: 0.03, fill: { color: fondo }, line: { color: col, width: 1 } });
    T(s, [{ text: n + "  ", options: { bold: true } }, { text: d, options: { color: C.muted } }], 0.4, y + 0.01, 2.1, 0.22, { fontSize: 9.5, align: "right" });
  });
  s.addShape(pptx.ShapeType.line, { x: x0 + 14 * dia, y: y0 - 0.02, w: 0, h: 2.1, line: { color: C.ink, width: 1.5 } });
  T(s, "Hoy, 19/10: inicio del Sprint 1", x0 + 14 * dia - 1.0, y0 + 2.08, 2.0, 0.22, { fontSize: 9, bold: true, align: "center" });
  const ciclo = [["Planificación", "4 h · backlog del sprint, tareas, Scrumboard"], ["Daily Standup", "15 min · impedimentos"],
    ["Revisión", "2 h · el PO acepta o rechaza"], ["Retrospectiva", "2 h · mejoras accionables"]];
  ciclo.forEach(([t, d], i) => {
    const x = 0.5 + i * 2.28;
    caja(s, x, 3.9, 2.08, 0.95, C.green, C.greenSoft);
    T(s, t, x + 0.1, 3.98, 1.9, 0.3, { fontSize: 13, bold: true });
    T(s, d, x + 0.1, 4.3, 1.9, 0.5, { fontSize: 10.5, color: C.muted });
    if (i < 3) flecha(s, x + 2.1, 4.37, x + 2.26, 4.37);
  });
  T(s, "Ciclo de cada sprint", 0.5, 3.6, 4, 0.28, { fontSize: 12, bold: true, color: C.green });
}

// ---------- 19. Síntesis ----------
{
  const s = nueva("Síntesis",
    "Cierre: qué deja la Unidad I y qué viene. Abrir preguntas.");
  T(s, "Lo que deja la Unidad I", 0.5, 1.2, 4.3, 0.3, { fontSize: 15, bold: true, color: C.green });
  vinetas(s, ["Un problema y una propuesta claros, con base científica y datos públicos.",
    "Los entregables de las semanas 2 a 5, vinculados a sus procesos de la Guía SBOK.",
    "Las salidas obligatorias que faltaban: FGAP020, definición de listo y planificación de la liberación.",
    "Un backlog de 12 historias priorizado, estimado y repartido en cuatro sprints."], 0.5, 1.6, 4.3, 2.8, 13, 8);
  T(s, "Lo que viene", 5.2, 1.2, 4.3, 0.3, { fontSize: 15, bold: true, color: C.amber });
  vinetas(s, ["Sprints 1 y 2: etapa espacial.", "Sprint 3: modelo temporal y evaluación comparativa.",
    "Sprint 4: interfaz, alerta y log de tiempos.", "Cierre con FGAP090: 14 al 18 de diciembre."], 5.2, 1.6, 4.3, 2.8, 13, 8);
  T(s, "Gracias. ¿Preguntas?", 0.5, 4.35, 9, 0.5, { fontSize: 22, bold: true, align: "center" });
}

pptx.writeFile({ fileName: OUT }).then((f) => console.log("Escrito:", f));
