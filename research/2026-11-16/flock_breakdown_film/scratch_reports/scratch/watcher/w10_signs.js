// SCRIPT: W10-SIGNS (watcher) first-principles sign of a face on every link, from the Fresnel rule r = (Y1-Y2)/(Y1+Y2) alone.
// Convention taken from the CENTRE-ARM link of the code itself: light leaving the centre cell outward reflects +tanh(r/2), i.e. Yc/Yarm = z (side 1 = centre cell).
// Then for ANY link, light passing a face of arm k INTO the centre cell must reflect with (Yarm-Yc)/(Yarm+Yc) = -tanh(r_k/2), and OUT of the centre cell +tanh(r_k/2).
// This script reads the code's marks (forward = i->j direction, reflection of forward light = +rho by the scatterer in FL step lines 81-82) and compares.
const FL = require('/home/claude/balls/w/fl/fl_math_v1.js');
const fres = (Y1, Y2) => (Y1 - Y2) / (Y1 + Y2);
let bad = 0, n = 0;
for (const zz of [[3,5,7],[7,9,13]]) {
  const W = FL.makeWorld({ N: 7, z: zz });
  for (const l of W.links) {
    const faces = l.marks.filter(m => m.kind === 'face');
    for (const m of l.marks) { if (m.kind !== 'face') continue;
      // which arm does this face belong to, and is forward light entering or leaving the centre cell?
      let arm, entering;
      if (l.i === 0) { arm = l.j; entering = false; }           // centre -> arm: leaves centre
      else { const first = (m === faces[0]); arm = first ? l.i : l.j; entering = first; } // arm i -> centre cell (first face) ; centre cell -> arm j (last face)
      const z = Math.exp(W.balls[arm].r), Yc = z, Ya = 1;      // Yc/Ya = z : side 1 = centre
      const expect = entering ? fres(Ya, Yc) : fres(Yc, Ya);
      const ok = Math.abs(expect - m.rho) < 1e-12; n++; if (!ok) { bad++; }
      if (zz[0] === 3 && (l.i === 0 || ok === false) && (l.j < 4 || !ok)) {} }
  }
  // print one representative of each link kind
  const l01 = W.links.find(l => l.i === 0), laa = W.links.find(l => l.i > 0);
  console.log('z=' + zz + ' centre-arm link (0,' + l01.j + ') marks: ' + l01.marks.map(m => m.kind + ' rho=' + m.rho.toFixed(6)).join(', '));
  console.log('         arm-arm link (' + laa.i + ',' + laa.j + ') marks: ' + laa.marks.map(m => m.kind + ' rho=' + m.rho.toFixed(6)).join(', '));
  const a = laa.i, b = laa.j; const Ga = Math.tanh(W.balls[a].r/2), Gb = Math.tanh(W.balls[b].r/2);
  console.log('         Fresnel expects: face a (entering centre) ' + (-Ga).toFixed(6) + ', face b (leaving centre) ' + Gb.toFixed(6));
}
console.log('faces checked ' + n + ', faces whose code sign differs from the Fresnel expectation: ' + bad);
