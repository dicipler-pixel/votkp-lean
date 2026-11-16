/* SCRIPT: SR-MATH-V1
   The Series of the Ball: the moving matrix on the ball ends. Jeromie Beasley. 15 Nov 2026. AI-assisted.
   Every face of the ball is the end of a ball (a sphere meeting the rim at right angles). The generators carry each end into the next:
   inside the end of word w sit the ends w·m (m ≠ the letter back), the same kind of ball, smaller. Series: 6 → +30 → +150 ends.
   Nodes = ball ends. Two ends are joined when they bound the same cell; the strength is the step transmission of the distance
   between them, c0·sech(δ): δ = 0 where the ends cross or kiss, δ = arccosh g where they stand apart (g = sinh h_a sinh h_b, the
   pair invariant; opposite ends of one arm stand apart by the full step r). Pure functions; needs LH (Surprise maths) and MM (MM-MATH-V1). */
var SR = (function(){
"use strict";
const LHr = (typeof LH !== 'undefined') ? LH : require('../surprise/src/lh_math.js');
const MMr = (typeof MM !== 'undefined') ? MM : require('../mm/mm_math_v1.js');
const AXU = k => LHr.letterDir(k);
/* the ends of the series up to level L: word w (non-empty, reduced); its cell is the word w without its last letter */
function ends(L){ const E = []; const rec = (w, lev) => { for(let m=0;m<6;m++){ if(w.length && m === (w[w.length-1]^1)) continue; const v = w.concat(m); E.push({ word:v, last:m, level:lev, cell:w.join(',') }); if(lev < L) rec(v, lev+1); } };
  rec([], 1); E.sort((a,b) => a.level - b.level); return E; }
/* cells whose six ends are all present (words of length ≤ L−1), each with its six ends: the entry end and its children */
function cellsOf(E, L){ const idx = new Map(E.map((e,i) => [e.word.join(','), i])), C = [];
  const rec = w => { if(w.length > L-1) return; const six = []; if(w.length) six.push(idx.get(w.join(',')));
    for(let m=0;m<6;m++){ if(w.length && m === (w[w.length-1]^1)) continue; six.push(idx.get(w.concat(m).join(','))); }
    C.push({ word:w, ends:six }); for(let m=0;m<6;m++){ if(w.length && m === (w[w.length-1]^1)) continue; rec(w.concat(m)); } };
  rec([]); return C; }
/* live geometry at one clock value: the cell matrix g of each end's cell, the end's plane N (outward from its cell), and its foot point */
function geometry(S, E){ const gc = new Map(); const gOf = w => { const k = w.join(','); let g = gc.get(k); if(g) return g; g = w.reduce((G,m) => LHr.mm(G, S.gens[m]), LHr.I4()); gc.set(k, g); return g; };
  return E.map(e => { const w = e.word.slice(0,-1), g = gOf(w), k = e.last, h = S.h[k>>1], u = AXU(k);
    return { g, N:LHr.mv(g, S.N0[k]), foot:LHr.mv(g, [Math.cosh(h), Math.sinh(h)*u[0], Math.sinh(h)*u[1], Math.sinh(h)*u[2]]), h, k }; }); }
/* distance between two ends of the same cell (in that cell's own frame, so it is exact at any depth) */
function pairDelta(S, ka, kb){ const a = ka>>1, b = kb>>1; if(a === b) return S.r[a];               /* opposite ends of one arm: apart by the step */
  const g = Math.sinh(S.h[a])*Math.sinh(S.h[b]); return g <= 1 ? 0 : Math.acosh(g); }            /* crossing or kissing: 0; apart: arccosh g */
/* the letter of each of a cell's six ends, as seen from that cell (the entry end is the inverse of the cell's last letter) */
function cellLetters(c, E){ return c.ends.map((ei, n) => (c.word.length && n === 0) ? (c.word[c.word.length-1]^1) : E[ei].last); }
function linksOf(S, E, C, geo, c0){ const seen = new Map(), L = [];
  for(const c of C){ const lt = cellLetters(c, E); for(let a=0;a<6;a++) for(let b=a+1;b<6;b++){ const i = c.ends[a], j = c.ends[b], key = i < j ? i+','+j : j+','+i; if(seen.has(key)) continue;
    const del = pairDelta(S, lt[a], lt[b]), d = LHr.hdist(geo[i].foot, geo[j].foot), R = MMr.linkRotation(geo[i].foot, geo[j].foot);
    const l = { i, j, d, del, Gam:Math.tanh(del/2), c:c0/Math.cosh(del), R, U:MMr.su2(R), la:lt[a], lb:lt[b], cellw:c.word }; seen.set(key, L.length); L.push(l); } }
  return L; }
function makeWorld(S, L, opts){ opts = Object.assign({ c0:0.5, omega:2.0, kappa:0.25, seaBack:true }, opts||{});
  const E = ends(L), C = cellsOf(E, L), geo = geometry(S, E), links = linksOf(S, E, C, geo, opts.c0), N = E.length;
  const nbr = Array.from({length:N}, () => []); links.forEach((l,k) => { nbr[l.i].push(k); nbr[l.j].push(k); });
  /* each end's field starts along its own outward normal (the direction its ball comes in from) */
  const d = geo.map(G => { const n = [G.N[1], G.N[2], G.N[3]], m = Math.hypot(...n); return n.map(x => x/m*opts.omega/2); });
  /* triangles: three ends that are pairwise joined */
  const has = new Set(links.map(l => l.i+','+l.j)), tris = []; const J = (a,b) => has.has(Math.min(a,b)+','+Math.max(a,b));
  for(const c of C){ const s = c.ends; for(let a=0;a<6;a++) for(let b=a+1;b<6;b++) for(let q=b+1;q<6;q++) if(J(s[a],s[b]) && J(s[b],s[q]) && J(s[a],s[q])) tris.push([s[a],s[b],s[q]]); }
  return { N, balls:geo.map(G => ({ p:G.foot })), links, tris, nbr, d, opts, ends:E, cells:C, geo, L }; }
function relink(W, S){ const geo = geometry(S, W.ends); W.geo = geo; W.balls = geo.map(G => ({ p:G.foot }));
  W.links.forEach(l => { const del = pairDelta(S, l.la, l.lb), R = MMr.linkRotation(geo[l.i].foot, geo[l.j].foot); l.del = del; l.Gam = Math.tanh(del/2); l.c = W.opts.c0/Math.cosh(del); l.d = LHr.hdist(geo[l.i].foot, geo[l.j].foot); l.R = R; l.U = MMr.su2(R); }); }
function advance(W, St, S, dtau, hmax){ const w = St.work||0, n = Math.max(1, Math.ceil(dtau/(hmax||0.02))), h = dtau/n; for(let k=0;k<n;k++) St = MMr.rk4(W, St, h);
  const E0 = MMr.energies(W, St).E; relink(W, S); const E1 = MMr.energies(W, St).E; St.work = w + (E1 - E0); return St; }
/* the matrix's eigenvectors at the present geometry: energies and, per end, the weight |v_i|^2 and phase of the larger component */
function modes(W, d){ const H = MMr.denseH(W, d), Ev = MMr.eigh(H.Hr, H.Hi); return Ev; }
return { ends, cellsOf, geometry, pairDelta, cellLetters, linksOf, makeWorld, relink, advance, modes };
})();
if(typeof module !== 'undefined') module.exports = SR;
