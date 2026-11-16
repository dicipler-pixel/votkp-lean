/*LH-MATH-BEGIN*/
/* SCRIPT: light_hypersurface_surprise_v1  (maths block: pure functions, no DOM, no three.js) */
var LH=(function(){
"use strict";
const PI=Math.PI, UNIT=[[1,0,0],[0,1,0],[0,0,1]], WALL=3+2*Math.SQRT2, O4=[1,0,0,0];
/* hyperboloid model, vectors (t,x,y,z), form <p,q> = t t' - x x' - y y' - z z' */
const mink=(p,q)=>p[0]*q[0]-p[1]*q[1]-p[2]*q[2]-p[3]*q[3];
function boost(u,r){const c=Math.cosh(r),s=Math.sinh(r),B=[[c,s*u[0],s*u[1],s*u[2]],[s*u[0],0,0,0],[s*u[1],0,0,0],[s*u[2],0,0,0]];
  for(let i=0;i<3;i++)for(let j=0;j<3;j++)B[i+1][j+1]=(i===j?1:0)+(c-1)*u[i]*u[j];return B;}
const mm=(A,B)=>A.map(r=>[0,1,2,3].map(j=>r[0]*B[0][j]+r[1]*B[1][j]+r[2]*B[2][j]+r[3]*B[3][j]));
const mv=(A,v)=>A.map(r=>r[0]*v[0]+r[1]*v[1]+r[2]*v[2]+r[3]*v[3]);
const I4=()=>[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]];
const hdist=(p,q)=>Math.acosh(Math.max(1,mink(p,q)));
/* Smith coordinate of a ratio */
const smith=z=>(z-1)/(z+1);
/* complex numbers as [re,im] */
const C={mul:(a,b)=>[a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]],add:(a,b)=>[a[0]+b[0],a[1]+b[1]],sub:(a,b)=>[a[0]-b[0],a[1]-b[1]],
  div:(a,b)=>{const d=b[0]*b[0]+b[1]*b[1];return[(a[0]*b[0]+a[1]*b[1])/d,(a[1]*b[0]-a[0]*b[1])/d];},abs2:a=>a[0]*a[0]+a[1]*a[1],ei:t=>[Math.cos(t),Math.sin(t)]};
/* Smith addition u (+) v = (u+v)/(1+uv) */
const oplus=(u,v)=>C.div(C.add(u,v),C.add([1,0],C.mul(u,v)));
/* letters 0..5: axis a = k>>1, sign + for even k, - for odd k; inverse letter k^1 */
const letterDir=k=>{const a=k>>1,s=(k&1)?-1:1;return UNIT[a].map(x=>x*s);};
/* unit normal of the face halfway (distance h) along direction u */
const faceN=(u,h)=>[Math.sinh(h),Math.cosh(h)*u[0],Math.cosh(h)*u[1],Math.cosh(h)*u[2]];

/* ---------- the feed: one state for one clock value ---------- */
function feed(P,tau){
  const r=[0,1,2].map(a=>Math.max(Math.log(1.3),Math.log(P.zbar[a])+P.amp*Math.sin(2*PI*tau/P.T[a]+P.ph[a])));
  const z=r.map(Math.exp),G=z.map(smith),R=G.map(g=>g*g),Tt=R.map(x=>1-x),h=r.map(x=>x/2);
  const gens=[],N0=[];for(let k=0;k<6;k++){const u=letterDir(k);gens.push(boost(u,r[k>>1]));N0.push(faceN(u,h[k>>1]));}
  return{tau,r,z,G,R,T:Tt,h,gens,N0,sigma:P.sigma,phi:2*PI*tau/P.Tphi,chi:2*PI*tau/P.Tchi};
}
/* ---------- one face: normal and oblique step ---------- */
/* a = Y^2 (declared reading), C = a1 sin^2(theta1) is the conserved quantity, oblique admittance sqrt(a - C) */
function split(Y1,Y2,c1){const a1=Y1*Y1,a2=Y2*Y2,s1sq=Math.max(0,1-c1*c1),Cq=a1*s1sq,y1=Math.sqrt(Math.max(0,a1-Cq));
  if(a2>Cq){const y2=Math.sqrt(a2-Cq),r=(y1-y2)/(y1+y2),t=2*y1/(y1+y2);
    return{total:false,r,t,R:r*r,T:4*y1*y2/((y1+y2)*(y1+y2)),Cq,s2sq:Cq/a2,y1,y2};}
  const ke=Math.sqrt(Cq-a2);return{total:true,r:1,t:0,R:1,T:0,Cq,s2sq:Cq/a2,y1,ke,phase:-2*Math.atan2(ke,y1)};}
/* ---------- geodesic rays in the ball ---------- */
function hit(X,v,N){const a=mink(X,N),b=mink(v,N);if(Math.abs(b)<1e-13)return null;const th=-a/b;if(!(th>1e-9)||th>=1)return null;return Math.atanh(th);}
const geoX=(X,v,s)=>{const c=Math.cosh(s),sh=Math.sinh(s);return[X[0]*c+v[0]*sh,X[1]*c+v[1]*sh,X[2]*c+v[2]*sh,X[3]*c+v[3]*sh];};
const geoV=(X,v,s)=>{const c=Math.cosh(s),sh=Math.sinh(s);return[X[0]*sh+v[0]*c,X[1]*sh+v[1]*c,X[2]*sh+v[2]*c,X[3]*sh+v[3]*c];};
function cellOf(cells,S,parent,k){const w=parent.word,back=w.length&&w[w.length-1]===(k^1),word=back?w.slice(0,-1):w.concat(k),key=word.join('');
  let c=cells.get(key);if(c)return c;const za=S.z[k>>1],g=mm(parent.g,S.gens[k]);
  c={g,word,key,depth:word.length,Y:back?parent.Y*Math.pow(za,S.sigma):parent.Y*Math.pow(za,-S.sigma)};cells.set(key,c);return c;}
const OPT={maxEv:6,fmin:0.004,smax:7,maxSeg:60};
function trace(S,dirs,opt){opt=opt||OPT;
  /* each ray is carried in the frame of the cell it is in (X, v local; world point = cell.g * X), so the six faces of every cell
     are the same six planes N0 and the arithmetic stays well conditioned at any depth */
  const cells=new Map(),root={g:I4(),word:[],key:'',depth:0,Y:1};cells.set('',root);
  const segs=[],events=[],land=[],out={segs,events,land,cells,rim:0,cut:0,small:0,nRays:dirs.length,nTotal:0,push:[0,0,0],
    resFlux:0,resCons:0,resNorm:0,resPlane:0,resInc:0};
  for(let i=0;i<dirs.length;i++){const d=dirs[i],stack=[{X:O4,v:[0,d[0],d[1],d[2]],cell:root,flux:1,kind:0,n:0,skip:-1}];let count=0;
    while(stack.length){const it=stack.pop();let best=null;
      for(let k=0;k<6;k++){if(k===it.skip)continue;const s=hit(it.X,it.v,S.N0[k]);if(s!==null&&(!best||s<best.s))best={s,k};}
      if(!best){segs.push({g:it.cell.g,X:it.X,v:it.v,s:opt.smax,flux:it.flux,kind:it.kind,depth:it.cell.depth,rim:true,ray:i});out.rim+=it.flux;
        const q=mv(it.cell.g,[it.X[0]+it.v[0],it.X[1]+it.v[1],it.X[2]+it.v[2],it.X[3]+it.v[3]]);land.push({d:[q[1]/q[0],q[2]/q[0],q[3]/q[0]],flux:it.flux,depth:it.cell.depth});continue;}
      const k=best.k,N=S.N0[k];let Xh=geoX(it.X,it.v,best.s),vh=geoV(it.X,it.v,best.s);
      /* rounding drift, measured before it is removed */
      {const xx=mink(Xh,Xh),vv=mink(vh,vh),xv=mink(Xh,vh);out.resNorm=Math.max(out.resNorm,Math.abs(xx-1),Math.abs(vv+1),Math.abs(xv));
       const q=Math.sqrt(xx);Xh=Xh.map(x=>x/q);const e=mink(vh,Xh);vh=vh.map((x,j)=>x-e*Xh[j]);const w=Math.sqrt(-mink(vh,vh));vh=vh.map(x=>x/w);}
      const vn=mink(vh,N),c1=Math.min(1,Math.abs(vn));
      segs.push({g:it.cell.g,X:it.X,v:it.v,s:best.s,flux:it.flux,kind:it.kind,depth:it.cell.depth,rim:false,ray:i});count++;
      const next=cellOf(cells,S,it.cell,k),sp=split(it.cell.Y,next.Y,c1),u=letterDir(k);
      const ev={g:it.cell.g,X:Xh,k,axis:k>>1,c1,flux:it.flux,R:sp.R,T:sp.T,total:sp.total,depth:it.cell.depth,first:it.kind===0,cosPsi:it.kind===0?it.v[1]*u[0]+it.v[2]*u[1]+it.v[3]*u[2]:0};
      events.push(ev);out.push[k>>1]+=it.flux*2*sp.R*c1*c1;
      out.resPlane=Math.max(out.resPlane,Math.abs(mink(Xh,N)));
      if(!sp.total)out.resFlux=Math.max(out.resFlux,Math.abs(sp.r*sp.r+(sp.y2/sp.y1)*sp.t*sp.t-1));
      if(it.kind===0)out.resInc=Math.max(out.resInc,Math.abs(Math.sqrt(Math.max(0,1-vn*vn))-Math.cosh(S.h[k>>1])*Math.sqrt(Math.max(0,1-ev.cosPsi*ev.cosPsi))));
      if(sp.total)out.nTotal++;
      if(it.n+1>=opt.maxEv||count>=opt.maxSeg){out.cut+=it.flux;continue;}
      /* returned part: mirror the tangent in the face */
      const fr=it.flux*sp.R;
      if(fr>opt.fmin)stack.push({X:Xh,v:[vh[0]+2*vn*N[0],vh[1]+2*vn*N[1],vh[2]+2*vn*N[2],vh[3]+2*vn*N[3]],cell:it.cell,flux:fr,kind:sp.total?3:2,n:it.n+1,skip:k});else out.small+=fr;
      if(!sp.total){const ft=it.flux*sp.T,s1=Math.sqrt(Math.max(0,1-c1*c1)),s2=Math.sqrt(sp.s2sq),c2=Math.sqrt(Math.max(0,1-sp.s2sq)),sg=vn>0?-1:1;let v2;
        if(s1<1e-12)v2=N.map(x=>sg*x);else v2=[0,1,2,3].map(j=>c2*sg*N[j]+s2*(vh[j]+vn*N[j])/s1);
        /* conserved quantity, both angles measured from the tangent vectors actually used */
        const m2=mink(v2,N);out.resCons=Math.max(out.resCons,Math.abs(it.cell.Y*it.cell.Y*(1-vn*vn)-next.Y*next.Y*(1-m2*m2))/(it.cell.Y*it.cell.Y));
        out.resNorm=Math.max(out.resNorm,Math.abs(mink(v2,v2)+1),Math.abs(mink(Xh,v2)));
        /* pass to the frame of the next cell: one inverse step */
        const Bi=S.gens[k^1];
        if(ft>opt.fmin)stack.push({X:mv(Bi,Xh),v:mv(Bi,v2),cell:next,flux:ft,kind:1,n:it.n+1,skip:k^1});else out.small+=ft;}
    }}
  out.resLedger=Math.abs(out.rim+out.cut+out.small-dirs.length)/dirs.length;return out;}
/* source directions: a fixed even set on the sphere, turned as one body by the clock (declared drive) */
function sourceDirs(n,chi){const out=[],ga=PI*(3-Math.sqrt(5)),c1=Math.cos(chi),s1=Math.sin(chi),c2=Math.cos(chi*0.6180339887),s2=Math.sin(chi*0.6180339887);
  for(let i=0;i<n;i++){const y=1-2*(i+0.5)/n,rr=Math.sqrt(1-y*y),a=ga*i;let x=rr*Math.cos(a),zz=rr*Math.sin(a),yy=y;
    let x1=c1*x-s1*yy,y1=s1*x+c1*yy;x=x1;yy=y1;let y2=c2*yy-s2*zz,z2=s2*yy+c2*zz;out.push([x,y2,z2]);}return out;}
/* a fan about each of the six arms, spanning the edge of its window: polar angles are fixed fractions of psi_w,
   where sin(psi_w) = 1/(z cosh(r/2)) is the centre angle whose ray meets the face at arcsin(1/z); turned by the clock (declared drive) */
const FANF=[0.3,0.62,0.9,1.12];
function fanDirs(S,chi){const out=[];for(let k=0;k<6;k++){const a=k>>1,u=letterDir(k),e1=UNIT[(a+1)%3],e2=UNIT[(a+2)%3],pw=Math.asin(Math.min(1,1/(S.z[a]*Math.cosh(S.h[a]))));
  for(let m=0;m<FANF.length;m++)for(let q=0;q<3;q++){const ps=FANF[m]*pw,t=2*PI*q/3+3*chi+m*0.7+k,c=Math.cos(ps),sn=Math.sin(ps);
    out.push([0,1,2].map(j=>c*u[j]+sn*(Math.cos(t)*e1[j]+Math.sin(t)*e2[j])));}}return out;}
/* ---------- layers on one arm: echoes composed by Smith addition ---------- */
function stack(Ys,phi){const D=Ys.length-1,e2=C.ei(2*phi),e1=C.ei(phi),g=[];for(let k=0;k<D;k++)g.push((Ys[k]-Ys[k+1])/(Ys[k]+Ys[k+1]));
  const rho=new Array(D+1);rho[D]=[0,0];for(let k=D-1;k>=0;k--)rho[k]=oplus([g[k],0],C.mul(rho[k+1],e2));
  const fwd=[1],bwd=[C.abs2(rho[0])],flux=[1-C.abs2(rho[0])];let A=[1,0];
  for(let k=0;k<D;k++){const F=C.div(C.mul(A,C.add([1,0],rho[k])),C.add([1,0],C.mul(rho[k+1],e2))),f2=C.abs2(F),b2=f2*C.abs2(rho[k+1]);
    fwd.push(f2);bwd.push(b2);flux.push(Ys[k+1]/Ys[0]*(f2-b2));A=C.mul(F,e1);}
  let lo=Infinity,hi=-Infinity;flux.forEach(f=>{lo=Math.min(lo,f);hi=Math.max(hi,f);});
  return{g,rho,r:rho[0],R:C.abs2(rho[0]),fwd,bwd,flux,spread:hi-lo};}
/* ---------- two faces: cross or stand apart ---------- */
function pair(S,a,b){const ha=S.h[a],hb=S.h[b],g=Math.sinh(ha)*Math.sinh(hb),over=g<1;
  return{a,b,g,over,alpha:over?Math.acos(g):NaN,delta:over?NaN:Math.acosh(g)};}
function gapFeet(Na,Nb){const g=mink(Na,Nb);if(!(g>1))return null;const k=1/Math.sqrt(g*g-1);let pa=[0,1,2,3].map(j=>k*(Nb[j]+g*Na[j])),pb=[0,1,2,3].map(j=>k*(Na[j]+g*Nb[j]));
  if(pa[0]<0)pa=pa.map(x=>-x);if(pb[0]<0)pb=pb.map(x=>-x);return{pa,pb,g};}
/* ---------- two steps: a boost and a turn; four steps: turn, lock or run ---------- */
function thomas(ua,ra,ub,rb){const M=mm(boost(ua,ra),boost(ub,rb)),vx=[M[1][0],M[2][0],M[3][0]],n=Math.hypot(vx[0],vx[1],vx[2]),rap=Math.acosh(M[0][0]),d=vx.map(x=>x/n),
  L=boost(d,rap),R=mm(boost(d,-rap),M),c=(R[1][1]+R[2][2]+R[3][3]-1)/2;return{M,L,R,angle:Math.acos(Math.max(-1,Math.min(1,c)))};}
const thomasFormula=(Ga,Gb)=>2*Math.atan(Ga*Gb);
function loop(S,a,b){const ua=UNIT[a],ub=UNIT[b],na=ua.map(x=>-x),nb=ub.map(x=>-x),steps=[boost(ua,S.r[a]),boost(ub,S.r[b]),boost(na,S.r[a]),boost(nb,S.r[b])];
  let W=I4();const part=[I4()];steps.forEach(B=>{W=mm(W,B);part.push(W);});const tr=W[0][0]+W[1][1]+W[2][2]+W[3][3],half=(tr-2)/2,g=Math.sinh(S.h[a])*Math.sinh(S.h[b]);
  const o={a,b,W,part,tr,half,g,kind:Math.abs(g-1)<1e-6?'locks':g<1?'turns':'runs'};
  if(g<1){o.phiF=Math.acos(Math.max(-1,Math.min(1,8*g*g*g*g-8*g*g+1)));o.phiM=Math.acos(Math.max(-1,Math.min(1,half)));}
  else{o.runF=4*Math.acosh(g);o.runM=Math.acosh(Math.max(1,half));}return o;}
/* ---------- pressure of a wave front (Maxwell stress), Gaussian units ---------- */
function normalStress(E,H,n){const dot=(p,q)=>p[0]*q[0]+p[1]*q[1]+p[2]*q[2],k=1/(4*PI);
  return k*(dot(E,n)*dot(E,n)+dot(H,n)*dot(H,n))-(dot(E,E)+dot(H,H))/(8*PI)*dot(n,n);}
const pushOblique=(R,c1)=>2*R*c1*c1;
/* ---------- occupation reading ---------- */
const occupation=z=>1/(z+1);
const thetaCrit=(z,sigma)=>sigma>0?Math.asin(1/z):NaN;
return{PI,UNIT,WALL,O4,mink,boost,mm,mv,I4,hdist,smith,C,oplus,letterDir,faceN,feed,split,hit,geoX,geoV,trace,sourceDirs,fanDirs,FANF,stack,pair,gapFeet,thomas,thomasFormula,loop,normalStress,pushOblique,occupation,thetaCrit,OPT};
})();
if(typeof module!=='undefined')module.exports=LH;
/*LH-MATH-END*/
