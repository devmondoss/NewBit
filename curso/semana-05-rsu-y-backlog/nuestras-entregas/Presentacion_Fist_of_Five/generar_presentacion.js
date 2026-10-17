// Genera Presentacion_Fist_of_Five.html y Presentacion_Fist_of_Five.pptx desde una sola definición.
// Uso: node generar_presentacion.js [carpeta_con_node_modules]   (requiere pptxgenjs@3.12.0)
// Coordenadas en pulgadas sobre 10 × 5.625 (16:9). En el HTML, 1 in = 128 px.
const path = require("path");
const fs = require("fs");
const modDir = process.argv[2];
const pptxgen = require(modDir ? path.join(modDir, "node_modules", "pptxgenjs") : "pptxgenjs");

const OUT = path.join(__dirname, "Presentacion_Fist_of_Five");
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

// ---------- diapositivas ----------
const S = [];

// 1 · Portada
S.push({
  dark: true,
  notes: "Albert (PO). Presenta al Grupo D3 (laboratorio D, equipo 3) y el tema: una técnica de estimación del SBOK que se hace con una sola mano. Duración total: unos 10 minutos más una votación con el aula.",
  els: [
    text(0.7, 0.85, 6, 0.3, "INGENIERÍA DE SOFTWARE II · ESTIMACIÓN EN SCRUM", { size: 11, bold: true, color: C.accent, spacing: 1.5 }),
    text(0.7, 1.3, 6, 1.0, "Puño de cinco", { size: 54, bold: true, color: C.white }),
    text(0.7, 2.3, 5.2, 0.9, [{ text: "Fist of Five", italic: true }, { text: ": estimar y decidir en equipo con una sola mano" }], { size: 20, color: "D9D9D6" }),
    ...hand(6.75, 0.95, 2.2, 5, C.accent),
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

// 2 · Qué es
S.push({
  title: "Votar a la vez, con los dedos, del 1 al 5",
  notes: "Anthony. Es una técnica del SBOK dentro del proceso 9.2 Estimar historias de usuario. Tiene dos usos: estimar el tamaño relativo de una historia y medir el acuerdo del equipo en una decisión. Vota el Equipo Scrum; el Product Owner no estima, solo aclara dudas. Solo se estiman historias que cumplen la definición de listo.",
  els: [
    text(0.6, 1.25, 8.8, 0.4, "Técnica del SBOK (proceso 9.2 Estimar historias de usuario). Sencilla, rápida y sin materiales.", { size: 15, color: C.muted }),
    box(0.6, 1.9, 4.25, 2.55, C.soft, { r: 0.18 }),
    ...hand(0.95, 2.2, 0.85, 3, C.ink),
    text(2.05, 2.25, 2.6, 0.4, "Para estimar", { size: 20, bold: true }),
    text(2.05, 2.7, 2.6, 0.85, "Los dedos indican el tamaño relativo de una historia de usuario.", { size: 14 }),
    text(0.95, 3.8, 3.7, 0.4, [{ text: "Ej.: ", bold: true }, { text: "1 = muy pequeña · 5 = muy grande" }], { size: 12, color: C.muted }),
    box(5.15, 1.9, 4.25, 2.55, C.soft, { r: 0.18 }),
    ...hand(5.5, 2.2, 0.85, 5, C.yes),
    text(6.6, 2.25, 2.6, 0.4, "Para decidir", { size: 20, bold: true }),
    text(6.6, 2.7, 2.6, 0.85, "Los dedos indican cuánto estoy de acuerdo con la propuesta.", { size: 14 }),
    text(5.5, 3.8, 3.7, 0.4, [{ text: "Ej.: ", bold: true }, { text: "¿esta historia entra al sprint?" }], { size: 12, color: C.muted }),
    text(0.6, 4.65, 8.8, 0.3, "Vota el Equipo Scrum · el Product Owner solo aclara dudas · solo se estiman historias que cumplen la definición de listo", { size: 11, color: C.muted }),
  ],
});

// 3 · Los cinco niveles
const levels = [
  "No estoy de acuerdo y tengo grandes inquietudes",
  "No estoy de acuerdo; quiero hablar de temas menores",
  "No estoy seguro, pero me sumo al grupo",
  "Estoy de acuerdo; quiero comentar temas menores",
  "Estoy totalmente de acuerdo",
];
const lvEls = [
  text(0.6, 1.3, 3.4, 0.3, "NO ESTOY DE ACUERDO", { size: 11, bold: true, color: C.no, spacing: 1, align: "center" }),
  text(4.2, 1.3, 1.6, 0.3, "DUDA", { size: 11, bold: true, color: C.doubt, spacing: 1, align: "center" }),
  text(6.0, 1.3, 3.4, 0.3, "DE ACUERDO", { size: 11, bold: true, color: C.yes, spacing: 1, align: "center" }),
];
levels.forEach((lab, i) => {
  const cx = 0.6 + i * 1.8, n = i + 1;
  lvEls.push(...hand(cx + 0.35, 1.8, 0.9, n, VOTE[n]));
  lvEls.push(text(cx, 2.95, 1.6, 0.55, String(n), { size: 30, bold: true, color: VOTE[n], align: "center" }));
  lvEls.push(text(cx, 3.5, 1.6, 0.95, lab, { size: 13, align: "center", valign: "top" }));
});
lvEls.push(text(0.6, 4.65, 8.8, 0.3, [{ text: "Sugerencia: ", bold: true }, { text: "si alguien muestra 1 o 2, se escucha su razón antes de cerrar." }], { size: 13, color: C.ink }));
S.push({
  title: "Qué significa cada dedo",
  notes: "Anthony. Estos son los cinco niveles tal como los define el SBOK cuando la técnica se usa para formar consenso. Con 1 o 2 la persona no está de acuerdo; con 3 tiene dudas pero acompaña al grupo; con 4 o 5 está de acuerdo. La sugerencia final es del equipo, no del libro.",
  els: lvEls,
});

// 4 · Paso a paso
const steps = [
  ["Presentar", "El PO lee la historia y sus criterios de aceptación. Se aclaran dudas."],
  ["Votar a la vez", "«3, 2, 1… ¡mano!» Todos muestran los dedos al mismo tiempo."],
  ["Explicar extremos", "Quien votó más alto y quien votó más bajo explican por qué."],
  ["Re-votar o decidir", "Nueva ronda hasta acercarse. Se anota el valor acordado."],
];
const stEls = [];
steps.forEach(([h, b], i) => {
  const x = 0.6 + i * 2.27;
  stEls.push(box(x, 1.35, 2.0, 2.8, C.soft, { r: 0.18 }));
  stEls.push(circle(x + 0.25, 1.6, 0.55, C.accent));
  stEls.push(text(x + 0.25, 1.6, 0.55, 0.55, String(i + 1), { size: 20, bold: true, color: C.white, align: "center", valign: "middle" }));
  stEls.push(text(x + 0.25, 2.3, 1.6, 0.62, h, { size: 17, bold: true, valign: "bottom" }));
  stEls.push(text(x + 0.25, 3.05, 1.6, 1.0, b, { size: 13, valign: "top" }));
});
stEls.push(box(0.6, 4.35, 8.8, 0.62, C.accentSoft, { r: 0.12 }));
stEls.push(text(0.85, 4.35, 8.4, 0.62, "Lo valioso no es solo el número: es la conversación que abren los votos distintos.", { size: 15, bold: true, valign: "middle" }));
S.push({
  title: "Cómo se usa, en 4 pasos",
  notes: "Luis. 1) El PO presenta la historia. 2) Todos votan al mismo tiempo para que nadie se deje llevar por el voto del otro. 3) Los votos más alto y más bajo explican su razón: ahí aparece la información que faltaba. 4) Se vuelve a votar o se toma la decisión. El SBOK destaca que el valor está en el debate, no solo en el consenso.",
  els: stEls,
});

// 5 · Ejemplo con NewBit
function voter(x, y, n, name) {
  return [
    ...hand(x, y, 0.42, n, VOTE[n]),
    text(x + 0.48, y + 0.02, 0.4, 0.5, String(n), { size: 24, bold: true, color: VOTE[n], valign: "middle" }),
    text(x - 0.1, y + 0.55, 0.9, 0.25, name, { size: 10, color: C.muted }),
  ];
}
S.push({
  title: "Ejemplo: HU07 «Procesar el clip con ConvLSTM»",
  notes: "Luis. Simulación con una historia real de nuestras épicas (FGAP040, épica EP04). Izquierda: estimación. Anthony vota 2 porque creía que solo era mostrar el resultado; Luis vota 5 porque hay que armar secuencias de frames y entrenar el ConvLSTM. Tras explicarse, los dos votan 4: historia grande. Derecha: decisión con los tres. Hay dos votos de 2, así que no se cierra: se decide dividir HU07. Opcional: repetir la votación con el aula.",
  els: [
    text(0.6, 1.12, 8.8, 0.3, "Épica EP04 · Clasificación espacio-temporal (ConvLSTM) · simulación del equipo NewBit", { size: 12, color: C.muted }),
    // Estimar
    box(0.6, 1.55, 4.3, 3.4, C.soft, { r: 0.18 }),
    text(0.85, 1.7, 3.8, 0.35, "1 · Estimar la historia", { size: 16, bold: true }),
    text(0.85, 2.03, 3.8, 0.25, "Vota el equipo de desarrollo", { size: 11, color: C.muted }),
    text(0.85, 2.55, 0.8, 0.3, "Ronda 1", { size: 12, bold: true }),
    ...voter(1.75, 2.4, 2, "Anthony"),
    ...voter(2.75, 2.4, 5, "Luis"),
    text(3.7, 2.45, 1.1, 0.5, "Muy distintos", { size: 11, bold: true, color: C.no, valign: "middle" }),
    text(0.85, 3.25, 3.9, 0.55, [
      { text: "Luis: «Hay que armar secuencias y entrenar ConvLSTM».", breakLine: true },
      { text: "Anthony: «Creí que solo era mostrar el resultado»." },
    ], { size: 11, italic: true }),
    text(0.85, 4.1, 0.8, 0.3, "Ronda 2", { size: 12, bold: true }),
    ...voter(1.75, 3.95, 4, "Anthony"),
    ...voter(2.75, 3.95, 4, "Luis"),
    text(3.7, 4.0, 1.1, 0.5, "Acuerdo: 4 (grande)", { size: 11, bold: true, color: C.yes, valign: "middle" }),
    // Decidir
    box(5.1, 1.55, 4.3, 3.4, C.soft, { r: 0.18 }),
    text(5.35, 1.7, 3.8, 0.35, "2 · Decidir en equipo", { size: 16, bold: true }),
    text(5.35, 2.03, 3.8, 0.25, "Votan los tres", { size: 11, color: C.muted }),
    box(5.35, 2.4, 3.8, 0.5, C.white, { r: 0.1 }),
    text(5.5, 2.4, 3.6, 0.5, "¿HU07 entra completa al Sprint 3?", { size: 14, bold: true, valign: "middle" }),
    ...voter(5.55, 3.1, 2, "Albert"),
    ...voter(6.75, 3.1, 3, "Anthony"),
    ...voter(7.95, 3.1, 2, "Luis"),
    text(5.35, 4.0, 3.8, 0.75, [
      { text: "Dos votos de 2: hay dudas serias.", breakLine: true },
      { text: "Decisión: dividir HU07 en dos historias.", bold: true },
    ], { size: 12 }),
  ],
});

// 6 · Las 12 historias de NewBit estimadas
const HUS = [
  ["HU01", "Cargar un video industrial", 1, "EP01"], ["HU02", "Fragmentar el video en frames", 2, "EP01"],
  ["HU03", "Detectar operarios con YOLOv8", 4, "EP02"], ["HU04", "Descartar frames sin operarios", 2, "EP02"],
  ["HU05", "Agrupar frames en clips", 3, "EP03"], ["HU06", "Descartar clips muy cortos", 2, "EP03"],
  ["HU07", "Procesar el clip con ConvLSTM", 5, "EP04"], ["HU08", "Clasificar y tipificar conducta", 3, "EP04"],
  ["HU09", "Ver el video con recuadro", 4, "EP05"], ["HU10", "Activar alerta de riesgo", 2, "EP05"],
  ["HU11", "Ajustar umbral de YOLOv8", 1, "EP06"], ["HU12", "Ver log de tiempos y ahorro", 2, "EP06"],
];
const SIZE_ALPHA = [null, 72, 55, 35, 15, 0];
const huEls = [text(0.6, 1.12, 8.8, 0.3, "Nuestras 12 historias (FGAP040, épicas EP01–EP06) · tamaño acordado tras votar · 1 = muy pequeña, 5 = muy grande", { size: 12, color: C.muted })];
HUS.forEach(([id, name, n, ep], i) => {
  const x = 0.6 + (i % 4) * 2.25, y = 1.5 + Math.floor(i / 4) * 1.12;
  huEls.push(box(x, y, 2.05, 1.0, C.soft, { r: 0.14 }));
  huEls.push(text(x + 0.15, y + 0.1, 1.3, 0.25, [{ text: id, bold: true }, { text: " · " + ep }], { size: 11, color: C.accent }));
  huEls.push(text(x + 0.15, y + 0.36, 1.32, 0.58, name, { size: 11, valign: "top" }));
  huEls.push(box(x + 1.5, y + 0.25, 0.44, 0.44, C.accent, { r: 0.22, alpha: SIZE_ALPHA[n] }));
  huEls.push(text(x + 1.5, y + 0.25, 0.44, 0.44, String(n), { size: 16, bold: true, color: n >= 3 ? C.white : C.ink, align: "center", valign: "middle" }));
});
huEls.push(text(0.6, 4.88, 8.8, 0.28, [{ text: "Lectura: ", bold: true }, { text: "la EP04 (ConvLSTM) concentra el mayor esfuerzo; las historias de carga y configuración son pequeñas. Votos consensuados." }], { size: 11, color: C.muted }));
S.push({
  title: "Estimamos las 12 historias de NewBit",
  notes: "Anthony. Aplicamos el puño de cinco a nuestras doce historias de usuario. Cada número es el tamaño acordado después de votar y de que los extremos explicaran su razón. La más grande es la HU07, procesar el clip con ConvLSTM, que vimos en el ejemplo anterior. Las de carga y configuración son pequeñas. Los puntos se calibran para 4 sprints equilibrados de unos 8 puntos.",
  els: huEls,
});

// 7 · Decidir qué entra a cada sprint
const DEC = [
  ["Sprint 1", "¿HU01 a HU03 entran al Sprint 1 (7 pts)?", [5, 4, 5], "Aprobado", C.yes],
  ["Sprint 2", "¿HU04, HU05, HU06 y HU11 al Sprint 2 (8 pts)?", [4, 4, 5], "Aprobado", C.yes],
  ["Sprint 4", "¿HU09, HU10 y HU12 quedan para el Sprint 4 (8 pts)?", [4, 5, 4], "Aprobado", C.yes],
];
const decEls = [text(0.6, 1.12, 8.8, 0.3, "Votan los tres: Albert (PO), Anthony y Luis · la EP04 va en el Sprint 3, dividida (ver ejemplo)", { size: 12, color: C.muted })];
DEC.forEach(([sp, q, votes, res, col], i) => {
  const y = 1.52 + i * 1.12;
  decEls.push(box(0.6, y, 4.55, 0.92, C.soft, { r: 0.14 }));
  decEls.push(text(0.8, y + 0.1, 1.2, 0.25, sp.toUpperCase(), { size: 10, bold: true, color: C.accent, spacing: 1 }));
  decEls.push(text(0.8, y + 0.34, 4.2, 0.5, q, { size: 13, bold: true, valign: "top" }));
  votes.forEach((n, k) => decEls.push(...voter(5.45 + k * 0.92, y + 0.08, n, ["Albert", "Anthony", "Luis"][k])));
  decEls.push(box(8.2, y + 0.16, 1.2, 0.6, col, { r: 0.12, alpha: 82 }));
  decEls.push(text(8.25, y + 0.16, 1.1, 0.6, res, { size: 10.5, bold: true, color: C.ink, align: "center", valign: "middle" }));
});
decEls.push(text(0.6, 4.88, 8.8, 0.28, [{ text: "Regla del equipo: ", bold: true }, { text: "si hay algún 1 o 2, se discute antes de cerrar. Votos simulados." }], { size: 11, color: C.muted }));
S.push({
  title: "Decidimos en equipo qué entra a cada sprint",
  notes: "Luis. Usamos el puño de cinco para decidir. Primera: la EP01 entra completa al Sprint 1, votos 5, 4 y 5, aprobado. Segunda: la EP02 y la EP03 juntas en el Sprint 2; hubo dos votos de 3, así que se acepta pero con una revisión a mitad del sprint. Tercera: la EP05 y la EP06 quedan para el Sprint 4, aprobado. La EP04 va en el Sprint 3 y la dividimos, como vimos en el ejemplo. Votos simulados.",
  els: decEls,
});

// 6 · Comparación y cierre
S.push({
  title: "¿Cuándo usar el puño de cinco?",
  notes: "Albert. Comparación con las otras tres técnicas de estimación del SBOK. El puño de cinco es la más rápida y además sirve para decidir; Planning Poker da más precisión. Cierre: lo importante es que los votos extremos expliquen su razón. Preguntas.",
  els: [
    { t: "table", x: 0.6, y: 1.3, w: 8.8, colW: [2.0, 3.6, 3.2], rowH: 0.42, size: 13,
      rows: [
        ["Técnica", "Cómo se vota", "Mejor para"],
        ["Puño de cinco", "Dedos del 1 al 5, todos a la vez", "Estimar rápido y decidir por consenso"],
        ["Planning Poker", "Cartas numeradas; se repite hasta el consenso", "Estimar en puntos con más precisión"],
        ["Wideband Delphi", "Estimaciones anónimas en rondas", "Evitar que unos influyan en otros"],
        ["Afinidad (tallas)", "Ordenar historias en la pared por tamaño", "Estimar muchas historias a la vez"],
      ], highlight: 1 },
    box(0.6, 3.75, 8.8, 0.8, C.accentSoft, { r: 0.12 }),
    ...hand(0.85, 3.83, 0.53, 5, C.accent),
    text(1.6, 3.75, 7.6, 0.8, "Simple, rápido y sin materiales. La clave: que los votos extremos expliquen su razón.", { size: 15, bold: true, valign: "middle" }),
    text(0.6, 4.7, 8.8, 0.3, [
      { text: "Fuente: SCRUMstudy. (2022). " },
      { text: "Guía de los fundamentos de Scrum (Guía del SBOK®)", italic: true },
      { text: " (4.ª ed.), 9.2.2.1, pp. 193–195." },
    ], { size: 10, color: C.muted }),
  ],
});

// ---------- salida PPTX ----------
async function buildPptx() {
  const pres = new pptxgen();
  pres.layout = "LAYOUT_16x9";
  pres.title = "Puño de cinco (Fist of Five)";
  pres.author = "Grupo D3 (Laboratorio D · Equipo 3)";
  pres.theme = { headFontFace: FONT, bodyFontFace: FONT };
  pres.defineSlideMaster({ title: "PORTADA", background: { color: C.ink } });
  pres.defineSlideMaster({
    title: "CONTENIDO", background: { color: C.white },
    objects: [
      { placeholder: { options: { name: "title", type: "title", x: 0.6, y: 0.4, w: 8.8, h: 0.7, fontFace: FONT, fontSize: 30, bold: true, color: C.ink, margin: 0, align: "left", valign: "middle" }, text: "" } },
      { text: { text: "Puño de cinco · Grupo D3", options: { x: 0.6, y: 5.2, w: 5, h: 0.25, fontFace: FONT, fontSize: 9, color: C.muted, margin: 0 } } },
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
        slide.addText(e.runs.map(r => ({ text: r.text, options: { bold: r.bold, italic: r.italic, breakLine: r.breakLine } })), {
          x: e.x, y: e.y, w: e.w, h: e.h, objectName: name, isTextBox: true, margin: 0,
          fontFace: FONT, fontSize: e.size, color: e.color || C.ink, bold: !!e.bold, italic: !!e.italic,
          align: e.align || "left", valign: e.valign || "top", ...(e.spacing ? { charSpacing: e.spacing } : {}),
        });
      } else if (e.t === "table") {
        const rows = e.rows.map((row, ri) => row.map((cell, ci) => ({
          text: cell, options: {
            bold: ri === 0 || ci === 0, color: ri === 0 ? C.white : C.ink,
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
    const runs = e.runs.map(r => `<span style="${r.bold ? "font-weight:700;" : ""}${r.italic ? "font-style:italic;" : ""}">${esc(r.text)}</span>${r.breakLine ? "<br>" : ""}`).join("");
    const jc = { top: "flex-start", middle: "center", bottom: "flex-end" }[e.valign || "top"];
    return `<div class="tx" style="${pos};font-size:${pt(e.size)};color:#${e.color || (dark ? C.white : C.ink)};font-weight:${e.bold ? 700 : 400};${e.italic ? "font-style:italic;" : ""}text-align:${e.align || "left"};justify-content:${jc}${e.spacing ? `;letter-spacing:${pt(e.spacing)}` : ""}"><div>${runs}</div></div>`;
  }
  if (e.t === "table") {
    const cols = e.colW.map(w => `<col style="width:${px(w)}">`).join("");
    const body = e.rows.map((row, ri) => `<tr style="height:${px(e.rowH)};background:#${ri === 0 ? C.ink : ri === e.highlight ? C.accentSoft : C.white};color:#${ri === 0 ? C.white : C.ink}">${row.map((c, ci) => `<td style="font-weight:${ri === 0 || ci === 0 ? 700 : 400}">${esc(c)}</td>`).join("")}</tr>`).join("");
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
    const foot = s.dark ? "" : `<div class="tx foot" style="left:${px(0.6)};top:${px(5.2)};width:${px(5)};height:${px(0.25)};font-size:${pt(9)}"><div>Puño de cinco · Grupo D3</div></div><div class="tx foot" style="left:${px(8.9)};top:${px(5.2)};width:${px(0.5)};height:${px(0.25)};font-size:${pt(9)};text-align:right"><div>${i + 1}</div></div>`;
    return `<section class="slide${s.dark ? " dark" : ""}" aria-label="Diapositiva ${i + 1}">${title}${s.els.map(e => htmlEl(e, s.dark)).join("")}${foot}<aside class="notes">${esc(s.notes)}</aside></section>`;
  }).join("\n");
  const html = `<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Puño de cinco</title>
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
