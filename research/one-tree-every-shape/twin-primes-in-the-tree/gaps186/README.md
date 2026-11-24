# Checking OpenAI's 186 bound (24 Nov 2026)

Jeromie Beasley · notes

**Source.** github.com/openai/PrimeGaps186 (read only; none of its code was run here).

**The claim.** DHL[40,2] gives liminf (p_{n+1} − p_n) ≤ 186. It uses Maynard–Tao sieve weights with three new pieces:
- triple dense divisibility;
- Stadlmann's prime minorant;
- Dickman-type fragment measures.

The level of distribution is 0.5253 at order three and 0.504 to 0.5062 at order two. The numerical certificate is a 77-coefficient trial in 40 variables, and its normalized margin is just over 1/50000.

**The three Lean axioms.**
- **Axiom 1.** |Kl3(c;p)| ≤ 3. This is Deligne's bound (Katz, GKM Thm 4.1.1).
- **Axiom 2.** |Σ_{t≠0,−1} K2(A/t) K2(B/(t+1))| ≤ 8 p√p for every prime p and every pair of nonzero A, B, including A = B (Fouvry–Kowalski–Michel, Prop. 2).
- **Axiom 3.** 104 outer and 45 inner physical-integral bounds, plus 3 cap bounds. These come from their Python certificate and have not been proved in Lean.

## Our checks
- **The 40-tuple** {0, 2, 6, …, 186}: admissible, size 40, width 186. **Pass.**
- **Axiom 1**, exhaustive over all p ≤ 160 and all c (GAPS186-AXIOM-CHECK-01): max |Kl3| = 2.665 at p = 107, against the bound 3. **Pass.**
- **Axiom 2**, exhaustive over all p ≤ 160 and all A, B: max ratio 4.06 at p = 137, against the bound 8. **Pass.**
- **Axiom 2, split by case** (GAPS186-AXIOM2-DIAGONAL-01, p ≤ 400): the largest ratio is 3.30 when A = B and 4.50 when A ≠ B. The case A = B shows no main term and behaves like A ≠ B.
  - The kill condition as written was "the fitted exponent is above 0". Fitted exponents came out 0.14 and 0.12, so it fired.
  - That condition was badly chosen. The maximum taken over p² pairs grows slowly as an extreme value, so a small positive exponent is expected even when the bound holds. The test is inconclusive, not a refutation.
  - Whether the cited Proposition 2 allows A = B is not yet confirmed. The note itself could not be fetched.
- **Next tuples down.** Dropping the end at 186 gives a 39-tuple of width 182. The known narrowest widths (standard table, OEIS A008407, not re-fetched) are H(39) = 182, H(38) = 176 and H(37) = 168.

## What it would take to go lower
DHL[39,2] would give 182. Their margin at k = 40 is about 2×10⁻⁵, while the criterion changes by roughly 1% from k = 40 to k = 39 (a rough estimate from how M_k grows). So k = 39 needs at least one of these:
- a better trial than 77 coefficients;
- better distribution exponents;
- a new sieve idea.

Axiom 3 can be pinned down independently only by reimplementing their certificate in interval arithmetic. That is also the tool needed to search a k = 39 trial.

## Rebuild of the cap forms, and k = 39 (24 Nov, afternoon)

The scripts are our own code. No OpenAI code was run.

**GAPS-CAP-GRAM-02** (`capgram.py`, `exactconv.py`)
- The engine is rebuilt from the paper's formulas: geometry, ladders, Dickman fragment measure, shells, caps and hybrid constants.
- The cap forms are assembled as 77×77 Gram matrices.
- Convolution is exact, through FLINT integer polynomials on non-negative parts only. The bundled FLINT fails OpenAI's signed-FFT regression check.
- Float64 FFT was 8% off (GAPS-FFT-CHECK-01) and is not used.

**k = 40, full grid (N = 98304), with their 77 coefficients**

| quantity | ours | their certificate |
|---|---|---|
| I_H | 2.3685317853e-14 | in [2.3685317816, 2.3685317890]e-14 |
| J | 9.0248755655e-14 | ≥ 9.0248755123e-14 |
| cap quotient | 1.00020609 | > 1.000206 |

This independently confirms the cap part of axiom 3. The 97 loss components were not rebuilt.

**Best trial in the same 77-function space** (`optq.py`, generalized eigenvalue)
- k = 40: 1.00021374. Their trial reaches 1.00020609, so this space is close to saturated.
- k = 39: **0.99439115**. This is below 1 before any loss is charged. At k = 40 the losses cost about 0.00018.

**Verdict:** DHL[39,2], and so the gap 182, cannot come from this trial space with these distribution inputs and this geometry. The deficit is about 0.0056, roughly 250 times their final k = 40 margin.

**What remains open:**
- a larger trial space (more signatures and degrees, another profile g);
- retuning S, T, ρ and the hybrid constants for k = 39;
- new distribution inputs.

## Recentering the setup for k = 39 (GAPS-RECENTER-SCAN-01)

**Calibration.** The coarse grid (N = 12288) gives best quotients 0.998745 at k = 40 and 0.992932 at k = 39. Both sit 0.00147 below the full grid, so the k = 40 to k = 39 drop matches: 0.00581 coarse, 0.00582 full.

**Scan.** 10 profiles g × 12 values of the hybrid λ, with the best 77-trial taken at each setting.
- λ = 1/125, their value, is best in every case.
- Their profile (w = 0.105, slow = 0.01, fast = 181.4) is best among those tried:

| change to the profile | coarse best quotient |
|---|---|
| none (their profile) | 0.992932 |
| fast = 90 | 0.990748 |
| fast = 360 | 0.989670 |
| w = 0.05 | 0.992843 |
| w = 0.2 | 0.992706 |
| slow = 0.5 | 0.992928 |
| slow = 2 | 0.992915 |
| w = 0 | 0.992775 |
| w = 1 | 0.949931 |
| w = 0.3, slow = 0.5, fast = 60 | 0.983087 |

**KILL fired.** No setting reaches 0.99871. Their setup is already centred, and recentring the free settings does not rescue k = 39.

**Rough size of the missing arithmetic.** The quotient carries a factor ρ*. Recovering 0.58% by ρ alone would need ρ to rise by about 0.0015, which is about +0.003 in the order-three level (0.525 to about 0.528). This ignores how S, T and the shells move with ρ, so it is untested.
