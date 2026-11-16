// SCRIPT: L3-RUN-03
// Reproduce the README loop number 0.7110545751 at tau = 0 (steps from the single-ball feed, as t_tb1.js line 3-4), plus t_tb1's connection energy line.
const MM = require('/home/claude/balls/w/mm/mm_math_v1.js'), TB = require('/home/claude/balls/w/tb/tb_math_v1.js');
const LH = require('/home/claude/balls/in/367c3aed-Light_at_the_Hypersurface_Mixer_v2_Source/lh_math_v1.js');
const P = { zbar:[3,5,7], amp:0.35, T:[8,13,21], ph:[0,2*Math.PI/3,4*Math.PI/3], sigma:1, Tphi:9, Tchi:55 };
const r0 = LH.feedLite(P, 0).r; console.log('feedLite r(0) =', r0.map(x => x.toFixed(10)).join(', '), ' z =', r0.map(x => Math.exp(x).toFixed(6)).join(', '));
const W = TB.makeWorld(r0), lp = TB.loop(W, r0);
console.log('loop: turn', lp.ang.toFixed(10), ' area', lp.area.toFixed(10), ' Thomas 2atan(G_I G_J)', lp.thomas.toFixed(10), ' README 0.7110545751');
console.log('cosh d_BC - cosh r_I cosh r_J', (Math.cosh(W.links[2].d) - Math.cosh(r0[0])*Math.cosh(r0[1])).toExponential(1));
const nn = MM.nnceCheck(W, W.d); console.log('connection energy at rest: lhs', nn.lhs.toExponential(3), ' rhs', nn.rhs.toExponential(3), ' rest residual', W.restResidual.toExponential(1));
const Md = TB.modes(W, W.d); console.log('eigenvalues', Md.vals.map(x => x.toFixed(3)).join(' '), ' leading shares', Md.share[Md.lead].map(x => x.toFixed(3)).join(' '), ' margin', Md.margin.toFixed(3));
