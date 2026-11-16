// SCRIPT: L3-RUN-05
// (a) the paper's weighted form on the matrix that moves the light: K = D + i*(hop part of denseH); (1/8)||[K,K*]||^2 against sum c^2 * 2|d_i - R d_j|^2.
// (b) connection energy held at rest: three-ball, seven-ball (MM), and the Flock worlds with clocks z and clocks equal.
const MM = require('/home/claude/balls/w/mm/mm_math_v1.js'), TB = require('/home/claude/balls/w/tb/tb_math_v1.js'), FL = require('/home/claude/balls/w/fl/fl_math_v1.js');
let seed = 5; const rnd = () => (seed = (seed*16807) % 2147483647)/2147483647 - 0.5;
function weighted(W, d){ const H = MM.denseH(W, d), n = H.n, Kr = H.Hr.map(r => Array.from(r)), Ki = H.Hi.map(r => Array.from(r));
  // subtract D, multiply the rest by i, add D back:  i*(a+ib) = -b + ia  on entries outside the 2x2 ball blocks
  for(let i=0;i<n;i++) for(let j=0;j<n;j++){ if((i>>1) === (j>>1)) continue; const a = H.Hr[i][j], b = H.Hi[i][j]; Kr[i][j] = -b; Ki[i][j] = a; }
  const mul = (Ar,Ai,Br,Bi) => { const Cr = Array.from({length:n}, () => new Float64Array(n)), Ci = Array.from({length:n}, () => new Float64Array(n)); for(let i=0;i<n;i++) for(let k=0;k<n;k++) for(let j=0;j<n;j++){ Cr[i][j] += Ar[i][k]*Br[k][j] - Ai[i][k]*Bi[k][j]; Ci[i][j] += Ar[i][k]*Bi[k][j] + Ai[i][k]*Br[k][j]; } return [Cr,Ci]; };
  const Sr = Kr.map((r,i) => r.map((_,j) => Kr[j][i])), Si = Ki.map((r,i) => r.map((_,j) => -Ki[j][i])); let skew = 0; for(let i=0;i<n;i++) for(let j=0;j<n;j++) if((i>>1)!==(j>>1)) skew = Math.max(skew, Math.abs(Kr[i][j]+Sr[i][j]), Math.abs(Ki[i][j]+Si[i][j]));
  const [Ar,Ai] = mul(Kr,Ki,Sr,Si), [Br,Bi] = mul(Sr,Si,Kr,Ki); let lhs = 0; for(let i=0;i<n;i++) for(let j=0;j<n;j++) lhs += (Ar[i][j]-Br[i][j])**2 + (Ai[i][j]-Bi[i][j])**2; lhs /= 8;
  let rhs = 0; for(const l of W.links){ const Rd = MM.v3(l.R, d[l.j]); rhs += l.c*l.c*2*((d[l.i][0]-Rd[0])**2 + (d[l.i][1]-Rd[1])**2 + (d[l.i][2]-Rd[2])**2); } return { lhs, rhs, skew }; }
for(const [name, W] of [['3-ball', TB.makeWorld([Math.log(3), Math.log(5)])], ['7-ball', MM.makeWorld(1)]]){ let worst = 0, first = null; for(let k=0;k<100;k++){ const d = Array.from({length:W.N}, () => [2*rnd(),2*rnd(),2*rnd()]), a = weighted(W, d); worst = Math.max(worst, Math.abs(a.lhs-a.rhs)/a.rhs); if(!first) first = a; }
  console.log('(a)', name, 'K = D + i*hop: off-block part skew to', first.skew.toExponential(1), ' sample lhs', first.lhs.toPrecision(12), 'rhs', first.rhs.toPrecision(12), ' worst rel diff over 100 random d', worst.toExponential(2)); }
console.log('(b) connection energy held at rest (unit weights, MM.nnceCheck) and face energy:');
{ const W = TB.makeWorld([Math.log(3), Math.log(5)]), a = MM.nnceCheck(W, W.d); console.log('   three-ball (z = 3,5): rhs', a.rhs.toExponential(2), ' faces', MM.faceEnergy(W, W.d).E.toExponential(2)); }
{ const W = MM.makeWorld(1), R = MM.restState(W, { iters:60000, eta:0.08, withSea:false, tol:1e-11 }), a = MM.nnceCheck(W, R.d); console.log('   seven-ball MM (steps 0.9), faces only, descended from the radial start: residual', R.residual.toExponential(1), ' lhs', a.lhs.toPrecision(10), ' rhs', a.rhs.toPrecision(10), ' faces', MM.faceEnergy(W, R.d).E.toPrecision(8)); }
for(const N of [3,4,7]) for(const clocks of ['z','equal']){ const W = FL.makeWorld({ N, clocks }), a = MM.nnceCheck(W, W.dRest); let floor = 0; for(const l of W.links){ const mi = Math.hypot(...W.dRest[l.i]), mj = Math.hypot(...W.dRest[l.j]); floor += 2*(mi-mj)**2; }
  console.log('   Flock N =', N, 'clocks', clocks, ': lhs', a.lhs.toPrecision(10), ' rhs', a.rhs.toPrecision(10), ' part forced by unequal level spacings 2*sum(|d_i|-|d_j|)^2 =', floor.toPrecision(10), ' rest residual', W.restResidual.toExponential(1)); }
