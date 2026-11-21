# Anion chemistry from hydrogen through neodymium

[49 anion chemistry rows](anion_chemistry_h_nd.csv) · [11 elements without a ground-state anion rung](no_bound_anion_h_nd.csv) · [source manifest](source_hashes.csv) · [historical ladder fingerprints](historical_input_hashes.csv)

**DERIVED, conditional on the inputs.** The eight anions inside the loop wall are fluorine, sulfur, chlorine, selenium, bromine, silver, tellurium and iodine. Forty other measured affinities give outside rungs. All 48 measured-affinity rows keep their classifications over their complete reported input boxes. The 49th row uses the 0.636 eV *estimated* affinity of technetium. Its central-value class is outside. Its uncertainty and interval fields are empty. This accounts for each of the 60 elements through neodymium.

## What the CSV measures and derives

**MEASURED/ESTIMATED.** I is the pinned ground-state first ionization energy and A is the adopted ground-state electron affinity. Both are in eV. Every row preserves the ASD uncertainty, grade and literature reference for I, plus the year, link, original value, units and uncertainty for A. On selenium the source gives cm⁻¹. The generator uses A(eV) = A(cm⁻¹) × 100hc/e with the exact SI defining constants and retains all digits until serialization. [Pinned thresholds](https://github.com/dicipler-pixel/votkp-lean/blob/8e5d44f1d9e36f242e6522bbe70cea18fb315c7a/data/element_thresholds_20261011.json.gz) · [Adopted H–Sn evaluations](../../batch10/robust/CUTOFF_INTERVALS_H_SN.md) · [Sb–Cs sources](../../batch11/ladder/README.md) · [Ba–Nd sources](../ladder/README.md)

**DERIVED.** For positive I>A, absolute hardness in the paper is η=(I-A)/2, Mulliken electronegativity χ=(I+A)/2, and electrophilicity ω=χ²/(2η). Then Γ₀=η/χ, and ω/η=1/(2Γ₀²). The ratio’s unit-free comparison with one can be made with a single exact quadratic. The new column `signed_wall_slack` is

**s = 2Γ₀² − 1 = (I² − 6IA + A²)/(I + A)².**

Positive s means outside, negative inside, and zero on the wall. This is an *even* power-based side report under reversal. The signed peel reflection is retained separately in `Gamma0`.

**DERIVED.** The Critical EA column asks what affinity would put this particular atom at the forward wall if its pinned I held fixed. Its value is A★=I/(3+2√2)=I(3-2√2). The additional signed difference A-A★ has eV units and is positive on the inside. Silver is 4.594 meV above its critical affinity, silicon is 9.086 meV below its own, and copper is 89.857 meV below its own. This orders the margins by an absolute energy perturbation. `slack_lo`, `slack_hi` and the two bounds on ω/η use each measured atom’s separate uncertainty in both I and A. These are deterministic corner ranges conditional on the quoted intervals, with no assigned joint probability.

**DERIVED.** Silver’s slack lies in [−0.002509247, −0.002482865]. Silicon’s lies in [0.004600389, 0.004606293] using the paper’s frozen elemental reference. Batch 10 separately tested all three stable silicon isotope affinities. A changed reference capable of moving an endpoint across zero would overturn that guaranteed label. For technetium, a measured positive affinity below 1.221492497 eV would preserve the outside call at central I. An affinity between that boundary and I would give inside. [Silicon isotope controls](../../batch10/robust/CUTOFF_INTERVALS_H_SN.md) · [Technetium estimate](https://doi.org/10.1103/PhysRevA.65.064502)

## The convention test

**DERIVED.** Some authors call the entire gap H=I-A=2η the hardness. A comparison with a conventionally named electrophilicity has to specify whether the numerator was also recomputed. This table gives both transformations using the *same atom*.

| Quantity reported | Exact value in the paper’s convention | At the wall | Inside |
|---|---:|---:|---:|
| ω/η with half gap | ω/η | 1 | >1 |
| Paper’s ω divided by full gap H | (ω/η)/2 | 1/2 | >1/2 |
| Recomputed Ω=χ²/(2H), divided by H | (ω/η)/4 | 1/4 | >1/4 |
| χ/H | 1/(2Γ₀) | 1/√2 | >1/√2 |

**DERIVED.** As a false control, choose χ=3,η=2. These values correspond to I=5 eV and A=1 eV. Original ω/η=9/8>1. Recomputed Ω/H=9/32>1/4. Comparing that last reading against one falsely moves the same inputs outside. The Lean file establishes the rescalings for general positive rational η, gives the proper comparison on either side, and kernel-checks this counterexample. An exact boundary witness uses the squared coordinate χ²=2,η=1. [Hardness definitions](https://doi.org/10.1021/ja00364a005) · [Electrophilicity index](https://doi.org/10.1021/ja983494x) · [Lean source](HardnessConventions.lean) · [Axiom output](lean_audit.txt)

## Source continuity and reproduction

**CHECKED.** The 10 CSVs representing the earlier hydrogen–cesium ladders have the same bytes as the Git objects at `b2f90be53cf595aee388f5924da9bd32e5728db8`. This covers 1,594 historical rows, including 44 numeric anion inputs. The companion uses the batch-10 evaluated affinity inputs. There are two historical display differences against these exact inputs. Scandium’s early CSV used 0.179380 eV, while the later evaluated record uses 0.179378(22) eV. Selenium’s early exact-constants conversion was serialized to a finite decimal. Both original decisions survive. The remaining 42 historical numeric affinities agree exactly. Each earlier CSV and each input used here is opened read-only. [Scandium and yttrium measurement, 2023](https://doi.org/10.1063/5.0124882) · [Selenium measurement, 2026](https://pubmed.ncbi.nlm.nih.gov/41626821/)

**SOURCE NOTE.** For neodymium the direct Fu et al. (2020) paper and Ning–Lu (2022), Table 3, agree on 0.09748(31) eV. Table 3 also prints 786.3(26) cm⁻¹. Fu’s body, Table IV and conclusion instead give 0.09749(32) eV, consistent with standard conversion of 786.3(26) cm⁻¹. The secondary 0.09749(33) eV can be compared as a different decimal rendering of the same measurement. The full source variants, including the changed first ionization energy, are quantified in the companion ladder. [2022 evaluation, author PDF](https://info.phys.tsinghua.edu.cn/henucl/ning/148.pdf) · [2020 measurement](https://doi.org/10.1103/PhysRevA.101.022502) · [Source substitutions](../ladder/source_variants.csv)

```sh
d=research/2026-11-20-element-paper-loop-wall/batch12/chemistry
a=data/element_thresholds_20261011.json.gz
python3 "$d/chemistry_all.py" "$a"
python3 "$d/verify_companion.py" "$a"
lean "$d/HardnessConventions.lean"   # Lean 4.34.1
```

The generator uses exact rational arithmetic for all classifications. An independent decimal implementation reparses the displayed table, recomputes each reported chemistry field, and checks all four corners of every complete box. A changed convention, archive digest, source-file identity, historical ladder or last displayed digit of a checked field produces an error.
