// Genera PPT_Producto_Unidad_1_NewBit.pptx: presentación del Producto de la Unidad I de NewBit (v3).
// Uso: node generar_ppt.js [carpeta_con_node_modules]   (requiere pptxgenjs@3.12.0)
//
// Estilo: minimalismo funcional (láminas de contenido claras, tarjetas con bordes sutiles, íconos de
// línea) + minimalismo editorial (portadas de sección oscuras, titulares grandes, pocos elementos).
// Lienzo 13.333 × 7.5 in (16:9). Calibri Light para titulares y Calibri para texto.
// Narrativa de pitch: problema → idea → cómo funciona en 4 pasos → beneficio → cómo lo construimos con
// Scrum (Guía SBOK) → entregables semana a semana → lo que viene. Cifras iguales al informe.
const path = require("path");
const modDir = process.argv[2];
const pptxgen = require(modDir ? path.join(modDir, "node_modules", "pptxgenjs") : "pptxgenjs");

const OUT = path.join(__dirname, "PPT_Producto_Unidad_1_NewBit.pptx");
const IMG = (f) => path.join(__dirname, "img", f);
const ICO = (n, c) => path.join(__dirname, "img", "iconos", `${n}-${c}.png`);
const TIT = "Calibri Light", TXT = "Calibri";
const C = {
  papel: "FAFAF9", tarjeta: "FFFFFF", borde: "E7E5E4", tinta: "1A1A1A", tinta2: "57534E", gris: "8A8984",
  azul: "3E63DD", azulSuave: "EEF2FF", ambar: "C2410C", ambarSuave: "FFF4ED", verde: "2F855A", verdeSuave: "EEF8F2",
  noche: "111111", nocheBorde: "2B2B2A", claro: "F5F5F4", claro2: "A8A29E",
};
const W = 13.333, M = 0.8; // ancho y margen

const pptx = new pptxgen();
pptx.layout = "LAYOUT_WIDE";
pptx.author = "Grupo D3 · Ingeniería de Software II · UNS";
pptx.title = "NewBit · Producto de la Unidad I";

// ---------- primitivas ----------
let nro = 0;
const T = (s, txt, x, y, w, h, o = {}) =>
  s.addText(txt, { x, y, w, h, fontFace: TXT, fontSize: 16, color: C.tinta, valign: "top", margin: 0, ...o });
const icono = (s, n, c, x, y, d = 0.42) => s.addImage({ path: ICO(n, c), x, y, w: d, h: d });
function tarjeta(s, x, y, w, h, o = {}) {
  s.addShape(pptx.ShapeType.roundRect, { x, y, w, h, rectRadius: 0.08,
    fill: { color: o.fill || C.tarjeta }, line: { color: o.borde || C.borde, width: o.grosor || 0.75 } });
}
function linea(s, x1, y1, x2, y2, color = C.borde, ancho = 0.75, o = {}) {
  s.addShape(pptx.ShapeType.line, { x: Math.min(x1, x2), y: Math.min(y1, y2), w: Math.abs(x2 - x1), h: Math.abs(y2 - y1),
    flipH: x2 < x1, line: { color, width: ancho, ...o } });
}
const flecha = (s, x1, y, x2, color = C.gris) => linea(s, x1, y, x2, y, color, 1, { endArrowType: "triangle" });
// Fragmentos con **negrita**
const rico = (str, base = {}) => str.split(/(\*\*[^*]+\*\*)/).filter(Boolean).map((p) =>
  p.startsWith("**") ? { text: p.slice(2, -2), options: { ...base, bold: true } } : { text: p, options: base });

function base(oscura, antetitulo, titulo, notas, o = {}) {
  const s = pptx.addSlide();
  nro += 1;
  s.background = { color: oscura ? C.noche : C.papel };
  const tinta = oscura ? C.claro : C.tinta, sec = oscura ? C.claro2 : C.gris;
  if (antetitulo) T(s, antetitulo.toUpperCase(), M, 0.55, 11, 0.3, { fontSize: 11, color: oscura ? C.claro2 : C.azul, bold: true, charSpacing: 1.5 });
  if (titulo) T(s, titulo, M, 0.85, o.anchoTitulo || 11.7, o.altoTitulo || 0.9, { fontFace: TIT, fontSize: o.tamTitulo || 34, color: tinta });
  if (!o.sinPie) {
    T(s, "NewBit", M, 6.95, 3, 0.25, { fontSize: 10, color: sec, bold: true });
    T(s, "Producto de la Unidad I · Grupo D3", M + 0.7, 6.95, 5, 0.25, { fontSize: 10, color: sec });
    T(s, String(nro).padStart(2, "0"), W - M - 0.8, 6.95, 0.8, 0.25, { fontSize: 10, color: sec, align: "right" });
  }
  if (notas) s.addNotes(notas);
  return s;
}
const clara = (a, t, n, o) => base(false, a, t, n, o);
const oscura = (a, t, n, o) => base(true, a, t, n, o);
const fuente = (s, txt, oscuro = false) => T(s, txt, M, 6.55, W - 2 * M, 0.3, { fontSize: 10, color: oscuro ? C.claro2 : C.gris });

// ===================================================================== PARTE 1 · EL PITCH
// 01 · Portada
{
  const s = clara(null, null, "Presentación del Producto de la Unidad I. Abrir con la frase grande: NewBit busca que las cámaras que ya existen avisen antes de que ocurra un accidente. Presentar al equipo y al docente.", { sinPie: true });
  s.addImage({ path: IMG("logo-uns.png"), x: M, y: 0.55, w: 0.62, h: 0.81 });
  T(s, [{ text: "Universidad Nacional del Santa", options: { bold: true, breakLine: true } },
    { text: "Ingeniería de Software II · Producto de la Unidad I" }], M + 0.8, 0.68, 8, 0.6, { fontSize: 12, color: C.tinta2 });
  T(s, "NewBit", M, 1.85, 11, 1.4, { fontFace: TIT, fontSize: 88, color: C.tinta });
  T(s, "Que las cámaras avisen antes del accidente.", M, 3.25, 11, 0.8, { fontFace: TIT, fontSize: 32, color: C.tinta2 });
  T(s, "Sistema web con visión artificial para la detección de actos inseguros en áreas operativas de manufactura metalmecánica · PY-NB-001",
    M, 4.1, 10.5, 0.6, { fontSize: 13, color: C.gris });
  linea(s, M, 5.25, W - M, 5.25);
  [["Albert Chumacero Chávarry", "Product Owner"], ["Anthony Lopez Yrribarren", "Scrum Master y Developer"],
   ["Luis Salazar Diaz", "Developer"], ["Dr. Ing. Alfredo Daza Vergaray", "Docente"]].forEach(([n, r], i) => {
    const x = M + i * 2.95;
    T(s, n, x, 5.45, 2.85, 0.3, { fontSize: 13, bold: true });
    T(s, r, x, 5.78, 2.85, 0.3, { fontSize: 12, color: C.gris });
  });
  T(s, "Grupo D3 · Nuevo Chimbote, octubre de 2026", M, 6.75, 8, 0.3, { fontSize: 11, color: C.gris });
}

// 02 · El problema (enunciado)
{
  const s = oscura("El problema", null, "Las cámaras ya están instaladas y graban todo el día, pero nadie revisa ese video a tiempo. El inspector de SST pasa por turnos; lo que ocurre entre ronda y ronda queda grabado y olvidado.");
  T(s, "Las cámaras graban.", M, 1.6, 11.5, 1.2, { fontFace: TIT, fontSize: 64, color: C.claro });
  T(s, "Nadie las mira.", M, 2.75, 11.5, 1.2, { fontFace: TIT, fontSize: 64, color: C.claro2 });
  T(s, "En un taller metalmecánico, el inspector de seguridad recorre la planta por turnos. Lo que pasa entre una ronda y otra queda grabado, pero nadie lo revisa a tiempo.",
    M, 4.45, 8.2, 1.2, { fontSize: 18, color: C.claro2 });
}

// 03 · Una escena
{
  const s = clara("El problema", "Una escena de todos los días",
    "Contar la escena como una historia. Un operario cruza fuera de la vía peatonal, donde circulan montacargas. Nadie lo ve. Al final del turno hay ocho horas de video sin revisar. Al día siguiente, el riesgo se repite.");
  const pasos = [
    ["10:42", "Un operario cruza fuera de la vía peatonal, por donde pasan montacargas.", C.ambar],
    ["10:43", "Sigue trabajando. Nadie lo vio; la cámara sí lo grabó.", C.tinta2],
    ["18:00", "Termina el turno: ocho horas de video que nadie revisará.", C.tinta2],
    ["Mañana", "El mismo riesgo se repite, hasta que un día no es solo un riesgo.", C.ambar],
  ];
  linea(s, M + 0.1, 2.75, W - M - 0.1, 2.75, C.borde, 1.25);
  pasos.forEach(([h, d, col], i) => {
    const x = M + i * 2.95;
    s.addShape(pptx.ShapeType.ellipse, { x: x + 0.02, y: 2.63, w: 0.24, h: 0.24, fill: { color: col }, line: { color: col } });
    T(s, h, x, 3.1, 2.7, 0.55, { fontFace: TIT, fontSize: 30, color: C.tinta });
    T(s, d, x, 3.7, 2.6, 1.2, { fontSize: 16, color: C.tinta2 });
  });
  T(s, rico("El acto inseguro **existe**, pero se detecta **tarde o nunca**."), M, 5.45, 11, 0.5, { fontFace: TIT, fontSize: 24 });
  fuente(s, "Escena ilustrativa. Conductas tomadas del conjunto de datos de Önal y Dandıl (2024).");
}

// 04 · A quién le duele
{
  const s = clara("El problema", "¿A quién le duele?",
    "Tres personas del caso, con nombre. Mariana no puede revisar horas de video. Lucía mira muchas cámaras y algo se le escapa. Ricardo necesita datos para decidir dónde invertir.");
  [["Mariana Torres", "Supervisora de SST", "No puede revisar horas de video. Necesita saber a tiempo qué pasó, dónde y cuándo."],
   ["Lucía Ramos", "Operadora de monitoreo", "Mira muchas cámaras a la vez. Es fácil que algo se le pase."],
   ["Ricardo Salcedo", "Gerente general", "Necesita datos claros para decidir dónde invertir en prevención."]].forEach(([n, r, d], i) => {
    const x = M + i * 3.95;
    tarjeta(s, x, 2.15, 3.65, 3.3);
    icono(s, "persona", "ink", x + 0.35, 2.45, 0.5);
    T(s, n, x + 0.35, 3.15, 3.0, 0.4, { fontSize: 20, bold: true });
    T(s, r, x + 0.35, 3.55, 3.0, 0.35, { fontSize: 14, color: C.gris });
    T(s, d, x + 0.35, 4.05, 3.0, 1.2, { fontSize: 16, color: C.tinta2 });
  });
  fuente(s, "Perfiles del caso académico, definidos en el formato FGAP030 (Roles y prototipos).");
}

// 05 · La idea
{
  const s = oscura("La idea", null, "La idea en una sola frase. Pausa después de decirla.");
  T(s, "NewBit revisa el video por ti", M, 1.55, 11.7, 1.0, { fontFace: TIT, fontSize: 54, color: C.claro });
  T(s, "y te muestra solo los segundos", M, 2.5, 11.7, 1.0, { fontFace: TIT, fontSize: 54, color: C.claro2 });
  T(s, "que importan.", M, 3.45, 11.7, 1.0, { fontFace: TIT, fontSize: 54, color: C.claro2 });
  T(s, "Sin cámaras nuevas: usa el video que la planta ya graba.", M, 4.85, 9, 0.5, { fontSize: 18, color: C.claro2 });
}

// 06 · Cómo funciona en 4 pasos
{
  const s = clara("Cómo funciona", "Cuatro pasos, sin tecnicismos",
    "Explicar cada paso como si fuera para alguien que no sabe de tecnología. Abajo, en gris, está el nombre técnico por si alguien pregunta. Cerrar con la analogía del asistente.");
  const p = [
    ["01", "video", "Subes el video", "Cargas los clips que tus cámaras ya graban.", "archivos .mp4 o .avi, por lotes"],
    ["02", "buscar", "Encuentra a las personas", "Revisa cada imagen y marca dónde hay operarios. Lo que no tiene a nadie, lo descarta.", "detector YOLOv8"],
    ["03", "secuencia", "Entiende lo que hacen", "No mira una foto suelta: mira la secuencia, como un video corto, para saber qué conducta es.", "red ConvLSTM"],
    ["04", "alerta", "Te avisa con la prueba", "Si la conducta es insegura, alerta y te muestra el clip. La decisión es tuya.", "alerta y registro"],
  ];
  p.forEach(([n, ic, t, d, tec], i) => {
    const x = M + i * 2.98;
    tarjeta(s, x, 2.05, 2.75, 3.35);
    T(s, n, x + 0.3, 2.3, 1, 0.35, { fontSize: 13, bold: true, color: C.azul });
    icono(s, ic, "ink", x + 2.0, 2.25, 0.45);
    T(s, t, x + 0.3, 2.85, 2.3, 0.75, { fontSize: 19, bold: true });
    T(s, d, x + 0.3, 3.6, 2.25, 1.25, { fontSize: 14, color: C.tinta2 });
    T(s, "Por dentro: " + tec, x + 0.3, 4.92, 2.3, 0.3, { fontSize: 11, color: C.gris });
    if (i < 3) flecha(s, x + 2.78, 3.72, x + 2.95, C.gris);
  });
  T(s, rico("Es como un asistente que ve **todo** el video y solo te llama cuando algo merece tu atención."),
    M, 5.8, 11.5, 0.5, { fontFace: TIT, fontSize: 22, color: C.tinta2 });
}

// 07 · Qué detecta
{
  const s = clara("Primera versión", "Qué detecta, por ahora",
    "Dos conductas de alto riesgo en un taller. El sistema aprende la diferencia viendo también el caso seguro. La arquitectura deja espacio para agregar más conductas.");
  T(s, "CONDUCTA INSEGURA · ALERTA", M + 1.2, 2.0, 5, 0.3, { fontSize: 11, bold: true, color: C.ambar, charSpacing: 1 });
  T(s, "CASO SEGURO · CONTRASTE", M + 6.55, 2.0, 5, 0.3, { fontSize: 11, bold: true, color: C.verde, charSpacing: 1 });
  [["via", "Caminar fuera de la vía peatonal", "Caminar por la vía peatonal"],
   ["tablero", "Dejar abierto el tablero eléctrico", "Cerrar el tablero tras la intervención"]].forEach(([ic, mal, bien], i) => {
    const y = 2.45 + i * 1.65;
    icono(s, ic, "ink", M, y + 0.35, 0.6);
    tarjeta(s, M + 1.2, y, 5.1, 1.35, { fill: C.ambarSuave, borde: "F5D0BD" });
    icono(s, "riesgo", "ambar", M + 1.5, y + 0.45, 0.42);
    T(s, mal, M + 2.15, y + 0.45, 4, 0.5, { fontSize: 18 });
    tarjeta(s, M + 6.55, y, 5.1, 1.35, { fill: C.verdeSuave, borde: "C7E6D4" });
    icono(s, "seguro", "verde", M + 6.85, y + 0.45, 0.42);
    T(s, bien, M + 7.5, y + 0.45, 4, 0.5, { fontSize: 18 });
  });
  fuente(s, "Conductas «Safe Walkway Violation» y «Opened Panel Cover» del conjunto de datos público de Önal y Dandıl (2024), licencia CC BY 4.0.");
}

// 08 · Por qué creemos que funciona
{
  const s = clara("Evidencia", "¿Por qué creemos que funciona?",
    "NewBit no parte de cero. Se basa en Unsafe-Net, una investigación publicada que probó esta idea con video real de una fábrica. Aclarar que el 95.81 % es de los autores, en su conjunto de datos; NewBit fijará sus propias metas en el Sprint 3.");
  T(s, "95.81 %", M, 1.95, 6, 1.4, { fontFace: TIT, fontSize: 96, color: C.tinta });
  T(s, "exactitud promedio por clase de Unsafe-Net en su conjunto de datos (Önal y Dandıl, 2025).", M, 3.45, 5.6, 0.9, { fontSize: 16, color: C.tinta2 });
  [["reloj", "39 días de video", "grabados en una fábrica real, con dos cámaras."],
   ["libro", "Datos públicos", "el mismo conjunto de datos que NewBit reutiliza, con licencia CC BY 4.0."],
   ["capas", "De objetos a conductas", "en el Perú ya se detecta EPP en imágenes (PUCP, UCV, UPN); NewBit reconoce acciones en video."]].forEach(([ic, t, d], i) => {
    const y = 2.0 + i * 1.3;
    icono(s, ic, "ink", 7.3, y + 0.05, 0.45);
    T(s, t, 8.0, y, 4.5, 0.4, { fontSize: 18, bold: true });
    T(s, d, 8.0, y + 0.42, 4.5, 0.75, { fontSize: 14, color: C.tinta2 });
  });
  fuente(s, "Cifras reportadas por los autores en su propio estudio; no son una promesa para NewBit. Las metas propias se fijarán con la línea base del Sprint 3.");
}

// 09 · Qué gana cada uno
{
  const s = clara("Beneficio", "Qué gana cada uno",
    "El beneficio contado por persona. Sin cifras inventadas: lo que gana cada rol en su día a día.");
  [["reloj", "Supervisora de SST", "Menos horas mirando video. La evidencia llega lista para actuar."],
   ["alerta", "Operadora de monitoreo", "Ve solo lo importante y confirma o descarta en un clic."],
   ["grafico", "Gerencia", "Reportes por tipo de conducta, zona y semana para decidir dónde invertir."],
   ["escudo", "Trabajadores", "Prevención sin vigilancia: nadie es identificado por su rostro."]].forEach(([ic, t, d], i) => {
    const x = M + (i % 2) * 5.95, y = 2.0 + Math.floor(i / 2) * 2.05;
    tarjeta(s, x, y, 5.7, 1.8);
    icono(s, ic, "azul", x + 0.35, y + 0.4, 0.5);
    T(s, t, x + 1.15, y + 0.35, 4.3, 0.4, { fontSize: 19, bold: true });
    T(s, d, x + 1.15, y + 0.8, 4.3, 0.85, { fontSize: 15, color: C.tinta2 });
  });
}

// 10 · Lo que no hace
{
  const s = clara("Límites claros", "Lo que NewBit no hace",
    "Decir lo que no hace genera confianza. No reconoce rostros, no reemplaza al supervisor y no promete reducir accidentes sin medirlo.");
  [["sin-rostro", "No reconoce rostros", "ni identifica a las personas. Analiza conductas, no quién las hace."],
   ["persona", "No reemplaza al supervisor", "Le entrega evidencia; la decisión siempre es humana."],
   ["grafico", "No promete sin medir", "No afirma que reducirá accidentes hasta tener evidencia propia."],
   ["video", "No instala hardware", "Procesa el video que ya existe; no requiere cámaras ni sensores nuevos."]].forEach(([ic, t, d], i) => {
    const y = 1.95 + i * 1.12;
    icono(s, "no", "gris", M, y + 0.08, 0.42);
    T(s, t, M + 0.7, y, 4.2, 0.5, { fontSize: 20, bold: true });
    T(s, d, M + 4.9, y + 0.05, 6.8, 0.6, { fontSize: 17, color: C.tinta2 });
    if (i < 3) linea(s, M, y + 0.88, W - M, y + 0.88);
  });
}

// ===================================================================== PARTE 2 · SCRUM
// 11 · Portada de sección
{
  const s = oscura("Parte 2", null, "Pasamos de qué es NewBit a cómo lo construimos. Todo sigue la Guía SBOK, el libro base del curso.");
  T(s, "Cómo lo construimos:", M, 2.0, 11.5, 1.0, { fontFace: TIT, fontSize: 54, color: C.claro });
  T(s, "Scrum, según la Guía SBOK", M, 3.0, 11.5, 1.0, { fontFace: TIT, fontSize: 54, color: C.claro2 });
  T(s, "SCRUMstudy (2022). Guía de los fundamentos de Scrum, 4.ª ed.", M, 4.6, 9, 0.4, { fontSize: 16, color: C.claro2 });
}

// 12 · Scrum en una lámina
{
  const s = clara("Scrum en una lámina", "Tres roles, un ciclo que se repite",
    "Tres roles sin jerarquía entre ellos (p. 42). Trabajamos en sprints de dos semanas; cada sprint tiene cuatro reuniones con tiempo fijo (pp. 35–37). Somos tres; la guía recomienda de seis a diez, y ese riesgo está en el acta.");
  [["Product Owner", "Albert", "Decide qué se construye primero y acepta el trabajo."],
   ["Scrum Master", "Anthony", "Cuida el proceso y quita los obstáculos."],
   ["Equipo Scrum", "Anthony y Luis", "Estima, construye y prueba."]].forEach(([r, q, d], i) => {
    const y = 2.0 + i * 1.4;
    tarjeta(s, M, y, 5.2, 1.2);
    T(s, [{ text: r, options: { bold: true } }, { text: "  ·  " + q, options: { color: C.gris } }], M + 0.3, y + 0.2, 4.7, 0.4, { fontSize: 18 });
    T(s, d, M + 0.3, y + 0.62, 4.7, 0.45, { fontSize: 15, color: C.tinta2 });
  });
  // Ciclo del sprint
  const cx = 9.55, cy = 3.9;
  s.addShape(pptx.ShapeType.ellipse, { x: cx - 1.05, y: cy - 1.05, w: 2.1, h: 2.1, fill: { color: C.azulSuave }, line: { color: "C7D2FE", width: 0.75 } });
  icono(s, "ciclo", "azul", cx - 0.25, cy - 0.62, 0.5);
  T(s, "Sprint", cx - 0.9, cy - 0.05, 1.8, 0.35, { fontSize: 18, bold: true, align: "center" });
  T(s, "2 semanas", cx - 0.9, cy + 0.32, 1.8, 0.3, { fontSize: 13, color: C.gris, align: "center" });
  [["Planificación", "4 h", cx - 0.9, cy - 2.05], ["Daily Standup", "15 min al día", cx + 1.17, cy - 0.38],
   ["Revisión", "2 h", cx - 0.9, cy + 1.3], ["Retrospectiva", "2 h", cx - 2.97, cy - 0.38]].forEach(([t, d, x, y]) => {
    tarjeta(s, x, y, 1.8, 0.75);
    T(s, t, x + 0.1, y + 0.1, 1.6, 0.3, { fontSize: 14, bold: true, align: "center" });
    T(s, d, x + 0.1, y + 0.42, 1.6, 0.28, { fontSize: 12, color: C.gris, align: "center" });
  });
  fuente(s, "Fuente: SCRUMstudy (2022), pp. 35–37 y 42–43.");
}

// 13 · Seis principios
{
  const s = clara("Principios", "Seis principios que no se negocian",
    "La guía dice que los principios son obligatorios (p. 9). Para cada uno, una frase de cómo lo aplicamos en NewBit.");
  [["Control del proceso empírico", "Mostramos, revisamos y ajustamos. La idea cambió tres veces antes del primer sprint.", "22"],
   ["Autoorganización", "El equipo decide cómo hacer el trabajo en cada planificación.", "27"],
   ["Colaboración", "PO, equipo y usuarios validan juntos; revisamos el código entre pares.", "29"],
   ["Priorización basada en valor", "Primero lo que más valor da, respetando las dependencias.", "33"],
   ["Time-boxing", "Tiempos fijos: sprints de dos semanas y reuniones con duración máxima.", "35"],
   ["Desarrollo iterativo", "Un incremento revisable al final de cada sprint.", "38"]].forEach(([t, d, p], i) => {
    const x = M + (i % 3) * 3.95, y = 2.0 + Math.floor(i / 3) * 2.15;
    tarjeta(s, x, y, 3.7, 1.9);
    T(s, String(i + 1).padStart(2, "0"), x + 0.3, y + 0.25, 0.6, 0.3, { fontSize: 13, bold: true, color: C.azul });
    T(s, "p. " + p, x + 2.7, y + 0.25, 0.7, 0.3, { fontSize: 11, color: C.gris, align: "right" });
    T(s, t, x + 0.3, y + 0.6, 3.2, 0.4, { fontSize: 17, bold: true });
    T(s, d, x + 0.3, y + 1.05, 3.15, 0.8, { fontSize: 13.5, color: C.tinta2 });
  });
  fuente(s, "Fuente: SCRUMstudy (2022), pp. 21–40.");
}

// 14 · La Unidad I es la fase de inicio
{
  const s = clara("Guía SBOK → formatos del curso", "La Unidad I es la fase de Inicio",
    "Cada formato del curso es la salida de un proceso del libro. La fase de Inicio tiene seis procesos (8.1 a 8.6); a eso sumamos crear y estimar historias (9.1 y 9.2).");
  const p = [
    ["8.1", "Crear la visión", "Acta FGAP010 · Justificación EGAP015"], ["8.2", "Identificar interesados", "Registro FGAP020"],
    ["8.3", "Formar el equipo", "Roles FGAP030"], ["8.4", "Desarrollar épicas", "Épicas FGAP040 · personajes"],
    ["8.5", "Crear el backlog priorizado", "Backlog FGAP060 · Terminado FGAP070 · Listo"], ["8.6", "Planificar la liberación", "Sprints de 2 semanas · cierre 14–18/12"],
  ];
  p.forEach(([n, t, f], i) => {
    const x = M + i * 1.98;
    T(s, n, x, 2.05, 1.8, 0.4, { fontFace: TIT, fontSize: 28, color: C.azul });
    linea(s, x, 2.6, x + 1.75, 2.6, C.azul, 1.5);
    T(s, t, x, 2.8, 1.8, 0.8, { fontSize: 16, bold: true });
    T(s, f, x, 3.6, 1.8, 1.2, { fontSize: 13, color: C.tinta2 });
  });
  tarjeta(s, M, 5.05, W - 2 * M, 1.05, { fill: C.azulSuave, borde: "C7D2FE" });
  T(s, rico("Y de la fase siguiente: **9.1 Crear historias** (FGAP040) y **9.2 Estimar historias** (puño de cinco)."),
    M + 0.35, 5.35, W - 2 * M - 0.7, 0.5, { fontSize: 16 });
  fuente(s, "Fuente: SCRUMstudy (2022), tabla 1-1 (p. 15) y procesos 8.1–9.2 (pp. 139–195).");
}

// 15 · Evolución
{
  const s = clara("Inspeccionar y adaptar", "Cómo evolucionó la idea",
    "El control empírico aplicado a la propia idea: tres versiones, cada una resolvió un problema de la anterior. Lo que no cambió: sin rostros, decisión humana y evaluar el evento completo.");
  [["Semanas 2–3", "VIGIA Industrial", "Detectaba casco y chaleco en cámaras en vivo.", "Problema: veía objetos, no conductas.", C.ambar],
   ["Semana 4", "Elegimos Unsafe-Net", "Una investigación que reconoce conductas en el tiempo.", "Ganancia: datos públicos; se va el mayor riesgo.", C.verde],
   ["Semana 5", "NewBit", "Taller metalmecánico, video por lotes y 12 historias con criterios.", "Resultado: formatos coherentes entre sí.", C.verde]].forEach(([sem, t, d, r, col], i) => {
    const x = M + i * 3.98;
    T(s, sem.toUpperCase(), x, 2.0, 3.6, 0.3, { fontSize: 11, bold: true, color: C.gris, charSpacing: 1 });
    T(s, t, x, 2.35, 3.6, 0.5, { fontFace: TIT, fontSize: 28 });
    T(s, d, x, 3.0, 3.5, 0.9, { fontSize: 15, color: C.tinta2 });
    T(s, r, x, 3.95, 3.5, 0.8, { fontSize: 15, color: col, bold: true });
    if (i < 2) flecha(s, x + 3.55, 2.65, x + 3.9);
  });
  linea(s, M, 5.15, W - M, 5.15);
  T(s, rico("Lo que **no** cambió: sin reconocimiento facial · la decisión final es humana · se evalúa el evento completo, no una imagen suelta."),
    M, 5.35, W - 2 * M, 0.6, { fontSize: 16, color: C.tinta2 });
}

// ===================================================================== PARTE 3 · SEMANA A SEMANA
// 16 · Portada de sección
{
  const s = oscura("Parte 3", null, "Recorrido por lo que entregamos cada semana, de la 2 a la 6.");
  T(s, "Lo que entregamos,", M, 2.0, 11.5, 1.0, { fontFace: TIT, fontSize: 54, color: C.claro });
  T(s, "semana a semana", M, 3.0, 11.5, 1.0, { fontFace: TIT, fontSize: 54, color: C.claro2 });
  ["Semana 2 · Acta", "Semana 3 · Roles y visión", "Semana 4 · Justificación y épicas", "Semana 5 · Backlog y calidad", "Semana 6 · Lo que faltaba"].forEach((t, i) => {
    T(s, t, M + i * 2.4, 4.75, 2.3, 0.6, { fontSize: 14, color: C.claro2 });
    linea(s, M + i * 2.4, 4.6, M + i * 2.4 + 2.1, 4.6, C.nocheBorde, 1.5);
  });
}

// 17 · Semana 2: acta
{
  const s = clara("Semana 2 · Acta de constitución (FGAP010)", "El proyecto en una página",
    "El acta es la salida del proceso 8.1, Crear la visión. Cuatro datos clave. A la derecha, el cuadro comparativo de los principios, la otra tarea de la semana 2.");
  [["2", "conductas priorizadas", "con sus casos seguros de contraste"], ["S/ 20 768", "de presupuesto", "90 % es dedicación valorizada del equipo"],
   ["11 semanas", "del 05/10 al 18/12", "inicio, cuatro sprints y cierre"], ["7 riesgos", "con respuesta prevista", "el mayor: ajustar el modelo temporal"]].forEach(([n, t, d], i) => {
    const x = M + (i % 2) * 3.0, y = 2.0 + Math.floor(i / 2) * 2.1;
    T(s, n, x, y, 2.9, 0.75, { fontFace: TIT, fontSize: 36 });
    T(s, t, x, y + 0.78, 2.8, 0.35, { fontSize: 15, bold: true });
    T(s, d, x, y + 1.13, 2.8, 0.6, { fontSize: 13, color: C.gris });
  });
  s.addImage({ path: IMG("cuadro-principios.png"), x: 7.05, y: 2.0, w: 5.48, h: 3.08 });
  s.addShape(pptx.ShapeType.rect, { x: 7.05, y: 2.0, w: 5.48, h: 3.08, fill: { type: "none" }, line: { color: C.borde, width: 0.75 } });
  T(s, "También en la semana 2: cuadro comparativo de los principios de Scrum.", 7.05, 5.2, 5.5, 0.5, { fontSize: 12, color: C.gris });
}

// 18 · Semana 3: roles
{
  const s = clara("Semana 3 · Roles y prototipos (FGAP030)", "Cinco personas usan NewBit",
    "Los personajes son la salida obligatoria del proceso 8.4 (p. 164). Cada uno tiene nombre, rol y una necesidad concreta, que luego se convierte en historias de usuario.");
  [["JP", "Jorge Ponce", "Administrador (TI)", "Cargar videos y ajustar la sensibilidad sin tocar código."],
   ["MT", "Mariana Torres", "Supervisora de SST", "Alertas con un clip corto de evidencia."],
   ["CV", "César Vásquez", "Supervisor de turno", "Saber qué pasó, dónde y cuándo, sin alertas repetidas."],
   ["LR", "Lucía Ramos", "Operadora de monitoreo", "Ver solo lo importante y confirmar en un clic."],
   ["RS", "Ricardo Salcedo", "Gerente general (sponsor)", "Reportes por tipo, zona y semana."]].forEach(([ini, n, r, d], i) => {
    const x = M + i * 2.37;
    tarjeta(s, x, 2.0, 2.2, 3.7);
    s.addShape(pptx.ShapeType.ellipse, { x: x + 0.3, y: 2.3, w: 0.7, h: 0.7, fill: { color: C.azulSuave }, line: { color: "C7D2FE" } });
    T(s, ini, x + 0.3, 2.47, 0.7, 0.35, { fontSize: 15, bold: true, color: C.azul, align: "center" });
    T(s, n, x + 0.3, 3.2, 1.8, 0.35, { fontSize: 16, bold: true });
    T(s, r, x + 0.3, 3.55, 1.8, 0.55, { fontSize: 12.5, color: C.gris });
    T(s, d, x + 0.3, 4.15, 1.75, 1.4, { fontSize: 13.5, color: C.tinta2 });
  });
  fuente(s, "Perfiles ficticios de un caso académico. Fuente del concepto de personajes: SCRUMstudy (2022), p. 164.");
}

// 19 · Semana 3: visión
{
  const s = clara("Semana 3 · Visión del producto", "Cómo comunicamos la idea",
    "Infografía y diagrama de arquitectura: piezas para la reunión de la visión (proceso 8.1). Se muestran tal como se entregaron; todavía decían YOLOv4, que en la semana 5 cambió a YOLOv8.");
  const caja = (archivo, x, w, h, pw, ph, pie) => {
    const r = Math.min(w / pw, h / ph), iw = pw * r, ih = ph * r, ix = x + (w - iw) / 2;
    s.addImage({ path: IMG(archivo), x: ix, y: 1.95, w: iw, h: ih });
    s.addShape(pptx.ShapeType.rect, { x: ix, y: 1.95, w: iw, h: ih, fill: { type: "none" }, line: { color: C.borde, width: 0.75 } });
    T(s, pie, x, 1.95 + ih + 0.12, w, 0.3, { fontSize: 12, color: C.gris, align: "center" });
  };
  caja("infografia-pasos-1-6.png", M, 5.6, 4.35, 1680, 1440, "Infografía «Pasos para desarrollar NewBit» (pasos 1 a 6)");
  caja("diagrama-arquitectura.png", 6.95, 5.6, 4.35, 1224, 982, "Diagrama de arquitectura: el flujo en siete etapas");
}

// 20 · Semana 4: justificación
{
  const s = clara("Semana 4 · Justificación (EGAP015)", "¿Por qué vale la pena hacerlo?",
    "La justificación cumple el papel del caso de negocio, entrada obligatoria del proceso 8.1 (p. 141). Cuatro razones, una frase cada una, y sin prometer ahorros que no estén demostrados.");
  [["objetivo", "Necesidad", "Las inspecciones son intermitentes y las cámaras graban sin avisar."],
   ["capas", "Tecnología", "Dos etapas (YOLOv8 + ConvLSTM) con software abierto y datos públicos."],
   ["persona", "Operación", "Apoya la decisión del supervisor; no la reemplaza."],
   ["dinero", "Economía", "S/ 20 768, igual que en el acta; el gasto en efectivo es de S/ 280 más la contingencia."]].forEach(([ic, t, d], i) => {
    const y = 1.95 + i * 1.08;
    icono(s, ic, "ink", M, y + 0.05, 0.45);
    T(s, t, M + 0.75, y, 2.6, 0.5, { fontSize: 20, bold: true });
    T(s, d, M + 3.4, y + 0.05, 8.4, 0.7, { fontSize: 17, color: C.tinta2 });
    if (i < 3) linea(s, M, y + 0.85, W - M, y + 0.85);
  });
  T(s, "No prometemos ahorros ni menos accidentes sin evidencia.", M, 6.1, 11, 0.4, { fontSize: 15, bold: true, color: C.ambar });
}

// 21 · Semana 4: épicas
{
  const s = clara("Semana 4 · Épicas e historias (FGAP040)", "Del video a la alerta, en seis épicas",
    "Las épicas siguen el recorrido del dato (proceso 8.4) y se dividen en 12 historias, cada una con dos criterios de aceptación (proceso 9.1). Leer el ejemplo de HU10.");
  [["EP01", "Ingestión", "HU01–02"], ["EP02", "Detección", "HU03"], ["EP03", "Reducción y clips", "HU04–06"],
   ["EP04", "Clasificación", "HU07–08"], ["EP05", "Monitoreo y alertas", "HU09–10"], ["EP06", "Calibración", "HU11–12"]].forEach(([id, t, h], i) => {
    const x = M + i * 1.98, col = i < 3 ? C.azul : (i < 5 ? C.ambar : C.gris);
    T(s, id, x, 2.0, 1.8, 0.3, { fontSize: 12, bold: true, color: col });
    linea(s, x, 2.38, x + 1.78, 2.38, col, 2);
    T(s, t, x, 2.55, 1.8, 0.75, { fontSize: 17, bold: true });
    T(s, h, x, 3.3, 1.8, 0.3, { fontSize: 13, color: C.gris });
  });
  tarjeta(s, M, 4.1, W - 2 * M, 2.1);
  T(s, "EJEMPLO · HU10", M + 0.35, 4.3, 4, 0.3, { fontSize: 11, bold: true, color: C.azul, charSpacing: 1 });
  T(s, "Como operadora de monitoreo, quiero una alerta inmediata con hora y evidencia ante una conducta insegura, para intervenir a tiempo.",
    M + 0.35, 4.65, W - 2 * M - 0.7, 0.8, { fontFace: TIT, fontSize: 20 });
  T(s, "Criterios de aceptación: notificación visual y sonora · guarda fecha, marca de tiempo, clip y probabilidad.",
    M + 0.35, 5.55, W - 2 * M - 0.7, 0.4, { fontSize: 14, color: C.gris });
}

// 22 · Semana 5: backlog
{
  const s = clara("Semana 5 · Backlog priorizado (FGAP060)", "Qué se construye primero, y por qué",
    "Proceso 8.5: el backlog se ordena por valor, riesgo y dependencias. Tres pasos: MoSCoW, 100 puntos por integrante y dependencias. Resultado: 31 puntos en cuatro sprints.");
  [["1", "MoSCoW", "8 debe, 3 debería, 1 podría."], ["2", "100 puntos", "Cada integrante reparte 100 puntos entre las historias."],
   ["3", "Dependencias", "Ninguna etapa se prueba sin la anterior; por eso HU11 y HU06 se adelantan."]].forEach(([n, t, d], i) => {
    const y = 2.0 + i * 1.3;
    s.addShape(pptx.ShapeType.ellipse, { x: M, y: y + 0.02, w: 0.5, h: 0.5, fill: { color: C.azulSuave }, line: { color: "C7D2FE" } });
    T(s, n, M, y + 0.1, 0.5, 0.35, { fontSize: 15, bold: true, color: C.azul, align: "center" });
    T(s, t, M + 0.75, y, 4.2, 0.4, { fontSize: 18, bold: true });
    T(s, d, M + 0.75, y + 0.42, 4.3, 0.7, { fontSize: 14, color: C.tinta2 });
  });
  T(s, "31", 6.5, 1.85, 1.6, 1.0, { fontFace: TIT, fontSize: 60 });
  T(s, "puntos de historia en cuatro sprints", 7.75, 2.2, 4.5, 0.5, { fontSize: 16, color: C.tinta2 });
  [["Sprint 1", "HU01–HU03 · subir video y detectar personas", 7], ["Sprint 2", "HU04–HU06 y HU11 · filtrar y armar clips", 8],
   ["Sprint 3", "HU07–HU08 · reconocer la conducta", 8], ["Sprint 4", "HU09, HU10 y HU12 · alertas y reportes", 8]].forEach(([sp, d, pts], i) => {
    const y = 3.15 + i * 0.78, col = i < 2 ? C.azul : C.ambar;
    T(s, sp, 6.5, y, 1.2, 0.35, { fontSize: 14, bold: true });
    s.addShape(pptx.ShapeType.rect, { x: 7.75, y: y + 0.05, w: pts * 0.42, h: 0.26, fill: { color: col }, line: { color: col } });
    T(s, String(pts), 7.75 + pts * 0.42 + 0.1, y, 0.5, 0.35, { fontSize: 14, bold: true });
    T(s, d, 7.75, y + 0.36, 4.8, 0.3, { fontSize: 11.5, color: C.gris });
  });
  fuente(s, "Fuente del método: SCRUMstudy (2022), pp. 76–78 y 166–172.");
}

// 23 · Semana 5: estimación y tablero
{
  const s = clara("Semana 5 · Estimación y tablero", "Estimamos con los dedos y seguimos con un tablero",
    "Puño de cinco (proceso 9.2, p. 194): todos votan a la vez de 1 a 5; los extremos explican y se vota otra vez. A la derecha, el tablero del Sprint 1 con sus tareas propuestas (proceso 9.3).");
  icono(s, "mano", "ink", M, 2.05, 0.6);
  T(s, "Puño de cinco", M + 0.8, 2.1, 4, 0.5, { fontSize: 22, bold: true });
  ["Todos muestran de 1 a 5 dedos a la vez: 1 es muy pequeña y 5, muy grande.", "Quienes votaron en los extremos explican por qué.",
   "Se vuelve a votar hasta acordar el tamaño."].forEach((t, i) => {
    T(s, String(i + 1), M, 2.95 + i * 0.85, 0.4, 0.4, { fontSize: 16, bold: true, color: C.azul });
    T(s, t, M + 0.45, 2.95 + i * 0.85, 4.4, 0.75, { fontSize: 15, color: C.tinta2 });
  });
  T(s, "La épica más grande resultó la EP04: reconocer la conducta.", M, 5.6, 5, 0.6, { fontSize: 14, bold: true });
  s.addImage({ path: IMG("scrumboard-sprint1.png"), x: 6.25, y: 2.0, w: 6.28, h: 3.53 });
  s.addShape(pptx.ShapeType.rect, { x: 6.25, y: 2.0, w: 6.28, h: 3.53, fill: { type: "none" }, line: { color: C.borde, width: 0.75 } });
  T(s, "Scrumboard del Sprint 1: por hacer, en progreso, en prueba y terminada.", 6.25, 5.62, 6.3, 0.3, { fontSize: 12, color: C.gris });
}

// 24 · Semana 5: terminado
{
  const s = clara("Semana 5 · Criterios de terminado (FGAP070)", "¿Cuándo algo está realmente terminado?",
    "Diferenciar dos ideas que se confunden. Los criterios de aceptación son de cada historia y los define el PO. Los criterios de terminado valen para todas y no se negocian (p. 92).");
  tarjeta(s, M, 2.0, 5.65, 4.1);
  T(s, "CRITERIOS DE ACEPTACIÓN", M + 0.4, 2.3, 5, 0.3, { fontSize: 11, bold: true, color: C.gris, charSpacing: 1 });
  T(s, "Uno por historia", M + 0.4, 2.65, 5, 0.6, { fontFace: TIT, fontSize: 28 });
  T(s, "Los define el Product Owner. Ejemplo, HU01: acepta .mp4 y .avi, y muestra la duración y la resolución del video.",
    M + 0.4, 3.4, 4.85, 1.6, { fontSize: 15, color: C.tinta2 });
  tarjeta(s, 6.88, 2.0, 5.65, 4.1, { fill: C.azulSuave, borde: "C7D2FE" });
  T(s, "CRITERIOS DE TERMINADO", 7.28, 2.3, 5, 0.3, { fontSize: 11, bold: true, color: C.azul, charSpacing: 1 });
  T(s, "Iguales para todas", 7.28, 2.65, 5, 0.6, { fontFace: TIT, fontSize: 28 });
  ["Pruebas unitarias e integradas", "Revisión de código entre pares", "Documentación de datos, modelo y métricas",
   "Aprobación técnica y del Product Owner", "Ética: licencia respetada y sin biometría"].forEach((t, i) => {
    icono(s, "seguro", "azul", 7.28, 3.45 + i * 0.5, 0.3);
    T(s, t, 7.7, 3.47 + i * 0.5, 4.6, 0.35, { fontSize: 14.5 });
  });
}

// 25 · Semana 6
{
  const s = clara("Semana 6 · Lo que completamos", "Lo que el libro pedía y nos faltaba",
    "Al comparar nuestros formatos con la Guía SBOK aparecieron tres salidas obligatorias sin formato propio. Las elaboramos en esta semana; son propuesta del equipo.");
  [["equipo", "Registro de interesados", "FGAP020 · proceso 8.2", "Quién influye en el proyecto, qué espera y cómo lo involucramos: matriz de poder e interés."],
   ["lista", "Definición de listo", "proceso 8.5 · p. 92", "Una historia entra a un sprint solo si tiene criterios, dependencias resueltas, estimación y los datos que necesita."],
   ["calendario", "Plan de liberación", "proceso 8.6 · p. 178", "Sprints de dos semanas y una sola liberación al cierre, del 14 al 18 de diciembre."]].forEach(([ic, t, sub, d], i) => {
    const x = M + i * 3.95;
    tarjeta(s, x, 2.0, 3.7, 3.9);
    icono(s, ic, "azul", x + 0.35, 2.35, 0.5);
    T(s, t, x + 0.35, 3.05, 3.1, 0.45, { fontSize: 19, bold: true });
    T(s, sub, x + 0.35, 3.5, 3.1, 0.3, { fontSize: 12, color: C.gris });
    T(s, d, x + 0.35, 4.0, 3.05, 1.7, { fontSize: 14.5, color: C.tinta2 });
  });
}

// ===================================================================== PARTE 4 · LO QUE VIENE
// 26 · Plan de sprints
{
  const s = clara("Parte 4 · Lo que viene", "Cuatro sprints hasta diciembre",
    "Hoy empieza el Sprint 1. Cada sprint entrega algo que el usuario puede ver. El Sprint 3 es el de mayor riesgo técnico: ahí se fijan las metas con la línea base.");
  const x0 = M + 0.1, dia = (W - 2 * M - 0.2) / 74, y0 = 2.35;
  [[0, "05 oct"], [14, "19 oct"], [28, "02 nov"], [42, "16 nov"], [56, "30 nov"], [70, "14 dic"]].forEach(([d, t]) => {
    T(s, t, x0 + d * dia - 0.5, y0 - 0.45, 1.0, 0.3, { fontSize: 11, color: C.gris, align: "center" });
    linea(s, x0 + d * dia, y0 - 0.1, x0 + d * dia, y0 + 3.15, C.borde, 0.75);
  });
  [["Inicio", "Formatos de la Unidad I", 0, 11, C.gris], ["Sprint 1", "Subir video y detectar personas", 14, 25, C.azul],
   ["Sprint 2", "Filtrar fotogramas y armar clips", 28, 39, C.azul], ["Sprint 3", "Reconocer la conducta", 42, 53, C.ambar],
   ["Sprint 4", "Alertas, recuadro de riesgo y reportes", 56, 67, C.ambar], ["Cierre", "FGAP090", 70, 74, C.gris]].forEach(([n, d, a, b, col], i) => {
    const y = y0 + i * 0.52;
    s.addShape(pptx.ShapeType.roundRect, { x: x0 + a * dia, y, w: (b - a) * dia, h: 0.32, rectRadius: 0.05, fill: { color: col }, line: { color: col } });
    const tx = b > 60 ? x0 + a * dia - 3.6 : x0 + b * dia + 0.15;
    T(s, [{ text: n + "  ", options: { bold: true } }, { text: d, options: { color: C.tinta2 } }], tx, y + 0.02, 3.5, 0.3,
      { fontSize: 13, align: b > 60 ? "right" : "left" });
  });
  linea(s, x0 + 14 * dia, y0 + 0.45, x0 + 14 * dia, y0 + 3.2, C.tinta, 1.75);
  T(s, "Hoy · 19 de octubre", x0 + 14 * dia + 0.1, y0 + 3.0, 2.5, 0.3, { fontSize: 12, bold: true });
  fuente(s, "Fechas del acta (FGAP010). Cada sprint: planificación 4 h · Daily 15 min · revisión 2 h · retrospectiva 2 h.");
}

// 27 · Cierre
{
  const s = oscura(null, null, "Cerrar con la frase y abrir preguntas.", { sinPie: true });
  T(s, "Menos horas mirando video.", M, 2.0, 11.5, 1.0, { fontFace: TIT, fontSize: 54, color: C.claro });
  T(s, "Más tiempo para prevenir.", M, 3.0, 11.5, 1.0, { fontFace: TIT, fontSize: 54, color: C.claro2 });
  T(s, "Gracias · ¿Preguntas?", M, 4.6, 8, 0.5, { fontSize: 20, color: C.claro });
  linea(s, M, 5.75, W - M, 5.75, C.nocheBorde, 1);
  T(s, "NewBit · Grupo D3 · Albert Chumacero · Anthony Lopez · Luis Salazar · Ingeniería de Software II · UNS · 2026-II",
    M, 5.95, W - 2 * M, 0.4, { fontSize: 12, color: C.claro2 });
}

pptx.writeFile({ fileName: OUT }).then((f) => console.log("Escrito:", f));
