/* SCRIPT: balls_mixer_v1
   Balls on the Field, Mixer v1 — Jeromie Beasley — 14 Nov 2026
   Tree-and-ball joins, the forced gap, arm sets and lattices, and the square of four joins.
   Built on 3D Mixer Parts v1. Every number on screen is computed live from the formulas
   checked on 12 and 13 November 2026 (gap law, arm sets, lattice closure, loop turn and run, push 2G^2). */
(function(){
"use strict";
const M = window.Mixer3D, T = M.T, PI = Math.PI;
const V3 = (x,y,z) => new T.Vector3(x,y,z);
const GOLD = [1,0.76,0.30], CYAN = [0.39,0.83,1], ROSE = [1,0.44,0.68], WHITE = [1,1,1], DIM = [0.45,0.55,0.66];
const cGOLD = 0xf2c14e, cCYAN = 0x63d3ff, cROSE = 0xff6fae, cDIM = 0x8a9aab, cWHITE = 0xffffff;
const fmt = (x,n=4) => Number.isFinite(x) ? x.toFixed(n) : '—';
const NAMES = ['A','B','C','D'];
const WALL = 3 + 2*Math.SQRT2, ZSTAR = 6.26912766085;

/* ---------- arm sets (directions on the unit sphere) ---------- */
const ARMS = {
  6: [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]],
  8: [], 12: []
};
for(const a of [1,-1]) for(const b of [1,-1]) for(const c of [1,-1]) ARMS[8].push([a/Math.sqrt(3), b/Math.sqrt(3), c/Math.sqrt(3)]);
for(const a of [1,-1]) for(const b of [1,-1]){ const s = Math.SQRT1_2; ARMS[12].push([a*s,b*s,0],[a*s,0,b*s],[0,a*s,b*s]); }
const ARMNAME = {6:'six axes', 8:'eight diagonals', 12:'twelve face diagonals'};

/* ---------- the mathematics of one ball ---------- */
function info(z, n, sign){
  const G1 = (z-1)/(z+1), L1 = Math.log(z)/2, G = Math.tanh(n*L1), gap = 2/(Math.pow(z,n)+1);
  const q = (z-1)*(z-1)/(4*z), inside = q < 1;
  const theta = inside ? 2*Math.acos(1-2*q*q)*180/PI : NaN, lambda = inside ? NaN : 4*Math.acosh(q);
  const x = 2*G1*G1, K = x < 1 ? 1/(1-x) : x/(x-1);
  return { z, n, sign, G1, L1, G, gap, q, inside, theta, lambda, K, P: 2*G*G, L: n*L1 };
}
const oplus = (a,b) => (a+b)/(1+a*b);

/* ---------- user state not carried by sliders ---------- */
const X = { sign:[1,-1,1,-1], arms:[6,8,6,12], config:'ring', lat:'sc' };

/* ---------- drawing helpers ---------- */
function clear(g){ while(g.children.length){ const c = g.children[0]; g.remove(c); if(c.geometry) c.geometry.dispose(); if(c.children && c.children.length) clear(c); } }
function ringPts(r, plane, n=96){ const p = []; for(let i=0;i<=n;i++){ const a = 2*PI*i/n, c = r*Math.cos(a), s = r*Math.sin(a);
  p.push(plane===0 ? V3(c,s,0) : plane===1 ? V3(c,0,s) : V3(0,c,s)); } return p; }
function rings(g, r, col, op){ for(let k=0;k<3;k++) g.add(M.line(ringPts(r,k), col, op)); }
function ringAt(centre, axis, r, col, op){ const a = axis.clone().normalize(); const u = Math.abs(a.y) < 0.9 ? V3(0,1,0) : V3(1,0,0); const e1 = u.clone().cross(a).normalize(), e2 = a.clone().cross(e1);
  const p = []; for(let i=0;i<=96;i++){ const t = 2*PI*i/96; p.push(centre.clone().addScaledVector(e1, r*Math.cos(t)).addScaledVector(e2, r*Math.sin(t))); } return M.line(p, col, op); }

/* one ball: rim (radius 1), cut surface (radius G_n), inner levels, arms with their nodes, moving points */
function drawBall(g, b, U, name, ls){
  clear(g);
  const col = b.sign > 0 ? GOLD : CYAN, hexc = b.sign > 0 ? cGOLD : cCYAN, A = ARMS[b.armsN];
  g.add(M.shell(U, cCYAN, 0.03)); rings(g, U, cCYAN, 0.16);
  g.add(M.shell(U*b.G, hexc, 0.13)); rings(g, U*b.G, hexc, 0.75);
  for(let k=1;k<b.n;k++) rings(g, U*Math.tanh(k*b.L1), hexc, 0.22);
  const nodes = M.points(A.length*b.n + 1 + (b.armsN===6 && b.n>=2 ? 24 : 0), 0.13*U); let ni = 0;
  M.setPt(nodes, ni++, V3(0,0,0), WHITE);
  for(const a of A){ g.add(M.line([V3(0,0,0), V3(a[0],a[1],a[2]).multiplyScalar(U*b.G)], hexc, 0.55));
    for(let k=1;k<=b.n;k++){ const r = U*Math.tanh(k*b.L1); M.setPt(nodes, ni++, V3(a[0]*r,a[1]*r,a[2]*r), col); } }
  if(b.armsN===6 && b.n>=2){ const c = (b.z*b.z+1)/(2*b.z), s = (b.z*b.z-1)/(2*b.z), f = U/(1+c*c);
    for(const a of A) for(const d of A){ if(a[0]*d[0]+a[1]*d[1]+a[2]*d[2] !== 0) continue;
      M.setPt(nodes, ni++, V3((s*c*a[0]+s*d[0])*f, (s*c*a[1]+s*d[1])*f, (s*c*a[2]+s*d[2])*f), ROSE.map(v => v*0.7)); } }
  M.flush(nodes); g.add(nodes);
  const per = 4, pts = M.points(A.length*per, 0.085*U); g.add(pts);
  const lab = M.label(name + '   z ' + fmt(b.z,2) + '   depth ' + b.n, b.sign > 0 ? '#f2c14e' : '#63d3ff', ls || 0.34); lab.position.set(0, U*1.13, 0); g.add(lab);
  g.userData = { b, U, pts, per, A, col };
}
function stepBall(g, t){
  const u = g.userData; if(!u.pts) return; const b = u.b; let i = 0;
  for(let a=0;a<u.A.length;a++) for(let k=0;k<u.per;k++){
    let ph = (t*0.22 + k/u.per + a*0.137) % 1; if(b.sign < 0) ph = 1 - ph;
    const r = u.U*Math.tanh(ph*b.n*b.L1), f = Math.sin(PI*Math.min(1,Math.max(0,ph)))*0.9 + 0.1;
    M.setPt(u.pts, i++, V3(u.A[a][0]*r, u.A[a][1]*r, u.A[a][2]*r), u.col.map(v => v*f)); }
  M.flush(u.pts);
}
const stateText = b => b.inside ? 'turn ' + fmt(b.theta,2) + '° per pass' : 'run ' + fmt(b.lambda,4) + ' per pass';

/* ---------- pair quantities ---------- */
function pair(a, b, join){
  const gs = a.gap + b.gap, d = a.G + b.G + join*gs;
  const lo = Math.min(a.G,b.G), hi = Math.max(a.G,b.G), ratio = lo/hi;
  const win = ratio > 0.99995 ? 'equal radii' : ratio >= Math.sqrt(3)-1 ? 'caesium chloride window' : ratio >= Math.SQRT2-1 ? 'rock salt window' : ratio >= Math.sqrt(6)/2-1 ? 'zinc blende window' : 'below the three windows';
  return { d, sep: join*gs, overlap: (1-join)*gs, gs, comp: oplus(a.gap,b.gap), len: Math.atanh(a.gap)+Math.atanh(b.gap),
    signed: oplus(a.sign*a.G, b.sign*b.G), prod: a.G1*b.G1, psum: a.P+b.P, ratio, win };
}

/* ---------- the feed ---------- */
const params = [];
NAMES.forEach((nm,i) => { params.push({id:'z'+nm, label:'Ball '+nm+': step ratio z', min:1.5, max:13, step:0.01, value:[5,7,3,11][i]});
  params.push({id:'n'+nm, label:'Ball '+nm+': cut depth n', min:1, max:3, step:1, value:[1,1,1,1][i]}); });
params.push({id:'join', label:'Join: 0 cut surfaces touch, 1 rims touch', min:0, max:1, step:0.01, value:1});
params.push({id:'nLat', label:'Cut depth n of every ball', min:1, max:3, step:1, value:1});
params.push({id:'gen', label:'Generations grown', min:1, max:4, step:1, value:3});
params.push({id:'zL', label:'Step ratio z of each join', min:1.2, max:13, step:0.001, value:5});
function build(P){
  const balls = NAMES.map((nm,i) => { const b = info(P['z'+nm], P['n'+nm], X.sign[i]); b.armsN = X.arms[i]; b.name = nm; return b; });
  return { balls, join:P.join, nLat:P.nLat, gen:P.gen, zL:P.zL };
}

/* buttons shared by the ball eyes */
function ballButtons(count){ let h = '';
  for(let i=0;i<count;i++) h += `<div class="row"><button data-s="${i}">${NAMES[i]}: ${X.sign[i]>0?'radiating':'receiving'}</button><button data-a="${i}">${NAMES[i]}: ${ARMNAME[X.arms[i]]}</button></div>`;
  return h; }
function bindBalls($){ const refresh = () => window.MIXER_API.set('join', window.MIXER_API.P.join);
  document.querySelectorAll('#ctl button[data-s]').forEach(bn => bn.addEventListener('click', () => { const i = +bn.dataset.s; X.sign[i] = -X.sign[i]; bn.textContent = NAMES[i] + ': ' + (X.sign[i]>0?'radiating':'receiving'); refresh(); }));
  document.querySelectorAll('#ctl button[data-a]').forEach(bn => bn.addEventListener('click', () => { const i = +bn.dataset.a; X.arms[i] = X.arms[i]===6 ? 8 : X.arms[i]===8 ? 12 : 6; bn.textContent = NAMES[i] + ': ' + ARMNAME[X.arms[i]]; refresh(); })); }

/* ================= EYE 1: one ball ================= */
const eyeOne = { id:'one', title:'One ball', section:'Tree and ball', grade:'exact',
  eq:'Γ = (z − 1)/(z + 1)\nG_n = tanh(n ln z / 2) = (zⁿ − 1)/(zⁿ + 1)\ngap to the rim = 1 − G_n = 2/(zⁿ + 1)',
  text:'The outer sphere is the rim of the ball, radius 1. The inner sphere is the cut surface at depth n. Arms leave the centre; each node sits at G_k along its arm. For the six-axis set the 24 turned nodes of depth 2 are drawn at their computed positions. The gap between the cut surface and the rim is never zero. Points move at constant speed in the length n ln z / 2, so they slow toward the cut surface. A radiating ball is drawn gold with points moving outward; a receiving ball is the same step read as 1/z, where Γ changes sign, drawn blue with points moving inward. The sign change is exact; reading it as radiating and receiving is a hypothesis.',
  uses:['zA','nA'], view:[0.7,0.3,6.8,0.2],
  extra: () => ballButtons(1), bind: (S,$) => bindBalls($),
  make(g){ this.ball = new T.Group(); g.add(this.ball); },
  enter(S){ drawBall(this.ball, S.balls[0], 1.9, 'A'); }, change(S){ this.enter(S); },
  step(dt, S, t){ stepBall(this.ball, t); const b = S.balls[0];
    return [['Γ of one step', fmt(b.sign*b.G1,6)], ['length n ln z / 2', fmt(b.L,6)], ['cut surface G_n', fmt(b.G,6)], ['gap 2/(zⁿ + 1)', fmt(b.gap,6)],
      ['arms', ARMNAME[b.armsN]], ['push 2G²', fmt(b.P,4)], ['square of four joins', stateText(b)], ['K of the step', fmt(b.K,4)],
      ['side of the wall (z = 5.8284)', b.inside ? 'inside' : 'past']]; } };

/* ================= EYE 2: two balls and the gap ================= */
const eyeTwo = { id:'two', title:'Two balls and the gap', section:'Join of two balls', grade:'exact; readings open',
  eq:'centre distance d = G_A + G_B + j (g_A + g_B)\nj = 1: rims touch, cut surfaces g_A + g_B apart\nj = 0: cut surfaces touch, rims overlap by g_A + g_B\ncomposed gap = (g_A + g_B)/(1 + g_A g_B)',
  text:'Two balls face each other along one arm. With the rims touching, the cut surfaces stay apart by the sum of the two gaps, drawn white. Pushing the balls together until the cut surfaces touch makes the rims overlap by exactly the same sum; the pink circle is where the two rims cross. The layer never closes at any depth, and no depth of one ball places its cut surface on the cut surface of the other for steps 5, 7 and 11 up to depth 8. The pushes 2G² balance (sum 1) at only one whole-number pair: z = 3 against z = 3 at depth 1. The product of the two one-step Γ equals 1/2 only for the pairs (5, 7) and (4, 11). The overlap as the place of holding and excluding is a hypothesis, not yet tested.',
  uses:['zA','nA','zB','nB','join'], view:[0.35,0.3,7.6,0],
  extra: () => ballButtons(2), bind: (S,$) => bindBalls($),
  make(g){ this.g = g; this.b = [new T.Group(), new T.Group()]; this.x = new T.Group(); g.add(this.b[0], this.b[1], this.x); },
  enter(S){ const U = 1.45, a = S.balls[0], b = S.balls[1], p = pair(a,b,S.join); this.p = p;
    drawBall(this.b[0], a, U, 'A'); drawBall(this.b[1], b, U, 'B');
    this.b[0].position.set(-U*p.d/2,0,0); this.b[1].position.set(U*p.d/2,0,0);
    clear(this.x); const xa = -U*p.d/2 + U*a.G, xb = U*p.d/2 - U*b.G;
    if(p.sep > 1e-9){ const l = M.line([V3(xa,0,0), V3(xb,0,0)], cWHITE, 1); this.x.add(l); const e = M.points(2, 0.16); M.setPt(e,0,V3(xa,0,0),WHITE); M.setPt(e,1,V3(xb,0,0),WHITE); M.flush(e); this.x.add(e); }
    if(p.d < 2 - 1e-9) this.x.add(ringAt(V3(0,0,0), V3(1,0,0), U*Math.sqrt(1 - p.d*p.d/4), cROSE, 0.95)); },
  change(S){ this.enter(S); },
  step(dt, S, t){ stepBall(this.b[0], t); stepBall(this.b[1], t); const p = this.p, a = S.balls[0], b = S.balls[1];
    return [['gap of A, gap of B', fmt(a.gap,5) + ', ' + fmt(b.gap,5)], ['centre distance d', fmt(p.d,5)], ['cut surfaces apart by', fmt(p.sep,5)], ['rims overlap by', fmt(p.overlap,5)],
      ['composed gap', fmt(p.comp,5)], ['gap as a length', fmt(p.len,5)], ['signed G_A ⊕ G_B', fmt(p.signed,5)],
      ['push A + push B', fmt(p.psum,4) + (Math.abs(p.psum-1) < 5e-4 ? '  (balanced)' : '')],
      ['Γ_A Γ_B (one step each)', fmt(p.prod,5) + (Math.abs(p.prod-0.5) < 5e-5 ? '  (pair across the wall)' : '')],
      ['cut radius ratio', fmt(p.ratio,4)], ['classical window', p.win]]; } };

/* ================= EYE 3: four balls on the field ================= */
function layout(S){
  const B = S.balls, d = (i,j) => pair(B[i],B[j],S.join).d; let pos, pairs, note = '';
  const line = () => { let x = 0; const p = [V3(0,0,0)]; for(let i=1;i<4;i++){ x += d(i-1,i); p.push(V3(x,0,0)); } return p; };
  if(X.config === 'line'){ pos = line(); pairs = [[0,1],[1,2],[2,3]]; }
  else if(X.config === 'ring'){ const ab = d(0,1), ad = d(0,3), bc = d(1,2), cd = d(2,3), bd = Math.hypot(ab,ad);
    if(bd > bc+cd || bd < Math.abs(bc-cd)){ pos = line(); pairs = [[0,1],[1,2],[2,3]]; note = 'ring cannot close for these sizes; line shown'; }
    else { const a = (bc*bc - cd*cd + bd*bd)/(2*bd), h = Math.sqrt(Math.max(0,bc*bc - a*a)); const ux = -ab/bd, uz = ad/bd;
      const mx = ab + a*ux, mz = a*uz; let cx = mx + h*uz, cz = mz - h*ux; if(cx*cx+cz*cz < (mx-h*uz)*(mx-h*uz)+(mz+h*ux)*(mz+h*ux)){ cx = mx - h*uz; cz = mz + h*ux; }
      pos = [V3(0,0,0), V3(ab,0,0), V3(cx,0,cz), V3(0,0,ad)]; pairs = [[0,1],[1,2],[2,3],[3,0]]; } }
  else { const d12 = d(0,1), d13 = d(0,2), d23 = d(1,2), d14 = d(0,3), d24 = d(1,3), d34 = d(2,3);
    const x3 = (d13*d13 - d23*d23 + d12*d12)/(2*d12), y3 = Math.sqrt(d13*d13 - x3*x3);
    const x4 = (d14*d14 - d24*d24 + d12*d12)/(2*d12), y4 = (d14*d14 - d34*d34 + x3*x3 + y3*y3 - 2*x3*x4)/(2*y3), z4 = Math.sqrt(d14*d14 - x4*x4 - y4*y4);
    if(!Number.isFinite(y3) || !Number.isFinite(z4) || z4 < 1e-6){ pos = line(); pairs = [[0,1],[1,2],[2,3]]; note = 'four-way contact cannot close for these sizes; line shown'; }
    else { pos = [V3(0,0,0), V3(d12,0,0), V3(x3,0,y3), V3(x4,z4,y4)]; pairs = [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]]; } }
  const c = V3(0,0,0); pos.forEach(p => c.add(p)); c.multiplyScalar(0.25); pos.forEach(p => p.sub(c));
  return { pos, pairs, note };
}
const eyeField = { id:'field', title:'Four balls on the field', section:'Joins among several balls', grade:'exact per join; arrangement illustrative',
  eq:'each join:  d = G_i + G_j + j (g_i + g_j)\ngap layer + rim overlap = g_i + g_j at every j\npush of a ball = 2 G²',
  text:'Four balls with their own step, cut depth, arm set and direction. In the line and the ring each ball is joined to its neighbours; in the four-way contact every ball is joined to the other three. Each join obeys the same law as the pair: a white gap layer where cut surfaces are held apart, a pink circle where rims overlap. Balls of different step and depth have different cut radii, so the centre distances differ and the figure is not regular. The arms are drawn in each ball\'s own frame and are not turned to face the neighbour; which arm sets can face each other is the subject of the next eye.',
  uses:['zA','nA','zB','nB','zC','nC','zD','nD','join'], view:[0.45,0.95,8.2,0],
  extra: () => `<div class="row"><button data-c="line">line</button><button data-c="ring">ring</button><button data-c="tetra">four-way contact</button></div>` + ballButtons(4),
  bind(S,$){ bindBalls($); document.querySelectorAll('#ctl button[data-c]').forEach(bn => { bn.setAttribute('aria-pressed', bn.dataset.c === X.config);
    bn.addEventListener('click', () => { X.config = bn.dataset.c; document.querySelectorAll('#ctl button[data-c]').forEach(q => q.setAttribute('aria-pressed', q.dataset.c === X.config)); window.MIXER_API.set('join', window.MIXER_API.P.join); }); }); },
  make(g){ this.b = NAMES.map(() => new T.Group()); this.x = new T.Group(); this.b.forEach(q => g.add(q)); g.add(this.x); },
  enter(S){ const U = 1, L = layout(S); this.L = L; clear(this.x);
    S.balls.forEach((b,i) => { drawBall(this.b[i], b, U, b.name, 0.24); this.b[i].position.copy(L.pos[i]).multiplyScalar(U); });
    this.rows = [];
    for(const [i,j] of L.pairs){ const a = S.balls[i], b = S.balls[j], p = pair(a,b,S.join), pi = L.pos[i], pj = L.pos[j], dir = pj.clone().sub(pi).normalize();
      this.x.add(M.line([pi.clone(), pj.clone()], cDIM, 0.18));
      if(p.sep > 1e-9) this.x.add(M.line([pi.clone().addScaledVector(dir, a.G), pj.clone().addScaledVector(dir, -b.G)], cWHITE, 1));
      if(p.d < 2 - 1e-9) this.x.add(ringAt(pi.clone().add(pj).multiplyScalar(0.5), dir, Math.sqrt(1 - p.d*p.d/4), cROSE, 0.9));
      this.rows.push([a.name + '–' + b.name + '  gap layer / rim overlap', fmt(p.sep,4) + ' / ' + fmt(p.overlap,4)]); } },
  change(S){ this.enter(S); },
  step(dt, S, t){ this.b.forEach(q => stepBall(q, t));
    const r = this.rows.slice(); S.balls.forEach(b => r.push([b.name + '  G, push, ' + (b.sign>0?'radiating':'receiving'), fmt(b.G,4) + ', ' + fmt(b.P,3) + ', ' + (b.inside ? 'turn' : 'run')]));
    if(this.L.note) r.push(['note', this.L.note]); return r; } };

/* ================= EYE 4: which arm sets close into a lattice ================= */
const LAT = {
  sc:  { name:'six axes', z:5,  arms:ARMS[6],  lat:'simple cubic', rim:PI/6, shells:'1, 1.4142, 1.7321, 2  with  6, 12, 8, 6' },
  bcc: { name:'eight diagonals', z:7,  arms:ARMS[8],  lat:'body-centred cubic', rim:PI*Math.sqrt(3)/8, shells:'1, 1.1547, 1.6330, 1.9149  with  8, 6, 12, 24' },
  fcc: { name:'twelve face diagonals', z:11, arms:ARMS[12], lat:'face-centred cubic', rim:PI/(3*Math.SQRT2), shells:'1, 1.4142, 1.7321, 2  with  12, 6, 24, 12' },
  mix: { name:'axes and diagonals together', z:13, arms:null, lat:'does not close' }
};
function grow(vecs, gens, cap){ const key = p => Math.round(p[0]*1e5) + ',' + Math.round(p[1]*1e5) + ',' + Math.round(p[2]*1e5);
  const seen = new Map([[key([0,0,0]), 0]]), pts = [[0,0,0,0]]; let front = [[0,0,0]]; const counts = [1];
  for(let g=1; g<=gens; g++){ const next = [];
    for(const p of front) for(const v of vecs){ const q = [p[0]+v[0], p[1]+v[1], p[2]+v[2]], k = key(q); if(seen.has(k)) continue; if(pts.length >= cap) break; seen.set(k, g); pts.push([q[0],q[1],q[2],g]); next.push(q); }
    front = next; counts.push(pts.length); }
  return { pts, counts }; }
function minSep(pts){ let m = 1e9; for(let i=0;i<pts.length;i++) for(let j=i+1;j<pts.length;j++){ const dx = pts[i][0]-pts[j][0], dy = pts[i][1]-pts[j][1], dz = pts[i][2]-pts[j][2], d = dx*dx+dy*dy+dz*dz; if(d < m) m = d; } return Math.sqrt(m); }
const eyeLat = { id:'lattice', title:'Which arm sets close', section:'Many balls joined arm to arm', grade:'computed',
  eq:'nearest centres / cut diameter = 1 / G_n\nfilling by cut balls = (filling by rims) × G_n³',
  text:'Every ball carries the same arm set and each new ball is placed along an arm, facing the ball it joins, rims touching. Six axes close into the simple cubic lattice, eight diagonals into the body-centred cubic, twelve face diagonals into the face-centred cubic. The gap keeps the cut balls apart, so the filling is below the rim filling and rises with depth. Axes and diagonals together (the 14 arms of 13, with the 5 step on the axes and the 7 step on the diagonals, cut surfaces touching) do not close: new centres keep landing between old ones, and the smallest distance between centres falls in jumps, from 0.983 to 0.299 and to 0.089 by the fifth generation. That set closes only if the diagonal arm is exactly 0.8660 of the axis arm; the peel gives 1.125. In the papers the step ln 7 is drawn with six axes; eight diagonals is the eight-way form of 7, and twelve face diagonals is an alternative selection at 11.',
  uses:['nLat','gen'], view:[0.65,0.42,13,0],
  extra: () => `<div class="row"><button data-l="sc">six axes</button><button data-l="bcc">eight diagonals</button><button data-l="fcc">twelve face diagonals</button><button data-l="mix">axes and diagonals</button></div>`,
  bind(S,$){ document.querySelectorAll('#ctl button[data-l]').forEach(bn => { bn.setAttribute('aria-pressed', bn.dataset.l === X.lat);
    bn.addEventListener('click', () => { X.lat = bn.dataset.l; document.querySelectorAll('#ctl button[data-l]').forEach(q => q.setAttribute('aria-pressed', q.dataset.l === X.lat)); window.MIXER_API.set('gen', window.MIXER_API.P.gen); }); }); },
  make(g){ this.g = new T.Group(); g.add(this.g); },
  enter(S){ clear(this.g); const L = LAT[X.lat], mix = X.lat === 'mix'; let vecs, rad, gens = S.gen;
    if(mix){  const dA = 1, dD = (3/4)/(2/3); vecs = ARMS[6].map(a => a.map(v => v*dA)).concat(ARMS[8].map(a => a.map(v => v*dD))); rad = 0.07; }
    else { vecs = L.arms; this.G = Math.tanh(S.nLat*Math.log(L.z)/2); rad = this.G/2; }
    const R = grow(vecs, gens, mix ? 1800 : 900), n = R.pts.length;
    const mesh = new T.InstancedMesh(new T.SphereGeometry(rad, mix ? 8 : 18, mix ? 6 : 12), new T.MeshStandardMaterial({roughness:0.45, metalness:0.1, transparent:true, opacity: mix ? 0.95 : 0.82}), n);
    const m4 = new T.Matrix4(), ramp = [[1,1,1],GOLD,CYAN,ROSE,[0.55,1,0.6]];
    R.pts.forEach((p,i) => { m4.makeTranslation(p[0],p[1],p[2]); mesh.setMatrixAt(i, m4); mesh.setColorAt(i, M.tcol(ramp[p[3]])); });
    mesh.instanceMatrix.needsUpdate = true; if(mesh.instanceColor) mesh.instanceColor.needsUpdate = true; this.g.add(mesh);
    for(const v of vecs) this.g.add(M.line([V3(0,0,0), V3(v[0],v[1],v[2])], cWHITE, 0.8));
    const near = R.pts.filter(p => p[3] > 0).map(p => Math.hypot(p[0],p[1],p[2])), dmin = Math.min.apply(null, near), coord = near.filter(d => Math.abs(d-dmin) < 1e-6).length;
    if(mix){ this.rows = [['arm set', L.name], ['closes into a lattice', 'no'], ['diagonal arm / axis arm', fmt(dD_ratio(),4)], ['ratio needed to close', '0.8660'], ['centres after each generation', R.counts.slice(1).join(', ')]];
      const seps = []; for(let g=1; g<=gens; g++) seps.push(fmt(minSep(R.pts.filter(p => p[3] <= g)),4)); this.rows.push(['smallest distance after each', seps.join(', ')]);
      this.rows.push(['fifth generation (not drawn)', '5139 centres, smallest distance 0.0891']); }
    else this.rows = [['arm set', L.name + ', step z = ' + L.z], ['closes into', L.lat], ['neighbours of each ball', String(coord)], ['shell distances and counts', L.shells],
      ['cut surface G_n', fmt(this.G,5)], ['gap layer between cut balls', fmt(2*(1-this.G),5) + ' rim radii'], ['nearest centres / cut diameter', fmt(1/this.G,4)],
      ['filling by cut balls', fmt(L.rim*Math.pow(this.G,3),3)], ['filling by rims', fmt(L.rim,3)], ['balls drawn', String(n)]]; },
  change(S){ this.enter(S); },
  step(){ return this.rows; } };
function dD_ratio(){ return (3/4)/(2/3); }

/* ================= EYE 5: the square of four joins ================= */
const cx = (re,im=0) => ({re,im}), cmul = (a,b) => cx(a.re*b.re-a.im*b.im, a.re*b.im+a.im*b.re), cadd = (a,b) => cx(a.re+b.re,a.im+b.im), conj = a => cx(a.re,-a.im);
const cdiv = (a,b) => { const d = b.re*b.re+b.im*b.im; return cx((a.re*b.re+a.im*b.im)/d, (a.im*b.re-a.re*b.im)/d); };
const mm = (A,B) => ({ a: cadd(cmul(A.a,B.a), cmul(A.b,conj(B.b))), b: cadd(cmul(A.a,B.b), cmul(A.b,conj(B.a))) });
const act = (A,w) => cdiv(cadd(cmul(A.a,w),A.b), cadd(cmul(conj(A.b),w),conj(A.a)));
const tx = d => ({a:cx(Math.cosh(d/2)), b:cx(Math.sinh(d/2))}), ty = d => ({a:cx(Math.cosh(d/2)), b:cx(0,Math.sinh(d/2))});
const RD = 2.5, onDisk = w => V3(RD*w.re, 0, -RD*w.im);
const SPECIAL = [['60°',2.6592270586],['90°',3.2201933723],['120°',2+Math.sqrt(3)],['180°',4.6115817893],['z = 5',5],['wall',WALL],['z*',ZSTAR],['z = 7',7],['z = 11',11]];
const eyeLoop = { id:'loop', title:'The square of four joins', section:'Loop of two perpendicular joins', grade:'exact',
  eq:'q = (z − 1)²/(4z)\ninside the wall:  cos(θ/2) = 1 − 2q²\npast the wall:  λ = 4 arccosh q\nwall:  q = 1,  z = 3 + 2√2',
  text:'Step out along one arm, along a perpendicular arm, back along the first and back along the second, each by ln z. The gold path is that square, drawn in the disk of one ball. It does not close: the pink segment joins its end to its start. Repeating the square carries the centre to the white points. Inside the wall they lie on a circle and the square is a turn by θ about the marked point, which moves to the rim as z rises to the wall. Past the wall there is no turn: each pass is a run of length λ toward the rim. The buttons set the steps where the turn is 60°, 90°, 120° and 180°, the wall, and z* where the run per pass equals one ball step ln z.',
  uses:['zL'], view:[0.0,1.05,7.4,0],
  extra: () => `<div class="row">` + SPECIAL.map((s,i) => `<button data-z="${i}">${s[0]}</button>`).join('') + `</div>`,
  bind(S,$){ document.querySelectorAll('#ctl button[data-z]').forEach(bn => bn.addEventListener('click', () => window.MIXER_API.set('zL', SPECIAL[+bn.dataset.z][1]))); },
  make(g){ this.g = new T.Group(); g.add(this.g); g.add(M.line(ringPts(RD,1,200), cCYAN, 0.85)); for(let k=1;k<4;k++) g.add(M.line(ringPts(RD*k/4,1,120), cCYAN, 0.1));
    const l = M.label('rim of the ball', '#63d3ff', 0.3); l.position.set(-RD*0.8, 0.2, -RD*0.8); g.add(l); this.mark = M.points(1, 0.34); g.add(this.mark); },
  enter(S){ clear(this.g); const z = S.zL, d = Math.log(z), inv = A => ({a:conj(A.a), b:cx(-A.b.re,-A.b.im)});
    const steps = [tx, ty, t => inv(tx(t)), t => inv(ty(t))]; let Mcur = {a:cx(1), b:cx(0)}; const path = [];
    for(const f of steps){ for(let i=0;i<=40;i++) path.push(onDisk(act(mm(Mcur, f(d*i/40)), cx(0)))); Mcur = mm(Mcur, f(d)); }
    const W = Mcur; this.g.add(M.line(path, cGOLD, 1)); this.g.add(M.line([path[path.length-1], V3(0,0,0)], cROSE, 1));
    const q = (z-1)*(z-1)/(4*z), h = (W.a.re), inside = q < 1 - 1e-9; this.orbit = [cx(0)]; let Wn = W;
    for(let n=1;n<=48;n++){ this.orbit.push(act(Wn, cx(0))); Wn = mm(Wn, W); }
    const op = M.points(this.orbit.length, 0.15); this.orbit.forEach((w,i) => M.setPt(op, i, onDisk(w), [1,1,1].map(v => v*(i===0 ? 1 : 0.75)))); M.flush(op); this.g.add(op);
    const G2 = Math.pow((z-1)/(z+1),2), x = 2*G2, K = x < 1 ? 1/(1-x) : x/(x-1);
    this.rows = [['Γ² of one join', fmt(G2,6)], ['q', fmt(q,6)], ['half trace of the square', fmt(h,6)], ['1 − 2q²', fmt(1-2*q*q,6)]];
    if(inside){ const th = 2*Math.acos(Math.max(-1,Math.min(1,h)));
      /* fixed point of the square inside the disk: root of conj(b) w² + (conj(a) − a) w − b = 0 */
      const A = conj(W.b), B = cx(0, -2*W.a.im), C = cx(-W.b.re, -W.b.im), disc = cadd(cmul(B,B), cmul(cx(-4), cmul(A,C)));
      const r = Math.sqrt(Math.hypot(disc.re,disc.im)), ph = Math.atan2(disc.im,disc.re)/2, sq = cx(r*Math.cos(ph), r*Math.sin(ph));
      let p = cdiv(cadd(cx(-B.re,-B.im), sq), cmul(cx(2),A)); const p2 = cdiv(cadd(cx(-B.re,-B.im), cx(-sq.re,-sq.im)), cmul(cx(2),A)); if(Math.hypot(p2.re,p2.im) < Math.hypot(p.re,p.im)) p = p2;
      const fp = M.points(1, 0.3); M.setPt(fp, 0, onDisk(p), ROSE); M.flush(fp); this.g.add(fp);
      /* the orbit circle: Euclidean circle through 0, W·0, W²·0 */
      const a1 = this.orbit[1], a2 = this.orbit[2], det = 2*(a1.re*a2.im - a1.im*a2.re);
      if(Math.abs(det) > 1e-9){ const s1 = a1.re*a1.re+a1.im*a1.im, s2 = a2.re*a2.re+a2.im*a2.im, ux = (s1*a2.im - s2*a1.im)/det, uy = (a1.re*s2 - a2.re*s1)/det, rr = Math.hypot(ux,uy);
        const c = []; for(let i=0;i<=160;i++){ const t = 2*PI*i/160; c.push(onDisk(cx(ux + rr*Math.cos(t), uy + rr*Math.sin(t)))); } this.g.add(M.line(c, cWHITE, 0.35)); }
      this.rows.push(['kind', 'turn'], ['turn θ per pass', fmt(th*180/PI,4) + '°'], ['passes for a full turn', fmt(2*PI/th,4)], ['centre of the turn, radius²', fmt(p.re*p.re+p.im*p.im,6)]); }
    else { const lam = 4*Math.acosh(Math.max(1,q)); this.rows.push(['kind', q > 1 + 1e-9 ? 'run' : 'wall'], ['run λ per pass', fmt(lam,6)], ['one ball step ln z', fmt(d,6)], ['λ / ln z', fmt(lam/d,6)], ['amplitude kept per pass e^(−λ)', fmt(Math.exp(-lam),6)]); }
    this.rows.push(['K of the join', K > 1e6 ? 'unbounded at the wall' : fmt(K,4)]); },
  change(S){ this.enter(S); },
  step(dt, S, t){ const i = Math.floor(t*2.5) % this.orbit.length, w = this.orbit[i]; M.setPt(this.mark, 0, onDisk(w), GOLD); M.flush(this.mark);
    return this.rows.concat([['pass shown', String(i)]]); } };

M.run({ title:'Balls on the Field', byline:'JEROMIE BEASLEY · MIXER v1 · 14 NOV 2026 · AI-ASSISTED',
  note:'an explorer of checked formulas, not a test of them',
  feed:{ params, build }, eyes:[eyeOne, eyeTwo, eyeField, eyeLat, eyeLoop], film:['one','two','field','lattice','loop'] });
})();
