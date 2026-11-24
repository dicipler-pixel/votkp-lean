# Does the twin chain's frame turn converge? (Jeromie Beasley, 24 Nov 2026, AI-assisted)

Scripts: `conv_probe.py` (TWIN-TURN-CONV-PROBE-01), `conv_checks.py` (TWIN-TURN-CONV-CHECKS-01). Grades: **proved** (exact algebra, checked), **standard** (a known theorem, cited), **conditional** (holds under the stated hypothesis), **measured**.

## Setup
Twin starts a₀ = 11 < a₁ < … ; step n is a boost of rapidity rₙ = ln(aₙ₊₁/aₙ) along the body axis e_s of the next pair's end digit (1, 7, 9 → i, j, k).
Lₙ = B(e_{s₁}, r₁)…B(e_{sₙ}, rₙ). Split Lₙ = Boost(dₙ nₙ)·R̂ₙ: distance dₙ, heading nₙ, frame R̂ₙ. Path Lₙ' = Σ rₖ = ln(aₙ/11). Body heading uₙ = R̂ₙᵀ nₙ.

## Step 1 — one step (proved; check C1)
With w = R̂ e_s and θ the angle between n and w:
- frame: R̂' = W R̂, W the rotation by ω = r·tanh(d/2)·(w × n) + O(r²)  [Wigner rotation; |ω|/(r sin θ) = tanh(d/2) to 6 digits at d = 2, 4; vector law to 5×10⁻³ over 200 random frames]
- distance: d' = d + r cos θ + O(r²)
- heading: n moves by r sin θ / sinh d + O(r²)
In body coordinates: u' = u + r·tanh(d/2)·(e_s − (e_s·u)u) + O(r e^{−d}) + O(r²). The heading is pulled toward the active arm.

## Step 2 — the steps are Robbins–Monro steps (measured, and conditional)
Σ rₙ = ln(aₙ/11) → ∞ (exact). Σ rₙ² = 1.1917, 1.2543, 1.2664, 1.2683, 1.2685 at 10³…10⁷ (measured; finite under Hardy–Littlewood, unconditionally unknown).
These are exactly the step-size conditions of stochastic approximation (Robbins–Monro 1951; Kushner–Clark 1978).

## Step 3 — the averaged flow (proved for the flow; standard for the passage)
Averaged over arms with weights p = (p_i, p_j, p_k), the body heading follows du/dL = Π_u(P), P = Σ p_s e_s: the projected gradient flow on the sphere, with one attracting point u* = P/|P|, angle decaying as dα/dL = −|P| sin α. Kushner–Clark (deterministic noise form): if the step sizes satisfy Step 2 and the weighted noise Σ rₙ(e_{sₙ} − P) converges, uₙ → u*.
Measured: angle(heading, frame · cube diagonal) = 21.3°, 8.5°, 3.8°, 1.6°, 0.76° at 10³…10⁷, settling at the small tilt of the actual weighted mean.

## Step 4 — the endpoint law (derived, confirmed)
At u*, each step gains r·(u*·e_s) on average, so d = |P|·L' + c. With balanced arms |P| = 1/√3 (the cube's body diagonal against an edge).
**d − L'/√3 = 0.1089, 0.1090, 0.1091, 0.1082, 0.1090 at 10⁵, 10⁶, 10⁷, 10⁸, 10⁹** (from harness T2 ratios, 4-digit rounding ±0.0008). The endpoint ratio d/L' → 1/√3 = 0.57735, from above as 0.109/L'.

## Step 5 — the frame converges (conditional)
R̂ₙ converges iff Σ ωₙ converges (Σ|ωₙ|² ≤ Σ rₙ² < ∞). Write e_s × u = (e_s − P) × u + P × u.
- P × u: size |P| sin αₙ, which decays exponentially in L' plus the noise tail; summable against rₙ.
- (e_s − P) × u: Abel summation against the convergent noise series; the frame's variation is Σ rₙ, so this needs the noise tail after L' to be O(L'^{−1−δ}).
**Theorem (conditional).** If (H2) Σ rₙ² < ∞ and (H3) for some fixed weights p the tail sup_{L''>L'} |Σ_{L'<Lₙ≤L''} rₙ(e_{sₙ} − P)| = O(L'^{−1−δ}), then the heading, the body heading and the frame all converge, and d/L' → |P|.
Under the Hardy–Littlewood conjecture with a power-saving error term (twin starts in each class mod 10 at density 1/3 each), H2 and H3 hold with p = (⅓, ⅓, ⅓): the turn converges and d/L' → 1/√3.
**Unconditional corollary.** If there are only finitely many twin primes, everything converges trivially. So a proof that the turn does **not** converge would prove infinitely many twin primes.

## What the data says about H3 (measured, undecided)
Gap-weighted arm sums S_s = Σ rₙ(1[sₙ = s] − ⅓) to 10⁸: S_i = −0.230, −0.240, −0.248, −0.257 and S_j = −0.305, −0.276, −0.270, −0.263 at 10⁵…10⁸: a steady drift of about 0.004 per unit of path (a weight tilt, absorbed into P), with small wobble. Whether the remainder meets the O(L'^{−1−δ}) tail cannot be settled at 10⁸; under Hardy–Littlewood the tilt decays like 1/L'².

Prior art: Wigner–Thomas rotation (Ungar's gyrovector form); Robbins and Monro (1951); Kushner and Clark (1978); Brun (1919) for the twin-prime constant analogy; Hardy and Littlewood (1923).
