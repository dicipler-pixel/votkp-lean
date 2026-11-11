/* SCRIPT: PHOTON-MIXER-V2-SCENE-REDSHIFT */
(function(){
"use strict";
const PHX = window.PHX, { M, T, K, V3, f, sci, TAU, hue, lamRGB, lamName, cloud, clearCloud, fill, ringLine, LE } = PHX;
/* 5 ---------- the packet stretched by the expansion ----------
   Flat ΛCDM, H0 = 70 km/s/Mpc, Ωm = 0.3, ΩΛ = 0.7 (radiation neglected).
   H(a) = H0 sqrt(Ωm a⁻³ + ΩΛ); cosmic time t(a) = ∫ da/(a H); comoving distance travelled by light χ(a) = c ∫ da/(a² H).
   The animation runs uniformly in cosmic time from emission (a = 1/(1+z), today's a = 1) to arrival.
   Galaxies sit at fixed comoving lattice points, so their separations grow ∝ a; each galaxy keeps its own size (bound).
   The packet's wavelength and length grow ∝ a and its field amplitude falls ∝ 1/a; its colour is its current wavelength. */
const H0 = 70, OM = 0.3, OL = 0.7, C = 299792.458, MPC_GLY = 3.26156e-3;     /* km/s/Mpc, km/s, Gly per Mpc */
const TH = 977.792/H0;                                                       /* Hubble time 1/H0 in Gyr */
const E = a => Math.sqrt(OM/(a*a*a) + OL);
/* integrate from a0 to 1 with n Simpson panels; returns arrays a[i], t[i] (Gyr since emission), chi[i] (Mpc travelled) */
function history(z, n){ const a0 = 1/(1+z), A = [], Tt = [], X = []; let t = 0, x = 0; const h = (1-a0)/n;
  const ft = a => 1/(a*E(a)), fx = a => 1/(a*a*E(a));
  A.push(a0); Tt.push(0); X.push(0);
  for(let i=0;i<n;i++){ const a = a0 + i*h, m = a + h/2, b = a + h;
    t += h/6*(ft(a) + 4*ft(m) + ft(b)); x += h/6*(fx(a) + 4*fx(m) + fx(b)); A.push(b); Tt.push(t*TH); X.push(x*C/H0); }
  return { A, T:Tt, X, age: Tt[n], chi: X[n] }; }
/* colour of a monochromatic line from the CIE 1931 2° colour-matching functions (10 nm table, 380–780 nm, linear interpolation),
   converted to linear sRGB, negatives clipped, scaled to max 1. Brightness b follows the luminosity function ȳ (square root),
   floored at 0.3 so a packet that has been stretched past 700 nm stays visible (drawn dim red; real infrared is invisible). */
const CIE = [[.001368,.000039,.00645],[.004243,.00012,.02005],[.01431,.000396,.06785],[.04351,.00121,.2074],[.13438,.004,.6456],[.2839,.0116,1.3856],[.34828,.023,1.74706],
  [.3362,.038,1.77211],[.2908,.06,1.6692],[.19536,.09098,1.28764],[.09564,.13902,.81295],[.03201,.20802,.46518],[.0049,.323,.272],[.0093,.503,.1582],[.06327,.71,.07825],
  [.1655,.862,.04216],[.2904,.954,.0203],[.43345,.99495,.00875],[.5945,.995,.0039],[.7621,.952,.0021],[.9163,.87,.00165],[1.0263,.757,.0011],[1.0622,.631,.0008],
  [1.0026,.503,.00034],[.85445,.381,.00019],[.6424,.265,.00005],[.4479,.175,.00002],[.2835,.107,0],[.1649,.061,0],[.0874,.032,0],[.04677,.017,0],[.0227,.00821,0],
  [.011359,.004102,0],[.00579,.002091,0],[.002899,.001047,0],[.00144,.00052,0],[.00069,.000249,0],[.000332,.00012,0],[.000166,.00006,0],[.000083,.00003,0],[.000042,.000015,0]];
function lineColour(nm){ const x = Math.max(0, Math.min(40, (nm-380)/10)), i = Math.min(39, Math.floor(x)), w = x - i, q = [0,1,2].map(k => CIE[i][k]*(1-w) + CIE[i+1][k]*w);
  if(nm > 780) q[0] = 0.000042, q[1] = 0.000015, q[2] = 0;
  const rgb = [3.2406*q[0]-1.5372*q[1]-0.4986*q[2], -0.9689*q[0]+1.8758*q[1]+0.0415*q[2], 0.0557*q[0]-0.2040*q[1]+1.0570*q[2]].map(v => Math.max(0, v));
  const m = Math.max(...rgb, 1e-12), b = Math.max(0.3, Math.min(1, Math.sqrt((nm > 780 ? 0 : q[1])/0.2)));
  return { rgb: rgb.map(v => v/m), b }; }
const hexOf = c => '#'+c.map(v => Math.round(M.colour.enc(v)*255).toString(16).padStart(2,'0')).join('');
const bandOf = nm => nm < 380 ? 'ultraviolet' : nm > 780 ? 'infrared' : nm > 700 ? 'deep red, edge of vision' : 'visible';
/* lattice of galaxies (comoving): NX × NY × NZ nodes, spacing D in drawn units at a = 1 */
const NX = 7, NY = 3, NZ = 4, D = 1.12, GP = 450;   /* GP points per galaxy */

PHX.add({ id:'redshift', section:'V · The long commute', grade:'standard physics, recomputed (flat ΛCDM)', title:'Stretched by the expansion',
  eq:'λ_observed = (1 + z) λ_emitted,   E_observed = E_emitted / (1 + z)\nH(a) = H₀ √(Ωm a⁻³ + ΩΛ),   a = 1/(1 + z)',
  text:'A lattice of galaxies at fixed comoving positions: the space between them grows with the scale factor a while each galaxy, held together by its own gravity, keeps its size. The wave packet crosses the lattice from the moment of emission to today. Its wavelength grows in proportion to a and its field amplitude falls as 1/a, so it arrives longer, weaker and redder, with less energy, yet the white dots show that the number of crests never changes: only the spacing between them grows. The packet’s colour is its current wavelength; the animation runs evenly in cosmic time from flat ΛCDM.',
  uses:['z','lam'], view:[0.5,0.32,9.4,0],
  make(G, st){ this.G = G;
    /* galaxies: each a small flattened disc of points, a fixed physical size; colours a neutral starlight white */
    const n = NX*NY*NZ; this.gal = cloud(n*GP, 0.036); G.add(this.gal); this.nodes = []; this.loc = [];
    for(let i=0;i<NX;i++) for(let j=0;j<NY;j++) for(let k=0;k<NZ;k++){ const c = V3((i-(NX-1)/2)*D, (j-(NY-1)/2)*D, (k-(NZ-1)/2)*D);
      c.x += (Math.random()-0.5)*0.25*D; c.y += (Math.random()-0.5)*0.25*D; c.z += (Math.random()-0.5)*0.25*D; this.nodes.push(c);
      const ax = V3(Math.random()-0.5, Math.random()-0.5, Math.random()-0.5).normalize(), b1 = V3(1,0,0).cross(ax).normalize(), b2 = ax.clone().cross(b1);
      const warm = Math.random();
      for(let p=0;p<GP;p++){ const r = 0.075*-Math.log(Math.random()+1e-6), th = TAU*Math.random(), h = (Math.random()-0.5)*0.16*Math.exp(-r/0.05);   /* exponential disc */
        const v = b1.clone().multiplyScalar(r*Math.cos(th)).add(b2.clone().multiplyScalar(r*Math.sin(th))).add(ax.clone().multiplyScalar(h));
        this.loc.push(v); const br = Math.exp(-r/0.05)*0.3 + 0.14, idx = this.loc.length-1;
        this.gal.geometry.attributes.color.setXYZ(idx, br*(0.85+0.15*warm), br*(0.85), br*(0.95-0.25*warm)); } }
    this.gal.geometry.attributes.color.needsUpdate = true;
    /* the comoving grid: lines joining neighbouring nodes, drawn as segments, scaled with a */
    const seg = []; const id = (i,j,k) => (i*NY + j)*NZ + k;
    for(let i=0;i<NX;i++) for(let j=0;j<NY;j++) for(let k=0;k<NZ;k++){ if(i<NX-1) seg.push([id(i,j,k), id(i+1,j,k)]); if(j<NY-1) seg.push([id(i,j,k), id(i,j+1,k)]); if(k<NZ-1) seg.push([id(i,j,k), id(i,j,k+1)]); }
    this.seg = seg; const geo = new T.BufferGeometry(); geo.setAttribute('position', new T.BufferAttribute(new Float32Array(seg.length*6), 3));
    this.grid = new T.LineSegments(geo, new T.LineBasicMaterial({color:0x63d3ff, transparent:true, opacity:0.24})); this.grid.frustumCulled = false; G.add(this.grid);
    /* the packet, sampled once in its own frame (unit length along x); stretched by the object's scale */
    this.pk = cloud(40000, 0.032); G.add(this.pk);
    { const a = this.pk.geometry.attributes, N = a.position.count, k = TAU/0.16, sg = 0.5;
      this.pkFrac = new Float32Array(N);
      for(let i=0;i<N;i++){ let x, e; for(let r=0;r<30;r++){ x = sg*3.2*(2*Math.random()-1); e = Math.exp(-x*x/(2*sg*sg)); if(Math.random() < e) break; }
        const fv = e*Math.cos(k*x), s = Math.random()*fv, w = (Math.random()-0.5)*0.03;
        if(i%2===0) a.position.setXYZ(i, x, s, w); else a.position.setXYZ(i, x, w, s); this.pkFrac[i] = i%2===0 ? 0.62 : 0.4; }
      a.position.needsUpdate = true;
      /* crest markers: the crests of E inside ±2σ (x = mλ, |x| ≤ 2σ), carried and stretched with the packet; their number never changes */
      const ms = []; for(let m=-20;m<=20;m++) if(Math.abs(m*0.16) <= 2*sg + 1e-9) ms.push(m); this.NCREST = ms.length;
      this.cr = cloud(ms.length, 0.2); ms.forEach((m,i) => { const x = m*0.16; M.setPt(this.cr, i, V3(x, Math.exp(-x*x/(2*sg*sg)), 0), [1,1,1]); }); M.flush(this.cr); this.pk.add(this.cr); }
    this.lb = null; this.lbT = ''; this.hist = null; this.hkey = null; this.t = 0; this.col = null; },
  enter(S){ PHX.base(); this.t = 0; this.G.rotation.set(0,0,0); this.y0 = PHX.S3.view.yaw; },
  label(txt, x, y){ if(txt !== this.lbT){ this.lbT = txt; if(this.lb){ this.G.remove(this.lb); this.lb.material.map.dispose(); this.lb.material.dispose(); }
      this.lb = M.label(txt, '#ffffff', 0.22); this.G.add(this.lb); } this.lb.position.set(x, y, 0); },
  step(dt, S){ dt = Math.max(0, dt); this.t += dt; const V = PHX.S3.view;
    if(V.auto) this.G.rotation.y = (V.yaw - this.y0) - 0.3*Math.sin(0.18*this.t);
    if(this.hkey !== S.z){ this.hkey = S.z; this.hist = history(Math.max(S.z, 1e-4), 600); }
    const H = this.hist, PER = 10, u = Math.min(1, (this.t % (PER + 2.5))/PER), tc = u*H.age;
    let i = 0; while(i < H.T.length-2 && H.T[i+1] < tc) i++; const w = H.T[i+1] > H.T[i] ? (tc - H.T[i])/(H.T[i+1] - H.T[i]) : 0;
    const a = H.A[i] + w*(H.A[i+1]-H.A[i]), chi = H.X[i] + w*(H.X[i+1]-H.X[i]), r = a*(1+S.z);    /* r = a / a_emit, from 1 to 1+z */
    /* drawn sizes: lattice spacing D·a (to scale in a); galaxies keep their size; packet length ∝ a, amplitude ∝ 1/(a/a_emit) */
    const gl = this.gal.geometry.attributes.position; let q = 0;
    for(let n=0;n<this.nodes.length;n++){ const c = this.nodes[n]; for(let p=0;p<GP;p++,q++){ const v = this.loc[q]; gl.setXYZ(q, c.x*a + v.x, c.y*a + v.y, c.z*a + v.z); } }
    gl.needsUpdate = true;
    const lp = this.grid.geometry.attributes.position; this.seg.forEach((sg, m) => { const A = this.nodes[sg[0]], B = this.nodes[sg[1]];
      lp.setXYZ(2*m, A.x*a, A.y*a, A.z*a); lp.setXYZ(2*m+1, B.x*a, B.y*a, B.z*a); }); lp.needsUpdate = true;
    /* packet: comoving position from chi(a), normalised to the lattice; physical position = a × comoving */
    const xc = (-0.4 + 0.6*chi/H.chi)*(NX-1)*D, lamNow = S.lam*r, L = 1.1*a, amp = 0.7/r;
    this.pk.position.set(xc*a, 0, 0); this.pk.scale.set(L, amp, amp);
    const LC = lineColour(lamNow), cc = LC.rgb, dim = LC.b, key = cc.map(v => v.toFixed(2)).join(',')+dim.toFixed(2);
    if(key !== this.col){ this.col = key; const ca = this.pk.geometry.attributes.color; for(let k=0;k<ca.count;k++){ const b = this.pkFrac[k]*dim; ca.setXYZ(k, cc[0]*b, cc[1]*b, cc[2]*b); } ca.needsUpdate = true; }
    this.label('λ = '+f(lamNow,0)+' nm  ·  '+this.NCREST+' crests', xc*a, amp + 0.32);
    return [['redshift z', f(S.z,2)], ['scale factor a', f(a,3)+'  (emitted at '+f(1/(1+S.z),3)+', today 1)'], ['stretch a / a_emit', f(r,3)+' of '+f(1+S.z,3)],
      ['wavelength now', f(lamNow,0)+' nm ('+bandOf(lamNow)+', '+hexOf(cc)+')'], ['energy now', f(S.E/r,3)+' eV (emitted '+f(S.E,3)+')'],
      ['crests within ±2σ', this.NCREST+', the same at emission and arrival'], ['crest spacing', f(S.lam,0)+' nm × '+f(r,3)+' = '+f(lamNow,0)+' nm'], ['on arrival', f(S.rs.lam,0)+' nm, '+f(S.rs.E,3)+' eV'], ['light-travel time', f(H.age,2)+' Gyr'], ['comoving distance', f(H.chi,0)+' Mpc = '+f(H.chi*MPC_GLY,2)+' Gly'],
      ['cosmology', 'H₀ = 70, Ωm = 0.3, ΩΛ = 0.7']]; }});


})();
