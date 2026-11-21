// SCRIPT: CHECK-GPT-MATCHED-JUNCTION-01
// Exterior (port-to-lattice) links get clock 1 (Gamma = 0); the element's peel ratio stays on the
// centre-to-port link inside each ball. Compare with the original assignment.
require('./hsb/hsb_model_v1.js'); const A = globalThis.HSB;
delete globalThis.HSB; require('./hsb/hsb_model_matched.js'); const B = globalThis.HSB;
const runs=[['Na L opening',47.28636/5.13907696],['Ar rung1',27.62967/15.7596119],['Ar L opening',422.6/143.4567],['Na K opening',1465.0992/299.856],['Ar K opening',4120.66559/918.375],['all 1',1]];
for(const [n,z] of runs){ const o={sep:4,spins:'opposed',kick:0,faceZ:[z,z,z]};
  const a=A.read(A.build(o)).rowMin, b=B.read(B.build(Object.assign({},o,{extZ:[1,1,1]}))).rowMin;
  console.log(n.padEnd(14),'original',a.toFixed(9),'matched',b.toFixed(9)); }
