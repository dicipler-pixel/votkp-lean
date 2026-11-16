/* SCRIPT: TB-LAYER-V3
   Three Balls on the Field, v3 — one light carried through all three balls by the single ball's own law; eyes (or layers) on together, each with its own switch and, where it has one, its own timing.
   Jeromie Beasley. 15 Nov 2026. AI-assisted.
   Ball A is the page's ball. Ball B is the same space seen from one step out along A's I arm; ball C from one step out along J.
   The page traces its light once, from the centre of the ball that was kicked. That same light is then drawn in each ball as that
   ball sees it: every ray point X is carried to X' = G_b^-1 G_s X (G = the peel step that takes A's centre to that ball's centre).
   A ray that crosses the shared face in one ball therefore comes in through the matching face of the next, at the matching point
   and angle, with the crossing share T = 1 - Γ² of its energy. Nothing else passes energy between the balls: no added link strength.
   Host adapter window.__TBHOST = { S3, WORLD, tau(), S(), light:[objects], kind, tr() } is set by the page app. Needs Mixer3D only. */
(function(){
"use strict";
const H = window.__TBHOST, M = window.Mixer3D, T = M.T, S3 = H.S3, WORLD = H.WORLD, RB = 2.6, PI = Math.PI;
const fmt = (x,n) => Number.isFinite(x) ? x.toFixed(n == null ? 4 : n) : '—', sci = x => Number.isFinite(x) ? x.toExponential(1) : '—';
const NAMES = ['A','B','C'], COL = ['#fff2cc', '#ff8d7c', '#63d3ff'];
const X = { on:true, src:0, eps:0 };
/* ---- hyperboloid helpers: vectors (t, i, j, k) ---- */
const UNIT = [[1,0,0],[0,1,0],[0,0,1]], letterDir = k => UNIT[k>>1].map(v => (k&1) ? -v : v);
function boost(u, r){ const c = Math.cosh(r), s = Math.sinh(r), B = [[c, s*u[0], s*u[1], s*u[2]],[s*u[0],0,0,0],[s*u[1],0,0,0],[s*u[2],0,0,0]]; for(let i=0;i<3;i++) for(let j=0;j<3;j++) B[i+1][j+1] = (i===j?1:0) + (c-1)*u[i]*u[j]; return B; }
const mm = (A,B) => A.map(r => [0,1,2,3].map(j => r[0]*B[0][j]+r[1]*B[1][j]+r[2]*B[2][j]+r[3]*B[3][j]));
const mv = (A,v) => A.map(r => r[0]*v[0]+r[1]*v[1]+r[2]*v[2]+r[3]*v[3]);
const mink = (p,q) => p[0]*q[0]-p[1]*q[1]-p[2]*q[2]-p[3]*q[3];
const I4 = () => [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]];
/* the step that takes A's centre to each ball's centre; eps is a deliberate placement error of B and C along their arms */
function cells(S){ return [I4(), boost(UNIT[0], S.r[0] + X.eps), boost(UNIT[1], S.r[1] + X.eps)]; }
function cellsInv(S){ return [I4(), boost(UNIT[0], -(S.r[0] + X.eps)), boost(UNIT[1], -(S.r[1] + X.eps))]; }
const chart = (S, b) => mm(cellsInv(S)[b], cells(S)[X.src]);            /* what ball b sees of light sourced at the centre of ball src */
/* letters from the kicked ball to each other ball, in the kicked ball's own frame */
const REL = [ { 1:[0], 2:[2] }, { 0:[1], 2:[1,2] }, { 0:[3], 1:[3,0] } ];
/* ---- the field objects ---- */
const FIELD = new T.Group(); S3.world.add(FIELD);
const seg = (n, op) => { const g = new T.BufferGeometry(); g.setAttribute('position', new T.BufferAttribute(new Float32Array(n*6), 3)); g.setAttribute('color', new T.BufferAttribute(new Float32Array(n*6), 3));
  const m = new T.LineSegments(g, new T.LineBasicMaterial({ vertexColors:true, transparent:true, opacity:op, depthWrite:false, blending:T.AdditiveBlending })); m.frustumCulled = false; FIELD.add(m); let i = 0;
  return { reset(){ i = 0; }, add(a, b, c){ if(i >= n) return; const p = g.attributes.position, q = g.attributes.color; p.setXYZ(2*i, a.x, a.y, a.z); p.setXYZ(2*i+1, b.x, b.y, b.z); q.setXYZ(2*i, c[0], c[1], c[2]); q.setXYZ(2*i+1, c[0], c[1], c[2]); i++; }, done(){ g.setDrawRange(0, 2*i); g.attributes.position.needsUpdate = g.attributes.color.needsUpdate = true; } }; };
const lens = seg(3*128, 1); const labels = NAMES.map((n, i) => { const l = M.label('ball ' + n, COL[i], 0.42); FIELD.add(l); return l; });
let pos = [new T.Vector3(), new T.Vector3(), new T.Vector3()], HO = null;
function layout(S){ const dI = RB*(1 + Math.tanh((S.h[0] + X.eps)/2)), dJ = RB*(1 + Math.tanh((S.h[1] + X.eps)/2)), P = [new T.Vector3(0,0,0), new T.Vector3(dI,0,0), new T.Vector3(0,0,-dJ)];
  const c = P[0].clone().add(P[1]).add(P[2]).multiplyScalar(1/3); P.forEach(p => p.sub(c)); return P; }
/* ---- what the page's own trace says crosses into each ball (hand-over), and how well the crossings sit on the next ball's face ---- */
function handover(S){ const enter = {}, kinks = {}; let nR = 1;
  if(H.kind === 'surprise'){ const TR = H.tr(); nR = TR.nRays; const keyOf = new Map(); TR.cells.forEach((c, key) => keyOf.set(c.g, key));
    for(const e of TR.events){ if(e.total) continue; const ck = keyOf.get(e.g), w = ck.split('').map(Number), back = w.length && w[w.length-1] === (e.k^1), nk = (back ? w.slice(0,-1) : w.concat(e.k)).join('');
      enter[nk] = (enter[nk]||0) + e.flux*e.T; if(ck === '') (kinks[e.k] = kinks[e.k] || []).push(mv(e.g, e.X)); } }
  else { const segs = S.segs; let mx = 0; for(const g of segs){ mx = Math.max(mx, g.ray); if(g.end !== 'face' || g.sp.total) continue; const nk = g.w2.join(''); enter[nk] = (enter[nk]||0) + g.flux*g.sp.T; if(g.word.length === 0) (kinks[g.k] = kinks[g.k] || []).push(g.hit); } nR = mx + 1; }
  const out = { share:[0,0,0], gap:[NaN,NaN,NaN], nk:[0,0,0] }; let got = 0;
  for(const b of [0,1,2]){ if(b === X.src) continue; const w = REL[X.src][b]; out.share[b] = (enter[w.join('')]||0)/nR; got += out.share[b];
    /* just right: every point where a ray crosses out of the kicked ball toward ball b must lie on ball b's own face toward the kicked ball */
    if(w.length === 1){ const k = w[0], back = k^1, a = back>>1, hB = S.h[a], u = letterDir(back), N = [Math.sinh(hB), Math.cosh(hB)*u[0], Math.cosh(hB)*u[1], Math.cosh(hB)*u[2]], Mb = chart(S, b); let worst = 0;
      for(const Xk of (kinks[k]||[])) worst = Math.max(worst, Math.abs(Math.asinh(mink(mv(Mb, Xk), N)))); out.gap[b] = worst; out.nk[b] = (kinks[k]||[]).length; } }
  out.share[X.src] = 1 - got; return out; }
/* ---- carry a drawn point of the ball by a step: world (x, y, z)/RB = (i, k, -j) ---- */
function carry(src, dst, n, Mx){ for(let o=0;o<n*3;o+=3){ const bi = src[o]/RB, bk = src[o+1]/RB, bj = -src[o+2]/RB, r2 = bi*bi + bj*bj + bk*bk; if(r2 === 0){ dst[o] = dst[o+1] = dst[o+2] = 0; continue; }
    let q0, q1, q2, q3, s;
    if(r2 < 0.9996){ const d = 1 - r2, p0 = (1 + r2)/d, p1 = 2*bi/d, p2 = 2*bj/d, p3 = 2*bk/d;
      q0 = Mx[0][0]*p0 + Mx[0][1]*p1 + Mx[0][2]*p2 + Mx[0][3]*p3; q1 = Mx[1][0]*p0 + Mx[1][1]*p1 + Mx[1][2]*p2 + Mx[1][3]*p3; q2 = Mx[2][0]*p0 + Mx[2][1]*p1 + Mx[2][2]*p2 + Mx[2][3]*p3; q3 = Mx[3][0]*p0 + Mx[3][1]*p1 + Mx[3][2]*p2 + Mx[3][3]*p3; s = RB/(1 + q0); }
    else { const r = Math.sqrt(r2), p1 = bi/r, p2 = bj/r, p3 = bk/r;      /* a point on the rim is a direction of light: carried as a null vector */
      q0 = Mx[0][0] + Mx[0][1]*p1 + Mx[0][2]*p2 + Mx[0][3]*p3; q1 = Mx[1][0] + Mx[1][1]*p1 + Mx[1][2]*p2 + Mx[1][3]*p3; q2 = Mx[2][0] + Mx[2][1]*p1 + Mx[2][2]*p2 + Mx[2][3]*p3; q3 = Mx[3][0] + Mx[3][1]*p1 + Mx[3][2]*p2 + Mx[3][3]*p3; s = RB*r/q0; }
    dst[o] = q1*s; dst[o+1] = q3*s; dst[o+2] = -q2*s; } }
const LIGHT = H.light.map(o => ({ o, attr:o.geometry.attributes.position, back:new Float32Array(o.geometry.attributes.position.array.length) }));
function count(L){ const dr = L.o.geometry.drawRange, c = L.attr.count; return Math.min(c, Number.isFinite(dr.count) ? dr.start + dr.count : c); }
/* ---- draw the three balls ---- */
const R = S3.renderer, cam = S3.camera, scene = S3.scene, orig = R.render.bind(R), bg = scene.background ? scene.background.clone() : new T.Color(0x05070b);
R.render = function(sc, cm){ if(sc !== scene || !X.on){ FIELD.visible = false; WORLD.position.set(0,0,0); R.autoClear = true; scene.background = bg; return orig(sc, cm); }
  const S = H.S(); pos = layout(S); HO = handover(S);
  /* the ring where two rims meet, lit by the share of the kicked light that crosses between those two balls */
  lens.reset(); [[0,1],[0,2],[1,2]].forEach(([i,j]) => { const a = pos[i], b = pos[j], ab = b.clone().sub(a), D = ab.length(); if(D >= 2*RB) return; const n = ab.clone().multiplyScalar(1/D), mid = a.clone().add(b).multiplyScalar(0.5);
    const direct = (i === X.src || j === X.src), f = direct ? Math.sqrt(Math.min(1, HO.share[i === X.src ? j : i]*4)) : 0, c = [0.18 + 0.8*f, 0.2 + 0.75*f, 0.24 + 0.6*f];
    const rr = Math.sqrt(RB*RB - D*D/4), e1 = (Math.abs(n.y) < 0.9 ? new T.Vector3(0,1,0) : new T.Vector3(1,0,0)).cross(n).normalize(), e2 = n.clone().cross(e1); let prev = null;
    for(let s=0;s<=128;s++){ const t = 2*PI*s/128, p = mid.clone().addScaledVector(e1, rr*Math.cos(t)).addScaledVector(e2, rr*Math.sin(t)); if(prev) lens.add(prev, p, c); prev = p; } }); lens.done();
  for(let i=0;i<3;i++) labels[i].position.set(pos[i].x, pos[i].y + RB + 0.35, pos[i].z);
  const V = S3.view, Dc = V.dist*2.0*(window.innerWidth < 640 ? 1.5 : 1), pt = Math.max(-1.3, Math.min(1.35, V.pitch + 0.55)), yw = V.yaw + 0.55;
  cam.position.set(Dc*Math.cos(pt)*Math.sin(yw), Dc*Math.sin(pt), Dc*Math.cos(pt)*Math.cos(yw)); cam.lookAt(0, 0, 0); cam.updateMatrixWorld();
  scene.background = null; R.autoClear = false; R.setClearColor(bg, 1); R.clear();
  const Ns = LIGHT.map(count); LIGHT.forEach((L, k) => L.back.set(L.attr.array.subarray(0, Ns[k]*3)));
  for(let b=0;b<3;b++){ const Mx = chart(S, b); LIGHT.forEach((L, k) => { if(b === X.src) L.attr.array.set(L.back.subarray(0, Ns[k]*3)); else carry(L.back, L.attr.array, Ns[k], Mx); L.attr.needsUpdate = true; });
    WORLD.position.copy(pos[b]); FIELD.visible = b === 0; orig(sc, cm); }
  LIGHT.forEach((L, k) => { L.attr.array.set(L.back.subarray(0, Ns[k]*3)); L.attr.needsUpdate = true; }); WORLD.position.set(0,0,0); };
/* ---- panel ---- */
const css = document.createElement('style'); css.textContent = `.tb{position:fixed;top:12px;right:12px;width:min(300px,calc(100% - 400px));max-height:calc(100% - 110px);overflow:auto;background:var(--panel,rgba(9,13,20,.86));border:1px solid var(--edge,#1f2a38);border-radius:8px;padding:11px 12px;font-size:12px;color:var(--ink,#dfe7ef);backdrop-filter:blur(6px);z-index:5}
.tb h2{margin:0 0 4px;font-size:13px;letter-spacing:.08em;text-transform:uppercase;font-family:var(--head,inherit)}.tb p{margin:4px 0 8px;color:var(--dim,#8a9aab);font-size:11.5px;line-height:1.5}
.tb .r{display:flex;flex-wrap:wrap;gap:5px;margin:5px 0;align-items:center}.tb button{font-size:11.5px;padding:4px 8px;background:#0e1520;color:inherit;border:1px solid var(--edge,#1f2a38);border-radius:5px;cursor:pointer}.tb button[aria-pressed=true]{border-color:#f2c14e;color:#f2c14e}
.tb .row{display:flex;justify-content:space-between;gap:10px;padding:4px 0;border-bottom:1px solid rgba(31,42,56,.6);color:var(--dim,#8a9aab)}.tb .row b{font-family:var(--mono,monospace);font-weight:400;color:var(--ink,#dfe7ef);text-align:right;font-size:11px;white-space:pre-wrap}
.tb .g{font-size:10px;color:var(--faint,#55657a);margin:-1px 0 2px}.tb input{accent-color:#63d3ff;width:130px;vertical-align:middle}.tb summary{cursor:pointer;color:var(--dim,#8a9aab)}body.clean .tb{display:none}body.linked .tb,body.linked .panel,body.linked .strip,body.linked #back{display:none !important}
@media (max-width:900px){.tb{top:auto;bottom:60px;left:8px;right:8px;width:auto;max-height:34%}}`; document.head.append(css);
document.body.insertAdjacentHTML('beforeend', `<div class="tb" id="tb"><h2>Three balls on the field</h2>
<details><summary>What this shows</summary><p>Three whole balls of the same kind. Ball B is the same space as ball A seen from one step out along the I arm, and ball C from one step out along the J arm. The light is traced once, from the centre of the ball you kick, by this page’s own law: at each face a ray divides by the step law, bends by the conserved a sin²θ, or is returned whole. That one light is drawn in every ball as that ball sees it, so a ray that crosses the shared face in one ball comes in through the matching face of the next, at the matching point and angle, with the crossing share of the energy. No other rule passes energy between the balls. Move a ball off its place with the slider and the crossings no longer sit on its face: the readout measures by how much.</p></details>
<div class="r"><button id="tb_three" aria-pressed="true">Three balls</button><button id="tb_one" aria-pressed="false">One ball</button></div>
<div class="r"><button data-kick="0" aria-pressed="true">Kick ball A</button><button data-kick="1" aria-pressed="false">Kick ball B</button><button data-kick="2" aria-pressed="false">Kick ball C</button></div>
<div class="r"><label>B and C moved off their place by <span id="tb_eo">0.00</span> <input id="tb_eps" type="range" min="-0.6" max="0.6" step="0.01" value="0"></label><button id="tb_fit">Just right</button></div><div class="row"><span>crosses into</span><b id="tb_sh"></b></div><details><summary>All the numbers</summary><div id="tb_rows"></div></details></div>`);
const $ = id => document.getElementById(id);
function setOn(b){ X.on = b; $('tb_three').setAttribute('aria-pressed', b); $('tb_one').setAttribute('aria-pressed', !b); }
$('tb_three').addEventListener('click', () => setOn(true)); $('tb_one').addEventListener('click', () => setOn(false));
document.querySelectorAll('#tb button[data-kick]').forEach(b => b.addEventListener('click', () => { X.src = +b.dataset.kick; document.querySelectorAll('#tb button[data-kick]').forEach(q => q.setAttribute('aria-pressed', q === b)); }));
$('tb_eps').addEventListener('input', e => { X.eps = +e.target.value; $('tb_eo').textContent = X.eps.toFixed(2); }); $('tb_fit').addEventListener('click', () => { X.eps = 0; $('tb_eps').value = 0; $('tb_eo').textContent = '0.00'; });
const row = (a, b, g) => `<div class="row"><span>${a}</span><b>${b}</b></div>` + (g ? `<div class="g">${g}</div>` : '');
function rows(){ if(!HO) return; const S = H.S(), s = X.src, others = [0,1,2].filter(b => b !== s); let h = '';
  h += row('kicked: ball ' + NAMES[s], 'steps  I ' + fmt(S.r[0], 3) + '   J ' + fmt(S.r[1], 3), 'B is one I step from A, C one J step from A; B and C reach each other through A');
  h += row('share of the kicked light that crosses into each ball', others.map(b => NAMES[b] + ' ' + fmt(HO.share[b], 4)).join('   '), 'summed from this page’s own trace: every crossing carries flux × T, T = 1 − R by the step law');
  h += row('the rest (stays in ball ' + NAMES[s] + ', goes on elsewhere, or reaches the rim)', fmt(HO.share[s], 4));
  h += row('placement: the two copies of the shared face stand apart by', fmt(Math.abs(X.eps), 3), 'zero when the ball sits exactly one step out');
  for(const b of others){ if(Number.isFinite(HO.gap[b])) h += row('crossings toward ball ' + NAMES[b] + ': farthest from ball ' + NAMES[b] + '’s own face', sci(HO.gap[b]) + '  (' + HO.nk[b] + ' crossings)', 'each ray leaves ball ' + NAMES[s] + ' at a point; in ball ' + NAMES[b] + ' that point must lie on the face it comes in through');
    else h += row('ball ' + NAMES[b] + ' is reached through ball A', 'two faces'); }
  $('tb_rows').innerHTML = h; $('tb_sh').textContent = others.map(b => NAMES[b] + ' ' + fmt(HO.share[b], 3)).join('   '); }
setInterval(rows, 250);

/* ---- eyes on together (Mixer ball): any set of eyes shown at once; each part of the object takes the strongest weight among the eyes that are on ---- */
const ON = new Set();
if(H.eyes){ const box = document.createElement('div'); box.innerHTML = `<div class="g" style="margin-top:8px">Eyes on together (the open eye is always on)</div><div class="r" id="tb_eyes">` + H.eyes.map(e => `<button data-eye="${e.id}" aria-pressed="false" title="${e.title.replace(/"/g,'')}">${e.id}</button>`).join('') + `<button id="tb_eall">all</button><button id="tb_enone">only the open eye</button></div>
<div class="g">Own timing (speed of each moving part against the clock)</div><div class="r">` + [['rays','rays'],['stack','layers'],['loop','rotation'],['rim','rim']].map(([k,n]) => `<label style="font-size:11px">${n} <span id="tb_tv_${k}">1.0</span> <input data-tim="${k}" type="range" min="0" max="3" step="0.1" value="1" style="width:70px"></label>`).join('') + `</div>`;
  $('tb').insertBefore(box, $('tb').querySelector('details:last-of-type'));
  const paint = () => document.querySelectorAll('#tb_eyes button[data-eye]').forEach(b => b.setAttribute('aria-pressed', ON.has(b.dataset.eye)));
  document.querySelectorAll('#tb_eyes button[data-eye]').forEach(b => b.addEventListener('click', () => { ON.has(b.dataset.eye) ? ON.delete(b.dataset.eye) : ON.add(b.dataset.eye); paint(); }));
  $('tb_eall').addEventListener('click', () => { H.eyes.forEach(e => ON.add(e.id)); paint(); }); $('tb_enone').addEventListener('click', () => { ON.clear(); paint(); });
  document.querySelectorAll('#tb input[data-tim]').forEach(i => i.addEventListener('input', () => { H.TSP[i.dataset.tim] = +i.value; $('tb_tv_' + i.dataset.tim).textContent = (+i.value).toFixed(1); }));
  setInterval(() => { const cur = H.cur(), ids = [cur].concat([...ON]); for(const c in H.EMPH[cur]){ let w = 0; for(const id of ids) w = Math.max(w, H.EMPH[id][c]); H.WT[c] = w; } }, 80);
  const base = rows; const more = () => { const cur = H.cur(); let h = ''; for(const e of H.eyes){ if(e.id === cur || !ON.has(e.id)) continue; let rr = []; try { rr = e.rows(); } catch(err){ rr = [['readout', 'not available while this eye is not the open one']]; }
      h += `<div class="g" style="margin-top:8px;color:#f2c14e">${e.title}</div>` + rr.map(r => row(r[0], r[1])).join(''); } let el = $('tb_more'); if(!el){ el = document.createElement('div'); el.id = 'tb_more'; $('tb_rows').after(el); } el.innerHTML = h; };
  setInterval(more, 400); }
/* ---- layers on together (white ball): each layer of the drawing has its own switch ---- */
if(H.layers){ const names = Object.keys(H.layers), box = document.createElement('div'); box.innerHTML = `<div class="g" style="margin-top:8px">Layers, each with its own switch</div><div class="r" id="tb_lay">` + names.map(n => `<button data-lay="${n}" aria-pressed="true">${n}</button>`).join('') + `</div>`;
  $('tb').insertBefore(box, $('tb').querySelector('details:last-of-type'));
  document.querySelectorAll('#tb_lay button').forEach(b => b.addEventListener('click', () => { const on = b.getAttribute('aria-pressed') !== 'true'; b.setAttribute('aria-pressed', on); H.layers[b.dataset.lay].forEach(o => o.visible = on); })); }
window.__tb = { X, rows, setOn, ON, get HO(){ return HO; }, chart:b => chart(H.S(), b) };
})();
