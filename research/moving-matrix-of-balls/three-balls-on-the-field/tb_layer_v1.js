/* SCRIPT: TB-LAYER-V1
   Three Balls on the Field — drawing and controls. Jeromie Beasley. 15 Nov 2026. AI-assisted.
   The page's own ball (WORLD) is left exactly as it is and drawn three times each frame: A at the centre of the field,
   B out along A's I arm, C out along A's J arm, each a whole ball with its own rim. Each ball is lit by the share of the
   energy it holds. Between the balls: the lens where two rims meet (the glue), the flow across it, and each ball's field.
   Host adapter window.__TBHOST = { S3, WORLD, tau(), S(), AXV } is set by the page app. Needs Mixer3D, MM, TB. */
(function(){
"use strict";
const H = window.__TBHOST, M = window.Mixer3D, T = M.T, S3 = H.S3, WORLD = H.WORLD, RB = 2.6, PI = Math.PI;
const fmt = (x,n) => Number.isFinite(x) ? x.toFixed(n == null ? 4 : n) : '—', sci = x => Number.isFinite(x) ? x.toExponential(1) : '—';
const NAMES = TB.NAMES, COL = ['#fff2cc', '#ff8d7c', '#63d3ff'], COLV = [[1,0.95,0.8],[1,0.55,0.49],[0.39,0.83,1]];
const X = { on:true, seaBack:true, view:'light', n:5, src:0 };
let W = null, St = null, E0 = 0, ES0 = 0, IN = 0, NU0 = null, AL = null, AS = null, T0 = 0, lastTau = null, MD = null, EN = null, CUR = null, TR = [0,0,0], share = [1,0,0], pos = [new T.Vector3(), new T.Vector3(), new T.Vector3()];
/* ---- the field objects (drawn once per frame, with the first ball) ---- */
const FIELD = new T.Group(); S3.world.add(FIELD);
const seg = (n, op) => { const g = new T.BufferGeometry(); g.setAttribute('position', new T.BufferAttribute(new Float32Array(n*6), 3)); g.setAttribute('color', new T.BufferAttribute(new Float32Array(n*6), 3));
  const m = new T.LineSegments(g, new T.LineBasicMaterial({ vertexColors:true, transparent:true, opacity:op, depthWrite:false, blending:T.AdditiveBlending })); m.frustumCulled = false; FIELD.add(m); let i = 0;
  return { reset(){ i = 0; }, add(a, b, c){ if(i >= n) return; const p = g.attributes.position, q = g.attributes.color; p.setXYZ(2*i, a.x, a.y, a.z); p.setXYZ(2*i+1, b.x, b.y, b.z); q.setXYZ(2*i, c[0], c[1], c[2]); q.setXYZ(2*i+1, c[0], c[1], c[2]); i++; }, done(){ g.setDrawRange(0, 2*i); g.attributes.position.needsUpdate = g.attributes.color.needsUpdate = true; } }; };
const lens = seg(3*128, 1), flowLine = seg(3*40, 0.9), arrows = seg(3*4, 1);
const flowPts = M.points(3*14, 0.3); FIELD.add(flowPts); const midPts = M.points(3, 1.1); FIELD.add(midPts); const corePts = M.points(3, 1.6); FIELD.add(corePts);
const labels = NAMES.map((n, i) => { const l = M.label('ball ' + n, COL[i], 0.42); FIELD.add(l); return l; });
/* ---- layout: each ball's centre sits so that the cap vertex on the shared arm is where the other ball's rim passes ---- */
function layout(S){ const dI = RB*(1 + Math.tanh(S.h[0]/2)), dJ = RB*(1 + Math.tanh(S.h[1]/2)), P = [new T.Vector3(0,0,0), new T.Vector3(dI,0,0), new T.Vector3(0,0,-dJ)];
  const c = P[0].clone().add(P[1]).add(P[2]).multiplyScalar(1/3); P.forEach(p => p.sub(c)); return P; }
function build(){ const S = H.S(); W = TB.makeWorld(S.r, { seaBack:X.seaBack }); St = MM.initState(W, { source:X.src }); St.work = 0; const e = MM.energies(W, St); E0 = e.E; ES0 = e.ES; IN = 0; T0 = H.tau(); lastTau = H.tau();
  NU0 = MM.ballCensus(W, St).map(c => c.nu[0]); AL = [null,null,null]; AS = [null,null,null]; AL[X.src] = 0; TR = [0,0,0]; MD = TB.modes(W, St.d); X.n = MD.lead; const el = document.getElementById('tb_n'); if(el){ el.value = X.n; document.getElementById('tb_on').textContent = X.n; } }
function kick(i){ const b = MM.energies(W, St).E, S2 = MM.initState(Object.assign({}, W, { d:St.d }), { source:i, noSea:true }); St.psr = S2.psr; St.psi = S2.psi; IN += MM.energies(W, St).E - b; }
function intoMode(){ MD = TB.modes(W, St.d); const v = MD.vecs[X.n], b = MM.energies(W, St).E; St.psr = Float64Array.from(v[0]); St.psi = Float64Array.from(v[1]); IN += MM.energies(W, St).E - b; }
function step(){ const S = H.S(), tau = H.tau(); if(!W || tau < lastTau - 1e-9) build(); const dt = Math.min(0.1, tau - lastTau); lastTau = tau;
  if(dt > 0){ St = TB.advance(W, St, S.r, dt, 0.01); const C = MM.ballCensus(W, St), t = tau - T0; for(let i=0;i<3;i++){ if(AL[i] === null && MM.lightDensity(St, i) > 1e-3) AL[i] = t; if(AS[i] === null && Math.abs(C[i].nu[0] - NU0[i]) > 1e-3) AS[i] = t; } }
  EN = MM.energies(W, St); CUR = MM.lightCurrents(W, St); for(let k=0;k<3;k++) TR[k] += Math.abs(CUR[k])*dt;
  share = X.view === 'mode' && MD ? MD.share[X.n] : [0,1,2].map(i => MM.lightDensity(St, i));
  pos = layout(S);
  /* glue: the circle where two rims meet, gold by what that face holds, white by what crosses it */
  lens.reset(); flowLine.reset(); arrows.reset(); const jm = Math.max(1e-6, ...CUR.map(Math.abs)), em = Math.max(0.02, ...EN.Eper); let np = 0;
  TB.PAIRS.forEach(([i,j], k) => { const a = pos[i], b = pos[j], ab = b.clone().sub(a), D = ab.length(), n = ab.clone().multiplyScalar(1/D), mid = a.clone().add(b).multiplyScalar(0.5);
    const ge = Math.sqrt(EN.Eper[k]/em), gj = Math.sqrt(Math.abs(CUR[k])/jm), c = [0.25 + 0.75*Math.max(ge, gj), 0.2 + 0.55*ge + 0.75*gj, 0.12 + 0.2*ge + 0.75*gj];
    if(D < 2*RB){ const rr = Math.sqrt(RB*RB - D*D/4), e1 = (Math.abs(n.y) < 0.9 ? new T.Vector3(0,1,0) : new T.Vector3(1,0,0)).cross(n).normalize(), e2 = n.clone().cross(e1); let prev = null;
      for(let s=0;s<=128;s++){ const t = 2*PI*s/128, p = mid.clone().addScaledVector(e1, rr*Math.cos(t)).addScaledVector(e2, rr*Math.sin(t)); if(prev) lens.add(prev, p, c); prev = p; } }
    /* the path from centre to centre, brightness by all that has crossed; markers move in the sense of the flow (J > 0: from j into i) */
    const tm = Math.max(1e-9, ...TR), tr = Math.sqrt(TR[k]/tm), tc = [0.95*tr, 0.85*tr, 0.6*tr]; for(let s=0;s<40;s++) flowLine.add(a.clone().lerp(b, s/40), a.clone().lerp(b, (s+1)/40), tc);
    const f = Math.abs(CUR[k])/jm, dir = CUR[k] > 0 ? -1 : 1, ph = ((performance.now()/1000*0.45*dir) % 1 + 1) % 1; for(let m=0;m<14;m++){ const t = ((m/14 + ph) % 1 + 1) % 1; M.setPt(flowPts, np++, a.clone().lerp(b, t), [Math.sqrt(f), 0.93*Math.sqrt(f), 0.65*Math.sqrt(f)]); }
    M.setPt(midPts, k, mid, [c[0]*0.9, c[1]*0.9, c[2]*0.9]); });
  for(let i=0;i<3;i++){ const d = St.d[i], m = Math.hypot(d[0], d[1], d[2]), u = new T.Vector3(d[0]/m, d[2]/m, -d[1]/m), p = pos[i], tip = p.clone().addScaledVector(u, 0.95), side = (Math.abs(u.y) < 0.9 ? new T.Vector3(0,1,0) : new T.Vector3(1,0,0)).cross(u).normalize();
    arrows.add(p, tip, [1,0.78,0.35]); arrows.add(tip, tip.clone().addScaledVector(u, -0.2).addScaledVector(side, 0.09), [1,0.9,0.6]); arrows.add(tip, tip.clone().addScaledVector(u, -0.2).addScaledVector(side, -0.09), [1,0.9,0.6]);
    const s = Math.min(1, 1.2*Math.sqrt(share[i])); M.setPt(corePts, i, p, [COLV[i][0]*s, COLV[i][1]*s, COLV[i][2]*s]); labels[i].position.set(p.x, p.y + RB + 0.35, p.z); }
  lens.done(); flowLine.done(); arrows.done(); M.flush(flowPts); M.flush(midPts); M.flush(corePts); }
/* ---- draw the page's ball three times; pull the camera back so the field fits ---- */
const R = S3.renderer, cam = S3.camera, scene = S3.scene, orig = R.render.bind(R), bg = scene.background ? scene.background.clone() : new T.Color(0x05070b);
R.toneMapping = T.LinearToneMapping;
R.render = function(sc, cm){ if(sc !== scene || !X.on){ FIELD.visible = false; WORLD.position.set(0,0,0); R.autoClear = true; scene.background = bg; R.toneMappingExposure = 1; return orig(sc, cm); }
  step(); const V = S3.view, ty = 0, Dc = V.dist*2.0*(window.innerWidth < 640 ? 1.5 : 1), pt = Math.max(-1.3, Math.min(1.35, V.pitch + 0.55)), yw = V.yaw + 0.55;   /* the field is seen from higher up and a little round, so the three balls stand apart */
  cam.position.set(Dc*Math.cos(pt)*Math.sin(yw), ty + Dc*Math.sin(pt), Dc*Math.cos(pt)*Math.cos(yw)); cam.lookAt(0, ty, 0); cam.updateMatrixWorld();
  scene.background = null; R.autoClear = false; R.setClearColor(bg, 1); R.clear();
  for(let b=0;b<3;b++){ WORLD.position.copy(pos[b]); FIELD.visible = b === 0; R.toneMappingExposure = 0.28 + 0.85*Math.min(1, share[b]); orig(sc, cm); }
  WORLD.position.set(0,0,0); R.toneMappingExposure = 1; };
/* ---- panel ---- */
const css = document.createElement('style'); css.textContent = `.tb{position:fixed;top:12px;right:12px;width:min(340px,calc(100% - 400px));max-height:calc(100% - 110px);overflow:auto;background:var(--panel,rgba(9,13,20,.86));border:1px solid var(--edge,#1f2a38);border-radius:8px;padding:11px 12px;font-size:12px;color:var(--ink,#dfe7ef);backdrop-filter:blur(6px);z-index:5}
.tb h2{margin:0 0 4px;font-size:13px;letter-spacing:.08em;text-transform:uppercase;font-family:var(--head,inherit)}.tb p{margin:4px 0 8px;color:var(--dim,#8a9aab);font-size:11.5px;line-height:1.5}
.tb .r{display:flex;flex-wrap:wrap;gap:5px;margin:5px 0}.tb button{font-size:11.5px;padding:4px 8px;background:#0e1520;color:inherit;border:1px solid var(--edge,#1f2a38);border-radius:5px;cursor:pointer}.tb button[aria-pressed=true]{border-color:#f2c14e;color:#f2c14e}
.tb .row{display:flex;justify-content:space-between;gap:10px;padding:4px 0;border-bottom:1px solid rgba(31,42,56,.6);color:var(--dim,#8a9aab)}.tb .row b{font-family:var(--mono,monospace);font-weight:400;color:var(--ink,#dfe7ef);text-align:right;font-size:11px;white-space:pre-wrap}
.tb .g{font-size:10px;color:var(--faint,#55657a);margin:-1px 0 2px}.tb input{accent-color:#63d3ff;width:120px;vertical-align:middle}body.clean .tb{display:none}
@media (max-width:900px){.tb{top:auto;bottom:60px;left:8px;right:8px;width:auto;max-height:34%}}`; document.head.append(css);
document.body.insertAdjacentHTML('beforeend', `<div class="tb" id="tb"><h2>Three balls on the field</h2>
<details><summary style="cursor:pointer;color:var(--dim,#8a9aab)">What this shows</summary><p>Three whole balls of the same kind, each with its own rim. Ball B sits one step out along A’s I arm and ball C one step out along A’s J arm, so the cap you see inside A on that arm is the other ball’s end pushing in, and A’s end pushes into it. Each ball is lit by the share of the energy it holds. The ring between two balls is where their rims meet: gold for what that face holds, white for what is crossing. One matrix moves the light, the electron sea and each ball’s field (the arrows).</p></details>
<div class="r"><button id="tb_three" aria-pressed="true">Three balls</button><button id="tb_one" aria-pressed="false">One ball</button><button id="tb_restart">Restart</button><button id="tb_sea">Sea pushes back: yes</button></div>
<div class="r"><button data-kick="0">Kick ball A</button><button data-kick="1">Kick ball B</button><button data-kick="2">Kick ball C</button></div>
<div class="r"><button id="tb_view">Lit by: the light in each ball</button><button id="tb_into">Put the light in this eigenvector</button></div>
<div class="r"><label>Eigenvector <span id="tb_on">5</span> <input id="tb_n" type="range" min="0" max="5" step="1" value="5"></label><button id="tb_lead">Leading eigenvector</button></div><div class="row"><span>light in A, B, C</span><b id="tb_sh"></b></div><details><summary style="cursor:pointer;color:var(--dim,#8a9aab)">All the numbers</summary><div id="tb_rows"></div></details></div>`);
const $ = id => document.getElementById(id);
function setOn(b){ X.on = b; $('tb_three').setAttribute('aria-pressed', b); $('tb_one').setAttribute('aria-pressed', !b); }
$('tb_three').addEventListener('click', () => setOn(true)); $('tb_one').addEventListener('click', () => setOn(false)); $('tb_restart').addEventListener('click', () => build());
$('tb_sea').addEventListener('click', () => { X.seaBack = !X.seaBack; $('tb_sea').textContent = 'Sea pushes back: ' + (X.seaBack ? 'yes' : 'no'); build(); });
document.querySelectorAll('#tb button[data-kick]').forEach(b => b.addEventListener('click', () => { X.src = +b.dataset.kick; kick(X.src); }));
$('tb_view').addEventListener('click', () => { X.view = X.view === 'light' ? 'mode' : 'light'; $('tb_view').textContent = X.view === 'light' ? 'Lit by: the light in each ball' : 'Lit by: the chosen eigenvector'; });
$('tb_into').addEventListener('click', () => intoMode()); $('tb_n').addEventListener('input', e => { X.n = +e.target.value; $('tb_on').textContent = X.n; });
$('tb_lead').addEventListener('click', () => { MD = TB.modes(W, St.d); X.n = MD.lead; $('tb_n').value = X.n; $('tb_on').textContent = X.n; });
const row = (a, b, g) => `<div class="row"><span>${a}</span><b>${b}</b></div>` + (g ? `<div class="g">${g}</div>` : '');
function rows(){ if(!W || !EN) return; const S = H.S(), lp = TB.loop(W, S.r), PW = MM.ballPowers(W, St), D = MM.deriv(W, St), g = MM.seaSpeed(W, St), C = MM.ballCensus(W, St); MD = TB.modes(W, St.d);
  let io = 0, lim = 0, norm = 0; for(let i=0;i<3;i++){ io = Math.max(io, Math.abs(PW[i].fromLight + PW[i].fromSea - PW[i].toFaces)); const td = MM.tauDot(W, St, D, i); lim = Math.max(lim, td*td/(4*g*C[i].S)); norm += MM.lightDensity(St, i); }
  const pr = k => NAMES[TB.PAIRS[k][0]] + NAMES[TB.PAIRS[k][1]], L3 = f => [0,1,2].map(k => pr(k) + ' ' + f(k)).join('   '), ld = MD.lead;
  let h = '';
  h += row('steps between the balls (hyperbolic)', L3(k => fmt(W.links[k].d, 3)), 'A–B is the I step, A–C the J step; B–C is the third side, cosh d = cosh r_I · cosh r_J');
  h += row('link strength c₀ sech(d/2) = c₀ √(1 − Γ²)', L3(k => fmt(W.links[k].c, 3)), 'VOTKP peel step, Γ = tanh(d/2); c₀ = 0.5, ω = 2, κ = 0.25 are model choices');
  h += row('light in each ball', [0,1,2].map(i => NAMES[i] + ' ' + fmt(MM.lightDensity(St, i), 3)).join('   '));
  h += row('flow across each face (into the first named)', L3(k => fmt(CUR[k], 4)));
  h += row('held on each face (connection energy)', L3(k => fmt(EN.Eper[k], 4)), 'κ|dᵢ − Rᵢⱼ dⱼ|²: the mismatch of the two balls’ fields carried across the face');
  h += row('loop A → B → C → A: turn | area | 2 arctan(Γ_I Γ_J)', fmt(lp.ang, 6) + ' | ' + fmt(lp.area, 6) + ' | ' + fmt(lp.thomas, 6), 'the frame carried round the three balls turns by the triangle’s area, which is the Thomas turn of the two steps');
  h += row('books: change − work by the breathing steps − light put in', sci(EN.E - E0 - St.work - IN) + '  (work ' + fmt(St.work, 4) + ')');
  h += row('light norm − 1;  each ball passes on all it takes', sci(norm - 1) + ';  ' + sci(io));
  h += row('light reached the ball / the sea answered', [0,1,2].map(i => NAMES[i] + ' ' + (AL[i] === null ? '—' : fmt(AL[i], 2)) + ' / ' + (AS[i] === null ? '—' : fmt(AS[i], 2))).join('   '), 'first time |ψ|² > 10⁻³ / the sea’s occupation moved by 10⁻³');
  h += row('clock limit τ̇² ≤ 4gS, largest ratio', fmt(lim, 5), 'g = ‖PH(1−P)‖² = ' + fmt(g, 4));
  h += row('eigenvalues of the three-ball matrix', MD.vals.map(x => fmt(x, 3)).join('  '));
  h += row('eigenvector ' + X.n + ': share on A, B, C', MD.share[X.n].map(x => fmt(x, 3)).join('   '));
  h += row('leading eigenvector (' + ld + '): share on A, B, C', MD.share[ld].map(x => fmt(x, 3)).join('   '), 'margin |λ₂/λ₁| = ' + fmt(MD.margin, 4) + ': how strongly the leading one wins the vote');
  $('tb_rows').innerHTML = h; $('tb_sh').textContent = [0,1,2].map(i => NAMES[i] + ' ' + fmt(MM.lightDensity(St, i), 3)).join('   '); }
setInterval(rows, 250);
window.__tb = { X, build, kick, intoMode, rows, setOn, get state(){ return { W, St, EN, E0, IN, AL, AS, MD, share, CUR, pos }; }, books:() => EN.E - E0 - St.work - IN };
})();
