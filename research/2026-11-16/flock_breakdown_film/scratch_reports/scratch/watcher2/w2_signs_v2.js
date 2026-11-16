// SCRIPT: W2-SIGNS-V2 (watcher phase 2). Kill: page 4.1 numbers (0.0325/0.4212 ; 0.1136/0.3250) must come out of fl_math_v2 armSign options; v2 default must equal reversed v1.
const V1=require('/home/claude/balls/w/fl/fl_math_v1.js'), V2=require('/home/claude/balls/w/fl/fl_math_v2.js');
function run(F,opts,src,T){const W=F.makeWorld(opts),S=F.initState(W,{source:src});F.advance(W,S,T);return [0,1,2].map(i=>F.ballLight(S,i).toFixed(4)).join(' ')+' books '+F.books(W,S).total.toFixed(10);}
console.log('A) N3 z7,9,11 kick B torque0 t=3');
console.log(' v1      ',run(V1,{N:3,z:[7,9,11],torque:0},1,3));
console.log(' v2 asBuiltV1',run(V2,{N:3,z:[7,9,11],torque:0,armSign:'asBuiltV1'},1,3));
console.log(' v2 default  ',run(V2,{N:3,z:[7,9,11],torque:0},1,3));
console.log('B) N3 z3,5,7 kick B t=2 (torque default)');
console.log(' v1      ',run(V1,{N:3,z:[3,5,7]},1,2));
console.log(' v2 asBuiltV1',run(V2,{N:3,z:[3,5,7],armSign:'asBuiltV1'},1,2));
console.log(' v2 default  ',run(V2,{N:3,z:[3,5,7]},1,2));
console.log('C) default push check');
console.log(V2.makeWorld({}).opts.push, V2.makeWorld({}).opts.armSign);
