# Batch 8 uncertainty boxes

For each quoted uncertainty u, use the closed rational interval [E−u,E+u]. The underlying measurements need not be independent: the full rectangle includes every pairing of allowed input energies. A quoted uncertainty specifies the width used in the computation; it does not guarantee that the true physical energy lies in the rectangle.

Of the 189 physical comparisons, 187 have both uncertainties. Lean certifies each of these 187 over its entire rational rectangle, with 182 strictly inside and 5 strictly outside. All four bound-anion comparisons and the Rb krypton-core opening are outside. The remaining two physical comparisons, Zr k=1 and k=2, both involve IE2 = 13.13 eV, whose uncertainty is missing. At Kr k=0 the affinity data specify no bound ground-state anion. This case has its own constructor, separate from a positive measured energy with missing uncertainty.

If 0 < aₗ ≤ a ≤ aᵤ ≤ bₗ ≤ b ≤ bᵤ, sufficient inequalities for the whole box are

- inside: 2(bᵤ−aₗ)² < (aₗ+bₗ)²,
- outside: (aᵤ+bᵤ)² < 2(bₗ−aᵤ)².

These use conservative, independently bounded numerator and denominator terms; they resolve every defined box here. The generic lemmas in IntervalWall.lean derive the wall inequality for every rational pair in a certified box, including both endpoints. The generated lists retain missing uncertainties as none. A concrete zirconium theorem and a rejected source mutation guard against mistaking a missing uncertainty for zero.

From the repository root, with Lean 4.34.1 active:

```sh
base=research/2026-11-20-element-paper-loop-wall/batch8
python3 "$base/intervals/verify_intervals.py" data/element_thresholds_20261011.json.gz "$base/ladder/batch8_ladder.py"
```

The generator reads the archive after checking its SHA-256 and reads the literal affinity table from the batch-8 generator without executing that file. The compiled module and the false-control variant live in a temporary directory. The saved run lists all 11 public theorem audits.
