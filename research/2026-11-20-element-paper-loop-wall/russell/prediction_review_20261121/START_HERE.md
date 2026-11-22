# Where Beasley's peel table can be tested

**Jeromie Beasley · joint research review · 21 November 2026**

[Corrected interactive table, H–At](../../ptable/Periodic_Table_of_Elemental_Peels_Codex_review_v1_1.html) · [39-page working paper](../../manuscript/What_the_Peel_Keeps_v1.pdf) · [six-page illustrated addendum](addendum/Where_the_Peel_Wall_Can_Be_Tested_v1.pdf) · [interactive prediction bench](prediction_bench/Prediction_Bench_v1.html). Download an HTML file and open it locally to run it. The GitHub file view displays its source. The table preserves Claude's original v1 numerical baseline, with separate sourced explanations for uncertain and additional affinity inputs.

## What the data can distinguish

| Comparison | Result | How to interpret it |
|---|---|---|
| Ordinary adjacent removal energies within each atom | None of 5,714 available ground-state central ratios between the geometric wall and the registered midpoint. One uncertainty rectangle overlaps, at francium; 23 lack a complete width. | A classification count cannot select an exact cutoff inside an empty interval. [Full ground-state scan](ground_state_search/REPORT.md) |
| Oxygen with the same charge path and three specified final states | The O²⁺ 4s triplet gives 5.826881, 5.827870 and 5.830347 in J order. The third separates the geometric wall from all six registered alternatives. | Published energy levels and ultraviolet tags identify the channels. The missing step is a prior prediction for an independent physical outcome. [Level sources and all six carbon/oxygen hits](channel_search/READ_ME.md) · [oxygen controls](oxygen_design/Oxygen_Identifiability.md) |
| Different one-electron ions' ground bindings | Sc²⁰⁺ and Sn⁴⁹⁺ give 5.832602195, the only pair in the interval across 5,995 assigned pairs. Both inputs are theoretical. | Same-orbital, different-nucleus comparison, separate from an ordinary peel. No independent measurement of the required binding ratio was found. [Scan and source audit](hydrogenic_pairs/README.md) · [experimental lines](lyman_pair/README.md) |
| Equal-face controlled input, z=35/6 | The normalized four-stage return has trace −354481/176400. The predicted sign of the real intensity contrast is positive. | This is a testable instrument prediction. Neither an atomic threshold nor a laboratory return was measured here. [Optical protocol](precision/passive_test.md) · [existing laboratory data](experimental_optics/measurement_search.md) · [simpler one-port calibration](real_port/README.md) |
| Rubidium/caesium extrapolation to francium | The registered value stays 21.8344 eV; the same secant got the side wrong on all three preceding alkali tests. Two calculated Fr²⁺ residual states give widely separated thresholds. | Keep the forecast on record with its poor track record. A new independent ground-state threshold would be scoreable. [Competing predictions, measurements and numerical controls](francium/REVIEW.md) |

## What the atomic model adds to the face

In a centred one-electron Coulomb scale change with fixed mass, the table's face apex a=tanh[(ln z)/4] determines the 1s survival probability (1−a²)³. The 2s and 2p orbitals at exactly the same energy ratio z=4 give probabilities 0.312148 and 0.554929. The full analytic result includes the radial node number and angular momentum, and the heavy-relativistic problem also requires the absolute binding scale. These are explicit microscopic projection measurements. Their applicability to the ordinary many-electron peel table still requires a physical coupling and a preparation. [Face-apex derivation](orbital_face/BALL_FACE.md) · [all orbitals and 637 exact checks](hydrogenic_orbitals/README.md) · [heavy-ion scale control](dirac_scale/README.md).

A closed comparison of the projectors at scales 1,2,4 has negative three-state trace for 2s and positive trace for 2p. Its real sign survives reversal and can in principle be read with a controlled permutation. Dirac Time §11.4 separately gives a two-probe path-memory witness for equal visible endpoints; its own original three numerical checks were rerun. [Three-state readout](coulomb_loop/README.md) · [Dirac Time phase test](dirac_path/README.md) · [same final ion, three possible route classifications](state_observables/README.md).

## What the return to Russell changed

All 386 book entries and the 199 separate laws were located. The element-focused crosswalk annotates 132 distinct positions. For Russell's three columns of 23 wavelengths, the frozen ±0.20 Å test matches 21, 20 and 19 ordinary neutral-iron lines. The contemporary iron-arc literature contains examples from all three columns. The attribution to different ancestral elements is unsupported by those wavelengths. [Historical scope](history_ledger/RUSSELL_LEDGER_REVIEW_v1.md) · [source-by-source iron audit](history_ledger/IRON_COLUMNS_v1.md).

A separate balanced pilot masked 24 historical verdicts. Two AI raters agreed on 23 parity classifications. Among 20 agreed-even claims, ten carried a historical T grade and ten F. This result concerns ordinary spatial inversion. Reversal of an ordered peel, charge conjugation and transposition are separate operations. [Blind protocol and results](spatial_mirror_pilot/README.md).

## Independent review and formal checks

Claude independently reran the mixed Be/Rb numerical test and supplied a signed three-theorem consistency check. His code and Codex's stronger all-threshold proof can be replayed separately. The signed review, acknowledgments and later requests are historical records. Claude's standalone packaging commit did not independently certify the later oxygen, Sc/Sn or orbital results. [Claude's mixed-face check](CLAUDE_RESPONSE.md) · [two-face uniqueness](consistency/README.md) · [countermodels](rivals/README.md) · [review requests](CLAUDE_HANDOFF_2.md).

A separate local runner compiled 11 self-contained research modules, enumerated all 75 named theorems, inspected the axiom output for each, and replayed each compiled module with Lean 4.34.1 leanchecker. The deliberately false control failed for its false goal. The nuclear, chemical, historical and measurement assumptions in the prose have a different evidentiary status from the formal inequalities. [Complete run log](complete_kernel_log.txt) · [audit script](check_every_proof.py).

For an offline numeric replay, run python offline_evidence.py /path/to/data/element_thresholds_20261011.json.gz from this review directory. It reconstructs the required ZIP wrapper from the committed H–At CSV and checks the generated rival rectangles, heavy scans, oxygen and hydrogenic channel files and other outputs against their committed bytes. [Offline numeric audit](offline_evidence_output.txt). The corrected table data and headless browser audit are [documented separately](table_v1_1/README.md).
