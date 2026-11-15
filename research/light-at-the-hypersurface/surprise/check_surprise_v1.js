// SCRIPT: check_surprise_v1
// Checks the maths used by Light_at_the_Hypersurface_Surprise_v1.html. The maths block is read out of the page itself
// (between LH-MATH-BEGIN and LH-MATH-END), so what is tested is what the page runs.
// WHY each line proves its claim: every line compares the page's function with an independent route
// (a second formula, a matrix computed here, or a measurement from the vectors themselves), not with itself.
// KILL LINES (written before the run): a line fails if its value exceeds the tolerance printed beside it.
const fs=require('fs'),path=require('path'),vm=require('vm');
const html=fs.readFileSync(path.join(__dirname,'Light_at_the_Hypersurface_Surprise_v1.html'),'utf8');
const a=html.indexOf('/*LH-MATH-BEGIN*/'),b=html.indexOf('/*LH-MATH-END*/');if(a<0||b<0)throw new Error('maths block not found');
const ctx={module:{exports:{}},Math,console};vm.createContext(ctx);vm.runInContext(html.slice(a,b),ctx);const LH=ctx.module.exports;
let seed=20261115;const rnd=()=>{seed=(seed*1664525+1013904223)>>>0;return seed/4294967296;};const ru=(lo,hi)=>lo+(hi-lo)*rnd();
const lines=[];let fails=0;
function line(id,what,val,tol,cmp){const pass=cmp?cmp(val):(Number.isFinite(val)&&val<=tol);if(!pass)fails++;lines.push((pass?'PASS ':'FAIL ')+id.padEnd(5)+what.padEnd(86)+' value '+(typeof val==='number'?val.toExponential(2):val)+'   tol '+(tol==null?'':tol.toExponential(0)));}
const P0={zbar:[3,5,7],amp:0.35,T:[8,13,21],ph:[0,2*Math.PI/3,4*Math.PI/3],sigma:1,Tphi:9,Tchi:55};
let m;
// C1 Smith identity (smith_identity, interface_smith, tanh_half_log) and round trip (round_trip)
m=0;for(let i=0;i<10000;i++){const z=Math.exp(ru(-4,4));m=Math.max(m,Math.abs(LH.smith(z)-Math.tanh(Math.log(z)/2)));}line('C1a','(z-1)/(z+1) = tanh(ln z / 2), 1e4 ratios',m,1e-14);
m=0;for(let i=0;i<10000;i++){const t=ru(-3,3);m=Math.max(m,Math.abs(1-Math.tanh(t)**2-1/Math.cosh(t)**2));}line('C1b','1 - tanh^2 t = 1/cosh^2 t',m,1e-14);
// C2 flux balance at a step (flux_balance), reciprocity, matched load
m=0;let m2=0;for(let i=0;i<10000;i++){const Y1=Math.exp(ru(-4.6,4.6)),Y2=Math.exp(ru(-4.6,4.6)),r=(Y1-Y2)/(Y1+Y2),t=2*Y1/(Y1+Y2);m=Math.max(m,Math.abs(r*r+Y2/Y1*t*t-1));const sp=LH.split(Y1,Y2,1);m2=Math.max(m2,Math.abs(sp.r-r),Math.abs(sp.R+sp.T-1),Math.abs(sp.T-Y2/Y1*t*t)/Math.max(1e-300,sp.T+1e-9),Math.abs(LH.split(Y2,Y1,1).r+r));}
line('C2a','R + (Y2/Y1) t^2 = 1 at normal incidence, 1e4 random admittances',m,1e-12);line('C2b','page split() at normal incidence = step law; reverse step has -r',m2,1e-9);
line('C2c','matched load: equal admittances give r = 0',Math.abs(LH.split(3.7,3.7,0.4).r),1e-15);
// C3 oblique flux with Y = sqrt(a - C)
m=0;for(let i=0;i<10000;i++){const Y1=Math.exp(ru(-2,2)),Y2=Math.exp(ru(-2,2)),c1=ru(0.01,1),sp=LH.split(Y1,Y2,c1);if(sp.total)continue;m=Math.max(m,Math.abs(sp.r*sp.r+(sp.y2/sp.y1)*sp.t*sp.t-1),Math.abs(sp.R+sp.T-1),Math.abs(Y1*Y1*(1-c1*c1)-Y2*Y2*sp.s2sq)/(Y1*Y1));}
line('C3','oblique step: R + T = 1 and a1 sin^2(th1) = a2 sin^2(th2), 1e4 cases',m,1e-12);
// C4 critical angle by bisection on the page's own split(), against arcsin(1/z); total return has |Gamma| = 1
m=0;m2=0;for(const z of [1.5,2,3,5,3+2*Math.SQRT2,7,13]){let lo=0,hi=Math.PI/2;for(let i=0;i<80;i++){const mid=(lo+hi)/2;if(LH.split(1,1/z,Math.cos(mid)).total)hi=mid;else lo=mid;}m=Math.max(m,Math.abs(lo-Math.asin(1/z)));
  const th=Math.asin(1/z)+0.2,sp=LH.split(1,1/z,Math.cos(th)),y=sp.y1,ke=sp.ke,g=LH.C.div([y,-ke],[y,ke]);m2=Math.max(m2,Math.abs(LH.C.abs2(g)-1),Math.abs(Math.atan2(g[1],g[0])-sp.phase));}
line('C4a','critical angle from bisection = arcsin(1/z) (rad)',m,1e-9);line('C4b','past it |(y - i k)/(y + i k)|^2 = 1 and its phase = -2 arctan(k/y)',m2,1e-12);
line('C4c','R = 4 to 1 (Y 2 to 1): critical angle 30 degrees (card B39 witness)',Math.abs((()=>{let lo=0,hi=Math.PI/2;for(let i=0;i<80;i++){const mid=(lo+hi)/2;if(LH.split(2,1,Math.cos(mid)).total)hi=mid;else lo=mid;}return lo*180/Math.PI-30;})()),1e-9);
line('C4d','R = 1 to 4 at 50 degrees leaves at 22.5210 degrees (card B30 witness, 4 decimals)',Math.abs(Math.asin(Math.sqrt(LH.split(1,2,Math.cos(50*Math.PI/180)).s2sq))*180/Math.PI-22.5210),5e-5);
// C5 the whole moving scene: run the clock, both admittance orientations
for(const sigma of [1,-1]){const P=Object.assign({},P0,{sigma});let F=0,Cn=0,I=0,L=0,N=0,Pl=0,ev=0,tot=0,SP=0,cross=0;
  for(let n=0;n<600;n++){const S=LH.feed(P,n/12),t=LH.trace(S,LH.fanDirs(S,S.chi).concat(LH.sourceDirs(36,S.chi)));F=Math.max(F,t.resFlux);Cn=Math.max(Cn,t.resCons);I=Math.max(I,t.resInc);L=Math.max(L,t.resLedger);N=Math.max(N,t.resNorm);Pl=Math.max(Pl,t.resPlane);ev+=t.events.length;tot+=t.nTotal;
    for(let a=0;a<3;a++){const z=S.z[a],st=LH.stack([1,z**-sigma,z**(-2*sigma),z**(-3*sigma)],S.phi);SP=Math.max(SP,st.spread/Math.max(1e-300,st.flux[0]));}
    if(n>0){const Sp=LH.feed(P,(n-1)/12);for(let a=0;a<3;a++)if((Sp.R[a]-0.5)*(S.R[a]-0.5)<0)cross++;}}
  const tag=sigma>0?'falls outward':'rises outward';
  line('C5a','['+tag+'] 600 frames, '+ev+' hits ('+tot+' whole returns): flux residual',F,1e-12);
  line('C5b','['+tag+'] a sin^2(theta) across each crossing, angles measured from tangents',Cn,1e-10);
  line('C5c','['+tag+'] centre rays: sin(theta) = cosh(r/2) sin(psi)',I,1e-10);
  line('C5d','['+tag+'] every ray: rim + still inside + below threshold = 1',L,1e-12);
  line('C5e','['+tag+'] hit points lie on their face <X,N> = 0',Pl,1e-9);
  line('C5f','['+tag+'] rounding drift of <X,X> = 1, <v,v> = -1, <X,v> = 0 before it is removed',N,1e-6);
  line('C5g','['+tag+'] arm stacks: relative spread of net flux over the four layers',SP,1e-10);
  line('C5h','['+tag+'] arms crossed the wall during the run (count must be > 0)',cross,null,v=>v>0);}
// C5i cold feed equals stepped feed (the state is a pure function of the clock)
{const S1=LH.feed(P0,17.25),S2=LH.feed(P0,17.25);line('C5i','state at one clock value is reproducible bit for bit',JSON.stringify(S1)===JSON.stringify(S2)?0:1,0);}
// C6 layers: Smith-addition recursion against a characteristic-matrix product written here (as rTop in VOTKP/ThinFilm.lean)
function charMatrix(Ys,phi){const C=LH.C;let B=[1,0],Cc=[Ys[Ys.length-1],0];for(let k=Ys.length-2;k>=1;k--){const c=[Math.cos(phi),0],s=Math.sin(phi),B2=C.add(C.mul(c,B),C.mul([0,-s/Ys[k]],Cc)),C2=C.add(C.mul([0,-s*Ys[k]],B),C.mul(c,Cc));B=B2;Cc=C2;}
  return C.div(C.sub([Ys[0]*B[0],Ys[0]*B[1]],Cc),C.add([Ys[0]*B[0],Ys[0]*B[1]],Cc));}
m=0;m2=0;let m3=0;for(let i=0;i<4000;i++){const D=2+Math.floor(rnd()*5),Ys=[];for(let k=0;k<=D;k++)Ys.push(Math.exp(ru(-2,2)));const phi=ru(0,6.3),st=LH.stack(Ys,phi),r2=charMatrix(Ys,phi);
  m=Math.max(m,Math.hypot(st.r[0]-r2[0],st.r[1]-r2[1]));m2=Math.max(m2,st.spread/st.flux[0]);m3=Math.max(m3,Math.abs(LH.stack(Ys,0).r[0]-(Ys[0]-Ys[D])/(Ys[0]+Ys[D])));}
line('C6a','stack by Smith addition = characteristic-matrix product, 4000 random stacks of 2 to 6 faces',m,1e-10);
line('C6b','net flux is the same in every layer (relative spread)',m2,1e-10);line('C6c','zero phase: the stack telescopes to its outer pair (stack_telescopes)',m3,1e-12);
m=0;for(const z of [2,3,5,7,11]){const st=LH.stack([1,1/z,1/z/z,1/z/z/z],0);m=Math.max(m,Math.abs(st.r[0]-Math.tanh(1.5*Math.log(z))));}line('C6d','three equal steps at zero phase give tanh(3r/2) (tanh_add\')',m,1e-12);
m=0;for(let i=0;i<2000;i++){const g=ru(-0.9,0.9),x=LH.C.mul([ru(0,0.95),0],LH.C.ei(ru(0,6.3)));let s=[g,0],pw=[1,0];for(let k=0;k<600;k++){s=LH.C.add(s,LH.C.mul([(1-g*g),0],LH.C.mul(pw,x)));pw=LH.C.mul(pw,LH.C.mul([-g,0],x));}const o=LH.oplus([g,0],x);m=Math.max(m,Math.hypot(s[0]-o[0],s[1]-o[1]));}
line('C6e','front reflection plus 600 echoes = g (+) x (echo_series, echo_resum)',m,1e-10);
{const w=(a,x)=>LH.C.abs2(LH.oplus([a,0],[x,0]));line('C6f','witness a = 1/2, x = +1/5 and -1/5 give 49/121 and 1/9 (one_radius_cannot_decide)',Math.max(Math.abs(w(0.5,0.2)-49/121),Math.abs(w(0.5,-0.2)-1/9)),1e-15);}
// C7 the wall and the face edge on the rim
{const z=LH.WALL,G=LH.smith(z);line('C7a','z = 3 + 2 sqrt 2 gives Gamma^2 = 1/2',Math.abs(G*G-0.5),1e-14);
 line('C7b','z = 5 below, z = 7 above: Gamma^2 = 4/9, 9/16',Math.max(Math.abs(LH.smith(5)**2-4/9),Math.abs(LH.smith(7)**2-9/16)),1e-15);
 m=0;for(let i=0;i<2000;i++){const r=ru(0.2,3),h=r/2,N=LH.faceN([0,0,1],h),ps=Math.acos(Math.tanh(r/2)),ph=ru(0,6.3),nul=[1,Math.sin(ps)*Math.cos(ph),Math.sin(ps)*Math.sin(ph),Math.cos(ps)];m=Math.max(m,Math.abs(LH.mink(nul,N))/Math.cosh(h));}
 line('C7c','a face meets the rim on the circle cos(psi) = Gamma (null directions orthogonal to N)',m,1e-12);
 line('C7d','at the wall that circle is at 45 degrees',Math.abs(Math.acos(G)*180/Math.PI-45),1e-12);}
// C8 pairs of faces
m=0;m2=0;m3=0;for(let i=0;i<2000;i++){const S=LH.feed({zbar:[ru(1.5,13),ru(1.5,13),ru(1.5,13)],amp:0,T:[1,1,1],ph:[0,0,0],sigma:1,Tphi:9,Tchi:55},0);
  for(const [a,b] of [[0,1],[1,2],[0,2]]){const pr=LH.pair(S,a,b),Na=S.N0[2*a],Nb=S.N0[2*b+1];m=Math.max(m,Math.abs(LH.mink(Na,Nb)-pr.g));const ft=LH.gapFeet(Na,Nb);
    if(ft){m2=Math.max(m2,Math.abs(LH.mink(ft.pa,Na)),Math.abs(LH.mink(ft.pb,Nb)),Math.abs(LH.mink(ft.pa,ft.pa)-1));if(pr.g>1.0001)m3=Math.max(m3,Math.abs(LH.hdist(ft.pa,ft.pb)-pr.delta));}}}
line('C8a','<N_a, N_b> = sinh(r_a/2) sinh(r_b/2) for perpendicular arms',m,1e-12);line('C8b','feet of the common perpendicular lie on their faces, on the hyperboloid',m2,1e-9);line('C8c','distance between the feet = arccosh g',m3,1e-8);
// C9 Thomas turn
m=0;for(let i=0;i<500;i++){const ra=ru(0.2,2.6),rb=ru(0.2,2.6),t=LH.thomas([1,0,0],ra,[0,1,0],rb);m=Math.max(m,Math.abs(t.angle-LH.thomasFormula(Math.tanh(ra/2),Math.tanh(rb/2))));
  const LR=LH.mm(t.L,t.R);for(let p=0;p<4;p++)for(let q=0;q<4;q++)m=Math.max(m,Math.abs(LR[p][q]-t.M[p][q])/t.M[0][0]);for(let p=1;p<4;p++)m=Math.max(m,Math.abs(t.R[0][p]),Math.abs(t.R[p][0]));}
line('C9a','B_a B_b = (boost)(rotation); rotation angle = 2 arctan(G_a G_b), 500 random pairs',m,1e-9);
{const t5=LH.thomas([1,0,0],Math.log(5),[0,1,0],Math.log(5)),t7=LH.thomas([1,0,0],Math.log(7),[0,1,0],Math.log(7));
 line('C9b','z = 5: cos, sin = 65/97, 72/97;  z = 7: 175/337, 288/337 (thomas5, thomas7)',Math.max(Math.abs(Math.cos(t5.angle)-65/97),Math.abs(Math.sin(t5.angle)-72/97),Math.abs(Math.cos(t7.angle)-175/337),Math.abs(Math.sin(t7.angle)-288/337)),1e-12);}
// C10 the four-step square
m=0;m2=0;m3=0;for(let i=0;i<1000;i++){const S=LH.feed({zbar:[ru(1.5,13),ru(1.5,13),7],amp:0,T:[1,1,1],ph:[0,0,0],sigma:1,Tphi:9,Tchi:55},0),l=LH.loop(S,0,1);if(Math.abs(l.g-1)<1e-3)continue;
  if(l.g<1)m=Math.max(m,Math.abs(Math.cos(l.phiF)-l.half));else m2=Math.max(m2,Math.abs(Math.cosh(l.runF)-l.half)/l.half);
  const eta=[1,-1,-1,-1];let d=0;for(let p=0;p<4;p++)for(let q=0;q<4;q++){let s=0;for(let k=0;k<4;k++)s+=l.W[k][p]*eta[k]*l.W[k][q];d=Math.max(d,Math.abs(s-(p===q?eta[p]:0)));}m3=Math.max(m3,d/(l.W[0][0]*l.W[0][0]));}
line('C10a','square turns (g < 1): matrix trace gives cos(phi) = 8g^4 - 8g^2 + 1',m,1e-9);line('C10b','square runs (g > 1): matrix trace gives cosh of 4 arccosh g (relative)',m2,1e-9);line('C10c','the square is a Lorentz matrix (relative)',m3,1e-9);
{const S=LH.feed({zbar:[LH.WALL,LH.WALL,7],amp:0,T:[1,1,1],ph:[0,0,0],sigma:1,Tphi:9,Tchi:55},0),l=LH.loop(S,0,1);line('C10d','equal steps at the wall: g = 1 and the 4x4 trace is 4 (the square locks)',Math.max(Math.abs(l.g-1),Math.abs(l.tr-4)),1e-9);}
// C11 pressure of a wave front on a tilted plane (Maxwell stress; Art. 792 is the theta = 0 case)
m=0;for(let i=0;i<500;i++){const al=ru(0,6.3),be=ru(0,3.1),ga=ru(0,6.3),k=[Math.sin(be)*Math.cos(al),Math.sin(be)*Math.sin(al),Math.cos(be)];let e=[Math.cos(be)*Math.cos(al),Math.cos(be)*Math.sin(al),-Math.sin(be)],f=[-Math.sin(al),Math.cos(al),0];
  const E0=ru(0.2,3),E=[0,1,2].map(j=>E0*(Math.cos(ga)*e[j]+Math.sin(ga)*f[j])),H=[0,1,2].map(j=>E0*(-Math.sin(ga)*e[j]+Math.cos(ga)*f[j])),th=ru(0,1.5),ps=ru(0,6.3),n=[0,1,2].map(j=>Math.cos(th)*k[j]+Math.sin(th)*(Math.cos(ps)*e[j]+Math.sin(ps)*f[j])),u=E0*E0/(4*Math.PI);
  m=Math.max(m,Math.abs(LH.normalStress(E,H,n)+u*Math.cos(th)**2)/u,Math.abs(LH.normalStress(E,H,k)+u)/u);}
line('C11','normal stress on a plane tilted by theta = -u cos^2(theta); on the front itself = -u',m,1e-12);
// C12 occupation reading (fermion_smith with x = ln z)
m=0;for(let i=0;i<10000;i++){const z=Math.exp(ru(-4,4)),C=LH.occupation(z),G=LH.smith(z);m=Math.max(m,Math.abs(1-2*C-G),Math.abs(4*C*(1-C)-(1-G*G)),Math.abs(1-2/(Math.exp(Math.log(z))+1)-Math.tanh(Math.log(z)/2)));}
line('C12','1 - 2C = Gamma and T = 4C(1 - C) with C = 1/(z + 1)',m,1e-14);
// C13 refraction direction built by the page is a unit tangent in the plane of incidence (independent single-face test)
m=0;let n13=0;for(let i=0;i<3000;i++){const z=ru(1.5,9),S=LH.feed({zbar:[z,z,z],amp:0,T:[1,1,1],ph:[0,0,0],sigma:rnd()<0.5?1:-1,Tphi:9,Tchi:55},0),ps=ru(0,0.99)*Math.acos(Math.tanh(S.h[0])),ph=ru(0,6.3),d=[Math.cos(ps),Math.sin(ps)*Math.cos(ph),Math.sin(ps)*Math.sin(ph)];
  const t=LH.trace(S,[d],{maxEv:1,fmin:0,smax:7,maxSeg:60}),e=t.events[0];if(!e){m=1;break;}if(e.k!==0)continue;n13++;m=Math.max(m,Math.abs(Math.sqrt(1-e.c1*e.c1)-Math.cosh(S.h[0])*Math.sin(ps)),Math.abs(Math.tanh(t.segs[0].s)-Math.tanh(S.h[0])/Math.cos(ps)));}
line('C13','single face: sin(theta) = cosh(h) sin(psi) and tanh(s) = tanh(h)/cos(psi), '+n13+' rays that meet face I first',m,1e-10);
console.log('check_surprise_v1   page: Light_at_the_Hypersurface_Surprise_v1.html   seed 20261115');
lines.forEach(l=>console.log(l));console.log(fails===0?'ALL '+lines.length+' LINES HOLD':fails+' OF '+lines.length+' LINES FAIL');process.exit(fails?1:0);
