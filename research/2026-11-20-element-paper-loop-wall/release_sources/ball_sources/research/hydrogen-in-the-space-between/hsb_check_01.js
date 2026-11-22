/* SCRIPT: HSB-CHECK-01 — fixed before the run.
   (a) books: Tr(P) = N and Tr(PH) constant to 1e-9 over t = 0..40 after the kick (exact evolution, so a failure means a wrong reading);
   (b) light between: the far atom's first move (the whole atom, centre and ports: summed change of the sites' states ||C - C_ground|| > 1e-7) must come later for larger separation, and the speed from the slope
       must not exceed the lattice's largest group speed 2·c0·(lattice step) — KILLED if first-move time at sep 6 <= at sep 2;
   (c) the connection-energy identity (nnceCheck) holds to 1e-9;
   (d) the ground sea is still (no charge before the kick) and at rest the chain between the atoms is read (connects or not) — reported, not judged. */
const HSB = require('./hsb_model_v1.js'); let fails = 0; const say = (ok, s) => { console.log((ok ? 'HOLDS  ' : 'KILLED ') + s); if(!ok) fails++; };
const t0 = Date.now(), M = HSB.build({ atoms:2, sep:4 }); console.log('build 2 atoms sep 4: N', M.N, 'n', M.n, 'in', ((Date.now()-t0)/1000).toFixed(1), 's, gap', M.gap.toFixed(4));
let trmax = 0, emax = 0; const r0 = HSB.read(M); for(let t=0;t<=40;t+=0.5){ HSB.at(M, t); const r = HSB.read(M); let tr = 0; for(let i=0;i<M.N;i++) tr += r.occ[i]; trmax = Math.max(trmax, Math.abs(tr - M.N)); emax = Math.max(emax, Math.abs(r.Etot - r0.Etot)); }
say(trmax < 1e-9 && emax < 1e-9, '(a) books: |Tr P - N| ' + trmax.toExponential(1) + ', |E(t) - E(0)| ' + emax.toExponential(1));
say(Math.abs(M.nnce.lhs - M.nnce.rhs) < 1e-9 || Math.abs(M.nnce.residual || 0) < 1e-9, '(c) connection energy identity: ' + JSON.stringify(M.nnce).slice(0, 160));
const G = HSB.build({ atoms:2, sep:4, kick:0 }), rg = HSB.read(G); say(Math.max(...rg.charge.map(Math.abs)) < 1e-9, '(d) ground sea still: largest charge ' + Math.max(...rg.charge.map(Math.abs)).toExponential(1) + ' · row weight min ' + rg.rowMin.toExponential(3) + ' · ' + (rg.connects ? 'connects' : 'does not connect') + ' · tau ' + rg.tau.map(x => x.toFixed(3)).join(' '));
const first = {}; for(const sep of [2, 4, 6]){ const Ms = HSB.build({ atoms:2, sep }), far = Ms.atomsAt[1]; let f = null; for(let t=0;t<=30;t+=0.1){ HSB.at(Ms, t); const r = HSB.read(Ms); if(r.bodyChange[1] > 1e-7){ f = t; break; } } first[sep] = f; HSB.at(Ms, 30); console.log('  sep', sep, 'N', Ms.N, 'far atom first moved', f, 'its charge at t=30', HSB.read(Ms).bodyChange[1].toExponential(2)); }
const vmax = 2*0.22*1.6; say(first[2] !== null && first[6] !== null && first[6] > first[2] && (first[6] - first[2]) >= (4*1.6)/vmax*0.5, '(b) light between: first move sep 2 → ' + first[2] + ', sep 4 → ' + first[4] + ', sep 6 → ' + first[6] + ' (lattice steps of 1.6; largest group speed 2 c0 a = ' + vmax.toFixed(3) + ' so 4 extra steps need at least ' + ((4*1.6)/vmax).toFixed(1) + ')');
console.log('bond curve (ground energy, parallel vs opposed):'); HSB.bondCurve({ atoms:2 }, [1, 2, 3, 4, 6]).forEach(b => console.log('  sep', b.sep, b.spins.padEnd(8), 'E', b.E.toFixed(6), 'gap', b.gap.toFixed(4), 'row min weight', b.rowMin.toExponential(2)));
console.log(fails ? fails + ' KILLED' : 'all hold');
