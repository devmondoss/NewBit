/* Mini Project · editor de cronogramas al estilo de MS Project (formato MSPDI).
   Grupo D3 · NewBit · Ingeniería de Software II (UNS, 2026-II). Sin dependencias. */
"use strict";

// ------------------------------------------------------------------ utilidades
const $ = (s) => document.querySelector(s);
const DIA_MS = 864e5;
const NOM_DIA = ["dom", "lun", "mar", "mié", "jue", "vie", "sáb"];
const LETRA_DIA = ["D", "L", "M", "X", "J", "V", "S"];
const MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"];
const FILA = 26;
const CAB = 46;
const ESCALAS = [3, 5, 8, 12, 18, 26, 36];
const SVGNS = "http://www.w3.org/2000/svg";
const pad = (n) => String(n).padStart(2, "0");

// fechas = número de día desde 1970-01-01 (UTC); así no hay líos de zona horaria
const aDia = (iso) => Math.round(Date.UTC(+iso.slice(0, 4), +iso.slice(5, 7) - 1, +iso.slice(8, 10)) / DIA_MS);
const aIso = (n) => new Date(n * DIA_MS).toISOString().slice(0, 10);
const diaSem = (n) => (((n + 4) % 7) + 7) % 7; // 0 = domingo
const partes = (n) => { const d = new Date(n * DIA_MS); return [d.getUTCDate(), d.getUTCMonth() + 1, d.getUTCFullYear()]; };
const fmtCorta = (n) => { const [d, m, a] = partes(n); return `${pad(d)}/${pad(m)}/${String(a).slice(2)}`; };
const fmtMs = (n) => `${NOM_DIA[diaSem(n)]} ${fmtCorta(n)}`; // «lun 19/10/26», como MS Project en español
const fmtLarga = (n) => { const [d, m, a] = partes(n); return `${pad(d)}/${pad(m)}/${a}`; };
const hoy = () => { const d = new Date(); return Math.round(Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()) / DIA_MS); };

function leerFecha(txt) {
  const s = String(txt || "").trim().toLowerCase().replace(/^[a-záéíóú]{2,4}\.?\s+/, "");
  if (!s) return null;
  let m = s.match(/^(\d{4})-(\d{1,2})-(\d{1,2})$/);
  if (m) return aDia(`${m[1]}-${pad(m[2])}-${pad(m[3])}`);
  m = s.match(/^(\d{1,2})[/.-](\d{1,2})(?:[/.-](\d{2,4}))?$/);
  if (!m) return NaN;
  let a = m[3] ? +m[3] : partes(P.inicio)[2];
  if (a < 100) a += 2000;
  const d = +m[1], mes = +m[2];
  if (mes < 1 || mes > 12 || d < 1 || d > 31) return NaN;
  const n = aDia(`${a}-${pad(mes)}-${pad(d)}`);
  return partes(n)[0] === d ? n : NaN;
}

function leerDuracion(txt) {
  const s = String(txt || "").trim().toLowerCase().replace(",", ".");
  const m = s.match(/^(\d+(?:\.\d+)?)\s*(d|día|días|dia|dias|s|sem|semana|semanas)?\.?$/);
  if (!m) return NaN;
  let v = parseFloat(m[1]);
  if (m[2] && m[2].startsWith("s")) v *= 5;
  return Math.round(v);
}

const fmtDur = (n) => `${n} ${n === 1 ? "día" : "días"}`;

// ------------------------------------------------------------------ estado
let P = proyectoNuevo();
let ruta = null;          // ruta relativa al repo del .xml abierto
let generadores = [];
let sucio = false;
let sel = new Set();      // uid seleccionados
let ancla = null;
let pilaDeshacer = [], pilaRehacer = [];
let escala = 12;          // px por día
let colapsados = new Set();
let feriados = new Set();
let d0 = 0;               // primer día dibujado en el Gantt
let visibles = [];

function proyectoNuevo() {
  let n = hoy();
  while (diaSem(n) !== 1) n++; // próximo lunes
  return { titulo: "Proyecto nuevo", inicio: n, feriados: [], tareas: [], sigUid: 1, avisos: [] };
}
const nuevaTarea = (o = {}) => ({ uid: P.sigUid++, nombre: "Nueva tarea", nivel: 1, dur: 1, cini: null, preds: [], rec: "", ...o });

// ------------------------------------------------------------------ calendario
const laborable = (n) => { const w = diaSem(n); return w !== 0 && w !== 6 && !feriados.has(n); };
function sigLab(n) { let k = 0; while (!laborable(n) && k++ < 4000) n++; return n; }
function sumarLab(ini, dur) { let n = ini, k = 1; while (k < dur) { n++; if (laborable(n)) k++; } return n; }
function contarLab(a, b) { let c = 0; for (let n = a; n <= b; n++) if (laborable(n)) c++; return c; }
function avanzarLab(n, k) { // k días laborables después de n (n ya es laborable)
  if (k > 0) { while (k > 0) { n++; if (laborable(n)) k--; } }
  else if (k < 0) { while (k < 0) { n--; if (laborable(n)) k++; } }
  return n;
}

// ------------------------------------------------------------------ programación (como MS Project: fin → comienzo)
function calcular() {
  feriados = new Set(P.feriados);
  const T = P.tareas;
  const porUid = new Map(T.map((t) => [t.uid, t]));
  const pila = [];
  T.forEach((t, i) => {
    t.id = i + 1;
    t.resumen = i + 1 < T.length && T[i + 1].nivel > t.nivel;
    while (pila.length && pila[pila.length - 1].nivel >= t.nivel) pila.pop();
    t.padre = pila.length ? pila[pila.length - 1] : null;
    pila.push(t);
    if (t.ini == null) { t.ini = P.inicio; t.fin = P.inicio; }
    t.error = null;
  });
  let cambios = true, pasadas = 0;
  while (cambios && pasadas < 200) {
    cambios = false; pasadas++;
    for (const t of T) {
      if (t.resumen) continue;
      let es = P.inicio, hito = null;
      if (t.cini != null) es = Math.max(es, t.cini);
      for (let a = t; a; a = a.padre) {
        for (const p of a.preds) {
          const q = porUid.get(p.uid);
          if (!q) continue;
          const s = avanzarLab(sigLab(q.fin + 1), p.lag || 0);
          es = Math.max(es, s);
          if (t.dur === 0 && a === t) hito = Math.max(hito ?? -Infinity, p.lag ? s : q.fin);
        }
      }
      let ini, fin;
      if (t.dur === 0) ini = fin = (hito != null && t.cini == null) ? hito : sigLab(es);
      else { ini = sigLab(es); fin = sumarLab(ini, t.dur); }
      if (ini !== t.ini || fin !== t.fin) { t.ini = ini; t.fin = fin; cambios = true; }
    }
    for (let i = T.length - 1; i >= 0; i--) {
      const t = T[i];
      if (!t.resumen) continue;
      let a = Infinity, b = -Infinity;
      for (let j = i + 1; j < T.length && T[j].nivel > t.nivel; j++) { a = Math.min(a, T[j].ini); b = Math.max(b, T[j].fin); }
      if (a !== t.ini || b !== t.fin) { t.ini = a; t.fin = b; cambios = true; }
    }
  }
  if (cambios) T.forEach((t) => { if (t.preds.length) t.error = "Vínculos circulares"; });
  T.forEach((t) => { t.durMostrar = t.resumen ? contarLab(t.ini, t.fin) : t.dur; });
  // filas visibles (respeta resúmenes contraídos)
  visibles = [];
  let ocultarHasta = null;
  for (const t of T) {
    if (ocultarHasta != null && t.nivel > ocultarHasta) continue;
    ocultarHasta = null;
    visibles.push(t);
    if (t.resumen && colapsados.has(t.uid)) ocultarHasta = t.nivel;
  }
}

const subarbolFin = (i) => { const T = P.tareas; let j = i; while (j + 1 < T.length && T[j + 1].nivel > T[i].nivel) j++; return j; };
const indice = (uid) => P.tareas.findIndex((t) => t.uid === uid);
function esAncestro(a, b) { for (let x = b.padre; x; x = x.padre) if (x === a) return true; return false; }

// ------------------------------------------------------------------ deshacer / cambios
const instantanea = () => JSON.stringify({ titulo: P.titulo, inicio: P.inicio, feriados: P.feriados, sigUid: P.sigUid,
  tareas: P.tareas.map(({ uid, nombre, nivel, dur, cini, preds, rec }) => ({ uid, nombre, nivel, dur, cini, preds, rec })) });
function restaurar(s) { const o = JSON.parse(s); P = { ...P, ...o }; }
function cambio(fn, mensaje) {
  const antes = instantanea();
  const r = fn();
  if (r === false) return;
  if (instantanea() === antes) return;
  pilaDeshacer.push(antes);
  if (pilaDeshacer.length > 200) pilaDeshacer.shift();
  pilaRehacer = [];
  marcarSucio(true);
  render();
  if (mensaje) estado(mensaje);
}
function deshacer() { if (!pilaDeshacer.length) return estado("Nada que deshacer"); pilaRehacer.push(instantanea()); restaurar(pilaDeshacer.pop()); marcarSucio(true); render(); estado("Deshecho"); }
function rehacer() { if (!pilaRehacer.length) return estado("Nada que rehacer"); pilaDeshacer.push(instantanea()); restaurar(pilaRehacer.pop()); marcarSucio(true); render(); estado("Rehecho"); }
function marcarSucio(v) { sucio = v; $("#sucio").classList.toggle("si", v); }
function estado(msg, error = false) { const e = $("#msgEstado"); e.textContent = msg; e.className = error ? "error" : ""; }

// ------------------------------------------------------------------ tabla
const COLS = [
  { k: "id", cls: "c-id", tit: "" },
  { k: "ind", cls: "c-ind", tit: "ⓘ" },
  { k: "nombre", cls: "c-nombre", tit: "Nombre de tarea" },
  { k: "dur", cls: "c-dur", tit: "Duración" },
  { k: "ini", cls: "c-ini", tit: "Comienzo" },
  { k: "fin", cls: "c-fin", tit: "Fin" },
  { k: "pred", cls: "c-pred", tit: "Predecesoras" },
  { k: "rec", cls: "c-rec", tit: "Nombres de los recursos" },
];
const EDITABLES = ["nombre", "dur", "ini", "fin", "pred"];

function textoPred(t) {
  const porUid = new Map(P.tareas.map((x) => [x.uid, x]));
  return t.preds.filter((p) => porUid.has(p.uid))
    .map((p) => porUid.get(p.uid).id + (p.lag ? (p.lag > 0 ? "+" : "") + p.lag + "d" : "")).join(";");
}
function valorCelda(t, k) {
  switch (k) {
    case "nombre": return t.nombre;
    case "dur": return fmtDur(t.durMostrar);
    case "ini": return fmtMs(t.ini);
    case "fin": return fmtMs(t.fin);
    case "pred": return textoPred(t);
    case "rec": return t.rec || "";
  }
  return "";
}

// ---- columnas: ancho arrastrable, autoajuste al contenido y orden por arrastre (se recuerdan en el navegador)
const ANCHO_DEF = { id: 38, ind: 24, nombre: 300, dur: 74, ini: 106, fin: 106, pred: 100, rec: 180 };
const FIJAS = ["id", "ind"];
const leerLocal = (k) => { try { return JSON.parse(localStorage.getItem(k)); } catch { return null; } };
const guardarLocal = (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)); } catch { /* sin almacenamiento */ } };
let anchos = { ...ANCHO_DEF, ...(leerLocal("mp-anchos") || {}) };
let orden = (() => {
  const o = leerLocal("mp-orden"), todas = COLS.map((c) => c.k).filter((k) => !FIJAS.includes(k));
  return Array.isArray(o) && o.length === todas.length && todas.every((k) => o.includes(k)) ? o : todas;
})();
let anchosManuales = !!leerLocal("mp-anchos");
const columnas = () => [...FIJAS, ...orden].map((k) => COLS.find((c) => c.k === k));

function aplicarAnchos() {
  const pt = $("#panelTabla");
  for (const k in anchos) pt.style.setProperty(`--w-${k}`, anchos[k] + "px");
  pt.style.setProperty("--w-total", Object.values(anchos).reduce((a, b) => a + b, 0) + "px");
}

let lienzo;
function medir(texto, negrita = false) {
  lienzo ||= document.createElement("canvas").getContext("2d");
  const fam = getComputedStyle(document.documentElement).fontFamily;
  lienzo.font = `${negrita ? "700 " : ""}13px ${fam}`;
  return lienzo.measureText(texto).width;
}
function autoAjustar(k) {
  if (FIJAS.includes(k)) return;
  const c = COLS.find((x) => x.k === k);
  let w = medir(c.tit, true) + 22;
  for (const t of visibles) {
    let tw = medir(valorCelda(t, k), t.resumen) + 18;
    if (k === "nombre") tw += 6 + (t.nivel - 1) * 18 + (t.resumen ? 14 : 0);
    w = Math.max(w, tw);
  }
  anchos[k] = Math.round(Math.min(Math.max(w, 48), k === "nombre" ? 640 : 360));
}
function autoAjustarTodo(manual = false) {
  for (const k of orden) autoAjustar(k);
  aplicarAnchos();
  const total = Object.values(anchos).reduce((a, b) => a + b, 0) + 4;
  $("#panelTabla").style.width = Math.max(320, Math.min(total, Math.round(window.innerWidth * 0.66))) + "px";
  if (manual) { anchosManuales = true; guardarLocal("mp-anchos", anchos); estado("Columnas ajustadas al contenido"); }
  sincronizarScroll();
}

function renderTabla() {
  const cols = columnas();
  $("#cabTabla").innerHTML = '<div class="fila cab-fila">' + cols.map((c) =>
    `<div class="celda ${c.cls}" data-col="${c.k}"${FIJAS.includes(c.k) ? "" : ' draggable="true" title="Arrastra el título para mover la columna · arrastra el borde para cambiar el ancho · doble clic en el borde para ajustarla"'}>` +
    `<span class="tit-col">${c.tit}</span>${FIJAS.includes(c.k) ? "" : `<span class="asa-col" data-asa-col="${c.k}"></span>`}</div>`).join("") + "</div>";
  const frag = document.createDocumentFragment();
  for (const t of visibles) frag.appendChild(filaTabla(t));
  const nueva = document.createElement("div");
  nueva.className = "fila nueva";
  nueva.dataset.uid = "nueva";
  nueva.innerHTML = cols.map((c) => c.k === "id" ? `<div class="celda c-id">${P.tareas.length + 1}</div>`
    : c.k === "nombre" ? '<div class="celda c-nombre"><input data-k="nombre" placeholder="Escribe aquí para agregar una tarea…"></div>'
    : `<div class="celda ${c.cls}"></div>`).join("");
  frag.appendChild(nueva);
  const relleno = document.createElement("div");
  relleno.style.height = "60px";
  frag.appendChild(relleno);
  $("#cuerpoTabla").replaceChildren(frag);
  aplicarAnchos();
}

function filaTabla(t) {
  const f = document.createElement("div");
  f.className = "fila" + (t.resumen ? " resumen" : "") + (sel.has(t.uid) ? " sel" : "") + (t.error ? " error" : "");
  f.dataset.uid = t.uid;
  const ind = t.dur === 0 && !t.resumen ? "◆" : (t.cini != null && !t.resumen ? "📌" : "");
  const indTitulo = t.error ? t.error : (t.cini != null ? `No comenzar antes del ${fmtMs(t.cini)}` : "");
  const sangria = 6 + (t.nivel - 1) * 18;
  const toggle = t.resumen ? `<button class="toggle" data-toggle="${t.uid}" title="Contraer o expandir">${colapsados.has(t.uid) ? "▶" : "▼"}</button>` : "";
  const ro = (k) => (t.resumen && k !== "nombre" && k !== "pred" ? " readonly" : "");
  f.innerHTML = columnas().map((c) => {
    if (c.k === "id") return `<div class="celda c-id" title="Seleccionar fila">${t.id}</div>`;
    if (c.k === "ind") return `<div class="celda c-ind" title="${indTitulo}">${t.error ? "⚠" : ind}</div>`;
    if (c.k === "nombre") return `<div class="celda c-nombre" style="padding-left:${sangria}px">${toggle}<input data-k="nombre"></div>`;
    return `<div class="celda ${c.cls}"><input data-k="${c.k}"${ro(c.k)}></div>`;
  }).join("");
  for (const inp of f.querySelectorAll("input")) { inp.value = valorCelda(t, inp.dataset.k); inp.dataset.orig = inp.value; inp.title = inp.value; }
  return f;
}

let redimensionandoCol = false;
function iniciarColumnas() {
  const cab = $("#cabTabla");
  cab.addEventListener("pointerdown", (e) => {
    const asa = e.target.closest("[data-asa-col]");
    if (!asa) return;
    e.preventDefault(); e.stopPropagation();
    const k = asa.dataset.asaCol, x0 = e.clientX, w0 = anchos[k];
    redimensionandoCol = true;
    document.body.classList.add("redimensionando");
    const mv = (ev) => { anchos[k] = Math.max(40, Math.min(900, w0 + ev.clientX - x0)); aplicarAnchos(); };
    const up = () => {
      window.removeEventListener("pointermove", mv); window.removeEventListener("pointerup", up);
      document.body.classList.remove("redimensionando");
      setTimeout(() => { redimensionandoCol = false; });
      anchosManuales = true; guardarLocal("mp-anchos", anchos);
    };
    window.addEventListener("pointermove", mv); window.addEventListener("pointerup", up);
  });
  cab.addEventListener("dblclick", (e) => {
    const asa = e.target.closest("[data-asa-col]");
    if (!asa) return;
    autoAjustar(asa.dataset.asaCol); aplicarAnchos(); anchosManuales = true; guardarLocal("mp-anchos", anchos);
  });
  let arrastrada = null;
  cab.addEventListener("dragstart", (e) => {
    const c = e.target.closest("[data-col][draggable]");
    if (!c || redimensionandoCol) { e.preventDefault(); return; }
    arrastrada = c.dataset.col; e.dataTransfer.effectAllowed = "move"; e.dataTransfer.setData("text/plain", arrastrada);
  });
  cab.addEventListener("dragover", (e) => {
    const c = e.target.closest("[data-col][draggable]");
    if (!arrastrada || !c) return;
    e.preventDefault();
    cab.querySelectorAll(".soltar-izq,.soltar-der").forEach((x) => x.classList.remove("soltar-izq", "soltar-der"));
    const r = c.getBoundingClientRect();
    c.classList.add(e.clientX < r.left + r.width / 2 ? "soltar-izq" : "soltar-der");
  });
  cab.addEventListener("drop", (e) => {
    const c = e.target.closest("[data-col][draggable]");
    if (!arrastrada || !c) return;
    e.preventDefault();
    const destino = c.dataset.col, r = c.getBoundingClientRect(), despues = e.clientX >= r.left + r.width / 2;
    if (destino !== arrastrada) {
      orden = orden.filter((k) => k !== arrastrada);
      orden.splice(orden.indexOf(destino) + (despues ? 1 : 0), 0, arrastrada);
      guardarLocal("mp-orden", orden);
      renderTabla();
      estado(`Columna «${COLS.find((x) => x.k === arrastrada).tit}» movida`);
    }
    arrastrada = null;
  });
  cab.addEventListener("dragend", () => { arrastrada = null; cab.querySelectorAll(".soltar-izq,.soltar-der").forEach((x) => x.classList.remove("soltar-izq", "soltar-der")); });
  window.addEventListener("resize", () => {
    const pt = $("#panelTabla"), max = Math.round(window.innerWidth * 0.75);
    if (pt.offsetWidth > max) pt.style.width = max + "px";
  });
}

function confirmarCelda(uid, k, valor) {
  if (uid === "nueva") {
    if (k !== "nombre" || !valor.trim()) return;
    cambio(() => {
      const ult = P.tareas[P.tareas.length - 1];
      const t = nuevaTarea({ nombre: valor.trim(), nivel: ult ? ult.nivel : 1 });
      P.tareas.push(t);
      sel = new Set([t.uid]);
    }, "Tarea agregada");
    return;
  }
  uid = +uid;
  const t = P.tareas.find((x) => x.uid === uid);
  if (!t || valorCelda(t, k) === valor) return;
  if (k === "nombre") return cambio(() => { t.nombre = valor.trim() || t.nombre; });
  if (k === "rec") return t.resumen ? render() : cambio(() => { t.rec = valor.split(/[;,]/).map((s) => s.trim()).filter(Boolean).join("; "); });
  if (t.resumen && k !== "pred") return;
  if (k === "dur") {
    const d = leerDuracion(valor);
    if (!Number.isFinite(d) || d < 0) return estado("Duración no válida: usa un número de días, p. ej. 5 o «2 sem»", true), render();
    return cambio(() => { t.dur = d; });
  }
  if (k === "ini") {
    const n = leerFecha(valor);
    if (Number.isNaN(n)) return estado("Fecha no válida: usa dd/mm/aa", true), render();
    return cambio(() => { t.cini = n == null ? null : sigLab(n); }, n == null ? "Restricción quitada" : "Fecha de comienzo fijada (no comenzar antes de)");
  }
  if (k === "fin") {
    const n = leerFecha(valor);
    if (n == null || Number.isNaN(n)) return estado("Fecha no válida: usa dd/mm/aa", true), render();
    if (n < t.ini) return estado("El fin no puede ser anterior al comienzo", true), render();
    return cambio(() => { t.dur = Math.max(t.dur === 0 ? 0 : 1, contarLab(t.ini, n)); });
  }
  if (k === "pred") {
    const porId = new Map(P.tareas.map((x) => [x.id, x]));
    const nuevas = [];
    for (const trozo of valor.split(/[;,\s]+/).filter(Boolean)) {
      const m = trozo.match(/^(\d+)(?:fc)?(?:([+-]\d+)\s*d?)?$/i);
      if (!m) return estado(`Predecesora no válida: «${trozo}». Usa el Id, p. ej. 3 o 3+2d`, true), render();
      const q = porId.get(+m[1]);
      if (!q) return estado(`No existe la tarea ${m[1]}`, true), render();
      if (q === t || esAncestro(q, t) || esAncestro(t, q)) return estado("Una tarea no puede vincularse consigo misma ni con su resumen o sus subtareas", true), render();
      nuevas.push({ uid: q.uid, lag: m[2] ? +m[2] : 0 });
    }
    return cambio(() => { t.preds = nuevas; });
  }
}

// ------------------------------------------------------------------ Gantt
function el(tag, attrs = {}, padre) {
  const e = document.createElementNS(SVGNS, tag);
  for (const k in attrs) e.setAttribute(k, attrs[k]);
  if (padre) padre.appendChild(e);
  return e;
}

function rangoGantt() {
  const T = P.tareas;
  let a = P.inicio, b = P.inicio + 70;
  if (T.length) { a = Math.min(a, ...T.map((t) => t.ini)); b = Math.max(...T.map((t) => t.fin)) + 21; }
  a -= 7; while (diaSem(a) !== 1) a--;
  while (diaSem(b) !== 0) b++;
  return [a, b];
}

function renderGantt() {
  const [a, b] = rangoGantt();
  d0 = a;
  const dias = b - a + 1, W = dias * escala, H = Math.max(visibles.length + 3, 1) * FILA + 60;
  const cab = $("#svgCab"), svg = $("#svgGantt");
  cab.replaceChildren(); svg.replaceChildren();
  cab.setAttribute("width", W); cab.setAttribute("height", CAB);
  svg.setAttribute("width", W); svg.setAttribute("height", H);
  const X = (n) => (n - d0) * escala;
  // encabezado: meses arriba; semanas o días abajo
  el("line", { x1: 0, y1: CAB / 2, x2: W, y2: CAB / 2, stroke: "#d4d4d4" }, cab);
  for (let n = a; n <= b;) {
    const [, m, y] = partes(n);
    let fin = n; while (fin + 1 <= b && partes(fin + 1)[1] === m) fin++;
    el("line", { x1: X(n), y1: 0, x2: X(n), y2: CAB / 2, stroke: "#d4d4d4" }, cab);
    const t = el("text", { x: (X(n) + X(fin + 1)) / 2, y: 16, "text-anchor": "middle", class: "txt-cab" }, cab);
    t.textContent = (fin - n + 1) * escala > 90 ? `${MESES[m - 1]} ${y}` : MESES[m - 1].slice(0, 3);
    n = fin + 1;
  }
  const porDia = escala >= 18;
  for (let n = a; n <= b; n++) {
    if (!laborable(n)) el("rect", { x: X(n), y: 0, width: escala, height: H, class: "finde" }, svg);
    if (porDia) {
      el("line", { x1: X(n), y1: CAB / 2, x2: X(n), y2: CAB, stroke: "#e0e0e0" }, cab);
      const t = el("text", { x: X(n) + escala / 2, y: 38, "text-anchor": "middle", class: "txt-cab" }, cab);
      t.textContent = escala >= 26 ? `${LETRA_DIA[diaSem(n)]} ${partes(n)[0]}` : LETRA_DIA[diaSem(n)];
    }
    if (diaSem(n) === 1) {
      el("line", { x1: X(n), y1: 0, x2: X(n), y2: H, class: "linea-sem" }, svg);
      if (!porDia) {
        el("line", { x1: X(n), y1: CAB / 2, x2: X(n), y2: CAB, stroke: "#d4d4d4" }, cab);
        if (7 * escala >= 34) { const t = el("text", { x: X(n) + 3.5 * escala, y: 38, "text-anchor": "middle", class: "txt-cab" }, cab); t.textContent = fmtCorta(n).slice(0, 5); }
      }
    }
  }
  const h = hoy();
  if (h >= a && h <= b) el("line", { x1: X(h) + escala / 2, y1: 0, x2: X(h) + escala / 2, y2: H, class: "linea-hoy" }, svg);
  // filas seleccionadas
  visibles.forEach((t, i) => { if (sel.has(t.uid)) el("rect", { x: 0, y: i * FILA, width: W, height: FILA, class: "fila-sel" }, svg); });
  // barras
  const pos = new Map();
  const capaFlechas = el("g", {}, svg);
  visibles.forEach((t, i) => {
    const yc = i * FILA + FILA / 2;
    const x1 = X(t.ini) + 1, x2 = X(t.fin + 1) - 1;
    if (t.resumen) {
      el("rect", { x: x1, y: yc - 5, width: Math.max(x2 - x1, 2), height: 5, class: "resumen-barra" }, svg);
      for (const xx of [x1, x2]) el("polygon", { points: `${xx - 4},${yc - 5} ${xx + 4},${yc - 5} ${xx},${yc + 3}`, class: "resumen-barra" }, svg);
      pos.set(t.uid, { a: x1, b: x2, y: yc, top: yc - 5 });
    } else if (t.dur === 0) {
      const x = X(t.fin + 1) - escala * 0.3;
      el("polygon", { points: `${x},${yc - 7} ${x + 7},${yc} ${x},${yc + 7} ${x - 7},${yc}`, class: "hito barra-arrastrable", "data-uid": t.uid }, svg);
      const lab = el("text", { x: x + 11, y: yc + 4, class: "txt-hito" }, svg); lab.textContent = fmtCorta(t.fin).slice(0, 5);
      pos.set(t.uid, { a: x, b: x, y: yc, top: yc - 7 });
    } else {
      const g = el("g", { "data-uid": t.uid, class: "barra-arrastrable" }, svg);
      el("rect", { x: x1, y: yc - 6, width: Math.max(x2 - x1, 3), height: 12, class: "barra" }, g);
      el("rect", { x: x2 - 5, y: yc - 6, width: 8, height: 12, class: "asa", "data-asa": "1" }, g);
      el("title", {}, g).textContent = `${t.nombre}\n${fmtMs(t.ini)} → ${fmtMs(t.fin)} · ${fmtDur(t.dur)}` + (t.rec ? `\n${t.rec}` : "");
      if (t.rec && escala >= 5) { const r = el("text", { x: x2 + 5, y: yc + 4, class: "txt-rec" }, svg); r.textContent = t.rec.replace(/; /g, ", "); }
      pos.set(t.uid, { a: x1, b: x2, y: yc, top: yc - 6 });
    }
  });
  // flechas de predecesoras
  for (const t of visibles) {
    const s = pos.get(t.uid);
    for (const p of t.preds) {
      const o = pos.get(p.uid);
      if (!o || !s) continue;
      const xm = o.b + 6;
      let d, punta;
      if (s.a - xm >= 6) {
        d = `M${o.b},${o.y} H${xm} V${s.y} H${s.a - 4}`;
        punta = `${s.a},${s.y} ${s.a - 5},${s.y - 3.5} ${s.a - 5},${s.y + 3.5}`;
      } else {
        const yy = s.y > o.y ? s.top : s.y + (s.y - s.top);
        d = `M${o.b},${o.y} H${xm} V${yy + (s.y > o.y ? -4 : 4)}`;
        punta = s.y > o.y ? `${xm},${yy} ${xm - 3.5},${yy - 5} ${xm + 3.5},${yy - 5}` : `${xm},${yy} ${xm - 3.5},${yy + 5} ${xm + 3.5},${yy + 5}`;
      }
      el("path", { d, class: "flecha" }, capaFlechas);
      el("polygon", { points: punta, class: "punta" }, capaFlechas);
    }
  }
}

// arrastrar barras: mover (fija «no comenzar antes de») o estirar el final (cambia duración)
let arrastre = null;
function inicioArrastre(e) {
  const g = e.target.closest(".barra-arrastrable");
  if (!g || e.button !== 0) return;
  const t = P.tareas.find((x) => x.uid === +g.dataset.uid);
  if (!t || t.resumen) return;
  e.preventDefault();
  seleccionar(t.uid, e);
  arrastre = { t, g, x0: e.clientX, modo: e.target.dataset.asa ? "estirar" : "mover", dd: 0 };
  g.setPointerCapture?.(e.pointerId);
}
function moverArrastre(e) {
  if (!arrastre) return;
  arrastre.dd = Math.round((e.clientX - arrastre.x0) / escala);
  const px = arrastre.dd * escala;
  if (arrastre.modo === "mover") arrastre.g.setAttribute("transform", `translate(${px},0)`);
  else { const r = arrastre.g.querySelector(".barra"); r.setAttribute("width", Math.max(3, (arrastre.w0 ??= +r.getAttribute("width")) + px)); }
  estado(arrastre.modo === "mover" ? `Mover ${arrastre.dd >= 0 ? "+" : ""}${arrastre.dd} días` : `Fin: ${fmtMs(arrastre.t.fin + arrastre.dd)}`);
}
function finArrastre() {
  if (!arrastre) return;
  const { t, dd, modo } = arrastre;
  arrastre = null;
  if (!dd) return render();
  if (modo === "mover") cambio(() => { t.cini = sigLab(t.ini + dd); }, `Comienzo fijado: ${fmtMs(sigLab(t.ini + dd))}`);
  else cambio(() => { const fin = Math.max(t.ini, t.fin + dd); t.dur = Math.max(1, contarLab(t.ini, fin)); });
}

// ------------------------------------------------------------------ render general
function render() {
  calcular();
  renderTabla();
  renderGantt();
  $("#nombreArchivo").textContent = (P.titulo || "Sin título") + (ruta ? `  —  ${ruta}` : "  —  (sin guardar)");
  const T = P.tareas;
  if (T.length) {
    const a = Math.min(...T.map((t) => t.ini)), b = Math.max(...T.map((t) => t.fin));
    $("#resumenEstado").textContent = `${T.length} tareas · ${fmtMs(a)} → ${fmtMs(b)} · ${contarLab(a, b)} días laborables` +
      (P.feriados.length ? ` · ${P.feriados.length} feriado(s)` : "");
  } else $("#resumenEstado").textContent = "Sin tareas";
  const err = T.find((t) => t.error);
  if (err) estado(`⚠ ${err.error}: revisa las predecesoras`, true);
  sincronizarScroll();
}

function seleccionar(uid, e) {
  if (e && e.shiftKey && ancla != null) {
    const ids = visibles.map((t) => t.uid), i = ids.indexOf(ancla), j = ids.indexOf(uid);
    sel = new Set(ids.slice(Math.min(i, j), Math.max(i, j) + 1));
  } else if (e && (e.metaKey || e.ctrlKey)) {
    sel.has(uid) ? sel.delete(uid) : sel.add(uid);
    ancla = uid;
  } else { sel = new Set([uid]); ancla = uid; }
  pintarSeleccion();
}
function pintarSeleccion() {
  for (const f of document.querySelectorAll("#cuerpoTabla .fila")) f.classList.toggle("sel", sel.has(+f.dataset.uid));
  const svg = $("#svgGantt");
  svg.querySelectorAll(".fila-sel").forEach((r) => r.remove());
  const W = svg.getAttribute("width");
  visibles.forEach((t, i) => {
    if (!sel.has(t.uid)) return;
    const r = el("rect", { x: 0, y: i * FILA, width: W, height: FILA, class: "fila-sel" });
    svg.insertBefore(r, svg.querySelector("g"));
  });
}
function enfocar(uid, k) {
  const f = document.querySelector(`#cuerpoTabla .fila[data-uid="${uid}"]`);
  const inp = f && f.querySelector(`input[data-k="${k}"]`);
  if (inp) { inp.focus(); inp.select(); }
}

// ------------------------------------------------------------------ acciones
const seleccionadas = () => P.tareas.filter((t) => sel.has(t.uid));
const acciones = {
  nuevo() {
    if (sucio && !confirm("Hay cambios sin guardar. ¿Empezar un proyecto nuevo de todos modos?")) return;
    P = proyectoNuevo(); ruta = null; generadores = []; sel.clear(); pilaDeshacer = []; pilaRehacer = []; colapsados.clear();
    marcarSucio(false); history.replaceState(null, "", "#"); render(); acciones.propiedades();
  },
  abrir: abrirDialogo,
  guardar,
  guardarComo,
  deshacer, rehacer,
  insertar(hito = false) {
    cambio(() => {
      const ref = P.tareas.findIndex((t) => sel.has(t.uid));
      const i = ref < 0 ? P.tareas.length : ref;
      const nivel = ref < 0 ? (P.tareas.at(-1)?.nivel || 1) : P.tareas[ref].nivel;
      const t = nuevaTarea(hito ? { nombre: "Nuevo hito", dur: 0, nivel } : { nivel });
      P.tareas.splice(i, 0, t);
      sel = new Set([t.uid]);
      setTimeout(() => enfocar(t.uid, "nombre"));
    }, hito ? "Hito insertado" : "Tarea insertada");
  },
  hito() { acciones.insertar(true); },
  eliminar() {
    if (!sel.size) return estado("Selecciona una fila (clic en su número)", true);
    cambio(() => {
      const quitar = new Set();
      P.tareas.forEach((t, i) => { if (sel.has(t.uid)) for (let j = i; j <= subarbolFin(i); j++) quitar.add(P.tareas[j].uid); });
      P.tareas = P.tareas.filter((t) => !quitar.has(t.uid));
      P.tareas.forEach((t) => { t.preds = t.preds.filter((p) => !quitar.has(p.uid)); });
      sel.clear();
    }, "Eliminado");
  },
  sangria() {
    cambio(() => {
      let hizo = false;
      for (let i = 0; i < P.tareas.length; i++) {
        const t = P.tareas[i];
        if (!sel.has(t.uid) || i === 0) continue;
        if (t.nivel > P.tareas[i - 1].nivel) continue;
        const fin = subarbolFin(i);
        for (let j = i; j <= fin; j++) P.tareas[j].nivel++;
        // un resumen no puede quedar vinculado con sus subtareas
        hizo = true;
      }
      limpiarVinculosInvalidos();
      return hizo;
    });
  },
  anularSangria() {
    cambio(() => {
      let hizo = false;
      for (let i = 0; i < P.tareas.length; i++) {
        const t = P.tareas[i];
        if (!sel.has(t.uid) || t.nivel <= 1) continue;
        const fin = subarbolFin(i);
        for (let j = i; j <= fin; j++) P.tareas[j].nivel--;
        hizo = true;
      }
      limpiarVinculosInvalidos();
      return hizo;
    });
  },
  subir() { mover(-1); },
  bajar() { mover(1); },
  vincular() {
    const S = seleccionadas().filter((t) => !t.resumen || true);
    if (S.length < 2) return estado("Selecciona 2 o más filas (Shift o Ctrl/Cmd + clic en el número) para vincularlas", true);
    cambio(() => {
      calcular();
      for (let k = 1; k < S.length; k++) {
        const a = S[k - 1], b = S[k];
        if (esAncestro(a, b) || esAncestro(b, a)) continue;
        if (!b.preds.some((p) => p.uid === a.uid)) b.preds.push({ uid: a.uid, lag: 0 });
      }
    }, "Tareas vinculadas (fin → comienzo)");
  },
  acercar() { const i = ESCALAS.indexOf(escala); escala = ESCALAS[Math.min(ESCALAS.length - 1, i + 1)]; renderGantt(); sincronizarScroll(); },
  alejar() { const i = ESCALAS.indexOf(escala); escala = ESCALAS[Math.max(0, i - 1)]; renderGantt(); sincronizarScroll(); },
  ajustarColumnas() { autoAjustarTodo(true); },
  restablecerColumnas() {
    anchos = { ...ANCHO_DEF }; orden = COLS.map((c) => c.k).filter((k) => !FIJAS.includes(k));
    try { localStorage.removeItem("mp-anchos"); localStorage.removeItem("mp-orden"); } catch { /* */ }
    anchosManuales = false; render(); autoAjustarTodo(); estado("Columnas restablecidas");
  },
  irHoy() { $("#cuerpoGantt").scrollLeft = Math.max(0, (hoy() - d0) * escala - 120); },
  propiedades: propiedadesDialogo,
  exportarPng,
  generar,
};

function limpiarVinculosInvalidos() {
  calcular();
  const porUid = new Map(P.tareas.map((t) => [t.uid, t]));
  for (const t of P.tareas) t.preds = t.preds.filter((p) => { const q = porUid.get(p.uid); return q && q !== t && !esAncestro(q, t) && !esAncestro(t, q); });
}

function mover(dir) {
  const S = seleccionadas();
  if (S.length !== 1) return estado("Selecciona una sola fila para moverla", true);
  cambio(() => {
    const T = P.tareas, i = indice(S[0].uid), j = subarbolFin(i), nivel = T[i].nivel;
    if (dir < 0) {
      let k = i - 1;
      while (k >= 0 && T[k].nivel > nivel) k--;
      if (k < 0 || T[k].nivel < nivel) return false;
      const bloque = T.splice(i, j - i + 1);
      T.splice(k, 0, ...bloque);
    } else {
      const k = j + 1;
      if (k >= T.length || T[k].nivel !== nivel) return false;
      const m = subarbolFin(k);
      const bloque = T.splice(i, j - i + 1);
      T.splice(m - bloque.length + 1, 0, ...bloque);
    }
    limpiarVinculosInvalidos();
  });
}

// ------------------------------------------------------------------ MSPDI (XML de MS Project)
function leerXml(texto) {
  const doc = new DOMParser().parseFromString(texto, "application/xml");
  if (doc.getElementsByTagName("parsererror").length) throw new Error("El archivo no es un XML válido");
  const raiz = doc.documentElement;
  if (raiz.localName !== "Project") throw new Error("No es un proyecto de MS Project (falta <Project>)");
  const hijos = (e, n) => (e ? [...e.children].filter((c) => c.localName === n) : []);
  const hijo = (e, n) => hijos(e, n)[0] || null;
  const tx = (e, n) => { const c = hijo(e, n); return c ? c.textContent.trim() : ""; };
  const np = proyectoNuevo();
  np.titulo = tx(raiz, "Title") || tx(raiz, "Name").replace(/\.xml$/i, "") || "Proyecto";
  if (tx(raiz, "StartDate")) np.inicio = aDia(tx(raiz, "StartDate").slice(0, 10));
  // feriados del calendario del proyecto
  const calUid = tx(raiz, "CalendarUID");
  const fer = new Set();
  for (const cal of hijos(hijo(raiz, "Calendars"), "Calendar")) {
    if (calUid && tx(cal, "UID") !== calUid) continue;
    const periodos = [];
    for (const ex of hijos(hijo(cal, "Exceptions"), "Exception")) if (tx(ex, "DayWorking") === "0") periodos.push(hijo(ex, "TimePeriod"));
    for (const wd of hijos(hijo(cal, "WeekDays"), "WeekDay")) if (tx(wd, "DayType") === "0" && tx(wd, "DayWorking") === "0") periodos.push(hijo(wd, "TimePeriod"));
    for (const tp of periodos) {
      if (!tp) continue;
      const a = aDia(tx(tp, "FromDate").slice(0, 10)), b = aDia(tx(tp, "ToDate").slice(0, 10));
      for (let n = a; n <= b && n - a < 400; n++) fer.add(n);
    }
  }
  np.feriados = [...fer].sort((x, y) => x - y);
  // recursos y asignaciones (Nombres de los recursos)
  const recursos = new Map(hijos(hijo(raiz, "Resources"), "Resource").filter((r) => tx(r, "Name")).map((r) => [tx(r, "UID"), tx(r, "Name")]));
  const asig = new Map();
  for (const a of hijos(hijo(raiz, "Assignments"), "Assignment")) {
    const r = recursos.get(tx(a, "ResourceUID"));
    if (r) asig.set(tx(a, "TaskUID"), [...(asig.get(tx(a, "TaskUID")) || []), r]);
  }
  // tareas
  const mapa = new Map(), crudas = [];
  let otrosTipos = 0;
  for (const e of hijos(hijo(raiz, "Tasks"), "Task")) {
    if (tx(e, "IsNull") === "1") continue;
    const nivel = +(tx(e, "OutlineLevel") || 1);
    if (nivel === 0 || tx(e, "UID") === "0") continue;
    const horas = duracionHoras(tx(e, "Duration"));
    const hito = tx(e, "Milestone") === "1";
    const t = nuevaTareaDe(np, { nombre: tx(e, "Name") || "(sin nombre)", nivel, dur: hito ? 0 : Math.max(0, Math.round(horas / 8)),
      rec: (asig.get(tx(e, "UID")) || []).join("; ") });
    const ct = +(tx(e, "ConstraintType") || 0);
    if ([2, 4].includes(ct) && tx(e, "ConstraintDate")) t.cini = aDia(tx(e, "ConstraintDate").slice(0, 10));
    t._ini = tx(e, "Start") ? aDia(tx(e, "Start").slice(0, 10)) : null;
    t._preds = hijos(e, "PredecessorLink").map((l) => {
      if ((tx(l, "Type") || "1") !== "1") otrosTipos++;
      return { uid: tx(l, "PredecessorUID"), lag: Math.round((+tx(l, "LinkLag") || 0) / 4800) };
    });
    mapa.set(tx(e, "UID"), t);
    crudas.push(t);
  }
  for (const t of crudas) {
    t.preds = t._preds.filter((p) => mapa.has(p.uid)).map((p) => ({ uid: mapa.get(p.uid).uid, lag: p.lag }));
    delete t._preds;
  }
  // tareas sin vínculos ni restricción: conservar su fecha de comienzo (no amontonarlas al inicio)
  crudas.forEach((t, i) => {
    const resumen = i + 1 < crudas.length && crudas[i + 1].nivel > t.nivel;
    if (!resumen && t.cini == null && !t.preds.length && t._ini != null && t._ini > np.inicio) {
      let tienePredHeredada = false;
      for (let k = i - 1, nv = t.nivel; k >= 0; k--) if (crudas[k].nivel < nv) { nv = crudas[k].nivel; if (crudas[k].preds.length) tienePredHeredada = true; }
      if (!tienePredHeredada) t.cini = t._ini;
    }
    delete t._ini;
  });
  np.tareas = crudas;
  if (otrosTipos) np.avisos.push(`${otrosTipos} vínculo(s) no eran «fin a comienzo»; se tratan como fin a comienzo.`);
  return np;
}
function nuevaTareaDe(p, o) { return { uid: p.sigUid++, nombre: "", nivel: 1, dur: 1, cini: null, preds: [], rec: "", ...o }; }
function duracionHoras(s) {
  const m = String(s).match(/^PT(\d+(?:\.\d+)?)H(\d+(?:\.\d+)?)M/);
  return m ? +m[1] + +m[2] / 60 : 0;
}

const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
function escribirXml() {
  calcular();
  const T = P.tareas;
  const a = T.length ? Math.min(...T.map((t) => t.ini)) : P.inicio;
  const b = T.length ? Math.max(...T.map((t) => t.fin)) : P.inicio;
  const dt = (n, h) => `${aIso(n)}T${h}`;
  const horas = (d) => `PT${d * 8}H0M0S`;
  const dias = [];
  for (let k = 1; k <= 7; k++) {
    dias.push(k === 1 || k === 7
      ? `<WeekDay><DayType>${k}</DayType><DayWorking>0</DayWorking></WeekDay>`
      : `<WeekDay><DayType>${k}</DayType><DayWorking>1</DayWorking><WorkingTimes>` +
        "<WorkingTime><FromTime>08:00:00</FromTime><ToTime>12:00:00</ToTime></WorkingTime>" +
        "<WorkingTime><FromTime>13:00:00</FromTime><ToTime>17:00:00</ToTime></WorkingTime></WorkingTimes></WeekDay>");
  }
  const excepciones = P.feriados.map((n) => "<Exception><EnteredByOccurrences>0</EnteredByOccurrences>" +
    `<TimePeriod><FromDate>${dt(n, "00:00:00")}</FromDate><ToDate>${dt(n, "23:59:00")}</ToDate></TimePeriod>` +
    `<Occurrences>1</Occurrences><Name>Feriado ${fmtLarga(n)}</Name><Type>1</Type><DayWorking>0</DayWorking></Exception>`).join("");
  const cal = "<Calendars><Calendar><UID>1</UID><Name>Estándar</Name><IsBaseCalendar>1</IsBaseCalendar><BaseCalendarUID>-1</BaseCalendarUID>" +
    `<WeekDays>${dias.join("")}</WeekDays>${excepciones ? `<Exceptions>${excepciones}</Exceptions>` : ""}</Calendar></Calendars>`;
  const tarea = (uid, id, nombre, wbs, nivel, ini, fin, d, { resumen = false, hito = false, preds = [], cini = null } = {}) =>
    `<Task><UID>${uid}</UID><ID>${id}</ID><Name>${esc(nombre)}</Name><Type>1</Type><IsNull>0</IsNull>` +
    `<WBS>${wbs}</WBS><OutlineNumber>${wbs}</OutlineNumber><OutlineLevel>${nivel}</OutlineLevel><Priority>500</Priority>` +
    `<Start>${dt(ini, hito ? "17:00:00" : "08:00:00")}</Start><Finish>${dt(fin, "17:00:00")}</Finish>` +
    `<Duration>${horas(d)}</Duration><DurationFormat>7</DurationFormat>` +
    `<Milestone>${hito ? 1 : 0}</Milestone><Summary>${resumen ? 1 : 0}</Summary>` +
    (cini != null ? `<ConstraintType>4</ConstraintType><ConstraintDate>${dt(cini, "08:00:00")}</ConstraintDate>` : "<ConstraintType>0</ConstraintType>") +
    preds.map((p) => `<PredecessorLink><PredecessorUID>${p.uid}</PredecessorUID><Type>1</Type><CrossProject>0</CrossProject>` +
      `<LinkLag>${(p.lag || 0) * 4800}</LinkLag><LagFormat>7</LagFormat></PredecessorLink>`).join("") + "</Task>";
  const xs = [tarea(0, 0, P.titulo, "0", 0, a, b, contarLab(a, b), { resumen: true })];
  const cont = [];
  for (const t of T) {
    cont.length = t.nivel; cont[t.nivel - 1] = (cont[t.nivel - 1] || 0) + 1;
    for (let k = 0; k < t.nivel; k++) cont[k] ||= 1;
    const wbs = cont.slice(0, t.nivel).join(".");
    xs.push(tarea(t.uid, t.id, t.nombre, wbs, t.nivel, t.ini, t.fin, t.resumen ? contarLab(t.ini, t.fin) : t.dur,
      { resumen: t.resumen, hito: t.dur === 0 && !t.resumen, preds: t.preds, cini: t.resumen ? null : t.cini }));
  }
  const nombresRec = [];
  const recDe = (t) => (t.resumen ? [] : (t.rec || "").split(";").map((s) => s.trim()).filter(Boolean));
  for (const t of T) for (const r of recDe(t)) if (!nombresRec.includes(r)) nombresRec.push(r);
  const recursosXml = nombresRec.map((r, i) => `<Resource><UID>${i + 1}</UID><ID>${i + 1}</ID><Name>${esc(r)}</Name><Type>1</Type>` +
    "<IsNull>0</IsNull><MaxUnits>1.00</MaxUnits></Resource>").join("");
  let na = 0;
  const asigXml = T.flatMap((t) => recDe(t).map((r) => `<Assignment><UID>${++na}</UID><TaskUID>${t.uid}</TaskUID>` +
    `<ResourceUID>${nombresRec.indexOf(r) + 1}</ResourceUID><Units>1</Units></Assignment>`)).join("");
  const nombre = ruta ? ruta.split("/").pop() : "proyecto.xml";
  return '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<Project xmlns="http://schemas.microsoft.com/project">' +
    `<SaveVersion>14</SaveVersion><Name>${esc(nombre)}</Name><Title>${esc(P.titulo)}</Title><Author>Grupo D3 (NewBit) - UNS</Author>` +
    `<CreationDate>${aIso(hoy())}T08:00:00</CreationDate><ScheduleFromStart>1</ScheduleFromStart>` +
    `<StartDate>${dt(P.inicio, "08:00:00")}</StartDate><FinishDate>${dt(b, "17:00:00")}</FinishDate><CalendarUID>1</CalendarUID>` +
    "<DefaultStartTime>08:00:00</DefaultStartTime><DefaultFinishTime>17:00:00</DefaultFinishTime>" +
    "<MinutesPerDay>480</MinutesPerDay><MinutesPerWeek>2400</MinutesPerWeek><DaysPerMonth>20</DaysPerMonth>" +
    "<DefaultTaskType>1</DefaultTaskType><DurationFormat>7</DurationFormat>" +
    `${cal}<Tasks>${xs.join("")}</Tasks><Resources>${recursosXml}</Resources><Assignments>${asigXml}</Assignments></Project>\n`;
}

// ------------------------------------------------------------------ servidor local
async function api(url, cuerpo) {
  const r = await fetch(url, cuerpo ? { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(cuerpo) } : {});
  const j = await r.json().catch(() => ({ error: `Respuesta no válida (${r.status})` }));
  if (!r.ok && !("salida" in j)) throw new Error(j.error || `Error ${r.status}`);
  return j;
}

async function abrirRuta(rel) {
  try {
    const j = await api(`/api/abrir?ruta=${encodeURIComponent(rel)}`);
    P = leerXml(j.xml);
    ruta = j.ruta; generadores = j.generadores || [];
    sel.clear(); colapsados.clear(); pilaDeshacer = []; pilaRehacer = [];
    marcarSucio(false);
    history.replaceState(null, "", "#" + ruta);
    render();
    if (!anchosManuales) autoAjustarTodo();
    const T = P.tareas;
    if (T.length) $("#cuerpoGantt").scrollLeft = Math.max(0, (Math.min(...T.map((t) => t.ini)) - d0) * escala - 30);
    estado(`Abierto: ${ruta}` + (P.avisos.length ? ` · ${P.avisos.join(" ")}` : ""));
  } catch (e) { estado(`No se pudo abrir: ${e.message}`, true); }
}

async function abrirDialogo() {
  if (sucio && !confirm("Hay cambios sin guardar. ¿Abrir otro proyecto de todos modos?")) return;
  const dlg = $("#dlgAbrir"), lista = $("#listaAbrir"), filtro = $("#filtroAbrir");
  lista.innerHTML = "<li>Buscando…</li>";
  dlg.showModal();
  let items = [];
  try { items = (await api("/api/proyectos")).proyectos; } catch (e) { lista.innerHTML = `<li>${esc(e.message)}</li>`; return; }
  const pintar = () => {
    const q = filtro.value.toLowerCase();
    const vis = items.filter((it) => it.ruta.toLowerCase().includes(q));
    lista.innerHTML = vis.length ? vis.map((it) => {
      const partesRuta = it.ruta.split("/");
      return `<li tabindex="0" data-ruta="${esc(it.ruta)}"><b>${esc(partesRuta.pop())}</b>${esc(partesRuta.join("/"))}</li>`;
    }).join("") : "<li>No hay archivos XML de MS Project en el repo. Usa «Nuevo».</li>";
  };
  filtro.value = ""; filtro.oninput = pintar; pintar(); filtro.focus();
  lista.onclick = lista.onkeydown = (e) => {
    if (e.type === "keydown" && e.key !== "Enter") return;
    const li = e.target.closest("li[data-ruta]");
    if (!li) return;
    dlg.close(); abrirRuta(li.dataset.ruta);
  };
}

async function guardar() {
  if (!ruta) return guardarComo();
  try {
    const j = await api("/api/guardar", { ruta, xml: escribirXml() });
    generadores = j.generadores || [];
    marcarSucio(false);
    estado(`Guardado: ${ruta}`);
    return true;
  } catch (e) { estado(`No se pudo guardar: ${e.message}`, true); return false; }
}

function guardarComo() {
  return new Promise((resolve) => {
    const dlg = $("#dlgGuardar"), inp = $("#rutaGuardar");
    inp.value = ruta || "";
    dlg.showModal(); inp.focus();
    dlg.onclose = async () => {
      if (dlg.returnValue !== "ok") return resolve(false);
      let r = inp.value.trim().replace(/^\/+/, "");
      if (!r.toLowerCase().endsWith(".xml")) r += ".xml";
      try {
        let j = await api("/api/guardar", { ruta: r, xml: escribirXml(), sobrescribir: false }).catch((e) => ({ error: e.message }));
        if (j.error && /existe/i.test(j.error)) {
          if (!confirm(`Ya existe ${r}. ¿Reemplazarlo?`)) return resolve(false);
          j = await api("/api/guardar", { ruta: r, xml: escribirXml(), sobrescribir: true });
        } else if (j.error) throw new Error(j.error);
        ruta = j.ruta; generadores = j.generadores || [];
        marcarSucio(false); history.replaceState(null, "", "#" + ruta); render();
        estado(`Guardado: ${ruta}`);
        resolve(true);
      } catch (e) { estado(`No se pudo guardar: ${e.message}`, true); resolve(false); }
    };
  });
}

async function generar() {
  if (!(await guardar())) return;
  if (!generadores.length) {
    return mostrarSalida("No hay generador", "En la carpeta de este .xml no hay un generar_*.py que acepte --xml.\n\n" +
      "Convención: un script generar_<formato>.py que reciba «--xml <archivo>» y produzca el Word (y con --pdf, el PDF).\n" +
      "Ejemplo: curso/semana-09-stakeholders-y-lanzamiento/nuestras-entregas/FGAP080_Cronograma_Lanzamiento_NewBit/generar_fgap080.py");
  }
  estado(`Generando con ${generadores[0]}…`);
  try {
    const j = await api("/api/generar", { ruta, pdf: true });
    mostrarSalida(j.ok ? `Listo: ${j.script}` : `Falló ${j.script}`, j.salida || "(sin salida)");
    estado(j.ok ? "Word/PDF generados en la carpeta del proyecto" : "El generador terminó con error", !j.ok);
  } catch (e) { estado(`No se pudo generar: ${e.message}`, true); }
}

function mostrarSalida(titulo, texto) { $("#salidaTitulo").textContent = titulo; $("#salidaTexto").textContent = texto; $("#dlgSalida").showModal(); }

function propiedadesDialogo() {
  const dlg = $("#dlgPropiedades");
  $("#propTitulo").value = P.titulo;
  $("#propInicio").value = aIso(P.inicio);
  $("#propFeriados").value = P.feriados.map(fmtLarga).join("\n");
  dlg.showModal();
  dlg.onclose = () => {
    if (dlg.returnValue !== "ok") return;
    const fer = [];
    for (const lin of $("#propFeriados").value.split(/\n+/).map((s) => s.trim()).filter(Boolean)) {
      const n = leerFecha(lin);
      if (n == null || Number.isNaN(n)) return estado(`Feriado no válido: «${lin}» (usa dd/mm/aaaa)`, true);
      fer.push(n);
    }
    const ini = $("#propInicio").value;
    cambio(() => {
      P.titulo = $("#propTitulo").value.trim() || P.titulo;
      if (ini) P.inicio = aDia(ini);
      P.feriados = [...new Set(fer)].sort((x, y) => x - y);
    }, "Proyecto actualizado");
  };
}

// ------------------------------------------------------------------ exportar PNG (tabla + Gantt, como la vista de MS Project)
function exportarPng() {
  calcular();
  const filas = visibles;
  const colsT = [["", 34], ["Nombre de tarea", 330], ["Duración", 70], ["Comienzo", 96], ["Fin", 96]];
  const wT = colsT.reduce((s, c) => s + c[1], 0);
  const cab = $("#svgCab"), cuerpo = $("#svgGantt");
  const wG = +cuerpo.getAttribute("width"), H = CAB + filas.length * FILA + 6;
  const css = getComputedStyle(document.documentElement);
  const v = (n) => css.getPropertyValue(n).trim();
  let s = `<svg xmlns="${SVGNS}" width="${wT + wG}" height="${H}" font-family="Segoe UI, Arial, sans-serif" font-size="12">` +
    `<style>.barra{fill:${v("--barra")};stroke:${v("--barra-borde")}}.resumen-barra,.hito{fill:${v("--resumen")}}.flecha{stroke:${v("--flecha")};fill:none}` +
    `.punta{fill:${v("--flecha")}}.finde{fill:${v("--finde")}}.linea-sem{stroke:#dedede}.linea-hoy,.fila-sel,.asa{display:none}.txt-cab,.txt-hito{font-size:11px}</style>` +
    `<rect width="100%" height="100%" fill="#fff"/><rect width="${wT}" height="${CAB}" fill="#e8e8e8"/>` +
    `<line x1="0" y1="${CAB}" x2="${wT}" y2="${CAB}" stroke="${v("--verde")}" stroke-width="2"/>`;
  let x = 0;
  for (const [tit, w] of colsT) { s += `<text x="${x + 6}" y="${CAB - 10}" font-weight="600">${esc(tit)}</text><line x1="${x + w}" y1="0" x2="${x + w}" y2="${H}" stroke="#d4d4d4"/>`; x += w; }
  filas.forEach((t, i) => {
    const y = CAB + i * FILA, yt = y + 17, b = t.resumen ? ' font-weight="700"' : "";
    s += `<line x1="0" y1="${y + FILA}" x2="${wT}" y2="${y + FILA}" stroke="#ececec"/>` +
      `<text x="17" y="${yt}" text-anchor="middle" fill="#666" font-size="11">${t.id}</text>` +
      `<text x="${34 + 6 + (t.nivel - 1) * 16}" y="${yt}"${b}>${esc(t.nombre)}</text>` +
      `<text x="${364 + 6}" y="${yt}"${b}>${fmtDur(t.durMostrar)}</text>` +
      `<text x="${434 + 6}" y="${yt}"${b}>${fmtMs(t.ini)}</text><text x="${530 + 6}" y="${yt}"${b}>${fmtMs(t.fin)}</text>`;
  });
  s += `<g transform="translate(${wT},0)"><rect width="${wG}" height="${CAB}" fill="#e8e8e8"/>${cab.innerHTML}` +
    `<line x1="0" y1="${CAB}" x2="${wG}" y2="${CAB}" stroke="${v("--verde")}" stroke-width="2"/></g>` +
    `<g transform="translate(${wT},${CAB})">${cuerpo.innerHTML}</g></svg>`;
  const img = new Image();
  img.onload = () => {
    const k = 2, c = document.createElement("canvas");
    c.width = (wT + wG) * k; c.height = H * k;
    const g = c.getContext("2d"); g.scale(k, k); g.drawImage(img, 0, 0);
    c.toBlob((blob) => {
      const a = document.createElement("a");
      a.href = URL.createObjectURL(blob);
      a.download = (ruta ? ruta.split("/").pop().replace(/\.xml$/i, "") : "cronograma") + "_gantt.png";
      a.click();
      setTimeout(() => URL.revokeObjectURL(a.href), 4000);
      estado("PNG descargado");
    });
  };
  img.onerror = () => estado("No se pudo crear la imagen", true);
  img.src = "data:image/svg+xml;charset=utf-8," + encodeURIComponent(s);
}

// ------------------------------------------------------------------ scroll, divisor y eventos
function sincronizarScroll() {
  const g = $("#cuerpoGantt"), t = $("#cuerpoTabla");
  $("#cabGantt").scrollLeft = g.scrollLeft;
  if (t.scrollTop !== g.scrollTop) t.scrollTop = g.scrollTop;
}

function iniciar() {
  document.querySelector(".cinta").addEventListener("click", (e) => {
    const b = e.target.closest("button[data-accion]");
    if (b) acciones[b.dataset.accion]();
  });
  const cuerpo = $("#cuerpoTabla");
  cuerpo.addEventListener("change", (e) => {
    if (e.target.matches("input[data-k]")) confirmarCelda(e.target.closest(".fila").dataset.uid, e.target.dataset.k, e.target.value);
  });
  cuerpo.addEventListener("focusin", (e) => {
    const f = e.target.closest(".fila");
    if (f && f.dataset.uid !== "nueva" && !sel.has(+f.dataset.uid)) { sel = new Set([+f.dataset.uid]); ancla = +f.dataset.uid; pintarSeleccion(); }
  });
  cuerpo.addEventListener("mousedown", (e) => {
    const tg = e.target.closest("[data-toggle]");
    if (tg) { e.preventDefault(); const u = +tg.dataset.toggle; colapsados.has(u) ? colapsados.delete(u) : colapsados.add(u); render(); return; }
    const id = e.target.closest(".c-id");
    if (id) { const f = id.closest(".fila"); if (f.dataset.uid !== "nueva") { e.preventDefault(); document.activeElement?.blur(); seleccionar(+f.dataset.uid, e); } }
  });
  cuerpo.addEventListener("keydown", (e) => {
    const inp = e.target.closest("input[data-k]");
    if (!inp || e.altKey) return;
    const f = inp.closest(".fila"), k = inp.dataset.k;
    const mov = { Enter: 1, ArrowDown: 1, ArrowUp: -1 }[e.key];
    if (mov === undefined || (e.key === "Enter" && e.shiftKey)) { if (e.key === "Escape") { inp.value = inp.dataset.orig ?? ""; inp.blur(); } return; }
    e.preventDefault();
    const filas = [...cuerpo.querySelectorAll(".fila")];
    const destino = filas[filas.indexOf(f) + mov];
    const uidDestino = destino ? destino.dataset.uid : f.dataset.uid;
    const cuantas = P.tareas.length;
    if (inp.value !== inp.dataset.orig) confirmarCelda(f.dataset.uid, k, inp.value);
    // si se creó una tarea desde la fila nueva, seguir en la nueva fila vacía
    const objetivo = f.dataset.uid === "nueva" && P.tareas.length > cuantas ? "nueva" : uidDestino;
    const fila = cuerpo.querySelector(`.fila[data-uid="${objetivo}"]`);
    const sig = fila && (fila.querySelector(`input[data-k="${k}"]`) || fila.querySelector("input"));
    if (sig) { sig.focus(); sig.select(); }
  });
  const g = $("#cuerpoGantt");
  g.addEventListener("scroll", sincronizarScroll);
  cuerpo.addEventListener("scroll", () => {
    $("#cabTabla").scrollLeft = cuerpo.scrollLeft;
    if (g.scrollTop !== cuerpo.scrollTop) g.scrollTop = cuerpo.scrollTop;
  });
  cuerpo.addEventListener("wheel", (e) => { if (Math.abs(e.deltaY) > Math.abs(e.deltaX)) { g.scrollTop += e.deltaY; e.preventDefault(); } }, { passive: false });
  const svg = $("#svgGantt");
  svg.addEventListener("pointerdown", inicioArrastre);
  window.addEventListener("pointermove", moverArrastre);
  window.addEventListener("pointerup", finArrastre);
  svg.addEventListener("dblclick", (e) => { const b = e.target.closest("[data-uid]"); if (b) enfocar(+b.dataset.uid, "nombre"); });
  svg.addEventListener("click", (e) => {
    if (e.target.closest("[data-uid]")) return;
    const i = Math.floor(e.offsetY / FILA);
    if (visibles[i]) seleccionar(visibles[i].uid, e);
  });
  // divisor arrastrable
  const div = $("#divisor"), pt = $("#panelTabla");
  div.addEventListener("pointerdown", (e) => {
    const x0 = e.clientX, w0 = pt.offsetWidth;
    const mv = (ev) => { pt.style.width = Math.max(260, Math.min(window.innerWidth - 200, w0 + ev.clientX - x0)) + "px"; };
    const up = () => { window.removeEventListener("pointermove", mv); window.removeEventListener("pointerup", up); };
    window.addEventListener("pointermove", mv); window.addEventListener("pointerup", up);
  });
  // atajos de teclado
  window.addEventListener("keydown", (e) => {
    const mod = e.metaKey || e.ctrlKey;
    const enInput = e.target.matches?.("input, textarea");
    const textoEditado = enInput && e.target.value !== e.target.dataset.orig;
    if (mod && e.key.toLowerCase() === "s") { e.preventDefault(); document.activeElement?.blur(); setTimeout(guardar); }
    else if (mod && e.key.toLowerCase() === "o") { e.preventDefault(); abrirDialogo(); }
    else if (mod && !e.shiftKey && e.key.toLowerCase() === "z" && !textoEditado) { e.preventDefault(); document.activeElement?.blur(); deshacer(); }
    else if (mod && (e.key.toLowerCase() === "y" || (e.shiftKey && e.key.toLowerCase() === "z")) && !textoEditado) { e.preventDefault(); rehacer(); }
    else if (e.altKey && e.shiftKey && e.key === "ArrowRight") { e.preventDefault(); document.activeElement?.blur(); acciones.sangria(); }
    else if (e.altKey && e.shiftKey && e.key === "ArrowLeft") { e.preventDefault(); document.activeElement?.blur(); acciones.anularSangria(); }
    else if (e.altKey && e.shiftKey && e.key === "ArrowUp") { e.preventDefault(); document.activeElement?.blur(); acciones.subir(); }
    else if (e.altKey && e.shiftKey && e.key === "ArrowDown") { e.preventDefault(); document.activeElement?.blur(); acciones.bajar(); }
    else if (e.key === "Insert") { e.preventDefault(); acciones.insertar(); }
    else if (mod && (e.key === "Delete" || e.key === "Backspace") && !enInput) { e.preventDefault(); acciones.eliminar(); }
    else if (!enInput && (e.key === "Delete") && sel.size) { e.preventDefault(); acciones.eliminar(); }
  });
  window.addEventListener("beforeunload", (e) => { if (sucio) { e.preventDefault(); e.returnValue = ""; } });
  iniciarColumnas();
  const inicial = decodeURIComponent(location.hash.slice(1));
  render();
  if (inicial) abrirRuta(inicial); else estado("Listo · Abre un .xml del repo o crea uno nuevo");
}

document.addEventListener("DOMContentLoaded", iniciar);
