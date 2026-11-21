# Batch 9 central-value certificates

The standalone file imports the previous packet's exact ordinary-pair predicate. For adjacent positive encoded energies a and b it verifies that a < b and 2(b−a)² < (a+b)² at every ordinary step. The five lists contain 215 ionization energies, each reparsed from the emitted Lean source and compared with the pinned archive. All 210 adjacent pairs are strictly inside the loop wall. Neither anion data nor uncertainty intervals enter these ordinary central-value results.

A separate theorem states that an atom with Z ≤ 45, under removal of k electrons, has Z−k < 36+10. Consequently the particular [Kr]4d¹⁰ core (which requires 46 electrons) cannot occur in any neutral or positive Nb–Rh ladder. This arithmetic statement says nothing about unrelated excited configurations with holes in a deeper orbital. The Kr-core opening and the first removal from a partially filled 4d configuration remain meaningful and distinct.

Two source mutations falsely mark the Nb Kr-core opening (k=5) and the Rh He-core opening (k=43) outside. Each is also proved false in the positive source. Eight axiom printouts are in lean_run.txt. The electron-count proof uses propext and Quot.sound; the seven data and control declarations also use Classical.choice.

Run with the repository's Lean from its root:

```sh
base=research/2026-11-20-element-paper-loop-wall
python3 "$base/batch9/lean/verify_batch9_lean.py" data/element_thresholds_20261011.json.gz "$base/batch8/lean/OrdinaryGaZr.lean"
```
