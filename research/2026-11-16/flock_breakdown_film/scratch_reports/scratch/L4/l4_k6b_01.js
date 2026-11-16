// SCRIPT: L4-K6B-01
// Why the retarded face push (fl_math_v1.js line 93, push 'retarded') is unstable at rest.
// Hand derivation (two balls, equal fields D along z, R = identity, no light, small transverse tilt delta = x + i y, a = 2 kappa D):
//   step (c): d' = G x d, G = 2 kappa (d_i - d_j(t - tau))   =>   delta_i' = -i a (delta_i - delta_j(t - tau)).
//   Antisymmetric mode delta_1 = -delta_2:  lambda = -i a (1 + exp(-lambda tau)).  tau = 0 gives lambda = -2 i a (a pure precession, no growth);
//   first order in tau: Re lambda = +2 a^2 tau  (> 0). Symmetric mode: lambda = -i a (1 - exp(-lambda tau)) keeps lambda = 0 (rigid turn).
// PART A tests the formula: standalone two-ball integrator with the SAME rotation update as line 94-95 and a ring-buffer delay of n steps
//   (read before write, as lines 93 and 96, so the delay is exactly n h). Measured growth rate of |delta| against the root of the characteristic
//   equation found by Newton iteration from lambda = -2 i a.
//   KILL LINE A (written first): the measured growth rate differs from Re lambda by more than 5 percent (relative) or 1e-4 (absolute) at any tau
//   in the list, or growth at n = 0 is not zero within 1e-6.
// PART B tests the cause inside the real code (scratch copy, option delayScale scales the delay: nTot = max(1, round(delayScale d / h))).
//   A 1e-6 tilt is put on every ball field, no light, push 'retarded'; the largest tilt over each 200 steps is fitted (ln against t) between 1e-5 and 1e-1.
//   KILL LINE B (written first): the delay explanation is killed if the growth rate at delayScale 0.05 is more than half the rate at delayScale 1,
//   or if the rate is not non-decreasing in delayScale over 0.05, 0.1, 0.25, 0.5. Controls: push 'static' and 'off' under the same tilt must not grow
//   (largest tilt stays below 1e-5 for the whole run).
const FLs = require('./fl_math_scratch.js');
function partA(){
  const kappa=0.25, D=1.0, a=2*kappa*D, h=0.005;
  console.log('PART A: two balls, a = 2 kappa D = '+a);
  for(const tau of [0,0.05,0.1,0.2,0.5,1.0,2.0]){
    const n=Math.round(tau/h);
    // Newton for lambda = -i a (1 + exp(-lambda tau)), complex arithmetic by hand
    let lr=0, li=-2*a; for(let k=0;k<200;k++){ const e=Math.exp(-lr*tau), er=e*Math.cos(li*tau), ei=-e*Math.sin(li*tau);   // exp(-lambda tau)
      const fr=lr-(a*(1+er)*0)-( a*ei*1), fi=li+a*(1+er);   // f = lambda + i a (1+E): real = lr - a*ei ... see below
      // f = lambda + i a (1 + E) = (lr + i li) + i a (1+er) + i a i ei = (lr - a ei) + i (li + a (1+er))
      const Fr=lr-a*ei, Fi=li+a*(1+er);
      // f' = 1 - i a tau E = 1 - i a tau (er + i ei) = (1 + a tau ei) - i a tau er
      const dr=1+a*tau*ei, di=-a*tau*er, den=dr*dr+di*di, sr=(Fr*dr+Fi*di)/den, si=(Fi*dr-Fr*di)/den; lr-=sr; li-=si; if(Math.hypot(sr,si)<1e-14) break; }
    // integrate
    const N=2, d=[[1e-6,0,D],[-1e-6,0,D]].map(v=>{ const m=Math.hypot(...v); return v.map(x=>x/m*D); });
    const hist=[[],[]]; for(let k=0;k<Math.max(n,1);k++){ hist[0].push(d[0].slice()); hist[1].push(d[1].slice()); }
    let head=0, cur=d.map(v=>v.slice()); const env=[]; const steps=Math.round(Math.max(60/Math.max(Math.abs(lr),0.02),40)/h);
    const T=Math.min(steps*h, 400);
    for(let k=0;k<Math.round(T/h);k++){
      const nd=[];
      for(let i=0;i<2;i++){ const j=1-i; const dj = n===0 ? cur[j] : hist[j][head]; const G=[2*kappa*(cur[i][0]-dj[0]),2*kappa*(cur[i][1]-dj[1]),2*kappa*(cur[i][2]-dj[2])];
        const g=Math.hypot(...G); if(g<1e-300){ nd.push(cur[i].slice()); continue; } const u=G.map(x=>x/g), an=g*h, ca=Math.cos(an), sa=Math.sin(an), di=cur[i], ud=u[0]*di[0]+u[1]*di[1]+u[2]*di[2], cx=[u[1]*di[2]-u[2]*di[1],u[2]*di[0]-u[0]*di[2],u[0]*di[1]-u[1]*di[0]];
        nd.push([0,1,2].map(q=>di[q]*ca+cx[q]*sa+u[q]*ud*(1-ca))); }
      if(n>0){ hist[0][head]=cur[0].slice(); hist[1][head]=cur[1].slice(); head=(head+1)%n; }
      cur=nd; if(k%40===0) env.push([ (k+1)*h, Math.hypot(cur[0][0],cur[0][1]) ]); }
    // growth rate: least squares of ln of the running maximum of |delta| in blocks of 5 samples, between 1e-5 and 1e-1 (or whole run if no growth)
    const blocks=[]; for(let k=0;k+5<=env.length;k+=5){ blocks.push([env[k][0], Math.log(Math.max(...env.slice(k,k+5).map(e=>e[1])))]); }
    const sel=blocks.filter(b=>b[1]>Math.log(1e-5)&&b[1]<Math.log(1e-1)); const use=sel.length>=6?sel:blocks;
    let sx=0,sy=0,sxx=0,sxy=0,m=use.length; use.forEach(([x,y])=>{sx+=x;sy+=y;sxx+=x*x;sxy+=x*y;}); const rate=(m*sxy-sx*sy)/(m*sxx-sx*sx);
    const pred=lr, rel=Math.abs(rate-pred)/Math.max(Math.abs(pred),1e-12), ok = n===0 ? Math.abs(rate)<1e-6 : (rel<0.05||Math.abs(rate-pred)<1e-4);
    console.log('  tau='+tau.toFixed(3)+' (n='+n+')  predicted Re lambda = '+pred.toExponential(4)+'  (Im '+li.toFixed(4)+'; small-tau formula 2 a^2 tau = '+(2*a*a*tau).toExponential(3)+')  measured rate = '+rate.toExponential(4)+'  '+(ok?'agrees':'KILLED'));
  } }
function tiltGrow(P, T){
  const W=FLs.makeWorld(P), S=FLs.initState(W,{}); // no light
  for(let i=0;i<W.N;i++){ const d=S.d[i], m=Math.hypot(...d), v=[d[0]+1e-6*m*0.7, d[1]-1e-6*m*0.4, d[2]]; const mm=Math.hypot(...v); S.d[i]=v.map(x=>x/mm*m); }
  const blocks=[]; let mx=0, peak=0; const steps=Math.round(T/P.h);
  for(let k=0;k<steps;k++){ FLs.step(W,S); let t=0; for(let i=0;i<W.N;i++) t=Math.max(t,FLs.tilt(W,S,i)); mx=Math.max(mx,t); peak=Math.max(peak,t); if((k+1)%200===0){ blocks.push([S.t,Math.log(Math.max(mx,1e-300))]); mx=0; if(peak>0.5) break; } }
  const sel=blocks.filter(b=>b[1]>Math.log(1e-5)&&b[1]<Math.log(1e-1)); if(sel.length<4) return { rate:NaN, peak, nsel:sel.length, delay:W.links.map(l=>l.nTot*P.h) };
  let sx=0,sy=0,sxx=0,sxy=0,m=sel.length; sel.forEach(([x,y])=>{sx+=x;sy+=y;sxx+=x*x;sxy+=x*y;}); return { rate:(m*sxy-sx*sy)/(m*sxx-sx*sx), peak, nsel:sel.length, delay:W.links.map(l=>l.nTot*P.h) }; }
function partB(){
  console.log('PART B: real code (scratch copy), 1e-6 tilt on every ball field, no light');
  for(const N of [3,7]){ const res={};
    for(const ds of [0.02,0.05,0.1,0.25,0.5,1,2]){ const r=tiltGrow({N,push:'retarded',delayScale:ds,h:0.005}, N===3?600:300); res[ds]=r;
      console.log('  N='+N+' retarded delayScale='+ds+'  link delays '+r.delay.map(x=>x.toFixed(2)).join(',')+'  growth rate (1/time) '+(Number.isNaN(r.rate)?'no growth window (peak tilt '+r.peak.toExponential(1)+')':r.rate.toFixed(4))+'  peak tilt '+r.peak.toExponential(2)); }
    const lo=res[0.05].rate, hi=res[1].rate; const mono=[0.05,0.1,0.25,0.5].every((x,k,arr)=>k===0||(res[x].rate>=res[arr[k-1]].rate-1e-9||Number.isNaN(res[arr[k-1]].rate)));
    console.log('  N='+N+' KILL B check: rate(0.05) = '+lo+', rate(1) = '+hi+', half of rate(1) = '+(hi/2)+' -> '+((lo>hi/2||!mono)?'KILLED':'delay explanation stands')+'; monotone on 0.05..0.5: '+mono);
    for(const push of ['static','off']){ const r=tiltGrow({N,push,h:0.005},200); console.log('  N='+N+' control push '+push+': peak tilt over t=200 '+r.peak.toExponential(2)+(r.peak<1e-5?'  (no growth, as required)':'  (CONTROL FAILED)')); } } }
partA(); partB();
