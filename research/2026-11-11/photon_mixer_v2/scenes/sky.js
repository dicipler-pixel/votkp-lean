/* SCRIPT: PHOTON-MIXER-V2-SCENE-SKY */
(function(){
"use strict";
const PHX = window.PHX, { M, T, K, V3, f, sci, TAU, hue, lamRGB, lamName, cloud, clearCloud, fill, ringLine, LE } = PHX;
/* ---------- geometry: real Earth and real air for every number; drawn with the air six times thicker relative to the Earth ---------- */
const RE = 6371, H = 8, ZTOP = 100;                 /* km: Earth radius, Rayleigh scale height, top of the computed air */
const RD = 30, EX = 6, HD = RD*EX*H/RE;              /* drawn Earth radius (units), thickness factor, drawn scale height (0.226) */
const ZDTOP = 8*HD;                                  /* drawn air up to 8 scale heights (64 km) */
const XOFF = 2.2;                                    /* drawn x of the observer */
const NB = 36000, NS = 70000, NG = 18000;
/* drawn position at Earth-central angles (ax, az) and drawn height zd; true angles, so the Sun's elevation is drawn as it is */
function drawn(ax, az, zd){ const r = RD + zd, nx = Math.tan(ax), nz = Math.tan(az), L = Math.hypot(nx, 1, nz);
  return [XOFF + r*nx/L, r/L - RD, r*nz/L]; }
const realZ = zd => zd/HD*H;                          /* a drawn point stands for the real air at the same number of scale heights */
/* ---------- air between a point and the Sun: X(z, χ) in units of the vertical column from sea level ---------- */
const ZG = [], CG = []; for(let i=0;i<48;i++) ZG.push(ZTOP*(i/47)**2); for(let j=0;j<=180;j++) CG.push(110*j/180);
const XT = (() => { const t = new Float64Array(ZG.length*CG.length);
  for(let i=0;i<ZG.length;i++) for(let j=0;j<CG.length;j++){ const r0 = RE + ZG[i], ch = CG[j]*Math.PI/180, mu = Math.cos(ch);
    if(ch > Math.PI/2 && r0*Math.sin(ch) < RE){ t[i*CG.length+j] = Infinity; continue; }          /* ray to the Sun hits the Earth: shadow */
    const rt = RE + ZTOP, Lm = -r0*mu + Math.sqrt(Math.max(0, rt*rt - r0*r0*(1 - mu*mu)));     /* path to the top of the air */
    const n = 600, dt = Lm/n; let s = 0;
    for(let k=0;k<=n;k++){ const tt = k*dt, z = Math.sqrt(r0*r0 + tt*tt + 2*r0*tt*mu) - RE, w = (k===0||k===n) ? 1 : (k&1 ? 4 : 2); s += w*Math.exp(-z/H); }
    t[i*CG.length+j] = s*dt/3/H; }
  return t; })();
function Xair(z, chiDeg){ if(chiDeg >= 110) return Infinity;
  let a = 0; while(a < ZG.length-2 && ZG[a+1] < z) a++; const fa = Math.max(0, Math.min(1, (z - ZG[a])/(ZG[a+1] - ZG[a])));
  const bj = chiDeg/110*180, b = Math.min(179, Math.max(0, Math.floor(bj))), fb = bj - b, nc = CG.length;
  const v = [XT[a*nc+b], XT[a*nc+b+1], XT[(a+1)*nc+b], XT[(a+1)*nc+b+1]]; if(v.some(x => !isFinite(x))) return Infinity;
  const L = v.map(Math.log); return Math.exp((L[0]*(1-fb) + L[1]*fb)*(1-fa) + (L[2]*(1-fb) + L[3]*fb)*fa); }
/* ---------- colour of sunlight after air X: transmitted Planck(5772 K)·e^{−τX}, and the Rayleigh-scattered part Planck·τ·e^{−τX} ---------- */
const WL = M.colour.WL, PL = WL.map(l => K.planck(l, K.T_SUN)), TAUL = WL.map(l => K.tauRayleigh(l));
const NX = 400, XMAX = 120, xOf = k => XMAX*(k/(NX-1))**2;
const LUT = (() => { const tr = [], sc = []; let l0t = 0, l0s = 0;
  for(let k=0;k<NX;k++){ const X = xOf(k), a = M.colour.spec(PL.map((p,i) => p*Math.exp(-TAUL[i]*X))), b = M.colour.spec(PL.map((p,i) => p*TAUL[i]*Math.exp(-TAUL[i]*X)));
    if(k===0){ l0t = M.colour.lum(a); l0s = M.colour.lum(b); }
    tr.push([...M.colour.norm(a), M.colour.lum(a)/l0t]); sc.push([...M.colour.norm(b), M.colour.lum(b)/l0s]); }
  return { tr, sc }; })();
/* photons per second on a face: Planck(5772 K) scaled to 1361 W/m² at the top of the air, times Rayleigh transmission, counted per photon (250–5000 nm) */
const FACE = 0.03, S0 = 1361, HC = 1.98644586e-25;
const FL = []; for(let l=250;l<=5000;l+=5) FL.push(l);
const FP = FL.map(l => K.planck(l, K.T_SUN)), FN = S0/FP.reduce((a,b) => a+b*5, 0);    /* W m⁻² nm⁻¹ per Planck unit */
function faceCount(X){ let E = 0, n = 0; for(let i=0;i<FL.length;i++){ const e = FN*FP[i]*Math.exp(-K.tauRayleigh(FL[i])*X)*5; E += e; n += e/(HC/(FL[i]*1e-9)); }
  return { E, n: n*FACE, mean: E/n/1.602176634e-19 }; }
const look = (tab, X) => { if(!isFinite(X) || X > XMAX) return null; return tab[Math.min(NX-1, Math.round(Math.sqrt(X/XMAX)*(NX-1)))]; };

/* 8 ---------- sunlight through the atmosphere: the computed colour of the low Sun ---------- */
PHX.add({ id:'sky', section:'VIII · Into the sunset', grade:'standard physics, recomputed', title:'Why the low Sun turns red',
  eq:'transmitted = Planck(5772 K) × exp(−τ_R(λ) X),   τ_R ∝ λ⁻⁴\nX = airmass at elevation h',
  text:'Earth’s limb with its air drawn as a cloud whose density falls off with height (the air is drawn six times thicker than scale; every colour is computed for the real air). The Sun’s direct beam comes in at the true elevation and ends at an observer on the ground; each point of the beam carries the colour of the sunlight that is left after the air it has crossed so far. The faint glow is the light scattered out of sunlight everywhere in the air, bluish because short wavelengths scatter most. The lower the Sun, the longer the path, and the beam that reaches the ground turns orange and then red. Every colour seen is light that has been absorbed; even so, about 10²⁰ solar photons reach a face each second.',
  uses:['elev'], view:[0.0,0.34,8.0,0.75],
  make(G, st){
    this.b = cloud(NB, 0.036); G.add(this.b); this.sc = cloud(NS, 0.032); G.add(this.sc); this.g = cloud(NG, 0.03); G.add(this.g);
    /* air: Earth-central angles uniform over the cap, height from the exponential profile (point density ∝ air density) */
    const sa = this.sc.geometry.attributes.position, cut = 1 - Math.exp(-ZDTOP/HD); this.sp = new Float32Array(NS*3);
    for(let i=0;i<NS;i++){ const ax = -0.4 + 0.52*Math.random(), az = -0.07 + 0.14*Math.random(), z = -HD*Math.log(1 - cut*Math.random());
      this.sp[3*i] = ax; this.sp[3*i+1] = az; this.sp[3*i+2] = z; const p = drawn(ax, az, z); sa.setXYZ(i, p[0], p[1], p[2]); }
    sa.needsUpdate = true;
    const ga = this.g.geometry.attributes.position; this.gp = new Float32Array(NG*2);
    for(let i=0;i<NG;i++){ const ax = -0.4 + 0.52*Math.random(), az = -0.07 + 0.14*Math.random(); this.gp[2*i] = ax; this.gp[2*i+1] = az; const p = drawn(ax, az, 0); ga.setXYZ(i, p[0], p[1], p[2]); }
    ga.needsUpdate = true;
    /* guides: the ground and the top of the drawn air along the beam's great circle */
    const arc = zd => { const pts = []; for(let i=0;i<=200;i++){ const p = drawn(-0.4 + 0.52*i/200, 0, zd); pts.push(V3(p[0], p[1], p[2])); } return pts; };
    G.add(M.line(arc(0), 0x8fa6bf, 0.45)); G.add(M.line(arc(ZDTOP), 0x63d3ff, 0.12));
    this.bs = new Float32Array(NB); this.bc = new Float32Array(NB*3);
    this.hz = M.line([V3(XOFF-2.2,0,0), V3(XOFF+0.6,0,0)], 0xffffff, 0.35); G.add(this.hz);
    const lo = M.label('observer', '#ffffff', 0.24); lo.position.set(XOFF+0.25, -0.28, 0); G.add(lo);
    this.lx = M.label('air drawn 6× thicker', '#63d3ff', 0.22); G.add(this.lx);
    this.key = ''; this.t = 0; },
  enter(){ PHX.base(); PHX.S3.world.rotation.set(0,0,0); this.key = ''; this.t = 0; },
  rebuild(S){ const h = S.elev, hg = Math.max(h, 0.2)*Math.PI/180, sx = -Math.cos(hg), sy = Math.sin(hg);   /* unit vector toward the Sun at the observer */
    const Xkey = K.airmass(h), Xg = Xair(0, 90 - Math.max(h, 0.2)), kx = Xkey/Xg;   /* scale the geometric column to the Kasten–Young airmass */
    /* the beam: a straight ray from the observer back toward the Sun at the true elevation; at each point the air still ahead of it toward the Sun
       is the real X at the same scale-height level and the same local zenith angle */
    const path = []; let d = 0;
    for(;;){ const px = d*sx, py = RD + d*sy, r = Math.hypot(px, py), zd = r - RD, chi = Math.acos(Math.max(-1, Math.min(1, (px*sx + py*sy)/r)))*180/Math.PI;
      path.push([drawn(Math.atan2(px, py), 0, zd), Xair(realZ(Math.min(zd, ZDTOP)), chi)*kx]); if(zd >= ZDTOP) break; d += Math.max(0.01, Math.min(0.25, zd*0.5 + 0.02)); }
    path.reverse();   /* from the top of the air down to the observer */
    const p0 = path[0][0], ux = sx, uy = sy, un = 1, OUT = 2.5;   /* the drawing keeps true angles, so the drawn ray is straight along the Sun direction */
    path.unshift([[p0[0] + ux/un*OUT, p0[1] + uy/un*OUT, 0], 0]);   /* above the air: free flight, nothing removed */
    const cum = [0]; for(let k=1;k<path.length;k++){ const a = path[k-1][0], b = path[k][0]; cum.push(cum[k-1] + Math.hypot(b[0]-a[0], b[1]-a[1])); }
    const Ltot = cum[cum.length-1], ba = this.b.geometry.attributes.position; let k = 0;
    for(let i=0;i<NB;i++){ const s = Ltot*Math.random(); while(k > 0 && cum[k] > s) k--; while(k < cum.length-2 && cum[k+1] < s) k++;
      const fr = (s - cum[k])/Math.max(1e-9, cum[k+1] - cum[k]), A = path[k], B = path[k+1];
      const x = A[0][0] + fr*(B[0][0]-A[0][0]), y = A[0][1] + fr*(B[0][1]-A[0][1]), X = A[1] + fr*(B[1]-A[1]);
      const rr = 0.035*Math.sqrt(-2*Math.log(Math.random()+1e-9)), an = TAU*Math.random(), c = look(LUT.tr, X) || [0,0,0,0];
      ba.setXYZ(i, x + rr*Math.cos(an)*uy/un, y - rr*Math.cos(an)*ux/un, rr*Math.sin(an)); this.bs[i] = s;
      const br = 0.3*(0.35 + 0.65*c[3]); this.bc[3*i] = c[0]*br; this.bc[3*i+1] = c[1]*br; this.bc[3*i+2] = c[2]*br; }
    ba.needsUpdate = true; this.Ltot = Ltot;
    /* scattered light and ground: each point lit by the Sun through its own column of air (parallel rays, Earth's shadow included) */
    const sxv = -Math.cos(h*Math.PI/180), syv = Math.sin(h*Math.PI/180), sc = this.sc.geometry.attributes.color, gc = this.g.geometry.attributes.color;
    const chiAt = (ax, az) => { const nx = Math.tan(ax), nz = Math.tan(az), L = Math.hypot(nx, 1, nz); return Math.acos((nx*sxv + syv)/L)*180/Math.PI; };
    for(let i=0;i<NS;i++){ const ax = this.sp[3*i], az = this.sp[3*i+1], z = this.sp[3*i+2], c = look(LUT.sc, Xair(realZ(z), chiAt(ax, az)));
      const w = c ? 0.3*c[3] : 0; sc.setXYZ(i, c ? c[0]*w : 0, c ? c[1]*w : 0, c ? c[2]*w : 0); }
    for(let i=0;i<NG;i++){ const ax = this.gp[2*i], az = this.gp[2*i+1], chi = chiAt(ax, az), c = look(LUT.tr, Xair(0, chi)), cz = Math.max(0, Math.cos(chi*Math.PI/180));
      const w = c ? 0.32*c[3]*cz : 0; gc.setXYZ(i, (c ? c[0]*w : 0) + 0.025, (c ? c[1]*w : 0) + 0.028, (c ? c[2]*w : 0) + 0.035); }
    sc.needsUpdate = gc.needsUpdate = true;
    this.lx.position.set(XOFF - 0.6, ZDTOP + 0.22, 0);
    const X = Xkey, T450 = Math.exp(-K.tauRayleigh(450)*X), T650 = Math.exp(-K.tauRayleigh(650)*X), cg = look(LUT.tr, X), fc = faceCount(X);
    this.rows = [['Sun elevation', f(h,1)+'°'], ['airmass X', f(X,2)], ['transmitted at 450 nm', f(100*T450,1)+' %'], ['transmitted at 650 nm', f(100*T650,1)+' %'],
      ['visible luminance left', f(100*(cg ? cg[3] : 0),1)+' %'], ['ground colour of the beam', M.colour.hex(M.colour.norm(M.colour.spec(K.sunSpectrum(h, WL))))],
      ['sunlight on a face toward the Sun', f(fc.E,0)+' W/m² (Rayleigh only, clear air)'], ['photons per second on a face', sci(fc.n,2)+'  (area 0.03 m², mean '+f(fc.mean,2)+' eV)'],
      ['colour', 'beam: transmitted sunlight · haze: scattered light'], ['drawing', 'air 6× thicker than scale; numbers for the real air (H = 8 km)']]; },
  step(dt, S){ this.t += dt; if(this.key !== S.key){ this.key = S.key; this.rebuild(S); }
    /* light moving down the beam: a travelling brightness modulation on the computed colours */
    const ca = this.b.geometry.attributes.color.array, bs = this.bs, bc = this.bc, ph = this.t*1.4;
    for(let i=0, j=0;i<NB;i++, j+=3){ const m = 0.7 + 0.3*Math.cos(bs[i]*3.2 - ph); ca[j] = bc[j]*m; ca[j+1] = bc[j+1]*m; ca[j+2] = bc[j+2]*m; }
    this.b.geometry.attributes.color.needsUpdate = true;
    const V = PHX.S3.view; if(V.auto) V.yaw = 0.32*Math.sin(this.t*0.09);
    return this.rows; }});


})();
