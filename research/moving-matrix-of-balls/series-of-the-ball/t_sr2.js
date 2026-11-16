// SCRIPT: SR-T2 — rest, light, sea, books, eigenvectors on the series (node)
const LH = require('../surprise/src/lh_math.js'), MM = require('../mm/mm_math_v1.js'), SR = require('./sr_math_v1.js');
const P = { zbar:[3,5,7], amp:0.35, T:[8,13,21], ph:[0,2*Math.PI/3,4*Math.PI/3], sigma:1, Tphi:9, Tchi:55 };
const S0 = LH.feed(P, 0), out = {};
for(const L of [1,2,3]){ const W = SR.makeWorld(S0, L); let t0 = Date.now();
  let seed = 7; const rnd = () => (seed = (seed*16807) % 2147483647)/2147483647 - 0.5;
  W.d = W.d.map(v => { const w = v.map(x => x + 0.15*rnd()), m = Math.hypot(...w); return w.map(x => x/m*W.opts.omega/2); });
  const R = MM.restState(W, { iters: L===3 ? 40000 : 40000, eta:0.06, withSea:false, tol:1e-9 }); W.d = R.d; out['rest'+L] = R.d;
  console.log('L'+L, 'rest: faces', MM.faceEnergy(W, W.d).E.toFixed(5), 'residual', R.residual.toExponential(1), 'iters', R.iters, 'ms', Date.now()-t0);
  const noSea = L === 3; let St = MM.initState(W, { source:0, noSea }); const E0 = MM.energies(W, St).E, nu0 = noSea ? null : MM.ballCensus(W, St).map(c => c.nu[0]);
  const AL = Array(W.N).fill(null), AS = Array(W.N).fill(null); t0 = Date.now(); const steps = 600;
  for(let k=0;k<steps;k++){ St = MM.rk4(W, St, 0.01); for(let i=0;i<W.N;i++){ if(AL[i]===null && MM.lightDensity(St,i) > 1e-3) AL[i] = St.t; } if(!noSea){ const C = MM.ballCensus(W,St); for(let i=0;i<W.N;i++) if(AS[i]===null && Math.abs(C[i].nu[0]-nu0[i]) > 1e-3) AS[i] = St.t; } }
  const ms = (Date.now()-t0)/steps; let both=0, first=0; for(let i=1;i<W.N;i++) if(AL[i]!==null && AS[i]!==null){ both++; if(AL[i] < AS[i]) first++; }
  const PW = MM.ballPowers(W, St); let io = 0; PW.forEach(p => io = Math.max(io, Math.abs(p.fromLight + p.fromSea - p.toFaces)));
  console.log('   faces still, t=6: drift', (MM.energies(W,St).E - E0).toExponential(1), ' ms/step', ms.toFixed(1), ' light reached', AL.filter(x=>x!==null).length, ' light before sea', first+'/'+both, ' in-out', io.toExponential(1), noSea ? '(no sea)' : 'gap '+St.gap0.toFixed(3)+' rank '+St.kSea);
  // breathing books
  let Sb = MM.initState(W, { source:0, noSea }); Sb.work = 0; const Eb = MM.energies(W, Sb).E; let tau = 0; for(let f=0;f<120;f++){ tau += 1/60; Sb = SR.advance(W, Sb, LH.feed(P, tau), 1/60, 0.02); }
  console.log('   breathing 2s: books', (MM.energies(W,Sb).E - Eb - Sb.work).toExponential(1), ' work', Sb.work.toFixed(5)); SR.relink(W, S0);
  t0 = Date.now(); const M = SR.modes(W, W.d); console.log('   eigenvectors', M.vals.length, 'ms', Date.now()-t0, ' lowest/highest', M.vals[0].toFixed(3), M.vals[M.vals.length-1].toFixed(3));
}
require('fs').writeFileSync('rest_series_v1.json', JSON.stringify(out));
