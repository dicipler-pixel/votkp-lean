// SCRIPT: L4-SYNC-02
// L4-SYNC-01 plus: (i) sign switch for the arm-arm faces (sign = 'asis' uses lines 50-51 as written; 'swap' uses first face -Gamma_a, second +Gamma_b),
// (ii) a sink: ball sinkBall gets an extra absorbing port at rate sinkRate (the 'absorbing end'), (iii) a surrogate control for r.
// Run: node l4_sync_02.js '{"N":3,"clocks":"z","torque":1,"gamma":0.3,"gloss":0,"sign":"asis","sinkBall":-1,"sinkRate":0,"T":400,"h":0.005}'
// KILL LINE 1 (written before the SYNC-01 sweep, unchanged): a pair i,j is LOCKED only if in BOTH of the last two windows their measured rates
// agree within 0.01*omega (= 0.02), AND either (clocks z) their free rates differ by more than that, or (clocks equal) the s.d. of their
// unwrapped phase difference over the last half is below 0.5 rad with torque on while it is above 0.5 rad in the matching torque-off run.
// KILL LINE 2 (written BEFORE the SYNC-02 runs, after seeing that minW in the SYNC-01 rows was ~1e-4: phases of a ball holding almost no light are noise):
// a cell is called LOCKED only if some pair meets line 1 AND both balls of that pair have weight > 0.02 in at least half of the last-half samples
// AND the cell's mean r exceeds the mean r of 300 time-shift surrogates (each ball's phase series circularly shifted by an independent random amount,
// weights shifted with it) by more than 3 surrogate standard deviations. Otherwise NO LOCK.
const P=Object.assign({N:3,clocks:'z',torque:1,gamma:0.3,gloss:0,sign:'asis',sinkBall:-1,sinkRate:0,T:400,h:0.005,kappa:0.25},JSON.parse(process.argv[2]||'{}'));
const {N,clocks,torque,gamma,gloss,T,h}=P;
const FL = require(path_(P));
function path_(P){ return (P.gloss>0||P.sign==='swap'||P.sinkRate>0) ? './fl_math_scratch.js' : '/home/claude/balls/w/fl/fl_math_v1.js'; }
const W=FL.makeWorld({N,clocks,torque,gamma,h,gloss,kappa:P.kappa,signSwap:P.sign==='swap',sinkBall:P.sinkBall,sinkRate:P.sinkRate}), S=FL.initState(W,{source:(P.source||0)}), n=W.N;
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
let sd_=12345; const rn=()=> (sd_=(sd_*16807)%2147483647)/2147483647; const K=half.length, sur=[];
for(let q=0;q<300;q++){ const sh=Array.from({length:n},()=>Math.floor(rn()*K)); let cr=0,ci=0,ww=0; const kk=Math.floor(rn()*K); for(let a=0;a<K;a++){ cr=0;ci=0;ww=0; } 
  let sum=0,cnt=0; for(let a=0;a<K;a+=10){ let cr2=0,ci2=0,w2=0; for(let i=0;i<n;i++){ const k=half[(a+sh[i])%K]; cr2+=wt[i][k]*Math.cos(ph[i][k]); ci2+=wt[i][k]*Math.sin(ph[i][k]); w2+=wt[i][k]; } sum+= w2>1e-12?Math.hypot(cr2,ci2)/w2:0; cnt++; } sur.push(sum/cnt); }
const sm=sur.reduce((a,x)=>a+x,0)/sur.length, ssd=Math.sqrt(sur.reduce((a,x)=>a+(x-sm)**2,0)/sur.length);
const eps=0.01*W.opts.omega;
const heavy=(i)=>half.filter(k=>wt[i][k]>0.02).length/K;
const kl1=pairs.filter(p=>p.dr[0]<eps&&p.dr[1]<eps&&(clocks==='z'?p.dfree>eps:p.sd<0.5)).map(p=>[p.i,p.j]);
const kl2=kl1.filter(([i,j])=>heavy(i)>=0.5&&heavy(j)>=0.5);
const rExcess=(rm-sm)/ssd, rOK=rm>sm+3*ssd;
const verdict1=kl1.length>0?'pairs '+JSON.stringify(kl1):'NO LOCK', verdict2=(kl2.length>0&&rOK)?'LOCKED pairs '+JSON.stringify(kl2):'NO LOCK';
console.log(JSON.stringify({P,spec,free,rates,rMean:rm,rSd:rsd,surMean:sm,surSd:ssd,rExcess,pairs,heavy:Array.from({length:n},(_,i)=>heavy(i)),maxTilt,book:worstBook,lightLeft:b.total,lost:S.lost||0,minW,verdict1,verdict2}));
