/* SCRIPT: HW-WORLD-V4 — the walls move with the breath. Each link is one delay line with no fixed marks; every step, the face scattering is applied at the
   wall's present place, s = r_c(t) from each ball, and the gap layer at the middle of the present empty stretch (Two Trees in One Ball, Thm 5.3: the step carries
   the wall with it, the plane at −δ to r − δ). The scatter is the Flock's own, f' = τ f − ρ U b, b' = ρ U† f + τ b, on the forward sample about to cross the wall
   from the inside and the backward sample about to cross it from the outside. V3's breath depth control is kept.
   Hydrogen in a row, breathing. Jeromie Beasley. 17 Nov 2026. AI-assisted.
   The world for the Flock engine (FL-MATH-V2, unchanged), from the drawing and the page: balls on one line, A, B, C, each the Light at the
   Hypersurface ball breathing on its own schedule, r_k(t) = ln z + A sin(2π(t − k·T/3)/T) with the page's A = 0.35 and T = 8 (the first arm's
   period), each ball a third of a breath behind the one before. Everything else follows from r_k(t) alone: the wall's place on the disk
   Γ_k = tanh(r_k/2); the cloud reach r_c,k = r_c0 Γ_k/Γ_0 (the room's rule r_c0 = (s/2)(1 − E)^(1/3), The Space Between); the empty stretch
   δ = s − r_c,A − r_c,B and the gap layer tanh(κ_g δ) (the Flock breakdown); the face between two neighbours returns by their clock ratio,
   Γ_AB = tanh((r_A − r_B)/2), +Γ from A's side and −Γ from B's (the Flock v2 signs): equal breaths, nothing returns. The links are delay lines
   at speed one. In time: the breath wave runs at the light's speed when s = T/3. */
(function(root){
"use strict";
const FL = root.FL || require('../sea/fl_math_v2.js'), MM = root.MM || require('../mm/mm_math_v1.js');
const PI = Math.PI, T0 = 8, AMP = 0.35;
function rk(o, k, t){ return Math.max(Math.log(1.05), Math.log(o.z) + (o.breathe ? (o.amp === undefined ? AMP : o.amp)*Math.sin(2*PI*(t - k*T0/3)/T0) : 0)); }
function makeWorld(o){ o = Object.assign({ atoms:3, sep:T0/3, E:0.5, z:3, spins:'opposed', breathe:true, omega:2.0, gamma:0.6, kappa:0.25, kgap:1.0, h:0.01, tilt:0.35 }, o || {});
  const N = o.atoms, rc0 = (o.sep/2)*Math.cbrt(Math.max(0, 1 - o.E)), r0 = Math.log(o.z), G0 = Math.tanh(r0/2);
  const place = x => [Math.cosh(x), Math.sinh(x), 0, 0], balls = []; for(let k=0;k<N;k++) balls.push({ p:place(k*o.sep), arm:k ? 0 : -1, r:r0, rate:1, name:'ABC'[k], x:k*o.sep, k });
  const links = [], mk = (i, j, marks) => { const d = MM.linkDistance(balls[i].p, balls[j].p), R = MM.linkRotation(balls[i].p, balls[j].p), U = MM.su2(R), cuts = [0].concat(marks.map(m => m.s)).concat([d]), segs = [];
    for(let q=0;q<cuts.length-1;q++){ const len = cuts[q+1] - cuts[q], n = Math.max(1, Math.round(len/o.h)); segs.push({ s0:cuts[q], len, n, f:new Float64Array(4*n), b:new Float64Array(4*n), head:0 }); }
    const nTot = Math.max(1, Math.round(d/o.h)); links.push({ i, j, d, R, U, Gam:0, marks, segs, nTot, hi:new Float64Array(3*nTot), hj:new Float64Array(3*nTot), hh:0, c:0 }); };
  for(let k=0;k<N-1;k++) mk(k, k+1, []); links.forEach(l => { l.live = [{ s:rc0, rho:0, kind:'face' }, { s:o.sep/2, rho:0, kind:'gap', delta:0 }, { s:o.sep - rc0, rho:0, kind:'face' }]; });
  const nbr = Array.from({length:N}, () => []); links.forEach((l, q) => { nbr[l.i].push(q); nbr[l.j].push(q); });
  const W = { N, balls, links, nbr, opts:Object.assign({ push:'off', torque:0, clocks:'equal' }, o), r:[r0], d:null, rc0, G0, T:T0, A:AMP, rc:balls.map(() => rc0), rk:balls.map(() => r0), delta:[], fill:1 - o.E, connects:(1 - o.E) >= 1/3 };
  const a = o.tilt, dA = [Math.sin(a), 0, Math.cos(a)].map(x => x*o.omega/2); W.d = balls.map((b, k) => { if(k === 0) return dA.slice(); const sg = (o.spins === 'opposed' && (k % 2)) ? -1 : 1; let v = dA.slice(); for(let q=0;q<k;q++) v = MM.v3(MM.T3(links[q].R), v); return v.map(x => sg*x); }); W.dRest = W.d.map(v => v.slice());
  W.conn = links.map(l => { const di = W.d[l.i], Rd = MM.v3(l.R, W.d[l.j]); return 2*((di[0]-Rd[0])**2 + (di[1]-Rd[1])**2 + (di[2]-Rd[2])**2); });
  breathe(W, 0); return W; }
/* one breath step: from t alone, every ball's r, wall, cloud, and every link's faces and gap */
function breathe(W, t){ const o = W.opts, N = W.N; for(let k=0;k<N;k++){ W.rk[k] = rk(o, k, t); W.rc[k] = W.rc0*Math.tanh(W.rk[k]/2)/W.G0; }
  W.links.forEach((l, q) => { const G = Math.tanh((W.rk[l.i] - W.rk[l.j])/2), delta = Math.max(0, o.sep - W.rc[l.i] - W.rc[l.j]), m = l.live; m[0].rho = G; m[0].s = W.rc[l.i]; m[2].rho = -G; m[2].s = o.sep - W.rc[l.j]; m[1].rho = Math.tanh(o.kgap*delta); m[1].delta = delta; m[1].s = W.rc[l.i] + delta/2; W.delta[q] = delta; l.Gam = G; l.passGap = 1 - m[1].rho**2; l.passFace = 1 - G*G; l.marks = m; }); }
/* the scattering at the walls where they are now: once per step, after the transport */
function scatter(W, S){ const h = W.opts.h; for(const l of W.links){ const sg = l.segs[0], n = sg.n, d = l.d; for(const m of l.live){ if(Math.abs(m.rho) < 1e-15) continue; const kf = Math.max(0, Math.min(n-1, Math.round(m.s/h - 0.5))), kb = Math.max(0, Math.min(n-1, Math.round((d - m.s)/h - 0.5))), idf = ((sg.head - 1 - kf) % n + n) % n, idb = ((sg.head - 1 - kb) % n + n) % n, of = 4*idf, ob = 4*idb;
      const f = [sg.f[of], sg.f[of+1], sg.f[of+2], sg.f[of+3]], b = [sg.b[ob], sg.b[ob+1], sg.b[ob+2], sg.b[ob+3]], Ub = FL.applyU(l.U, b, false), Uf = FL.applyU(l.U, f, true), rho = m.rho, tau = Math.sqrt(1 - rho*rho);
      for(let c=0;c<4;c++){ sg.f[of+c] = tau*f[c] - rho*Ub[c]; sg.b[ob+c] = rho*Uf[c] + tau*b[c]; } } } }
root.HW = { makeWorld, breathe, scatter, rk, T0, AMP };
})(typeof window !== 'undefined' ? window : globalThis);
if(typeof module !== 'undefined') module.exports = globalThis.HW;
