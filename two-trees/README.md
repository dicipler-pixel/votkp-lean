# Two Trees in One Ball

**Norm Ladders, Peel Steps and Knot Boosts — version 4, 30 October 2026**

Jeromie Beasley. Prepared with AI assistance (Claude, Anthropic); see [`../AI_USE.md`](../AI_USE.md).

[![Two Trees core Lean check](https://github.com/dicipler-pixel/votkp-lean/actions/workflows/two-trees-core.yml/badge.svg)](https://github.com/dicipler-pixel/votkp-lean/actions/workflows/two-trees-core.yml)
![Lean](https://img.shields.io/badge/Lean-v4.34.1%20core-blue)
![Theorems](https://img.shields.io/badge/theorems-159-2EA043)
![sorry](https://img.shields.io/badge/sorry-0-2EA043)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.23847114-blue)](https://doi.org/10.5281/zenodo.23847114)

Zenodo record (paper, code and the interactive Knot Atlas): [10.5281/zenodo.23847114](https://doi.org/10.5281/zenodo.23847114).

The paper: [`paper/Two_Trees_in_One_Ball_v4.pdf`](paper/Two_Trees_in_One_Ball_v4.pdf) (101 pages; every Lean file and
every script with its output is printed in the appendices) and the same text as
[`paper/Two_Trees_in_One_Ball_v4.html`](paper/Two_Trees_in_One_Ball_v4.html).

Garrett's tree is built from the six quaternions of norm 5, `1 ± 2i, 1 ± 2j, 1 ± 2k`. In the peel coordinate of
[VOTKP](https://doi.org/10.5281/zenodo.23011140), a step that multiplies a ratio by `z` has Smith step
`Γ = (z − 1)/(z + 1)` and hyperbolic length `ln z`. Read that way, each generator is a Lorentz boost of length
`ln 5` along its own axis, and the whole tree sits in the Poincaré ball with exact rational coordinates. On the
knot side, the Riley meridians of a two-bridge knot on its real curve are boosts of length `2x`, and the knot
relation closes the word walk into a loop. The paper sets the two trees side by side in one disk: one never closes,
the other does.

## What is proved

| | Result | Grade |
| :-- | :-- | :-- |
| 5.1 | The ln 5 boosts generate a free group: `5^L cosh d` is never divisible by 5 | Lean |
| 5.2 | Free for every whole ratio `z ≥ 2` with an odd divisor | Lean |
| 8.1 | Free for every **even** ratio, so for powers of 2 (ping-pong at the prime `1 + i`) | proved, written |
| 8.2 | So the boost group is free for **every** whole ratio `z ≥ 2` | proved |
| 5.3 | Schottky (free and discrete) exactly above `Γ² = 1/2`, i.e. `z > 3 + 2√2` | proved; inequalities in Lean |
| — | At ln 5 the commutator is a rotation of infinite order: free but not discrete | trace, fixed point and angle in Lean; infinite order proved |
| 8.3 | The ln 5 boost group is **not** conjugate to the Lubotzky–Phillips–Sarnak group in PGL(2, ℚ₅): `tr²/det` is 36/5 against 4/5 | proved |
| 8.4 | At ln 7: `ℓ + (L − 1)δ ≤ d(O, wO) ≤ Lℓ`, `cosh δ = 9/7`, and δ is optimal | proved; ping-pong in Lean |
| 8.5 | The relator polygon's area vanishes on the whole geodesic `|z| = 1/√v`, by a reflection symmetry | proved |
| 8.6 | `tr[a,b] = 2 − v((s − 1/s)² − v)`: the knot commutator turns only when the meridian axes cross, and below `Γ² = 1/2` always does | Lean |
| 8.7 | For T(2,3), T(2,5), T(2,7) the commutator never turns (`tr(ab) = 2cos((2j−1)π/n) < 2`) | Lean |
| 8.8 | Census of 26 two-bridge knots: 19 turn, 7 never (T(2,3), T(2,5), T(2,7), 6₃, 7₅, 8₇, 8₈) | computed, 80–200 digits |

Thomas rotation `tan(θ/2) = Γ²` for every ratio, the exact points of Garrett's caption (`3 ln 7 = 5.838`, `4.742`),
and the trefoil and figure-eight relations over any commutative ring are also in Lean.

## The Lean files

Core Lean 4.34.1, **no Mathlib**: each file is checked with plain `lean <file>`. No `sorry`, no `native_decide`.

| File | Theorems | What it holds |
| :-- | :-: | :-- |
| [`lean/PeelTrees.lean`](lean/PeelTrees.lean) | 74 | quaternions, peel ladder, boosts at ln 5 and ln 7, Thomas rotation, freeness at 5 and 7, knot relations |
| [`lean/PeelTrees2.lean`](lean/PeelTrees2.lean) | 49 | freeness for every ratio that is not a power of 2; Thomas for every ratio |
| [`lean/PeelTrees3.lean`](lean/PeelTrees3.lean) | 7 | the ln 5 commutator: fixed point, trace 196, `cos φ = −527/625`; the ln 7 commutator trace |
| [`lean/PeelTrees4.lean`](lean/PeelTrees4.lean) | 12 | the knot commutator band; torus knots T(2,3), T(2,5), T(2,7) |
| [`lean/PingPong7.lean`](lean/PingPong7.lean) | 17 | the ping-pong at ln 7 on the integer light cone; free of rank 3 |
| | **159** | |

[`lean/controls/`](lean/controls/) holds six deliberately false statements; each must be rejected.

## How it is checked

Every push that touches this folder runs [`check_core.py`](check_core.py) in
[the Two Trees workflow](../.github/workflows/two-trees-core.yml):

1. each file compiles with Lean v4.34.1, with the expected theorem count;
2. no `sorry`, `admit`, `native_decide` or `axiom` declaration in the code;
3. `#print axioms` for every theorem: only `propext`, `Classical.choice`, `Quot.sound`;
4. all six false controls are rejected.

This folder is separate from the VOTKP Mathlib library above it and is not part of that build.

## Not in Lean

- Theorem 8.1 (every even ratio): a written proof, checked on 100,000 exact test points, with negative
  controls at odd ratios. It needs the `(1 + i)`-adic valuation on `ℤ[i]`.
- The distance bound of Theorem 8.4 (it needs real numbers).
- Theorems 8.3 and 8.5 are written proofs with exact and high-precision checks.

## Open

- Whether a non-backtracking word returns to the origin at a ratio that is a power of 2 (none found to length 14).
- What the four non-torus knots that never turn (6₃, 7₅, 8₇, 8₈) share. It is not the Alexander roots.
- Why the limits of `2 − tr[a,b]` as `x → ∞` are squares of numbers `2cos(jπ/n)/m`.
- Whether the geodesic `|z| = 1/√v` is the whole zero set of the polygon area.

## Scripts

[`scripts/`](scripts/) holds every computation behind the computed grades, each with its output. See
[`scripts/README.md`](scripts/README.md).

## References

The full list is in the paper. The main ones: J. Beasley, *VOTKP*, [10.5281/zenodo.23011140](https://doi.org/10.5281/zenodo.23011140);
Lubotzky, Phillips and Sarnak, *Ramanujan graphs* (1988); R. Riley, *Nonabelian representations of 2-bridge knot
groups* (1984); A. F. Beardon, *The Geometry of Discrete Groups* (1983); Garrett (@Ebayednoob), post on the
norm-5 quaternion tree in the Poincaré ball (2026).
