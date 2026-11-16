/* SCRIPT: PHOTON-MIXER-V2-SCENE-RESONANCE */
(function(){
"use strict";
const PHX = window.PHX, { M, T, K, V3, f, sci, TAU, hue, lamRGB, lamName, cloud, clearCloud, fill, ringLine, LE } = PHX;
/* exact hydrogen orbitals, atomic units (Bohr radius a0 = 1), both normalised to 1 */
const psi1s = r => Math.exp(-r)/Math.sqrt(Math.PI);
const psi2pz = (r, z) => z*Math.exp(-r/2)/Math.sqrt(32*Math.PI);
/* hydrogen 1s -> 2p with the reduced-mass Rydberg (Lyman alpha, 121.567 nm in vacuum) */
const RY_EV = 13.605693*0.99945568, GAP = 0.75*RY_EV, LAM_GAP = 1239.84198/GAP;
const BEAT_FS = 4.135667696/GAP;                 /* h/ΔE in fs */
const DZ = 128*Math.SQRT2/243;                   /* <1s|z|2pz> in a0 = 0.7449 */
const N = 90000, SC = 0.24;                      /* points; display units per a0 */
/* the leaf: chlorophyll a, approximate band peaks in solution near 430 nm (Soret) and 662 nm (Qy) */
const QY_NM = 662, QY_EV = 1239.84198/QY_NM, OM_EV = 0.03;   /* drive strength ħΩ set to the Qy band half-width, about 0.03 eV */
const NL = 2400, LX = 0, LY0 = -0.5, LY1 = 0.5, LR = 0.45;
function chlBand(l){ const a = K.chlA(l)/K.chlA(430);
  const where = Math.abs(l-430) <= 30 ? 'Soret (blue) band' : Math.abs(l-662) <= 22 ? 'Qy (red) band' : (l > 480 && l < 640) ? 'green gap: weakly absorbed' : 'band edge';
  return [where, a]; }
/* 7 ---------- absorption needs resonance: hydrogen 1s -> 2p, exact orbitals ---------- */
PHX.add({ id:'resonance', section:'VII · Laid to rest', grade:'exact orbitals; resonance rule recomputed', title:'Absorption needs resonance',
  eq:'ψ(t) = cos(Ωt/2) ψ₁ₛ − i sin(Ωt/2) e^{−iωt} ψ₂ₚ   (on resonance)\nabsorbs only when h c / λ = E₂ − E₁ = 10.2 eV  (λ = 121.6 nm)\nP_excited = Ω²/(Ω²+Δ²) · sin²(√(Ω²+Δ²) t / 2)',
  text:'A photon can only be absorbed if its energy matches a gap in the absorber. The large cloud is a hydrogen atom with its exact orbitals: driven on resonance, the electron moves from the round 1s state toward the 2p state, and its density sloshes along the field axis at the beat frequency. A leaf follows the same rule with chlorophyll a, which absorbs strongly near 430 nm and 662 nm and only weakly in the green, so green light is sent back and leaves look green. The small inset is a two-level model of the 662 nm gap driven at the chosen wavelength: the fraction lifted to the upper ring is the Rabi formula, large only near resonance. The absorbed energy lifts an electron, and photosynthesis stores it as sugar.',
  uses:['lam'], view:[0.6,0.16,7.0,0],
  make(G, st){
    this.c = cloud(N, 0.03); G.add(this.c);
    /* importance-sample once from the equal mixture q = ½|ψ1s|² + ½|ψ2pz|² (both exact):
       1s radial r²e^{-2r} = Gamma(3, rate 2), isotropic;  2pz radial r⁴e^{-r} = Gamma(5, 1), cos θ with pdf ∝ cos²θ */
    this.s = new Float32Array(N); this.p = new Float32Array(N); this.q = new Float32Array(N);
    const pa = this.c.geometry.attributes.position, lnU = () => Math.log(Math.random() + 1e-12);
    for(let i=0;i<N;i++){ let r, u;
      if(i & 1){ r = -(lnU()+lnU()+lnU()+lnU()+lnU()); const v = Math.cbrt(Math.random()); u = Math.random() < 0.5 ? -v : v; }
      else { r = -(lnU()+lnU()+lnU())/2; u = 2*Math.random()-1; }
      const a = TAU*Math.random(), st = Math.sqrt(1-u*u), x = r*st*Math.cos(a), y = r*st*Math.sin(a), z = r*u;
      const s = psi1s(r), p = psi2pz(r, z); this.s[i] = s; this.p[i] = p; this.q[i] = 0.5*s*s + 0.5*p*p;
      pa.setXYZ(i, x*SC, z*SC, y*SC); }   /* atomic z (the field axis) is drawn vertical */
    pa.needsUpdate = true;
    /* guides: the field axis and a ring at the dipole moment <z>(t) */
    G.add(M.line([V3(0,-3.2,0), V3(0,3.2,0)], 0x63d3ff, 0.22));
    this.ring = ringLine(0.32, 0, 0xffffff, 0.75); G.add(this.ring);
    const lz = M.label('field axis z', '#63d3ff', 0.26); lz.position.set(0.15, 3.1, 0); G.add(lz);
    const ld = M.label('dipole ⟨z⟩ × 3', '#ffffff', 0.22); ld.position.set(0.85, 0, 0); this.ld = ld; G.add(ld);
    /* two-level inset for the chlorophyll Qy gap: lower ring = ground state, upper ring = excited state; each point is one molecule */
    this.ig = new T.Group(); G.add(this.ig);   /* kept beside the atom on the camera's right */
    this.lf = cloud(NL, 0.035); this.ig.add(this.lf); this.lu = new Float32Array(NL); this.la = new Float32Array(NL);
    for(let i=0;i<NL;i++){ this.lu[i] = Math.random(); this.la[i] = TAU*Math.random(); }
    const g0 = ringLine(LR, LY0, 0x8fa6bf, 0.35), g1 = ringLine(LR, LY1, 0xff5040, 0.35); this.ig.add(g0); this.ig.add(g1);
    const l0 = M.label('chlorophyll a · Qy gap 662 nm', '#ffffff', 0.19); l0.position.set(0, LY1 + 0.4, 0); this.ig.add(l0);
    const l1 = M.label('excited', '#ff8070', 0.18), l2 = M.label('ground', '#8fa6bf', 0.18); l1.position.set(LR + 0.45, LY1, 0); l2.position.set(LR + 0.4, LY0, 0); this.ig.add(l1); this.ig.add(l2);
    this.t = 0; },
  enter(){ PHX.base(); PHX.S3.world.rotation.set(0,0,0); this.t = 0; },
  step(dt, S){ this.t += dt;
    /* shown slowed: Rabi angle Ωt advances 0.4 rad/s (full 1s -> 2p -> 1s cycle ≈ 16 s), beat ωt 4.2 rad/s (period ≈ 1.5 s) */
    const W = this.t*0.4, wt = this.t*4.2, a1 = Math.cos(W/2), a2 = Math.sin(W/2), pop = a2*a2, sw = Math.sin(wt), cw = Math.cos(wt);
    const ca = this.c.geometry.attributes.color.array, s = this.s, p = this.p, q = this.q, g = 0.26;
    for(let i=0, j=0;i<N;i++, j+=3){
      /* ψ = a1 ψ1s − i a2 e^{−iωt} ψ2p  ⇒  Re = a1 s − a2 p sin ωt,  Im = −a2 p cos ωt */
      const re = a1*s[i] - a2*p[i]*sw, im = -a2*p[i]*cw, w = (re*re + im*im)/q[i];   /* density / sampling density, 0 ≤ w ≤ 4 */
      /* per-point brightness so that the drawn intensity (point density × brightness) is |ψ|^1.2, a gamma like the films' log scale */
      let h = Math.atan2(im, re)/TAU; h = (h - Math.floor(h))*6; const k = Math.floor(h), fr = h - k, b = Math.min(1.6, g*Math.pow(w, 0.6)*Math.pow(q[i]/0.005, -0.4));
      let R, Gc, B;
      switch(k){ case 0: R=1; Gc=fr; B=0; break; case 1: R=1-fr; Gc=1; B=0; break; case 2: R=0; Gc=1; B=fr; break;
                 case 3: R=0; Gc=1-fr; B=1; break; case 4: R=fr; Gc=0; B=1; break; default: R=1; Gc=0; B=1-fr; }
      ca[j] = R*b; ca[j+1] = Gc*b; ca[j+2] = B*b; }
    this.c.geometry.attributes.color.needsUpdate = true;
    const zd = -2*a1*a2*sw*DZ;   /* <z>(t) in a0 */
    this.ring.position.y = zd*SC*3; this.ld.position.y = zd*SC*3;
    /* leaf inset: Rabi formula at the feed's detuning from the Qy gap (same slowed clock: ΩT advances 0.8 rad/s) */
    const dq = S.E - QY_EV, Wg = Math.hypot(OM_EV, dq), Pq = (OM_EV/Wg)**2*Math.sin(Wg/OM_EV*this.t*0.8/2)**2, la = this.lf.geometry.attributes, rc = lamRGB(QY_NM);
    for(let i=0;i<NL;i++){ const up = this.lu[i] < Pq, y = up ? LY1 : LY0, rr = LR*(0.92 + 0.16*((i*0.618)%1)), a = this.la[i] + this.t*0.15;
      la.position.setXYZ(i, LX + rr*Math.cos(a), y, rr*Math.sin(a)); if(up) la.color.setXYZ(i, rc[0]*0.9, rc[1]*0.9, rc[2]*0.9); else la.color.setXYZ(i, 0.16, 0.2, 0.26); }
    la.position.needsUpdate = la.color.needsUpdate = true;
    const yw = PHX.S3.view.yaw; this.ig.position.set(2.25*Math.cos(yw), -0.3, -2.25*Math.sin(yw)); this.ig.rotation.y = yw;
    const det = S.E - GAP, cb = chlBand(S.lam);
    return [['photon energy (feed)', f(S.E,3)+' eV  ('+S.lam+' nm)'], ['hydrogen 1s → 2p gap', f(GAP,3)+' eV  ('+f(LAM_GAP,1)+' nm)'], ['detuning', f(det,3)+' eV'],
      ['absorbed by this atom?', Math.abs(det) < 1e-3 ? 'yes' : 'no: off resonance'], ['shown', 'resonant drive (Rabi), slowed'], ['population in 2p', f(pop,2)],
      ['beat period h/ΔE', f(BEAT_FS,4)+' fs'],
      ['chlorophyll a at this λ', cb[0]+', absorbance '+f(cb[1],2)+' of the 430 nm peak'], ['detuning from Qy (662 nm)', f(dq,3)+' eV'],
      ['inset: excited fraction now / at most', f(Pq,3)+' / '+f((OM_EV/Wg)**2,3)], ['dipole ⟨z⟩ (ring, ×3)', f(zd,3)+' a₀'], ['colour', 'atom: phase of ψ relative to 1s, brightness |ψ|^1.2 · inset: 662 nm']]; }});


})();
