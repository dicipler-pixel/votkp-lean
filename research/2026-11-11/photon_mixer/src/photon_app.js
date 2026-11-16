/* SCRIPT: PHOTON-MIXER-APP
   Ballad of a Dead Photon — 3D mixer for the song (Jeromie Beasley). Built on 3D Mixer Parts v1.
   One feed operator (the photon's wavelength and the settings of each stage) drives eight eyes in film order:
   the photon's life from the Sun's core to a leaf, and a closing scene driving out into the sunset.
   Every readout is computed by PHO (core). */
(function(){
"use strict";
const M = window.Mixer3D, T = M.T, K = window.PHO;
const V3 = (x,y,z) => new T.Vector3(x,y,z);
const RGB = h => [((h>>16)&255)/255, ((h>>8)&255)/255, (h&255)/255];
const f = (x,d) => (x==null || !isFinite(x)) ? '—' : (+x).toFixed(d==null?3:d);
const sci = (x,d) => (+x).toExponential(d==null?2:d).replace('e+','e');
let S3 = null;

/* colour of a wavelength from the parts' colour science; outside 400–700 nm it is shown dim and labelled */
function lamRGB(l){ const q = Math.round(l/10)*10; if(q < 400 || q > 700) return [0.35,0.05,0.04]; return M.colour.wave(q); }
const lamHex = l => (l < 400 ? 'ultraviolet' : l > 700 ? 'infrared' : M.colour.hex(lamRGB(l)));
function base(bg){ S3.scene.background = new T.Color(bg == null ? 0x05070b : bg); S3.scene.fog = null; }
function clear(g){ while(g.children.length){ const c = g.children.pop(); c.traverse(o => { if(o.geometry) o.geometry.dispose(); }); } }
function rod(p, q, color, r, op){ const d = q.clone().sub(p), L = d.length() || 1e-6;
  const m = new T.Mesh(new T.CylinderGeometry(r, r, L, 10, 1, true), new T.MeshStandardMaterial({color, emissive:color, emissiveIntensity:.7, roughness:.4, transparent:op!=null, opacity:op==null?1:op, depthWrite:op==null}));
  m.position.copy(p).add(q).multiplyScalar(.5); m.quaternion.setFromUnitVectors(V3(0,1,0), d.normalize()); return m; }
function glowSprite(size, rgb, op){ const s = new T.Sprite(new T.SpriteMaterial({map:M.sprite, color:new T.Color(rgb[0],rgb[1],rgb[2]), transparent:true, opacity:op==null?1:op, depthWrite:false, blending:T.AdditiveBlending})); s.scale.set(size,size,1); return s; }

/* ---------- feed operator ---------- */
const MIXER = {
  title: 'Ballad of a Dead Photon',
  byline: 'Jeromie Beasley · 3D mixer for the song · physics recomputed live',
  note: 'Film plays the photon’s life in order.',
  feed: {
    params: [
      {id:'lam',  label:'Wavelength at emission (nm)', min:400, max:700, step:10, value:550},
      {id:'lmfp', label:'Mean free path in the Sun, log₁₀ m', min:-5, max:-1, step:0.1, value:-3},
      {id:'th',   label:'Angle of incidence (degrees)', min:0, max:89, step:0.5, value:35},
      {id:'n1',   label:'Index of the glass', min:1.1, max:2.4, step:0.01, value:1.5},
      {id:'dsl',  label:'Slit separation (micrometres)', min:20, max:300, step:5, value:100},
      {id:'z',    label:'Redshift z', min:0, max:3, step:0.01, value:0.5},
      {id:'phi',  label:'Work function of the metal (eV)', min:1.5, max:5, step:0.05, value:2.3},
      {id:'elev', label:'Sun elevation (degrees)', min:-1, max:40, step:0.5, value:4},
      {id:'hop',  label:'Hydraulic hop', min:0, max:1, step:0.05, value:0.5}
    ],
    build(P){
      const lam = P.lam, l = Math.pow(10, P.lmfp), th = P.th*Math.PI/180;
      return { lam, rgb: lamRGB(lam), E: K.energyEV(lam), walk: K.walk(l), l, th, n1: P.n1,
        sn: K.snell(P.n1, 1.0, th), thc: K.critical(P.n1, 1.0), dep: K.evanescentDepth(lam, P.n1, 1.0, th), R: K.fresnelR(P.n1, 1.0, th),
        d: P.dsl*1e-6, z: P.z, rs: K.redshift(lam, P.z), phi: P.phi, pe: K.photoelectric(lam, P.phi), absorb: K.chlA(lam),
        elev: P.elev, hop: P.hop };
    }
  },
  eyes: [], film: ['core','flight','snell','slits','redshift','photoelectric','leaf','sunset']
};

/* ---------- 1. random walk out of the Sun ---------- */
MIXER.eyes.push({ id:'core', section:'I · Born in the core', grade:'estimate (random walk)', title:'Random walk out of the Sun',
  eq:'⟨r²⟩ = N ℓ²   ⇒   N ≈ (R/ℓ)²\nt ≈ N ℓ / c = R² / (ℓ c)',
  text:'In the dense interior a photon is absorbed and re-emitted in a new direction after a short free path ℓ. After N steps its distance from the centre grows only as √N ℓ, so leaving the Sun takes about (R/ℓ)² steps. The real free path changes with depth, so the time is an order of magnitude, not a fixed number.',
  uses:['lmfp','lam'], view:[0.6,0.35,8.5,0],
  make(G){
    this.R = 2.4;
    G.add(M.shell(this.R, 0xff9a3c, 0.10)); G.add(M.shell(this.R*0.55, 0xffd27a, 0.18)); G.add(M.shell(this.R*0.25, 0xfff3c4, 0.35));
    const ring = []; for(let i=0;i<=128;i++){ const a=2*Math.PI*i/128; ring.push(V3(this.R*Math.cos(a),0,this.R*Math.sin(a))); }
    G.add(M.line(ring, 0xffb347, 0.35));
    this.tr = M.trail(900, 0.07); G.add(this.tr); this.ph = glowSprite(0.32, [1,1,1]); G.add(this.ph);
    this.out = M.line([V3(),V3()], 0xffffff, 0.0); G.add(this.out);
    const lb = M.label('surface', '#ffcf7a', 0.28); lb.position.set(0, this.R+0.25, 0); G.add(lb);
    this.p = V3(); this.esc = 0; this.steps = 0; this.acc = 0;
  },
  enter(S){ base(); this.p.set(0,0,0); this.steps = 0; this.esc = 0; M.clearTrail(this.tr); },
  step(dt, S){
    const stepVis = 0.06 + 0.05*(S.l > 1e-3 ? 1 : 0.6);
    this.acc += dt;
    while(this.acc > 0.012 && !this.esc){ this.acc -= 0.012;
      const u = 2*Math.random()-1, a = 2*Math.PI*Math.random(), s = Math.sqrt(1-u*u);
      this.p.add(V3(s*Math.cos(a)*stepVis, u*stepVis, s*Math.sin(a)*stepVis)); this.steps++;
      M.pushTrail(this.tr, this.p, S.rgb);
      if(this.p.length() > this.R){ this.esc = 1; this.dir = this.p.clone().normalize(); this.t0 = 0; } }
    if(this.esc){ this.t0 += dt; const q = this.dir.clone().multiplyScalar(this.R + this.t0*3.2);
      M.setLine(this.out, [this.dir.clone().multiplyScalar(this.R), q]); this.out.material.opacity = 0.9; this.out.material.color.setRGB(...S.rgb);
      this.ph.position.copy(q); if(this.t0 > 1.6){ this.p.set(0,0,0); this.steps = 0; this.esc = 0; M.clearTrail(this.tr); this.out.material.opacity = 0; } }
    else this.ph.position.copy(this.p);
    this.ph.material.color.setRGB(...S.rgb);
    const w = S.walk;
    return [['mean free path ℓ', sci(S.l,1)+' m'], ['steps to the surface (R/ℓ)²', sci(w.N,2)], ['time to escape R²/(ℓc)', sci(w.years,2)+' years'],
      ['the same distance in a straight line', f(w.straight,2)+' s'], ['steps taken in this picture', this.steps], ['photon energy', f(S.E,3)+' eV']];
  }});

/* ---------- 2. eight minutes to the Earth ---------- */
MIXER.eyes.push({ id:'flight', section:'II · Eight minutes', grade:'standard physics, recomputed', title:'Eight minutes to the Earth',
  eq:'t = 1 AU / c = 499.0 s\nalong a light path  dτ² = dt² − dx²/c² = 0',
  text:'Leaving the surface, the photon crosses one astronomical unit in 499 seconds of Earth time. Along its own path the elapsed proper time is zero: a clock cannot ride with light, so in the photon’s terms emission and absorption have no time between them.',
  uses:['lam'], view:[0.0,0.25,10,0],
  make(G){
    const sun = M.orb(1.0, 0xffb347); sun.position.set(-5,0,0); G.add(sun); const sg = glowSprite(4.5,[1,0.7,0.3],0.8); sg.position.set(-5,0,0); G.add(sg);
    const earth = new T.Mesh(new T.SphereGeometry(0.28,32,20), new T.MeshStandardMaterial({color:0x2f6fd6, emissive:0x0b2a66, emissiveIntensity:.5, roughness:.6})); earth.position.set(5,0,0); G.add(earth);
    for(let m=0;m<=8;m++){ const x = -4 + 9*m/8.3165; const tk = M.line([V3(x,-0.5,0),V3(x,-0.35,0)], 0x55657a, 0.9); G.add(tk);
      if(m%2===0){ const lb = M.label(m+' min', '#8a9aab', 0.22); lb.position.set(x,-0.7,0); G.add(lb); } }
    this.wave = M.line([V3(),V3()], 0xffffff, 1); G.add(this.wave); this.ph = glowSprite(0.45,[1,1,1]); G.add(this.ph); this.t = 0;
  },
  enter(){ base(); this.t = 0; },
  step(dt, S){
    this.t += dt; const T8 = 8.3165, frac = (this.t % (T8*0.9)) / (T8*0.9), x0 = -4 + 9*frac;
    const pts = []; const k = 2*Math.PI/(0.12 + 0.0006*(S.lam-400));
    for(let i=0;i<=160;i++){ const x = Math.max(-4, x0 - 2.2 + 2.2*i/160); pts.push(V3(x, 0.18*Math.sin(k*(x - x0)), 0)); }
    M.setLine(this.wave, pts); this.wave.material.color.setRGB(...S.rgb); this.ph.position.set(x0,0,0); this.ph.material.color.setRGB(...S.rgb);
    const fl = K.flight();
    return [['Earth-frame time in flight', f(fl.t*frac,1)+' s of '+f(fl.t,1)+' s'], ['photon proper time', '0 s (null path)'], ['wavelength', S.lam+' nm'],
      ['frequency', sci(K.freq(S.lam),3)+' Hz'], ['energy E = hc/λ', f(S.E,3)+' eV'], ['colour', lamHex(S.lam)]];
  }});

/* ---------- 3. Snell and total internal reflection ---------- */
MIXER.eyes.push({ id:'snell', section:'III · Bent at the glass', grade:'standard physics, recomputed', title:'Refraction and total internal reflection',
  eq:'n₁ sin θ₁ = n₂ sin θ₂\nθc = arcsin(n₂/n₁)\npast θc:  field ∝ exp(−z/δ),  δ = λ / (2π √(n₁² sin²θ₁ − n₂²))',
  text:'Going from glass into air the ray bends away from the normal. Past the critical angle sin θ₂ would have to exceed 1, so nothing propagates into the air: the light is totally reflected and only an evanescent field reaches across the gap, dying off within a fraction of a wavelength.',
  uses:['th','n1','lam'], view:[0.0,0.05,8,0],
  make(G){
    const glass = new T.Mesh(new T.BoxGeometry(8,2.4,2.4), new T.MeshStandardMaterial({color:0x2d5d8a, transparent:true, opacity:0.22, roughness:0.05, metalness:0.1, depthWrite:false}));
    glass.position.set(0,1.2,0); G.add(glass);
    G.add(M.line([V3(-4,0,1.2),V3(4,0,1.2)], 0x63d3ff, 0.6)); G.add(M.line([V3(0,-2.4,0),V3(0,2.4,0)], 0x55657a, 0.5));
    const lg = M.label('glass  n₁', '#8fc7ff', 0.26); lg.position.set(-3.1,2.1,0); G.add(lg); const la = M.label('air  n₂ = 1', '#8a9aab', 0.26); la.position.set(-3.1,-0.4,0); G.add(la);
    this.inc = M.line([V3(),V3()], 0xffffff, 1); this.ref = M.line([V3(),V3()], 0xffffff, 1); this.tra = M.line([V3(),V3()], 0xffffff, 1); G.add(this.inc, this.ref, this.tra);
    this.ev = M.points(600, 0.06); G.add(this.ev); this.ph = glowSprite(0.3,[1,1,1]); G.add(this.ph); this.t = 0;
  },
  enter(){ base(); },
  step(dt, S){
    this.t += dt; const th = S.th, L = 3.2, s = Math.sin(th), c = Math.cos(th), col = S.rgb;
    const A = V3(-L*s, L*c, 0), O = V3(0,0,0);
    M.setLine(this.inc, [A, O]); M.setLine(this.ref, [O, V3(L*s, L*c, 0)]);
    this.inc.material.color.setRGB(...col); this.ref.material.color.setRGB(...col); this.ref.material.opacity = 0.25 + 0.75*S.R;
    const ev = this.ev.geometry.attributes; let n = 0;
    if(!S.sn.tir){ const t2 = S.sn.th2; M.setLine(this.tra, [O, V3(L*Math.sin(t2), -L*Math.cos(t2), 0)]); this.tra.material.opacity = 0.25 + 0.75*(1-S.R); this.tra.material.color.setRGB(...col); }
    else this.tra.material.opacity = 0;
    if(S.sn.tir){ const dVis = Math.min(1.2, 0.25*S.dep/100); for(let i=0;i<600;i++){ const x = -2.5 + 5*(i%60)/59, zz = -(Math.floor(i/60))*0.06, a = Math.exp(zz/dVis)*(0.5+0.5*Math.cos(6*x - 4*this.t));
        ev.position.setXYZ(i, x, zz, 0.6*Math.sin(i)); ev.color.setXYZ(i, col[0]*a, col[1]*a, col[2]*a); n++; } }
    else for(let i=0;i<600;i++) ev.color.setXYZ(i,0,0,0);
    ev.position.needsUpdate = ev.color.needsUpdate = true;
    const u = (this.t % 2)/2; this.ph.position.copy(A.clone().lerp(O, Math.min(1, u*2))); if(u > .5){ this.ph.position.copy(O.clone().lerp(S.sn.tir ? V3(L*s,L*c,0) : V3(L*Math.sin(S.sn.th2||0), -L*Math.cos(S.sn.th2||0), 0), (u-.5)*2)); }
    this.ph.material.color.setRGB(...col);
    return [['angle of incidence θ₁', f(S.th*180/Math.PI,1)+'°'], ['critical angle θc', S.thc==null ? 'none (n₁ ≤ n₂)' : f(S.thc*180/Math.PI,2)+'°'],
      ['transmitted angle θ₂', S.sn.tir ? 'none: total internal reflection' : f(S.sn.th2*180/Math.PI,2)+'°'],
      ['reflected share (Fresnel, unpolarised)', f(100*S.R,1)+' %'], ['evanescent depth δ', S.sn.tir ? f(S.dep,1)+' nm' : '—'], ['wavelength', S.lam+' nm']];
  }});

/* ---------- 4. double slit ---------- */
MIXER.eyes.push({ id:'slits', section:'IV · Both ways', grade:'standard physics, recomputed', title:'Two slits, one photon at a time',
  eq:'I(y) ∝ cos²(π d y / λL) · sinc²(π a y / λL)\nfringe spacing  Δy = λ L / d',
  text:'Photons are sent one at a time. Each lands at a single point, yet the points build the two-slit interference pattern, because each photon’s arrival probability is set by both paths. Asking which slit it used removes the pattern.',
  uses:['lam','dsl'], view:[0.9,0.25,9,0],
  make(G){
    const wall = new T.Mesh(new T.BoxGeometry(0.12,3,3), new T.MeshStandardMaterial({color:0x1b2635, roughness:.8})); wall.position.set(-2,0,0); G.add(wall);
    for(const yz of [-0.35,0.35]){ const sl = new T.Mesh(new T.BoxGeometry(0.14,3,0.08), new T.MeshBasicMaterial({color:0x63d3ff})); sl.position.set(-2,0,yz); G.add(sl); }
    const scr = new T.Mesh(new T.PlaneGeometry(3,3), new T.MeshStandardMaterial({color:0x0c121c, roughness:.9, side:T.DoubleSide})); scr.rotation.y = Math.PI/2; scr.position.set(3,0,0); G.add(scr);
    this.hits = M.points(4000, 0.05); G.add(this.hits); this.n = 0; this.ph = glowSprite(0.3,[1,1,1]); G.add(this.ph); this.t = 0; this.target = V3(3,0,0);
    const ls = M.label('two slits', '#63d3ff', 0.24); ls.position.set(-2,1.75,0); G.add(ls); const lsc = M.label('screen', '#8a9aab', 0.24); lsc.position.set(3,1.75,0); G.add(lsc);
  },
  enter(){ base(); this.n = 0; const a = this.hits.geometry.attributes; a.color.array.fill(0); a.color.needsUpdate = true; },
  change(){ this.enter(); },
  step(dt, S){
    this.t += dt; const lam = S.lam*1e-9, Lm = 1, a = 0.25*S.d, half = 1.4;
    const yScale = 1.4/ (6*K.fringe(lam, S.d, Lm));   /* about six fringes across the visible half-screen */
    const sample = () => { for(let k=0;k<200;k++){ const yv = (2*Math.random()-1)*half, y = yv/yScale; if(Math.random() < K.slitI(y, lam, S.d, a, Lm)) return yv; } return 0; };
    const fire = 0.02; this.acc = (this.acc||0) + dt;
    while(this.acc > fire && this.n < 4000){ this.acc -= fire; const yv = sample(); M.setPt(this.hits, this.n, V3(2.98, (Math.random()*2-1)*1.4, yv), S.rgb); this.n++; this.target.set(3, 0, yv); this.t = 0; }
    M.flush(this.hits); const u = Math.min(1, this.t/0.02); this.ph.position.copy(V3(-4,0,0).lerp(this.target, u)); this.ph.material.color.setRGB(...S.rgb);
    if(this.n >= 4000) this.enter();
    return [['slit separation d', f(S.d*1e6,0)+' µm'], ['wavelength λ', S.lam+' nm'], ['fringe spacing at L = 1 m', f(K.fringe(lam,S.d,1)*1e3,2)+' mm'], ['photons recorded', this.n], ['which-path information', 'none (pattern present)']];
  }});

/* ---------- 5. cosmological redshift ---------- */
MIXER.eyes.push({ id:'redshift', section:'V · The long commute', grade:'standard physics, recomputed', title:'Stretched by the expansion',
  eq:'λ_observed = (1 + z) λ_emitted\nE_observed = E_emitted / (1 + z)',
  text:'Crossing an expanding universe, the wave is stretched by the same factor as the space it travels through. The photon arrives redder and with less energy; nothing is lost along the way in the local sense, the stretch belongs to the expansion.',
  uses:['z','lam'], view:[0.4,0.3,9.5,0],
  make(G){ this.grid = M.grid(8, 16, 0x1f2a38, 0.55); G.add(this.grid); this.wave = M.line([V3(),V3()], 0xffffff, 1); G.add(this.wave); this.gal = [];
    for(let i=0;i<14;i++){ const g = glowSprite(0.25, [0.6,0.7,1], 0.7); g.userData.p = V3((Math.random()-.5)*8, 0.05, (Math.random()-.5)*8); this.gal.push(g); G.add(g); } this.t = 0; },
  enter(){ base(); this.t = 0; },
  step(dt, S){
    this.t += dt; const u = (this.t % 7)/7, a = 1 + S.z*u;
    this.grid.scale.set(a, 1, a); this.gal.forEach(g => g.position.copy(g.userData.p.clone().multiplyScalar(a/(1+S.z*0.5))));
    const lamNow = S.lam*a, col = lamRGB(lamNow), k = 2*Math.PI/(0.35*lamNow/550), pts = [];
    for(let i=0;i<=300;i++){ const x = -4 + 8*i/300; pts.push(V3(x, 0.8 + 0.35*Math.sin(k*x - 3*this.t), 0)); }
    M.setLine(this.wave, pts); this.wave.material.color.setRGB(...col);
    return [['redshift z', f(S.z,2)], ['scale factor now / at emission', f(a,3)], ['wavelength now', f(lamNow,0)+' nm  ('+lamHex(lamNow)+')'],
      ['wavelength on arrival', f(S.rs.lam,0)+' nm'], ['energy on arrival', f(S.rs.E,3)+' eV  (was '+f(S.E,3)+')']];
  }});

/* ---------- 6. photoelectric effect ---------- */
MIXER.eyes.push({ id:'photoelectric', section:'VI · Paid in full', grade:'standard physics, recomputed', title:'Absorbed: the photoelectric effect',
  eq:'K_max = h f − φ\nthreshold  λ₀ = h c / φ',
  text:'At a metal surface the photon gives up all of its energy to one electron. If h f exceeds the work function φ the electron leaves with the remainder as kinetic energy; below threshold no electron leaves, however bright the light. Einstein’s 1905 explanation of this is what the 1921 Nobel Prize cited.',
  uses:['lam','phi'], view:[0.7,0.35,7.5,0],
  make(G){ const slab = new T.Mesh(new T.BoxGeometry(4,0.5,2.6), new T.MeshStandardMaterial({color:0x8d97a6, metalness:0.9, roughness:0.25})); slab.position.set(0,-0.25,0); G.add(slab);
    this.ph = glowSprite(0.4,[1,1,1]); G.add(this.ph); this.el = M.orb(0.09, 0x63d3ff); G.add(this.el); this.tr = M.trail(120, 0.06); G.add(this.tr); this.t = 0; },
  enter(){ base(); this.t = 0; M.clearTrail(this.tr); },
  step(dt, S){
    this.t += dt; const u = (this.t % 3)/3, pe = S.pe;
    if(u < 0.45){ const w = u/0.45; this.ph.visible = true; this.ph.position.set(-2.4*(1-w), 2.4*(1-w), 0); this.el.position.set(0,0.03,0); this.ph.material.color.setRGB(...S.rgb); }
    else { this.ph.visible = false; const w = (u-0.45)/0.55;
      if(pe.emits){ const v = Math.sqrt(pe.K)*1.6; const p = V3(1.2*v*w, 2.6*v*w*(1-0.25*w), 0.4*v*w); this.el.position.copy(p).add(V3(0,0.03,0)); M.pushTrail(this.tr, this.el.position, [0.39,0.83,1]); }
      else { this.el.position.set(0, 0.03 + 0.05*Math.sin(30*w)*(1-w), 0); } }
    if(u < 0.02) M.clearTrail(this.tr);
    return [['photon energy h f', f(pe.E,3)+' eV'], ['work function φ', f(S.phi,2)+' eV'], ['electron leaves?', pe.emits ? 'yes' : 'no (below threshold)'],
      ['electron kinetic energy K_max', f(pe.K,3)+' eV'], ['threshold wavelength λ₀', f(pe.lam0,0)+' nm']];
  }});

/* ---------- 7. leaf ---------- */
MIXER.eyes.push({ id:'leaf', section:'VII · Laid to rest in a leaf', grade:'illustrative absorption shape', title:'Absorbed: a chlorophyll molecule',
  eq:'E = h c / λ   →   excited electron in chlorophyll\nstrong absorption near 430 nm and 662 nm, weak in the green',
  text:'In a leaf the photon is absorbed by chlorophyll and lifts an electron to an excited state; that energy starts the chain that builds sugar. Chlorophyll absorbs blue and red strongly and green weakly, which is why the leaf looks green. The curve drawn here is an approximate shape for chlorophyll a in solution, for illustration.',
  uses:['lam'], view:[0.5,0.45,8,0.3],
  make(G){
    const sh = new T.Shape(); sh.moveTo(0,-1.8); sh.bezierCurveTo(1.6,-0.8,1.5,1.2,0,2.0); sh.bezierCurveTo(-1.5,1.2,-1.6,-0.8,0,-1.8);
    const leaf = new T.Mesh(new T.ShapeGeometry(sh, 40), new T.MeshStandardMaterial({color:0x2f9e4a, emissive:0x0c3a18, emissiveIntensity:.4, roughness:.6, side:T.DoubleSide})); leaf.rotation.x = -Math.PI/2.4; G.add(leaf);
    G.add(M.line([V3(0,-0.2,1.6), V3(0,0.45,-1.7)], 0x7fd38a, 0.7));
    const pts = []; for(let l=400;l<=700;l+=2) pts.push(V3(-3+6*(l-400)/300, 1.7 + 1.1*K.chlA(l), -1.2)); G.add(M.line(pts, 0x9fe0a8, 0.9));
    const lb = M.label('absorption (approximate shape)', '#8a9aab', 0.22); lb.position.set(0, 3.15, -1.2); G.add(lb);
    this.mark = M.orb(0.07, 0xffffff); G.add(this.mark); this.ph = glowSprite(0.4,[1,1,1]); G.add(this.ph); this.burst = glowSprite(1.4,[1,1,1],0); G.add(this.burst);
    this.lev = []; for(let i=0;i<2;i++){ const y = 0.25 + 0.6*i; const ln = M.line([V3(1.7,y,0.3),V3(2.5,y,0.3)], 0x8a9aab, 0.8); G.add(ln); }
    this.e = M.orb(0.07, 0x63d3ff); G.add(this.e); this.t = 0;
  },
  enter(){ base(); this.t = 0; },
  step(dt, S){
    this.t += dt; const u = (this.t % 3)/3, A = Math.min(1, S.absorb);
    this.mark.position.set(-3+6*(S.lam-400)/300, 1.7 + 1.1*K.chlA(S.lam), -1.2); this.mark.material.color.setRGB(...S.rgb); this.mark.material.emissive.setRGB(...S.rgb);
    const absorbed = ((Math.floor(this.t/3)+1) * 0.6180339 % 1) < A;
    if(u < 0.5){ const w = u/0.5; this.ph.visible = true; this.ph.position.set(-1.5*(1-w), 3*(1-w), 0.8*(1-w)); this.ph.material.color.setRGB(...S.rgb); this.burst.material.opacity = 0; this.e.position.set(2.1, 0.25, 0.3); }
    else { const w = (u-0.5)/0.5;
      if(absorbed){ this.ph.visible = false; this.burst.material.color.setRGB(...S.rgb); this.burst.material.opacity = 0.9*(1-w); this.e.position.set(2.1, 0.25 + 0.6*Math.min(1, w*3), 0.3); }
      else { this.ph.visible = true; this.ph.position.set(1.5*w, 3*w, -0.8*w); } }
    return [['wavelength', S.lam+' nm  ('+lamHex(S.lam)+')'], ['photon energy', f(S.E,3)+' eV'], ['relative absorption (shape)', f(A,2)],
      ['this photon', absorbed ? 'absorbed; electron excited' : 'passed through or reflected'], ['why the leaf is green', 'green is absorbed least']];
  }});

/* ---------- 8. the closing scene: out into the sunset ---------- */
const DURAG_SUN = '<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="-256 -256 512 512"><circle r="195" fill="#ffffff"/><path d="M-178,-40 C-170,-160 -80,-205 0,-205 C80,-205 170,-160 178,-40 C120,-62 60,-70 0,-70 C-60,-70 -120,-62 -178,-40 Z" fill="#f4f4f2"/><path d="M-178,-40 C-120,-62 -60,-70 0,-70 C60,-70 120,-62 178,-40 L174,-22 C118,-44 58,-52 0,-52 C-58,-52 -118,-44 -174,-22 Z" fill="#dcdcd8"/><path d="M0,-205 L0,-75" stroke="#cfcfca" stroke-width="5"/><path d="M150,-60 C200,-30 215,40 205,120 C200,160 190,190 175,215 L150,205 C168,170 178,120 180,70 C182,20 170,-20 140,-45 Z" fill="#f4f4f2"/><path d="M175,-55 C225,-15 245,60 240,140 L215,138 C218,70 205,10 160,-40 Z" fill="#e4e4e0"/><path d="M-115,-28 L-30,-6" stroke="#4a2306" stroke-width="13" stroke-linecap="round"/><path d="M115,-28 L30,-6" stroke="#4a2306" stroke-width="13" stroke-linecap="round"/><path d="M-108,22 C-90,6 -50,6 -32,20 C-50,30 -90,32 -108,22 Z" fill="#ffffff"/><path d="M108,22 C90,6 50,6 32,20 C50,30 90,32 108,22 Z" fill="#ffffff"/><circle cx="-62" cy="20" r="9" fill="#2a1403"/><circle cx="62" cy="20" r="9" fill="#2a1403"/><path d="M-12,40 C-6,62 -10,74 -20,80 M12,40 C6,62 10,74 20,80" fill="none" stroke="#c98a2a" stroke-width="5" stroke-linecap="round"/><path d="M-55,118 C-30,108 30,108 55,118" fill="none" stroke="#4a2306" stroke-width="9" stroke-linecap="round"/></svg>';
function svgTexture(svg){ const tex = new T.Texture(); const img = new Image(); img.onload = () => { const c = document.createElement('canvas'); c.width = c.height = 512; c.getContext('2d').drawImage(img,0,0,512,512); tex.image = c; tex.colorSpace = T.SRGBColorSpace; tex.needsUpdate = true; };
  img.src = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg); return tex; }
function palm(h){ const g = new T.Group(), mat = new T.MeshStandardMaterial({color:0x140a12, roughness:1});
  let p = V3(0,0,0); const lean = (Math.random()-.5)*0.5;
  for(let i=0;i<8;i++){ const q = p.clone().add(V3(lean*0.12*i, h/8, 0)); g.add(rod(p, q, 0x140a12, 0.07 - 0.004*i)); p = q; }
  for(let k=0;k<7;k++){ const a = 2*Math.PI*k/7, fr = new T.Mesh(new T.ConeGeometry(0.18, 1.6, 4, 1), mat); fr.scale.set(1,1,0.2);
    fr.position.copy(p).add(V3(0.6*Math.cos(a), -0.15, 0.6*Math.sin(a))); fr.rotation.set(0, -a, Math.PI/2 + 0.45); fr.rotateOnAxis(V3(0,1,0), 0); g.add(fr); }
  return g; }
function lowrider(){
  const car = new T.Group(), body = new T.Group(); car.add(body);
  const paint = new T.MeshStandardMaterial({color:0x5b1f7a, metalness:0.7, roughness:0.22, emissive:0x1a0624, emissiveIntensity:0.4});
  const chrome = new T.MeshStandardMaterial({color:0xe9eef5, metalness:1, roughness:0.08});
  const glass = new T.MeshStandardMaterial({color:0x0b0f18, metalness:0.3, roughness:0.05, transparent:true, opacity:0.45, depthWrite:false});
  const b = (w,h,d,m,x,y,z) => { const o = new T.Mesh(new T.BoxGeometry(w,h,d), m); o.position.set(x,y,z); body.add(o); return o; };
  b(1.9,0.42,4.8,paint, 0,0.42,0);                     /* lower body */
  b(1.86,0.12,1.7,paint, 0,0.69,-1.45);                /* hood */
  b(1.86,0.12,1.2,paint, 0,0.69,1.75);                 /* trunk deck */
  b(1.7,0.5,1.9,glass, 0,0.92,0.25);                   /* cabin glass */
  b(1.74,0.07,1.95,paint, 0,1.19,0.25);                /* roof */
  b(2.0,0.12,0.12,chrome, 0,0.3,-2.44); b(2.0,0.12,0.12,chrome, 0,0.3,2.44);       /* bumpers */
  b(0.05,0.05,4.6,chrome, 0.96,0.5,0); b(0.05,0.05,4.6,chrome, -0.96,0.5,0);      /* side trim */
  const tl = new T.MeshStandardMaterial({color:0xff2a2a, emissive:0xff2a2a, emissiveIntensity:1.2});
  b(0.4,0.12,0.04,tl, 0.65,0.5,2.42); b(0.4,0.12,0.04,tl, -0.65,0.5,2.42);
  const hl = new T.MeshStandardMaterial({color:0xfff2c4, emissive:0xfff2c4, emissiveIntensity:1.0});
  b(0.3,0.14,0.04,hl, 0.6,0.46,-2.42); b(0.3,0.14,0.04,hl, -0.6,0.46,-2.42);
  const driver = glowSprite(1.1, [1,1,1]); driver.position.set(-0.4, 1.02, 0.15); driver.renderOrder = 5; body.add(driver);
  const wheels = [];
  for(const [x,z] of [[0.92,-1.55],[-0.92,-1.55],[0.92,1.55],[-0.92,1.55]]){
    const w = new T.Group(); w.position.set(x,0.33,z);
    const tire = new T.Mesh(new T.CylinderGeometry(0.33,0.33,0.24,28), new T.MeshStandardMaterial({color:0x0b0b0e, roughness:0.9})); tire.rotation.z = Math.PI/2; w.add(tire);
    const ww = new T.Mesh(new T.TorusGeometry(0.24,0.045,10,32), new T.MeshStandardMaterial({color:0xf4f4f2, roughness:0.5})); ww.rotation.y = Math.PI/2; ww.position.x = Math.sign(x)*0.125; w.add(ww);
    const hub = new T.Group(); hub.position.x = Math.sign(x)*0.13;
    for(let s=0;s<12;s++){ const sp = new T.Mesh(new T.BoxGeometry(0.01,0.36,0.012), chrome); sp.rotation.x = Math.PI*s/12; hub.add(sp); }
    const cap = new T.Mesh(new T.CylinderGeometry(0.06,0.06,0.04,16), chrome); cap.rotation.z = Math.PI/2; hub.add(cap); w.add(hub);
    car.add(w); wheels.push(w); }
  car.userData = {body, wheels, driver}; return car; }
const skyVS = 'varying vec3 vW; void main(){ vec4 w = modelMatrix*vec4(position,1.0); vW = w.xyz; gl_Position = projectionMatrix*viewMatrix*w; }';
const skyFS = 'uniform vec3 top; uniform vec3 hor; uniform vec3 sunC; uniform vec3 sunD; varying vec3 vW; void main(){ vec3 d = normalize(vW); float h = max(d.y, 0.0); vec3 c = mix(hor, top, pow(h, 0.55)); float g = max(dot(d, sunD), 0.0); c += sunC*(0.55*pow(g, 18.0) + 0.25*pow(g, 3.0)); if(d.y < 0.0) c = mix(hor*0.55, vec3(0.04,0.02,0.05), min(1.0, -d.y*8.0)); gl_FragColor = vec4(c, 1.0); }';
MIXER.eyes.push({ id:'sunset', section:'VIII · Out into the sunset', grade:'standard physics, recomputed (closing scene)', title:'Out into the sunset',
  eq:'sunlight seen = Planck(5772 K) × exp(−τ_R(λ) X)\nτ_R ∝ λ⁻⁴ (Rayleigh),  X = airmass at elevation h',
  text:'The closing scene of the song. The colour of the setting Sun is computed: the Sun’s Planck spectrum is dimmed by Rayleigh scattering through the air it crosses, which grows as the Sun sinks. Short wavelengths are scattered out of the beam first, so the low Sun turns orange and then red.',
  uses:['elev','hop'], view:[0.0,0.12,9.5,1.0],
  make(G){
    this.sky = new T.Mesh(new T.SphereGeometry(95, 48, 24), new T.ShaderMaterial({vertexShader:skyVS, fragmentShader:skyFS, side:T.BackSide, depthWrite:false,
      uniforms:{top:{value:new T.Color()}, hor:{value:new T.Color()}, sunC:{value:new T.Color()}, sunD:{value:V3(0,0.05,-1)}}})); G.add(this.sky);
    const ground = new T.Mesh(new T.PlaneGeometry(400,400), new T.MeshStandardMaterial({color:0x1a0f1e, roughness:1})); ground.rotation.x = -Math.PI/2; G.add(ground);
    const road = new T.Mesh(new T.PlaneGeometry(7,400), new T.MeshStandardMaterial({color:0x121218, roughness:0.85})); road.rotation.x = -Math.PI/2; road.position.y = 0.01; G.add(road);
    this.dash = []; for(let i=0;i<30;i++){ const d = new T.Mesh(new T.BoxGeometry(0.14,0.02,1.4), new T.MeshBasicMaterial({color:0xf2c14e})); d.position.set(0,0.02,-i*4); this.dash.push(d); G.add(d); }
    this.palms = []; for(let i=0;i<16;i++){ const p = palm(4 + Math.random()*2.5); p.position.set((i%2 ? 1 : -1)*(5 + Math.random()*3), 0, -i*9); this.palms.push(p); G.add(p); }
    this.sunGlow = glowSprite(30, [1,0.6,0.3], 0.9); G.add(this.sunGlow);
    this.sun = new T.Sprite(new T.SpriteMaterial({map:svgTexture(DURAG_SUN), transparent:true, depthWrite:false, fog:false})); this.sun.scale.set(16,16,1); G.add(this.sun);
    this.car = lowrider(); G.add(this.car);
    this.hemi = new T.HemisphereLight(0xffffff, 0x1a0f1e, 0.6); G.add(this.hemi); const fill = new T.PointLight(0xc79bff, 40, 30, 1.6); fill.position.set(2.5, 3.5, 7); G.add(fill); this.keyL = new T.DirectionalLight(0xffffff, 1.4); G.add(this.keyL);
    this.t = 0; this.WL = M.colour.WL;
  },
  enter(){ base(0x0a0612); S3.scene.fog = new T.Fog(0x3a1a2a, 30, 110); this.t = 0; },
  step(dt, S){
    this.t += dt; const h = S.elev, hr = h*Math.PI/180;
    const spec = K.sunSpectrum(h, this.WL), top = K.sunSpectrum(90, this.WL), Lr = M.colour.spec(spec), L0 = M.colour.spec(top);
    const sunRGB = M.colour.norm(Lr), dim = Math.min(1, M.colour.lum(Lr)/M.colour.lum(L0));
    const sd = V3(0, Math.sin(hr), -Math.cos(hr)).normalize(), sunPos = sd.clone().multiplyScalar(85);
    this.sun.position.copy(sunPos); this.sunGlow.position.copy(sunPos); this.sun.material.color.setRGB(sunRGB[0], sunRGB[1], sunRGB[2]); this.sunGlow.material.color.setRGB(sunRGB[0], sunRGB[1]*0.85, sunRGB[2]*0.7);
    const u = this.sky.material.uniforms, warm = Math.max(0, Math.min(1, 1 - h/30));
    u.sunD.value.copy(sd); u.sunC.value.setRGB(sunRGB[0], sunRGB[1], sunRGB[2]);
    u.hor.value.setRGB(0.25 + 0.7*sunRGB[0]*(0.5+0.5*warm), 0.15 + 0.45*sunRGB[1], 0.25 + 0.35*sunRGB[2]);
    u.top.value.setRGB(0.05 + 0.15*(1-warm), 0.06 + 0.25*(1-warm), 0.18 + 0.45*(1-warm));
    S3.scene.fog.color.setRGB(u.hor.value.r*0.6, u.hor.value.g*0.5, u.hor.value.b*0.6);
    this.keyL.position.copy(sunPos); this.keyL.color.setRGB(sunRGB[0], sunRGB[1], sunRGB[2]); this.keyL.intensity = 0.6 + 1.6*dim; this.hemi.color.setRGB(u.hor.value.r, u.hor.value.g, u.hor.value.b);
    const v = 9; for(const d of this.dash){ d.position.z += v*dt; if(d.position.z > 12) d.position.z -= 120; }
    for(const p of this.palms){ p.position.z += v*dt; if(p.position.z > 14) p.position.z -= 144; }
    const cu = this.car.userData; cu.wheels.forEach(w => w.children[2].rotation.x -= v*dt/0.33);
    const hop = S.hop*Math.max(0, Math.sin(this.t*2.6))**3; cu.body.position.y = 0.35*hop; cu.body.rotation.x = 0.16*hop;
    cu.driver.material.color.setRGB(1, 0.95, 0.8); cu.driver.scale.setScalar(1.05 + 0.1*Math.sin(this.t*6));
    const X = K.airmass(Math.max(h,-0.5)), T450 = Math.exp(-K.tauRayleigh(450)*X), T650 = Math.exp(-K.tauRayleigh(650)*X);
    return [['Sun elevation', f(h,1)+'°'], ['airmass X', f(X,2)], ['Rayleigh transmission at 450 nm', f(100*T450,1)+' %'], ['Rayleigh transmission at 650 nm', f(100*T650,1)+' %'],
      ['red-to-blue survival ratio', f(T650/T450,2)], ['computed colour of the Sun', M.colour.hex(sunRGB)]];
  }});

/* ---------- run on the parts, keeping a handle on the stage ---------- */
MIXER.eyes.forEach(e => { const mk = e.make; e.make = function(G, st){ S3 = st; return mk.call(this, G, st); }; });
M.run(MIXER);
})();
