# Element paper: the loop wall (H to Ne)

Jeromie Beasley · 20 November 2026 · VOTKP element work, first two batches (Z = 1 to 10)

This folder holds the Lean formalization of the loop wall and the hydrogen-to-neon element
certificates, the arithmetic checks of the two element batches, and the research batches they
check. It is kept for the element paper.

## What is proved (`lean/LoopWall.lean` and `lean/OpeningMap.lean`, core Lean 4.34.1, no Mathlib, exact `Rat` arithmetic)

101 theorems in `LoopWall.lean` and 72 in `OpeningMap.lean`. Axioms: only `propext`, `Classical.choice`, `Quot.sound`. No `sorry`, `admit`,
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
   exactly 5, the screened Z = 7 outside, Γ² odd, francium's upper end inside, Mg's L opening outside, Si's rung 0 inside, Ca's M opening outside, S above σ with a
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
14. **The noble-core opening map** (`lean/OpeningMap.lean`, generated from the archive by
   `checks/gen_opening_map_lean.py`): every opening ratio in `data/element_thresholds_20261011.json.gz`
   behind a He, Ne, Ar, Kr, Xe or Rn core, 433 in all, each certified on its side of the wall.
   Outside: Li, Be, B, C (He core); Na (Ne); K (Ar); Rb (Kr); Cs (Xe). Everything else is inside.
   After its first element, each of the Ne, Ar, Kr and Xe sequences is inside at once.
   The frozen Rb/Sr prediction holds (`frozen_prediction_Rb_Sr`). Francium's encoded central ratio
   is inside, but its input interval straddles the wall (`francium_straddles`). Every ordinary step
   of Sc, Ti, V, Cr and Mn (110 steps) is inside (`ladder_*_all_inside`), and the anion rungs of
   Sc, Ti, V, Cr, Fe, Co, Ni and Cu are outside (`rung0_Sc` to `rung0_Cu`; Mn and Zn have no bound
   ground-state anion). The ladders of Fe, Co, Ni, Cu and Zn are certified inside as well, so every
   ordinary step from Sc to Zn is inside. Across H to Zn the only outside steps are the anion rungs
   and the core openings Li, Be, B, C, Na and K.
15. **Batch 6, Fe to Zn, the junction cutoff and the β-Mn screw.** The model's 1/12 cutoff is
   (1/4)/3, a third of the largest per-link share in a half-filled chain. The sum rule
   Σ_j ‖P_ij‖² = Tr(C_i − C_i²) carries it to any lattice as X > B/(3n): the nearest shell holds more
   than a third of the site's shared weight. A half-filled bcc band passes; a dilute band fails for
   every filling f ≤ 1/25 (`dilute_bcc_fails`); a filled gapped band passes. So the third reads
   shell concentration, not conduction by itself. β-Mn's screw (¼−y, x−¼, z+¼), a = 6.3145 Å, gives
   χ = (d₀×d₁)·d₂ = +9.9306 Å³; χ is unchanged by reversing the path (`chi_reverse`) and flips under a
   mirror (`chi_mirror`), the opposite of Γ.

16. **Batch 7, gallium to bromine** (`gpt_batches/batch7_Ga_to_Br.md`, checked by
   `checks/check_batch7_v1.py`): 165 energies match the archive and all 160 ordinary z, Γ pairs
   match, recomputed from the archive itself. Every ordinary step is inside (`ladder_Ga_all_inside`
   to `ladder_Br_all_inside`). The anion rung is outside for gallium, germanium and arsenic and inside
   for selenium and bromine (`rung0_Ga` to `rung0_Br`). Arsenic uses the 2025 affinity 0.804486 eV and
   selenium the 2026 value 2.020667 eV; both are also certified at the older values, so neither
   revision moves a call. Trigonal selenium (P3₁21, COD 1534711) gives a screw sign
   χ = +11.1638 Å³ that is unchanged by reversing the path and flips under a mirror
   (`checks/check_se_screw_v1.py`), the same law as β-manganese.
17. **Batch 8, krypton to zirconium** (`batch8/`, checked again by `checks/check_batch8_v1.py`):
   190 energies and 185 ordinary pairs match the archive. The only outside steps are the anion rungs
   of rubidium, strontium, yttrium and zirconium (`rung0_Rb` to `rung0_Zr`; krypton has no bound
   anion) and rubidium's krypton-core opening. Every other ordinary step is inside
   (`ladder_Kr_all_inside` to `ladder_Zr_all_inside`; the rubidium theorem leaves out only its
   core opening, certified in `coreKr_outside`). Review exchange: `CLAUDE_REVIEW.md`.

## The page

`VOTKP_Element_Paper_Loop_Wall_v1_20261121.html` is the readable breakdown of all of the above, H to Zn.
It is built by `html/build_element_paper_html_v1.py` from the archive and the Lean files
(`python3 html/build_element_paper_html_v1.py ../../data/element_thresholds_20261011.json.gz lean OUT html/element_paper_template_v1.html`);
every table and the opening-map figure are computed, none typed.

## Sources

- Element and screening work: branch `claude/sm-ball-20261111`, commit `74125d2`,
  `research/2026-11-11-standard-model-ball/elements/shell_screen_04.py` and
  `SHELL_AND_SCREENING_AT_THE_WALL_20261111_v1.md`.
- Equal-face interpretation: branch `claude/moving-matrix-of-balls`, commit
  `a60a000dc41e21be6f1cca3ff9197595a3819ade`, `research/the-ball-is-the-tree`.
- Earlier wall checks at z = 5 and 7: `two-trees/lean/PeelTrees.lean` (`schottky_ratio`).
- Thresholds: NIST Atomic Spectra Database v5.12 (2024) ionization energies; electron affinities
  as listed in `gpt_batches/VOTKP_H_to_Ne_corrected_ladders.csv` (H: 0.754195 eV measured).

## The Sc–Mn table

The batch-5 research table as received has three energies that differ from the archive (V k=11:
254.8 eV; Cr k=9: 209.5 eV; Cr k=20: 1495.1 eV) and five displayed z, Γ pairs that are wrong:
V k=10 (1.10542, .05007), Cr k=8 (1.13390, .06275), k=17 (1.08990, .04302), k=19 (1.07214, .03481),
k=20 (1.09297, .04442); V k=14 is a rounding difference only (977.2/896 = 1.090625).
`checks/check_batch5_v1_output.txt` is the raw comparison against the printed table, so it also
flags rows whose ratio was right but whose energy text was mistyped. Use
`checks/batch5_corrected.csv`, rebuilt from the archive. No wall classification changes, and the
Lean certificates were built from the archive, not from the printed table.

## The Fe–Zn table

The batch-6 research table as received has two energies that differ from the archive (Ni k=21:
1750 eV, archive 1758.0; Cu k=5: 79.5 eV, archive 79.8) and four displayed z, Γ pairs that are wrong:
Ni k=15 (archive 1.070441, .034022), k=20 (1.068044, .032902), k=21 (1.069397, .033535),
k=22 (1.068138, .032947). (The first version of this note gave k=20 and k=21 from the mistyped
1750 eV; the corrected values above, and `checks/batch6_corrected.csv`, use the archive's 1758.0 eV.) The Cu k=4 and k=5 ratios are right; only the energy text is mistyped.
The table's "140/140 matched the archive" line is therefore not right. Use
`checks/batch6_corrected.csv`, rebuilt from the archive. No wall classification changes. The
corrected Sc–Mn CSV sent with batch 6 agrees with `checks/batch5_corrected.csv` (V k=14 differs by
rounding only).

## The other files

- `checks/check_batch1_v1.py`, `checks/check_batch2_v1.py` and their outputs: every z, ln z and Γ
  of batches 1 and 2 recomputed from the quoted thresholds (0 mismatches in 45 steps), with the
  5/8 diagnostics, the screened-series ratios and the ball fractions.
- `gpt_batches/`: the element research batches for H–B and C–Ne and the rung-0 and ball-folder
  correction, as received (ChatGPT, run by Jeromie Beasley), with the corrected H–Ne ladder table.
  They are research inputs; their numbers are checked by the scripts above, not taken on trust.
