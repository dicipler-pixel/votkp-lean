/* SCRIPT: votkp_mixer_v1
   VOTKP Mixer v1 — Jeromie Beasley — 7 Nov 2026
   The Volume of the Knot Potential: Decay and Direction on the Vacuum Disk.
   Built on 3D Mixer Parts v1. Every eye computes its picture live from the paper's own mathematics and data. */
(function(){
"use strict";
const M = window.Mixer3D, T = M.T, DATA = window.VOTKP_DATA;
const R = 2.4;                                   // disk radius in world units
const PI = Math.PI, SQ3 = Math.sqrt(3), V0 = 1.0149416064096536, K2 = 3*SQ3/4;

/* ---------- complex numbers ---------- */
const C = (re,im=0) => ({re,im});
const add=(a,b)=>C(a.re+b.re,a.im+b.im), sub=(a,b)=>C(a.re-b.re,a.im-b.im);
const mul=(a,b)=>C(a.re*b.re-a.im*b.im,a.re*b.im+a.im*b.re);
const div=(a,b)=>{const d=b.re*b.re+b.im*b.im; return C((a.re*b.re+a.im*b.im)/d,(a.im*b.re-a.re*b.im)/d);};
const abs=a=>Math.hypot(a.re,a.im), arg=a=>Math.atan2(a.im,a.re), conj=a=>C(a.re,-a.im);
const clog=a=>C(Math.log(abs(a)),arg(a)), cexp=a=>C(Math.exp(a.re)*Math.cos(a.im),Math.exp(a.re)*Math.sin(a.im));
const W = C(0.5, SQ3/2), Wb = conj(W), ONE = C(1,0);
const Gof = z => div(sub(z,W), sub(z,Wb));                      // the vacuum disk
const zOfG = g => div(sub(W, mul(Wb,g)), sub(ONE,g));            // inverse map

/* Bloch-Wigner dilogarithm D(z), by its symmetries into |z|<=1, Re z<=1/2, then the Bernoulli series in -log(1-z) */
const BERN=[1,-1/2,1/6,0,-1/30,0,1/42,0,-1/30,0,5/66,0,-691/2730,0,7/6,0,-3617/510,0,43867/798,0,-174611/330];
function li2small(z){ const w = C(-Math.log(abs(sub(ONE,z))), -arg(sub(ONE,z))); let s=C(0,0), p=w, f=1;
  for(let n=0;n<BERN.length;n++){ f*= (n+1); if(BERN[n]!==0) s=add(s, mul(C(BERN[n]/f,0), p)); p=mul(p,w); } return s; }
function D(z){ if(Math.abs(z.im)<1e-14) return 0; let sgn=1;
  if(abs(z)>1){ z=div(ONE,z); sgn=-sgn; }                 // D(1/z) = -D(z)
  if(z.re>0.5){ z=sub(ONE,z); sgn=-sgn; }                 // D(1-z) = -D(z)
  if(abs(z)>1){ z=div(ONE,z); sgn=-sgn; }
  const L=li2small(z); return sgn*(L.im + arg(sub(ONE,z))*Math.log(abs(z))); }

/* ---------- shared drawing helpers ---------- */
const V3=(x,y,z)=>new T.Vector3(x,y,z);
const disk = g => V3(R*g.re, 0, -R*g.im);
function ring(r, col, op, y=0, n=160){ const p=[]; for(let i=0;i<=n;i++){const a=2*PI*i/n; p.push(V3(r*Math.cos(a),y,r*Math.sin(a)));} return M.line(p,col,op); }
function diskFrame(g, withHalf){ g.add(ring(R,0x63d3ff,0.85)); for(let k=1;k<4;k++) g.add(ring(R*k/4,0x63d3ff,0.12));
  if(withHalf) g.add(ring(R*Math.SQRT1_2,0x8a9aab,0.45));
  const st=M.points(1,0.42); M.setPt(st,0,V3(0,0.01,0),[1,1,1]); M.flush(st); g.add(st);
  const l1=lab('vacuum',0xdfe7ef,0.28); l1.position.set(0.15,0.25,0.25); g.add(l1);
  const l2=lab('ground (rim)',0x63d3ff,0.28); l2.position.set(-R*0.75,0.2,-R*0.75); g.add(l2); }
const lab=(t,c,sc)=>M.label(t,typeof c==='number'?'#'+c.toString(16).padStart(6,'0'):c,sc);
const fmt=(x,n=4)=>Number.isFinite(x)?x.toFixed(n):'—';
const ramp=t=>M.colour.ramp(t);

/* ---------- the feed ---------- */
const KN = ['5_2','6_1','6_2'];
const JK = Object.keys(DATA.jones);
const feed = { params:[
  {id:'zr', label:'Shape z, real part', min:-0.6, max:1.6, step:0.01, value:0.30},
  {id:'zi', label:'Shape z, imaginary part', min:0.15, max:2.0, step:0.01, value:1.10},
  {id:'kn', label:'Knot (5_2, 6_1, 6_2)', min:0, max:2, step:1, value:1},
  {id:'jk', label:'Knot for the light string', min:0, max:JK.length-1, step:1, value:2},
  {id:'film', label:'Film thickness (nm)', min:0, max:1000, step:10, value:500},
  {id:'p', label:'Torus knot p', min:2, max:4, step:1, value:3},
  {id:'q', label:'Torus knot q', min:3, max:7, step:1, value:4}],
  build(P){ const z=C(P.zr,P.zi); return {P, z, G:Gof(z), knot:KN[P.kn], jk:JK[P.jk]}; } };

/* =========================== EYES =========================== */
const eyes=[];

/* 1. The vacuum disk and the racket */
eyes.push({ id:'disk', title:'The vacuum disk', section:'Section 2, Proposition 1', grade:'proven',
  eq:'G = (z − w)/(z − w̄),  w = e^{iπ/3}\nz → 1/(1−z):  G → e^{2πi/3} G',
  text:'Every tetrahedron of a hyperbolic knot is a point on this disk. The regular tetrahedron sits at the centre, the vacuum. Flat ones sit on the rim. Reading one tetrahedron along another edge pair turns its point by exactly 120 degrees: the axis switches, the distance and the volume stay.',
  uses:['zr','zi'], view:[0.0,1.05,7.4,0],
  make(g){ diskFrame(g,false); const tet=DATA.tet; const p=M.points(tet.length,0.11);
    tet.forEach((t,i)=>{ const G=Gof(C(t[0],t[1])); M.setPt(p,i,disk(G),[0.35,0.55,1.0]); }); M.flush(p); g.add(p);
    this.tri=M.points(3,0.34); g.add(this.tri); this.spokes=[0,1,2].map(()=>{const l=M.line([V3(),V3()],0xff6fae,0.9); g.add(l); return l;});
    this.tr=M.trail(240,0.12); g.add(this.tr); },
  enter(S){ M.clearTrail(this.tr); },
  step(dt,S,t){ const z=S.z, zs=[z, div(ONE,sub(ONE,z)), sub(ONE,div(ONE,z))];
    const spin=C(Math.cos(0.35*t),Math.sin(0.35*t));
    zs.forEach((zz,i)=>{ const G=mul(Gof(zz),spin); const P=disk(G); P.y=0.02; M.setPt(this.tri,i,P,[1,0.43,0.68]); M.setLine(this.spokes[i],[V3(0,0.02,0),P]); if(i===0) M.pushTrail(this.tr,P,[1,0.76,0.3]); });
    M.flush(this.tri); const G=Gof(z);
    return [['|G| of all three labels', fmt(abs(G),6)], ['angles (deg)', zs.map(q=>fmt(arg(Gof(q))*180/PI,1)).join(' · ')],
            ['volume D on all three', zs.map(q=>fmt(D(q),5)).join(' · ')], ['tetrahedra shown', DATA.tet.length]]; } });

/* 2. The vacuum bowl */
eyes.push({ id:'bowl', title:'Decay: the vacuum bowl', section:'Section 3, Theorem 2', grade:'derived + measured',
  eq:'D = V₀ − (3√3/4)|G|² + (√3/8)(G³+Ḡ³) + (3√3/16)|G|⁴ + …\nVol(K) ≈ Σ [V₀ − (3√3/4)|G_j|²]',
  text:'Height is the volume of a tetrahedron, computed live from the Bloch–Wigner dilogarithm over the whole disk. It is a bowl turned upside down: full at the vacuum, zero on the rim, with a three-fold ripple that is the racket. The real tetrahedra of 4–8 crossing knots sit on its surface. Summed over a knot\'s pieces, the series gives its volume to a median error of 0.076% over 12,954 knots.',
  uses:['zr','zi'], view:[0.6,0.55,8.2,0.6],
  make(g){ const N=70, s=M.surface(N,N,R,R), H=[], Cc=[]; for(let a=0;a<N;a++){ H.push([]); Cc.push([]); for(let b=0;b<N;b++){
      const x=-1+2*a/(N-1), y=-1+2*b/(N-1), r=Math.hypot(x,y); let h=0;
      if(r<0.995){ h=D(zOfG(C(x,y)))*1.6; } const c=r<0.995? ramp(h/1.65) : [0.02,0.03,0.05]; H[a].push(h); Cc[a].push(c.map(v=>v*0.55)); } }
    M.setSurface(s,H,Cc); g.add(s); g.add(ring(R,0x63d3ff,0.6));
    const tet=DATA.tet, p=M.points(tet.length,0.1); tet.forEach((t,i)=>{ const z=C(t[0],t[1]), G=Gof(z), P=disk(G); P.y=D(z)*1.6+0.03; M.setPt(p,i,P,[1,1,1]); }); M.flush(p); g.add(p);
    this.cur=M.points(1,0.36); g.add(this.cur); },
  step(dt,S){ const z=S.z, G=Gof(S.z), r2=abs(G)**2, P=disk(G); P.y=D(z)*1.6+0.05; M.setPt(this.cur,0,P,[1,0.76,0.3]); M.flush(this.cur);
    const G3=mul(mul(G,G),G).re*2, s2=V0-K2*r2, s4=s2+SQ3/8*G3+3*SQ3/16*r2*r2;
    return [['|G|² (distance² from vacuum)', fmt(r2,5)], ['D(z) exact', fmt(D(z),6)], ['bowl, quadratic', fmt(s2,6)], ['bowl + cubic + quartic', fmt(s4,6)], ['V₀ (regular tetrahedron)', fmt(V0,6)]]; } });

/* 3. Nearest the vacuum */
eyes.push({ id:'nearest', title:'Nearest the vacuum', section:'Section 4', grade:'computed 31 / 31',
  eq:'true geometry = argmin Σ |G_j|²  (= max volume)',
  text:'A knot\'s gluing equations have several solutions: its true geometry, its mirror, flat ones and others. Each solution here is a ring of glowing pieces at its own height, the solution\'s volume. The true geometry is always the one whose pieces sit nearest the vacuum. Mirrors fall outside the disk and flat solutions lie exactly on the rim.',
  uses:['kn'], view:[0.5,0.62,9.5,0.4],
  make(g){ diskFrame(g,false); this.g=g; this.pts=M.points(80,0.2); g.add(this.pts); this.lines=[]; },
  enter(S){ this.build(S); }, change(S){ this.build(S); },
  build(S){ this.lines.forEach(l=>this.g.remove(l)); this.lines=[]; const sols=DATA.sols[S.knot]; let k=0; this.info=[];
    sols.forEach(s=>{ const zs=s.z.map(q=>C(q[0],q[1])); let vol=0, s2=0; zs.forEach(z=>{vol+=D(z); s2+=abs(Gof(z))**2;});
      const h=vol*0.45, col=s.geo?[1,0.76,0.3]:(vol<0?[1,0.42,0.68]:[0.4,0.8,1]); const ring3=[];
      zs.forEach(z=>{ let G=Gof(z); const a=abs(G); if(a>1) G=mul(G,C(Math.min(a,1.6)/a,0)); const P=disk(G); P.y=h; M.setPt(this.pts,k++,P,col); ring3.push(P); });
      ring3.forEach(P=>{ const l=M.line([V3(P.x,0,P.z),P], s.geo?0xf2c14e:0x55657a, s.geo?0.9:0.35); this.g.add(l); this.lines.push(l); }); this.info.push([s2,vol,s.geo]); });
    for(;k<80;k++) M.setPt(this.pts,k,V3(0,-99,0),[0,0,0]); M.flush(this.pts); this.info.sort((a,b)=>a[0]-b[0]); },
  step(){ return [['knot', this.info?this.info.length+' solutions':'']].concat((this.info||[]).map(r=>[(r[2]?'★ true  ':'')+'Σ|G|² '+fmt(r[0],2), 'vol '+fmt(r[1],3)])); } });

/* 4. Windings carry the twist */
eyes.push({ id:'wind', title:'Direction: windings', section:'Section 5', grade:'reproduction (Neumann)',
  eq:'w₀ = log z + pπi,  w₁ = log z′ + qπi\ni(Vol + i CS) = Σ ε R(z; p, q)',
  text:'Each piece carries a phase. Its logarithm can wind round by whole half-turns, the integers p and q. The helix shows one piece\'s phase climbing by πi per winding. Volume needs none of these integers. The Chern–Simons twist is exact only with them: 454 of 454 runs with the windings, 1 of 79 without.',
  uses:['zr','zi'], view:[0.9,0.35,8.5,1.2],
  make(g){ g.add(ring(1.2,0x63d3ff,0.4)); this.hel=M.line([V3(),V3()],0xf2c14e,0.95); g.add(this.hel); this.dots=M.points(9,0.3); g.add(this.dots);
    for(let p=-2;p<=4;p++){ const l=lab('p = '+p,0x8a9aab,0.2); l.position.set(1.7,0.6*p+0.6,0); g.add(l); } },
  step(dt,S,t){ const z=S.z, L=clog(z), pts=[]; const top=Math.min(4,Math.floor(t*0.8)%7-2);
    for(let i=0;i<=600;i++){ const u=-2+6*i/600, ang=L.im+u*PI; pts.push(V3(1.2*Math.cos(ang),0.6*u+0.6,1.2*Math.sin(ang))); } M.setLine(this.hel,pts);
    for(let p=-2;p<=4;p++){ const ang=L.im+p*PI; M.setPt(this.dots,p+2,V3(1.2*Math.cos(ang),0.6*p+0.6,1.2*Math.sin(ang)), p===top?[1,0.43,0.68]:[0.4,0.8,1]); } M.flush(this.dots);
    return [['log|z|', fmt(L.re,4)], ['arg z', fmt(L.im,4)], ['highlighted winding p', top], ['CS with windings', '454 / 454 exact'], ['CS without', '1 / 79']]; } });

/* 5. Read off the drawing */
eyes.push({ id:'drawing', title:'Our polynomial, read off the drawing', section:'Section 6', grade:'computed 79 / 79',
  eq:'P_K(x) = Π_ρ (x − e^{λ V₀(ρ)})\ndecay = Im V₀ (volume),  direction = Re V₀',
  text:'The knot potential is read straight off the drawing, one variable per side and four dilogarithms per crossing. It gives one root per geometry. Here each root stands at its direction (angle round the circle) and its decay (height). The top root is the knot\'s true complex volume on 79 of 79 knots, and the whole ladder is the same from different drawings.',
  uses:['kn'], view:[0.4,0.45,9.0,0.8],
  make(g){ g.add(ring(1.8,0x63d3ff,0.5)); this.g=g; this.p=M.points(40,0.32); g.add(this.p); this.ls=[]; const l=lab('decay 0',0x8a9aab,0.22); l.position.set(1.9,0,0); g.add(l); },
  enter(S){ this.build(S); }, change(S){ this.build(S); },
  build(S){ this.ls.forEach(l=>this.g.remove(l)); this.ls=[]; const nm=S.knot, sp=DATA.spectra[nm]; let k=0;
    sp.forEach(r=>{ const ang=2*PI*r[1]/(PI*PI), P=V3(1.8*Math.cos(ang), r[0]*0.45, 1.8*Math.sin(ang)); const top=r[0]===Math.max(...sp.map(q=>q[0]));
      M.setPt(this.p,k++,P, top?[1,0.76,0.3]:(r[0]<0?[1,0.42,0.68]:[0.4,0.8,1])); const l=M.line([V3(P.x,0,P.z),P],0x55657a,0.6); this.g.add(l); this.ls.push(l); });
    for(;k<40;k++) M.setPt(this.p,k,V3(0,-99,0),[0,0,0]); M.flush(this.p); this.sp=sp; },
  step(dt,S){ return [['knot', S.knot]].concat((this.sp||[]).map(r=>['decay '+fmt(r[0],5),'direction '+fmt(r[1],4)])); } });

/* 6. Torus knots: pure direction */
function torusKnot(p,q,n=900,Ra=1.6,ra=0.6){ const pts=[]; for(let i=0;i<=n;i++){ const t=2*PI*i/n; const r=Ra+ra*Math.cos(q*t); pts.push(V3(r*Math.cos(p*t), ra*Math.sin(q*t), r*Math.sin(p*t))); } return pts; }
eyes.push({ id:'torus', title:'Torus knots: pure direction', section:'Section 6', grade:'reproduction (Kirk–Klassen)',
  eq:'decay = 0,  direction = −k²/(pq) of a turn\ncount = (p−1)(q−1)/2',
  text:'A torus knot winds evenly round a torus and makes no hyperbolic space. Every one of its roots has zero decay. What is left is direction alone, an exact rational fraction of a turn. These are the knots that chemistry builds by self-assembly.',
  uses:['p','q'], view:[0.6,0.7,7.5,0],
  make(g){ this.g=g; this.k=M.line([V3(),V3()],0x63d3ff,0.95); g.add(this.k); this.glow=M.points(900,0.06); g.add(this.glow); this.dir=M.points(12,0.3); g.add(this.dir); g.add(ring(2.6,0x55657a,0.5)); },
  enter(S){ this.build(S); }, change(S){ this.build(S); },
  build(S){ let p=S.P.p, q=S.P.q; this.pq=[p,q]; const pts=torusKnot(p,q); M.setLine(this.k,pts); pts.slice(0,900).forEach((P,i)=>M.setPt(this.glow,i,P,ramp(i/900).map(v=>v*0.7))); M.flush(this.glow);
    const key=Object.keys(DATA.torus).find(k=>DATA.torus[k][0]===p&&DATA.torus[k][1]===q); this.name=key||null;
    this.fr=key?DATA.torus[key][2]:[]; this.fr.forEach((f,i)=>M.setPt(this.dir,i,V3(2.6*Math.cos(2*PI*f),0,2.6*Math.sin(2*PI*f)),[1,0.76,0.3])); for(let i=this.fr.length;i<12;i++) M.setPt(this.dir,i,V3(0,-99,0),[0,0,0]); M.flush(this.dir); },
  step(dt,S,t){ this.g.rotation.y=0.15*t; const [p,q]=this.pq, gcd=(a,b)=>b?gcd(b,a%b):a;
    return [['T(p, q)', 'T('+p+', '+q+')'+(gcd(p,q)>1?'  (a link, not a knot)':'')+(this.name?'  = '+this.name:'')], ['expected count (p−1)(q−1)/2', (p-1)*(q-1)/2], ['directions found from the drawing', this.fr.length?this.fr.map(x=>fmt(x,4)).join(', '):'not computed'], ['decay of every root', '0']]; } });

/* 7. The light string (Jones) */
function jonesAt(K,t){ let s=C(0,0), tp=cexp(C(0,K.lo*t)); for(let i=0;i<K.c.length;i++){ s=add(s,mul(C(K.c[i],0),tp)); tp=mul(tp,cexp(C(0,t))); } return s; }
eyes.push({ id:'light', title:'Light strings: climb and turn', section:'Section 7', grade:'empirical, 2,970 knots',
  eq:'climb = mean log|V(e^{iθ})|  (carries volume, ρ = 0.854)\nturn = swept area / mean|V|²  (carries |signature|, ρ = 0.83)',
  text:'Let light run once round the circle, the way colour runs from violet to red, and follow the Jones polynomial. The string leaves V(1) = 1 and comes back. How far it climbs carries the volume beyond the determinant. The area it sweeps carries the handedness.',
  uses:['jk'], view:[0.5,0.5,8.6,0.6],
  make(g){ this.str=M.line([V3(),V3()],0xf2c14e,0.95); g.add(this.str); this.tr=M.trail(260,0.16); g.add(this.tr); g.add(ring(2.0,0x55657a,0.5,-1.2)); g.add(ring(2.0,0x55657a,0.5,1.2)); this.o=M.points(2,0.3); g.add(this.o); },
  enter(S){ this.build(S); }, change(S){ this.build(S); },
  build(S){ const K=DATA.jones[S.jk]; this.K=K; const pts=[]; let ml=0, area=0, m2=0, prev=null; const N=720; let mx=0; for(let i=0;i<N;i++) mx=Math.max(mx,abs(jonesAt(K,2*PI*i/N))); const sc=2.0/mx; this.sc=sc;
    for(let i=0;i<=N;i++){ const th=2*PI*i/N, v=jonesAt(K,th); pts.push(V3(sc*v.re, -1.2+2.4*th/(2*PI), -sc*v.im)); if(i<N){ ml+=Math.log(abs(v)+1e-12); m2+=abs(v)**2; if(prev) area+=0.5*(prev.re*v.im-prev.im*v.re); prev=v; } }
    M.setLine(this.str,pts); M.setPt(this.o,0,V3(sc,-1.2,0),[1,1,1]); M.setPt(this.o,1,V3(sc,1.2,0),[1,1,1]); M.flush(this.o); this.ml=ml/N; this.turn=area/(m2/N); M.clearTrail(this.tr); },
  step(dt,S,t){ const th=(0.5*t)%(2*PI), v=jonesAt(this.K,th); M.pushTrail(this.tr,V3(this.sc*v.re,-1.2+2.4*th/(2*PI),-this.sc*v.im),[1,0.43,0.68]);
    return [['knot', S.jk], ['volume', fmt(this.K.vol,4)], ['climb (Mahler measure)', fmt(this.ml,4)], ['signature', this.K.sig], ['turn (swept area)', fmt(this.turn,3)], ['log det', fmt(Math.log(this.K.det),4)]]; } });

/* 8. HOMFLY light lines */
eyes.push({ id:'homfly', title:'HOMFLY along its light lines', section:'Section 7', grade:'empirical, 12,955 knots',
  eq:'v = t^{−N/2},  z = t^{1/2} − t^{−1/2}\nN = 0 Alexander,  N = 2 Jones',
  text:'On a plain torus of two phases HOMFLY carries nothing. Along its sl(N) light lines it carries volume, and each higher line adds a slice the Jones line misses. Pillar height is the climb against volume; the gold cap is the share of volume explained with the determinant and Jones.',
  uses:[], view:[0.75,0.45,9,0.8],
  make(g){ const H=DATA.homfly; this.bars=[]; H.N.forEach((n,i)=>{ const h=Math.max(0.03,H.rho[i])*3, b=M.box(0.34,h,0.34, n===2?0xf2c14e:0x63d3ff, 0.55); b.position.set(-2.4+0.6*i,h/2,0); g.add(b);
      const c=M.points(1,0.3); M.setPt(c,0,V3(-2.4+0.6*i,(H.r2[i]-0.78)*40,0),[1,0.76,0.3]); M.flush(c); g.add(c);
      const l=lab('N='+n,0x8a9aab,0.22); l.position.set(-2.4+0.6*i,-0.25,0.3); g.add(l); }); g.add(M.grid(6,12,0x1f2a38,0.5)); },
  step(){ const H=DATA.homfly; return [['N = 2 (Jones) climb vs volume', H.rho[2]], ['N = 8 climb vs volume', H.rho[8]], ['R², log det + Jones', '0.795'], ['R², all lines + log det', '0.838']]; } });

/* 9. Colour on the same disk, and the film winding */
function reflN(n,k){ const N=C(n,k); return div(sub(ONE,N),add(ONE,N)); }
eyes.push({ id:'colour', title:'Colour on the same disk', section:'Section 9', grade:'measured data; film = recognised physics',
  eq:'Γ = (1 − N)/(1 + N)\nfilm:  r = (r₀₁ + r₁₂ e^{2iδ}) / (1 + r₀₁ r₁₂ e^{2iδ})',
  text:'Each element\'s reflection across the visible traces a track on the same disk, drawn in the colour it really reflects. Metals ride near the rim, which is ground; the line |Γ|² = 1/2 separates 35 of 35 metals from all 6 non-metals. A clear film adds an integer: its reflection winds round the vacuum a whole number of times, one more every 247 nm.',
  uses:['film'], view:[0.0,1.05,7.4,0],
  make(g){ diskFrame(g,true); const els=DATA.elements; this.film=M.line([V3(),V3()],0xff6fae,0.95); g.add(this.film);
    els.forEach(e=>{ const pts=e.n.map((n,i)=>disk(reflN(n,e.k[i])));
      const E=M.colour.WL.map(l=>{ const idx=Math.min(30,Math.max(0,Math.round((l-400)/10))); return abs(reflN(e.n[idx],e.k[idx]))**2; });
      const col=M.colour.norm(M.colour.spec(E)); const ln=M.line(pts,new T.Color().setRGB(col[0],col[1],col[2]),0.9); g.add(ln); }); },
  step(dt,S,t){ const e=DATA.elements.find(x=>x.el==='Al')||DATA.elements[0]; const d=S.P.film, nf=1.5, r01=(1-nf)/(1+nf), pts=[]; let wind=0, prev=null;
    for(let i=0;i<=200;i++){ const lam=380+400*i/200, idx=Math.min(30,Math.max(0,Math.round((lam-400)/10))), N=C(e.n[idx],e.k[idx]);
      const r12=div(sub(C(nf,0),N),add(C(nf,0),N)), ph=cexp(C(0,4*PI*nf*d/lam)), r=div(add(C(r01,0),mul(r12,ph)),add(ONE,mul(C(r01,0),mul(r12,ph))));
      pts.push(disk(r)); if(prev){ let da=arg(r)-arg(prev); if(da>PI) da-=2*PI; if(da<-PI) da+=2*PI; wind+=da; } prev=r; }
    M.setLine(this.film,pts); return [['film on aluminium, thickness', d+' nm'], ['windings round the vacuum (380–780 nm)', fmt(Math.abs(wind)/(2*PI),2)], ['theory 2 n d (1/380 − 1/780)', fmt(2*1.5*d*(1/380-1/780),2)], ['metals above |Γ|² = 1/2', '35 / 35']]; } });

/* 10. The electron */
eyes.push({ id:'electron', title:'The electron’s group', section:'Section 10', grade:'standard mathematics; spin lift conjectural',
  eq:'SL(2,ℂ) → PSL(2,ℂ) = Möbius maps = isometries of H³\nspin: 720° to return',
  text:'An electron\'s spin lives in two complex numbers, turned and boosted by SL(2,ℂ). Dropping the sign gives the Möbius maps, which are the Smith chart\'s own moves and the symmetries of the space a knot\'s volume lives in. The arrow returns after one turn; the spinor\'s sign needs two. That sign may be the last piece of the twist.',
  uses:[], view:[0.6,0.4,7.5,0.4],
  make(g){ this.s=M.shell(1.4,0x63d3ff,0.06); g.add(this.s); g.add(ring(1.4,0x63d3ff,0.5)); this.arrow=M.line([V3(),V3()],0xf2c14e,1); g.add(this.arrow);
    this.tip=M.points(1,0.35); g.add(this.tip); this.sign=lab('+',0xf2c14e,0.5); this.sign.position.set(-2,1.4,0); g.add(this.sign); this.tr=M.trail(200,0.12); g.add(this.tr); },
  step(dt,S,t){ const a=0.6*t, P=V3(1.4*Math.sin(1.0)*Math.cos(a),1.4*Math.cos(1.0),1.4*Math.sin(1.0)*Math.sin(a)); M.setLine(this.arrow,[V3(),P]); M.setPt(this.tip,0,P,[1,0.76,0.3]); M.flush(this.tip); M.pushTrail(this.tr,P,[0.4,0.8,1]);
    const turns=a/(2*PI), sgn=Math.floor(turns)%2===0?'+':'−'; if(this.sign.userData.s!==sgn){ this.g=this.sign.parent; this.g.remove(this.sign); this.sign=lab('spinor sign '+sgn,sgn==='+'?0xf2c14e:0xff6fae,0.42); this.sign.position.set(-2,1.6,0); this.g.add(this.sign); this.sign.userData.s=sgn; }
    return [['turns of the arrow', fmt(turns,2)], ['spinor sign', sgn], ['CS exact modulo', 'π²/2 (π²: open)']]; } });

/* 11. Knots that build themselves */
eyes.push({ id:'self', title:'Knots that build themselves', section:'Section 11', grade:'observed, 5 of 6',
  eq:'privileged: 3_1, 4_1, 5_1, 8_19, 10_124, 15n_41185\ntorus knots: T(2,3) T(2,5) T(3,4) T(3,5) T(4,5)',
  text:'Molecular knots that self-assemble are, with one exception, torus knots: knots that make no space. Shown are T(2,3), T(2,5), T(3,4), T(3,5) and T(4,5). The exception, the figure-eight, has the smallest volume of any hyperbolic knot.',
  uses:[], view:[0.4,0.75,11,0],
  make(g){ const list=[[2,3],[2,5],[3,4],[3,5],[4,5]], cols=[0x63d3ff,0xf2c14e,0xff6fae,0x8fe388,0xc7a2ff]; this.ks=[];
    list.forEach((pq,i)=>{ const k=new T.Group(); k.add(M.line(torusKnot(pq[0],pq[1],900,0.9,0.32),cols[i],0.95)); const a=2*PI*i/5; k.position.set(2.6*Math.cos(a),0,2.6*Math.sin(a));
      const l=lab('T('+pq[0]+','+pq[1]+')',cols[i],0.24); l.position.set(0,1.0,0); k.add(l); g.add(k); this.ks.push(k); }); },
  step(dt,S,t){ this.ks.forEach((k,i)=>{ k.rotation.y=0.4*t+i; k.rotation.x=0.3*Math.sin(0.3*t+i); });
    return [['self-assembling knots that are torus knots', '5 of 6'], ['their hyperbolic volume', '0'], ['the exception, 4_1, volume', '2.02988']]; } });

M.run({ title:'VOTKP', byline:'Jeromie Beasley · Decay and Direction on the Vacuum Disk · v1 · 7 Nov 2026',
  note:'every eye computes from the paper’s data', feed, eyes,
  film:['disk','bowl','nearest','wind','drawing','torus','light','homfly','colour','electron','self'] });
})();
