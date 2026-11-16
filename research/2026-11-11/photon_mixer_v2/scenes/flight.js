/* SCRIPT: PHOTON-MIXER-V2-SCENE-FLIGHT */
(function(){
"use strict";
const PHX = window.PHX, { M, T, K, V3, f, sci, TAU, hue, lamRGB, lamName, cloud, clearCloud, fill, ringLine, LE } = PHX;
/* 2 ---------- a wave packet crossing 1 AU ----------
   Distances along the path are to scale (1 AU = the Sun–Earth gap on screen); the Sun, the Earth and the packet are
   magnified so they can be seen. The packet is a Gaussian wave packet: E along y, B along z, both ∝ exp(−(x−ct)²/2σ²) cos(kx − ωt).
   In vacuum ω = ck, so the whole pattern moves rigidly at c: it is sampled once and carried. */
const XS = -3.3, XE = 4.35, RS = 1.2, RE = 0.36;      /* Sun centre, Earth centre, drawn radii */
const X0 = XS + RS + 0.15, X1 = XE - RE - 0.15;     /* the packet runs from the Sun's surface to the Earth's surface */
const PER = 9;                                        /* seconds of animation per crossing */
const HEAT = [[0.20,0.03,0.30],[0.90,0.30,0.10],[1.00,0.66,0.12],[1.00,0.95,0.70]];
function heat(t){ t = Math.max(0, Math.min(1, t)); const x = t*(HEAT.length-1), i = Math.min(HEAT.length-2, Math.floor(x)), fr = x-i; return [0,1,2].map(k => HEAT[i][k]*(1-fr) + HEAT[i+1][k]*fr); }

PHX.add({ id:'flight', section:'II · Eight minutes', grade:'standard physics, recomputed', title:'Eight minutes to the Earth',
  eq:'E(x,t) = E₀ exp(−(x−ct)²/2σ²) cos(kx − ωt),  ω = ck\nt = 1 AU / c = 499.0 s,   along a light path dτ = 0',
  text:'The Sun (point density from the computed n = 3 density, colour its temperature), the Earth, and between them one photon drawn as a wave packet: the electric field in one plane, the magnetic field at right angles, colour the phase kx − ωt. The gap is one astronomical unit, ticked off in light-minutes; the bodies and the wavelength are magnified. The Earth’s clock runs to 499 seconds during the crossing. The floor is a spacetime diagram on the same scale, distance across and Earth time into the screen: the photon’s worldline runs at 45°, where the interval c²Δt² − Δx² is zero. Along the photon’s own path the proper time is zero, so its clock never moves: emission and absorption are not separated in time for the photon.',
  uses:['lam'], view:[-0.1,0.36,12.2,-0.75],
  make(G, st){ this.G = G;
    /* the Sun: density theta^3 inside, a photosphere shell, colour = temperature */
    this.sun = cloud(80000, 0.03); G.add(this.sun);
    fill(this.sun, [-RS,RS,-RS,RS,-RS,RS], (x,y,z) => { const r = Math.hypot(x,y,z)/RS; if(r >= 1) return 0; return Math.pow(LE.theta(r),3) + (r > 0.96 ? 0.12 : 0.02); }, 1.12,
      (x,y,z) => { const th = LE.theta(Math.hypot(x,y,z)/RS), h = heat(0.25 + 0.75*th), b = 0.42 + 0.2*th; return [h[0]*b, h[1]*b, h[2]*b]; });
    this.sun.position.set(XS, 0, 0);
    this.cor = cloud(7000, 0.04); G.add(this.cor);   /* radiation leaving the surface: energy density ∝ 1/r² beyond R */
    fill(this.cor, [-2.6*RS,2.6*RS,-2.6*RS,2.6*RS,-2.6*RS,2.6*RS], (x,y,z) => { const r = Math.hypot(x,y,z)/RS; return r > 1 && r < 2.6 ? 1/(r*r) : 0; }, 1, () => [0.22,0.10,0.02]);
    this.cor.position.set(XS, 0, 0);
    this.sl = new T.PointLight(0xfff1d8, 3.2, 0, 0); this.sl.position.set(XS, 0, 0); G.add(this.sl);
    /* the Earth: a lit sphere and a thin atmosphere */
    this.earth = new T.Mesh(new T.SphereGeometry(RE, 48, 32), new T.MeshStandardMaterial({color:0x2a6fd6, emissive:0x061430, emissiveIntensity:1, roughness:0.55, metalness:0}));
    this.earth.position.set(XE, 0, 0); G.add(this.earth);
    this.atm = M.shell(RE*1.08, 0x5fb4ff, 0.10); this.atm.position.set(XE, 0, 0); G.add(this.atm);
    /* the 1 AU path, ticked in light-minutes (1 AU = 8.317 light-minutes) */
    const AUm = K.AU/K.c/60, sx = (X1 - X0)/AUm;
    G.add(M.line([V3(X0,0,0), V3(X1,0,0)], 0x63d3ff, 0.30));
    for(let m=0;m<=Math.floor(AUm);m++){ const x = X0 + m*sx; G.add(M.line([V3(x,-0.12,0), V3(x,0.12,0)], 0x63d3ff, m%4===0?0.8:0.4));
      if(m%4===0 && m>0){ const L = M.label(m+' min', '#9fe4ff', 0.2); L.position.set(x, -0.42, 0); G.add(L); } }
    const LA = M.label('1 AU = 499.0 light-seconds', '#9fe4ff', 0.22); LA.position.set((X0+X1)/2, -2.9 - 0.34, 0.15); G.add(LA);
    const LS = M.label('Sun', '#ffd27a', 0.26); LS.position.set(XS, -RS-0.45, 0); G.add(LS);
    const LE2 = M.label('Earth', '#9fd0ff', 0.26); LE2.position.set(XE, -RE-0.45, 0); G.add(LE2);
    /* the packet: E sheet (y) and B sheet (z), points uniformly fill the area between the axis and the field curve */
    this.pk = cloud(26000, 0.026); G.add(this.pk); this.lamK = null;
    /* the two clocks, drawn above: the Earth clock (hand sweeps once per crossing, t / 499 s) and the photon's clock (hand fixed at zero) */
    const CR = 0.36, CY = 1.35; this.CR = CR; this.CY = CY;
    this.ecr = ringLine(CR, 0, 0x9fd0ff, 0.35); this.ecr.rotation.x = Math.PI/2; this.ecr.position.set(XE, CY, 0); G.add(this.ecr);
    this.ec = M.line([V3(),V3()], 0x9fd0ff, 1); G.add(this.ec); this.eh = M.line([V3(),V3()], 0xffffff, 0.95); G.add(this.eh);
    this.pc = ringLine(CR, 0, 0xffffff, 0.45); this.pc.rotation.x = Math.PI/2; G.add(this.pc); this.ph = M.line([V3(0,0,0),V3(0,CR,0)], 0xffffff, 1); G.add(this.ph);
    this.lbE = null; this.lbP = M.label('photon: τ = 0 s', '#ffffff', 0.22); G.add(this.lbP);
    this.lnk = M.line([V3(),V3()], 0xffffff, 0.25); G.add(this.lnk);
    /* the floor is a spacetime diagram drawn to the same scale: across = distance x, into the screen = Earth time ct (1 light-minute = 1 tick).
       The photon's worldline runs at 45°: c²Δt² − Δx² = 0 at every step, so its proper time is zero from emission to arrival. */
    const FY = -2.9, W = X1 - X0; this.FY = FY; this.W = W;
    G.add(M.line([V3(X0,FY,0), V3(X1,FY,0)], 0x63d3ff, 0.35));
    G.add(M.line([V3(X0,FY,0), V3(X0,FY,-W)], 0xffd27a, 0.6)); G.add(M.line([V3(X1,FY,0), V3(X1,FY,-W)], 0x9fd0ff, 0.6));
    for(let m=1;m<=Math.floor(AUm);m++){ G.add(M.line([V3(X1-0.1,FY,-m*sx), V3(X1+0.1,FY,-m*sx)], 0x9fd0ff, 0.5)); G.add(M.line([V3(X0-0.1,FY,-m*sx), V3(X0+0.1,FY,-m*sx)], 0xffd27a, 0.4)); }
    this.wl = M.line([V3(X0,FY,0), V3(X0,FY,0)], 0xffffff, 0.95); G.add(this.wl);
    G.add(M.line([V3(X0,FY,0), V3(X1,FY,-W)], 0xffffff, 0.14));
    this.ev = cloud(3, 0.22); G.add(this.ev); M.setPt(this.ev, 0, V3(X0,FY,0), [1,0.85,0.5]); M.setPt(this.ev, 1, V3(X1,FY,-W), [0,0,0]); M.flush(this.ev);
    const l1 = M.label('Earth time ct (light-minutes)', '#9fd0ff', 0.26); l1.position.set(X1+1.75, FY, -W*0.4); G.add(l1);
    const l2 = M.label('photon worldline: ds² = 0', '#ffffff', 0.28); l2.position.set(X0 + W*0.22, FY + 0.3, -W*0.45); G.add(l2);
    const l3 = M.label('emission', '#ffd27a', 0.24); l3.position.set(X0, FY - 0.3, 0.1); G.add(l3);
    this.l4 = M.label('arrival: 499.0 s later on Earth, 0 s later for the photon', '#ffffff', 0.26); this.l4.position.set(X1 - 2.2, FY - 0.1, -W*0.8); G.add(this.l4);
    this.t = 0; this.shown = -1; },
  sample(S){ /* sample the packet once per wavelength: length units are drawn units, wavelength magnified */
    const a = this.pk.geometry.attributes, n = a.position.count, lv = 0.13 + 0.12*(S.lam-400)/300, k = TAU/lv, sg = 0.42, A = 0.62;
    for(let i=0;i<n;i++){ let x, e; for(let r=0;r<30;r++){ x = sg*3.2*(2*Math.random()-1); e = Math.exp(-x*x/(2*sg*sg)); if(Math.random() < e) break; }
      const fv = A*e*Math.cos(k*x), s = Math.random()*fv, w = (Math.random()-0.5)*0.025;    /* a point between the axis and the field value */
      if(i % 2 === 0) a.position.setXYZ(i, x, s, w); else a.position.setXYZ(i, x, w, s);    /* E in the x–y plane, B in the x–z plane */
      const c = hue(k*x), b = i%2===0 ? 1 : 0.65; a.color.setXYZ(i, c[0]*b, c[1]*b, c[2]*b); }
    a.position.needsUpdate = a.color.needsUpdate = true; this.lamK = S.lam; },
  enter(S){ PHX.base(); this.t = 0; this.G.rotation.set(0,0,0); this.y0 = PHX.S3.view.yaw; },
  step(dt, S){ dt = Math.max(0, dt); this.t += dt; const V = PHX.S3.view;
    if(this.lamK !== S.lam) this.sample(S);
    if(V.auto) this.G.rotation.y = (V.yaw - this.y0) - 0.12*Math.sin(0.2*this.t);    /* hold the Sun–Earth line across the view */
    const u = Math.min(1, (this.t % (PER + 1.2))/PER), x = X0 + (X1 - X0)*u, fl = K.flight(), te = fl.t*u;
    this.pk.position.set(x, 0, 0); this.pk.visible = u < 1;
    const CR = this.CR, CY = this.CY;
    const xq = Math.min(x, XE - 1.3); this.pc.position.set(xq, CY, 0); this.ph.position.set(xq, CY, 0); this.lbP.position.set(xq, CY + CR + 0.25, 0); M.setLine(this.lnk, [V3(x, 0.7, 0), V3(xq, CY - CR, 0)]); this.lnk.visible = u < 1;
    const pts = []; const nn = Math.max(2, Math.ceil(80*u)); for(let i=0;i<=nn;i++){ const a = TAU*u*i/nn; pts.push(V3(XE + CR*0.85*Math.sin(a), CY + CR*0.85*Math.cos(a), 0)); }
    M.setLine(this.ec, pts); M.setLine(this.eh, [V3(XE, CY, 0), V3(XE + CR*Math.sin(TAU*u), CY + CR*Math.cos(TAU*u), 0)]);
    const sec = Math.round(te); if(sec !== this.shown){ this.shown = sec; if(this.lbE){ this.G.remove(this.lbE); this.lbE.material.map.dispose(); this.lbE.material.dispose(); }
      this.lbE = M.label('Earth: '+sec+' s', '#9fd0ff', 0.22); this.lbE.position.set(XE, CY + CR + 0.25, 0); this.G.add(this.lbE); }
    this.earth.rotation.y += dt*0.15;
    M.setLine(this.wl, [V3(X0,this.FY,0), V3(x,this.FY,-(x-X0))]); M.setPt(this.ev, 2, V3(x,this.FY,-(x-X0)), S.rgb.map(v => v*0.9));
    M.setPt(this.ev, 1, V3(X1,this.FY,-this.W), u >= 1 ? [1,1,1] : [0,0,0]); M.flush(this.ev); this.l4.visible = u >= 1;
    return [['Earth-frame time', f(te,1)+' s of '+f(fl.t,1)+' s ('+f(fl.minutes,2)+' min)'], ['photon proper time', '0 s (null path, dτ = 0)'], ['interval c²Δt² − Δx²', '(499.0 ls)² − (499.0 ls)² = 0'],
      ['distance', '1 AU = '+sci(K.AU,4)+' m'], ['wavelength', S.lam+' nm ('+lamName(S.lam)+')'],
      ['frequency', sci(K.freq(S.lam),3)+' Hz'], ['energy hc/λ', f(S.E,3)+' eV'], ['colour of the packet', 'phase kx − ωt'], ['scale', 'distance to scale; bodies, λ magnified']]; }});


})();
