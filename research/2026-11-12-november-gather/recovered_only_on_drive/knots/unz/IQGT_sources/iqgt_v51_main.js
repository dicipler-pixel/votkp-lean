/* IQGT Mixer 3D v5.1: the acts follow the paper, then run */
(() => {
const E = [].concat(window.__IQGT_EYES_A || [], window.__IQGT_EYES_B || [], window.__IQGT_EYES_C1 || [], window.__IQGT_EYES_C2 || []);
const have = new Set(E.map(e => e.id));
const acts = [
  {name:'I. The tensor, its pullbacks and its bounds', eyes:['charts','crew','twist','weights','count']},
  {name:'II. Degenerate strata, geodesics and dissipation', eyes:['folds','nothing','ridge','canyon','speed','toll']},
  {name:'III. Data, mixed states and the subspace as observable', eyes:['roommates','split','fog','cards','house','ring']},
  {name:'IV. Comparison with spacetime geometry', eyes:['cone']}
].map(a => ({name:a.name, eyes:a.eyes.filter(id => have.has(id))})).filter(a => a.eyes.length);
API.run({ title:'IQGT', short:'IQGT_Mixer_3D_v5_1', home:'https://atlas-memoriae.dicipler.workers.dev/',
  subtitle:'Intrinsic Quantum Geometric Tensor on the Grassmannian and Spectral Lower Bounds on Dissipation. Eighteen interactive views of an isolated spectral subspace, the tensor defined on it, and what parametrisations, degenerate strata, dissipation and measured data reveal about it.',
  byline:'Jeromie Beasley · built from the paper, version 7.3.1',
  foot:'Every number the paper prints is shown beside the number this page computes, and each is labelled. The self-test checks this page against the paper; it does not grade the paper. AI tools were used for computation and for building this page; the author directed the work.',
  acts, eyes:E });
})();
