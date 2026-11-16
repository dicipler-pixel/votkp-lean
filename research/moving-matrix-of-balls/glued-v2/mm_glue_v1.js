/* SCRIPT: MM-GLUE-V1
   The moving matrix on the glued balls of Light at the Hypersurface. Jeromie Beasley. 15 Nov 2026. AI-assisted.
   Balls = the cells of the tree (centre, its six neighbours, their thirty neighbours: 37 balls), each at its cell centre g·O.
   Links = the faces two cells share: centre–k across face N0[k]; k–km across face gens[k]·N0[m]. Each face sits halfway along its step.
   One matrix H = D + A (MM-MATH-V1) moves light, sea and balls. The faces breathe on the page clock: the links are rebuilt from the
   live geometry each frame, and the energy the breathing puts in is recorded as work, so the books still close. Pure functions; needs LH and MM. */
var MMG = (function(){
"use strict";
const LHr = (typeof LH !== 'undefined') ? LH : require('../surprise/src/lh_math.js');
const MMr = (typeof MM !== 'undefined') ? MM : require('../mm/mm_math_v1.js');
/* the cells: words '' , [k], [k,m] with m != k^1 */
function cells(){ const C = [{ word:[], parent:-1, via:-1 }]; for(let k=0;k<6;k++){ C.push({ word:[k], parent:0, via:k }); }
  for(let k=0;k<6;k++) for(let m=0;m<6;m++){ if(m === (k^1)) continue; C.push({ word:[k,m], parent:1+k, via:m }); } return C; }
const CELLS = cells();
/* geometry of every cell and every shared face at one clock value */
function geometry(S){ const g = CELLS.map(c => c.word.reduce((G,k) => LHr.mm(G, S.gens[k]), LHr.I4()));
  const p = g.map(G => LHr.mv(G, LHr.O4));
  const faces = CELLS.map((c,i) => i === 0 ? null : LHr.mv(g[c.parent], S.N0[c.via]));
  return { g, p, faces }; }
function linkOf(p, i, j, c0){ const d = LHr.hdist(p[i], p[j]), R = MMr.linkRotation(p[i], p[j]); return { i, j, d, Gam:Math.tanh(d/2), c:c0/Math.cosh(d/2), R, U:MMr.su2(R) }; }
/* the world: same fields as MM.makeWorld, so every MM function runs on it unchanged */
function makeWorld(S, opts){ opts = Object.assign({ c0:0.5, omega:2.0, kappa:0.25, seaBack:true }, opts||{});
  const G = geometry(S), N = CELLS.length, links = [];
  for(let i=1;i<N;i++) links.push(linkOf(G.p, CELLS[i].parent, i, opts.c0));
  const nbr = Array.from({length:N}, () => []); links.forEach((l,k) => { nbr[l.i].push(k); nbr[l.j].push(k); });
  /* the glued rest: the centre ball up, each child its parent carried across the shared face (d_j = R^T d_i), so every face holds zero */
  const d = Array(N); d[0] = [0, 0, opts.omega/2];
  links.forEach(l => { const R = l.R, a = d[l.i]; d[l.j] = [0,1,2].map(r => R[0][r]*a[0] + R[1][r]*a[1] + R[2][r]*a[2]); });
  return { N, balls:G.p.map(p => ({ p })), links, tris:[], nbr, d, opts, geo:G, cells:CELLS }; }
/* the faces move: rebuild positions and links from the live geometry; the state (light, sea, ball directions) is kept */
function relink(W, S){ const G = geometry(S); W.geo = G; W.balls = G.p.map(p => ({ p }));
  W.links.forEach((l, k) => { const n = linkOf(G.p, l.i, l.j, W.opts.c0); l.d = n.d; l.Gam = n.Gam; l.c = n.c; l.R = n.R; l.U = n.U; }); }
/* step the matrix on one clock: geometry fixed within a frame; the energy jump at each relink is the work the breathing faces do */
function advance(W, St, S, dtau, hmax){ const w = St.work||0, n = Math.max(1, Math.ceil(dtau/(hmax||0.01))), h = dtau/n; for(let k=0;k<n;k++) St = MMr.rk4(W, St, h);
  const E0 = MMr.energies(W, St).E; relink(W, S); const E1 = MMr.energies(W, St).E; St.work = w + (E1 - E0); return St; }
return { CELLS, cells, geometry, makeWorld, relink, advance };
})();
if(typeof module !== 'undefined') module.exports = MMG;
