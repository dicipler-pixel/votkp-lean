# Dysprosium through ytterbium

**DERIVED from evaluated thresholds.** The [printed CSV](batch14_dy_yb.csv) has 345 rows. All 340 numeric ionization energies agree exactly with the October archive, and all 340 archived energy, uncertainty, grade and bibliography tuples match the newly fetched NIST ASD snapshot. There are 6 experimental, 24 semi-empirical and 310 theoretical energy entries. All 335 ordinary ratios are inside the loop wall both centrally and throughout their independent input rectangles. Of five k=0 slots, two have evaluated point values, both outside. Two carry binding upper limits and one carries the evaluated absence of a stable anion. [Full threshold snapshot](asd_states_20261121.csv) · [independent audit, five damaged inputs rejected](audit.txt) · [detailed signed ladder and face coordinates](rungs_detailed.csv)

## The first filled 4f shell in this sequence

**DERIVED.** In all five atoms ASD assigns the second removal to the last 6s electron and the third to the first 4f occupation loss. At k=2 the intermediate states have 4f occupancies 10, 11, 12, 13 and 14, respectively; their central ratios are 1.965313, 1.934471, 1.905002, 1.961044 and 2.057034. The fully occupied 4f¹⁴ case in ytterbium exceeds all four preceding intervals even at its low endpoint: 2.054977 versus a maximum earlier upper endpoint of 1.971274. Yet it lies below both the loop wall and the pure hydrogenic n=6 to n=4 comparison 9/4. This distinguishes a filled subshell from the earlier closed noble-gas core openings. [Direct calculation](four_f_opening.csv)

**DERIVED.** The largest ordinary central step for each is the helium-core opening: 4.054136, 4.050130, 4.046084, 4.042100 and 4.038080. The terminal S readout rises through 0.744235, 0.748540, 0.752950, 0.757462 and 0.762071. The σ readout falls through −1.361398, −1.463030, −1.568358, −1.677816 and −1.791005. Those computed values use the archive’s H-like and He-like theoretical entries and the 2022 CODATA Hartree. The nominal xenon electron-count rows all remain inside; none has an ASD closed 5p⁶ state there. [Core/configuration table](asg_openings.csv) · [screening](screening.csv)

## Five different affinity records

**MEASURED or evaluated.** This table distinguishes positive point estimates from upper bounds and the evaluated absence of a stable atomic anion. For η, χ and ω/η, the full numeric rows and theoretical scenarios appear in [the chemistry table](affinity_chemistry.csv). The quoted experimental upper-bound rows evaluate the boundary and state the consequence *conditional on binding*. They do not assign a positive ground-state electron affinity.

| Element | Evidence in eV | Rung-zero result under this evidence |
|---|---|---|
| Dysprosium | Electric-dissociation/AMS estimate; the 2022 Table 3 recommendation is 0.015(3). The 1994 p₁/₂ fit gives 0.0155(25). | z=395.9374, Γ=0.994961, ω/η=0.505077 under the recommendation; outside under either. |
| Holmium | Experimental upper limit about 0.005; a positive bound ground state is unestablished. | If bound, z≥1204.18 using the low IE₁ endpoint and that upper limit; outside. No point rung. |
| Erbium | Experimental upper limit about 0.005; a positive bound ground state is unestablished. | If bound, z≥1221.34 on the same convention; outside. No point rung. |
| Thulium | The 2022 evaluation recommends the AMS estimate 0.032(7). A competing 2002 photodetachment analysis reported 1.029(22). | z=193.2626, Γ=0.989705, ω/η=0.510457 under the recommendation. Both full source boxes stay outside. |
| Ytterbium | 2019 AMS re-examination withdrew the earlier identification. The 2022 evaluation concluded no stable atomic Yb⁻; its Table 3 gives a <0.0036 experimental ceiling and negative theoretical EA. | No physical bound-anion rung in this ledger. |

**DERIVED / source test.** The competing thulium interpretation gives a materially different z=6.010109 with a rectangular range [5.884294, 6.141421]. Both endpoints still lie above the loop wall, but the same range straddles the comparator six. Treat the two sources as competing assignments rather than averaging them. The 2022 review's Table 3 and §4.3 use the small estimate; it does not publish a definitive new spectrum settling the discrepancy. Similarly, entering the old ytterbium 0.010(3) as if it were a current measurement would invent an extra outside row. Its primary investigators re-examined the attribution. [Computed alternatives](source_controls.csv) · [Ning & Lu 2022](https://doi.org/10.1063/5.0080243) · [1997 survey](https://doi.org/10.1016/S0168-583X(96)00749-5) · [1994 dissociation analysis](https://faculty.kfupm.edu.sa/PHYS/mgarwan/download/Electric%20dissociation%20of%20negative%20ions.pdf) · [Davis & Thompson, thulium (2002)](https://doi.org/10.1103/PhysRevA.65.010501) · [Zhao et al., ytterbium (2019)](https://doi.org/10.1016/j.nimb.2019.01.023)

**HYPOTHESIS / falsifier.** A reproducible, species-selected bound-to-ground detachment threshold would change the status for holmium, erbium or ytterbium. For the disputed thulium source, a resolved spectroscopy measurement demonstrating the 1.029 eV feature belongs to the ground threshold would replace the numerical recommendation; it would leave the wall call intact over the reported uncertainty.

## Direction and shared thresholds

**DERIVED.** All ordinary centers have positive Γ. Thirty-five of the independent rectangles allow Γ<0; two additional rectangles permit only endpoint equality (erbium k=16 and 21). Gaps between energies two removals apart are strict across their full widths, so adjacent ratios cannot both reverse. Applying the exhaustive shared-energy construction yields maxima 3, 3, 3, 5, 5, totaling **19** simultaneous negative Γ across the five ladders. One sharp example in ytterbium reverses k=13,16,18,20,22. In its 22nd pair the opposite endpoint shifts can first reach equality at 595 eV using exactly one half of both quoted widths. These interval witnesses use the common theoretical L582 source; they do not establish physical reversals or a covariance model for its errors. [All affected pairs](direction_limits.csv) · [exact joint counts and witnesses](joint_direction.csv) · [Carlson et al. 1970](https://doi.org/10.1016/S0092-640X%2870%2980005-5)

## Reproduce

From this directory:

```sh
python fetch_states.py /tmp/fresh_dy_yb.csv
diff asd_states_20261121.csv /tmp/fresh_dy_yb.csv
python generate.py ../../../../data/element_thresholds_20261011.json.gz
python scenarios.py
python direction.py
python verify.py
python ../../checks/check_batch_range_v2.py ../../../../data/element_thresholds_20261011.json.gz batch14_dy_yb.csv 66 70
```

The generator and independent verifier share the established batch-13 conventions through range parameters; their numerical implementations remain separate. [Pre-check falsifiers](FALSIFIERS.md) · [Affinity inputs](affinities.csv) · [NIST differences, header only](asd_differences.csv)
