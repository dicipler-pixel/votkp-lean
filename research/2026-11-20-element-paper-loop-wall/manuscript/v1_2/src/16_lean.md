## Appendix A. The Lean certificates

Every exact statement in this paper that can be checked in finite rational arithmetic is checked in Lean 4.34.1, core library only — no Mathlib — in exact rational arithmetic. Running `sh run_checks.sh` in the `lean/` folder builds:

- **`LoopWall.lean` — 140 theorems.**
- **`OpeningMap.lean` — 117 theorems**, generated from the archive, covering all 433 noble-core openings and every ordinary ladder from scandium to astatine.
- **`TwoFaceForms.lean` — 3 theorems:** `two_face_identity`, `two_face_forms_agree` ($xy<(1-x)(1-y)\iff x+y<1$), `two_face_forms_split_at_midpoint` (at $t = 0.5005$ the pair $x = 0.9999$, $y = 0.0005$ gets different verdicts from the two forms).
- **`BoundaryAgreement.lean` — 11 theorems** (`witnessInterior`, `witnessTie`, `witnessProduct`, `halfScaling`, `uniqueInteriorBoundary`, `wrongThird`, `midInterior`, `midMargins`, `strictCounterexample`, `productAntitone`, `rationalThreeWayControl`): the all-threshold form of the two-face agreement.

The axiom audit prints only `propext`, `Classical.choice` and `Quot.sound` for every theorem; a source scan finds no `sorry`, `admit`, `native_decide` or `axiom`. Eleven false controls are each rejected by the compiler and also proved false inside the files: carbon's helium-core opening inside, calcium's argon-core opening outside, fluorine's anion rung outside, francium's upper end inside, magnesium's L opening outside, nitrogen's helium-core opening outside, neon's ratio exactly five, silicon's anion rung inside, $S$ above $\sigma$ with a bare hydrogen-like energy, an odd power of $\Gamma$ invariant under reversal, and the screened series outside at $Z = 7$. A further 75 named theorems across 11 self-contained research modules were replayed with the kernel checker, and the whole cross-reference hub of my work (the Work Atlas: 181 results, 80 with a linked Lean proof, across 46 repositories) updates itself from these files.

| Theorem | What it certifies |
|---|---|
| `smith_identity`, `gam_inverse` | $\Gamma = (z-1)/(z+1) = \tanh(\tfrac12\ln z)$; $z = (1+\Gamma)/(1-\Gamma)$ |
| `gam_reverse`, `power_even`, `reverse_same_side` | reversal flips $\Gamma$, keeps $\Gamma^2$ and the side of the wall |
| `wall_quadratic`, `wall_two_branches`, `outside_iff` | $\Gamma^2 = \tfrac12\iff z^2-6z+1 = 0$; both branches; outside $\iff z^2-6z+1>0$ |
| `sinh_sq_form`, `six_and_sixth` | the equal-face sinh form; $z = 6$ gives $\Gamma = 5/7$ and $z = 1/6$ gives $\Gamma = -5/7$, both with $\Gamma^2 = 25/49>\tfrac12$ |
| `hydrogenic_limit`, `two_thirds_iff`, `shell_floors_inside` | $z = 4\Rightarrow\Gamma = 3/5$; $\Gamma = 2/3\iff z = 5$; bare shell floors inside |
| `face_apex`, `matched_junction` | the quarter-log apex; equal clocks give $\Gamma = 0$ |
| `k_opening_Li` … `k_opening_Ne`, `crossing_C_N`, `neon_just_above_two_thirds` | helium-core openings; the wall lies between carbon and nitrogen |
| `l_crossing_Na_Mg`, `m_crossing_K_Ca`, `rank_swap_Mg_Al`, `rank_swap_K_Ca` | the neon- and argon-core crossings; rank swaps |
| `mg_all_inside`, `ca_all_ordinary_inside` | every ordinary step of magnesium and calcium inside |
| `oxygen_two_sides`, `rung0_Si_low`, `rung0_Si_high` | oxygen on both sides; silicon's anion rung outside across its box |
| `screened_six_outside`, `screened_seven_inside` | the screened core series crosses between $Z = 6$ and 7 |
| `readouts_identity`, `readouts_control` | $Z(S-\sigma) = (h-Z^2/2)-\sigma^2/2$ and its control |
| `gam_anion_rung`, `omega_eta_wall` | $\Gamma_0 = \eta/\chi$; the wall is $\omega = \eta$ |
| `heavy_anion_prediction` | the seven heavy-anion calls with adopted values |
| `window_silver_silicon`, `ordinary_window_nitrogen_caesium` | the two data windows |
| `francium_straddles`, `frozen_prediction_Rb_Sr` | francium's interval straddles; rubidium outside, strontium inside |
| `chi_reverse`, `chi_mirror` | the screw sign keeps under reversal and flips under a mirror |
| `dilute_bcc_fails` | a dilute band fails the one-third shell test for $f\le1/25$ |

Not certified, and marked so in the text: the dysprosium and thulium estimate-grade affinities, the promethium theory value, the samarium lower bound and the preliminary polonium value.
