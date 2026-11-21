/* SCRIPT: element_mixer_v2
   The Loop Wall — element paper mixer, version 2 (film edition) — Jeromie Beasley — 21 Nov 2026
   Built on the shared 3D parts (mixer3d_parts_v1.js). Every number shown comes from the pinned
   threshold archive (element_data_v1.js) or from the ladder block computation (ladder_data_v2.js).

   Connection energy on every link of a chain (The Weight Between, scalar edge, atlas card B189):
     E⁻ = (IEₖ₊₁ − IEₖ)²   the connection book,  E⁺ = (IEₖ₊₁ + IEₖ)²  the opposite book,
     E⁻ / E⁺ = Γₖ²  exactly.
   Drawn so the picture is the identity: the bright core of a link has radius Γ·R inside a fine
   outline sheath of radius R, so core area / sheath area = Γ² = E⁻/E⁺. The fine gold ring on
   every link sits at R/√2: a core that reaches past it is a step outside the loop wall.

   Film: a song-locked timeline (cues below). FILM.renderAt(t) draws one exact frame for a
   frame-by-frame recording; the live page plays the same timeline against the embedded song. */
(function(){
"use strict";
const M = window.Mixer3D, T = M.T, D = window.ELEMENT_DATA, LD = window.LADDER_DATA, EL = D.el;
const V3 = (x,y,z) => new T.Vector3(x,y,z);
const ZW = 3 + 2*Math.SQRT2, EW = Math.log(ZW);
const gam = z => (z-1)/(z+1);
const clamp = (x,a,b) => Math.max(a, Math.min(b, x));
const ease = x => { x = clamp(x,0,1); return x*x*(3-2*x); };
const f = (x,n) => (x == null || !isFinite(x)) ? '—' : Number(x).toFixed(n);
const fe = x => { if(!isFinite(x)) return '—'; const e = Math.floor(Math.log10(Math.abs(x))); return e >= 5 || e <= -3 ? (x/Math.pow(10,e)).toFixed(3)+'×10'+sup(e) : x.toFixed(e >= 2 ? 1 : 3); };
const sup = n => String(n).split('').map(c => '⁰¹²³⁴⁵⁶⁷⁸⁹'['0123456789'.indexOf(c)] || (c === '-' ? '⁻' : c)).join('');
const GOLD=[1.0,0.72,0.26], CYAN=[0.36,0.80,1.0], ROSE=[1.0,0.40,0.62], WHITE=[0.93,0.96,1.0], DIM=[0.30,0.38,0.48], PALE=[0.70,0.80,0.92];
const mix = (a,b,t) => a.map((v,i) => v + (b[i]-v)*clamp(t,0,1));
const col = v => M.tcol(v);
const gcol = g2 => g2 > 0.5 ? mix(GOLD, ROSE, (g2-0.5)/0.45) : mix(CYAN, PALE, g2/0.5);
const NAME = e => e.n === 'Cesium' ? 'Caesium' : e.n;
const K = k => { let a = 1, b = Math.sqrt(1-k*k); for(let i=0;i<30;i++){ const an = (a+b)/2; b = Math.sqrt(a*b); a = an; } return Math.PI/(2*a); };
const ladderSpacing = u => 4*Math.PI*K(u)/K(Math.sqrt(1-u*u));
window.LOOPWALL_CHECK = { ladderSpacing, gam, ZW };

/* ---------------- film clock ---------------- */
const FILM = { on:false, manual:false, t:0, local:0, cue:-1, dur:10 };
const clock = tEye => FILM.on ? FILM.local : tEye;

/* ---------------- fine-line parts ---------------- */
function segs(arr, color, op){ const g = new T.BufferGeometry(); g.setAttribute('position', new T.Float32BufferAttribute(arr,3));
  const l = new T.LineSegments(g, new T.LineBasicMaterial({color, transparent:true, opacity:op, depthWrite:false})); l.frustumCulled = false; return l; }
function circleArr(r, y, n){ const p = []; n = n || 96; for(let i=0;i<n;i++){ const a0 = 2*Math.PI*i/n, a1 = 2*Math.PI*(i+1)/n; p.push(r*Math.cos(a0),y,r*Math.sin(a0), r*Math.cos(a1),y,r*Math.sin(a1)); } return p; }
function ring(r, color, op, n){ return segs(circleArr(r,0,n), color, op); }
function cageArr(n){ const p = []; for(let i=0;i<n;i++){ const a = 2*Math.PI*i/n, c = Math.cos(a), s = Math.sin(a); p.push(c,-0.5,s, c,0.5,s); }
  return p.concat(circleArr(1,-0.5,48), circleArr(1,0.5,48)); }
const CAGE = (() => { const g = new T.BufferGeometry(); g.setAttribute('position', new T.Float32BufferAttribute(cageArr(10),3)); return g; })();
const WRING = (() => { const g = new T.BufferGeometry(); g.setAttribute('position', new T.Float32BufferAttribute(circleArr(Math.SQRT1_2,0,48),3)); return g; })();
const CYL = new T.CylinderGeometry(1,1,1,24,1,true);
function between(obj, a, b){ const d = b.clone().sub(a), L = Math.max(1e-6, d.length()); obj.position.copy(a).addScaledVector(d,0.5); obj.quaternion.setFromUnitVectors(V3(0,1,0), d.multiplyScalar(1/L)); return L; }
const LS = 1.45;
function addLabel(g, text, color, P, s){ const l = M.label(text, color, LS*(s || 0.26)); l.position.copy(P); g.add(l); return l; }
function setLabelOpacity(l, o){ l.material.opacity = o; l.visible = o > 0.01; }

/* a link of a chain: outline sheath (E⁺), bright core of radius Γ·R (E⁻), the wall ring at R/√2 */
function makeLink(parent){
  const g = new T.Group();
  const sheath = new T.LineSegments(CAGE, new T.LineBasicMaterial({color:0xa9bdd2, transparent:true, opacity:0.45, depthWrite:false}));
  const core = new T.Mesh(CYL, new T.MeshBasicMaterial({color:0xffffff, transparent:true, opacity:0.85, blending:T.AdditiveBlending, depthWrite:false, side:T.DoubleSide}));
  const wr = new T.LineSegments(WRING, new T.LineBasicMaterial({color:0xf2c14e, transparent:true, opacity:0.7, depthWrite:false}));
  const halo = new T.Mesh(CYL, new T.MeshBasicMaterial({color:0xffffff, transparent:true, opacity:0.2, blending:T.AdditiveBlending, depthWrite:false, side:T.DoubleSide}));
  const spine = new T.Line(new T.BufferGeometry().setFromPoints([V3(0,-0.5,0), V3(0,0.5,0)]), new T.LineBasicMaterial({color:0xffffff, transparent:true, opacity:0.8, depthWrite:false}));
  sheath.frustumCulled = core.frustumCulled = wr.frustumCulled = halo.frustumCulled = spine.frustumCulled = false;
  g.add(sheath, halo, core, spine, wr); parent.add(g); return {g, sheath, core, wr, halo, spine};
}
function setLink(L, a, b, R, G, grow, bright, fade, coreFade){
  const bb = a.clone().lerp(b, clamp(grow, 0.002, 1)), len = between(L.g, a, bb), g2 = G*G;
  const rc = R*Math.max(0.02, Math.abs(G)), cf = coreFade == null ? 1 : coreFade, c = gcol(g2), bo = Math.min(0.62, 0.3 + 0.16*bright);
  L.sheath.scale.set(R, len, R); L.core.scale.set(rc, len, rc); L.wr.scale.set(R, 1, R);
  L.halo.scale.set(rc*1.9, len, rc*1.9); L.spine.scale.set(1, len, 1);
  L.core.material.color = col(c); L.core.material.opacity = bo*fade*cf;
  L.halo.material.color = col(c); L.halo.material.opacity = 0.07*Math.min(3, bright)*fade*cf;
  L.spine.material.color = col(mix(c, WHITE, 0.45)); L.spine.material.opacity = 0.75*fade*cf;
  L.sheath.material.opacity = 0.42*fade;
  L.wr.material.color = col(g2 > 0.5 ? GOLD : [0.85,0.70,0.40]);
  L.wr.material.opacity = (g2 > 0.5 ? 1.0 : 0.5)*fade;
  L.g.visible = fade > 0.005;
}

/* an expanding shock ring (released connection energy) */
function makeShock(parent){ const r = ring(1, 0xffffff, 0, 72); parent.add(r); return r; }
function setShock(r, P, age, size, c, strength){ if(age < 0 || age > 1){ r.visible = false; return; }
  r.visible = true; r.position.copy(P); const s = 0.05 + size*ease(age); r.scale.set(s,1,s); r.material.color = col(c); r.material.opacity = strength*(1-age)*(1-age); }

/* ---------------- the eyes ---------------- */
const eyes = [];
const EYE = {};

/* 1. the wall: every step of the table on the reflection disk */
eyes.push({ id:'wall', section:'§2 the wall', grade:'EXACT', title:'The wall on the reflection disk',
  eq:'zₖ = IEₖ₊₁ / IEₖ,   Γ = (z − 1)/(z + 1) = tanh h,   h = ½ ln z\nloop wall: Γ² = ½  ⇔  z = 3 + 2√2 = 5.828427\nE⁻/E⁺ = Γ²:  at the wall the two books split one to two',
  text:'Each successive removal step of every element from hydrogen to astatine is a point on the disk at radius Γ. The gold ring is the loop wall Γ² = ½. Of the 3,570 steps only eight lie outside it, all first openings of a noble-gas core: lithium, beryllium, boron, carbon, sodium, potassium, rubidium and caesium.',
  uses:[], view:[0.6,0.95,8.6,0],
  make(g, S3){ this.g = g; const Rd = this.Rd = 3.0;
    g.add(ring(Rd, 0x8fa3b8, 0.55, 160)); [0.25,0.5,0.75].forEach(r => g.add(ring(Rd*r, 0x52667c, 0.22, 128)));
    this.wallRing = ring(Rd*Math.SQRT1_2, 0xf2c14e, 0.95, 160); g.add(this.wallRing);
    const ax = []; for(let i=0;i<12;i++){ const a = Math.PI*i/6; ax.push(0,0,0, Rd*Math.cos(a),0,Rd*Math.sin(a)); } g.add(segs(ax, 0x3a4a5c, 0.25));
    addLabel(g, 'Γ² = ½', '#f2c14e', V3(Rd*0.707*0.72, 0.18, -Rd*0.707*0.72), 0.3);
    addLabel(g, 'z = 3 + 2√2', '#f2c14e', V3(Rd*0.707*0.72, -0.12, -Rd*0.707*0.72), 0.24);
    const pts = []; this.out = [];
    EL.forEach(e => { for(let k=0;k<e.ie.length-1;k++){ const z = e.ie[k+1]/e.ie[k], G = gam(z), a = 2*Math.PI*(e.Z-1)/85 + 0.06*Math.sin(k*2.1);
      pts.push([G, a, e, k]); if(G*G > 0.5) this.out.push([G, a, e, k]); } });
    this.dust = M.points(pts.length, 0.07); pts.forEach((q,i) => M.setPt(this.dust, i, V3(Rd*q[0]*Math.cos(q[1]), 0, Rd*q[0]*Math.sin(q[1])), gcol(q[0]*q[0]).map(v => v*(q[0]*q[0] > 0.5 ? 1 : 0.55)))); M.flush(this.dust); g.add(this.dust);
    this.outLbl = this.out.map((q,i) => { const rr = Rd*q[0]*(1.10 + 0.13*(i % 4)); return addLabel(g, NAME(q[2]), '#f2c14e', V3(rr*Math.cos(q[1]), 0.22, rr*Math.sin(q[1])), 0.2); });
    this.outGlow = M.points(this.out.length, 0.32); this.out.forEach((q,i) => M.setPt(this.outGlow, i, V3(Rd*q[0]*Math.cos(q[1]), 0, Rd*q[0]*Math.sin(q[1])), GOLD)); M.flush(this.outGlow); g.add(this.outGlow);
    this.spoke = M.line([V3(0,0,0), V3(1,0,0)], 0xdfe7ef, 0.8); g.add(this.spoke);
    this.probe = M.points(1, 0.42); g.add(this.probe); this.shock = makeShock(g); },
  cue(o){ }, enter(){},
  step(dt, S, tEye){ const t = clock(tEye), Rd = this.Rd;
    const cyc = (t % 12)/12, z = 1 + 13.0289*(0.5 - 0.5*Math.cos(2*Math.PI*cyc)), G = gam(z), a = -0.35 + 0.15*Math.sin(t*0.2);
    const P = V3(Rd*G*Math.cos(a), 0, Rd*G*Math.sin(a)); M.setLine(this.spoke, [V3(0,0,0), P]);
    M.setPt(this.probe, 0, P, G*G > 0.5 ? GOLD : CYAN); M.flush(this.probe);
    const tc = 12*Math.acos(1 - 2*(ZW-1)/13.0289)/(2*Math.PI); const ph = t % 12, age = Math.min(Math.abs(ph - tc), Math.abs(ph - (12 - tc)))/1.2;
    this.shock.visible = false;
    this.wallRing.material.opacity = 0.75 + 0.25*Math.max(0, 1 - age);
    const show = clamp((t - 2.5)/3, 0, 1); this.outLbl.forEach(l => setLabelOpacity(l, show)); this.outGlow.material.opacity = 0.5 + 0.5*show;
    return [['z (probe)', f(z,4)], ['Γ', f(G,5)], ['Γ² = E⁻/E⁺', f(G*G,5)], ['side', G*G > 0.5 ? 'outside the wall' : 'inside the wall'], ['steps on the disk', '3,570'], ['outside the wall', '8']]; } });

/* 2. the chain: builds electron by electron, holds, then peels */
eyes.push({ id:'chain', section:'§3 the peel chain', grade:'EXACT (archive)', title:'A chain builds and peels',
  eq:'link k joins removal k to removal k+1\nE⁻ = (IEₖ₊₁ − IEₖ)²,   E⁺ = (IEₖ₊₁ + IEₖ)²,   E⁻/E⁺ = Γₖ²\ncore area / outline area = Γ²;  gold ring at Γ² = ½\npeel ledger: Σ ln zₖ = ln(IEₙ / IE₁)',
  text:'The chain of one element, one node per removal energy on a logarithmic height. Built from the bare nucleus, each bound electron adds a link whose bright core is its connection energy E⁻ inside the outline of the opposite book E⁺. Peeled from the outside in, each link releases its core and leaves its outline as the record; the ledger of offsets telescopes to ln(IEₙ/IE₁).',
  uses:['Z'], view:[0.5,0.22,9.0,2.1],
  make(g, S3){ this.g = g; this.Z = 0; this.mode = 'cycle'; this.dur = 24; },
  build(Z){ const g = this.g; while(g.children.length) g.remove(g.children[0]);
    const e = EL[Z-1], ie = e.ie, n = ie.length, l0 = Math.log10(ie[0]), span = Math.max(0.3, Math.log10(ie[n-1]) - l0);
    const Ys = 6.2/span, R0 = 1.75; this.e = e; this.Z = Z;
    this.P = ie.map((v,k) => V3(R0*Math.cos(k*0.95 + 0.4), (Math.log10(v) - l0)*Ys, R0*Math.sin(k*0.95 + 0.4)));
    this.ty = 0.5*(this.P[n-1].y);
    this.z = []; for(let k=0;k<n-1;k++) this.z.push(ie[k+1]/ie[k]);
    const axis = []; const top = this.P[n-1].y + 0.6; axis.push(0,-0.4,0, 0,top,0); g.add(segs(axis, 0x2e3c4c, 0.35));
    this.nuc = M.points(1, 0.62); M.setPt(this.nuc, 0, V3(0, top, 0), [1,0.92,0.78]); M.flush(this.nuc); g.add(this.nuc);
    this.nucLbl = addLabel(g, 'nucleus  Z = ' + Z, '#dfe7ef', V3(0, top + 0.38, 0), 0.24);
    this.spine = []; for(let k=0;k<n;k++){ const s = M.line([V3(0,this.P[k].y,0), this.P[k]], 0x31465c, 0.0); g.add(s); this.spine.push(s); }
    this.links = this.z.map(() => makeLink(g));
    this.nodes = M.points(n, 0.5); g.add(this.nodes);
    this.fly = M.points(n, 0.55);
    this.trails = this.P.map(() => { const l = M.line([V3(0,0,0),V3(0,0,0)], 0xffffff, 0); g.add(l); return l; });
    this.pulse = M.points(1, 0.6); g.add(this.pulse);
    this.call = addLabel(g, '', '#ffffff', V3(0,0,0), 0.24); this.callLine = M.line([V3(0,0,0),V3(0,0,0)], 0xdfe7ef, 0.6); g.add(this.callLine); g.add(this.fly);
    this.shocks = this.z.map(() => makeShock(g));
    this.zl = this.z.map((z,k) => { const m = this.P[k].clone().lerp(this.P[k+1], 0.5); const out = V3(m.x, 0, m.z).normalize().multiplyScalar(0.95);
      return addLabel(g, 'z = ' + f(z,3), z > ZW ? '#f2c14e' : '#9fb3c8', m.clone().add(out), 0.19); });
    this.kl = this.P.map((p,k) => { const out = V3(p.x,0,p.z).normalize().multiplyScalar(0.42); return addLabel(g, String(k+1), '#6f8296', p.clone().add(out).add(V3(0,0.12,0)), 0.17); });
    this.title = addLabel(g, NAME(e), '#dfe7ef', V3(0, -0.95, 0), 0.36);
    this.R = 0.42; },
  cue(o, dur){ this.mode = o.mode || 'cycle'; this.dur = dur || 24; if(o.Z && o.Z !== this.Z) this.build(o.Z); },
  enter(S){ if(this.Z !== S.P.Z) this.build(S.P.Z); },
  change(S){ this.build(S.P.Z); },
  /* the state at local time t:  bind(k) ∈ [0,1] arrival of electron k;  peel(k) ∈ [0,1] its removal */
  state(t){ const n = this.P.length, mode = this.mode, dur = this.dur;
    let Tb, t0b = 0.4, Tp, t0p;
    if(mode === 'build'){ Tb = (dur - 3.5)/n; t0p = 1e9; Tp = 1; }
    else if(mode === 'peel'){ Tb = 0; t0p = 0.8; Tp = (dur - 2.5)/n; }
    else { const L = Math.max(14, 2.2*n + 8); t = t % L; Tb = (0.42*L)/n; t0p = 0.42*L + 1.8; Tp = (0.42*L)/n; }
    const bind = [], peel = [];
    for(let k=0;k<n;k++){ const i = n-1-k; bind.push(Tb === 0 ? 1 : clamp((t - t0b - i*Tb)/(0.85*Tb), 0, 1)); peel.push(clamp((t - t0p - k*Tp)/(0.9*Tp), 0, 1)); }
    return {bind, peel, t, Tb, Tp, t0p}; },
  step(dt, S, tEye){ if(!this.links) return [];
    const t = clock(tEye), st = this.state(t), n = this.P.length, P = this.P, R = this.R;
    let ledger = 0, outside = 0, cur = -1, flare = 0;
    for(let k=0;k<n;k++){ const b = st.bind[k], p = st.peel[k];
      /* electron k: flies in from outside, sits, then escapes */
      const home = P[k], away = V3(home.x*4.2, home.y + 2.6, home.z*4.2), esc = V3(home.x*5.5, home.y + 3.4, home.z*5.5);
      let Q, show = 1;
      if(b < 1){ Q = away.clone().lerp(home, ease(b)); show = b > 0 ? ease(b*4) : 0; }
      else if(p > 0){ Q = home.clone().lerp(esc, ease((p - 0.35)/0.65)); show = p < 0.35 ? 1 : 1 - ease((p - 0.35)/0.65); }
      else Q = home;
      const sitting = b >= 1 && p <= 0.35;
      M.setPt(this.nodes, k, home, sitting ? [0.85,0.92,1.0] : (p > 0.35 ? [0.16,0.2,0.26] : [0,0,0]));
      M.setPt(this.fly, k, Q, (!sitting && show > 0) ? (p > 0 ? gcol(k < n-1 ? gam(this.z[k])**2 : 0.2).map(v => v*show*1.3) : [0.75*show,0.85*show,1.0*show]) : [0,0,0]);
      this.spine[k].material.opacity = sitting ? 0.32 : 0.06*(b >= 1 ? 1 : 0);
      const tr = this.trails[k]; if(!sitting && show > 0.02){ const tail = b < 1 ? away.clone().lerp(home, ease(b - 0.25)) : home.clone().lerp(esc, ease((p - 0.5)/0.65)); M.setLine(tr, [tail, Q]); tr.material.opacity = 0.55*show; tr.material.color = col(p > 0 ? gcol(k < n-1 ? gam(this.z[k])**2 : 0.2) : CYAN); } else tr.material.opacity = 0;
      setLabelOpacity(this.kl[k], sitting ? 0.85 : (b >= 1 ? 0.25 : 0));
    }
    M.flush(this.nodes); M.flush(this.fly);
    for(let k=0;k<n-1;k++){ const G = gam(this.z[k]), bIn = st.bind[k], p = st.peel[k];
      /* link k grows from the already bound inner node k+1 down to node k as electron k lands */
      const grow = ease((bIn - 0.45)/0.55), built = bIn >= 1;
      let bright = 1, coreFade = 1, fade = grow > 0 ? 1 : 0;
      if(built && p === 0 && st.Tb > 0){ const tl = t - (0.4 + (n-1-k)*st.Tb + 0.85*st.Tb); bright = 1 + 1.6*Math.exp(-Math.max(0,tl)*2.2); }
      if(p > 0){ bright = 1 + 2.2*Math.sin(Math.PI*clamp(p/0.4,0,1)); coreFade = 1 - ease((p - 0.35)/0.5); fade = 1 - 0.72*ease((p - 0.35)/0.6); if(p < 1) { cur = k; flare = p; } }
      if(p > 0.35){ ledger += Math.log(this.z[k]); if(G*G > 0.5) outside++; }
      const grown = p > 0.35 ? 1 : grow;
      setLink(this.links[k], P[k+1], P[k], R, G, grown, bright, fade, coreFade);
      if(grow <= 0 && p === 0) this.links[k].g.visible = false;
      setShock(this.shocks[k], P[k], p > 0.3 ? (p - 0.3)/0.7 : -1, (G*G > 0.5 ? 3.2 : 1.4), G*G > 0.5 ? GOLD : gcol(G*G), G*G > 0.5 ? 1.0 : 0.55);
      setLabelOpacity(this.zl[k], (built ? (p > 0.35 ? 0.3 : 0.95) : grow*0.8)); }
    if(cur < 0 && this.mode !== 'peel'){ for(let k=n-2;k>=0;k--) if(st.bind[k] > 0 && st.bind[k] < 1){ cur = k; break; } }
    let shown = cur; if(shown < 0){ let lastPeeled = -1, lowBuilt = -1; for(let k=0;k<n-1;k++){ if(st.peel[k] >= 1) lastPeeled = k; if(lowBuilt < 0 && st.bind[k] >= 1 && st.peel[k] === 0) lowBuilt = k; } shown = lowBuilt >= 0 ? lowBuilt : lastPeeled; }
    { const allBound = st.bind[0] >= 1 && st.peel[0] === 0; if(allBound && n > 1){ const u = ((t*0.55) % 2), w = u < 1 ? u : 2 - u, x = w*(n-1), i = Math.min(n-2, Math.floor(x));
        M.setPt(this.pulse, 0, P[i].clone().lerp(P[i+1], x - i), [1,0.95,0.85]); } else M.setPt(this.pulse, 0, V3(0,0,0), [0,0,0]); M.flush(this.pulse); }
    const allOut = st.peel[n-1] > 0.35; this.nuc.material.opacity = 1; M.setPt(this.nuc, 0, V3(0, P[n-1].y + 0.6, 0), allOut ? [1,0.75,0.4] : [1,0.92,0.78]); M.flush(this.nuc);
    const e = this.e, k = clamp(shown < 0 ? 0 : shown, 0, Math.max(0, n-2)), z = this.z[k], G = gam(z);
    if(n > 1){ const m = P[k].clone().lerp(P[k+1], 0.5), out = V3(m.x, 0, m.z).normalize(), A = m.clone().addScaledVector(out, 0.55), B = m.clone().addScaledVector(out, 1.6).add(V3(0, k === n-2 ? -0.7 : 0.55, 0));
      const txt = 'E⁻/E⁺ = Γ² = ' + f(G*G,4); if(this.call.userData.txt !== txt){ this.call.userData.txt = txt; const nl = M.label(txt, G*G > 0.5 ? '#f2c14e' : '#ffffff', LS*0.24); this.call.material.map = nl.material.map; this.call.scale.copy(nl.scale); this.call.material.needsUpdate = true; }
      const vis = shown >= 0 && !(st.peel[k] >= 1 && cur < 0 && st.peel[n-2] >= 1 && k === n-2 && false) ? 1 : 0; this.call.position.copy(B).add(V3(0, 0.25, 0)); setLabelOpacity(this.call, vis); M.setLine(this.callLine, [A, B]); this.callLine.material.opacity = 0.6*vis; }
    const Em = (e.ie[k+1] - e.ie[k])**2, Ep = (e.ie[k+1] + e.ie[k])**2;
    return [['element', NAME(e) + ' (Z = ' + e.Z + ')'], ['link', 'removal ' + (k+1) + ' → ' + (k+2)], ['z = IEₖ₊₁/IEₖ', f(z,6)], ['E⁻ (eV²)', fe(Em)], ['E⁺ (eV²)', fe(Ep)], ['Γ² = E⁻/E⁺', f(G*G,5) + (G*G > 0.5 ? '  outside' : '  inside')], ['peel ledger Σ ln z', f(ledger,4)], ['links released outside', String(outside)]]; } });

/* 3. across the table: every element's chain, 3,570 links */
eyes.push({ id:'table', section:'§4 hydrogen to astatine', grade:'EXACT (archive)', title:'Every chain on the table',
  eq:'85 chains · 3,570 links · height = log₁₀ IE\nthe eight links outside the wall are the first openings\nof the helium, neon, argon, krypton and xenon cores',
  text:'Each element stands as its own chain on a ring ordered by atomic number, with a common logarithmic height, so the shells of different elements line up across the ring and every core opening shows as a long link. The sweep builds them in order; links outside the loop wall keep their gold core.',
  uses:[], view:[0.3,0.48,13.5,2.4],
  make(g, S3){ this.g = g; const Rr = 5.2, Ys = 1.05, y0 = 0.55; this.mode = 'sweep'; this.dur = 30;
    this.ch = EL.map(e => { const a = 2*Math.PI*(e.Z - 1)/85 - Math.PI/2, x = Rr*Math.cos(a), zz = Rr*Math.sin(a);
      const P = e.ie.map(v => V3(x, (Math.log10(v) - y0)*Ys, zz)).reverse();   /* index 0 = innermost (top) */
      const cols = []; for(let i=0;i<P.length;i++){ const k = P.length - 1 - i; const z = k < e.ie.length - 1 ? e.ie[k+1]/e.ie[k] : 1; cols.push(...gcol(gam(z)**2)); }
      const geo = new T.BufferGeometry().setFromPoints(P); geo.setAttribute('color', new T.Float32BufferAttribute(cols,3));
      const line = new T.Line(geo, new T.LineBasicMaterial({vertexColors:true, transparent:true, opacity:0.0, depthWrite:false})); line.frustumCulled = false; g.add(line);
      const pts = M.points(P.length, 0.16); P.forEach((p,i) => M.setPt(pts, i, p, [0.8,0.88,1])); M.flush(pts); g.add(pts);
      const lab = addLabel(g, e.s, '#8a9aab', V3(x*1.07, (Math.log10(e.ie[0]) - y0)*Ys - 0.35, zz*1.07), 0.2);
      return {e, P, line, pts, lab, a}; });
    this.outs = []; EL.forEach(e => { for(let k=0;k<e.ie.length-1;k++){ const z = e.ie[k+1]/e.ie[k]; if(z > ZW){ const c = this.ch[e.Z-1], n = e.ie.length;
      const A = c.P[n-1-k], B = c.P[n-2-k]; const L = makeLink(g); const sh = makeShock(g); const lb = addLabel(g, NAME(e) + '  z = ' + f(z,3), '#f2c14e', A.clone().lerp(B,0.5).add(V3(Math.cos(c.a)*(1.1 + 0.5*(this.outs.length % 3)), 0.25*(this.outs.length % 2), Math.sin(c.a)*(1.1 + 0.5*(this.outs.length % 3)))), 0.2);
      this.outs.push({e, k, z, A, B, L, sh, lb}); } } });
    const shells = []; [1,2,3,4,5].forEach(d => { shells.push(...circleArr(Rr, (d - y0)*Ys, 170)); }); g.add(segs(shells, 0x2a3644, 0.35));
    [1,2,3,4,5].forEach(d => addLabel(g, '10' + sup(d) + ' eV', '#55657a', V3(Rr + 0.6, (d - y0)*Ys, 0), 0.18));
    this.cursor = M.points(1, 0.55); g.add(this.cursor); },
  cue(o, dur){ this.mode = o.mode || 'sweep'; this.dur = dur || 30; },
  enter(){},
  step(dt, S, tEye){ const t = clock(tEye);
    const span = this.mode === 'final' ? 0 : Math.max(6, this.dur - 3.5), Zc = this.mode === 'final' ? 86 : 1 + 85*clamp((t - 0.6)/span, 0, 1);
    let steps = 0, outside = 0, last = '—';
    this.ch.forEach((c,i) => { const Z = i + 1, n = c.P.length;
      let frac = clamp(Zc - Z, 0, 1); const built = Zc >= Z + 1;
      const shown = Math.max(0, Math.min(n, Math.round(frac*n)));
      c.line.geometry.setDrawRange(0, shown); c.pts.geometry.setDrawRange(0, shown);
      const near = Math.exp(-Math.abs(Zc - Z - 0.5)*0.45);
      c.line.material.opacity = built ? 0.32 + 0.6*near : (frac > 0 ? 1 : 0);
      c.pts.material.opacity = built ? 0.25 + 0.75*near : (frac > 0 ? 1 : 0);
      setLabelOpacity(c.lab, frac > 0 ? 0.35 + 0.6*near : 0);
      if(frac > 0) steps += Math.max(0, Math.min(n-1, shown - 1)); });
    this.outs.forEach(o => { const Z = o.e.Z, n = o.e.ie.length, idxTop = n - 2 - o.k; /* link appears when its lower node is drawn */
      const frac = clamp(Zc - Z, 0, 1), on = frac*n >= idxTop + 2 - 0.5, tOn = Z + (idxTop + 2)/n;
      const age = (Zc - tOn)*(span/85)/1.3;
      if(on){ outside++; last = NAME(o.e); }
      const pulse = this.mode === 'final' ? 1 + 0.35*Math.sin(t*2 + Z) : 1 + 2.2*Math.exp(-Math.max(0,age)*2);
      setLink(o.L, o.A, o.B, 0.2, gam(o.z), 1, pulse, on ? 1 : 0, 1);
      setShock(o.sh, o.A.clone().lerp(o.B,0.5), on && this.mode !== 'final' ? age : -1, 2.2, GOLD, 1);
      setLabelOpacity(o.lb, on ? (this.mode === 'final' ? 0.9 : 0.95) : 0); });
    const zi = clamp(Math.floor(Zc), 1, 85), c = this.ch[zi-1]; M.setPt(this.cursor, 0, V3(c.P[0].x*1.12, c.P[0].y + 0.5, c.P[0].z*1.12), this.mode === 'final' ? [0,0,0] : [1,1,1]); M.flush(this.cursor);
    if(this.mode === 'final') steps = 3570;
    return [['element', this.mode === 'final' ? 'hydrogen to astatine' : NAME(c.e) + ' (Z = ' + zi + ')'], ['links drawn', steps.toLocaleString('en')], ['outside the wall', outside + ' of ' + steps.toLocaleString('en')], ['latest outside', last]]; } });

/* 4. two faces, one loop: the Lambert quadrilateral in the Poincaré disk */
function circInter(c1, r1, c2, r2){ const dx = c2[0]-c1[0], dy = c2[1]-c1[1], d = Math.hypot(dx,dy); if(d > r1 + r2 || d < Math.abs(r1 - r2) || d === 0) return [];
  const a = (r1*r1 - r2*r2 + d*d)/(2*d), h = Math.sqrt(Math.max(0, r1*r1 - a*a)), mx = c1[0] + a*dx/d, my = c1[1] + a*dy/d;
  return [[mx + h*dy/d, my - h*dx/d], [mx - h*dy/d, my + h*dx/d]]; }
eyes.push({ id:'faces', section:'§5 two faces', grade:'EXACT', title:'Two faces close one loop',
  eq:'faces at distances a = ½ ln z_a and b = ½ ln z_b, at right angles\ncloses  ⇔  Γ_a² + Γ_b² < 1  ⇔  sinh a · sinh b < 1\nclosed: cos φ = sinh a sinh b      open: cosh d = sinh a sinh b\ncarbon fixed: crossover z_b = 5.591156',
  text:'In the Poincaré disk each step is a geodesic face standing at hyperbolic distance h = ½ ln z from the centre, drawn as a circle of radius 1/sinh h. Two faces at right angles close a Lambert quadrilateral exactly when sinh a · sinh b < 1; the product is then the cosine of the fourth angle. Past the crossing the faces part, and the same product becomes cosh of the gap between them. This is the two-plane licence of the gravity paper on the element disk.',
  uses:['za','zb'], view:[0.15,1.05,7.4,0],
  make(g, S3){ this.g = g; this.Rd = 2.9; this.mode = 'sweep'; this.dur = 26;
    g.add(ring(this.Rd, 0x8fa3b8, 0.6, 180)); g.add(segs([-this.Rd,0,0, this.Rd,0,0, 0,0,-this.Rd, 0,0,this.Rd], 0x3c4c5e, 0.5));
    this.A = M.line([V3(0,0,0),V3(0,0,0)], 0x7fdcff, 1); this.B = M.line([V3(0,0,0),V3(0,0,0)], 0xff9fcb, 1); g.add(this.A, this.B);
    this.Ag = M.line([V3(0,0,0),V3(0,0,0)], 0x63d3ff, 0.32); this.Bg = M.line([V3(0,0,0),V3(0,0,0)], 0xff8fc2, 0.32); g.add(this.Ag, this.Bg);
    this.fill = new T.Mesh(new T.BufferGeometry(), new T.MeshBasicMaterial({color:0xf2c14e, transparent:true, opacity:0.14, side:T.DoubleSide, depthWrite:false, blending:T.AdditiveBlending})); this.fill.frustumCulled = false; g.add(this.fill);
    this.edge = M.line([V3(0,0,0),V3(0,0,0)], 0xf2c14e, 0.9); g.add(this.edge);
    this.gap = M.line([V3(0,0,0),V3(0,0,0)], 0xffffff, 0.95); g.add(this.gap);
    this.X = M.points(3, 0.5); this.feet = M.points(2, 0.4); g.add(this.feet); g.add(this.X);
    this.la = addLabel(g, 'face a', '#63d3ff', V3(0,0,0), 0.22); this.lb = addLabel(g, 'face b', '#ff8fc2', V3(0,0,0), 0.22);
    this.lphi = addLabel(g, 'φ', '#f2c14e', V3(0,0,0), 0.3); this.lgap = addLabel(g, 'gap d', '#ffffff', V3(0,0,0), 0.24); this.za = 6.079534; this.zb = 5.639665; },
  cue(o, dur){ this.mode = o.mode || 'sweep'; this.dur = dur || 26; },
  enter(S){ this.za = S.P.za; this.zb = S.P.zb; }, change(S){ this.za = S.P.za; this.zb = S.P.zb; },
  step(dt, S, tEye){ const t = clock(tEye), Rd = this.Rd, W = (x,y) => V3(Rd*x, 0, -Rd*y);
    let za = this.za, zb = this.zb;
    if(FILM.on){ za = 6.079534; zb = 5.591156 + 0.33*Math.sin(2*Math.PI*(t/this.dur)*1.0 + Math.PI); }
    const a = 0.5*Math.log(za), b = 0.5*Math.log(zb), sa = Math.sinh(a), sb = Math.sinh(b), s = sa*sb;
    const cA = [1/Math.tanh(a), 0], rA = 1/sa, cB = [0, 1/Math.tanh(b)], rB = 1/sb;
    const arc = (c, r, n) => { const out = []; for(let i=0;i<=n;i++){ const th = 2*Math.PI*i/n, x = c[0] + r*Math.cos(th), y = c[1] + r*Math.sin(th); if(x*x + y*y < 0.9995) out.push([x,y,th]); } return out; };
    const sortRun = pts => { if(!pts.length) return pts; let best = 0; for(let i=1;i<pts.length;i++) if(Math.hypot(pts[i][0]-pts[i-1][0], pts[i][1]-pts[i-1][1]) > 0.2){ best = i; } return pts.slice(best).concat(pts.slice(0,best)); };
    const aA = sortRun(arc(cA, rA, 720)), aB = sortRun(arc(cB, rB, 720));
    M.setLine(this.Ag, aA.map(p => W(p[0],p[1]))); M.setLine(this.Bg, aB.map(p => W(p[0],p[1])));
    const A0 = [Math.tanh(a/2), 0], B0 = [0, Math.tanh(b/2)];
    const ins = circInter(cA, rA, cB, rB).filter(p => p[0]*p[0] + p[1]*p[1] < 1);
    const closes = s < 1 && ins.length > 0;
    let cosphi = s, phi = closes ? Math.acos(clamp(s,-1,1))*180/Math.PI : NaN;
    if(closes){ const X = ins[0];
      const thA0 = Math.PI, thAX = Math.atan2(X[1] - cA[1], X[0] - cA[0]), thB0 = -Math.PI/2, thBX = Math.atan2(X[1] - cB[1], X[0] - cB[0]);
      const sweep = (c, r, t0, t1, n) => { let d = t1 - t0; while(d > Math.PI) d -= 2*Math.PI; while(d < -Math.PI) d += 2*Math.PI; const o = []; for(let i=0;i<=n;i++){ const th = t0 + d*i/n; o.push([c[0] + r*Math.cos(th), c[1] + r*Math.sin(th)]); } return o; };
      const eA = sweep(cA, rA, thA0, thAX, 60), eB = sweep(cB, rB, thBX, thB0, 60);
      const bnd = [[0,0], A0].concat(eA, eB, [B0, [0,0]]);
      M.setLine(this.edge, bnd.map(p => W(p[0],p[1]))); this.edge.visible = true;
      M.setLine(this.A, eA.map(p => W(p[0],p[1]))); M.setLine(this.B, eB.map(p => W(p[0],p[1])));
      const pos = []; for(let i=1;i<bnd.length-2;i++){ const p = bnd[i], q = bnd[i+1]; pos.push(0,0.001,0, Rd*p[0],0.001,-Rd*p[1], Rd*q[0],0.001,-Rd*q[1]); }
      this.fill.geometry.dispose(); this.fill.geometry = new T.BufferGeometry(); this.fill.geometry.setAttribute('position', new T.Float32BufferAttribute(pos,3)); this.fill.visible = true;
      M.setPt(this.X, 0, W(X[0],X[1]), GOLD); this.lphi.position.copy(W(X[0]*0.86, X[1]*0.86)).add(V3(0,0.2,0)); setLabelOpacity(this.lphi, 1);
      this.gap.visible = false; setLabelOpacity(this.lgap, 0);
    } else {
      this.edge.visible = false; this.fill.visible = false; M.setPt(this.X, 0, V3(0,0,0), [0,0,0]); setLabelOpacity(this.lphi, 0);
      M.setLine(this.A, aA.map(p => W(p[0],p[1]))); M.setLine(this.B, aB.map(p => W(p[0],p[1])));
      /* common perpendicular: normal m ∝ (tanh a, tanh b) centre, radius √(s²−1)/(cosh a cosh b) */
      const cm = [Math.tanh(a), Math.tanh(b)], rm = Math.sqrt(Math.max(0, s*s - 1))/(Math.cosh(a)*Math.cosh(b));
      const pA = circInter(cm, rm, cA, rA).filter(p => p[0]*p[0] + p[1]*p[1] < 1)[0], pB = circInter(cm, rm, cB, rB).filter(p => p[0]*p[0] + p[1]*p[1] < 1)[0];
      if(pA && pB){ const t0 = Math.atan2(pA[1]-cm[1], pA[0]-cm[0]), t1 = Math.atan2(pB[1]-cm[1], pB[0]-cm[0]); let d = t1 - t0; while(d > Math.PI) d -= 2*Math.PI; while(d < -Math.PI) d += 2*Math.PI;
        const gp = []; for(let i=0;i<=40;i++){ const th = t0 + d*i/40; gp.push(W(cm[0] + rm*Math.cos(th), cm[1] + rm*Math.sin(th))); }
        M.setLine(this.gap, gp); this.gap.visible = true; this.lgap.position.copy(gp[20]).add(V3(0,0.22,0)); setLabelOpacity(this.lgap, 1);
        M.setPt(this.X, 1, W(pA[0],pA[1]), [1,1,1]); M.setPt(this.X, 2, W(pB[0],pB[1]), [1,1,1]); }
    }
    if(closes){ M.setPt(this.X, 1, V3(0,0,0), [0,0,0]); M.setPt(this.X, 2, V3(0,0,0), [0,0,0]); }
    M.flush(this.X);
    this.la.position.copy(W(A0[0] + 0.02, -0.12)); this.lb.position.copy(W(-0.14, B0[1] + 0.03));
    M.setPt(this.feet, 0, W(A0[0],0), CYAN); M.setPt(this.feet, 1, W(0,B0[1]), ROSE); M.flush(this.feet);
    const Ga = gam(za), Gb = gam(zb);
    return [['face a  z_a', f(za,6) + (FILM.on ? '  carbon' : '')], ['face b  z_b', f(zb,6)], ['Γ_a² + Γ_b²', f(Ga*Ga + Gb*Gb,6)], ['sinh a · sinh b', f(s,6)], ['loop', closes ? 'closes' : 'open'], [closes ? 'fourth angle φ' : 'gap d', closes ? f(phi,3) + '°' : f(Math.acosh(Math.max(1,s)),5)]]; } });

/* 5. transport around the loop: the line that is kept (What Transport Keeps) */
eyes.push({ id:'transport', section:'§5 transport', grade:'EXACT', title:'What the loop transport keeps',
  eq:'W = A B A⁻¹ B⁻¹,   A, B: half-steps a = ½ ln z_a, b = ½ ln z_b at right angles\ntr W = 2 − 4 sinh²a sinh²b\ninside the wall |tr W| < 2: lines turn for ever\noutside tr W < −2: one line is selected and kept',
  text:'Carry a line once around the loop of two faces and back. Inside the wall the round trip is a rotation: no line is ever kept, and the iterates walk round the circle of directions. At the wall tr W = −2 and selection is slow. Outside, the round trip selects one line and every starting line is drawn onto it. The three runs use nitrogen’s helium-core opening on both faces, carbon’s on both faces, and carbon’s paired with nitrogen’s.',
  uses:['za','zb'], view:[0.0,1.2,6.6,0],
  make(g, S3){ this.g = g; this.Rr = 2.4; this.dur = 24;
    g.add(ring(this.Rr, 0x8fa3b8, 0.55, 180)); const tk = []; for(let i=0;i<36;i++){ const a = Math.PI*i/36; const c = Math.cos(a), s = Math.sin(a); tk.push(this.Rr*c,0,this.Rr*s, this.Rr*1.05*c,0,this.Rr*1.05*s, -this.Rr*c,0,-this.Rr*s, -this.Rr*1.05*c,0,-this.Rr*1.05*s); } g.add(segs(tk, 0x4a5a6c, 0.5));
    this.dia = []; for(let i=0;i<48;i++){ const l = M.line([V3(0,0,0),V3(1,0,0)], 0xffffff, 0); g.add(l); this.dia.push(l); }
    this.ends = M.points(96, 0.28); g.add(this.ends); this.hist = M.points(800, 0.14); g.add(this.hist); this.fix = M.line([V3(0,0,0),V3(1,0,0)], 0xf2c14e, 0); g.add(this.fix);
    this.lab = addLabel(g, '', '#dfe7ef', V3(0, 0.0, -this.Rr - 0.6), 0.26); this.cap = null; this.za = 5.639665; this.zb = 5.639665; },
  cue(o, dur){ this.dur = dur || 24; }, enter(S){ this.za = S.P.za; this.zb = S.P.zb; }, change(S){ this.za = S.P.za; this.zb = S.P.zb; },
  step(dt, S, tEye){ const t = clock(tEye), Rr = this.Rr;
    let za = this.za, zb = this.zb, run = 'faces as set', lt = t % 14;
    if(FILM.on){ const third = this.dur/3, i = Math.min(2, Math.floor(t/third)); lt = t - i*third;
      [[5.639665,5.639665,'nitrogen on both faces'],[6.079534,6.079534,'carbon on both faces'],[6.079534,5.639665,'carbon paired with nitrogen']].forEach((r,j) => { if(j === i){ za = r[0]; zb = r[1]; run = r[2]; } }); }
    const a = 0.5*Math.log(za), b = 0.5*Math.log(zb), ea = Math.exp(a), ch = Math.cosh(b), sh = Math.sinh(b);
    /* A = diag(e^a, e^−a), B = [[ch, sh],[sh, ch]] */
    const mul = (X,Y) => [X[0]*Y[0]+X[1]*Y[2], X[0]*Y[1]+X[1]*Y[3], X[2]*Y[0]+X[3]*Y[2], X[2]*Y[1]+X[3]*Y[3]];
    const A = [ea,0,0,1/ea], Ai = [1/ea,0,0,ea], B = [ch,sh,sh,ch], Bi = [ch,-sh,-sh,ch], W = mul(mul(A,B), mul(Ai,Bi)), tr = W[0] + W[3];
    const per = 0.42, N = Math.floor(lt/per), frac = (lt % per)/per;
    let v = [Math.cos(0.35), Math.sin(0.35)]; const its = [v];
    for(let i=0;i<N && i<400;i++){ v = [W[0]*v[0] + W[1]*v[1], W[2]*v[0] + W[3]*v[1]]; const nv = Math.hypot(v[0],v[1]); v = [v[0]/nv, v[1]/nv]; its.push(v); }
    for(let j=0;j<this.dia.length;j++){ const idx = its.length - 1 - j; const l = this.dia[j];
      if(idx < 0){ l.material.opacity = 0; M.setPt(this.ends, 2*j, V3(0,0,0), [0,0,0]); M.setPt(this.ends, 2*j+1, V3(0,0,0), [0,0,0]); continue; }
      const u = its[idx], P = V3(Rr*u[0], 0, -Rr*u[1]), Q = P.clone().multiplyScalar(-1); M.setLine(l, [Q, P]);
      const age = j + frac, o = j === 0 ? 1 : Math.pow(0.86, age); l.material.opacity = o*0.95; l.material.color = col(j === 0 ? WHITE : CYAN);
      const c = (j === 0 ? WHITE : CYAN).map(x => x*o); M.setPt(this.ends, 2*j, P, c); M.setPt(this.ends, 2*j+1, Q, c); }
    for(let i=0;i<400;i++){ const u = its[i]; if(!u){ M.setPt(this.hist, 2*i, V3(0,0,0), [0,0,0]); M.setPt(this.hist, 2*i+1, V3(0,0,0), [0,0,0]); continue; } const o = 0.5; M.setPt(this.hist, 2*i, V3(Rr*u[0],0,-Rr*u[1]), CYAN.map(v => v*o)); M.setPt(this.hist, 2*i+1, V3(-Rr*u[0],0,Rr*u[1]), CYAN.map(v => v*o)); }
    M.flush(this.ends); M.flush(this.hist);
    const disc = tr*tr - 4; let kind;
    if(tr < -2){ /* eigenline of the larger |eigenvalue| */ const lam = (tr - Math.sqrt(disc))/2; let e = [W[1], lam - W[0]]; if(Math.hypot(e[0],e[1]) < 1e-12) e = [lam - W[3], W[2]]; const ne = Math.hypot(e[0],e[1]); e = [e[0]/ne, e[1]/ne];
      M.setLine(this.fix, [V3(-Rr*1.12*e[0],0,Rr*1.12*e[1]), V3(Rr*1.12*e[0],0,-Rr*1.12*e[1])]); this.fix.material.opacity = 0.9; kind = 'selects one line'; }
    else { this.fix.material.opacity = 0; kind = Math.abs(tr) < 2 ? 'turns for ever' : 'at the wall'; }
    const rot = Math.abs(tr) < 2 ? Math.acos(tr/2)*180/Math.PI : NaN;
    return [['run', run], ['z_a, z_b', f(za,6) + ', ' + f(zb,6)], ['tr W', f(tr,6)], ['sinh a · sinh b', f(Math.sinh(a)*Math.sinh(b),6)], ['round trip', kind], ['turn per trip', isFinite(rot) ? f(rot,3) + '°' : '—'], ['trips', String(N)]]; } });

/* 6. the speed limit (The Offset Speed Limit) */
eyes.push({ id:'speed', section:'§6 the speed limit', grade:'EXACT (corollary)', title:'Where the reflection can change fastest',
  eq:'θ = arcsin Γ,   per mode |dθ/dt| ≤ 2√E_B\nso |d(Γ²)/dt| ≤ 2√E_B · sin 2θ, largest at θ = 45°:  Γ² = ½\ncensus ν(1 − ν) = (1 − Γ²)/4,  sharpness 8 at the wall',
  text:'Write each step as an angle θ with sin θ = Γ. The speed limit of the offset paper bounds the angle’s rate by twice the square root of the coupling energy, so the returned share Γ² can change at most at a rate proportional to sin 2θ. That bound peaks at 45°, which is exactly the loop wall. The dust on the arc is every step of the table; the eight beyond 45° are the eight outside steps.',
  uses:[], view:[0.0,0.12,7.2,1.4],
  make(g, S3){ this.g = g; const Ra = this.Ra = 2.6;
    const arc = [], env = []; for(let i=0;i<=180;i++){ const th = Math.PI/2*i/180; arc.push(V3(Ra*Math.cos(th), Ra*Math.sin(th), 0)); const r = Ra + 1.15*Math.sin(2*th); env.push(V3(r*Math.cos(th), r*Math.sin(th), 0)); }
    g.add(M.line(arc, 0x8fa3b8, 0.7)); this.env = M.line(env, 0xf2c14e, 0.85); g.add(this.env);
    g.add(segs([0,0,0, Ra*1.6,0,0, 0,0,0, 0,Ra*1.25,0], 0x3c4c5e, 0.6));
    const w = Math.PI/4; g.add(segs([0,0,0, (Ra+1.3)*Math.cos(w),(Ra+1.3)*Math.sin(w),0], 0xf2c14e, 0.9));
    addLabel(g, 'θ = 45°   Γ² = ½', '#f2c14e', V3((Ra+1.55)*Math.cos(w), (Ra+1.55)*Math.sin(w) + 0.15, 0), 0.24);
    addLabel(g, 'rate bound ∝ sin 2θ', '#f2c14e', V3((Ra+1.15)*Math.cos(0.35)+0.4, (Ra+1.15)*Math.sin(0.35), 0), 0.2);
    addLabel(g, 'Γ²', '#dfe7ef', V3(-0.35, Ra + 0.15, 0), 0.24); addLabel(g, '½', '#f2c14e', V3(-0.3, Ra*0.5, 0), 0.24);
    g.add(segs([-0.12,Ra*0.5,0, 0.12,Ra*0.5,0, -0.08,Ra,0, 0.08,Ra,0], 0xf2c14e, 0.9));
    const all = []; EL.forEach(e => { for(let k=0;k<e.ie.length-1;k++){ const G = gam(e.ie[k+1]/e.ie[k]); all.push([Math.asin(G), G*G, e]); } });
    this.dust = M.points(all.length, 0.06); all.forEach((q,i) => { const r = Ra*(0.985 + 0.03*((i*0.6180339) % 1)), dz = 0.5*(((i*0.7548776) % 1) - 0.5); M.setPt(this.dust, i, V3(r*Math.cos(q[0]), r*Math.sin(q[0]), dz), gcol(q[1]).map(v => v*(q[1] > 0.5 ? 1.2 : 0.5))); }); M.flush(this.dust); g.add(this.dust);
    this.p = M.points(1, 0.42); this.q = M.points(1, 0.36); this.qt = M.points(24, 0.2); g.add(this.p, this.q, this.qt);
    this.hl = M.line([V3(0,0,0),V3(1,0,0)], 0xdfe7ef, 0.5); this.rad = M.line([V3(0,0,0),V3(1,0,0)], 0xdfe7ef, 0.8); g.add(this.hl, this.rad); this.sh = makeShock(g); },
  cue(){}, enter(){},
  step(dt, S, tEye){ const t = clock(tEye), Ra = this.Ra, per = 6.5;
    const th = t => Math.PI/2*((t % per)/per);
    const T0 = th(t), G = Math.sin(T0), P = V3(Ra*Math.cos(T0), Ra*Math.sin(T0), 0);
    M.setPt(this.p, 0, P, G*G > 0.5 ? GOLD : CYAN); M.flush(this.p); M.setLine(this.rad, [V3(0,0,0), P]); M.setLine(this.hl, [P, V3(0, Ra*G, 0)]);
    M.setPt(this.q, 0, V3(0, Ra*G*G, 0), [1,1,1]); M.flush(this.q);
    for(let i=0;i<24;i++){ const ti = t - i*0.09; const ok = ti >= 0 && Math.floor(ti/per) === Math.floor(t/per); const gi = Math.sin(th(ti)); const o = ok ? Math.pow(0.88,i) : 0;
      M.setPt(this.qt, i, V3(0.0, Ra*gi*gi, 0), (gi*gi > 0.5 ? GOLD : CYAN).map(v => v*o)); }
    M.flush(this.qt);
    const pc = (t % per)/per; setShock(this.sh, V3(0, Ra*0.5, 0), (pc - 0.5)*per/1.0, 1.0, GOLD, 0.9);
    this.sh.rotation.x = Math.PI/2;
    return [['θ', f(T0*180/Math.PI,2) + '°'], ['Γ = sin θ', f(G,5)], ['Γ²', f(G*G,5)], ['sin 2θ', f(Math.sin(2*T0),4)], ['census ν(1 − ν)', f((1 - G*G)/4,5)], ['sharpness 1/[ν(1 − ν)]', f(4/(1 - G*G),3)]]; } });

/* 7. the entanglement ladder (The Offset Belongs to the Boundary) */
eyes.push({ id:'ladder', section:'§7 the entanglement ladder', grade:'EXACT · MEASURED', title:'Every entanglement level is a peel step',
  eq:'level ε of a block:  z = (1 − ν)/ν = e^ε,   Γ = tanh(ε/2)\ninside the wall  ⇔  |ε| < ln(3 + 2√2) = 1.762747\nladder spacing Δ = 4π K(ũ)/K′(ũ),   ũ = (t₂ − t₁)/(t₂ + t₁)\nũ² = ½  (t₂/t₁ = 3 + 2√2):  K = K′,  Δ = 4π',
  text:'The levels of a block of a dimerised chain form an evenly spaced ladder. Each level is itself a peel step with z = (1 − ν)/ν, so the same wall sorts the rungs: only rungs within ±1.7627 of zero are inside it. The chain’s own bond ratio is a peel ratio too: when ũ² reaches ½, which is t₂/t₁ = 3 + 2√2, the spacing is exactly 4π. On the reference Rice–Mele block (0.6, 1, 0.4) the one rung inside the wall carries 72% of the block’s entanglement entropy.',
  uses:['u'], view:[0.55,0.18,10.5,0],
  make(g, S3){ this.g = g; this.s = 0.19; this.mode = 'sweep'; this.dur = 28; const s = this.s;
    g.add(segs([0,-30*s,0, 0,30*s,0], 0x3c4c5e, 0.6));
    const band = []; [EW, -EW].forEach(e => band.push(...circleArr(2.1, e*s, 120))); g.add(segs(band, 0xf2c14e, 0.95));
    const bandMesh = new T.Mesh(new T.CylinderGeometry(2.1,2.1,2*EW*s,64,1,true), new T.MeshBasicMaterial({color:0xf2c14e, transparent:true, opacity:0.07, side:T.DoubleSide, depthWrite:false, blending:T.AdditiveBlending})); g.add(bandMesh);
    addLabel(g, 'inside the wall  |ε| < 1.7627', '#f2c14e', V3(3.9, 0.0, 0), 0.2);
    this.rungs = []; for(let i=0;i<24;i++){ const r = ring(1, 0xffffff, 0, 96); g.add(r); const c = M.points(1, 0.5); g.add(c); const lb = addLabel(g, '', '#8a9aab', V3(0,0,0), 0.18); this.rungs.push({r, c, lb}); }
    this.ticks = []; for(let n=-2;n<=2;n++){ const lb = addLabel(g, '', '#6f8296', V3(-1.9, 0, 0), 0.18); this.ticks.push(lb); }
    this.sites = M.points(14, 0.22); g.add(this.sites); this.bonds = []; for(let i=0;i<13;i++){ const b = M.line([V3(0,0,0),V3(1,0,0)], 0xa9bdd2, 0.5); g.add(b); this.bonds.push(b); }
    this.spacingLbl = addLabel(g, '', '#ffffff', V3(-2.6, 2.2, 0), 0.26); this.sub = addLabel(g, '', '#a9bdd2', V3(0, -7.0, 0), 0.22); this.u = Math.SQRT1_2; },
  cue(o, dur){ this.mode = o.mode || 'sweep'; this.dur = dur || 28; }, enter(S){ this.u = S.P.u; }, change(S){ this.u = S.P.u; },
  step(dt, S, tEye){ const t = clock(tEye), s = this.s; let u = this.u, mode = this.mode, levels, sizes = null;
    if(FILM.on && mode === 'sweep'){ const ph = clamp(t/this.dur, 0, 1); u = ph < 0.62 ? 0.30 + (Math.SQRT1_2 - 0.30)*ease(ph/0.62) : Math.SQRT1_2; }
    let D = 0, refShare = null;
    if(mode === 'ref'){ levels = LD.ref.filter(x => Math.abs(x) < 26); const nu = levels.map(e => 1/(1 + Math.exp(e))), ent = nu.map(v => -(v*Math.log(v) + (1-v)*Math.log(1-v))), tot = ent.reduce((a,b) => a+b, 0);
      sizes = ent.map(x => x/tot); refShare = sizes.filter((x,i) => Math.abs(levels[i]) < EW).reduce((a,b) => a+b, 0); }
    else { D = ladderSpacing(u); levels = []; for(let n=-6;n<=6;n++){ const e = n*D; if(Math.abs(e) < 29) levels.push(e); } }
    this.rungs.forEach((R, i) => { if(i >= levels.length){ R.r.visible = false; R.c.visible = false; setLabelOpacity(R.lb, 0); return; }
      const e = levels[i], inside = Math.abs(e) < EW, G = Math.tanh(e/2), rad = sizes ? 0.45 + 2.6*Math.sqrt(sizes[i]) : (inside ? 1.75 : 1.3);
      R.r.visible = true; R.r.position.set(0, e*s, 0); R.r.scale.set(rad, 1, rad); R.r.material.color = col(inside ? CYAN : PALE); R.r.material.opacity = inside ? 1 : 0.55;
      R.c.visible = true; M.setPt(R.c, 0, V3(0, e*s, 0), inside ? CYAN : [0.25,0.3,0.38]); M.flush(R.c);
      setLabelOpacity(R.lb, 0); });
    const lab = (l, txt) => { if(l.userData.txt === txt) return; l.userData.txt = txt; const n = M.label(txt, '#ffffff', LS*0.26); l.material.map = n.material.map; l.scale.copy(n.scale); l.material.needsUpdate = true; };
    lab(this.spacingLbl, mode === 'ref' ? 'one rung inside: ' + f(100*refShare,1) + '% of the entropy' : 'spacing Δ = ' + f(D,4) + (Math.abs(u*u - 0.5) < 2e-4 ? '  = 4π' : ''));
    this.spacingLbl.position.set(-4.4, mode === 'ref' ? 1.3 : D*s*0.5, 0);
    const t1 = 1, t2 = mode === 'ref' ? 1/0.6 : (1 + u)/(1 - u), sc = 1/(t2 + 0.0001);
    for(let i=0;i<14;i++) M.setPt(this.sites, i, V3(-3.25 + 0.5*i, -6.4, 0), mode === 'ref' ? (i % 2 ? [0.5,0.6,1] : [1,0.6,0.5]) : [0.85,0.9,1]); M.flush(this.sites);
    this.bonds.forEach((b,i) => { M.setLine(b, [V3(-3.25 + 0.5*i, -6.4, 0), V3(-3.25 + 0.5*(i+1), -6.4, 0)]); b.material.opacity = i % 2 ? 0.95 : 0.15 + 0.8*(t1/t2); });
    lab(this.sub, mode === 'ref' ? 'Rice–Mele block  t₁ = 0.6, t₂ = 1, v = 0.4' : 't₂/t₁ = ' + f(t2,4) + (Math.abs(u*u - 0.5) < 2e-4 ? '  = 3 + 2√2' : ''));
    return mode === 'ref' ? [['block', 'Rice–Mele (0.6, 1, 0.4), 41 sites'], ['rungs inside the wall', String(levels.filter(e => Math.abs(e) < EW).length)], ['inside rung ε', f(levels.filter(e => Math.abs(e) < EW)[0],4)], ['its share of the entropy', f(100*refShare,1) + '%']]
      : [['ũ', f(u,5)], ['ũ²', f(u*u,5)], ['t₂/t₁', f(t2,5)], ['spacing Δ', f(D,5)], ['4π', f(4*Math.PI,5)], ['rungs inside the wall', String(levels.filter(e => Math.abs(e) < EW).length)]]; } });

/* 8. reversal and mirror: one law for both signs */
eyes.push({ id:'reverse', section:'§8 the two signs', grade:'EXACT', title:'Reversal flips the peel, keeps the screw',
  eq:'reversing an n-step oriented volume multiplies it by (−1)^{n(n+1)/2}\npeel reflection Γ, n = 1:  reversed, Γ → −Γ (z → 1/z, Γ² kept)\nscrew sign χ = (d₀ × d₁)·d₂, n = 3:  reversed, χ kept;  mirrored, χ flips',
  text:'Two signs follow one rule. A peel step is a one-step oriented quantity: run it backwards and z becomes 1/z, so Γ changes sign while Γ² is kept. The screw sign of the shortest-contact chain of trigonal selenium is a three-step oriented volume: reversing the path leaves it unchanged, and only a mirror flips it.',
  uses:[], view:[0.25,0.25,9.2,0.9],
  make(g, S3){ this.g = g; this.dur = 18;
    const e = EL[5]; this.ie = [e.ie[3], e.ie[4]]; this.zc = this.ie[1]/this.ie[0];
    this.pA = V3(-4.3, 0.2, 0); this.pB = V3(-1.7, 2.3, 0); this.L = makeLink(g); this.nod = M.points(2, 0.34); g.add(this.nod);
    this.arrow = new T.Mesh(new T.ConeGeometry(0.16, 0.42, 20), new T.MeshBasicMaterial({color:0xf2c14e, transparent:true, opacity:0.95})); g.add(this.arrow);
    this.l1 = addLabel(g, 'carbon removal 4  64.49 eV', '#a9bdd2', V3(-4.3, -0.25, 0), 0.2); this.l2 = addLabel(g, 'removal 5  392.09 eV', '#a9bdd2', V3(-1.7, 2.75, 0), 0.2);
    this.gl = addLabel(g, '', '#ffffff', V3(-3.0, -1.0, 0), 0.26);
    const [a, c, u] = D.screw.Se, r = Math.abs(a*u), sc = 1.05; this.cr = {r, c, sc};
    this.hel = new T.Group(); this.hel.position.set(3.0, -1.4, 0); g.add(this.hel);
    const P = j => V3(r*Math.cos(2*Math.PI*j/3)*sc, j*c/3*sc*0.42, r*Math.sin(2*Math.PI*j/3)*sc);
    const chain = []; for(let j=-2;j<=8;j++) chain.push(P(j)); this.hel.add(M.line(chain, 0x63d3ff, 0.4));
    const pts = M.points(chain.length, 0.16); chain.forEach((q,i) => M.setPt(pts, i, q, [0.75,0.85,1])); M.flush(pts); this.hel.add(pts);
    this.four = [P(0),P(1),P(2),P(3)]; this.segs = [0,1,2].map(i => { const l = M.line([this.four[i], this.four[i+1]], 0xf2c14e, 1); this.hel.add(l); return l; });
    this.beads = M.points(4, 0.3); this.hel.add(this.beads); this.walker = M.points(1, 0.4); this.hel.add(this.walker);
    this.xl = addLabel(g, '', '#ffffff', V3(3.0, -2.2, 0), 0.26); addLabel(g, 'selenium screw (P3₁21)', '#a9bdd2', V3(3.0, 4.2, 0), 0.22);
    const crossChi = (p) => { const d = [0,1,2].map(i => [p[i+1][0]-p[i][0], p[i+1][1]-p[i][1], p[i+1][2]-p[i][2]]); const x = [d[0][1]*d[1][2]-d[0][2]*d[1][1], d[0][2]*d[1][0]-d[0][0]*d[1][2], d[0][0]*d[1][1]-d[0][1]*d[1][0]]; return x[0]*d[2][0] + x[1]*d[2][1] + x[2]*d[2][2]; };
    const cp = j => [r*Math.cos(2*Math.PI*j/3), r*Math.sin(2*Math.PI*j/3), j*c/3];
    this.chiF = crossChi([cp(0),cp(1),cp(2),cp(3)]); this.chiR = crossChi([cp(3),cp(2),cp(1),cp(0)]); this.chiM = crossChi([0,1,2,3].map(j => { const q = cp(j); return [-q[0], q[1], q[2]]; })); },
  cue(o, dur){ this.dur = dur || 18; }, enter(){},
  lab(l, txt, colr){ if(l.userData.txt === txt) return; l.userData.txt = txt; const n = M.label(txt, colr || '#ffffff', LS*0.26); l.material.map = n.material.map; l.scale.copy(n.scale); l.material.needsUpdate = true; },
  step(dt, S, tEye){ const t = clock(tEye), d = FILM.on ? this.dur : 18, ph = (t % d)/d;
    const stage = ph < 0.34 ? 0 : ph < 0.67 ? 1 : 2, w = stage === 1 ? ease((ph - 0.34)/0.08) : stage === 2 ? 1 : 0, m = stage === 2 ? ease((ph - 0.67)/0.1) : 0;
    const rev = stage >= 1, z = rev ? 1/this.zc : this.zc, G = gam(z);
    const from = rev ? this.pB : this.pA, to = rev ? this.pA : this.pB;
    setLink(this.L, this.pA, this.pB, 0.42, gam(this.zc), 1, 1.3 + 0.4*Math.sin(t*3), 1, 1);
    M.setPt(this.nod, 0, this.pA, [0.85,0.9,1]); M.setPt(this.nod, 1, this.pB, [0.85,0.9,1]); M.flush(this.nod);
    const dir = to.clone().sub(from).normalize(), mid = this.pA.clone().lerp(this.pB, 0.5).addScaledVector(dir, 0.0);
    this.arrow.position.copy(mid.clone().addScaledVector(dir, 0.75)); this.arrow.quaternion.setFromUnitVectors(V3(0,1,0), dir);
    this.lab(this.gl, (rev ? 'reversed:  ' : 'forward:  ') + 'Γ = ' + (G >= 0 ? '+' : '−') + f(Math.abs(G),4) + '   Γ² = ' + f(G*G,4), rev ? '#ff8fc2' : '#f2c14e');
    this.hel.scale.x = 1 - 2*m;
    const order = rev ? [3,2,1,0] : [0,1,2,3]; this.four.forEach((q,i) => M.setPt(this.beads, i, q, i === order[0] ? [0.45,1,0.6] : GOLD)); M.flush(this.beads);
    const wk = (t*0.9) % 3, i0 = Math.floor(wk), fr = wk - i0, A = this.four[order[i0]], B = this.four[order[i0+1]]; M.setPt(this.walker, 0, A.clone().lerp(B, fr), [1,1,1]); M.flush(this.walker);
    const chi = stage === 2 ? this.chiM : (rev ? this.chiR : this.chiF);
    this.lab(this.xl, (stage === 2 ? 'mirrored:  ' : rev ? 'path reversed:  ' : 'forward:  ') + 'χ = ' + (chi >= 0 ? '+' : '−') + f(Math.abs(chi),4) + ' Å³', stage === 2 ? '#ff8fc2' : '#f2c14e');
    return [['peel step', 'carbon, removal 4 → 5'], ['z', f(z,6)], ['Γ', f(G,6)], ['Γ²', f(G*G,6)], ['screw path', stage === 2 ? 'mirrored crystal' : rev ? 'reversed' : 'forward'], ['χ (Å³)', f(chi,4)]]; } });

/* 9. electrophilicity meets hardness: the anion rung */
eyes.push({ id:'anion', section:'§9 the anion rung', grade:'EXACT · MEASURED', title:'Electrophilicity meets hardness',
  eq:'η = (IE − EA)/2,   χ = (IE + EA)/2,   ω = χ²/(2η)\nΓ₀ = (IE − EA)/(IE + EA) = η/χ,   ω/η = 1/(2Γ₀²)\nthe wall Γ₀² = ½ is the plane ω = η\nlicence: Γ₀² < 1 always, its determinant is IE · EA',
  text:'The first rung of every bound anion is a peel step from the electron affinity to the first ionisation energy. Its reflection is hardness over electronegativity, and the loop wall becomes the plane where electrophilicity equals hardness. Height is ln(ω/η): the twelve elements above the plane, the halogens with sulfur, selenium, tellurium, silver, iridium, platinum and gold, are inside the wall. Below the plane the anion rung opens; the rung itself fails only as the affinity goes to zero.',
  uses:[], view:[0.7,0.38,10.6,0.3],
  make(g, S3){ this.g = g; this.dur = 36;
    const an = EL.filter(e => e.ea).map(e => { const IE = e.ie[0], EA = e.ea, eta = (IE - EA)/2, chi = (IE + EA)/2, om = chi*chi/(2*eta), G0 = eta/chi;
      return {e, IE, EA, eta, chi, om, G0, P: V3((EA - 1.7)*1.75, Math.log(om/eta)*3.4, (9.2 - IE)*0.62)}; });
    this.an = an;
    const pl = []; const Sx = [-3.4, 3.4], Sz = [-3.3, 3.6]; for(let i=0;i<=16;i++){ const x = Sx[0] + (Sx[1]-Sx[0])*i/16; pl.push(x,0,Sz[0], x,0,Sz[1]); } for(let i=0;i<=14;i++){ const z = Sz[0] + (Sz[1]-Sz[0])*i/14; pl.push(Sx[0],0,z, Sx[1],0,z); }
    this.plane = segs(pl, 0xf2c14e, 0.32); g.add(this.plane);
    const pm = new T.Mesh(new T.PlaneGeometry(Sx[1]-Sx[0], Sz[1]-Sz[0]), new T.MeshBasicMaterial({color:0xf2c14e, transparent:true, opacity:0.05, side:T.DoubleSide, depthWrite:false, blending:T.AdditiveBlending})); pm.rotation.x = -Math.PI/2; pm.position.set((Sx[0]+Sx[1])/2, 0, (Sz[0]+Sz[1])/2); g.add(pm);
    addLabel(g, 'ω = η   (Γ₀² = ½)', '#f2c14e', V3(Sx[1] - 0.6, 0.2, Sz[0] - 0.2), 0.26);
    addLabel(g, 'electron affinity EA →', '#8a9aab', V3(1.4, -0.3, Sz[1] - 0.2), 0.18); addLabel(g, '← first ionisation energy IE', '#8a9aab', V3(Sx[0] - 0.6, -0.3, 0.0), 0.2); addLabel(g, 'height ln(ω/η)', '#8a9aab', V3(Sx[0], 2.6, Sz[0]), 0.2);
    this.pts = M.points(an.length, 0.3); g.add(this.pts); this.drops = an.map(a => { const l = M.line([V3(a.P.x,0,a.P.z), a.P], 0xa9bdd2, 0.0); g.add(l); return l; });
    const key = new Set(['F','Cl','Br','I','At','S','Se','Te','Ag','Ir','Pt','Au','H','Li','Cs','C','O','Si']);
    this.lbs = an.map(a => key.has(a.e.s) ? addLabel(g, NAME(a.e), a.G0*a.G0 < 0.5 ? '#bfe9ff' : '#8a9aab', a.P.clone().add(V3(0, a.P.y >= 0 ? 0.3 : -0.3, 0)), 0.2) : null);
    this.focus = ['Cl','F','Au','Pt','S','Si','O','H','Ca'].map(s => an.find(a => a.e.s === s)).filter(Boolean);
    this.ring = ring(0.35, 0xffffff, 0.9, 48); g.add(this.ring); },
  cue(o, dur){ this.dur = dur || 36; }, enter(){},
  step(dt, S, tEye){ const t = clock(tEye), rise = FILM.on ? this.dur*0.38 : 6;
    this.an.forEach((a,i) => { const k = clamp((t - 0.5 - i*(rise/this.an.length))/1.2, 0, 1), y = a.P.y*ease(k), inside = a.G0*a.G0 < 0.5;
      const P = V3(a.P.x, y, a.P.z); M.setPt(this.pts, i, P, k > 0 ? (inside ? CYAN.map(v => v*1.2) : [0.45,0.52,0.62]) : [0,0,0]);
      M.setLine(this.drops[i], [V3(a.P.x,0,a.P.z), P]); this.drops[i].material.opacity = k > 0 ? (inside ? 0.6 : 0.25) : 0;
      if(this.lbs[i]){ this.lbs[i].position.set(a.P.x, y + (a.P.y >= 0 ? 0.3 : -0.3), a.P.z); setLabelOpacity(this.lbs[i], ease((k - 0.6)/0.4)*0.95); } });
    M.flush(this.pts);
    const ft = Math.max(0, t - rise - 1), per = 3.2, fi = Math.floor(ft/per) % this.focus.length, a = this.focus[fi];
    this.ring.position.copy(a.P); this.ring.visible = t > rise + 1; const pul = 1 + 0.25*Math.sin(t*4); this.ring.scale.set(pul,1,pul);
    this.plane.material.opacity = 0.28 + 0.12*Math.sin(t*1.3);
    const inside = this.an.filter(x => x.G0*x.G0 < 0.5).length;
    return [['element', NAME(a.e)], ['IE, EA (eV)', f(a.IE,4) + ', ' + f(a.EA,4)], ['η, χ (eV)', f(a.eta,4) + ', ' + f(a.chi,4)], ['ω (eV)', f(a.om,4)], ['ω/η = 1/(2Γ₀²)', f(a.om/a.eta,4)], ['Γ₀²', f(a.G0*a.G0,5) + (a.G0*a.G0 < 0.5 ? '  inside' : '  outside')], ['IE · EA (eV²)', f(a.IE*a.EA,4)], ['inside the wall', inside + ' of ' + this.an.length + ' anions']]; } });

eyes.forEach(e => EYE[e.id] = e);

/* ---------------- film timeline, locked to the song (273.24 s) ---------------- */
const SONG = 273.24;
const CUES = [
  { t:0,   eye:'wall',  cam:{yaw:[0.2,0.75], pitch:[1.15,0.72], dist:[9.8,8.4], ty:0},
    cap:['The Loop Wall', 'Every removal step on one disk', 'Γ = (z − 1)/(z + 1),   the wall Γ² = ½,   z = 3 + 2√2'] },
  { t:16,  eye:'chain', opts:{Z:6, mode:'build'}, cam:{yaw:[0.9,1.9], pitch:[0.14,0.24], dist:[14.6,13.0], ty:'eye'},
    cap:['Carbon, built from the nucleus', 'Each bound electron adds a link: bright core E⁻, fine outline E⁺', 'E⁻/E⁺ = Γ²;  the gold ring on each link is Γ² = ½'] },
  { t:44,  eye:'chain', opts:{Z:6, mode:'peel'}, cam:{yaw:[1.9,3.0], pitch:[0.24,0.16], dist:[13.0,13.8], ty:'eye'},
    cap:['Carbon, peeled from the outside in', 'Each removal releases its link’s connection energy; the outline stays as the record', 'removal 4 → 5: z = 6.0795, Γ² = 0.5147, outside the wall'] },
  { t:72,  eye:'table', opts:{mode:'sweep'}, cam:{yaw:[0.1,1.55], pitch:[0.5,0.36], dist:[17.0,15.2], ty:2.2},
    cap:['Hydrogen to astatine', '85 chains, 3,570 links, eight outside the wall', 'every one a first opening of a noble-gas core'] },
  { t:102, eye:'faces', opts:{}, cam:{yaw:[0.05,0.35], pitch:[1.22,0.98], dist:[9.2,8.4], ty:-0.3},
    cap:['Two faces, one loop', 'Carbon’s helium-core opening against a second face swept through the crossing', 'closes ⇔ sinh a · sinh b < 1:  cos φ closed,  cosh d open'] },
  { t:128, eye:'transport', opts:{}, cam:{yaw:[0.0,0.6], pitch:[1.25,1.05], dist:[7.8,7.2], ty:-0.2},
    cap:['What the loop transport keeps', 'Nitrogen on both faces, carbon on both, then carbon with nitrogen', 'tr W = 2 − 4 sinh²a sinh²b;  tr W < −2 selects one line'] },
  { t:150, eye:'speed', opts:{}, cam:{yaw:[-0.25,0.3], pitch:[0.1,0.22], dist:[7.4,7.0], ty:1.5},
    cap:['The speed limit at the wall', 'With Γ = sin θ the returned share can change fastest at 45°', '|d(Γ²)/dt| ≤ 2√E_B · sin 2θ,  largest at Γ² = ½'] },
  { t:170, eye:'ladder', opts:{mode:'sweep'}, cam:{yaw:[0.35,0.8], pitch:[0.14,0.2], dist:[11.4,10.6], ty:-0.4},
    cap:['The entanglement ladder', 'Every level of a block is a peel step; at ũ² = ½ the spacing is 4π', 'z = (1 − ν)/ν,   Γ = tanh(ε/2),   Δ = 4π K(ũ)/K′(ũ)'] },
  { t:186, eye:'ladder', opts:{mode:'ref'}, cam:{yaw:[0.8,1.2], pitch:[0.2,0.3], dist:[10.6,9.8], ty:-0.4},
    cap:['One rung inside the wall', 'Rice–Mele block (0.6, 1, 0.4): the inside rung ε = 0.9971', 'carries 72% of the block’s entanglement entropy'] },
  { t:198, eye:'reverse', opts:{}, cam:{yaw:[0.1,0.45], pitch:[0.2,0.28], dist:[9.6,9.0], ty:0.9},
    cap:['Two signs, one rule', 'Reversal multiplies an n-step volume by (−1)^{n(n+1)/2}', 'the peel Γ flips (n = 1); the selenium screw χ is kept (n = 3), and flips only in a mirror'] },
  { t:216, eye:'anion', opts:{}, cam:{yaw:[0.55,1.05], pitch:[0.36,0.27], dist:[10.2,9.4], ty:0.9},
    cap:['Electrophilicity meets hardness', 'The anion rung: Γ₀ = η/χ, and the wall is the plane ω = η', 'twelve of 65 anions stand inside it'] },
  { t:252, eye:'table', opts:{mode:'final'}, cam:{yaw:[1.6,2.6], pitch:[0.36,0.55], dist:[15.0,17.5], ty:1.6},
    cap:['The Loop Wall', 'Jeromie Beasley', ''] }
];
CUES.forEach((c,i) => c.end = i + 1 < CUES.length ? CUES[i+1].t : SONG);
const cueAt = t => { let i = 0; for(let k=0;k<CUES.length;k++) if(t >= CUES[k].t) i = k; return i; };
const lerp = (r, x) => Array.isArray(r) ? r[0] + (r[1]-r[0])*x : r;

/* the kit hands each eye the stage when it is made; keep one handle for the film director */
eyes.forEach(e => { const mk = e.make; e.make = function(g, S3){ window.__S3 = S3; return mk.call(this, g, S3); }; });

/* ---------------- run: panel (eye mode) on the parts kit ---------------- */
M.run({ title:'The Loop Wall', byline:'Jeromie Beasley · element paper mixer v2 · hydrogen to astatine',
  note:'Film plays the timeline against the song.',
  feed:{ params:[
    {id:'Z', label:'element Z (chain)', min:1, max:85, step:1, value:6},
    {id:'za', label:'face a ratio z_a', min:1.5, max:9, step:0.000001, value:6.079534},
    {id:'zb', label:'face b ratio z_b', min:1.5, max:9, step:0.000001, value:5.639665},
    {id:'u', label:'rail ũ (ladder)', min:0.2, max:0.95, step:0.0001, value:0.7071}],
    build(P){ return {P:Object.assign({}, P)}; } },
  eyes, film: eyes.map(e => e.id) });

/* ---------------- film director ---------------- */
const API = window.MIXER_API, $ = id => document.getElementById(id);
window.__S3.scene.background = new T.Color(0x000000);
{ const n = 1400, st = M.points(n, 0.32); let s0 = 7; const rnd = () => { s0 = (s0*16807) % 2147483647; return s0/2147483647; };
  for(let i=0;i<n;i++){ const u = 2*rnd() - 1, ph = 2*Math.PI*rnd(), r = 38 + 30*rnd(), q = Math.sqrt(1-u*u), b = 0.08 + 0.22*rnd()*rnd();
    M.setPt(st, i, V3(r*q*Math.cos(ph), r*u, r*q*Math.sin(ph)), [b*0.85, b*0.92, b]); } M.flush(st); window.__S3.scene.add(st); }

const css = document.createElement('style'); css.textContent = `
:root{--void:#000}
body{background:#000}
#cap{position:fixed;left:5.2vw;bottom:7.2vh;max-width:62vw;pointer-events:none;color:#e8eef5;opacity:0;transition:none;text-shadow:0 0 18px rgba(0,0,0,.95),0 0 4px rgba(0,0,0,.9)}
#cap .eb{font:600 1.05vw/1.2 "Chakra Petch","Segoe UI",system-ui,sans-serif;letter-spacing:.22em;text-transform:uppercase;color:#f2c14e}
#cap .tt{font:500 2.35vw/1.15 "Inter Tight",system-ui,sans-serif;margin:.35vw 0 .3vw;letter-spacing:.01em}
#cap .ln{font:400 1.12vw/1.4 "Inter Tight",system-ui,sans-serif;color:#b9c7d6}
#cap .eq{font:400 1.02vw/1.4 "JetBrains Mono",ui-monospace,Menlo,Consolas,monospace;color:#f2c14e;margin-top:.35vw}
#cap .rule{width:4.2vw;height:1px;background:#f2c14e;opacity:.8;margin:.45vw 0 .2vw}
#titlecard.end{place-content:start center;padding-top:8vh}
#titlecard{position:fixed;inset:0;display:grid;place-content:center;text-align:center;pointer-events:none;opacity:0;text-shadow:0 0 24px rgba(0,0,0,1)}
#titlecard .a{font:500 3.1vw/1.1 "Inter Tight",system-ui,sans-serif;color:#f4f7fb;letter-spacing:.02em}
#titlecard .b{font:600 1.05vw/1.2 "Chakra Petch","Segoe UI",system-ui,sans-serif;letter-spacing:.3em;text-transform:uppercase;color:#f2c14e;margin-top:1.1vw}
#fade{position:fixed;inset:0;background:#000;pointer-events:none;opacity:0}
.filmrow{display:flex;flex-wrap:wrap;gap:6px}.filmrow button{font-size:12px;padding:4px 9px}
#scrub{width:100%;accent-color:#f2c14e}.tc{font-family:var(--mono);font-size:11px;color:var(--dim)}
body.film .cleanexit{display:none}
#m_film,#sec,#o_sec{display:none}label:has(#sec){display:none}`;
document.head.append(css);
document.body.insertAdjacentHTML('beforeend', `<div id="cap"><div class="eb"></div><div class="rule"></div><div class="tt"></div><div class="ln"></div><div class="eq"></div></div>
<div id="titlecard"><div class="a">Where the Wanting Meets the Stone</div><div class="b">The Loop Wall · Jeromie Beasley</div></div><div id="fade"></div>`);
const panel = $('panel'); panel.insertAdjacentHTML('beforeend', `<div class="filmrow"><button id="f_play">Play film with song</button><button id="f_stop">Stop film</button><button id="f_caps" aria-pressed="true">Captions</button></div>
<label class="tc">film time <span id="f_tc">0:00.0</span> / 4:33.2<input id="scrub" type="range" min="0" max="${SONG}" step="0.1" value="0"></label>`);
const song = $('song');
let caps = true;
$('f_caps').addEventListener('click', e => { caps = !caps; e.target.setAttribute('aria-pressed', caps); });


function setCap(c){ const [tt, ln, eq] = c.cap; $('cap').querySelector('.eb').textContent = EYE[c.eye].section.replace(/^§\d+\s*/, '');
  $('cap').querySelector('.tt').textContent = tt; $('cap').querySelector('.ln').textContent = ln; $('cap').querySelector('.eq').textContent = eq; }
function apply(t){
  t = clamp(t, 0, SONG - 0.001); FILM.t = t;
  const i = cueAt(t), c = CUES[i];
  if(i !== FILM.cue){ FILM.cue = i; API.show(c.eye); const e = EYE[c.eye]; if(e.cue) e.cue(c.opts || {}, c.end - c.t); setCap(c); }
  FILM.local = t - c.t; FILM.dur = c.end - c.t;
  const x = clamp(FILM.local/FILM.dur, 0, 1), V = window.__S3 ? window.__S3.view : null, e = EYE[c.eye];
  if(V){ V.auto = false; V.yaw = lerp(c.cam.yaw, ease(x)*0.5 + x*0.5); V.pitch = lerp(c.cam.pitch, ease(x)); V.dist = lerp(c.cam.dist, ease(x)); V.ty = c.cam.ty === 'eye' ? (e.ty || 0) : c.cam.ty; }
  /* captions: in after 0.9 s, out 1.2 s before the cut; the final card reads as a title */
  const capIn = clamp((FILM.local - 0.9)/0.8, 0, 1), capOut = clamp((c.end - t - 0.6)/0.8, 0, 1);
  $('cap').style.opacity = caps && c.cap[0] && i !== CUES.length - 1 ? Math.min(capIn, capOut) : 0;
  const tcA = clamp((t - 0.4)/0.9, 0, 1)*clamp((7.5 - t)/1.2, 0, 1), tcB = clamp((t - 256)/1.6, 0, 1)*clamp((SONG - t)/1.0, 0, 1);
  const tc = $('titlecard'); tc.style.opacity = Math.max(tcA, tcB); tc.classList.toggle('end', t > 200);
  /* a short dip to black on each cut, symmetric about the cue boundary */
  let fd = 0; CUES.forEach(q => { if(q.t > 0) fd = Math.max(fd, 1 - Math.abs(t - q.t)/0.38); }); fd = Math.max(fd, clamp((t - (SONG - 1.6))/1.4, 0, 1), clamp(1 - t/0.8, 0, 1));
  $('fade').style.opacity = fd;
  $('f_tc').textContent = Math.floor(t/60) + ':' + (t % 60).toFixed(1).padStart(4, '0'); $('scrub').value = t;
}
function filmView(){ document.body.classList.add('clean','film'); if(window.__S3 && !window.__S3.view.panel){ window.__S3.view.panel = true; window.__S3.resize(); } }
function startFilm(from){ FILM.on = true; FILM.cue = -1; filmView(); if(window.__S3){ window.__S3.view.panel = false; window.__S3.resize(); }
  if(song){ song.currentTime = from || 0; song.play().catch(() => {}); } FILM.wall0 = performance.now()/1000 - (from || 0); apply(from || 0); }
function stopFilm(){ FILM.on = false; document.body.classList.remove('film'); if(song) song.pause(); $('cap').style.opacity = 0; $('titlecard').style.opacity = 0; $('fade').style.opacity = 0; FILM.cue = -1; }
$('f_play').addEventListener('click', () => startFilm(+$('scrub').value || 0));
$('f_stop').addEventListener('click', stopFilm);
$('scrub').addEventListener('input', e => { const t = +e.target.value; if(FILM.on){ if(song) song.currentTime = t; FILM.wall0 = performance.now()/1000 - t; } apply(t); });
document.addEventListener('keydown', e => { if(e.key === ' ' && FILM.on){ e.preventDefault(); if(song.paused) song.play(); else song.pause(); } if(e.key === 'Escape' && FILM.on) stopFilm(); });
(function loop(){ if(FILM.on && !FILM.manual){ const t = song && !isNaN(song.duration) && song.currentTime > 0 ? song.currentTime : performance.now()/1000 - FILM.wall0; apply(t); if(t >= SONG - 0.05) stopFilm(); } requestAnimationFrame(loop); })();

/* exact frame for recording: FILM.renderAt(t) */
FILM.renderAt = t => { FILM.on = true; FILM.manual = true; filmView(); apply(t); const S3 = window.__S3, e = EYE[CUES[FILM.cue].eye];
  e.step(1/24, API.S, FILM.local); const V = S3.view, cam = S3.camera, Dd = V.dist;
  cam.position.set(Dd*Math.cos(V.pitch)*Math.sin(V.yaw), V.ty + Dd*Math.sin(V.pitch), Dd*Math.cos(V.pitch)*Math.cos(V.yaw)); cam.lookAt(0, V.ty, 0);
  S3.renderer.render(S3.scene, cam); return FILM.cue; };
FILM.cues = CUES; FILM.song = SONG; FILM.start = startFilm; FILM.stop = stopFilm;
window.FILM = FILM;
})();
