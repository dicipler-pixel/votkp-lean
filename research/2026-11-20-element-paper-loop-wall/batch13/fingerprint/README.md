# The frozen fingerprint finds 14 of 24 xenon-family positions

**HYPOTHESIS tested.** The previous three noble-core families gave 72/72 correct positions with a fixed feature: the first log-step share minus the second. Before opening the xenon-family score, the batch 9 analysis had specified the three offsets, eight initial charges, primary feature and decision boundaries. Commit 4f55424 recorded the execution protocol. One wrong position defeats perfect transfer. [Original hypothesis](../../batch9/fingerprint/FINGERPRINT.md) · [test protocol](PROTOCOL.md)

**DERIVED — held-out results.** On the 24 xenon-family central values, the frozen contrast found 14 positions. All 10 misses were assigned zero extra electrons. Every 54-electron case scored correctly on its central values, but only four of the eight 55-electron cases and two of the eight 56-electron cases did. There was no retraining. These overlapping windows come from ten elements. They are correlated observations.

| Actual extra electrons | Predicted 0 | Predicted 1 | Predicted 2 |
|---|---:|---:|---:|
| 0 | 8 | 0 | 0 |
| 1 | 4 | 4 | 0 |
| 2 | 6 | 0 | 2 |

**DERIVED — three misses survive the entire reported input boxes.** Cerium²⁺, praseodymium³⁺ and neodymium⁴⁺ each start with 56 electrons. No allowed combination in their five reported threshold intervals puts them in class 2. Eleven of the 24 windows remain correct across their full boxes, and ten admit both the actual class and at least one other. The endpoints vary independently within each window; correlations or defects in the archived level estimates can change the uncertainty assessment. The original training means were fixed at their central values. [All 24 rows and grades](xenon_predictions.csv)

**DERIVED — the clearest miss.** For cerium²⁺ the five successive removal energies are 20.1974, 36.906, 65.55, 77.6 and 91.0 eV in the pin. The first two ratios are both large by comparison with the later two. The first-two contrast is ln[36.906²/(20.1974·65.55)] / ln(91.0/20.1974) = +0.0188541. Class 2 requires a value below −0.1639453. Its entire permitted range is +0.01569 to +0.02212. ASD assigns 4f² → 4f → closed 5p⁶ to the first three ionic ground configurations in this cerium window. It is possible for an identifiable closed core to have this profile. A claim about the 4f change causing every miss would go beyond the test. [ASD configurations and input grades](../../batch12/ladder/asd_states_20261121.csv)

**RECOGNISED — what the vector retained.** Keeping all four ordered shares scored 15/24, recovering the cerium²⁺ case. The endpoint alone scored 10/24; sorted shares and the first two shares each scored 14/24. The 72/72 result for the original three core families still stands. The proposed perfect transfer failed on the fourth. Near the start of the lanthanides, “first two shares look similar” ceases to distinguish starting on 54 electrons from starting above it. These results grade the fixed shell-position classifier; the separate exact loop-wall identity has no classifier in its hypotheses.

**DERIVED — interval method.** Write xᵢ=ln Eᵢ. The contrast numerator is 2x₂−x₁−x₃ and its denominator is Σ|xᵢ₊₁−xᵢ|. On each fixed-order chamber the ratio is linear-fractional with positive denominator. Its extrema occur at vertices. Each block of equal adjacent coordinates at a vertex must be pinned to at least one original interval endpoint, since otherwise the entire block can move. Enumerating all endpoint values that lie within each input interval therefore includes every extremizing vertex. We evaluate the logarithms with 48-digit decimal arithmetic and publish rounded values; this is a numerical interval audit. [Scoring and box script](test_xenon_transfer.py) · [captured run](score.txt)
