// SCRIPT: L1-SIGN-CHECK-02
// Does the sign convention of the marks on an arm-arm link change the run? FL-MATH-V1 read-only; marks changed in memory only.
// Why it decides: K3 and K4 measure squared first-pass fractions, which do not see a sign. If the ball light changes when the signs change,
// the sign is physical (it sets how face echoes meet the port echoes) and needs a source.
const FL = require('/home/claude/balls/w/fl/fl_math_v1.js');
const variants = { 'as built (+a, +gap, -b)':m => m.rho, 'faces negated (-a, +gap, +b)':m => m.kind === 'face' ? -m.rho : m.rho, 'all negated (-a, -gap, +b)':m => -m.rho, 'gap negated (+a, -gap, -b)':m => m.kind === 'gap' ? -m.rho : m.rho };
for(const torque of [1, 0]){ console.log('torque = '+torque+' (0: ball fields do not turn under the light, so the run is linear)   kick B, z = 7, 9, 11, light in A B C');
  for(const name in variants){ const W = FL.makeWorld({ N:3, z:[7,9,11], torque }); W.links[2].marks.forEach(m => m.rho = variants[name](m)); const S = FL.initState(W, { source:1 }); const out = [];
    for(const T of [3, 5, 10, 20]){ FL.advance(W, S, T - S.t); out.push('t='+T+': '+[0,1,2].map(i => FL.ballLight(S,i).toFixed(5)).join(' ')); }
    console.log('  '+name.padEnd(30)+out.join(' | ')+' | books '+FL.books(W,S).total.toFixed(12)); } }
// closed form of the gap at kgap = 1: sech(arccosh g) = 1/g, g = sinh(ra/2) sinh(rb/2), and sinh^2(r/2) = R/T.
for(const [za, zb] of [[5,7],[7,9],[9,13]]){ const G = z => (z-1)/(z+1), Ra = G(za)**2, Rb = G(zb)**2, Ta = 1-Ra, Tb = 1-Rb, g2 = (Ra/Ta)*(Rb/Tb), g = Math.sinh(Math.log(za)/2)*Math.sinh(Math.log(zb)/2);
  console.log('z = '+za+','+zb+': g^2 = '+(g*g).toFixed(10)+', (Ra/Ta)(Rb/Tb) = '+g2.toFixed(10)+', gap passes 1/g^2 = '+(1/g2).toFixed(10)+', sech^2(arccosh g) = '+(1/Math.cosh(Math.acosh(g))**2).toFixed(10)+', first pass (Ta Tb)^2/(Ra Rb) = '+((Ta*Tb)**2/(Ra*Rb)).toFixed(10)); }
