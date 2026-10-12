// Genera Priorizacion_MoSCoW_100_Puntos_NewBit.html y .pptx desde una sola definición.
// Uso: node generar_presentacion.js [carpeta_con_node_modules]   (requiere pptxgenjs@3.12.0)
// Coordenadas en pulgadas sobre 10 × 5.625 (16:9). En el HTML, 1 in = 128 px.
const path = require("path");
const fs = require("fs");
const modDir = process.argv[2];
const pptxgen = require(modDir ? path.join(modDir, "node_modules", "pptxgenjs") : "pptxgenjs");

const OUT = path.join(__dirname, "Priorizacion_MoSCoW_100_Puntos_NewBit");
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
// Votos de los 100 puntos del Grupo D3 (sesión en clase, 12/10/2026).
const EP = {
  EP01: { name: "Ingestión de video", color: "5B6B7A" },
  EP02: { name: "Filtrado YOLOv4", color: "2F6DB5" },
  EP03: { name: "Segmentación temporal", color: "7A5AB8" },
  EP04: { name: "Clasificación ConvLSTM", color: "B4235A" },
  EP05: { name: "GUI y validación", color: "1F8A70" },
  EP06: { name: "Administración", color: "8A6D1E" },
};
// v = [Albert, Anthony, Luis]; dep = historias de las que depende; final = orden final del backlog.
const HU = [
  { id: "HU01", ep: "EP01", t: "Cargar video", mo: "Must", v: [6, 8, 5], dep: "—", sp: 1, final: 1 },
  { id: "HU02", ep: "EP01", t: "Extraer frames", mo: "Must", v: [5, 8, 7], dep: "HU01", sp: 1, final: 2 },
  { id: "HU03", ep: "EP02", t: "Detectar trabajadores", mo: "Must", v: [12, 12, 13], dep: "HU02", sp: 1, final: 3 },
  { id: "HU04", ep: "EP02", t: "Descartar frames vacíos", mo: "Must", v: [8, 10, 10], dep: "HU03", sp: 2, final: 4 },
  { id: "HU05", ep: "EP03", t: "Agrupar en clips", mo: "Must", v: [6, 9, 10], dep: "HU04", sp: 2, final: 5 },
  { id: "HU06", ep: "EP03", t: "Descartar clips cortos", mo: "Should", v: [3, 4, 5], dep: "HU05", sp: 2, final: 11 },
  { id: "HU07", ep: "EP04", t: "Procesar con ConvLSTM", mo: "Must", v: [15, 14, 18], dep: "HU05", sp: 3, final: 6 },
  { id: "HU08", ep: "EP04", t: "Etiquetar el clip", mo: "Must", v: [14, 12, 12], dep: "HU07", sp: 3, final: 7 },
  { id: "HU09", ep: "EP05", t: "Ver video con recuadro", mo: "Must", v: [13, 9, 8], dep: "HU08", sp: 4, final: 8 },
  { id: "HU10", ep: "EP05", t: "Alerta insegura", mo: "Should", v: [10, 6, 5], dep: "HU08", sp: 4, final: 9 },
  { id: "HU11", ep: "EP06", t: "Ajustar umbral", mo: "Could", v: [2, 3, 3], dep: "HU03", sp: 2, final: 12 },
  { id: "HU12", ep: "EP06", t: "Ver log de tiempos", mo: "Should", v: [6, 5, 4], dep: "HU04", sp: 4, final: 10 },
];
HU.forEach(h => h.tot = h.v.reduce((a, b) => a + b, 0));
const WONT = [
  { id: "W1", t: "Cámaras en vivo" },
  { id: "W2", t: "Alertas físicas en planta" },
  { id: "W3", t: "Reconocimiento facial" },
];
const VOTERS = ["Albert", "Anthony", "Luis"];
const MO = {
  Must: { bg: C.ink, fg: C.white, es: "Debe tener" },
  Should: { bg: "9CA3AF", fg: C.white, es: "Debería tener" },
  Could: { bg: C.line, fg: C.ink, es: "Podría tener" },
  Wont: { bg: "F9E0E0", fg: "B42318", es: "No tendrá" },
};
const byTot = [...HU].sort((a, b) => b.tot - a.tot || a.id.localeCompare(b.id));
const byFinal = [...HU].sort((a, b) => a.final - b.final);
const MAXTOT = Math.max(...HU.map(h => h.tot));

// ---------- piezas ----------
const pill = (x, y, w, h, label, bg, fg, size = 9) => [
  box(x, y, w, h, bg, { r: h / 2 }),
  text(x, y, w, h, label, { size, bold: true, color: fg, align: "center", valign: "middle" }),
];
const moPill = (x, y, mo, w = 0.66) => pill(x, y, w, 0.22, mo === "Wont" ? "WON'T" : mo.toUpperCase(), MO[mo].bg, MO[mo].fg, 8);
const dot = (x, y, color, d = 0.14) => circle(x, y, d, color);
function chip(x, y, w, h, color, id, title) {
  return [
    box(x, y, w, h, C.white, { r: 0.08 }),
    dot(x + 0.12, y + 0.1, color, 0.12),
    text(x + 0.3, y + 0.05, w - 0.38, 0.22, id, { size: 10, bold: true, valign: "middle" }),
    text(x + 0.12, y + 0.26, w - 0.2, 0.34, title, { size: 10 }),
  ];
}
// Fila de tabla hecha con formas: mismas posiciones en HTML y PPTX.
function gridRow(y, h, cols, cells, o = {}) {
  const els = [];
  if (o.fill) els.push(box(cols[0].x, y, cols[cols.length - 1].x + cols[cols.length - 1].w - cols[0].x, h, o.fill, { r: o.r || 0 }));
  cells.forEach((c, i) => {
    if (c === null || c === undefined) return;
    const col = cols[i], cell = typeof c === "object" && !Array.isArray(c) ? c : { v: c };
    els.push(text(col.x + 0.08, y, col.w - 0.16, h, String(cell.v), {
      size: o.size || 10, bold: o.bold || cell.bold, color: o.color || cell.color || C.ink,
      align: col.align || "left", valign: "middle",
    }));
  });
  return els;
}

// ---------- diapositivas ----------
const S = [];

// 1 · Portada
const bars = [["M", "Must", 2.6], ["S", "Should", 1.9], ["C", "Could", 1.25], ["W", "Wont", 0.7]].flatMap(([l, m, w], i) => [
  box(6.3, 1.15 + i * 0.58, w, 0.42, i === 0 ? C.accent : ["", "6B7280", "4A514C", "343A36"][i], { r: 0.08 }),
  text(6.42, 1.15 + i * 0.58, 0.4, 0.42, l, { size: 16, bold: true, color: C.white, valign: "middle" }),
]);
S.push({
  dark: true,
  notes: "Albert (PO). Presenta al Grupo D3 y la actividad: priorizar el Product Backlog de NewBit con dos métodos de la Guía del SBOK, MoSCoW y los 100 puntos.",
  els: [
    text(0.7, 0.85, 5.4, 0.3, "INGENIERÍA DE SOFTWARE II · PRIORIZACIÓN EN SCRUM", { size: 11, bold: true, color: C.accent, spacing: 1.5 }),
    text(0.7, 1.3, 5.5, 1.0, "Priorización", { size: 50, bold: true, color: C.white }),
    text(0.7, 2.25, 5.3, 0.9, "Métodos MoSCoW y de los 100 puntos aplicados a las historias de NewBit", { size: 19, color: "D9D9D6" }),
    ...bars,
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

// 2 · Los dos métodos
const m2 = [
  text(0.6, 1.08, 8.8, 0.28, "La prioridad combina valor, riesgo y dependencias (SBOK 8.5). Estos dos métodos miden el valor de cada historia.", { size: 12, color: C.muted }),
  box(0.6, 1.5, 4.3, 3.45, C.soft, { r: 0.14 }),
  text(0.85, 1.65, 3.8, 0.35, "Método MoSCoW", { size: 18, bold: true }),
  text(0.85, 2.0, 3.85, 0.45, "Clasifica cada historia en 4 grupos, de mayor a menor prioridad.", { size: 12, color: C.muted }),
];
[["Must", "Sin ella el producto no tiene valor"], ["Should", "Importante, pero puede esperar"], ["Could", "Sería bueno; no es necesaria"], ["Wont", "Queda fuera de esta versión"]].forEach(([m, d], i) => {
  const y = 2.6 + i * 0.5;
  m2.push(...moPill(0.85, y + 0.04, m, 0.78));
  m2.push(text(1.75, y, 3.0, 0.3, [{ text: MO[m].es, bold: true }, { text: " · " + d }], { size: 11, valign: "middle" }));
});
m2.push(text(0.85, 4.6, 3.8, 0.25, "SBOK 4.5.2 y 8.5.2.1 · pp. 77 y 169", { size: 10, color: C.muted }));
m2.push(box(5.1, 1.5, 4.3, 3.45, C.soft, { r: 0.14 }));
m2.push(text(5.35, 1.65, 3.8, 0.35, "Método de los 100 puntos", { size: 18, bold: true }));
m2.push(text(5.35, 2.0, 3.85, 0.45, "Leffingwell y Widrig (2003): se vota con puntos el valor de cada historia.", { size: 12, color: C.muted }));
["Cada integrante tiene 100 puntos.", "Los reparte: más puntos a lo más importante.", "Se suman los puntos de cada historia.", "Se ordena de mayor a menor total."].forEach((t, i) => {
  const y = 2.6 + i * 0.5;
  m2.push(circle(5.35, y + 0.01, 0.3, C.accent));
  m2.push(text(5.35, y + 0.01, 0.3, 0.3, String(i + 1), { size: 12, bold: true, color: C.white, align: "center", valign: "middle" }));
  m2.push(text(5.8, y, 3.4, 0.32, t, { size: 12, valign: "middle" }));
});
m2.push(text(5.35, 4.6, 3.8, 0.25, "SBOK 4.5.2 y 8.5.2.1 · pp. 77 y 169", { size: 10, color: C.muted }));
S.push({
  title: "Dos métodos del SBOK para priorizar",
  notes: "Anthony. MoSCoW clasifica cada historia en cuatro grupos: debe, debería, podría y no tendrá. Los 100 puntos son una votación: cada integrante reparte 100 puntos y se suman. MoSCoW dice en qué grupo va cada historia; los 100 puntos, cuál va primero dentro del grupo.",
  els: m2,
});

// 3 · MoSCoW aplicado
const colsMo = [
  { m: "Must", x: 0.6, w: 3.2, q: "Sin ella, NewBit no detecta conductas inseguras" },
  { m: "Should", x: 3.95, w: 1.75, q: "Importante, pero NewBit funciona sin ella" },
  { m: "Could", x: 5.85, w: 1.75, q: "Suma si sobra tiempo" },
  { m: "Wont", x: 7.75, w: 1.65, q: "Fuera del alcance del Acta" },
];
const m3 = [text(0.6, 1.08, 8.8, 0.28, "Pregunta guía del PO para cada historia del FGAP040: ¿qué pasa con NewBit si no la hacemos?", { size: 12, color: C.muted })];
colsMo.forEach(c => {
  const items = c.m === "Wont" ? WONT.map(w => ({ id: w.id, t: w.t, color: "B42318" })) : HU.filter(h => h.mo === c.m).sort((a, b) => b.tot - a.tot).map(h => ({ id: h.id, t: h.t, color: EP[h.ep].color }));
  m3.push(box(c.x, 1.45, c.w, 3.6, C.soft, { r: 0.14 }));
  m3.push(...pill(c.x + 0.12, 1.57, c.w - 0.24, 0.3, `${MO[c.m].es.toUpperCase()} · ${items.length}`, MO[c.m].bg, MO[c.m].fg, 10));
  m3.push(text(c.x + 0.14, 1.93, c.w - 0.28, 0.42, c.q, { size: 10, italic: true, color: C.muted }));
  const two = c.m === "Must", cw = two ? (c.w - 0.36) / 2 : c.w - 0.24;
  items.forEach((it, k) => {
    const col = two ? k % 2 : 0, row = two ? Math.floor(k / 2) : k;
    m3.push(...chip(c.x + 0.12 + col * (cw + 0.12), 2.42 + row * 0.65, cw, 0.6, it.color, it.id, it.t));
  });
});
S.push({
  title: "Paso 1 · MoSCoW: las historias en 4 grupos",
  notes: "Albert (PO). Para cada historia preguntamos: ¿qué pasa con NewBit si no la hacemos? Ocho son Must: sin ellas no hay detección. Tres son Should: la alerta, el log de tiempos y descartar clips cortos. HU11, ajustar el umbral, es Could. En Won't van tres cosas que el Acta dejó fuera de alcance: cámaras en vivo, alertas físicas y reconocimiento facial.",
  els: m3,
});

// 4 · 100 puntos
const cols4 = [
  { x: 0.6, w: 0.62 }, { x: 1.22, w: 2.1 }, { x: 3.32, w: 0.72, align: "center" },
  { x: 4.04, w: 0.82, align: "center" }, { x: 4.86, w: 0.62, align: "center" }, { x: 5.48, w: 0.62, align: "center" }, { x: 6.1, w: 3.3 },
];
const RH = 0.24, Y0 = 1.45;
const m4 = [
  text(0.6, 1.08, 8.8, 0.28, "Votación en clase (12/10): cada integrante repartió sus 100 puntos por separado y luego se sumaron.", { size: 12, color: C.muted }),
  ...gridRow(Y0, RH + 0.04, cols4, ["HU", "Historia", ...VOTERS, "Total", "Puntos totales"], { fill: C.ink, color: C.white, bold: true, r: 0.06 }),
];
byTot.forEach((h, i) => {
  const y = Y0 + 0.32 + i * RH;
  if (i % 2 === 0) m4.push(box(0.6, y, 8.8, RH, C.soft));
  m4.push(dot(0.66, y + 0.06, EP[h.ep].color, 0.12));
  m4.push(text(0.84, y, 0.4, RH, h.id, { size: 10, bold: true, valign: "middle" }));
  m4.push(...gridRow(y, RH, cols4, [null, h.t, ...h.v, { v: h.tot, bold: true }, null]));
  const bw = 2.6 * h.tot / MAXTOT;
  m4.push(box(6.18, y + 0.05, bw, RH - 0.1, i < 3 ? C.accent : "F6A98F", { r: 0.03 }));
});
const ySum = Y0 + 0.32 + 12 * RH + 0.04;
m4.push(...gridRow(ySum, RH + 0.04, cols4, [{ v: "Suma", bold: true }, null, 100, 100, 100, 300, null], { bold: true, fill: C.accentSoft, r: 0.06 }));
m4.push(text(6.18, ySum, 3.2, RH + 0.04, "cada uno reparte exactamente 100", { size: 10, color: C.muted, valign: "middle" }));
S.push({
  title: "Paso 2 · 100 puntos por integrante",
  notes: "Luis. Cada uno repartió 100 puntos sin ver los votos de los demás. La más votada es HU07, el modelo ConvLSTM, con 47 puntos; luego HU08 y HU03. La menos votada es HU11, ajustar el umbral, con 8. Albert, como PO, dio más puntos a lo que ve el usuario (la GUI y la alerta); los developers, al modelo.",
  els: m4,
});

// 5 · Backlog final
const cols5 = [
  { x: 0.6, w: 0.45, align: "center" }, { x: 1.05, w: 0.68 }, { x: 1.73, w: 2.45 }, { x: 4.18, w: 1.0, align: "center" },
  { x: 5.18, w: 1.0, align: "center" }, { x: 6.18, w: 1.4, align: "center" }, { x: 7.58, w: 1.82, align: "center" },
];
const m5 = [
  text(0.6, 1.08, 8.8, 0.28, "1) MoSCoW define el grupo · 2) los 100 puntos ordenan dentro del grupo · 3) las dependencias fijan el orden de ejecución", { size: 12, color: C.muted }),
  ...gridRow(Y0, RH + 0.04, cols5, ["#", "HU", "Historia", "MoSCoW", "100 pts", "Depende de", "Sprint"], { fill: C.ink, color: C.white, bold: true, r: 0.06 }),
];
byFinal.forEach((h, i) => {
  const y = Y0 + 0.32 + i * RH;
  if (i % 2 === 0) m5.push(box(0.6, y, 8.8, RH, C.soft));
  m5.push(...gridRow(y, RH, cols5, [h.final, { v: h.id, bold: true }, h.t, null, { v: h.tot, bold: true }, h.dep, `Sprint ${h.sp}`]));
  m5.push(...moPill(4.35, y + 0.02, h.mo));
});
const yN = Y0 + 0.32 + 12 * RH + 0.08;
m5.push(box(0.6, yN, 8.8, 0.36, C.accentSoft, { r: 0.08 }));
m5.push(text(0.8, yN, 8.4, 0.36, [{ text: "Ejemplo: ", bold: true }, { text: "HU10 (alerta) sacó 21 puntos, más que HU01 y HU02, pero va después: es Should y depende de HU08." }], { size: 11, valign: "middle" }));
S.push({
  title: "Paso 3 · Resultado: backlog priorizado",
  notes: "Anthony. Combinamos los dos métodos: MoSCoW decide el grupo, los 100 puntos ordenan dentro del grupo y las dependencias deciden cuándo se puede hacer. Por eso las Must van en el orden del flujo: no se puede clasificar un clip sin antes cargar el video y armar los clips. Este orden es el que usamos en el tablero Kanban.",
  els: m5,
});

// 6 · Conclusiones
const concl = [
  ["47", "HU07 · ConvLSTM", "Es la historia más valorada por los tres: es el núcleo de NewBit."],
  ["8 / 3 / 1", "Must / Should / Could", "Ocho historias son imprescindibles; HU11 es la única Could."],
  ["13 vs 8", "HU09 · Albert vs Luis", "El PO valora lo que ve el usuario; los developers, el modelo. Los votos distintos abren la conversación."],
];
const m6 = [];
concl.forEach(([big, lab, d], i) => {
  const x = 0.6 + i * 3.0;
  m6.push(box(x, 1.35, 2.8, 2.55, C.soft, { r: 0.14 }));
  m6.push(text(x + 0.25, 1.5, 2.4, 0.75, big, { size: 34, bold: true, color: C.accent }));
  m6.push(text(x + 0.25, 2.25, 2.4, 0.3, lab, { size: 13, bold: true }));
  m6.push(text(x + 0.25, 2.6, 2.35, 1.15, d, { size: 12 }));
});
m6.push(box(0.6, 4.1, 8.8, 0.62, C.accentSoft, { r: 0.12 }));
m6.push(text(0.85, 4.1, 8.4, 0.62, "MoSCoW es rápido para separar lo esencial; los 100 puntos ordenan con más detalle. Juntos, más las dependencias, dan el backlog.", { size: 13, bold: true, valign: "middle" }));
m6.push(text(0.6, 4.85, 8.8, 0.25, [
  { text: "Fuente: SCRUMstudy. (2022). " },
  { text: "Guía de los fundamentos de Scrum (Guía del SBOK®)", italic: true },
  { text: " (4.ª ed.), 4.5.2 y 8.5.2.1, pp. 76–78 y 169." },
], { size: 10, color: C.muted }));
S.push({
  title: "Qué aprendimos",
  notes: "Albert (PO). Tres ideas: HU07 es la más valorada; ocho historias son imprescindibles; y los votos distintos entre PO y developers son útiles porque abren la conversación. MoSCoW separa lo esencial rápido; los 100 puntos ordenan con más detalle.",
  els: m6,
});

// ---------- salida PPTX ----------
async function buildPptx() {
  const pres = new pptxgen();
  pres.layout = "LAYOUT_16x9";
  pres.title = "Priorización MoSCoW y 100 puntos · NewBit";
  pres.author = "Grupo D3 (Laboratorio D · Equipo 3)";
  pres.theme = { headFontFace: FONT, bodyFontFace: FONT };
  pres.defineSlideMaster({ title: "PORTADA", background: { color: C.ink } });
  pres.defineSlideMaster({
    title: "CONTENIDO", background: { color: C.white },
    objects: [
      { placeholder: { options: { name: "title", type: "title", x: 0.6, y: 0.4, w: 8.8, h: 0.7, fontFace: FONT, fontSize: 30, bold: true, color: C.ink, margin: 0, align: "left", valign: "middle" }, text: "" } },
      { text: { text: "Priorización · NewBit · Grupo D3", options: { x: 0.6, y: 5.2, w: 5, h: 0.25, fontFace: FONT, fontSize: 9, color: C.muted, margin: 0 } } },
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
    const foot = s.dark ? "" : `<div class="tx foot" style="left:${px(0.6)};top:${px(5.2)};width:${px(5)};height:${px(0.25)};font-size:${pt(9)}"><div>Priorización · NewBit · Grupo D3</div></div><div class="tx foot" style="left:${px(8.9)};top:${px(5.2)};width:${px(0.5)};height:${px(0.25)};font-size:${pt(9)};text-align:right"><div>${i + 1}</div></div>`;
    return `<section class="slide${s.dark ? " dark" : ""}" aria-label="Diapositiva ${i + 1}">${title}${s.els.map(e => htmlEl(e, s.dark)).join("")}${foot}<aside class="notes">${esc(s.notes)}</aside></section>`;
  }).join("\n");
  const html = `<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Priorización NewBit</title>
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
