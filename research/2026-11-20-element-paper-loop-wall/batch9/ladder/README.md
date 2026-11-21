# Niobium through rhodium

Inputs are the original NIST-derived archive at commit 182da01a14b10ce1e07e247565466d01822121c5. The Python generator reads the compressed archive directly, writes the simple CSV and a detailed CSV of face coordinates, then reopens the simple CSV and checks its energy, grade, order, endpoints and both displayed ratios from independently rounded integer fractions. Existing estimate grades remain attached to the energies. The quoted uncertainty endpoints form conservative rectangles under the quoted individual ranges. They do not supply a joint probability model.

Run from this directory with the archive path and an output directory.

```sh
python3 batch9_ladder.py /path/to/data/element_thresholds_20261011.json.gz .
python3 batch9_ladder.py /path/to/data/element_thresholds_20261011.json.gz . --verify-only
python3 batch9_rank_control.py /path/to/data/element_thresholds_20261011.json.gz
```

**DERIVED.** The published CSV contains 215 archive energies and five affinity inputs. All 210 ordinary steps are inside the loop wall. Four experimental electron affinities give outside anion rungs. Technetium's estimated affinity also gives an outside rung conditional on that input. The largest ordinary step for each element opens the helium-like core. In this batch, 203 of 215 interval tests have both quoted uncertainties and retain their central decision. The audit identifies the twelve rows with incomplete uncertainties. [Energy source](https://github.com/dicipler-pixel/votkp-lean/blob/182da01a14b10ce1e07e247565466d01822121c5/data/element_thresholds_20261011.json.gz)

**MEASURED.** Ning and Lu give experimental affinities of 0.91740(7) eV for niobium, 0.74723(8) eV for molybdenum and 1.046270(20) eV for ruthenium. For rhodium the 2026 primary measurement is 1.14273(5) eV, updating the 2022 evaluation's 1.14289(20) eV. Source tags EA22 and Rh26 in the machine CSV correspond to these two sources. [Ning and Lu (2022), Table 3](https://doi.org/10.1063/5.0080243) · [Chen et al. (2026)](https://doi.org/10.1088/1674-1056/ae5173)

**DERIVED FROM AN ESTIMATE.** The same 2022 evaluation labels technetium's 0.636 eV affinity calculated/semiempirical and gives no uncertainty. This is EA22-estimate in the CSV. The corresponding central ratio is 11.193993711. For a bound anion and forward rung, the critical affinity equals IE₁(3−2√2) = 1.221492497 eV. A future affinity below that value leaves the rung outside, and an affinity between that value and IE₁ puts it inside. Equality lands on the wall. [Ning and Lu (2022), Table 3](https://doi.org/10.1063/5.0080243)

**DERIVED.** The 36-electron krypton core and the 28-electron closed 3d¹⁰ subshell have separate ordinary openings. Their relative ranks swap between molybdenum and technetium. With molybdenum, even the lowest permitted Kr-core ratio exceeds the highest 3d¹⁰ ratio by 0.025404446. For technetium the upper Kr-core ratio falls below the lower 3d¹⁰ ratio by 0.005722226. Run the exact endpoint check to reproduce the separation using all input digits. The krypton core opens by 4d→4p, both n=4, whereas the filled 3d¹⁰ threshold compares 4s→3d. The neutral and positive ions here have fewer than the 46 electrons needed for a closed [Kr]4d¹⁰ configuration. Rhodium's negative ion does have 46 electrons, but its observed ground term is ³F₄, incompatible with a pure closed 4d¹⁰ shell. No 4d¹⁰ opening is assigned. [NIST ASD](https://doi.org/10.18434/T4W30F) · [Rhodium anion measurement](https://doi.org/10.1088/1674-1056/ae5173)

**RECOGNISED.** The small increase in the central 3d¹⁰-opening ratio from niobium to molybdenum is less resolved than the within-element rank swap. Those two 3d¹⁰ endpoint intervals overlap. The distinction prevents the turning point in the rounded central values from being read as a measured reversal. The detailed CSV gives the start and end grades, reference codes, quoted uncertainties, rung clocks, ratios, reflections and intrinsic face apices.
