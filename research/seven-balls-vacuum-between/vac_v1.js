/*VAC-BEGIN*/
/* SCRIPT: SB-VAC-V1 — the vacuum between the balls. Jeromie Beasley's seven balls; layer added 18 Nov 2026 (AI-assisted).
   Units of the page: r = 1, c = 1, hbar = 1.
   1. WHERE THE VACUUM IS. Two side balls on perpendicular axes stand apart when |c_i - c_j| > 2r; the gap is s = |c_i - c_j| - 2r.
      Opposite side balls are not a gap: ball C sits on the line between them. With d = r(1 + tanh(ln z/4)) (his face apex),
      two equal neighbours touch exactly when z = 3 + 2 sqrt2 (d = sqrt2: tanh(ln(1+sqrt2)/2) = sqrt2 - 1). Below the wall
      they overlap, above it the gap opens. EXACT (geometry of this page).
   2. THE PULL. Each face of the gap is his face: index ratio z_gap between ball and gap (the page's own gap rule
      Y_gap = Y / z_gap), so the face returns Gamma_f^2, Gamma_f = (z_gap - 1)/(z_gap + 1) at normal incidence.
      Lifshitz (T = 0, no dispersion: MODEL) between two such half-spaces: energy per area -eta pi^2/(720 s^3), with
        eta(n) = int_0^{pi/2} cos(phi) [Li4(rTE^2) + Li4(rTM^2)] dphi / (2 zeta(4)),
        rTE = (1 - q)/(1 + q), rTM = (n^2 - q)/(n^2 + q), q = sqrt(cos^2 phi + n^2 sin^2 phi).
      Between two balls of radius r (proximity force, valid for s << r: MODEL): U = -eta pi^3 r/(1440 s^2), pull F = eta pi^3 r/(720 s^3).
   3. THE GAP'S OWN LIGHT. Standing modes across the gap, omega_k = k pi / s (one axis, the line of centres: MODEL).
      Each face keeps R_f = Gamma_f^2 of the power per bounce, so a mode leaks at kappa = -ln(R_f^2)/(2 s).
   4. LIGHT MADE BY THE BREATHING (dynamic Casimir). For one mode, in the instantaneous basis a(t):
        da/dt = -i omega a - (kappa/2) a + lambda a^dagger,  lambda = omega_dot/(2 omega)   (exact for qddot + omega(t)^2 q = 0)
      moments n = <a^dagger a>, m = <a a>, vacuum bath at zero temperature:
        dn/dt = -kappa n + 2 lambda Re m,   dm/dt = (-2 i omega - kappa) m + lambda (2n + 1).
      Starting from the vacuum (n = m = 0). Energy made = omega n, paid by the breathing; leaked = int kappa omega n dt
      (into the balls). Not fed back into the balls' motion and not into the ray light (books kept separate). */
const VAC=(function(){
"use strict";
const ZW=3+2*Math.SQRT2;
function li4(x){if(x<=0)return 0;let s=0,p=1;for(let k=1;k<=4000;k++){p*=x;const t=p/(k*k*k*k);s+=t;if(t<1e-17)break;}return s;}
const ZETA4=Math.pow(Math.PI,4)/90;
const etaCache=new Map();
function eta(n){const key=n.toFixed(6);if(etaCache.has(key))return etaCache.get(key);const e2=n*n,N=600,h=(Math.PI/2)/N;let s=0;
  for(let i=0;i<=N;i++){const ph=i*h,c=Math.cos(ph),sn=Math.sin(ph),q=Math.sqrt(c*c+e2*sn*sn),a=(1-q)/(1+q),b=(e2-q)/(e2+q),f=c*(li4(a*a)+li4(b*b));s+=f*((i===0||i===N)?1:(i%2?4:2));}
  const v=s*h/3/(2*ZETA4);etaCache.set(key,v);return v;}
/* plates: energy per area E/A = -eta pi^2/(720 s^3); pressure P = -eta pi^2/(240 s^4).
   spheres r1 = r2 = r (proximity force): U(s) = 2 pi R_eff int_s^inf E/A ds' = -eta pi^3 R_eff/(720 s^2), R_eff = r/2;
   pull F = -dU/ds = eta pi^3 R_eff/(360 s^3) (toward each other). */
const plateE=(s,et)=>-et*Math.PI*Math.PI/(720*s*s*s);
const sphereU=(s,et,r)=>-et*Math.pow(Math.PI,3)*(r/2)/(720*s*s);
const sphereF=(s,et,r)=>et*Math.pow(Math.PI,3)*(r/2)/(360*s*s*s);
const faceR=zg=>Math.pow((zg-1)/(zg+1),2);
const leak=(s,zg)=>-Math.log(faceR(zg)*faceR(zg))/(2*s);
/* the 12 neighbour gaps: side balls i (1..6) and j on perpendicular axes. With the side balls on the axes at d_a,
   |c_i - c_j| = hypot(d_a, d_b) for every sign, so the twelve gaps come in three kinds, one per pair of axes
   (x-y, y-z, x-z), four gaps of each kind, always equal. The modes are run once per kind. */
const NB=[];for(let i=1;i<7;i++)for(let j=i+1;j<7;j++){if(((i-1)>>1)!==((j-1)>>1))NB.push([i,j]);}
const KINDS=[[0,1],[1,2],[0,2]];
const kindOf=(i,j)=>{const a=(i-1)>>1,b=(j-1)>>1,lo=Math.min(a,b),hi=Math.max(a,b);return KINDS.findIndex(k=>k[0]===lo&&k[1]===hi);};
const gapOf=(S,i,j)=>{const a=S.balls[i],b=S.balls[j];return Math.hypot(a.c[0]-b.c[0],a.c[1]-b.c[1],a.c[2]-b.c[2])-a.r-b.r;};
/* one mode: advance (n, m) from t to t+h; coef(t) -> [omega, omega_dot, kappa] is evaluated at every RK4 stage */
function modeStep(st,coef,t,h){
  const f=(tt,n,mr,mi)=>{const c=coef(tt),om=c[0],lam=c[1]/(2*c[0]),kap=c[2];return [-kap*n+2*lam*mr, 2*om*mi-kap*mr+lam*(2*n+1), -2*om*mr-kap*mi];};
  const n=st.n,mr=st.mr,mi=st.mi;
  const k1=f(t,n,mr,mi),k2=f(t+h/2,n+h/2*k1[0],mr+h/2*k1[1],mi+h/2*k1[2]),k3=f(t+h/2,n+h/2*k2[0],mr+h/2*k2[1],mi+h/2*k2[2]),k4=f(t+h,n+h*k3[0],mr+h*k3[1],mi+h*k3[2]);
  st.n=n+h/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0]);st.mr=mr+h/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1]);st.mi=mi+h/6*(k1[2]+2*k2[2]+2*k3[2]+k4[2]);}
/* the vacuum world: per kind of gap (axes i, j), three modes; sFn(i, j, t) gives the gap at any time (omega_dot from it, not a frame difference) */
function makeVac(o){o=Object.assign({zgap:ZW,kmax:3,smin:0.02,r:1},o||{});
  return {o,t:0,g:KINDS.map(([i,j])=>({i,j,open:false,s:0,eta:0,F:0,U:0,modes:[0,1,2].slice(0,o.kmax).map(k=>({k:k+1,n:0,mr:0,mi:0})),made:0,leaked:0,closedWith:0,opens:0})),madeTot:0,leakTot:0,closedTot:0,workTot:0};}
function stepVac(V,sFn,t0,dt){const o=V.o,et=eta(o.zgap);
  for(const G of V.g){const s0=sFn(G.i,G.j,t0),s1=sFn(G.i,G.j,t0+dt);
    const open=s0>o.smin&&s1>o.smin;
    if(!open){if(G.open){/* the gap closed: whatever light the gap held goes into the walls (booked) */
        let e=0;for(const M of G.modes){e+=M.k*Math.PI/Math.max(s0,o.smin)*M.n;M.n=0;M.mr=0;M.mi=0;}G.closedWith+=e;V.closedTot+=e;}
      G.open=false;G.s=s1;G.F=0;G.U=0;G.eta=et;G.made=0;continue;}
    if(!G.open){G.open=true;G.opens++;}
    G.s=s1;G.eta=et;G.F=sphereF(s1,et,o.r);G.U=sphereU(s1,et,o.r);
    for(const M of G.modes){const wmax=M.k*Math.PI/Math.min(s0,s1),nsub=Math.max(1,Math.ceil(dt*wmax/0.1)),h=dt/nsub;
      const coef=tt=>{const sa=sFn(G.i,G.j,tt),e=1e-5,ds=(sFn(G.i,G.j,tt+e)-sFn(G.i,G.j,tt-e))/(2*e);return [M.k*Math.PI/sa,-M.k*Math.PI*ds/(sa*sa),leak(sa,o.zgap)];};
      for(let q=0;q<nsub;q++){const ta=t0+q*h,ca=coef(ta),cb=coef(ta+h),Ea=ca[0]*M.n;
        const nBefore=M.n;modeStep(M,coef,ta,h);
        const lk=0.5*(ca[2]*ca[0]*nBefore+cb[2]*cb[0]*M.n)*h;G.leaked+=lk;V.leakTot+=lk;
        V.workTot+=cb[0]*M.n-Ea+lk;}}  /* breathing work on the mode = change of its energy omega n + what leaked (book identity) */
    G.made=G.modes.reduce((a,M)=>a+M.k*Math.PI/s1*M.n,0);}
  V.madeTot=V.g.reduce((a,G)=>a+G.made,0);V.t=t0+dt;return V;}
/* textbook pump: a single gap of mean width s0 breathing as s0 (1 - eps sin(2 omega_1 t)), so omega_1 is pumped at twice itself */
function pumpRun(s0,epsA,zg,T,nOut,lossOn){const om0=Math.PI/s0,M={k:1,n:0,mr:0,mi:0},out=[];
  const coef=t=>{const sa=s0*(1-epsA*Math.sin(2*om0*t)),ds=-s0*epsA*2*om0*Math.cos(2*om0*t);return [Math.PI/sa,-Math.PI*ds/(sa*sa),lossOn===false?0:leak(sa,zg)];};
  const h=0.01/om0,N=Math.ceil(T/h),every=Math.max(1,Math.floor(N/(nOut||200)));
  for(let q=0;q<N;q++){modeStep(M,coef,q*h,h);if(q%every===0)out.push([(q+1)*h,M.n]);}
  return {om0,out,n:M.n,T:N*h};}
return {ZW,li4,eta,plateE,sphereU,sphereF,faceR,leak,NB,KINDS,kindOf,gapOf,modeStep,makeVac,stepVac,pumpRun};
})();
/*VAC-END*/
