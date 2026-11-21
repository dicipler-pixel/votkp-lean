# Palladium through tin · complete peel ladder

**DERIVED.** All 235 ordinary pairs are inside the loop wall at the archive values. Only three rungs are outside: the bound-anion rungs of palladium, indium and tin. Silver has a bound anion with its rung just inside. Cadmium has no bound atomic ground-state anion in the 2022 evaluation. Palladium's outside rung also opens its filled 4d¹⁰ subshell, because its anion has one 5s electron outside the neutral filled shell. No new category of outside ordinary step was found.

**Audit.** The script reads the NIST-derived archive bytes at commit bcedbd9bba0de5a75fd2a860a912ebc4882f4e8a. It generates the simple CSV, reopens it, reparses the archive and independently rounds the ratios and reflections using integer arithmetic. Differences between printed energies and archive: none, 240 of 240 matched. Differences between printed pairs and exact fractions at six decimals: none, 235 of 235 ordinary and four of four bound-anion pairs matched. The 245 rows also include a blank cadmium-anion placeholder and five terminal energies. Of the 239 ratio rows, 237 have both input uncertainties; all 237 retain their central call at the extremes. Palladium's second and third ordinary pairs share the palladium third threshold, whose uncertainty is unavailable. [Pinned archive](https://github.com/dicipler-pixel/votkp-lean/blob/bcedbd9bba0de5a75fd2a860a912ebc4882f4e8a/data/element_thresholds_20261011.json.gz)

**MEASURED / EVALUATED.** Rung zero uses the recommended affinities in **Table 3** of Ning and Lu (2022): palladium 0.56214(12), silver 1.30447(2), indium 0.38392(6) and tin 1.112070(2) eV. Cadmium is listed as unbound using electron-scattering/accelerator evidence. A search for newer element-specific spectroscopic measurements found no replacement for these four values. The silver uncertainty here is the evaluation's 0.00002 eV. The recent high-sensitivity threshold method demonstrated in 2025 was tested on chlorine. [2022 evaluation](https://doi.org/10.1063/5.0080243) · [palladium experiment, 1998](https://doi.org/10.1103/PhysRevA.58.2051) · [silver experiment, 1998](https://doi.org/10.1088/0953-4075/31/17/013) · [indium experiment, 2010](https://doi.org/10.1103/PhysRevA.82.032507) · [tin experiment, 2013](https://doi.org/10.1088/0953-4075/46/12/125002) · [2025 method](https://doi.org/10.1038/s41467-025-64581-x)

## How the individual boundaries move

**Rejection tests.** The proposed decline in filled-4d¹⁰ opening would fail if a successive ratio rose. It would remain interval-unresolved if any earlier lower bound overlapped the next upper bound. The silver anion's central inside classification would lose interval support if its highest possible forward ratio attained the wall. A “bare shell floor” interpreted literally as a lower bound for data fails wherever a complete experimental/evaluated interval lies below it.

| Element | Anion z | Filled 4d¹⁰ z | Krypton core z | Filled 3d¹⁰ z | Argon core z | Neon core z | Helium core z |
|---|---:|---:|---:|---:|---:|---:|---:|
| Palladium | 14.830539 | 14.830539 | 1.491995 | 1.770492 | 1.143255 | 2.349624 | 4.144553 |
| Silver | 5.807902 | 2.835762 | 1.443936 | 1.766926 | 1.138111 | 2.343180 | 4.139194 |
| Cadmium | unbound | 2.215951 | 1.399083 | 1.763123 | 1.132722 | 2.336890 | 4.133974 |
| Indium | 15.071775 | 1.977239 | 1.369478 | 1.757727 | 1.128308 | 2.330367 | 4.128884 |
| Tin | 6.603827 | 1.890771 | 1.343972 | 1.754495 | 1.124729 | 2.324352 | 4.123914 |

**DERIVED.** The first **ordinary** 5s → filled 4d¹⁰ opening is silver's first ratio. Cadmium, indium and tin supply the second, third and fourth ordinary ratios respectively for this comparison. All four have non-overlapping, strictly declining endpoint intervals. Palladium's anion/neutral boundary precedes these and also has its interval strictly above silver's. Indium and tin are the first two p-block homologues of gallium and germanium. Their 4d-opening values decrease in the same direction as the earlier 3d-opening values; this check covers only the first two p-block entries.

**DERIVED.** For silver, the upper-end anion ratio is 5.808010273, below 3+2√2 = 5.828427125… . With the encoded first ionization energy, the critical affinity is IE₁(3−2√2) = 1.299876251 eV. The adopted measured affinity exceeds it. This is a ground-state atomic detachment test and supplies no bulk conductivity criterion.

**DERIVED.** For the inner 4s → 3d¹⁰ opening the bare change of principal shell gives 16/9, about 1.777778. The central ratios go from 1.780731 in ruthenium to 1.776570 in rhodium, but both intervals contain the bare value. Palladium is decisively below at the encoded precision: its upper value is 1.777632010. Each of silver through tin also remains below across its quoted interval. Thus the bare ratio provides a useful reference and does not universally bound the empirical ionization ratio from below. These cases remain inside the loop wall.

## The last two electrons

**DERIVED.** The gap per charge S=(h−b)/Z continues rising, with the hydrogen-like energy h and helium-like energy b in hartree. The fitted screening charge σ=Z−√(2b) changes sign **between palladium and silver**. The sign follows exactly from whether b is smaller or larger than Z²/2. The table gives that difference in eV alongside the reported uncertainty of the theoretical helium-like entry.

| Element | Terminal h/b | S | σ | Helium-like minus bare (eV) | Quoted helium-like uncertainty (eV) |
|---|---:|---:|---:|---:|---:|
| Palladium | 1.029422 | 0.676384 | 0.010878 | -13.614648 | 0.014 |
| Silver | 1.028855 | 0.679054 | -0.033092 | 42.337891 | 0.015 |
| Cadmium | 1.028314 | 0.681790 | -0.079216 | 103.553045 | 0.017 |
| Indium | 1.027798 | 0.684596 | -0.127574 | 170.323812 | 0.019 |
| Tin | 1.027304 | 0.687472 | -0.178222 | 242.915193 | 0.022 |

**Interpretation.** At silver, the helium-like ionization energy exceeds the *nonrelativistic* bare one-electron value by 42.337891 eV. This sign diagnoses the specific effective-charge reference. Direct inference of a negative electric screening density from σ would need a physical model linking that parameter to density. The hydrogen-like/helium-like energy gap itself is positive throughout. Prior work on the relativistic part of the screening diagnostic motivates keeping this comparison distinct from both the equal-face loop and the actual last-step gap. [CODATA hartree energy in eV](https://physics.nist.gov/cgi-bin/cuu/Value?threv)

## Rerun

```sh
python3 batch10_ladder.py /path/to/data/element_thresholds_20261011.json.gz .
python3 batch10_ladder.py /path/to/data/element_thresholds_20261011.json.gz . --verify-only
python3 batch10_controls.py /path/to/data/element_thresholds_20261011.json.gz
```

The compact CSV occupies [batch10_pd_sn.csv](batch10_pd_sn.csv). The [detailed rungs](batch10_rungs_detailed.csv) include endpoints and uncertainties, source references and grades for both energies, the dimensionless internal logarithmic clock spacing, reflection and face apex. The [summary](batch10_summary.csv) is generated from the same arrays and the serialized compact CSV. The calculated quantities refer to internal atomic steps; an interatomic junction has its own clock input.

## Why the sign falls between palladium and silver

**DERIVED · comparison of references.** In electronvolts let H be the archive hydrogen-like energy, B the archive helium-like energy, N the nonrelativistic bare binding and D the point-nucleus, infinite-nuclear-mass Dirac ground-state binding. With Eₕ the energy of one hartree and α the fine-structure constant,

\[
 N=E_h Z^2/2,\quad D=\frac{E_h Z^2}{1+\sqrt{1-(\alpha Z)^2}},\quad
 B-N=\underbrace{D-N-(H-B)}_{\text{point reference with archive gap}}+\underbrace{H-D}_{\text{remaining H-like correction}}.
\]

Test the simple model D−N−5ZEₕ/8 against the archive sign, first replacing only its leading gap by H−B, then replacing D by H. The simple model becomes positive between ruthenium and rhodium. The point reference with the archive gap becomes positive one element later, between rhodium and palladium. Restoring the archive hydrogen-like value moves the zero once more to between palladium and silver. At palladium, D−N−(H−B) = +13.54 eV (rounded), but the residual H−D is about −27.16 eV, enough to give B−N < 0. At silver, the corresponding positive excess is about +71.54 eV and the residual about −29.21 eV, leaving B−N > 0. The separate [machine-generated comparison](screening_controls.csv) gives the full values. The residual combines the effects omitted from the point Dirac energy. The published comparison below separates leading recoil from the authors’ combined Lamb term. The middle control uses the archive gap and therefore serves as a sensitivity test, rather than an independent prediction. [Hydrogen-like level components, Yerokhin and Shabaev (2015)](https://arxiv.org/abs/1506.01885) · [CODATA 2022](https://www.nist.gov/publications/codata-recommended-values-fundamental-physical-constants-2022)

Run `python3 screening_controls.py /path/to/data/element_thresholds_20261011.json.gz screening_controls.csv` to reproduce the comparison.


**Published component test.** Yerokhin and Shabaev’s 2015 Table III lists the point Dirac level, leading recoil (“MASS”), combined Lamb correction (“LAMB”) and total for each isotope considered. Positive level shifts reduce the positive ionization binding by the same amount. For palladium-106 the published losses are 0.149118 eV from leading recoil and 27.010566 eV from the combined Lamb term. The point-reference balance before these corrections is +13.544455 eV: including leading recoil alone leaves it positive, whereas including the Lamb term alone makes it negative. For silver-107 the losses are 0.154289 and 29.052237 eV, too small together to reverse the +71.544955 eV balance. Across the five selected isotopes the published loss sums agree with the archive hydrogen-like residual to within 0.0008 eV at the displayed precision. The term labelled LAMB in the source includes finite-size and several QED contributions; this test identifies that combined group. It does not isolate any one of its internal components. [2015 source, Table III, p. 45 of the PDF](https://arxiv.org/pdf/1506.01885#page=45) · [extracted rows](hydrogen_like_components_2015.csv)
