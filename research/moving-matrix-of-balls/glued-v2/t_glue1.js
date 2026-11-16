// SCRIPT: MM-GLUE-T1 — checks of the moving matrix on the glued balls (node)
const LH = require('../surprise/src/lh_math.js'), MM = require('../mm/mm_math_v1.js'), G = require('./mm_glue_v1.js');
const P = { zbar:[3,5,7], amp:0.35, T:[8,13,21], ph:[0,2*Math.PI/3,4*Math.PI/3], sigma:1, Tphi:9, Tchi:55 };
let S = LH.feed(P, 0), W = G.makeWorld(S);
console.log('balls', W.N, 'links', W.links.length, 'step lengths', [...new Set(W.links.map(l => l.d.toFixed(4)))].join(' '));
// face check: the shared face is halfway: <midpoint, face normal> = 0
let fw = 0; W.links.forEach(l => { const pi = W.geo.p[l.i], pj = W.geo.p[l.j], N = W.geo.faces[l.j], s = Math.sinh(l.d/2)/Math.sinh(l.d), m = pi.map((x,k) => s*x + s*pj[k]); fw = Math.max(fw, Math.abs(LH.mink(m, N))); });
console.log('shared face passes through the link midpoint, worst', fw.toExponential(2));
console.log('glued rest: faces energy', MM.faceEnergy(W, W.d).E.toExponential(2), ' NNCE', JSON.stringify(MM.nnceCheck(W, W.d)));
// still: no light, no breathing -> nothing moves
let St = MM.initState(W, { source:0 }); St.psr.fill(0); St.psi.fill(0); const d0 = JSON.stringify(St.d);
for(let k=0;k<200;k++) St = MM.rk4(W, St, 0.01); let mv = 0; St.d.forEach((v,i) => v.forEach((x,a) => mv = Math.max(mv, Math.abs(x - JSON.parse(d0)[i][a])))); console.log('no light, faces still: largest ball turn', mv.toExponential(2));
// fixed faces with light: conservation and arrivals
W = G.makeWorld(S); St = MM.initState(W, { source:0 }); const E0 = MM.energies(W, St).E; const nu0 = MM.ballCensus(W, St).map(c => c.nu[0]); const AL = Array(W.N).fill(null), AS = Array(W.N).fill(null);
let t0 = Date.now(); for(let k=0;k<600;k++){ St = MM.rk4(W, St, 0.01); for(let i=0;i<W.N;i++){ if(AL[i]===null && MM.lightDensity(St,i) > 1e-3) AL[i] = St.t; if(AS[i]===null && Math.abs(MM.ballCensus(W,St)[i].nu[0]-nu0[i]) > 1e-3) AS[i] = St.t; } }
console.log('fixed faces, t=6: energy drift', (MM.energies(W, St).E - E0).toExponential(2), ' ms/step', ((Date.now()-t0)/600).toFixed(1));
let both = 0, first = 0; for(let i=1;i<W.N;i++) if(AL[i]!==null && AS[i]!==null){ both++; if(AL[i] < AS[i]) first++; } console.log('light before sea', first, '/', both, ' light reached', AL.filter(x=>x!==null).length, ' sea answered', AS.filter(x=>x!==null).length);
const PW = MM.ballPowers(W, St); console.log('ball in - out worst', Math.max(...PW.map(p => Math.abs(p.fromLight + p.fromSea - p.toFaces))).toExponential(2));
const D = MM.deriv(W, St), g = MM.seaSpeed(W, St), C = MM.ballCensus(W, St); let r = 0; for(let i=0;i<W.N;i++){ const td = MM.tauDot(W, St, D, i); r = Math.max(r, td*td/(4*g*C[i].S)); } console.log('speed limit max ratio', r.toFixed(5));
// breathing faces: books close with the work term
W = G.makeWorld(S); St = MM.initState(W, { source:0 }); St.work = 0; const Eb = MM.energies(W, St).E; let tau = 0;
for(let f=0;f<600;f++){ tau += 1/60; St = G.advance(W, St, LH.feed(P, tau), 1/60); }
const Ee = MM.energies(W, St).E; console.log('breathing, tau=10: E change', (Ee-Eb).toFixed(6), ' work by faces', St.work.toFixed(6), ' books', (Ee - Eb - St.work).toExponential(2), ' faces now', MM.faceEnergy(W, St.d).E.toFixed(5));
// no light, breathing: the faces alone load the glue
W = G.makeWorld(S); St = MM.initState(W, { source:0 }); St.psr.fill(0); St.psi.fill(0); St.work = 0; const Ec = MM.energies(W, St).E; tau = 0;
for(let f=0;f<600;f++){ tau += 1/60; St = G.advance(W, St, LH.feed(P, tau), 1/60); } console.log('no light, breathing: faces', MM.faceEnergy(W, St.d).E.toFixed(5), ' books', (MM.energies(W,St).E - Ec - St.work).toExponential(2));
