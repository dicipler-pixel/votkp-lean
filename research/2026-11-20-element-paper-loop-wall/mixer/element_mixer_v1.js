/* SCRIPT: ELEMENT-PAPER-LOOP-WALL-MIXER-V1
   The Loop Wall: Peeling the Elements from Hydrogen to Astatine — mixer (Jeromie Beasley).
   Built for this paper on the shared 3D parts (mixer3d_parts_v1). One feed operator, one live eye per
   result, in film order. Every readout is computed live from the archive data block (ELEMENT_DATA)
   or from the mathematics it reports. The mixer explores the results; it does not test them. */
(function(){
"use strict";
const M = window.Mixer3D, T = M.T, D = window.ELEMENT_DATA;
const GOLD=[1.0,0.70,0.22], BLUE=[0.22,0.62,1.0], ROSE=[1.0,0.36,0.48], WHITE=[0.86,0.93,1.0], DIM=[0.22,0.29,0.37], GREEN=[0.45,1.0,0.55];
const V3=(x,y,z)=>new T.Vector3(x,y,z);
const WALL=3+2*Math.SQRT2;
const gam=z=>(z-1)/(z+1);
const outside=z=>z>WALL;
const f=(x,d=4)=>(x<0?'−':'')+Math.abs(x).toFixed(d);
const col=v=>new T.Color(v[0],v[1],v[2]);
const mix=(a,b,t)=>[0,1,2].map(i=>a[i]*(1-t)+b[i]*t);
function lbl(g,txt,c,x,y,z,sc){ const s=M.label(txt,c,sc||0.26); s.position.set(x,y,z); g.add(s); return s; }
function circleXZ(r,y,color,op,cx=0,cz=0,n=220){ const p=[]; for(let i=0;i<=n;i++){ const a=i/n*Math.PI*2; p.push(V3(cx+r*Math.cos(a),y,cz+r*Math.sin(a))); } return M.line(p,color,op); }
function plane(w,d,y,color,op){ const m=new T.Mesh(new T.PlaneGeometry(w,d), new T.MeshBasicMaterial({color,transparent:true,opacity:op,side:T.DoubleSide,depthWrite:false})); m.rotation.x=-Math.PI/2; m.position.y=y; return m; }
function bead(c,r){ return M.orb(r||0.06,col(c)); }
const EL=D.el;
const elem=Z=>EL[Math.max(1,Math.min(85,Math.round(Z)))-1];

/* ---------------- feed operator ---------------- */
const feed={ params:[
  {id:'Z',label:'Element (atomic number)',min:1,max:85,step:1,value:6},
  {id:'za',label:'Face a ratio z',min:1.2,max:12,step:0.000001,value:6.079534},
  {id:'zb',label:'Face b ratio z',min:1.2,max:12,step:0.000001,value:5.639665},
  {id:'mesh',label:'Crystal sample size (mesh)',min:4,max:10,step:2,value:4},
  {id:'crystal',label:'Crystal (0 selenium, 1 tellurium)',min:0,max:1,step:1,value:0},
  {id:'mirror',label:'Mirror the crystal (0 no, 1 yes)',min:0,max:1,step:1,value:0},
  {id:'rev',label:'Reverse the path (0 no, 1 yes)',min:0,max:1,step:1,value:0},
  {id:'phi',label:'Loop phase Φ (degrees)',min:-180,max:180,step:1,value:90}],
  build(P){ const e=elem(P.Z); const ie=e.ie; const steps=[];
    for(let k=0;k+1<ie.length;k++){ const z=ie[k+1]/ie[k]; steps.push({k:k+1,z,g:gam(z),out:outside(z)}); }
    const r0=e.ea?{z:ie[0]/e.ea,g:gam(ie[0]/e.ea),out:outside(ie[0]/e.ea)}:null;
    return {P,e,steps,r0}; } };

const eyes=[];

/* ---------------- 1. the peel ladder ---------------- */
eyes.push({ id:'ladder', section:'§1–2', grade:'MEASURED · DERIVED', title:'The peel ladder',
  eq:'z = IE(k+1) / IE(k)\nΓ = (z − 1)/(z + 1) = tanh(½ ln z)\noutside the wall when z > 3 + 2√2',
  text:'Each removal energy of the chosen element is a step, rising with ln IE. The colour of a step is its reflection Γ; a step outside the loop wall glows gold and carries a ring. From hydrogen to astatine only anion rungs and the first opening of a noble-gas core reach outside.',
  uses:['Z'], view:[0.6,0.35,8.5,1.2],
  make(g){ this.g=g; },
  enter(S){ this.draw(S); }, change(S){ this.draw(S); },
  draw(S){ const g=this.g; while(g.children.length) g.remove(g.children[0]);
    const ie=S.e.ie, n=ie.length, lmax=Math.log(ie[n-1]), lmin=S.e.ea?Math.log(S.e.ea):Math.log(ie[0]);
    const X=i=>-3+6*(i/(Math.max(1,n))), Y=l=>-0.2+3.4*(l-lmin)/Math.max(1e-6,lmax-lmin);
    const pts=[]; const R=Math.max(0.8,2.2-n/60);
    const P=k=>{ const a=k/n*Math.PI*1.6-0.8; return V3(R*Math.cos(a)*1.4, Y(Math.log(ie[k])), R*Math.sin(a)*1.4); };
    for(let k=0;k<n;k++) pts.push(P(k));
    g.add(M.line(pts,0x63d3ff,0.35));
    S.steps.forEach((s,i)=>{ const a=pts[i], b=pts[i+1]; const c=s.out?GOLD:mix(BLUE,WHITE,Math.min(1,s.g/0.707));
      const seg=M.line([a,b],col(c),s.out?1:0.8); g.add(seg);
      if(s.out){ const ring=circleXZ(0.22,b.y,0xffb23a,0.95,b.x,b.z,64); g.add(ring); lbl(g,'z '+s.z.toFixed(3),'#ffcf66',b.x+0.25,b.y+0.18,b.z,0.22); } });
    pts.forEach((p,k)=>{ const o=bead(k===0?WHITE:BLUE,0.045+0.03*(k===0)); o.position.copy(p); g.add(o); });
    if(S.e.ea){ const p=V3(pts[0].x-0.6,Y(Math.log(S.e.ea)),pts[0].z); const o=bead(S.r0.out?GOLD:ROSE,0.07); o.position.copy(p); g.add(o);
      g.add(M.line([p,pts[0]],S.r0.out?0xffb23a:0xff5c7a,1)); lbl(g,'anion rung '+S.r0.z.toFixed(3),S.r0.out?'#ffcf66':'#ff8aa0',p.x-0.2,p.y-0.3,p.z,0.22); }
    lbl(g,S.e.n+' ('+S.e.Z+')','#dfe7ef',0,Y(lmax)+0.6,0,0.36);
    g.add(M.grid(8,16,0x1f2a38,0.35)); },
  step(dt,S){ const outs=S.steps.filter(s=>s.out).map(s=>s.k+'→'+(s.k+1));
    const big=S.steps.reduce((m,s)=>s.z>m.z?s:m,{z:0});
    return [['element',S.e.n],['removals',S.e.ie.length],['anion rung z',S.r0?S.r0.z.toFixed(4)+(S.r0.out?' outside':' inside'):'no bound anion'],
      ['outside ordinary steps',outs.length?outs.join(', '):'none'],['largest ratio',big.z.toFixed(4)+' at '+big.k+'→'+(big.k+1)]]; } });

/* ---------------- 2. the loop wall in the disk ---------------- */
eyes.push({ id:'wall', section:'§1, §5', grade:'DERIVED', title:'Two faces, one loop',
  eq:'face at h = ½ ln z;  perpendicular radius 1/sinh h\ncircles meet ⇔ sinh hₐ · sinh h_b < 1\n⇔ Γₐ² + Γ_b² < 1   (equal faces: z = 3 + 2√2)',
  text:'The corner of a ball sits at the centre of the disk with one face along each of two perpendicular directions. At each face the line perpendicular to its direction is a circle meeting the rim at right angles. When the two circles cross the loop closes; when they miss it is open. Carbon’s helium-core opening ratio (6.0795) and nitrogen’s (5.6397) are the defaults: the mixed loop is open by 0.0031.',
  uses:['za','zb'], view:[0.0,1.25,6.4,0],
  make(g){ this.g=g; this.R=2.4; g.add(circleXZ(this.R,0,0x63d3ff,0.8)); g.add(M.line([V3(0,0,0),V3(this.R,0,0)],0x8a9aab,0.6)); g.add(M.line([V3(0,0,0),V3(0,0,this.R)],0x8a9aab,0.6));
    this.ca=M.line([V3(),V3()],0xffb23a,1); this.cb=M.line([V3(),V3()],0x5ab8ff,1); g.add(this.ca); g.add(this.cb);
    this.pa=bead(GOLD,0.07); this.pb=bead(BLUE,0.07); this.hit=bead(GREEN,0.09); g.add(this.pa,this.pb,this.hit);
    lbl(g,'face a','#ffcf66',this.R*0.9,0.25,-0.25,0.24); lbl(g,'face b','#8cc8ff',-0.3,0.25,this.R*0.9,0.24); },
  arc(z,axis){ const h=0.5*Math.log(z), r=Math.tanh(h/2), c=(1+r*r)/(2*r), Rr=(1-r*r)/(2*r), R=this.R, pts=[];
    for(let i=0;i<=240;i++){ const a=Math.PI+(-1+2*i/240)*Math.PI/2; const x=c+Rr*Math.cos(a), y=Rr*Math.sin(a); if(x*x+y*y<=1.0001) pts.push(axis==='a'?V3(R*x,0,R*y):V3(R*y,0,R*x)); }
    return {pts,r,c,Rr}; },
  enter(S){ this.change(S); },
  change(S){ const A=this.arc(S.P.za,'a'), B=this.arc(S.P.zb,'b'); M.setLine(this.ca,A.pts); M.setLine(this.cb,B.pts);
    this.pa.position.set(this.R*A.r,0,0); this.pb.position.set(0,0,this.R*B.r);
    const meet=Math.hypot(A.c,B.c)<A.Rr+B.Rr; this.hit.visible=meet;
    if(meet){ /* intersection of circles centred (ca,0) and (0,cb) inside the disk */
      const x0=A.c, y0=0, x1=0, y1=B.c, d=Math.hypot(x1-x0,y1-y0), aa=(A.Rr*A.Rr-B.Rr*B.Rr+d*d)/(2*d), hh=Math.sqrt(Math.max(0,A.Rr*A.Rr-aa*aa));
      const xm=x0+aa*(x1-x0)/d, ym=y0+aa*(y1-y0)/d; const c1=[xm+hh*(y1-y0)/d, ym-hh*(x1-x0)/d], c2=[xm-hh*(y1-y0)/d, ym+hh*(x1-x0)/d];
      const p=(c1[0]*c1[0]+c1[1]*c1[1]<c2[0]*c2[0]+c2[1]*c2[1])?c1:c2; this.hit.position.set(this.R*p[0],0,this.R*p[1]); } },
  step(dt,S,t){ const ga=gam(S.P.za), gb=gam(S.P.zb), sum=ga*ga+gb*gb, sh=z=>{ const h=0.5*Math.log(z); return Math.sinh(h); };
    const S2=sh(S.P.za)*sh(S.P.zb); this.hit.scale.setScalar(1+0.25*Math.sin(t*4));
    const sa=sh(S.P.za)*sh(S.P.za)>0?1/(sh(S.P.za)*sh(S.P.za)):0, cc=2+4*sa, zc=(cc+Math.sqrt(cc*cc-4))/2;
    return [['Γₐ²',f(ga*ga,5)],['Γ_b²',f(gb*gb,5)],['Γₐ² + Γ_b²',f(sum,5)],['sinh hₐ · sinh h_b',f(S2,5)],
      ['loop',sum<1?'closes':(sum>1?'open':'touches the rim')],['face b that touches, with face a held',zc.toFixed(6)]]; } });

/* ---------------- 3. opening map ---------------- */
eyes.push({ id:'map', section:'§3', grade:'MEASURED · DERIVED', title:'The opening map',
  eq:'opening of a noble core:\nlast removal above the core → first removal from it\nwall plane: ln z = ln(3 + 2√2)',
  text:'Every opening of a helium, neon, argon, krypton and xenon core in the archive, each sequence a strand across the atomic numbers that carry it. The translucent plane is the loop wall. Each strand starts above the wall at its first element and crosses below it almost at once: after carbon, sodium, potassium, rubidium and caesium.',
  uses:[], view:[0.35,0.42,9.5,0.9],
  make(g){ const cores=Object.entries(D.cores), X=Z=>-4+8*(Z-1)/84, Y=z=>Math.log(z)*1.15, cc=[[1,0.78,0.3],[1,0.55,0.3],[0.45,0.8,1],[0.6,0.95,0.55],[0.85,0.6,1]];
    cores.forEach(([nm,seq],i)=>{ const zc=-1.6+i*0.8; const pts=seq.map(([Z,z])=>V3(X(Z),Y(z),zc)); g.add(M.line(pts,col(cc[i]),0.95));
      const p=M.points(seq.length,0.09); seq.forEach(([Z,z],k)=>M.setPt(p,k,pts[k],outside(z)?GOLD:cc[i])); M.flush(p); g.add(p);
      lbl(g,nm+' core',  '#'+cc[i].map(v=>Math.round(v*255).toString(16).padStart(2,'0')).join(''), pts[0].x-0.2, pts[0].y+0.3, zc, 0.22); });
    const pl=plane(8.6,4.2,Y(WALL),0xffffff,0.07); g.add(pl); lbl(g,'loop wall z = 3 + 2√2','#ffffff',3.2,Y(WALL)+0.18,1.9,0.22);
    g.add(M.grid(8.6,24,0x1f2a38,0.3)); this.first=cores.map(([nm,seq])=>[nm,seq[0][1]]); },
  step(){ return this.first.map(([nm,z])=>[nm+' core, first ratio',z.toFixed(3)+(outside(z)?' outside':' inside')]); } });

/* ---------------- 4. hardness and electrophilicity ---------------- */
eyes.push({ id:'chem', section:'§6', grade:'DERIVED · RECOGNISED', title:'Hardness and electrophilicity',
  eq:'η = (IE − EA)/2   χ = (IE + EA)/2   ω = χ²/2η\nΓ₀ = η/χ,   ω/η = 1/(2Γ₀²)\nthe wall Γ₀² = ½  ⇔  ω = η',
  text:'Each bound anion is placed by its electronegativity (across) and hardness (depth); its height is ω/η on a log scale. The translucent plane is ω = η, the loop wall at the anion rung. Above it the hunger for an electron beats the resistance to change: the halogens, the chalcogens below oxygen, silver, iridium, platinum, gold and astatine.',
  uses:['Z'], view:[0.55,0.35,8.2,0.4],
  make(g){ this.g=g; const an=EL.filter(e=>e.ea); this.an=an; const X=chi=>-3.5+7*(chi-2)/5, Z=eta=>-2.5+5*(eta-1)/4, Y=r=>1.6*Math.log(r);
    const p=M.points(an.length,0.13); an.forEach((e,i)=>{ const I=e.ie[0],A=e.ea, eta=(I-A)/2, chi=(I+A)/2, r=chi*chi/(2*eta)/eta; e._p=V3(X(chi),Y(r),Z(eta)); M.setPt(p,i,e._p, r>1?ROSE:BLUE); }); M.flush(p); g.add(p);
    an.forEach(e=>{ if(['F','Cl','Br','I','At','Ag','Au','Pt','Ir','Si','Ca','Cs'].includes(e.s)) lbl(g,e.n,'#b8c6d6',e._p.x+0.12,e._p.y+0.14,e._p.z,0.2); });
    g.add(plane(7.4,5.4,0,0xff6f9a,0.08)); lbl(g,'ω = η','#ff9ab8',3.4,0.15,2.6,0.24);
    this.sel=bead(GOLD,0.11); g.add(this.sel); g.add(M.grid(7.4,14,0x1f2a38,0.3)); },
  enter(S){ this.change(S); }, change(S){ const e=S.e; this.sel.visible=!!e.ea; if(e.ea) this.sel.position.copy(EL[e.Z-1]._p); },
  step(dt,S,t){ const e=S.e; this.sel.scale.setScalar(1+0.3*Math.sin(t*5)); if(!e.ea) return [['element',e.n],['anion','no bound anion in the paper’s table'],['inside the wall','fluorine, sulfur, chlorine, selenium, bromine, silver, tellurium, iodine, iridium, platinum, gold, astatine']];
    const I=e.ie[0],A=e.ea, eta=(I-A)/2, chi=(I+A)/2, w=chi*chi/(2*eta);
    return [['element',e.n],['hardness η (eV)',f(eta,4)],['electronegativity χ (eV)',f(chi,4)],['η/χ = Γ₀',f(eta/chi,5)],['ω/η',f(w/eta,4)],['side',w>eta?'inside (ω > η)':'outside (ω < η)']]; } });

/* ---------------- 5. screening readouts ---------------- */
eyes.push({ id:'screen', section:'§4', grade:'DERIVED', title:'The two screening readouts',
  eq:'S = (h − b)/Z,   σ = Z − √(2b)\nZ(S − σ) = (h − Z²/2) − σ²/2',
  text:'The last two electrons of every element give two readings of the same pair. With a scalar wave alone S stays below 5/8 and σ above it; the electron’s spinor (Dirac) structure carries them across. σ passes 5/8 between neon and sodium (measured, recoil included), S meets σ between aluminium and silicon, S passes 5/8 between argon and potassium, σ passes ½ between nickel and copper and turns negative between palladium and silver.',
  uses:[], view:[0.15,0.25,8.4,0.6],
  make(g){ const X=Z=>-4+8*(Z-2)/83, Y=v=>(v-0.5)*9; const s=D.scr.map(r=>V3(X(r[0]),Y(Math.min(0.75,r[1])),0.3)), q=D.scr.map(r=>V3(X(r[0]),Y(Math.max(-0.2,Math.min(0.75,r[2]))),-0.3));
    g.add(M.line(s,0xffb23a,1)); g.add(M.line(q,0x5ab8ff,1)); lbl(g,'S','#ffcf66',4.2,Y(0.66),0.3,0.3); lbl(g,'σ','#8cc8ff',4.2,Y(0.2),-0.3,0.3);
    g.add(M.line([V3(-4,Y(0.625),0),V3(4,Y(0.625),0)],0xffffff,0.35)); lbl(g,'5/8','#ffffff',-4.4,Y(0.625),0,0.24);
    g.add(M.line([V3(-4,Y(0.5),0),V3(4,Y(0.5),0)],0xffffff,0.18)); lbl(g,'½','#ffffff',-4.4,Y(0.5),0,0.24);
    [[10.5,'neon | sodium'],[13.5,'aluminium | silicon'],[18.5,'argon | potassium'],[28.5,'nickel | copper'],[46.5,'palladium | silver']].forEach(([z,t],i)=>{ const x=X(z); g.add(M.line([V3(x,Y(0.1),0),V3(x,Y(0.72),0)],0x6f7f90,0.35)); lbl(g,t,'#8a9aab',x,Y(0.74)+0.15*(i%2),0,0.18); });
    this.X=X; this.Y=Y; this.cur=bead(GOLD,0.08); this.cur2=bead(BLUE,0.08); g.add(this.cur,this.cur2); },
  step(dt,S,t){ const i=Math.floor((t*6)%D.scr.length), r=D.scr[i]; this.cur.position.set(this.X(r[0]),this.Y(Math.min(0.75,r[1])),0.3); this.cur2.position.set(this.X(r[0]),this.Y(Math.max(-0.2,Math.min(0.75,r[2]))),-0.3);
    return [['element',EL[r[0]-1].n],['S',f(r[1],5)],['σ',f(r[2],5)],['S − σ',f(r[1]-r[2],5)]]; } });

/* ---------------- 6. the reach of sharing ---------------- */
eyes.push({ id:'reach', section:'§7', grade:'DERIVED (computed crystals)', title:'How far the sharing reaches',
  eq:'Σ_{j≠i} ‖P_ij‖² = Tr(C_i − C_i²)\nVar(X) = ½ Σ_ij ‖P_ij‖² (x_i − x_j)²',
  text:'Left, body-centred cubic rubidium; right, face-centred cubic solid krypton. The halo around each centre site has a radius set by the cell-centre spread per electron at the chosen crystal sample size. Both pass the nearest-shell third, yet the rubidium halo keeps growing with the sample while the krypton halo stays put: growth against saturation, the metal against the insulator, on the sizes computed.',
  uses:['mesh'], view:[0.3,0.35,9.0,0.3],
  make(g){ const lat=(cx,fcc)=>{ const pts=[]; for(let i=-2;i<=2;i++)for(let j=-2;j<=2;j++)for(let k=-2;k<=2;k++){ pts.push([i,j,k]); if(!fcc) pts.push([i+.5,j+.5,k+.5]); else { pts.push([i+.5,j+.5,k],[i+.5,j,k+.5],[i,j+.5,k+.5]); } }
      const p=M.points(pts.length,0.08); pts.forEach((q,n)=>M.setPt(p,n,V3(cx+q[0]*0.55,q[1]*0.55,q[2]*0.55),fcc?[0.4,0.75,1]:[1,0.75,0.35])); M.flush(p); return p; };
    g.add(lat(-2.4,false)); g.add(lat(2.4,true));
    this.hR=M.shell(1,0xffb23a,0.16); this.hK=M.shell(1,0x5ab8ff,0.2); this.hR.position.x=-2.4; this.hK.position.x=2.4; g.add(this.hR,this.hK);
    lbl(g,'rubidium (metal)','#ffcf66',-2.4,1.9,0,0.26); lbl(g,'solid krypton (insulator)','#8cc8ff',2.4,1.9,0,0.26); },
  enter(S){ this.change(S); },
  change(S){ const m=S.P.mesh, R=D.loc.Rb.find(r=>r[0]===m)||D.loc.Rb[3], K=D.loc.Kr.find(r=>r[0]===m)||D.loc.Kr[2];
    this.r=R; this.k=K; this.hR.scale.setScalar(0.55*Math.sqrt(R[1])/1.2); this.hK.scale.setScalar(Math.max(0.12,0.55*Math.sqrt(K[1])/1.2*4)); },
  step(dt,S,t){ const m=S.P.mesh; return [['sample size (mesh)',m],['rubidium spread (Å²)',this.r[1].toFixed(4)+(this.r[0]!==m?' (mesh '+this.r[0]+')':'')],
      ['krypton spread (Å²)',this.k[1].toFixed(5)+(this.k[0]!==m?' (largest computed, mesh '+this.k[0]+')':'')],['nearest-shell share, rubidium',D.loc.share.Rb.toFixed(4)],['nearest-shell share, krypton',D.loc.share.Kr.toFixed(4)],['krypton halo','drawn four times larger to be seen']]; } });

/* ---------------- 7. the screw sign ---------------- */
eyes.push({ id:'screw', section:'§8', grade:'DERIVED (crystal records)', title:'The screw sign',
  eq:'χ = (d₀ × d₁) · d₂,   dⱼ = pⱼ₊₁ − pⱼ\nreverse the path: χ stays\nmirror the crystal: χ flips',
  text:'The shortest-contact chain of trigonal selenium or tellurium winds as a three-fold screw. Four successive sites give the screw sign χ. Reversing the order of the path leaves χ unchanged; mirroring the crystal flips it. The peel reflection Γ does the opposite: reversal flips it, a mirror leaves it.',
  uses:['crystal','mirror','rev'], view:[0.6,0.3,6.5,0.8],
  make(g){ this.g=g; },
  enter(S){ this.change(S); },
  change(S){ const g=this.g; while(g.children.length) g.remove(g.children[0]);
    const [a,c,u]=S.P.crystal? D.screw.Te : D.screw.Se, s=S.P.crystal?1:1, r=Math.abs(a*u), sc=0.9;
    const P=j=>V3(r*Math.cos(s*2*Math.PI*j/3)*sc*(S.P.mirror?-1:1), j*c/3*sc*0.6, r*Math.sin(s*2*Math.PI*j/3)*sc);
    const chain=[]; for(let j=-3;j<=9;j++) chain.push(P(j)); g.add(M.line(chain,0x63d3ff,0.35));
    const p=M.points(chain.length,0.12); chain.forEach((q,i)=>M.setPt(p,i,q,[0.75,0.85,1])); M.flush(p); g.add(p);
    let four=[P(0),P(1),P(2),P(3)]; if(S.P.rev) four=four.reverse(); this.four=four;
    for(let i=0;i<3;i++){ g.add(M.line([four[i],four[i+1]],0xffb23a,1)); }
    four.forEach((q,i)=>{ const o=bead(i===0?GREEN:GOLD,0.09); o.position.copy(q); g.add(o); });
    lbl(g,(S.P.crystal?'tellurium':'selenium')+(S.P.mirror?' (mirrored)':''),'#dfe7ef',0,4.0*0.6*sc+0.6,0,0.28);
    const sub=(p,q)=>[p.x-q.x,p.y-q.y,p.z-q.z]; const d=[0,1,2].map(i=>sub(four[i+1],four[i]).map(v=>v/(sc))); d.forEach(v=>{ v[1]/=0.6; }); for(let i=0;i<3;i++){ const v=d[i]; d[i]=[v[0],v[2],v[1]]; } /* back to the crystal frame (height last) */
    const cr=[d[0][1]*d[1][2]-d[0][2]*d[1][1], d[0][2]*d[1][0]-d[0][0]*d[1][2], d[0][0]*d[1][1]-d[0][1]*d[1][0]];
    this.chi=cr[0]*d[2][0]+cr[1]*d[2][1]+cr[2]*d[2][2]; this.bond=Math.hypot(...d[0]); },
  step(dt,S){ return [['crystal',S.P.crystal?'tellurium, P3₁21':'selenium, P3₁21'],['bond (Å)',this.bond.toFixed(5)],['χ (Å³)',f(this.chi,4)],['path',S.P.rev?'reversed':'forward'],['crystal',S.P.mirror?'mirrored':'as recorded']]; } });

/* ---------------- 8. the three-mode loop ---------------- */
eyes.push({ id:'loop3', section:'spinor peel', grade:'DERIVED', title:'Same energies, opposite motion',
  eq:'H₁₂ = H₂₃ = J,  H₃₁ = J e^{iΦ},  W = J³ e^{iΦ}\ndet(λ − H) = λ³ − 3J²λ − 2J³ cos Φ\nP(1→2) − P(2→1) ≈ 2 Im(W) τ³',
  text:'Three equal modes joined in a loop with phase Φ. The energies see only cos Φ, so +Φ and −Φ share one spectrum, yet the amplitude circulates in opposite directions. At Φ = ±90° the state moves from mode to mode with certainty, once every 2π/(3√3 J). Deleting a mode loses the phase; eliminating it exactly keeps it in the remaining link.',
  uses:['phi'], view:[0.0,1.1,5.2,0],
  make(g){ this.o=[0,1,2].map(i=>{ const a=Math.PI/2+i*2*Math.PI/3; const b=bead(WHITE,0.22); b.position.set(1.6*Math.cos(a),0,1.6*Math.sin(a)); g.add(b); lbl(g,'mode '+(i+1),'#b8c6d6',1.95*Math.cos(a),0.35,1.95*Math.sin(a),0.24); return b; });
    g.add(M.line([0,1,2,0].map(i=>this.o[i].position.clone()),0x63d3ff,0.5)); this.tr=M.trail(160,0.12); g.add(this.tr); this.reset(); },
  reset(){ this.re=[1,0,0]; this.im=[0,0,0]; this.t=0; },
  enter(S){ this.reset(); M.clearTrail(this.tr); }, change(S){ this.reset(); M.clearTrail(this.tr); },
  step(dt,S){ const ph=S.P.phi*Math.PI/180, c=Math.cos(ph), s=Math.sin(ph);
    /* H: H12=H23=1, H31=e^{iφ}, H13 = e^{-iφ}; i dψ/dt = Hψ, RK4 */
    const Hr=[[0,1,c],[1,0,1],[c,1,0]], Hi=[[0,0,-s],[0,0,0],[s,0,0]];
    const der=(re,im)=>{ const dr=[0,0,0], di=[0,0,0]; for(let a=0;a<3;a++) for(let b=0;b<3;b++){ const hr=Hr[a][b], hi=Hi[a][b]; const pr=hr*re[b]-hi*im[b], pi=hr*im[b]+hi*re[b]; dr[a]+=pi; di[a]-=pr; } return [dr,di]; };
    const h=Math.min(dt,0.03)*0.9; let re=this.re, im=this.im;
    const k1=der(re,im), a2=[re.map((v,i)=>v+h/2*k1[0][i]),im.map((v,i)=>v+h/2*k1[1][i])], k2=der(...a2), a3=[re.map((v,i)=>v+h/2*k2[0][i]),im.map((v,i)=>v+h/2*k2[1][i])], k3=der(...a3), a4=[re.map((v,i)=>v+h*k3[0][i]),im.map((v,i)=>v+h*k3[1][i])], k4=der(...a4);
    this.re=re.map((v,i)=>v+h/6*(k1[0][i]+2*k2[0][i]+2*k3[0][i]+k4[0][i])); this.im=im.map((v,i)=>v+h/6*(k1[1][i]+2*k2[1][i]+2*k3[1][i]+k4[1][i])); this.t+=h;
    const p=[0,1,2].map(i=>this.re[i]**2+this.im[i]**2), n=p[0]+p[1]+p[2];
    this.o.forEach((o,i)=>{ M.paintOrb(o,mix(DIM,GOLD,p[i]/n),0.2+1.6*p[i]/n); o.scale.setScalar(0.6+0.9*p[i]/n); });
    const cen=V3(0,0,0); this.o.forEach((o,i)=>cen.addScaledVector(o.position,p[i]/n)); M.pushTrail(this.tr,cen,GOLD);
    const th=Math.acos(Math.max(-1,Math.min(1,c))), ev=[0,1,2].map(k=>2*Math.cos((th+2*Math.PI*k)/3)).sort((x,y)=>x-y);
    return [['Φ (degrees)',S.P.phi],['energies (J)',ev.map(v=>f(v,3)).join(', ')],['Re W, Im W',f(c,3)+', '+f(s,3)],['P₁, P₂, P₃',p.map(v=>(v/n).toFixed(3)).join(', ')],['time (ħ/J)',this.t.toFixed(2)],['full-transfer time 2π/(3√3)',(2*Math.PI/(3*Math.sqrt(3))).toFixed(4)]]; } });

/* ---------------- 9. Russell's octave against the wall ---------------- */
eyes.push({ id:'russell', section:'Russell', grade:'MEASURED · RECOGNISED', title:'Russell’s octave against the wall',
  eq:'tones 1+ 2+ 3+ | 4 | 3− 2− 1−\nheight: Γ₀ = (IE − EA)/(IE + EA)\nmates: Γ = (IE_donor − EA_acceptor)/(IE_donor + EA_acceptor)',
  text:'Walter Russell’s octaves run from one inert gas to the next, climbing 1+, 2+, 3+ to an apex at 4 and falling 3−, 2−, 1−. Here each main-group element sits at the height of its anion-rung reflection; the plane is the loop wall. The generative side stays above it, the radiative side falls below it one tone after his apex. Chords join his mates; the 1± mates are always the best-matched junction of their octave.',
  uses:[], view:[0.25,0.32,9.6,0.9],
  make(g){ const oct=[['helium octave',[3,4,5,6,7,8,9]],['neon octave',[11,12,13,14,15,16,17]],['argon octave',[19,20,31,32,33,34,35]],['krypton octave',[37,38,49,50,51,52,53]],['xenon octave',[55,56,81,82,83,84,85]]];
    const X=i=>-3+i, Y=gg=>(gg-0.5)*7, wall=Y(Math.SQRT1_2); this.rows=[];
    g.add(plane(7.4,5.2,wall,0xffffff,0.07)); lbl(g,'loop wall Γ₀² = ½','#ffffff',3.3,wall+0.15,2.4,0.22);
    oct.forEach(([nm,Zs],o)=>{ const zc=-2+o; const pts=[]; Zs.forEach((Z,i)=>{ const e=EL[Z-1]; if(!e.ea) return; const gg=gam(e.ie[0]/e.ea); const P=V3(X(i),Y(gg),zc); pts.push(P);
        const b=bead(gg*gg>0.5?GOLD:BLUE,0.08); b.position.copy(P); g.add(b); if(o===0||i===3) lbl(g,e.n,'#b8c6d6',P.x,P.y+0.25,zc,0.18); });
      g.add(M.line(pts,0x63d3ff,0.45)); lbl(g,nm,'#8a9aab',-3.9,Y(0.95),zc,0.2);
      [[0,6],[1,5],[2,4]].forEach(([a,b])=>{ const d=EL[Zs[a]-1], ac=EL[Zs[b]-1]; if(!ac.ea) return; const gg=gam(d.ie[0]/ac.ea);
        const A=V3(X(a),Y(0.42)-0.22*(b-a===6?0:b-a===4?1:2),zc), B=V3(X(b),A.y,zc); const mid=V3((A.x+B.x)/2,A.y-0.35*(b-a)/6,zc);
        const curve=[]; for(let k=0;k<=30;k++){ const t=k/30; curve.push(V3((1-t)*(1-t)*A.x+2*t*(1-t)*mid.x+t*t*B.x,(1-t)*(1-t)*A.y+2*t*(1-t)*mid.y+t*t*B.y,zc)); }
        g.add(M.line(curve,col(gg*gg>0.5?GOLD:mix(GREEN,BLUE,gg/0.707)),0.9)); this.rows.push([d.n+' → '+ac.n,gg]); }); });
    lbl(g,'1+   2+   3+   4   3−   2−   1−','#dfe7ef',0,Y(1.02),2.6,0.24); },
  step(dt,S,t){ const k=Math.floor(t/1.6)%this.rows.length, r=this.rows[k];
    return [['mate junction',r[0]],['Γ',f(r[1],4)+(r[1]*r[1]>0.5?' outside':' inside')],['the rule','1± mates are the best matched in every octave'],['the turn','between 3− and 2− (oxygen | fluorine in the helium octave)']]; } });

M.run({ title:'The Loop Wall', byline:'JEROMIE BEASLEY · ELEMENT PAPER · MIXER', note:'every readout is computed live from the archive', feed, eyes,
  film:['ladder','wall','map','chem','screen','reach','screw','loop3','russell'] });
})();
