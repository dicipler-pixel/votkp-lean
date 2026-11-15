/* SCRIPT: LH-K15-RERUN
   K15 was killed on the first run (lh_selftest_v1.out): 'mean residence 51' at 2.35e-8 and 'network ledger' at 1.91e-9, tolerance 1e-9.
   Cause found in the TEST, not the model: (1) the residence integral summed 2e5 quadrature steps (rounding about 1e-9 times 51);
   (2) the ledger's half step was fed the source (p0, p0, pm) instead of the source on that half interval.
   Same kill line (K15, > 1e-9). Moments now from the closed form: total = κ(−M⁻¹)₀₀, mean = (M⁻²)₀₀/(−M⁻¹)₀₀.
   Opposite run under the same line: a wrong residence formula must be killed. */
const L = require('./lh_math_v1.js');
const inv = M => { const d = M[0][0]*M[1][1]-M[0][1]*M[1][0]; return [[M[1][1]/d, -M[0][1]/d],[-M[1][0]/d, M[0][0]/d]]; }, mul = (A,B) => [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],[A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]];
const mom = (k,a,b,swap) => { const M = swap ? [[-(k+a), a],[b, -b]] : [[-(k+a), b],[a, -b]], Mi = inv(M), Mi2 = mul(Mi,Mi); return { total:-k*Mi[0][0], mean:Mi2[0][0]/(-Mi[0][0]) }; };
const out = [], line = (v, note) => out.push((v <= 1e-9 ? 'HOLDS ' : 'KILLED') + '  K15  ' + v.toExponential(2).padStart(9) + '  tol 1e-9  ' + note);
line(Math.abs(mom(1,1,0.2).total - 1), 'impulse total outflow = 1 (closed form)');
line(Math.abs(mom(1,1,0.2).mean - 6), 'mean residence 6 (closed form)');
line(Math.abs(mom(1,1,0.02).mean - 51), 'mean residence 51 (closed form)');
/* the stepper itself against the closed form: impulse response at t = 3 */
{ const k = 1, a = 1, b = 0.2, M = [[-(k+a), b],[a,-b]], E = L.expM2(M, 3); let x = 1, y = 0; for(let i=0;i<300;i++){ [x,y] = L.stocksStep(x,y,0,0,0,k,a,b,0.01); } line(Math.max(Math.abs(x-E[0][0]), Math.abs(y-E[1][0])), 'stepper after 300 steps equals exp(3M) applied to the impulse'); }
/* ledger: d(x + y)/dt = P − κx exactly; integrate in, out with the same Simpson nodes the stepper uses */
{ const P = Object.assign({}, L.DEF, { drive:'breathe' }), h = 1/60; let x = 0, y = 0, I = 0, O = 0;
  for(let n=0;n<2000;n++){ const t0 = n*h, p0 = L.pushAt(P,t0)[0].arrive[1], pm = L.pushAt(P,t0+h/2)[0].arrive[1], p1 = L.pushAt(P,t0+h)[0].arrive[1], pq = L.pushAt(P,t0+h/4)[0].arrive[1];
    const [xm,ym] = L.stocksStep(x,y,p0,pq,pm,P.kappa,P.ha,P.hb,h/2), [x1,y1] = L.stocksStep(x,y,p0,pm,p1,P.kappa,P.ha,P.hb,h);
    I += h/6*(p0+4*pm+p1); O += P.kappa*h/6*(x+4*xm+x1); x = x1; y = y1; }
  line(Math.abs(I - O - x - y)/Math.max(1,I), 'network ledger |in − out − stored| over 2000 frames (relative)'); }
/* opposite under the same line */
{ const w = mom(1,1,0.2,true); out.push('note   K15-opposite-1  swapping a and b in the y equation gives mean ' + w.mean.toFixed(6) + ': the x-moment does not see that swap, so it is not a valid opposite');
  const wrong = (1 + 0.2/1)/1, m = mom(1,1,0.2).mean; out.push((Math.abs(m - wrong) > 1e-9 ? 'HOLDS ' : 'KILLED') + '  K15-opposite-2  the wrong formula (1 + b/a)/κ = ' + wrong + ' is killed by the same line (closed form ' + m + ')'); }
console.log(out.join('\n'));
