/* SCRIPT: balls_mixer_v2
   Balls in One Ball, Mixer v2 — Jeromie Beasley — 14 Nov 2026
   Four balls in one ball: the centre and its three neighbours, each one peel step away along its own axis,
   placed exactly as in Two Trees in One Ball (Definition 4.1). Between two balls: the face halfway. Two faces
   either cross (overlap) or stand apart (gap). Built on 3D Mixer Parts v1; every number is computed live. */
(function(){
"use strict";
const M = window.Mixer3D, T = M.T, PI = Math.PI, RB = 2.6;
const V3 = (x,y,z) => new T.Vector3(x,y,z);
const fmt = (x,n=4) => Number.isFinite(x) ? x.toFixed(n) : '—';
const AXN = ['I','J','K'], AXL = ['i','j','k'], AXC = [0xff8d7c, 0x63d3ff, 0xf2c14e], AXV = [[1,0.55,0.49],[0.39,0.83,1],[0.95,0.76,0.31]];
const UNIT = [[1,0,0],[0,1,0],[0,0,1]];
const LINE = 3 + 2*Math.SQRT2;

/* ---------- hyperboloid model: vectors (t, x, y, z), boosts as 4x4 ---------- */
const O4 = [1,0,0,0];
function boost(u, r){ const c = Math.cosh(r), s = Math.sinh(r), B = [[c, s*u[0], s*u[1], s*u[2]],[s*u[0],0,0,0],[s*u[1],0,0,0],[s*u[2],0,0,0]];
  for(let i=0;i<3;i++) for(let j=0;j<3;j++) B[i+1][j+1] = (i===j ? 1 : 0) + (c-1)*u[i]*u[j]; return B; }
const mm = (A,B) => A.map(r => [0,1,2,3].map(j => r[0]*B[0][j]+r[1]*B[1][j]+r[2]*B[2][j]+r[3]*B[3][j]));
const mv = (A,v) => A.map(r => r[0]*v[0]+r[1]*v[1]+r[2]*v[2]+r[3]*v[3]);
const I4 = () => [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]];
const mink = (p,q) => p[0]*q[0]-p[1]*q[1]-p[2]*q[2]-p[3]*q[3];
const hdist = (p,q) => Math.acosh(Math.max(1, mink(p,q)));
/* ball point; world axes: i -> x, k -> up (y), j -> toward the viewer (-z) */
const toBall = p => { const k = RB/(1+p[0]); return V3(p[1]*k, p[3]*k, -p[2]*k); };
const w3 = u => V3(u[0], u[2], -u[1]);
function geo(p, q, n){ const d = hdist(p,q), out = []; for(let j=0;j<=n;j++){ const t = j/n; if(d < 1e-9){ out.push(toBall(p)); continue; }
  const a = Math.sinh((1-t)*d)/Math.sinh(d), b = Math.sinh(t*d)/Math.sinh(d); out.push(toBall([a*p[0]+b*q[0],a*p[1]+b*q[1],a*p[2]+b*q[2],a*p[3]+b*q[3]])); } return out; }

/* ---------- the face halfway to a neighbour: a spherical cap in the ball ---------- */
function faceGeom(u, h){ const rho = Math.tanh(h/2), c = (1+rho*rho)/(2*rho), R = (1-rho*rho)/(2*rho), tmax = Math.atan(1/R);
  const a = w3(u).normalize(), e1 = (Math.abs(a.y) < 0.9 ? V3(0,1,0) : V3(1,0,0)).cross(a).normalize(), e2 = a.clone().cross(e1);
  const NT = 14, NP = 40, pos = [], idx = [];
  for(let i=0;i<=NT;i++){ const th = tmax*i/NT; for(let j=0;j<=NP;j++){ const ph = 2*PI*j/NP;
    const p = a.clone().multiplyScalar(c - R*Math.cos(th)).addScaledVector(e1, R*Math.sin(th)*Math.cos(ph)).addScaledVector(e2, R*Math.sin(th)*Math.sin(ph)).multiplyScalar(RB); pos.push(p.x,p.y,p.z); } }
  for(let i=0;i<NT;i++) for(let j=0;j<NP;j++){ const k = i*(NP+1)+j; idx.push(k, k+1, k+NP+1, k+1, k+NP+2, k+NP+1); }
  const g = new T.BufferGeometry(); g.setAttribute('position', new T.Float32BufferAttribute(pos,3)); g.setIndex(idx); g.computeVertexNormals();
  const edge = []; for(let j=0;j<=NP;j++){ const k = NT*(NP+1)+j; edge.push(V3(pos[3*k],pos[3*k+1],pos[3*k+2])); }
  return { g, edge, centre: a.clone().multiplyScalar(c), R }; }
function face(group, u, h, col, op){ const f = faceGeom(u,h);
  group.add(new T.Mesh(f.g, new T.MeshBasicMaterial({color:col, transparent:true, opacity:op, side:T.DoubleSide, depthWrite:false})));
  group.add(M.line(f.edge, col, 0.7)); return f; }
/* where two faces cross: the circle common to their two spheres, kept inside the ball */
function crossing(fa, fb){ const A = fa.centre, B = fb.centre, d = A.distanceTo(B), x = (d*d + fa.R*fa.R - fb.R*fb.R)/(2*d), rr = fa.R*fa.R - x*x; if(rr <= 0) return null;
  const n = B.clone().sub(A).normalize(), c0 = A.clone().addScaledVector(n, x), e1 = (Math.abs(n.y) < 0.9 ? V3(0,1,0) : V3(1,0,0)).cross(n).normalize(), e2 = n.clone().cross(e1), r = Math.sqrt(rr);
  const segs = []; let cur = []; for(let i=0;i<=240;i++){ const t = 2*PI*i/240, p = c0.clone().addScaledVector(e1, r*Math.cos(t)).addScaledVector(e2, r*Math.sin(t));
    if(p.lengthSq() <= 1.0001){ cur.push(p.multiplyScalar(RB)); } else if(cur.length){ segs.push(cur); cur = []; } } if(cur.length) segs.push(cur); return segs; }

/* ---------- the mathematics of the field ---------- */
const X = { dir:[1,1,1], pair:[0,1] };
function pairMath(S, a, b){
  const ha = S.r[a]/2, hb = S.r[b]/2, g = Math.sinh(ha)*Math.sinh(hb), over = g < 1;
  const sa = X.dir[a], sb = X.dir[b], ua = UNIT[a].map(v => v*sa), ub = UNIT[b].map(v => v*sb);
  const Ba = boost(ua, S.r[a]), Bb = boost(ub, S.r[b]), Bai = boost(ua.map(v => -v), S.r[a]), Bbi = boost(ub.map(v => -v), S.r[b]);
  const steps = [Ba, Bb, Bai, Bbi]; let C = I4(); const corners = [O4]; steps.forEach(B => { C = mm(C,B); corners.push(mv(C,O4)); });
  const tr = C[0][0]+C[1][1]+C[2][2]+C[3][3], half = (tr-2)/2; let phi = NaN, tau = NaN, p = null, sense = 0;
  if(half < 1 - 1e-9){ phi = Math.acos(Math.max(-1,half))*180/PI;
    const id = [0, a+1, b+1], Rw = id.map(i => id.map(j => C[i][j] - (i===j ? 1 : 0))), cr = (x,y) => [x[1]*y[2]-x[2]*y[1], x[2]*y[0]-x[0]*y[2], x[0]*y[1]-x[1]*y[0]];
    let q = cr(Rw[0],Rw[1]); if(Math.hypot(q[0],q[1],q[2]) < 1e-12) q = cr(Rw[0],Rw[2]);
    p = [0,0,0,0]; p[0] = q[0]; p[a+1] = q[1]; p[b+1] = q[2]; if(p[0] < 0) p = p.map(v => -v); const n2 = mink(p,p);
    if(n2 > 0){ p = p.map(v => v/Math.sqrt(n2)); const pf = toBall(p), P1 = toBall(mv(C,O4)), ax = w3(UNIT[a]).cross(w3(UNIT[b]));
      sense = Math.sign(pf.clone().negate().cross(P1.clone().sub(pf)).dot(ax)); } else p = null; }
  else tau = Math.acosh(Math.max(1,half));
  const Na = mv(boost(UNIT[a], S.r[a]), O4), Nb = mv(boost(UNIT[b], S.r[b]), O4);
  return { a, b, g, over, alpha: over ? Math.acos(g)*180/PI : NaN, delta: over ? NaN : Math.acosh(g), C, corners, phi, tau, p, sense, dAB: hdist(Na,Nb) };
}
const params = [];
AXN.forEach((n,i) => params.push({id:'z'+n, label:'Ball '+n+' (axis '+AXL[i]+'): step ratio z', min:1.5, max:13, step:0.01, value:[3,5,7][i]}));
params.push({id:'depth', label:'Tree drawn to depth', min:1, max:4, step:1, value:3});
params.push({id:'np', label:'Passes of the square shown', min:1, max:120, step:1, value:40});
params.push({id:'zq', label:'One step ratio z for every arm', min:1.5, max:9, step:0.0001, value:2.8900536382639637});
function build(P){ const z = AXN.map(n => P['z'+n]); return { z, r: z.map(Math.log), G: z.map(v => (v-1)/(v+1)), depth:P.depth, np:P.np, zq:P.zq }; }
const refresh = () => window.MIXER_API.set('depth', window.MIXER_API.P.depth);

/* ---------- drawing shared by the eyes ---------- */
function clear(g){ while(g.children.length){ const c = g.children[0]; g.remove(c); if(c.geometry) c.geometry.dispose(); if(c.children && c.children.length) clear(c); } }
function rim(g){ g.add(M.shell(RB, 0x63d3ff, 0.035)); for(let k=0;k<3;k++){ const p = []; for(let i=0;i<=128;i++){ const a = 2*PI*i/128, c = RB*Math.cos(a), s = RB*Math.sin(a); p.push(k===0 ? V3(c,0,s) : k===1 ? V3(c,s,0) : V3(0,c,s)); } g.add(M.line(p, 0x63d3ff, k===0 ? 0.5 : 0.18)); }
  const l = M.label('rim: the ground', '#63d3ff', 0.3); l.position.set(-RB*0.74, 0.12, RB*0.74); g.add(l); }
function tree(g, S){ const gens = [], inv = []; for(let a=0;a<3;a++){ gens.push(boost(UNIT[a], S.r[a]), boost(UNIT[a].map(v => -v), S.r[a])); }
  const pos = [], col = []; const cc = AXC.map(c => new T.Color(c));
  (function walk(Mt, p, last, d){ if(d === S.depth) return; for(let k=0;k<6;k++){ if(last >= 0 && (k^1) === last) continue; const M2 = mm(Mt, gens[k]), q = mv(M2, O4), gg = geo(p, q, 6), c = cc[k>>1], f = Math.pow(0.6, d);
      for(let j=0;j<6;j++){ pos.push(gg[j].x,gg[j].y,gg[j].z, gg[j+1].x,gg[j+1].y,gg[j+1].z); col.push(c.r*f,c.g*f,c.b*f, c.r*f,c.g*f,c.b*f); } walk(M2, q, k, d+1); } })(I4(), O4, -1, 0);
  const bg = new T.BufferGeometry(); bg.setAttribute('position', new T.Float32BufferAttribute(pos,3)); bg.setAttribute('color', new T.Float32BufferAttribute(col,3));
  const ls = new T.LineSegments(bg, new T.LineBasicMaterial({vertexColors:true, transparent:true, opacity:0.55})); ls.frustumCulled = false; g.add(ls); }
function balls(g, S, which){ const c = new T.Mesh(new T.SphereGeometry(0.11, 24, 16), new T.MeshStandardMaterial({color:0xffffff, emissive:0xffffff, emissiveIntensity:0.5})); g.add(c);
  const lo = M.label('O  centre', '#dfe7ef', 0.26); lo.position.set(0.05, -0.28, 0); g.add(lo);
  which.forEach(a => { const p = toBall(mv(boost(UNIT[a], S.r[a]), O4)), f = 1 - p.lengthSq()/(RB*RB);
    const b = new T.Mesh(new T.SphereGeometry(0.05 + 0.16*f, 24, 16), new T.MeshStandardMaterial({color:AXC[a], emissive:AXC[a], emissiveIntensity:0.45, roughness:0.4})); b.position.copy(p); g.add(b);
    const l = M.label(AXN[a] + '   z ' + fmt(S.z[a],2), '#' + AXC[a].toString(16).padStart(6,'0'), 0.28); l.position.copy(p).add(V3(0, 0.3, 0)); g.add(l); }); }
function flowMake(g){ const p = M.points(3*6, 0.11); g.add(p); return p; }
function flowStep(p, S, t, which){ let i = 0; for(let a=0;a<3;a++) for(let k=0;k<6;k++){ let ph = (t*0.25 + k/6) % 1; if(X.dir[a] < 0) ph = 1 - ph; const rr = RB*Math.tanh(ph*S.r[a]/2), f = which.includes(a) ? Math.sin(PI*ph)*0.9 + 0.1 : 0;
    M.setPt(p, i++, w3(UNIT[a]).multiplyScalar(rr), AXV[a].map(v => v*f)); } M.flush(p); }
function dirButtons(){ return `<div class="row">` + AXN.map((n,i) => `<button data-d="${i}">${n}: flow ${X.dir[i] > 0 ? 'out from the centre' : 'in from the rim'}</button>`).join('') + `</div>`; }
function bindDir(){ document.querySelectorAll('#ctl button[data-d]').forEach(bn => bn.addEventListener('click', () => { const i = +bn.dataset.d; X.dir[i] = -X.dir[i]; bn.textContent = AXN[i] + ': flow ' + (X.dir[i] > 0 ? 'out from the centre' : 'in from the rim'); refresh(); })); }
const kindRow = m => m.over ? ['faces of ' + AXN[m.a] + ' and ' + AXN[m.b], 'cross at ' + fmt(m.alpha,3) + '°'] : ['faces of ' + AXN[m.a] + ' and ' + AXN[m.b], 'apart by ' + fmt(m.delta,4)];
const senseText = m => m.sense > 0 ? 'counter-clockwise' : m.sense < 0 ? 'clockwise' : '';

/* ================= EYE 1: four balls in one ball ================= */
const eyeField = { id:'field', title:'Four balls in one ball', section:'Two Trees Def. 4.1; faces as in Thm 8.4', grade:'exact placement; computed live',
  eq:'ball at Γ = (z − 1)/(z + 1) along its axis, ln z from the centre\nface halfway, at ln z / 2\ntwo faces:  g = sinh(ln z₁/2) · sinh(ln z₂/2)\ng < 1 cross at arccos g      g > 1 apart by arccosh g',
  text:'One ball. The centre O and its three neighbours I, J, K are four balls of the same tree, each neighbour one peel step from the centre along its own axis. A different step ratio gives a different size of step, so the three neighbours sit at different depths. The coloured cap in front of each neighbour is the face halfway between it and the centre. Where two faces cross, the two neighbours overlap and the crossing is drawn white. Where they do not meet there is a gap between them. Points on each arm show the direction of flow, out from the centre or in from the rim. The faint lines are the tree itself, drawn along true shortest paths.',
  uses:['zI','zJ','zK','depth'], view:[0.62,0.36,8.2,0],
  extra: dirButtons, bind: bindDir,
  make(g){ this.s = new T.Group(); this.d = new T.Group(); g.add(this.s, this.d); rim(this.s); this.fl = flowMake(g); },
  enter(S){ clear(this.d); tree(this.d, S); balls(this.d, S, [0,1,2]); const F = [0,1,2].map(a => face(this.d, UNIT[a], S.r[a]/2, AXC[a], 0.16));
    this.m = [[0,1],[1,2],[0,2]].map(([a,b]) => { const m = pairMath(S,a,b); if(m.over){ const sg = crossing(F[a], F[b]); if(sg) sg.forEach(s => this.d.add(M.line(s, 0xffffff, 1))); } return m; }); },
  change(S){ this.enter(S); },
  step(dt, S, t){ flowStep(this.fl, S, t, [0,1,2]); const r = [];
    for(let a=0;a<3;a++) r.push([AXN[a] + ':  Γ,  ln z,  Γ² against 1/2', fmt(S.G[a],4) + ',  ' + fmt(S.r[a],4) + ',  ' + (S.G[a]*S.G[a] < 0.5 ? 'below' : 'above')]);
    this.m.forEach(m => { r.push(kindRow(m)); r.push(['distance ' + AXN[m.a] + ' to ' + AXN[m.b], fmt(m.dAB,4)]); }); return r; } };

/* ================= EYE 2: two neighbours, overlap or gap, and the square ================= */
const eyePair = { id:'pair', title:'Two neighbours: overlap or gap', section:'Two Trees Thm 5.3, 5.4, 8.4; BallJoins J4, J7', grade:'exact; computed live',
  eq:'square:  a, b, back a, back b\ng < 1:  a turn by 4·arccos g about a fixed point\ng > 1:  a run of length 4·arccosh g\nreverse a step or the order: the turn reverses',
  text:'Two of the neighbours and the faces in front of them. The gold path steps to one neighbour, then by the other step, then undoes each: on a flat sheet it would close, here it does not. When the faces cross, the square is a turn about the white point and repeating it carries the centre round a ring: the walk is held. When the faces stand apart, the square is a run and repeating it carries the centre out toward the rim: nothing returns. Changing the direction of flow on one arm leaves every size on this page the same and reverses the sense of the turn.',
  uses:['zI','zJ','zK','np'], view:[0.5,0.62,7.4,0],
  extra: () => `<div class="row"><button data-p="0,1">I and J</button><button data-p="1,2">J and K</button><button data-p="0,2">I and K</button></div>` + dirButtons(),
  bind(){ bindDir(); document.querySelectorAll('#ctl button[data-p]').forEach(bn => { const pr = bn.dataset.p.split(',').map(Number); bn.setAttribute('aria-pressed', pr[0]===X.pair[0] && pr[1]===X.pair[1]);
    bn.addEventListener('click', () => { X.pair = pr; document.querySelectorAll('#ctl button[data-p]').forEach(q => q.setAttribute('aria-pressed', q === bn)); refresh(); }); }); },
  make(g){ this.s = new T.Group(); this.d = new T.Group(); g.add(this.s, this.d); rim(this.s); this.fl = flowMake(g); this.mk = M.points(1, 0.3); g.add(this.mk); },
  enter(S){ clear(this.d); const [a,b] = X.pair, m = pairMath(S,a,b); this.m = m; balls(this.d, S, [a,b]);
    const Fa = face(this.d, UNIT[a], S.r[a]/2, AXC[a], 0.2), Fb = face(this.d, UNIT[b], S.r[b]/2, AXC[b], 0.2);
    if(m.over){ const sg = crossing(Fa, Fb); if(sg) sg.forEach(s => this.d.add(M.line(s, 0xffffff, 1))); }
    let path = []; for(let i=0;i<4;i++) path = path.concat(geo(m.corners[i], m.corners[i+1], 24)); this.d.add(M.line(path, 0xf2c14e, 1));
    this.d.add(M.line([path[path.length-1], V3(0,0,0)], 0xff6fae, 1));
    this.orb = [V3(0,0,0)]; let x = O4; for(let n=1;n<=S.np;n++){ x = mv(m.C, x); const s = Math.sqrt(Math.max(1e-300, mink(x,x))); x = x.map(v => v/s); if(!(x[0] < 1e7)) break; this.orb.push(toBall(x)); }
    const op = M.points(this.orb.length, 0.12); this.orb.forEach((p,i) => M.setPt(op, i, p, [0.85,0.85,0.85])); M.flush(op); this.d.add(op);
    this.far = 0; x = O4; for(let n=1;n<=S.np;n++){ x = mv(m.C, x); this.far = Math.max(this.far, Math.acosh(Math.max(1,x[0]))); if(!(x[0] < 1e7)) break; }
    if(m.p){ const fp = new T.Mesh(new T.SphereGeometry(0.07, 16, 12), new T.MeshBasicMaterial({color:0xffffff})); fp.position.copy(toBall(m.p)); this.d.add(fp); } },
  change(S){ this.enter(S); },
  step(dt, S, t){ flowStep(this.fl, S, t, X.pair); const m = this.m, i = Math.floor(t*3) % this.orb.length; M.setPt(this.mk, 0, this.orb[i], [1,0.76,0.3]); M.flush(this.mk);
    const r = [['g = sinh(ln z₁/2)·sinh(ln z₂/2)', fmt(m.g,6)], kindRow(m), ['distance between the two balls', fmt(m.dAB,4)]];
    if(m.p) r.push(['the square', 'turn'], ['turn per pass', fmt(m.phi,3) + '°, ' + senseText(m)], ['4·arccos g (same turn, either way round)', fmt(Math.min(4*Math.acos(Math.min(1,m.g))*180/PI, 360 - 4*Math.acos(Math.min(1,m.g))*180/PI),3) + '°'],
      ['fixed point, distance from the centre', fmt(Math.acosh(m.p[0]),4)], ['farthest the centre is carried', fmt(this.far,4) + '  (bound ' + fmt(2*Math.acosh(m.p[0]),4) + ')']);
    else r.push(['the square', 'run'], ['run per pass', fmt(m.tau,5)], ['4·arccosh g', fmt(4*Math.acosh(Math.max(1,m.g)),5)], ['farthest the centre is carried', fmt(this.far,3) + '  (no bound)']);
    r.push(['pass shown', String(i)]); return r; } };

/* ================= EYE 3: when the balls close into a lattice ================= */
const zOf = q => Math.pow(Math.sqrt(q) + Math.sqrt(1+q), 2);
const SPEC = [['5 round an edge', zOf(Math.cos(2*PI/5))], ['6 round an edge', 2+Math.sqrt(3)], ['8 round an edge', zOf(Math.cos(2*PI/8))], ['z = 3', 3], ['z = 5', 5], ['the line', LINE], ['z = 7', 7]];
const eyeClose = { id:'close', title:'When the balls close', section:'Six arms, one step ratio', grade:'computed to depth 5',
  eq:'q = (z − 1)²/(4z),  faces cross at α = arccos q\nballs round each edge = 360° / α\nclosing steps:  q = cos(360°/n)',
  text:'Here every arm has the same step. All the balls reached by words of up to five steps are drawn. At most step ratios new balls keep landing between old ones and the smallest distance between two balls keeps falling: the tree never settles. At the steps where a whole number of balls fit round each edge the balls land on each other and the smallest distance stays at one step, ln z: the tree has closed into a lattice. Past the line Γ² = 1/2 nothing lands on anything and every ball stays at least a gap away. The whole numbers 3 and 5 are not closing steps, and 7 is past the line.',
  uses:['zq'], view:[0.62,0.36,8.2,0],
  extra: () => `<div class="row">` + SPEC.map((s,i) => `<button data-q="${i}">${s[0]}</button>`).join('') + `</div>`,
  bind(){ document.querySelectorAll('#ctl button[data-q]').forEach(bn => bn.addEventListener('click', () => window.MIXER_API.set('zq', SPEC[+bn.dataset.q][1]))); },
  make(g){ this.s = new T.Group(); this.d = new T.Group(); g.add(this.s, this.d); rim(this.s); },
  enter(S){ clear(this.d); const z = S.zq, r = Math.log(z), q = (z-1)*(z-1)/(4*z), gens = []; for(let a=0;a<3;a++) gens.push(boost(UNIT[a], r), boost(UNIT[a].map(v => -v), r));
    const seen = new Map(), pts = [O4], seg = []; const key = p => { const k = 1/(1+p[0]); return Math.round(p[1]*k*1e6) + ',' + Math.round(p[2]*k*1e6) + ',' + Math.round(p[3]*k*1e6); }; seen.set(key(O4), 0);
    let front = [[I4(), O4, -1]], words = 1;
    for(let d=1; d<=5; d++){ const nx = []; for(const [Mt, p, last] of front) for(let k=0;k<6;k++){ if(last >= 0 && (k^1) === last) continue; const M2 = mm(Mt, gens[k]), qn = mv(M2, O4); words++;
        const gg = geo(p, qn, 3); for(let j=0;j<3;j++) seg.push(gg[j].x,gg[j].y,gg[j].z, gg[j+1].x,gg[j+1].y,gg[j+1].z);
        const kk = key(qn); if(!seen.has(kk)){ seen.set(kk, d); pts.push(qn); } nx.push([M2, qn, k]); } front = nx; }
    let ms = 1e9; for(let i=0;i<pts.length;i++) for(let j=i+1;j<pts.length;j++){ const ip = mink(pts[i],pts[j]); if(ip < ms) ms = ip; } ms = Math.acosh(Math.max(1,ms));
    const bg = new T.BufferGeometry(); bg.setAttribute('position', new T.Float32BufferAttribute(seg,3)); const ls = new T.LineSegments(bg, new T.LineBasicMaterial({color:0x8a9aab, transparent:true, opacity:0.22})); ls.frustumCulled = false; this.d.add(ls);
    const pp = M.points(pts.length, 0.075); pts.forEach((p,i) => M.setPt(pp, i, toBall(p), i === 0 ? [1,1,1] : [0.95,0.76,0.31])); M.flush(pp); this.d.add(pp);
    const over = q < 1 - 1e-9, alpha = over ? Math.acos(q)*180/PI : NaN, closed = ms > r - 1e-6 && pts.length < words;
    this.rows = [['Γ² of the step', fmt(Math.pow((z-1)/(z+1),2),6)], ['q', fmt(q,6)], over ? ['faces cross at α', fmt(alpha,4) + '°'] : ['gap between faces δ', fmt(Math.acosh(Math.max(1,q)),5)],
      ['balls round each edge, 360°/α', over ? fmt(360/alpha,4) : 'none (past the line)'], ['words of up to five steps', String(words)], ['distinct balls they reach', String(pts.length)],
      ['smallest distance between two balls', fmt(ms,5)], ['one step ln z', fmt(r,5)],
      ['state', closed ? 'closed: balls land on each other, spacing holds' : (ms < r - 1e-6 ? 'not settled: balls land between balls' : (over ? 'no ball closer than one step at this depth' : 'apart: every ball keeps its gap'))]]; },
  change(S){ this.enter(S); },
  step(){ return this.rows; } };

M.run({ title:'Balls in One Ball', byline:'JEROMIE BEASLEY · MIXER v2 · 14 NOV 2026 · AI-ASSISTED',
  note:'an explorer of checked formulas, not a test of them',
  feed:{ params, build }, eyes:[eyeField, eyePair, eyeClose], film:['field','pair','close'] });
})();
