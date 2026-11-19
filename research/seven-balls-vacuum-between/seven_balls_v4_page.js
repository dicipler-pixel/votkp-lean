/* SCRIPT: seven_balls_v4. Seven equal balls, C plus +-x +-y +-z at his z = 3, 5, 7, pushing into C and into each other; his light; the vacuum between (SB-VAC-V1). Built on seven_balls_v3. */
/*GEOM-BEGIN*/
const GEOM=(function(){
  "use strict";
  /* v3 geometry. Seven equal balls (radius r = 1). Side ball i on axis a = i>>1 (x, y, z) sits at d_a(t) = r (1 + tanh(r_a(t)/4)),
     r_a(t) = ln z_a(t) from his breathe drive (LH-MATH-V1 rOf: z = 3, 5, 7, periods 8, 13, 21, phases a third apart, +-A in ln z).
     d formula: SB3-LIGHT-V2 balls() in his v4 file: the neighbour's near point sits at his face apex rho = tanh(h/2), h = r_a/2
     (LH-MIXER-V2 capParams), so d = 1 + tanh(r_a/4). On his wall z = 3 + 2sqrt2 this gives d = sqrt2 exactly (90 degree crossing).
     DENT RULE (pairwise, all seven): every ball has a rank. A point of ball A's sphere is REMOVED if it lies inside any visible ball
     of higher rank; it is a DENT WALL (A's own sphere seen inside the hole it makes) if it lies inside a visible ball of lower rank.
     C has the lowest rank (every side ball pushes into C). Between side balls the order is a choice (MODEL): default x over y over z. */
  const Lh=()=>(typeof LH!=='undefined')?LH:globalThis.LH;
  const AX=[[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]];
  const NAMES=['+x','\u2212x','+y','\u2212y','+z','\u2212z'];
  const ZW=3+2*Math.SQRT2, PER=[8,13,21], PHS=[0,2*Math.PI/3,4*Math.PI/3];
  const ORDERS={xyz:[3,2,1],zyx:[1,2,3]};             /* rank of the x, y, z side balls; C = 0 */
  const rOf=(o,a,t)=>Lh().rOf({zI:o.z[0],zJ:o.z[1],zK:o.z[2],A:o.A,drive:o.breathe?'breathe':'hold'},a,t*(o.k||1)); /* o.k: breath speed (MODEL, 1 = his drive) */
  const dOfR=(r,rad)=>(rad||1)*(1+Math.tanh(r/4));
  const len=p=>Math.hypot(p[0],p[1],p[2]);
  const dist=(p,c)=>Math.hypot(p[0]-c[0],p[1]-c[1],p[2]-c[2]);
  function state(o,t,margin,vis,order){
    const rad=1,rk=ORDERS[order||'xyz'];
    const balls=[{id:0,name:'C',c:[0,0,0],r:rad,visible:true,z:1,lnz:0,G:0,d:0,rank:0,axis:null,a:-1}];
    const ra=[0,1,2].map(a=>rOf(o,a,t));
    for(let i=0;i<6;i++){const a=i>>1,r=ra[a],d=dOfR(r,rad),ax=AX[i];
      balls.push({id:i+1,name:'N'+NAMES[i],c:[ax[0]*d,ax[1]*d,ax[2]*d],r:rad,visible:!!vis[i],z:Math.exp(r),lnz:r,G:Math.tanh(r/2),d,rank:rk[a],axis:ax,a});}
    /* container fixed: every d < 2r, so 3r + margin always holds all seven */
    return {t,r:rad,R:3*rad+margin,margin,balls,order:order||'xyz',ra};
  }
  const inBall=(p,b)=>dist(p,b.c)<b.r;
  /* the dent rule for ball id at a point p on its sphere: -1 removed, 1 dent wall, 0 outside part */
  function classify(S,id,p){const A=S.balls[id];let dent=false;
    for(const B of S.balls){if(B.id===id||!B.visible)continue;if(inBall(p,B)){if(B.rank>A.rank)return -1;dent=true;}}
    return dent?1:0;}
  function insideContainer(S,p){return len(p)<S.R;}
  function insideAnyBall(S,p){for(const b of S.balls){if(b.visible&&inBall(p,b))return true;}return false;}
  function isMedium(S,p){return insideContainer(S,p)&&!insideAnyBall(S,p);}
  function maskOf(S,p){const w=[];for(const b of S.balls)if(b.visible&&inBall(p,b))w.push(b.id);return w;}
  /* every overlapping visible pair: who owns the wall, the contact circle, the crossing angle */
  function pairs(S){const out=[];const B=S.balls;
    for(let i=0;i<7;i++)for(let j=i+1;j<7;j++){const a=B[i],b=B[j];if(!a.visible||!b.visible)continue;const D=dist(a.c,b.c);if(D>=a.r+b.r)continue;
      const own=a.rank>b.rank?a:b,den=own===a?b:a,e=[(den.c[0]-own.c[0])/D,(den.c[1]-own.c[1])/D,(den.c[2]-own.c[2])/D];
      const m=[(a.c[0]+b.c[0])/2,(a.c[1]+b.c[1])/2,(a.c[2]+b.c[2])/2];
      out.push({i,j,owner:own.id,dented:den.id,D,depth:a.r+b.r-D,cosCross:(2*a.r*a.r-D*D)/(2*a.r*a.r),
        circle:{centre:m,normal:e,radius:Math.sqrt(Math.max(0,a.r*a.r-D*D/4))},side:i>0&&j>0});}
    return out;}
  function fib(n){const o=[],g=Math.PI*(3-Math.sqrt(5));for(let k=0;k<n;k++){const y=1-2*(k+.5)/n,s=Math.sqrt(1-y*y),t=g*k;o.push([Math.cos(t)*s,y,Math.sin(t)*s]);}return o;}
  function basis(a){const e1=Math.abs(a[0])<.9?[1,0,0]:[0,1,0];let v=[a[1]*e1[2]-a[2]*e1[1],a[2]*e1[0]-a[0]*e1[2],a[0]*e1[1]-a[1]*e1[0]];const l=len(v);v=v.map(x=>x/l);
    return [v,[a[1]*v[2]-a[2]*v[1],a[2]*v[0]-a[0]*v[2],a[0]*v[1]-a[1]*v[0]]];}
  function checks(S,n,nMed){
    n=n||40000;nMed=nMed||20000;const U=fib(n),out=[],B=S.balls,r=S.r;
    /* plane test (independent of the distance test): for equal radii, p on sphere A lies inside B  <=>  (p - cA).e_AB > |cB - cA|/2 */
    const planeIn=(p,A,Bb)=>{const D=dist(A.c,Bb.c);return ((p[0]-A.c[0])*(Bb.c[0]-A.c[0])+(p[1]-A.c[1])*(Bb.c[1]-A.c[1])+(p[2]-A.c[2])*(Bb.c[2]-A.c[2]))/D>D/2;};
    const planeEdge=(p,A,Bb)=>{const D=dist(A.c,Bb.c);return Math.abs(((p[0]-A.c[0])*(Bb.c[0]-A.c[0])+(p[1]-A.c[1])*(Bb.c[1]-A.c[1])+(p[2]-A.c[2])*(Bb.c[2]-A.c[2]))/D-D/2)<1e-9;};
    let onOwner=0,inDented=-Infinity,nDent=0,mis=0,nRem=0,nDentSide=0;
    for(const A of B){if(!A.visible)continue;
      for(const u of U){const p=[A.c[0]+r*u[0],A.c[1]+r*u[1],A.c[2]+r*u[2]];const cls=classify(S,A.id,p);
        let rem=false,den=false,edge=false;for(const Bb of B){if(Bb===A||!Bb.visible)continue;if(planeEdge(p,A,Bb)){edge=true;break;}if(planeIn(p,A,Bb)){if(Bb.rank>A.rank)rem=true;else den=true;}}
        if(!edge){const ana=rem?-1:(den?1:0);if(ana!==cls)mis++;}
        if(cls===-1)nRem++;
        if(cls===1){nDent++;onOwner=Math.max(onOwner,Math.abs(dist(p,A.c)-r));let m=Infinity;for(const Bb of B){if(Bb!==A&&Bb.visible&&Bb.rank<A.rank)m=Math.min(m,dist(p,Bb.c)-r);}inDented=Math.max(inDented,m);
          if(A.id>0){for(const Bb of B){if(Bb.id>0&&Bb!==A&&Bb.visible&&Bb.rank<A.rank&&inBall(p,Bb)){nDentSide++;break;}}}}}}
    out.push(['Dent-wall points ('+nDent+' of them, '+nDentSide+' inside another SIDE ball): max | |p \u2212 c_owner| \u2212 r |',onOwner,onOwner<=1e-12]);
    out.push(['Dent-wall points lie inside the ball they dent: max (|p \u2212 c_dented| \u2212 r) (must be < 0)',nDent?inDented:0,!nDent||inDented<0]);
    out.push(['Removed / dent / outside per point vs the analytic plane test, all 7 balls pairwise: mismatches',mis,mis===0]);
    const PR=pairs(S);let ccErr=0,angErr=0;
    for(const q of PR){const [v,w]=basis(q.circle.normal),A=B[q.i],Bb=B[q.j];
      for(let k=0;k<360;k++){const t=k*Math.PI/180,p=[0,1,2].map(j=>q.circle.centre[j]+q.circle.radius*(Math.cos(t)*v[j]+Math.sin(t)*w[j]));
        ccErr=Math.max(ccErr,Math.abs(dist(p,A.c)-r),Math.abs(dist(p,Bb.c)-r));
        const na=[0,1,2].map(j=>(p[j]-A.c[j])/r),nb=[0,1,2].map(j=>(p[j]-Bb.c[j])/r);angErr=Math.max(angErr,Math.abs(na[0]*nb[0]+na[1]*nb[1]+na[2]*nb[2]-q.cosCross));}}
    out.push(['Contact circles of all '+PR.length+' overlapping pairs ('+PR.filter(q=>q.side).length+' side\u2013side) on both spheres: max error',ccErr,ccErr<1e-12]);
    out.push(['Crossing angle on every contact circle: n\u2081\u00b7n\u2082 = (2r\u00b2 \u2212 d\u00b2)/2r\u00b2 against the two sphere normals: max diff',angErr,angErr<1e-12]);
    let areaErr=0;for(const q of PR){const A=B[q.owner],Bb=B[q.dented];let c=0;for(const u of U){const p=[Bb.c[0]+r*u[0],Bb.c[1]+r*u[1],Bb.c[2]+r*u[2]];if(inBall(p,A))c++;}areaErr=Math.max(areaErr,Math.abs(c/n-(r-q.D/2)/(2*r)));}
    out.push(['Hole each pair cuts, area fraction vs exact (r \u2212 d/2)/2r: max diff (tol 2e-3, sampling)',areaErr,areaErr<2e-3]);
    let dErr=0;for(let i=1;i<7;i++){const b=B[i],rho=Math.tanh((b.lnz/2)/2);dErr=Math.max(dErr,Math.abs((len(b.c)-b.r)-rho*r),Math.abs(b.G-(b.z-1)/(b.z+1)));}
    out.push(['d\u1d62 = r(1 + tanh(ln z/4)): near point of each side ball at his face apex tanh(h/2), h = ln z/2; and \u0393 = (z\u22121)/(z+1): max diff',dErr,dErr<1e-14]);
    let opp=Infinity;for(let i=1;i<7;i+=2){opp=Math.min(opp,dist(B[i].c,B[i+1].c)-2*r);}
    out.push(['Opposite side balls never overlap: min (centre gap \u2212 2r) (must be > 0)',opp,opp>0]);
    let worst=-Infinity;for(const b of B){if(b.visible)worst=Math.max(worst,len(b.c)+b.r-S.R);}
    out.push(['All balls inside the container: max (|c| + r \u2212 R) (must be < 0)',worst,worst<0]);
    let medBad=0;let seed=12345;const rnd=()=>{seed=(seed*16807)%2147483647;return seed/2147483647;};
    for(let k=0;k<nMed;k++){const p=[(rnd()*2-1)*S.R,(rnd()*2-1)*S.R,(rnd()*2-1)*S.R];const m=isMedium(S,p);const inB=B.some(b=>b.visible&&dist(p,b.c)<b.r);if(m!==(len(p)<S.R&&!inB))medBad++;}
    out.push(['medium.isMedium agrees with container \u2212 balls ('+nMed+' pts): mismatches',medBad,medBad===0]);
    return out;
  }
  return {AX,NAMES,ZW,PER,PHS,ORDERS,rOf,dOfR,state,len,dist,inBall,classify,insideContainer,insideAnyBall,isMedium,maskOf,pairs,fib,basis,checks};
})();
/*GEOM-END*/

/*LIGHT-BEGIN*/
/* SCRIPT: SB-LIGHT-V3 — his light among the seven balls. Every wall is a real ball sphere; the split at every wall is his.
   Uses LH-MATH-V1 (Jeromie Beasley, 15 Nov 2026) unchanged: splitAtFace, tunnelGap, stocksStep, fanDirs, occupation.
   Packets of light move in straight lines at speed 1 (as the 'room' mode of his v4 file, SB3-LIGHT-V2).
   Admittance of a region: Y = product of 1/z over the side balls that hold the light (C counts 1) — his v4 file's extension of
   nodeAdmittance. Entering side ball j multiplies Y by 1/z_j, so at normal incidence the wall returns Gamma^2, Gamma = (z-1)/(z+1).
   At every wall: LH.splitAtFace(Y1^2, Y2^2, sin^2 theta, omega, 1): oblique split, Snell (a sin^2 kept), and past the critical
   angle (sin theta > Y2/Y1) the whole packet returns. That total return is what traps the light.
   The gap (outside every ball): MODEL. Its admittance is one step z_gap below the region the light leaves (default z_gap = 3 + 2sqrt2).
     window 'closed' (default): the gap face returns all propagating light (his v4 ground rule); light gets into the gap ONLY by
       LH.tunnelGap: past the critical angle, the evanescent film of width w (straight along the face normal to the next ball) passes T.
     window 'open': inside the window his split also passes 1 - R into the gap as propagating light.
   Light in the gap is FREE. Tunnelled light crosses the film along the normal and enters the far ball with its incoming direction
   (MODEL: tunnelGap assumes the same medium on both sides; no second split). Propagating free light that reaches the container
   wall leaves (booked 'out', kept as the record on the ground). A breathing ball that sweeps over light moves it to the new region
   without a split (MODEL, counted). Books: in balls + free + out + cut = emitted, exactly. */
const LIGHT=(function(){
"use strict";
const Lh=()=>(typeof LH!=='undefined')?LH:globalThis.LH;
const dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2],sub=(a,b)=>[a[0]-b[0],a[1]-b[1],a[2]-b[2]],add=(a,b,s)=>[a[0]+s*b[0],a[1]+s*b[1],a[2]+s*b[2]];
const nrm=a=>{const l=Math.hypot(a[0],a[1],a[2]);return [a[0]/l,a[1]/l,a[2]/l];};
const ZW=3+2*Math.SQRT2;
function makeWorld(o){o=Object.assign({omega:3,zgap:ZW,window:'closed',emitEvery:2,nray:9,fan:62,source:0,cut:1e-3,maxPk:2500,kappa:1,ha:1,hb:0.2},o||{});
  return {o,t:0,pk:[],emitted:0,out:0,cut:0,freeIn:{tunnel:0,window:0},swept:0,sweptN:0,stuck:0,nTotal:0,totalFlux:0,nHits:0,
    push:new Float64Array(7),pushRate:new Float64Array(7),K:new Float64Array(7),arriveRate:new Float64Array(7),arriveAcc:new Float64Array(7),stocks:[0,1,2,3,4,5,6].map(()=>[0,0]),
    hits:[],tunnels:[],deposits:[],lastEmit:-1e9,S:null,log:null};}
const Yof=(w,S)=>{let Y=1;for(const j of w)Y/=S.balls[j].z;return Y;};
const toggle=(w,j)=>w.indexOf(j)>=0?w.filter(x=>x!==j):w.concat([j]).sort((a,b)=>a-b);
function maskOf(p,S){const w=[];for(const b of S.balls){if(!b.visible)continue;const d=sub(p,b.c);if(dot(d,d)<b.r*b.r)w.push(b.id);}return w;}
function onAnySphere(p,S){for(const b of S.balls){if(!b.visible)continue;if(Math.abs(Math.hypot(p[0]-b.c[0],p[1]-b.c[1],p[2]-b.c[2])-b.r)<1e-9)return true;}return false;}
/* next sphere crossing along p + s u (s in (0, Lmax]); j = -1 is the container wall */
function nextEvent(p,u,S,Lmax,skip){let best=null;
  for(const b of S.balls){if(!b.visible)continue;const d=sub(p,b.c),bb=dot(d,u),c=dot(d,d)-b.r*b.r,D=bb*bb-c;if(D<0)continue;const sq=Math.sqrt(D);
    for(let s of [-bb-sq,-bb+sq]){if(s>Lmax)continue;if(b.id===skip?s<1e-7:(skip===-2?s<=-1e-12:s<=1e-10))continue;if(s<0)s=0;if(!best||s<best.s)best={s,j:b.id};}}
  {const bb=dot(p,u),c=dot(p,p)-S.R*S.R,D=bb*bb-c;if(D>=0){const s=-bb+Math.sqrt(D);if(s>1e-10&&s<=Lmax&&(!best||s<best.s))best={s,j:-1};}}
  return best;}
/* width of the gap film: straight along the outward normal n from p to the first ball the line enters */
function gapWidth(p,n,S,from){let best=null;
  for(const b of S.balls){if(!b.visible||b.id===from)continue;const d=sub(p,b.c),bb=dot(d,n),c=dot(d,d)-b.r*b.r,D=bb*bb-c;if(D<0)continue;const s=-bb-Math.sqrt(D);
    if(s>1e-12&&(!best||s<best.w))best={w:s,k:b.id};}
  if(best){const q=add(p,n,best.w);if(dot(q,q)>=S.R*S.R)return null;}
  return best;}
const refractDir=(u,n,un,s1sq,sin2sq)=>{const tp=add(u,n,-un),s1=Math.sqrt(s1sq),s2=Math.sqrt(Math.max(0,Math.min(1,sin2sq))),c2=Math.sqrt(Math.max(0,1-s2*s2));
  return s1<1e-15?n.map(v=>Math.sign(un)*c2*v):[0,1,2].map(q=>Math.sign(un)*c2*n[q]+(s2/s1)*tp[q]);};
/* the split of packet k at sphere j, at point p. Returns the children (packets) and books the push. */
function split(W,k,p,j){const S=W.S,o=W.o,L=Lh(),b=S.balls[j],n=nrm(sub(p,b.c)),u=k.u,un=dot(u,n),s1sq=Math.max(0,1-un*un),refl=add(u,n,-2*un),f=k.f,kids=[];
  let R=0,T=0,ev={j,kind:'',total:false};
  if(k.kind==='gap'){ /* free light reaches ball j from the gap */
    const w2=[j].concat(maskOf(add(p,u,1e-9),S).filter(x=>x!==j)).sort((a,b)=>a-b),Y1=k.Yg,Y2=Yof(w2,S),sp=L.splitAtFace(Y1*Y1,Y2*Y2,s1sq,o.omega,1);
    R=sp.R;T=sp.total?0:sp.T;ev.kind='enter';ev.total=sp.total;
    if(R>0)kids.push({p,u:refl,f:f*R,w:[],kind:'gap',Yg:k.Yg,gen:k.gen+1,skip:j});
    if(T>0)kids.push({p,u:refractDir(u,n,un,s1sq,sp.sin2sq),f:f*T,w:w2,kind:'in',gen:k.gen+1,skip:j});}
  else{const w2=toggle(k.w,j),Y1=Yof(k.w,S);
    if(w2.length===0){ /* leaving every ball: the gap */
      const Yg=Y1/o.zgap,a1=Y1*Y1,a2=Yg*Yg,sp=L.splitAtFace(a1,a2,s1sq,o.omega,1);
      if(!sp.total){ev.kind='window';
        if(o.window==='open'){R=sp.R;T=sp.T;if(T>0){kids.push({p,u:refractDir(u,n,un,s1sq,sp.sin2sq),f:f*T,w:[],kind:'gap',Yg,gen:k.gen+1,skip:j});W.freeIn.window+=f*T;}}
        else{R=1;T=0;}}
      else{ev.kind='total';ev.total=true;W.nTotal++;
        const gw=gapWidth(p,n,S,j);
        if(gw){const Cc=a1*s1sq,ke=o.omega*Math.sqrt(Cc-a2),kp=o.omega*Math.sqrt((Cc-a2)/a2),tg=L.tunnelGap(o.omega*Math.sqrt(a1-Cc),ke,kp,gw.w);
          R=tg.R;T=tg.T;ev.kind='tunnel';ev.w=gw.w;
          if(T>0){const q=add(p,n,gw.w);if(W.tunnels.length<1500)W.tunnels.push({a:p.slice(),b:q.slice(),f:f*T,age:0});kids.push({p,u,f:f*T,w:[],kind:'tun',gen:k.gen+1,tun:{from:p.slice(),n,len:gw.w,s:0,k:gw.k,q,uIn:u.slice()}});W.freeIn.tunnel+=f*T;}}
        else{R=1;T=0;}
        W.totalFlux+=f*R;}
      if(R>0)kids.push({p,u:refl,f:f*R,w:k.w,kind:'in',gen:k.gen+1,skip:j});}
    else{ /* a wall between two ball regions */
      const Y2=Yof(w2,S),sp=L.splitAtFace(Y1*Y1,Y2*Y2,s1sq,o.omega,1);
      R=sp.R;T=sp.total?0:sp.T;ev.kind=sp.total?'total':'wall';ev.total=sp.total;if(sp.total){W.nTotal++;W.totalFlux+=f;}
      if(R>0)kids.push({p,u:refl,f:f*R,w:k.w,kind:'in',gen:k.gen+1,skip:j});
      if(T>0)kids.push({p,u:refractDir(u,n,un,s1sq,sp.sin2sq),f:f*T,w:w2,kind:'in',gen:k.gen+1,skip:j});}}
  W.nHits++;W.push[j]+=2*R*f*un*un;W.arriveAcc[j]+=f*Math.abs(un);
  if(W.hits.length<4000)W.hits.push({q:p.slice(),f:f*R,age:0,total:ev.total,kind:ev.kind});
  if(W.log)W.log.push({j,kind:ev.kind,total:ev.total,R,T,f,s1sq,w:k.w.slice(),Y:k.kind==='gap'?k.Yg:Yof(k.w,S),un});
  return kids;}
function emit(W){const L=Lh(),S=W.S,o=W.o,dirs=L.fanDirs({chi:2*Math.PI*W.t/34,nray:o.nray,fan:o.fan}),src=S.balls[o.source]&&S.balls[o.source].visible?o.source:0,c=S.balls[src].c;
  for(const d of dirs)W.pk.push({p:c.slice(),u:d.slice(),f:1/dirs.length,w:maskOf(c,S),kind:'in',gen:0,skip:-2});
  W.emitted+=1;W.lastEmit=W.t;}
/* advance every packet by dt with the balls held at W.S; then call setGeom with the moved balls */
function step(W,dt){const o=W.o,S=W.S,out=[],cutF=o.cut/o.nray;
  for(const k0 of W.pk){const queue=[[k0,dt]];
    let nev=0;
    while(queue.length){const [k,Lrem]=queue.pop();
      if(k.f<cutF){W.cut+=k.f;continue;}
      if(++nev>4000){W.cut+=k.f;W.stuck+=k.f;continue;}
      if(k.kind==='tun'){const t=k.tun,left=t.len-t.s;
        if(Lrem<left){t.s+=Lrem;k.p=add(t.from,t.n,t.s);out.push(k);continue;}
        /* arrived on ball t.k: enter it with the incoming direction (folded inward if it points out) */
        const b=S.balls[t.k],q=add(t.from,t.n,t.len),nk=nrm(sub(q,b.c));let u=t.uIn;const un=dot(u,nk);if(un>0)u=add(u,nk,-2*un);
        const w=[t.k].concat(maskOf(add(q,u,1e-9),S).filter(x=>x!==t.k)).sort((a,b)=>a-b);
        queue.push([{p:q,u,f:k.f,w,kind:'in',gen:k.gen,skip:t.k},Lrem-left]);continue;}
      const ev=nextEvent(k.p,k.u,S,Lrem,k.skip);
      if(!ev){k.p=add(k.p,k.u,Lrem);if(Lrem>1e-7)k.skip=-2;out.push(k);continue;}
      const p=add(k.p,k.u,ev.s),Lr=Lrem-ev.s;
      if(ev.j===-1){W.out+=k.f;if(W.deposits.length<3000)W.deposits.push({q:p,f:k.f,age:0});continue;}
      for(const c of split(W,k,p,ev.j))queue.push([c,Lr]);}}
  if(out.length>o.maxPk){out.sort((a,b)=>b.f-a.f);for(let q=o.maxPk;q<out.length;q++)W.cut+=out[q].f;out.length=o.maxPk;}
  W.pk=out;W.t+=dt;
  /* B182 stocks per ball (hypothesis layer): source = arrival rate at the ball's walls, smoothed over one time unit */
  const a=Math.min(1,dt);for(let j=0;j<7;j++){W.K[j]+=W.push[j];W.pushRate[j]+=a*(W.push[j]/dt-W.pushRate[j]);W.push[j]=0;const rate=W.arriveAcc[j]/dt;W.arriveRate[j]+=a*(rate-W.arriveRate[j]);W.arriveAcc[j]=0;
    const s=W.stocks[j],P=W.arriveRate[j];const nx=Lh().stocksStep(s[0],s[1],P,P,P,o.kappa,o.ha,o.hb,dt);s[0]=nx[0];s[1]=nx[1];}
  for(const h of W.hits)h.age+=dt;W.hits=W.hits.filter(h=>h.age<0.6);for(const h of W.tunnels)h.age+=dt;W.tunnels=W.tunnels.filter(h=>h.age<2.5);for(const h of W.deposits)h.age+=dt;
  if(o.emitEvery>0&&W.t-W.lastEmit>=o.emitEvery-1e-9)emit(W);}
/* the balls moved (or one was hidden). A sphere that sweeps over light is a wall crossing at that moment: the packet is put on the
   sphere and split there by the same rule as any wall (direction mirrored into the new region if the wall overtook it: MODEL). */
function setGeom(W,S){W.S=S;if(!W.pk.length)return;const out=[];
  for(const k of W.pk){if(k.kind==='tun'||onAnySphere(k.p,S)){out.push(k);continue;}
    const m=maskOf(k.p,S),old=k.kind==='gap'?[]:k.w;let j=-1;
    for(const x of m)if(old.indexOf(x)<0){j=x;break;}
    if(j<0)for(const x of old)if(m.indexOf(x)<0){j=x;break;}
    if(j<0){out.push(k);continue;}
    const b=S.balls[j],n=nrm(sub(k.p,b.c)),nIn=m.indexOf(j)>=0?n.map(v=>-v):n,un=dot(k.u,nIn),u=un<0?add(k.u,nIn,-2*un):k.u.slice(),ps=add(b.c,n,b.r);
    if(!b.visible){/* a hidden ball: its light moves to the region it is in now, no wall (the ball is gone) */
      if(m.length===0){k.Yg=Yof(old.filter(x=>x!==j),S)/W.o.zgap;k.kind='gap';k.w=[];}else{k.kind='in';k.w=m;}out.push(k);continue;}
    W.swept+=k.f;W.sweptN++;
    for(const c of split(W,Object.assign({},k,{p:ps,u}),ps,j))out.push(c);}
  W.pk=out;}
function books(W){let inB=0,fr=0,tun=0;const by=new Float64Array(7);
  for(const k of W.pk){if(k.kind==='in'){inB+=k.f;let top=k.w[0],rk=-1;for(const j of k.w){const r=W.S.balls[j].rank;if(r>rk){rk=r;top=j;}}by[top]+=k.f;}else{fr+=k.f;if(k.kind==='tun')tun+=k.f;}}
  const E=Math.max(1,W.emitted);
  return {emitted:W.emitted,inBalls:inB,free:fr,tunnelling:tun,out:W.out,cut:W.cut,total:inB+fr+W.out+W.cut,frac:{inBalls:inB/E,free:fr/E,out:W.out/E,cut:W.cut/E,total:(inB+fr+W.out+W.cut)/E},
    byBall:Array.from(by),n:W.pk.length,freeIn:Object.assign({},W.freeIn),swept:W.swept,stuck:W.stuck,nTotal:W.nTotal,totalFlux:W.totalFlux};}
return {makeWorld,setGeom,step,emit,split,books,maskOf,Yof,gapWidth,nextEvent,ZW};
})();
/*LIGHT-END*/

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


if(typeof module!=='undefined'){module.exports={GEOM,LIGHT,VAC};}
else (function(){"use strict";
/* SCRIPT: seven_balls_v4 — drawing and controls (v3's, plus the vacuum between). Built on 3D Mixer Parts v1 (glow points, labels: Jeromie Beasley, 27 Oct 2026),
   the FL-LAYER-V1 look kept from v2 (glass balls, rims meeting, cores, clocks, names, great circles), and his LH-MATH-V1 for the light. */
const T=THREE,M=window.Mixer3D,PI=Math.PI,TAU=2*PI,cl=(x,a,b)=>Math.max(a,Math.min(b,x)),L=window.LH;
const r=1,ZW=GEOM.ZW;
const COL=['#fff2cc','#ff8d7c','#ff8d7c','#9be28a','#9be28a','#63d3ff','#63d3ff'],COLV=[[1,0.95,0.8],[1,0.55,0.49],[1,0.55,0.49],[0.61,0.89,0.54],[0.61,0.89,0.54],[0.39,0.83,1],[0.39,0.83,1]];
/* colours: one per axis (x red, y green, z blue) so a dent's wall shows whose sphere it is */
const hexOf=s=>parseInt(s.slice(1),16);
const fmt3=(x,n)=>Number.isFinite(x)?x.toFixed(n==null?3:n):'\u2014';
const P={z:[3,5,7],A:0.35,breathe:true,order:'xyz',margin:0.5,copC:1,outOp:1,cut:false,med:false,lab:true,vis:[1,1,1,1,1,1],look:'glass',ghost:0,speed:1,clocks:'equal',
  omega:3,zgap:ZW,window:'closed',emitEvery:2,source:0,kappa:1,ha:1,hb:0.2,
  show:{light:true,free:true,hits:true,rims:true,occ:true,push:true,record:true,clocks:true,names:true,circles:true,vac:true,pull:true,made:true},breathK:1,pumpEps:0.3};
const CLOCK={t:0,playing:true};
const geoOpts=()=>({z:P.z,A:P.A,breathe:P.breathe,k:P.breathK});
let S=GEOM.state(geoOpts(),0,P.margin,P.vis,P.order);
const DT=1/60;
/* ---------- the medium slot (same API as v1/v2) ---------- */
const medium={
  insideContainer:p=>GEOM.insideContainer(S,p), insideAnyBall:p=>GEOM.insideAnyBall(S,p), isMedium:p=>GEOM.isMedium(S,p),
  get container(){return {centre:[0,0,0],radius:S.R};}, get balls(){return S.balls.filter(b=>b.visible).map(b=>({id:b.id,name:b.name,c:b.c.slice(),r:b.r,z:b.z}));},
  plugins:[], scene:null,
  register(pl){this.plugins.push(pl);if(this.scene&&pl.init)pl.init(this.scene,this);return pl;},
  unregister(pl){const i=this.plugins.indexOf(pl);if(i>=0){this.plugins.splice(i,1);if(pl.dispose)pl.dispose();}}
};
Object.defineProperty(medium,'light',{get(){return LW?{books:LIGHT.books(LW),free:LW.pk.filter(k=>k.kind!=='in').map(k=>({p:k.p.slice(),f:k.f,kind:k.kind})),tunnels:LW.tunnels.map(h=>({a:h.a,b:h.b,f:h.f,age:h.age}))}:null;}});
window.medium=medium;window.GEOM=GEOM;window.LIGHT=LIGHT;
medium.register({name:'empty (placeholder)',init(){},update(){},rebuild(){},dispose(){}});

/* ---------- ball surfaces: exact sphere per fragment; pairwise dent rule by rank ---------- */
const VS=`varying vec3 vW;void main(){vec4 w=modelMatrix*vec4(position,1.0);vW=w.xyz;gl_Position=projectionMatrix*viewMatrix*w;}`;
const FS=`
uniform int uId;uniform int uPart;uniform int uMode;uniform vec3 uC[7];uniform float uVis[7];uniform float uRank[7];uniform float uR;
uniform vec3 uCol;uniform vec3 uDentCol;uniform float uOpacity;uniform float uCut;uniform vec3 uCutN;uniform vec3 uCam;uniform float uGlass;uniform float uGlow;
varying vec3 vW;
void main(){
  vec3 c=uC[uId];
  vec3 p=c+uR*normalize(vW-c);
  if(uCut>0.5&&dot(p,uCutN)>0.0)discard;
  float myRank=uRank[uId];float dent=0.0;float seam=0.0;
  for(int i=0;i<7;i++){
    if(i==uId||uVis[i]<0.5)continue;
    float di=distance(p,uC[i]);
    if(di<uR){if(uRank[i]>myRank)discard;dent=1.0;}
    seam=max(seam,1.0-smoothstep(0.0,0.012,abs(di-uR)));
  }
  if(uPart==0&&dent<0.5)discard;
  if(uPart==1&&dent>0.5)discard;
  if(uMode==1){gl_FragColor=vec4(p,float(uId)+1.0+0.5*dent);return;}
  vec3 n=normalize(p-c);if(!gl_FrontFacing)n=-n;
  vec3 v=normalize(uCam-p);
  float ring=0.0;
  if(dent>0.5&&length(c)>1e-6){float a=acos(clamp(dot(normalize(p-c),normalize(c)),-1.0,1.0))/0.2617994;float q=abs(fract(a)-0.5);ring=1.0-smoothstep(0.38,0.47,q);}
  if(uGlass>0.5){
    float f=pow(1.0-abs(dot(n,v)),2.2);
    vec3 b=dent>0.5?uDentCol*1.7:uCol;
    vec3 col=b*(0.05+0.42*f)*(0.55+1.5*uGlow)*uOpacity+b*0.07*uGlow*uOpacity;
    if(dent>0.5)col+=uDentCol*0.10+uDentCol*ring*0.45;
    col+=vec3(0.95,0.97,1.0)*seam*0.55;
    gl_FragColor=vec4(col,1.0);return;}
  vec3 L1=normalize(vec3(.35,.8,.5));
  float lam=.22+.25*max(dot(n,v),0.0)+.75*max(dot(n,L1),0.0);
  float spec=pow(max(dot(n,normalize(L1+v)),0.0),40.0)*.35;
  float rim=pow(1.0-max(dot(n,v),0.0),3.0)*.2+spec;
  vec3 base=dent>0.5?uDentCol:uCol;
  vec3 col=base*lam*(0.8+0.6*uGlow)+rim;if(dent>0.5)col=mix(col,uDentCol*1.6,ring*0.35);col=mix(col,vec3(0.95,0.97,1.0),seam*.8);
  gl_FragColor=vec4(col,uOpacity);
}`;
const GEO=new T.SphereGeometry(r,160,112);
const world=new T.Group();
const uShared={uC:{value:S.balls.map(b=>new T.Vector3(...b.c))},uVis:{value:S.balls.map(b=>b.visible?1:0)},uRank:{value:S.balls.map(b=>b.rank)},uR:{value:r},uCut:{value:0},uCutN:{value:new T.Vector3(0,0,1)},uCam:{value:new T.Vector3()},uMode:{value:0},uGlass:{value:1}};
function mat(id,part,col,dentCol){return new T.ShaderMaterial({vertexShader:VS,fragmentShader:FS,side:T.DoubleSide,uniforms:Object.assign({},uShared,{uId:{value:id},uPart:{value:part},uCol:{value:new T.Color(col)},uDentCol:{value:new T.Color(dentCol)},uOpacity:{value:1},uGlow:{value:0}})});}
const BALL=[];
{const g=new T.Group();g.name='C';const m=new T.Mesh(GEO,mat(0,2,hexOf(COL[0]),hexOf(COL[0])));g.add(m);world.add(g);BALL.push({g,dent:null,out:m});}
for(let i=0;i<6;i++){const g=new T.Group();g.name=S.balls[i+1].name;const base=new T.Color(COL[i+1]);const dc=base.clone().multiplyScalar(.72).getHex(),oc=base.getHex();
  const dm=new T.Mesh(GEO,mat(i+1,0,oc,dc)),om=new T.Mesh(GEO,mat(i+1,1,oc,dc));om.renderOrder=2;g.add(dm,om);world.add(g);BALL.push({g,dent:dm,out:om});}
const ALLMATS=()=>BALL.flatMap(b=>b.dent?[b.dent.material,b.out.material]:[b.out.material]);
const LAB=new T.Group();world.add(LAB);
const CONT=new T.Group();world.add(CONT);
const MED=new T.Group();world.add(MED);
const FIELD=new T.Group();world.add(FIELD);

/* ---------- FL-LAYER-V1 drawing parts kept from v2 (seg lines, glow points), plus the rays ---------- */
const KS=1/2.6;
const seg=(n,op,add,depth)=>{const g=new T.BufferGeometry();g.setAttribute('position',new T.BufferAttribute(new Float32Array(n*6),3));g.setAttribute('color',new T.BufferAttribute(new Float32Array(n*6),3));
  const m=new T.LineSegments(g,new T.LineBasicMaterial({vertexColors:true,transparent:true,opacity:op,depthWrite:false,depthTest:!!depth,blending:add===false?T.NormalBlending:T.AdditiveBlending}));m.frustumCulled=false;m.renderOrder=5;FIELD.add(m);let i=0;
  return {mesh:m,reset(){i=0;},add(a,b,c){if(i>=n)return;const p=g.attributes.position,q=g.attributes.color;p.setXYZ(2*i,a.x,a.y,a.z);p.setXYZ(2*i+1,b.x,b.y,b.z);q.setXYZ(2*i,c[0],c[1],c[2]);q.setXYZ(2*i+1,c[0],c[1],c[2]);i++;},done(){g.setDrawRange(0,2*i);g.attributes.position.needsUpdate=g.attributes.color.needsUpdate=true;}};};
const NPK=2600,NHIT=1500,NTUN=1500,NDEP=3000;
const rayLine=seg(NPK,0.9),tunLine=seg(NTUN,1),rimLine=seg(24*96,1),occLine=seg(24*48,1),pushLine=seg(12,1),clockLine=seg(7*40,1),circLine=seg(7*3*128,1,true,true);
const pts=(n,size)=>{const p=M.points(n,size);p.material.depthTest=false;p.renderOrder=6;p.frustumCulled=false;FIELD.add(p);return p;};
const vacLine=seg(12*(2*64+2),1),pullLine=seg(24,1),madePts=pts(12*24,0.11),leakPts=pts(24*8,0.07),fillPts=pts(12*90,0.085);
const pkPts=pts(NPK,0.2),hitPts=pts(NHIT,0.09),depPts=pts(NDEP,0.08),corePts=pts(7,1.5*KS),handPts=pts(7,0.4*KS);
const zero3=[0,0,0],_r=new T.Vector3(),_u=new T.Vector3(),FAR=new T.Vector3(0,-999,0),V=(a)=>new T.Vector3(a[0],a[1],a[2]);
let labels=[],labelTxt=[];

/* ---------- light (SB-LIGHT-V3, his split everywhere) ---------- */
let LW=null,BK=null,acc=0;const tau=new Float64Array(7);
let VW=null;const sFnV=(a,b,t)=>{const o=geoOpts();return Math.hypot(GEOM.dOfR(GEOM.rOf(o,a,t),r),GEOM.dOfR(GEOM.rOf(o,b,t),r))-2*r;};
const sDot=(a,b,t)=>(sFnV(a,b,t+1e-4)-sFnV(a,b,t-1e-4))/2e-4;
function lightOpts(){return {omega:P.omega,zgap:P.zgap,window:P.window,emitEvery:P.emitEvery,source:P.source,kappa:P.kappa,ha:P.ha,hb:P.hb};}
function buildLight(src){if(src!=null)P.source=src;VW=VAC.makeVac({zgap:P.zgap,r});VW.t=CLOCK.t;VAC.stepVac(VW,sFnV,CLOCK.t,1e-9);LW=LIGHT.makeWorld(lightOpts());LW.t=CLOCK.t;LIGHT.setGeom(LW,GEOM.state(geoOpts(),CLOCK.t,P.margin,P.vis,P.order));LIGHT.emit(LW);tau.fill(0);acc=0;readLight();}
function readLight(){BK=LIGHT.books(LW);}
function stepLight(n){for(let k=0;k<n;k++){const tv=LW.t;LIGHT.step(LW,DT);if(VW){VW.o.zgap=P.zgap;VAC.stepVac(VW,sFnV,tv,DT);}const Sn=GEOM.state(geoOpts(),LW.t,P.margin,P.vis,P.order);LIGHT.setGeom(LW,Sn);
    for(let i=0;i<7;i++)tau[i]+=DT*(P.clocks==='z'?1/Sn.balls[i].z:1);}
  CLOCK.t=LW.t;}

/* ---------- static parts: labels, container, medium dots ---------- */
function rebuild(){
  S=GEOM.state(geoOpts(),CLOCK.t,P.margin,P.vis,P.order);
  uShared.uCut.value=P.cut?1:0;uShared.uGlass.value=P.look==='glass'?1:0;
  const glass=P.look==='glass';
  ALLMATS().forEach(m=>{m.blending=glass?T.AdditiveBlending:T.NormalBlending;m.transparent=glass;m.depthWrite=!glass;m.needsUpdate=true;});
  const cm=BALL[0].out.material;cm.uniforms.uOpacity.value=P.copC;if(!glass){cm.transparent=P.copC<1;cm.depthWrite=P.copC>=1;}
  for(let i=1;i<7;i++){const o=BALL[i].out,gh=i===P.ghost;o.visible=P.outOp>0||gh;o.material.uniforms.uOpacity.value=gh?(glass?0.25:0.13):P.outOp;if(!glass){o.material.transparent=gh||P.outOp<1;o.material.depthWrite=!gh&&P.outOp>=1;}o.renderOrder=gh?9:2;BALL[i].dent.material.uniforms.uOpacity.value=1;}
  labels.forEach(l=>LAB.remove(l));labels=[];labelTxt=[];
  while(CONT.children.length){const o=CONT.children[0];CONT.remove(o);if(o.geometry)o.geometry.dispose();}
  CONT.add(new T.Mesh(new T.SphereGeometry(S.R,40,26),new T.MeshBasicMaterial({color:0x2a4a6e,wireframe:true,transparent:true,opacity:.10,depthWrite:false})));
  const cl2=M.label('container  R = '+S.R.toFixed(2)+' r',  '#7a8a9b',.16);cl2.position.set(0,-S.R-.12,0);CONT.add(cl2);
  while(MED.children.length){const o=MED.children[0];MED.remove(o);if(o.geometry)o.geometry.dispose();}
  medCand=null;
  if(P.med){const c=[];let seed=7;const rnd=()=>{seed=(seed*16807)%2147483647;return seed/2147483647;};
    for(let k=0;k<30000&&c.length<3*12000;k++){const p=[(rnd()*2-1)*S.R,(rnd()*2-1)*S.R,(rnd()*2-1)*S.R];if(GEOM.len(p)<S.R)c.push(...p);}
    medCand=new Float32Array(c);const g=new T.BufferGeometry();g.setAttribute('position',new T.BufferAttribute(new Float32Array(c.length),3));
    medPts=new T.Points(g,new T.PointsMaterial({color:0x8fe3ff,size:.04,transparent:true,opacity:.7,depthWrite:false}));medPts.frustumCulled=false;MED.add(medPts);
    const ml=M.label('medium slot (empty): window.medium','#63d3ff',.15);ml.position.set(0,S.R+.12,0);MED.add(ml);}
  apply();
  medium.plugins.forEach(pl=>pl.rebuild&&pl.rebuild(medium));
  if(!CLOCK.playing)scheduleCheck();
}
let medCand=null,medPts=null;

/* ---------- per frame ---------- */
function apply(){
  S=GEOM.state(geoOpts(),CLOCK.t,P.margin,P.vis,P.order);
  S.balls.forEach((b,i)=>{BALL[i].g.position.set(...b.c);uShared.uC.value[i].set(...b.c);uShared.uVis.value[i]=b.visible?1:0;uShared.uRank.value[i]=b.rank;BALL[i].g.visible=b.visible;});
  if(medCand&&medPts){const a=medPts.geometry.attributes.position.array;let n=0;for(let k=0;k<medCand.length;k+=3){const p=[medCand[k],medCand[k+1],medCand[k+2]];if(P.cut&&p[2]>0)continue;if(GEOM.isMedium(S,p)){a[n++]=p[0];a[n++]=p[1];a[n++]=p[2];}}medPts.geometry.setDrawRange(0,n/3);medPts.geometry.attributes.position.needsUpdate=true;}
  draw();readout();
}
function circlePts(cc,n,from,to){const [v,w]=GEOM.basis(cc.normal),out=[];for(let s=0;s<=n;s++){const t=from+(to-from)*s/n;out.push(new T.Vector3(cc.centre[0]+cc.radius*(Math.cos(t)*v[0]+Math.sin(t)*w[0]),cc.centre[1]+cc.radius*(Math.cos(t)*v[1]+Math.sin(t)*w[1]),cc.centre[2]+cc.radius*(Math.cos(t)*v[2]+Math.sin(t)*w[2])));}return out;}
function draw(){
  const sh=P.show;_r.setFromMatrixColumn(cam.matrixWorld,0);_u.setFromMatrixColumn(cam.matrixWorld,1);
  rayLine.reset();tunLine.reset();rimLine.reset();occLine.reset();pushLine.reset();clockLine.reset();circLine.reset();
  const cutOK=p=>!(P.cut&&p[2]>0);
  /* packets of light: gold in the balls, violet free in the gap; each with a short tail along its direction */
  let np=0;
  if(LW)for(const k of LW.pk){if(np>=NPK)break;if(!cutOK(k.p))continue;const free=k.kind!=='in';if(free?!sh.free:!sh.light)continue;
    const g=Math.min(1,0.18+1.1*Math.pow(k.f*9,0.33)),c=free?[0.75*g,0.55*g,g]:[g,0.82*g,0.42*g];
    M.setPt(pkPts,np,V(k.p),c);const tail=free?0.16:0.14;rayLine.add(V([k.p[0]-tail*k.u[0],k.p[1]-tail*k.u[1],k.p[2]-tail*k.u[2]]),V(k.p),[c[0]*0.6,c[1]*0.6,c[2]*0.6]);np++;}
  for(let q=np;q<NPK;q++)M.setPt(pkPts,q,FAR,zero3);
  /* total returns (rose flashes) */
  let nh=0;if(LW&&sh.hits)for(const h of LW.hits){if(nh>=NHIT)break;if(!h.total||!cutOK(h.q))continue;const g=Math.min(1,(1-h.age/0.6)*(0.25+1.5*Math.pow(h.f*9,0.4)));M.setPt(hitPts,nh++,V(h.q),[g,0.35*g,0.55*g]);}
  for(let q=nh;q<NHIT;q++)M.setPt(hitPts,q,FAR,zero3);
  /* free light that tunnelled across a gap: violet bridges, fading */
  if(LW&&sh.free)for(const h of LW.tunnels){if(!cutOK(h.a))continue;const g=Math.min(1,(1-h.age/2.5)*(0.3+3*Math.pow(h.f*9,0.4)));tunLine.add(V(h.a),V(h.b),[0.7*g,0.5*g,g]);}
  /* record on the ground: light that left through the container wall */
  let nd=0;if(LW&&sh.record)for(const h of LW.deposits){if(nd>=NDEP)break;if(!cutOK(h.q))continue;const g=Math.min(1,0.2+2*Math.pow(h.f*9,0.4));M.setPt(depPts,nd++,V(h.q),[g,0.75*g,0.3*g]);}
  for(let q=nd;q<NDEP;q++)M.setPt(depPts,q,FAR,zero3);
  /* rims meeting: every contact circle (C-side gold, side-side white); occupation arc C = 1/(z + 1) of the owner (his hypothesis) */
  const PR=GEOM.pairs(S);
  for(const q of PR){const c=q.side?[0.85,0.9,1.0]:[1.0,0.82,0.45];
    if(sh.rims){const pp=circlePts(q.circle,96,0,TAU);for(let s=1;s<pp.length;s++){if(P.cut&&(pp[s].z>0||pp[s-1].z>0))continue;rimLine.add(pp[s-1],pp[s],c);}}
    if(sh.occ){const z=S.balls[q.owner].z,Cocc=1/(z+1),cc=Object.assign({},q.circle,{radius:q.circle.radius*1.04}),pp=circlePts(cc,48,0,TAU*Cocc);
      for(let s=1;s<pp.length;s+=2){if(P.cut&&(pp[s].z>0||pp[s-1].z>0))continue;occLine.add(pp[s-1],pp[s],[1,0.7,0.28]);}}}
  /* push on each side ball (his oblique push 2R cos^2 theta, smoothed rate) */
  if(LW&&sh.push)for(let i=1;i<7;i++){const b=S.balls[i];if(!b.visible||!cutOK(b.c))continue;const pr=LW.pushRate[i],l=Math.min(1.2,0.25*Math.sqrt(pr));
    pushLine.add(V(b.c),V([b.c[0]+b.axis[0]*l,b.c[1]+b.axis[1]*l,b.c[2]+b.axis[2]*l]),[1,0.55,0.2]);}
  /* great circles of each ball, dropped where the dent rule removes that ball's surface */
  if(sh.circles)for(let i=0;i<7;i++){const b=S.balls[i];if(!b.visible)continue;const cv=COLV[i];
    for(let q=0;q<3;q++){const op=q===0?0.5:0.2;let prev=null,pk=false;
      for(let s=0;s<=128;s++){const a=TAU*s/128,cs=r*Math.cos(a),sn=r*Math.sin(a),o=q===0?[cs,0,sn]:q===1?[cs,sn,0]:[0,cs,sn],p=[b.c[0]+o[0],b.c[1]+o[1],b.c[2]+o[2]];
        let ok=cutOK(p)&&GEOM.classify(S,i,p)!==-1;const v=new T.Vector3(...p);
        if(prev&&ok&&pk)circLine.add(prev,v,[cv[0]*op,cv[1]*op,cv[2]*op]);prev=v;pk=ok;}}}
  const by=BK?BK.byBall:[0,0,0,0,0,0,0],E=BK?Math.max(1,BK.emitted):1;
  for(let i=0;i<7;i++){const b=S.balls[i],p=V(b.c),hidden=!b.visible||(P.cut&&b.c[2]>0&&i>0);
    const s=Math.min(1,1.3*Math.pow(by[i]/E,0.35));M.setPt(corePts,i,hidden?FAR:p,hidden?zero3:[COLV[i][0]*s,COLV[i][1]*s,COLV[i][2]*s]);
    const glow=hidden?0:s;BALL[i].out.material.uniforms.uGlow.value=glow;if(BALL[i].dent)BALL[i].dent.material.uniforms.uGlow.value=glow;
    const c=p.clone().addScaledVector(_u,r+0.42),rc=0.42*KS,cc=COLV[i];
    if(sh.clocks&&!hidden){let prev=null;for(let q=0;q<=32;q++){const t=TAU*q/32,pt=c.clone().addScaledVector(_r,rc*Math.sin(t)).addScaledVector(_u,rc*Math.cos(t));if(prev)clockLine.add(prev,pt,[0.5*cc[0],0.5*cc[1],0.5*cc[2]]);prev=pt;}
      const ang=PI*tau[i],tip=c.clone().addScaledVector(_r,0.9*rc*Math.sin(ang)).addScaledVector(_u,0.9*rc*Math.cos(ang));clockLine.add(c,tip,cc);M.setPt(handPts,i,tip,cc);}else M.setPt(handPts,i,FAR,zero3);
    const txt=i===0?'ball C':'ball '+b.name+'  z '+b.z.toFixed(2)+(P.clocks==='z'?'  clock \u00f7'+b.z.toFixed(1):'');
    if(labelTxt[i]!==txt){if(labels[i])LAB.remove(labels[i]);const lb=M.label(txt,COL[i],0.75*KS);lb.material.depthTest=false;lb.renderOrder=7;LAB.add(lb);labels[i]=lb;labelTxt[i]=txt;}
    labels[i].visible=sh.names&&P.lab&&!hidden;labels[i].position.copy(p).addScaledVector(_u,r+(sh.clocks?0.8:0.18));}
  drawVac();
  [rayLine,tunLine,rimLine,occLine,pushLine,clockLine,circLine,vacLine,pullLine].forEach(x=>x.done());[pkPts,hitPts,depPts,corePts,handPts,madePts,leakPts,fillPts].forEach(M.flush);
}

/* the vacuum between (SB-VAC-V1): every neighbour gap that stands open */
let vacPhase=0;
function drawVac(){vacLine.reset();pullLine.reset();const sh=P.show;let nm=0,nl=0,nf=0;vacPhase+=0.07;
  if(VW)for(const [i,j] of VAC.NB){const a=S.balls[i],b=S.balls[j];if(!a.visible||!b.visible)continue;const G=VW.g[VAC.kindOf(i,j)];if(!G.open)continue;
    if(P.cut&&(a.c[2]>0||b.c[2]>0))continue;
    const D=GEOM.dist(a.c,b.c),e=[0,1,2].map(q=>(b.c[q]-a.c[q])/D),pa=[0,1,2].map(q=>a.c[q]+e[q]*r),pb=[0,1,2].map(q=>b.c[q]-e[q]*r),mid=[0,1,2].map(q=>(pa[q]+pb[q])/2);
    const lg=Math.log10(1+G.F),g=Math.min(1,0.25+0.25*lg);
    if(sh.vac){vacLine.add(V(pa),V(pb),[0.9*g,0.8*g,1.0*g]);
      /* the vacuum itself: the space between the two faces, out to the patch radius, filled (violet) */
      {const rho=Math.min(0.6,Math.sqrt(r*G.s)),[v,w]=GEOM.basis(e);
        for(let q=0;q<90&&nf<12*90;q++){const u=rho*Math.sqrt(((q*0.7548776662)%1)),ph=TAU*((q*0.5698402910)%1),dz=r-Math.sqrt(Math.max(0,r*r-u*u)),ax=-dz+(G.s+2*dz)*((q*0.3819660113+vacPhase*0.05)%1);
          const p=[0,1,2].map(m=>pa[m]+ax*e[m]+u*(Math.cos(ph)*v[m]+Math.sin(ph)*w[m]));const fl=g*(0.55+0.45*Math.sin(vacPhase*2+q));M.setPt(fillPts,nf++,V(p),[Math.min(1,0.8*fl+0.15),Math.min(1,0.6*fl+0.1),1.0]);}}
      /* the patch that carries the pull (proximity force): radius sqrt(r s) on each face */
      const rho=Math.min(0.6,Math.sqrt(r*G.s)),[v,w]=GEOM.basis(e);
      for(const [cc,sg] of [[pa,-1],[pb,1]]){const dz=r-Math.sqrt(Math.max(0,r*r-rho*rho));let prev=null;
        for(let q=0;q<=64;q++){const t=TAU*q/64,p=[0,1,2].map(m=>cc[m]+sg*dz*e[m]+rho*(Math.cos(t)*v[m]+Math.sin(t)*w[m]));const pv=V(p);if(prev)vacLine.add(prev,pv,[0.85,0.75,1.0]);prev=pv;}}}
    if(sh.pull){const L=Math.min(0.9,0.16*lg+0.12);pullLine.add(V(a.c),V([a.c[0]+e[0]*L,a.c[1]+e[1]*L,a.c[2]+e[2]*L]),[0.35,0.95,1]);pullLine.add(V(b.c),V([b.c[0]-e[0]*L,b.c[1]-e[1]*L,b.c[2]-e[2]*L]),[0.35,0.95,1]);}
    if(sh.made){const En=G.made,bright=Math.min(1,Math.pow(En*40,0.33));
      for(let q=0;q<24&&nm<12*24;q++){const ph=vacPhase*(1+q%5)+q*2.399,rr=Math.min(0.5,Math.sqrt(r*G.s))*Math.sqrt(((q*0.618)%1)),p=[0,1,2].map(m=>mid[m]+rr*(Math.cos(ph)*GEOM.basis(e)[0][m]+Math.sin(ph)*GEOM.basis(e)[1][m]));
        const fl=bright*(0.6+0.4*Math.sin(ph*3));M.setPt(madePts,nm++,V(p),[fl,0.95*fl,fl]);}
      const lr=G.modes.reduce((s,M)=>s+M.n*M.k*Math.PI/G.s*VAC.leak(G.s,P.zgap),0),lb=Math.min(1,Math.pow(lr*10,0.33));
      for(let q=0;q<4&&nl<24*8;q++){const f=((vacPhase*0.5+q/4)%1);for(const [cc,c0,sg] of [[pa,a.c,-1],[pb,b.c,1]]){const p=[0,1,2].map(m=>cc[m]+(c0[m]-cc[m])*0.35*f);M.setPt(leakPts,nl++,V(p),[lb*(1-f),0.85*lb*(1-f),0.5*lb*(1-f)]);}}}}
  for(let q=nf;q<12*90;q++)M.setPt(fillPts,q,FAR,zero3);for(let q=nm;q<12*24;q++)M.setPt(madePts,q,FAR,zero3);for(let q=nl;q<24*8;q++)M.setPt(leakPts,q,FAR,zero3);}

/* ---------- every rule in the page, with its tag ---------- */
const RULES=[
 ['exact','Dent rule, all seven pairwise: a ball\u2019s surface is removed inside every higher-ranked ball; the wall seen in the hole is that ball\u2019s own sphere (checked live, and pixel by pixel)'],
 ['lean','\u0393 = tanh(ln z / 2) = (z \u2212 1)/(z + 1): votkp-lean Smith.lean smith_identity; event-horizon-lean Edition10 tanh_half_log'],
 ['lean','One face: r = (Y\u2081 \u2212 Y\u2082)/(Y\u2081 + Y\u2082), R + (Y\u2082/Y\u2081)|t|\u00b2 = 1: Edition10 step_matching, flux_balance'],
 ['lean','Oblique admittance Y = \u03c9\u221a(a \u2212 a\u2081sin\u00b2\u03b8\u2081): Edition10 admittance'],
 ['lean','Refraction a\u2081 sin\u00b2\u03b8\u2081 = a\u2082 sin\u00b2\u03b8\u2082: square-case-lean three_body_refraction_is_squared_snell; upg-lean refraction_law'],
 ['lean','Total return past the critical angle, sin \u03b8c = Y\u2082/Y\u2081 (= 1/z entering a side ball): Edition10 total_reflection, turning_point'],
 ['num','The gap as an evanescent film, LH tunnelGap, |r|\u00b2 + |t|\u00b2 = 1: his check K7 only (ingredients total_reflection, film_is_oplus are Lean; the gap identity is not)'],
 ['paper','B182 stocks \u1e8b = \ud835\udcab \u2212 (\u03ba + a)x + by, \u1e8f = ax \u2212 by; residence (1 + a/b)/\u03ba; b = 0 keeps a/(\u03ba + a): Atlas B182 (Black Hole v8.4 \u00a74.5), no Lean; his check K15'],
 ['paper','The wall z = 3 + 2\u221a2: \u0393\u00b2 = \u00bd (Two Trees v4 Thm 5.3; Lean only brackets it: z = 5 below, 7 above)'],
 ['hyp','Electron occupation C = 1/(z + 1) per face (amber arc = fraction C of the rim). The algebra 1 \u2212 2C = \u0393, 4C(1 \u2212 C) = T is Lean (Edition10 fermion_impedance, fermion_smith, particle_hole); reading C as electrons is his hypothesis. Pauli exclusion is NOT modelled.'],
 ['hyp','Push on a wall P = 2R cos\u00b2\u03b8 per hit, record K = \u222b P dt: his own chip says \u201cP = 2R as a physical pressure is untested\u201d'],
 ['hyp','The sea of electrons is the ground and keeps the record (his LH hypothesis layer). Here the ground is the container wall (MODEL)'],
 ['hyp','Clock rate 1/z (Flock), only if chosen'],
 ['drive','Breathing: his drive LH-MATH-V1 rOf, r\u2090 = ln z\u0304\u2090 + A sin(2\u03c0t/P\u2090 + \u03c6\u2090), P = 8, 13, 21, phases a third apart. A schedule, not math'],
 ['drive','Light source: his fan LH fanDirs, 9 rays over \u00b162\u00b0, turning \u03c7 = 2\u03c0t/34; a new fan every 2 (his v4 file\u2019s cadence)'],
 ['v4','Side ball centre d = r(1 + tanh(ln z/4)): its near point sits on his face apex \u03c1 = tanh(h/2), h = ln z/2 (LH-MIXER-V2 capParams). From his v4 file (AI-made); equals his face only on the wall, d = \u221a2 r, 90\u00b0'],
 ['v4','Admittance inside overlaps Y = \u03a0 1/z over the side balls holding the light (C counts 1): his v4 file\u2019s extension of nodeAdmittance (identity interface_smith is Lean; the assignment is a model)'],
 ['v4','Light moves in straight lines at speed 1 among the seven spheres (v4 \u201croom\u201d mode)'],
 ['model','Dent ownership between side balls: x pushes into y and z, y into z (toggle reverses). One of the two balls has to give way in a lens; nothing in his files says which'],
 ['model','Gap admittance one step below the region the light leaves: Y_gap = Y / z_gap, z_gap = 3 + 2\u221a2 by default'],
 ['model','Window closed (default): the gap face returns propagating light whole (his v4 ground rule), so light gets into the gap only by tunnelGap. The evanescent tail still uses Y_gap: a mixed rule. Window open: his split passes 1 \u2212 R into the gap'],
 ['model','Gap width for tunnelGap: straight along the face normal to the next ball; none in reach \u2192 whole return. Tunnelled light enters the far ball with its incoming direction, no second split'],
 ['model','A breathing sphere that sweeps over light is a wall crossing at that moment, split by the same rule (direction mirrored into the new region if the wall overtook it)'],
 ['model','Light reaching the container wall leaves (booked \u201cout\u201d, drawn as the record)'],
 ['model','B182 stocks per ball are driven by the normal flux arriving at that ball\u2019s walls (f\u00b7cos\u03b8 per hit, smoothed over 1 time unit); they do not feed back into the rays'],
 ['exact','The vacuum is only in the twelve neighbour gaps (side balls on perpendicular axes); opposite side balls have C between them. Gap s = hypot(d\u2090, d\u1d66) \u2212 2r, so the twelve gaps are three kinds (x\u2013y, y\u2013z, x\u2013z), four each. Two equal neighbours touch exactly at z = 3 + 2\u221a2: below the wall they overlap, above it the gap opens'],
 ['cited','Static pull between two of his faces: Lifshitz (1956) energy per area \u2212\u03b7\u03c0\u00b2\u0127c/720s\u00b3, with each face his split at index ratio z_gap (\u0393_f = (z_gap \u2212 1)/(z_gap + 1) at normal incidence); \u03b7 = 0.456 at the wall. Checked against an independent high-precision run (CASIMIR-WALL-01)'],
 ['model','No dispersion: z_gap held at every frequency. Ball\u2013ball pull by the proximity force rule, U = \u2212\u03b7\u03c0\u00b3\u0127c r/1440s\u00b2, F = \u03b7\u03c0\u00b3\u0127c r/720s\u00b3, good only for s \u226a r. The pull is drawn; it does not move the balls'],
 ['model','The gap\u2019s own light: standing modes across the gap along the line of centres, \u03c9\u2096 = k\u03c0/s (k = 1, 2, 3); each leaks through its two faces at \u03ba = \u2212ln(R_f\u00b2)/2s, R_f = \u0393_f\u00b2. Gaps under 0.02 r are treated as shut'],
 ['cited','Light made by the breathing (dynamic Casimir): for q\u0308 + \u03c9(t)\u00b2q = 0 the instantaneous mode obeys \u0227 = \u2212i\u03c9a \u2212 (\u03ba/2)a + (\u03c9\u0307/2\u03c9)a\u2020; from the vacuum, n = \u27e8a\u2020a\u27e9, m = \u27e8aa\u27e9 obey \u1e45 = \u2212\u03ban + (\u03c9\u0307/\u03c9)Re m, \u1e41 = (\u22122i\u03c9 \u2212 \u03ba)m + (\u03c9\u0307/2\u03c9)(2n + 1). Checked against the mode function itself (no loss) to 1e\u22124'],
 ['exact','Vacuum books: work done by the breathing on the gap light = light in the gaps now + leaked into the balls + held when a gap shut. Kept apart from the ray books, which stay exact'],
 ['model','Breath speed \u00d7k scales the time in his drive (k = 1 is his drive). Resonance needs the gap pumped at twice its own light, period about s: for s = 0.05 and P = 8, k \u2248 160'],
 ['model','Bookkeeping: packets below 1e\u22123 of a ray, the faintest past 2500 packets, and grazing packets past 4000 bounces in one step go to \u201ccut\u201d (counted, not lost)']];
const TAGN={cited:'CITED PHYSICS',exact:'EXACT',lean:'LEAN',num:'HIS-CHECKED-NUMERICALLY',paper:'PAPER',hyp:'HYPOTHESIS (his)',drive:'HIS DRIVE',v4:'MODEL \u00b7 his v4 file',model:'MODEL (new, mine)'};

/* ---------- page ---------- */
const CSS=':root{color-scheme:dark}html,body{height:100%;margin:0;background:#05070b;color:#dfe7ef;font-family:"DejaVu Sans",system-ui,sans-serif;font-size:13.5px;overflow:hidden}#stage{position:fixed;inset:0;touch-action:none;cursor:grab}.panel{position:fixed;top:12px;left:12px;width:360px;max-height:calc(100% - 24px);overflow:auto;background:rgba(9,13,20,.9);border:1px solid #1f2a38;border-radius:8px;padding:14px;display:grid;gap:9px;box-sizing:border-box}@media(max-width:640px){.panel{top:auto;bottom:8px;left:8px;right:8px;width:auto;max-height:46%}.strip{display:none}}body.clean .panel,body.clean .strip{display:none}.ce{position:fixed;right:12px;top:12px;display:none}body.clean .ce{display:block}h1{font-size:15px;letter-spacing:.05em;text-transform:uppercase;margin:0}.by{font-size:10.5px;color:#7a8a9b}button{font:inherit;color:#dfe7ef;background:#101824;border:1px solid #1f2a38;border-radius:5px;padding:4px 8px;cursor:pointer}button[aria-pressed=true]{border-color:#f2c14e;color:#f2c14e}.eq{color:#f2c14e;font-size:12px;line-height:1.5;white-space:pre-line}.what{color:#a4b1bf;line-height:1.45;margin:0}.ctl{display:grid;gap:6px}.ctl label{display:grid;grid-template-columns:1fr auto;gap:2px 8px;font-size:12px;color:#a4b1bf}.ctl input[type=range]{grid-column:1/-1;width:100%;accent-color:#63d3ff}.tg{display:flex;flex-wrap:wrap;gap:4px 10px;font-size:12px;color:#a4b1bf}.tg label{display:flex;gap:4px;align-items:center}.tg input{accent-color:#63d3ff;margin:0}.rd{font-size:11px;line-height:1.55;border-top:1px solid #1f2a38;padding-top:7px;color:#a4b1bf;font-variant-numeric:tabular-nums}.rd div{display:flex;justify-content:space-between;gap:10px}.rd b{color:#dfe7ef;font-weight:400;text-align:right}.rd table{width:100%;border-collapse:collapse}.rd td,.rd th{text-align:right;padding:0 3px;font-weight:400}.rd th{color:#7a8a9b}.rd td:first-child,.rd th:first-child{text-align:left}.row{display:flex;gap:6px;flex-wrap:wrap}.ck{font-size:11px;line-height:1.45;border-top:1px solid #1f2a38;padding-top:7px;color:#a4b1bf;font-variant-numeric:tabular-nums}.ck div{display:grid;grid-template-columns:1fr auto auto;gap:6px;padding:1px 0}.pass{color:#3fbf80}.fail{color:#e8553f;font-weight:700}.ck h2{font-size:12px;margin:0 0 4px;color:#dfe7ef;font-weight:600}.slot{font-size:11px;color:#63d3ff;border-left:2px solid #63d3ff;padding-left:7px;line-height:1.5}.grade{font-size:11px;line-height:1.5;color:#a4b1bf;border-left:2px solid #f2c14e;padding-left:7px}.grade b{color:#f2c14e;font-weight:600}select{font:inherit;font-size:12px;color:#dfe7ef;background:#101824;border:1px solid #1f2a38;border-radius:5px}.strip{position:fixed;left:390px;right:12px;bottom:12px;background:rgba(9,13,20,.9);border:1px solid #1f2a38;border-radius:8px;padding:8px 10px;display:grid;gap:6px;font-size:11.5px;color:#a4b1bf}.strip .row{align-items:center;gap:5px}.strip .k{color:#7a8a9b;margin:0 2px 0 8px;text-transform:uppercase;font-size:10.5px;letter-spacing:.05em}.strip .st{color:#f2c14e;font-variant-numeric:tabular-nums}.live{font-size:11px}'+'.tag{display:inline-block;font-size:9.5px;letter-spacing:.03em;border-radius:3px;padding:0 4px;margin-right:5px;color:#05070b;font-weight:600}.t-exact{background:#3fbf80}.t-lean{background:#f2c14e}.t-num{background:#8fd9ff}.t-paper{background:#c9b3ff}.t-hyp{background:transparent;color:#ffb347;border:1px solid #ffb347}.t-drive{background:#7a8a9b}.t-v4{background:#ff9f80}.t-model{background:#e8553f;color:#fff}.t-cited{background:#b8a0ff}.rules{font-size:10.8px;line-height:1.45;color:#a4b1bf;display:grid;gap:3px;border-left:2px solid #f2c14e;padding-left:7px}details summary{cursor:pointer;color:#dfe7ef;font-size:12px}';
const st=document.createElement('style');st.textContent=CSS;document.head.append(st);
const NM=['C'].concat(GEOM.NAMES.map(n=>'N'+n));
document.body.insertAdjacentHTML('beforeend','<canvas id="stage"></canvas><div class="panel"><div><h1>Seven Balls, One Container</h1><div class="by">v4 \u00b7 the vacuum between \u00b7 real balls pushing into each other \u00b7 his light \u00b7 Jeromie Beasley \u00b7 3D model \u00b7 AI-assisted</div></div>'
+'<div class="eq">seven equal balls, radius r\nside ball on axis a: z\u2090(t) from his drive (3, 5, 7)\ncentre d\u2090 = r(1 + tanh(ln z\u2090 / 4))\n\u0393 = tanh(ln z/2),  normal return \u0393\u00b2, pass 1 \u2212 \u0393\u00b2\nevery wall: his oblique split, Snell, total return past sin \u03b8c = Y\u2082/Y\u2081\ngap: tunnelGap across width w\nz = 3 + 2\u221a2:  \u0393\u00b2 = \u00bd,  d = \u221a2 r,  walls cross at 90\u00b0</div>'
+'<p class="what">Every dent is the other ball\u2019s own sphere, between C and the side balls and now between side balls too. Light (<b style="color:#ffd27a">gold</b>) is his fan of rays. At each wall it splits by his rule; past the critical angle it returns whole, and that is what keeps it in the balls (<b style="color:#ff8fb0">rose</b> = a total return). Where two balls stand close, part of a total return tunnels across the gap (<b style="color:#b8a0ff">violet</b> = free light).</p>'
+'<details class="rules"><summary>Every rule and its source ('+RULES.length+')</summary>'+RULES.map(x=>'<div><span class="tag t-'+x[0]+'">'+TAGN[x[0]]+'</span>'+x[1]+'</div>').join('')+'</details>'
+'<div class="ctl"><label>z on the x axis (his z\u0304_I) <output id="ozx"></output><input id="szx" type="range" min="1.2" max="13" step="0.01"></label>'
+'<label>z on the y axis (z\u0304_J) <output id="ozy"></output><input id="szy" type="range" min="1.2" max="13" step="0.01"></label>'
+'<label>z on the z axis (z\u0304_K) <output id="ozz"></output><input id="szz" type="range" min="1.2" max="13" step="0.01"></label>'
+'<div class="row"><button id="b357">his 3, 5, 7</button><button id="bwall">all on the wall 3 + 2\u221a2</button></div>'
+'<label>Breathing amplitude A (in ln z, his drive) <output id="oa"></output><input id="sa" type="range" min="0" max="1" step="0.01"></label>'
+'<label>Speed (field time per second) <output id="os"></output><input id="ss" type="range" min="0.1" max="4" step="0.1"></label>'
+'<label>\u03c9 (his) <output id="ow"></output><input id="sw" type="range" min="0.5" max="8" step="0.1"></label>'
+'<label>z_gap: gap one step below (MODEL) <output id="og"></output><input id="sg" type="range" min="1.5" max="20" step="0.01"></label>'
+'<label>hypothesis B182: \u03ba (loss) <output id="ok1"></output><input id="sk1" type="range" min="0.1" max="3" step="0.05"></label>'
+'<label>hypothesis B182: a (held) <output id="ok2"></output><input id="sk2" type="range" min="0" max="3" step="0.05"></label>'
+'<label>hypothesis B182: b (given back) <output id="ok3"></output><input id="sk3" type="range" min="0" max="2" step="0.01"></label></div>'
+'<div class="tg"><label>dents between side balls <select id="sord"><option value="xyz">x into y, z; y into z</option><option value="zyx">z into y, x; y into x</option></select></label>'
+'<label>window into the gap <select id="swin"><option value="closed">closed: free only by tunnelGap</option><option value="open">open: his split too</option></select></label>'
+'<label>see the dents a ball makes <select id="sgh"><option value="0">none</option>'+GEOM.NAMES.map((n,i)=>'<option value="'+(i+1)+'">N'+n+' (hide its outside, see the dents it makes)</option>').join('')+'</select></label><label>clocks <select id="sclk"><option value="equal">equal</option><option value="z">rate 1/z (HYPOTHESIS)</option></select></label></div>'
+'<div class="ctl"><label>Container margin (in r) <output id="om"></output><input id="sm" type="range" min="0.1" max="2" step="0.05"></label>'
+'<label>Side balls, outside part <output id="oo"></output><input id="so" type="range" min="0" max="1" step="0.05"></label>'
+'<label>C opacity / brightness <output id="oc"></output><input id="sc" type="range" min="0.15" max="1" step="0.05"></label></div>'
+'<div class="tg">'+GEOM.NAMES.map((n,i)=>'<label><input type="checkbox" id="v'+i+'" checked><span style="color:'+COL[i+1]+'">N'+n+'</span></label>').join('')+'</div>'
+'<div class="tg"><label><input type="checkbox" id="tcut">cutaway (z &gt; 0 removed)</label><label><input type="checkbox" id="tmed">medium dots</label><label><input type="checkbox" id="tlab" checked>labels</label></div>'
+'<div class="ctl"><label>Breath speed \u00d7k (MODEL; 1 = his drive) <output id="obk"></output><input id="sbk" type="range" min="0" max="2.6" step="0.01"></label></div>'
+'<div class="rd" id="rd"></div><div class="rd" id="rd2"></div><div class="rd" id="rd3"></div>'
+'<details class="rules" id="pumpbox"><summary>The vacuum test: pump one gap at twice its own light</summary><div class="what" style="font-size:11px">One gap of his faces (z_gap as set), its width swinging by \u03b5 at 2\u03c9\u2081. Gold: with the leak through his faces. Grey: no leak. Light made from the vacuum, photons in the mode, against time in periods of the mode.</div>'
+'<div class="ctl"><label>pump depth \u03b5 (swing of the gap width) <output id="ope"></output><input id="spe" type="range" min="0.02" max="0.6" step="0.01"></label></div><canvas id="pumpcv" width="320" height="140" style="width:100%;background:#070a10;border:1px solid #1f2a38;border-radius:4px"></canvas><div class="rd" id="pumprd"></div></details>'
+'<div class="slot">Medium slot = inside the container, outside all balls (moves with the breathing). Free light lives only there. Read it with <b>medium.light</b>. Code hook: <b>window.medium</b> (insideContainer, insideAnyBall, isMedium, register). Empty now.</div>'
+'<div class="ck live" id="live"></div>'
+'<div class="ck" id="ck"></div><div class="row"><button id="bck">Run full checks (pauses)</button><button id="bcl">Clean view</button></div>'
+'<div class="by">Drag to turn, scroll to zoom. Not modelled: Pauli exclusion, peeling of shells, light changing the balls\u2019 motion.</div></div><button class="ce" id="bk">show panel</button>'
+'<div class="strip"><div class="row"><span class="st" id="tau">t 0.00</span><button id="bplay" aria-pressed="true">Play</button><button id="bstep">Step</button><button id="bbr" aria-pressed="true">breathe</button><button id="brs">Restart</button>'
+'<span class="k">light from</span>'+NM.map((n,i)=>'<button data-kick="'+i+'" style="color:'+COL[i]+'">'+n+'</button>').join('')
+'<span class="k">look</span><button data-look="glass">Old balls (glass)</button><button data-look="solid">Solid</button></div>'
+'<div class="row"><span class="k">show</span>'+[['vac','Vacuum gaps'],['pull','Pull'],['made','Light made'],['light','Light in the balls'],['free','Free (gap)'],['hits','Total returns'],['rims','Rims meeting'],['occ','Occupation C'],['push','Push'],['record','Record'],['clocks','Clocks'],['names','Names'],['circles','Great circles']].map(x=>'<button data-show="'+x[0]+'">'+x[1]+'</button>').join('')+'</div>'
+'<div class="row st" id="books"></div></div>');
const $=i=>document.getElementById(i),cv=$('stage');
const R=new T.WebGLRenderer({canvas:cv,antialias:true,preserveDrawingBuffer:true});R.setPixelRatio(Math.min(2,window.devicePixelRatio||1));
const scene=new T.Scene();scene.background=new T.Color(0x05070b);const cam=new T.PerspectiveCamera(40,1,.05,200);scene.add(world);medium.scene=scene;
medium.plugins.forEach(pl=>pl.init&&pl.init(scene,medium));
const Vw={yaw:.62,pitch:.42,dist:11,panel:true};
function size(){const w=innerWidth,h=innerHeight;R.setSize(w,h,false);cam.aspect=w/h;cam.updateProjectionMatrix();if(Vw.panel&&w>=640)cam.setViewOffset(w,h,-Math.min(180,w*.14),0,w,h);else cam.clearViewOffset();}addEventListener('resize',size);
let drag=null;cv.addEventListener('pointerdown',e=>{cv.setPointerCapture(e.pointerId);drag={x:e.clientX,y:e.clientY};});cv.addEventListener('pointermove',e=>{if(!drag)return;Vw.yaw-=(e.clientX-drag.x)*.006;Vw.pitch=cl(Vw.pitch+(e.clientY-drag.y)*.006,-1.45,1.45);drag={x:e.clientX,y:e.clientY};});['pointerup','pointercancel'].forEach(t=>cv.addEventListener(t,()=>drag=null));cv.addEventListener('wheel',e=>{e.preventDefault();Vw.dist=cl(Vw.dist*Math.exp(e.deltaY*.001),1.5,40);},{passive:false});
const TGT=new T.Vector3();
function setCam(){cam.position.set(TGT.x+Vw.dist*Math.cos(Vw.pitch)*Math.sin(Vw.yaw),TGT.y+Vw.dist*Math.sin(Vw.pitch),TGT.z+Vw.dist*Math.cos(Vw.pitch)*Math.cos(Vw.yaw));cam.lookAt(TGT);cam.updateMatrixWorld();uShared.uCam.value.copy(cam.position);}
function bind(id,out,get,setv,fmt,after){const s=$(id);s.value=get();$(out).textContent=fmt(get());s.addEventListener('input',()=>{setv(+s.value);$(out).textContent=fmt(get());(after||rebuild)();});}
const relight=()=>{buildLight(P.source);rebuild();};
bind('szx','ozx',()=>P.z[0],v=>P.z[0]=v,v=>v.toFixed(2));bind('szy','ozy',()=>P.z[1],v=>P.z[1]=v,v=>v.toFixed(2));bind('szz','ozz',()=>P.z[2],v=>P.z[2]=v,v=>v.toFixed(2));
bind('sa','oa',()=>P.A,v=>P.A=v,v=>v.toFixed(2));bind('ss','os',()=>P.speed,v=>P.speed=v,v=>v.toFixed(1),()=>{});
bind('sw','ow',()=>P.omega,v=>P.omega=v,v=>v.toFixed(1),()=>{LW.o.omega=P.omega;});bind('sg','og',()=>P.zgap,v=>P.zgap=v,v=>v.toFixed(2),()=>{LW.o.zgap=P.zgap;drawPump();});
bind('sk1','ok1',()=>P.kappa,v=>P.kappa=v,v=>v.toFixed(2),()=>{LW.o.kappa=P.kappa;});bind('sk2','ok2',()=>P.ha,v=>P.ha=v,v=>v.toFixed(2),()=>{LW.o.ha=P.ha;});bind('sk3','ok3',()=>P.hb,v=>P.hb=v,v=>v.toFixed(2),()=>{LW.o.hb=P.hb;});
(function(){const s=$('sbk'),o=$('obk');s.value=Math.log10(P.breathK);o.textContent='\u00d7'+P.breathK.toFixed(P.breathK<10?2:0);s.addEventListener('input',()=>{P.breathK=Math.pow(10,+s.value);o.textContent='\u00d7'+P.breathK.toFixed(P.breathK<10?2:0);});})();
bind('spe','ope',()=>P.pumpEps,v=>P.pumpEps=v,v=>v.toFixed(2),()=>drawPump());
bind('sm','om',()=>P.margin,v=>P.margin=v,v=>v.toFixed(2));bind('so','oo',()=>P.outOp,v=>P.outOp=v,v=>v.toFixed(2));bind('sc','oc',()=>P.copC,v=>P.copC=v,v=>v.toFixed(2));
function syncZ(){[['szx','ozx',0],['szy','ozy',1],['szz','ozz',2]].forEach(m=>{$(m[0]).value=P.z[m[2]];$(m[1]).textContent=P.z[m[2]].toFixed(2);});$('sa').value=P.A;$('oa').textContent=P.A.toFixed(2);}
$('b357').onclick=()=>{P.z=[3,5,7];P.A=0.35;P.breathe=true;syncZ();rebuild();strip();};
$('bwall').onclick=()=>{P.z=[ZW,ZW,ZW];P.A=0;syncZ();rebuild();strip();};
$('sord').value=P.order;$('sord').addEventListener('change',e=>{P.order=e.target.value;rebuild();});
$('swin').value=P.window;$('swin').addEventListener('change',e=>{P.window=e.target.value;relight();});
$('sgh').value=P.ghost;$('sgh').addEventListener('change',e=>{P.ghost=+e.target.value;rebuild();});
$('sclk').value=P.clocks;$('sclk').addEventListener('change',e=>{P.clocks=e.target.value;});
for(let i=0;i<6;i++)$('v'+i).addEventListener('change',e=>{P.vis[i]=e.target.checked?1:0;rebuild();});
$('tcut').addEventListener('change',e=>{P.cut=e.target.checked;rebuild();});$('tmed').addEventListener('change',e=>{P.med=e.target.checked;rebuild();});$('tlab').addEventListener('change',e=>{P.lab=e.target.checked;rebuild();});
$('bcl').onclick=()=>{document.body.classList.add('clean');Vw.panel=false;size();};$('bk').onclick=()=>{document.body.classList.remove('clean');Vw.panel=true;size();};
$('bplay').onclick=()=>{CLOCK.playing=!CLOCK.playing;strip();if(!CLOCK.playing)scheduleCheck();};
$('bstep').onclick=()=>{CLOCK.playing=false;stepLight(Math.round(0.1/DT));readLight();apply();strip();scheduleCheck();};
$('bbr').onclick=()=>{P.breathe=!P.breathe;rebuild();strip();};
$('brs').onclick=()=>{CLOCK.t=0;buildLight(P.source);rebuild();};
document.querySelectorAll('[data-kick]').forEach(b=>b.onclick=()=>{buildLight(+b.dataset.kick);apply();});
document.querySelectorAll('[data-look]').forEach(b=>b.onclick=()=>{P.look=b.dataset.look;if(P.look==='solid'&&P.outOp===1)P.outOp=0.35;if(P.look==='glass')P.outOp=1;$('so').value=P.outOp;$('oo').textContent=P.outOp.toFixed(2);rebuild();strip();});
document.querySelectorAll('[data-show]').forEach(b=>b.onclick=()=>{P.show[b.dataset.show]=!P.show[b.dataset.show];apply();strip();});
function strip(){$('bplay').textContent=CLOCK.playing?'Pause':'Play';$('bplay').setAttribute('aria-pressed',CLOCK.playing);$('bbr').setAttribute('aria-pressed',P.breathe);
  document.querySelectorAll('[data-look]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.look===P.look));document.querySelectorAll('[data-show]').forEach(b=>b.setAttribute('aria-pressed',!!P.show[b.dataset.show]));}
const deg=x=>(x*180/PI).toFixed(1)+'\u00b0';
function readout(){const B=S.balls,E=BK?Math.max(1,BK.emitted):1;
  let h='<table><tr><th>ball</th><th>z</th><th>\u0393</th><th>R=\u0393\u00b2</th><th>\u03b8c</th><th>d</th><th>C</th><th>light</th><th>push</th><th>K</th></tr>';
  h+='<tr><td style="color:'+COL[0]+'">C</td><td>1</td><td>0</td><td>0</td><td>\u2014</td><td>0</td><td>\u2014</td><td>'+(BK?(BK.byBall[0]/E).toFixed(3):'')+'</td><td>'+(LW?LW.pushRate[0].toFixed(2):'')+'</td><td>'+(LW?LW.K[0].toFixed(1):'')+'</td></tr>';
  for(let i=1;i<7;i++){const b=B[i];h+='<tr><td style="color:'+COL[i]+'">N'+GEOM.NAMES[i-1]+'</td><td>'+b.z.toFixed(2)+'</td><td>'+b.G.toFixed(3)+'</td><td>'+(b.G*b.G).toFixed(3)+'</td><td>'+deg(Math.asin(1/b.z))+'</td><td>'+b.d.toFixed(3)+'</td><td style="color:#ffb347">'+(1/(b.z+1)).toFixed(3)+'</td><td>'+(BK?(BK.byBall[i]/E).toFixed(3):'')+'</td><td>'+(LW?LW.pushRate[i].toFixed(2):'')+'</td><td>'+(LW?LW.K[i].toFixed(1):'')+'</td></tr>';}
  h+='</table>';
  const PR=GEOM.pairs(S);let h2='<table><tr><th>overlap</th><th>wall is</th><th>depth</th><th>normals meet</th></tr>';
  for(const q of PR){h2+='<tr><td>'+B[q.i].name+' \u00b7 '+B[q.j].name+'</td><td style="color:'+COL[q.owner]+'">'+B[q.owner].name+'</td><td>'+q.depth.toFixed(3)+'</td><td>'+deg(Math.acos(Math.max(-1,Math.min(1,q.cosCross))))+'</td></tr>';}
  h2+='</table>';
  if(LW){h2+='<div><span>hypothesis B182 free x / held y (per ball)</span><b>'+LW.stocks.map(s=>s[0].toFixed(2)+'/'+s[1].toFixed(2)).join(' ')+'</b></div>';
    h2+='<div><span>B182 mean residence (1 + a/b)/\u03ba;  b = 0 keeps a/(\u03ba + a)</span><b>'+(P.hb>0?((1+P.ha/P.hb)/P.kappa).toFixed(3):'\u2014')+';  '+(P.ha/(P.kappa+P.ha)).toFixed(3)+'</b></div>';}
  $('rd').innerHTML=h;$('rd2').innerHTML=h2;
  if(VW){const KN=['x\u2013y','y\u2013z','x\u2013z'],e3=x=>Number.isFinite(x)?(x===0?'0':x.toExponential(2)):'\u2014';
    let h3='<table><tr><th>gaps (4 each)</th><th>s</th><th>pull</th><th>\u03c9\u2081</th><th>\u03ba/\u03c9\u2081</th><th>|\u1e61| (c)</th><th>n\u2081</th><th>n\u2082</th><th>n\u2083</th></tr>';
    VW.g.forEach((G,q)=>{const sd=Math.abs(sDot(G.i,G.j,CLOCK.t));h3+='<tr><td>'+KN[q]+'</td><td>'+(G.open?G.s.toFixed(4):'<span style="color:#7a8a9b">shut</span>')+'</td><td>'+(G.open?e3(G.F):'\u2014')+'</td><td>'+(G.open?(Math.PI/G.s).toFixed(1):'\u2014')+'</td><td>'+(G.open?(VAC.leak(G.s,P.zgap)*G.s/Math.PI).toFixed(3):'\u2014')+'</td><td>'+sd.toFixed(4)+'</td>'+G.modes.map(M=>'<td>'+(G.open?e3(M.n):'\u2014')+'</td>').join('')+'</tr>';});
    h3+='</table><div><span>\u03b7 at z_gap = '+P.zgap.toFixed(3)+' (share of the perfect-mirror pull)</span><b>'+VAC.eta(P.zgap).toFixed(4)+'</b></div>';
    h3+='<div><span>vacuum books, all 12 gaps (\u0127c/r): breathing work = in gaps + leaked + held at shutting</span><b>'+e3(4*VW.workTot)+' = '+e3(4*VW.madeTot)+' + '+e3(4*VW.leakTot)+' + '+e3(4*VW.closedTot)+'</b></div>';
    $('rd3').innerHTML=h3;}
  $('tau').textContent='t '+CLOCK.t.toFixed(2);
  if(BK){const f=BK.frac;$('books').innerHTML=(VW?'<span style="color:#d8ccff">vacuum: '+VW.g.filter(G=>G.open).length+' of 3 gap kinds open \u00b7 light in the gaps '+(4*VW.madeTot).toExponential(2)+' \u0127c/r, paid by the breathing</span>  \u00b7  ':'')+'light (share of '+BK.emitted+' fans): <span style="color:#ffd27a">in balls '+f.inBalls.toFixed(4)+'</span> + <span style="color:#b8a0ff">free '+f.free.toFixed(4)+'</span> + out '+f.out.toFixed(4)+' + cut '+f.cut.toFixed(4)+' = '+f.total.toFixed(12)+'  \u00b7  into the gap so far: tunnelGap '+(BK.freeIn.tunnel/E).toFixed(4)+', window '+(BK.freeIn.window/E).toFixed(4)+'  \u00b7  total returns '+BK.nTotal+'  \u00b7  packets '+BK.n;}}

/* ---------- checks ---------- */
const fmt=v=>typeof v==='number'?(Number.isInteger(v)?String(v):(Math.abs(v)<1e-3&&v!==0?v.toExponential(2):v.toFixed(5))):String(v);
let ckT=0;function scheduleCheck(){clearTimeout(ckT);ckT=setTimeout(runChecks,350);}
function gpuCheck(W,H,hideOut){
  W=W||480;H=H||300;setCam();const outVis=BALL.map(b=>b.out.visible);if(hideOut)for(let i=1;i<7;i++)BALL[i].out.visible=false;if(P.ghost)BALL[P.ghost].out.visible=false;
  const rt=new T.WebGLRenderTarget(W,H,{type:T.FloatType,format:T.RGBAFormat,minFilter:T.NearestFilter,magFilter:T.NearestFilter,depthBuffer:true});
  const vis=[LAB.visible,CONT.visible,MED.visible,FIELD.visible];LAB.visible=CONT.visible=MED.visible=FIELD.visible=false;
  const mats=ALLMATS(),ops=mats.map(m=>[m.transparent,m.depthWrite,m.blending]);mats.forEach(m=>{m.transparent=false;m.depthWrite=true;m.blending=T.NormalBlending;m.needsUpdate=true;});
  const bg=scene.background;scene.background=null;const cc=new T.Color();R.getClearColor(cc);const ca=R.getClearAlpha();
  const saveOff=cam.view?Object.assign({},cam.view):null;const pw=R.domElement.width,ph=R.domElement.height;
  if(saveOff&&saveOff.enabled){cam.setViewOffset(pw,ph,saveOff.offsetX*pw/saveOff.fullWidth,0,pw,ph);}
  uShared.uMode.value=1;R.setRenderTarget(rt);R.setClearColor(0x000000,0);R.clear();R.render(scene,cam);
  const buf=new Float32Array(W*H*4);R.readRenderTargetPixels(rt,0,0,W,H,buf);
  R.setRenderTarget(null);uShared.uMode.value=0;R.setClearColor(cc,ca);scene.background=bg;LAB.visible=vis[0];CONT.visible=vis[1];MED.visible=vis[2];FIELD.visible=vis[3];
  mats.forEach((m,i)=>{m.transparent=ops[i][0];m.depthWrite=ops[i][1];m.blending=ops[i][2];m.needsUpdate=true;});rt.dispose();BALL.forEach((b,i)=>b.out.visible=outVis[i]);
  if(saveOff&&saveOff.enabled)size();
  const anaId=new Int16Array(W*H),gpuId=new Int16Array(W*H),cutPx=new Uint8Array(W*H);const ro=cam.position.clone(),v=new T.Vector3();
  const showOut=P.outOp>0&&!hideOut;let maxSph=0,maxDentIn=-Infinity,minOut=Infinity,nC=0,nD=0,nDS=0,nO=0;
  for(let j=0;j<H;j++)for(let i=0;i<W;i++){const k=j*W+i;
    v.set((i+.5)/W*2-1,(j+.5)/H*2-1,.5).unproject(cam).sub(ro).normalize();
    let best=Infinity,bid=-1,nearCut=false;
    for(const b of S.balls){if(!b.visible)continue;const oc=[ro.x-b.c[0],ro.y-b.c[1],ro.z-b.c[2]];const Bq=oc[0]*v.x+oc[1]*v.y+oc[2]*v.z,Cq=oc[0]*oc[0]+oc[1]*oc[1]+oc[2]*oc[2]-b.r*b.r,D=Bq*Bq-Cq;if(D<0)continue;const sq=Math.sqrt(D);
      for(const t of [-Bq-sq,-Bq+sq]){if(t<=0||t>=best)continue;const p=[ro.x+t*v.x,ro.y+t*v.y,ro.z+t*v.z];if(P.cut&&Math.abs(p[2])<2e-3)nearCut=true;if(P.cut&&p[2]>0)continue;
        const cls=GEOM.classify(S,b.id,p);if(cls===-1)continue;if(b.id>0&&cls===0&&(!showOut||b.id===P.ghost))continue;best=t;bid=cls===1?b.id+10:b.id;}}
    anaId[k]=bid;cutPx[k]=nearCut?1:0;
    const a=buf[k*4+3];let g=-1;if(a>0.75){const id=Math.floor(a+1e-3)-1,dent=(a-id-1)>0.25;g=dent?id+10:id;const p=[buf[k*4],buf[k*4+1],buf[k*4+2]],b=S.balls[id];
      maxSph=Math.max(maxSph,Math.abs(GEOM.dist(p,b.c)-r));if(id===0)nC++;
      for(const o of S.balls){if(o===b||!o.visible)continue;if(o.rank>b.rank)minOut=Math.min(minOut,GEOM.dist(p,o.c)-r);}
      if(dent){nD++;let m=Infinity,side=false;for(const o of S.balls){if(o!==b&&o.visible&&o.rank<b.rank){const dd=GEOM.dist(p,o.c)-r;if(dd<m)m=dd;if(o.id>0&&dd<0)side=true;}}maxDentIn=Math.max(maxDentIn,m);if(side)nDS++;}else if(id>0)nO++;}
    gpuId[k]=g;}
  let mis=0,misOff=0,misCut=0;const E=2;
  for(let j=0;j<H;j++)for(let i=0;i<W;i++){const k=j*W+i;if(anaId[k]===gpuId[k])continue;mis++;let edge=false;
    if(cutPx[k]){misCut++;continue;}
    for(let dj=-E;dj<=E&&!edge;dj++)for(let di=-E;di<=E;di++){const ii=i+di,jj=j+dj;if(ii<0||jj<0||ii>=W||jj>=H)continue;if(anaId[jj*W+ii]!==anaId[k]){edge=true;break;}}
    if(!edge)misOff++;}
  return {W,H,nC,nD,nDS,nO,maxSph,maxDentIn:maxDentIn===-Infinity?0:maxDentIn,minOut:minOut===Infinity?0:minOut,mis,misOff,misCut};
}
/* light unit checks: his split at a real wall of this page, and the gap rule */
function lightChecks(){const rows=[],Wt=LIGHT.makeWorld(lightOpts());
  const Sx=GEOM.state({z:P.z,A:0,breathe:false},0,P.margin,[1,1,1,1,1,1],P.order);LIGHT.setGeom(Wt,Sx);
  /* a packet in C, straight at the dent wall of N+x (the near point of N+x's sphere, normal incidence) */
  const b=Sx.balls[1],pN=[b.d-r,0,0];let kids=LIGHT.split(Wt,{p:[0,0,0],u:[1,0,0],f:1,w:[0],kind:'in',gen:0},pN,1);
  const ret=kids.filter(k=>k.u[0]<0).reduce((s,k)=>s+k.f,0),pass=kids.filter(k=>k.u[0]>0).reduce((s,k)=>s+k.f,0),G=b.G;
  rows.push({name:'His split at the real wall C\u2192N+x (z = '+b.z.toFixed(3)+', normal): |returned \u2212 \u0393\u00b2| + |passed \u2212 (1 \u2212 \u0393\u00b2)|',val:Math.abs(ret-G*G)+Math.abs(pass-(1-G*G)),pass:Math.abs(ret-G*G)+Math.abs(pass-(1-G*G))<1e-12});
  /* past the critical angle sin = 1/z the same wall returns everything */
  let worstT=0,worstP=Infinity;for(const s of [1.0001,1.05,1.5,3]){const sn=Math.min(0.9999,s/b.z),u=[Math.sqrt(1-sn*sn),sn,0];
    const kk=LIGHT.split(Wt,{p:[0,0,0],u,f:1,w:[0],kind:'in',gen:0},pN,1),rr=kk.filter(k=>k.w.join()==='0').reduce((q,k)=>q+k.f,0);worstT=Math.max(worstT,Math.abs(rr-1));}
  for(const s of [0.3,0.7,0.98]){const sn=s/b.z,u=[Math.sqrt(1-sn*sn),sn,0];const kk=LIGHT.split(Wt,{p:[0,0,0],u,f:1,w:[0],kind:'in',gen:0},pN,1),tt=kk.filter(k=>k.w.join()!=='0').reduce((q,k)=>q+k.f,0);worstP=Math.min(worstP,tt);}
  rows.push({name:'Past \u03b8c = arcsin(1/z) = '+deg(Math.asin(1/b.z))+' the wall returns all: max |returned \u2212 1| (4 angles)',val:worstT,pass:worstT<1e-12});
  rows.push({name:'Below \u03b8c light passes: min passed share (3 angles, must be > 0)',val:worstP,pass:worstP>0});
  /* tunnelGap: R + T = 1 at the gap faces of this page */
  let e7=0;for(let q=0;q<200;q++){const a1=Math.pow(10,-2+2*Math.random()),a2=a1/Math.pow(P.zgap,2),s1=Math.sqrt(a2/a1)+(1-Math.sqrt(a2/a1))*Math.random(),Cc=a1*s1*s1,ke=P.omega*Math.sqrt(Cc-a2),kp=P.omega*Math.sqrt((Cc-a2)/a2),tg=L.tunnelGap(P.omega*Math.sqrt(a1-Cc),ke,kp,Math.random()*0.5);e7=Math.max(e7,Math.abs(tg.R+tg.T-1));}
  rows.push({name:'tunnelGap at the gap faces: max | R + T \u2212 1 | (200 random)',val:e7,pass:e7<1e-12});
  /* electron occupation algebra */
  let e17=0;for(const bb of Sx.balls.slice(1)){const C=1/(bb.z+1);e17=Math.max(e17,Math.abs(1-2*C-bb.G),Math.abs(4*C*(1-C)-(1-bb.G*bb.G)));}
  rows.push({name:'Occupation C = 1/(z+1): 1 \u2212 2C = \u0393 and 4C(1 \u2212 C) = T on all six (algebra only)',val:e17,pass:e17<1e-14});
  /* the wall */
  const Sw=GEOM.state({z:[ZW,ZW,ZW],A:0,breathe:false},0,P.margin,[1,1,1,1,1,1],P.order),pw=GEOM.pairs(Sw).filter(q=>!q.side);
  const ew=Math.max(...Sw.balls.slice(1).map(x=>Math.abs(x.d-Math.SQRT2*r)),...pw.map(q=>Math.abs(q.cosCross)),...Sw.balls.slice(1).map(x=>Math.abs(x.G*x.G-0.5)));
  rows.push({name:'At z = 3 + 2\u221a2: d = \u221a2 r, C and side spheres meet at 90\u00b0, \u0393\u00b2 = \u00bd: max error',val:ew,pass:ew<1e-14});
  /* the live books */
  const bk=LIGHT.books(LW);rows.push({name:'Light books: | in balls + free + out + cut \u2212 emitted | / emitted (must be < 1e-12)',val:Math.abs(bk.total-bk.emitted)/Math.max(1,bk.emitted),pass:Math.abs(bk.total-bk.emitted)/Math.max(1,bk.emitted)<1e-12});
  if(P.window==='closed')rows.push({name:'Window closed: light put into the gap other than by tunnelGap (must be 0)',val:bk.freeIn.window,pass:bk.freeIn.window===0&&bk.out<=bk.freeIn.tunnel+1e-12});
  else rows.push({name:'Window open: light into the gap by tunnelGap / by his split in the window',val:(bk.freeIn.tunnel/Math.max(1,bk.emitted)).toFixed(4)+' / '+(bk.freeIn.window/Math.max(1,bk.emitted)).toFixed(4),pass:true});
  return rows;}
function vacChecks(){const rows=[];
  for(const [z,ref] of [[3,0.261245],[ZW,0.456192],[7,0.504067]]){const e=VAC.eta(z);rows.push({name:'\u03b7(z = '+z.toFixed(3)+') against the independent high-precision run '+ref,val:e,pass:Math.abs(e-ref)<2e-6});}
  {const Sw=GEOM.state({z:[ZW,ZW,ZW],A:0,breathe:false},0,P.margin,[1,1,1,1,1,1],P.order);let m=0;for(const [i,j] of VAC.NB)m=Math.max(m,Math.abs(VAC.gapOf(Sw,i,j)));rows.push({name:'All on the wall: the twelve neighbour gaps are exactly shut (balls touch): max |s|',val:m,pass:m<1e-14});}
  {let e=0;for(const t of [CLOCK.t,CLOCK.t+0.37,CLOCK.t+4.1]){const St=GEOM.state(geoOpts(),t,P.margin,[1,1,1,1,1,1],P.order);for(const [i,j] of VAC.NB){const k=VAC.KINDS[VAC.kindOf(i,j)];e=Math.max(e,Math.abs(VAC.gapOf(St,i,j)-sFnV(k[0],k[1],t)));}}rows.push({name:'Twelve gaps = three kinds, ball to ball, 3 times: max diff',val:e,pass:e<1e-14});}
  {const s0=0.2,eps=0.05,om0=Math.PI/s0,rr=VAC.pumpRun(s0,eps,ZW,20/om0,5,false),T=rr.T,w=t=>Math.PI/(s0*(1-eps*Math.sin(2*om0*t)));let y=[1/Math.sqrt(2*om0),0,0,-om0/Math.sqrt(2*om0)],t=0;const h=0.004/om0;
    const F=(t,y)=>{const ww=w(t);return [y[2],y[3],-ww*ww*y[0],-ww*ww*y[1]];};
    while(t<T-1e-15){const hh=Math.min(h,T-t),k1=F(t,y),k2=F(t+hh/2,y.map((v,i)=>v+hh/2*k1[i])),k3=F(t+hh/2,y.map((v,i)=>v+hh/2*k2[i])),k4=F(t+hh,y.map((v,i)=>v+hh*k3[i]));y=y.map((v,i)=>v+hh/6*(k1[i]+2*k2[i]+2*k3[i]+k4[i]));t+=hh;}
    const ww=w(T),b2=((ww*y[0]+y[3])**2+(ww*y[1]-y[2])**2)/(2*ww);rows.push({name:'Light made from the vacuum, no leak: moment equations vs the mode function |\u03b2|\u00b2 (rel)',val:Math.abs(rr.n/b2-1),pass:Math.abs(rr.n/b2-1)<1e-3});}
  if(VW){const d=Math.abs(VW.workTot-(VW.madeTot+VW.leakTot+VW.closedTot));rows.push({name:'Vacuum books close: |work \u2212 (in gaps + leaked + held at shutting)|',val:d,pass:d<=1e-9*Math.max(1,Math.abs(VW.workTot))});}
  return rows;}
/* the pump test drawing */
function drawPump(){const cv2=document.getElementById('pumpcv');if(!cv2)return;const c=cv2.getContext('2d'),W=cv2.width,H=cv2.height,s0=0.1,om0=Math.PI/s0,per=2*Math.PI/om0,T=40*per;
  const A=VAC.pumpRun(s0,P.pumpEps,P.zgap,T,320,true),B=VAC.pumpRun(s0,P.pumpEps,P.zgap,T,320,false);
  c.fillStyle='#070a10';c.fillRect(0,0,W,H);const lo=-6,hi=6,Y=n=>H-6-(H-12)*(Math.log10(Math.max(1e-6,n))-lo)/(hi-lo),X=t=>6+(W-12)*t/T;
  c.strokeStyle='#1f2a38';c.lineWidth=1;for(let k=lo;k<=hi;k+=2){c.beginPath();c.moveTo(6,Y(Math.pow(10,k)));c.lineTo(W-6,Y(Math.pow(10,k)));c.stroke();}
  c.fillStyle='#7a8a9b';c.font='10px sans-serif';c.fillText('n = 1',W-40,Y(1)-2);c.fillText('40 periods',W-62,H-2);
  for(const [R,col] of [[B,'#7a8a9b'],[A,'#ffd27a']]){c.strokeStyle=col;c.lineWidth=1.5;c.beginPath();R.out.forEach((p,k)=>{const x=X(p[0]),y=Y(p[1]);k?c.lineTo(x,y):c.moveTo(x,y);});c.stroke();}
  const thr=VAC.leak(1,P.zgap)/Math.PI;
  document.getElementById('pumprd').innerHTML='<div><span>after 40 periods: with his faces / no leak</span><b>'+A.n.toExponential(2)+' / '+B.n.toExponential(2)+'</b></div><div><span>leak per radian \u03ba/\u03c9\u2081 (growth needs \u03b5 above about this)</span><b>'+thr.toFixed(3)+'</b></div>';}
function runChecks(){
  const res=GEOM.checks(S);let g=null,gerr=null,g2=null;
  try{g=gpuCheck();g2=gpuCheck(480,300,true);}catch(e){gerr=String(e);}
  const rows=res.map(x=>({name:x[0],val:x[1],pass:x[2]}));
  for(const [gg,lab] of [[g,'as shown'],[g2,'side balls\u2019 outside parts hidden, so every dent is in view']])if(gg){const g=gg,tol=2e-5;rows.push({name:'\u2014 pixel check, '+lab,val:'',pass:true});
    rows.push({name:'Rendered pixels: max | |p \u2212 c_ball| \u2212 r | ('+(g.nC+g.nD+g.nO)+' px; float32)',val:g.maxSph,pass:g.maxSph<tol});
    rows.push({name:'Rendered pixels: min distance outside every higher-ranked ball (must be \u2265 0)',val:g.minOut,pass:g.minOut>=-tol});
    rows.push({name:'Rendered dent-wall pixels ('+g.nD+' px, '+g.nDS+' in a side ball): on the owner\u2019s sphere, inside the dented ball: max (|p \u2212 c_dented| \u2212 r)',val:g.maxDentIn,pass:g.maxDentIn<=tol});
    rows.push({name:'Rendered pixels vs exact ray-cast of the rule ('+g.W+'\u00d7'+g.H+'): mismatched px',val:g.mis,pass:true});
    rows.push({name:'  of which NOT within 2 px of an edge or of the cut plane (|z| < 2e\u22123: '+g.misCut+' px) (must be 0)',val:g.misOff,pass:g.misOff===0});}
  if(!g)rows.push({name:'GPU pixel check could not run: '+gerr,val:'-',pass:false});
  lightChecks().forEach(x=>rows.push(x));vacChecks().forEach(x=>rows.push(x));
  const all=rows.every(x=>x.pass);
  $('ck').innerHTML='<h2>Full check at t = '+CLOCK.t.toFixed(3)+': '+(all?'<span class="pass">PASS</span>':'<span class="fail">FAIL</span>')+' ('+rows.filter(x=>x.pass).length+'/'+rows.length+')</h2>'+rows.map(x=>'<div><span>'+x.name+'</span><b>'+fmt(x.val)+'</b><span class="'+(x.pass?'pass':'fail')+'">'+(x.pass?'PASS':'FAIL')+'</span></div>').join('');
  window.lastCheck={t:CLOCK.t,ds:S.balls.slice(1).map(b=>b.d),zs:S.balls.slice(1).map(b=>b.z),params:JSON.parse(JSON.stringify(P)),R:S.R,all,rows,gpu:g,gpuDents:g2};return window.lastCheck;}
window.runChecks=runChecks;
let liveT=0;
function liveCheck(){const res=GEOM.checks(S,3000,1500),ok=res.filter(x=>!/sampling/.test(x[0])).every(x=>x[2]),bk=BK?Math.abs(BK.total-BK.emitted)/Math.max(1,BK.emitted):0;
  $('live').innerHTML='Live check at t = '+CLOCK.t.toFixed(2)+' (dent rule pairwise on 3000 pts per ball, contact circles, angles, d from z, container, medium; light books): '+((ok&&bk<1e-12)?'<span class="pass">PASS</span>':'<span class="fail">FAIL</span>')+'  \u00b7  max dent error '+fmt(res[0][1]);}
/* deterministic jump for screenshots and tests: restart the light at t = 0 in ball src and run to time t */
function seek(t,src){CLOCK.playing=false;CLOCK.t=0;buildLight(src==null?P.source:src);stepLight(Math.round(t/DT));readLight();rebuild();strip();setCam();
  return {t:CLOCK.t,books:BK,zs:S.balls.slice(1).map(b=>b.z),ds:S.balls.slice(1).map(b=>b.d)};}
window.seven={P,rebuild,seek,setView:(yaw,pitch,dist,tgt)=>{Vw.yaw=yaw;Vw.pitch=pitch;if(dist)Vw.dist=dist;TGT.set(...(tgt||[0,0,0]));},state:()=>S,light:()=>({t:LW.t,books:BK}),
  play:()=>{CLOCK.playing=true;strip();},pause:()=>{CLOCK.playing=false;strip();},
  set:(o)=>{const sh=o.show;delete o.show;Object.assign(P,o);if(sh)Object.assign(P.show,sh);
    syncZ();[['sm','om','margin',2],['so','oo','outOp',2],['sc','oc','copC',2],['ss','os','speed',1],['sw','ow','omega',1],['sg','og','zgap',2]].forEach(m=>{$(m[0]).value=P[m[2]];$(m[1]).textContent=(+P[m[2]]).toFixed(m[3]);});
    $('sord').value=P.order;$('swin').value=P.window;$('sgh').value=P.ghost;$('sclk').value=P.clocks;for(let i=0;i<6;i++)$('v'+i).checked=!!P.vis[i];$('tcut').checked=P.cut;$('tmed').checked=P.med;$('tlab').checked=P.lab;
    rebuild();strip();}};
$('bck').onclick=()=>{CLOCK.playing=false;strip();runChecks();};
size();setCam();buildLight(0);syncZ();rebuild();strip();drawPump();
let last=performance.now();
(function loop(now){requestAnimationFrame(loop);now=now||performance.now();const dt=Math.max(0,Math.min(0.1,(now-last)/1000));last=now;setCam();
  if(CLOCK.playing){acc+=dt*P.speed;let n=Math.floor(acc/DT);acc-=n*DT;n=Math.min(n,12);if(n>0){stepLight(n);readLight();}}
  apply();
  if(now-liveT>1000){liveT=now;liveCheck();}
  medium.plugins.forEach(pl=>pl.update&&pl.update(CLOCK.t,medium));R.render(scene,cam);})();
})();
