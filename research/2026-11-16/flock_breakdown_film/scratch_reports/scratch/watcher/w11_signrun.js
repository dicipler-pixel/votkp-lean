// SCRIPT: W11-SIGNRUN (watcher) run original and the scratch copy with the two arm-arm face signs reversed; independent of L1/L2 scripts. torque 0 = linear run.
const A = require('/home/claude/balls/w/fl/fl_math_v1.js'), B = require('./fl_math_signflip_copy.js');
for (const torque of [0,1]) { const WA = A.makeWorld({N:3, z:[7,9,11], torque}), WB = B.makeWorld({N:3, z:[7,9,11], torque}), SA = A.initState(WA,{source:1}), SB = B.initState(WB,{source:1});
  for (const T of [3,10,20]) { A.advance(WA,SA,T-SA.t); B.advance(WB,SB,T-SB.t);
    console.log('torque '+torque+' t='+T+' as built '+[0,1,2].map(i=>A.ballLight(SA,i).toFixed(5)).join(' ')+' | reversed '+[0,1,2].map(i=>B.ballLight(SB,i).toFixed(5)).join(' ')+' | books '+A.books(WA,SA).total.toFixed(10)+' '+B.books(WB,SB).total.toFixed(10)); } }
