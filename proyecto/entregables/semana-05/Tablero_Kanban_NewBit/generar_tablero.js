// Genera Tablero_Kanban_NewBit.html y Tablero_Kanban_NewBit.pptx desde una sola definición.
// Uso: node generar_presentacion.js [carpeta_con_node_modules]   (requiere pptxgenjs@3.12.0)
// Coordenadas en pulgadas sobre 10 × 5.625 (16:9). En el HTML, 1 in = 128 px.
const path = require("path");
const fs = require("fs");
const modDir = process.argv[2];
const pptxgen = require(modDir ? path.join(modDir, "node_modules", "pptxgenjs") : "pptxgenjs");

const OUT = path.join(__dirname, "Tablero_Kanban_NewBit");
const FONT = "Calibri";
const C = {
  ink: "1F2421", muted: "6B7280", soft: "F4F4F2", line: "E5E5E2", white: "FFFFFF",
  accent: "F2643D", accentSoft: "FDEDE7",
  no: "E5484D", doubt: "F0A020", yes: "2F9E6E",
};
const VOTE = [null, C.no, C.no, C.doubt, C.yes, C.yes];

// ---------- primitivas ----------
const text = (x, y, w, h, runs, o = {}) => ({ t: "text", x, y, w, h, runs: typeof runs === "string" ? [{ text: runs }] : runs, ...o });
const box = (x, y, w, h, fill, o = {}) => ({ t: "rect", x, y, w, h, fill, ...o });
const circle = (x, y, d, fill) => ({ t: "rect", x, y, w: d, h: d, fill, r: d / 2 });

// Mano vista de frente: índice, medio, anular, meñique y pulgar se levantan en ese orden (n = 1..5).
function hand(x, y, W, n, color) {
  const H = W * 1.2, els = [];
  const palm = { x: x + 0.14 * W, y: y + 0.5 * H, w: 0.72 * W, h: 0.46 * H };
  const tall = [0.4, 0.44, 0.4, 0.32];
  for (let i = 0; i < 4; i++) {
    const fx = palm.x + i * 0.18 * W + 0.02 * W, fw = 0.14 * W, up = i < n;
    const fh = up ? tall[i] * H : 0.11 * H;
    const fy = palm.y + 0.06 * H - fh;
    els.push(box(fx, fy, fw, fh, color, { r: fw / 2, alpha: up ? 0 : 60 }));
  }
  const thumbUp = n >= 5;
  if (thumbUp) els.push(box(x + 0.02 * W, y + 0.42 * H, 0.15 * W, 0.34 * H, color, { r: 0.075 * W, rot: -32 }));
  els.push(box(palm.x, palm.y, palm.w, palm.h, color, { r: 0.16 * W }));
  return els;
}


// ---------- datos (FGAP040, versión del equipo) ----------
// Prioridad (MoSCoW + 100 puntos) y estimación (puño de cinco) votadas por el Grupo D3 el 12/10/2026.
const EP = {
  EP01: { name: "Ingestión de video", color: "5B6B7A" },
  EP02: { name: "Filtrado YOLOv4", color: "2F6DB5" },
  EP03: { name: "Segmentación temporal", color: "7A5AB8" },
  EP04: { name: "Clasificación ConvLSTM", color: "B4235A" },
  EP05: { name: "GUI y validación", color: "1F8A70" },
  EP06: { name: "Administración", color: "8A6D1E" },
};
const HU = [
  { id: "HU01", ep: "EP01", t: "Cargar video", rank: 1, mo: "Must", pts: 1, sp: 1,
    story: "Como investigador, quiero cargar un video industrial, para iniciar el análisis.",
    ac: ["Acepta .mp4 y .avi; otro formato muestra un mensaje de error.", "Muestra nombre, duración y resolución del video cargado."],
    tasks: ["Pantalla de carga", "Validar formato", "Ver datos del video"] },
  { id: "HU02", ep: "EP01", t: "Extraer frames", rank: 2, mo: "Must", pts: 2, sp: 1,
    story: "Como investigador, quiero fragmentar el video en frames, para la inferencia espacial.",
    ac: ["Guarda los frames numerados y en el orden del video.", "Los redimensiona al tamaño de entrada de YOLOv4."],
    tasks: ["Extraer frames", "Redimensionar frames", "Guardar en orden"] },
  { id: "HU03", ep: "EP02", t: "Detectar trabajadores", rank: 3, mo: "Must", pts: 4, sp: 1,
    story: "Como investigador, quiero que YOLOv4 detecte trabajadores, para ubicar la acción.",
    ac: ["Devuelve por frame las cajas de «persona» con su confianza.", "Un frame de prueba se ve con las cajas dibujadas."],
    tasks: ["Instalar YOLOv4", "Detectar personas", "Probar con 1 video"] },
  { id: "HU04", ep: "EP02", t: "Descartar frames vacíos", rank: 4, mo: "Must", pts: 2, sp: 2,
    story: "Como investigador, quiero descartar frames sin trabajadores, para no saturar el modelo.",
    ac: ["Los frames sin personas no pasan a la siguiente etapa.", "Registra cuántos frames entraron y cuántos se descartaron."] },
  { id: "HU05", ep: "EP03", t: "Agrupar en clips", rank: 5, mo: "Must", pts: 3, sp: 2,
    story: "Como investigador, quiero agrupar los frames en clips fijos, para la red temporal.",
    ac: ["Todos los clips tienen N frames consecutivos (N configurable).", "La salida tiene la forma de entrada que espera ConvLSTM."] },
  { id: "HU06", ep: "EP03", t: "Descartar clips cortos", rank: 11, mo: "Should", pts: 2, sp: 2,
    story: "Como investigador, quiero descartar clips sin tiempo mínimo, para evitar falsos.",
    ac: ["Los clips con menos frames que el mínimo se descartan.", "Registra cuántos clips se descartaron."] },
  { id: "HU07", ep: "EP04", t: "Procesar con ConvLSTM", rank: 6, mo: "Must", pts: 5, sp: 3,
    story: "Como investigador, quiero procesar el clip con ConvLSTM, para extraer el movimiento.",
    ac: ["Entrena con el split oficial y guarda pesos y métricas.", "Recibe un clip y devuelve una probabilidad por clase."] },
  { id: "HU08", ep: "EP04", t: "Etiquetar el clip", rank: 7, mo: "Must", pts: 3, sp: 3,
    story: "Como investigador, quiero la etiqueta seguro/inseguro, para obtener el resultado.",
    ac: ["Cada clip queda etiquetado con su probabilidad.", "Reporta accuracy, precision, recall y F1 del set de prueba."] },
  { id: "HU09", ep: "EP05", t: "Ver video con recuadro", rank: 8, mo: "Must", pts: 4, sp: 4,
    story: "Como evaluador, quiero ver el video con un recuadro de color, para validar la inferencia.",
    ac: ["El recuadro es verde (seguro) o rojo (inseguro) por tramo.", "Funciona con los videos del conjunto de prueba."] },
  { id: "HU10", ep: "EP05", t: "Alerta insegura", rank: 9, mo: "Should", pts: 2, sp: 4,
    story: "Como evaluador, quiero una alerta ante un riesgo, para probar la respuesta.",
    ac: ["Una conducta insegura dispara un aviso visual y sonoro.", "Cada alerta se guarda con hora, video y probabilidad."] },
  { id: "HU11", ep: "EP06", t: "Ajustar umbral", rank: 12, mo: "Could", pts: 1, sp: 2,
    story: "Como administrador, quiero cambiar el umbral de YOLOv4, para calibrar el filtrado.",
    ac: ["El umbral se cambia en la configuración, sin tocar código.", "Rechaza valores fuera de 0–1 y anota el cambio en el log."] },
  { id: "HU12", ep: "EP06", t: "Ver log de tiempos", rank: 10, mo: "Should", pts: 2, sp: 4,
    story: "Como administrador, quiero ver el log de tiempos, para saber si el filtrado acelera.",
    ac: ["Muestra el tiempo de cada etapa del procesamiento.", "Compara el mismo video con y sin filtrado."] },
];
const SPRINTS = [
  { n: 1, d: "19/10 – 01/11" }, { n: 2, d: "02/11 – 15/11" }, { n: 3, d: "16/11 – 29/11" }, { n: 4, d: "30/11 – 11/12" },
];
const MO = { Must: { bg: C.ink, fg: C.white }, Should: { bg: "9CA3AF", fg: C.white }, Could: { bg: C.line, fg: C.ink } };
const byRank = [...HU].sort((a, b) => a.rank - b.rank);
const ptsOf = n => HU.filter(h => h.sp === n).reduce((s, h) => s + h.pts, 0);
const TOTAL = HU.reduce((s, h) => s + h.pts, 0);

// ---------- piezas ----------
const pill = (x, y, w, h, label, bg, fg, size = 9) => [
  box(x, y, w, h, bg, { r: h / 2 }),
  text(x, y, w, h, label, { size, bold: true, color: fg, align: "center", valign: "middle" }),
];
const badges = (x, y, h) => [
  ...pill(x, y, 0.62, 0.22, h.mo.toUpperCase(), MO[h.mo].bg, MO[h.mo].fg, 8),
  ...pill(x + 0.68, y, 0.44, 0.22, `${h.pts} pt`, C.accent, C.white, 9),
];
const dot = (x, y, color) => circle(x, y, 0.14, color);

// Tarjeta completa: historia + criterios de aceptación.
function storyCard(x, y, h) {
  const W = 2.8, H = 1.8, els = [box(x, y, W, H, C.soft, { r: 0.12 })];
  els.push(dot(x + 0.16, y + 0.2, EP[h.ep].color));
  els.push(text(x + 0.38, y + 0.14, 1.25, 0.26, [{ text: h.id + " ", bold: true }, { text: h.ep, color: EP[h.ep].color }], { size: 11, valign: "middle" }));
  els.push(...badges(x + W - 1.28, y + 0.16, h));
  els.push(text(x + 0.16, y + 0.42, W - 0.32, 0.25, h.t, { size: 12, bold: true }));
  els.push(text(x + 0.16, y + 0.66, W - 0.32, 0.34, h.story, { size: 10, italic: true, color: C.muted }));
  h.ac.forEach((a, i) => {
    const cy = y + 1.06 + i * 0.35;
    els.push(circle(x + 0.18, cy + 0.06, 0.07, C.accent));
    els.push(text(x + 0.32, cy, W - 0.48, 0.32, a, { size: 10 }));
  });
  return els;
}

// ---------- diapositivas ----------
const S = [];

// 1 · Portada
const mini = [];
[["Por hacer", 3], ["En progreso", 2], ["Terminada", 1]].forEach(([lab, n], c) => {
  const x = 6.35 + c * 1.0;
  mini.push(text(x, 1.0, 0.9, 0.25, lab, { size: 9, bold: true, color: "A3A3A0" }));
  mini.push(box(x, 1.3, 0.88, 2.25, "2B302D", { r: 0.1 }));
  for (let k = 0; k < n; k++) mini.push(box(x + 0.1, 1.42 + k * 0.5, 0.68, 0.4, k === 0 && c === 1 ? C.accent : "4A514C", { r: 0.06 }));
});
S.push({
  dark: true,
  notes: "Albert (PO). Presenta al Grupo D3 y el tema: el tablero de NewBit con las historias de usuario, sus criterios de aceptación, prioridad y estimación, siguiendo la Guía del SBOK (8.5 backlog priorizado, 9.1–9.2 historias y estimación, 9.3.3 Scrumboard).",
  els: [
    text(0.7, 0.85, 5.5, 0.3, "INGENIERÍA DE SOFTWARE II · BACKLOG Y SCRUMBOARD", { size: 11, bold: true, color: C.accent, spacing: 1.5 }),
    text(0.7, 1.3, 5.6, 1.0, "Tablero Kanban", { size: 50, bold: true, color: C.white }),
    text(0.7, 2.25, 5.4, 0.9, "Historias de usuario de NewBit con criterios de aceptación, prioridad y estimación", { size: 19, color: "D9D9D6" }),
    ...mini,
    text(0.7, 3.62, 8.6, 0.3, [{ text: "GRUPO D3", bold: true }, { text: " · Laboratorio D · Equipo 3 · Proyecto NewBit" }], { size: 11, color: C.accent, spacing: 1 }),
    ...[["AC", "Albert Chumacero", "Product Owner"], ["AL", "Anthony Lopez", "Scrum Master · Developer"], ["LS", "Luis Salazar", "Developer"]]
      .flatMap(([ini, name, role], i) => {
        const x = 0.7 + i * 2.9;
        return [
          circle(x, 4.05, 0.5, "343A36"),
          text(x, 4.05, 0.5, 0.5, ini, { size: 13, bold: true, color: C.accent, align: "center", valign: "middle" }),
          text(x + 0.62, 4.04, 2.2, 0.28, name, { size: 14, bold: true, color: C.white }),
          text(x + 0.62, 4.32, 2.2, 0.25, role, { size: 11, color: "A3A3A0" }),
        ];
      }),
    text(0.7, 4.95, 8.6, 0.25, "Docente: Dr. Ing. Alfredo Daza Vergaray · Ingeniería de Software II · UNS · 2026-II", { size: 10, color: "8A8A86" }),
  ],
});

// 2 · Backlog priorizado
S.push({
  title: "Product Backlog priorizado",
  notes: "Albert (PO). Las 12 historias del FGAP040 ordenadas por prioridad: MoSCoW, los 100 puntos y las dependencias (SBOK 8.5; ver la actividad de priorización). Cada una tiene su prioridad MoSCoW, su estimación en puntos y el sprint donde entra. Total 31 puntos en 4 sprints. La prioridad salió de MoSCoW y los 100 puntos; la estimación, del puño de cinco.",
  els: [
    text(0.6, 1.08, 8.8, 0.28, `12 historias · ${TOTAL} puntos · 4 sprints de 2 semanas · priorizado con MoSCoW y 100 puntos · estimado con el puño de cinco`, { size: 12, color: C.muted }),
    { t: "table", x: 0.6, y: 1.45, w: 8.8, colW: [0.45, 0.65, 2.75, 2.25, 1.0, 0.6, 1.1], rowH: 0.27, size: 11,
      rows: [["#", "HU", "Historia", "Épica", "Prioridad", "Pts", "Sprint"],
        ...byRank.map(h => [String(h.rank), h.id, h.t, `${h.ep} · ${EP[h.ep].name}`, h.mo, String(h.pts), `Sprint ${h.sp}`])],
      boldCols: [1], center: [0, 4, 5, 6] },
  ],
});

// 3–4 · Criterios de aceptación
[[0, 6], [6, 12]].forEach(([a, b], k) => {
  const els = [text(0.6, 1.08, 8.8, 0.25, "Cada historia con sus criterios de aceptación: los define el PO y son los que se revisan al aceptar o rechazar la historia.", { size: 11, color: C.muted })];
  HU.slice(a, b).forEach((h, i) => els.push(...storyCard(0.6 + (i % 3) * 3.0, 1.42 + Math.floor(i / 3) * 1.86, h)));
  S.push({
    title: `Criterios de aceptación (${k + 1}/2)`,
    notes: k === 0
      ? "Anthony. Cada tarjeta es una historia: código y épica, prioridad y puntos arriba; la historia en formato «Como…, quiero…, para…»; y abajo sus criterios de aceptación, que son verificables. Aquí las épicas EP01 a EP03: ingestión, filtrado con YOLOv4 y segmentación."
      : "Luis. Épicas EP04 a EP06: clasificación con ConvLSTM, la interfaz con la alerta y la administración. En HU08 el criterio es reportar las métricas, no alcanzar una cifra: no afirmamos resultados que aún no tenemos.",
    els,
  });
});

// 5 · Scrumboard del Sprint 1
const cols = ["Historia", "Por hacer", "En progreso", "En prueba", "Terminada"];
const cx = [0.6, 2.64, 4.34, 6.04, 7.74], cw = [1.9, 1.62, 1.62, 1.62, 1.66];
const sb = [text(0.6, 1.08, 8.8, 0.28, `Sprint 1 · ${SPRINTS[0].d} · 3 historias · ${ptsOf(1)} puntos · inicio del sprint · tareas propuestas por el equipo`, { size: 12, color: C.muted })];
cols.forEach((c, i) => sb.push(...pill(cx[i], 1.45, cw[i], 0.3, c, i === 0 ? C.accent : C.ink, C.white, 11)));
HU.filter(h => h.sp === 1).forEach((h, r) => {
  const y = 1.88 + r * 1.06;
  sb.push(box(cx[0], y, cw[0], 0.96, C.soft, { r: 0.1 }));
  sb.push(dot(cx[0] + 0.12, y + 0.14, EP[h.ep].color));
  sb.push(text(cx[0] + 0.32, y + 0.08, 1.5, 0.26, [{ text: h.id + " ", bold: true }, { text: h.ep, color: EP[h.ep].color }], { size: 11, valign: "middle" }));
  sb.push(text(cx[0] + 0.12, y + 0.36, 1.7, 0.26, h.t, { size: 12, bold: true }));
  sb.push(...badges(cx[0] + 0.12, y + 0.64, h));
  for (let c = 1; c < 5; c++) sb.push(box(cx[c], y, cw[c], 0.96, "FAFAF9", { r: 0.1 }));
  h.tasks.forEach((t, k) => {
    sb.push(box(cx[1] + 0.08, y + 0.07 + k * 0.28, cw[1] - 0.16, 0.25, "FFE9A8", { r: 0.04 }));
    sb.push(text(cx[1] + 0.16, y + 0.07 + k * 0.28, cw[1] - 0.3, 0.25, t, { size: 10, valign: "middle" }));
  });
});
S.push({
  title: "Tablero del Sprint 1 (Scrumboard)",
  notes: "Luis. Es el Scrumboard de la Guía del SBOK (9.3.3, fig. 9-10): cada fila es una historia comprometida en el Sprint 1 y sus tareas son notas que avanzan de Por hacer a Terminada. Hoy, antes de empezar el sprint, todas están en Por hacer. La columna «En prueba» es la variante del libro para tareas terminadas que aún se están verificando.",
  els: sb,
});

// 6 · Cómo priorizamos y estimamos
const pe = [
  box(0.6, 1.2, 4.3, 3.65, C.soft, { r: 0.14 }),
  text(0.85, 1.35, 3.8, 0.35, "Prioridad", { size: 18, bold: true }),
  text(0.85, 1.72, 3.85, 0.5, "Valor + riesgo + dependencias (SBOK 8.5), con la escala MoSCoW.", { size: 12, color: C.muted }),
];
[["Must", "Debe tener"], ["Should", "Debería tener"], ["Could", "Podría tener"]].forEach(([m, lab], i) => {
  const x = 0.85 + i * 1.3, n = HU.filter(h => h.mo === m).length;
  pe.push(text(x, 2.3, 1.2, 0.7, String(n), { size: 40, bold: true, color: m === "Must" ? C.ink : "6B7280" }));
  pe.push(...pill(x, 3.02, 0.75, 0.22, m.toUpperCase(), MO[m].bg, MO[m].fg, 8));
  pe.push(text(x, 3.3, 1.2, 0.25, lab, { size: 11, color: C.muted }));
});
pe.push(text(0.85, 3.75, 3.85, 1.1, "HU11 es Could pero entra en el Sprint 2: es pequeña y calibra el filtrado de HU03–HU04 (dependencia).", { size: 11 }));
pe.push(box(5.1, 1.2, 4.3, 3.65, C.soft, { r: 0.14 }));
pe.push(text(5.35, 1.35, 3.8, 0.35, "Estimación y plan", { size: 18, bold: true }));
pe.push(text(5.35, 1.72, 3.85, 0.5, "Puntos 1–5 con el puño de cinco: votan Anthony y Luis; el PO aclara dudas.", { size: 12, color: C.muted }));
SPRINTS.forEach((s, i) => {
  const y = 2.3 + i * 0.58, p = ptsOf(s.n), ids = HU.filter(h => h.sp === s.n).map(h => h.id).join(" · ");
  pe.push(text(5.35, y, 0.45, 0.25, `S${s.n}`, { size: 12, bold: true }));
  pe.push(box(5.8, y + 0.03, 3.0 * p / 8, 0.2, C.accent, { r: 0.04 }));
  pe.push(text(5.8 + 3.0 * p / 8 + 0.08, y, 0.6, 0.25, `${p} pts`, { size: 11, bold: true, color: C.accent }));
  pe.push(text(5.8, y + 0.26, 3.4, 0.22, `${s.d} · ${ids}`, { size: 10, color: C.muted }));
});
pe.push(text(5.35, 4.58, 3.9, 0.22, `Total ${TOTAL} puntos · unos 8 por sprint`, { size: 11, bold: true }));
pe.push(text(0.6, 4.95, 8.8, 0.2, "Criterios de aceptación (por historia) ≠ Definición de terminado (común a todas, FGAP070)", { size: 9, color: C.muted }));
S.push({
  title: "Cómo priorizamos y estimamos",
  notes: "Anthony. Prioridad: el PO ordena por valor, riesgo y dependencias; usamos MoSCoW: 8 Must, 3 Should y 1 Could. Estimación: los developers votan con el puño de cinco (1 = muy pequeña, 5 = muy grande). Total 31 puntos repartidos en 4 sprints de unos 8 puntos. Cierre: los criterios de aceptación son por historia; la definición de terminado (FGAP070) es común a todas.",
  els: pe,
});


// ---------- salida PPTX ----------
async function buildPptx() {
  const pres = new pptxgen();
  pres.layout = "LAYOUT_16x9";
  pres.title = "Tablero Kanban de NewBit";
  pres.author = "Grupo D3 (Laboratorio D · Equipo 3)";
  pres.theme = { headFontFace: FONT, bodyFontFace: FONT };
  pres.defineSlideMaster({ title: "PORTADA", background: { color: C.ink } });
  pres.defineSlideMaster({
    title: "CONTENIDO", background: { color: C.white },
    objects: [
      { placeholder: { options: { name: "title", type: "title", x: 0.6, y: 0.4, w: 8.8, h: 0.7, fontFace: FONT, fontSize: 30, bold: true, color: C.ink, margin: 0, align: "left", valign: "middle" }, text: "" } },
      { text: { text: "Tablero Kanban · NewBit · Grupo D3", options: { x: 0.6, y: 5.2, w: 5, h: 0.25, fontFace: FONT, fontSize: 9, color: C.muted, margin: 0 } } },
    ],
    slideNumber: { x: 8.9, y: 5.2, w: 0.5, h: 0.25, fontFace: FONT, fontSize: 9, color: C.muted, align: "right" },
  });
  let k = 0;
  for (const s of S) {
    const slide = pres.addSlide({ masterName: s.dark ? "PORTADA" : "CONTENIDO" });
    if (s.title) slide.addText(s.title, { placeholder: "title" });
    for (const e of s.els) {
      const name = `obj${++k}`;
      if (e.t === "rect") {
        const r = e.r ? Math.min(e.r, e.w / 2, e.h / 2) : 0;
        slide.addShape(r ? pres.ShapeType.roundRect : pres.ShapeType.rect, {
          x: e.x, y: e.y, w: e.w, h: e.h, objectName: name,
          fill: { color: e.fill, transparency: e.alpha || 0 }, line: { type: "none" },
          ...(r ? { rectRadius: r } : {}), ...(e.rot ? { rotate: e.rot } : {}),
        });
      } else if (e.t === "text") {
        slide.addText(e.runs.map(r => ({ text: r.text, options: { bold: r.bold, italic: r.italic, breakLine: r.breakLine, ...(r.color ? { color: r.color } : {}) } })), {
          x: e.x, y: e.y, w: e.w, h: e.h, objectName: name, isTextBox: true, margin: 0,
          fontFace: FONT, fontSize: e.size, color: e.color || C.ink, bold: !!e.bold, italic: !!e.italic,
          align: e.align || "left", valign: e.valign || "top", ...(e.spacing ? { charSpacing: e.spacing } : {}),
        });
      } else if (e.t === "table") {
        const rows = e.rows.map((row, ri) => row.map((cell, ci) => ({
          text: cell, options: {
            bold: ri === 0 || (e.boldCols || [0]).includes(ci), color: ri === 0 ? C.white : C.ink,
            align: (e.center || []).includes(ci) ? "center" : "left",
            fill: { color: ri === 0 ? C.ink : ri === e.highlight ? C.accentSoft : C.white },
          },
        })));
        slide.addTable(rows, { x: e.x, y: e.y, w: e.w, colW: e.colW, rowH: e.rowH, fontFace: FONT, fontSize: e.size, valign: "middle", margin: [0, 0.1, 0, 0.1], border: { type: "solid", pt: 0.75, color: C.line }, objectName: name });
      }
    }
    slide.addNotes(s.notes);
  }
  await pres.writeFile({ fileName: OUT + ".pptx" });
}

// ---------- salida HTML ----------
const PX = 128, pt = s => (s * PX / 72).toFixed(2) + "px", px = v => (v * PX).toFixed(1) + "px";
const esc = s => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
const hex = (c, alpha = 0) => alpha ? `rgba(${parseInt(c.slice(0, 2), 16)},${parseInt(c.slice(2, 4), 16)},${parseInt(c.slice(4), 16)},${(100 - alpha) / 100})` : "#" + c;
function htmlEl(e, dark) {
  const pos = `left:${px(e.x)};top:${px(e.y)};width:${px(e.w)};height:${px(e.h)}`;
  if (e.t === "rect") {
    const r = e.r ? Math.min(e.r, e.w / 2, e.h / 2) : 0;
    return `<div class="sh" style="${pos};background:${hex(e.fill, e.alpha)};border-radius:${px(r)}${e.rot ? `;transform:rotate(${e.rot}deg)` : ""}"></div>`;
  }
  if (e.t === "text") {
    const runs = e.runs.map(r => `<span style="${r.bold ? "font-weight:700;" : ""}${r.italic ? "font-style:italic;" : ""}${r.color ? `color:#${r.color};` : ""}">${esc(r.text)}</span>${r.breakLine ? "<br>" : ""}`).join("");
    const jc = { top: "flex-start", middle: "center", bottom: "flex-end" }[e.valign || "top"];
    return `<div class="tx" style="${pos};font-size:${pt(e.size)};color:#${e.color || (dark ? C.white : C.ink)};font-weight:${e.bold ? 700 : 400};${e.italic ? "font-style:italic;" : ""}text-align:${e.align || "left"};justify-content:${jc}${e.spacing ? `;letter-spacing:${pt(e.spacing)}` : ""}"><div>${runs}</div></div>`;
  }
  if (e.t === "table") {
    const cols = e.colW.map(w => `<col style="width:${px(w)}">`).join("");
    const body = e.rows.map((row, ri) => `<tr style="height:${px(e.rowH)};background:#${ri === 0 ? C.ink : ri === e.highlight ? C.accentSoft : C.white};color:#${ri === 0 ? C.white : C.ink}">${row.map((c, ci) => `<td style="font-weight:${ri === 0 || (e.boldCols || [0]).includes(ci) ? 700 : 400};text-align:${(e.center || []).includes(ci) ? "center" : "left"}">${esc(c)}</td>`).join("")}</tr>`).join("");
    return `<table class="tb" style="left:${px(e.x)};top:${px(e.y)};width:${px(e.w)};font-size:${pt(e.size)}"><colgroup>${cols}</colgroup>${body}</table>`;
  }
}
// Carlito (OFL, misma métrica que Calibri) incrustada: el HTML se ve igual sin internet y sin Calibri instalada.
function fontFaces() {
  return [["Regular", 400, "normal"], ["Bold", 700, "normal"], ["Italic", 400, "italic"], ["BoldItalic", 700, "italic"]]
    .map(([f, w, st]) => `@font-face { font-family:"Deck"; font-weight:${w}; font-style:${st}; font-display:block; src:url(data:font/woff2;base64,${fs.readFileSync(path.join(__dirname, `Carlito-${f}.woff2`)).toString("base64")}) format("woff2"); }`)
    .join("\n  ");
}
function buildHtml() {
  const slides = S.map((s, i) => {
    const title = s.title ? `<div class="tx title" style="left:${px(0.6)};top:${px(0.4)};width:${px(8.8)};height:${px(0.7)};font-size:${pt(30)};justify-content:center"><div>${esc(s.title)}</div></div>` : "";
    const foot = s.dark ? "" : `<div class="tx foot" style="left:${px(0.6)};top:${px(5.2)};width:${px(5)};height:${px(0.25)};font-size:${pt(9)}"><div>Tablero Kanban · NewBit · Grupo D3</div></div><div class="tx foot" style="left:${px(8.9)};top:${px(5.2)};width:${px(0.5)};height:${px(0.25)};font-size:${pt(9)};text-align:right"><div>${i + 1}</div></div>`;
    return `<section class="slide${s.dark ? " dark" : ""}" aria-label="Diapositiva ${i + 1}">${title}${s.els.map(e => htmlEl(e, s.dark)).join("")}${foot}<aside class="notes">${esc(s.notes)}</aside></section>`;
  }).join("\n");
  const html = `<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Tablero Kanban NewBit</title>
<style>
  ${fontFaces()}
  :root { --ink:#${C.ink}; --muted:#${C.muted}; --bg:#E9E9E6; }
  * { box-sizing:border-box; margin:0; padding:0; }
  html, body { height:100%; background:var(--bg); font-family:"Deck", Calibri, Carlito, sans-serif; -webkit-font-smoothing:antialiased; text-rendering:geometricPrecision; font-kerning:normal; color:var(--ink); }
  .deck { position:fixed; inset:0; overflow:hidden; }
  .slide { position:absolute; left:50%; top:calc(50% - 16px); width:1280px; height:720px; margin:-360px 0 0 -640px; background:#fff; overflow:hidden; display:none; transform-origin:50% 50%; box-shadow:0 10px 40px rgba(0,0,0,.12); -webkit-print-color-adjust:exact; print-color-adjust:exact; }
  .slide.on { display:block; }
  .slide.dark { background:var(--ink); }
  .sh, .tx, .tb { position:absolute; margin:0; }
  .sh, .tb, .tb tr { -webkit-print-color-adjust:exact; print-color-adjust:exact; }
  .tx > div { width:100%; overflow-wrap:normal; }
  .tx { display:flex; flex-direction:column; line-height:1.2; }
  .title { font-weight:700; }
  .foot { color:var(--muted); }
  .tb { border-collapse:collapse; table-layout:fixed; }
  .tb td { border:1px solid #${C.line}; padding:0 ${px(0.1)}; vertical-align:middle; line-height:1.15; }
  .notes { display:none; position:absolute; left:0; right:0; bottom:0; padding:16px 24px; background:rgba(31,36,33,.94); color:#fff; font-size:18px; line-height:1.4; }
  body.show-notes .notes { display:block; }
  .hud { position:fixed; right:16px; bottom:12px; font:13px/1 system-ui, sans-serif; color:#6B7280; user-select:none; }
  .hud button { font:inherit; border:0; background:#fff; color:#1F2421; border-radius:6px; padding:6px 10px; margin-left:4px; cursor:pointer; }
  @media print {
    @page { size:13.333in 7.5in; margin:0; }
    html, body { background:#fff; height:auto; }
    .deck { position:static; overflow:visible; }
    .slide { display:block !important; position:relative; left:0; top:0; margin:0; transform:none !important; box-shadow:none; page-break-after:always; break-after:page; }
    .slide:last-child { page-break-after:auto; break-after:auto; }
    .hud, .notes { display:none !important; }
  }
</style>
</head>
<body>
<main class="deck">
${slides}
</main>
<div class="hud"><span id="n"></span><button id="prev" aria-label="Anterior">←</button><button id="next" aria-label="Siguiente">→</button><button id="nt" aria-label="Notas">Notas</button><button id="pdf" aria-label="Exportar a PDF">PDF</button></div>
<script>
  const slides = [...document.querySelectorAll('.slide')];
  let i = Math.max(0, Math.min(slides.length - 1, (parseInt(location.hash.slice(1)) || 1) - 1));
  function fit() { const s = Math.min(innerWidth / 1280, (innerHeight - 48) / 720) * 0.97; slides.forEach(el => el.style.transform = 'scale(' + s + ')'); }
  function show(k) { i = Math.max(0, Math.min(slides.length - 1, k)); slides.forEach((el, j) => el.classList.toggle('on', j === i)); document.getElementById('n').textContent = (i + 1) + ' / ' + slides.length; history.replaceState(null, '', '#' + (i + 1)); }
  addEventListener('keydown', e => {
    if (['ArrowRight', 'PageDown', ' '].includes(e.key)) { e.preventDefault(); show(i + 1); }
    if (['ArrowLeft', 'PageUp'].includes(e.key)) show(i - 1);
    if (e.key === 'Home') show(0);
    if (e.key === 'End') show(slides.length - 1);
    if (e.key.toLowerCase() === 'n') document.body.classList.toggle('show-notes');
    if (e.key.toLowerCase() === 'f') document.documentElement.requestFullscreen?.();
  });
  document.getElementById('prev').onclick = () => show(i - 1);
  document.getElementById('next').onclick = () => show(i + 1);
  document.getElementById('nt').onclick = () => document.body.classList.toggle('show-notes');
  document.getElementById('pdf').onclick = () => print();
  let x0 = null;
  addEventListener('touchstart', e => x0 = e.touches[0].clientX, { passive: true });
  addEventListener('touchend', e => { if (x0 === null) return; const d = e.changedTouches[0].clientX - x0; if (Math.abs(d) > 40) show(i + (d < 0 ? 1 : -1)); x0 = null; });
  addEventListener('resize', fit); fit(); show(i);
</script>
</body>
</html>
`;
  fs.writeFileSync(OUT + ".html", html);
}

buildHtml();
buildPptx().then(() => console.log("OK:", OUT + ".html / .pptx"));
