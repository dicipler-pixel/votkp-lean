/* SCRIPT: HW-FEED-V1 — the ball's streams are the link's. Jeromie Beasley. 17 Nov 2026. AI-assisted.
   The Light at the Hypersurface ball computes a private stack from a unit source (LH-MATH-V1 axisStack) and draws its streams, pushes and record rings from it.
   This hook, loaded after the ball's scripts and touching none of them, replaces that private stack's amplitudes on the I arm with the link light the Flock engine
   carries (HW-WORLD-V6 feedBalls) whenever a ball was created with options.hw, and replaces its record K on that arm with the record of the link's pushes.
   Every other arm, every other drawn object, and every formula of the ball stay the ball's own. */
(function(){
"use strict";
const L = window.LH, C = L.C, feed0 = L.feed, advance0 = L.advance;
L.feed = function(P, tau){ const S = feed0(P, tau); const F = P.hw; if(F && F.ap){ const st = S.stacks[0], D = st.amps.length - 1;
    for(let k=0;k<=D;k++){ st.amps[k] = { ap:(F.ap[k] || [0,0]).slice(), am:(F.am[k] || [0,0]).slice() }; }
    /* the ball's own reading of push and arrival, now from the link's amplitudes: 2R_k (Y_k |a+_k|^2 - Y_{k+1} |a-_{k+1} e^{-i phi}|^2) / Y_0 */
    const Ys = st.Ys, phis = st.phis, Rk = st.G.map(g => C.abs2(g));
    st.push = st.G.map((g, k) => 2*Rk[k]*((Ys[k][0])*C.abs2(st.amps[k].ap) - (Ys[k+1][0])*C.abs2(C.mul(st.amps[k+1].am, k+1 < D ? C.exp([0, -phis[k+1]]) : [1,0])))/Ys[0][0]);
    st.arrive = st.G.map((g, k) => Ys[k][0]*C.abs2(st.amps[k].ap)/Ys[0][0]); st.fed = true; }
  return S; };
L.advance = function(st, P, tau0, dtau){ advance0(st, P, tau0, dtau); const F = P.hw; if(F && F.K){ for(let k=0;k<st.K[0].length;k++) st.K[0][k] = F.K[k] || 0; } return st; };
window.HWFEED = { version:1 };
})();
