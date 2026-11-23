
/* ---------- v2: heavy elements, spiral, decay, window, two faces, corpus ---------- */
const GR={E:'experimental',S:'semiempirical',T:'theoretical'};
function drawHeavy(){const svg=$('heavysvg'),W=1300,H=560,L=70,R=30,T=30,B=50;const HV=EL.filter(e=>e.heavy&&e.steps.length);
  const X=z=>L+(W-L-R)*(z-86)/24, Y=r=>T+(H-T-B)*(1-Math.log(r)/Math.log(8));
  [1,2,4,8].forEach(v=>{svg.appendChild(el('line',{x1:L,x2:W-R,y1:Y(v),y2:Y(v),stroke:'#141c26'}));axisText(svg,L-10,Y(v)+4,v,{'text-anchor':'end'});});
  for(let z=86;z<=110;z+=2)axisText(svg,X(z),H-B+20,z,{'text-anchor':'middle'});
  axisText(svg,(L+W)/2,H-8,'atomic number Z',{'text-anchor':'middle'});axisText(svg,18,T+10,'step ratio z',{});
  svg.appendChild(el('line',{x1:L,x2:W-R,y1:Y(WALL),y2:Y(WALL),stroke:'#f2c14e','stroke-width':1.6}));axisText(svg,W-R,Y(WALL)-6,'wall z = 3 + 2√2',{fill:'#f2c14e','text-anchor':'end'});
  HV.forEach(e=>{e.steps.forEach(s=>{const ix=e.q.indexOf(s.k-1),g=e.grade[ix]+e.grade[ix+1];const ex=g.indexOf('T')<0;const p=el('circle',{cx:X(e.Z)+((s.k*37)%11-5)*1.6,cy:Y(Math.min(s.z,7.9)),r:ex?3:1.7,fill:ex?'#7be0a0':gcol(s.g2),opacity:.8});p.appendChild(el('title',{},`${e.name} step ${s.k}: z = ${f(s.z,4)}, Γ² = ${f(s.g2,4)}, grades ${g}`));svg.appendChild(p);});
    const st=e.strongest;if(st){const p=el('circle',{cx:X(e.Z),cy:Y(st.z),r:5,fill:'none',stroke:'#ff6fae','stroke-width':1.5,style:'cursor:pointer'});p.appendChild(el('title',{},`${e.name}: strongest step ${st.step}, z = ${f(st.z,4)}`));p.onclick=()=>openEl(e.Z);svg.appendChild(p);axisText(svg,X(e.Z),Y(st.z)-9,e.sym,{'text-anchor':'middle','font-size':11,fill:'#ff9fcb'});}});
  const n=HV.reduce((a,e)=>a+e.steps.length,0),o=HV.reduce((a,e)=>a+e.outside,0),cp=EL.filter(e=>e.heavy&&e.complete).length,nd=EL.filter(e=>e.heavy&&!e.ie.length).length;
  $('heavynote').innerHTML=`Radon to darmstadtium from the same archive: <b>${n.toLocaleString()}</b> adjacent steps, <b>${o}</b> outside the wall. ${cp} ladders are complete (radon to lawrencium); rutherfordium to darmstadtium have partial ladders, and only adjacent archived charges form a step. Elements 111 to 118 have no archived thresholds. Most of these energies are theoretical; small green dots mark steps whose two energies are both experimental or semiempirical, and the pink ring marks each element's strongest step. These steps are reported separately and are not part of the 3,570 count.`;
}
function drawDecay(){const host=$('decaybox');host.innerHTML='';D.decay.forEach((p,ix)=>{const W=1300,H=300,L=80,R=30,T=26,B=40,Q=p.Q.map(v=>v/1000),n=Q.length,lo=Math.min(0,...Q),hi=Math.max(0,...Q),pad=(hi-lo)*0.08;
  const X=i=>L+(W-L-R)*i/(n-1),Y=v=>T+(H-T-B)*(1-(v-lo+pad)/(hi-lo+2*pad));
  const sv=document.createElementNS(ns,'svg');sv.setAttribute('viewBox',`0 0 ${W} ${H}`);sv.setAttribute('class','chart');sv.setAttribute('role','img');
  const ttl=`${p.heavier} minus ${p.lighter}`;sv.setAttribute('aria-label',`Mass gap ${ttl} against common ionic charge`);
  const ticks=5;for(let i=0;i<=ticks;i++){const v=lo+(hi-lo)*i/ticks;sv.appendChild(el('line',{x1:L,x2:W-R,y1:Y(v),y2:Y(v),stroke:'#121a24'}));sv.appendChild(el('text',{x:L-8,y:Y(v)+4,fill:'#8fa0b2','font-size':12,'text-anchor':'end'},v.toFixed(1)));}
  sv.appendChild(el('line',{x1:L,x2:W-R,y1:Y(0),y2:Y(0),stroke:'#8fa0b2','stroke-dasharray':'5 5'}));
  for(let q=0;q<n;q+=10)sv.appendChild(el('text',{x:X(q),y:H-B+18,fill:'#8fa0b2','font-size':12,'text-anchor':'middle'},q+'+'));
  for(let i=1;i<n;i++){sv.appendChild(el('line',{x1:X(i-1),y1:Y(Q[i-1]),x2:X(i),y2:Y(Q[i]),stroke:Q[i]<0?'#ff6fae':'#63d3ff','stroke-width':2}));}
  Q.forEach((v,i)=>{const c=el('circle',{cx:X(i),cy:Y(v),r:p.flips.includes(i)?6:2.2,fill:p.flips.includes(i)?'#f2c14e':(v<0?'#ff6fae':'#63d3ff')});c.appendChild(el('title',{},`charge ${i}+: Q = ${v.toFixed(3)} keV`));sv.appendChild(c);});
  p.flips.forEach(i=>sv.appendChild(el('text',{x:X(i)-10,y:Y(Q[i-1])-10,fill:'#f2c14e','font-size':13,'text-anchor':'end'},`order swaps between ${i-1}+ and ${i}+`)));
  sv.appendChild(el('text',{x:L,y:16,fill:'#e6edf4','font-size':15},`${ttl}, Q(q) in keV`));
  const fig=document.createElement('figure');fig.style.margin='0 0 26px';fig.appendChild(sv);const cap=document.createElement('p');cap.className='note';
  cap.innerHTML=`Neutral anchor: ${esc(p.src)} Bare end: ${Q[n-1].toFixed(3)} keV. ${p.flips.length?`Ground-mass order swaps between ${p.flips[0]-1}+ and ${p.flips[0]}+.`:'The order never swaps; the gap grows as electrons are removed.'}`;fig.appendChild(cap);host.appendChild(fig);});}
function drawWindow(){const svg=$('windowsvg'),W=1300,H=420,L=60,R=40,zl=5.55,zh=6.15,X=z=>L+(W-L-R)*(z-zl)/(zh-zl);const w=D.window;
  const ord=EL.filter(e=>!e.heavy).flatMap(e=>e.steps.map(s=>[s.z,`${e.sym} step ${s.k}`,s.out]));
  const olo=Math.max(...ord.filter(t=>!t[2]).map(t=>t[0])),ohi=Math.min(...ord.filter(t=>t[2]).map(t=>t[0]));
  const yA=120,yO=280;
  svg.appendChild(el('rect',{x:X(olo),y:yO-40,width:X(ohi)-X(olo),height:80,fill:'#0f1a26'}));
  svg.appendChild(el('rect',{x:X(w.lo),y:yA-40,width:X(w.hi)-X(w.lo),height:80,fill:'#1a2a18'}));
  [5.6,5.7,5.8,5.9,6.0,6.1].forEach(z=>{svg.appendChild(el('line',{x1:X(z),x2:X(z),y1:60,y2:H-50,stroke:'#121a24'}));axisText(svg,X(z),H-30,z.toFixed(1),{'text-anchor':'middle'});});
  svg.appendChild(el('line',{x1:X(WALL),x2:X(WALL),y1:50,y2:H-50,stroke:'#f2c14e','stroke-width':2}));axisText(svg,X(WALL)+6,46,'wall 3 + 2√2 = 5.828427',{fill:'#f2c14e'});
  axisText(svg,L,yA-50,`all labels, anion rungs included: [${w.lo.toFixed(6)}, ${w.hi.toFixed(6)}), ${w.lo_name} to ${w.hi_name}`,{fill:'#9fe08f'});
  axisText(svg,L,yO-50,`ordinary steps only: [${olo.toFixed(6)}, ${ohi.toFixed(6)})`,{fill:'#9fdcff'});
  const pts=[...EL.filter(e=>e.anion).map(e=>[e.anion.z0,e.sym+' anion',e.anion.out,yA]),...ord.map(t=>[t[0],t[1],t[2],yO])].filter(t=>t[0]>zl&&t[0]<zh);
  pts.forEach(([z,nm,o,y],i)=>{const c=el('circle',{cx:X(z),cy:y,r:6,fill:o?'#f2c14e':'#63d3ff'});c.appendChild(el('title',{},`${nm}: z = ${z.toFixed(6)}, ${o?'outside':'inside'}`));svg.appendChild(c);axisText(svg,X(z),y+(i%2?24:-14),nm,{'text-anchor':'middle','font-size':12,fill:o?'#f2c14e':'#bfe9ff'});});
  $('windownote').innerHTML=`Every forward cutoff inside the green band sorts all ${(ord.length+EL.filter(e=>e.anion).length).toLocaleString()} scored steps and rungs exactly as the wall does. The band runs from ${w.lo_name} (inside, included) to ${w.hi_name} (outside, excluded) and is ${(w.hi-w.lo).toFixed(4)} wide; the wall sits inside it, derived from geometry, not fitted. Without the anion rungs the band widens to the blue one, from the last inside ordinary step to caesium's xenon-core opening.`;}
function drawFaces(){const svg=$('facesvg'),S=640,L=70,T=20,X=v=>L+(S-L-20)*v,Y=v=>T+(S-T-60)*(1-v);const hue={helium:'#9fdcff',neon:'#b5a3ff',argon:'#7be0a0',krypton:'#ff9fcb',xenon:'#ffd58a'};
  [0,0.25,0.5,0.75,1].forEach(v=>{svg.appendChild(el('line',{x1:X(v),x2:X(v),y1:Y(0),y2:Y(1),stroke:'#121a24'}));svg.appendChild(el('line',{x1:X(0),x2:X(1),y1:Y(v),y2:Y(v),stroke:'#121a24'}));axisText(svg,X(v),Y(0)+20,v,{'text-anchor':'middle'});axisText(svg,X(0)-8,Y(v)+4,v,{'text-anchor':'end'});});
  svg.appendChild(el('line',{x1:X(0),y1:Y(1),x2:X(1),y2:Y(0),stroke:'#f2c14e','stroke-width':2}));axisText(svg,X(0.74),Y(0.2),'Γa² + Γb² = 1',{fill:'#f2c14e'});axisText(svg,X(0)-50,Y(1)-6,'Γb², next face',{fill:'#8fa0b2'});
  axisText(svg,X(0.08),Y(0.1),'the loop closes',{fill:'#63d3ff'});axisText(svg,X(0.62),Y(0.92),'the loop opens',{fill:'#f2c14e'});
  axisText(svg,X(0.5),S-14,'Γa², first face (one element’s core opening)',{'text-anchor':'middle'});
  D.faces.forEach(p=>{const c=el('circle',{cx:X(p.ga2),cy:Y(p.gb2),r:p.open?6:3,fill:p.open?'#f2c14e':hue[p.core],opacity:.9});c.appendChild(el('title',{},`${p.a} then ${p.b}, ${p.core} core: Γa² + Γb² = ${f(p.sum,4)}`));svg.appendChild(c);if(p.open||Math.abs(p.sum-1)<0.05)axisText(svg,X(p.ga2)+8,Y(p.gb2)-6,`${p.a}·${p.b}`,{'font-size':12,fill:p.open?'#f2c14e':'#e6edf4'});});
  const op=D.faces.filter(p=>p.open),nr=[...D.faces].sort((a,b)=>Math.abs(a.sum-1)-Math.abs(b.sum-1))[0];
  $('facenote').innerHTML=`Each point is a pair of neighbouring elements opening the same core: x is the first element's opening, y the next one's. The derived two-face rule closes the loop below the line and opens it above. Of ${D.faces.length} neighbouring pairs, ${op.length} open: ${op.map(p=>p.a+'–'+p.b).join(', ')}. The pair nearest the line is ${nr.a}–${nr.b} at ${f(nr.sum,4)}.`;}

let S3=null;
function drawSpiral(){if(S3){S3.stop();S3=null;}if(!window.THREE)return;const T=THREE,cv=$('spiral3d'),w=cv.clientWidth,hgt=cv.clientHeight;if(!w)return;
  const ren=new T.WebGLRenderer({canvas:cv,antialias:true});ren.setPixelRatio(Math.min(2,devicePixelRatio||1));ren.setSize(w,hgt,false);
  const sc=new T.Scene(),cam=new T.PerspectiveCamera(42,w/hgt,0.1,200),g=new T.Group();sc.add(g);
  const mode=$('spiralmode').value,PS=[[1,2],[3,8],[11,8],[19,18],[37,18],[55,32],[87,32]],RS=6,HS=1.7;
  const per=Z=>{for(let i=PS.length-1;i>=0;i--)if(Z>=PS[i][0])return i;return 0;};
  const val=e=>{if(mode==='anion')return e.anion?Math.sqrt(e.anion.g2):null;if(mode==='core'){const c=e.cores.length?e.cores[e.cores.length-1]:null;return c?Math.sqrt(c.g2):null;}return e.strongest?Math.sqrt(e.strongest.g2):null;};
  const cyl=new T.Mesh(new T.CylinderGeometry(RS*Math.SQRT1_2,RS*Math.SQRT1_2,HS*7.4,72,1,true),new T.MeshBasicMaterial({color:0xf2c14e,transparent:true,opacity:0.07,side:T.DoubleSide,depthWrite:false}));cyl.position.y=HS*3.2;g.add(cyl);
  const cw=new T.LineSegments(new T.EdgesGeometry(new T.CylinderGeometry(RS*Math.SQRT1_2,RS*Math.SQRT1_2,HS*7.4,36,6,true)),new T.LineBasicMaterial({color:0xf2c14e,transparent:true,opacity:0.18}));cw.position.y=HS*3.2;g.add(cw);
  const outer=[];for(let i=0;i<=720;i++){const t=i/720*7,a=2*Math.PI*t;outer.push(new T.Vector3(RS*Math.cos(a),HS*t-HS*0.3,RS*Math.sin(a)));}
  g.add(new T.Line(new T.BufferGeometry().setFromPoints(outer),new T.LineBasicMaterial({color:0x2a3a4c})));
  const tex={};const sprite=(txt,col)=>{const k=txt+col;if(!tex[k]){const c=document.createElement('canvas');c.width=128;c.height=64;const x=c.getContext('2d');x.font='600 40px Inter Tight, sans-serif';x.fillStyle=col;x.textAlign='center';x.textBaseline='middle';x.fillText(txt,64,34);tex[k]=new T.CanvasTexture(c);}const s=new T.Sprite(new T.SpriteMaterial({map:tex[k],transparent:true,depthWrite:false}));s.scale.set(0.9,0.45,1);return s;};
  const pick=[],P=[];
  EL.forEach(e=>{const i=per(e.Z),[z0,n]=PS[i],t=i+(e.Z-z0)/n,a=2*Math.PI*t,v=val(e);const r=v==null?0.25:RS*v;
    const pos=new T.Vector3(r*Math.cos(a),HS*t-HS*0.3,r*Math.sin(a));P.push([e,pos]);
    const col=v==null?0x3a4656:(v*v>0.5?0xf2c14e:0x63d3ff);const m=new T.Mesh(new T.SphereGeometry(v==null?0.07:0.13,12,10),new T.MeshBasicMaterial({color:col}));m.position.copy(pos);m.userData.Z=e.Z;g.add(m);pick.push(m);
    if(v!=null){const sp=[new T.Vector3(0,pos.y,0),pos];g.add(new T.Line(new T.BufferGeometry().setFromPoints(sp),new T.LineBasicMaterial({color:col,transparent:true,opacity:0.18})));}
    const lb=sprite(e.sym,v==null?'#56667a':(v*v>0.5?'#f2c14e':'#bfe9ff'));lb.position.copy(pos).add(new T.Vector3(0,0.32,0));g.add(lb);});
  g.add(new T.Line(new T.BufferGeometry().setFromPoints(P.map(p=>p[1])),new T.LineBasicMaterial({color:0x56667a,transparent:true,opacity:0.5})));
  const cnt=EL.filter(e=>val(e)!=null),o=cnt.filter(e=>val(e)**2>0.5).length;
  $('spiralnote').textContent=`${cnt.length} elements carry this reading; ${o} sit outside the cylinder of radius 1/√2. Grey points have no such reading and sit on the axis side.`;
  let yaw=0.5,pitch=0.35,dist=26,drag=null,auto=true,raf=0,moved=0;
  cv.onpointerdown=ev=>{drag=[ev.clientX,ev.clientY];moved=0;auto=false;cv.setPointerCapture(ev.pointerId);};
  cv.onpointermove=ev=>{if(!drag)return;const dx=ev.clientX-drag[0],dy=ev.clientY-drag[1];moved+=Math.abs(dx)+Math.abs(dy);yaw-=dx*0.008;pitch=Math.max(-1.3,Math.min(1.3,pitch+dy*0.008));drag=[ev.clientX,ev.clientY];};
  cv.onpointerup=ev=>{drag=null;if(moved<4){const rc=new T.Raycaster(),rect=cv.getBoundingClientRect(),m=new T.Vector2((ev.clientX-rect.left)/rect.width*2-1,-(ev.clientY-rect.top)/rect.height*2+1);rc.setFromCamera(m,cam);const h=rc.intersectObjects(pick);if(h.length)openEl(h[0].object.userData.Z);}};
  cv.onwheel=ev=>{ev.preventDefault();dist=Math.max(10,Math.min(60,dist+ev.deltaY*0.02));};
  const still=matchMedia('(prefers-reduced-motion: reduce)').matches;
  (function loop(){if(auto&&!still)yaw+=0.003;cam.position.set(dist*Math.cos(pitch)*Math.sin(yaw),HS*3.2+dist*Math.sin(pitch),dist*Math.cos(pitch)*Math.cos(yaw));cam.lookAt(0,HS*3.2,0);ren.render(sc,cam);raf=requestAnimationFrame(loop);})();
  S3={stop(){cancelAnimationFrame(raf);ren.dispose();}};}
function corpus(){const P=[
 ['What the Peel Keeps','v1.2.2, 22 Nov 2026','https://github.com/dicipler-pixel/votkp-lean/blob/element-paper/loop-wall/research/2026-11-20-element-paper-loop-wall/manuscript/v1_2_2/What_the_Peel_Keeps_v1_2_2_Jeromie_Beasley.pdf','The paper behind every view: the peel step, the wall, the 3,570 steps, the anion rung, the address, the window, decay, Dirac Time, the ball, the ledgers and the Lean appendix.','every view'],
 ['VOTKP: The Vector of Traits Kept under Peeling','v2.9 published; v3.3 content','https://doi.org/10.5281/zenodo.23340757','The peel coordinate Γ = tanh(½ ln z) on the Smith disc, the addition law, the wall as a hyperbolic length, the screened core-opening series and the visible-line rule.','the disk, core strands, tests'],
 ['The Volume of the Knot Potential: Decay and Direction on the Vacuum Disk','v6','','The complex optical coordinate (1 − N)/(1 + N) and the optical constants behind the colour line: all 35 metals above |Γ|² = ½, none of the 6 non-metals.','colour line'],
 ['The Dirac Time of the Gigantefermion','long form v3.0.1','https://doi.org/10.5281/zenodo.22979186','Memory before clock; the Smith coordinate; the population-gap point tanh(βΔ/2) = 1/√2 matching the wall length 2 ln(1 + √2).','the disk, about'],
 ['Two Trees in One Ball','v4','','Theorem 5.3: past z = 3 + 2√2 three perpendicular steps generate a free discrete group, a tree. The loop angle in each drawer is the turning side of that result.','drawer: loop angle'],
 ['Intrinsic Quantum Geometric Tensor on the Grassmannian','v7.2 published','https://doi.org/10.5281/zenodo.23351266','The intrinsic tensor on the projector bundle. Premetric with respect to spacetime, Riemannian on the Grassmannian; no spacetime metric is substituted anywhere on this table.','about'],
 ['Non-Normality Is Connection Energy','v15','https://doi.org/10.5281/zenodo.22803572','The two books E⁻ = (ΔIE)² and E⁺ = (ΣIE)² on every link, with E⁻/E⁺ = Γ²; the wall as the non-zero nilpotent point. The obliqueness K = 1/(1 − 2Γ²) in each drawer.','drawer: two books, K'],
 ['Colour Selects the Leader','v1.2','https://doi.org/10.5281/zenodo.23876186','The log-det ledger S = −½ ln(1 − Γ²), equal to ½ ln 2 at the wall, and the corrected colour results. The ledger column in each drawer.','drawer: ledger S'],
 ['Periodic Table of Elemental Peels','v1.1 published','https://zenodo.org/records/24432624','The edition this one extends: every v1.1 view is kept.','all v1.1 views'],
 ['Lean certificates','LoopWall.lean, OpeningMap.lean, TwoFaceForms.lean','https://github.com/dicipler-pixel/votkp-lean/tree/element-paper/loop-wall/research/2026-11-20-element-paper-loop-wall/lean','The exact wall statements and the element sides, certified in core Lean with no Mathlib. Each drawer links its theorems.','drawer: Lean'],
 ['Also standing behind the table','unlinked here','','The Ledger Outlives the Metric (positivity licence for Γa² + Γb² ≤ 1); Matter at a Scale (scale invariance, why one cutoff fits all elements); What Transport Keeps (the Catalan rail 17 + 12√2 = (3 + 2√2)²); The Offset Belongs to the Boundary (the per-mode offset as the peel rapidity); Universal Projector Geometry, The Weight Between, The Offset Speed Limit and the Operator-First Atlas.','two faces, about']];
 $('corpus').innerHTML=P.map(([t,v,u,p,w])=>`<div class="card"><div class="g">${esc(v)} · on this table: ${esc(w)}</div><h3>${u?`<a href="${u}" target="_blank" rel="noopener">${esc(t)}</a>`:esc(t)}</h3><p>${esc(p)}</p></div>`).join('');}
