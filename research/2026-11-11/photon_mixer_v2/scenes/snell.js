/* SCRIPT: PHOTON-MIXER-V2-SCENE-SNELL */
(function(){
"use strict";
const PHX = window.PHX, { M, T, K, V3, f, sci, TAU, hue, lamRGB, lamName, cloud, clearCloud, fill, ringLine, LE } = PHX;
/* 3 ---------- a finite (Gaussian) beam in glass meeting a thin air gap before a second glass block, s polarisation ----------
   The beam is an angular spectrum of plane waves (Gaussian amplitude over angle). Each plane wave is matched exactly across
   glass | air gap of width d | glass, so refraction, reflection, total internal reflection, the evanescent field in the gap and
   the light that tunnels across it (frustrated total internal reflection) all come from the same sum.
   Upper glass y > 0, gap -d < y < 0, lower glass y < -d. Scene units: the vacuum wavelength is drawn as 0.45 (lam/550),
   so 1 nm = 0.45/550 units at every wavelength; the gap is a fixed 200 nm. The disc shows the computed reflection
   coefficient r of a single glass–air face, for s and p polarisation, on the unit disc. */
const NPT = 150000, NGL = 30000, NEV = 40000;
const GX0 = -4, GX1 = 4, GY0 = -2.3, GY1 = 3.1, GZ = 1.4, W0 = 1.0, NA = 49, L0 = 0.45, DGAP_NM = 200, DG = DGAP_NM*0.45/550;
/* small complex arithmetic */
const cadd = (a,b) => [a[0]+b[0], a[1]+b[1]], csub = (a,b) => [a[0]-b[0], a[1]-b[1]], cmul = (a,b) => [a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]];
const cdiv = (a,b) => { const d = b[0]*b[0]+b[1]*b[1]; return [(a[0]*b[0]+a[1]*b[1])/d, (a[1]*b[0]-a[0]*b[1])/d]; };
const cexp = a => { const g = Math.exp(a[0]); return [g*Math.cos(a[1]), g*Math.sin(a[1])]; };
const csc = (a,s) => [a[0]*s, a[1]*s];
/* normal wavevector component in air (units of k0) for tangential n1 sin(a): real, or +i kappa past the critical angle */
const qAir = (n1, a) => { const q = 1 - Math.pow(n1*Math.sin(a), 2); return q >= 0 ? [Math.sqrt(q), 0] : [0, Math.sqrt(-q)]; };
/* single glass→air face: r_s = (q1 − q2)/(q1 + q2), r_p = (n2² q1 − n1² q2)/(n2² q1 + n1² q2), q in units of k0 */
function rFace(n1, a){ const q1 = [n1*Math.cos(a), 0], q2 = qAir(n1, a);
  return { s: cdiv(csub(q1,q2), cadd(q1,q2)), p: cdiv(csub(q1, csc(q2, n1*n1)), cadd(q1, csc(q2, n1*n1))) }; }
/* the three-layer stack for one plane wave, s polarisation: returns r, gap amplitudes A, B and t */
function stack(n1, a, k0, d){ const q1 = [n1*k0*Math.cos(a), 0], q2 = csc(qAir(n1, a), k0);
  const r12 = cdiv(csub(q1,q2), cadd(q1,q2)), e2 = cexp(cmul([0,2*d], q2));
  const r = cdiv(cmul(r12, csub([1,0], e2)), csub([1,0], cmul(cmul(r12,r12), e2)));
  const op = cadd([1,0], r), qr = cdiv(cmul(q1, csub([1,0], r)), q2), A = csc(cadd(op, qr), 0.5), B = csc(csub(op, qr), 0.5);
  const t = cadd(cmul(A, cexp(cmul([0,d], q2))), cmul(B, cexp(cmul([0,-d], q2))));
  return { q1: q1[0], q2, r, A, B, t }; }

PHX.add({ id:'snell', section:'III · Bent at the glass', grade:'standard physics, recomputed', title:'The field at a glass–air boundary',
  sub:'A light beam in glass meets a 200 nm air gap: bent, totally reflected, or tunnelling across',
  eq:'n₁ sin θ₁ = n₂ sin θ₂,   r_s = (n₁cosθ₁ − n₂cosθ₂)/(n₁cosθ₁ + n₂cosθ₂)\npast θc: field in the gap ∝ exp(−|y|/δ),  δ = λ / 2π√(n₁²sin²θ₁ − n₂²)\nacross a gap d the tunnelled amplitude falls roughly as exp(−d/δ)',
  text:'A light beam in glass meets a 200 nm air gap before a second block. Points follow the computed intensity |E|², built plane wave by plane wave with exact boundary matching; colour is the phase, so the bands are wavefronts. Below the critical angle the beam bends and crosses. Past it, one face alone would reflect everything and lock the light in the glass; here the evanescent field fades exponentially across the gap and a weaker beam tunnels into the second block (frustrated total internal reflection). The disc plots the reflection coefficient r of one glass–air face: on the rim under total reflection, at the centre for p light at Brewster’s angle.',
  uses:['th','n1','lam'], view:[0.06,0.02,13.5,0.45],
  make(G, st){ this.G = G; G.position.x = -1.55;
    this.c = cloud(NPT, 0.03); G.add(this.c); this.ph = new Float32Array(NPT); this.br = new Float32Array(NPT);
    /* points in the gap go to their own cloud with larger sprites, so the thin evanescent layer reads at this distance */
    this.ev = cloud(NEV, 0.05); G.add(this.ev); this.eph = new Float32Array(NEV); this.ebr = new Float32Array(NEV);
    /* the two glass blocks: faint uniform point clouds plus their edges */
    this.gl = cloud(NGL, 0.018); G.add(this.gl); const ga = this.gl.geometry.attributes;
    const hu = GY1, hl = -DG - GY0;
    for(let i=0;i<NGL;i++){ const x = GX0 + Math.random()*(GX1-GX0), z = (2*Math.random()-1)*GZ; const up = Math.random() < hu/(hu+hl);
      const y = up ? Math.random()*hu : -DG - Math.random()*hl; ga.position.setXYZ(i,x,y,z); ga.color.setXYZ(i,0.07,0.11,0.17); }
    ga.position.needsUpdate = ga.color.needsUpdate = true;
    const boxEdges = (y0, y1, opB, opT) => { const c = [[GX0,-GZ],[GX1,-GZ],[GX1,GZ],[GX0,GZ]];
      for(let i=0;i<4;i++){ const a = c[i], b = c[(i+1)%4];
        G.add(M.line([V3(a[0],y0,a[1]),V3(b[0],y0,b[1])], 0x63d3ff, opB)); G.add(M.line([V3(a[0],y1,a[1]),V3(b[0],y1,b[1])], 0x63d3ff, opT)); G.add(M.line([V3(a[0],y0,a[1]),V3(a[0],y1,a[1])], 0x63d3ff, 0.14)); } };
    boxEdges(0, GY1, 0.45, 0.14); boxEdges(-DG, GY0, 0.45, 0.14);
    this.normal = M.line([V3(0,GY0,0),V3(0,GY1,0)], 0xffffff, 0.16); G.add(this.normal);
    this.rayI = M.line([V3(),V3()], 0xffffff, 0.2); G.add(this.rayI); this.rayR = M.line([V3(),V3()], 0xffffff, 0.2); G.add(this.rayR); this.rayT = M.line([V3(),V3()], 0xffffff, 0.2); G.add(this.rayT);
    const lg = M.label('glass', '#8fc7ff', 0.28); lg.position.set(GX0+0.35, GY1+0.25, -GZ); G.add(lg);
    const la = M.label('air gap 200 nm', '#8a9aab', 0.24); la.position.set(GX0+1.0, -0.42, GZ); G.add(la);
    const l2 = M.label('glass', '#8fc7ff', 0.28); l2.position.set(GX0+0.35, GY0-0.25, -GZ); G.add(l2);
    /* the reflection-coefficient disc: unit circle, axes, the loci of r_s and r_p over all angles, and the current points */
    const D = new T.Group(); this.disc = D; D.position.set(GX1+2.05, 1.0, 0); G.add(D); const RD = 1.2; this.RD = RD;
    const circ = []; for(let i=0;i<=180;i++){ const a = TAU*i/180; circ.push(V3(RD*Math.cos(a), RD*Math.sin(a), 0)); } D.add(M.line(circ, 0xffffff, 0.55));
    D.add(M.line([V3(-RD,0,0),V3(RD,0,0)], 0xffffff, 0.15)); D.add(M.line([V3(0,-RD,0),V3(0,RD,0)], 0xffffff, 0.15));
    const fillD = cloud(5000, 0.02); D.add(fillD); const fa = fillD.geometry.attributes;
    for(let i=0;i<5000;i++){ const rr = RD*Math.sqrt(Math.random()), a = TAU*Math.random(); fa.position.setXYZ(i, rr*Math.cos(a), rr*Math.sin(a), 0); fa.color.setXYZ(i, 0.04,0.06,0.09); }
    fa.position.needsUpdate = fa.color.needsUpdate = true;
    this.locS = M.line([V3(),V3()], 0x63d3ff, 0.5); D.add(this.locS); this.locP = M.line([V3(),V3()], 0xf2c14e, 0.5); D.add(this.locP);
    this.dotS = cloud(500, 0.035); D.add(this.dotS); this.dotP = cloud(500, 0.035); D.add(this.dotP);
    const lr = M.label('reflection coefficient r', '#dfe7ef', 0.3); lr.position.set(0, RD+0.32, 0); D.add(lr);
    const ls = M.label('r_s', '#63d3ff', 0.32); ls.position.set(-RD+0.05, -RD-0.25, 0); D.add(ls);
    const lp = M.label('r_p', '#f2c14e', 0.32); lp.position.set(-RD+0.6, -RD-0.25, 0); D.add(lp);
    const lrim = M.label('rim: |r| = 1', '#8a9aab', 0.26); lrim.position.set(RD*0.55, -RD-0.25, 0); D.add(lrim);
    this.lev = M.label('evanescent field in the gap', '#63d3ff', 0.24); this.lev.position.set(GX0+1.25, -0.78, GZ); G.add(this.lev);
    this.key = ''; this.t = 0; this.tc = 9; this.n = 0; this.ne = 0; },
  enter(){ PHX.base(); PHX.S3.world.rotation.set(0,0,0); this.key = ''; this.tc = 9; },
  blob(p, x, y, c){ const a = p.geometry.attributes, n = a.position.count;
    for(let i=0;i<n;i++){ const s = 0.035*Math.sqrt(-2*Math.log(Math.random()+1e-9)), u = TAU*Math.random(); a.position.setXYZ(i, x + s*Math.cos(u), y + s*Math.sin(u), 0.01); a.color.setXYZ(i, c[0], c[1], c[2]); }
    a.position.needsUpdate = a.color.needsUpdate = true; },
  compute(S){
    const n1 = S.n1, th = S.th, l0 = L0*(S.lam/550), k0 = TAU/l0, k1 = n1*k0, d = DG;
    const h = Math.min(0.03, l0/n1/7), nx = Math.ceil((GX1-GX0)/h)+1, ny = Math.ceil((GY1-GY0)/h)+1;
    /* angular spectrum: component at angle a = th + dd, amplitude exp(-(k1 w0 dd / 2)^2) gives a waist w0 at the origin */
    const dmax = 6/(k1*W0), comp = [];
    for(let j=0;j<NA;j++){ const dd = -dmax + 2*dmax*j/(NA-1), a = th + dd; if(Math.abs(a) >= Math.PI/2 - 1e-3) continue;
      const st = stack(n1, a, k0, d); st.A0 = Math.exp(-Math.pow(k1*W0*dd/2, 2)); st.kx = k1*Math.sin(a); comp.push(st); }
    let A0 = 0; comp.forEach(c => A0 += c.A0);
    const re = new Float32Array(nx*ny), im = new Float32Array(nx*ny), exr = new Float32Array(nx), exi = new Float32Array(nx);
    for(const c of comp){
      for(let ix=0;ix<nx;ix++){ const x = GX0 + ix*h, p = c.kx*x; exr[ix] = c.A0*Math.cos(p)/A0; exi[ix] = c.A0*Math.sin(p)/A0; }
      for(let iy=0;iy<ny;iy++){ const y = GY0 + iy*h; let Y;
        if(y >= 0) Y = cadd(cexp([0, -c.q1*y]), cmul(c.r, cexp([0, c.q1*y])));                                 /* incident + reflected */
        else if(y > -d) Y = cadd(cmul(c.A, cexp(cmul([0,-y], c.q2))), cmul(c.B, cexp(cmul([0,y], c.q2))));    /* in the gap */
        else Y = cmul(c.t, cexp([0, -c.q1*(y+d)]));                                                              /* onward in the second block */
        const o = iy*nx; for(let ix=0;ix<nx;ix++){ re[o+ix] += exr[ix]*Y[0] - exi[ix]*Y[1]; im[o+ix] += exr[ix]*Y[1] + exi[ix]*Y[0]; } } }
    /* sample points from |E|^2 via the cumulative distribution over grid cells */
    const N = nx*ny, cdf = new Float64Array(N); let s = 0, Imax = 0;
    for(let i=0;i<N;i++){ const I = re[i]*re[i] + im[i]*im[i]; if(I > Imax) Imax = I; s += I; cdf[i] = s; }
    const a = this.c.geometry.attributes, ea = this.ev.geometry.attributes, sz = 0.2;   /* thin in z (a light sheet) so the wavefront sheets stay legible */
    const bil = (arr, fx, fy) => { const ix = Math.min(nx-2, Math.floor(fx)), iy = Math.min(ny-2, Math.floor(fy)), u = fx-ix, v = fy-iy, o = iy*nx+ix;
      return arr[o]*(1-u)*(1-v) + arr[o+1]*u*(1-v) + arr[o+nx]*(1-u)*v + arr[o+nx+1]*u*v; };
    const region = y => y >= 0 ? 0 : y > -d ? 1 : 2;
    let k = 0, ke = 0, tries = 0;
    while(k < NPT && tries < 3*NPT){ tries++; const R = Math.random()*s; let lo = 0, hi = N-1; while(lo < hi){ const m = (lo+hi) >> 1; if(cdf[m] < R) lo = m+1; else hi = m; }
      const iy = Math.floor(lo/nx), ix = lo - iy*nx; const fx = Math.max(0, Math.min(nx-1.001, ix + Math.random() - 0.5)); let fy = Math.max(0, Math.min(ny-1.001, iy + Math.random() - 0.5));
      if(region(GY0 + fy*h) !== region(GY0 + iy*h)) fy = iy;   /* keep each point in its own layer */
      let z = sz*Math.sqrt(-2*Math.log(Math.random()+1e-12))*Math.cos(TAU*Math.random()); if(Math.abs(z) > GZ) z = (2*Math.random()-1)*sz;
      const er = bil(re, fx, fy), ei = bil(im, fx, fy), I = er*er + ei*ei, x = GX0 + fx*h, y = GY0 + fy*h, b = 0.38 + 0.5*Math.sqrt(I/Imax);
      if(region(y) === 1){ if(ke < NEV){ ea.position.setXYZ(ke, x, y, z); this.eph[ke] = Math.atan2(ei, er); this.ebr[ke] = b; ke++; } }
      else { a.position.setXYZ(k, x, y, z); this.ph[k] = Math.atan2(ei, er); this.br[k] = b; k++; } }
    for(let i=k;i<NPT;i++) a.color.setXYZ(i,0,0,0); for(let i=ke;i<NEV;i++) ea.color.setXYZ(i,0,0,0);
    a.position.needsUpdate = ea.position.needsUpdate = a.color.needsUpdate = ea.color.needsUpdate = true; this.n = k; this.ne = ke;
    /* guide rays along the beam axes */
    const si = Math.sin(th), ci = Math.cos(th), L = Math.min(GY1/Math.max(ci,1e-3), (GX1-0.05)/Math.max(si,1e-3), 6);
    M.setLine(this.rayI, [V3(-L*si, L*ci, 0), V3(0,0,0)]); M.setLine(this.rayR, [V3(0,0,0), V3(L*si, L*ci, 0)]);
    const lb = Math.min((-DG-GY0)/Math.max(ci,1e-3), (GX1-0.05)/Math.max(si,1e-3)); M.setLine(this.rayT, [V3(0,-d,0), V3(lb*si, -d - lb*ci, 0)]);
    this.lev.visible = !!S.sn.tir;
    /* central plane wave: the stack, and a single face */
    const c0 = stack(n1, th, k0, d); this.Rst = c0.r[0]*c0.r[0] + c0.r[1]*c0.r[1]; this.Tst = c0.t[0]*c0.t[0] + c0.t[1]*c0.t[1];
    const rf = rFace(n1, th); this.rf = rf;
    /* disc: loci over all angles for this glass, and the current points */
    const RD = this.RD, ls = [], lp = [];
    for(let i=0;i<=356;i++){ const a = i*0.25*Math.PI/180, q = rFace(n1, a); ls.push(V3(RD*q.s[0], RD*q.s[1], 0)); lp.push(V3(RD*q.p[0], RD*q.p[1], 0)); }
    M.setLine(this.locS, ls); M.setLine(this.locP, lp);
    this.blob(this.dotS, RD*rf.s[0], RD*rf.s[1], [0.25,0.7,0.95]); this.blob(this.dotP, RD*rf.p[0], RD*rf.p[1], [0.95,0.7,0.25]);
    this.w0l = W0/l0; },
  step(dt, S){ this.t += dt; this.tc += dt;
    if(this.key !== S.key && this.tc > 0.2){ this.key = S.key; this.tc = 0; this.compute(S); }
    this.disc.lookAt(PHX.S3.camera.position);
    /* time evolution of a monochromatic field: the phase advances uniformly, |E|^2 stays put */
    const a = this.c.geometry.attributes, ea = this.ev.geometry.attributes, W = 2.4*this.t;
    for(let i=0;i<this.n;i++){ const c = hue(this.ph[i] - W, this.br[i]); a.color.setXYZ(i, c[0], c[1], c[2]); }
    for(let i=0;i<this.ne;i++){ const c = hue(this.eph[i] - W, this.ebr[i]); ea.color.setXYZ(i, c[0], c[1], c[2]); }
    a.color.needsUpdate = ea.color.needsUpdate = true;
    const rf = this.rf || {s:[0,0], p:[0,0]}, pol = z => f(Math.hypot(z[0],z[1]),3)+' ∠ '+f(Math.atan2(z[1],z[0])*180/Math.PI,1)+'°';
    return [['angle θ₁ (in glass)', f(S.th*180/Math.PI,1)+'°'], ['critical angle θc', S.thc==null ? 'none' : f(S.thc*180/Math.PI,2)+'°'],
      ['Brewster angle θB (p)', f(Math.atan(1/S.n1)*180/Math.PI,2)+'°'],
      ['one face', S.sn.tir ? 'total reflection' : 'refracted at θ₂ = '+f(S.sn.th2*180/Math.PI,2)+'°'],
      ['r_s, one face', pol(rf.s)], ['r_p, one face', pol(rf.p)],
      ['evanescent depth δ (field 1/e)', S.sn.tir ? f(S.dep,0)+' nm' : '—'],
      ['across the 200 nm gap (s)', 'R '+f(100*(this.Rst||0),1)+' %, T '+f(100*(this.Tst||0),1)+' %'],
      ['beam waist (drawn)', f(this.w0l||0,1)+' λ'], ['points', 'density |E|², colour = phase']]; }});

})();
