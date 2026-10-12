<div align="center">

# VOTKP: The Vector of Traits Kept under Peeling — Lean proofs

**The exact results of *VOTKP*: peel shape as a Smith reflection coordinate, peel steps that add like velocities, the shell part `(2n − 1)/(n² + (n − 1)²)` of a step across a shell wall, the thin-film echo and its exact circle, and the finite peel theorems, checked by Lean.**

[![Lean proof check](https://github.com/dicipler-pixel/votkp-lean/actions/workflows/build.yml/badge.svg)](https://github.com/dicipler-pixel/votkp-lean/actions/workflows/build.yml)
![Lean](https://img.shields.io/badge/Lean-v4.34.1-blue)
![Theorems](https://img.shields.io/badge/theorems-120-2EA043)
![sorry](https://img.shields.io/badge/sorry-0-2EA043)
[![Paper DOI](https://img.shields.io/badge/paper-10.5281%2Fzenodo.23011140-blue)](https://doi.org/10.5281/zenodo.23011140)
![Code: MIT](https://img.shields.io/badge/code-MIT-lightgrey)
![Text: CC BY 4.0](https://img.shields.io/badge/text-CC%20BY%204.0-lightgrey)

Jeromie Beasley

</div>

---

Companion to *VOTKP: The Vector of Traits Kept under Peeling — Elemental Peeling of Atoms and
Knots*, version 1.1, 25 September 2026
([10.5281/zenodo.23011140](https://doi.org/10.5281/zenodo.23011140)).

## What is proved

| File | Theorems | Paper | What it does |
| :--- | :-: | :--- | :--- |
| [`VOTKP/Smith.lean`](VOTKP/Smith.lean) | 21 | §8.1, §8.7, §15.2–15.4 | `(z − 1)/(z + 1) = tanh(½ ln z)`; `tanh(a + b) = tanh a ⊕ tanh b`, so a block of removals is the `⊕`-sum of its steps; `⊕` commutes and associates, so the ladders `1, 2, 6` and `1, 3, 6` share the composite `5/7` with different steps; the hyperbolic length `ln z`; the screening/shell split and the shell-part wall values `3/5, 5/13, …, 13/85` with their Pythagorean triples; scale blindness of ratios; a negative ratio leaves the disk |
| [`VOTKP/Film.lean`](VOTKP/Film.lean) | 12 | §6.4, Theorems 6.1–6.2, §15.2 | The film reflection `(Γ + x)/(1 + Γx)` is `Γ ⊕ x` by definition, with first-order echo `1 − Γ²`; the echo series; the exact identity `\|r\|² − \|a\|² = (A\|x\|² + 2 Re(Cx))/\|1 + ax\|²` with `A = 1 − \|a\|⁴`, `C = ā(1 − a²)`; for any `A > 0` and `C`, `A\|x\|² + 2 Re(Cx) > 0` exactly when `x` lies outside a circle through the origin (with these `A` and `C` and `\|a\| < 1`, the two together decide rise or fall; the combined statement is not stated in Lean); one radius cannot decide (`49/121` against `1/9`); the zero-phase stack telescopes |
| [`VOTKP/Peel.lean`](VOTKP/Peel.lean) | 18 | §5, §15.2 | Positive-channel peel (form, order, kernels); form tomography; Schur boundary memory; the four-reading coefficient and its sign; phase-reference recovery and its error bound; the cumulant witness (`c₃ = 0` against `3/50`); the transmission closed form, shared records `T(0) = T(√2) = 1/2`, later outcomes `0` against `4/5` and the gap `79,600,000/400,039,601`; one-energy snapshots; the reduced-product associator |
| [`VOTKP/Knot.lean`](VOTKP/Knot.lean) | 1 | Appendix A.12 | `(1 − ω)/(1 − ω̄) = −ω` on the unit circle, for `ω ≠ 1` |
| [`VOTKP/Ordinal.lean`](VOTKP/Ordinal.lean) | 5 | §18, control 41 (v1.2) | Zero permutation entropy at delay 2 holds for the ladder `1,…,6` and for the same ladder with one transposition, so it does not identify the defect; delay 1 does |
| [`VOTKP/Energy.lean`](VOTKP/Energy.lean) | 17 | New §21 | Finite binding/removal ledger, ground-energy differences, telescoping, reference shifts, anchored peel inversion and negative controls; see [section and visual](docs/energy-state-atlas.md) |
| [`VOTKP/Observer.lean`](VOTKP/Observer.lean) | 7 | Theorem 3.1 | The finite linear predictive quotient: identical futures iff the difference lies in `N = ker 𝒪`; `N` is `L`-invariant; `dim V/N = rank 𝒪`; every output-preserving autonomous summary forgets only directions in `N`, and `V/N` is one; the present observation closes iff `ker R` is `L`-invariant; the Cayley–Hamilton horizon |
| [`VOTKP/Curvature.lean`](VOTKP/Curvature.lean) | 5 | Theorem 4.1 | The spectrum `δ ∓ E(a)` of `H_M(a)`; `U(a) = U(0) + μ_eff a²/2 + O(a⁴)` with the remainder bounded explicitly; the Bloch slope `c/δ`, `g_aa(0) = c²/4δ²`, `χ = 2c²/δ = 8δ g_aa(0)`; the critical occupation `r_c` |
| [`VOTKP/Memory.lean`](VOTKP/Memory.lean) | 4 | 5.4, 5.5 | Variation of constants: a peeled layer leaves the kernel `B e^{(t−u)D} C` and forcing `B e^{tD} y(0)`; the transfer `B(zI − D)⁻¹C` vanishes at every `z` off the spectrum iff `B Dʲ C = 0` for `j < q`; the five-site shift shows the bound is sharp |
| [`VOTKP/ThinFilm.lean`](VOTKP/ThinFilm.lean) | 2 | Theorem 6.3 | From the characteristic matrix, the exact film reflection and the shunt law `Y = n_b − ikd(N² − n_b²)` agree at `d = 0` with equal derivative in the real thickness; at the substrate face the law reads `Y = n_b − ikd(N² − n₀²)` |
| [`VOTKP/WallParity.lean`](VOTKP/WallParity.lean) | 3 | Proposition 11.1 | `det((1 − ω)V + (1 − ω̄)Vᵀ) = (1 − ω̄)^{2g} det(V − ωVᵀ)` on the unit circle; the sign of a nonsingular Hermitian determinant is `(−1)^{#negative eigenvalues}`; across a zero of order `m` of `det H`, half the signature change is `≡ m (mod 2)` |
| [`VOTKP/Scaling.lean`](VOTKP/Scaling.lean) | 3 | Theorem 15.4 | Second derivatives scale by `λ²` under dilation; pair-Coulomb sums are homogeneous of degree `−1`; if `Hψ = Eψ` then `ψ(λ·)` satisfies `H_λ φ = λE φ` with every mass multiplied by `λ` |
| [`VOTKP/Directed.lean`](VOTKP/Directed.lean) | 22 | §19 | Prop. 19.1: the directed coordinate in `(−1, 1)` without ordering, reversal, `⊕` as a group law on `(−1, 1)`, the telescoping composite, when a step shrinks the distance; Prop. 19.2: `L_rec − D_end = 4 min(R₊, R₋)` and its equality case; Prop. 19.3: lifts `U_b D U_bᵀ` share the spectrum and gap coordinate `tanh ρ` while the ground projector moves at metric `b²`; Prop. 19.4: `𝓛 ≥ a·TV`, Cauchy–Schwarz, `W ≥ w* 𝓛²/T ≥ w* a² L_rec²/4T`; §19.6: equal weights iff `de = 1/τ²`, the `1`/`4` example, equal populations give no friction |
| | **120** | | |

The last seven rows follow the section numbering of version 2.2 (11 October 2026).

What is not proved is listed in [`LIMITATIONS.md`](LIMITATIONS.md).

## Start here: the showcase

[`Showcase.lean`](Showcase.lean) is the one file a reader has to trust. It imports only Mathlib,
defines every notion it uses, contains no proofs, and states twelve headline results as one
`MainTheorem`: the Smith identity, peel steps adding like velocities, order dropping out of the
composite, the shell part at a shell wall, the film echo identity and its decision circle, one
radius not deciding, the telescoping stack, the cumulant witness, the reduced-record witness, the
unit-circle ratio, and control 41.

[`Showcase_WithProofs.lean`](Showcase_WithProofs.lean) proves `MainTheorem` from the library.
Lean accepts that proof only if each library theorem's statement is the showcase statement, so
the 692 lines of the library cannot be proving something weaker than the one page that states
them.

## How it is checked

Every push runs [the proof check](.github/workflows/build.yml) on GitHub:

1. **Build**: every module compiles against Lean v4.34.1 and Mathlib `v4.34.1`.
2. **Independent replay**: every module is re-checked by Lean's separate kernel checker.
3. **Axiom audit**: every named theorem depends only on `propext`, `Classical.choice` and
   `Quot.sound`. No `sorry`, no project axioms, no `native_decide`.
4. **Showcase**: `Showcase.lean` imports only Mathlib and holds no proofs, axioms, `sorry`,
   notation, macros or options; `example : Showcase.MainTheorem := Showcase.main_theorem`
   compiles, so the proved theorem carries exactly the showcase statement.
5. **False controls**: thirteen deliberately wrong claims must fail to compile, for a mathematical
   reason: the shell part at the first shell wall (the Smith reflection of the ratio `4`) being
   `1/2` (it is `3/5`); the ladders `1, 2, 6` and `1, 3, 6` having the same first step; the echo
   `x = −1/5` raising the reflectance; the two channel sets sharing a third cumulant; the shared
   record `T(0)` fixing the later transmission; zero entropy at delay 2 excluding the transposed
   ladder; and the showcase's shell wall altered from `2n − 1` to `2n + 1`, which the proved main
   theorem cannot stand in for; the ground-energy binding sign reversed; equal first
   thresholds asserted to imply equal total binding; the gaps `1` and `3` sharing a friction
   weight; an out-and-back record whose endpoint distance equals its length; the five-site
   shift's fifth Markov parameter being `0`; and the curvature vanishing at half filling.

```bash
lake exe cache get
lake build
python3 scripts/verify.py
python3 scripts/verify_energy_data.py
```

## Licence, citation and AI use

Copyright (c) 2026 Jeromie Beasley. Code and proofs: [MIT](LICENSE). Written text:
[CC BY 4.0](LICENSE-CC-BY-4.0.md). See [`LICENSING.md`](LICENSING.md). Citation metadata is in
[`CITATION.cff`](CITATION.cff); where the files came from is in [`PROVENANCE.md`](PROVENANCE.md);
how AI tools were used is stated in [`AI_USE.md`](AI_USE.md).

## Energy and the element atlas — 11 October 2026

[New section §21](docs/energy-state-atlas.md) applies the energy ledger to all 118 element slots. [Archived inputs](data/element_thresholds_20261011.json.gz) preserve evidence grades and references; [exact arithmetic controls](scripts/verify_energy_data.py) cover 5,847 thresholds, 103 complete ladders and 5,714 peels. This adds finite identities, not new atomic response or decay laws.

![Electronic binding remaining](docs/assets/element-energy-landscape.png)

![Peel shape aligned by electron count](docs/assets/element-peel-landscape.png)
