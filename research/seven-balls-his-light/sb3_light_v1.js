/* SCRIPT: SB3-LIGHT-V1 — his light in the seven balls, with no walls but the balls.
   Jeromie Beasley. 18 Nov 2026. AI-assisted.

   The balls. C is his ball, radius 1. Six neighbour balls sit on ±x ±y ±z. In his ball each of the six faces is a sphere standing
   at h = r_a/2 on its arm, meeting C's rim at right angles: apex at ρ = tanh(h/2), centre (1 + ρ²)/(2ρ), radius (1 − ρ²)/(2ρ)
   (LH-MIXER-V2 capParams). Here that sphere IS the neighbour ball, at every moment: it moves in and out along its arm and grows and
   shrinks with the breath, as the face did. r_a(t) is his own drive (LH-MATH-V1 rOf: PER 8, 13, 21, phases a third apart).
   The two balls on one axis share it. Nothing else is a wall.

   The light (two ways, a switch):
   'his'  — his ball's light. Packets of light move in time along C's own geodesics (hyperboloid X(s) = cosh s X + sinh s V, speed 1),
            exactly as his tracer's rays (LH-MATH-V1 traceRay), but every face is a real neighbour ball. In C's own geometry C's sphere
            is infinitely far, so the light never leaves C: what it does not return goes on toward the rim, the ground, and is booked there.
   'room' — straight light in the room: packets move in straight lines at speed 1 among all seven balls; any ball's sphere is a wall;
            where a packet would leave every ball (the gap) the rim is ground and returns everything (VOTKP: |Γ| = 1 is ground).
   At every wall the split is his: Y = Π 1/z over the balls the packet is inside, other than C (his nodeAdmittance, orient 1),
   LH.splitAtFace(Y1², Y2², sin²θ, ω, 1), reflected by LH.reflectDir, passed by LH.refractDir (in 'room' their straight-line forms).
   A ball that moves over a packet is a wall crossing too, split the same way at that moment.
   Books: emitted = in flight + on the ground (his) + below the cut, exactly. */
(function(root){
"use strict";
const L = root.LH || require('./lh_math_v1.js');
const mink = L.mink, lin = L.lin;
const AXW = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]];   /* neighbour i: +x −x +y −y +z −z = his generators k = i (I = x, J = y, K = z) */
const RIM = 0.985;                                                  /* his rim cut (traceRay) */
const X0RIM = (1 + RIM*RIM)/(1 - RIM*RIM);

/* ---------- the balls at time t ---------- */
function balls(P, tau){ const out = [{ name:'C', c:[0,0,0], R:1, z:1, G:0, r:0 }];
  for(let i=0;i<6;i++){ const a = i >> 1, r = L.rOf(P, a, tau), h = r/2, rho = Math.tanh(h/2), cc = (1 + rho*rho)/(2*rho), R = (1 - rho*rho)/(2*rho);
    out.push({ name:'N' + ['+x','−x','+y','−y','+z','−z'][i], i, a, c:AXW[i].map(v => v*cc), R, cc, r, h, rho, z:Math.exp(r), G:Math.tanh(r/2) }); }
  return out; }
/* the neighbour's sphere as a plane section of C's hyperboloid: |q − k|² − R² ∝ F(X) = mink(n, X) + C0, n = (1 + K, 2k), K = |k|² − R², C0 = K − 1.
   F < 0 inside the ball. For a sphere at right angles to C (K = 1) C0 = 0: a plane through the origin, his face. */
function planeOf(b){ const K = b.c[0]*b.c[0] + b.c[1]*b.c[1] + b.c[2]*b.c[2] - b.R*b.R; return { n:[1 + K, 2*b.c[0], 2*b.c[1], 2*b.c[2]], C0:K - 1 }; }
const Fval = (pl, X) => mink(pl.n, X) + pl.C0;
const toQ = X => [X[1]/(1 + X[0]), X[2]/(1 + X[0]), X[3]/(1 + X[0])];
function admit(word, B){ let Y = 1; for(const j of word) Y /= B[j].z; return Y; }
const toggle = (word, j) => word.indexOf(j) >= 0 ? word.filter(x => x !== j) : word.concat([j]).sort((a,b) => a - b);

/* ---------- 'his': the next event along C's geodesic within length Lmax ---------- */
function rootsE(a, b, c){ /* a e² + b e + c = 0, roots e > 1 */ const out = []; if(Math.abs(a) < 1e-14){ if(Math.abs(b) > 1e-300){ const e = -c/b; if(e > 1) out.push(e); } return out; }
  const D = b*b - 4*a*c; if(D < 0) return out; const sq = Math.sqrt(D), q = -0.5*(b + (b >= 0 ? sq : -sq)); const e1 = q/a, e2 = Math.abs(q) > 1e-300 ? c/q : Infinity; [e1, e2].forEach(e => { if(e > 1 && Number.isFinite(e)) out.push(e); }); return out; }
function nextHyp(X, V, PL, Lmax, skip){ let best = null;
  for(let j=1;j<PL.length;j++){ const pl = PL[j], A = mink(pl.n, X), B = mink(pl.n, V), C0 = pl.C0;
    for(const e of rootsE(A + B, 2*C0, A - B)){ const s = Math.log(e); if(s <= 1e-9 || s > Lmax) continue; if(j === skip && s < 1e-7) continue; if(!best || s < best.s) best = { s, j }; } }
  /* the rim: X0 cosh s + V0 sinh s = X0RIM */
  for(const e of rootsE(X[0] + V[0], -2*X0RIM, X[0] - V[0])){ const s = Math.log(e); if(s > 1e-12 && s <= Lmax && (!best || s < best.s)) best = { s, j:0 }; }
  return best; }
/* the split at wall j: the plane's normal at the hit, his incidence / split / reflect / refract */
function splitHyp(Y, T, pl, word, j, B, omega){ const m = mink(pl.n, Y), nt = lin(1, pl.n, -m, Y), nn = Math.sqrt(Math.max(1e-300, -mink(nt, nt))), N = nt.map(v => v/nn);
  const inc = L.incidence(T, N), w2 = toggle(word, j), Y1 = admit(word, B), Y2 = admit(w2, B), sp = L.splitAtFace(Y1*Y1, Y2*Y2, inc.sin*inc.sin, omega, 1);
  return { N, sp, w2, tr:L.reflectDir(T, N), tt:sp.total ? null : L.refractDir(T, N, sp.sin2sq) }; }
const renorm = (X, V) => { const x = Math.sqrt(Math.max(1e-300, mink(X, X))); X = X.map(v => v/x); const m = mink(X, V); V = lin(1, V, -m, X); const v = Math.sqrt(Math.max(1e-300, -mink(V, V))); return [X, V.map(u => u/v)]; };

/* ---------- 'room': straight light among the seven spheres ---------- */
const dot = (a,b) => a[0]*b[0] + a[1]*b[1] + a[2]*b[2], sub = (a,b) => [a[0]-b[0], a[1]-b[1], a[2]-b[2]], add = (a,b,s) => [a[0]+s*b[0], a[1]+s*b[1], a[2]+s*b[2]];
const inside = (p, b) => { const d = sub(p, b.c); return dot(d, d) < b.R*b.R; };
function maskOf(p, B){ const w = []; for(let j=0;j<B.length;j++) if(inside(p, B[j])) w.push(j); return w; }
function nextRoom(p, u, B, Lmax, skip){ let best = null; for(let j=0;j<B.length;j++){ const d = sub(p, B[j].c), b = dot(d, u), c = dot(d, d) - B[j].R*B[j].R, D = b*b - c; if(D < 0) continue; const sq = Math.sqrt(D);
    for(const t of [-b - sq, -b + sq]){ if(t <= 1e-9 || t > Lmax) continue; if(j === skip && t < 1e-7) continue; if(!best || t < best.s) best = { s:t, j }; } } return best; }
function admitRoom(w, B){ let Y = 1; for(const j of w) if(j !== 0) Y /= B[j].z; return Y; }
function splitRoom(p, u, j, word, B, omega){ const n0 = sub(p, B[j].c), nl = Math.hypot(n0[0], n0[1], n0[2]), n = n0.map(v => v/nl), un = dot(u, n), w2 = toggle(word, j);
  const reflect = add(u, n, -2*un), s1sq = Math.max(0, 1 - un*un);
  if(w2.length === 0) return { n, w2, ground:true, sp:{ R:1, T:0, total:true }, tr:reflect, tt:null };   /* leaving every ball: the rim is ground */
  const Y1 = admitRoom(word, B), Y2 = admitRoom(w2, B), sp = L.splitAtFace(Y1*Y1, Y2*Y2, s1sq, omega, 1); let tt = null;
  if(!sp.total){ const tp = add(u, n, -un), s1 = Math.sqrt(s1sq), s2 = Math.sqrt(Math.max(0, Math.min(1, sp.sin2sq))), c2 = Math.sqrt(Math.max(0, 1 - s2*s2));
    tt = s1 < 1e-15 ? n.map(v => Math.sign(un)*c2*v) : [0,1,2].map(q => Math.sign(un)*c2*n[q] + (s2/s1)*tp[q]); }
  return { n, w2, sp, tr:reflect, tt }; }

/* ---------- the world ---------- */
function makeWorld(o){ o = Object.assign({ mode:'his', zI:3, zJ:5, zK:7, A:0.35, breathe:true, omega:3, fan:62, nray:9, cut:1e-3, maxPk:5000, emitEvery:0, source:0 }, o || {});
  const W = { o, t:0, pk:[], emitted:0, ground:0, cut:0, groundBy:new Float64Array(7), push:new Float64Array(7), hits:[], deposits:[], nHits:0 };
  W.P = { zI:o.zI, zJ:o.zJ, zK:o.zK, A:o.A, drive:o.breathe ? 'breathe' : 'hold' }; W.B = balls(W.P, 0); W.PL = W.B.map(planeOf); W.lastEmit = -1e9; return W; }
/* his fan of rays (LH-MATH-V1 fanDirs), turning with χ = 2πτ/34, from the source's centre */
function emit(W){ const S = { chi:2*Math.PI*W.t/34, nray:W.o.nray, fan:W.o.fan }, dirs = L.fanDirs(S), f = 1/dirs.length, src = W.o.mode === 'his' ? 0 : W.o.source;
  for(const d of dirs){ if(W.o.mode === 'his') W.pk.push({ X:[1,0,0,0], V:[0, d[0], d[1], d[2]], flux:f, word:[], depth:0, trail:[] });
    else { const p = W.B[src].c.slice(); W.pk.push({ p, u:d.slice(), flux:f, word:maskOf(p, W.B), depth:0, trail:[] }); } }
  W.emitted += 1; W.lastEmit = W.t; }
function posOf(W, k){ return W.o.mode === 'his' ? toQ(k.X) : k.p; }
/* advance every packet by length Lstep; the balls are held at their time-t places during the step and moved after */
function step(W, dt){ const o = W.o, B = W.B, PL = W.PL, out = [];
  const pushPk = (k) => { if(k.flux < o.cut*(1/o.nray)){ W.cut += k.flux; return; } out.push(k); };
  for(const k0 of W.pk){ let queue = [[k0, dt, -1]];
    while(queue.length){ const [k, Lrem, skip] = queue.pop();
      if(o.mode === 'his'){ const ev = nextHyp(k.X, k.V, PL, Lrem, skip);
        if(!ev){ const X = lin(Math.cosh(Lrem), k.X, Math.sinh(Lrem), k.V), V = lin(Math.sinh(Lrem), k.X, Math.cosh(Lrem), k.V); [k.X, k.V] = renorm(X, V); pushPk(k); continue; }
        const Y = lin(Math.cosh(ev.s), k.X, Math.sinh(ev.s), k.V), T = lin(Math.sinh(ev.s), k.X, Math.cosh(ev.s), k.V);
        if(ev.j === 0){ W.ground += k.flux; const q = toQ(Y); let by = 0; for(const j of k.word) by = j; W.groundBy[by] += k.flux; W.deposits.push({ q, f:k.flux, age:0 }); continue; }
        const sp = splitHyp(Y, T, PL[ev.j], k.word, ev.j, B, o.omega); W.nHits++; W.hits.push({ q:toQ(Y), f:k.flux*sp.sp.R, age:0, total:sp.sp.total }); W.push[ev.j] += 2*sp.sp.R*k.flux;
        const R = k.flux*sp.sp.R, Tf = k.flux*sp.sp.T, Lr = Lrem - ev.s;
        if(R > 0){ let [X, V] = renorm(Y, sp.tr); const c = { X, V, flux:R, word:k.word, depth:k.depth + 1, trail:k.trail.slice() }; if(R < o.cut/o.nray) W.cut += R; else queue.push([c, Lr, ev.j]); }
        if(Tf > 0 && sp.tt){ let [X, V] = renorm(Y, sp.tt); const c = { X, V, flux:Tf, word:sp.w2, depth:k.depth + 1, trail:k.trail.slice() }; if(Tf < o.cut/o.nray) W.cut += Tf; else queue.push([c, Lr, ev.j]); } }
      else { const ev = nextRoom(k.p, k.u, B, Lrem, skip);
        if(!ev){ k.p = add(k.p, k.u, Lrem); pushPk(k); continue; }
        const p = add(k.p, k.u, ev.s), sp = splitRoom(p, k.u, ev.j, k.word, B, o.omega); W.nHits++; W.hits.push({ q:p, f:k.flux*sp.sp.R, age:0, total:sp.sp.total || !!sp.ground }); W.push[ev.j] += 2*sp.sp.R*k.flux;
        const R = k.flux*sp.sp.R, Tf = k.flux*sp.sp.T, Lr = Lrem - ev.s;
        if(R > 0){ const c = { p:p.slice(), u:sp.tr, flux:R, word:k.word, depth:k.depth + 1, trail:k.trail.slice() }; if(R < o.cut/o.nray) W.cut += R; else queue.push([c, Lr, ev.j]); }
        if(Tf > 0 && sp.tt){ const c = { p:p.slice(), u:sp.tt, flux:Tf, word:sp.w2, depth:k.depth + 1, trail:k.trail.slice() }; if(Tf < o.cut/o.nray) W.cut += Tf; else queue.push([c, Lr, ev.j]); } } } }
  /* too many packets: the faintest go below the cut, booked */
  if(out.length > o.maxPk){ out.sort((a, b) => b.flux - a.flux); for(let q=o.maxPk;q<out.length;q++) W.cut += out[q].flux; out.length = o.maxPk; }
  W.pk = out; W.t += dt;
  /* the balls move: a ball that passes over a packet is a wall crossing at that moment */
  const B2 = balls(W.P, W.t), PL2 = B2.map(planeOf), keep = [];
  for(const k of W.pk){ let cur = k;
    if(o.mode === 'his'){ for(let j=1;j<7;j++){ const was = Fval(PL[j], cur.X) < 0, now = Fval(PL2[j], cur.X) < 0; if(was === (cur.word.indexOf(j) >= 0) && was !== now){ const sp = splitHyp(cur.X, cur.V, PL2[j], cur.word, j, B2, o.omega); W.nHits++; W.push[j] += 2*sp.sp.R*cur.flux;
          const R = cur.flux*sp.sp.R, Tf = cur.flux*sp.sp.T; /* the ball came over the packet: the passed part is inside it now, the returned part stays outside */
          if(R >= o.cut/o.nray){ const [X, V] = renorm(cur.X, sp.tr); keep.push({ X, V, flux:R, word:cur.word, depth:cur.depth + 1, trail:cur.trail.slice() }); } else W.cut += R;
          if(Tf >= o.cut/o.nray && sp.tt){ const [X, V] = renorm(cur.X, sp.tt); cur = { X, V, flux:Tf, word:sp.w2, depth:cur.depth + 1, trail:cur.trail }; } else { W.cut += Tf; cur = null; break; } } } }
    else { const now = maskOf(cur.p, B2); for(let j=0;j<7;j++){ const inW = cur.word.indexOf(j) >= 0, inN = now.indexOf(j) >= 0; if(inW === inN) continue; const sp = splitRoom(cur.p, cur.u, j, cur.word, B2, o.omega); W.nHits++; W.push[j] += 2*sp.sp.R*cur.flux;
        const R = cur.flux*sp.sp.R, Tf = cur.flux*sp.sp.T;
        if(sp.ground){ /* the gap came over the packet: the ground returns it into the ball it was in, which is still around it in the old word */ cur = { p:cur.p, u:sp.tr, flux:cur.flux, word:cur.word, depth:cur.depth + 1, trail:cur.trail }; continue; }
        if(Tf >= o.cut/o.nray && sp.tt){ if(R >= o.cut/o.nray) keep.push({ p:cur.p.slice(), u:sp.tr, flux:R, word:cur.word, depth:cur.depth + 1, trail:cur.trail.slice() }); else W.cut += R; cur = { p:cur.p, u:sp.tt, flux:Tf, word:sp.w2, depth:cur.depth + 1, trail:cur.trail }; }
        else { W.cut += Tf; cur = { p:cur.p, u:sp.tr, flux:R, word:cur.word, depth:cur.depth + 1, trail:cur.trail }; } } }
    if(cur) keep.push(cur); }
  W.pk = keep; W.B = B2; W.PL = PL2;
  if(o.emitEvery > 0 && W.t - W.lastEmit >= o.emitEvery) emit(W); }
function books(W){ let fl = 0; const by = new Float64Array(7); for(const k of W.pk){ fl += k.flux; let w = 0; for(const j of k.word) if(j !== 0) w = j; by[w] += k.flux; } return { emitted:W.emitted, flight:fl, ground:W.ground, cut:W.cut, total:fl + W.ground + W.cut, inBall:by }; }
/* a static trace with the same event code, for the check against his traceRay (depth limit and cut as his) */
function traceStatic(P, tau, omega, d, cut){ const B = balls(P, tau), PL = B.map(planeOf), segs = [], stack = [{ X:[1,0,0,0], V:[0, d[0], d[1], d[2]], flux:1, word:[], depth:0, skip:-1 }];
  while(stack.length){ const q = stack.pop(), ev = nextHyp(q.X, q.V, PL, 50, q.skip);
    if(!ev || ev.j === 0){ segs.push({ word:q.word, flux:q.flux, depth:q.depth, end:'rim', X:q.X, V:q.V }); continue; }
    const Y = lin(Math.cosh(ev.s), q.X, Math.sinh(ev.s), q.V), T = lin(Math.sinh(ev.s), q.X, Math.cosh(ev.s), q.V), sp = splitHyp(Y, T, PL[ev.j], q.word, ev.j, B, omega);
    segs.push({ word:q.word, flux:q.flux, depth:q.depth, end:'face', X:q.X, V:q.V, hit:Y, s:ev.s, j:ev.j, R:sp.sp.R, T:sp.sp.T, total:sp.sp.total, tr:sp.tr, tt:sp.tt });
    if(q.depth + 1 >= 6) continue; const fr = q.flux*sp.sp.R, ft = q.flux*sp.sp.T;
    if(fr > cut) stack.push({ X:Y, V:sp.tr, flux:fr, word:q.word, depth:q.depth + 1, skip:ev.j });
    if(!sp.sp.total && ft > cut) stack.push({ X:Y, V:sp.tt, flux:ft, word:sp.w2, depth:q.depth + 1, skip:ev.j }); }
  return segs; }
root.SB3 = { balls, planeOf, Fval, toQ, makeWorld, emit, step, books, posOf, traceStatic, AXW, RIM };
})(typeof window !== 'undefined' ? window : globalThis);
if(typeof module !== 'undefined') module.exports = globalThis.SB3;
