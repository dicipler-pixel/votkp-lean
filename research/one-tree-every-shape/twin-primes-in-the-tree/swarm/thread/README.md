# The twin chain as a cut thread

Jeromie Beasley · 24 November 2026

## The thread
- **Turn:** 30 integers. Twin starts can sit only at 11, 17 and 29 (mod 30), so this is a three-start thread.
- **Starts:** spaced 6, 12 and 12 apart.
- **Path:** in log length, the pitch gets finer as size grows (one turn = 30/a).

## Test
TWIN-THREAD-FORM-01 and TWIN-THREAD-NOISE-01. Kill conditions were written before the runs.

Method:
- Cut the thread with the small primes up to P (Granville-type sieve model).
- For each cut, measure dev_j × G, where dev_j is the gap-weighted end-digit share minus the count share, and G is the mean gap.
- Compare against the real twin starts in (1e8, 1e9]: dev×G for digits 1/7/9 = −0.924, +0.839, +0.085 (se 0.041, 0.034, 0.054).

| thread cut | model dev×G (1/7/9) | match within 2 se |
|---|---|---|
| mod 30 (2·3·5) | +0.662, −0.645, −0.017 | no: wrong sign |
| mod 210 (adds 7) | −0.942, +0.974, −0.032 | digit 1 yes, digit 7 off by 2.4 se |
| mod 30030 (to 13) | −1.177, +1.142, +0.034 | no: overshoots |
| to 17, to 19 (one seed each) | −0.88, +0.86, +0.02 and −1.04, +0.88, +0.15 | within noise of the real values |

## Findings
- **Sign:** cutting the thread by 7 flips the tilt to the real sign. The mod-30 screw alone gives the wrong sign.
- **Size:** about 0.9–1.2 for every cut from 7 on, so the order of magnitude is right.
- **Kill as written fires:** no single cut matches all three digits within 2 se. The size is not yet nailed; the model holds density fixed at 10^8.5, while the real data run over a decade.
- **Not the first flank:** the exact nearest clearance before each start does not show the flip (digit 1 stays +). The tilt comes from longer-range structure across the roughly 20 slots one gap spans.

## The thread cut by every prime: the tilt derived (24 Nov, later)

### Exact screw, sieve primes ≤ P (TWIN-THREAD-EXACT-01)
- No random runs; 1e8–1e9 values below. Digit 1 is followed through each cut:

  | P | digit 1 |
  |---|---|
  | 5 | +0.675 |
  | 7 | −0.905 |
  | 11 | −1.074 |
  | 13 | −1.158 |
  | 17 | −0.965 |
  | 19 | −0.971 (matched every decade) |
  | 23 | −0.741 (TWIN-THREAD-EXACT-23: kill fired) |

- So stopping at any finite prime gives an answer that swings. The thread has to be cut by all primes at once.

### Full product (TWIN-THREAD-ALLPRIMES-01)
- Method: Hardy–Littlewood local factors f_p(h) = p(p − ν_p(h))/(p − 2)², where ν_p(h) = #{0, −2, h, h−2} mod p, together with the mod-30 class rule and a mean-field first-arrival gap.
- Validation against the exact 19-prime screw: max miss 0.039, which passes.
- The result has converged by p ≤ 1000. At 1e8–1e9 it gives dev×G = (−0.939, +0.820, +0.119), against the real (−0.924 ± 0.041, +0.839 ± 0.034, +0.085 ± 0.054).

### Every decade (TWIN-THREAD-ALLPRIMES-02)
- Digits 1 and 7 are within 1.1 se of the real values in each decade from 1e5 to 1e9: passes.
- The predicted mean gaps beyond the cache are 378, 459 and 548. The 1e12 walk gives 375, 457 and 547.

### Past 1e9 (TWIN-THREAD-CHECK-1E12)
- Checked against the 1e12 walk, after calibrating the step-weighting on 1e8–1e9.
- Digit 1 agrees within 0.03 in each decade, and all digits within 0.10: passes.
- The 7/9 split is consistently off, by about +0.07 on digit 7 and −0.06 on digit 9.

### Consequence
- dev×G stays near a constant, about (−0.95, +0.81, +0.14). So the tilt itself dies like 1/(mean gap), derived from Hardy–Littlewood.
- That is the condition the 12.4651° limit needed. It now rests on Hardy–Littlewood, not only on the measured trend.

## Two views, one light sphere: connection energy (TWIN-HCE-1E12)

- **Setup.** L (forward, lab heading n) and Lᵀ (reversed, body heading u) are two views of the same product. Both headings run out to points on the light sphere.
- **The mismatch.** ‖[L, L*]‖_F/‖L‖_F² = √2 tanh d sin(φ/2) sin β measures the mismatch between the two views.
  - φ is the frame turn; β is the angle between the turn axis and the heading.
  - It is zero exactly when the operator is normal.
- **Identity check.** At 1e8 the explicit matrix gives 0.1263187207 and the formula gives 0.1263187207.

| up to | 𝒩 |
|---|---|
| 1e5 | 0.08863 |
| 1e6 | 0.11711 |
| 1e7 | 0.12429 |
| 1e8 | 0.12632 |
| 1e9 | 0.12731 |
| 1e10 | 0.12777 |
| 1e11 | 0.12815 |
| 1e12 | 0.12853 |

- **Kill conditions.**
  - Written before any run: fails if |𝒩(1e9) − 𝒩(1e8)| > |𝒩(1e8) − 𝒩(1e7)|. It passes.
  - Extended: the change at 1e12 must be smaller than at 1e10. It passes.
  - Caveat: the change per decade has flattened at about 3.8e-4. It follows the turn's slow climb as the tilt dies.
- **β.** 57.39° at 1e9, rising to 57.71° at 1e12. It is not arccos(1/√3) = 54.74°: killed.
- **Limit (estimate, untested).** With the turn limit 12.4651° and tanh d → 1, 𝒩 → 0.15353 sin β∞, which is about 0.130 if β levels near 58°.

## The wall as the thread's bite (TWIN-WALL-BITE-01)

**Method.** Scramble the end-digit arms inside one window of 13 steps, keeping the counts fixed, 200 times. Measure the spread of the final turn and of c at 1e8.

| window | twin starts | turn sd | turn range | c sd |
|---|---|---|---|---|
| A, before the wall | 11 to 227 | 8.378° | 2.5° to 41.5° | 0.0787 |
| B, just after the wall | 227 to 641 | 1.075° | | 0.0119 |
| C, near 1e5 | 99989 to 101531 | 0.0030° | | 0.00009 |

**Kill condition:** C runout ≥ half of A. Measured ratio 0.0004: **pass**.

**Caveat:** early steps are also larger, so this test cannot separate "the wall" from "big steps". A curvature-dial run, which moves the wall crossing to other twin starts, would separate them. That run is untested.

## The wall is not the bite: the first cut is (TWIN-CURVATURE-DIAL-01, -01b, -02; 24 Nov, night)

Kill conditions in `CURVATURE_DIAL_PREREG.md`, written before each run.

- **Dial.** Every rapidity is multiplied by λ: the same chain in a ball whose curvature is λ² times stronger. The big steps stay at the start, while the wall crossing moves.
- **Result.** At λ = 0.25, 0.35 and 0.5 the wall sits at twin starts 2,069,381, 61,979 and 4,421. There the before/after runout ratios are 1.29, 0.81 and 0.78. **The kill fires.**
- **First steps.** The first window, twin starts 11–227, carries 2.3° to 9° of runout at every λ.
- **Opposite setup.** λ = 1, with the walk started at 10,007 or at 100,151: ratios 0.52 and 1.30. **The kill fires again.** The first 13 steps of the walk carry about 100 times the runout near the wall.
- **Verdict.** The turn is set by the walk's own first steps, its first cut. The wall crossing is a distance the walker passes. (At λ = 2 the turn is read through the SVD polar split; the readings agree at λ = 1.)

## Honeycomb {5,3,4} (TWIN-HONEYCOMB-534-01, -02)

Kill conditions in `HONEYCOMB_PREREG.md`.

- **Geometry.**
  - The edges at a vertex run along ±x, ±y, ±z, which are the twin arms.
  - Each face is a right-angled regular pentagon, with cosh ℓ = φ and Γ² = √5 − 2.
  - Two perpendicular edges turn the frame by arctan(1/2) = 26.5651°, which is exact.
  - The pentagon loop closes to a 90° rotation: **pass**.
- **Walk.** One edge per twin step, so only the order of the end digits is walked.
  - Repeat rate: 0.30921, against 0.33333 for independent digits.
  - Drift per step: 0.756495 real, against 0.764406 ± 0.000154 for the shuffles, so z = −51.
- **Markov surrogate** (first-order, with the real transition matrix): 0.757747 ± 0.000145, so z = −8.7. The pair bias explains 84% of the signal.
- **Block-Markov check:** see `honeycomb_534_markov_blocks_out.txt`.

## Version 1 predictions 6 and 7 (split_and_cousin.py; kill conditions in SPLIT_COUSIN_PREREG.md)

- **7/9 split.** A direct gap-weighted count on 23,988,173 twin starts in (1e9, 1e10] gives (−0.950, +0.775, +0.175), with se (0.032, 0.033, 0.036). Against the prediction that is z = (−0.2, −1.0, +1.1): **pass**. The offset is the walk's step weighting.
- **Cousin tilt.** The real values are (+0.680, +0.241, −0.921), with se (0.072, 0.081, 0.092). The prediction is (+0.705, +0.143, −0.847): **pass**, with |z| ≤ 1.2. The block se used here is wider than the se in version 1.

## Other prime pairs: see ../families/ (an agent's run, reproduced in paper v2, Section 10)
