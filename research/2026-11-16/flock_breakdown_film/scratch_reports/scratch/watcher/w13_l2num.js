// SCRIPT: W13-L2NUM (watcher) reproduce L2's quoted sign-swap numbers (N=3, z=3,5,7, kick A t=40; kick B t=2) with my own scratch copy
const A = require('/home/claude/balls/w/fl/fl_math_v1.js'), B = require('./fl_math_signflip_copy.js');
for (const [src,T] of [[0,40],[1,2]]) { const WA=A.makeWorld({N:3,z:[3,5,7]}), WB=B.makeWorld({N:3,z:[3,5,7]}), SA=A.initState(WA,{source:src}), SB=B.initState(WB,{source:src}); A.advance(WA,SA,T); B.advance(WB,SB,T);
 console.log('kick '+'ABC'[src]+' t='+T+' as written '+[0,1,2].map(i=>A.ballLight(SA,i).toFixed(4)).join(' ')+' | swapped '+[0,1,2].map(i=>B.ballLight(SB,i).toFixed(4)).join(' ')); }
