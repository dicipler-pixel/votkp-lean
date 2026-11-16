// SCRIPT: L3-RUN-02
// The C4 line: why tau - tau0 reads -Infinity; the speed limit ratio; finite-difference test of tauDot. Unchanged copies only.
const MM = require('/home/claude/balls/w/mm/mm_math_v1.js'), TB = require('/home/claude/balls/w/tb/tb_math_v1.js');
const r0 = [Math.log(3), Math.log(5)], W = TB.makeWorld(r0);
console.log('link U (u00,u01,u10,u11 as [re,im]):'); W.links.forEach(l => console.log('  ', l.i, l.j, JSON.stringify(l.U.map(u => u.map(x => +x.toFixed(6)))), ' R row z', l.R[2].map(x => x.toFixed(6)).join(',')));
{ const G = MM.groundProjector(W, W.d); let up = 0, cross = 0; for(let i=0;i<3;i++) for(let j=0;j<3;j++){ up = Math.max(up, Math.hypot(G.Pr[2*i][2*j], G.Pi[2*i][2*j])); cross = Math.max(cross, Math.hypot(G.Pr[2*i][2*j+1], G.Pi[2*i][2*j+1])); } console.log('rest sea P: largest up-up entry', up.toExponential(2), ' largest up-down entry', cross.toExponential(2), ' rank', G.k);
  for(const k of [2,3,4]){ const Gk = MM.groundProjector(W, W.d, k), S = { Pr:Gk.Pr, Pi:Gk.Pi }; console.log('  cut k =', k, ' gap', Gk.gap.toFixed(4), ' nu per ball', MM.ballCensus(W, S).map(c => c.nu.map(x => x.toFixed(6)).join('/')).join('  ')); } }
let S = MM.initState(W, { source:0 }); console.log('\nkick A, sea on.  t | ball: nu0, nu1, tau, S, tauDot analytic, tauDot finite difference, ratio tauDot^2/(4 g S)');
let worst = 0, worstFD = 0, minnu = 1, maxnu = 0; const h = 0.01;
for(let k=1;k<=600;k++){ const Sm = S; S = MM.rk4(W, S, h);
  const C = MM.ballCensus(W, S), D = MM.deriv(W, S), g = MM.seaSpeed(W, S);
  for(let i=0;i<3;i++){ const td = MM.tauDot(W, S, D, i), ratio = td*td/(4*g*C[i].S); if(isFinite(ratio)) worst = Math.max(worst, ratio); minnu = Math.min(minnu, C[i].nu[0]); maxnu = Math.max(maxnu, C[i].nu[1]); }
  if(k % 100 === 0 || k === 1 || k === 10){ const Sp = MM.rk4(W, S, 1e-4), Sn = Sm; const Cp = MM.ballCensus(W, Sp);
    console.log(' t', S.t.toFixed(2), ' g', g.toExponential(3)); for(let i=0;i<3;i++){ const td = MM.tauDot(W, S, D, i), fd = (Cp[i].tau - C[i].tau)/1e-4; worstFD = Math.max(worstFD, Math.abs(fd-td)/Math.max(1,Math.abs(td)));
      console.log('    ', TB.NAMES[i], ' nu', C[i].nu.map(x => x.toExponential(4)).join(', '), ' tau', C[i].tau.toFixed(4), ' S', C[i].S.toExponential(3), ' tau\'', td.toFixed(4), ' fd', fd.toFixed(4), ' ratio', (td*td/(4*g*C[i].S)).toExponential(3)); } } }
console.log('kick A to t = 6: largest ratio', worst.toExponential(3), ' smallest nu0', minnu.toExponential(3), ' largest nu1', maxnu.toFixed(6), ' worst rel. gap analytic vs forward difference', worstFD.toExponential(2));
// all three kicks, to t = 10, and the 7-ball world
for(const src of [0,1,2]){ let St = MM.initState(W, { source:src }), w = 0; for(let k=0;k<1000;k++){ St = MM.rk4(W, St, 0.01); const C = MM.ballCensus(W, St), D = MM.deriv(W, St), g = MM.seaSpeed(W, St); for(let i=0;i<3;i++){ const td = MM.tauDot(W, St, D, i), q = td*td/(4*g*C[i].S); if(isFinite(q)) w = Math.max(w, q); } } console.log('3-ball kick', TB.NAMES[src], 'to t = 10: largest tauDot^2/(4 g S) over all balls and steps', w.toFixed(5)); }
{ const W7 = MM.makeWorld(1); let St = MM.initState(W7, { source:0 }); const C0 = MM.ballCensus(W7, St); console.log('\n7-ball (MM.makeWorld(1)): rank', St.kSea, 'gap', St.gap0.toFixed(4), ' nu at t=0, ball 0:', C0[0].nu.map(x => x.toFixed(6)).join(', '), ' ball 1:', C0[1].nu.map(x => x.toFixed(6)).join(', '), ' tau0', C0.map(c => c.tau.toFixed(4)).join(' '));
  let w = 0; for(let k=0;k<300;k++){ St = MM.rk4(W7, St, 0.01); if(k % 10 === 9){ const C = MM.ballCensus(W7, St), D = MM.deriv(W7, St), g = MM.seaSpeed(W7, St); for(let i=0;i<W7.N;i++){ const td = MM.tauDot(W7, St, D, i), q = td*td/(4*g*C[i].S); if(isFinite(q)) w = Math.max(w, q); } } }
  console.log('7-ball kick 0 to t = 3 (every 10th step): largest ratio', w.toFixed(5), ' tau - tau0', MM.ballCensus(W7, St).map((c,i) => (c.tau - C0[i].tau).toFixed(4)).join(' ')); }
