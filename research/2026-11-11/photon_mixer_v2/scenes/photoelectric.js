/* SCRIPT: PHOTON-MIXER-V2-SCENE-PHOTOELECTRIC */
(function(){
"use strict";
const PHX = window.PHX, { M, T, K, V3, f, sci, TAU, hue, lamRGB, lamName, cloud, clearCloud, fill, ringLine, LE } = PHX;
/* 6 ---------- photoelectric effect: a metal crystal, one photon, all or nothing ----------
   Scene unit = 1 nm. The metal is a bcc crystal (lattice constant a = 0.61 nm) of ion cores, each a small dense sphere of points,
   with a faint uniform haze for the free-electron gas. The photon is a packet coloured by its wavelength; it is drawn with its
   wavelength scaled down 1000 times (550 nm would be 900 lattice spacings). Above threshold the electron is a free Gaussian
   wave packet: |psi|^2 has standard deviation sigma(t) = sigma0 sqrt(1 + tau^2), tau = hbar t / (2 m sigma0^2), centre moving at
   v = sqrt(2K/m), colour = phase of psi including the spreading chirp. Below threshold the photon's energy stays in the lattice
   as vibration (heat), drawn slowed and exaggerated. */
const HBAR_M = 0.115767;            /* hbar / m_e in nm^2 / fs */
const HBAR = 0.6582119569;          /* eV fs */
const VEL = 0.593097;               /* nm/fs per sqrt(eV): v = sqrt(2 K e / m_e) */
const A = 0.61, S0 = 0.6, CYC = 6.4, TP = 2.1, TA = 0.35;
const NE = 22000, NP = 9000, NH = 5000, PER = 44, XL = 2.6, ZL = 1.9;
PHX.add({ id:'photoelectric', section:'VI · Paid in full', grade:'standard physics, recomputed', title:'Absorbed: the photoelectric effect',
  sub:'The whole photon goes to one electron; it leaves only if h f exceeds the work function',
  eq:'h f = φ + K_max   (Einstein 1905; Nobel Prize 1921)\nthreshold: λ₀ = h c / φ\nfree electron packet:  σ(t)² = σ₀² + (ħt / 2mσ₀)²,   v = √(2K/m),   λ_dB = h / √(2mK)',
  text:'The metal is drawn as its crystal: ion cores as small dense spheres in a body-centred cubic lattice, with a faint haze for the free electrons. A single photon arrives (colour = its wavelength) and is absorbed whole: all of its energy goes to one electron. If h f exceeds the work function φ, the electron leaves the surface with kinetic energy h f − φ as a free wave packet that moves off and spreads (colour = phase of its wavefunction). If not, no electron leaves, however bright the light; the energy stays in the metal as a small lattice vibration, which is heat.',
  uses:['lam','phi'], view:[0.6,0.3,11,0.6],
  make(G, st){ this.G = G;
    /* crystal: bcc sites inside the slab x in [-3.4,3.4], z in [-2.4,2.4], y in [-1.85,0] */
    const sites = [];
    for(let i=-5;i<=5;i++) for(let k=-4;k<=4;k++) for(let j=0;j<=3;j++){
      const p = [i*A, -j*A, k*A], q = [i*A + A/2, -j*A - A/2, k*A + A/2];
      [p,q].forEach(s => { if(Math.abs(s[0]) <= XL+0.05 && Math.abs(s[2]) <= ZL+0.05 && s[1] >= -1.9) sites.push(s); }); }
    this.sites = sites; const NL = sites.length*PER; this.L = cloud(NL, 0.036); G.add(this.L); this.off = new Float32Array(NL*3);
    const la = this.L.geometry.attributes;
    for(let s=0;s<sites.length;s++) for(let m=0;m<PER;m++){ const i = s*PER+m, r = Math.min(0.11, 0.045*Math.sqrt(-2*Math.log(Math.random()+1e-9))), u = 2*Math.random()-1, ph = TAU*Math.random(), w = Math.sqrt(1-u*u);
      this.off[3*i] = r*w*Math.cos(ph); this.off[3*i+1] = r*u; this.off[3*i+2] = r*w*Math.sin(ph);
      la.position.setXYZ(i, sites[s][0]+this.off[3*i], sites[s][1]+this.off[3*i+1], sites[s][2]+this.off[3*i+2]); la.color.setXYZ(i, 0.5,0.58,0.72); }
    la.position.needsUpdate = la.color.needsUpdate = true;
    this.gas = cloud(NH, 0.022); G.add(this.gas); const ha = this.gas.geometry.attributes;
    for(let i=0;i<NH;i++){ ha.position.setXYZ(i, (2*Math.random()-1)*(XL+0.2), -1.95*Math.random(), (2*Math.random()-1)*(ZL+0.2)); ha.color.setXYZ(i, 0.02,0.05,0.08); } ha.position.needsUpdate = ha.color.needsUpdate = true;
    const c = [[-XL-0.2,-ZL-0.2],[XL+0.2,-ZL-0.2],[XL+0.2,ZL+0.2],[-XL-0.2,ZL+0.2]];
    for(let i=0;i<4;i++){ const a = c[i], b = c[(i+1)%4]; G.add(M.line([V3(a[0],0.06,a[1]), V3(b[0],0.06,b[1])], 0x63d3ff, 0.32)); G.add(M.line([V3(a[0],0.06,a[1]), V3(a[0],-1.95,a[1])], 0x63d3ff, 0.12)); }
    this.e = cloud(NE, 0.036); G.add(this.e); this.p = cloud(NP, 0.032); G.add(this.p); this.fl = cloud(600, 0.05); G.add(this.fl);
    this.path = M.line([V3(0,0.1,0), V3(0,4.5,0)], 0xffffff, 0.12); G.add(this.path);
    const lm = M.label('metal crystal (bcc, a = 0.61 nm)', '#8fc7ff', 0.26); lm.position.set(-0.6, -2.4, ZL+0.4); G.add(lm);
    this.lab = []; this.key = ''; this.t = 0; },
  enter(){ PHX.base(); PHX.S3.world.rotation.set(0,0,0); this.t = 0; this.key = ''; },
  relabel(S){ const pe = S.pe; this.lab.forEach(l => { this.G.remove(l); l.material.map.dispose(); l.material.dispose(); }); this.lab = [];
    const add = (txt, col, sc, x, y, z) => { const l = M.label(txt, col, sc); l.position.set(x,y,z); this.G.add(l); this.lab.push(l); return l; };
    this.lPh = add('photon  h f = '+f(pe.E,2)+' eV', M.colour.hex(S.rgb), 0.3, -3.9, 2.9, 1.1);
    this.lEl = add(pe.emits ? 'electron  K = '+f(pe.K,3)+' eV' : 'no electron: '+f(pe.E,2)+' eV < φ = '+f(S.phi,2)+' eV', pe.emits ? '#dfe7ef' : '#ff9a6a', 0.3, pe.emits ? 2.3 : 0.4, pe.emits ? 3.0 : 1.0, 0);
    this.lHeat = add('photon energy left as lattice vibration (heat)', '#ff9a6a', 0.28, 0.3, 0.55, 0); },
  step(dt, S){ this.t += dt; const pe = S.pe;
    if(this.key !== S.key){ this.key = S.key; this.relabel(S); }
    const u = this.t % CYC, ea = this.e.geometry.attributes, pa = this.p.geometry.attributes, fa = this.fl.geometry.attributes, la = this.L.geometry.attributes;
    const target = V3(0,0.06,0), start = V3(-3.0,3.6,1.0), dir = target.clone().sub(start).normalize(), Lp = start.distanceTo(target);
    /* ---- photon packet: envelope sigma_long 0.5, sigma_trans 0.2, bands at the drawn wavelength lam/1000 nm ---- */
    const lamD = S.lam/1000, kD = TAU/lamD, rgb = S.rgb; let shrink = 1, pc = null;
    if(u < TP + TA){ const w = Math.min(1, u/TP); pc = start.clone().lerp(target, w); shrink = u < TP ? 1 : Math.max(0, 1 - (u-TP)/TA); }
    const e1 = V3(dir.y, -dir.x, 0).normalize(), e2 = dir.clone().cross(e1);
    for(let i=0;i<NP;i++){
      if(!pc || shrink <= 0){ pa.color.setXYZ(i,0,0,0); continue; }
      let s, tries = 0; do { s = 0.5*Math.sqrt(-2*Math.log(Math.random()+1e-9))*Math.cos(TAU*Math.random()); tries++; } while(Math.random() > Math.pow(Math.cos(kD*s - 9*this.t), 2) && tries < 8);
      const a1 = 0.2*Math.sqrt(-2*Math.log(Math.random()+1e-9))*Math.cos(TAU*Math.random()), a2 = 0.2*Math.sqrt(-2*Math.log(Math.random()+1e-9))*Math.cos(TAU*Math.random());
      let x = pc.x + (dir.x*s + e1.x*a1 + e2.x*a2)*shrink, y = pc.y + (dir.y*s + e1.y*a1 + e2.y*a2)*shrink, z = pc.z + (dir.z*s + e1.z*a1 + e2.z*a2)*shrink;
      if(y < 0.06){ pa.color.setXYZ(i,0,0,0); continue; }   /* nothing of the photon is drawn inside the metal: it is absorbed at the surface */
      pa.position.setXYZ(i, x, y, z); pa.color.setXYZ(i, rgb[0]*0.8, rgb[1]*0.8, rgb[2]*0.8); }
    /* ---- absorption flash at the site ---- */
    const fT = u - TP, fOn = fT > -0.05 && fT < 0.6, fb = fOn ? Math.exp(-Math.max(0,fT)/0.18) : 0;
    for(let i=0;i<600;i++){ if(!fOn){ fa.color.setXYZ(i,0,0,0); continue; } const r = 0.12*Math.sqrt(-2*Math.log(Math.random()+1e-9)), a = TAU*Math.random(), b = Math.acos(2*Math.random()-1);
      fa.position.setXYZ(i, r*Math.sin(b)*Math.cos(a), 0.06 + Math.abs(r*Math.cos(b)), r*Math.sin(b)*Math.sin(a)); fa.color.setXYZ(i, fb*(0.6+0.4*rgb[0]), fb*(0.6+0.4*rgb[1]), fb*(0.6+0.4*rgb[2])); }
    /* ---- after absorption: electron packet, or lattice vibration ---- */
    const after = u - (TP + TA), span = CYC - (TP + TA) - 0.3; let tfs = 0, sig = S0;
    const v = VEL*Math.sqrt(Math.max(pe.K, 0)), tEnd = pe.emits ? Math.min(40, 2.6/Math.max(v,1e-6)) : 0;
    if(pe.emits && after > 0){
      tfs = Math.min(1, after/span)*tEnd; const tau = HBAR_M*tfs/(2*S0*S0), k0 = v/HBAR_M, om = pe.K/HBAR, yc = 0.12 + v*tfs; sig = S0*Math.sqrt(1 + tau*tau);
      const chirp = tau/(4*S0*S0*(1 + tau*tau)), gph = -1.5*Math.atan(tau), fade = after > span ? Math.max(0, 1 - (after-span)/0.3) : 1;
      for(let i=0;i<NE;i++){ const g = () => sig*Math.sqrt(-2*Math.log(Math.random()+1e-9))*Math.cos(TAU*Math.random());
        const dx = g(), dy = g(), dz = g(), y = yc + dy;
        if(y < 0.08){ ea.color.setXYZ(i,0,0,0); continue; }   /* the packet is drawn only outside the metal */
        const ph = k0*(y - 0.12) - om*tfs + (dx*dx + dy*dy + dz*dz)*chirp + gph, c = hue(ph, 0.95*fade);
        ea.position.setXYZ(i, dx, y, dz); ea.color.setXYZ(i, c[0], c[1], c[2]); }
      this.path.visible = true; M.setLine(this.path, [V3(0,0.1,0), V3(0, Math.max(0.12, yc), 0)]);
    } else { for(let i=0;i<NE;i++) ea.color.setXYZ(i,0,0,0); this.path.visible = false; }
    /* lattice: at rest, or (below threshold) a vibration spreading out from the absorption site, slowed and exaggerated */
    const heat = !pe.emits && after > 0, tt = Math.max(0, after);
    for(let s=0;s<this.sites.length;s++){ const P = this.sites[s]; let dx = 0, dy = 0, dz = 0, warm = 0;
      if(heat){ const r = Math.hypot(P[0], P[1], P[2]) + 1e-6, front = 0.9*tt, env = 0.2*Math.exp(-tt/1.8)*Math.exp(-Math.pow(r - front, 2)/(2*0.45*0.45))/(1 + 0.6*r), osc = Math.sin(TAU*3.2*tt - 4*r);
        const d = env*osc; dx = d*P[0]/r; dy = d*P[1]/r; dz = d*P[2]/r; warm = Math.min(1, env/0.03); }
      const cr = 0.5 + 0.8*warm, cg = 0.58 - 0.05*warm, cb = 0.72 - 0.6*warm;
      for(let m=0;m<PER;m++){ const i = s*PER+m; la.position.setXYZ(i, P[0]+dx+this.off[3*i], P[1]+dy+this.off[3*i+1], P[2]+dz+this.off[3*i+2]); la.color.setXYZ(i, cr, cg, cb); } }
    this.lEl.visible = after > 0; this.lHeat.visible = heat; this.lPh.visible = u < TP;
    ea.position.needsUpdate = ea.color.needsUpdate = pa.position.needsUpdate = pa.color.needsUpdate = fa.position.needsUpdate = fa.color.needsUpdate = la.position.needsUpdate = la.color.needsUpdate = true;
    const ldb = pe.emits ? 1.2264262/Math.sqrt(pe.K) : null;
    return [['photon energy h f', f(pe.E,3)+' eV'], ['work function φ', f(S.phi,2)+' eV'], ['threshold λ₀ = hc/φ', f(pe.lam0,1)+' nm'],
      ['electron leaves?', pe.emits ? 'yes: h f > φ' : 'no: h f < φ (energy becomes heat)'], ['K_max = h f − φ', f(pe.K,3)+' eV'],
      ['electron speed', pe.emits ? sci(v*1e6,2)+' m/s' : '—'], ['de Broglie wavelength', pe.emits ? f(ldb,2)+' nm' : '—'],
      ['electron clock / packet width σ', pe.emits && after > 0 ? f(tfs,1)+' fs / '+f(sig,2)+' nm' : '—'],
      ['photon drawn at', 'λ / 1000 (true λ ≫ lattice)']]; }});

})();
