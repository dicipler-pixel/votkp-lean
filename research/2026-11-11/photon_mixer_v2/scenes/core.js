/* SCRIPT: PHOTON-MIXER-V2-SCENE-CORE */
(function(){
"use strict";
const PHX = window.PHX, { M, T, K, V3, f, sci, TAU, hue, lamRGB, lamName, cloud, clearCloud, fill, ringLine, LE } = PHX;
/* 1 ---------- the Sun's interior and the random walk ----------
   Interior: Eddington's standard model, Lane–Emden n = 3. Density rho = rho_c theta^3, temperature T = T_c theta.
   rho_c / rho_mean = 54.18 for n = 3 (computed below from the same solution), T_c from the 15.7 MK solar value.
   One octant is cut away so the inside and the walk can be seen. */
const TC = 1.57e7;                          /* central temperature of the Sun, K (standard solar model) */
/* heat scale for temperature (inferno-like, 0 = cold, 1 = hottest) */
const HEAT = [[0.00,0.00,0.02],[0.20,0.03,0.30],[0.55,0.08,0.35],[0.90,0.30,0.10],[1.00,0.66,0.12],[1.00,0.95,0.70]];
function heat(t){ t = Math.max(0, Math.min(1, t)); const x = t*(HEAT.length-1), i = Math.min(HEAT.length-2, Math.floor(x)), fr = x-i;
  return [0,1,2].map(k => HEAT[i][k]*(1-fr) + HEAT[i+1][k]*fr); }
/* temperature on the heat scale, linear: T/Tc = theta */
const tScale = th => 0.12 + 0.88*th;
/* radius (fraction of R) where theta^3 falls to a given fraction of the central density */
function rAt(frac){ let lo = 0, hi = 1; for(let i=0;i<50;i++){ const m = (lo+hi)/2; if(Math.pow(LE.theta(m),3) > frac) lo = m; else hi = m; } return (lo+hi)/2; }
/* mean density over central density: 3 * integral theta^3 r^2 dr */
const MEANR = (() => { let s = 0; const n = 4000; for(let i=0;i<n;i++){ const r = (i+0.5)/n; s += Math.pow(LE.theta(r),3)*r*r/n; } return 3*s; })();
/* pp-chain energy release: 4 m(¹H) − m(⁴He), atomic masses (positron annihilation included) */
const QPP = (4*1.00782503 - 4.00260325)*931.49410;
const cut = (x,y,z) => x > 0 && y > 0 && z > 0;

PHX.add({ id:'core', section:'I · Born in the core', grade:'model (n = 3 polytrope) + estimate', title:'Random walk out of the Sun',
  eq:'density ρ = ρc θ³,  temperature T = Tc θ,  θ from the Lane–Emden equation (n = 3)\n⟨r²⟩ = N ℓ²  ⇒  N = (R/ℓ)²,  t ≈ R² / (ℓ c)',
  text:'The Sun’s interior from Eddington’s standard model, with one octant cut away. The photon is born at the centre, where hydrogen fuses into helium. Points in the volume follow the computed density, so most sit in the core; the cut faces show the layers, and the rings mark where the density falls to 1/10, 1/100 and 1/1000 of its central value. Colour is the computed temperature on a heat scale. The gold path is one photon’s random walk: absorbed and re-emitted in a new direction at every step, it needs about (R/ℓ)² steps, tens of thousands of years, to reach the photosphere, the bright outer shell it finally breaks through.',
  uses:['lmfp','lam'], view:[0.62,0.36,9.6,0],
  make(G, st){ this.G = G; const R = this.R = 2.55;
    /* the volume: point density follows rho = theta^3 (plus the photosphere as a thin shell at R) */
    this.vol = cloud(70000, 0.034); G.add(this.vol);
    fill(this.vol, [-R,R,-R,R,-R,R], (x,y,z) => { if(cut(x,y,z)) return 0; const r = Math.hypot(x,y,z)/R; return r < 1 ? Math.pow(LE.theta(r),3) : 0; }, 1,
      (x,y,z) => { const h = heat(tScale(LE.theta(Math.hypot(x,y,z)/R))); const b = 0.22 + 0.3*(1-LE.theta(Math.hypot(x,y,z)/R)); return [h[0]*b, h[1]*b, h[2]*b]; });
    this.sh = cloud(24000, 0.032); G.add(this.sh);
    fill(this.sh, [-R,R,-R,R,-R,R], (x,y,z) => { if(cut(x,y,z)) return 0; const r = Math.hypot(x,y,z)/R; return Math.abs(r-0.995) < 0.006 ? 1 : 0; }, 1, () => [0.62,0.24,0.05]);
    /* the three cut faces (x=0, y=0, z=0 inside the removed octant): point density follows theta (temperature) so the outer layers stay visible */
    this.faces = cloud(36000, 0.03); G.add(this.faces);
    { const a = this.faces.geometry.attributes, n = a.position.count; let k = 0, t = 0;
      while(k < n && t < n*40){ t++; const u = Math.random()*R, v = Math.random()*R, r = Math.hypot(u,v)/R; if(r >= 1) continue;
        const th = LE.theta(r); if(Math.random() > 0.15 + 0.85*th) continue; const s = k%3;
        const P = s===0 ? [0,u,v] : s===1 ? [u,0,v] : [u,v,0]; a.position.setXYZ(k, P[0], P[1], P[2]);
        const h = heat(tScale(th)); a.color.setXYZ(k, h[0]*0.7, h[1]*0.7, h[2]*0.7); k++; }
      for(let i=k;i<n;i++) a.color.setXYZ(i,0,0,0); a.position.needsUpdate = a.color.needsUpdate = true; }
    /* isodensity rings on the cut faces and around the body (computed radii) */
    this.rings = [0.1, 0.01, 0.001].map(fr => rAt(fr));
    this.rings.forEach((rr, i) => { const r = rr*R, arc = (pl) => { const pts = []; for(let j=0;j<=40;j++){ const a = j/40*Math.PI/2, c = r*Math.cos(a), s = r*Math.sin(a);
        pts.push(pl===0 ? V3(0,c,s) : pl===1 ? V3(c,0,s) : V3(c,s,0)); } return pts; };
      [0,1,2].forEach(pl => G.add(M.line(arc(pl), 0x63d3ff, 0.55 - i*0.12)));
      const eq = []; for(let j=0;j<=120;j++){ const a = Math.PI/2 + j/120*1.5*Math.PI; eq.push(V3(r*Math.cos(a), 0, -r*Math.sin(a))); } G.add(M.line(eq, 0x63d3ff, 0.18)); });
    const outline = (pl) => { const pts = []; for(let j=0;j<=40;j++){ const a = j/40*Math.PI/2, c = R*Math.cos(a), s = R*Math.sin(a); pts.push(pl===0 ? V3(0,c,s) : pl===1 ? V3(c,0,s) : V3(c,s,0)); } return pts; };
    [0,1,2].forEach(pl => G.add(M.line(outline(pl), 0xf2c14e, 0.35)));
    G.add(M.line([V3(0,0,0),V3(R,0,0)],0xf2c14e,0.25)); G.add(M.line([V3(0,0,0),V3(0,R,0)],0xf2c14e,0.25)); G.add(M.line([V3(0,0,0),V3(0,0,R)],0xf2c14e,0.25));
    const lb = ['ρc/10','ρc/100','ρc/1000']; this.rings.forEach((rr,i) => { const L = M.label(lb[i], '#9fe4ff', 0.2); L.position.set(rr*R*0.72+0.05, rr*R*0.72+0.12, 0.02); G.add(L); });
    /* the random walk */
    this.trl = M.trail(2600, 0.09); G.add(this.trl); this.path = []; this.pl = M.line([V3(),V3()], 0xffc23a, 1); G.add(this.pl);
    this.head = cloud(1, 0.35); G.add(this.head);
    this.out = M.line([V3(),V3()],0xffffff,0); G.add(this.out);
    /* birth: a flash at the centre when the pp chain releases the photon; breakout: a flash where the walk crosses the photosphere */
    this.fl = cloud(1400, 0.09); G.add(this.fl); this.fd = []; for(let i=0;i<1400;i++){ const u = 2*Math.random()-1, a = TAU*Math.random(), s = Math.sqrt(1-u*u); this.fd.push(V3(s*Math.cos(a), u, s*Math.sin(a))); }
    this.fo = V3(); this.fage = 9; this.fcol = [1,1,1];
    this.lbB = M.label('4 ¹H → ⁴He + 2e⁺ + 2νe + γ', '#ffffff', 0.22); G.add(this.lbB);
    this.lbS = M.label('photosphere', '#ffb36b', 0.22); this.lbS.position.set(-R*0.62, R*0.86, R*0.2); G.add(this.lbS);
    this.p = V3(); this.steps = 0; this.esc = 0; this.acc = 0; this.sv = 0.085; this.t = 0; },
  enter(){ PHX.base(); this.t = 0; this.G.rotation.set(0,0,0); this.y0 = PHX.S3.view.yaw; this.reset(); },
  reset(){ this.p.set(0,0,0); this.steps = 0; this.esc = 0; M.clearTrail(this.trl); this.path = [V3()]; this.out.material.opacity = 0; this.flash(V3(), [0.55,0.85,1]); },
  flash(o, c){ this.fo.copy(o); this.fage = 0; this.fcol = c; },
  step(dt, S){ dt = Math.max(0, dt); this.t += dt; this.acc += dt; const sv = this.sv, V = PHX.S3.view;
    /* keep the open octant towards the camera while the camera drifts; a drag hands control back to the viewer */
    if(V.auto) this.G.rotation.y = (V.yaw - this.y0) - 0.35*Math.sin(0.25*this.t);
    while(this.acc > 0.006 && !this.esc){ this.acc -= 0.006; const u = 2*Math.random()-1, a = TAU*Math.random(), s = Math.sqrt(1-u*u);
      this.p.add(V3(s*Math.cos(a)*sv, u*sv, s*Math.sin(a)*sv)); this.steps++; M.pushTrail(this.trl, this.p, [1,0.72,0.12]); this.path.push(this.p.clone());
      if(this.path.length > 2600) this.path.shift();
      if(this.p.length() > this.R){ this.esc = 1; this.dir = this.p.clone().normalize(); this.t0 = 0; this.p.copy(this.dir).multiplyScalar(this.R); this.flash(this.p, [1,0.6,0.25]); } }
    if(this.path.length > 1) M.setLine(this.pl, this.path);
    this.fage = Math.max(0, this.fage + dt); { const k = Math.max(0, 1 - this.fage/2), rad = 0.1 + 0.9*Math.sqrt(this.fage), c = this.fcol;
      for(let i=0;i<this.fd.length;i++){ const d = this.fd[i], q = rad*(0.6 + 0.4*((i*0.618)%1)); M.setPt(this.fl, i, V3(this.fo.x + d.x*q, this.fo.y + d.y*q, this.fo.z + d.z*q), [c[0]*k*1.3, c[1]*k*1.3, c[2]*k*1.3]); } M.flush(this.fl);
      this.lbB.visible = this.steps < 400 && !this.esc; this.lbB.position.set(0.15, -0.45, 0.4); }
    M.setPt(this.head, 0, this.p, [1,0.95,0.7]); M.flush(this.head);
    if(this.esc){ this.t0 += dt; M.setLine(this.out, [this.p.clone(), this.p.clone().add(this.dir.clone().multiplyScalar(this.t0*3))]); this.out.material.opacity = 0.95; this.out.material.color.setRGB(...S.rgb);
      if(this.t0 > 1.6) this.reset(); }
    /* each drawn step of length s stands for (s/l)^2 real steps of length l (random-walk coarse graining) */
    const sm = this.sv/this.R*K.R_SUN, per = (sm/S.l)**2;
    return [['model', 'n = 3 polytrope, ξ₁ = '+f(LE.xi1,4)+', ρc/ρ̄ = '+f(1/MEANR,1)], ['rings (r/R)', this.rings.map(r => f(r,2)).join(', ')],
      ['mean free path ℓ', sci(S.l,1)+' m'], ['steps to the surface (R/ℓ)²', sci(S.walk.N,2)],
      ['escape time R²/(ℓc)', sci(S.walk.years,2)+' years'], ['straight-line crossing R/c', f(S.walk.straight,2)+' s'],
      ['released per ⁴He (pp chain)', f(QPP,2)+' MeV'], ['steps drawn', this.steps+(this.esc?' (escaped)':'')], ['one drawn step', sci(per,2)+' real steps']]; }});


})();
