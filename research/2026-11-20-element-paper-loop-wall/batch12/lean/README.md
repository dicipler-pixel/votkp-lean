# Barium through neodymium in exact threshold arithmetic

The rational-valued results use 290 ionization energies and their reported uncertainties from the pinned archive, plus five electron affinities from Ning and Lu (2022), Table 3. The script compares the five elements’ complete printed energy columns and both printed reflection columns against the source fractions. It separately reparses the 290 new Lean energy/uncertainty literals. A rectangular bound means that each true input falls in its stated interval. The certificates make no distributional or confidence-coverage assumption.

## The wall call and the direction

All 285 ordinary central ratios and all 285 ordinary uncertainty rectangles fall inside the loop wall. The five bound-anion rungs lie outside even at their least favorable corners. On the anion central values Lean also checks Γ₀ = η/χ, ω/η = 1/(2Γ₀²), and ω < η, using Pearson finite-difference hardness η, Mulliken electronegativity χ and ω = χ²/(2η). The 1,770 ordinary central steps from hydrogen through neodymium still admit exactly the interval

    nitrogen’s 552.06741 / 97.8901 ≤ cutoff < caesium’s 23.15745 / 3.89390572743.

For every new ordinary box the minimum forward ratio is at least one and the maximum is strictly below 4.1. Neodymium has the only new box that can realize equality with one. At its tenth ordinary step the thresholds 152 ± 8 eV and 168 ± 8 eV (both archive grade T, reference L582) meet at 160 eV. The central Γ is 1/20. The admissible endpoint pair (160, 160) has Γ = 0. This distinction matters for any claim of a strictly signed step based on the stated widths.

Within each element the helium-core opening strictly outranks all its other ordinary steps, for every simultaneous rational realization in the supplied boxes. The helium-core opening itself falls strictly as Z increases from 56 to 60; adjacent elements’ squared-reflection ranges are disjoint. Sign is nonnegative over these reference boxes, so squared-reflection order agrees with forward ratio order.

## Following the 54-electron middle ion

The hypothesis tested in this comparison is that the ratio, indexed by k = Z − 54, falls across all six elements even when the reported uncertainties are propagated. The falsifier is an overlap or reversed order between any adjacent pair of intervals. Lean checks all five strict comparisons.

| Element | k | Lowest z | Central z | Highest z |
|---|---:|---:|---:|---:|
| Caesium | 1 | 5.947085425 | 5.947100834 | 5.947116243 |
| Barium | 2 | 3.582754939 | 3.583009141 | 3.583263343 |
| Lanthanum | 3 | 2.601431856 | 2.604641946 | 2.607852237 |
| Cerium | 4 | 1.768928620 | 1.776133962 | 1.783342819 |
| Praseodymium | 5 | 1.354637027 | 1.425343299 | 1.496172582 |
| Neodymium | 6 | 1.068181818 | 1.178571429 | 1.300000000 |

Taking 36/25 as the nominal hydrogenic 6s-to-5p reference, the central praseodymium reading is below it. Within the praseodymium rectangle, three pairs with first threshold 57.53 eV and second threshold respectively 78, 82.8432 and 86 eV realize all three possibilities: below, exactly on, and above 36/25. For neodymium every admissible ratio is strictly below 36/25.

The comparison tracks **electron count**. The 54-electron ion’s actual ground configuration must be read for each element. For neodymium the assignment is disputed. ASD gives [Cd]4f²5p⁴ for the intermediate 54-electron ion. Table A.2 of Carvajal Gallego et al. (2024) reports three calculations assigning the closed 5p⁶ configuration instead. Both energy inputs are archive grade T, and the count-based proof applies under either assignment. The 36/25 number describes the specified bare shell model; the two removals need their own configuration assignments. These finite comparisons do not give a universal lower bound or identify an orbital from energy alone. See the [configuration snapshots and openings](../ladder/asg_openings.csv) and the [channel check](../xe_sequence/).

## Reproduction

Use Lean 4.34.1 and Python 3. From the repository root:

```sh
paper=research/2026-11-20-element-paper-loop-wall
python3 "$paper/batch12/lean/verify.py" --lean /path/to/lean
```

The verifier checks the archive SHA-256, regenerated source, serialized energies and reflections, builds each imported module in a fresh directory, prints the axiom dependencies and attempts five named false claims. It uses the existing batch-10 power-bound theorem and batch-11 ordinary cutoff proof as imports. The generic implications are rational theorems. Ion configurations come from spectroscopy and do not follow from these arithmetic proofs.

[Threshold archive](../../../../data/element_thresholds_20261011.json.gz) · [Affinity table](../ladder/affinities.csv) · [Ning and Lu (2022)](https://doi.org/10.1063/5.0080243)
