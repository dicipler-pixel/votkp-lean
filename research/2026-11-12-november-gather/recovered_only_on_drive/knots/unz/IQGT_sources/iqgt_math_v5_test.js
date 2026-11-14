// SCRIPT: IQGT-MIXER-V5-MATH-TEST
// Kill conditions written before the run:
// T1 chart: pulled-back components change with the warp, but the length of the same step agrees in both charts and with Tr(Pi V V) to 1e-6
// T2 Chern: lattice count 1, 1, 2, 0 for (wrap 1, warp 0), (wrap 1, warp 1), (wrap 2), (no wrap); Riemann sum within 1e-3 of the same
// T3 fold: det g = 0.0179 at x = 0.6 (paper 0.0179 / check 0.01787), 0 at x = 0; intrinsic g(V,V)/||X||^2 = 1 to 1e-12
// T4 gap closing: two orthogonal approaches at m = 0 end 1.000 apart; at m = 0.3 they end at the same projector
// T5 slopes of the pair model: -2, -2, -3, -1 exactly; finite-temperature friction slope within 0.02 of 0 at gap 0.01
// T6 turning points: polar 0.32981248 at 35 deg from 0.6; narrowing 1.0969 at 50 deg from 0.8
// T7 toll: constant speed meets the floor L^2/T; any ease > 0 lies above it
// T8 corridor: tail never above its Davis-Kahan bound in 300 trials at inner gap 0.01; tip median > 10 x tail median
// T9 fog: residual -> 0 as eta -> 0 without leak; stays at |leak| with leak
// T10 cards: swaps 5, 3.512407, on the upper bound (pos 1); 10-cycle 5, 2.896405; doubling 4, 2.7706
const IQ = require('./iqgt_math_v5.js'), C = IQ.C; const out = {};
{ const w = 0.8, th = 1.3, ph = 0.9, xd = [0.4, 0.7]; const uv = IQ.chartInv(th, ph, w), J = IQ.chartJ(uv[0], uv[1], w);
  const det = J[0][0]*J[1][1]-J[0][1]*J[1][0], ud = [( J[1][1]*xd[0]-J[0][1]*xd[1])/det, (-J[1][0]*xd[0]+J[0][0]*xd[1])/det];
  const GA = IQ.gRound(th), GB = IQ.pull(GA, J); const lA = IQ.quad(GA, xd, xd), lB = IQ.quad(GB, ud, ud);
  const h = 1e-6, P = t => IQ.piOf(IQ.sph(th + xd[0]*t, ph + xd[1]*t)), V = IQ.sub2(P(h), P(-h), 1/(2*h)), lT = IQ.Q2(P(0), V, V)[0];
  out.T1 = [[GA[0][0], GB[0][0], lA, lB, lT], Math.abs(GA[0][0]-GB[0][0]) > 0.01 && Math.abs(lA-lB) < 1e-6 && Math.abs(lA-lT) < 1e-6]; }
{ const a = IQ.chern(1, 0, 48), b = IQ.chern(1, 1, 48), c2 = IQ.chern(2, 0.5, 48), d = IQ.chern(0, 0.5, 48);
  const L = [a.lattice, b.lattice, c2.lattice, d.lattice], R = [a.riemann, b.riemann, c2.riemann, d.riemann];
  out.T2 = [[L.map(x => +x.toFixed(6)), R.map(x => +x.toFixed(5))], [1,1,2,0].every((v,i) => Math.abs(L[i]-v) < 1e-6 && Math.abs(R[i]-v) < 1e-3)]; }
{ const a = IQ.pullG(IQ.foldN, 0.6, 0), b = IQ.pullG(IQ.foldN, 0, 0); const r = C.rng(9); let worst = 0;
  for(let t=0;t<200;t++){ const q = IQ.tangent2(a.P0, r); const g = IQ.Q2(a.P0, q.V, q.V)[0]; const x = q.X.reduce((s, z) => s + z[0]*z[0] + z[1]*z[1], 0); worst = Math.max(worst, Math.abs(g/x - 1)); }
  out.T3 = [[a.det, b.det, worst], Math.abs(a.det - 0.01787) < 2e-5 && Math.abs(b.det) < 1e-12 && worst < 1e-12]; }
{ const d0 = IQ.piDist(IQ.approach(0, 0, 1e-9), IQ.approach(0, Math.PI/2, 1e-9)), d1 = IQ.piDist(IQ.approach(0.3, 0, 0), IQ.approach(0.3, Math.PI/2, 0));
  out.T4 = [[d0, d1], Math.abs(d0 - 1) < 1e-9 && d1 < 1e-12]; }
{ const m = IQ.pairModel, s = [IQ.slope(m.metric, 0.5), IQ.slope(m.curvature, 0.5), IQ.slope(m.dipole, 0.5), IQ.slope(m.friction0, 0.5), IQ.slope(D => m.frictionT(D, 0.3), 0.01)];
  out.T5 = [s.map(x => +x.toFixed(4)), Math.abs(s[0]+2) < 1e-6 && Math.abs(s[1]+2) < 1e-6 && Math.abs(s[2]+3) < 1e-6 && Math.abs(s[3]+1) < 1e-6 && Math.abs(s[4]) < 0.02]; }
{ const a = IQ.polarTurn(0.6, 35*Math.PI/180), b = IQ.narrowTurn(0.8, 50*Math.PI/180); out.T6 = [[a, b], Math.abs(a - 0.32981248) < 1e-7 && Math.abs(b - 1.0969) < 1e-3]; }
{ const a = IQ.toll(1, 4, 0), b = IQ.toll(1, 4, 0.6); out.T7 = [[a.W, a.bound, b.W], Math.abs(a.W - a.bound) < 1e-9 && b.W > a.bound]; }
{ const r = C.rng(17), Q = C.randOrth(7, r); let viol = 0; const tips = [], tails = [];
  for(let t=0;t<300;t++){ const x = IQ.corridorTrial(0.01, 3, 0.02, r, Q); if(Math.sin(x.tail) > x.tailBound) viol++; tips.push(x.tip); tails.push(x.tail); }
  const med = a => a.slice().sort((p,q) => p-q)[a.length>>1]; out.T8 = [[viol, C.deg(med(tips)), C.deg(med(tails))], viol === 0 && med(tips) > 10*med(tails)]; }
{ const a = IQ.sld(0.7, 0, 1e-9).res, b = IQ.sld(0.7, 0.2, 1e-9).res; out.T9 = [[a, b], a < 1e-7 && Math.abs(b - 0.2) < 1e-6]; }
{ const a = IQ.permRead('swaps'), b = IQ.permRead('cycle'), c3 = IQ.permRead('dbl');
  out.T10 = [[a.s2, a.L, a.pos, b.s2, b.L, c3.s2, c3.L], Math.abs(a.s2-5)<1e-9 && Math.abs(a.L-3.512407)<1e-5 && Math.abs(a.pos-1)<1e-9 && Math.abs(b.s2-5)<1e-9 && Math.abs(b.L-2.896405)<1e-5 && Math.abs(c3.s2-4)<1e-9 && Math.abs(c3.L-2.7706)<1e-3]; }
for(const [k, v] of Object.entries(out)) console.log(k, v[1] ? 'PASS' : 'FAIL', JSON.stringify(v[0]));
