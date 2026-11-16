/* SCRIPT: TB-MATH-V1
   Three Balls on the Field: the matrix between three whole balls. Jeromie Beasley. 15 Nov 2026. AI-assisted.
   Ball A at the centre of the field, ball B one peel step out along A's I arm, ball C one peel step out along A's J arm.
   The cap seen inside A on the I arm is B's end pushing in (and A's end inside B); the same for C on the J arm.
   Links: A–B (step r_I), A–C (step r_J), B–C (the third side of the right triangle, cosh d = cosh r_I cosh r_J).
   Each link is a VOTKP peel step: Γ = tanh(d/2), strength c0·sech(d/2) = c0·sqrt(1 − Γ²), with the ball's transport on it.
   One matrix H = D + A (MM-MATH-V1) moves the light, the electron sea and each ball's field. Pure functions; needs MM. */
var TB = (function(){
"use strict";
const MMr = (typeof MM !== 'undefined') ? MM : require('../mm/mm_math_v1.js');
const PAIRS = [[0,1],[0,2],[1,2]], NAMES = ['A','B','C'];
const pts = r => [[1,0,0,0], [Math.cosh(r[0]), Math.sinh(r[0]), 0, 0], [Math.cosh(r[1]), 0, Math.sinh(r[1]), 0]];
function linkOf(p, i, j, c0){ const d = MMr.linkDistance(p[i], p[j]), R = MMr.linkRotation(p[i], p[j]); return { i, j, d, Gam:Math.tanh(d/2), c:c0/Math.cosh(d/2), R, U:MMr.su2(R) }; }
function makeWorld(r, opts){ opts = Object.assign({ c0:0.5, omega:2.0, kappa:0.25, seaBack:true }, opts||{});
  const p = pts(r), links = PAIRS.map(([i,j]) => linkOf(p, i, j, opts.c0)), nbr = [[0,1],[0,2],[1,2]];
  const W = { N:3, balls:p.map(q => ({ p:q })), links, tris:[[0,1,2]], nbr, d:null, opts };
  /* rest of the faces: start a little off the symmetric position (fixed seed) and descend */
  let seed = 11; const rnd = () => (seed = (seed*16807) % 2147483647)/2147483647 - 0.5;
  W.d = [0,1,2].map(() => { const v = [0.2*rnd(), 0.2*rnd(), 1 + 0.2*rnd()], m = Math.hypot(...v); return v.map(x => x/m*opts.omega/2); });
  const R = MMr.restState(W, { iters:60000, eta:0.08, withSea:false, tol:1e-11 }); W.d = R.d; W.restResidual = R.residual; return W; }
function relink(W, r){ const p = pts(r); W.balls = p.map(q => ({ p:q })); W.links.forEach(l => { const n = linkOf(p, l.i, l.j, W.opts.c0); l.d = n.d; l.Gam = n.Gam; l.c = n.c; l.R = n.R; l.U = n.U; }); }
function advance(W, St, r, dtau, hmax){ const w = St.work||0, n = Math.max(1, Math.ceil(dtau/(hmax||0.01))), h = dtau/n; for(let k=0;k<n;k++) St = MMr.rk4(W, St, h);
  const E0 = MMr.energies(W, St).E; relink(W, r); const E1 = MMr.energies(W, St).E; St.work = w + (E1 - E0); return St; }
/* eigenvectors of the three-ball matrix, each with its share on A, B, C; the leading one is the largest eigenvalue; margin = |λ2/λ1| */
function modes(W, d){ const H = MMr.denseH(W, d), E = MMr.eigh(H.Hr, H.Hi), share = E.vecs.map(v => [0,1,2].map(i => v[0][2*i]**2 + v[1][2*i]**2 + v[0][2*i+1]**2 + v[1][2*i+1]**2));
  const order = E.vals.map((x,k) => [Math.abs(x), k]).sort((a,b) => b[0]-a[0]); return { vals:E.vals, vecs:E.vecs, share, lead:order[0][1], margin:order[1][0]/order[0][0] }; }
/* the loop A → B → C → A: turn of a carried frame, the triangle's area, and the Thomas turn 2 arctan(Γ_I Γ_J) of the two steps */
function loop(W, r){ const h = MMr.triangleHolonomy(W, [0,1,2]); return { ang:h.ang, area:h.area, thomas:2*Math.atan(Math.tanh(r[0]/2)*Math.tanh(r[1]/2)) }; }
return { PAIRS, NAMES, pts, makeWorld, relink, advance, modes, loop };
})();
if(typeof module !== 'undefined') module.exports = TB;
