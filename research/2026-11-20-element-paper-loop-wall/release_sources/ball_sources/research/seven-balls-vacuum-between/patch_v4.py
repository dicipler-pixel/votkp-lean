# SCRIPT: SB-V4-PATCH — builds seven_balls_v4 (the vacuum between) from his One Container v3 page script plus SB-VAC-V1
import sys
src=open('p3.js').read(); vac=open('vac_v1.js').read()
def rep(a,b,count=1):
    global src
    n=src.count(a); assert n==count,(n,a[:100]); src=src.replace(a,b)
rep("/* SCRIPT: seven_balls_v3. Seven equal balls, C plus +-x +-y +-z at his z = 3, 5, 7, pushing into C and into each other; his light. */",
    "/* SCRIPT: seven_balls_v4. Seven equal balls, C plus +-x +-y +-z at his z = 3, 5, 7, pushing into C and into each other; his light; the vacuum between (SB-VAC-V1). Built on seven_balls_v3. */")
rep("const rOf=(o,a,t)=>Lh().rOf({zI:o.z[0],zJ:o.z[1],zK:o.z[2],A:o.A,drive:o.breathe?'breathe':'hold'},a,t);",
    "const rOf=(o,a,t)=>Lh().rOf({zI:o.z[0],zJ:o.z[1],zK:o.z[2],A:o.A,drive:o.breathe?'breathe':'hold'},a,t*(o.k||1)); /* o.k: breath speed (MODEL, 1 = his drive) */")
rep("/*LIGHT-END*/\n","/*LIGHT-END*/\n\n"+vac+"\n")
rep("if(typeof module!=='undefined'){module.exports={GEOM,LIGHT};}","if(typeof module!=='undefined'){module.exports={GEOM,LIGHT,VAC};}")
rep("/* SCRIPT: seven_balls_v3 — drawing and controls.","/* SCRIPT: seven_balls_v4 — drawing and controls (v3's, plus the vacuum between).")
rep("show:{light:true,free:true,hits:true,rims:true,occ:true,push:true,record:true,clocks:true,names:true,circles:true}};",
    "show:{light:true,free:true,hits:true,rims:true,occ:true,push:true,record:true,clocks:true,names:true,circles:true,vac:true,pull:true,made:true},breathK:1,pumpEps:0.3};")
rep("const geoOpts=()=>({z:P.z,A:P.A,breathe:P.breathe});","const geoOpts=()=>({z:P.z,A:P.A,breathe:P.breathe,k:P.breathK});")
# vacuum world, stepped with the light
rep("let LW=null,BK=null,acc=0;const tau=new Float64Array(7);",
    "let LW=null,BK=null,acc=0;const tau=new Float64Array(7);\nlet VW=null;const sFnV=(a,b,t)=>{const o=geoOpts();return Math.hypot(GEOM.dOfR(GEOM.rOf(o,a,t),r),GEOM.dOfR(GEOM.rOf(o,b,t),r))-2*r;};\nconst sDot=(a,b,t)=>(sFnV(a,b,t+1e-4)-sFnV(a,b,t-1e-4))/2e-4;")
rep("function buildLight(src){if(src!=null)P.source=src;LW=LIGHT.makeWorld(lightOpts());",
    "function buildLight(src){if(src!=null)P.source=src;VW=VAC.makeVac({zgap:P.zgap,r});VW.t=CLOCK.t;VAC.stepVac(VW,sFnV,CLOCK.t,1e-9);LW=LIGHT.makeWorld(lightOpts());")
rep("function stepLight(n){for(let k=0;k<n;k++){LIGHT.step(LW,DT);",
    "function stepLight(n){for(let k=0;k<n;k++){const tv=LW.t;LIGHT.step(LW,DT);if(VW){VW.o.zgap=P.zgap;VAC.stepVac(VW,sFnV,tv,DT);}")
# drawing parts
rep("const pkPts=pts(NPK,0.2),",
    "const vacLine=seg(12*(2*64+2),1),pullLine=seg(24,1),madePts=pts(12*24,0.11),leakPts=pts(24*8,0.07);\nconst pkPts=pts(NPK,0.2),")
rep("  [rayLine,tunLine,rimLine,occLine,pushLine,clockLine,circLine].forEach(x=>x.done());[pkPts,hitPts,depPts,corePts,handPts].forEach(M.flush);",
"""  drawVac();
  [rayLine,tunLine,rimLine,occLine,pushLine,clockLine,circLine,vacLine,pullLine].forEach(x=>x.done());[pkPts,hitPts,depPts,corePts,handPts,madePts,leakPts].forEach(M.flush);""")
rep("/* ---------- every rule in the page, with its tag ---------- */",
"""/* the vacuum between (SB-VAC-V1): every neighbour gap that stands open */
let vacPhase=0;
function drawVac(){vacLine.reset();pullLine.reset();const sh=P.show;let nm=0,nl=0;vacPhase+=0.07;
  if(VW)for(const [i,j] of VAC.NB){const a=S.balls[i],b=S.balls[j];if(!a.visible||!b.visible)continue;const G=VW.g[VAC.kindOf(i,j)];if(!G.open)continue;
    if(P.cut&&(a.c[2]>0||b.c[2]>0))continue;
    const D=GEOM.dist(a.c,b.c),e=[0,1,2].map(q=>(b.c[q]-a.c[q])/D),pa=[0,1,2].map(q=>a.c[q]+e[q]*r),pb=[0,1,2].map(q=>b.c[q]-e[q]*r),mid=[0,1,2].map(q=>(pa[q]+pb[q])/2);
    const lg=Math.log10(1+G.F),g=Math.min(1,0.25+0.25*lg);
    if(sh.vac){vacLine.add(V(pa),V(pb),[0.9*g,0.8*g,1.0*g]);
      /* the patch that carries the pull (proximity force): radius sqrt(r s) on each face */
      const rho=Math.min(0.6,Math.sqrt(r*G.s)),[v,w]=GEOM.basis(e);
      for(const [cc,sg] of [[pa,-1],[pb,1]]){const dz=r-Math.sqrt(Math.max(0,r*r-rho*rho));let prev=null;
        for(let q=0;q<=64;q++){const t=TAU*q/64,p=[0,1,2].map(m=>cc[m]+sg*dz*e[m]+rho*(Math.cos(t)*v[m]+Math.sin(t)*w[m]));const pv=V(p);if(prev)vacLine.add(prev,pv,[0.55*g,0.5*g,0.95*g]);prev=pv;}}}
    if(sh.pull){const L=Math.min(0.9,0.12*lg+0.05);pullLine.add(V(a.c),V([a.c[0]+e[0]*L,a.c[1]+e[1]*L,a.c[2]+e[2]*L]),[0.35,0.95,1]);pullLine.add(V(b.c),V([b.c[0]-e[0]*L,b.c[1]-e[1]*L,b.c[2]-e[2]*L]),[0.35,0.95,1]);}
    if(sh.made){const En=G.made,bright=Math.min(1,Math.pow(En*40,0.33));
      for(let q=0;q<24&&nm<12*24;q++){const ph=vacPhase*(1+q%5)+q*2.399,rr=Math.min(0.5,Math.sqrt(r*G.s))*Math.sqrt(((q*0.618)%1)),p=[0,1,2].map(m=>mid[m]+rr*(Math.cos(ph)*GEOM.basis(e)[0][m]+Math.sin(ph)*GEOM.basis(e)[1][m]));
        const fl=bright*(0.6+0.4*Math.sin(ph*3));M.setPt(madePts,nm++,V(p),[fl,0.95*fl,fl]);}
      const lr=G.modes.reduce((s,M)=>s+M.n*M.k*Math.PI/G.s*VAC.leak(G.s,P.zgap),0),lb=Math.min(1,Math.pow(lr*10,0.33));
      for(let q=0;q<4&&nl<24*8;q++){const f=((vacPhase*0.5+q/4)%1);for(const [cc,c0,sg] of [[pa,a.c,-1],[pb,b.c,1]]){const p=[0,1,2].map(m=>cc[m]+(c0[m]-cc[m])*0.35*f);M.setPt(leakPts,nl++,V(p),[lb*(1-f),0.85*lb*(1-f),0.5*lb*(1-f)]);}}}}
  for(let q=nm;q<12*24;q++)M.setPt(madePts,q,FAR,zero3);for(let q=nl;q<24*8;q++)M.setPt(leakPts,q,FAR,zero3);}

/* ---------- every rule in the page, with its tag ---------- */""")
rep(" ['model','Bookkeeping: packets below 1e\\u22123 of a ray,",
""" ['exact','The vacuum is only in the twelve neighbour gaps (side balls on perpendicular axes); opposite side balls have C between them. Gap s = hypot(d\\u2090, d\\u1d66) \\u2212 2r, so the twelve gaps are three kinds (x\\u2013y, y\\u2013z, x\\u2013z), four each. Two equal neighbours touch exactly at z = 3 + 2\\u221a2: below the wall they overlap, above it the gap opens'],
 ['cited','Static pull between two of his faces: Lifshitz (1956) energy per area \\u2212\\u03b7\\u03c0\\u00b2\\u0127c/720s\\u00b3, with each face his split at index ratio z_gap (\\u0393_f = (z_gap \\u2212 1)/(z_gap + 1) at normal incidence); \\u03b7 = 0.456 at the wall. Checked against an independent high-precision run (CASIMIR-WALL-01)'],
 ['model','No dispersion: z_gap held at every frequency. Ball\\u2013ball pull by the proximity force rule, U = \\u2212\\u03b7\\u03c0\\u00b3\\u0127c r/1440s\\u00b2, F = \\u03b7\\u03c0\\u00b3\\u0127c r/720s\\u00b3, good only for s \\u226a r. The pull is drawn; it does not move the balls'],
 ['model','The gap\\u2019s own light: standing modes across the gap along the line of centres, \\u03c9\\u2096 = k\\u03c0/s (k = 1, 2, 3); each leaks through its two faces at \\u03ba = \\u2212ln(R_f\\u00b2)/2s, R_f = \\u0393_f\\u00b2. Gaps under 0.02 r are treated as shut'],
 ['cited','Light made by the breathing (dynamic Casimir): for q\\u0308 + \\u03c9(t)\\u00b2q = 0 the instantaneous mode obeys \\u0227 = \\u2212i\\u03c9a \\u2212 (\\u03ba/2)a + (\\u03c9\\u0307/2\\u03c9)a\\u2020; from the vacuum, n = \\u27e8a\\u2020a\\u27e9, m = \\u27e8aa\\u27e9 obey \\u1e45 = \\u2212\\u03ban + (\\u03c9\\u0307/\\u03c9)Re m, \\u1e41 = (\\u22122i\\u03c9 \\u2212 \\u03ba)m + (\\u03c9\\u0307/2\\u03c9)(2n + 1). Checked against the mode function itself (no loss) to 1e\\u22124'],
 ['exact','Vacuum books: work done by the breathing on the gap light = light in the gaps now + leaked into the balls + held when a gap shut. Kept apart from the ray books, which stay exact'],
 ['model','Breath speed \\u00d7k scales the time in his drive (k = 1 is his drive). Resonance needs the gap pumped at twice its own light, period about s: for s = 0.05 and P = 8, k \\u2248 160'],
 ['model','Bookkeeping: packets below 1e\\u22123 of a ray,""")
rep("const TAGN={exact:'EXACT',","const TAGN={cited:'CITED PHYSICS',exact:'EXACT',")
src=src.replace(".t-model{background:#e8553f;color:#fff}",".t-model{background:#e8553f;color:#fff}.t-cited{background:#b8a0ff}")
rep("<h1>Seven Balls, One Container</h1><div class=\"by\">v3 \\u00b7 real balls pushing into each other \\u00b7 his light \\u00b7",
    "<h1>Seven Balls, One Container</h1><div class=\"by\">v4 \\u00b7 the vacuum between \\u00b7 real balls pushing into each other \\u00b7 his light \\u00b7")
# panel: vacuum controls, readout, pump test
rep("+'<div class=\"rd\" id=\"rd\"></div><div class=\"rd\" id=\"rd2\"></div>'",
"""+'<div class="ctl"><label>Breath speed \\u00d7k (MODEL; 1 = his drive) <output id="obk"></output><input id="sbk" type="range" min="0" max="2.6" step="0.01"></label></div>'
+'<div class="rd" id="rd"></div><div class="rd" id="rd2"></div><div class="rd" id="rd3"></div>'
+'<details class="rules" id="pumpbox"><summary>The vacuum test: pump one gap at twice its own light</summary><div class="what" style="font-size:11px">One gap of his faces (z_gap as set), its width swinging by \\u03b5 at 2\\u03c9\\u2081. Gold: with the leak through his faces. Grey: no leak. Light made from the vacuum, photons in the mode, against time in periods of the mode.</div>'
+'<div class="ctl"><label>pump depth \\u03b5 (swing of the gap width) <output id="ope"></output><input id="spe" type="range" min="0.02" max="0.6" step="0.01"></label></div><canvas id="pumpcv" width="320" height="140" style="width:100%;background:#070a10;border:1px solid #1f2a38;border-radius:4px"></canvas><div class="rd" id="pumprd"></div></details>'""")
rep("+'<div class=\"row\"><span class=\"k\">show</span>'+[['light','Light in the balls'],",
    "+'<div class=\"row\"><span class=\"k\">show</span>'+[['vac','Vacuum gaps'],['pull','Pull'],['made','Light made'],['light','Light in the balls'],")
rep("bind('sm','om',()=>P.margin,",
"""(function(){const s=$('sbk'),o=$('obk');s.value=Math.log10(P.breathK);o.textContent='\\u00d7'+P.breathK.toFixed(P.breathK<10?2:0);s.addEventListener('input',()=>{P.breathK=Math.pow(10,+s.value);o.textContent='\\u00d7'+P.breathK.toFixed(P.breathK<10?2:0);});})();
bind('spe','ope',()=>P.pumpEps,v=>P.pumpEps=v,v=>v.toFixed(2),()=>drawPump());
bind('sm','om',()=>P.margin,""")
rep("bind('sg','og',()=>P.zgap,v=>P.zgap=v,v=>v.toFixed(2),()=>{LW.o.zgap=P.zgap;});",
    "bind('sg','og',()=>P.zgap,v=>P.zgap=v,v=>v.toFixed(2),()=>{LW.o.zgap=P.zgap;drawPump();});")
rep("  $('rd').innerHTML=h;$('rd2').innerHTML=h2;",
"""  $('rd').innerHTML=h;$('rd2').innerHTML=h2;
  if(VW){const KN=['x\\u2013y','y\\u2013z','x\\u2013z'],e3=x=>Number.isFinite(x)?(x===0?'0':x.toExponential(2)):'\\u2014';
    let h3='<table><tr><th>gaps (4 each)</th><th>s</th><th>pull</th><th>\\u03c9\\u2081</th><th>\\u03ba/\\u03c9\\u2081</th><th>|\\u1e61| (c)</th><th>n\\u2081</th><th>n\\u2082</th><th>n\\u2083</th></tr>';
    VW.g.forEach((G,q)=>{const sd=Math.abs(sDot(G.i,G.j,CLOCK.t));h3+='<tr><td>'+KN[q]+'</td><td>'+(G.open?G.s.toFixed(4):'<span style="color:#7a8a9b">shut</span>')+'</td><td>'+(G.open?e3(G.F):'\\u2014')+'</td><td>'+(G.open?(Math.PI/G.s).toFixed(1):'\\u2014')+'</td><td>'+(G.open?(VAC.leak(G.s,P.zgap)*G.s/Math.PI).toFixed(3):'\\u2014')+'</td><td>'+sd.toFixed(4)+'</td>'+G.modes.map(M=>'<td>'+(G.open?e3(M.n):'\\u2014')+'</td>').join('')+'</tr>';});
    h3+='</table><div><span>\\u03b7 at z_gap = '+P.zgap.toFixed(3)+' (share of the perfect-mirror pull)</span><b>'+VAC.eta(P.zgap).toFixed(4)+'</b></div>';
    h3+='<div><span>vacuum books, all 12 gaps (\\u0127c/r): breathing work = in gaps + leaked + held at shutting</span><b>'+e3(4*VW.workTot)+' = '+e3(4*VW.madeTot)+' + '+e3(4*VW.leakTot)+' + '+e3(4*VW.closedTot)+'</b></div>';
    $('rd3').innerHTML=h3;}""")
rep("lightChecks().forEach(x=>rows.push(x));","lightChecks().forEach(x=>rows.push(x));vacChecks().forEach(x=>rows.push(x));")
rep("function runChecks(){",
"""function vacChecks(){const rows=[];
  for(const [z,ref] of [[3,0.261245],[ZW,0.456192],[7,0.504067]]){const e=VAC.eta(z);rows.push({name:'\\u03b7(z = '+z.toFixed(3)+') against the independent high-precision run '+ref,val:e,pass:Math.abs(e-ref)<2e-6});}
  {const Sw=GEOM.state({z:[ZW,ZW,ZW],A:0,breathe:false},0,P.margin,[1,1,1,1,1,1],P.order);let m=0;for(const [i,j] of VAC.NB)m=Math.max(m,Math.abs(VAC.gapOf(Sw,i,j)));rows.push({name:'All on the wall: the twelve neighbour gaps are exactly shut (balls touch): max |s|',val:m,pass:m<1e-14});}
  {let e=0;for(const t of [CLOCK.t,CLOCK.t+0.37,CLOCK.t+4.1]){const St=GEOM.state(geoOpts(),t,P.margin,[1,1,1,1,1,1],P.order);for(const [i,j] of VAC.NB){const k=VAC.KINDS[VAC.kindOf(i,j)];e=Math.max(e,Math.abs(VAC.gapOf(St,i,j)-sFnV(k[0],k[1],t)));}}rows.push({name:'Twelve gaps = three kinds, ball to ball, 3 times: max diff',val:e,pass:e<1e-14});}
  {const s0=0.2,eps=0.05,om0=Math.PI/s0,rr=VAC.pumpRun(s0,eps,ZW,20/om0,5,false),T=rr.T,w=t=>Math.PI/(s0*(1-eps*Math.sin(2*om0*t)));let y=[1/Math.sqrt(2*om0),0,0,-om0/Math.sqrt(2*om0)],t=0;const h=0.004/om0;
    const F=(t,y)=>{const ww=w(t);return [y[2],y[3],-ww*ww*y[0],-ww*ww*y[1]];};
    while(t<T-1e-15){const hh=Math.min(h,T-t),k1=F(t,y),k2=F(t+hh/2,y.map((v,i)=>v+hh/2*k1[i])),k3=F(t+hh/2,y.map((v,i)=>v+hh/2*k2[i])),k4=F(t+hh,y.map((v,i)=>v+hh*k3[i]));y=y.map((v,i)=>v+hh/6*(k1[i]+2*k2[i]+2*k3[i]+k4[i]));t+=hh;}
    const ww=w(T),b2=((ww*y[0]+y[3])**2+(ww*y[1]-y[2])**2)/(2*ww);rows.push({name:'Light made from the vacuum, no leak: moment equations vs the mode function |\\u03b2|\\u00b2 (rel)',val:Math.abs(rr.n/b2-1),pass:Math.abs(rr.n/b2-1)<1e-3});}
  if(VW){const d=Math.abs(VW.workTot-(VW.madeTot+VW.leakTot+VW.closedTot));rows.push({name:'Vacuum books close: |work \\u2212 (in gaps + leaked + held at shutting)|',val:d,pass:d<=1e-9*Math.max(1,Math.abs(VW.workTot))});}
  return rows;}
/* the pump test drawing */
function drawPump(){const cv2=document.getElementById('pumpcv');if(!cv2)return;const c=cv2.getContext('2d'),W=cv2.width,H=cv2.height,s0=0.1,om0=Math.PI/s0,per=2*Math.PI/om0,T=40*per;
  const A=VAC.pumpRun(s0,P.pumpEps,P.zgap,T,320,true),B=VAC.pumpRun(s0,P.pumpEps,P.zgap,T,320,false);
  c.fillStyle='#070a10';c.fillRect(0,0,W,H);const lo=-6,hi=6,Y=n=>H-6-(H-12)*(Math.log10(Math.max(1e-6,n))-lo)/(hi-lo),X=t=>6+(W-12)*t/T;
  c.strokeStyle='#1f2a38';c.lineWidth=1;for(let k=lo;k<=hi;k+=2){c.beginPath();c.moveTo(6,Y(Math.pow(10,k)));c.lineTo(W-6,Y(Math.pow(10,k)));c.stroke();}
  c.fillStyle='#7a8a9b';c.font='10px sans-serif';c.fillText('n = 1',W-40,Y(1)-2);c.fillText('40 periods',W-62,H-2);
  for(const [R,col] of [[B,'#7a8a9b'],[A,'#ffd27a']]){c.strokeStyle=col;c.lineWidth=1.5;c.beginPath();R.out.forEach((p,k)=>{const x=X(p[0]),y=Y(p[1]);k?c.lineTo(x,y):c.moveTo(x,y);});c.stroke();}
  const thr=VAC.leak(1,P.zgap)/Math.PI;
  document.getElementById('pumprd').innerHTML='<div><span>after 40 periods: with his faces / no leak</span><b>'+A.n.toExponential(2)+' / '+B.n.toExponential(2)+'</b></div><div><span>leak per radian \\u03ba/\\u03c9\\u2081 (growth needs \\u03b5 above about this)</span><b>'+thr.toFixed(3)+'</b></div>';}
function runChecks(){""")
rep("  if(BK){const f=BK.frac;$('books').innerHTML=",
    "  if(BK){const f=BK.frac;$('books').innerHTML=(VW?'<span style=\"color:#d8ccff\">vacuum: '+VW.g.filter(G=>G.open).length+' of 3 gap kinds open \\u00b7 light in the gaps '+(4*VW.madeTot).toExponential(2)+' \\u0127c/r, paid by the breathing</span>  \\u00b7  ':'')+")
rep("size();setCam();buildLight(0);syncZ();rebuild();strip();","size();setCam();buildLight(0);syncZ();rebuild();strip();drawPump();")
open('p3v4.js','w').write(src)
print('ok',len(src))
