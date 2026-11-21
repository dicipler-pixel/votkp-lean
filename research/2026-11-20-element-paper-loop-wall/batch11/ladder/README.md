# Antimony through cesium

**DERIVED.** Only three steps in this batch are outside the two-face wall: the anion rungs of antimony and cesium and the **ordinary xenon-core opening in cesium**. The four bound-anion energies are separate measured inputs; the ordinary ladder comes entirely from the pinned archive. Tellurium and iodine have bound anions with inside rungs. Xenon has no bound ground-state anion in the evaluation.

**Audit of serialized output.** The generator read the compressed archive at 8e5d44f1d9e36f242e6522bbe70cea18fb315c7a and verified its SHA-256. After writing the CSV, it reopened the written rows, parsed the archive again, and recalculated the pairs by integer-fraction arithmetic with half-up rounding. Differences in the 265 ordinary ionization energies: zero. Differences in the 260 ordinary and four bound-anion displayed ratio/reflection pairs: zero. The compact CSV has 270 rows, including a blank xenon-anion placeholder and five terminal energies with no outgoing ratio. The inputs provide both endpoint uncertainties for 262 of 264 pairs. Every such pair retains its decision at the endpoints. Antimony's third removal energy has no quoted uncertainty, affecting steps two and three. [Pinned source](https://github.com/dicipler-pixel/votkp-lean/blob/8e5d44f1d9e36f242e6522bbe70cea18fb315c7a/data/element_thresholds_20261011.json.gz)

**MEASURED / EVALUATED.** Rung zero uses Ning and Lu (2022), **Table 3**, which recommends antimony 1.047401(19), tellurium 1.970875(7), iodine 3.0590465(36) and cesium 0.471626(25) eV. The iodine experiment measured iodine-127. The cesium recommendation cites Slater and colleagues (1978) and Scheer and colleagues (1998); preserve the evaluated uncertainty. Xenon is listed as unbound by semiempirical evaluation. A targeted search found no subsequent element-specific replacement measurement for these four affinities. The 2024 tellurium result at 2.0693 eV measures the molecular dimer. [2022 evaluation](https://doi.org/10.1063/5.0080243) · [antimony experiment, 1997](https://doi.org/10.1103/PhysRevLett.79.4104) · [tellurium experiment, 1996](https://doi.org/10.1007/s004600050085) · [iodine experiment, 2009](https://doi.org/10.1088/0953-4075/42/12/125001) · [cesium, 1978](https://doi.org/10.1103/PhysRevA.17.201) · [cesium, 1998](https://doi.org/10.1103/PhysRevLett.80.684) · [2024 tellurium dimer](https://doi.org/10.1063/5.0190983)

**Rejection tests.** The full-period comparison with gallium through bromine fails as a trend in the central values if any consecutive filled-4d¹⁰ p-block ratio rises between indium and iodine. An endpoint interval allowing an increase defeats a strictly resolved trend. The relative-strength comparison fails if the normalized difference in any homologous pair can vanish. The cesium opening would cease to be interval-resolved outside if its least-open ratio reached the wall.

## Where the core opens

| Element | Anion ratio | Anion reflection | Xenon core | Filled 4d¹⁰ | Krypton core | Filled 3d¹⁰ | Argon core | Neon core | Helium core |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Antimony | 8.218809 | 0.783052 | — | 1.809273 | 1.324921 | 1.751147 | 1.120778 | 2.315172 | 4.119051 |
| Tellurium | 4.571476 | 0.641029 | — | 1.797395 | 1.302260 | 1.747708 | 1.117619 | 2.309109 | 4.114282 |
| Iodine | 3.416501 | 0.547153 | — | 1.721379 | 1.284987 | 1.744505 | 1.114626 | 2.303249 | 4.109605 |
| Xenon | unbound | — | — | 1.696959 | 1.264977 | 1.742124 | 1.111304 | 2.297678 | 4.105016 |
| Cesium | 8.256342 | 0.783932 | 5.947101 | 1.698113 | 1.254202 | 1.737802 | 1.107762 | 2.292396 | 4.100498 |

**DERIVED.** Cesium gives 23.15745/3.89390572743 = 5.947100834 at its first ordinary step, against the forward wall at 3+2√2 ≈ 5.828427125. The corresponding Γ is 0.712110124, r is 1.782903846 and the face apex is 0.418379415. The endpoint interval [5.947085425, 5.947116243] remains wholly outside. This is the first 6s → 5p opening of the xenon core, whose bare principal-shell reference is 36/25. The next element, barium, was already part of the earlier published core survey; the present batch confirms the cesium side from the archived energies. Counting this as a second prediction success would double-count the same data. For the other four elements, the helium-core opening is their largest ordinary ratio.

**RECOGNISED.** The full 4d¹⁰ p-block sequence now falls centrally from indium through tin, antimony, tellurium and iodine. Three of the four adjacent declines have nonoverlapping endpoint intervals. The antimony–tellurium intervals overlap. The filled 4d¹⁰ ratio continues down to xenon; the small central increase at cesium is unresolved. Inside an individual element the 4d¹⁰ and 3d¹⁰ openings also swap rank: 4d¹⁰ is higher throughout antimony's quoted boxes, the boxes overlap for tellurium, and 4d¹⁰ is lower throughout iodine's, xenon's and cesium's boxes.

## What changes after dividing out the bare ratio

**DERIVED.** Compare the filled 3d¹⁰ opening to the filled 4d¹⁰ opening in each corresponding p-block column. The former removal crosses 4s → 3d and has bare reference 16/9. The latter crosses 5s → 4d and has bare reference 25/16. Each 4d¹⁰ jump is smaller in absolute ratio than the corresponding 3d¹⁰ jump. Yet each is *farther above its own bare reference proportionally*. Both inequalities retain their sign across all five pairs of quoted endpoint boxes. This is an energy-ratio comparison. The observed fractional excess includes every physical contribution to the input energies; assigning the whole excess to screening alone requires an additional model.

| Earlier element | Later element | 3d¹⁰ ratio | 4d¹⁰ ratio | 3d¹⁰ / (16/9) | 4d¹⁰ / (25/16) |
|---|---|---:|---:|---:|---:|
| Gallium | Indium | 2.058240 | 1.977239 | 1.157760 | 1.265433 |
| Germanium | Tin | 1.979635 | 1.890771 | 1.113545 | 1.210093 |
| Arsenic | Antimony | 1.930699 | 1.809273 | 1.086018 | 1.157935 |
| Selenium | Tellurium | 1.898167 | 1.797395 | 1.067719 | 1.150333 |
| Bromine | Iodine | 1.869455 | 1.721379 | 1.051569 | 1.101682 |

## Two screening readouts

**DERIVED.** The hydrogen-like over helium-like ratio continues toward one across this batch. The energy gap per unit charge S=(h−b)/Z grows, and the effective screening parameter σ=Z−√(2b) becomes increasingly negative. The energies h and b in those expressions are in hartree. A negative σ means the evaluated helium-like binding exceeds the reference Z²/2. This parameter alone gives no electronic charge density or transport observable.

| Element | h/b | S | σ | Helium-like binding minus bare one-electron reference (eV) |
|---|---:|---:|---:|---:|
| Antimony | 1.026831 | 0.690421 | -0.231229 | 321.622187 |
| Tellurium | 1.026379 | 0.693446 | -0.286650 | 406.725795 |
| Iodine | 1.025946 | 0.696538 | -0.344606 | 498.608018 |
| Xenon | 1.025531 | 0.699708 | -0.405124 | 597.528853 |
| Cesium | 1.025132 | 0.702957 | -0.468303 | 703.858303 |

## Reproduce

```sh
python3 batch11_ladder.py /path/to/data/element_thresholds_20261011.json.gz .
python3 batch11_ladder.py /path/to/data/element_thresholds_20261011.json.gz . --verify-only
python3 batch11_controls.py /path/to/data/element_thresholds_20261011.json.gz batch11_homologs.csv
```

[Compact generated CSV](batch11_sb_cs.csv) · [All ratios, reflections, face apices, logarithmic clocks, endpoint grades and source identifiers](batch11_rungs_detailed.csv) · [Screening and core table](batch11_summary.csv) · [Cross-period endpoint separations](batch11_homologs.csv) · [Audit transcript](batch11_audit.txt)
