/* SCRIPT: HB-WORLD-V1 — two hydrogen atoms in a ball, and the work the walls do. Jeromie Beasley. 17 Nov 2026. AI-assisted.
   The minimum model. Two cells A and B a distance s apart, each on its own clock r(t) = ln z + A sin(2π(t − φ)/T), and a container C around them: a third cell
   whose face is the rim at distance R from the pair's centre, on its own clock r_C(t) when it breathes. Three stretches: A–B between the atoms, A–C and B–C between
   each atom and the rim. On every stretch the rung is the twin: the cell's face at r/2 from its centre returning its own Γ = tanh(r/2), the far cell's face returning
   −Γ, the junction between them returning the clock ratio tanh((r_i − r_j)/2), and the gap element on an empty stretch (switch). The container closed: its face is
   ground, |Γ| = 1, returns everything and keeps the record K = ∫ 2|a⁺|² dt. Open: its face returns its own Γ_C and what passes is in cell C, the outside, counted.
   The one new rule, switchable: a moving face does work on the light it returns. A wall moving toward the light it reflects returns more than it took, moving away
   less, by the mirror's Doppler factor D = (1 + v)/(1 − v) in energy, v the wall's speed toward that stream (speed of light one) — recognised, not derived here.
   The work W, the energy each moving wall adds to the pair it scatters, is a third line of the books: cells + stretches − W = 1. The Flock engine (FL-MATH-V2) is unchanged. */
(function(root){
"use strict";
const FL = root.FL || require('../sea/fl_math_v2.js'), MM = root.MM || require('../mm/mm_math_v1.js');
const PI = Math.PI, T0 = 8, AMP = 0.35;
function rOf(o, phi, amp, t){ return Math.max(Math.log(1.05), Math.log(o.z) + amp*Math.sin(2*PI*(t - phi)/T0)); }
function rDot(o, phi, amp, t){ const r = Math.log(o.z) + amp*Math.sin(2*PI*(t - phi)/T0); return r > Math.log(1.05) ? amp*(2*PI/T0)*Math.cos(2*PI*(t - phi)/T0) : 0; }
function makeWorld(o){ o = Object.assign({ sep:T0/3, R:T0/3, z:3, container:'closed', containerBreathe:true, wallWork:true, breathe:true, amp:AMP, ampC:AMP, phase:'inTime', gapElement:true, omega:2.0, gamma:0.6, kappa:0.25, kgap:1.0, h:0.01, tilt:0.35 }, o || {});
  const r0 = Math.log(o.z), s = o.sep, R = o.R, place = x => [Math.cosh(x), Math.sinh(x), 0, 0];
  /* A at −s/2, B at +s/2, the container's centre-of-face cells at ±R (the rim, left and right); one container clock */
  const balls = [{ p:place(-s/2), name:'A', x:-s/2, phi:0, amp:o.breathe ? o.amp : 0 }, { p:place(s/2), name:'B', x:s/2, phi:(o.phase === 'inTime' ? T0/3 : T0/3*(1 + Math.sqrt(5))/2), amp:o.breathe ? o.amp : 0 },
    { p:place(-R), name:'C', x:-R, phi:T0/2, amp:(o.breathe && o.containerBreathe) ? o.ampC : 0 }, { p:place(R), name:'C', x:R, phi:T0/2, amp:(o.breathe && o.containerBreathe) ? o.ampC : 0 }];
  balls.forEach((b, k) => { b.k = k; b.arm = k ? 0 : -1; b.r = r0; b.rate = 1; });
  const links = [], mk = (i, j, kind) => { const d = MM.linkDistance(balls[i].p, balls[j].p), Rm = MM.linkRotation(balls[i].p, balls[j].p), U = MM.su2(Rm), n = Math.max(1, Math.round(d/o.h));
    links.push({ i, j, d, R:Rm, U, Gam:0, kind, marks:[], live:[], segs:[{ s0:0, len:d, n, f:new Float64Array(4*n), b:new Float64Array(4*n), head:0 }], nTot:n, hi:new Float64Array(3*n), hj:new Float64Array(3*n), hh:0, c:0, K:0, W:0 }); };
  mk(0, 1, 'AB'); mk(2, 0, 'CA'); mk(1, 3, 'BC');
  const nbr = Array.from({length:4}, () => []); links.forEach((l, q) => { nbr[l.i].push(q); nbr[l.j].push(q); });
  const W = { N:4, balls, links, nbr, opts:Object.assign({ push:'off', torque:0, clocks:'equal' }, o), r:[r0], d:null, T:T0, rk:[r0, r0, r0, r0], rdot:[0, 0, 0, 0], work:0 };
  const a = o.tilt, dA = [Math.sin(a), 0, Math.cos(a)].map(x => x*o.omega/2); W.d = balls.map(() => dA.slice()); W.dRest = W.d.map(v => v.slice());
  W.conn = links.map(l => { const di = W.d[l.i], Rd = MM.v3(l.R, W.d[l.j]); return 2*((di[0]-Rd[0])**2 + (di[1]-Rd[1])**2 + (di[2]-Rd[2])**2); });
  breathe(W, 0); return W; }
function breathe(W, t){ const o = W.opts; W.balls.forEach((b, k) => { W.rk[k] = rOf(o, b.phi, b.amp, t); W.rdot[k] = rDot(o, b.phi, b.amp, t); });
  W.links.forEach(l => { const ri = W.rk[l.i], rj = W.rk[l.j], Gi = Math.tanh(ri/2), Gj = Math.tanh(rj/2), d = l.d, rungs = [], iC = l.i >= 2, jC = l.j >= 2, closed = o.container === 'closed';
    /* face positions and their speeds along the link (s grows from i to j): i's face at r_i/2 moves with ṙ_i/2, j's face at d − r_j/2 with −ṙ_j/2 */
    let si = Math.min(d - 1e-9, ri/2), sj = Math.max(1e-9, d - rj/2), vi = W.rdot[l.i]/2, vj = -W.rdot[l.j]/2; const gI = iC && closed, gJ = jC && closed, gap4 = 4*o.h;
    /* two walls on one stretch cannot pass through each other on the grid: when they meet, the one that arrives pushes the other (a ground wall pushes, a face yields; two faces push each other equally) and the pushed wall moves with the pusher. A model choice, stated. */
    if(sj - si < gap4){ if(gI){ sj = si + gap4; vj = vi; } else if(gJ){ si = sj - gap4; vi = vj; } else { const mid = (si + sj)/2, vm = (vi + vj)/2; si = mid - gap4/2; sj = mid + gap4/2; vi = vm; vj = vm; } l.pushed = true; } else l.pushed = false;
    rungs.push({ s:si, v:vi, rho:gI ? 1 : Gi, kind:gI ? 'ground' : 'face', cell:l.i });
    const delta = sj - si, sm = (si + sj)/2, Gij = Math.tanh((ri - rj)/2); rungs.push({ s:sm, v:(vi + vj)/2, rho:Gij, kind:'junction', delta });
    if(o.gapElement && delta > 2*gap4) rungs.push({ s:sm + gap4/2, v:(vi + vj)/2, rho:Math.tanh(o.kgap*delta), kind:'gap', delta });
    rungs.push({ s:sj, v:vj, rho:gJ ? -1 : -Gj, kind:gJ ? 'ground' : 'face', cell:l.j });
    /* the order on the stretch is fixed: i's wall, the junction, the gap element, j's wall */ l.live = rungs; l.marks = rungs; l.delta = delta; l.Gam = Gij; }); }
/* scatter at every rung, by crossings. A wall at sample index k(t) is crossed during a step by the forward samples that were at or inside it before the move and
   are past it after (j in [k_new, k_old], now at j + 1) and by the backward samples that were at or outside it and are inside after (q in [k_old, k_new], now at q − 1).
   A wall moving away from a stream is crossed by it less often, a wall moving toward it more often — the crossing count is the Doppler of the grid. Each crossing
   sample is scattered once, against the opposite stream at its own position, and both are marked so a wall that steps onto its own reflection does not hit it twice
   (the first build did, and leaked past a ground wall). With wallWork a moving wall returns the Doppler-scaled stream and the surplus is booked as work. */
function scatter(W, S){ const h = W.opts.h, ww = W.opts.wallWork; for(const l of W.links){ const sg = l.segs[0], n = sg.n; if(!l.mem) l.mem = {}; let prevK = -3;
    for(const m of l.live){ if(Math.abs(m.rho) < 1e-15) continue; const key = m.kind + (m.cell === undefined ? '' : m.cell); let kN = Math.max(0, Math.min(n-1, Math.round(m.s/h - 0.5))); if(kN <= prevK + 1) kN = Math.min(n-1, prevK + 2); prevK = kN;
      const mem = l.mem[key] || (l.mem[key] = { k:kN, dF:[], dB:[] }); const kO = mem.k; mem.k = kN; const rho = m.rho, tau = Math.sqrt(Math.max(0, 1 - rho*rho));
      let Df = 1, Db = 1; if(ww && m.v){ const vf = Math.max(-0.9, Math.min(0.9, -m.v)), vb = Math.max(-0.9, Math.min(0.9, m.v)); Df = (1 + vf)/(1 - vf); Db = (1 + vb)/(1 - vb); } const sf = Math.sqrt(Df), sb = Math.sqrt(Db);
      const pair = (p, fromF) => { if(p < 0 || p > n-1) return; const iF = ((sg.head - 1 - p) % n + n) % n, iB = ((sg.head - 1 - (n - 1 - p)) % n + n) % n; /* the forward sample at position p is age p; the backward sample there is age n − 1 − p */
        const fDone = mem.dF.indexOf(iF) >= 0, bDone = mem.dB.indexOf(iB) >= 0; if(fromF ? fDone : bDone) return; const of = 4*iF, ob = 4*iB;
        /* a partner already scattered by this wall is not scattered again: it enters as zero and keeps its place; the new output is merged into it with the energies added (no interference on the grid) */
        const f0 = [sg.f[of], sg.f[of+1], sg.f[of+2], sg.f[of+3]], b0 = [sg.b[ob], sg.b[ob+1], sg.b[ob+2], sg.b[ob+3]], f = fDone ? [0,0,0,0] : f0, b = bDone ? [0,0,0,0] : b0, Ub = FL.applyU(l.U, b, false), Uf = FL.applyU(l.U, f, true);
        const en = x => x[0]*x[0] + x[1]*x[1] + x[2]*x[2] + x[3]*x[3], ef = en(f), eb = en(b);
        if(m.kind === 'ground') l.K += 2*(m.cell === l.i ? eb : ef)*h;
        const fo = [0,1,2,3].map(c => tau*f[c] - rho*sb*Ub[c]), bo = [0,1,2,3].map(c => rho*sf*Uf[c] + tau*b[c]); const w = en(fo) + en(bo) - ef - eb; l.W += w; W.work += w;
        const put = (arr, o, old, out, keep) => { if(!keep){ for(let c=0;c<4;c++) arr[o+c] = out[c]; return; } const e1 = en(old), e2 = en(out), sum = [0,1,2,3].map(c => old[c] + out[c]), es = en(sum), k = es > 1e-300 ? Math.sqrt((e1 + e2)/es) : 0; for(let c=0;c<4;c++) arr[o+c] = k*sum[c]; };
        put(sg.f, of, f0, fo, fDone); put(sg.b, ob, b0, bo, bDone); mem.dF.push(iF); mem.dB.push(iB); if(mem.dF.length > 16){ mem.dF.shift(); mem.dB.shift(); } };
      for(let jj=kN; jj<=kO; jj++) pair(jj + 1, true); for(let q=kO; q<=kN; q++) pair(q - 1, false); } } }
function books(W, S){ const B = FL.books(W, S); return { cells:FL.ballLight(S, 0) + FL.ballLight(S, 1), outside:FL.ballLight(S, 2) + FL.ballLight(S, 3), stretches:B.gaps, per:B.perLink, work:W.work, total:B.total, closed:B.total - W.work }; }
root.HB = { makeWorld, breathe, scatter, books, rOf, rDot, T0, AMP };
})(typeof window !== 'undefined' ? window : globalThis);
if(typeof module !== 'undefined') module.exports = globalThis.HB;
