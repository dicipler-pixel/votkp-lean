/* SCRIPT: light_hypersurface_surprise_v1
   Light at the Hypersurface, Surprise v1. Jeromie Beasley. 15 Nov 2026.
   One Poincare ball in the peel (Smith) coordinate. One clock. Every number on the page is computed live from LH (the maths block above).
   Built on 3D Mixer Parts v1 (stage, glow points, lines, labels). */
(function(){
"use strict";
const M=window.Mixer3D,T=M.T,PI=Math.PI,RB=2.6;
const $=id=>document.getElementById(id);
const fmt=(x,n)=>Number.isFinite(x)?x.toFixed(n==null?4:n):'n/a';
const sci=x=>x===0?'0':x.toExponential(1);
const deg=x=>x*180/PI;
const AXN=['I','J','K'],AXV=[[1,0.55,0.49],[0.39,0.83,1],[0.95,0.76,0.31]],AXH=['#ff8d7c','#63d3ff','#f2c14e'];
const HYP=[0.71,0.55,1.0];
/* ball point; world axes as in the Balls mixer: i -> x, k -> up (y), j -> toward the viewer (-z) */
function wp(p,o){const k=RB/(1+p[0]);o[0]=p[1]*k;o[1]=p[3]*k;o[2]=-p[2]*k;return o;}
const w3=(u,s)=>[u[0]*s,u[2]*s,-u[1]*s];
const tmp=[0,0,0],tmp2=[0,0,0];

/* ---------- parameters (the feed) ---------- */
const P={zbar:[3,5,7],amp:0.35,T:[8,13,21],ph:[0,2*PI/3,4*PI/3],sigma:1,Tphi:9,Tchi:55};
const CLOCK={tau:0,anim:0,playing:!window.matchMedia('(prefers-reduced-motion: reduce)').matches,speed:1};
const UI={hyp:true,nRays:36};

/* ---------- dynamic buffers ---------- */
function segBuf(n,opacity,additive){const geo=new T.BufferGeometry(),pos=new Float32Array(n*6),col=new Float32Array(n*6);
  geo.setAttribute('position',new T.BufferAttribute(pos,3));geo.setAttribute('color',new T.BufferAttribute(col,3));
  const mesh=new T.LineSegments(geo,new T.LineBasicMaterial({vertexColors:true,transparent:true,opacity,depthWrite:false,blending:additive?T.AdditiveBlending:T.NormalBlending}));mesh.frustumCulled=false;
  let i=0;return{mesh,reset(){i=0;},add(a,b,ca,cb){if(i>=n)return;const o=i*6;pos[o]=a[0];pos[o+1]=a[1];pos[o+2]=a[2];pos[o+3]=b[0];pos[o+4]=b[1];pos[o+5]=b[2];
    col[o]=ca[0];col[o+1]=ca[1];col[o+2]=ca[2];cb=cb||ca;col[o+3]=cb[0];col[o+4]=cb[1];col[o+5]=cb[2];i++;},
    commit(){geo.setDrawRange(0,i*2);geo.attributes.position.needsUpdate=true;geo.attributes.color.needsUpdate=true;},get count(){return i;}};}
function ptBuf(n,size){const p=M.points(n,size),pos=p.geometry.attributes.position.array,col=p.geometry.attributes.color.array;let i=0;
  return{mesh:p,reset(){i=0;},add(a,c,f){if(i>=n)return;const o=i*3;pos[o]=a[0];pos[o+1]=a[1];pos[o+2]=a[2];col[o]=c[0]*f;col[o+1]=c[1]*f;col[o+2]=c[2]*f;i++;},
    commit(){p.geometry.setDrawRange(0,i);p.geometry.attributes.position.needsUpdate=true;p.geometry.attributes.color.needsUpdate=true;},get count(){return i;}};}

/* ---------- stage and the one object ---------- */
const S3=M.stage($('stage'));S3.setView([0.7,0.32,7.4,0]);
const WORLD=new T.Group();S3.world.add(WORLD);
/* rim */
WORLD.add(M.shell(RB,0x63d3ff,0.03));
for(let k=0;k<3;k++){const p=[];for(let i=0;i<=160;i++){const a=2*PI*i/160,c=RB*Math.cos(a),s=RB*Math.sin(a);p.push(k===0?new T.Vector3(c,0,s):k===1?new T.Vector3(c,s,0):new T.Vector3(0,c,s));}WORLD.add(M.line(p,0x63d3ff,k===0?0.4:0.14));}
/* the six fixed cap rings on the rim: directions at 45 degrees from each arm (cos psi = 1/sqrt 2) */
(function(){const b=segBuf(6*96,0.5,true);for(let k=0;k<6;k++){const u=LH.letterDir(k),a=k>>1,e1=LH.UNIT[(a+1)%3],e2=LH.UNIT[(a+2)%3],c=AXV[a].map(x=>x*0.55);let prev=null;
  for(let i=0;i<=96;i++){const t=2*PI*i/96,d=[0,1,2].map(j=>Math.SQRT1_2*u[j]+Math.SQRT1_2*(Math.cos(t)*e1[j]+Math.sin(t)*e2[j])),q=w3(d,RB);if(prev&&i%2)b.add(prev,q,c);prev=q;}}b.commit();WORLD.add(b.mesh);})();
/* faces: six first-level caps (meshes), deeper faces as rings */
const NT=12,NP=44,faces=[];
for(let k=0;k<6;k++){const geo=new T.BufferGeometry(),pos=new Float32Array((NT+1)*(NP+1)*3),idx=[];for(let i=0;i<NT;i++)for(let j=0;j<NP;j++){const q=i*(NP+1)+j;idx.push(q,q+1,q+NP+1,q+1,q+NP+2,q+NP+1);}
  geo.setAttribute('position',new T.BufferAttribute(pos,3));geo.setIndex(idx);
  const mesh=new T.Mesh(geo,new T.MeshBasicMaterial({color:new T.Color(AXH[k>>1]),transparent:true,opacity:0.1,side:T.DoubleSide,depthWrite:false,blending:T.AdditiveBlending}));mesh.frustumCulled=false;WORLD.add(mesh);faces.push({mesh,pos});}
const faceLines=segBuf(6*64*3+30*48*2+200,0.8,true);WORLD.add(faceLines.mesh);
const crossLines=segBuf(12*96,0.9,true);WORLD.add(crossLines.mesh);
const hypLines=segBuf(12*16+400,0.95,true);WORLD.add(hypLines.mesh);
const treeLines=segBuf(36*8,0.45,true);WORLD.add(treeLines.mesh);
const nodePts=ptBuf(200,0.16);WORLD.add(nodePts.mesh);
const rayLines=segBuf(60000,0.5,true);WORLD.add(rayLines.mesh);
const rayPts=ptBuf(30000,0.07);WORLD.add(rayPts.mesh);
const sparkPts=ptBuf(9000,0.11);WORLD.add(sparkPts.mesh);
const axisPts=ptBuf(1200,0.12);WORLD.add(axisPts.mesh);
const loopLines=segBuf(3*12*4*6+100,0.55,true);WORLD.add(loopLines.mesh);
const loopPts=ptBuf(60,0.2);WORLD.add(loopPts.mesh);
/* rim record (hypothesis layer): ring buffer of landing points */
const NREC=16000,rec=M.points(NREC,0.055),recBase=new Float32Array(NREC*3),recBorn=new Float32Array(NREC).fill(-1e9);let recI=0;WORLD.add(rec.mesh||rec);
const centre=new T.Mesh(new T.SphereGeometry(0.03,20,14),new T.MeshBasicMaterial({color:0xfff2cc}));WORLD.add(centre);
const labels=AXN.map((n,a)=>{const l=M.label(n,AXH[a],0.3);WORLD.add(l);return l;});
const lrim=M.label('rim','#63d3ff',0.26);lrim.position.set(-RB*0.8,0.1,RB*0.8);WORLD.add(lrim);
const lrec=M.label('landing record on the rim (hypothesis)','#b58cff',0.15);lrec.position.set(RB*0.86,-0.1,-RB*0.86);WORLD.add(lrec);

/* a face (geodesic plane with unit normal N) is a sphere in the unit ball: centre n/n0, radius 1/|n0| */
function capFrame(N){let n0=N[0],sg=n0<0?-1:1;const c=[N[1]/n0,N[2]/n0,N[3]/n0],Rr=1/Math.abs(n0),cl=Math.hypot(c[0],c[1],c[2]),a=c.map(x=>-x/cl);
  let e1=Math.abs(a[2])<0.9?[a[1],-a[0],0]:[0,a[2],-a[1]];const l=Math.hypot(e1[0],e1[1],e1[2]);e1=e1.map(x=>x/l);
  const e2=[a[1]*e1[2]-a[2]*e1[1],a[2]*e1[0]-a[0]*e1[2],a[0]*e1[1]-a[1]*e1[0]];return{c,Rr,a,e1,e2,tmax:Math.atan(1/Rr)};}
function capPoint(f,th,ph,o){const ct=Math.cos(th),st=Math.sin(th),cp=Math.cos(ph),sp=Math.sin(ph);
  const x=f.c[0]+f.Rr*(f.a[0]*ct+st*(cp*f.e1[0]+sp*f.e2[0])),y=f.c[1]+f.Rr*(f.a[1]*ct+st*(cp*f.e1[1]+sp*f.e2[1])),z=f.c[2]+f.Rr*(f.a[2]*ct+st*(cp*f.e1[2]+sp*f.e2[2]));
  o[0]=x*RB;o[1]=z*RB;o[2]=-y*RB;return o;}
function ring(buf,f,th,n,c,dash){let prev=[0,0,0],cur=[0,0,0];capPoint(f,th,0,prev);for(let i=1;i<=n;i++){capPoint(f,th,2*PI*i/n,cur);if(!dash||i%2)buf.add(prev,cur,c);prev[0]=cur[0];prev[1]=cur[1];prev[2]=cur[2];}}
function geoLine(buf,p,q,n,c,dash){const d=LH.hdist(p,q);if(d<1e-9)return;const sh=Math.sinh(d);let prev=[0,0,0],cur=[0,0,0];wp(p,prev);
  for(let j=1;j<=n;j++){const t=j/n,a=Math.sinh((1-t)*d)/sh,b=Math.sinh(t*d)/sh;wp([a*p[0]+b*q[0],a*p[1]+b*q[1],a*p[2]+b*q[2],a*p[3]+b*q[3]],cur);if(!dash||j%2)buf.add(prev,cur,c);prev[0]=cur[0];prev[1]=cur[1];prev[2]=cur[2];}}

/* colours of light by the layer the ray is in; a ray returned whole is rose */
const DEPTHC=[[1,0.88,0.62],[0.4,0.85,1],[0.45,1,0.6],[0.9,0.95,0.5],[1,1,1]],ROSE=[1,0.42,0.66],WHITE=[1,1,1];
const segCol=s=>s.kind===3?ROSE:DEPTHC[Math.min(4,s.depth)];

/* ---------- running sums (integrated on the clock) ---------- */
const REC={push:[0,0,0],t0:0};
let S=null,TR=null,STK=null,PAIRS=null,LOOPS=null,TH=null,frameN=0;

function draw(dt){
  S=LH.feed(P,CLOCK.tau);
  TR=LH.trace(S,LH.fanDirs(S,S.chi).concat(LH.sourceDirs(UI.nRays,S.chi)));
  /* faces of the centre cell */
  faceLines.reset();crossLines.reset();hypLines.reset();
  const frames=[];
  for(let k=0;k<6;k++){const a=k>>1,f=capFrame(S.N0[k]),F=faces[k],pos=F.pos;frames.push(f);let o=0;
    for(let i=0;i<=NT;i++){const th=f.tmax*i/NT;for(let j=0;j<=NP;j++){capPoint(f,th,2*PI*j/NP,tmp);pos[o++]=tmp[0];pos[o++]=tmp[1];pos[o++]=tmp[2];}}
    F.mesh.geometry.attributes.position.needsUpdate=true;F.mesh.material.opacity=0.025+0.13*S.R[a];
    ring(faceLines,f,f.tmax,64,AXV[a]);ring(faceLines,f,f.tmax*0.5,48,AXV[a].map(x=>x*0.25));
    /* the window: centre rays inside it cross, outside it they are returned whole (only when admittance falls outward) */
    if(S.sigma>0){const psc=Math.asin(Math.min(1,1/(S.z[a]*Math.cosh(S.h[a])))),sH=Math.atanh(Math.tanh(S.h[a])/Math.cos(psc)),u=LH.letterDir(k),e1=LH.UNIT[(a+1)%3],e2=LH.UNIT[(a+2)%3];let prev=null;
      for(let i=0;i<=48;i++){const t=2*PI*i/48,d=[0,1,2].map(j=>Math.cos(psc)*u[j]+Math.sin(psc)*(Math.cos(t)*e1[j]+Math.sin(t)*e2[j])),q=w3(d,RB*Math.tanh(sH/2));if(prev)faceLines.add(prev,q,WHITE);prev=q;}}
  }
  /* deeper faces: the rings of the 30 faces of the six neighbouring cells */
  for(let k=0;k<6;k++)for(let m=0;m<6;m++){if(m===(k^1))continue;const N=LH.mv(S.gens[k],S.N0[m]),f=capFrame(N);ring(faceLines,f,f.tmax,48,AXV[m>>1].map(x=>x*0.3));}
  faceLines.commit();
  /* pairs of faces of the centre cell: crossing circle (white) or gap (hypothesis layer: common perpendicular) */
  PAIRS=[];
  for(let a=0;a<3;a++)for(let b=a+1;b<3;b++){const pr=LH.pair(S,a,b);PAIRS.push(pr);
    for(let sa=0;sa<2;sa++)for(let sb=0;sb<2;sb++){const ka=2*a+sa,kb=2*b+sb,fa=frames[ka],fb=frames[kb];
      if(pr.over){const A=fa.c,B=fb.c,dv=[B[0]-A[0],B[1]-A[1],B[2]-A[2]],d=Math.hypot(dv[0],dv[1],dv[2]),x=(d*d+fa.Rr*fa.Rr-fb.Rr*fb.Rr)/(2*d),rr=fa.Rr*fa.Rr-x*x;if(rr>0){
        const n=dv.map(v=>v/d),c0=[A[0]+n[0]*x,A[1]+n[1]*x,A[2]+n[2]*x];let e1=Math.abs(n[2])<0.9?[n[1],-n[0],0]:[0,n[2],-n[1]];const l=Math.hypot(e1[0],e1[1],e1[2]);e1=e1.map(v=>v/l);
        const e2=[n[1]*e1[2]-n[2]*e1[1],n[2]*e1[0]-n[0]*e1[2],n[0]*e1[1]-n[1]*e1[0]],r=Math.sqrt(rr);let prev=null,pin=false;
        for(let i=0;i<=96;i++){const t=2*PI*i/96,p=[0,1,2].map(j=>c0[j]+r*(Math.cos(t)*e1[j]+Math.sin(t)*e2[j])),inn=p[0]*p[0]+p[1]*p[1]+p[2]*p[2]<=1,q=[p[0]*RB,p[2]*RB,-p[1]*RB];if(prev&&inn&&pin)crossLines.add(prev,q,[0.9,0.95,1]);prev=q;pin=inn;}}}
      else if(UI.hyp){const ft=LH.gapFeet(S.N0[ka],S.N0[kb]);if(ft)geoLine(hypLines,ft.pa,ft.pb,12,HYP,true);}
    }}
  crossLines.commit();
  /* tree: centre, six neighbours, their neighbours */
  treeLines.reset();nodePts.reset();
  for(let k=0;k<6;k++){const p1=LH.mv(S.gens[k],LH.O4);geoLine(treeLines,LH.O4,p1,6,AXV[k>>1].map(x=>x*0.8));nodePts.add(wp(p1,tmp),AXV[k>>1],1);
    if(!(k&1))labels[k>>1].position.set(tmp[0],tmp[1]+0.26,tmp[2]);
    for(let m=0;m<6;m++){if(m===(k^1))continue;const g2=LH.mm(S.gens[k],S.gens[m]),p2=LH.mv(g2,LH.O4);geoLine(treeLines,p1,p2,4,AXV[m>>1].map(x=>x*0.4));nodePts.add(wp(p2,tmp),AXV[m>>1],0.55);}}
  treeLines.commit();nodePts.commit();
  /* light: every segment of every ray, and the markers that move along it */
  rayLines.reset();rayPts.reset();sparkPts.reset();
  const NFAN=6*3*LH.FANF.length,SP=0.34,off=(CLOCK.anim*0.42)%SP,a3=[0,0,0],b3=[0,0,0];
  for(let i=0;i<TR.segs.length;i++){const s=TR.segs[i],c=segCol(s),f=Math.pow(s.flux,0.55),n=Math.max(2,Math.min(16,Math.ceil(s.s/0.22))),lf=f*(s.ray<NFAN?0.9:0.3),cc=[c[0]*lf,c[1]*lf,c[2]*lf];
    wp(LH.mv(s.g,s.X),a3);for(let j=1;j<=n;j++){wp(LH.mv(s.g,LH.geoX(s.X,s.v,s.s*j/n)),b3);rayLines.add(a3,b3,cc);a3[0]=b3[0];a3[1]=b3[1];a3[2]=b3[2];}
    if(s.flux>0.012){let nm=0;for(let q=off;q<s.s&&nm<16;q+=SP,nm++){wp(LH.mv(s.g,LH.geoX(s.X,s.v,q)),b3);const e=1-(b3[0]*b3[0]+b3[1]*b3[1]+b3[2]*b3[2])/(RB*RB);if(e<0.012)break;rayPts.add(b3,c,f*(s.ray<NFAN?1:0.6)*Math.min(1,5*e));}}}
  for(let i=0;i<TR.events.length;i++){const e=TR.events[i];wp(LH.mv(e.g,e.X),b3);sparkPts.add(b3,e.total?ROSE:AXV[e.axis],Math.min(1,0.12+0.5*e.flux*LH.pushOblique(e.R,e.c1))*Math.min(1,5*(1-(b3[0]*b3[0]+b3[1]*b3[1]+b3[2]*b3[2])/(RB*RB))));}
  rayLines.commit();rayPts.commit();sparkPts.commit();
  /* on each arm: the coherent layer stack, forward and returning streams, brightness = flux carried */
  axisPts.reset();STK=[];
  for(let a=0;a<3;a++){const z=S.z[a],r=S.r[a],Ys=[1,Math.pow(z,-S.sigma),Math.pow(z,-2*S.sigma),Math.pow(z,-3*S.sigma)],st=LH.stack(Ys,S.phi);STK.push(st);
    for(let sgn=0;sgn<2;sgn++){const u=LH.letterDir(2*a+sgn),sp=0.3,o=(CLOCK.anim*0.5)%sp;
      for(let L=0;L<4;L++){const s0=L===0?0:(L-0.5)*r,s1=L===3?s0+1.4:(L+0.5)*r,ff=Math.min(1,st.fwd[L]*Ys[L]),fb=Math.min(1,st.bwd[L]*Ys[L]);
        for(let q=s0+o;q<s1;q+=sp){const rho=Math.tanh(q/2),pt=w3(u,RB*rho);axisPts.add(pt,WHITE,(0.25+0.75*ff)*Math.min(1,5*(1-rho*rho)));}
        if(L<3)for(let q=s1-o;q>s0;q-=sp){const rho=Math.tanh(q/2),pt=w3(u,RB*rho);axisPts.add(pt,[0.45,0.9,1],fb*Math.min(1,5*(1-rho*rho)));}}}}
  axisPts.commit();
  /* the four-step square of each pair of arms, repeated: it turns, locks or runs; and the Thomas turn of two steps */
  loopLines.reset();loopPts.reset();LOOPS=[];TH=[];
  [[0,1],[1,2],[2,0]].forEach((ab,pi)=>{const lp=LH.loop(S,ab[0],ab[1]);LOOPS.push(lp);const th=LH.thomas(LH.UNIT[ab[0]],S.r[ab[0]],LH.UNIT[ab[1]],S.r[ab[1]]);th.formula=LH.thomasFormula(S.G[ab[0]],S.G[ab[1]]);TH.push(th);
    const col=[0.95,0.93,0.8],NREP=10,pts=[];let Wn=LH.I4();
    for(let n=0;n<NREP;n++){for(let j=0;j<4;j++)pts.push(LH.mv(LH.mm(Wn,lp.part[j]),LH.O4));Wn=LH.mm(Wn,lp.W);if(Wn[0][0]>4000)break;}pts.push(LH.mv(Wn,LH.O4));
    for(let j=0;j+1<pts.length;j++)geoLine(loopLines,pts[j],pts[j+1],5,col.map(x=>x*(0.55*Math.pow(0.86,j/4))));
    const ph=(CLOCK.anim*0.9+pi*1.3)%(pts.length-1),j0=Math.floor(ph),t=ph-j0,p=pts[j0],q=pts[j0+1],d=LH.hdist(p,q);
    if(d>1e-9){const sh=Math.sinh(d),a=Math.sinh((1-t)*d)/sh,b=Math.sinh(t*d)/sh;loopPts.add(wp([a*p[0]+b*q[0],a*p[1]+b*q[1],a*p[2]+b*q[2],a*p[3]+b*q[3]],tmp),col,1);}
    /* frame at the corner reached by two steps: carried by the product (bright) and by its pure boost part (dim); they differ by the Thomas turn */
    const corner=LH.mv(th.M,LH.O4);for(let e=1;e<4;e++){const ev=[0,0,0,0];ev[e]=1;const v1=LH.mv(th.M,ev),v2=LH.mv(th.L,ev);
      geoLine(loopLines,corner,LH.geoX(corner,v1,0.7),4,[1,1,1]);geoLine(loopLines,corner,LH.geoX(corner,v2,0.7),4,[0.35,0.35,0.4]);}
  });
  loopLines.commit();loopPts.commit();
  /* integrated on the clock: push record per axis; landing record on the rim */
  if(dt>0){for(let a=0;a<3;a++)REC.push[a]+=TR.push[a]/TR.nRays*dt;}
  const ra=rec.geometry.attributes;
  if(dt>0&&UI.hyp&&(frameN%2===0)){for(let i=0;i<TR.land.length;i++){const L=TR.land[i];if(L.flux<0.02)continue;const d=L.d,n=Math.hypot(d[0],d[1],d[2]),q=w3(d,RB*1.002/n),f=Math.pow(L.flux,0.5);
    ra.position.setXYZ(recI,q[0],q[1],q[2]);recBase[3*recI]=HYP[0]*f;recBase[3*recI+1]=HYP[1]*f;recBase[3*recI+2]=HYP[2]*f;recBorn[recI]=CLOCK.anim;recI=(recI+1)%NREC;}ra.position.needsUpdate=true;}
  const LIFE=9;for(let i=0;i<NREC;i++){const age=(CLOCK.anim-recBorn[i])/LIFE,f=UI.hyp&&age<1?(1-age)*(1-age):0;ra.color.array[3*i]=recBase[3*i]*f;ra.color.array[3*i+1]=recBase[3*i+1]*f;ra.color.array[3*i+2]=recBase[3*i+2]*f;}
  ra.color.needsUpdate=true;lrec.visible=UI.hyp;
  hypLines.commit();frameN++;
}

/* ---------- readouts ---------- */
const chip=(t,k)=>`<span class="chip ${k||''}">${t}</span>`;
function row(name,val,chips){return `<div class="law"><div class="ln"><span>${name}</span><b>${val}</b></div><div class="ch">${chips}</div></div>`;}
function readout(){
  const zs=S.z.map((z,a)=>`<i style="color:${AXH[a]}">${AXN[a]}</i> ${fmt(z,3)}`).join('  ');
  let h='';
  h+=row('step ratio z = e<sup>r</sup> on each arm',zs,chip('DRIVE','d')+' r(τ) = ln z̄ + A sin(2πτ/T + φ₀); no law of motion is claimed');
  h+=row('Γ = (z − 1)/(z + 1) = tanh(r/2)',S.G.map(g=>fmt(g,4)).join('  '),chip('LEAN · smith_identity')+chip('LEAN · interface_smith')+' VOTKP/Smith.lean:42, Film.lean:116');
  h+=row('R = Γ²,  T = 1 − Γ² = 1/cosh²(r/2)',S.R.map((R,a)=>fmt(R,3)+' | '+fmt(S.T[a],3)).join('   '),chip('LEAN · round_trip')+chip('READING','r')+' Y₁/Y₂ = z across a face');
  h+=row('flux balance r² + (Y₂/Y₁)t² − 1, largest over '+TR.events.length+' hits',sci(TR.resFlux),chip('LEAN · flux_balance')+chip('LEAN · step_matching')+' EventHorizon/Edition10.lean:59, 47');
  h+=row('a sin²θ before − after each crossing, largest (angles measured from the drawn tangents)',sci(TR.resCons),chip('CARD · B30 theorem')+chip('LEAN · three_body_refraction_is_squared_snell')+' algebra only; '+chip('READING','r')+' a = Y²');
  h+=row('centre ray at angle ψ meets a face at θ:  sin θ − cosh(r/2) sin ψ, largest',sci(TR.resInc),chip('CHECKED · 1e-10','c'));
  if(S.sigma>0)h+=row('critical angle θ<sub>c</sub> = arcsin(1/z)',S.z.map(z=>fmt(deg(Math.asin(1/z)),2)+'°').join('  '),chip('CARD · B39 theorem')+chip('LEAN · total_reflection')+chip('LEAN · turning_point')+' Edition10.lean:86, 102');
  else h+=row('critical angle (outward)','none: admittance rises outward',chip('LEAN · turning_point'));
  h+=row('hits returned whole (|Γ| = 1) this frame',TR.nTotal+' of '+TR.events.length,chip('LEAN · total_reflection'));
  h+=row('source flux: reached the rim | still inside after '+LH.OPT.maxEv+' hits | below 0.004',fmt(TR.rim/TR.nRays,3)+' | '+fmt(TR.cut/TR.nRays,3)+' | '+fmt(TR.small/TR.nRays,3),chip('CHECKED · sum = 1 to 1e-12','c')+' residual '+sci(TR.resLedger));
  h+=row('layers on an arm, r = Γ ⊕ (ρ e<sup>2iφ</sup>):  |r|²',STK.map(s=>fmt(s.R,4)).join('  '),chip('LEAN · film_is_oplus')+chip('LEAN · echo_series')+' Film.lean:29, 42; '+chip('DRIVE','d')+' φ = '+fmt(((S.phi%PI)+PI)%PI,3));
  h+=row('net flux, spread over the four layers of each arm',STK.map(s=>sci(s.spread)).join('  '),chip('CHECKED · 1e-12','c'));
  h+=row('same stack at zero phase: tanh(3r/2)',S.r.map(r=>fmt(Math.tanh(1.5*r),5)).join('  '),chip('LEAN · stack_telescopes')+chip('LEAN · tanh_add\'')+' Film.lean:124, Smith.lean:72');
  h+=row('wall Γ² = ½ (z = 3 + 2√2):  Γ² − ½',S.R.map(R=>(R>0.5?'+':'')+fmt(R-0.5,3)).join('  '),chip('LEAN · schottky_five_below')+chip('LEAN · schottky_seven_above')+chip('PROVED · Two Trees v4 Thm 5.3','p'));
  h+=row('face edge on the rim, arccos Γ (fixed rings: 45°)',S.G.map(g=>fmt(deg(Math.acos(g)),2)+'°').join('  '),chip('CHECKED · 1e-12','c'));
  h+=row('pairs of faces, g = sinh(r₁/2) sinh(r₂/2)',PAIRS.map(p=>AXN[p.a]+AXN[p.b]+' '+(p.over?'cross '+fmt(deg(p.alpha),1)+'°':'apart '+fmt(p.delta,3))).join('  '),chip('PROVED · Two Trees v4 Thm 8.4','p')+chip('CHECKED · 1e-10','c'));
  h+=row('two steps: Thomas turn, matrix | 2 arctan(Γ₁Γ₂)',TH.map(t=>fmt(deg(t.angle),2)+'° | '+fmt(deg(t.formula),2)+'°').join('   '),chip('LEAN · thomas5, thomas7')+' equal steps at z = 5, 7; '+chip('CHECKED · 1e-9','c')+' otherwise');
  h+=row('four steps (the square)',LOOPS.map(l=>AXN[l.a]+AXN[l.b]+' '+l.kind+' '+(l.g<1?fmt(deg(l.phiM),1)+'°':fmt(l.runM,3))).join('  '),chip('LEAN · comm_trace')+' PeelTrees4.lean:35; '+chip('CHECKED · 1e-9','c'));
  h+=row('push on the faces of each axis, Σ flux · 2R cos²θ (per unit source flux)',TR.push.map(p=>fmt(p/TR.nRays,3)).join('  '),chip('LEAN · art792_radiation_pressure_components')+' wave front only; '+chip('READING','r')+' untested as a physical pressure');
  h+=row('the same, summed on the clock since τ = '+fmt(REC.t0,1),REC.push.map(p=>fmt(p,2)).join('  '),chip('READING','r'));
  $('laws').innerHTML=h;
  let y='';
  y+=row('hypothesis: occupation of a face  C = 1/(z + 1) = (1 − Γ)/2',S.z.map(z=>fmt(LH.occupation(z),4)).join('  '),chip('HYPOTHESIS','h')+' the identity 1 − 2/(eˣ + 1) = tanh(x/2) is '+chip('LEAN · fermion_smith')+'; x = ln z is the hypothesis');
  y+=row('hypothesis: T = 4C(1 − C)',S.z.map(z=>{const c=LH.occupation(z);return fmt(4*c*(1-c),4);}).join('  '),chip('HYPOTHESIS','h')+chip('CHECKED · 1e-14','c')+' as arithmetic');
  y+=row('hypothesis: light held between faces (flux still inside after '+LH.OPT.maxEv+' hits)',fmt(TR.cut/TR.nRays,3),chip('HYPOTHESIS','h')+' that the faces are electron layers');
  const gaps=PAIRS.filter(p=>!p.over);
  y+=row('hypothesis: gap layer kept between faces, δ = arccosh g',gaps.length?gaps.map(p=>AXN[p.a]+AXN[p.b]+' '+fmt(p.delta,3)).join('  '):'no pair apart at this instant',chip('HYPOTHESIS','h')+' that a least gap is enforced; δ itself is '+chip('PROVED · Two Trees v4','p'));
  y+=row('hypothesis: the rim as ground keeps a record of where light lands',TR.land.length+' landings this frame',chip('HYPOTHESIS','h')+' the landing points are computed; their reading as a record is not');
  $('hyp').innerHTML=y;$('hypbox').style.display=UI.hyp?'':'none';
  $('o_tau').textContent=fmt(CLOCK.tau,2);
}

/* ---------- controls ---------- */
function bindRange(id,out,fn,f){const e=$(id);e.addEventListener('input',()=>{const v=+e.value;$(out).textContent=f?f(v):v;fn(v);});}
bindRange('speed','o_speed',v=>CLOCK.speed=v,v=>v.toFixed(1));
bindRange('amp','o_amp',v=>P.amp=v,v=>v.toFixed(2));
bindRange('rays','o_rays',v=>UI.nRays=v);
$('play').addEventListener('click',()=>{CLOCK.playing=!CLOCK.playing;$('play').textContent=CLOCK.playing?'Pause':'Play';});
$('play').textContent=CLOCK.playing?'Pause':'Play';
$('reset').addEventListener('click',()=>{CLOCK.tau=0;REC.push=[0,0,0];REC.t0=0;});
$('hypt').addEventListener('click',()=>{UI.hyp=!UI.hyp;$('hypt').setAttribute('aria-pressed',UI.hyp);$('hypt').textContent='Hypothesis layer: '+(UI.hyp?'shown':'hidden');});
$('sig').addEventListener('click',()=>{P.sigma=-P.sigma;$('sig').textContent='Admittance: '+(P.sigma>0?'falls outward':'rises outward');REC.push=[0,0,0];REC.t0=CLOCK.tau;});
const VIEWS={whole:[0.7,0.32,7.4,0],cell:[0.55,0.28,3.4,0],arm:[0.05,1.25,5.2,0.6],rim:[2.3,-0.25,5.4,0]};
document.querySelectorAll('button[data-view]').forEach(b=>b.addEventListener('click',()=>{S3.setView(VIEWS[b.dataset.view]);}));
$('clean').addEventListener('click',()=>{document.body.classList.add('clean');S3.view.panel=false;S3.resize();});
$('back').addEventListener('click',()=>{document.body.classList.remove('clean');S3.view.panel=true;S3.resize();});
document.addEventListener('keydown',e=>{if(e.key==='Escape')$('back').click();});

/* ---------- the one clock ---------- */
let rt=1;
S3.onFrame(dt=>{dt=Math.max(0,dt);const d=CLOCK.playing?dt*CLOCK.speed:0;CLOCK.tau+=d;CLOCK.anim+=d;draw(d);rt+=dt;if(rt>0.2){rt=0;readout();}});
window.__LHS={CLOCK,P,UI,S3,get state(){return{S,TR,STK,PAIRS,LOOPS,TH};},step(d){CLOCK.tau+=d;CLOCK.anim+=d;draw(d);readout();}};
})();
