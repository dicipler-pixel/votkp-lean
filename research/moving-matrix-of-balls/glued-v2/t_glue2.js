// SCRIPT: MM-GLUE-T2 — where the breathing books leak: within-frame drift vs relink jumps
const LH = require('../surprise/src/lh_math.js'), MM = require('../mm/mm_math_v1.js'), G = require('./mm_glue_v1.js');
const P = { zbar:[3,5,7], amp:0.35, T:[8,13,21], ph:[0,2*Math.PI/3,4*Math.PI/3], sigma:1, Tphi:9, Tchi:55 };
for(const noSea of [true,false]){
let W = G.makeWorld(LH.feed(P,0)), St = MM.initState(W, { source:0, noSea }); St.psr.fill(0); St.psi.fill(0);
let tau = 0, inFrame = 0, jumps = 0, worstIn = 0;
for(let f=0;f<300;f++){ tau += 1/60; const a = MM.energies(W, St).E; for(let k=0;k<2;k++) St = MM.rk4(W, St, 1/120); const b = MM.energies(W, St).E; inFrame += b - a; worstIn = Math.max(worstIn, Math.abs(b-a));
  G.relink(W, LH.feed(P, tau)); const c = MM.energies(W, St).E; jumps += c - b; }
let n = 0; St.d.forEach(v => n = Math.max(n, Math.abs(Math.hypot(...v) - 1)));
console.log('noSea', noSea, ' sum in-frame drift', inFrame.toExponential(3), ' worst frame', worstIn.toExponential(2), ' jumps', jumps.toFixed(5), ' |d|-1 worst', n.toExponential(2), ' faces', MM.faceEnergy(W, St.d).E.toFixed(4));
}
