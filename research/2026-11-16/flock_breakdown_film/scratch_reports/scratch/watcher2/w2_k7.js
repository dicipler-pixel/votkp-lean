// SCRIPT: W2-K7 K7 numbers for v1 and v2 at t=6 and t=20
const V1=require('/home/claude/balls/w/fl/fl_math_v1.js'), V2=require('/home/claude/balls/w/fl/fl_math_v2.js');
for(const [n,F] of [['v1',V1],['v2',V2]]) for(const T of [6,20]){const o=[];for(const h of [0.01,0.005,0.0025]){const W=F.makeWorld({N:3,h});const S=F.initState(W,{source:0});F.advance(W,S,T);o.push(F.ballLight(S,1).toFixed(5));}console.log(n,'T',T,o.join(' '));}
