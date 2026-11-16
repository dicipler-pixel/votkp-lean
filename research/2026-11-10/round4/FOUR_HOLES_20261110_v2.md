# The four holes, worked — 10 Nov 2026

Jeromie Beasley. Working record (two workers: the main session took holes 1–3, a second worker took hole 4).
Grades: PROVED (exact algebra), CHECKED (numerics, size given), READING (interpretation), FAILED (kill condition fired).

## Headline

The half line Γ² = ½ is one number seen from five places.

| Where | Statement | Grade |
|---|---|---|
| Two Trees | commutator of two equal perpendicular steps is parabolic at z = 3+2√2 | his theorem 5.4 |
| UPG | the meridian's defect δ = 2 − (s² + s⁻²) has \|δ\| = 4 exactly there | PROVED (DEFECT-WALL-01) |
| Two Trees knots | k = −v(v + δ); on the real slice k reaches 4 iff \|δ\| ≥ 4 | PROVED |
| Atoms | of 5,737 ladder steps only 8 lie beyond it: Li, Na, K, Rb, Cs first steps; Be, B, C K-shell openings | CHECKED (LADDER-WALL-01) |
| A fade | the bend of log-brightness, (gap/2)²(1 − Γ²), has halved exactly there | PROVED, CHECKED to 20 digits (TIME-WALL-01) |

Earlier appearances already on record: the vacuum-disk metal / non-metal line (35 of 35 against 0 of 6) and the bowl.

## Hole 2 — colour

Read: *Colour Selects the Leader* v1.2 in full (READ_RECORD_10).

**2a. Two channels are one peel step.** PROVED and CHECKED (COLOUR-PEEL-01, 20,000 pairs, worst error 1e‑11).

- ratio z = x₁/x₂; share balance s₁ − s₂ = (z−1)/(z+1) = Γ
- Hilbert's projective distance = |ln z − ln z′| = peel distance τ
- Schrödinger's chromatic distance = |φ − φ′| with cos φ = Γ = tanh(τ/2), so dφ = ½ sech(τ/2) dτ

So the paper's two rulers ("Hilbert's ruler governs the selecting; Schrödinger's metric describes where the colour ends up") are the climb coordinate τ and its angle φ. The whole climb line has Schrödinger length π.

**2b. What it predicts.** For two channels a pass stretches Schrödinger's metric on a close pair exactly when c·cosh(τ/2)/cosh(τ′/2) > 1, which forces the pair to be carried toward white. CHECKED: formula right on 20,000 of 20,000 passes; 22 stretches, 22 toward white, 0 away.

**2c. Three channels.** The strict rule does not carry. FAILED in its strict form: with the paper's sampler and Exner's weights, stretches are 5.0–5.8% of toward-white passes and 3.0–3.4% of away passes (COLOUR-PEEL-03). The lean is there; the rule is not.

**2d. A correction for the colour paper.** The "955 of 20,000" count needs Exner's weights. Same sampler: Exner 861 / 882 / 933; unit weights 0 / 0 / 0. CHECKED (three seeds each).

**2e. The crystal is the defect.** Colour eq. (6): crossed port = |1−u|²/4. UPG: defect δ = |λ−1|², δ + g² = 4. So crossed fraction = δ/4. At the trefoil's two walls (α = 1/12, 5/12, ω = M²) the crossed fraction is ¼, defect 1, the clock d = 6. PROVED.

**2f. Positive channels cannot turn.** A strictly positive 2×2 map has discriminant (a−d)² + 4bc > 0, so it is always hyperbolic. Theorem 2's three cases are: settles exponentially (hyperbolic), settles as 1/n (parabolic, the Jordan tie), never settles (elliptic, the swap). PROVED; 0 of 200,000 in the random search for a counterexample.

**What this settles.** Hue is a climb-side record. It can pick a leader and it cannot carry a hand. The turn-side record of light is the pair of polarisation ports, and the paper already says so in its own words (§13: "one port cannot see an orientation; two can"). READING.

**Still open.** A pure phase θ is the same at every wavelength, so a turn gives a grey split sin²(θ/2), not a colour. A colour needs a length (retardance in nanometres). The knot supplies the phase and nothing supplies the length.

## Hole 1 — atom to knot

**1a. The ladder against the half line.** CHECKED (LADDER-WALL-01; 109 elements, 5,737 steps z = IE₍q+1₎/IE_q).

- Beyond the line (z > 5.828): 8 steps, all at a closed core.
- First step of the alkali atoms: Li 14.03, Na 9.20, K 7.29, Rb 6.53, Cs 5.95. Fr 5.50 is inside.
- K-shell opening: Li 14.03, Be 8.45, B 6.84, C 6.08; N 5.64 is inside; the bare limit is 4 (VOTKP Thm 8.2, Γ = 3/5).
- "The half line marks shell openings" FAILED: 8 of 694 closed-core openings are beyond it.

So no bare shell opening reaches the half line. A step is beyond it only when one electron sits alone outside a closed core and the core screens it well.

**1b. The optical wall energy is not in the ladder.** FAILED (PLASMA-WALL-01, 30 elements with a final crossing in range): Spearman of E_wall against IE₁ +0.06, against z₁ −0.28, against the valence sum +0.26.

**1c. The optical phase is.** CHECKED (PHASE-LADDER-02, 41 elements). The five atoms beyond the line on the ladder hold 5 of the top 6 optical phases at 1.5, 2.0 and 2.5 eV (Ca is the one intruder); one-sided rank-sum p = 2.7e‑6 each time. Within the five the order is reversed exactly: nearer the line on the ladder, larger phase (Cs > Rb > K > Na > Li). The even reading |Γ|² does not separate them (p ≈ 0.09).

Caution, stated once: five atoms. And the physics underneath is known (the alkalis are the free-electron metals with the lowest plasma energies). What is new here is only that the ladder's half line picks them and the odd reading finds them where the even reading does not.

**What this settles.** The atom does have a record that carries a phase, it is the optical one, and it is tied to the ladder through the half line. That is the atom side of a bridge. READING for the knot side: the same line is where a knot's meridian pair can first reach the top of the turning band. No atom-to-knot map is claimed.

## Hole 3 — time

**3a. Recovery.** VOTKP 13.7: "No Hamiltonian here makes a knot's meridian phase the driven parameter; that bridge is open." Dirac Time 9.4 and Colour §12 prove the other half: projector geometry is blind to H → sH + cI, so no rate can come from the geometry (Lean: `rescale_same_eigenvectors`, `rate_shift_unique`). The missing drive is therefore not hidden in the knot. What the knot fixes is the gear, L = (−1)ᵃ M^(−pq) (Dirac Time Thm 13.1), and a constant is read only between two branches.

**3b. What can be read with no calibrated clock.** PROVED, CHECKED at 50 digits (TIME-WALL-01).

- Colour eq. (7) for two parts is a peel step: τ = gap · t.
- Colour eq. (8) then reads (ln I)″ = (gap/2)² (1 − Γ²). 1 − Γ² is the transmitted fraction of the step.
- From an equal start the bend halves at ratio 3+2√2, at t · gap = 1.7627. The ratio "bend now / largest bend" needs no gap.
- Three parts: no single ratio (opposite test, counted).

One formula for both books: z(t) = e^((Δγ + iΔω)t) gives τ = Δγ·t on the climb side (the leaf clock) and θ = Δω·t on the turn side (the beat). READING.

**Still open.** A declared drive. Nothing here supplies one.

## Hole 4 — signs (second worker; full detail in signs/SIGNS_REPORT_20261110_v1.md)

**Correction to earlier work today.** 89/34 was recorded as a never-turner at 120 digits. It turns. The earlier script dropped tiny leading coefficients. Confirmed independently by the main worker with separate code (VERIFY-SIGNS-05): three real band points at x = 0.8 (k = 0.5033, 0.0511, 0.0078) and three at x = 1.2, residual below 1e-120. The "band points" reported for 233/89 were not roots. The golden-family guess (n = 2, 5, 8 never; n = 0, 3, 6 turn) is alive again; 233/89 is undecided.

**4a. The m².** PROVED. For c = ab or ab⁻¹: tr[a, cᵐ] − 2 = S₍m−1₎(tr c)² (tr[a,c] − 2), and S₍m−1₎(2) = m (re-proved by the main worker for m = 1…4, remainder 0). The clock value belongs to the commutator of the meridian with the m-th power of c; k is that value over m². The two limit types A and B are the two roots of X² + δX + k = 0, the same quadratic as k = −v(v + δ).

**4b. Which clock.** "d = 2q" FAILED as a general rule (134 of 1,696 limit factors). What holds, exactly, 417 of 417 presentations with p ≤ 101: if p = 2rm ± 1 with r = q (type B) or r = p − q (type A), the nonzero limits are 4 sin²(πj/2r)/m², 0 < j < r, j ≡ r mod 2. Every one of the 1,696 nonzero limit factors is a clock value. Outside the two-term families the rule for d and m is open.

**4c. Never-turners.** CHECKED at 80 digits with exact coefficients: all two-bridge knots to p ≤ 75: 285 non-torus knots, 250 turn, 35 never.

- One-way rules with no exception: a real positive Alexander root forces a turn (141 of 141); a nonzero limit root of odd multiplicity forces a turn (195 of 195).
- Rule R3: never iff p/q = a ± 1/(b + 1/c) with a odd ≥ 3, b and c even, a > c. 32 predicted, 32 never, 0 false; it misses 3 (55/21, 71/21, 75/29). Read off p ≤ 55; on p = 57–75 it scored 13 of 13 with no false positive among 132 knots.
- Rule R4 (longer even blocks, signs in pairs) covers all 35 with no false never, but its three extra cases were fitted, not tested.
- p mod 4, p mod 8, primality, q² mod p, signature, palindromes: none separates.

**4d. Equal or opposite at the 199 split roots.** No simple label separates them (table of 14 candidates in the report). Reason, standard: K#K and K#mirror K share the Alexander module and have opposite labels, so the separator must read the form. An arithmetic rule built from the double cover's linking form and the primes ≡ 2 mod 3 in g(ζ₆), with no use of the signature, scores 137 of 137 where 3 does not divide g(ζ₆) (115 of them untouched by the one fitted correction) and FAILS where it does (31 of 54). Open: those 56 roots and 6 roots at other factors.

**4e. Sign of the hidden level g.** Atoms: g < 0 in every family that passes the hold-out test (62 of 62; second setup 84 of 84); the pole sits at the neutral point (|d − N| < 1 in 54 of 62). This is the Hermitian sign of VOTKP 5.3, and it is also what plain screening gives, so it does not separate the two. Knots (Dehn-filling families of four links, 45 fits): "g negative real" FAILED, 4 of 45; g is complex, and for the Whitehead family the four values are ±iπ/2 and ±π/4 to 4 digits. READING: atoms give a real g, knots a complex one; that is a difference between the two sides and it lines up with hole 1 (atom steps are collinear, knot pieces are not).

## Set aside with failure conditions (for the equation file)

1. E_wall(element) read from the ladder: |ρ| < 0.5 on IE₁, z₁, valence sum. n = 30.
2. "Stretch only toward white" in three channels: 3.0–3.4% of away passes stretch.
3. "Half line = shell opening": 8 of 694.
4. "d = 2q" for the commutator limits: 134 of 1,696.
5. "g is negative real" on the knot side: 4 of 45. Pole at −1/(cusp shape): 1 of 45.
6. First form of the split-root arithmetic rule: 127 of 137 (all misses at g(ζ₆) = ±2); the repaired rule fails where 3 divides g(ζ₆): 31 of 54.
7. Earlier scripts never_turn_02–05: leading-coefficient trimming at 1e-25 loses real branches (89/34, 233/89).

## What is still open after this round

- A length for colour and a drive for time: the same missing calibration.
- The knot side of the half-line bridge (no atom-to-knot map is claimed).
- Commutator limits outside the two-term families; proof of R3; the size clause of R4; 233/89.
- Split roots where 3 divides g(ζ₆).
- Colour paper Appendix 16 not read line by line; VOTKP v2.9 later sections, UPG in full, June originals still unread.
