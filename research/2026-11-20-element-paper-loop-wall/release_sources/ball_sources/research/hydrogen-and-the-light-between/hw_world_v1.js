/* SCRIPT: HW-WORLD-V1
   Hydrogen, the space between, and the light between. Jeromie Beasley. 17 Nov 2026. AI-assisted.
   The world for the Flock engine (FL-MATH-V2, unchanged), built from the drawing: each ball a hydrogen atom standing apart from the next;
   the separation s is the room; each atom fills its room out to r_c = (s/2)(1 − E)^(1/3), E the space between (The Space Between, §2);
   the stretch the clouds do not cover, δ = s − 2 r_c, is the gap, and light passes it with the gap layer's sech²(κ_g δ) (the Flock
   breakdown's gap element); at each atom's wall the face returns Γ² with Γ = tanh(ln z / 2), z the clock ratio between the two atoms
   (1 for hydrogen next to hydrogen: nothing returns); parallel or opposed electrons set the second atom's field along or against the first's,
   and the connection energy of the link is ‖D_i − U D_j U†‖² (Non-Normality Is Connection Energy). The links are delay lines: light takes
   the time the distance needs. Nothing else is in it. */
(function(root){
"use strict";
const FL = root.FL || require('../sea/fl_math_v2.js'), MM = root.MM || require('../mm/mm_math_v1.js');
function makeWorld(o){ o = Object.assign({ atoms:2, sep:3.0, E:0.667, z:1, spins:'opposed', omega:2.0, gamma:0.6, kappa:0.25, kgap:1.0, h:0.01, tilt:0.35 }, o || {});
  const N = o.atoms, rc = (o.sep/2)*Math.cbrt(Math.max(0, 1 - o.E)), delta = Math.max(0, o.sep - 2*rc), rr = Math.log(o.z), Gam = Math.tanh(rr/2);
  /* the atoms on one line through the centre: A at 0, B at +s, C at -s (hyperboloid points along the first axis, so the Flock's link geometry is exact) */
  const place = x => [Math.cosh(x), Math.sinh(x), 0, 0], balls = [{ p:place(0), arm:-1, r:0, rate:1, name:'A', x:0 }, { p:place(o.sep), arm:0, r:rr, rate:1/o.z, name:'B', x:o.sep }];
  if(N > 2) balls.push({ p:place(-o.sep), arm:1, r:rr, rate:1/o.z, name:'C', x:-o.sep });
  const links = [], mk = (i, j, marks) => { const d = MM.linkDistance(balls[i].p, balls[j].p), R = MM.linkRotation(balls[i].p, balls[j].p), U = MM.su2(R), cuts = [0].concat(marks.map(m => m.s)).concat([d]), segs = [];
    for(let k=0;k<cuts.length-1;k++){ const len = cuts[k+1] - cuts[k], n = Math.max(1, Math.round(len/o.h)); segs.push({ s0:cuts[k], len, n, f:new Float64Array(4*n), b:new Float64Array(4*n), head:0 }); }
    const nTot = Math.max(1, Math.round(d/o.h)); links.push({ i, j, d, R, U, Gam, marks, segs, nTot, hi:new Float64Array(3*nTot), hj:new Float64Array(3*nTot), hh:0, c:0, delta, rc }); };
  /* marks along A -> B: A's wall at its cloud edge r_c (face +Γ), the gap layer in the middle of the empty stretch, B's wall at s - r_c (face -Γ, the Flock v2 sign from the other side) */
  for(let k=1;k<N;k++){ const marks = [{ s:rc, rho:Gam, kind:'face' }]; if(delta > 0) marks.push({ s:o.sep/2, rho:Math.tanh(o.kgap*delta), kind:'gap', delta }); marks.push({ s:o.sep - rc, rho:-Gam, kind:'face' }); mk(0, k, marks); }
  const nbr = Array.from({length:N}, () => []); links.forEach((l, k) => { nbr[l.i].push(k); nbr[l.j].push(k); });
  const W = { N, balls, links, nbr, opts:Object.assign({ push:'off', torque:0, clocks:'z' }, o), r:[rr], d:null, rc, delta };
  /* fields: |d_i| = ω rate_i / 2 (the Flock's rule); A along its tilt; the others along (parallel) or against (opposed) A, carried across the link by R */
  const a = o.tilt, dA = [Math.sin(a), 0, Math.cos(a)].map(x => x*o.omega/2); W.d = balls.map((b, i) => { if(i === 0) return dA.slice(); const Rd = MM.v3(MM.T3(links[i-1].R), dA), sg = o.spins === 'opposed' ? -1 : 1; return Rd.map(x => sg*x*b.rate); }); W.dRest = W.d.map(v => v.slice());
  /* connection energy per link: ||D_i - U D_j U^dag||^2 = 2 |d_i - R d_j|^2 */
  W.conn = links.map(l => { const di = W.d[l.i], Rd = MM.v3(l.R, W.d[l.j]); return 2*((di[0]-Rd[0])**2 + (di[1]-Rd[1])**2 + (di[2]-Rd[2])**2); });
  links.forEach(l => { let t = 1; l.marks.forEach(m => t *= Math.sqrt(1 - m.rho*m.rho)); l.c = 0.5*t; });
  /* the filling of the gap: the volume share the atom fills, 1 − E; connects past Bruggeman's third (E below 2/3) */
  W.fill = 1 - o.E; W.connects = W.fill >= 1/3; W.passGap = delta > 0 ? 1 - Math.tanh(o.kgap*delta)**2 : 1; W.passFace = 1 - Gam*Gam;
  return W; }
root.HW = { makeWorld };
})(typeof window !== 'undefined' ? window : globalThis);
if(typeof module !== 'undefined') module.exports = globalThis.HW;
