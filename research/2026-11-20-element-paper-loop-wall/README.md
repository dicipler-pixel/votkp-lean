# Element paper: the loop wall (H to Ne)

Jeromie Beasley · 20 November 2026 · VOTKP element work, first two batches (Z = 1 to 10)

This folder holds the Lean formalization of the loop wall and the hydrogen-to-neon element
certificates, the arithmetic checks of the two element batches, and the research batches they
check. It is kept for the element paper.

## What is proved (`lean/LoopWall.lean`, core Lean 4.34.1, no Mathlib, exact `Rat` arithmetic)

81 theorems. Axioms: only `propext`, `Classical.choice`, `Quot.sound`. No `sorry`, `admit`,
`native_decide` or `axiom`. Run `lean/run_checks.sh`; its output is `lean/run_checks_output.txt`.

The peel step of an ordered pair of thresholds (a, then b) has ratio z = b/a and reflection
Γ(z) = (z − 1)/(z + 1), which is tanh(½ ln z) (proved for reals in `VOTKP/Smith.lean`, `smith_identity`).

1. **Direction.** Reversing the order gives Γ(1/z) = −Γ(z) (`gam_reverse`); the returned power
   Γ² is the same both ways (`power_even`). The sign carries the direction; a ledger of Γ² alone
   cannot tell the two orders apart. "Γ² is odd" is refuted at z = 2 (`refute_power_odd`).
2. **The loop wall.** For every positive z,
   Γ(z)² > ½ ⇔ z² − 6z + 1 > 0 ⇔ 0 < z < 3 − 2√2 or z > 3 + 2√2
   (`wall_quadratic`, `wall_two_branches`). The upper branch alone is the statement for forward
   ratios z ≥ 1 (`outside_iff`). Reversal keeps the wall classification (`reverse_same_side`):
   z = 6 gives Γ = 5/7, z = 1/6 gives Γ = −5/7, both Γ² = 25/49 > ½ (`six_and_sixth`).
   √2 never enters: the branches are written as z > 3 ∧ (z − 3)² > 8 and z < 3 ∧ (3 − z)² > 8.
3. **The equal-face form.** With h = ½ ln z, sinh² h = (z − 1)²/(4z) = Γ²/(1 − Γ²)
   (`sinh_sq_form`), so the equal-face condition sinh h_a · sinh h_b = 1 is exactly Γ² = ½.
4. **Fixed points.** The hydrogenic n = 2 → 1 limit z = 4 gives Γ = 3/5, inside the wall
   (`hydrogenic_limit`); Γ = 2/3 exactly at z = 5 (`two_thirds_iff`).
5. **The 1s core opening** (last 2s removal → first 1s removal), using the encoded reference
   thresholds (NIST ASD v5.12): Li, Be, B, C outside the wall; N, O, F, Ne inside
   (`k_opening_*`, `crossing_C_N`). Neon's encoded ratio is strictly greater than five
   (`neon_just_above_two_thirds`); measurement uncertainty is a separate question.
6. **Rung 0** (anion → neutral: electron affinity, then first ionization energy): H, Li, B, C, O
   outside; F inside (`rung0_*`). He, Be, N and Ne have no bound ground-state anion.
   Oxygen's anion rung is outside the loop wall and its 1s core-opening rung is inside, using
   the encoded reference thresholds (`oxygen_two_sides`).
7. **The screened series** of the 11 November 2026 shell-screening note puts the crossing
   between Z = 6 and 7 (`screened_six_outside`, `screened_seven_inside`); the unscreened control
   moves it to between 9 and 10 (`bare_nine_outside`, `bare_ten_inside`).
8. **False controls** (`lean/controls/`): N outside, F's rung 0 outside, C inside, neon's ratio
   exactly 5, the screened Z = 7 outside, Γ² odd, Mg's L opening outside, Si's rung 0 inside, Ca's M opening outside, S above σ with a
   bare hydrogenic H-like energy. Each is rejected by Lean and each is refuted
   as a theorem in `LoopWall.lean` (`refute_*`).

9. **Batch 3, sodium to phosphorus.** The L opening (last 3s → first 2p) crosses the wall
   between Na and Mg (`l_crossing_Na_Mg`); the K opening is inside for all five; rung 0 is outside
   for Na, Al, Si and P, and silicon's stays outside at both ends of its quoted uncertainties
   (`rung0_Si_low`, `rung0_Si_high`). Every step of magnesium's ladder is inside the wall
   (`mg_all_inside`), and Mg conducts, so an outside atomic rung is not required for conduction.
   The strongest ordinary step changes from the L to the K opening between Mg and Al
   (`rank_swap_Mg_Al`). The screened series keeps the K opening inside for Z = 11 to 15.
10. **Batch 4, sulfur to calcium.** The M opening (last 4s → first 3p) crosses the wall between
   K and Ca (`m_crossing_K_Ca`); L and K openings are inside for all five; rung 0 is inside for S
   and Cl, outside for K and Ca (Ca at Γ₀ ≈ 0.992, still outside at the high end of its EA). Every
   ordinary step of calcium's ladder is inside (`ca_all_ordinary_inside`), and Ca is a metal. The
   strongest ordinary step changes from the M to the K opening between K and Ca (`rank_swap_K_Ca`).
11. **The two screening readouts.** With b = (Z − σ)²/2 and S = (h − b)/Z, exactly
   Z(S − σ) = (h − Z²/2) − σ²/2 (`readouts_identity`). With the bare hydrogenic h = Z²/2, S − σ ≤ 0
   for every Z > 0 and every σ (`readouts_control`): S can pass σ (between Al and Si) only through
   the H-like ion's binding beyond Z²/2 (the Dirac, nuclear-mass and Lamb terms).
12. **Junctions, faces and shell floors.** Equal clocks at a junction give Γ = 0 (`matched_junction`);
   the ratio comes back from the reflection, z = (1 + Γ)/(1 − Γ) (`gam_inverse`); the face apex
   Γ(√z) = tanh(r/4) returns the full ratio (`face_apex`); the bare shell floors 4, 9/4, 16/9,
   25/16, 36/25, 49/36 are all inside the wall (`shell_floors_inside`).
13. **The matched-junction rerun** (`checks/check_projector_matched_junction_v1.js`, with
   `checks/hsb/hsb_model_matched.js`, one line changed so the port-to-lattice links take their own
   clock): with exterior clocks set to 1 and each element's peel ratio kept inside the ball, the
   backward sodium-below-argon ranking closes by about 98%. All rows stay below 1/12.

## Sources

- Element and screening work: branch `claude/sm-ball-20261111`, commit `74125d2`,
  `research/2026-11-11-standard-model-ball/elements/shell_screen_04.py` and
  `SHELL_AND_SCREENING_AT_THE_WALL_20261111_v1.md`.
- Equal-face interpretation: branch `claude/moving-matrix-of-balls`, commit
  `a60a000dc41e21be6f1cca3ff9197595a3819ade`, `research/the-ball-is-the-tree`.
- Earlier wall checks at z = 5 and 7: `two-trees/lean/PeelTrees.lean` (`schottky_ratio`).
- Thresholds: NIST Atomic Spectra Database v5.12 (2024) ionization energies; electron affinities
  as listed in `gpt_batches/VOTKP_H_to_Ne_corrected_ladders.csv` (H: 0.754195 eV measured).

## The other files

- `checks/check_batch1_v1.py`, `checks/check_batch2_v1.py` and their outputs: every z, ln z and Γ
  of batches 1 and 2 recomputed from the quoted thresholds (0 mismatches in 45 steps), with the
  5/8 diagnostics, the screened-series ratios and the ball fractions.
- `gpt_batches/`: the element research batches for H–B and C–Ne and the rung-0 and ball-folder
  correction, as received (ChatGPT, run by Jeromie Beasley), with the corrected H–Ne ladder table.
  They are research inputs; their numbers are checked by the scripts above, not taken on trust.
