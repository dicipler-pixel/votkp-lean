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
