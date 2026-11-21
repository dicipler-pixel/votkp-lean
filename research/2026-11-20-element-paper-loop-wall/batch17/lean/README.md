# Two independent frozen predictions

The archived ionization thresholds supply the ordinary helium-core opening. Ground-state electron-detachment measurements supply the extra affinity input for the anion rung. The results below refer to isolated atomic thresholds. Thermal, transport and pressure behavior require their own material evidence.

## Does the helium-core opening fall below four between gold and mercury?

**DERIVED.** At each atomic number beginning with lithium, use the last lithium-like 2s removal energy $A$ and the next helium-like 1s removal energy $B$, at ordinary step $k=Z-2$. The freeze said that the forward ratio $B/A$ first drops below the bare hydrogenic reference 4 between gold and mercury. An earlier value below four, or the absence of the predicted crossing, would defeat it.

| Element | k | Lowest ratio | Central ratio | Highest ratio | Equal-face loop wall |
|---|---:|---:|---:|---:|---|
| Gold | 77 | 4.001832223 | 4.001897840 | 4.001963460 | inside |
| Mercury | 78 | 3.997740439 | 3.997804121 | 3.997867804 | inside |

All 77 complete input rectangles from lithium through gold lie strictly above four. The six from mercury through astatine lie strictly below. Every one of the 82 adjacent pairs of shell-opening intervals is disjoint and descending. This establishes the first crossing on the archived thresholds even if each energy is varied independently inside its quoted range. Many high-ion energies come from theory. Both ordinary steps in the table remain inside the equal-face wall; the number four is the separate bare-shell comparison. Gold’s anion rung is also inside the wall, with an entire ratio interval below four at [3.996097269, 3.996204593], even though gold's helium-core opening remains above four. These are two distinct observations in one element. [Prior frozen prediction](../../holdouts/k_opening/PROTOCOL.md)

**DERIVED — grading the curves separately.** Both frozen extrapolations pick the correct crossing bracket. Comparing their numerical values with the full test set gives a sharper result. For every one of the 15 targets from lutetium through astatine, the entire threshold-ratio interval lies on the linear forecast’s side of the midpoint between the two models. Consequently the linear forecast is strictly closer than the point-Coulomb-plus-$1/Z$ estimate for every allowed realization. This remains true even if each printed nine-decimal model value varies by half its last displayed unit. Only the linear predictions for lutetium and mercury lie inside the threshold boxes. For gold, the linear value 4.001830827 is just below the lower threshold-box edge 4.001832223. All 15 of the spinor-plus-empirical-correction values lie outside their threshold boxes. These comparisons grade the two specified extrapolations, including their calibration; they do not test the underlying Dirac equation. [Frozen model values](../../holdouts/k_opening/predictions.csv)

## Seven primary heavy-anion tests and one preliminary report

**DERIVED.** The eight signed calls were recorded before these batches and were informed by prior chemistry knowledge. The primary score uses each accepted ground-state affinity and the neutral ionization threshold from the pin. Independent positive input widths $A\pm u$ and $B\pm v$ give the ratio interval $[(B-v)/(A+u),(B+v)/(A-u)]$. The kernel propagates the two-sided squared reflection itself at every admitted input. A complete box on the other side of the wall would defeat that forecast. A missing full source uncertainty stays open.

| Atom | Forecast | Accepted affinity in eV | Ratio interval | Primary outcome |
|---|---|---:|---|---|
| Osmium | outside | 1.077661(24) | 7.829774–7.830494 | outside |
| Iridium | inside | 1.564057(11) | 5.732999–5.733361 | inside |
| Platinum | inside | 2.12510(5) | 4.215575–4.215868 | inside |
| Gold | inside | 2.30861(3) | 3.996097–3.996205 | inside |
| Lead | outside | 0.356721(2), $^{208}$Pb | 20.791144–20.791381 | outside |
| Bismuth | outside | 0.942362(13) | 7.731009–7.731235 | outside |
| Polonium | outside | preliminary; full uncertainty pending | — | unresolved |
| Astatine | inside | 2.41578(7) | 3.856792–3.857081 | inside |

All seven supported outcomes hold throughout their quoted rectangles. Each rectangle also preserves every cutoff in the earlier silver–silicon central window. Thus these seven tests support the forecasts while leaving the earlier numerical ambiguity in the classifier cutoff intact. Thallium’s complete box is outside and mercury has no adopted bound-ground-state point; neither was one of the eight forecasts. For each scored case the certificate also checks the Pearson finite-difference identity and the corresponding electrophilicity comparison. [Frozen scoring rule](../../holdouts/heavy_anions_protocol.md) · [Batch 16 source identities, dates and uncertainties](../../batch16/ladder/affinities.csv) · [Batch 17 source identities, dates and uncertainties](../ladder/affinities.csv)

**POLONIUM — SOURCE-CONDITIONAL.** The preliminary $^{210}$Po JyvIS number is 11905.631(9) cm⁻¹. The full systematic uncertainty is outstanding. Using only the displayed statistical digits gives a conditional ratio box [5.702866977, 5.702881018], inside. Taking the entire displayed 11800–11950 cm⁻¹ plot span as an assumed input interval gives [5.681697171, 5.753927603], also inside. The plot span is an explicit scenario, not a coverage interval. Both outcomes run contrary to the frozen outside prediction; neither supplies a primary experimental verdict.

With the archived neutral threshold $8.418070\pm0.000004$ eV and the exact SI conversion $1\;\mathrm{cm}^{-1}=(6621486190496429/53405887800000000000)$ eV, the critical wavenumber is
$\tilde\nu_*=IE_1(3-2\sqrt2)/(hc)$. The entire IE uncertainty puts it strictly between 11649.160 and 11649.172 cm⁻¹. At the lower test wavenumber every admitted IE gives outside; at the upper every admitted IE gives inside. The reported central reading would have to move down by more than 256.459 cm⁻¹ to reach the wall under this IE model. This difference quantifies the required shift and makes no assumption about the size of the unreported systematic error. [Preliminary 2026 workshop report](https://indico.global/event/16399/contributions/141980/attachments/66656/128992/Po_CRIS_2026.pdf)

## Reproduction

From the repository root with Lean 4.34.1 and Python 3:

```sh
p=research/2026-11-20-element-paper-loop-wall
python3 "$p/batch17/lean/verify.py" --lean /path/to/lean
```

The script compares printed primary energy and reflection fields to archive plus affinity sources, checks all 83 emitted shell rows and runs four false claims. The Lean bounds quantify over rational realizations of the supplied energy intervals. The first-crossing certificate grades the bracket. The separate forecast scores retain the pointwise residuals of both extrapolation models.
