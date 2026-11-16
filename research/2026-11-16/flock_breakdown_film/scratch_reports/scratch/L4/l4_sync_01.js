// SCRIPT: L4-SYNC-01
// Does the flock lock? One run per call: node l4_sync_01.js N clocks torque gamma gloss [T] [h]
// Readouts: each ball's MEASURED clock rate = slope of its unwrapped clock phase (FL.clockPhase) over a window, by least squares;
// the Kuramoto order parameter r (weighted, FL.order) mean and spread; spread of each pair's phase difference.
// Why the rate decides it: locked clocks run at ONE common rate (or in a fixed whole-number ratio) that differs from their free rates,
// and stay so from window to window. Unlocked clocks keep rates near their own free rates or wander between windows.
// ADDED after the first timing run and L4-ISO-01 (FL.clockPhase is measured in a frame tied to the ball field, which tilts under torque):
// a second, frame-free clock: the spectrum of each ball's amplitude along the up and down states of its REST field over the last half;
// peak frequencies nu_up, nu_dn (convention exp(-i nu t)); a free ball has nu_up = +omega rate/2, nu_dn = -omega rate/2.
// KILL LINE (written before any run): a pair i,j is called LOCKED only if in BOTH of the last two windows their measured rates
// agree within 0.01*omega, AND either (clocks z) their free rates differ by more than that, or (clocks equal) the spread (s.d.) of
// their unwrapped phase difference over the last half of the run is below 0.5 rad with torque on while it is above 0.5 rad in the
// matching torque-off run. If no pair meets it, the cell is NO LOCK. gloss = 0 uses the original fl_math_v1.js.
const [N,clocks,torque,gamma,gloss,T,h]=[+process.argv[2],process.argv[3],+process.argv[4],+process.argv[5],+process.argv[6],+(process.argv[7]||400),+(process.argv[8]||0.01)];
const FL = require(gloss>0 ? './fl_math_scratch.js' : '/home/claude/balls/w/fl/fl_math_v1.js');
const W=FL.makeWorld({N,clocks,torque,gamma,h,gloss}), S=FL.initState(W,{source:0}), n=W.N;
const every=Math.max(1,Math.round(0.05/h)), ts=[], ph=Array.from({length:n},()=>[]), wt=Array.from({length:n},()=>[]), rs=[], last=new Array(n).fill(null), acc=new Array(n).fill(0);
let maxTilt=0, worstBook=0;
const ups=W.dRest.map(d=>{ const m=Math.hypot(...d), th=Math.acos(d[2]/m), p=Math.atan2(d[1],d[0]); return { up:[Math.cos(th/2),0,Math.sin(th/2)*Math.cos(p),Math.sin(th/2)*Math.sin(p)], dn:[-Math.sin(th/2)*Math.cos(p),Math.sin(th/2)*Math.sin(p),Math.cos(th/2),0] }; });
const ip=(a,x)=>[a[0]*x[0]+a[1]*x[1]+a[2]*x[2]+a[3]*x[3], a[0]*x[1]-a[1]*x[0]+a[2]*x[3]-a[3]*x[2]];
const cu=Array.from({length:n},()=>[]), cd=Array.from({length:n},()=>[]);
const steps=Math.round(T/h);
for(let k=0;k<steps;k++){ FL.step(W,S); if(k%every===0){ ts.push(S.t); const o=FL.order(W,S); rs.push(o.r); for(let i=0;i<n;i++){ const p=o.phases[i].phase; if(last[i]!==null){ let dp=p-last[i]; while(dp>Math.PI) dp-=2*Math.PI; while(dp<-Math.PI) dp+=2*Math.PI; acc[i]+=dp; } last[i]=p; ph[i].push(acc[i]); wt[i].push(o.phases[i].weight); maxTilt=Math.max(maxTilt,FL.tilt(W,S,i)); cu[i].push(ip(ups[i].up,S.psi[i])); cd[i].push(ip(ups[i].dn,S.psi[i])); } } }
const b=FL.books(W,S); worstBook=Math.abs(b.total+(S.lost||0)-1);
function slope(i,t0,t1){ let sx=0,sy=0,sxx=0,sxy=0,m=0; for(let k=0;k<ts.length;k++) if(ts[k]>=t0&&ts[k]<t1){ sx+=ts[k]; sy+=ph[i][k]; sxx+=ts[k]*ts[k]; sxy+=ts[k]*ph[i][k]; m++; } return (m*sxy-sx*sy)/(m*sxx-sx*sx); }
const wins=[[T/2,3*T/4],[3*T/4,T]], rates=wins.map(w=>Array.from({length:n},(_,i)=>slope(i,w[0],w[1]))), free=W.balls.map(x=>W.opts.omega*x.rate);
const half=ts.map((t,k)=>k).filter(k=>ts[k]>=T/2), rm=half.reduce((a,k)=>a+rs[k],0)/half.length, rsd=Math.sqrt(half.reduce((a,k)=>a+(rs[k]-rm)**2,0)/half.length);
const pairs=[]; for(let i=0;i<n;i++) for(let j=i+1;j<n;j++){ const dd=half.map(k=>ph[i][k]-ph[j][k]), m=dd.reduce((a,x)=>a+x,0)/dd.length, sd=Math.sqrt(dd.reduce((a,x)=>a+(x-m)**2,0)/dd.length);
  pairs.push({i,j,sd,dr:[Math.abs(rates[0][i]-rates[0][j]),Math.abs(rates[1][i]-rates[1][j])],dfree:Math.abs(free[i]-free[j])}); }
const minW=wt.map(a=>Math.min(...half.map(k=>a[k])));
function peak(sig){ const K=half.length; let best=[0,0], tot=0; const P=[]; for(let q=-600;q<=600;q++){ const nu=q*0.005; let re=0,im=0; for(let a=0;a<K;a++){ const k=half[a], w=0.5-0.5*Math.cos(2*Math.PI*a/(K-1)), c=Math.cos(nu*ts[k]), s=Math.sin(nu*ts[k]); re+=w*(sig[k][0]*c-sig[k][1]*s); im+=w*(sig[k][0]*s+sig[k][1]*c); } const p=re*re+im*im; P.push(p); tot+=p; if(p>best[1]) best=[nu,p]; } return { nu:best[0], frac:best[1]/tot }; }
const spec=Array.from({length:n},(_,i)=>({up:peak(cu[i]),dn:peak(cd[i])}));
console.log(JSON.stringify({spec,N,clocks,torque,gamma,gloss,T,h,free,rates,rMean:rm,rSd:rsd,pairs,maxTilt,book:worstBook,lightLeft:b.total,minW}));
