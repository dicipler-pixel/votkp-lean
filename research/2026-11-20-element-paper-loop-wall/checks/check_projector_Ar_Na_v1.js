// SCRIPT: CHECK-GPT-ARGON-PROJECTOR-01
// Rerun Jeromie's hydrogen-in-the-space-between model with argon and sodium peel ratios as the face
// clocks (same scalar on all three axes), opposed fields, separation 4, no kick. Report the row minimum.
require('./hsb/hsb_model_v1.js'); const HSB = globalThis.HSB;
const runs = [['Ar rung1', 27.62967/15.7596119], ['Ar K opening', 4120.66559/918.375], ['Na L opening', 47.28636/5.13907696], ['Na rung0', 5.13907696/0.547926], ['control [3,5,7]', null]];
for (const [name, z] of runs) {
  const o = { sep:4, spins:'opposed', kick:0 }; if (z) o.faceZ = [z, z, z];
  const M = HSB.build(o); const r = HSB.read(M);
  console.log(name, 'N', M.N, 'rowMin', r.rowMin, 'connected (>1/12)?', r.rowMin > 1/12);
}
