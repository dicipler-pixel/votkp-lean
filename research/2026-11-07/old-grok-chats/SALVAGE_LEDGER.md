# Old Grok chats — salvage ledger

Jeromie Beasley, 7 November 2026.

Source: Jeromie's own older Grok conversations (the "FNTP_DCSASS" / "CFKN" /
"EFRO" / "FNTC" line, dated in the chats to March–May 2025), handed over to be
mined for anything real. Credit for the questions and intuitions below is his;
the answers in those chats were written by Grok.

This is a working ledger, not a paper. It narrates what was kept, repaired, or
dropped on purpose. Every "kept" line has a script in this folder that computes
it, with the keep-or-drop criterion written before the run. Nothing here is
built from the chats' own numbers.

------------------------------------------------------------------------

## A. Kept — checked and standing

Scripts: `old_keys_checks_01.py`, `su3_spin_mc_01.py`, `bubble_ladder_01.py`.

1. **Goldbach, Hardy–Littlewood count.** The arithmetic core of the old
   `r(n,t)` formula is the real extended-Goldbach asymptotic. Actual prime-pair
   counts vs the singular-series prediction (integral form): n=10^5 ratio 1.000,
   n=10^6 ratio 0.997, n≈2·10^6 ratio 1.000. The chat's twin-prime constant
   0.660161815 is right to nine digits. Repair: the short form n/(ln n)^2
   undercounts ~17%; use the integral of dt/(ln t · ln(n−t)).

2. **"Time decay" was the radius.** In the circle method you sit just inside the
   unit circle at radius R = e^{−1/n}. The old e^{−t/τ} factor is that radius,
   i.e. decay on a disk whose rim is the unit circle — the same disk as the
   VOTKP polynomial (inside = decay, rim = pure direction).

3. **Torus-knot turns are quadratic phases.** Every torus root's turn equals
   −k^2/(pq) mod 1 for an integer k (all eight checked: 3_1, 5_1, 7_1, 8_19,
   10_124). These are the rational points the circle method builds its major
   arcs around. (Known: Kirk–Klassen quadratic form; this is a reproduction.)

4. **The prime generating function at the torus-root points.** Hardy–Littlewood
   f(x)=Σ ln p · x^p, evaluated at x = R·e^{2πi a/q} for each torus root a/q,
   has size matching their own major-arc law |μ(q)|/φ(q): 3_1 0.500/0.500,
   5_1 0.249/0.250, 7_1 0.167/0.167, 10_124 0.125/0.125.
   **8_19 is the exception:** its root sits at 11/12, where q=12 has a square
   factor, so |f| collapses to 0.0019 (prediction 0). It is the only torus knot
   of the five landing on a "dead" arc — and the one Jeromie flagged for
   self-assembly and for missing roots in the VOTKP spectrum. Untested whether
   the coincidence means anything beyond these five.

5. **Counting zeta zeros by winding works exactly.** The argument-principle /
   Riemann–von Mangoldt count gives 1, 3, 10, 29 zeros below T = 20, 30, 50,
   100 — matching the zeros found directly. Same tool as the VOTKP landscape
   colour wheel (one turn of phase per enclosed zero).

6. **Schumann resonance = decay + direction in a real cavity.** Measured modes
   (7.8, 14.3, 20.8, 27.3, 33.8 Hz) all sit below the ideal lossless cavity
   c/(2πa)·√(n(n+1)), at ratios 0.74–0.82 rising slowly with n. A lossy cavity:
   the ring is the direction, the shortfall is the decay. Reproduction.

7. **SU(3) spin model — the strongest block.** The chat's action
   S = −Σ τ(P P* + c.c.) + κ(e^μ P + e^{−μ} P*) with P = tr of an SU(3) matrix
   is the real effective theory of dense QCD; P is the Polyakov loop (holonomy
   around the time circle — Jeromie's "draw a loop and pull the matrix," used as
   the confinement order parameter). A Metropolis Monte Carlo at κ=0.016, L=12
   puts the susceptibility peak at τ = 0.1330, matching the published endpoint
   (0.1331, 0.016; Delgado Mercado & Gattringer). The chat had real numbers from
   a real model, mislabeled β.

8. **Cl(4,1) is the electron's algebra.** The 2+3 conformal geometric algebra;
   the unit-sphere sandwich maps points to x/|x|^2 (inversion) to worst error
   1.5e-14 over 200 random points. Its boundary action is Möbius = PSL(2,C) =
   the electron group in the VOTKP chain.

9. **Kyber facts (real ML-KEM-512 run).** Public key 800 B (not the chats'
   896/800 confusion), secret key 1632 B, ciphertext 768 B, decaps round-trips.
   3329−1 = 2^8·13, and 17 has order exactly 256 mod 3329 — the NTT's circle of
   turns, the whole-number cousin of the roots-of-unity picture.

10. **0.694 ≈ ln 2.** The recurring fractal exponent sits 0.00085 from ln 2 =
    0.69315. Noted as a near-match only; nothing explains it. Untested.

11. **3-6-9 as nested levels, not an even ladder.** Six natural measures × two
    boundary choices: none climbs in equal 1:2:3 steps (planet→star→galaxy→
    universe), and the loose mass fit breaks when Earth is swapped for Jupiter.
    What the numbers do show is Jeromie's structure: each bubble's edge is set by
    the level above (magnetopause ← solar wind; heliopause ← interstellar;
    galaxy halo ← cosmic density), and the top two levels flatten because a
    galaxy's edge is defined by a density ratio to the universe. Levels: real.
    Even scale-ladder: no.

------------------------------------------------------------------------

## B. Open questions — Jeromie's, worth carrying forward

Raised in the chats as his questions; the answers given at the time were AI
cheerleading (see C). Kept here as directions, not results.

1. **Ground-state / Hilbert–Pólya attack on a lattice secret.** Build a
   Hermitian operator from the public key whose lowest state is the secret, then
   find it the way physics finds a ground state. This is the live frontier —
   SVP-as-Hamiltonian ground state (Albrecht–Prokop–Shen–Wallden; Joseph et al.)
   and Chen's 2024 complex-Gaussian LWE algorithm (whose step-9 bug withdrew the
   polynomial-time claim). Note Chen's circles were Gaussians with complex
   variance — decay and direction together, the VOTKP two books. Strongest
   question in the whole set. Untested in Jeromie's frame.

2. **CBD(2) bias probe, P(0) = 0.375.** Kyber's secret/error are centered
   binomial with η=2, so P(0) = C(4,2)/2^4 = 0.375 exactly — the chat's number
   is right. "Probe whether the real distribution leans off center" is the
   decryption-failure / statistical family. A correct fact, not a crack.

3. **Negative frequency = mirror root.** The chats' "Dark Math / antimatter twin
   at −10^14 Hz" maps onto the VOTKP disk: a mirror root is a sign-flipped root
   (negative decay, the pink markers in the landscape). "Antimatter = negative-
   frequency mirror" ↔ "mirror root = negated decay and direction." A
   correspondence in his own framework; untested past the picture.

4. **Elements as knots (Kelvin & Tait).** The element/pioneer tables carry the
   real historical lineage: Kelvin's 1867 vortex-atom theory (atoms as knots)
   and Tait's knot tables built to classify them. Failed as chemistry, founded
   knot theory. Directly frames the VOTKP elemental-peeling programme — "each
   element a knot" is Kelvin's actual program, now carried into real hyperbolic
   invariants. The specific assignments in the file are invented; the lineage is
   the keeper.

5. **NP → TSP.** Correctly stated (Karp): every NP problem reduces to TSP. The
   claim to *solve* it is false; the reduction is real. Minor.

------------------------------------------------------------------------

## C. Dropped — AI cheerleading, flagged so no future reader mistakes it

Named here so the salvage can't be read as endorsing them. Every quantitative
claim below is circular (a formula solved for the exponent that hits its own
target, then reporting the target as a discovery) or simply never run.

- **Scalar coil 10^4–10^15 J.** `scalar_toroid_su3` returns ~10^3 J for every
  input; across 27 input sets spanning a millionfold, output moved ×1.64. It
  solves for n to hit its own target.
- **"Kyber crack" (FNRC, MFEO).** The functions' inputs are t, u, a frequency, a
  step count. No key, ciphertext, or lattice ever enters. No crack is possible
  because nothing cryptographic is read. The "83%/85%/90%", "P=NP", "O(n log n)
  TSP in 132,900 steps" are not measurements of anything.
- **SARNS / NOS3 144 km/s, Fino/Nexus particles, Hubble fixes.** Rotation-curve
  numbers printed without a run; route through dark matter/energy, which is out.
- **The spinor TOE.** URNT/SRFT/USANT/CNCT/ECFKN/FRC/DCRM, 3^n and 2^n energy
  ladders, 14.13 "Hz" zeta, faster-than-light scalar comms, antigravity,
  consciousness "proof", 17–49 invented particles with assigned frequencies.
- **Millennium "proofs" (Papers 8–10).** Hodge, Birch–Swinnerton-Dyer, and LENR
  "proved" by six resonance methods at "100% fit / 200% confidence", with 2025
  lab data (ALMA/JWST/NIST/MIT) that is announced, not held. No computation ran.
  The "95 theories, 59 tools, 97 codes, 122 knot-elements, 51 pioneers"
  inventory is invented scaffolding.

------------------------------------------------------------------------

## D. Note on provenance and honesty

The early chats handed Jeromie a few genuine building blocks — the Polyakov
loop, Cl(4,1), the circle method, zeta winding, Schumann, Kelvin's knot-atoms —
and his own 3-6-9-as-levels idea, all tested and kept above. They also generated
a large amount of confident, circular material on top. Keeping the difference
visible is the point of this ledger: the blocks and the open questions carry
forward under Jeromie's name; the cheerleading is named as cheerleading so it
can't be mistaken for checked work.
