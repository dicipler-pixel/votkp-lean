
/* ---------- SCRIPT: SR-LAYER-V1 — the series of ball ends and the moving matrix on them (inserted into the page app) ---------- */
const SX={on:true,level:2,seaBack:true,src:0,mode:'move',n:0,eig:null,eigLevel:0};
let XW=null,XS=null,XE0=0,XES0=0,XIN=0,XNU0=null,XAL=null,XAS=null,XCUR=null,XEN=null,XTR=null,XT0=0;
const NTX=7,NPX=40,XMAX=186;
/* every ball end drawn whole: the part of its sphere inside the ball */
const endMeshes=[];for(let k=0;k<XMAX;k++){const geo=new T.BufferGeometry(),pos=new Float32Array((NTX+1)*(NPX+1)*3),col=new Float32Array((NTX+1)*(NPX+1)*3),idx=[];
  for(let i=0;i<NTX;i++)for(let j=0;j<NPX;j++){const q=i*(NPX+1)+j;idx.push(q,q+1,q+NPX+1,q+1,q+NPX+2,q+NPX+1);}
  geo.setAttribute('position',new T.BufferAttribute(pos,3));geo.setAttribute('color',new T.BufferAttribute(col,3));geo.setIndex(idx);
  const mesh=new T.Mesh(geo,new T.MeshBasicMaterial({vertexColors:true,transparent:true,opacity:0.05,side:T.DoubleSide,depthWrite:false}));mesh.frustumCulled=false;mesh.visible=false;WORLD.add(mesh);endMeshes.push({mesh,pos,col});}
const xRims=segBuf(XMAX*64,0.9,true);WORLD.add(xRims.mesh);
const xArrows=segBuf(XMAX,1,true);WORLD.add(xArrows.mesh);
const xFlow=ptBuf(560*8,0.08);WORLD.add(xFlow.mesh);
const xTrace=segBuf(560*8,0.85,true);WORLD.add(xTrace.mesh);
const xFeet=ptBuf(XMAX,0.34);WORLD.add(xFeet.mesh);
function xBuild(){CLOCK.tau=0;XW=SR.makeWorld(LH.feed(P,0),SX.level,{seaBack:SX.seaBack});XW.d=window.SR_REST['rest'+SX.level].map(v=>v.slice());
  XS=MM.initState(XW,{source:SX.src,noSea:SX.level===3});XS.work=0;const e=MM.energies(XW,XS);XE0=e.E;XES0=e.ES;XIN=0;XT0=0;
  XNU0=XS.Pr?MM.ballCensus(XW,XS).map(c=>c.nu[0]):null;XAL=Array(XW.N).fill(null);XAS=Array(XW.N).fill(null);XAL[SX.src]=0;XTR=new Float64Array(XW.links.length);
  SX.eig=null;SX.n=0;if(SX.level<3)xModes();xRefresh();endMeshes.forEach((m,k)=>m.mesh.visible=SX.on&&k<XW.N);}
function xModes(){SX.eig=SR.modes(XW,XS.d);SX.eigLevel=SX.level;const el=$('x_n');if(el){el.max=SX.eig.vals.length-1;el.value=SX.n;}}
function xRefresh(){XEN=MM.energies(XW,XS);XCUR=MM.lightCurrents(XW,XS);}
function xPhoton(){const b=MM.energies(XW,XS).E,S2=MM.initState(Object.assign({},XW,{d:XS.d}),{source:SX.src,noSea:true});XS.psr=S2.psr;XS.psi=S2.psi;XIN+=MM.energies(XW,XS).E-b;}
/* put the light into eigenvector n (one quantum), so the page shows that mode moving on its own */
function xIntoMode(){if(!SX.eig)return;const v=SX.eig.vecs[SX.n],b=MM.energies(XW,XS).E;XS.psr=Float64Array.from(v[0]);XS.psi=Float64Array.from(v[1]);XIN+=MM.energies(XW,XS).E-b;}
function xFrame(dt,S){if(!XW)xBuild();const on=SX.on;endMeshes.forEach((m,k)=>m.mesh.visible=on&&k<XW.N);xRims.mesh.visible=xArrows.mesh.visible=xFlow.mesh.visible=xTrace.mesh.visible=xFeet.mesh.visible=on;if(!on)return;
  if(dt>0){XS=SR.advance(XW,XS,S,Math.min(0.05,dt),0.02);const t=CLOCK.tau-XT0;
    for(let i=0;i<XW.N;i++)if(XAL[i]===null&&MM.lightDensity(XS,i)>1e-3)XAL[i]=t;
    if(XS.Pr){const C=MM.ballCensus(XW,XS);for(let i=0;i<XW.N;i++)if(XAS[i]===null&&Math.abs(C[i].nu[0]-XNU0[i])>1e-3)XAS[i]=t;}}
  else SR.relink(XW,S);
  xRefresh();for(let k=0;k<XW.links.length;k++)XTR[k]+=Math.abs(XCUR[k])*Math.min(0.05,dt);
  /* per end: light held there, or the chosen eigenvector's weight and phase */
  const N=XW.N,er=XEN.Eper,lit=new Float64Array(N),hue=new Float64Array(N);let lm=1e-9;
  if(SX.mode==='mode'&&SX.eig){const v=SX.eig.vecs[SX.n];for(let i=0;i<N;i++){const a=v[0][2*i]**2+v[1][2*i]**2+v[0][2*i+1]**2+v[1][2*i+1]**2;lit[i]=a;lm=Math.max(lm,a);
      const big=v[0][2*i]**2+v[1][2*i]**2>=v[0][2*i+1]**2+v[1][2*i+1]**2?2*i:2*i+1;hue[i]=(Math.atan2(v[1][big],v[0][big])-SX.eig.vals[SX.n]*(CLOCK.tau-XT0)+20*PI)%(2*PI)/(2*PI);}}
  else for(let i=0;i<N;i++){lit[i]=MM.lightDensity(XS,i);lm=Math.max(lm,lit[i]);}
  xRims.reset();xArrows.reset();xFeet.reset();
  for(let i=0;i<N;i++){const G=XW.geo[i],f=capFrame(G.N),M_=endMeshes[i],a=G.k>>1,lev=XW.ends[i].level,w=Math.sqrt(lit[i]/lm);
    const c=SX.mode==='mode'?M.colour.ramp(hue[i]):[1,0.93,0.72],mix=Math.min(1,1.3*w),base=AXV[a];let o=0;
    M_.mesh.material.opacity=(lev===1?0.045:lev===2?0.035:0.025)+0.3*w*w;
    for(let ii=0;ii<=NTX;ii++){const th=f.tmax*ii/NTX,edge=0.55+0.45*ii/NTX;for(let j=0;j<=NPX;j++){capPoint(f,th,2*PI*j/NPX,tmp);M_.pos[3*o]=tmp[0];M_.pos[3*o+1]=tmp[1];M_.pos[3*o+2]=tmp[2];
      M_.col[3*o]=(base[0]*(1-mix)+c[0]*mix)*edge;M_.col[3*o+1]=(base[1]*(1-mix)+c[1]*mix)*edge;M_.col[3*o+2]=(base[2]*(1-mix)+c[2]*mix)*edge;o++;}}
    M_.mesh.geometry.attributes.position.needsUpdate=true;M_.mesh.geometry.attributes.color.needsUpdate=true;
    ring(xRims,f,f.tmax,lev===1?64:lev===2?40:24,(w>0.05?c:AXV[a]).map(x=>x*(0.25+0.75*w)));
    const q=wp(G.foot,[0,0,0]),d=XS.d[i],m=Math.hypot(d[0],d[1],d[2]),u=w3([d[0]/m,d[1]/m,d[2]/m],1),e=1-(q[0]*q[0]+q[1]*q[1]+q[2]*q[2])/(RB*RB),L=0.05+0.2*e;
    xArrows.add(q,[q[0]+u[0]*L,q[1]+u[1]*L,q[2]+u[2]*L],[1,0.72,0.3],[1,0.95,0.7]);xFeet.add(q,SX.mode==='mode'?c:[1,0.95,0.8],Math.min(1,0.15+w));}
  xRims.commit();xArrows.commit();xFeet.commit();
  /* the energy going from one end to the next: markers along every link in the sense of the flow, and the trace of all that has gone */
  xFlow.reset();xTrace.reset();const jm=Math.max(1e-9,...XCUR.map(Math.abs)),tm=Math.max(1e-9,...XTR);
  XW.links.forEach((l,k)=>{const p=XW.geo[l.i].foot,q=XW.geo[l.j].foot,dd=l.d,sh=Math.sinh(dd),at=t=>{const a=Math.sinh((1-t)*dd)/sh,b=Math.sinh(t*dd)/sh;return wp([a*p[0]+b*q[0],a*p[1]+b*q[1],a*p[2]+b*q[2],a*p[3]+b*q[3]],[0,0,0]);};
    const tr=Math.sqrt(XTR[k]/tm);if(tr>0.03){const tc=[0.95*tr,0.85*tr,0.6*tr];let prev=at(0);for(let s=1;s<=8;s++){const cur=at(s/8);xTrace.add(prev,cur,tc);prev=cur;}}
    const f=Math.abs(XCUR[k])/jm;if(f>0.03){const dir=XCUR[k]>0?-1:1,ph=((CLOCK.anim*0.7*dir)%1+1)%1;for(let m=0;m<8;m++){xFlow.add(at(((m/8+ph)%1+1)%1),[1,0.95,0.7],Math.sqrt(f));}}});
  xFlow.commit();xTrace.commit();}
function xRows(){if(!XW)return '';let h='';const E=XEN,PW=MM.ballPowers(XW,XS);let norm=0;for(let i=0;i<XW.N;i++)norm+=MM.lightDensity(XS,i);
  let io=0;PW.forEach(p=>io=Math.max(io,Math.abs(p.fromLight+p.fromSea-p.toFaces)));const nApart=XW.links.filter(l=>l.del>0).length;
  h+=row('the series: ball ends at level '+SX.level,XW.N+' ends, '+XW.cells.length+' cells, '+XW.links.length+' joins ('+(XW.links.length-nApart)+' crossing or kissing, '+nApart+' apart)',chip('LEAN · smith_identity')+' every end is a sphere meeting the rim at right angles; the generators carry each end into the next');
  h+=row('join strength c₀ sech δ: δ = 0 crossing or kissing, arccosh(sinh h₁ sinh h₂) apart, r for the two ends of one arm',XW.links.slice(0,3).map(l=>fmt(l.c,3)).join('  ')+' …',chip('PROVED · Two Trees v4 Thm 8.4','p')+' for g; '+chip('MODEL CHOICE','d')+' c₀ = 0.5, sech δ as the join; δ checked from the drawn spheres to 1e-13');
  h+=row('light, faces, sea since start',fmt(E.EL,4)+'   '+fmt(E.EF,4)+'   '+(XS.Pr?fmt(E.ES-XES0,4):'— (sea not run at level 3)'),chip('LEAN · connection energy (block form)'));
  h+=row('books: change − work by the breathing ends − light put in',sci(E.E-XE0-XS.work-XIN)+'   (work '+fmt(XS.work,4)+')',chip('CHECKED · live','c'));
  h+=row('light norm − 1;  each end passes on all it takes (worst)',sci(norm-1)+';  '+sci(io),chip('PROVED · ḋ·F = 0','p'));
  if(XS.Pr){let both=0,first=0;for(let i=0;i<XW.N;i++){if(i===SX.src)continue;if(XAL[i]!==null&&XAS[i]!==null){both++;if(XAL[i]<XAS[i])first++;}}
    h+=row('light reached the end before the sea answered',first+' of '+both,chip('MEASURED','c'));}
  if(SX.eig&&SX.eigLevel===SX.level){const v=SX.eig.vecs[SX.n];let p2=0,p4=0;for(let i=0;i<XW.N;i++){const a=v[0][2*i]**2+v[1][2*i]**2+v[0][2*i+1]**2+v[1][2*i+1]**2;p2+=a;p4+=a*a;}
    let lv=[0,0,0,0];for(let i=0;i<XW.N;i++){const a=v[0][2*i]**2+v[1][2*i]**2+v[0][2*i+1]**2+v[1][2*i+1]**2;lv[XW.ends[i].level]+=a;}
    h+=row('eigenvector '+SX.n+' of '+SX.eig.vals.length+': energy, spread (ends it fills)',fmt(SX.eig.vals[SX.n],4)+',  '+fmt(p2*p2/p4,1)+' of '+XW.N,chip('CHECKED · Jacobi residual 1e-14','c'));
    h+=row('its weight on each level of the series',lv.slice(1,SX.level+1).map((x,k)=>'L'+(k+1)+' '+fmt(x,3)).join('   '),chip('READING','r')+' where this mode lives in the series');}
  else h+=row('eigenvectors','at level 3 (372 × 372) press the button; it takes a few seconds',chip('READING','r'));
  return h;}
