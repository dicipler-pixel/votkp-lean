const M = require('./mm_math_v1.js'); const R=require('./rest_states_v1.json');
for(const L of [1,2]){
  const W = M.makeWorld(L); W.d = R['L'+L]; let S = M.initState(W,{source:0});
  // no light: nothing moves
  const Z={...S, psr:new Float64Array(2*W.N), psi:new Float64Array(2*W.N)}; const D0=M.deriv(W,Z); console.log('L',L,'sea cut',S.kSea,'gap',S.gap0.toFixed(4),'no-light max ball speed',Math.max(...D0.dd.map(v=>Math.hypot(...v))).toExponential(2));
  const E0 = M.energies(W,S); let maxDE=0, maxPow=0, maxSL=0, maxTdErr=0, h=0.01, T=L===1?30:12, steps=Math.round(T/h);
  const nu0 = M.ballCensus(W,S).map(c=>c.nu[0]); const tL=Array(W.N).fill(null), tS=Array(W.N).fill(null); let t0=Date.now();
  for(let k=0;k<steps;k++){ const S1 = M.rk4(W,S,h);
    for(let i=0;i<W.N;i++){ if(tL[i]===null && M.lightDensity(S1,i)>1e-3) tL[i]=S1.t; }
    const cen=M.ballCensus(W,S1); for(let i=0;i<W.N;i++){ if(tS[i]===null && Math.abs(cen[i].nu[0]-nu0[i])>1e-3) tS[i]=S1.t; }
    if(k%25===0){ const E=M.energies(W,S1); maxDE=Math.max(maxDE,Math.abs(E.E-E0.E));
      const pw=M.ballPowers(W,S1); for(const p of pw) maxPow=Math.max(maxPow,Math.abs(p.fromLight+p.fromSea-p.toFaces));
      const D=M.deriv(W,S1), g=M.seaSpeed(W,S1); const S2=M.rk4(W,S1,1e-5), c2=M.ballCensus(W,S2);
      for(let i=0;i<W.N;i++){ const td=M.tauDot(W,S1,D,i), fd=(c2[i].tau-cen[i].tau)/1e-5; maxTdErr=Math.max(maxTdErr,Math.abs(td-fd)/Math.max(1,Math.abs(td))); maxSL=Math.max(maxSL, td*td/(4*g*cen[i].S)); } }
    S=S1; }
  const E=M.energies(W,S);
  console.log(' T',T,'ms',Date.now()-t0,'conserved E drift',maxDE.toExponential(2),'ball in-out',maxPow.toExponential(2),'tau_dot analytic vs FD',maxTdErr.toExponential(2),'max tau_dot^2/(4gS)',maxSL.toFixed(6));
  console.log(' EL EF ES-Erest', E.EL.toFixed(5),E.EF.toFixed(5),(E.ES-E.Erest).toFixed(5),' from',E0.EL.toFixed(5),E0.EF.toFixed(5),(E0.ES-E0.Erest).toFixed(5));
  const pairs=[...Array(W.N).keys()].filter(i=>i>0&&tL[i]!==null).map(i=>[i,tL[i],tS[i]]); console.log(' light/sea first response:', pairs.slice(0,12).map(p=>p[0]+':'+p[1].toFixed(2)+'/'+(p[2]===null?'-':p[2].toFixed(2))).join(' '));
}
