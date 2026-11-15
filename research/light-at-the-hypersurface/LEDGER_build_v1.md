# Light at the Hypersurface, Mixer v1: build ledger

Jeromie Beasley, 15 November 2026. AI-assisted.

This build follows `PLAN_light_at_the_hypersurface.md`, which is included in this archive.

- **Page:** `Light_at_the_Hypersurface_Mixer_v1_20261115.html`.
- **Scripts:**

| Script | Role |
|---|---|
| `lh_math_v1.js` | Mathematics only. Also used by node. |
| `lh_app_v1.js` | The mixer. |
| `lh_build_v1.py` | Assembles the page. |
| `lh_selftest_v1.js` | Node run of K1–K18 and K14. |
| `lh_check_01.py` | Independent numpy check. |
| `lh_page_check_v1.py` | Browser checks: K14d, K19, K20. |
| `lh_shot_v1.py` | Screenshots. |

## Where the build departs from the plan, and why

1. **Push on a face (M5).**
   - The plan wrote `P_k = 2R_k(Φ_k⁺ − Φ_k⁻)/Φ_in`. In this stack the net flux `Φ_k⁺ − Φ_k⁻` is the same number in every layer: it equals `T_total`, which K6 checks. That formula would therefore give one push for every face.
   - The page instead uses the light arriving at each face from each side. Each arrival pushes with `2R`, and the two push in opposite senses: `P_k = 2R_k(Y_k|a_k⁺|² − Y_{k+1}|a_{k+1}⁻|²)/Y_0`, with the amplitudes taken at the face.
   - Graded `READING`, and as a physical pressure untested.
2. **The square carried on light (M6).**
   - The plan carried the direction by a continuous one-parameter flow through `W(τ)`. That flow has to pass through `−W` near the wall, and it reverses sense at the half-turn (trace 0). That makes the carried state jump, and K14f would fail.
   - The page instead carries the centre and one light direction round the four steps themselves, along the gold path. It multiplies in the exact `W(τ_m)` at each pass boundary `τ_m = 5m`, and starts again from the prepared direction every eighth pass.
   - The motion is continuous inside each pass. The integrated product does not depend on the frame step, and K14f holds at 2e-10.
3. **Wall crossing (review item 9).**
   - For each arm, `R` passes ½ and the face shadow passes the 45° cap ring on the same frame. In the K14 runs every one of the 13 arm crossings had both flips on one frame.
   - A pair's square changes regime at `g = sinh h_a sinh h_b = 1`. That is the same as `R = ½` only when the two steps are equal. In `breathe` and `sweep` the steps are unequal, so regime changes fall on other frames, as they should. They are listed in `lh_selftest_v1.out`.
4. **Gap tunnelling readout (eye D).**
   - The incidence used is that of the tagged ray if it returned whole; otherwise it is `θ_crit + 0.15 rad`.
   - The admittance is 1 in the centre cell and `1/z` in the gap.
   - It is a plane-parallel film of width `δ`; the faces are parallel only along their common perpendicular.
5. **Self-test K15 on the page** checks the residence formula only. The stepper is checked in node (`lh_k15_rerun.out`).

## Kill-line outcomes (the plan's lines, unchanged)

Each line that was killed is reported here. None was dropped.

### Node, `lh_selftest_v1.out`: 80 of 82 hold on the first run

K15 was killed on two lines:
- "mean residence 51": 2.35e-8.
- "network ledger": 1.91e-9.

The cause was in the test:
- 2×10⁵ summed quadrature steps.
- A half step fed the wrong source.

`lh_k15_rerun.out` reruns them under the same line, with closed-form moments and a consistent ledger: all hold (ledger 2.3e-10). A wrong residence formula is killed by the same line.

### Python, independent, `lh_check_01.out`: 40 of 42 hold on the first run

- **K6 killed (1.98).** The Python transfer matrix used the opposite time convention (e^{+iωt}), so its `r` is the complex conjugate of the page's `r`. The page follows Lean `film_is_oplus` (`x = r₁₂ e^{2iφ}`).
- **K18 killed (0.497).** The distance grid was confined to arc lengths −0.3 to 1.2, and the feet of the perpendicular lie farther out as g → 1.
- **Re-run, `lh_check_01b.out`:**
  - K6: 1.7e-15 in the same convention, and exactly the conjugate in the other.
  - K18: 4.2e-14, by minimising over both planes.
  - Both opposites (Γ ⊖ x; arccosh g²) are killed.

### Browser, `lh_page_check_v1.out`

- **K19 killed** (largest relative difference 1.29). The page's self-test values differ from node's on four lines, all in rounding noise:
  - 4.2e-15 against 5.2e-15;
  - 1.7e-13 against 2.1e-13;
  - 8.9e-15 against 3.9e-15;
  - 4.26e-14 against 4.29e-14.

  The browser is Chrome 153 V8 and node is Node 22 V8; their transcendental functions differ in the last place. All 24 pass verdicts are identical. A relative tolerance on residuals that sit at rounding level cannot hold across engines. That is a defect of this kill line, recorded here and not changed.
- **K14d killed once** (eye D at τ = 7). It could not be reproduced in three repeats, and no code path leads from the hypothesis toggle into a law readout. The re-run in `lh_page_check_v1b.out` holds: 3 repeats × 9 eyes × 3 clock values, with 1200 ms waits, and no differences. The likely cause is a readout captured between two refreshes on a 164 ms frame.
- **K20, console errors:** none in any eye at τ = 0, 7, 40. Holds.
- **K20, frame time: killed.** 164 ms per frame on the sandbox, which has no GPU and renders WebGL in software (SwiftShader). The page's own JavaScript takes 4.1 ms per frame. For reference, Balls in One Ball Mixer v2 runs at 78 ms per frame on the same sandbox, so this page costs about twice as much to render. On a machine with a GPU the frame time is expected to be set by the 4 ms of JavaScript, but that was not measured here.

## A fault found after the first page check

The full screenshot run (30 shots) raised one page error. The kit's first frame can report a slightly negative time step, so the clock started at τ = −0.057 s, and the rim eye then indexed arm −1. The first runs of `lh_page_check_v1.py` and `lh_page_check_v1b.py` happened to miss it.

Two fixes:
- The step is clamped at zero.
- The arm index uses a non-negative modulo.

After the fix the page was rebuilt, and `lh_page_check_v1.py` was run again (`lh_page_check_v1_rerun.out`), together with the screenshot set.

## Not claimed

The page says this in eye J:
- No law of motion for z(τ).
- No retardation, and no Doppler shift from a moving face.
- The admittance and `a = n²` identifications are readings.
- Γ ⊕ x with a phase is not velocity addition.
- The stack is computed only on each arm's axis.
- Off-axis rays split by flux without phases.
- `P = 2R` is untested as a physical pressure.
- Ping-pong above the wall is a numerical check; Lean covers z = 7.
- The Thomas turn is a turn of the frame, not a statement about polarisation.
- Lean was not re-run in this session.

## Originals

Nothing was written into the attachment folder or the repository clones. The two reference mixers and `feed_math.js` were copied in, read-only.
