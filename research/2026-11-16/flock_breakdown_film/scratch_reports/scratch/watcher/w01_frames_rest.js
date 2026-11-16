// SCRIPT: W01-FRAMES-REST  (watcher) frame consistency of U vs R, rest drift with a measure that can see small angles, K6 floor, g=1 continuity, arm-arm travel time
const MM = require('/home/claude/balls/w/mm/mm_math_v1.js'), FL = require('/home/claude/balls/w/fl/fl_math_v1.js');
// (1) U sigma.v U^dag = sigma.(R v) ?  or with R^T ?
{ const W = FL.makeWorld({N:7}); let worstA = 0, worstB = 0;
  const sig = v => [[v[2],0],[v[0],-v[1]],[v[0],v[1]],[-v[2],0]]; // [re,im] entries 00,01,10,11
  const mul = (A,B) => { const C=[]; for(let r=0;r<2;r++)for(let c=0;c<2;c++){ let re=0,im=0; for(let k=0;k<2;k++){ const a=A[2*r+k], b=B[2*k+c]; re+=a[0]*b[0]-a[1]*b[1]; im+=a[0]*b[1]+a[1]*b[0]; } C.push([re,im]); } return C; };
  const dag = A => [[A[0][0],-A[0][1]],[A[2][0],-A[2][1]],[A[1][0],-A[1][1]],[A[3][0],-A[3][1]]];
  for(const l of W.links){ const v=[0.3,-0.5,0.8], L = mul(mul(l.U, sig(v)), dag(l.U)), a = sig(MM.v3(l.R, v)), b = sig(MM.v3(MM.T3(l.R), v));
    let ea=0, eb=0; for(let k=0;k<4;k++){ ea=Math.max(ea,Math.abs(L[k][0]-a[k][0]),Math.abs(L[k][1]-a[k][1])); eb=Math.max(eb,Math.abs(L[k][0]-b[k][0]),Math.abs(L[k][1]-b[k][1])); } worstA=Math.max(worstA,ea); worstB=Math.max(worstB,eb); }
  console.log('U sig.v U^dag vs sig.(R v): worst', worstA.toExponential(2), ' vs sig.(R^T v): worst', worstB.toExponential(2));
  console.log('link rotation angles (rad):', W.links.map(l => MM.rotAngle(l.R).toFixed(3)).join(' ')); }
// (2) rest drift measured with |a x b|/(|a||b|) instead of acos
{ const W = FL.makeWorld({N:7}), S = FL.initState(W, {}); const ang = i => { const a=S.d[i], b=W.dRest[i], c=[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]; return Math.hypot(...c)/(Math.hypot(...a)*Math.hypot(...b)); };
  for(let k=0;k<10000;k++) FL.step(W,S); console.log('rest, N=7, t=50: largest turn by cross product', Math.max(...W.balls.map((_,i)=>ang(i))).toExponential(2), ' (acos tilt reads', Math.max(...W.balls.map((_,i)=>FL.tilt(W,S,i))).toExponential(2)+')', 'rest residual', W.restResidual.toExponential(2));
  console.log('smallest angle acos can report: acos(1-1.1e-16) =', Math.acos(1-1.1102230246251565e-16).toExponential(2));
  // perturb: tip ball B field by 1e-3 rad, static push, no light: does it grow, hold, or decay?
  const S2 = FL.initState(W, {}); const d = S2.d[1], m = Math.hypot(...d); const e = Math.abs(d[0])<0.9*m ? [1,0,0]:[0,1,0]; const p = [d[1]*e[2]-d[2]*e[1], d[2]*e[0]-d[0]*e[2], d[0]*e[1]-d[1]*e[0]]; const pm = Math.hypot(...p); for(let a=0;a<3;a++) d[a] += 1e-3*m*p[a]/pm; const mm2 = Math.hypot(...d); for(let a=0;a<3;a++) d[a]*=m/mm2;
  const out=[]; for(let k=0;k<=40000;k++){ if(k%10000===0) out.push('t='+S2.t.toFixed(0)+': '+W.balls.map((_,i)=>FL.tilt(W,S2,i).toExponential(1)).join(' ')); FL.step(W,S2); } console.log('static push, B tipped 1e-3 rad, no light: tilt of A..G\n  '+out.join('\n  ')); }
// (3) continuity at the wall g = 1: z just below and above
for(const eps of [-1e-3,-1e-6,0,1e-6,1e-3,1e-2]){ const zz = 3+2*Math.SQRT2+eps, W = FL.makeWorld({N:3, z:[zz,zz,7], gamma:0}), l = W.links[2]; let t=1; l.marks.forEach(m => t*= (1-m.rho*m.rho)); console.log('z = 5.8284271+('+eps+')  g =', l.g.toFixed(9), ' marks', l.marks.length, ' delta', (l.delta||0).toExponential(3), ' first-pass T =', t.toFixed(9)); }
// (4) arm-arm travel time: kick B in N=3, when does C first hold light? (direct link B-C length vs via A)
{ const W = FL.makeWorld({N:3}), S = FL.initState(W, {source:1}); let first=null; for(let k=0;k<1500&&first===null;k++){ FL.step(W,S); if(FL.ballLight(S,2)>1e-30) first=S.t; } const l=W.links[2]; console.log('kick B: first light in C at t =', first.toFixed(4), ' B-C link d =', l.d.toFixed(4), ' samples', l.segs.map(s=>s.n).join('+'), '=', l.segs.reduce((a,s)=>a+s.n,0), ' x h =', (l.segs.reduce((a,s)=>a+s.n,0)*W.opts.h).toFixed(4), ' seg true lengths', l.segs.map(s=>s.len.toFixed(4)).join(' '), ' nTot', l.nTot); 
  for(const l of FL.makeWorld({N:7}).links) { const ns=l.segs.reduce((a,s)=>a+s.n,0); if(Math.abs(ns*0.005-l.d)>0.004) console.log('  N=7 link',l.i,l.j,'d',l.d.toFixed(4),'delay',(ns*0.005).toFixed(4),'err',(ns*0.005-l.d).toFixed(4),'nTot*h',(l.nTot*0.005).toFixed(4)); } }
