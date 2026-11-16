// SCRIPT: W02-LONG (watcher) step-size convergence at later times; what the order parameter r really measures; phase rates; sign of arm-arm faces; integrator drift
const FL = require('/home/claude/balls/w/fl/fl_math_v1.js'), FLs = require('./fl_math_signflip_copy.js');
const f = (x,n) => x.toFixed(n==null?3:n);
// (A) convergence in h: light in each ball and r at t = 6, 20, 50, 100 for h = 0.01, 0.005, 0.0025, 0.00125 (N = 3, defaults)
console.log('(A) step-size test, N=3, kick A. light in A,B,C | r');
for(const T of [6, 20, 50, 100]){ for(const h of [0.01,0.005,0.0025,0.00125]){ const W = FL.makeWorld({N:3,h}), S = FL.initState(W,{source:0}); FL.advance(W,S,T); console.log('  t='+T+' h='+h+'  '+[0,1,2].map(i=>f(FL.ballLight(S,i),5)).join(' ')+' | r '+f(FL.order(W,S).r)+' | tilt '+[0,1,2].map(i=>f(FL.tilt(W,S,i))).join(' ')); } }
// (A2) same with the ball fields frozen (torque 0, push off): the linear part alone
console.log('(A2) same, linear part only (torque 0): light in B');
for(const T of [6, 50, 100]){ console.log('  t='+T+'  '+[0.01,0.005,0.0025,0.00125].map(h => { const W = FL.makeWorld({N:3,h,torque:0}), S = FL.initState(W,{source:0}); FL.advance(W,S,T); return 'h='+h+': '+f(FL.ballLight(S,1),5); }).join('   ')); }
// (B) order parameter over t in [200,300]: min, max, mean; unweighted r; r if the phases were random with the same weights; mean phase rate of each ball
console.log('(B) order parameter, t in [200,300], sampled every 0.1');
for(const [nm, F] of [['as delivered', FL], ['arm-arm face signs reversed', FLs]]) for(const N of [3,4,7]) for(const clocks of ['z','equal']){ const W = F.makeWorld({N,clocks}), S = F.initState(W,{source:0}); F.advance(W,S,200);
  let rs=[], ru=[], rr=[], last = W.balls.map((_,i)=>F.clockPhase(S,i).phase), tot = new Array(W.N).fill(0), mx = new Array(W.N).fill(0), av = new Array(W.N).fill(0), seed=7; const rnd=()=> (seed=(seed*16807)%2147483647)/2147483647;
  for(let k=0;k<20000;k++){ F.step(W,S); const o = F.order(W,S); for(let i=0;i<W.N;i++){ let dp = o.phases[i].phase-last[i]; while(dp>Math.PI) dp-=2*Math.PI; while(dp<-Math.PI) dp+=2*Math.PI; tot[i]+=dp; last[i]=o.phases[i].phase; const e=F.ballLight(S,i); mx[i]=Math.max(mx[i],e); av[i]+=e/20000; }
    if(k%20===0){ rs.push(o.r); let c=0,s=0; o.phases.forEach(p=>{c+=Math.cos(p.phase); s+=Math.sin(p.phase);}); ru.push(Math.hypot(c,s)/W.N); let c2=0,s2=0,w=0; o.phases.forEach(p=>{ const a=2*Math.PI*rnd(); c2+=p.weight*Math.cos(a); s2+=p.weight*Math.sin(a); w+=p.weight; }); rr.push(Math.hypot(c2,s2)/w); } }
  const st = a => { const m=a.reduce((x,y)=>x+y,0)/a.length; return f(m)+' ['+f(Math.min(...a),2)+', '+f(Math.max(...a),2)+']'; };
  console.log('  '+nm+' N='+N+' '+clocks.padEnd(5)+' | r weighted '+st(rs)+' | r unweighted '+st(ru)+' | SAME WEIGHTS, RANDOM PHASES '+st(rr)+' | phase rates '+tot.map(x=>f(x/100,3)).join(' ')+' | own rates '+W.balls.map(b=>f(2*b.rate,3)).join(' ')+' | mean share '+av.map(x=>f(x,3)).join(' ')); }
// (C) integrator drift of a tipped field, static push, no light: growth vs h
console.log('(C) B tipped 1e-3 rad, static push, no light: tilt of B at t = 0, 100, 200');
for(const h of [0.01,0.005,0.0025]){ const W = FL.makeWorld({N:7,h}), S = FL.initState(W,{}); const d=S.d[1], m=Math.hypot(...d), e=[1,0,0], p=[d[1]*e[2]-d[2]*e[1], d[2]*e[0]-d[0]*e[2], d[0]*e[1]-d[1]*e[0]], pm=Math.hypot(...p); for(let a=0;a<3;a++) d[a]+=1e-3*m*p[a]/pm; const m2=Math.hypot(...d); for(let a=0;a<3;a++) d[a]*=m/m2; const o=[FL.tilt(W,S,1)]; FL.advance(W,S,100); o.push(FL.tilt(W,S,1)); FL.advance(W,S,100); o.push(FL.tilt(W,S,1)); console.log('  h='+h+': '+o.map(x=>x.toExponential(3)).join('  ')); }
// (D) retarded push: how far by t = 100, 150, 200, N = 3, 4, 7
console.log('(D) retarded push, no light: largest tilt (rad; pi = half turn is the most this measure can read)');
for(const N of [3,4,7]){ const W = FL.makeWorld({N,push:'retarded'}), S = FL.initState(W,{}); const o=[]; for(const T of [50,100,150,200]){ FL.advance(W,S,50); o.push('t='+T+': '+Math.max(...W.balls.map((_,i)=>FL.tilt(W,S,i))).toExponential(2)); } console.log('  N='+N+'  '+o.join('  ')); }
