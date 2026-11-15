/* SCRIPT: MM-MIXER-V1
   The Moving Matrix of Balls, Mixer v1 — Jeromie Beasley — 15 Nov 2026 — AI-assisted.
   One law moves everything: light hops on the links, the electron sea (the gapped ground projector) evolves under the same matrix,
   and each ball turns under the light, the sea and its faces. Built on 3D Mixer Parts v1 and MM-MATH-V1. */
(function(){
"use strict";
const K = window.Mixer3D, T = K.T, MM = window.MM, PI = Math.PI, RB = 2.6, REST = window.MM_REST;
const V3 = (x,y,z) => new T.Vector3(x,y,z);
const fmt = (x,n=4) => Number.isFinite(x) ? x.toFixed(n) : '—', sci = x => Number.isFinite(x) ? x.toExponential(2) : '—';
const toBall = p => { const k = RB/(1+p[0]); return V3(p[1]*k, p[3]*k, -p[2]*k); };
const w3 = u => V3(u[0], u[2], -u[1]);
const still = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
/* ---------------- the clock and the world ---------------- */
const CLOCK = { t:0, playing:!still, speed:1, h:0.01 };
const P = { level:2, source:0, kappa:0.25, c0:0.5, omega:2.0, seaBack:true };
let W = null, S = null, E0 = null, NN = null, HOL = null, ARR = null, NU0 = null, INPUT = 0, CUR = null, EN = null, PW = null, CEN = null, G = NaN, DRV = null;
function build(){ W = MM.makeWorld(P.level, { kappa:P.kappa, c0:P.c0, omega:P.omega, seaBack:P.seaBack }); W.d = REST['L'+P.level].map(v => v.slice());
  S = MM.initState(W, { source:P.source, noSea:P.level === 3 }); E0 = MM.energies(W, S); INPUT = 0; CLOCK.t = 0;
  NN = P.level < 3 ? MM.nnceCheck(W, W.d) : null; HOL = W.tris.map(t => MM.triangleHolonomy(W, t));
  ARR = { light:Array(W.N).fill(null), sea:Array(W.N).fill(null) }; NU0 = S.Pr ? MM.ballCensus(W, S).map(c => c.nu[0]) : null;
  refresh(); scene.rebuild(); }
function sendPhoton(){ const before = MM.energies(W, S).E, S2 = MM.initState(Object.assign({}, W, { d:S.d }), { source:P.source, noSea:true }); S.psr = S2.psr; S.psi = S2.psi; INPUT += MM.energies(W, S).E - before; }
function refresh(){ EN = MM.energies(W, S); CUR = MM.lightCurrents(W, S); PW = MM.ballPowers(W, S); CEN = S.Pr ? MM.ballCensus(W, S) : null; G = S.Pr ? MM.seaSpeed(W, S) : NaN; DRV = S.Pr ? MM.deriv(W, S) : null; }
function advance(dtReal){ if(!CLOCK.playing) return; const budget = P.level === 2 ? 2 : P.level === 3 ? 4 : 8, want = Math.max(1, Math.min(budget, Math.round(dtReal*CLOCK.speed/CLOCK.h)));
  for(let k=0;k<want;k++) stepOnce();
  refresh(); }
function stepOnce(){ S = MM.rk4(W, S, CLOCK.h); CLOCK.t = S.t;
  for(let i=0;i<W.N;i++){ if(ARR.light[i] === null && MM.lightDensity(S, i) > 1e-3) ARR.light[i] = S.t; }
  if(S.Pr){ const c = MM.ballCensus(W, S); for(let i=0;i<W.N;i++) if(ARR.sea[i] === null && Math.abs(c[i].nu[0] - NU0[i]) > 1e-3) ARR.sea[i] = S.t; } }
/* ---------------- emphasis ---------------- */
const COMPS = ['balls','links','light','faces','loops','sea','rim'], Wt = {}, Wg = {}; COMPS.forEach(c => { Wt[c] = 1; Wg[c] = 1; }); const REG = [];
const reg = (m, c, b) => { m.transparent = true; REG.push([m, c, b == null ? m.opacity : b]); return m; };
function applyEmph(dt){ const k = Math.min(1, dt*4); COMPS.forEach(c => { Wt[c] += (Wg[c]-Wt[c])*k; }); REG.forEach(([m,c,b]) => { m.opacity = b*Wt[c]; m.visible = Wt[c] > 0.01; }); }
/* ---------------- the scene: one object ---------------- */
const WORLD = new T.Group(); const G_ = {}; COMPS.forEach(c => { G_[c] = new T.Group(); WORLD.add(G_[c]); });
(function rim(){ const sh = K.shell(RB, 0x63d3ff, 0.03); reg(sh.material, 'rim', 0.03); G_.rim.add(sh);
  for(let k=0;k<3;k++){ const p = []; for(let i=0;i<=128;i++){ const a = 2*PI*i/128, c = RB*Math.cos(a), s = RB*Math.sin(a); p.push(k===0 ? V3(c,0,s) : k===1 ? V3(c,s,0) : V3(0,c,s)); } const l = K.line(p, 0x63d3ff, k===0 ? 0.4 : 0.15); reg(l.material, 'rim'); G_.rim.add(l); } })();
const scene = { objs:[], rebuild(){ for(const o of this.objs){ o.parent && o.parent.remove(o); o.geometry && o.geometry.dispose(); const i = REG.findIndex(r => r[0] === o.material); if(i >= 0) REG.splice(i,1); } this.objs = [];
    const add = (o, c, b) => { reg(o.material, c, b); G_[c].add(o); this.objs.push(o); return o; };
    const N = W.N, pos = W.balls.map(b => toBall(b.p)), size = W.balls.map(b => 0.03 + 0.11*(1 - Math.min(1, toBall(b.p).lengthSq()/(RB*RB))));
    this.pos = pos; this.size = size;
    /* balls as instanced spheres */
    const im = new T.InstancedMesh(new T.SphereGeometry(1, 16, 12), new T.MeshStandardMaterial({ color:0xffffff, emissive:0x223344, roughness:0.45, transparent:true, opacity:0.95 }), N);
    const mtx = new T.Matrix4(); for(let i=0;i<N;i++){ mtx.makeScale(size[i], size[i], size[i]); mtx.setPosition(pos[i]); im.setMatrixAt(i, mtx); im.setColorAt(i, new T.Color(0xdfe7ef)); } im.instanceMatrix.needsUpdate = true; add(im, 'balls', 0.95); this.im = im;
    /* ball arrows: the direction of each ball's field d_i (its subspace) */
    const ag = new T.BufferGeometry(); ag.setAttribute('position', new T.BufferAttribute(new Float32Array(N*6), 3)); ag.setAttribute('color', new T.BufferAttribute(new Float32Array(N*6), 3));
    this.arrows = add(new T.LineSegments(ag, new T.LineBasicMaterial({ vertexColors:true, transparent:true, opacity:1 })), 'balls', 1);
    /* links: geodesic segments */
    const L = W.links.length, SEG = 8, lg = new T.BufferGeometry(); lg.setAttribute('position', new T.BufferAttribute(new Float32Array(L*SEG*6), 3)); lg.setAttribute('color', new T.BufferAttribute(new Float32Array(L*SEG*6), 3));
    this.geo = W.links.map(l => { const pi = W.balls[l.i].p, pj = W.balls[l.j].p, dd = l.d, out = []; for(let s=0;s<=SEG;s++){ const t = s/SEG, a = Math.sinh((1-t)*dd)/Math.sinh(dd), b = Math.sinh(t*dd)/Math.sinh(dd); out.push(toBall(pi.map((x,k) => a*x + b*pj[k]))); } return out; });
    const lp = lg.attributes.position; let q = 0; for(const g of this.geo) for(let s=0;s<SEG;s++){ lp.setXYZ(q++, g[s].x, g[s].y, g[s].z); lp.setXYZ(q++, g[s+1].x, g[s+1].y, g[s+1].z); }
    this.links = add(new T.LineSegments(lg, new T.LineBasicMaterial({ vertexColors:true, transparent:true, opacity:0.9, blending:T.AdditiveBlending, depthWrite:false })), 'links', 0.9);
    /* light markers moving along links with the current */
    this.lm = add(K.points(Math.min(12000, L*14), 0.06), 'light', 1);
    /* light glow at balls */
    this.glow = add(K.points(N, 0.5), 'light', 1);
    /* faces: a small disc at the halfway point of every link, across the link (the hypersurface) */
    const fg = new T.BufferGeometry(), FS = 14; fg.setAttribute('position', new T.BufferAttribute(new Float32Array(L*FS*3*3), 3)); fg.setAttribute('color', new T.BufferAttribute(new Float32Array(L*FS*3*3), 3));
    const fp = fg.attributes.position; q = 0; this.faceMid = [];
    W.links.forEach((l, k) => { const g = this.geo[k], mid = g[SEG/2], dir = g[SEG/2+1].clone().sub(g[SEG/2-1]).normalize(), e1 = (Math.abs(dir.y) < 0.9 ? V3(0,1,0) : V3(1,0,0)).cross(dir).normalize(), e2 = dir.clone().cross(e1), r = 0.55*Math.min(size[l.i], size[l.j]) + 0.01;
      this.faceMid.push(mid); for(let s=0;s<FS;s++){ const a0 = 2*PI*s/FS, a1 = 2*PI*(s+1)/FS; const v0 = mid, v1 = mid.clone().addScaledVector(e1, r*Math.cos(a0)).addScaledVector(e2, r*Math.sin(a0)), v2 = mid.clone().addScaledVector(e1, r*Math.cos(a1)).addScaledVector(e2, r*Math.sin(a1)); for(const v of [v0,v1,v2]) fp.setXYZ(q++, v.x, v.y, v.z); } });
    this.faces = add(new T.Mesh(fg, new T.MeshBasicMaterial({ vertexColors:true, transparent:true, opacity:0.9, side:T.DoubleSide, blending:T.AdditiveBlending, depthWrite:false })), 'faces', 0.9); this.FS = FS;
    /* loops: every triangle tinted by its holonomy (the turn of a frame carried round it) */
    const tg = new T.BufferGeometry(), nt = W.tris.length; tg.setAttribute('position', new T.BufferAttribute(new Float32Array(nt*9), 3)); tg.setAttribute('color', new T.BufferAttribute(new Float32Array(nt*9), 3));
    const hmax = Math.max(1e-9, ...HOL.filter(Boolean).map(h => h.ang)); W.tris.forEach((t, k) => { const h = HOL[k], c = K.colour.ramp(h ? 0.15 + 0.8*h.ang/hmax : 0); t.forEach((v, j) => { tg.attributes.position.setXYZ(3*k+j, pos[v].x, pos[v].y, pos[v].z); tg.attributes.color.setXYZ(3*k+j, c[0]*0.5, c[1]*0.5, c[2]*0.5); }); });
    add(new T.Mesh(tg, new T.MeshBasicMaterial({ vertexColors:true, transparent:true, opacity:0.18, side:T.DoubleSide, depthWrite:false })), 'loops', 0.18);
    /* sea rings: one ring per ball whose share of the sea is drawn as its lit fraction */
    this.sea = add(K.points(N*24, 0.045), 'sea', 1);
  },
  update(t){ if(!this.im) return; const N = W.N;
    /* ball colours: the sea's Smith coordinate Gamma = 1 - 2 nu (lower level), or white when the sea is not run */
    const col = new T.Color(); for(let i=0;i<N;i++){ if(CEN){ const g = CEN[i].Gamma[0]; const c = K.colour.ramp(0.5 + 0.5*g); col.setRGB(c[0], c[1], c[2]); } else col.setRGB(0.85,0.9,0.95); this.im.setColorAt(i, col); } this.im.instanceColor.needsUpdate = true;
    const ap = this.arrows.geometry.attributes.position, ac = this.arrows.geometry.attributes.color;
    for(let i=0;i<N;i++){ const d = S.d[i], m = Math.hypot(...d), u = w3(d.map(x=>x/m)), p = this.pos[i], q = p.clone().addScaledVector(u, this.size[i]*2.2); ap.setXYZ(2*i, p.x, p.y, p.z); ap.setXYZ(2*i+1, q.x, q.y, q.z); ac.setXYZ(2*i, 1, 0.8, 0.4); ac.setXYZ(2*i+1, 1, 0.95, 0.7); } ap.needsUpdate = ac.needsUpdate = true;
    const jmax = Math.max(1e-6, ...CUR.map(Math.abs)), lc = this.links.geometry.attributes.color, SEG = 8; let q = 0;
    CUR.forEach((j, k) => { const f = Math.sqrt(Math.abs(j)/jmax), c = [0.12 + 0.88*f, 0.25 + 0.6*f, 0.45 + 0.5*f]; for(let s=0;s<2*SEG;s++) lc.setXYZ(q++, c[0]*0.6, c[1]*0.6, c[2]*0.7); }); lc.needsUpdate = true;
    /* markers: spacing fixed, motion along the link in the direction of the flow (J > 0 is from j to i), count by strength */
    const lm = this.lm; lm.userData.n = 0; let n = 0; const cap = lm.geometry.attributes.position.count;
    CUR.forEach((j, k) => { const f = Math.abs(j)/jmax; if(f < 0.02) return; const g = this.geo[k], per = 6, phase = ((t*0.8*Math.sign(-j)) % 1 + 1) % 1;
      for(let m=0;m<per && n<cap;m++){ let s = ((m + phase*1)/per); s = ((s % 1) + 1) % 1; const x = s*SEG, i0 = Math.min(SEG-1, Math.floor(x)), fr = x - i0, p = g[i0].clone().lerp(g[i0+1], fr); K.setPt(lm, n++, p, [1*Math.sqrt(f), 0.92*Math.sqrt(f), 0.6*Math.sqrt(f)]); } });
    for(let i=n;i<cap;i++) K.setPt(lm, i, V3(0,0,0), [0,0,0]); K.flush(lm);
    for(let i=0;i<N;i++){ const r = MM.lightDensity(S, i); K.setPt(this.glow, i, this.pos[i], [Math.min(1, 2*Math.sqrt(r)), Math.min(1, 1.7*Math.sqrt(r)), Math.min(1, 1.2*Math.sqrt(r))]); } K.flush(this.glow);
    /* faces: energy above rest on each face */
    const er = EN.Eper, e0 = this.face0 || (this.face0 = er.slice()), fc = this.faces.geometry.attributes.color, FS = this.FS; q = 0; const emax = Math.max(1e-6, ...er.map((e,k) => Math.abs(e - e0[k])));
    er.forEach((e, k) => { const de = (e - e0[k])/emax, c = de >= 0 ? [0.25 + 0.75*de, 0.2 + 0.5*de, 0.35] : [0.2, 0.3 + 0.4*(-de), 0.45 + 0.55*(-de)], base = 0.25; for(let s=0;s<FS*3;s++) fc.setXYZ(q++, base + c[0]*0.8, base*0.8 + c[1]*0.6, base + c[2]*0.6); }); fc.needsUpdate = true;
    /* sea rings */
    const sea = this.sea; let m = 0; for(let i=0;i<N;i++){ const r = this.size[i]*1.7, frac = CEN ? CEN[i].nu[0] : 0; for(let k=0;k<24;k++){ const a = 2*PI*k/24, p = this.pos[i].clone().add(V3(r*Math.cos(a), r*Math.sin(a), 0)), lit = k/24 < frac; K.setPt(sea, m++, p, lit ? [0.4, 0.9, 1] : [0.08, 0.12, 0.16]); } } K.flush(sea); } };
/* ---------------- chips and rows ---------------- */
const chip = (t, k) => `<span class="chip ${k||''}">${t}</span>`, LEAN = t => chip('LEAN · ' + t, 'lean'), PROV = t => chip('PROVED · ' + t), CHK = t => chip('CHECKED · ' + t), READ = chip('READING'), MODEL = chip('MODEL CHOICE', 'hyp');
const lvl = () => ['clock t  ·  level', fmt(CLOCK.t,2) + '  ·  ' + P.level + ' (' + W.N + ' balls, ' + W.links.length + ' links)'];
const levelBtns = () => `<div class="row">${[1,2,3].map(l => `<button data-level="${l}" aria-pressed="${P.level===l}">${l===1?'one super ball (7)':l===2?'super of supers (49)':'third series (343)'}</button>`).join('')}</div><div class="row"><button id="photon">Send a photon from the source ball</button></div>`;
function bind(){ document.querySelectorAll('#ctl button[data-level]').forEach(b => b.addEventListener('click', () => { P.level = +b.dataset.level; build(); document.querySelectorAll('#ctl button[data-level]').forEach(q => q.setAttribute('aria-pressed', q === b)); }));
  const ph = document.getElementById('photon'); if(ph) ph.addEventListener('click', () => { sendPhoton(); }); }
const EMPH = { A:{balls:1,links:1,light:1,faces:0.7,loops:0.6,sea:0.6,rim:1}, B:{balls:0.6,links:1,light:1,faces:0.3,loops:0.15,sea:0.2,rim:0.6}, C:{balls:1,links:0.6,light:0.8,faces:1,loops:0.2,sea:0.3,rim:0.6},
  D:{balls:0.6,links:0.5,light:0.4,faces:1,loops:0.3,sea:0.2,rim:0.6}, E:{balls:0.6,links:0.6,light:0.3,faces:0.3,loops:1,sea:0.1,rim:0.6}, F:{balls:1,links:0.5,light:0.4,faces:0.3,loops:0.15,sea:1,rim:0.6},
  G:{balls:1,links:0.4,light:0.4,faces:0.3,loops:0.15,sea:1,rim:0.6}, H:{balls:0.8,links:0.8,light:1,faces:0.3,loops:0.15,sea:1,rim:0.6}, I:{balls:1,links:1,light:1,faces:1,loops:1,sea:0.6,rim:0.6}, J:{balls:1,links:1,light:1,faces:1,loops:1,sea:1,rim:1} };
const VIEW = { A:[0.6,0.35,7.6,0], B:[0.9,0.4,7.0,0], C:[0.4,0.3,6.6,0], D:[0.4,0.5,6.6,0], E:[0.7,0.8,7.0,0], F:[0.6,0.3,7.2,0], G:[0.6,0.3,7.2,0], H:[0.9,0.3,7.4,0], I:[0.5,0.45,7.6,0], J:[0.6,0.35,8.0,0] };
let made = false; const curEye = { id:'A' };
function eye(o){ return Object.assign({ make(g, S3){ if(!made){ S3.world.add(WORLD); made = true; } }, enter(){ Object.assign(Wg, EMPH[o.id]); curEye.id = o.id; }, bind, extra:levelBtns, view:VIEW[o.id],
  step(dt){ advance(Math.min(0.05, Math.max(0, dt))); scene.update(CLOCK.t); applyEmph(dt); strip(); return o.rows(); } }, o); }
const noSea = () => [['the sea', 'not run at the third series (686 × 686 projector is too large for a live page); light, balls and faces run in full']];
const E_A = eye({ id:'A', title:'A · The series of super balls in one ball', section:'VOTKP peel step; Non-Normality Is Connection Energy', grade: LEAN('VOTKP: Γ = tanh(½ ln z)') + LEAN('connection energy (block form)') + MODEL,
  eq:'ball i:  Dᵢ = dᵢ·σ   (levels ±|dᵢ|, the ground half a quantum down)\nlink i–j:  cᵢⱼ Uᵢⱼ,   Uᵢⱼ = transport of the ball between them\ncᵢⱼ = c₀ √(1 − Γᵢⱼ²) = c₀ sech(dᵢⱼ/2),   Γᵢⱼ = tanh(dᵢⱼ/2)\nH = D + (links):  one matrix for light, sea and balls',
  text:'A super ball is seven balls: a centre and six neighbours, each one peel step out along an axis, joined to the centre and to each other where they meet. The next series places seven super balls the same way, and the next seven of those: 7, 49, 343 balls, all in one ball. Every link carries the transport of the ball between its two ends, and its strength is the transmitted part of a step, √(1 − Γ²). Each ball’s arrow is the direction of its own field, its subspace. Nothing moves until light arrives: the matrix starts at the rest of its faces, and the photon is sent from the source ball.',
  rows(){ const r = [lvl(), ['light energy, faces, sea (from rest)', fmt(EN.EL,4) + ',  ' + fmt(EN.EF,4) + ',  ' + (S.Pr ? fmt(EN.ES - EN.Erest,4) : '—')], ['conserved total, change since start', sci(EN.E - E0.E - INPUT)], ['light delivered by photons sent', fmt(INPUT,4)]]; return S.Pr ? r : r.concat(noSea()); } });
const E_B = eye({ id:'B', title:'B · Every path the light takes', section:'continuity on the matrix', grade: PROV('continuity of the light (Hermitian H)') + CHK('live'),
  eq:'Jᵢⱼ = 2 Im( ψᵢ† cᵢⱼ Uᵢⱼ ψⱼ )      (flow from j into i)\nd|ψᵢ|²/dt = Σⱼ Jᵢⱼ',
  text:'The light is one quantum spread over the matrix. On every link its flow is exact, and what leaves a ball arrives at its neighbours. The bright markers run along each link in the sense of the flow, and their brightness is its size. Turn to the third series to watch the light find its way through all 343 balls and 1026 links.',
  rows(){ let worst = 0; /* continuity: compare d|psi_i|^2/dt from the derivative with the sum of currents */ const D = MM.deriv(W, S);
    for(let i=0;i<W.N;i++){ const a = 2*i, b = a+1; const dr = 2*(S.psr[a]*D.dpsr[a] + S.psi[a]*D.dpsi[a] + S.psr[b]*D.dpsr[b] + S.psi[b]*D.dpsi[b]); let sum = 0; W.links.forEach((l,k) => { if(l.i === i) sum += CUR[k]; else if(l.j === i) sum -= CUR[k]; }); worst = Math.max(worst, Math.abs(dr - sum)); }
    const top = CUR.map((j,k) => [Math.abs(j), k]).sort((a,b) => b[0]-a[0]).slice(0,4);
    let norm = 0; for(let i=0;i<W.N;i++) norm += MM.lightDensity(S,i);
    return [lvl(), ['continuity, worst ball', sci(worst)], ['light norm', fmt(norm,10)]].concat(top.map(([j,k]) => ['strongest flow, link ' + W.links[k].i + '–' + W.links[k].j, fmt(CUR[k],5)])); } });
const E_C = eye({ id:'C', title:'C · The ball passes the energy on', section:'derived for this matrix', grade: PROV('ḋᵢ · Fᵢ = 0 for ḋᵢ = Fᵢ × dᵢ') + CHK('live'),
  eq:'ḋᵢ = Fᵢ × dᵢ,   Fᵢ = sᵢ(light) + [sᵢ(sea) − sᵢ(sea at rest)] + 2κ Σⱼ (dᵢ − Rᵢⱼ dⱼ)\npower in from light and sea  =  power out to the faces',
  text:'Each ball turns under three pushes: the light passing through it, the sea’s change from its rest, and its faces. It turns without changing its size, so it can store nothing: every kick it takes from the light goes straight on into its faces, and the ball itself only passes the energy along. The readout shows it ball by ball, every frame.',
  rows(){ let worst = 0, top = PW.map((p,i) => [Math.abs(p.fromLight)+Math.abs(p.fromSea), i]).sort((a,b) => b[0]-a[0]).slice(0,4); PW.forEach(p => worst = Math.max(worst, Math.abs(p.fromLight + p.fromSea - p.toFaces)));
    return [lvl(), ['worst ball: in − out', sci(worst)]].concat(top.map(([_,i]) => ['ball ' + i + ': from light, from sea, to faces', fmt(PW[i].fromLight,5) + ',  ' + fmt(PW[i].fromSea,5) + ',  ' + fmt(PW[i].toFaces,5)])); } });
const E_D = eye({ id:'D', title:'D · The faces halfway hold the energy', section:'Non-Normality Is Connection Energy', grade: LEAN('connection energy identity') + CHK('dense matrix, live') + READ,
  eq:'face i–j:  κ |dᵢ − Rᵢⱼ dⱼ|²   (half of ‖Dᵢ − Uᵢⱼ Dⱼ Uᵢⱼ*‖²)\n⅛ ‖[H, H*]‖² = Σ faces ‖Dᵢ − Uᵢⱼ Dⱼ Uᵢⱼ*‖²   (H = D + A, unitary links)',
  text:'Between every two balls, at the halfway point of their link, sits a face. The energy of the matrix that is not light lives there, as the mismatch of the two balls’ fields carried across the link. Gold faces hold more than at rest, blue faces less. The identity that puts this energy on the faces is the connection-energy theorem: the non-normality of D + A equals the sum of the face mismatches.',
  rows(){ const er = EN.Eper, e0 = scene.face0 || er, top = er.map((e,k) => [e - e0[k], k]).sort((a,b) => Math.abs(b[0]) - Math.abs(a[0])).slice(0,4);
    const r = [lvl(), ['faces total', fmt(EN.EF,6)], ['NNCE: ⅛‖[H,H*]‖², Σ faces (at rest)', NN ? fmt(NN.lhs,10) + ',  ' + fmt(NN.rhs,10) : '— (third series)']]; return r.concat(top.map(([de,k]) => ['face ' + W.links[k].i + '–' + W.links[k].j + ' change from rest', fmt(de,6)])); } });
const E_E = eye({ id:'E', title:'E · Curvature on the loops', section:'Yang–Mills on the ball', grade: CHK('holonomy = area, every triangle') + PROV('Gauss–Bonnet, curvature −1'),
  eq:'Hol(ijk) = Rᵢⱼ Rⱼₖ Rₖᵢ,    angle = π − (sum of the triangle’s angles) = area',
  text:'Carry a ball’s frame round a closed loop of links and it comes back turned. On the ball that turn is the area the loop encloses: the curvature of the space the balls live in, read by the links themselves. This is the gauge field of the matrix. Bright loops turn the most; a field cannot be parallel round a loop that turns, and that leftover is what the faces must hold.',
  rows(){ let worst = 0, mx = 0; HOL.forEach(h => { if(!h) return; worst = Math.max(worst, Math.abs(h.ang - h.area)); mx = Math.max(mx, h.ang); }); return [lvl(), ['loops', String(HOL.length)], ['worst |holonomy − area|', sci(worst)], ['largest turn on a loop', fmt(mx*180/PI,4) + '°']]; } });
const E_F = eye({ id:'F', title:'F · The sea is the ground, and rate is weight', section:'IQGT; The Weight Between', grade: LEAN('weight between (algebra)') + PROV('IQGT: tangent off-diagonal') + PROV('g = ‖PH(1−P)‖²') + CHK('live'),
  eq:'P = Riesz projector below the gapped cut nearest half filling\nṖ = −i[H, P]:  off-diagonal, g = ½‖Ṗ‖² = ‖PH(1−P)‖²\nsea energy change = ∫ Tr(P Ḣ) dt',
  text:'The electron sea is the ground of the whole matrix: the projector onto the levels below a gap, held by that gap. It is not relaxed by hand. It evolves under the same matrix as the light, and as the balls turn it is dragged. Its speed is the weight between the kept levels and the rest, ‖PH(1 − P)‖². The rings round each ball show how much of that ball the sea fills.',
  rows(){ if(!S.Pr) return [lvl()].concat(noSea()); return [lvl(), ['sea rank and gap at rest', S.kSea + ',  ' + fmt(S.gap0,5)], ['g = ‖PH(1−P)‖²', fmt(G,6)], ['sea energy change since start', fmt(EN.ES - E0.ES,6)], ['sea pushes back on the balls', P.seaBack ? 'yes (measured from its rest)' : 'no']]; } });
const E_G = eye({ id:'G', title:'G · Each ball’s clock is its offset', section:'The Weight Between; VOTKP; Dirac Time', grade: PROV('Γ = 1 − 2ν (bridge)') + PROV('τ̇² ≤ 4gS') + CHK('live') + READ,
  eq:'Cᵢ = the sea on ball i (2 × 2),   ν its occupations,   Γ = 1 − 2ν = tanh(ε/2)\nτᵢ = log det(I − Cᵢ)/det Cᵢ:  the clock face\nτ̇ᵢ² ≤ 4 g Sᵢ,   Sᵢ = Tr[(Cᵢ(I − Cᵢ))⁻¹]',
  text:'Each ball reads the sea on itself as two occupations, and each occupation as a Smith coordinate Γ = 1 − 2ν: the same coordinate as the peel step. Their sum, the offset τ, is the ball’s clock face; it is read from what the sea keeps, not from an outside clock. No clock can run faster than the sea moves: τ̇² ≤ 4gS. The ball colours are Γ of the lower occupation.',
  rows(){ if(!S.Pr) return [lvl()].concat(noSea()); let worst = 0; const rows = [lvl()]; for(let i=0;i<W.N;i++){ const td = MM.tauDot(W, S, DRV, i), r = td*td/(4*G*CEN[i].S); worst = Math.max(worst, r); }
    rows.push(['largest τ̇²/(4gS) over the balls', fmt(worst,6)]); for(const i of [0,1,2,3].filter(i => i < W.N)) rows.push(['ball ' + i + ': Γ, τ', fmt(CEN[i].Gamma[0],4) + ' / ' + fmt(CEN[i].Gamma[1],4) + ',  ' + fmt(CEN[i].tau,4)]); return rows; } });
const E_H = eye({ id:'H', title:'H · Light arrives before the electron', section:'measured on the matrix', grade: chip('MEASURED') + READ,
  eq:'light arrival:  first t with |ψᵢ|² > 10⁻³\nsea response:  first t with |νᵢ − νᵢ(0)| > 10⁻³',
  text:'Nothing in the matrix sets the speed of the electron sea. The light hops on the links; the sea only moves as the turning balls change the matrix under it. The table shows, ball by ball, when the light first arrives and when the sea first answers. The order is decided by the matrix, not chosen.',
  rows(){ if(!S.Pr) return [lvl()].concat(noSea()); const rows = [lvl()]; let first = 0, both = 0; for(let i=1;i<W.N;i++){ const a = ARR.light[i], b = ARR.sea[i]; if(a !== null && b !== null){ both++; if(a < b) first++; } }
    rows.push(['balls where light came first / both arrived', first + ' / ' + both]); for(const i of [1,4,7,9,12,20].filter(i => i < W.N)) rows.push(['ball ' + i + ': light, sea', (ARR.light[i] === null ? '—' : fmt(ARR.light[i],2)) + ',  ' + (ARR.sea[i] === null ? '—' : fmt(ARR.sea[i],2))]); return rows; } });
const E_I = eye({ id:'I', title:'I · Where the transport strains', section:'read from the math', grade: chip('MEASURED') + READ,
  eq:'strain on a face: its energy above rest\nstrain on a ball: τ̇²/(4gS) near 1\ntrapped light: density that stays',
  text:'All the energy uses the same links: light, sea and faces. Where the math says transport should pass and it does not, it shows here: the faces that pile up energy, the balls whose clocks run nearest their limit, the loops that turn the most, and the balls where the light stays.',
  rows(){ const er = EN.Eper, e0 = scene.face0 || er, f = er.map((e,k) => [e - e0[k], k]).sort((a,b) => b[0]-a[0])[0]; const lit = Array.from({length:W.N}, (_,i) => [MM.lightDensity(S,i), i]).sort((a,b) => b[0]-a[0]).slice(0,3);
    const rows = [lvl(), ['face holding the most above rest', W.links[f[1]].i + '–' + W.links[f[1]].j + ',  ' + fmt(f[0],6)]]; lit.forEach(([r,i]) => rows.push(['light held at ball ' + i, fmt(r,4)]));
    if(S.Pr){ let wi = 0, wr = 0; for(let i=0;i<W.N;i++){ const td = MM.tauDot(W,S,DRV,i), r = td*td/(4*G*CEN[i].S); if(r > wr){ wr = r; wi = i; } } rows.push(['ball nearest its clock limit', wi + ',  ' + fmt(wr,5)]); } return rows; } });
const E_J = eye({ id:'J', title:'J · Everything at once, and the books', section:'audit of every frame', grade: CHK('live'),
  eq:'E = light + faces + sea − (rest field · d)   is conserved\nlight norm = 1,   P² = P,   ball in = ball out',
  text:'All parts at once. The books: the conserved energy of the whole matrix, the light’s norm, the balls’ pass-through and the sea’s projector property. What is not claimed: the link strengths, the ball quantum and the face stiffness κ are model choices, not derived; the sea does not run live at the third series; the rest state is computed from the faces alone and the sea is measured from its rest; numbers are on a finite matrix and say nothing yet about a continuum.',
  extra:() => levelBtns() + `<div class="row"><button id="selfbtn">Run the books now</button></div>`,
  rows(){ let norm = 0; for(let i=0;i<W.N;i++) norm += MM.lightDensity(S,i); let worst = 0; PW.forEach(p => worst = Math.max(worst, Math.abs(p.fromLight + p.fromSea - p.toFaces)));
    let idem = '—'; if(S.Pr && W.N <= 7){ const n = 2*W.N; let e = 0; for(let i=0;i<n;i++) for(let j=0;j<n;j++){ let r = 0, im = 0; for(let q=0;q<n;q++){ r += S.Pr[i][q]*S.Pr[q][j] - S.Pi[i][q]*S.Pi[q][j]; im += S.Pr[i][q]*S.Pi[q][j] + S.Pi[i][q]*S.Pr[q][j]; } e = Math.max(e, Math.abs(r - S.Pr[i][j]), Math.abs(im - S.Pi[i][j])); } idem = sci(e); }
    return [lvl(), ['conserved energy, change since start (less photons sent)', sci(EN.E - E0.E - INPUT)], ['light norm − 1', sci(norm - 1)], ['worst ball in − out', sci(worst)], ['P² − P (first series)', idem]]; } });
/* ---------------- run ---------------- */
K.run({ title:'The Moving Matrix of Balls', byline:'JEROMIE BEASLEY · MIXER v1 · 15 NOV 2026 · AI-ASSISTED', note:'an explorer of checked formulas, not a test of them',
  feed:{ params:[], build(){ return P; } }, eyes:[E_A,E_B,E_C,E_D,E_E,E_F,E_G,E_H,E_I,E_J], film:['A','B','C','D','E','F','G','H','I','J'] });
const css = document.createElement('style'); css.textContent = `.chip{display:inline-block;font-family:var(--mono);font-size:10px;letter-spacing:.04em;color:#05070b;background:#8fd9ff;border-radius:3px;padding:1px 5px;margin:2px 4px 2px 0}.chip.lean{background:#f2c14e}.chip.hyp{background:transparent;color:#ffb347;border:1px solid #ffb347}
.strip{position:fixed;bottom:calc(12px + env(safe-area-inset-bottom,0px));right:12px;display:flex;flex-wrap:wrap;gap:5px;align-items:center;max-width:min(520px,calc(100% - 390px));justify-content:flex-end;background:var(--panel);border:1px solid var(--edge);border-radius:8px;padding:7px 8px;font-size:12px}
.strip button{font-size:11.5px;padding:4px 8px}.strip .tau{font-family:var(--mono);min-width:80px}.strip input{width:80px;accent-color:var(--cyan)}body.clean .strip{display:none}@media (max-width:640px){.strip{left:8px;right:8px;max-width:none}}`; document.head.append(css);
document.body.insertAdjacentHTML('beforeend', `<div class="strip"><span class="tau" id="tau">t 0.00</span><button id="s_play">${CLOCK.playing ? 'Pause' : 'Play'}</button><label>Speed <input id="s_speed" type="range" min="0.2" max="3" step="0.1" value="1"></label><button id="s_reset">Restart from rest</button><button id="s_back" aria-pressed="true">Sea pushes back: yes</button></div>`);
const $ = id => document.getElementById(id);
function strip(){ $('tau').textContent = 't ' + fmt(CLOCK.t,2); }
$('s_play').addEventListener('click', () => { CLOCK.playing = !CLOCK.playing; $('s_play').textContent = CLOCK.playing ? 'Pause' : 'Play'; });
$('s_speed').addEventListener('input', e => CLOCK.speed = +e.target.value);
$('s_reset').addEventListener('click', () => build());
$('s_back').addEventListener('click', () => { P.seaBack = !P.seaBack; $('s_back').textContent = 'Sea pushes back: ' + (P.seaBack ? 'yes' : 'no'); build(); });
build();
window.__mm = { go:id => window.MIXER_API.show(id), level:l => { P.level = l; build(); }, run:t => { const n = Math.round(t/CLOCK.h); for(let k=0;k<n;k++) stepOnce(); refresh(); }, arr:() => ARR, play:b => { CLOCK.playing = b; }, rows:() => document.getElementById('read').innerText, get S(){ return S; } };
})();
