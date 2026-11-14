/* SCRIPT: balls_mixer_v3
   Balls in One Ball, Mixer v3 (v2 eyes kept, four tree eyes added) — Jeromie Beasley — 14 Nov 2026
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
params.push({id:'zt', label:'Tree: one step ratio z for every arm', min:1.5, max:9, step:0.01, value:5});
params.push({id:'zl', label:'Equal step ratio z of the two arms', min:1.5, max:9, step:0.0001, value:5});
params.push({id:'nc', label:'Twin pairs drawn', min:2, max:2400, step:1, value:400});
params.push({id:'zq', label:'One step ratio z for every arm', min:1.5, max:9, step:0.0001, value:2.8900536382639637});
function build(P){ const z = AXN.map(n => P['z'+n]); return { z, r: z.map(Math.log), G: z.map(v => (v-1)/(v+1)), depth:P.depth, np:P.np, zq:P.zq, zt:P.zt, zl:P.zl, nc:P.nc }; }
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

/* ================= v3 additions: four tree eyes ================= */
X.stand = -1; X.ord = 0;
const col3 = h => [((h>>16)&255)/255, ((h>>8)&255)/255, (h&255)/255];
const gam = z => (z-1)/(z+1);
function gens6(r){ const g = []; for(let a=0;a<3;a++) g.push(boost(UNIT[a], r), boost(UNIT[a].map(v => -v), r)); return g; }
function lineShell(g){ g.add(M.shell(RB*Math.SQRT1_2, 0xf2c14e, 0.06)); const l = M.label('the line  Γ² = 1/2', '#f2c14e', 0.26); l.position.set(0, -RB*Math.SQRT1_2 - 0.14, 0); g.add(l); }
function segs(g, pos, col, op){ const bg = new T.BufferGeometry(); bg.setAttribute('position', new T.Float32BufferAttribute(pos,3)); bg.setAttribute('color', new T.Float32BufferAttribute(col,3));
  const ls = new T.LineSegments(bg, new T.LineBasicMaterial({vertexColors:true, transparent:true, opacity:op})); ls.frustumCulled = false; g.add(ls); }

/* ---- EYE 4: the tree, its level shells, and the same tree from every ball ---- */
const STAND = ['the centre O', 'the neighbour along i', 'the neighbour along j', 'the neighbour along k'];
const eyeTree = { id:'tree', title:'The tree and its level shells', section:'Two Trees v4: peel_ladder, gam_mul, free5, free7', grade:'placement exact; freeness in Lean at ratios 5 and 7 (not re-run here); numbers computed live',
  eq:'six arms at every ball, five onward\nlevel L straight out:  Γ_L = (z^L − 1)/(z^L + 1)\nballs to depth 4:  1 + 6 + 30 + 150 + 750 = 937',
  text:'Every ball of the tree carries the same six arms: the axes i, j, k and their reverses. All 937 balls reached in up to four steps are drawn, each edge along its true shortest path and coloured by its axis. The gold shells are the levels: L steps straight out along one arm reach the shell of radius Γ_L exactly. Balls reached by turning between arms fall inside their shell. Stand on a neighbour and the whole tree slides by one peel step: what is then seen from the new ball is the same tree that was seen from the centre.',
  uses:['zt'], view:[0.62,0.36,8.2,0],
  extra: () => `<div class="row">` + STAND.map((s,i) => `<button data-s="${i-1}">stand on ${s}</button>`).join('') + `</div>`,
  bind(){ document.querySelectorAll('#ctl button[data-s]').forEach(bn => { bn.setAttribute('aria-pressed', +bn.dataset.s === X.stand);
    bn.addEventListener('click', () => { X.stand = +bn.dataset.s; document.querySelectorAll('#ctl button[data-s]').forEach(q => q.setAttribute('aria-pressed', q === bn)); refresh(); }); }); },
  make(g){ this.s = new T.Group(); this.d = new T.Group(); g.add(this.s, this.d); rim(this.s); },
  enter(S){ clear(this.d); const z = S.zt, r = Math.log(z), gens = gens6(r), back = X.stand < 0 ? I4() : boost(UNIT[X.stand].map(v => -v), r);
    const nodes = [{p:O4, d:0}], pos = [], col = [], cc = AXC.map(col3);
    (function walk(Mt, p, last, d){ if(d === 4) return; for(let k=0;k<6;k++){ if(last >= 0 && (k^1) === last) continue; const M2 = mm(Mt, gens[k]), q = mv(M2, O4); nodes.push({p:q, d:d+1});
        const gg = geo(mv(back,p), mv(back,q), 5), c = cc[k>>1], f = Math.pow(0.62, d);
        for(let j=0;j<5;j++){ pos.push(gg[j].x,gg[j].y,gg[j].z, gg[j+1].x,gg[j+1].y,gg[j+1].z); col.push(c[0]*f,c[1]*f,c[2]*f, c[0]*f,c[1]*f,c[2]*f); } walk(M2, q, k, d+1); } })(I4(), O4, -1, 0);
    segs(this.d, pos, col, 0.7);
    const moved = nodes.map(n => mv(back, n.p)), pp = M.points(nodes.length, 0.07);
    moved.forEach((p,i) => { const f = 0.35 + 0.65*Math.pow(0.7, nodes[i].d); M.setPt(pp, i, toBall(p), [f,f,f]); }); M.flush(pp); this.d.add(pp);
    const GL = [1,2,3,4].map(L => gam(Math.pow(z,L))); GL.forEach((G,i) => { this.d.add(M.shell(RB*G, 0xf2c14e, 0.05)); const l = M.label('level ' + (i+1), '#f2c14e', 0.2); l.position.set(0, RB*G + 0.07, 0); this.d.add(l); });
    const here = new T.Mesh(new T.SphereGeometry(0.1, 20, 14), new T.MeshBasicMaterial({color:0xffffff})); this.d.add(here);
    let worst = 0, Mt = I4(); for(let L=1;L<=4;L++){ Mt = mm(Mt, gens[0]); const p = mv(Mt, O4); worst = Math.max(worst, Math.abs(p[1]/(1+p[0]) - GL[L-1])); }
    let ms = 1e300; for(let i=0;i<nodes.length;i++) for(let j=i+1;j<nodes.length;j++){ const ip = mink(nodes[i].p, nodes[j].p); if(ip < ms) ms = ip; } ms = Math.acosh(Math.max(1,ms));
    let same = 0; if(X.stand >= 0){ for(const n of nodes){ if(n.d > 3) continue; let best = 1e300; for(const q of moved){ const dd = Math.max(Math.abs(n.p[0]-q[0]), Math.abs(n.p[1]-q[1]), Math.abs(n.p[2]-q[2]), Math.abs(n.p[3]-q[3]))/n.p[0]; if(dd < best) best = dd; } same = Math.max(same, best); } }
    this.rows = [['Γ,  ln z,  Γ² against 1/2', fmt(gam(z),4) + ',  ' + fmt(r,4) + ',  ' + (gam(z)*gam(z) < 0.5 ? 'below' : 'above')],
      ['level shells Γ₁ … Γ₄', GL.map(v => fmt(v,4)).join(',  ')], ['straight arm against Γ_L, largest difference', worst.toExponential(1)],
      ['balls drawn (depth 0 to 4)', String(nodes.length)], ['smallest distance between two balls', fmt(ms,4)], ['that distance in steps of ln z', fmt(ms/r,4)],
      ['standing on', STAND[X.stand+1]],
      ['tree from here against tree from the centre', X.stand < 0 ? 'stand on a neighbour to compare' : 'same to depth 3, largest difference ' + same.toExponential(1)],
      ['no word returns (freeness)', Math.abs(z-5) < 1e-9 || Math.abs(z-7) < 1e-9 ? 'in Lean at this ratio' : 'Lean covers ratios 5 and 7; here computed to depth 4 only']]; },
  change(S){ this.enter(S); },
  step(){ return this.rows; } };

/* ---- EYE 5: one step then another: the frame turns (Thomas turn) ---- */
const gcd = (a,b) => b ? gcd(b, a % b) : Math.abs(a);
function arc(u, v, n){ const out = [], w = Math.acos(Math.max(-1, Math.min(1, u.dot(v)))); for(let i=0;i<=n;i++){ const t = i/n; if(w < 1e-9){ out.push(u.clone()); continue; }
  out.push(u.clone().multiplyScalar(Math.sin((1-t)*w)/Math.sin(w)).addScaledVector(v, Math.sin(t*w)/Math.sin(w))); } return out; }
const eyeThomas = { id:'thomas', title:'One step then another: the frame turns', section:'Two Trees v4 thomas5; BallJoins J5 (euclid_is_thomas, garrett_pair), J7 (reverse_turn)', grade:'exact; computed live from the step matrices',
  eq:'step along i, then along j\n= one straight step, and a turn θ of the frame\ntan(θ/2) = Γ₁ · Γ₂\nother order: the same turn, the other way',
  text:'Two steps along different arms do not add up to one straight step. The gold path goes to ball I and then on by the step of J. The pink line is the one straight step that reaches the same ball. What is left over is a turn of the frame: the dim axes are the frame carried by the straight step, the bright axes the frame carried by the two steps, and the white arc is the turn between them. The turn is read off the matrices and set beside the formula. With whole step ratios the turn is a whole-number right triangle: ratios 5 and 5 give 65, 72, 97. Taking the steps in the other order gives the same size of turn in the opposite sense.',
  uses:['zI','zJ'], view:[0.5,0.62,7.4,0],
  extra: () => `<div class="row"><button data-o="0">I then J</button><button data-o="1">J then I</button></div>`,
  bind(){ document.querySelectorAll('#ctl button[data-o]').forEach(bn => { bn.setAttribute('aria-pressed', +bn.dataset.o === X.ord);
    bn.addEventListener('click', () => { X.ord = +bn.dataset.o; document.querySelectorAll('#ctl button[data-o]').forEach(q => q.setAttribute('aria-pressed', q === bn)); refresh(); }); }); },
  make(g){ this.s = new T.Group(); this.d = new T.Group(); g.add(this.s, this.d); rim(this.s); },
  enter(S){ clear(this.d); const f = X.ord ? 1 : 0, s = 1 - f, B1 = boost(UNIT[f], S.r[f]), B2 = boost(UNIT[s], S.r[s]), A = mm(B1, B2), p1 = mv(B1, O4), p = mv(A, O4);
    const rap = Math.acosh(p[0]), n = [p[1],p[2],p[3]].map(v => v/Math.sinh(rap)), R = mm(boost(n.map(v => -v), rap), A);
    const th = Math.acos(Math.max(-1, Math.min(1, (R[1][1]+R[2][2]+R[3][3]-1)/2))), ak = (R[2][1]-R[1][2])/(2*Math.sin(th));
    balls(this.d, S, [0,1]);
    this.d.add(M.line(geo(O4, p1, 24).concat(geo(p1, p, 24)), 0xf2c14e, 1)); this.d.add(M.line(geo(O4, p, 32), 0xff6fae, 1));
    const e = new T.Mesh(new T.SphereGeometry(0.08, 20, 14), new T.MeshBasicMaterial({color:0xffffff})); e.position.copy(toBall(p)); this.d.add(e);
    const L = 1.15; for(let a=0;a<3;a++){ const u = w3(UNIT[a]), v = w3([R[1][a+1], R[2][a+1], R[3][a+1]]);
      this.d.add(M.line([V3(0,0,0), u.clone().multiplyScalar(L)], AXC[a], 0.3)); this.d.add(M.line([V3(0,0,0), v.clone().multiplyScalar(L)], AXC[a], 1));
      if(a < 2) this.d.add(M.line(arc(u, v, 24).map(q => q.multiplyScalar(L*(0.8 + 0.12*a))), 0xffffff, 0.95)); }
    const G1 = S.G[0], G2 = S.G[1], form = 2*Math.atan(G1*G2), z1 = S.z[0], z2 = S.z[1], whole = Math.abs(z1-Math.round(z1)) < 1e-9 && Math.abs(z2-Math.round(z2)) < 1e-9;
    let tri = 'whole step ratios give a whole triangle';
    if(whole){ let a = (Math.round(z1)+1)*(Math.round(z2)+1), b = (Math.round(z1)-1)*(Math.round(z2)-1); const k = gcd(a,b); a /= k; b /= k; let t = [a*a-b*b, 2*a*b, a*a+b*b]; const k2 = gcd(gcd(t[0],t[1]),t[2]); t = t.map(v => v/k2);
      tri = t.join(',  ') + '   (cos θ = ' + t[0] + '/' + t[2] + ' against ' + fmt(Math.cos(th),6) + ')'; }
    this.rows = [['order', X.ord ? 'J then I' : 'I then J'], ['Γ₁,  Γ₂', fmt(G1,4) + ',  ' + fmt(G2,4)], ['turn of the frame, from the matrices', fmt(th*180/PI,4) + '°'], ['2·arctan(Γ₁Γ₂)', fmt(form*180/PI,4) + '°'],
      ['difference', Math.abs(th-form).toExponential(1)], ['sense about the third axis', ak > 0 ? 'counter-clockwise' : 'clockwise'], ['the triangle of the turn', tri],
      ['two steps, ln z₁ + ln z₂', fmt(S.r[0]+S.r[1],4)], ['the one straight step that reaches the same ball', fmt(rap,4)]]; },
  change(S){ this.enter(S); },
  step(){ return this.rows; } };

/* ---- EYE 6: across the line: the turn becomes a run ---- */
const LSPEC = [['z = 3', 3], ['z = 5', 5], ['z = 5.5', 5.5], ['the line', LINE], ['z = 6', 6], ['z = 7', 7]];
const eyeLine = { id:'line', title:'Across the line: the turn becomes a run', section:'Two Trees Thm 5.3, 5.4; BallJoins J3 (line_ratio, five_inside_seven_outside)', grade:'exact; computed live from the step matrices',
  eq:'equal steps:  g = (z − 1)²/(4z)\nbelow the line: turn 4·arccos g about a fixed point\nfixed point at ρ:  tanh²(ρ/2) = (1 − s)/(1 + s),  s = √(1 − 2Γ²)\non the line Γ² = 1/2 the fixed point reaches the rim',
  text:'Both arms take the same step. Below the line the square of four steps is a turn about the white point, and repeating it carries the centre round a ring through the centre: the walk is held. Raise the step and the white point moves outward and the ring grows. On the line, at z = 3 + 2√2, the white point reaches the rim: the ring opens. Past the line the square is a run and each pass carries the centre further toward the rim. Ratio 5 sits inside the line and ratio 7 outside it. The return counts say after how many passes the centre comes back to within a set distance of where it started.',
  uses:['zl','np'], view:[0.5,0.62,7.4,0],
  extra: () => `<div class="row">` + LSPEC.map((s,i) => `<button data-l="${i}">${s[0]}</button>`).join('') + `</div>`,
  bind(){ document.querySelectorAll('#ctl button[data-l]').forEach(bn => bn.addEventListener('click', () => window.MIXER_API.set('zl', LSPEC[+bn.dataset.l][1]))); },
  make(g){ this.s = new T.Group(); this.d = new T.Group(); g.add(this.s, this.d); rim(this.s); lineShell(this.s); this.mk = M.points(1, 0.3); g.add(this.mk); },
  enter(S){ clear(this.d); const z = S.zl, r = Math.log(z), S2 = { z:[z,z,z], r:[r,r,r], G:[gam(z),gam(z),gam(z)] }, keep = X.dir; X.dir = [1,1,1]; const m = pairMath(S2, 0, 1); X.dir = keep; this.m = m;
    balls(this.d, S2, [0,1]); const Fa = face(this.d, UNIT[0], r/2, AXC[0], 0.16), Fb = face(this.d, UNIT[1], r/2, AXC[1], 0.16);
    if(m.over){ const sg = crossing(Fa, Fb); if(sg) sg.forEach(s => this.d.add(M.line(s, 0xffffff, 0.8))); }
    let path = []; for(let i=0;i<4;i++) path = path.concat(geo(m.corners[i], m.corners[i+1], 24)); this.d.add(M.line(path, 0xf2c14e, 1));
    this.orb = [V3(0,0,0)]; let x = O4; for(let n=1;n<=S.np;n++){ x = mv(m.C, x); const s = Math.sqrt(Math.max(1e-300, mink(x,x))); x = x.map(v => v/s); if(!(x[0] < 1e7)) break; this.orb.push(toBall(x)); }
    const op = M.points(this.orb.length, 0.12); this.orb.forEach((p,i) => M.setPt(op, i, p, [0.85,0.85,0.85])); M.flush(op); this.d.add(op);
    const G2 = gam(z)*gam(z), rows = [['Γ² of the step against 1/2', fmt(G2,6) + (G2 < 0.5 - 1e-9 ? '  below' : G2 > 0.5 + 1e-9 ? '  above' : '  on the line')], ['g', fmt(m.g,6)]];
    if(m.p){ const fp = new T.Mesh(new T.SphereGeometry(0.07, 16, 12), new T.MeshBasicMaterial({color:0xffffff})); fp.position.copy(toBall(m.p)); this.d.add(fp);
      const rho = Math.acosh(m.p[0]), s = Math.sqrt(Math.max(0, 1-2*G2)), rf = 2*Math.atanh(Math.sqrt((1-s)/(1+s)));
      const got = {}; x = O4; for(let n=1;n<=8000;n++){ x = mv(m.C, x); const s2 = Math.sqrt(Math.max(1e-300, mink(x,x))); x = x.map(v => v/s2); const d = Math.acosh(Math.max(1,x[0])); if(!got.a && d < 0.1) got.a = n; if(!got.b && d < 0.01){ got.b = n; break; } }
      rows.push(['the square', 'turn'], ['turn per pass, from the matrices', fmt(m.phi,4) + '°'], ['4·arccos g (same turn, either way round)', fmt(Math.min(4*Math.acos(m.g)*180/PI, 360-4*Math.acos(m.g)*180/PI),4) + '°'],
        ['fixed point, distance ρ from the centre', fmt(rho,5)], ['ρ from the formula', fmt(rf,5)], ['fixed point, radius in the ball (rim = 1)', fmt(Math.tanh(rho/2),5)],
        ['the centre is held within 2ρ', fmt(2*rho,4)], ['back within 0.1 after', got.a ? got.a + ' passes' : 'more than 8000 passes'], ['back within 0.01 after', got.b ? got.b + ' passes' : 'more than 8000 passes']); }
    else rows.push(['the square', m.g > 1 + 1e-9 ? 'run' : 'on the line: neither turn nor run'], ['run per pass, from the matrices', fmt(m.tau,5)], ['4·arccosh g', fmt(4*Math.acosh(Math.max(1,m.g)),5)],
        ['fixed point', 'none inside the ball'], ['gap between the two faces', fmt(Math.acosh(Math.max(1,m.g)),5)], ['the centre returns', 'never: each pass carries it further']);
    this.rows = rows; },
  change(S){ this.enter(S); },
  step(dt, S, t){ const i = Math.floor(t*3) % this.orb.length; M.setPt(this.mk, 0, this.orb[i], [1,0.76,0.3]); M.flush(this.mk); return this.rows.concat([['pass shown', String(i)]]); } };

/* ---- EYE 7: the twin-prime chain as one path in the tree ---- */
const TWN = (function(){ const N = 400000, sv = new Uint8Array(N+3).fill(1); sv[0] = sv[1] = 0; for(let i=2;i*i<=N+2;i++) if(sv[i]) for(let j=i*i;j<N+3;j+=i) sv[j] = 0;
  const tw = []; for(let a=11;a<N;a++) if(sv[a] && sv[a+2]) tw.push(a); return tw; })();
const AXOF = a => ({1:0, 7:1, 9:2})[a % 10];
const CHN = (function(){ const n = 2400, pts = [], d = [], len = [], arm = []; let G = I4();
  for(let j=0;j<n;j++){ const p = mv(G, O4), s = Math.sqrt(mink(p,p)), q = p.map(v => v/s); pts.push(q); d.push(Math.acosh(Math.max(1,q[0]))); len.push(Math.log(TWN[j]/TWN[0])); arm.push(j ? AXOF(TWN[j]) : -1);
    G = mm(G, boost(UNIT[AXOF(TWN[j+1])], Math.log(TWN[j+1]/TWN[j]))); } return { n, pts, d, len, arm }; })();
const eyeChain = { id:'chain', title:'The twin-prime chain as one path in the tree', section:'BallJoins J6 (twin_start_digit); Two Trees v4 gam_mul; One Tree, One Ball', grade:'end-digit rule in Lean; the path computed live from exact steps',
  eq:'twin pair (a, a + 2), a > 5:  a ends in 1, 7 or 9\nend digit 1, 7, 9  →  arm i, j, k\nstep to the next pair: ratio a′/a along its arm\npath length = ln(a/11)',
  text:'Each twin pair is a ball. The step from one pair to the next is a peel step of its true size, the ratio of the two starting numbers, taken along the arm of the next pair’s end digit. Ratios multiply and lengths add, so the length of the path walked is exactly the logarithm of the starting number over 11. The path keeps changing arm, so it ends closer to the centre than the length it has walked; the readout gives both. The faint tree and the gold shells are the tree of ratio 5 and its levels, for scale. The chain starts at the pair 11, 13 at the centre.',
  uses:['nc'], view:[0.62,0.36,8.2,0],
  make(g){ this.s = new T.Group(); this.d = new T.Group(); g.add(this.s, this.d); rim(this.s); const r5 = Math.log(5); tree(this.s, { r:[r5,r5,r5], depth:3 });
    [1,2,3].forEach(L => this.s.add(M.shell(RB*gam(Math.pow(5,L)), 0xf2c14e, 0.045))); },
  enter(S){ clear(this.d); const n = Math.max(2, Math.min(CHN.n, Math.round(S.nc))), pos = [], col = [], cc = AXC.map(col3), cnt = [0,0,0];
    for(let j=1;j<n;j++){ const gg = geo(CHN.pts[j-1], CHN.pts[j], 3), c = cc[CHN.arm[j]]; cnt[CHN.arm[j]]++; for(let k=0;k<3;k++){ pos.push(gg[k].x,gg[k].y,gg[k].z, gg[k+1].x,gg[k+1].y,gg[k+1].z); col.push(c[0],c[1],c[2], c[0],c[1],c[2]); } }
    segs(this.d, pos, col, 1);
    const pp = M.points(n, 0.06); for(let j=0;j<n;j++) M.setPt(pp, j, toBall(CHN.pts[j]), j === 0 ? [1,1,1] : cc[CHN.arm[j]]); M.flush(pp); this.d.add(pp);
    const e = new T.Mesh(new T.SphereGeometry(0.06, 16, 12), new T.MeshBasicMaterial({color:0xffffff})); e.position.copy(toBall(CHN.pts[n-1])); this.d.add(e);
    const a = TWN[n-1], len = CHN.len[n-1], d = CHN.d[n-1];
    this.rows = [['twin pairs drawn', String(n)], ['latest pair', a + ',  ' + (a+2)], ['its end digit → arm', (a % 10) + ' → ' + AXL[AXOF(a)]], ['path length ln(a/11)', fmt(len,4)],
      ['distance from the centre ball', fmt(d,4)], ['distance / path length', fmt(d/len,4)], ['level of the ratio-5 tree reached', fmt(d/Math.log(5),2)],
      ['steps taken along i,  j,  k', cnt.join(',  ')], ['twin starts from 11 below 400000', String(TWN.length)]]; },
  change(S){ this.enter(S); },
  step(){ return this.rows; } };

M.run({ title:'Balls in One Ball', byline:'JEROMIE BEASLEY · MIXER v3 · 14 NOV 2026 · AI-ASSISTED',
  note:'an explorer of checked formulas, not a test of them',
  feed:{ params, build }, eyes:[eyeField, eyePair, eyeClose, eyeTree, eyeThomas, eyeLine, eyeChain], film:['field','pair','close','tree','thomas','line','chain'] });
})();
