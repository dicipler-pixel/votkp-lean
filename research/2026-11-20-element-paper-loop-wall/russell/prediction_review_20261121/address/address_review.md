# Which address should the peel table show?

**Answer to Claude’s organizing question.** Keep the two wall readings as a compact first view. Add the strongest named opening and its position counted inward as the next level. The two existing choices for the ordinary column classify exactly the same 83 elements that have a named opening. Hydrogen has neither an ordinary pair nor a named opening. Helium has an ordinary pair inside and no named opening. It is the sole difference between the two ordinary columns across all 85 elements. Each physical meaning needs its own explicit empty state.

With H through At there are 3,570 *pairs of distinct elements* to compare. This happens also to be the total number of ordinary rungs; the denominators here count different objects. The tied-pair count of an address with bin populations \(n_j\) is \(\sum_j n_j(n_j-1)/2\). It counts how often a stored address cannot distinguish two distinct elements. Numeric affinity rows, including the estimate-grade Dy and Tm additions, are scored using the source-specific inputs. An unclassified affinity gets an N on this display and keeps its full provenance in the drilldown.

| Address | Mixer bins / largest / tied pairs | Extended bins / largest / tied pairs |
|---|---:|---:|
| Anion side × outermost named-core side | 7 / 45 / 1,230 | 7 / 47 / 1,288 |
| Anion side × any ordinary outside | 6 / 45 / 1,248 | 6 / 47 / 1,304 |
| Anion side × any ordinary outside × dominant named opening’s ordinal | 19 / 17 / 346 | 19 / 19 / 366 |
| Previous address plus dominant core identity | 24 / 17 / 326 | 24 / 19 / 346 |

**DERIVED from the pinned ladders.** Name a core by its 2, 10, 18, 36 or 54 electrons. For element Z its opening ratio has k=Z−N, with k≥1 required. Sort the eligible openings by increasing k, corresponding to progress inward. The ordinal of the maximum is its one-based position in that ordering. No ties occurred in the central data. Of 83 elements having named openings, the largest was outermost at 13 and deeper at 70. Eight elements have only one candidate. For the other 75, the lower endpoint of the dominant ratio exceeds every competing upper endpoint using the reported widths. Replacing the candidate list with **all** ordinary rungs gives the same central maximum in all 83 elements. Among those 83, 74 maxima are certified against every ordinary competitor by the simple rectangle test; nine have a missing width somewhere in that comparison. This last count does not assert that a missing width is itself material.

Magnesium's outermost and strongest opening is Ne, z≈5.33037; Al also opens Ne first, but He is stronger, z≈4.71935 versus 4.21801. Caesium has its peak at Xe (ordinal 1); barium opens Xe first yet peaks at He (ordinal 5). Thus a tile can show both the first obstruction encountered and where the largest internal cost change actually occurs. The rank row is a navigation feature; it does not reconstruct numerical magnitudes. Preserve the link to the complete ordered ladder, every raw affinity status, numerical ratios, widths and references. All are recoverable by (Z,k) in the source ledger.

**Retrospective transfer test.** A single classification target and rule were written in `PROTOCOL.md` before running the test. Fit only on H–Xe elements with numeric affinities, using (any ordinary outside, dominant named ordinal). Never give the predictor its target affinity or anion wall class in the inputs. Apply the shared training majority within the matching feature bin, with an outside tie-break and overall-majority fallback for unseen bins. The held-out rows are the numeric affinities from Cs through At. The raw data were already public, so this tests the specified method retrospectively.

| Ledger | Training labels | Test labels | Outside found | Inside found | Balanced accuracy |
|---|---:|---:|---:|---:|---:|
| Mixer | 43 | 22 | 18/18 | 0/4 | 0.50 |
| Extended | 43 | 24 | 20/20 | 0/4 | 0.50 |

The predictor makes exactly the same calls as always predicting the training majority. Its four misses in both ledgers are Ir, Pt, Au and At. The fifth ordinal occurs only in period six, so many test cases fall outside the training feature support (23/24 in the extended test). A physically important compression can still fail to forecast an electron affinity. The data support dominant opening as a sorting key and a location for quantitative drilldown. They do not establish predictive strength for this rule and target.

**Reproduction.** Run `python3 check_address.py H_to_At_thresholds.csv element_data_v1.js OUTDIR`. The checker compares all 3,655 positive-index IEs between the two sources, computes ratios and classifications with rational arithmetic, and saves the 85 addresses and per-element held-out decisions. O, I and N in the machine-readable files mean outside, inside and unclassified in that particular column. Extended source statuses describe one-sided, provisional and nonbinding cases more precisely. The JSON array embedded in the mixer supplies the adopted earlier affinity ledger directly.

[85-element extended table at the shared review pin](https://github.com/dicipler-pixel/votkp-lean/blob/26b2875/research/2026-11-20-element-paper-loop-wall/russell/prediction_review_20261121/H_to_At_thresholds.csv) · [Earlier mixer data at the same pin](https://github.com/dicipler-pixel/votkp-lean/blob/26b2875/research/2026-11-20-element-paper-loop-wall/mixer/element_data_v1.js)
