// SCRIPT: W-FL-MATH-SIGNFLIP-COPY (watcher scratch copy of FL-MATH-V1 with the two arm-arm face signs reversed; not a deliverable)
/* SCRIPT: FL-MATH-V1
   The Flock of Balls on the Field: mathematics. Jeromie Beasley. 16 Nov 2026. AI-assisted.
   N whole balls on the field (centre A and balls one VOTKP peel step out along the arms). What is new against MM-MATH-V1 / TB-MATH-V1:
   (1) THE GAP IS REAL. A link is a stretch of field of hyperbolic length d. Light crosses it at speed 1 (one unit of length per unit
       of field time), so it arrives after t = d and not before. On the way it meets the faces: each face is one reflecting step,
       r = Gamma = tanh(step/2), t = sqrt(1 - Gamma^2) (LEAN step_matching, flux_balance, reciprocity Gamma_21 = -Gamma_12).
       A centre-arm link crosses one face (at half the step). An arm-arm link crosses the two faces of the centre cell; when those
       faces stand apart (g = sinh h_a sinh h_b > 1, gap delta = arccosh g) the light between them only tunnels, amplitude
       sech(kappa_g delta) (lossless film with |t|^2 = sin^2 phi / (sinh^2 kd + sin^2 phi) at phi = pi/2).            [HYPOTHESIS: gap layer]
   (2) EACH BALL HAS ITS OWN CLOCK. Ball i runs at rate_i of the field time: its two levels sit at -+ omega rate_i / 2.
       Centre: rate 1. A ball one step r out: rate 1/z, z = e^r, the radar ratio of the step.                         [HYPOTHESIS: clock ratio z]
       clocks:'equal' gives every ball rate 1, for comparison.
   (3) THE BALL FIELDS. Each ball's field d_i turns under the light it holds (the light's spin) and under its faces.
       push:'static' (default): the faces hold ball i toward its rest direction, 2 kappa sum_j (d_i - R_ij d_j^rest); a change in a
       neighbour reaches it only as light through the gap. Rest is exactly still.                                       [MODEL CHOICE]
       push:'retarded': the face push uses ball j's direction as it was one crossing time ago. No field carries that push, so its
       energy is not booked, and FL-CHECK-01 finds the rest state unstable under it (delay instability). Kept for exploring only.
       push:'off': no face push.
   Light is one quantum, a two-component amplitude per ball and per point of each link. Every step is exactly unitary, so
   (light in the balls) + (light in the gaps) = 1 on every step: the books. Needs MM (MM-MATH-V1) for the hyperbolic geometry. */
var FL = (function(){
"use strict";
const MMr = (typeof MM !== 'undefined') ? MM : require('/home/claude/balls/w/mm/mm_math_v1.js');
const AX = MMr.AXES, NAMES = ['A','B','C','D','E','F','G'];
/* which arms carry a ball, for N = 3, 4, 7: +I, +J, +K, then -I, -J, -K */
const ARMS = { 3:[0,2], 4:[0,2,4], 7:[0,2,4,1,3,5] };
const perp = (a,b) => (a>>1) !== (b>>1);
/* ---------- 2-component complex helpers: a spinor is [re0, im0, re1, im1]; U is MM's su2 form [u00,u01,u10,u11] as [re,im] ---------- */
function applyU(U, x, dag, out){ out = out || [0,0,0,0];
  for(let r=0;r<2;r++){ let sr = 0, si = 0; for(let s=0;s<2;s++){ const u = dag ? U[2*s+r] : U[2*r+s], ur = u[0], ui = dag ? -u[1] : u[1], xr = x[2*s], xi = x[2*s+1]; sr += ur*xr - ui*xi; si += ur*xi + ui*xr; } out[2*r] = sr; out[2*r+1] = si; } return out; }
const n2 = x => x[0]*x[0]+x[1]*x[1]+x[2]*x[2]+x[3]*x[3];
/* point at arc length s on the geodesic from p to q (hyperboloid vectors), d = dist */
function geo(p, q, d, s){ const a = Math.sinh(d-s)/Math.sinh(d), b = Math.sinh(s)/Math.sinh(d); return p.map((x,k) => a*x + b*q[k]); }
/* arc length along p->q where the geodesic crosses the plane of points equidistant from u and v */
function crossAt(p, q, d, u, v){ const f = s => { const x = geo(p,q,d,s); return MMr.mink(x,u) - MMr.mink(x,v); }; let lo = 0, hi = d, flo = f(lo); for(let k=0;k<80;k++){ const m = (lo+hi)/2, fm = f(m); if((fm > 0) === (flo > 0)){ lo = m; flo = fm; } else hi = m; } return (lo+hi)/2; }
/* ---------- the world ---------- */
function makeWorld(opts){ opts = Object.assign({ N:3, z:[3,5,7], omega:2.0, gamma:0.6, kappa:0.25, kgap:1.0, h:0.005, clocks:'z', push:'static', torque:1 }, opts||{});
  const r = opts.z.map(Math.log), arms = ARMS[opts.N], N = arms.length + 1;
  const balls = [{ p:[1,0,0,0], arm:-1, r:0, rate:1, name:'A' }].concat(arms.map((a,k) => { const rr = r[a>>1], u = AX[a]; return { p:[Math.cosh(rr), Math.sinh(rr)*u[0], Math.sinh(rr)*u[1], Math.sinh(rr)*u[2]], arm:a, r:rr, rate:opts.clocks === 'z' ? Math.exp(-rr) : 1, name:NAMES[k+1] }; }));
  const links = [];
  const mk = (i, j, marks) => { const d = MMr.linkDistance(balls[i].p, balls[j].p), R = MMr.linkRotation(balls[i].p, balls[j].p), U = MMr.su2(R);
    /* marks: [{s, rho, kind}] scatterers in order along i -> j; segments between them hold the travelling light */
    const cuts = [0].concat(marks.map(m => m.s)).concat([d]), segs = [];
    for(let k=0;k<cuts.length-1;k++){ const len = cuts[k+1]-cuts[k], n = Math.max(1, Math.round(len/opts.h)); segs.push({ s0:cuts[k], len, n, f:new Float64Array(4*n), b:new Float64Array(4*n), head:0 }); }
    const nTot = Math.max(1, Math.round(d/opts.h));
    links.push({ i, j, d, R, U, Gam:Math.tanh(d/2), marks, segs, nTot, hi:new Float64Array(3*nTot), hj:new Float64Array(3*nTot), hh:0, c:0 }); };
  for(let k=1;k<N;k++){ const rr = balls[k].r; mk(0, k, [{ s:rr/2, rho:Math.tanh(rr/2), kind:'face' }]); }
  for(let a=1;a<N;a++) for(let b=a+1;b<N;b++) if(perp(balls[a].arm, balls[b].arm)){ const pa = balls[a].p, pb = balls[b].p, d = MMr.linkDistance(pa, pb);
    const s1 = crossAt(pa, pb, d, balls[0].p, pa), s2 = crossAt(pa, pb, d, balls[0].p, pb), g = Math.sinh(balls[a].r/2)*Math.sinh(balls[b].r/2), del = g > 1 ? Math.acosh(g) : 0;
    const marks = [{ s:s1, rho:-Math.tanh(balls[a].r/2), kind:'face' }]; if(del > 0) marks.push({ s:(s1+s2)/2, rho:Math.tanh(opts.kgap*del), kind:'gap', delta:del });
    marks.push({ s:s2, rho:Math.tanh(balls[b].r/2), kind:'face' });   /* entering b's side: the same face seen from inside the centre cell, Gamma_21 = -Gamma_12 */
    mk(a, b, marks); links[links.length-1].g = g; links[links.length-1].delta = del; }
  const nbr = Array.from({length:N}, () => []); links.forEach((l,k) => { nbr[l.i].push(k); nbr[l.j].push(k); });
  const W = { N, balls, links, nbr, opts, r, d:null };
  /* rest directions of the ball fields: |d_i| = omega rate_i / 2, descend the face energy from a fixed off-symmetric start */
  let seed = 11; const rnd = () => (seed = (seed*16807) % 2147483647)/2147483647 - 0.5;
  W.d = balls.map(b => { const v = [0.2*rnd(), 0.2*rnd(), 1 + 0.2*rnd()], m = Math.hypot(...v); return v.map(x => x/m*opts.omega*b.rate/2); });
  const R = MMr.restState(W, { iters:60000, eta:0.08, withSea:false, tol:1e-12 }); W.d = R.d; W.restResidual = R.residual; W.dRest = R.d.map(v => v.slice());
  /* reference only: link strengths of the instantaneous matrix (MM form), so its eigenvectors can be compared with the flock's long-time shares */
  links.forEach(l => { let t = 1; l.marks.forEach(m => t *= Math.sqrt(1 - m.rho*m.rho)); l.c = 0.5*t; });
  return W; }
/* ---------- state ---------- */
function initState(W, opts){ opts = opts || {}; const S = { t:0, psi:Array.from({length:W.N}, () => [0,0,0,0]), d:W.d.map(v => v.slice()), tau:new Float64Array(W.N), steps:0 };
  W.links.forEach(l => { l.segs.forEach(sg => { sg.f.fill(0); sg.b.fill(0); sg.head = 0; }); l.hh = 0; for(let k=0;k<l.nTot;k++){ l.hi.set(S.d[l.i], 3*k); l.hj.set(S.d[l.j], 3*k); } });
  if(opts.source != null) kick(W, S, opts.source, opts.spin); return S; }
/* put the one quantum of light in ball src, its spin across that ball's field (as MM.initState) */
function kick(W, S, src, spin){ S.psi.forEach(p => p.fill(0)); W.links.forEach(l => l.segs.forEach(sg => { sg.f.fill(0); sg.b.fill(0); }));
  let sp = spin; if(!sp){ const dd = S.d[src], m0 = Math.hypot(...dd), u = dd.map(x => x/m0), a = Math.abs(u[0]) < 0.9 ? [1,0,0] : [0,1,0]; sp = [u[1]*a[2]-u[2]*a[1], u[2]*a[0]-u[0]*a[2], u[0]*a[1]-u[1]*a[0]]; }
  const m = Math.hypot(...sp), th = Math.acos(sp[2]/m), ph = Math.atan2(sp[1], sp[0]); S.psi[src] = [Math.cos(th/2), 0, Math.sin(th/2)*Math.cos(ph), Math.sin(th/2)*Math.sin(ph)]; S.kickT = S.t; S.src = src; }
const bloch = p => [2*(p[0]*p[2] + p[1]*p[3]), 2*(p[0]*p[3] - p[1]*p[2]), p[0]*p[0]+p[1]*p[1] - p[2]*p[2] - p[3]*p[3]];
/* ---------- one step of length h (field time) ---------- */
const _fo = [], _bo = [], _t1 = [0,0,0,0], _t2 = [0,0,0,0];
function step(W, S){ const h = W.opts.h, th = Math.sqrt(W.opts.gamma*h), cth = Math.cos(th), sth = Math.sin(th), N = W.N;
  /* (a) light: every link moves its light one sample; faces and gaps scatter; ball ports exchange with the ball (exact rotations) */
  for(const l of W.links){ const m = l.segs.length;
    for(let k=0;k<m;k++){ const sg = l.segs[k], o = 4*sg.head; _fo[k] = [sg.f[o],sg.f[o+1],sg.f[o+2],sg.f[o+3]]; _bo[k] = [sg.b[o],sg.b[o+1],sg.b[o+2],sg.b[o+3]]; }
    const fin = new Array(m), bin = new Array(m);
    /* left port: ball i. The backward stream is kept in ball j's frame, the forward stream in ball i's frame. */
    { const inc = applyU(l.U, _bo[0], false, _t1), p = S.psi[l.i], out = [0,0,0,0]; for(let c=0;c<4;c++){ out[c] = sth*p[c] + cth*inc[c]; p[c] = cth*p[c] - sth*inc[c]; } fin[0] = out; }
    { const inc = applyU(l.U, _fo[m-1], true, _t2), p = S.psi[l.j], out = [0,0,0,0]; for(let c=0;c<4;c++){ out[c] = sth*p[c] + cth*inc[c]; p[c] = cth*p[c] - sth*inc[c]; } bin[m-1] = out; }
    for(let k=1;k<m;k++){ const rho = l.marks[k-1].rho, tau = Math.sqrt(1 - rho*rho), fL = _fo[k-1], bR = _bo[k], Ub = applyU(l.U, bR, false), Uf = applyU(l.U, fL, true);
      fin[k] = [0,1,2,3].map(c => tau*fL[c] - rho*Ub[c]); bin[k-1] = [0,1,2,3].map(c => rho*Uf[c] + tau*bR[c]); }
    for(let k=0;k<m;k++){ const sg = l.segs[k], o = 4*sg.head; for(let c=0;c<4;c++){ sg.f[o+c] = fin[k][c]; sg.b[o+c] = bin[k][c]; } sg.head = (sg.head+1) % sg.n; } }
  /* (b) each ball's own clock: psi <- exp(-i h d.sigma) psi, |d_i| = omega rate_i / 2 */
  for(let i=0;i<N;i++){ const d = S.d[i], m = Math.hypot(d[0],d[1],d[2]), c = Math.cos(m*h), s = Math.sin(m*h)/m, p = S.psi[i], a0 = p[0], a1 = p[1], b0 = p[2], b1 = p[3];
    /* (d.sigma) psi = [dz a + (dx - i dy) b, (dx + i dy) a - dz b] */
    const yr0 = d[2]*a0 + d[0]*b0 + d[1]*b1, yi0 = d[2]*a1 + d[0]*b1 - d[1]*b0, yr1 = d[0]*a0 - d[1]*a1 - d[2]*b0, yi1 = d[0]*a1 + d[1]*a0 - d[2]*b1;
    p[0] = c*a0 + s*yi0; p[1] = c*a1 - s*yr0; p[2] = c*b0 + s*yi1; p[3] = c*b1 - s*yr1; S.tau[i] += h*W.balls[i].rate; }
  /* (c) ball fields: d_i' = G_i x d_i, G_i = light spin + 2 kappa sum_j (d_i - R_ij d_j(t - d_ij)); a rotation, so |d_i| is kept */
  const k2 = 2*W.opts.kappa, nd = new Array(N);
  const push = W.opts.push, tq = W.opts.torque;
  for(let i=0;i<N;i++){ const G = bloch(S.psi[i]).map(x => x*tq), di = S.d[i];
    if(push !== 'off') for(const li of W.nbr[i]){ const l = W.links[li], o = 3*l.hh, me = l.i === i, hist = me ? l.hj : l.hi, dj = push === 'static' ? W.dRest[me ? l.j : l.i] : [hist[o], hist[o+1], hist[o+2]], Rd = MMr.v3(me ? l.R : MMr.T3(l.R), dj); for(let a=0;a<3;a++) G[a] += k2*(di[a] - Rd[a]); }
    const g = Math.hypot(G[0],G[1],G[2]); if(g < 1e-300){ nd[i] = di.slice(); continue; } const u = [G[0]/g, G[1]/g, G[2]/g], an = g*h, ca = Math.cos(an), sa = Math.sin(an), ud = u[0]*di[0]+u[1]*di[1]+u[2]*di[2], cx = [u[1]*di[2]-u[2]*di[1], u[2]*di[0]-u[0]*di[2], u[0]*di[1]-u[1]*di[0]];
    nd[i] = [0,1,2].map(a => di[a]*ca + cx[a]*sa + u[a]*ud*(1-ca)); }
  for(const l of W.links){ const o = 3*l.hh; l.hi.set(S.d[l.i], o); l.hj.set(S.d[l.j], o); l.hh = (l.hh+1) % l.nTot; }
  S.d = nd; S.t += h; S.steps++; return S; }
function advance(W, S, dt){ const n = Math.max(1, Math.round(dt/W.opts.h)); for(let k=0;k<n;k++) step(W, S); return S; }
/* ---------- readouts ---------- */
const ballLight = (S, i) => n2(S.psi[i]);
function linkLight(l){ let e = 0; for(const sg of l.segs){ for(let k=0;k<4*sg.n;k++) e += sg.f[k]*sg.f[k] + sg.b[k]*sg.b[k]; } return e; }
/* the books: light in the balls + light in the gaps (should stay 1 after a kick) */
function books(W, S){ let inB = 0, inG = 0; for(let i=0;i<W.N;i++) inB += ballLight(S, i); const per = W.links.map(l => { const e = linkLight(l); inG += e; return e; }); return { balls:inB, gaps:inG, total:inB+inG, perLink:per }; }
/* light along a link, for drawing: M samples of |forward|^2 and |backward|^2 against arc length from ball i */
function linkProfile(W, l, M){ const F = new Float64Array(M), B = new Float64Array(M), h = W.opts.h;
  for(const sg of l.segs){ for(let k=0;k<sg.n;k++){ const idx = ((sg.head - 1 - k) % sg.n + sg.n) % sg.n, o = 4*idx, ef = sg.f[o]**2+sg.f[o+1]**2+sg.f[o+2]**2+sg.f[o+3]**2, eb = sg.b[o]**2+sg.b[o+1]**2+sg.b[o+2]**2+sg.b[o+3]**2;
      const sf = sg.s0 + (k+0.5)*sg.len/sg.n, sb = sg.s0 + sg.len - (k+0.5)*sg.len/sg.n, mf = Math.min(M-1, Math.floor(sf/l.d*M)), mb = Math.min(M-1, Math.floor(sb/l.d*M)); F[mf] += ef; B[mb] += eb; } }
  const sc = M/(l.d/h); for(let k=0;k<M;k++){ F[k] *= sc; B[k] *= sc; } return { F, B }; }
/* each ball's clock phase: the angle of its light spin about its own field (advances at -omega rate_i when left alone); weight = spin across the field */
function clockPhase(S, i){ const d = S.d[i], m = Math.hypot(...d), u = d.map(x => x/m), s = bloch(S.psi[i]), sp = s[0]*u[0]+s[1]*u[1]+s[2]*u[2], t = [s[0]-sp*u[0], s[1]-sp*u[1], s[2]-sp*u[2]];
  const a = Math.abs(u[2]) < 0.9 ? [0,0,1] : [1,0,0], e1 = [a[1]*u[2]-a[2]*u[1], a[2]*u[0]-a[0]*u[2], a[0]*u[1]-a[1]*u[0]], m1 = Math.hypot(...e1), f1 = e1.map(x => x/m1), f2 = [u[1]*f1[2]-u[2]*f1[1], u[2]*f1[0]-u[0]*f1[2], u[0]*f1[1]-u[1]*f1[0]];
  return { phase:Math.atan2(t[0]*f2[0]+t[1]*f2[1]+t[2]*f2[2], t[0]*f1[0]+t[1]*f1[1]+t[2]*f1[2]), weight:Math.hypot(...t) }; }
/* Kuramoto order parameter of the flock's clock phases, weighted by how much each ball is swinging */
function order(W, S){ let cr = 0, ci = 0, w = 0; const ph = []; for(let i=0;i<W.N;i++){ const c = clockPhase(S, i); ph.push(c); cr += c.weight*Math.cos(c.phase); ci += c.weight*Math.sin(c.phase); w += c.weight; } return { r:w > 1e-12 ? Math.hypot(cr, ci)/w : 0, phases:ph }; }
/* how far each ball's field has turned from rest (radians) */
const tilt = (W, S, i) => { const a = S.d[i], b = W.dRest[i], c = (a[0]*b[0]+a[1]*b[1]+a[2]*b[2])/(Math.hypot(...a)*Math.hypot(...b)); return Math.acos(Math.max(-1, Math.min(1, c))); };
/* reference: eigenvectors of the instantaneous matrix H = D + A on the same balls (MM form), with each ball's share */
function modes(W){ const H = MMr.denseH(W, W.dRest), E = MMr.eigh(H.Hr, H.Hi), share = E.vecs.map(v => Array.from({length:W.N}, (_,i) => v[0][2*i]**2 + v[1][2*i]**2 + v[0][2*i+1]**2 + v[1][2*i+1]**2));
  const ord = E.vals.map((x,k) => [Math.abs(x), k]).sort((a,b) => b[0]-a[0]); return { vals:E.vals, share, lead:ord[0][1], margin:ord[1][0]/ord[0][0] }; }
return { NAMES, ARMS, makeWorld, initState, kick, step, advance, ballLight, linkLight, books, linkProfile, clockPhase, order, tilt, modes, bloch, geo, crossAt, applyU };
})();
if(typeof module !== 'undefined') module.exports = FL;
