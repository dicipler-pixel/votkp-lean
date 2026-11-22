# Periodic Table of Elemental Peels, v1.1

**Jeromie Beasley · 21 November 2026**

An interactive periodic table, hydrogen to astatine, that orders the elements by how their electrons peel away. The page itself is the separate file `Periodic_Table_of_Elemental_Peels_v1_1_Jeromie_Beasley.html` in this record. It opens offline in any browser.

## The rule

- A peel step is the ratio of successive removal energies, z = IEₖ₊₁ / IEₖ.
- Its reflection is Γ = (z − 1)/(z + 1) = tanh(½ ln z).
- The loop wall is Γ² = ½, equivalently z = 3 + 2√2 = 5.828427. It is derived from geometry, not fitted: it is where two equal faces at right angles stop closing a loop.
- Each element's address is where two of its steps fall: the anion rung (electron affinity to first ionisation energy), and the first opening of its noble-gas core.

## Results in this record

- **3,570 ordinary removal steps, 8 outside the wall.** All eight are first openings of a noble-gas core: lithium, beryllium, boron and carbon (helium core), and sodium, potassium, rubidium and caesium (neon, argon, krypton and xenon cores).
- **53 of 65 scored anion rungs outside the wall.** The wall is the line where electrophilicity equals hardness, ω = η.
- **The data allow cutoffs only in [5.80790, 5.86654),** from silver's anion rung to silicon's (Lean: `window_silver_silicon`).
- **Only 3 + 2√2 makes the two-face rule agree** in its product and sum forms (Lean: `TwoFaceForms.lean`, `BoundaryAgreement.lean`).
- **The same half-power line in the visible:** all 35 metals with optical data reflect above |Γ|² = ½ and none of the 6 non-metals do.
- **Registered prediction:** francium's radon-core opening is inside the wall if IE₂(Fr) < 23.738 eV (`PREDICTION_FRANCIUM_20261121.md`).

## Contents

- `table/`: the table's data (`ptable_data.json`) and its builder `build_ptable_data.py`; the v1 standalone page, the v1.1 review builder and validator (`build_review.py`, `validate.py`), and the browser test.
- `data/`: the pinned ionisation archive `element_thresholds_20261011.json.gz` and the extended hydrogen-to-astatine CSV with source and status for each affinity.
- `lean/`: the core Lean 4.34.1 proofs, with no Mathlib. `LoopWall.lean` has 140 theorems; also `OpeningMap.lean`, `TwoFaceForms.lean`, `BoundaryAgreement.lean`, the axiom audits, and 11 false controls. Run `sh run_checks.sh`; the output is in `run_checks_output.txt`.
- `checks/`: the independent recomputes of the beryllium–rubidium mixed pair and the two-face consistency test.

## Reproduce

    python3 table/build_ptable_data.py      # rebuild the data (paths inside the script point to the archive)
    cd lean && LEAN=/path/to/lean sh run_checks.sh

## Licence

Code, Lean, scripts and data files: MIT. Text: CC BY 4.0. Credit Jeromie Beasley. See `LICENSE.md`.

Source repository: https://github.com/dicipler-pixel/votkp-lean/tree/element-paper/loop-wall/research/2026-11-20-element-paper-loop-wall

## Checksums (SHA-256)

- interactive page: 68f8c367bc137be250b28c2489923080ca0270a4b99a770e20cf38159a7a6a90
- data/element_thresholds_20261011.json.gz: 75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c
- table/ptable_data.json: bc1600fa5d580bacefe2cae896bb50eca76e2d4284c79c0876fb7a573929d3c5

*AI-assisted: computations, page building, Lean formalisation and checks were carried out with Claude (Anthropic) and Codex (OpenAI), from the author's ideas and earlier papers.*
