/* SCRIPT: PHOTON-MIXER-V2-SCENE-SLITS */
(function(){
"use strict";
const PHX = window.PHX, { M, T, K, V3, f, sci, TAU, hue, lamRGB, lamName, cloud, clearCloud, fill, ringLine, LE } = PHX;
/* 4 ---------- two slits, one photon at a time; then the same with a which-path detector ----------
   The slits are long (along y) and narrow; each acts as a line source, so behind the barrier
   psi(x,z) = e^{ik r1}/sqrt(r1) + e^{ik r2}/sqrt(r2) (the 2D far-field form of a line source), the same at every height y.
   Without a detector the cloud is |psi|^2 and arrivals on the screen are drawn from |psi|^2 there: fringes.
   With a which-path detector the state is a mixture: |psi1|^2 + |psi2|^2, no cross term, no fringes.
   The film cycles: first half no detector, second half detector on. Scene: the wavelength is drawn as 0.24 (lam/550). */
const CAP = 4.4, NF = 150000, NI = 14000, NB = 9000, NS = 5000, NH = 6000, CYC = 18;
const X0 = -2.6, X1 = 3.6, XI = -3.9, ZW = 2.7, HY = 0.45;
PHX.add({ id:'slits', section:'IV · Both ways', grade:'standard physics, recomputed', title:'Two slits, one photon at a time',
  sub:'The field passes through both slits; a which-path detector removes the fringes',
  eq:'no detector:  P(z) ∝ |ψ₁ + ψ₂|² = |ψ₁|² + |ψ₂|² + 2 Re ψ₁*ψ₂   (fringes, spacing Δz ≈ λL/d)\nwhich-path detector:  P(z) ∝ |ψ₁|² + |ψ₂|²   (cross term gone, no fringes)\nψⱼ = e^{ikrⱼ}/√rⱼ  (each slit a line source)',
  text:'A plane wave meets a barrier with two narrow slits. Behind it the cloud is the computed field: point density follows |ψ|² (with the 1/r spreading compensated so the far field stays visible), colour is the phase, so the moving bands are wavefronts. The fringes exist in the field before anything is detected. Photons then arrive on the screen one at a time, each at a single point drawn from |ψ|², and the dots build the same fringes. In the second half of the cycle a which-path detector marks which slit each photon used: the two paths no longer interfere, the field becomes |ψ₁|² + |ψ₂|², and the arrivals pile into a plain double band with no fringes.',
  uses:['dsl','lam'], view:[-1.0,0.66,11.5,0.05],
  make(G, st){ this.G = G; G.position.x = -0.2;
    this.c = cloud(NF, 0.03); G.add(this.c); this.ph = new Float32Array(NF); this.br = new Float32Array(NF);
    this.inc = cloud(NI, 0.028); G.add(this.inc); this.ix = new Float32Array(NI);
    this.bar = cloud(NB, 0.024); G.add(this.bar);
    this.scr = cloud(NS, 0.02); G.add(this.scr); const sa = this.scr.geometry.attributes;
    for(let i=0;i<NS;i++){ sa.position.setXYZ(i, X1+0.03, (2*Math.random()-1)*HY, (2*Math.random()-1)*ZW); sa.color.setXYZ(i,0.08,0.09,0.12); } sa.position.needsUpdate = sa.color.needsUpdate = true;
    this.h = cloud(NH, 0.11); G.add(this.h); this.age = new Float32Array(NH);
    const ed = (pts, op) => G.add(M.line(pts, 0x8a9aab, op));
    ed([V3(X1,-HY,-ZW),V3(X1,HY,-ZW),V3(X1,HY,ZW),V3(X1,-HY,ZW),V3(X1,-HY,-ZW)], 0.35);
    this.det = []; for(let j=0;j<2;j++){ const l = M.line([V3(),V3()], 0x63d3ff, 0.9); this.det.push(l); G.add(l); }
    const ls = M.label('screen', '#8a9aab', 0.26); ls.position.set(X1+0.1, HY+0.3, -ZW+0.6); G.add(ls);
    const lb = M.label('two slits', '#8fc7ff', 0.26); lb.position.set(X0, HY+0.9, 0); G.add(lb);
    this.lmode = M.label('no which-path detector', '#dfe7ef', 0.3); this.lmode.position.set(0.4, HY+0.75, -ZW); G.add(this.lmode);
    this.lmode2 = M.label('which-path detector on', '#63d3ff', 0.3); this.lmode2.position.set(0.4, HY+0.75, -ZW); G.add(this.lmode2);
    this.key = ''; this.t = 0; this.n = 0; this.nb = 0; this.mode = -1; this.tc = 9; },
  enter(){ PHX.base(); PHX.S3.world.rotation.set(0,0,0); this.key = ''; this.t = 0; this.mode = -1; this.tc = 9; },
  geom(S){ const lamV = 0.24*(S.lam/550), k = TAU/lamV, d = S.dsl*lamV; return { lamV, k, d, z1: d/2, z2: -d/2 }; },
  /* fill the field cloud for mode 0 (coherent) or 1 (which-path mixture) */
  build(S, mode){ const g = this.geom(S), k = g.k, h = Math.min(0.03, g.lamV/8), nx = Math.ceil((X1-X0)/h), nz = Math.ceil(2*ZW/h)+1;
    const N = nx*nz, I = new Float32Array(N*(mode ? 2 : 1)), P = new Float32Array(N*(mode ? 2 : 1));
    const xc = i => X0 + (i+0.5)*h, zc = j => -ZW + j*h;
    for(let j=0;j<nz;j++) for(let i=0;i<nx;i++){ const x = xc(i), z = zc(j), r1 = Math.hypot(x-X0, z-g.z1), r2 = Math.hypot(x-X0, z-g.z2), w = Math.hypot(x-X0, z);
      const a1 = 1/Math.sqrt(r1), a2 = 1/Math.sqrt(r2), o = j*nx+i;
      if(!mode){ const re = a1*Math.cos(k*r1) + a2*Math.cos(k*r2), im = a1*Math.sin(k*r1) + a2*Math.sin(k*r2); I[o] = Math.min(CAP, (re*re+im*im)*w); P[o] = Math.atan2(im, re); }
      else { I[o] = Math.min(CAP/2, a1*a1*w); P[o] = k*r1; I[N+o] = Math.min(CAP/2, a2*a2*w); P[N+o] = k*r2; } }
    const M2 = I.length, cdf = new Float64Array(M2); let s = 0, mx = 0; for(let i=0;i<M2;i++){ s += I[i]; cdf[i] = s; if(I[i] > mx) mx = I[i]; }
    const a = this.c.geometry.attributes;
    for(let p=0;p<NF;p++){ const R = Math.random()*s; let lo = 0, hi = M2-1; while(lo < hi){ const m = (lo+hi) >> 1; if(cdf[m] < R) lo = m+1; else hi = m; }
      const o = lo % N, j = Math.floor(o/nx), i = o - j*nx, x = xc(i) + (Math.random()-0.5)*h, z = zc(j) + (Math.random()-0.5)*h;
      const y = (2*Math.random()-1)*HY*(0.75 + 0.25*Math.random());   /* uniform along the slit length, softened ends */
      a.position.setXYZ(p, x, y, z); this.ph[p] = P[lo]; this.br[p] = 0.12 + 0.9*Math.pow(I[lo]/(mode ? CAP/2 : CAP), 0.8); }
    a.position.needsUpdate = true; this.n = NF;
    /* screen intensity used for arrivals (true |psi|^2 or the mixture, no display weighting) */
    const NZ = 600, sc = new Float64Array(NZ); let ss = 0;
    for(let j=0;j<NZ;j++){ const z = -ZW + 2*ZW*(j+0.5)/NZ, r1 = Math.hypot(X1-X0, z-g.z1), r2 = Math.hypot(X1-X0, z-g.z2);
      const v = mode ? 1/r1 + 1/r2 : Math.pow(Math.cos(k*r1)/Math.sqrt(r1) + Math.cos(k*r2)/Math.sqrt(r2), 2) + Math.pow(Math.sin(k*r1)/Math.sqrt(r1) + Math.sin(k*r2)/Math.sqrt(r2), 2);
      ss += v; sc[j] = ss; }
    this.scdf = sc; this.ssum = ss;
    /* the barrier: a wall of points with two openings, and the incident plane wave in front of it */
    const ba = this.bar.geometry.attributes, sw = Math.max(0.05, 0.25*g.lamV);
    for(let i=0;i<NB;i++){ let z; do { z = (2*Math.random()-1)*ZW; } while(Math.abs(z-g.z1) < sw || Math.abs(z-g.z2) < sw);
      ba.position.setXYZ(i, X0 + (Math.random()-0.5)*0.08, (2*Math.random()-1)*HY, z); ba.color.setXYZ(i, 0.17,0.21,0.28); }
    ba.position.needsUpdate = ba.color.needsUpdate = true;
    const ia = this.inc.geometry.attributes;
    for(let i=0;i<NI;i++){ const x = XI + Math.random()*(X0-XI); ia.position.setXYZ(i, x, (2*Math.random()-1)*HY, (2*Math.random()-1)*ZW); this.ix[i] = k*(x - X0); }
    ia.position.needsUpdate = true;
    for(let j=0;j<2;j++){ const z0 = j ? g.z2 : g.z1, w = sw + 0.06;
      M.setLine(this.det[j], [V3(X0+0.05,-HY-0.1,z0-w),V3(X0+0.05,HY+0.1,z0-w),V3(X0+0.05,HY+0.1,z0+w),V3(X0+0.05,-HY-0.1,z0+w),V3(X0+0.05,-HY-0.1,z0-w)]); }
    this.g = g; },
  step(dt, S){ this.t += dt; this.tc += dt;
    const ph = (this.t % CYC)/CYC, mode = ph < 0.5 ? 0 : 1;
    if((this.key !== S.key && this.tc > 0.25) || mode !== this.mode){ const fresh = mode !== this.mode || this.key !== S.key; this.key = S.key; this.tc = 0; this.mode = mode; this.build(S, mode);
      if(fresh){ this.nb = 0; clearCloud(this.h); } }
    this.lmode.visible = mode === 0; this.lmode2.visible = mode === 1; this.det.forEach(l => l.visible = mode === 1);
    /* wavefronts move: colour = phase − ωt */
    const W = 2.6*this.t, a = this.c.geometry.attributes, ia = this.inc.geometry.attributes;
    for(let i=0;i<this.n;i++){ const c = hue(this.ph[i] - W, this.br[i]); a.color.setXYZ(i, c[0], c[1], c[2]); }
    for(let i=0;i<NI;i++){ const c = hue(this.ix[i] - W, 0.38); ia.color.setXYZ(i, c[0], c[1], c[2]); }
    a.color.needsUpdate = ia.color.needsUpdate = true;
    /* arrivals: one photon at a time, each at a point drawn from the screen intensity; new dots flash, then settle */
    this.acc = (this.acc||0) + dt; const rgb = S.rgb;
    while(this.acc > 0.004 && this.nb < NH){ this.acc -= 0.004; const R = Math.random()*this.ssum; let lo = 0, hi = this.scdf.length-1;
      while(lo < hi){ const m = (lo+hi) >> 1; if(this.scdf[m] < R) lo = m+1; else hi = m; }
      const z = -ZW + 2*ZW*(lo + Math.random())/this.scdf.length;
      M.setPt(this.h, this.nb, V3(X1+0.05, (2*Math.random()-1)*HY, z), rgb); this.age[this.nb] = 0; this.nb++; }
    if(this.nb >= NH) this.acc = 0;
    const ha = this.h.geometry.attributes;
    for(let i=Math.max(0, this.nb-200); i<this.nb; i++){ this.age[i] += dt; const b = 0.55 + 1.6*Math.exp(-this.age[i]/0.25); ha.color.setXYZ(i, rgb[0]*b, rgb[1]*b, rgb[2]*b); }
    M.flush(this.h);
    const th1 = Math.asin(Math.min(1, 1/S.dsl))*180/Math.PI;
    return [['which-path detector', mode ? 'on (second half of cycle)' : 'off (first half of cycle)'],
      ['field drawn', mode ? '|ψ₁|² + |ψ₂|², colour = phase' : '|ψ₁ + ψ₂|², colour = phase'],
      ['slit separation d', f(S.dsl,1)+' λ = '+f(S.dsl*S.lam,0)+' nm'], ['wavelength', S.lam+' nm'],
      ['first bright fringe off axis', mode ? 'none' : 'sin θ = λ/d → '+f(th1,2)+'°'],
      ['fringe spacing at L = 1 m (λL/d)', mode ? 'none' : f(1e3/S.dsl,1)+' mm'],
      ['photons recorded', this.nb]]; }});

})();
