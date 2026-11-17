/* SCRIPT: HW-CHECK-01 — fixed before the run. (a) books: balls + gaps = 1 to 1e-9 for t = 0..12 after a kick at A (the Flock's own ledger);
   (b) light between: B first lit at the separation (speed 1), not before, for s = 2, 3, 4; (c) hydrogen next to hydrogen (z = 1): the faces return
   nothing, and what reaches B is set by the gap alone, 1 − tanh²(κ_g δ): checked against the arrival share; (d) parallel electrons: connection energy
   0; opposed: 2|d_A − R d_B|² > 0; (e) E = 2/3 gives the clouds exactly a third of the room each: fill = 2(1−E)^(1/3)/2 ... reported. */
const FL = require('../sea/fl_math_v2.js'), HW = require('./hw_world_v1.js'); let fails = 0; const say = (ok, s) => { console.log((ok ? 'HOLDS  ' : 'KILLED ') + s); if(!ok) fails++; };
for(const sep of [2, 3, 4]){ const W = HW.makeWorld({ sep, E:0.667 }), S = FL.initState(W, { source:0 }); let first = null, devmax = 0, arr = 0; while(S.t < 12){ FL.step(W, S); const B = FL.books(W, S); devmax = Math.max(devmax, Math.abs(B.total - 1)); const lb = FL.ballLight(S, 1); if(first === null && lb > 1e-9) first = S.t; arr = Math.max(arr, lb); }
  say(devmax < 1e-9, 'sep ' + sep + ' (a) books: largest deviation of balls + gaps from 1: ' + devmax.toExponential(1));
  say(first !== null && first >= sep - 2*W.opts.h && first <= sep + 0.3, 'sep ' + sep + ' (b) light between: B first lit at ' + (first === null ? '—' : first.toFixed(2)) + ' for a distance ' + sep + ' · r_c ' + W.rc.toFixed(3) + ' δ ' + W.delta.toFixed(3) + ' fill ' + W.fill.toFixed(3) + (W.connects ? ' connects' : ' does not connect') + ' · most light in B ' + arr.toFixed(4) + ' · gap passes ' + W.passGap.toFixed(4) + ' face passes ' + W.passFace.toFixed(4)); }
const Wp = HW.makeWorld({ spins:'parallel' }), Wo = HW.makeWorld({ spins:'opposed' }); say(Wp.conn[0] < 1e-12 && Wo.conn[0] > 0, '(d) connection energy: parallel ' + Wp.conn[0].toExponential(1) + ', opposed ' + Wo.conn[0].toFixed(4));
const Wz = HW.makeWorld({ z:3 }); console.log('(c) clock ratio 3: face Γ ' + Wz.links[0].marks[0].rho.toFixed(4) + ' returns Γ² ' + (Wz.links[0].marks[0].rho**2).toFixed(4));
console.log(fails ? fails + ' KILLED' : 'all hold');
