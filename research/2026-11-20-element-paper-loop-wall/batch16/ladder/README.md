# Osmium through mercury — signed peels and two frozen tests

**DERIVED from evaluated atomic data.** The [printed ladder](batch16_os_hg.csv) has 395 rows. Every one of the 390 successive ionization energies matches the pinned October JSON exactly. Every energy, quoted width, source grade and reference string also matches a fresh [five-element NIST ASD extract](asd_states_20261121.csv) obtained on 2026-11-21. The [difference ledger](asd_differences.csv) has its header only. The printed energies and rounded ratios come from the same in-memory input, and each reflection is rounded directly from its exact fraction. Of 385 ordinary ratios, all 385 are inside the loop wall throughout their reported uncertainty rectangles. Four ground-state affinity measurements supply anion rungs. Osmium's is outside. Iridium, platinum and gold are inside. Mercury's rung is blank. [Exact audit and false controls](audit.txt) · [All start/end inputs, ratios, signed reflections, face apexes, occupations and rectangular bounds](rungs_detailed.csv)

## Four frozen chemistry calls

**HYPOTHESIS and test.** The signed calls were recorded before this batch. Opposite supported ground-state labels would defeat them. The source quantities are the isolated atom's first ionization energy I and ground-to-ground electron affinity A. Define η=(I−A)/2, χ=(I+A)/2. At these positive forward ratios, ω/η=(χ/η)²/2 drops below one outside the wall and exceeds one inside. Quoted independent bounds are extremized across the input rectangle; no independence of experimental errors or of the four chemistry predictions is assumed. [Prediction protocol, 5c5327b](../../holdouts/heavy_anions_protocol.md) · [Inputs](affinities.csv) · [Exact-rational scores before display rounding](heavy_anion_primary.csv)

| Element | IE₁ (eV) | Ground EA (eV) | z₀ range | Γ₀ | η (eV) | χ (eV) | ω/η | Frozen / returned |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Os | 8.43823(20) | 1.077661(24) | 7.829774–7.830494 | 0.773503 | 3.6802845 | 4.7579455 | 0.835692 | outside / outside |
| Ir | 8.96702(22) | 1.564057(11) | 5.732999–5.733361 | 0.702964 | 3.7014815 | 5.2655385 | 1.011823 | inside / inside |
| Pt | 8.95883(10) | 2.12510(5) | 4.215575–4.215868 | 0.616544 | 3.416865 | 5.541965 | 1.315352 | inside / inside |
| Au | 9.225554(4) | 2.30861(3) | 3.996097–3.996205 | 0.599692 | 3.458472 | 5.767082 | 1.390317 | inside / inside |
| Hg | 10.437504(6) | no established bound ground anion | — | — | — | — | — | no call |

**DERIVED.** For iridium, the nearest of the four to the wall, the largest possible z₀ is (8.96702+0.00022)/(1.564057−0.000011)=5.733360784. Its full box stays below 3+2√2. The comparator 5 would classify iridium outside. The fixed 5.8, 5.82, 5.83, 5.85, 5.9 and 6 reproduce all four signs. The highest inside value here is below silver, and the lowest outside value is above silicon. Consequently this batch leaves the earlier interval of equivalent central cutoffs at [3788117/652235, 20379200/3473803), or [5.807902059840…, 5.866538776091…). Each of six alternative-source rows retains the primary whole-box sign. Fresh NIST neutral thresholds agree with the pinned values in every digit. This separately checks numerical transcription, with no additional independent experiment implied. [Six alternative inputs](alternative_affinities.csv) · [Scores under all seven comparator cutoffs](heavy_anion_source_controls.csv) · [Earlier cutoff endpoints](../../batch11/robust/CUTOFF_H_CS.md)

### Affinity and threshold provenance

- **MEASURED — Os.** Slow-electron velocity-map imaging gives 8691.92(19) cm⁻¹ or 1.077661(24) eV. Ning and Lu tabulated it in 2022 against an unpublished reference. Lu et al. published the spectrum and value in 2023. The earlier laser measurement distinguished the 1.07780(12) eV ground binding from the 0.553(3) eV excited binding. Only the ground threshold enters the score. [2023 paper, Fig. 2](https://doi.org/10.1088/0256-307X/40/9/093101) · [2000 direct experiment](https://doi.org/10.1103/PhysRevLett.85.534)
- **MEASURED — Ir.** Lu et al. resolved the 5d⁸6s² ³F₄ anion → 5d⁷6s² ⁴F₉/₂ neutral threshold at 12614.97(9) cm⁻¹ or 1.564057(11) eV. The 1999 threshold-law analysis gave 12617.4(12) cm⁻¹ or 1.56436(15) eV. The experiment and its revision are separate rows in the score. [2020 direct imaging](https://doi.org/10.1063/1.5134535) · [1999 laser thresholds](https://doi.org/10.1103/PhysRevA.61.012505)
- **MEASURED — Pt.** Bilodeau et al. reported 17140.1(4) cm⁻¹ or 2.12510(5) eV. The NIST WebBook's 2.125104(44) eV is another tabulation of that same experiment. Ning and Lu's Table 3 prints 5d⁸6s² as the neutral valence configuration. ASD and the 2009 Pt⁻ spectroscopy identify the Pt neutral ground level as 5d⁹6s ³D₃. We use the latter configuration alongside the experimentally supported EA. The excited 5d¹⁰6s ²S₁/₂ anion state does not enter the ground threshold. [1999 direct measurement](https://doi.org/10.1103/PhysRevA.61.012505) · [NIST WebBook](https://webbook.nist.gov/cgi/cbook.cgi?ID=C7440064&Mask=20) · [NIST neutral configuration](https://physics.nist.gov/PhysRefData/Handbook/Tables/platinumtable1.htm) · [2009 excited-state identification](https://doi.org/10.1103/PhysRevA.79.022502)
- **MEASURED — Au.** Ning and Lu give 18620.2(2) cm⁻¹ or 2.30861(3) eV, reproducing Andersen et al. (1999), whose table points back to Hotop and Lineberger (1973, 1985). The directly reported 1973 central value was 2.3086(7) eV, with a wider uncertainty. The 2022 evaluation is not a new experiment. [2022 evaluation, Table 3](https://doi.org/10.1063/5.0080243) · [1999 evaluation](https://doi.org/10.1063/1.556047) · [1973 direct experiment](https://doi.org/10.1063/1.1679515)
- **MEASURED / evaluated status — Hg.** The 2022 evaluation reports no stable anion, gives “<0” in Table 3, and separately gives the accelerator-mass-spectrometry sensitivity bound of ≤0.005 eV for this group. Its Table 3 cites electron scattering and AMS. There is no positive central ground-state affinity to divide by. The number 0.005 is only a hypothetical positive-binding boundary in [the chemistry file](affinity_chemistry.csv). [2022 evaluation, Group 12 and Table 3](https://doi.org/10.1063/5.0080243)

**MEASURED — neutral ionization thresholds.** Fresh ASD gives the same neutral values as the archive. Its primary sources are Colarusso et al. 1997 for Os/Ir (Rydberg fit, 68058.9(16) and 72323.9(18) cm⁻¹), Jakubek and Simard 2000 plus Marijnissen et al. 1995 for Pt, Dyubko et al. 2005 for Au and Zia et al. 2003 plus Zia and Baig 2004 for Hg. The attached ASD snapshot retains the original bibliographic keys for every ion. No newer superseding neutral threshold was identified in the targeted search. [Os/Ir](https://doi.org/10.1103/PhysRevA.55.1526) · [Pt 2000](https://doi.org/10.1088/0953-4075/33/10/301) · [Pt 1995](https://doi.org/10.1103/PhysRevA.52.2606) · [Au](https://doi.org/10.1088/0953-4075/38/8/003) · [Hg 2003](https://doi.org/10.1088/0953-4075/36/23/003) · [Hg 2004](https://doi.org/10.1140/epjd/e2003-00325-0)

## The helium-core opening drops below four

**HYPOTHESIS tested.** Both forecasts fixed the first crossing of the bare reference four between Au and Hg. At k=Z−2 compare the cost of stripping the first helium-core electron to the cost of the previous Li-like 2s removal. Four is an independent shell reference; both sides of this crossing are inside the loop wall. These inputs are NIST theoretical entries. This is a truncated-range extrapolation against an already published archive. [Preregistered protocol, 4a30cc1](../../holdouts/k_opening/PROTOCOL.md) · [Frozen forecasts](../../holdouts/k_opening/predictions.csv) · [All five signed residuals and endpoint tests](k_opening_residuals.csv)

| Element | Li-like → He-like removal thresholds (eV) | Opening z | Full box | Actual − frozen secant | Actual − frozen Dirac+1/Z |
|---|---|---:|---|---:|---:|
| Au | 22868.1(3) → 91515.8(3) | 4.001897840 | 4.001832223–4.001963460 | +0.000067013 | −0.001496341 |
| Hg | 23544.1(3) → 94124.7(3) | 3.997804121 | 3.997740439–3.997867804 | +0.000001006 | −0.001648715 |

**DERIVED.** Across Os–Hg the K opening is the largest ordinary central ratio for each atom. It decreases from 4.014042618 to 3.997804121. The two frozen models both locate the crossing. The secant point prediction lies inside the Hg rectangle alone among these five; the Dirac+1/Z point prediction falls outside all five. Different tests are answered by the bracket and the pointwise residuals. In the terminal He-like → H-like step on [the screening ledger](screening.csv), S_Z instead rises from 0.792161 to 0.814682 as σ_Z falls from −2.562939 to −3.174743. The negative effective σ_Z records excess binding relative to Z²/2 in the defining parametrization. Neither series isolates a nuclear or QED component in this comparison.

## Which occupied subshell actually opens?

**DERIVED, conditional on the ASD ground configurations.** A loss of full occupancy is located by examining the post-removal occupations, including reclosure. Both Au and Hg expose a genuine 5d¹⁰ configuration between removals: Au k=1 gives 2.189896, Hg k=2 gives 1.838792, both with experimental endpoints. At 68 electrons, all five instead pass through [Xe]4f¹⁴ with 5d removal followed by 5p removal. The 4f occupancy survives that next removal. For each of these elements the 54-electron configuration is [Kr]4d¹⁰4f⁸; an equal electron count alone cannot identify a filled xenon core. [All core-count openings and actual levels](asg_openings.csv) · [All 4f and 5d opening/reclosure events](subshell_events.csv)

**RECOGNISED, source-conditional.** Osmium's assigned 4f count goes 14→13→14→13 from q=12 to 15. At q=13→14 the NIST configurations are [Cd]4f¹³5p² → [Cd]4f¹⁴. Two 5p slots empty and one 4f slot fills, so K=61, R=1 in the earlier [occupation ledger's convention](../../batch13/traits/README.md). The energies involved carry theoretical tags; the assignment could change under a revised configuration analysis. The other four elements each show one 4f¹⁴ opening. No electron trajectory is inferred from the configuration labels. [Snapshot](asd_states_20261121.csv) · [State-by-state rows](subshell_events.csv)

## When two consecutive peels can reverse together

**DERIVED.** All 385 central steps are forward. Varying each quoted input inside its interval allows a strictly reversed sign on 82 individual ordinary rungs; six others can reach equality only. At platinum k=30 and 31, the three successive thresholds 1040±50, 1090±50, 1140±60 eV admit 1089>1085>1081 eV simultaneously. Mercury k=31 and 32 admits 1169>1165>1161 within 1110±60, 1160±60 and 1220±60. This is a source-width sensitivity result. It gives no frequency for these sign patterns.

| Atom | Individually reversible | Equality only | Feasible strict-reversal sets | Maximum concurrent |
|---|---:|---:|---:|---:|
| Os | 15 | 1 | 2440 | 9 |
| Ir | 16 | 2 | 4290 | 9 |
| Pt | 17 | 1 | 8010 | 10 |
| Au | 17 | 1 | 5922 | 9 |
| Hg | 17 | 1 | 8010 | 10 |

**DERIVED.** Give an unselected edge the constraint Eᵢ≤Eᵢ₊₁ and a selected edge Eᵢ>Eᵢ₊₁. A directed path in this chain has a single direction. The ascending constraints admit the ordered central values. A descending run is feasible precisely when every earlier upper bound exceeds every later lower bound on that run. Sufficiency follows by propagating lower bounds in topological order with the same sufficiently small positive epsilon on each strict edge. The dynamic program counts patterns by the length of the final descending run. An independent integer difference-constraint solver tested all 491520 candidate subsets for these five chains, returned exactly the same counts and maxima, and treats equal endpoints as non-strict. [Examples and totals](joint_direction.csv) · [Dynamic program](direction.py) · [Exhaustive checker](exhaustive.py)

## Source grades and reproduction

| Element | Experimental thresholds | Semi-empirical | Theoretical |
|---|---:|---:|---:|
| Os | 1 | 4 | 71 |
| Ir | 1 | 4 | 72 |
| Pt | 3 | 3 | 72 |
| Au | 3 | 3 | 73 |
| Hg | 7 | 3 | 70 |
| Total | 15 | 17 | 358 |

**DERIVED.** Run the following from this directory with Python 3. Standard-library scripts read the pinned archive elsewhere in the same checkout. The fresh NIST download is optional when reproducing the existing snapshot.

```sh
python generate.py ../../../../data/element_thresholds_20261011.json.gz
python verify.py
python ../../checks/check_batch_range_v2.py ../../../../data/element_thresholds_20261011.json.gz batch16_os_hg.csv 76 80
python direction.py
python exhaustive.py
python subshells.py
python holdouts.py
python independent.py
```

**Set aside, with why.** The Hg positive-binding upper limit is conditional. The Pt excited-anion channel and the Os excited-state binding energy each address a different transition. A single unconstrained β, QED term, bulk conductivity or knot invariant cannot be inferred from the four atomic affinities, the two model residuals or the signs of rectangle endpoints.
