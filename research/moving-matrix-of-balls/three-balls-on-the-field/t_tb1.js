// SCRIPT: TB-T1 — checks of the three-ball matrix (node)
const MM = require('../mm/mm_math_v1.js'), TB = require('./tb_math_v1.js'), LHS = require('../surprise/src/lh_math.js');
const P = { zbar:[3,5,7], amp:0.35, T:[8,13,21], ph:[0,2*Math.PI/3,4*Math.PI/3], sigma:1, Tphi:9, Tchi:55 }, rOf = tau => LHS.feed(P, tau).r;
const r0 = rOf(0); let W = TB.makeWorld(r0);
console.log('steps r_I, r_J', r0[0].toFixed(4), r0[1].toFixed(4), ' links d', W.links.map(l => l.d.toFixed(4)).join(' '), ' check cosh d_BC - cosh r_I cosh r_J', (Math.cosh(W.links[2].d) - Math.cosh(r0[0])*Math.cosh(r0[1])).toExponential(1));
console.log('strengths c', W.links.map(l => l.c.toFixed(4)).join(' '), ' rest residual', W.restResidual.toExponential(1), ' faces at rest', MM.faceEnergy(W, W.d).E.toFixed(6), JSON.stringify(MM.faceEnergy(W, W.d).per.map(x => +x.toFixed(6))));
const lp = TB.loop(W, r0); console.log('loop: turn', lp.ang.toFixed(10), ' area', lp.area.toFixed(10), ' Thomas 2atan(G_I G_J)', lp.thomas.toFixed(10));
const nn = MM.nnceCheck(W, W.d); console.log('connection energy  1/8|[H,H*]|^2', nn.lhs.toFixed(10), ' sum of faces', nn.rhs.toFixed(10));
// still: nothing moves without light
let St = MM.initState(W, { source:0 }); St.psr.fill(0); St.psi.fill(0); const d0 = St.d.map(v => v.slice()); for(let k=0;k<400;k++) St = MM.rk4(W, St, 0.01); let mv = 0; St.d.forEach((v,i) => v.forEach((x,a) => mv = Math.max(mv, Math.abs(x-d0[i][a])))); console.log('no light, steps held: largest turn', mv.toExponential(1));
for(const src of [0,1,2]){ St = MM.initState(W, { source:src }); const E0 = MM.energies(W, St).E, nu0 = MM.ballCensus(W, St).map(c => c.nu[0]), AL = [null,null,null], AS = [null,null,null]; let mx = [0,0,0];
  for(let k=0;k<1000;k++){ St = MM.rk4(W, St, 0.01); const C = MM.ballCensus(W, St); for(let i=0;i<3;i++){ const rho = MM.lightDensity(St,i); mx[i] = Math.max(mx[i], rho); if(AL[i]===null && rho > 1e-3) AL[i] = St.t; if(AS[i]===null && Math.abs(C[i].nu[0]-nu0[i]) > 1e-3) AS[i] = St.t; } }
  const PW = MM.ballPowers(W, St); let io = 0; PW.forEach(p => io = Math.max(io, Math.abs(p.fromLight+p.fromSea-p.toFaces)));
  const D = MM.deriv(W, St), g = MM.seaSpeed(W, St), C = MM.ballCensus(W, St); let lim = 0; for(let i=0;i<3;i++){ const td = MM.tauDot(W, St, D, i); lim = Math.max(lim, td*td/(4*g*C[i].S)); }
  console.log('kick '+TB.NAMES[src]+': drift', (MM.energies(W,St).E-E0).toExponential(1), ' most light ever in A,B,C', mx.map(x => x.toFixed(3)).join(' '), ' light / sea arrival', [0,1,2].map(i => (AL[i]===null?'-':AL[i].toFixed(2))+'/'+(AS[i]===null?'-':AS[i].toFixed(2))).join('  '), ' in-out', io.toExponential(1), ' limit', lim.toFixed(4), ' gap', St.gap0.toFixed(3), 'rank', St.kSea); }
// breathing books
W = TB.makeWorld(r0); St = MM.initState(W, { source:0 }); St.work = 0; const Eb = MM.energies(W, St).E; let tau = 0; for(let f=0;f<1200;f++){ tau += 1/60; St = TB.advance(W, St, rOf(tau), 1/60); }
console.log('breathing to tau=20: books', (MM.energies(W,St).E - Eb - St.work).toExponential(1), ' work', St.work.toFixed(5), ' loop turn-area', (TB.loop(W, rOf(tau)).ang - TB.loop(W, rOf(tau)).area).toExponential(1));
const Md = TB.modes(TB.makeWorld(r0), TB.makeWorld(r0).d); console.log('eigenvalues', Md.vals.map(x => x.toFixed(4)).join(' ')); Md.share.forEach((s,k) => console.log('  mode', k, 'E', Md.vals[k].toFixed(4), 'share A,B,C', s.map(x => x.toFixed(3)).join(' '), k === Md.lead ? '<- leading' : '')); console.log('margin |l2/l1|', Md.margin.toFixed(4));
