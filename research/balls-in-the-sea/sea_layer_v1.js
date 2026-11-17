/* SCRIPT: SEA-LAYER-V1
   The balls in the sea: drawing and controls. Jeromie Beasley. 17 Nov 2026. AI-assisted.
   The Flock of Balls on the Field page is left as it is. This layer adds the sea under its balls (SEA-MATH-V1) and draws it on the same
   field: along every link, how far the sea's filling stands from rest; on every ball, how far the sea's spin stands from rest; between
   balls, the weight between them. Three ways the sea can move are kept side by side, with the ends, the feed and the push as switches.
   Nothing is placed on the right of the screen. Needs the Flock page (window.__FL, window.__TBHOST), Mixer3D, MM, FL, SEA and #sea_rest. */
(function(){
"use strict";
const H = window.__TBHOST, M3 = window.Mixer3D, T = M3.T, S3 = H.S3, WORLD = H.WORLD, FP = window.__FL, RB = 2.6, MP = 56, NL = 18;
const REST = JSON.parse(document.getElementById('sea_rest').textContent), RC = {};
const FIELD = S3.world.children.filter(c => c !== WORLD && c.isGroup).pop(), G = new T.Group(); FIELD.add(G);
const O = { on:true, machine:'tied', ends:'sealed', feed:'kick', push:false, show:{ links:true, balls:true, ties:true } };
let E = null, Wseen = null, okey = '', acc = 0, lastTau = null, RD = null, pos = [], building = false, first = null, msStep = 0, note = '';
const hyp3 = v => new T.Vector3(v[0], v[2], -v[1]);
const seg = (n, op) => { const g = new T.BufferGeometry(); g.setAttribute('position', new T.BufferAttribute(new Float32Array(n*6), 3)); g.setAttribute('color', new T.BufferAttribute(new Float32Array(n*6), 3));
  const m = new T.LineSegments(g, new T.LineBasicMaterial({ vertexColors:true, transparent:true, opacity:op, depthWrite:false, depthTest:false, blending:T.AdditiveBlending })); m.frustumCulled = false; m.renderOrder = 8; G.add(m); let i = 0;
  return { mesh:m, reset(){ i = 0; }, add(a, b, c){ if(i >= n) return; const p = g.attributes.position, q = g.attributes.color; p.setXYZ(2*i, a.x, a.y, a.z); p.setXYZ(2*i+1, b.x, b.y, b.z); q.setXYZ(2*i, c[0], c[1], c[2]); q.setXYZ(2*i+1, c[0], c[1], c[2]); i++; }, done(){ g.setDrawRange(0, 2*i); g.attributes.position.needsUpdate = g.attributes.color.needsUpdate = true; } }; };
const pts = (n, size) => { const p = M3.points(n, size); p.material.depthTest = false; p.renderOrder = 9; p.frustumCulled = false; G.add(p); return p; };
const seaF = pts(NL*MP, 0.3), seaB = pts(NL*MP, 0.3), heads = pts(7, 0.7), arrows = seg(7, 1), ties = seg(21, 1), zero3 = [0,0,0], _u = new T.Vector3();
function restOf(N, clocks, ends){ const k = N + '|' + clocks + '|' + (ends === 'container' ? 'container' : 'sealed'); if(RC[k] !== undefined) return RC[k]; const r = REST[k]; if(!r) return RC[k] = null;
  const bin = atob(r.b64), u8 = new Uint8Array(bin.length); for(let i=0;i<bin.length;i++) u8[i] = bin.charCodeAt(i); return RC[k] = { M:r.M, rank:r.rank, margin:r.margin, h:r.h, tri:new Float32Array(u8.buffer) }; }
function build(){ const W = FP.W; Wseen = W; okey = JSON.stringify(O); building = true; E = null; RD = null; first = null; note = 'Building the sea…'; ui();
  setTimeout(() => { const N = W.N, z = W.opts.z.slice(), clocks = W.opts.clocks === 'z' ? 'z' : 'equal', std = z.join(',') === '3,5,7', rest = (O.machine === 'tied' && std) ? restOf(N, clocks, O.ends) : null, h = rest ? rest.h : (N >= 7 ? 0.2 : 0.05);
    try { E = SEA.make(FL, MM, { N, z, clocks, h, machine:O.machine, ends:O.ends, feed:O.feed, push:O.push, rest }); note = E.ok ? '' : E.why; } catch(err){ E = null; note = 'The sea could not be built: ' + err.message; }
    pos = W.balls.map(b => b.arm < 0 ? new T.Vector3() : hyp3(MM.AXES[b.arm]).multiplyScalar(RB*(1 + Math.tanh(b.r/4)))); acc = 0; lastTau = H.tau(); building = false; if(E && E.ok) RD = SEA.read(E); ui(); }, 30); }
function tick(){ if(!FP.X.on || !O.on){ G.visible = false; return; } G.visible = true; if(building) return; if(FP.W !== Wseen || JSON.stringify(O) !== okey){ build(); return; }
  if(!E || !E.ok){ seaF.visible = seaB.visible = heads.visible = arrows.mesh.visible = ties.mesh.visible = false; return; }
  const tau = H.tau(); if(tau < lastTau - 1e-9){ build(); return; } const dt = Math.max(0, Math.min(0.1, tau - lastTau)); lastTau = tau; acc += dt*FP.X.speed; let n = Math.floor(acc/E.h); acc -= n*E.h; n = Math.min(n, 6);
  if(n){ const t0 = performance.now(); for(let k=0;k<n;k++){ SEA.step(E); } msStep = (performance.now() - t0)/n; RD = SEA.read(E); if(first === null && RD.farChange > 1e-6) first = E.t; }
  if(!RD) RD = SEA.read(E); draw(); status(); }
function draw(){ const sh = O.show, W = E.W, cam = S3.camera; _u.setFromMatrixColumn(cam.matrixWorld, 1); seaF.visible = seaB.visible = sh.links && !!E.sm; heads.visible = arrows.mesh.visible = sh.balls; ties.mesh.visible = sh.ties; let np = 0;
  if(sh.links && E.sm) W.links.forEach((l, k) => { const a = pos[l.i], b = pos[l.j], pr = SEA.linkChange(E, k, MP);
    for(let m=0;m<MP;m++){ const p = a.clone().lerp(b, (m + 0.5)/MP), cf = pr.F[m], cb = pr.B[m], f = Math.max(0, Math.min(1, (Math.log10(Math.abs(cf) + 1e-300) + 7)/6)), g = Math.max(0, Math.min(1, (Math.log10(Math.abs(cb) + 1e-300) + 7)/6));
      M3.setPt(seaF, np, p.clone().addScaledVector(_u, 0.16), Math.abs(cf) > 1e-9 ? (cf > 0 ? [0.25*f, f, 0.75*f] : [f, 0.3*f, 0.8*f]) : zero3); M3.setPt(seaB, np, p.clone().addScaledVector(_u, -0.16), Math.abs(cb) > 1e-9 ? (cb > 0 ? [0.25*g, g, 0.75*g] : [g, 0.3*g, 0.8*g]) : zero3); np++; } });
  for(let k=np;k<NL*MP;k++){ M3.setPt(seaF, k, pos[0] || new T.Vector3(), zero3); M3.setPt(seaB, k, pos[0] || new T.Vector3(), zero3); }
  arrows.reset(); for(let i=0;i<7;i++){ if(i >= E.N || !sh.balls){ M3.setPt(heads, i, new T.Vector3(), zero3); continue; } const s = RD.spin[i], m = Math.hypot(s[0], s[1], s[2]); if(m < 1e-9){ M3.setPt(heads, i, pos[i], zero3); continue; }
    const len = 0.45*Math.log10(1 + m/1e-4), tip = pos[i].clone().addScaledVector(hyp3(s).normalize(), len); arrows.add(pos[i], tip, [0.3, 1, 0.8]); M3.setPt(heads, i, tip, [0.3, 1, 0.8]); } arrows.done();
  ties.reset(); if(sh.ties) for(const t of RD.tie){ const b = Math.max(0, Math.min(1, (Math.log10(Math.max(t[2], 1e-300)) + 9)/9)); if(b > 0) ties.add(pos[t[0]].clone().addScaledVector(_u, 0.3), pos[t[1]].clone().addScaledVector(_u, 0.3), [0.75*b, 0.5*b, b]); } ties.done(); }
/* ---------- controls ---------- */
const css = document.createElement('style'); css.textContent = `.sea{position:fixed;left:412px;right:8px;top:8px;z-index:6;display:flex;flex-wrap:wrap;gap:4px 10px;align-items:center;padding:6px 9px;background:rgba(9,13,20,.8);border:1px solid var(--edge,#1f2a38);border-radius:8px;font-size:11.5px;color:var(--ink,#dfe7ef);backdrop-filter:blur(5px)}
.sea .g{display:flex;flex-wrap:wrap;gap:3px;align-items:center}.sea .g>span:first-child{color:var(--dim,#8a9aab);margin-right:2px}.sea button{font:inherit;font-size:11.5px;padding:3px 7px;background:#0e1520;color:inherit;border:1px solid var(--edge,#1f2a38);border-radius:5px;cursor:pointer}
.sea button[aria-pressed=true]{border-color:#4fe0c0;color:#4fe0c0}.sea .hy{border:1px dashed #d99a2b;color:#d99a2b;border-radius:4px;padding:0 4px;font-size:9.5px;letter-spacing:.05em;font-style:normal}
.sea .num{flex-basis:100%;font-family:var(--mono,ui-monospace,monospace);font-size:11px;color:#bfeee2;line-height:1.5}.sea .key{flex-basis:100%;color:var(--dim,#8a9aab);font-size:10.5px;line-height:1.45}.sea details{flex-basis:100%}.sea summary{cursor:pointer;color:var(--dim,#8a9aab);font-size:10.5px}
body.clean .sea{display:none}@media (max-width:900px){.sea{left:8px;top:auto;bottom:150px;max-height:34%;overflow:auto}}`; document.head.append(css);
const B = (attr, list) => list.map(([v, t, hy]) => `<button data-${attr}="${v}">${t}${hy ? ' <i class="hy">' + hy + '</i>' : ''}</button>`).join('');
document.body.insertAdjacentHTML('beforeend', `<div class="sea" id="sea"><div class="g"><span>The sea</span><button id="sea_on">On</button></div>
<div class="g"><span>It moves</span>${B('m', [['tied','Travelling, tied at rest','MODEL CHOICE'],['untied','Travelling, not tied'],['atonce','All at once']])}</div>
<div class="g"><span>Ends</span>${B('e', [['sealed','Sealed'],['leak','Open end'],['container','Bigger container']])}</div>
<div class="g"><span>Feed</span>${B('f', [['kick','One kick'],['kicks_in','Kicks in time'],['kicks_out','Kicks out of time'],['squeeze_in','Squeeze in time'],['squeeze_out','Squeeze out of time']])}</div>
<div class="g"><span>Sea pushes the balls</span>${B('p', [['0','Off'],['1','On','HYPOTHESIS']])}</div>
<div class="g"><span>Show</span>${B('s', [['links','Sea on the links'],['balls','Sea on the balls'],['ties','Ties']])}</div>
<div class="g"><button id="sea_kick">Kick the sea at A</button><button id="sea_rest_b">Back to rest</button></div>
<div class="num" id="sea_num"></div>
<details><summary>What is drawn</summary><div class="key">Green and violet dots beside each link: the sea’s filling there, above rest (green) or below (violet), movers toward the second ball on one side, movers back on the other. Brightness is on a log scale, from a change of 10⁻⁷ (dark) to 10⁻¹ (full). Green arrow on a ball: the change of the sea’s spin on that ball; its length grows with the logarithm of the change. Violet line between two balls: the weight between them, from 10⁻⁹ (dark) to 1 (bright) on a log scale. The sea fills half of everything light can occupy; which half is a choice, marked. The all-at-once way has no links, so nothing is drawn along them. The sea uses its own step (0.05 for 3 and 4 balls, 0.2 for 7), coarser than the light’s. The tied rest sea is stored for 3, 4 and 7 balls at step ratios 3, 5, 7 with sealed ends, and for 3 balls in the bigger container; it is stored in single precision, so with the push on and 7 balls, where the balls turn far, the numbers differ from the sweep’s by a few percent.</div></details></div>`);
const bar = document.getElementById('sea');
function ui(){ bar.querySelectorAll('[data-m]').forEach(b => b.setAttribute('aria-pressed', b.dataset.m === O.machine)); bar.querySelectorAll('[data-e]').forEach(b => b.setAttribute('aria-pressed', b.dataset.e === O.ends)); bar.querySelectorAll('[data-f]').forEach(b => b.setAttribute('aria-pressed', b.dataset.f === O.feed));
  bar.querySelectorAll('[data-p]').forEach(b => b.setAttribute('aria-pressed', (b.dataset.p === '1') === O.push)); bar.querySelectorAll('[data-s]').forEach(b => b.setAttribute('aria-pressed', !!O.show[b.dataset.s])); document.getElementById('sea_on').setAttribute('aria-pressed', O.on); document.getElementById('sea_on').textContent = O.on ? 'On' : 'Off'; status(); }
const e1 = x => Number.isFinite(x) ? (x === 0 ? '0' : x.toExponential(1)) : '—', f2 = x => Number.isFinite(x) ? x.toFixed(2) : '—';
function status(){ const el = document.getElementById('sea_num'); if(!O.on){ el.textContent = ''; return; } if(note || !E || !E.ok || !RD){ el.textContent = note || ''; return; }
  const tie = RD.tie.filter(t => t[0] === 0 && t[1] === E.far)[0][2], nm = E.W.balls[E.far].name, kickRead = O.feed === 'kick' && O.machine !== 'untied' && O.ends !== 'leak';
  el.textContent = 'sea time ' + f2(E.t) + '  ·  filled ' + E.rank + ' of ' + E.M + '  ·  books: filled now − at start = ' + e1(RD.trace - E.tr0) + (O.ends === 'leak' ? ' (left through the open end ' + e1(RD.left) + ')' : '') + '  ·  lifted out of the rest sea ' + e1(RD.lifted) +
    '  ·  far ball ' + nm + ': sea changed by ' + e1(RD.farChange) + (kickRead ? ', first moved at ' + (first === null ? '—' : f2(first)) + ' (light needs ' + f2(E.cross) + ')' : '') + '  ·  weight between A and ' + nm + ' ' + e1(tie) + (O.push ? '  ·  largest ball turn ' + e1(Math.max(...RD.turn)) : '') + '  ·  ' + msStep.toFixed(1) + ' ms a step'; }
bar.addEventListener('click', ev => { const b = ev.target.closest('button'); if(!b) return; const d = b.dataset; if(d.m) O.machine = d.m; else if(d.e) O.ends = d.e; else if(d.f) O.feed = d.f; else if(d.p) O.push = d.p === '1'; else if(d.s) O.show[d.s] = !O.show[d.s];
  else if(b.id === 'sea_on') O.on = !O.on; else if(b.id === 'sea_kick'){ if(E && E.ok){ SEA.kick(E, true); first = null; RD = SEA.read(E); } } else if(b.id === 'sea_rest_b'){ okey = ''; } if(d.s){ okey = JSON.stringify(O); } ui(); });
const R = S3.renderer, prev = R.render; R.render = function(sc, cm){ if(sc === S3.scene){ try { tick(); } catch(err){ note = 'The sea stopped: ' + err.message; E = null; } } return prev.call(R, sc, cm); };
ui(); window.__SEA = { O, get E(){ return E; }, read:() => RD, first:() => first, note:() => note, building:() => building, rebuild:() => { okey = ''; } };
})();
