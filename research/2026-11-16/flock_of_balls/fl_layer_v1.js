/* SCRIPT: FL-LAYER-V1
   The Flock of Balls on the Field: drawing and controls. Jeromie Beasley. 16 Nov 2026. AI-assisted.
   The page's own ball (WORLD) is left exactly as it is and drawn once per ball on the field: A at the centre, the others one peel
   step out along the arms. Between the balls the light is drawn where it is: travelling along each gap, meeting the faces and the
   gap layer (FL-MATH-V1). Each ball carries its own clock. Every view is its own switch and they combine freely.
   Nothing is placed on the right of the screen. Host adapter window.__TBHOST = { S3, WORLD, tau(), S() }. Needs Mixer3D, MM, FL. */
(function(){
"use strict";
const H = window.__TBHOST, M = window.Mixer3D, T = M.T, S3 = H.S3, WORLD = H.WORLD, RB = 2.6, PI = Math.PI, TAU = 2*PI;
const fmt = (x,n) => Number.isFinite(x) ? x.toFixed(n == null ? 3 : n) : '—', sci = x => Number.isFinite(x) ? x.toExponential(1) : '—';
const COL = ['#fff2cc','#ff8d7c','#63d3ff','#9be28a','#ffb35c','#b58cff','#7fe0d0'], COLV = [[1,0.95,0.8],[1,0.55,0.49],[0.39,0.83,1],[0.61,0.89,0.54],[1,0.7,0.36],[0.71,0.55,1],[0.5,0.88,0.82]];
const VIEWS = [['light','Light in the gaps'],['faces','Faces and gap layers'],['fields','Ball fields'],['clocks','Clocks'],['sync','Clock phases'],['rims','Rims meeting'],['names','Names']];
const X = { on:true, N:4, clocks:'z', push:'static', src:0, zoom:100, goalZoom:100, speed:1, show:{ light:true, faces:true, fields:true, clocks:true, sync:false, rims:true, names:true } };
const target = new T.Vector3(), goal = new T.Vector3();
let W = null, St = null, lastTau = null, acc = 0, pos = [], LK = [], zKey = '', share = [], BK = null, ORD = null, arrive = [], rHist = [];
const zOf = () => { const S = H.S ? H.S() : null, P = S && S.P; const z = P && (P.zbar || (P.zI ? [P.zI, P.zJ, P.zK] : null)); return (z && z.length === 3 && z.every(x => x > 1)) ? z.slice() : [3,5,7]; };
/* ---------- field objects ---------- */
const FIELD = new T.Group(); S3.world.add(FIELD);
const seg = (n, op, add) => { const g = new T.BufferGeometry(); g.setAttribute('position', new T.BufferAttribute(new Float32Array(n*6), 3)); g.setAttribute('color', new T.BufferAttribute(new Float32Array(n*6), 3));
  const m = new T.LineSegments(g, new T.LineBasicMaterial({ vertexColors:true, transparent:true, opacity:op, depthWrite:false, depthTest:false, blending:add === false ? T.NormalBlending : T.AdditiveBlending })); m.frustumCulled = false; m.renderOrder = 5; FIELD.add(m); let i = 0;
  return { mesh:m, reset(){ i = 0; }, add(a, b, c){ if(i >= n) return; const p = g.attributes.position, q = g.attributes.color; p.setXYZ(2*i, a.x, a.y, a.z); p.setXYZ(2*i+1, b.x, b.y, b.z); q.setXYZ(2*i, c[0], c[1], c[2]); q.setXYZ(2*i+1, c[0], c[1], c[2]); i++; }, done(){ g.setDrawRange(0, 2*i); g.attributes.position.needsUpdate = g.attributes.color.needsUpdate = true; } }; };
const NL = 18, MP = 56;
const pathLine = seg(NL*2, 0.55), faceLine = seg(NL*3*26, 1), rimLine = seg(6*96, 1), arrows = seg(7*3, 1), clockLine = seg(7*40, 1);
const pts = (n, size) => { const p = M.points(n, size); p.material.depthTest = false; p.renderOrder = 6; p.frustumCulled = false; FIELD.add(p); return p; };
const lightF = pts(NL*MP, 0.34), lightB = pts(NL*MP, 0.34), corePts = pts(7, 1.5), phasePts = pts(7, 0.55), handPts = pts(7, 0.4);
let labels = [];
const hyp3 = v => new T.Vector3(v[0], v[2], -v[1]);   /* the field's (x, y, z) drawn as (x, up, toward the viewer) as in the three-ball page */
function layout(){ const P = W.balls.map(b => b.arm < 0 ? new T.Vector3() : hyp3(MM.AXES[b.arm]).multiplyScalar(RB*(1 + Math.tanh(b.r/4)))); return P; }
function build(){ const z = zOf(); zKey = z.join(','); W = FL.makeWorld({ N:X.N, z, clocks:X.clocks, push:X.push }); if(X.src >= W.N) X.src = 0; St = FL.initState(W, { source:X.src }); lastTau = H.tau(); acc = 0; pos = layout(); arrive = new Array(W.N).fill(null); arrive[X.src] = 0; rHist = [];
  LK = W.links.map(l => ({ a:pos[l.i], b:pos[l.j] }));
  labels.forEach(l => FIELD.remove(l)); labels = W.balls.map((b, i) => { const l = M.label('ball ' + b.name + (X.clocks === 'z' && i ? '  clock ÷' + fmt(Math.exp(b.r), 0) : '  clock ×1'), COL[i], 0.4); l.material.depthTest = false; l.renderOrder = 7; FIELD.add(l); return l; });
  ui(); }
function kick(i){ X.src = i; FL.kick(W, St, i); arrive = new Array(W.N).fill(null); arrive[i] = 0; ui(); }
/* ---------- one frame of the field ---------- */
const _r = new T.Vector3(), _u = new T.Vector3(), zero3 = [0,0,0];
function step(){ const tau = H.tau(); if(!W || zOf().join(',') !== zKey || tau < lastTau - 1e-9) build(); const dt = Math.max(0, Math.min(0.1, tau - lastTau)); lastTau = tau;
  acc += dt*X.speed; const h = W.opts.h; let n = Math.floor(acc/h); acc -= n*h; n = Math.min(n, 60);
  for(let k=0;k<n;k++){ FL.step(W, St); if(k % 4 === 0) for(let i=0;i<W.N;i++) if(arrive[i] === null && FL.ballLight(St, i) > 1e-12) arrive[i] = St.t - (St.kickT || 0); }
  share = W.balls.map((_, i) => FL.ballLight(St, i)); BK = FL.books(W, St); ORD = FL.order(W, St); if(n){ rHist.push(ORD.r); if(rHist.length > 600) rHist.shift(); }
  const sh = X.show, cam = S3.camera; _r.setFromMatrixColumn(cam.matrixWorld, 0); _u.setFromMatrixColumn(cam.matrixWorld, 1);
  pathLine.reset(); faceLine.reset(); rimLine.reset(); arrows.reset(); clockLine.reset(); let np = 0;
  W.links.forEach((l, k) => { const a = LK[k].a, b = LK[k].b, at = s => a.clone().lerp(b, s/l.d), dir = b.clone().sub(a).normalize();
    if(sh.light || sh.faces) pathLine.add(a, b, [0.16,0.2,0.27]);
    const pr = FL.linkProfile(W, l, MP);
    for(let m=0;m<MP;m++){ const p = at((m+0.5)/MP*l.d), f = sh.light ? Math.min(1, 2.2*Math.pow(pr.F[m], 0.3)) : 0, g = sh.light ? Math.min(1, 2.2*Math.pow(pr.B[m], 0.3)) : 0;
      M.setPt(lightF, np, p.clone().addScaledVector(_u, 0.05), pr.F[m] > 1e-9 ? [f, 0.86*f, 0.5*f] : zero3); M.setPt(lightB, np, p.clone().addScaledVector(_u, -0.05), pr.B[m] > 1e-9 ? [0.45*g, 0.8*g, g] : zero3); np++; }
    if(sh.faces) l.marks.forEach(mk => { const c = at(mk.s), e1 = (Math.abs(dir.y) < 0.9 ? new T.Vector3(0,1,0) : new T.Vector3(1,0,0)).cross(dir).normalize(), e2 = dir.clone().cross(e1), R = Math.abs(mk.rho), isGap = mk.kind === 'gap', rad = isGap ? 0.2 : 0.3, col = isGap ? [0.75*(0.4+0.6*R), 0.45*(0.4+0.6*R), 1*(0.4+0.6*R)] : [0.35+0.65*R, 0.3+0.5*R, 0.15+0.2*R]; let prev = null;
        for(let s=0;s<=24;s++){ if(isGap && s % 2){ prev = null; continue; } const t = TAU*s/24, p = c.clone().addScaledVector(e1, rad*Math.cos(t)).addScaledVector(e2, rad*Math.sin(t)); if(prev) faceLine.add(prev, p, col); prev = p; if(isGap){ const q = c.clone().addScaledVector(e1, rad*Math.cos(t + TAU/24)).addScaledVector(e2, rad*Math.sin(t + TAU/24)); faceLine.add(p, q, col); } } });
    if(sh.rims && l.i === 0){ const D = a.distanceTo(b); if(D < 2*RB){ const mid = a.clone().add(b).multiplyScalar(0.5), rr = Math.sqrt(RB*RB - D*D/4), e1 = (Math.abs(dir.y) < 0.9 ? new T.Vector3(0,1,0) : new T.Vector3(1,0,0)).cross(dir).normalize(), e2 = dir.clone().cross(e1), mb = Math.min(MP-1, Math.floor(l.marks[0].s/l.d*MP));
        let near = 0; for(let m=Math.max(0, mb-3); m<=Math.min(MP-1, mb+3); m++) near += pr.F[m] + pr.B[m]; const w = Math.min(1, 1.6*Math.pow(near, 0.3)), c = [0.3 + 0.7*w, 0.24 + 0.7*w, 0.12 + 0.6*w]; let prev = null;
        for(let s=0;s<=96;s++){ const t = TAU*s/96, p = mid.clone().addScaledVector(e1, rr*Math.cos(t)).addScaledVector(e2, rr*Math.sin(t)); if(prev) rimLine.add(prev, p, c); prev = p; } } } });
  for(let k=np; k<NL*MP; k++){ M.setPt(lightF, k, target, zero3); M.setPt(lightB, k, target, zero3); }
  for(let i=0;i<7;i++){ if(i >= W.N){ M.setPt(corePts, i, target, zero3); M.setPt(phasePts, i, target, zero3); M.setPt(handPts, i, target, zero3); continue; }
    const p = pos[i], d = St.d[i], m = Math.hypot(d[0], d[1], d[2]), u = hyp3(d).multiplyScalar(1/m);
    if(sh.fields){ const tip = p.clone().addScaledVector(u, 0.95), side = (Math.abs(u.y) < 0.9 ? new T.Vector3(0,1,0) : new T.Vector3(1,0,0)).cross(u).normalize(); arrows.add(p, tip, [1,0.78,0.35]); arrows.add(tip, tip.clone().addScaledVector(u, -0.2).addScaledVector(side, 0.09), [1,0.9,0.6]); arrows.add(tip, tip.clone().addScaledVector(u, -0.2).addScaledVector(side, -0.09), [1,0.9,0.6]); }
    const s = Math.min(1, 1.3*Math.pow(share[i], 0.35)); M.setPt(corePts, i, p, [COLV[i][0]*s, COLV[i][1]*s, COLV[i][2]*s]);
    /* the ball's own clock: a dial facing the viewer above the ball; the hand turns once per 2 units of the ball's own time */
    const c = p.clone().addScaledVector(_u, RB + 1.05), rc = 0.42, cc = COLV[i];
    if(sh.clocks){ let prev = null; for(let q=0;q<=32;q++){ const t = TAU*q/32, pt = c.clone().addScaledVector(_r, rc*Math.sin(t)).addScaledVector(_u, rc*Math.cos(t)); if(prev) clockLine.add(prev, pt, [0.5*cc[0], 0.5*cc[1], 0.5*cc[2]]); prev = pt; }
      const ang = PI*St.tau[i], tip = c.clone().addScaledVector(_r, 0.9*rc*Math.sin(ang)).addScaledVector(_u, 0.9*rc*Math.cos(ang)); clockLine.add(c, tip, cc); M.setPt(handPts, i, tip, cc); } else M.setPt(handPts, i, target, zero3);
    if(sh.sync){ const ph = ORD.phases[i], wv = Math.min(1, 0.25 + 1.5*ph.weight); M.setPt(phasePts, i, c.clone().addScaledVector(_r, 1.25*rc*Math.sin(ph.phase)).addScaledVector(_u, 1.25*rc*Math.cos(ph.phase)), ph.weight > 1e-6 ? [wv, wv, wv] : zero3); } else M.setPt(phasePts, i, target, zero3);
    if(labels[i]){ labels[i].visible = sh.names; labels[i].position.copy(p).addScaledVector(_u, RB + 0.3); } }
  pathLine.done(); faceLine.done(); rimLine.done(); arrows.done(); clockLine.done(); [lightF, lightB, corePts, phasePts, handPts].forEach(M.flush); }
/* ---------- draw the page's ball once per ball; the camera looks at a point that can be moved over the field ---------- */
const R = S3.renderer, cam = S3.camera, scene = S3.scene, orig = R.render.bind(R), bg = scene.background ? scene.background.clone() : new T.Color(0x05070b);
R.toneMapping = T.LinearToneMapping;
const fieldSpan = () => X.N === 7 ? 3.1 : X.N === 4 ? 2.7 : 2.1;
R.render = function(sc, cm){ if(sc !== scene || !X.on){ FIELD.visible = false; WORLD.position.set(0,0,0); R.autoClear = true; scene.background = bg; R.toneMappingExposure = 1; return orig(sc, cm); }
  target.lerp(goal, 0.12); X.zoom += (X.goalZoom - X.zoom)*0.15; if(Math.abs(X.goalZoom - X.zoom) < 0.05) X.zoom = X.goalZoom;
  const V = S3.view, Dc = V.dist*fieldSpan()*(100/X.zoom)*(window.innerWidth < 640 ? 1.5 : 1), pt = Math.max(-1.3, Math.min(1.35, V.pitch + 0.45)), yw = V.yaw + 0.55;
  cam.position.set(target.x + Dc*Math.cos(pt)*Math.sin(yw), target.y + Dc*Math.sin(pt), target.z + Dc*Math.cos(pt)*Math.cos(yw)); cam.lookAt(target); cam.updateMatrixWorld();
  step(); scene.background = null; R.autoClear = false; R.setClearColor(bg, 1); R.clear();
  for(let b=0;b<W.N;b++){ WORLD.position.copy(pos[b]); FIELD.visible = b === W.N-1; R.toneMappingExposure = 0.26 + 0.9*Math.min(1, Math.pow(share[b], 0.4)); orig(sc, cm); }
  WORLD.position.set(0,0,0); R.toneMappingExposure = 1; status(); };
/* ---------- moving over the field ---------- */
const canvas = R.domElement; let pan = null;
function setZoom(z){ X.goalZoom = Math.max(20, Math.min(1200, z)); const el = document.getElementById('fl_zoom'); if(el && document.activeElement !== el) el.value = Math.round(X.goalZoom); }
function goTo(i){ if(i < 0){ goal.set(0,0,0); setZoom(100); } else { goal.copy(pos[i]); setZoom(Math.max(X.goalZoom, 230)); } }
function panBy(dx, dy, dz){ const Dc = S3.view.dist*fieldSpan()*(100/X.zoom); _r.setFromMatrixColumn(cam.matrixWorld, 0); const f = new T.Vector3().setFromMatrixColumn(cam.matrixWorld, 2).multiplyScalar(-1); f.y = 0; if(f.lengthSq() < 1e-6) f.set(0,0,-1); f.normalize(); const r = _r.clone(); r.y = 0; r.normalize();
  goal.addScaledVector(r, dx*Dc*0.06).addScaledVector(f, dy*Dc*0.06); goal.y += (dz||0)*Dc*0.06; const L = 3.2*RB; goal.x = Math.max(-L, Math.min(L, goal.x)); goal.y = Math.max(-L, Math.min(L, goal.y)); goal.z = Math.max(-L, Math.min(L, goal.z)); }
canvas.addEventListener('wheel', e => { if(!X.on) return; e.preventDefault(); e.stopImmediatePropagation(); setZoom(X.goalZoom*Math.exp(-e.deltaY*0.0012)); }, { capture:true, passive:false });
canvas.addEventListener('pointerdown', e => { if(!X.on || !(e.shiftKey || e.button === 2 || e.button === 1)) return; e.preventDefault(); e.stopImmediatePropagation(); pan = { x:e.clientX, y:e.clientY, id:e.pointerId }; canvas.setPointerCapture(e.pointerId); }, { capture:true });
canvas.addEventListener('pointermove', e => { if(!pan || e.pointerId !== pan.id) return; e.stopImmediatePropagation(); const Dc = S3.view.dist*fieldSpan()*(100/X.zoom), k = Dc*1.1/window.innerHeight; _r.setFromMatrixColumn(cam.matrixWorld, 0); _u.setFromMatrixColumn(cam.matrixWorld, 1);
  goal.addScaledVector(_r, -(e.clientX - pan.x)*k).addScaledVector(_u, (e.clientY - pan.y)*k); target.copy(goal); pan.x = e.clientX; pan.y = e.clientY; }, { capture:true });
['pointerup','pointercancel'].forEach(t => canvas.addEventListener(t, e => { if(pan && e.pointerId === pan.id){ pan = null; e.stopImmediatePropagation(); } }, { capture:true }));
canvas.addEventListener('contextmenu', e => { if(X.on) e.preventDefault(); });
canvas.addEventListener('dblclick', e => { if(!X.on || !W) return; let best = -1, bd = 140; pos.forEach((p, i) => { const q = p.clone().project(cam), x = (q.x*0.5 + 0.5)*window.innerWidth, y = (0.5 - q.y*0.5)*window.innerHeight, d = Math.hypot(x - e.clientX, y - e.clientY); if(q.z < 1 && d < bd){ bd = d; best = i; } }); goTo(best); });
window.addEventListener('keydown', e => { if(!X.on || e.ctrlKey || e.metaKey || /INPUT|TEXTAREA|SELECT/.test((e.target && e.target.tagName) || '')) return; const k = e.key.toLowerCase();
  if(k === 'arrowleft' || k === 'a') panBy(-1, 0); else if(k === 'arrowright' || k === 'd') panBy(1, 0); else if(k === 'arrowup' || k === 'w') panBy(0, 1); else if(k === 'arrowdown' || k === 's') panBy(0, -1); else if(k === 'q') panBy(0, 0, -1); else if(k === 'e') panBy(0, 0, 1);
  else if(k === '+' || k === '=') setZoom(X.goalZoom*1.15); else if(k === '-' || k === '_') setZoom(X.goalZoom/1.15); else if(k === '0') goTo(-1); else return; e.preventDefault(); });
/* ---------- controls: one bar along the bottom, numbers in a drawer that opens on the left; nothing on the right ---------- */
const css = document.createElement('style'); css.textContent = `
.fl{position:fixed;left:412px;right:10px;bottom:8px;z-index:6;display:flex;flex-wrap:wrap;gap:4px 10px;align-items:center;padding:6px 9px;background:rgba(9,13,20,.78);border:1px solid var(--edge,#1f2a38);border-radius:8px;font-size:11.5px;color:var(--ink,#dfe7ef);backdrop-filter:blur(5px)}
.fl .g{display:flex;flex-wrap:wrap;gap:3px;align-items:center}.fl .g>span{color:var(--dim,#8a9aab);margin-right:2px;font-size:10.5px;letter-spacing:.06em;text-transform:uppercase}
.fl button{font:inherit;font-size:11.5px;padding:3px 7px;background:#0e1520;color:inherit;border:1px solid var(--edge,#1f2a38);border-radius:5px;cursor:pointer}.fl button[aria-pressed=true]{border-color:#f2c14e;color:#f2c14e}.fl button:hover{border-color:#63d3ff}
.fl input{width:52px;font:inherit;font-size:11.5px;background:#0e1520;color:inherit;border:1px solid var(--edge,#1f2a38);border-radius:5px;padding:3px 4px}
.fl .st{font-family:var(--mono,monospace);font-size:11px;color:#f2c14e;white-space:nowrap}.fl .hy{border:1px dashed #d99a2b;color:#d99a2b;border-radius:4px;padding:0 4px;font-size:9.5px;letter-spacing:.05em}
.flnum{position:fixed;left:412px;bottom:96px;width:min(430px,calc(100% - 430px));max-height:min(62%,calc(100% - 130px));overflow:auto;z-index:6;background:rgba(9,13,20,.92);border:1px solid var(--edge,#1f2a38);border-radius:8px;padding:10px 12px;font-size:11.5px;color:var(--ink,#dfe7ef);display:none}
.flnum.open{display:block}.flnum h3{margin:8px 0 3px;font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--dim,#8a9aab);font-weight:600}.flnum h3:first-child{margin-top:0}
.flnum .row{display:flex;justify-content:space-between;gap:10px;padding:3px 0;border-bottom:1px solid rgba(31,42,56,.6);color:var(--dim,#8a9aab)}.flnum .row b{font-family:var(--mono,monospace);font-weight:400;color:var(--ink,#dfe7ef);text-align:right;font-size:11px;white-space:pre-wrap}
.flnum p{margin:4px 0;color:var(--dim,#8a9aab);line-height:1.5}.flnum .flc{display:inline-block;border-radius:4px;padding:0 5px;font-size:9.5px;letter-spacing:.05em;margin-right:5px;border:1px solid #2f8f5b;color:#6fd39a}.flnum .flc.h{border:1px dashed #d99a2b;color:#d99a2b}.flnum .flc.m{border-color:#4d7fb0;color:#8fc0ee}
body.clean .fl,body.clean .flnum{left:10px}.tb{display:none!important}
.strip{right:auto!important;left:412px!important;bottom:96px!important;justify-content:flex-start!important;max-width:calc(100% - 430px)!important}body.clean .strip{left:10px!important}
@media (max-width:900px){.fl,.flnum,.strip{left:8px!important}.fl{right:8px}.flnum{width:auto;right:8px}}`; document.head.append(css);
document.body.insertAdjacentHTML('beforeend', `<div class="flnum" id="fl_num"></div><div class="fl" id="fl">
<div class="g"><span>Balls</span><button data-n="3">3</button><button data-n="4">4</button><button data-n="7">7</button><button id="fl_one" title="The page's single ball, as it was">One ball</button></div>
<div class="g"><span>Kick</span><span id="fl_kicks" class="g"></span></div>
<div class="g"><span>Clocks</span><button data-clk="z">Ratio z <i class="hy">HYPOTHESIS</i></button><button data-clk="equal">All equal</button></div>
<div class="g"><span>Face push</span><button data-push="static">Held by faces</button><button data-push="retarded" title="Arrives one crossing time late. Not energy-booked; rest is unstable under it.">Delayed</button><button data-push="off">Off</button></div>
<div class="g"><span>Show</span>${VIEWS.map(v => `<button data-view="${v[0]}">${v[1]}</button>`).join('')}<button id="fl_all">All</button><button id="fl_none">None</button></div>
<div class="g" id="fl_eyeg" style="display:none"><span>Ball’s eyes</span><span id="fl_eyes" class="g"></span><button id="fl_eall">All</button><button id="fl_enone">Open eye only</button></div>
<div class="g" id="fl_layg" style="display:none"><span>Ball’s layers</span><span id="fl_lays" class="g"></span></div>
<div class="g"><span>Zoom</span><button id="fl_zm">−</button><input id="fl_zoom" type="number" min="20" max="1200" step="10" value="100" aria-label="Zoom percent">%<button id="fl_zp">+</button></div>
<div class="g"><span>Go to</span><span id="fl_gos" class="g"></span><button id="fl_field">Whole field</button></div>
<div class="g"><span>Speed</span><button data-sp="0.25">¼</button><button data-sp="1">1</button><button data-sp="3">3</button></div>
<div class="g"><button id="fl_restart">Restart</button><button id="fl_numb" aria-pressed="false">Numbers</button></div>
<div class="st" id="fl_st"></div></div>`);
const $ = id => document.getElementById(id), qa = s => Array.from(document.querySelectorAll(s));
function ui(){ qa('#fl button[data-n]').forEach(b => b.setAttribute('aria-pressed', X.on && +b.dataset.n === X.N)); $('fl_one').setAttribute('aria-pressed', !X.on);
  qa('#fl button[data-clk]').forEach(b => b.setAttribute('aria-pressed', b.dataset.clk === X.clocks)); qa('#fl button[data-push]').forEach(b => b.setAttribute('aria-pressed', b.dataset.push === X.push));
  qa('#fl button[data-view]').forEach(b => b.setAttribute('aria-pressed', !!X.show[b.dataset.view])); qa('#fl button[data-sp]').forEach(b => b.setAttribute('aria-pressed', +b.dataset.sp === X.speed));
  if(W){ $('fl_kicks').innerHTML = W.balls.map((b, i) => `<button data-kick="${i}" aria-pressed="${i === X.src}" style="color:${COL[i]}">${b.name}</button>`).join(''); $('fl_gos').innerHTML = W.balls.map((b, i) => `<button data-go="${i}" style="color:${COL[i]}">${b.name}</button>`).join(''); } }
$('fl').addEventListener('click', e => { const b = e.target.closest('button'); if(!b) return; const d = b.dataset;
  if(d.n){ X.N = +d.n; X.on = true; build(); goTo(-1); } else if(d.kick != null) kick(+d.kick); else if(d.clk){ X.clocks = d.clk; build(); } else if(d.push){ X.push = d.push; build(); }
  else if(d.view){ X.show[d.view] = !X.show[d.view]; } else if(d.go != null) goTo(+d.go); else if(d.sp) X.speed = +d.sp;
  else if(b.id === 'fl_one'){ X.on = !X.on; } else if(b.id === 'fl_all'){ VIEWS.forEach(v => X.show[v[0]] = true); } else if(b.id === 'fl_none'){ VIEWS.forEach(v => X.show[v[0]] = false); }
  else if(b.id === 'fl_zm') setZoom(X.goalZoom/1.25); else if(b.id === 'fl_zp') setZoom(X.goalZoom*1.25); else if(b.id === 'fl_field') goTo(-1); else if(b.id === 'fl_restart') build();
  else if(b.id === 'fl_numb'){ const o = $('fl_num').classList.toggle('open'); b.setAttribute('aria-pressed', o); if(o) numbers(); } ui(); });
$('fl_zoom').addEventListener('change', e => setZoom(+e.target.value || 100));
let lastSt = 0, lastNum = 0;
function status(){ const now = performance.now(); if(now - lastSt > 200 && BK){ lastSt = now; $('fl_st').textContent = 'field time ' + fmt(St.t, 2) + '  ·  light: balls ' + fmt(BK.balls, 3) + ' + gaps ' + fmt(BK.gaps, 3) + ' = ' + fmt(BK.total, 6) + '  ·  in step r = ' + fmt(ORD.r, 2) + '  ·  zoom ' + Math.round(X.zoom) + '%'; }
  if(now - lastNum > 500 && $('fl_num').classList.contains('open')){ lastNum = now; numbers(); } }
const row = (a, b) => `<div class="row"><span>${a}</span><b>${b}</b></div>`;
function numbers(){ if(!W || !BK) return; const nm = W.balls.map(b => b.name).join(', '), rm = rHist.length ? rHist.reduce((a,b) => a+b, 0)/rHist.length : NaN;
  let h = `<h3>The flock of balls</h3><p>${W.N} whole balls on the field. Light crosses each gap at one unit of length per unit of field time, meets the faces on the way, and only then reaches the next ball. The books below are recomputed on every frame.</p>`;
  h += row('field time since the kick at ' + W.balls[St.src == null ? 0 : St.src].name, fmt(St.t - (St.kickT || 0), 2));
  h += row('light in the balls (' + nm + ')', share.map(x => fmt(x, 3)).join('  ')) + row('light in the gaps', fmt(BK.gaps, 6)) + row('books: balls + gaps − 1', sci(BK.total - 1));
  h += `<h3>Gaps</h3><p><span class="flc">LEAN · step_matching, flux_balance</span>one face returns Γ² and passes 1 − Γ², Γ = tanh(step/2). <span class="flc">CHECKED · FL-CHECK-01 K1–K4</span></p>`;
  W.links.forEach(l => { const A = W.balls[l.i].name, B = W.balls[l.j].name, f = l.marks.filter(m => m.kind === 'face').map(m => 'Γ² ' + fmt(m.rho*m.rho, 3) + ' at ' + fmt(m.s, 2)).join(', '), gp = l.marks.find(m => m.kind === 'gap');
    h += row(A + '–' + B + '  length ' + fmt(l.d, 3) + (arrive[l.j] != null && l.i === (St.src||0) ? ', first light at ' + fmt(arrive[l.j], 2) : ''), 'faces: ' + f + (gp ? '\ngap δ ' + fmt(gp.delta, 3) + ', passes sech² = ' + fmt(1 - gp.rho*gp.rho, 3) : (l.g != null ? '\nfaces meet (g = ' + fmt(l.g, 2) + '), no gap layer' : '')) + '\nlight here ' + fmt(BK.perLink[W.links.indexOf(l)], 3)); });
  h += `<p><span class="flc h">HYPOTHESIS</span>Where two faces stand apart (g &gt; 1) the light between them only tunnels, by sech(κ δ) with κ = ${fmt(W.opts.kgap, 1)}. <span class="flc m">MODEL CHOICE</span>each ball gives light to a gap at rate γ = ${fmt(W.opts.gamma, 2)}; the links are drawn as straight lines between ball centres.</p>`;
  h += `<h3>Clocks</h3><p><span class="flc h">HYPOTHESIS</span>${X.clocks === 'z' ? 'Each ball one step out runs at 1/z of the centre clock, z = e^r the radar ratio of its step. Across an arm–arm gap the ratio is the ratio of the two z.' : 'Comparison setting: every ball runs at the same rate.'} <span class="flc">CHECKED · K5</span></p>`;
  W.balls.forEach((b, i) => { h += row('ball ' + b.name + (b.arm < 0 ? '  (centre)' : '  step z = ' + fmt(Math.exp(b.r), 2)), 'rate ' + fmt(b.rate, 4) + '   own time ' + fmt(St.tau[i], 2) + '\nfield turned ' + fmt(FL.tilt(W, St, i), 3) + ' rad   first light ' + (arrive[i] == null ? '—' : fmt(arrive[i], 2))); });
  h += `<h3>In step?</h3>` + row('order parameter r now', fmt(ORD.r, 3)) + row('r, mean over the recent run', fmt(rm, 3));
  h += `<p><span class="flc m">READING</span>r is Kuramoto’s measure taken on each ball’s clock phase (the angle of its light’s spin about its own field), weighted by how hard that ball is swinging: 1 means every swinging ball is at the same phase. In the runs so far the flock does not lock, with clocks at z or equal (FL-CHECK-01).</p>`;
  h += `<h3>Not claimed</h3><p>The electron sea of the three-ball page is not in this model yet: it needs its own travel time. Energy is booked as light count only; the energy carried by light in transit is not separately booked. ${X.push === 'retarded' ? 'The delayed face push is not energy-booked and the rest state is unstable under it. ' : ''}The gap lengths are held at the mean steps z = ${zKey}; the single ball’s own breathing drive does not change them here.</p>`;
  $('fl_num').innerHTML = h; }
/* the ball's own eyes (mixer ball): any set on together, each part of the ball takes the strongest weight among the eyes that are on;
   the ball's own layers (white ball): each has its own switch */
const EON = new Set();
if(H.eyes && H.EMPH && H.WT && H.cur){ $('fl_eyeg').style.display = ''; $('fl_eyes').innerHTML = H.eyes.map(e => `<button data-eye="${e.id}" aria-pressed="false" title="${String(e.title||'').replace(/"/g,'')}">${e.id}</button>`).join('');
  const paint = () => qa('#fl_eyes button').forEach(b => b.setAttribute('aria-pressed', EON.has(b.dataset.eye) || b.dataset.eye === H.cur()));
  $('fl_eyes').addEventListener('click', e => { const b = e.target.closest('button'); if(!b) return; e.stopPropagation(); EON.has(b.dataset.eye) ? EON.delete(b.dataset.eye) : EON.add(b.dataset.eye); paint(); });
  $('fl_eall').addEventListener('click', e => { e.stopPropagation(); H.eyes.forEach(x => EON.add(x.id)); paint(); }); $('fl_enone').addEventListener('click', e => { e.stopPropagation(); EON.clear(); paint(); });
  setInterval(() => { const cur = H.cur(), ids = [cur].concat([...EON]); for(const c in H.EMPH[cur]){ let w = 0; for(const id of ids) if(H.EMPH[id]) w = Math.max(w, H.EMPH[id][c]); H.WT[c] = w; } paint(); }, 80); }
if(H.layers){ $('fl_layg').style.display = ''; $('fl_lays').innerHTML = Object.keys(H.layers).map(n => `<button data-lay="${n}" aria-pressed="true">${n}</button>`).join('');
  $('fl_lays').addEventListener('click', e => { const b = e.target.closest('button'); if(!b) return; e.stopPropagation(); const on = b.getAttribute('aria-pressed') !== 'true'; b.setAttribute('aria-pressed', on); H.layers[b.dataset.lay].forEach(o => o.visible = on); }); }
/* keep the page's own clock strip and the numbers drawer stacked above the bar, on the left */
function place(){ const hb = $('fl').offsetHeight, st = document.querySelector('.strip, #strip'); let y = hb + 14; if(st){ st.style.setProperty('bottom', y + 'px', 'important'); y += st.offsetHeight + 8; } $('fl_num').style.bottom = y + 'px'; }
setInterval(place, 700); window.addEventListener('resize', place);
window.__FL = { X, get W(){ return W; }, get St(){ return St; }, build, kick, goTo, setZoom, panBy, books:() => BK, order:() => ORD, arrive:() => arrive };
build(); ui(); place();
})();
