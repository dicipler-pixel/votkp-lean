# Promethium to terbium: the numerical ladder

**DERIVED from the pinned archive.** The [printed CSV](batch13_pm_tb.csv) contains 320 rows. All 315 successive ionization energies, their uncertainties, grades and bibliographic reference fields agree with the [fresh NIST ASD snapshot](asd_states_20261121.csv) taken on 21 November 2026. Of these thresholds, 5 are experimental entries, 27 are semi-empirical, and 283 are theoretical. Most comparisons here test consistency with evaluated theoretical thresholds. Every displayed ratio and reflection was calculated directly from the source values before rounding. The [audit](audit.txt) also rejected seven deliberately damaged inputs.

**DERIVED.** All 310 ordinary central ratios and their entire input rectangles lie inside the loop wall. Each of the five elements has its largest ordinary central ratio at its helium-core opening. Those ratios fall from 4.074645 in promethium through 4.070477, 4.066354 and 4.062261 to 4.058219 in terbium. Every rectangle permits a unique wall classification. Direction has its own test below. [All rungs, grades, endpoint bounds, log steps, face apexes and orbital changes](rungs_detailed.csv) · [selected shell boundaries](asg_openings.csv)

## Rung zero and its measured status

**MEASURED or literature-evaluated.** Three elements have numeric experimental estimates. Samarium has an experimental lower bound only. No measured ground-state electron affinity for promethium was found. No element in this five has been classified here as having an unbound anion. Theory-only scenarios are explicitly separated in [the chemistry table](affinity_chemistry.csv). The samarium lower-bound row evaluates formulas at the excluded boundary solely to display the implied limit.

| Element | Ground-state affinity evidence, eV | Derived forward ratio | Derived Γ₀ | Derived ω/η | Wall call justified by this evidence |
|---|---|---:|---:|---:|---|
| Promethium | 0.154 is a calculation; no measured point found | — | — | — | Unresolved experimentally |
| Samarium | >0.05 from accelerator studies; positive binding evidence | <112.875 at the pinned central IE₁ | <0.98244 | — | Both sides possible |
| Europium | 0.116 ± 0.013, 2015 velocity-map imaging | 48.882629 | 0.959906 | 0.542641 | Outside including the full quoted box |
| Gadolinium | 0.212 ± 0.030, preliminary measurement reported in 2022 | 29.008491 | 0.933352 | 0.573956 | Outside within that preliminary box |
| Terbium | 0.13131 ± 0.00080, 2022 Table 3; 2020 primary gives ±0.00079 | 44.656157 | 0.956194 | 0.546862 | Outside under either quoted width |

**Source distinctions.** Ning and Lu table both measured and calculated values; the “Calc.” marker on promethium and samarium is essential. Their §4.3 distinguishes the samarium lower bound and the preliminary gadolinium result. The 1993 accelerator study detected atomic samarium anions. In terbium Fu et al. tentatively assigned an anion ground configuration with 4f⁸5d6s²6p and a neutral ground configuration of 4f⁹6s². The earlier 2015 thesis recovered a compatible affinity, 0.13 ± 0.07 eV, with a different assignment of the anion configuration. Energy agreement alone cannot settle that orbital difference. [Ning & Lu 2022](https://doi.org/10.1063/5.0080243) · [Garwan et al. 1993](https://faculty.kfupm.edu.sa/phys/mgarwan/download/Lanthanide%20negative%20ion%20detection.pdf) · [Eu experiment, Cheng & Castleman 2015](https://doi.org/10.1038/srep12414) · [Tb experiment, Fu et al. 2020](https://doi.org/10.1103/PhysRevA.101.022502) · [2015 thesis, ch. 6](https://scholarwolf.unr.edu/server/api/core/bitstreams/f41f5aac-9c22-4369-9e8a-1b2558eb8d5a/content)

**DERIVED / retrospective input control.** The superseded europium EA of 1.053(25) eV gives z₀=5.384981 and an entirely inside box. The current weak-binding measurement gives an entirely outside box. A superseded 1.98(10) eV assignment for terbium likewise gives an entirely inside box. Terbium hydride contamination was proposed for the older assignment in the 2015 thesis. Both changes persist across the source widths. This is sensitivity to spectroscopic assignment. [Computed alternative-source cases](source_controls.csv)

**HYPOTHESIS / falsifier.** In the forward range 0<EA<IE₁, an anion lies outside if EA < (3−2√2) IE₁. For samarium that threshold is approximately 0.96831 eV. Its measured lower bound permits, for example, 0.2 eV (outside) and 1.1 eV (inside). For promethium the critical EA is 0.95770 eV. The two theoretical estimates predict outside and would fail with a reliable measured affinity above the respective critical value and below IE₁. Leave the two experimental labels blank in classifications pending such measurements.

## The signed step with shared uncertainties

**DERIVED.** All central ordinary Γ values are positive. In the quoted rectangular input enclosure, nine individual ordinary steps allow Γ<0 and five additional steps permit Γ=0 only at an endpoint. All fourteen are adjacent pairs of theoretical thresholds carrying the same bibliographic identifier, L582. The source is Carlson et al. (1970), a calculation. Independent rectangular extremes describe what the supplied widths alone allow; they need not be physically or statistically independent errors. Multiplying every energy by one common positive calibration factor leaves every sign unchanged. [Direction rows](direction_limits.csv) · [NIST reference L582](https://doi.org/10.1016/S0092-640X%2870%2980005-5)

| Element | Individually strict-reversible k | Additional touch-only k | Maximum strict reversals together | First possible equality as widths expand |
|---|---|---|---:|---|
| Promethium | none | none | 0 | k=10 at 19/17 times the input widths |
| Samarium | 13,14 | none | 1 | k=14 at 19/26 |
| Europium | 13,14 | 15 | 1 | k=14 at 9/14 |
| Gadolinium | 13,14 | 15,16 | 1 | k=14 at 20/29 |
| Terbium | 13,14,17 | 15,16 | 2 | k=14 at 21/29 |

**DERIVED — sharp joint result.** For energies x±u, y±v with y>x, the smallest common multiplier t permitting equality is t=(y−x)/(u+v). Europium k=14 reaches it first in this batch: 263+14(9/14)=281−14(9/14)=272 eV. Two adjacent strict reversals would require three energies to decrease in a row. In every chain the largest permitted first energy is below the smallest permitted energy two rungs later, excluding every adjacent pair of reversals. Any nonadjacent subset of the individually reversible steps is realizable by putting its first endpoint high and its second low and leaving the other thresholds at their centers. The program verifies each full realization and excludes unintended reversals. Thus **five** is the sharp maximum simultaneous across these five elements. One witness reverses k=13 in samarium, europium, gadolinium and terbium, plus k=17 in terbium. No measured reversal is inferred. [Exact enumeration and witnesses](direction.py) · [summary](joint_direction.csv)

**DERIVED — relation to the reflection.** If u=px and v=py have a common relative half-width p, equality first occurs when the fractional perturbation tp equals (y−x)/(y+x)=Γ. A shared multiplicative shift cannot do this. It requires opposite shifts of the two thresholds. This gives the directed step an uncertainty interpretation under an explicitly specified perturbation model.

## Electron-count channel and screening

**RECOGNISED.** The 55→54→53 electron channel has central ratios 1.148515, 1.194915, 1.118056, 1.109091, 1.161290. The strict central descent seen from cesium through neodymium fails at samarium and again at terbium. All five quoted intervals overlap each other; no rise is forced over the uncertainties. The ASD leading configuration of the 54-electron state differs from closed 5p⁶ for all five. For europium and gadolinium it has a single 5p electron, while in terbium this leading assignment has none. The equal electron count labels this series without asserting any one set of orbitals. In 2024 calculations competing configurations were already found in lower charge states of these elements. [NIST snapshot](asd_states_20261121.csv) · [Carvajal Gallego et al. 2024, Table A.2](https://doi.org/10.1051/0004-6361/202347723)

**DERIVED.** The screened readouts continue separating. S rises from 0.724154 to 0.740064, and σ falls from −0.907468 to −1.263801. Each terminal ratio remains near 1.02. These entries use the two highest **theoretical** archive thresholds and the CODATA 2022 Hartree. The electron’s spinor (Dirac) structure was tested against component terms in the earlier batch; these numbers extend the scalar readouts. They provide no independent component decomposition. [Computed screening table](screening.csv)

## Reproduce

From this directory, use Python 3. The live fetch uses curl and all numerical checks otherwise use the standard library.

```sh
python fetch_states.py /tmp/batch13_fresh.csv
diff asd_states_20261121.csv /tmp/batch13_fresh.csv
python generate.py ../../../../data/element_thresholds_20261011.json.gz
python direction.py
python source_controls.py
python verify.py --controls
python ../../checks/check_batch_range_v2.py ../../../../data/element_thresholds_20261011.json.gz batch13_pm_tb.csv 61 65
```

[Pre-check falsifiers](FALSIFIERS.md) · [Affinity input table](affinities.csv) · [Live differences file, header only](asd_differences.csv) · [NIST ASD](https://physics.nist.gov/asd)
