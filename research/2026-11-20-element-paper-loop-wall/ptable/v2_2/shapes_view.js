/* ---------- v2.2: the shapes (Jeromie Beasley, 23 Nov 2026) ---------- */
const SHP={disk:0,triangle:3,square:4,diamond:4,hexagon:6};
function lgamS(x){const g=7,c=[0.99999999999980993,676.5203681218851,-1259.1392167224028,771.32342877765313,-176.61502916214059,12.507343278686905,-0.13857109526572012,9.9843695780195716e-6,1.5056327351493116e-7];if(x<.5)return Math.log(Math.PI/Math.sin(Math.PI*x))-lgamS(1-x);x-=1;let a=c[0];const t=x+g+.5;for(let i=1;i<9;i++)a+=c[i]/(x+i);return .5*Math.log(2*Math.PI)+(x+.5)*Math.log(t)-t+Math.log(a);}
function hypS(a,b,c,zr,zi){let sr=1,si=0,tr=1,ti=0;for(let k=0;k<1500;k++){const f=(a+k)*(b+k)/((c+k)*(k+1)),nr=(tr*zr-ti*zi)*f,ni=(tr*zi+ti*zr)*f;tr=nr;ti=ni;sr+=tr;si+=ti;if(Math.abs(tr)+Math.abs(ti)<1e-13)break;}return [sr,si];}
/* the shape's rotation: corners on the axes for triangle and diamond (open circuit at a corner), faces across the axes for square and hexagon */
function shapeRot(name,n){return (name==='square'||name==='hexagon')?Math.PI/n:0;}
function mapShape(name,type,gr,gi){const n=SHP[name];if(!n)return [gr,gi];const rot=shapeRot(name,n),cr=Math.cos(rot),sr=Math.sin(rot);
 let wr=gr*cr+gi*sr,wi=-gr*sr+gi*cr,ox,oy;
 if(type==='angles'){let m=Math.hypot(wr,wi);if(m>.992){wr*=.992/m;wi*=.992/m;}const a=1/n,b=2/n,c=1+1/n;let pr=1,pi=0;for(let k=0;k<n;k++){const t=pr*wr-pi*wi;pi=pr*wi+pi*wr;pr=t;}const F=hypS(a,b,c,pr,pi);const inr=Math.exp(lgamS(c)+lgamS(c-a-b)-lgamS(c-a)-lgamS(c-b))*Math.cos(Math.PI/n);ox=(wr*F[0]-wi*F[1])/inr;oy=(wr*F[1]+wi*F[0])/inr;}
 else{const q=wr*wr+wi*wi,kr=2*wr/(1+q),ki=2*wi/(1+q),r=Math.hypot(kr,ki);if(r<1e-12){ox=0;oy=0;}else{const ux=kr/r,uy=ki/r;let mx=-1e9;for(let j=0;j<n;j++){const th=Math.PI/n+2*Math.PI*j/n;mx=Math.max(mx,ux*Math.cos(th)+uy*Math.sin(th));}ox=ux*r/mx;oy=uy*r/mx;}}
 return [ox*cr-oy*sr,ox*sr+oy*cr];}
function shapeOutline(name){const n=SHP[name];if(!n){const p=[];for(let i=0;i<=200;i++)p.push([Math.cos(2*Math.PI*i/200),Math.sin(2*Math.PI*i/200)]);return p;}const rot=shapeRot(name,n),R=1/Math.cos(Math.PI/n),p=[];for(let j=0;j<=n;j++){const th=2*Math.PI*j/n+rot;p.push([R*Math.cos(th),R*Math.sin(th)]);}return p;}
function drawShapeDisk(){const svg=$('shapedisk');svg.innerHTML='';const name=$('shapepick').value,type=$('shapetype').value,c=450,R=330/(SHP[name]?1/Math.cos(Math.PI/SHP[name]):1);
 const P=([x,y])=>[c+R*x,c-R*y],path=pts=>'M'+pts.map(p=>P(p).map(v=>v.toFixed(1)).join(',')).join('L');
 svg.appendChild(el('path',{d:path(shapeOutline(name)),fill:'none',stroke:'#3a4a5c','stroke-width':1.4}));
 const wl=[];for(let i=0;i<=240;i++){const t=2*Math.PI*i/240;wl.push(mapShape(name,type,Math.SQRT1_2*Math.cos(t),Math.SQRT1_2*Math.sin(t)));}
 svg.appendChild(el('path',{d:path(wl),fill:'none',stroke:'#f2c14e','stroke-width':1.8}));
 let nout=0,nin=0,aout=0,ain=0;
 EL.filter(e=>!e.heavy).forEach(e=>{e.steps.forEach((s,k)=>{const G=Math.sqrt(s.g2),a=2*Math.PI*(e.Z-1)/85+0.06*Math.sin(k*2.1)+Math.PI/2;const p=P(mapShape(name,type,G*Math.cos(a),G*Math.sin(a)));s.out?nout++:nin++;
   const d=el('circle',{cx:p[0],cy:p[1],r:s.out?6:1.6,fill:s.out?'#f2c14e':gcol(s.g2),opacity:s.out?1:.7});if(s.out){d.appendChild(el('title',{},`${e.name} step ${s.k}: z = ${f(s.z,4)}, Γ² = ${f(s.g2,4)}`));d.style.cursor='pointer';d.onclick=()=>openEl(e.Z);axisText(svg,p[0]+8,p[1]-6,e.sym,{fill:'#f2c14e','font-size':13});}svg.appendChild(d);});
  if(e.anion){const G=Math.sqrt(e.anion.g2),a=2*Math.PI*(e.Z-1)/85+Math.PI/2,p=P(mapShape(name,type,G*Math.cos(a),G*Math.sin(a)));e.anion.out?aout++:ain++;const r=el('circle',{cx:p[0],cy:p[1],r:3.4,fill:'none',stroke:e.anion.out?'#c9a24a':'#63d3ff','stroke-width':1.2});r.appendChild(el('title',{},`${e.name} anion rung: Γ₀² = ${f(e.anion.g2,4)}`));svg.appendChild(r);}});
 $('shapedisknote').textContent=`${name}${SHP[name]?' · chart '+(type==='angles'?'keeps angles':'stretched to the faces'):''} · removal steps outside the wall: ${nout} of ${nout+nin} · anion rungs outside: ${aout} of ${aout+ain}. Changing the shape moves every point but never carries one across the wall (gold): the counts are the same in every shape.`;}
/* the address diamond: anion rung and first core opening, each its own edge */
function drawAddressDiamond(){const svg=$('addrsvg');svg.innerHTML='';const S=640,c=S/2,h=520;
 const X=(A,B)=>c+(A-B)*h/2,Y=(A,B)=>S-50-(A+B)*h/2;
 const pt=(A,B)=>[X(A,B),Y(A,B)],poly=ps=>ps.map(p=>pt(...p).map(v=>v.toFixed(1)).join(',')).join(' ');
 svg.appendChild(el('polygon',{points:poly([[0,0],[1,0],[1,1],[0,1]]),fill:'none',stroke:'#3a4a5c','stroke-width':1.4}));
 const w=Math.SQRT1_2;[[[w,0],[w,1]],[[0,w],[1,w]]].forEach(([a,b])=>{const p=pt(...a),q=pt(...b);svg.appendChild(el('line',{x1:p[0],y1:p[1],x2:q[0],y2:q[1],stroke:'#f2c14e','stroke-width':1.6,'stroke-dasharray':'6 4'}));});
 axisText(svg,...pt(.55,-.06),'anion rung Γ₀ →',{fill:'#8fa0b2','text-anchor':'middle'});axisText(svg,...pt(-.06,.55),'← first core opening Γ',{fill:'#8fa0b2','text-anchor':'middle'});
 [['both outside',.86,.86],['anion out · core in',.86,.3],['anion in · core out',.3,.86],['both inside',.3,.3]].forEach(([t,a,b])=>axisText(svg,...pt(a,b),t,{fill:'#56667a','text-anchor':'middle','font-size':12}));
 let k=0;EL.forEach(e=>{if(!e.anion||!e.cores.length)return;const A=Math.sqrt(e.anion.g2),B=Math.sqrt(e.cores[e.cores.length-1].g2),p=pt(A,B),dir=(B-A)/(1-A*B),size=(A+B)/(1+A*B);k++;
  const d=el('circle',{cx:p[0],cy:p[1],r:4.2,fill:(A>w||B>w)?'#f2c14e':'#63d3ff',opacity:.9});d.appendChild(el('title',{},`${e.name}: anion Γ₀ = ${f(A,4)}, core Γ = ${f(B,4)} · direction B⊖A = ${f(dir,4)} · size A⊕B = ${f(size,4)}`));d.style.cursor='pointer';d.onclick=()=>openEl(e.Z);svg.appendChild(d);
  if(A>w&&B>w||A<.45||B<.45)axisText(svg,p[0]+6,p[1]-5,e.sym,{'font-size':11,fill:'#e6edf4'});});
 $('addrnote').textContent=`${k} elements carry both books. Each element sits at (anion rung Γ₀, first core opening Γ): one edge of the diamond for each book, so neither bends the other. The dashed gold lines are the wall on each edge; the four corners of the grid are the four addresses of the Signatures view. Hover a point for its two diagonals: direction B ⊖ A (which book leads) and size A ⊕ B (both together), each by peel addition.`;}
/* which element is nearest, read on each shape (same books: the first 8 steps) */
let NN=null;
function shapeNeighbours(){if(NN)return NN;const K=8,E=EL.filter(e=>!e.heavy&&e.ie.length>=K+1&&e.col);const G=z=>(z-1)/(z+1);
 const z=E.map(e=>e.ie.slice(0,K+1).map((v,i,a)=>i?a[i]/a[i-1]:null).slice(1)),g=z.map(r=>r.map(G)),L=z.map(r=>r.map(v=>.5*Math.log(v))),LL=z.map(r=>r.map(v=>Math.log(Math.log(v))));
 const D={circle:(i,j)=>{const x=g[i].map(v=>v/Math.sqrt(K)*.999),y=g[j].map(v=>v/Math.sqrt(K)*.999);let d2=0,nx=1,ny=1;for(let k=0;k<K;k++){d2+=(x[k]-y[k])**2;nx-=x[k]*x[k];ny-=y[k]*y[k];}return Math.acosh(1+2*d2/(nx*ny));},
  diamond:(i,j)=>L[i].reduce((s,v,k)=>s+Math.abs(v-L[j][k]),0),
  cube:(i,j)=>{let mx=-1e9,mn=1e9;for(let k=0;k<K;k++)for(const s of[1,-1]){const r=Math.log(1-s*g[j][k])-Math.log(1-s*g[i][k]);mx=Math.max(mx,r);mn=Math.min(mn,r);}return .5*(mx-mn);},
  simplex:(i,j)=>{let mx=-1e9,mn=1e9;for(let k=0;k<K;k++){const r=LL[j][k]-LL[i][k];mx=Math.max(mx,r);mn=Math.min(mn,r);}return mx-mn;}};
 const out={},recall={};for(const s in D){let hit=0;E.forEach((e,i)=>{let best=1e99,bj=-1;for(let j=0;j<E.length;j++)if(j!==i){const d=D[s](i,j);if(d<best){best=d;bj=j;}}(out[e.sym]=out[e.sym]||{})[s]=E[bj].sym;if(E[bj].col===e.col)hit++;});recall[s]=hit/E.length;}
 NN={near:out,recall,n:E.length};return NN;}
function drawShapeTable(){const R=shapeNeighbours();$('shaperecall').innerHTML=`<table class="steps" style="max-width:640px"><tr><th style="text-align:left">shape reading the first 8 steps</th><th>nearest element in the same column</th></tr>${[['circle','circle (the disk, as now)'],['diamond','diamond (each step its own edge)'],['cube','cube (its own reading)'],['simplex','triangle family (ladder shape only)']].map(([k,t])=>`<tr><td style="text-align:left">${t}</td><td>${f(R.recall[k],3)} of ${R.n}</td></tr>`).join('')}<tr><td style="text-align:left">chance</td><td>about 0.05</td></tr></table>`;}
function drawShapes(){drawShapeDisk();drawAddressDiamond();drawShapeTable();}
{const _oe2=openEl;openEl=function(Z){_oe2(Z);const e=byZ[Z];if(!e)return;const R=shapeNeighbours().near[e.sym];if(R)$('dbody').insertAdjacentHTML('beforeend',`<div class="sec"><h4>On the shapes</h4><div class="kv"><span>nearest on the circle</span><b>${R.circle}</b><span>nearest on the diamond</span><b>${R.diamond}</b><span>nearest on the cube</span><b>${R.cube}</b><span>nearest on the triangle family</span><b>${R.simplex}</b></div><p class="sub" style="margin-top:6px">Same books (the first 8 removal steps) read on each shape. See the Shapes view.</p></div>`);};}
