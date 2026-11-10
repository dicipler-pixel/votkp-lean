# Signs group: four open questions, tests run 10 November 2026 (v1)

Jeromie Beasley's corpus. Second worker's report. All scripts and outputs are in /home/claude/work/agent_signs/. Nothing outside that folder was written. No web, no agents, no git.

Grades: PROVED = exact or symbolic. CHECKED = numerics, digits and sample size given. READING = interpretation.

Three things the main session should know first:

1. **A flaw in today's earlier never-turn scripts.** `never_turn_02.riley_coeffs` drops leading coefficients smaller than 1e-25 of the largest. At large s or large p the true leading coefficients are that small, so real branches are lost. Two earlier results were wrong because of it: 89/34 was reported NEVER at 120 digits and it TURNS; the three "band points" of 233/89 at 200 digits are not roots.
2. **A second trap in the root finder.** `mpmath.polyroots` loses the cluster of roots with v ~ s² even at 200 digits with exact coefficients. It then reports real branches as complex, and once (47/9, 80 digits) reported a spurious real root. The fix is to read each half of the band in the variable where its roots are small: v, or w = tr(ab) − 2.
3. **Standing results.** Q2 is answered for the two-term families. Q3 has a rule with no miss on 285 knots, part of it fitted. Q1 has no simple separator; an arithmetic rule works on 137 of 199. Q4 is run on both sides.

---

## Q1. Signs at split roots

**Scripts:** `split_signs_01.py` / `.out`, `split_signs_02.py` / `.out`.

**List rebuilt.** 199 nullity-2 double roots: 81 equal sign (jump ∓4: 73 and 8), 118 opposite (silent). One per knot, 199 knots. 193 of the 199 are the factor t² − t + 1 (the sixth root of unity). Outside the list: 22 nullity-2 roots of multiplicity 3 to 5.

**Kill conditions (written first).**
- A: any disagreement between the label recomputed from the Seifert matrix and KnotInfo's label.
- B: a candidate is a separator only if no value of it holds both labels.
- C: the arithmetic prediction is killed by one knot of its clean stratum on the wrong side.

**Part A. CHECKED, 199 of 199.** The label was recomputed from H(ω) = (1 − ω)V + (1 − ω̄)V^T just before and after the root (double precision, all 199 Seifert matrices). For the 193 roots at ζ6 the discriminant d of the two levels was also computed exactly over Q(√−3): equal sign exactly when d > 0, 193 of 193. This is the definition re-checked on a third column, not a finding.

**Part B. Contingency tables (equal / opposite).**

| Candidate | Table | Verdict |
|---|---|---|
| Root of the second Alexander polynomial, multiplicity | multiplicity 1: 81 / 118 | constant, cannot separate |
| Root of unity, order | order 6: 78 / 115; not a root of unity: 3 / 3 | no |
| Signature before the root, mod 4 | 0: 50 / 84; 2: 31 / 34 | no |
| Signature before the root | −2: 31 / 23; 0: 50 / 84; +2: 0 / 11 | no |
| Signature AT the root minus before | ∓2: 81 / 0; 0: 0 / 118 | separates, but it is the definition |
| Knot signature | 0: 0 / 62; ±2: 6 / 35; ±4: 36 / 18; ±6: 21 / 3; −8, −10: 18 / 0 | no (25 on the minority side) |
| Δ = f² exactly (trivial cofactor) | yes: 1 / 11; no: 80 / 107 | no |
| Unit-circle roots of the cofactor | 0: 34 / 62; 2: 27 / 35; 4: 18 / 18; 6: 2 / 3 | no |
| Alternating | Y: 43 / 63; N: 38 / 55 | no |
| Symmetry type | amphichiral (all three kinds): 0 / 11; reversible: 58 / 69; chiral: 23 / 38 | one-way only |
| Algebraic concordance order | finite: 0 / 21; infinite: 21 / 16; not listed: 60 / 81 | one-way only |
| Smooth four-genus | 0: 0 / 31; 1: 0 / 66; 2: 40 / 18; 3: 18 / 3; 4, 5: 23 / 0 | one-way only (21 minority) |
| Fibered | Y: 30 / 74; N: 51 / 44 | no |
| Connected sum K#K against K#mirror | no instance: KnotInfo lists prime knots only | cannot be tested here |

A sweep over every KnotInfo field with at most 40 values found no perfect separator. The best is double slice genus, 20 on the minority side.

**What the one-way rows are.** Amphichiral, finite concordance order and four-genus ≤ 1 each force "opposite" through the standard signature bounds. They are reproductions, not findings. Knot signature 0 gives opposite 62 of 62; that one is not forced by a bound I ran (CHECKED on this list only).

**Why the simple candidates cannot work. READING, standard theory.**
- At a double root the signature before the root mod 4 is fixed by the sign of the Alexander polynomial there, the same for both labels.
- K#K and K#mirror(K) have the same Alexander module and opposite labels, so nothing read from the module alone (Δ, second Alexander polynomial, order of the root, repeated factor) can separate in general.
- The separator has to see the form, not the module.

**Part C. An arithmetic separator for the factor t² − t + 1.**

Prediction as first written: the sign of d follows from Hilbert reciprocity for (d, −3). Inputs: the linking form of the double branched cover on its 3-part (from V + V^T) and the primes p ≡ 2 mod 3 at odd power in g(ζ6), g = Δ/(t² − t + 1)². The signature function is not used.

- **First form: KILLED.** 127 of 137 in the clean stratum (3 not dividing g(ζ6)). All 10 misses have g(ζ6) = ±2.
- **Repair, made after seeing the misses.** Count the generators of the Alexander module at the prime (2, t² + t + 1): the corank of V^T − ωV over F₄. Corank 2: use (−1)^(v₂(g)). Corank 3: use +1.
- **Repaired rule, clean stratum: CHECKED 137 of 137.** 115 of 115 on knots the repair was not fitted on (v₂(g) even); 22 of 22 on the knots it was read from. So the F₄ correction is a fit; the rest is a test.
- **Opposite (F₄ correction inverted), same kill:** 115 of 137. Killed.
- **Second setup (3 divides g(ζ6)):** 31 of 54 and 1 of 2. The rule FAILS there. Failure condition: the double cover's 3-part mixes the two levels with the cofactor's 3-part.

The rule, in the clean stratum: equal sign exactly when

χ₃(product of the two 3-part units) × (−1)^(number of odd primes p ≡ 2 mod 3 at odd power in g(ζ6)) × (−1)^(v₂(g(ζ6)) if F₄-corank is 2) = +1.

**Still open.**
- No rule for the 56 roots where 3 divides g(ζ6), nor for the 6 roots at other factors (2t² − 3t + 2 twice, 3t² − 5t + 3, three quartics).
- Whether the F₄-corank correction is right at other inert primes (5, 11, …): untested, no instance on the list needed it.
- On the full list of 199 no separator is perfect or near-perfect. The best non-definitional result is the arithmetic rule, exact on 137.

---

## Q2. The m² in the commutator limits

**Scripts:** `limit_m2_01.py` (p ≤ 61), `limit_m2_02.py` (p ≤ 101), `limit_m2_03.py` (stopped on a missing import, kept), `limit_m2_04.py`, `limit_real_03.py` (failed, kept), `limit_real_04.py`, `limit_real_05.py`, `limit_real_06.py`, libraries `riley_exact.py`, `riley_exact_w.py`.

**What was found earlier, read exactly.** DEFECT-JOIN-01 matched the eight m = 1 limits to 4 sin²(πj/d), d = 6, 4, 3, 10, 14. The values 1/2, 1/4, 1/9, φ²/4, φ⁻²/4 matched nothing. The lead d = 2q rested on 6₁, 7₂ (q = 5) and 8₁ (q = 7).

**Method.** k = v(t − 2), t = tr(ab). k stays finite as s → ∞ only if v ~ κ/s² (type A) or t − 2 ~ κ/s² (type B). Each was substituted into the exact integer Riley polynomial and the leading coefficient in s taken. That gives two polynomials P_A(κ), P_B(κ) whose roots are all candidate limits, with no digits involved.

**Identities. PROVED (sympy).**
- (i) v and w = t − 2 are the two roots of X² + dM·X + k = 0, with dM = 2 − s² − s⁻². This is the main worker's k = −v(v + dM) seen from both sides; types A and B are its two roots. Also tr(ab⁻¹) − 2 = v.
- (ii) For any SL(2) pair: tr[a, c^m] − 2 = S_(m−1)(tr c)² · (tr[a, c] − 2), S the Chebyshev polynomial, S_(m−1)(2) = m. Checked m = 1 to 6 on generic matrices.

**Where the m² comes from. PROVED given (ii).** Put c = ab (type B) or c = ab⁻¹ (type A). Then tr[a, c] = tr[a, b], and tr c → 2 in the limit. So lim (2 − tr[a, c^m]) = m² · k∞. The clock value belongs to the commutator of the meridian with the m-th POWER of c; k itself is that value divided by S_(m−1)(2)² = m². The main worker's suggestion that the m² is the quadratic in v is not it: the quadratic gives the A/B pairing, the m² is the Chebyshev factor.

**The rule that survives (two-term rule). CHECKED exactly, 417 of 417.**
For a presentation p/q (q odd) take r = q for type B, or r = p − q for type A. If p = 2rm ± 1, the nonzero limits are exactly

k∞ = 4 sin²(πj/(2r)) / m², 0 < j < r, j ≡ r mod 2.

- p ≤ 101, all 1,053 presentations: 408 exact matches by the matcher (type A 174, type B 234).
- The 9 "mismatches" in `limit_m2_02.out` are all p/3 with m = 13 to 17, outside the matcher's search cap m ≤ 12. `limit_m2_04.py` checks them as exact polynomial identities: P_B = 1 − m²κ, 9 of 9.
- Opposite (types swapped), same kill: 149 of 417, and those are cases where both sets coincide or are empty. Killed.
- Kill condition was: one presentation with p = 2rm ± 1 whose exact limit set differs. None.

**(a) The d candidates, over all 1,696 clock-value factors (p ≤ 101).**

| Candidate | Holds | Fails |
|---|---|---|
| d = 2q (the given q) | 134 | 1,562 |
| d = 2q (any of the four forms of q) | 182 | 1,514 |
| d = q (any form) | 148 | 1,548 |
| d = p | 0 | 1,696 |
| d = 2p | 0 | 1,696 |
| d divides 2q or 2(p − q) | 1,103 | 593 |

So "d = 2q" is true as stated only inside the two-term rule: type B with r = q, where the factor's d divides 2q. Type A uses 2(p − q). As a general rule d = 2q, q, p, 2p all fail.

**Every nonzero limit is a clock value. CHECKED exactly:** all 1,696 nonzero irreducible factors match 4 sin²(πj/d)/m² (the other 1,470 factors are κ = 0); none is anything else, once the 9 cap cases are counted.

**Which exact limits are reached by real branches. CHECKED** (x = 12, 200 digits, exact coefficients, each type read in its own variable; 59 presentations, p ≤ 25 plus seven larger).
- Simple roots: 134 of 134 reached by a real branch (102 in `limit_real_05`, 32 in `limit_real_06`).
- Repeated roots: 8 reached, 11 not. Example: 6₃ = 13/5 has (κ − 1)² in type A and no real branch, which is why it never turns.
- No real band branch sits away from an exact value.

**Failures recorded.** `limit_real_03` reported no real branch for 8₂ = 17/3, whose limit 1/9 is printed in Two Trees. Cause: the coefficient trimming. `limit_real_04` (exact coefficients, v only) still missed 41/7, 47/3, 59/29. Cause: the root finder loses the v ~ s² cluster.

**Still open.**
- The general rule for d and m outside the two-term families (612 presentation-type pairs at p ≤ 101 have nonzero limits it does not cover). Their limits are still clock values, with d such as 4, 6, 10 that come from inner pieces of the continued fraction, and with multiplicities.
- Why the m = 1 value is the clock 4 sin²(πj/2r): untested here.

---

## Q3. A rule for the never-turners

**Scripts:** `never_census_01.py` (superseded, kept), `never_census_02.py` with five output chunks, `never_rule_03.py`, `never_rule_04.py`, `never_rule_05.py`, `never_golden_03.py`, `never_border_06.py`.

**Definition used:** that of NEVER-TURN-02 (real root with v > 0, t > 2, k < 4, on the grid x = 0.1 to 1.5 step 0.1, then 2, 2.5, 3, 3.5, 4).

**Method changes.**
- Exact integer coefficients, no trimming.
- Pass 1: a sign change of the exact polynomial along the band proves a turn with no root finder.
- Pass 2 only if pass 1 is silent: roots at 80 digits in both variables, each for its own half of the band; a root-only hit must be confirmed by a sign change at 160 digits.

**Census. CHECKED, 80 digits.** Every two-bridge knot with p ≤ 75, up to mirror and q ↔ 1/q: 285 non-torus knots, 250 TURN, 35 NEVER. Torus knots were run for p ≤ 21 as a control (all never).
- Control passed: census 8.8 reproduces 19 turn / 7 never, and the nine-crossing additions 27/5, 29/9, 55/21 reproduce.
- Cap: p ≤ 75 instead of 101. A never verdict at p ~ 100 costs about 20 minutes of root finding per knot.
- `never_census_01` gave six false turns "by roots only" at x = 3.5 or 4 (47/9, 49/9, 49/17, 53/5, 53/17, 55/21). 47/9 was rechecked at 80, 160 and 320 digits: a spurious real root at 80 only. `never_census_02` has no root-only turns and no unconfirmed hits.
- Borderline re-check at 160 digits (`never_border_06`): 37/13, 61/21, 63/13 carry a nearly real complex pair (relative imaginary part 10⁻⁸·⁷, 10⁻¹⁵·⁶, 10⁻⁸·⁷). It is identical at 80 and 160 digits, so it is a true complex pair. NEVER stands.
- 43/5 is NEVER, confirming the earlier 80-digit result.

**The 35 non-torus never-turners, p ≤ 75:**
13/5, 17/5, 23/5, 25/9, 27/5, 29/9, 33/5, 37/5, 37/13, 41/9, 41/13, 43/5, 43/9, 47/5, 47/9, 49/9, 49/17, 53/5, 53/17, 55/21, 57/5, 59/9, 61/9, 61/21, 63/5, 63/13, 65/9, 65/21, 67/5, 67/9, 67/13, 71/21, 73/5, 73/25, 75/29.

**Rules scored on the 285 knots.**

| Rule | Result |
|---|---|
| T1 (one-way): Alexander polynomial has a real positive root → TURN | 141 of 141, no exception |
| T2 (one-way): a limit polynomial has a nonzero root of odd multiplicity → TURN | 195 of 195, no exception |
| T1 or T2 together | decide 232; the 53 left are 35 NEVER and 18 TURN |
| **R3: NEVER iff p/q = a ± 1/(b + 1/c), a odd ≥ 3, b, c even, a > c** | predicts 32, all 32 never, 0 wrong; misses 3 (55/21, 71/21, 75/29); 282 of 285 |
| R3 opposite (a < c) | 7 right, 9 wrong; killed |
| R3 without the clause a > c | 9 false nevers (31/7, 45/7, 47/11, 55/13, 59/7, 69/11, 71/11, 71/17, …); killed |
| **R4: R3 plus longer even blocks (below)** | 35 of 35, 0 false; 285 of 285, three of them fitted |
| Earlier family [a,2,2], a odd | 6 of 6 right, misses 29: a sub-case of R3 |
| Earlier family [a,1,1,2], a even | 7 of 7 right, misses 28: R3 with the minus sign |
| Earlier family [a,m,2], m even | 13 of 13 right, misses 22: R3 with c = 2 |
| p mod 4 | 1: 20 never / 123 turn; 3: 15 / 127; no |
| p mod 8 | 12/63, 8/66, 8/60, 7/61; no |
| p prime | prime 23 / 144; composite 12 / 106; no |
| q² ≡ +1, −1, other mod p | 1/12, 2/10, 32/228; no |
| Palindromic continued fraction | 3 / 5 against 32 / 245; no |
| Last continued-fraction entry even | odd: 0 / 112; even: 35 / 138; one-way only |
| Parity pattern of the continued fraction | "oee" 15 / 0; "eooe" 17 / 4; 4 wrong at best |
| Signature 0 | 7 / 58 against 28 / 192; no |
| \|signature\| = 2·genus | 15 / 82 against 20 / 168; no |
| All Alexander roots on the unit circle | 17 / 84 against 18 / 166; no |
| Real negative Alexander root | never occurs (0 of 285) |
| "No real Riley root in the turning range" | this IS the definition; it cannot be scored as a separate rule |

**R3 in ordinary continued fractions:** [a, b, c] and [a − 1, 1, b − 1, c], with a odd ≥ 3, b and c even, a > c. A knot qualifies if any of its forms does; 77/9 is both 9 − 1/(2 + 1/4) and 5 − 1/(2 + 1/8).

**R3 tested outside what it was read from.** R3 was read off p ≤ 55.
- p = 57 to 75: 13 predicted never, 13 never; no false positive among the 132 knots of that range. CHECKED, full method.
- p = 77 to 101 (`never_rule_04`, capped): 25 predicted never, 0 show a sign change at any grid x (80 and 160 digits). All 7 genuine near misses (a < c) are PROVED to turn by sign change. The root finder was run on only 4 of the 25 and only at x = 0.5, 0.8, 1.2, 2.0: no real band root. So for p > 75 "never" is not established, only not contradicted.

**R4 (a lead; the three exceptions are fitted, not tested).**
NEVER iff p/q = a ± 1/E, a odd ≥ 3, E = [e₁, …, e₂ₙ] with even entries, even length, signs pairing up (e₁e₂ > 0, e₃e₄ > 0, …; the sign may change only between pairs), and for n = 1 the clause a > e₂.
- 55/21 = 3 − 1/[2,2,−2,−2]; 71/21 = 3 + 1/[2,2,−2,−2]; 75/29 = 3 − 1/[2,2,2,2].
- Opposite (a sign change inside a pair), same kill: 61 of 69 turn at n = 1, 56 of 64 at n = 2. The 8 never in each are knots that also have a paired form.
- Predictions of R4 at n = 2: 97/21 and 99/29 never. Capped check: silent on the full sign scan, no real band root at four x. Not established.
- No size clause is known for n ≥ 2; none could be tested below p = 101.

**Golden family [2, 1ⁿ, 2] (`never_golden_03`).**

| n | knot | result | R4 says |
|---|---|---|---|
| 2 | 13/5 | NEVER (census) | never |
| 3 | 21/13 | TURN, proved by sign change at 200 and 400 digits | turn |
| 5 | 55/21 | NEVER (census) | never |
| 6 | 89/34 | **TURN**, proved by sign change at x = 0.8, 200 and 400 digits (k ≈ 0.0083) | turn |
| 8 | 233/89 | no sign change at any grid x at 200 digits; not decided | never |

- The earlier guess "n = 2, 5, 8 never; n = 0, 3, 6 turn" was recorded as failed because 89/34 came out never. That verdict was the trimming flaw. The guess is alive.
- **233/89 at 200 digits, finished.** The band point of NEVER-TURN-05 (x = 0.8, v = 1.1301089, k = 2.288) is not a root: the exact polynomial has the same sign at v(1 ∓ 10⁻⁴) at 200 and at 400 digits. No sign change at any of the 20 grid x. A never verdict would need the root finder at degree 116, which was not run; "never" for 233/89 is untested beyond that silence.

**Still open.**
- A proof of R3, and the size clause of R4 for n ≥ 2.
- T1 is given with a reason (the real slice passes through a reducible representation at s² = root and v changes sign); it was checked, not proved here. It matches the entry points printed in Two Trees census 8.8: 6₁ at x = 0.350 against ½ ln 2 = 0.347, and 8₁ at 0.285 against ½ ln((7 + √13)/6) = 0.285 (arithmetic on the printed values, not a new run).
- Whether a knot that turns always stays in the band as x → ∞ was not tested beyond the paper's 26.

---

## Q4. Sign of the hidden level g

**Scripts:** `hidden_g_01.py` (atoms), `hidden_g_02.py` and `hidden_g_03.py` (knots).

**Data found.**
- Atoms: `/home/claude/src/votkp-lean/data/element_thresholds_20261011.json.gz` (pointed out by the main worker): 118 elements, all thresholds.
- Knots: no fitted κ, g, d and no stored shape tables exist in the vd5 archive, votkp-lean or elemental-peeling-lean. Shapes were generated with SnapPy along Dehn-filling families.

**Kill condition (written first, both sides).** Fit on points with index mod 4 ≠ 2, predict the held-out points. The sign of g counts for a family only if held-out RMS of the one-pole form is at most half that of the straight line (and, for atoms, the pole lies outside the fitted range).

### Atom side

Family = fixed electron count N; a = Z; z = IE(Z, N)/IE(Z, N+1), the peel step between the ions holding N+1 and N electrons. 98 families with at least 12 points.

| Setup | Families that count | g < 0 | g > 0 |
|---|---|---|---|
| Main (interleaved hold-out) | 62 | 62 | 0 |
| Second setup (fit lower 70% of Z, predict top 30%) | 84 | 84 | 0 |
| Opposite (step read downward, z → 1/z) | 61 | 0 | 61 |

- **CHECKED: g is negative in every family that counts** (62 of 62; 84 of 84). Sign agrees between the two setups in 60 of the 62.
- The 36 families with no verdict are N = 6, 14, 28, 32, 40 and most N ≥ 44, where the line does about as well.
- By kind of step: 7 shell openings and 55 steps inside a shell, all g < 0.
- Fitted κ is within 0.05 of 1 in 55 of 62 families; 3.92 at N = 2 (bare value 4) and 2.10 at N = 10 (bare 2.25).
- The pole sits at the neutral point: d − N has median −0.22, and |d − N| < 1 in 54 of 62.
- **READING.** g < 0 is the Hermitian sign of VOTKP 5.3. It is also what plain screening gives (z falls toward κ as Z grows), so it confirms the reading without separating it from screening. The opposite run shows the sign belongs to the direction the step is read: read downward, every g is positive.

### Knot side

Family = (link, cusp, tetrahedron); a = the filling integer in slope (1, a), |a| = 3 to 40; complex κ, g, d. L5a1 with (1, a) gives the twist knots 6₁, 8₁, 10₁ (identified by SnapPy for a = 2, 3, 4). Second setup: L6a2, L7a5, L7a6, both cusps. Opposite: slopes (a, 1).

- 48 (family, tetrahedron) fits; 45 count. Fitted κ equals the cusped shape to 3 or 4 digits in every counted fit.
- **"g is negative real": KILLED.** 4 of 45. Re g < 0 in 19, > 0 in 26; arg g runs over the whole circle. The 4 that pass are forced by the symmetry of L5a1 and L6a2.
- For the Whitehead family the four values are g = +iπ/2, +π/4, −π/4, −iπ/2 (1.5711 and 0.7856 at |a| = 20 to 100, against π/2 = 1.5708 and π/4 = 0.7854). CHECKED to 4 digits.
- **The pole d = −1/τ (cusp shape, not fitted): KILLED.** 1 of 45 within 0.15. Each tetrahedron has its own pole.
- Second setup for the kills (`hidden_g_03`, |a| = 20 to 100 against 3 to 40): g and d are stable in 15 of 16 fits, so both kills stand; they are not artefacts of small fillings.
- **READING.** On the knot side the one-pole form holds as a fit, but the level is not Hermitian-coupled: g is complex. In the terms of read record 08 the tetrahedron is an open channel. Atoms give g < 0 real; knots give complex g. That is a difference between the two sides.

**Still open / what data is missing.**
- The original fitted κ, g, d that carried item 2 refers to are not on disk; if they came from another family (a different parameter a), that family would need to be named to refit it.
- Only (1, a) and (a, 1) fillings of four links were run. The knots-to-10-crossings shape table of the vacuum disk is not a one-parameter family and cannot be used for this fit.

---

## Files

- Q1: `split_signs_01.py/.out/.pkl`, `split_signs_02.py/.out`
- Q2: `limit_m2_01.py/.out/.pkl`, `limit_m2_02.py/.out/.pkl`, `limit_m2_03.py/.out`, `limit_m2_04.py/.out`, `limit_real_03.py/.out`, `limit_real_04.py/.out`, `limit_real_05.py/.out`, `limit_real_06.py/.out`
- Q3: `never_census_01.py` (+3 chunks), `never_census_02.py` (+5 chunks, .json and .out), `never_rule_03.py/.out`, `never_rule_04.py/.out`, `never_rule_05.py/.out`, `never_golden_03.py/.out`, `never_border_06.py/.out`
- Q4: `hidden_g_01.py/.out`, `hidden_g_02.py/.out`, `hidden_g_03.py/.out`
- Libraries: `riley_exact.py`, `riley_exact_w.py`

Memory: no stored fact was used as a result; the standing working rules in the task were followed as given. Nothing in memory asked for an action outside this task.
