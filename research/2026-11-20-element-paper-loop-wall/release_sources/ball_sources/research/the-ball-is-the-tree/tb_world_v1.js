/* SCRIPT: TB-WORLD-V1 — the ball is the tree. Jeromie Beasley. 17 Nov 2026. AI-assisted.
   One tree of cells, generated from the root by the six steps ±I ±J ±K to depth D (1 + 6 + 30 + 150 ...). Every cell c has its own clock, its own step
   r_c(t) = ln z + A sin(2π(t − φ_c)/T): rate is weight (Dirac Time §9.4), no geometry sets it from outside. A cell's face toward a neighbour sits at
   r_c/2 from its centre (the single ball's faces, Two Trees in One Ball) and returns the cell's own peel step Γ_c = tanh(r_c/2) (VOTKP), seen +Γ from
   its own side and −Γ from the far side. On the edge between parent p and child c the two faces interleave with the junction between them whose Γ is
   the two clocks' ratio tanh((r_p − r_c)/2): a rung is a twin, two faces and the stretch between. The leaves of the tree are the electrons, the ground:
   with leaves = 'ground' a leaf's face returns |Γ| = 1 (total reflection, the rim) and keeps the record K = ∫ 2|a⁺|² dt of what pushed on it (his push with
   R = 1 and nothing beyond); with leaves = 'open' a leaf is an ordinary cell and the light enters it. Both ways are built. The light is the Flock engine's
   (FL-MATH-V2, unchanged): one delay line per edge at speed one, scattered every step at every rung where it is now. Each cell's twin is the cell whose word
   has every sign flipped (the mirror tree); the light in a cell against the light in its twin is the two paths tracked. The weight of a path root→leaf is
   its total step Σ r; per layer it is one step. */
(function(root){
"use strict";
const FL = root.FL || require('../sea/fl_math_v2.js'), MM = root.MM || require('../mm/mm_math_v1.js');
const PI = Math.PI, T0 = 8, AMP = 0.35, AX = MM.AXES;
const mv = (B, p) => B.map(r => r[0]*p[0] + r[1]*p[1] + r[2]*p[2] + r[3]*p[3]);
function rc(o, c, t){ return Math.max(Math.log(1.05), Math.log(o.z) + (o.breathe ? (o.amp === undefined ? AMP : o.amp)*Math.sin(2*PI*(t - c.phi)/T0) : 0)); }
function makeWorld(o){ o = Object.assign({ depth:2, z:3, leaves:'ground', gapElement:true, breathe:true, amp:AMP, twinPhase:'own', omega:2.0, gamma:0.6, kappa:0.25, kgap:1.0, h:0.01, tilt:0.35 }, o || {});
  const r0 = Math.log(o.z), cells = [{ word:[], p:[1,0,0,0], parent:-1, depth:0, gen:-1, name:'O', k:0 }], byWord = new Map([['', 0]]);
  for(let d=1; d<=o.depth; d++){ const level = cells.filter(c => c.depth === d-1); for(const par of level){ for(let g=0; g<6; g++){ if(par.gen >= 0 && (par.gen ^ 1) === g) continue; /* no step back along the way it came */
      const word = par.word.concat([g]), B = MM.boost(AX[g], r0), p = mv(B, par.p), k = cells.length; cells.push({ word, p, parent:par.k, depth:d, gen:g, name:'O' + word.map(x => 'IiJjKk'[x]).join(''), k }); byWord.set(word.join(','), k); } } }
  const N = cells.length; cells.forEach(c => { const tw = c.word.map(x => x ^ 1); c.twin = byWord.get(tw.join(',')); c.leaf = c.depth === o.depth; const lev = cells.filter(q => q.depth === c.depth), idx = lev.indexOf(c);
    /* each cell its own schedule: a third of a breath per depth, spread across its level by its place; 'same' gives a cell and its twin one schedule */
    c.phi = T0*(c.depth/3 + (o.twinPhase === 'same' ? (Math.min(idx, lev.indexOf(cells[c.twin])))/(3*lev.length) : idx/(3*lev.length))); c.r = r0; c.rate = 1; c.arm = c.gen; });
  const balls = cells, links = [];
  for(const c of cells){ if(c.parent < 0) continue; const par = cells[c.parent], d = MM.linkDistance(par.p, c.p), R = MM.linkRotation(par.p, c.p), U = MM.su2(R), n = Math.max(1, Math.round(d/o.h));
    links.push({ i:par.k, j:c.k, d, R, U, Gam:0, marks:[], live:[], segs:[{ s0:0, len:d, n, f:new Float64Array(4*n), b:new Float64Array(4*n), head:0 }], nTot:n, hi:new Float64Array(3*n), hj:new Float64Array(3*n), hh:0, c:0, K:0, leaf:c.leaf }); }
  const nbr = Array.from({length:N}, () => []); links.forEach((l, q) => { nbr[l.i].push(q); nbr[l.j].push(q); });
  const W = { N, balls, cells, links, nbr, opts:Object.assign({ push:'off', torque:0, clocks:'equal' }, o), r:[r0], d:null, T:T0, rk:cells.map(() => r0) };
  const a = o.tilt, dA = [Math.sin(a), 0, Math.cos(a)].map(x => x*o.omega/2); W.d = cells.map(c => { let v = dA.slice(); let q = c; const chain = []; while(q.parent >= 0){ chain.unshift(q); q = cells[q.parent]; } for(const cc of chain){ const l = links[cc.k - 1]; v = MM.v3(MM.T3(l.R), v); } return v; }); W.dRest = W.d.map(v => v.slice());
  W.conn = links.map(l => { const di = W.d[l.i], Rd = MM.v3(l.R, W.d[l.j]); return 2*((di[0]-Rd[0])**2 + (di[1]-Rd[1])**2 + (di[2]-Rd[2])**2); });
  breathe(W, 0); return W; }
function breathe(W, t){ const o = W.opts; W.cells.forEach((c, k) => { W.rk[k] = rc(o, c, t); });
  W.links.forEach(l => { const rp = W.rk[l.i], rch = W.rk[l.j], Gp = Math.tanh(rp/2), Gc = Math.tanh(rch/2), d = l.d, ground = l.leaf && o.leaves === 'ground', rungs = [];
    const sp = Math.min(d - 1e-9, rp/2), sc = Math.max(1e-9, d - rch/2);
    rungs.push({ s:sp, rho:Gp, kind:'face', cell:l.i }); /* a ground leaf has no inside: its wall is the end of the step (the last sample before the port), not a face at r_c/2 */
    rungs.push(ground ? { s:d - 1.5*o.h, rho:-1, kind:'ground', cell:l.j } : { s:sc, rho:-Gc, kind:'face', cell:l.j });
    const delta = sc - sp, sm = (sp + sc)/2, Gpc = Math.tanh((rp - rch)/2); rungs.push({ s:Math.min(d - 1e-9, Math.max(1e-9, sm)), rho:Gpc, kind:'junction', delta });
    if(o.gapElement && delta > 0) rungs.push({ s:sm, rho:Math.tanh(o.kgap*delta), kind:'gap', delta });
    rungs.sort((a, b) => a.s - b.s); l.live = rungs; l.marks = rungs; l.delta = delta; l.Gam = Gpc; let G = 0; for(const r of rungs){ const g = Math.min(1 - 1e-12, Math.abs(r.rho)); G = (G + g)/(1 + G*g); } l.Gladder = G; }); }
/* scatter at every rung where it is now (HW-WORLD-V4); at a ground wall record the push 2|a⁺|² of the stream arriving from the inside */
function scatter(W, S){ const h = W.opts.h; for(const l of W.links){ const sg = l.segs[0], n = sg.n, d = l.d; let prev = -1; for(const m of l.live){ if(Math.abs(m.rho) < 1e-15) continue; let kf = Math.max(0, Math.min(n-1, Math.round(m.s/h - 0.5))); if(kf <= prev) kf = Math.min(n-1, prev + 1); prev = kf; /* two rungs never share a sample: the later one takes the next (two scatterers in one sample do not compose) */ const kb = n - 1 - kf, idf = ((sg.head - 1 - kf) % n + n) % n, idb = ((sg.head - 1 - kb) % n + n) % n, of = 4*idf, ob = 4*idb;
      const f = [sg.f[of], sg.f[of+1], sg.f[of+2], sg.f[of+3]], b = [sg.b[ob], sg.b[ob+1], sg.b[ob+2], sg.b[ob+3]];
      if(m.kind === 'ground'){ l.K += 2*(f[0]*f[0] + f[1]*f[1] + f[2]*f[2] + f[3]*f[3])*h; }
      const Ub = FL.applyU(l.U, b, false), Uf = FL.applyU(l.U, f, true), rho = m.rho, tau = Math.sqrt(Math.max(0, 1 - rho*rho));
      for(let c=0;c<4;c++){ sg.f[of+c] = tau*f[c] - rho*Ub[c]; sg.b[ob+c] = rho*Uf[c] + tau*b[c]; } } } }
/* readouts: light by depth, twin differences, the weight of every path, the record */
function levels(W, S){ const L = Array.from({length:W.opts.depth + 1}, () => 0); W.cells.forEach((c, k) => { L[c.depth] += FL.ballLight(S, k); }); return L; }
function twins(W, S){ let dmax = 0, sum = 0, n = 0; W.cells.forEach((c, k) => { if(c.twin === undefined || c.twin < k) return; const a = FL.ballLight(S, k), b = FL.ballLight(S, c.twin), dd = Math.abs(a - b); dmax = Math.max(dmax, dd); sum += dd; n++; }); return { dmax, mean:n ? sum/n : 0, pairs:n }; }
function weights(W){ const out = []; W.cells.forEach(c => { if(!c.leaf) return; let q = c, sum = 0, steps = 0; while(q.parent >= 0){ sum += W.rk[q.parent]; steps++; q = W.cells[q.parent]; } out.push({ leaf:c.k, sum, steps, perLayer:sum/steps }); }); return out; }
function record(W){ let K = 0; for(const l of W.links) K += l.K; return K; }
root.TB = { makeWorld, breathe, scatter, rc, levels, twins, weights, record, T0, AMP };
})(typeof window !== 'undefined' ? window : globalThis);
if(typeof module !== 'undefined') module.exports = globalThis.TB;
