// SCRIPT: L4-K6B-02
// Repair of PART A of L4-K6B-01. That run (l4_k6b_01.out) killed the prediction 'delay = n h' at n = 0 (measured 2.5e-3, predicted 0) and n = 10.
// Cause (derived, then tested here): the update of every ball field uses the OTHER ball's value from the START of the step (lines 92-95 build nd from S.d,
// then S.d = nd), so even with no stored history the neighbour is one step old: effective delay tau_eff = (n + 1) h.
// Prediction made before this run: rate(n, h) = Re lambda of  lambda = -i a (1 + exp(-lambda (n+1) h)), a = 0.5; at n = 0 this is about 2 a^2 h,
// so halving h must halve the n = 0 rate (1.25e-3 at h = 0.0025 and 5.0e-3 at h = 0.01).
// KILL LINE A' (written before this run): measured rate within 3 percent of the prediction for n in 0, 10, 40, 200 at h = 0.005, and the n = 0 rate at
// h = 0.01 and 0.0025 within 3 percent of the prediction at those h. Any miss kills the 'one step extra' repair.
function root(a,tau){ let lr=0, li=-2*a; for(let k=0;k<300;k++){ const e=Math.exp(-lr*tau), er=e*Math.cos(li*tau), ei=-e*Math.sin(li*tau); const Fr=lr-a*ei, Fi=li+a*(1+er), dr=1+a*tau*ei, di=-a*tau*er, den=dr*dr+di*di, sr=(Fr*dr+Fi*di)/den, si=(Fi*dr-Fr*di)/den; lr-=sr; li-=si; if(Math.hypot(sr,si)<1e-15) break; } return [lr,li]; }
function measure(n,h){ const kappa=0.25, D=1, a=2*kappa*D; let cur=[[1e-6,0,D],[-1e-6,0,D]].map(v=>{const m=Math.hypot(...v); return v.map(x=>x/m*D);}); const hist=[[],[]]; for(let k=0;k<Math.max(n,1);k++){ hist[0].push(cur[0].slice()); hist[1].push(cur[1].slice()); } let head=0;
  const [lr]=root(a,(n+1)*h); const T=Math.min(Math.max(14/Math.max(lr,1e-3),30),1500), pts=[];
  for(let k=0;k<Math.round(T/h);k++){ const nd=[]; for(let i=0;i<2;i++){ const j=1-i, dj=n===0?cur[j]:hist[j][head], G=[0,1,2].map(q=>2*kappa*(cur[i][q]-dj[q])), g=Math.hypot(...G); if(g<1e-300){nd.push(cur[i].slice());continue;} const u=G.map(x=>x/g), an=g*h, ca=Math.cos(an), sa=Math.sin(an), di=cur[i], ud=u[0]*di[0]+u[1]*di[1]+u[2]*di[2], cx=[u[1]*di[2]-u[2]*di[1],u[2]*di[0]-u[0]*di[2],u[0]*di[1]-u[1]*di[0]]; nd.push([0,1,2].map(q=>di[q]*ca+cx[q]*sa+u[q]*ud*(1-ca))); }
    if(n>0){ hist[0][head]=cur[0].slice(); hist[1][head]=cur[1].slice(); head=(head+1)%n; } cur=nd; if(k%Math.max(1,Math.round(0.2/h))===0) pts.push([(k+1)*h, Math.log(Math.hypot(cur[0][0],cur[0][1]))]); }
  // growth: least squares of the running max in blocks of 8 points, over points with |delta| between 1e-5 and 1e-1
  const bl=[]; for(let k=0;k+8<=pts.length;k+=8){ bl.push([pts[k][0], Math.max(...pts.slice(k,k+8).map(p=>p[1]))]); } const sel=bl.filter(b=>b[1]>Math.log(1e-5)&&b[1]<Math.log(1e-1)); const use=sel.length>=5?sel:bl;
  let sx=0,sy=0,sxx=0,sxy=0,m=use.length; use.forEach(([x,y])=>{sx+=x;sy+=y;sxx+=x*x;sxy+=x*y;}); return { rate:(m*sxy-sx*sy)/(m*sxx-sx*sx), pred:lr, T }; }
for(const [n,h] of [[0,0.005],[10,0.005],[40,0.005],[200,0.005],[0,0.01],[0,0.0025]]){ const r=measure(n,h), rel=Math.abs(r.rate-r.pred)/r.pred; console.log('n='+n+' h='+h+'  tau_eff = (n+1)h = '+((n+1)*h).toFixed(4)+'  predicted Re lambda = '+r.pred.toExponential(4)+'  measured = '+r.rate.toExponential(4)+'  relative difference '+(100*rel).toFixed(2)+' percent  '+(rel<0.03?'agrees':'KILLED')+'  (run length '+r.T.toFixed(0)+')'); }
