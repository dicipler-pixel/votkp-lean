# Gallium–zirconium ordinary peel certificates

These 20 core Lean declarations cover the 345 ordinary adjacent pairs for Z = 31–40, two nickel display corrections, and mixed-face checks. The reference values are decimal rationals from the pinned archive. For positive adjacent thresholds a and b, the ordinary certificate compares 2(b−a)² with (a+b)². It checks strict inequalities and positive increasing energies at each pair. The anion, input uncertainty, and material transport are separate questions.

Every one of the 160 ordinary pairs for Ga–Br is strictly inside. Among 185 ordinary pairs for Kr–Zr, only Rb k=1 is strictly outside. The tests operate on consecutive entries in each complete Z-row energy list. Public theorem names and their axioms are printed in [lean_run.txt](lean_run.txt).

For two forward face ratios b/a and d/c, the sign of (b−a)²(d−c)² − 16abcd gives the two-face comparison. Two symbolic polynomial identities connect that score to Γ₁²+Γ₂²−1 and to the equal-face wall. The tested C and N He-core faces together give a positive score. The Rb k=1 and Sr k=2 Kr-core faces together give a negative score. These are atomic face comparisons on model inputs.

The positive source includes four explicit negative propositions. The checker then injects the opposite claims one by one into temporary copies and checks that Lean rejects each change. The nickel test pins the two six-place display intervals directly from the archive and rejects the intervals arising from 1750 eV.

From the repository root, with the repository's Lean 4.34.1 active, run the following command using this folder's path.

```sh
python3 PATH_TO_THIS_FOLDER/verify_lean.py data/element_thresholds_20261011.json.gz
```

Only the Python standard library and core Lean are needed. The checker compares a regenerated source with the checked-in bytes before invoking Lean. To supply a different Lean executable explicitly, use `--lean /path/to/lean`.
