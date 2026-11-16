// SCRIPT: SR-T1 — checks of the series of ball ends (node)
const LH = require('../surprise/src/lh_math.js'), MM = require('../mm/mm_math_v1.js'), SR = require('./sr_math_v1.js');
const P = { zbar:[3,5,7], amp:0.35, T:[8,13,21], ph:[0,2*Math.PI/3,4*Math.PI/3], sigma:1, Tphi:9, Tchi:55 };
const S = LH.feed(P, 0);
for(const L of [1,2,3]){ const t0 = Date.now(), W = SR.makeWorld(S, L);
  let foot = 0, nrm = 0, dl = 0; W.geo.forEach(G => { foot = Math.max(foot, Math.abs(LH.mink(G.foot, G.N))); nrm = Math.max(nrm, Math.abs(LH.mink(G.N,G.N) + 1)); });
  // pair distance from the drawn planes: |<Ni,Nj>| = cosh(delta) when apart, <= 1 when crossing or kissing
  W.links.forEach(l => { const x = Math.abs(LH.mink(W.geo[l.i].N, W.geo[l.j].N)), del = x > 1 ? Math.acosh(x) : 0; dl = Math.max(dl, Math.abs(del - l.del)); });
  const cnt = {}; W.links.forEach(l => { const k = l.del === 0 ? 'cross/kiss' : 'apart'; cnt[k] = (cnt[k]||0) + 1; });
  console.log('L'+L, 'ends', W.N, 'cells', W.cells.length, 'links', W.links.length, JSON.stringify(cnt), 'tris', W.tris.length, '| foot on its end', foot.toExponential(1), ' |N|', nrm.toExponential(1), ' delta from planes vs formula', dl.toExponential(1), ' build ms', Date.now()-t0);
  const h = W.tris.slice(0,400).map(t => MM.triangleHolonomy(W, t)).filter(Boolean); let hw = 0; h.forEach(x => hw = Math.max(hw, Math.abs(x.ang - x.area))); console.log('   holonomy = area on', h.length, 'loops, worst', hw.toExponential(1));
}
