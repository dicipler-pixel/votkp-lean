// SCRIPT: L3-RUN-04
// README loop number at tau = 0, with the steps from the surprise-ball feed formula (ex_surp_2_light_hypersurface_surprise_v1.js line 29):
// r_a = max(ln 1.3, ln zbar_a + amp sin(2 pi tau / T_a + ph_a)), zbar = (3,5,7), amp = 0.35, ph = (0, 2pi/3, 4pi/3).
const MM = require('/home/claude/balls/w/mm/mm_math_v1.js'), TB = require('/home/claude/balls/w/tb/tb_math_v1.js');
const P = { zbar:[3,5,7], amp:0.35, T:[8,13,21], ph:[0,2*Math.PI/3,4*Math.PI/3] }, rOf = tau => [0,1,2].map(a => Math.max(Math.log(1.3), Math.log(P.zbar[a]) + P.amp*Math.sin(2*Math.PI*tau/P.T[a] + P.ph[a])));
const r0 = rOf(0); const W = TB.makeWorld(r0), lp = TB.loop(W, r0);
console.log('r(0) =', r0.map(x => x.toFixed(10)).join(', '));
console.log('loop: turn', lp.ang.toFixed(10), ' area', lp.area.toFixed(10), ' Thomas 2atan(G_I G_J)', lp.thomas.toFixed(10), ' README 0.7110545751');
console.log('differences turn-area', (lp.ang-lp.area).toExponential(2), ' turn-thomas', (lp.ang-lp.thomas).toExponential(2));
const Md = TB.modes(W, W.d); console.log('eigenvalues', Md.vals.map(x => x.toFixed(3)).join(' '), ' leading shares', Md.share[Md.lead].map(x => x.toFixed(3)).join(' '), ' margin', Md.margin.toFixed(3));
let St = MM.initState(W, { source:0 }); console.log('rank of sea', St.kSea, ' gap', St.gap0.toFixed(3), ' nu at t=0', MM.ballCensus(W, St).map(c => c.nu.map(x => x.toExponential(2)).join('/')).join('  '));
let w = 0; for(let k=0;k<1000;k++){ St = MM.rk4(W, St, 0.01); const C = MM.ballCensus(W, St), D = MM.deriv(W, St), g = MM.seaSpeed(W, St); for(let i=0;i<3;i++){ const td = MM.tauDot(W, St, D, i), q = td*td/(4*g*C[i].S); if(isFinite(q)) w = Math.max(w, q); } }
console.log('kick A to t = 10, every step: largest tauDot^2/(4 g S)', w.toFixed(4));
// g against its closed form ||P H (1-P)||_F^2 on the dense matrix
{ const H = MM.denseH(W, St.d), n = H.n; const mul = (Ar,Ai,Br,Bi) => { const Cr = Array.from({length:n}, () => new Float64Array(n)), Ci = Array.from({length:n}, () => new Float64Array(n)); for(let i=0;i<n;i++) for(let k=0;k<n;k++) for(let j=0;j<n;j++){ Cr[i][j] += Ar[i][k]*Br[k][j] - Ai[i][k]*Bi[k][j]; Ci[i][j] += Ar[i][k]*Bi[k][j] + Ai[i][k]*Br[k][j]; } return [Cr,Ci]; };
  const Qr = St.Pr.map((r,i) => r.map((v,j) => (i===j?1:0) - v)), Qi = St.Pi.map(r => r.map(v => -v)); const [Ar,Ai] = mul(St.Pr, St.Pi, H.Hr, H.Hi), [Br,Bi] = mul(Ar, Ai, Qr, Qi); let e = 0; for(let i=0;i<n;i++) for(let j=0;j<n;j++) e += Br[i][j]**2 + Bi[i][j]**2;
  let idem = 0; const [P2r,P2i] = mul(St.Pr, St.Pi, St.Pr, St.Pi); for(let i=0;i<n;i++) for(let j=0;j<n;j++) idem = Math.max(idem, Math.abs(P2r[i][j]-St.Pr[i][j]), Math.abs(P2i[i][j]-St.Pi[i][j]));
  let tr = 0; for(let i=0;i<n;i++) tr += St.Pr[i][i];
  console.log('at t = 10: seaSpeed g = 1/2||P\'||^2 =', MM.seaSpeed(W, St).toPrecision(12), '  ||P H (1-P)||_F^2 =', e.toPrecision(12), '  |P^2 - P| max', idem.toExponential(2), ' Tr P', tr.toFixed(12));
  const C = MM.ballCensus(W, St); console.log('census check Tr X_i = Tr C - Tr C^2 against sum nu(1-nu):', C.map(c => (c.trX - c.nu[0]*(1-c.nu[0]) - c.nu[1]*(1-c.nu[1])).toExponential(1)).join(' ')); }
