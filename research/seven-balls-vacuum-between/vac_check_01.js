// SCRIPT: SB-VAC-CHECK-01 — checks for the vacuum layer, run in node
const fs=require('fs');
global.LH=require('./p2.js');const {GEOM}=require('./p3.js');
const VAC=new Function(fs.readFileSync('./vac_v1.js','utf8')+';return VAC;')();
const ZW=VAC.ZW,out=[];const row=(name,val,pass)=>{out.push([name,val,pass]);console.log((pass?'PASS ':'FAIL ')+name+': '+val);};
// 1. eta against the independent mpmath run (CASIMIR-WALL-01)
for(const [z,ref] of [[3,0.261245],[5,0.414141],[ZW,0.456192],[7,0.504067]]){const e=VAC.eta(z);row('eta('+z.toFixed(4)+') vs mpmath '+ref,e.toFixed(6),Math.abs(e-ref)<2e-6);}
row('eta(1e4) -> 1 (perfect mirrors)',VAC.eta(1e4).toFixed(5),Math.abs(VAC.eta(1e4)-0.99810)<2e-4);
// 2. plates: perfect mirrors give the textbook pressure pi^2/240 s^4
{const s=0.3,P=-(VAC.plateE(s+1e-6,1)-VAC.plateE(s-1e-6,1))/2e-6;row('plate pressure from energy, perfect mirrors, vs pi^2/(240 s^4)',(P/(-(Math.PI**2)/(240*s**4))).toFixed(9),Math.abs(P/(-(Math.PI**2)/(240*s**4))-1)<1e-6);}
// 3. sphere pull is -dU/ds
{const s=0.07,e=0.456,F=VAC.sphereF(s,e,1),Fn=(VAC.sphereU(s+1e-7,e,1)-VAC.sphereU(s-1e-7,e,1))/2e-7;row('sphere pull (attraction) F = dU/ds, U = -eta pi^3 r/(1440 s^2)',(F/Fn).toFixed(9),Math.abs(F/Fn-1)<1e-6);}
// 4. geometry: equal neighbours touch exactly at the wall, overlap below, open above
for(const z of [ZW-0.01,ZW,ZW+0.01]){const S=GEOM.state({z:[z,z,z],A:0,breathe:false},0,0.5,[1,1,1,1,1,1],'xyz');const g=VAC.gapOf(S,1,3);
  row('neighbour gap at z = '+z.toFixed(4),g.toExponential(3),z===ZW?Math.abs(g)<1e-14:(z<ZW?g<0:g>0));}
// 5. the moment equations against the mode function itself (no loss): q'' + w(t)^2 q = 0, f(0)=1/sqrt(2w0), f'(0)=-i w0 f(0); |beta|^2=|w f - i f'|^2/(2w)
{const s0=0.2,eps=0.05,om0=Math.PI/s0,T=40/om0;const r=VAC.pumpRun(s0,eps,ZW,T,50,false);const Tr=r.T;
  const sF=t=>s0*(1-eps*Math.sin(2*om0*t)),w=t=>Math.PI/sF(t);let fr=1/Math.sqrt(2*om0),fi=0,gr=0,gi=-om0/Math.sqrt(2*om0);const h=0.002/om0;let t=0;
  const F=(t,y)=>{const ww=w(t);return [y[2],y[3],-ww*ww*y[0],-ww*ww*y[1]];};let y=[fr,fi,gr,gi];
  while(t<Tr-1e-15){const hh=Math.min(h,Tr-t);const k1=F(t,y),k2=F(t+hh/2,y.map((v,i)=>v+hh/2*k1[i])),k3=F(t+hh/2,y.map((v,i)=>v+hh/2*k2[i])),k4=F(t+hh,y.map((v,i)=>v+hh*k3[i]));y=y.map((v,i)=>v+hh/6*(k1[i]+2*k2[i]+2*k3[i]+k4[i]));t+=hh;}
  const ww=w(Tr),br=ww*y[0]+y[3],bi=ww*y[1]-y[2],beta2=(br*br+bi*bi)/(2*ww);
  row('pumped gap, no loss: n from the moment equations vs |beta|^2 from the mode function',r.n.toExponential(6)+' vs '+beta2.toExponential(6),Math.abs(r.n/beta2-1)<1e-4);}
// 6. threshold with his faces: smallest pump depth eps (gap width swing) at which the light in the gap grows instead of leaking
for(const zg of [ZW,7,20]){let lo=0,hi=0.95;for(let it=0;it<40;it++){const e=(lo+hi)/2,s0=0.2,om0=Math.PI/s0,a=VAC.pumpRun(s0,e,zg,60/om0,5,true).n,b=VAC.pumpRun(s0,e,zg,120/om0,5,true).n;if(b>a*1.5&&b>1e-3)hi=e;else lo=e;}
  console.log('   threshold eps* (z_gap = '+zg.toFixed(3)+', face return '+VAC.faceR(zg).toFixed(4)+', leak/omega1 = '+(VAC.leak(1,zg)/Math.PI).toFixed(4)+'): '+hi.toFixed(4));out.push(['thr',zg,hi]);}
// 7. his breathing, his drive, all twelve gaps over 3 periods of 21: the light the breathing makes (adiabatic) 
{const o={z:[3,5,7],A:0.35,breathe:true},sFn=(a,b,t)=>Math.hypot(GEOM.dOfR(GEOM.rOf(o,a,t)),GEOM.dOfR(GEOM.rOf(o,b,t)))-2;const V=VAC.makeVac({zgap:ZW});let t=0;const dt=1/60;let peak=0,maxF=0,opens=0;
  for(let q=0;q<60*63;q++){VAC.stepVac(V,sFn,t,dt);t+=dt;for(const G of V.g){for(const M of G.modes)peak=Math.max(peak,M.n);if(G.open)maxF=Math.max(maxF,G.F);}}
  opens=V.g.reduce((a,G)=>a+G.opens,0);
  console.log('   his drive (3,5,7; A 0.35; periods 8,13,21), 63 time units: gap openings '+opens+', largest photon number in any gap mode '+peak.toExponential(3)+', largest pull '+maxF.toExponential(3)+' (hbar c/r^2 units), made now '+V.madeTot.toExponential(3)+', leaked '+V.leakTot.toExponential(3)+', closed with '+V.closedTot.toExponential(3));
  row('book-keeping of the vacuum layer (an identity, checks the code): work = made now + leaked + closed-with (rel)',(Math.abs(V.workTot-(V.madeTot+V.leakTot+V.closedTot))/Math.max(1e-30,V.workTot)).toExponential(2),Math.abs(V.workTot-(V.madeTot+V.leakTot+V.closedTot))<=1e-6*Math.max(1e-30,Math.abs(V.workTot))+1e-15);}
// 7b. the three kinds stand for all twelve gaps: compare with the gap measured ball to ball at several times
{const o={z:[3,5,7],A:0.35,breathe:true};let e=0;for(const t of [0,1.7,5.2,9.9,17.3]){const S=GEOM.state(o,t,0.5,[1,1,1,1,1,1],'xyz');for(const [i,j] of VAC.NB){const k=VAC.KINDS[VAC.kindOf(i,j)];e=Math.max(e,Math.abs(VAC.gapOf(S,i,j)-(Math.hypot(GEOM.dOfR(GEOM.rOf(o,k[0],t)),GEOM.dOfR(GEOM.rOf(o,k[1],t)))-2)));}}
  row('twelve gaps = three kinds (x-y, y-z, x-z), ball to ball at 5 times: max diff',e.toExponential(2),e<1e-14);}
// 8. how much faster the breathing would need to be: resonance needs 2 pi k / P = 2 pi / s
console.log('   resonance needs breathing period P = s (one light crossing of the gap there and back is 2s; pump at 2 omega_1 = 2 pi/s): for s = 0.05 and P = 8, speed-up x'+(8/0.05).toFixed(0));
console.log(JSON.stringify(out.filter(x=>typeof x[2]==='boolean').every(x=>x[2])?'ALL PASS':'SOME FAIL'));
