// SCRIPT: L4-KURA-CTRL-01
// Positive and negative control for the rate test of kill line 1, on a system where the answer is known: three Kuramoto phase oscillators with delay (Yeung-Strogatz form)
//   theta_i' = w_i + (K/3) sum_j sin(theta_j(t - tau) - theta_i),   w = (1.0, 1.1, 1.3)  (different free rates, as clocks z).
// Why it decides the point: with K = 0 the measured rates must equal the free rates (test says NO LOCK); with K large enough the rates must merge into one common rate (test says LOCKED).
// If the test said LOCKED at K = 0 or NO LOCK at K = 3 the instrument could not be trusted. Same window rule as kill line 1: slope over the last two quarters of the run, agreement within 0.02.
function run(K,tau){ const dt=0.002, n=Math.round(tau/dt), w=[1.0,1.1,1.3], T=400, steps=T/dt; let th=[0,0.5,1.0]; const H=[[],[],[]]; for(let k=0;k<Math.max(n,1);k++) for(let i=0;i<3;i++) H[i].push(th[i]); let head=0; const rec=[]; 
  for(let s=0;s<steps;s++){ const old=th.map((_,i)=> n===0?th[i]:H[i][head]); const nt=th.map((x,i)=> x+dt*(w[i]+(K/3)*(Math.sin(old[0]-x)+Math.sin(old[1]-x)+Math.sin(old[2]-x)))); if(n>0){ for(let i=0;i<3;i++) H[i][head]=th[i]; head=(head+1)%n; } th=nt; if(s%250===0) rec.push([s*dt,th.slice()]); }
  const slope=(i,t0,t1)=>{ const a=rec.filter(r=>r[0]>=t0&&r[0]<t1); const n=a.length; let sx=0,sy=0,sxx=0,sxy=0; a.forEach(([t,p])=>{sx+=t;sy+=p[i];sxx+=t*t;sxy+=t*p[i];}); return (n*sxy-sx*sy)/(n*sxx-sx*sx); };
  const r1=[0,1,2].map(i=>slope(i,200,300)), r2=[0,1,2].map(i=>slope(i,300,400)); let locked=0, pairs=[]; for(const [i,j] of [[0,1],[0,2],[1,2]]){ const ok=Math.abs(r1[i]-r1[j])<0.02&&Math.abs(r2[i]-r2[j])<0.02&&Math.abs(w[i]-w[j])>0.02; pairs.push(ok); if(ok) locked++; }
  return { r1:r1.map(x=>x.toFixed(4)), r2:r2.map(x=>x.toFixed(4)), pairs, verdict: locked>0?'LOCKED pairs '+locked+' of 3':'NO LOCK' }; }
for(const [K,tau] of [[0,0],[0,0.3],[0.2,0],[3,0],[3,0.3],[3,1.0]]) console.log('K='+K+' tau='+tau+'  window rates (200-300) '+JSON.stringify(run(K,tau).r1)+'  (300-400) '+JSON.stringify(run(K,tau).r2)+'  '+run(K,tau).verdict);
