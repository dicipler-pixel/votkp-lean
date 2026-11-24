# Swarm 1 — the proof pushed (twin-chain frame turn)

Jeromie Beasley · swarm notes · 24 November 2026
Scripts:
- p1_exact_wigner.py (exact step, checked at 160 digits)
- p2_chain_tests.py (chain to 10⁹; kill conditions are in the header)
- p3_tracking.py

Grades: proved, measured, cited, open.

## Proved
1. **Frame-free form.** Every boost is symmetric, so Y_n = L_nᵀe₀ = (cosh d_n, sinh d_n·u_n) obeys Y_n = B(e_s, r_n)·Y_{n−1}. Distance and heading evolve without the frame.
2. **Exact Wigner step** (polar factor U = (M + M^{†−1})/tr H):
   - tan(ε/2) = sin θ / (coth(d/2)·coth(r/2) + cos θ), about the axis w × n.
   - cosh d' = cosh d·cosh r + sinh d·sinh r·cos θ.
   - Second-order term: −(r²/2)·tanh²(d/2)·sin θ·cos θ.
   - Checked to 10⁻¹¹¹ at 160 digits; an independent numpy check gives 7×10⁻¹⁴.
3. **Velocity form.** v = tanh(d)·u stays in the closed unit ball and never leaves the positive octant (velocity addition keeps every component ≥ 0).
4. **Theorem A.** Assume r_n → 0 and that the gap-weighted digit shares, over windows of fixed path length, settle to weights p_∞. Then the heading converges, d → ∞, and d/L → |P_∞|.
   - Proof: Benaïm/Kushner–Clark limit sets on the compact ball, with Lyapunov function V = P·v. Octant invariance excludes the point −P̂.
   - The finiteness of Σr² is not needed here.
5. **Lemma C (corrector).** Replaces the old Step 5, whose "converges iff Σω converges" is false for rotations that do not commute.
6. **Theorem B.** The frame converges under three conditions:
   - Σr² < ∞;
   - the weights have finite total change, ∫|p′| dL < ∞;
   - Σ r_n|N_n| < ∞, where N_n is the tail of r_k(e_{s_k} − p(L_k)).

   No O(L^{−1−δ}) rate is needed.
7. **Corollaries.**
   - d → ∞ alone implies infinitely many twins.
   - For an infinite chain: if the frame converges, liminf d > 0, and the heading's limit lies off the three axes, then r_n → 0. That is a twin in every interval (x, (1+ε)x], which is open.
   - So an unconditional convergence proof would prove an open twin statement.

## Conditional
- Σr² < ∞ follows from Hardy–Littlewood with error O(x/ln^{3+η} x).
- r_n → 0 follows from the plain Hardy–Littlewood count.

## Died
- Σr² < ∞ unconditionally, even granting infinitely many twins.
- "Hardy–Littlewood counts ⇒ H3." Adversarial chain: the real gaps, with equal counts per digit (1,141,501 each) but the largest gap in each triple given to digit 1. Gap-weighted shares become 0.567 / 0.291 / 0.143 and d/L = 0.656, against 0.583 for the true chain. The endpoint law needs gap-weighted digit equidistribution, which counting alone does not give.
- Exact lock on the cube diagonal. At 10⁹ the heading is 0.469° off the diagonal and tracks the local weighted mean (0.418° off, cos 0.999).
- The simple mod-30 lattice model of the tilt. Pooled for L ≥ 10, the measured weighted-minus-count shares are (−0.0058, +0.0029, +0.0029) for digits 1/7/9; the model gives (+0.0035, −0.0035, 0). The sign is wrong.

## Measured to 10⁹
- d − L/√3: 0.1085 at 10⁸, 0.1086 at 10⁹.
- Σr²: 1.2685621. Tail beyond 10⁸: 4.8×10⁻⁶.
- Frame movement per decade from 10⁴ to 10⁹: 5.46°, 2.45°, 0.85°, 0.20°, 0.098°.
- Digit-share deviation from 1/3: mean |w − 1/3| is 0.036 for L in [6,10) and 0.0024 for L in [14,18).
- L·|N| tail: 0.564, 0.366, 0.295, 0.167 at 10⁵ through 10⁸.

## Set aside for the equation file
- The second-order frame coefficient.
- Second-order cancellation in the balanced case.
- The digit-1 tilt of about −0.08ρ.

## Sources
- Lu, "Counts Converge, Spacings Do Not", ICML 2026 poster: icml.cc/virtual/2026/82562.
- Benaïm 1996 (fetched).
- Matomäki–Radziwiłł–Tao, arXiv:1707.01315.
- Kushner–Clark 1978, Benaïm 1999, Brun, Zhang, Maynard and Mikawa are standard references, not re-read.
