
/* ---------- SCRIPT: MM-GLUE-LAYER-V1 — the moving matrix drawn on the glued balls (inserted into the page app; uses its stage, buffers and clock) ---------- */
const MX={on:true,seaBack:true,src:0};
let MW=null,MS=null,ME0=0,MIN=0,MNU0=null,MAL=null,MAS=null,MNN=null,MCUR=null,MTR=null,MEN=null,MPW=null,MCEN=null,MG=NaN,MDRV=null;
const cmesh=new T.InstancedMesh(new T.SphereGeometry(1,18,12),new T.MeshStandardMaterial({color:0xffffff,emissive:0x1a2430,roughness:0.4,transparent:true,opacity:0.92}),37);cmesh.frustumCulled=false;WORLD.add(cmesh);
const shmesh=new T.InstancedMesh(new T.SphereGeometry(1,28,18),new T.MeshBasicMaterial({color:0xffffff,transparent:true,opacity:0.16,depthWrite:false,blending:T.AdditiveBlending}),37);shmesh.frustumCulled=false;WORLD.add(shmesh);
const mArrows=segBuf(37,1,true);WORLD.add(mArrows.mesh);
const mFlowPts=ptBuf(36*10,0.09);WORLD.add(mFlowPts.mesh);
const mGlow=ptBuf(37,0.6);WORLD.add(mGlow.mesh);
const mTrace=segBuf(36*12,0.9,true);WORLD.add(mTrace.mesh);
const mCross=ptBuf(36,0.26);WORLD.add(mCross.mesh);
/* the glue: one disc on every shared face, coloured by what that face holds (gold) and what crosses it (white) */
const GT=5,GP=30,glue=[];
for(let k=0;k<36;k++){const geo=new T.BufferGeometry(),pos=new Float32Array((GT+1)*(GP+1)*3),col=new Float32Array((GT+1)*(GP+1)*3),idx=[];
  for(let i=0;i<GT;i++)for(let j=0;j<GP;j++){const q=i*(GP+1)+j;idx.push(q,q+1,q+GP+1,q+1,q+GP+2,q+GP+1);}
  geo.setAttribute('position',new T.BufferAttribute(pos,3));geo.setAttribute('color',new T.BufferAttribute(col,3));geo.setIndex(idx);
  const mesh=new T.Mesh(geo,new T.MeshBasicMaterial({vertexColors:true,transparent:true,opacity:0.85,side:T.DoubleSide,depthWrite:false,blending:T.AdditiveBlending}));mesh.frustumCulled=false;WORLD.add(mesh);glue.push({mesh,pos,col});}
function mBuild(){MW=MMG.makeWorld(LH.feed(P,CLOCK.tau),{seaBack:MX.seaBack});MS=MM.initState(MW,{source:MX.src});MS.work=0;const e0=MM.energies(MW,MS);ME0=e0.E;MES0=e0.ES;MIN=0;
  MNU0=MM.ballCensus(MW,MS).map(c=>c.nu[0]);MAL=Array(MW.N).fill(null);MAS=Array(MW.N).fill(null);MAL[MX.src]=0;MNN=MM.nnceCheck(MW,MW.d);MTR=new Float64Array(36);MT0=CLOCK.tau;mRefresh();}
let MT0=0,MES0=0;
function mRefresh(){MEN=MM.energies(MW,MS);MCUR=MM.lightCurrents(MW,MS);}
function mPhoton(){const b=MM.energies(MW,MS).E,S2=MM.initState(Object.assign({},MW,{d:MS.d}),{source:MX.src,noSea:true});MS.psr=S2.psr;MS.psi=S2.psi;MIN+=MM.energies(MW,MS).E-b;}
function mFrame(dt,S){if(!MW)mBuild();if(dt>0&&MX.on){const w=MS.work;MS=MMG.advance(MW,MS,S,Math.min(0.05,dt),0.02);
    const C=MM.ballCensus(MW,MS),t=CLOCK.tau-MT0;for(let i=0;i<MW.N;i++){if(MAL[i]===null&&MM.lightDensity(MS,i)>1e-3)MAL[i]=t;if(MAS[i]===null&&Math.abs(C[i].nu[0]-MNU0[i])>1e-3)MAS[i]=t;}}
  else MMG.relink(MW,S);
  mRefresh();for(let k=0;k<36;k++)MTR[k]+=Math.abs(MCUR[k])*Math.min(0.05,dt);
  shmesh.visible=cmesh.visible=mArrows.mesh.visible=mFlowPts.mesh.visible=mGlow.mesh.visible=mTrace.mesh.visible=mCross.mesh.visible=MX.on;glue.forEach(g=>g.mesh.visible=MX.on);if(!MX.on)return;
  /* balls: at the cell centres, sized by how the ball compresses distance there, coloured by the sea's Gamma = 1 - 2 nu */
  const C=MM.ballCensus(MW,MS),mtx=new T.Matrix4(),cc=new T.Color(),bp=[];
  for(let i=0;i<MW.N;i++){const q=wp(MW.geo.p[i],[0,0,0]);bp.push(q);const e=1-(q[0]*q[0]+q[1]*q[1]+q[2]*q[2])/(RB*RB),r=0.015+0.045*e;mtx.makeScale(r,r,r);mtx.setPosition(q[0],q[1],q[2]);cmesh.setMatrixAt(i,mtx);
    const c=M.colour.ramp(0.5+0.5*C[i].Gamma[0]);cc.setRGB(c[0],c[1],c[2]);cmesh.setColorAt(i,cc);}
  /* shells: hyperbolic ball of radius rho = 0.85 x half the shortest link at that ball; in the Poincare ball it is a sphere with
     centre a(1 - t^2)/(1 - a^2 t^2) and radius t(1 - a^2)/(1 - a^2 t^2), t = tanh(rho/2), a = Euclidean distance of the ball's centre */
  for(let i=0;i<MW.N;i++){let hm=1e9;for(const li of MW.nbr[i])hm=Math.min(hm,MW.links[li].d/2);const t=Math.tanh(0.85*hm/2),q=bp[i],a=Math.hypot(q[0],q[1],q[2])/RB,den=1-a*a*t*t,cr=a*(1-t*t)/den,R=t*(1-a*a)/den,s=a>1e-9?cr/a:0;
    mtx.makeScale(R*RB,R*RB,R*RB);mtx.setPosition(q[0]*s,q[1]*s,q[2]*s);shmesh.setMatrixAt(i,mtx);const c=M.colour.ramp(0.5+0.5*C[i].Gamma[0]);cc.setRGB(c[0]*0.6,c[1]*0.6,c[2]*0.6);shmesh.setColorAt(i,cc);}
  shmesh.instanceMatrix.needsUpdate=true;shmesh.instanceColor.needsUpdate=true;
  cmesh.instanceMatrix.needsUpdate=true;cmesh.instanceColor.needsUpdate=true;
  mArrows.reset();mGlow.reset();for(let i=0;i<MW.N;i++){const d=MS.d[i],m=Math.hypot(d[0],d[1],d[2]),u=w3([d[0]/m,d[1]/m,d[2]/m],1),q=bp[i],e=1-(q[0]*q[0]+q[1]*q[1]+q[2]*q[2])/(RB*RB),L=0.06+0.22*e;
    mArrows.add(q,[q[0]+u[0]*L,q[1]+u[1]*L,q[2]+u[2]*L],[1,0.75,0.35],[1,0.95,0.7]);const rho=MM.lightDensity(MS,i);mGlow.add(q,[1,0.93,0.75],Math.min(1,1.6*Math.sqrt(rho)));}
  mArrows.commit();mGlow.commit();
  /* glue faces */
  const er=MEN.Eper,jm=Math.max(1e-6,...MCUR.map(Math.abs)),em=Math.max(0.02,...er);
  MW.links.forEach((l,k)=>{const f=capFrame(MW.geo.faces[l.j]),G=glue[k];let o=0;const ge=Math.sqrt(er[k]/em),gj=Math.sqrt(Math.abs(MCUR[k])/jm),mid=(()=>{const p=MW.geo.p[l.i],q=MW.geo.p[l.j],s=Math.sinh(l.d/2)/Math.sinh(l.d);return wp(p.map((x,k)=>s*x+s*q[k]),[0,0,0]);})(),em2=1-(mid[0]*mid[0]+mid[1]*mid[1]+mid[2]*mid[2])/(RB*RB),rad=Math.min(f.tmax,(0.015+0.06*em2)/f.Rr);
    for(let i=0;i<=GT;i++){const th=rad*i/GT,fall=1-0.6*i/GT;for(let j=0;j<=GP;j++){capPoint(f,th,2*PI*j/GP,tmp);G.pos[3*o]=tmp[0];G.pos[3*o+1]=tmp[1];G.pos[3*o+2]=tmp[2];
      G.col[3*o]=(0.06+0.6*ge+0.4*gj)*fall;G.col[3*o+1]=(0.05+0.42*ge+0.4*gj)*fall;G.col[3*o+2]=(0.08+0.12*ge+0.4*gj)*fall;o++;}}
    G.mesh.geometry.attributes.position.needsUpdate=true;G.mesh.geometry.attributes.color.needsUpdate=true;});
  /* flow along every link through its face, and the trace of all that has crossed */
  mFlowPts.reset();mTrace.reset();mCross.reset();const tm=Math.max(1e-9,...MTR);
  MW.links.forEach((l,k)=>{const p=MW.geo.p[l.i],q=MW.geo.p[l.j],d=l.d,sh=Math.sinh(d),at=t=>{const a=Math.sinh((1-t)*d)/sh,b=Math.sinh(t*d)/sh;return wp([a*p[0]+b*q[0],a*p[1]+b*q[1],a*p[2]+b*q[2],a*p[3]+b*q[3]],[0,0,0]);};
    const tr=Math.sqrt(MTR[k]/tm),tc=[0.35+0.65*tr,0.3+0.6*tr,0.2+0.5*tr].map(x=>x*tr);let prev=at(0);for(let s=1;s<=12;s++){const cur=at(s/12);mTrace.add(prev,cur,tc);prev=cur;}
    const j=MCUR[k],f=Math.abs(j)/jm;if(f>0.02){const dir=j>0?-1:1,ph=((CLOCK.anim*0.7*dir)%1+1)%1;for(let m=0;m<10;m++){const t=((m/10+ph)%1+1)%1;mFlowPts.add(at(t),[1,0.95,0.7],Math.sqrt(f));}}
    mCross.add(at(0.5),[1,1,1],Math.min(1,Math.sqrt(f)));});
  mFlowPts.commit();mTrace.commit();mCross.commit();}
function mRows(){if(!MW)return '';let h='';const E=MEN,PW=MM.ballPowers(MW,MS);MPW=PW;
  let norm=0;for(let i=0;i<MW.N;i++)norm+=MM.lightDensity(MS,i);
  let worst=0;PW.forEach(p=>worst=Math.max(worst,Math.abs(p.fromLight+p.fromSea-p.toFaces)));
  const D=MM.deriv(MW,MS),C=MM.ballCensus(MW,MS),g=MM.seaSpeed(MW,MS);let lim=0;for(let i=0;i<MW.N;i++){const td=MM.tauDot(MW,MS,D,i);lim=Math.max(lim,td*td/(4*g*C[i].S));}
  let both=0,first=0;for(let i=0;i<MW.N;i++){if(i===MX.src)continue;if(MAL[i]!==null&&MAS[i]!==null){both++;if(MAL[i]<MAS[i])first++;}}
  const ex=[1,7,8,20].map(i=>i+': '+(MAL[i]===null?'—':fmt(MAL[i],2))+' / '+(MAS[i]===null?'—':fmt(MAS[i],2))).join('   ');
  h+=row('balls glued at shared faces','37 balls, 36 faces; matrix clock τ − '+fmt(MT0,2)+' = '+fmt(CLOCK.tau-MT0,2),chip('MODEL CHOICE','d')+' c₀ = 0.5, ω = 2, κ = 0.25; one ball per cell, one link per shared face');
  h+=row('each face is halfway: the link midpoint lies on the shared face','yes, for all 36 (checked to 1e-14 in t_glue1.js)',chip('CHECKED','c'));
  h+=row('light, faces (glue), sea from start',fmt(E.EL,4)+'   '+fmt(E.EF,4)+'   '+(MS.Pr?fmt(E.ES-MES0,4):'—'),chip('LEAN · connection energy (block form)')+' faces κ|dᵢ − Rᵢⱼdⱼ|²');
  h+=row('books: change − work by the breathing faces − photons sent',sci(E.E-ME0-MS.work-MIN)+'   (work so far '+fmt(MS.work,4)+')',chip('CHECKED · live','c')+' the faces move on the page clock; what they put in is recorded');
  h+=row('connection energy at the glued start: ⅛‖[H,H*]‖² | Σ faces',sci(MNN.lhs)+' | '+sci(MNN.rhs),chip('LEAN · NNCE')+' the glued rest holds no mismatch on any face');
  h+=row('light norm − 1;  ball in − out, worst',sci(norm-1)+';  '+sci(worst),chip('PROVED · ḋ·F = 0','p')+chip('CHECKED · live','c'));
  h+=row('clock limit τ̇² ≤ 4gS, largest ratio over the balls',fmt(lim,5),chip('PROVED · Offset Speed Limit','p')+' g = ‖PH(1−P)‖² = '+fmt(g,4));
  h+=row('light reached the ball before the sea answered',first+' of '+both+'   (ball: light / sea  '+ex+')',chip('MEASURED','c')+' first t with |ψᵢ|² > 10⁻³ / |Δνᵢ| > 10⁻³');
  return h;}
