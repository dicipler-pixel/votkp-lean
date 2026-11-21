# Two Trees in One Ball (v4): the loop wall, read in full

Seed file: `/home/claude/atlas/seed/two_trees.json`. It has 76 entries covering every numbered result in the paper, plus the unnumbered results that carry content. 22 entries are tagged `loop-wall`, and 39 have a Lean theorem. Every Lean name in the file, whether in a `lean` field or cited in a statement, was checked against the `.lean` source on its branch. All six Lean files compile cleanly here with core Lean 4.34.1.

## Which version

- The newest version is **v4, 30 October 2026** (Zenodo 10.5281/zenodo.23847114). I searched Drive for every title containing "Two Trees" or "Two_Trees" and found no v5 and no later rebuild.
  - The v4 HTML on Drive (`Two_Trees_in_One_Ball_v4_20261030.html`, 2,694,237 bytes) is the same size as `two-trees/paper/Two_Trees_in_One_Ball_v4.html` in the repo.
  - "Two Trees, One Scale.html" (10 Nov) is a different piece and was not read.
- The `two-trees/` folder is byte-identical (same git blobs) on `main` and on all nine other branches, with one exception:
  - `lg2-3-gaps` (commit 7cd4c4e, 21 Nov 2026) adds `two-trees/lean/PeelTrees5.lean`. This is a post-v4 Lean statement of the Theorem 8.6 band criterion over the rationals. It also rewrites `controls/Controls4.lean` to hold only the false controls.
- Seed entries point to branch `main`, except `band_criterion`, which points to `lg2-3-gaps`.
- The existing atlas entry `two-trees.schottky-5-7` pointed at `claude/sm-ball-20261111`. I kept the id and moved it to `main`; the blob is the same.

## The wall forms that appear, where, and how each is derived

The wall is Γ² = ½, with Γ = (z − 1)/(z + 1) = tanh h and h = ½ ln z.

1. **Γ² = ½ and z = 3 + 2√2 = 5.828427** (§5.2, Theorem 5.3)
   - Derived by ping-pong on half-spaces. The planes about orthogonal axes are disjoint exactly when the distance is at least ln(1 + √2).
   - A boost of rapidity r carries the outside of the −u half-space into the +u one exactly when r ≥ 2 ln(1 + √2), that is, z ≥ (1 + √2)² = 3 + 2√2.
   - Then Γ(3 + 2√2) = 1/√2.
   - Grade: proved in the paper (the ping-pong lemma itself is prior art).
2. **Angle of parallelism 45°** (§5.2 proof; §5.2 note on the v2 report; PingPong7.lean)
   - In the proof of Theorem 5.3 the boundary circles have angular radius π/4 at the threshold and just touch there.
   - The v2 report gives Dirichlet caps with cos α = Γ. That gives α = 45° at Γ = 1/√2, but the paper never writes this out.
   - In Lean, `PingPong7.lean` defines the caps as t² < 2·comp², which is angular radius exactly 45°. It proves them disjoint (`caps_disjoint`) and proves the inclusion at ratio 7 (`pingpong_step`).
   - So the 45° cap geometry is in Lean, but only paired with the ratio-7 step.
3. **tr[A, B] = −2** (§5.3, after Theorem 5.4; Figure 4)
   - Stated formula: tr[A, B] = 2 − 4 sinh⁴(r/2) in PSL(2, ℝ), with sinh²(r/2) = (z − 1)²/(4z).
   - The commutator is a rotation below the wall, parabolic (trace −2) at z = 3 + 2√2, and a boost above.
   - Grade: computed. The paper gives it exactly at nine sample ratios, and the q1_commutator script prints tr = −2.0 at 3 + 2√2.
   - The Lean part is the ratio-5 exact data (`comm5_trace`, `comm5_fixes_p`) and the ratio-7 trace (`comm7_trace`). There is no Lean formula valid for every z.
4. **sinh h = 1** (same place)
   - With r/2 = h, the rotation condition sinh(r/2) < 1 is the wall written as sinh h = 1.
   - It also appears on the knot side: sinh x < 1 ⇔ tanh² x < ½ (§8.5).
5. **sinh a · sinh b = 1 and Γ_a² + Γ_b² = 1**
   - Not in Two Trees with unequal faces. Every use has two equal steps (a = b = r/2), so the paper only meets the equal-face case sinh² h = 1, Γ² = ½.
   - In the JSON this is linked to `wall.two-faces` as `special-case`.
6. **|Γ|² = ½**
   - The paper's Γ is real, so this appears only as Γ² = ½.
7. **Knot side** (§8.5, Theorem 8.6)
   - From 4k = (s − 1/s)⁴ − (2v − (s − 1/s)²)², the quantity k = 2 − tr[a, b] is at most 4 sinh⁴ x.
   - So below Γ² = tanh² x = ½, crossing meridian axes always give a rotating commutator. The wall in meridian length is 2 ln(1 + √2).
   - The census (§8.5) finds that every knot that turns does so before x = 0.73, below the wall at x = 0.8814.

Arithmetic I added (checked symbolically here; the paper does not state these, and the JSON marks them that way):

- At the wall the Thomas angle has tan(θ/2) = ½, so cos θ = 3/5 and sin θ = 4/5: the (3, 4, 5) triple.
- At the wall the boost entries are cosh ln z = 3 and sinh ln z = 2√2.
- At the wall the v2 constant cosh δ = sinh²(ℓ/2) equals 1, so δ = 0: the orthogonal planes touch.

## What is proved and what is only stated, for the five items named in the brief

| Item | What the paper claims | What Lean proves |
|---|---|---|
| Schottky exactly above Γ² = ½ | Theorem 5.3: proof written in the paper | **Only two numeric inequalities:** `schottky_five_below` (Γ(5)² < ½), `schottky_seven_above` (½ < Γ(7)²), `schottky_ratio` ((5−3)² < 8 < (7−3)²). Nothing general, and nothing in Lean says "Schottky" or "discrete". The earlier check is confirmed. |
| Ping-pong at ln 7 | §8.3 | `PingPong7.lean`: the 45° caps are disjoint, the inclusion holds at ratio 7 (with the sum-of-squares certificate `plane_core`), the abstract `pingpong` lemma, and freeness (`word_ne_id`). This proves freeness by ping-pong at z = 7 only. Discreteness is not stated. |
| Free of rank 3 for z ≥ 2 | Corollary 8.2: every whole number z ≥ 2 | **Lean for every z ≥ 2 that is not a power of 2** (`free_not_pow_two`, from `free_general`), and separately at 5 and 7 (`free5`, `free7`). The even ratios, which include the powers of 2, rest on Theorem 8.1: a written proof checked on 100,000 points, **not in Lean**. Lean proves "no non-backtracking word is the identity"; the bridge to Mathlib's `FreeGroup.lift` is not written. |
| Thomas rotation tan(θ/2) = Γ² | Theorem 4.7 (formula is prior art: Rhodes–Semon, Ungar) | **Lean for every rational ratio z > 0:** `thomas_rat` (B_i B_j = L R, with R written in t = Γ(z)²), `thomas_half_angle_t` (sin/(1 + cos) = t), plus integer forms for symbolic z. Exact at 5 and 7 (`thomas5`, `thomas7`, `thomas_half_angle`). Real, irrational z is outside core Lean. The paper does not evaluate it at the wall. |
| Knot meridian commutator tr[a,b] = 2 − v((s − 1/s)² − v) | Theorem 8.6 | **Lean as an identity over any commutative ring:** `comm_trace`, `comm_trace_ab`, `band_k`, `band_bound`, `band_peak`. The inequality k ≤ 4 sinh⁴ x and the wall conclusion are in the paper only. `band_bound` is the algebraic identity, not the inequality. Post-v4, `PeelTrees5.band_criterion` (branch `lg2-3-gaps`) proves the equivalence \|tr\| < 2 ⇔ 0 < v(...) < 4 over ℚ, still without the step sinh x < 1. |
| Peel boosts of length ln 5 | §2 and §4 | Lean: `peel_ladder` (Γ_L = (5^L − 1)/(5^L + 1) for every L), `gam_mul`, `cosh_from_gam` / `sinh_from_gam`, `lorentz5`, `inverse5`. The length ln 5 itself (d = 2 artanh Γ) is proved in the paper; core Lean has no logarithms. |

## Things the hub should know

- **README and CLAIMS do not match the Lean on some points:**
  - `two-trees/README.md` grades Theorem 8.6 as "Lean". In fact the "below Γ² = ½ always does" half is proved in the paper; Lean has the identity.
  - The README's "Schottky … proved; inequalities in Lean" is accurate.
  - The CLAIMS.md printed in Appendix A.4 still says "Theorem 5.1 for a general ratio z: in Lean only for z = 5 and 7". That is out of date, because `PeelTrees2.lean` proves it for every z that is not a power of 2.
- **A computed oddity in Appendix B, not used by the paper:**
  - q1_pp_powers.txt reports that the numerical cap search found no valid configuration for B_u³ at z = 5. That is ratio 125, which is far above the wall, and the search margin there was −1.03.
  - The paper only claims the squares. This looks like an optimiser failure rather than a counterexample, but it has not been looked into.
- **Mathlib drafts:**
  - Appendix A.4 (TwoTrees/Smith.lean and Riley.lean, 24 theorems) is "written, awaiting CI" and has never been built. That includes `TwoTrees.Smith.smith_identity`.
  - The only copy in the repo is under `research/2026-11-12-november-gather/.../Two_Trees_v3_Lean_files.zip/`.
  - No seed entry uses those names as a Lean proof.
- **Theorem count:** 159 theorems in five core files, as the paper says (74 + 49 + 7 + 12 + 17). The controls are 3 + 3 false statements. `controls/Controls4.lean` on `main` also re-proves the 12 true PeelTrees4 lemmas, so a naive count gives 15 there.

## Local checks run for this hub

- With `/opt/lean/lean-4.34.1-linux/bin/lean`, each file exited 0 with no messages:
  - PeelTrees (39 s), PeelTrees2 (17 s), PeelTrees3 (14 s), PeelTrees4, PingPong7, and PeelTrees5 from `lg2-3-gaps`.
- `#print axioms` was run for the theorems that touch the wall:
  - All stay within `propext`, `Classical.choice` and `Quot.sound`.
  - `schottky_ratio` and `thomas_half_angle` use no axioms.
  - `free5` uses `propext` and `Quot.sound` only.
- No `sorry`, `native_decide` or `axiom` declarations appear in the code. The only matches for those words are in header comments.
- Every non-blank line of the five repo Lean files appears verbatim in the paper's Appendix A, so the paper's Lean and the repo's Lean are the same.
- Sympy confirmed that at z = 3 + 2√2: Γ² = ½, sinh h = 1, 2 − 4 sinh⁴(r/2) = −2, cos θ = 3/5, sin θ = 4/5, cosh δ = 1, and arccos Γ = π/4.

## Files read

| File | Read in full? |
|---|---|
| `two-trees/paper/Two_Trees_in_One_Ball_v4.html` (as text): title, abstract, §1–§9, references | Yes |
| Same HTML: Appendix A (run logs, axiom audits, false controls, CLAIMS.md, Mathlib draft listings) | Yes for the logs, audits, controls and CLAIMS. The Lean sources were read from the repo files, which match the appendix line for line. The Mathlib draft sources (Smith.lean, Riley.lean, lakefile) were not read line by line; their CLAIMS rows were. |
| Same HTML: Appendix B (scripts and outputs, about 3,800 lines) | **No, partly.** I read the section index, KILL_CONDITIONS.txt, q1_commutator.py and its output, and the q1_pp_* ping-pong outputs, and searched the whole appendix for wall terms. I did not read the other scripts line by line. |
| `two-trees/paper/Two_Trees_in_One_Ball_v4.pdf` | Not opened. The HTML is the same text. |
| `two-trees/lean/PeelTrees.lean` (525 lines) | Yes |
| `two-trees/lean/PeelTrees2.lean` (551 lines) | Yes |
| `two-trees/lean/PeelTrees3.lean` (97 lines) | Yes |
| `two-trees/lean/PeelTrees4.lean` (114 lines) | Yes |
| `two-trees/lean/PingPong7.lean` (256 lines) | Yes |
| `two-trees/lean/controls/Controls1.lean`, `Controls4.lean` (main) | Yes (Controls4 skimmed past the repeated true lemmas, which match PeelTrees4) |
| `two-trees/lean/PeelTrees5.lean` and `controls/Controls4.lean` on `lg2-3-gaps` | Yes |
| `two-trees/README.md` | Yes |
| `/home/claude/atlas/atlas.json` (existing entry ids, for links) | Entry list and the five related entries only |
| Drive: Two Trees title search results | Metadata only. Content not opened, because the v4 file matches the repo copy. |

No writes were made to GitHub or Drive.
