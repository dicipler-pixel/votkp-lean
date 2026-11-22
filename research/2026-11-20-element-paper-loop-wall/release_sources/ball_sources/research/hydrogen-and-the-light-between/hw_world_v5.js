/* SCRIPT: HW-WORLD-V5 — the ladder of twins.
   Jeromie Beasley. 17 Nov 2026. AI-assisted. The Flock engine (FL-MATH-V2) is unchanged; this builds its world and its rungs.
   Balls A, B (, C) on one line, each breathing on its own schedule a third of a breath apart (r_i(t) as in HW-WORLD-V2/V4). Each ball is layers:
   its level faces sit at (k + ½) r_i(t) from its centre, k = 0 .. K−1, the way the single ball's stack and level shells sit (Balls in One Ball v3,
   the Light at the Hypersurface stack), and each returns Γ_i = tanh(r_i/2), the ball's own peel step, +Γ seen from inside, −Γ from the far side
   (the Flock v2 signs). On the link between two balls the two stacks interleave: A's layers from A's end, B's from B's end; those are the rungs,
   and every rung breathes with its own ball. Where the two stacks meet there is a junction rung whose Γ is the two balls' clock ratio at that
   moment, tanh((r_A − r_B)/2): open when they breathe alike, shut when one is large and the other small. If the outer layers leave an empty
   stretch δ, the junction may also carry the Flock's gap element tanh(κ_g δ) (a switch: both ways are built). The light is one delay line per
   link at speed one, scattered every step at every rung where it is now (HW-WORLD-V4's moving walls). Nothing is drawn that is not a rung. */
(function(root){
"use strict";
const FL = root.FL || require('../sea/fl_math_v2.js'), MM = root.MM || require('../mm/mm_math_v1.js');
const PI = Math.PI, T0 = 8, AMP = 0.35;
function rk(o, k, t){ return Math.max(Math.log(1.05), Math.log(o.z) + (o.breathe ? (o.amp === undefined ? AMP : o.amp)*Math.sin(2*PI*(t - k*T0/3)/T0) : 0)); }
function makeWorld(o){ o = Object.assign({ atoms:3, sep:T0/3, z:3, K:3, gapElement:true, breathe:true, amp:AMP, spins:'opposed', omega:2.0, gamma:0.6, kappa:0.25, kgap:1.0, h:0.01, tilt:0.35 }, o || {});
  const N = o.atoms, r0 = Math.log(o.z), place = x => [Math.cosh(x), Math.sinh(x), 0, 0], balls = []; for(let k=0;k<N;k++) balls.push({ p:place(k*o.sep), arm:k ? 0 : -1, r:r0, rate:1, name:'ABC'[k], x:k*o.sep, k });
  const links = [], mk = (i, j) => { const d = MM.linkDistance(balls[i].p, balls[j].p), R = MM.linkRotation(balls[i].p, balls[j].p), U = MM.su2(R), n = Math.max(1, Math.round(d/o.h));
    links.push({ i, j, d, R, U, Gam:0, marks:[], live:[], segs:[{ s0:0, len:d, n, f:new Float64Array(4*n), b:new Float64Array(4*n), head:0 }], nTot:n, hi:new Float64Array(3*n), hj:new Float64Array(3*n), hh:0, c:0 }); };
  for(let k=0;k<N-1;k++) mk(k, k+1);
  const nbr = Array.from({length:N}, () => []); links.forEach((l, q) => { nbr[l.i].push(q); nbr[l.j].push(q); });
  const W = { N, balls, links, nbr, opts:Object.assign({ push:'off', torque:0, clocks:'equal' }, o), r:[r0], d:null, T:T0, rk:balls.map(() => r0) };
  const a = o.tilt, dA = [Math.sin(a), 0, Math.cos(a)].map(x => x*o.omega/2); W.d = balls.map((b, k) => { if(k === 0) return dA.slice(); const sg = (o.spins === 'opposed' && (k % 2)) ? -1 : 1; let v = dA.slice(); for(let q=0;q<k;q++) v = MM.v3(MM.T3(links[q].R), v); return v.map(x => sg*x); }); W.dRest = W.d.map(v => v.slice());
  W.conn = links.map(l => { const di = W.d[l.i], Rd = MM.v3(l.R, W.d[l.j]); return 2*((di[0]-Rd[0])**2 + (di[1]-Rd[1])**2 + (di[2]-Rd[2])**2); });
  breathe(W, 0); return W; }
/* the rungs of every link from t alone */
function breathe(W, t){ const o = W.opts, N = W.N, K = o.K; for(let k=0;k<N;k++) W.rk[k] = rk(o, k, t);
  W.links.forEach(l => { const ri = W.rk[l.i], rj = W.rk[l.j], Gi = Math.tanh(ri/2), Gj = Math.tanh(rj/2), d = l.d, rungs = []; let si = 0, sj = d;
    for(let k=0;k<K;k++){ const s = (k + 0.5)*ri; if(s < d){ rungs.push({ s, rho:Gi, kind:'layer', ball:l.i, k }); si = Math.max(si, s); } }
    for(let k=0;k<K;k++){ const s = d - (k + 0.5)*rj; if(s > 0){ rungs.push({ s, rho:-Gj, kind:'layer', ball:l.j, k }); sj = Math.min(sj, s); } }
    /* the junction: between the two outermost layers (or at their crossing), the clock ratio of the two breaths; the empty stretch δ and its gap element if asked */
    const delta = sj - si, sm = (si + sj)/2, Gab = Math.tanh((ri - rj)/2); rungs.push({ s:Math.min(d - 1e-9, Math.max(1e-9, sm)), rho:Gab, kind:'junction', delta });
    if(o.gapElement && delta > 0) rungs.push({ s:sm, rho:Math.tanh(o.kgap*delta), kind:'gap', delta });
    rungs.sort((a, b) => a.s - b.s); l.live = rungs; l.marks = rungs; l.delta = delta; l.Gam = Gab;
    /* the composed peel coordinate of the ladder: Smith addition of every rung's |Γ|, Γ ⊕ Γ' = (Γ + Γ')/(1 + ΓΓ') (Two Trees V3; one axis) */
    let G = 0; for(const r of rungs){ const g = Math.abs(r.rho); G = (G + g)/(1 + G*g); } l.Gladder = G; l.ladderLength = 2*Math.atanh(Math.min(G, 1 - 1e-12)); }); }
/* the scattering at every rung where it is now, once per step after the transport (as HW-WORLD-V4) */
function scatter(W, S){ const h = W.opts.h; for(const l of W.links){ const sg = l.segs[0], n = sg.n, d = l.d; for(const m of l.live){ if(Math.abs(m.rho) < 1e-15) continue; const kf = Math.max(0, Math.min(n-1, Math.round(m.s/h - 0.5))), kb = Math.max(0, Math.min(n-1, Math.round((d - m.s)/h - 0.5))), idf = ((sg.head - 1 - kf) % n + n) % n, idb = ((sg.head - 1 - kb) % n + n) % n, of = 4*idf, ob = 4*idb;
      const f = [sg.f[of], sg.f[of+1], sg.f[of+2], sg.f[of+3]], b = [sg.b[ob], sg.b[ob+1], sg.b[ob+2], sg.b[ob+3]], Ub = FL.applyU(l.U, b, false), Uf = FL.applyU(l.U, f, true), rho = m.rho, tau = Math.sqrt(1 - rho*rho);
      for(let c=0;c<4;c++){ sg.f[of+c] = tau*f[c] - rho*Ub[c]; sg.b[ob+c] = rho*Uf[c] + tau*b[c]; } } } }
root.HW = { makeWorld, breathe, scatter, rk, T0, AMP };
})(typeof window !== 'undefined' ? window : globalThis);
if(typeof module !== 'undefined') module.exports = globalThis.HW;
