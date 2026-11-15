# Review of Light at the Hypersurface, Mixer v1

Reviewer: plan author. 15 Nov 2026. No build file was edited.

Read for this review: `lh_app_v1.js` in full; `lh_math_v1.js` (feed, advance, audit, ray tracing, stack, split); `lh_build_v1.py`; `killlines.txt`; every `.out` file; `LEDGER_build_v1.md`; the contact sheet and six single screenshots (C at 7, E at 7, G at 20 sweep, H at 7, I at 7, J at 40). The other 28 screenshots were seen only at contact-sheet size or not at all.

## Verdict

The mathematics, the single feed, the single object and the checks are sound. The page is not ready to hand over until the six must-fix items below are done. Five are wording or chip items; one is camera framing.

## Section 9 checklist

| # | Item | Result |
|---|---|---|
| 1 | One object | Holds. One `WORLD` group, added to the stage once in the first `make`; each eye only sets emphasis weights and a view. `update(dt)` runs every component in every eye. `CLOCK.tau` is the app's own and is not reset by the kit's `show`. |
| 2 | One feed | Holds. `rOf(P, a, tau)` is the only source of a step rapidity. It is called from `feed`, and from `pushAt` and `feedLite`, which are mid-step evaluations for the integrator. The app never computes `z`, `r` or `Γ` itself. |
| 3 | Kill lines unchanged | Holds. `killlines.txt` and both script headers match plan section 7. Two statements were run in a relative form where the plan wrote an absolute one (K3, K8 trace formula); both are said in the output lines. |
| 4 | Independence | Holds. `lh_check_01.py` imports numpy, json and math only. K3 recomputes the angles from the dumped tangents and also checks that each hit lies on its face. |
| 5 | Outputs | One gap: K13's "FEED-LOOP-03 P1, P2, P3 re-run unchanged" was not run in any script. See must-fix 1. K14 and K15 exist in node only, which the plan allowed. |
| 6 | Chips | All 27 Lean names in the chips exist as theorems at the files the plan cites (grep against `gh/`). No hypothesis item carries a law chip. Two chip faults: must-fix 1 and 2. |
| 7 | Words | Byline correct, AI-assisted line present, no bar graphs, no second sphere, no cosmology framing. Three wording faults: must-fix 3, 4, 5. |
| 8 | Section 6 on the page | Ten of the seventeen items are in eye J. One that the brief named is missing: must-fix 5. |
| 9 | Wall crossing | The builder is right and my item was wrong for unequal steps. Each arm's `R = ½` and its face shadow passing the cap ring fall on the same frame (13 of 13 crossings). A pair's square changes regime at `g = 1`, which is the wall only for equal steps. This makes the eye G text wrong as written: must-fix 4. |
| 10 | Picture | Rays bend and split as they should and the tagged ray is distinct. The total-return ring and window are drawn. Framing fault: must-fix 6. |
| 11 | Originals | Untouched. Attachment timestamps are unchanged, nothing in `gh/` is newer than the build, and the three.js and kit blocks in the page are byte-identical to Balls mixer v2. |

## The builder's departures from the plan

- **Push on a face.** Accepted. My formula does give one number for every face, since the net flux is the same in every layer. The arriving-flux form is the right repair and is graded `READING`.
- **Carried square by exact pass products.** Accepted. It is exact, independent of frame step, and avoids the sense flip.
- **Regime change at `g = 1`.** Accepted; see item 9.
- **K19 killed.** The fault is in my kill line: a relative comparison of residuals that sit at rounding level cannot hold across two engines. All 24 verdicts agree. For v2 the line should read "same verdict on every line, and both values within tolerance".
- **K20 frame time killed.** Not decidable on this sandbox (software WebGL). The page's own JavaScript is 4.2 ms a frame. Frame rate on a real laptop GPU is untested and should be said so to Jeromie.
- **K14d killed once, then held in 81 comparisons.** The cause is not established; "a readout captured between two refreshes" is a likely explanation, not a shown one. The code has no path from the toggle to a law readout, which I confirmed by reading it. Keep it in the ledger as unexplained once.
- **K6 and K18 in Python.** Both first-run kills were faults of the test (phase convention; search window), and both re-runs include the opposite, which is killed. Accepted.
- **K15.** First-run kills were quadrature and a mis-fed half step in the test. The re-run holds at 2.3e-10 under the same line. Accepted.

## Must fix

1. **Eye F chip `CHECKED · FEED-LOOP-03 P1–P3` is not backed by a run in this build.** Either re-run P1, P2 and P3 at their own tolerances and add the lines to the output, or change the chip to cite the 12 Nov run by name and record in the ledger that K13's second half was not run.
2. **Eye F states the tilted-plane pressure without its condition or its grade.** "On a plane tilted by θ with u cos²θ" holds for a transverse wave with `|E| = |H|`, and it is a numerical check (K13, 3e-15), not the Lean theorem. Add the condition to the equation block and a `CHECKED · 1e-12` chip for it; the Lean chip covers the untilted front only.
3. **Eye I speaks of Jeromie in the third person on his own page.** "Hypothesis, the author's picture", "his Snell's law" and the section line "his picture, drawn on the same object" should be first-person-neutral: for example "Hypothesis: light is trapped between layers … ; this is Snell's law and the Pauli principle at the hypersurface."
4. **Eye G text is wrong for unequal steps.** "Below the wall it turns … at the wall it locks; past the wall it runs" should be stated in `g`: turns while `g < 1`, locks at `g = 1`, runs for `g > 1`, and `g = 1` is the wall only when the two steps are equal. The same eye's readout already uses `g`.
5. **Eye J's not-claimed list omits an item the brief named.** Add: the `R sin²θ` form of the refraction law came from an earlier model, and Lean covers its algebra, not the path integration. Eye C shows `CARD · B30 (theorem)` beside two Lean chips, so without this sentence the chips read stronger than they are. Add in the same place that the Poincaré metric is not formalised in Lean (only `(1 + Γ)/(1 − Γ) = z`) and that `R sin²θ` is not identified with the projector distance (B4 is a conjecture).
6. **The ball is cut off in several eyes.** In E and I at 1500×900 the ball runs off the top and right of the canvas, the control strip covers ball K and its label, and "rim: the ground" is clipped to "the ground". B and F look the same at contact-sheet size. Raise the view distance for B, C, D, E, F and I (about 8.2, as A uses) or lower the view target, and re-shoot.

## Suggestions

1. **Readouts are below the fold.** At 900 px height the long text and sliders push most readout rows out of view in every eye; the numbers are the point of each eye. Put the readout above the sliders, or shorten the texts.
2. **Faint hypothesis labels in law eyes.** At 0.2 emphasis the two amber labels are visible but unreadable and overlap the rim. Hide the labels when the weight is below about 0.5.
3. **Hypothesis markers read cream, not amber.** Additive blending washes them out in eye I. A more saturated amber, or normal blending for that layer, would keep the law and hypothesis layers apart at a glance.
4. **Nine rays is thin for the quality bar.** The plan asked for a dense fan and a density control. With JavaScript at 4 ms a frame there is room for about 24 rays and a `Density` slider.
5. **Corner frames in eye G are small.** The solid and dashed frames that show the Thomas turn are hard to find in the sweep screenshot. Lengthen them and move the camera toward that corner.
6. **Self-test button placement and detail.** The plan put it in the sticky strip; it is only in eye J. Showing the list of lines, not only the count, would make a failure readable.
7. **Dropped flux is not ledgered.** Ray children below the 1e-3 cut or beyond six faces are not drawn. Add one ledger row with the total flux not drawn.
8. **Small wording.** "dies away" → "decays" (eye D). "the regime label `locks`" needs a tolerance; with exact equality it can never show. The dead condition `|| true` in `eye().step` can go.
9. **"rim: the ground" sits in the law layer.** It is inherited from Balls mixer v2, so I leave it, but the plan lists the ground reading as hypothesis; the label could move to the hypothesis layer.
10. **Page check robustness.** Compare `__lh.S` and `__lh.AUD` values, not panel text, so a refresh in mid-capture cannot produce a false difference.
