(function(){
"use strict";
/* SCRIPT: PHOTON-MIXER-V2-COMMON
   Ballad of a Dead Photon — 3D mixer v2 (Jeromie Beasley). Built on 3D Mixer Parts v1.
   Every scene is a computed field drawn as a cloud of points: positions are sampled from the field's own density and
   colour is its phase (or its temperature, or its computed colour), never decoration. Numbers come from PHO (core). */
const M = window.Mixer3D, T = M.T, K = window.PHO;
const V3 = (x,y,z) => new T.Vector3(x,y,z);
const f = (x,d) => (x==null || !isFinite(x)) ? '—' : (+x).toFixed(d==null?3:d);
const sci = (x,d) => (+x).toExponential(d==null?2:d).replace('e+','e');
let S3 = null;
const TAU = 2*Math.PI;

/* phase to colour: a hue wheel, the same convention as the films (colour = phase) */
function hue(p, v){ const h = ((p/TAU)%1+1)%1*6, i = Math.floor(h), fr = h-i, q = 1-fr; v = v==null?1:v;
  const c = [[1,fr,0],[q,1,0],[0,1,fr],[0,q,1],[fr,0,1],[1,0,q]][i%6]; return [c[0]*v, c[1]*v, c[2]*v]; }
const CIE_T = [[.001368,.000039,.00645],[.004243,.00012,.02005],[.01431,.000396,.06785],[.04351,.00121,.2074],[.13438,.004,.6456],[.2839,.0116,1.3856],[.34828,.023,1.74706],
  [.3362,.038,1.77211],[.2908,.06,1.6692],[.19536,.09098,1.28764],[.09564,.13902,.81295],[.03201,.20802,.46518],[.0049,.323,.272],[.0093,.503,.1582],[.06327,.71,.07825],
  [.1655,.862,.04216],[.2904,.954,.0203],[.43345,.99495,.00875],[.5945,.995,.0039],[.7621,.952,.0021],[.9163,.87,.00165],[1.0263,.757,.0011],[1.0622,.631,.0008],
  [1.0026,.503,.00034],[.85445,.381,.00019],[.6424,.265,.00005],[.4479,.175,.00002],[.2835,.107,0],[.1649,.061,0],[.0874,.032,0],[.04677,.017,0],[.0227,.00821,0],
  [.011359,.004102,0],[.00579,.002091,0],[.002899,.001047,0],[.00144,.00052,0],[.00069,.000249,0],[.000332,.00012,0],[.000166,.00006,0],[.000083,.00003,0],[.000042,.000015,0]];
/* colour of a spectral line: CIE 1931 2° matching functions -> linear sRGB, clipped, normalised to max 1 (hue only).
   Beyond 780 nm (infrared) a dim deep red marker; below 380 nm a dim violet marker. */
function lamRGB(l){ if(l > 780) return [0.45,0.03,0.02]; if(l < 380) return [0.35,0.05,0.5];
  const x = (l-380)/10, i = Math.min(39, Math.floor(x)), w = x - i, q = [0,1,2].map(k => CIE_T[i][k]*(1-w) + CIE_T[i+1][k]*w);
  const v = [3.2406*q[0]-1.5372*q[1]-0.4986*q[2], -0.9689*q[0]+1.8758*q[1]+0.0415*q[2], 0.0557*q[0]-0.2040*q[1]+1.0570*q[2]].map(t => Math.max(0, t));
  const m = Math.max(v[0],v[1],v[2]) || 1; return v.map(t => Math.pow(t/m, 1/2.2)); }
const lamName = l => (l < 400 ? 'ultraviolet' : l > 700 ? 'infrared' : M.colour.hex(lamRGB(l)));
function base(){ S3.scene.background = new T.Color(0x000000); S3.scene.fog = null; }
function cloud(n, size){ const p = M.points(n, size); p.material.opacity = 0.9; return p; }
function clearCloud(p, from){ const a = p.geometry.attributes; for(let i=from||0;i<a.color.count;i++) a.color.setXYZ(i,0,0,0); a.color.needsUpdate = true; }
/* rejection sampler: fills a cloud with points whose density follows w(x,y,z) inside a box; col(x,y,z) gives colour */
function fill(p, box, w, wmax, col, tries){ const a = p.geometry.attributes, n = a.position.count; let k = 0, t = 0; tries = tries || n*60;
  while(k < n && t < tries){ t++; const x = box[0]+Math.random()*(box[1]-box[0]), y = box[2]+Math.random()*(box[3]-box[2]), z = box[4]+Math.random()*(box[5]-box[4]);
    const v = w(x,y,z); if(Math.random()*wmax < v){ a.position.setXYZ(k,x,y,z); const c = col(x,y,z); a.color.setXYZ(k,c[0],c[1],c[2]); k++; } }
  for(let i=k;i<n;i++) a.color.setXYZ(i,0,0,0); a.position.needsUpdate = a.color.needsUpdate = true; return k; }
function ringLine(r, y, color, op){ const pts = []; for(let i=0;i<=160;i++){ const a = TAU*i/160; pts.push(V3(r*Math.cos(a), y, r*Math.sin(a))); } return M.line(pts, color, op); }

/* ---------- Lane–Emden n = 3 (Eddington's standard solar model): theta(xi), density ∝ theta^3, temperature ∝ theta ---------- */
const LE = (() => { const h = 1e-3; let xi = 1e-6, th = 1, dth = 0; const out = [[0,1]];
  const F = (x, y, yp) => -y*y*y - 2*yp/x;
  while(th > 0){ const k1 = dth, l1 = F(xi, th, dth), k2 = dth + h/2*l1, l2 = F(xi+h/2, th+h/2*k1, dth+h/2*l1), k3 = dth + h/2*l2, l3 = F(xi+h/2, th+h/2*k2, dth+h/2*l2), k4 = dth + h*l3, l4 = F(xi+h, th+h*k3, dth+h*l3);
    th += h/6*(k1+2*k2+2*k3+k4); dth += h/6*(l1+2*l2+2*l3+l4); xi += h; if(th > 0) out.push([xi, th]); }
  const xi1 = xi; return { xi1, theta: r => { const x = r*xi1, i = Math.min(out.length-1, Math.floor(x/h)); return Math.max(0, out[i][1]); } }; })();

const MIXER = {
  title: 'Ballad of a Dead Photon',
  byline: 'Jeromie Beasley · 3D mixer v2 · every cloud is a computed field',
  note: 'Colour is phase unless a scene says otherwise.',
  feed: {
    params: [
      {id:'lam',  label:'Wavelength at emission (nm)', min:400, max:700, step:10, value:550},
      {id:'lmfp', label:'Mean free path in the Sun, log₁₀ m', min:-5, max:-1, step:0.1, value:-3},
      {id:'th',   label:'Angle of incidence (degrees)', min:0, max:89, step:0.5, value:50},
      {id:'n1',   label:'Index of the glass', min:1.1, max:2.4, step:0.01, value:1.5},
      {id:'dsl',  label:'Slit separation (wavelengths)', min:2, max:12, step:0.5, value:5},
      {id:'z',    label:'Redshift z', min:0, max:3, step:0.01, value:0.5},
      {id:'phi',  label:'Work function of the metal (eV)', min:1.5, max:5, step:0.05, value:2.0},
      {id:'elev', label:'Sun elevation (degrees)', min:-1, max:60, step:0.5, value:3}
    ],
    build(P){ const lam = P.lam, l = Math.pow(10, P.lmfp), th = P.th*Math.PI/180;
      return { lam, rgb: lamRGB(lam), E: K.energyEV(lam), walk: K.walk(l), l, th, n1: P.n1, sn: K.snell(P.n1, 1, th), thc: K.critical(P.n1, 1),
        dep: K.evanescentDepth(lam, P.n1, 1, th), R: K.fresnelR(P.n1, 1, th), dsl: P.dsl, z: P.z, rs: K.redshift(lam, P.z), phi: P.phi, pe: K.photoelectric(lam, P.phi), elev: P.elev, key: JSON.stringify(P) }; }
  },
  eyes: [], film: ['core','flight','snell','slits','redshift','photoelectric','resonance','sky']
};

window.PHX = { M, T, K, V3, f, sci, TAU, hue, lamRGB, lamName, cloud, clearCloud, fill, ringLine, LE, MIXER,
  S3: null, base(){ const s = window.PHX.S3; s.scene.background = new T.Color(0x000000); s.scene.fog = null; },
  add(eye){ const mk = eye.make; eye.make = function(G, st){ window.PHX.S3 = st; return mk.call(this, G, st); }; MIXER.eyes.push(eye); } };
})();
