# Claims and their status

Status key:

- **Literature**: proved in the cited prior work (not re-proved here).
- **Lean**: proved in Lean in this repository.
- **Numeric**: checked numerically by [`checks/check_peel.py`](checks/check_peel.py) on
  30 October 2026 (floating point or small finite cases; not a proof).
- **Drawing**: a convention chosen for the picture, not a mathematical fact about the objects.
- **Proposal**: part of the synthesis, or an observation in the drawing; not a theorem.

All panel numbers are for T(2,3) at the artifact's default settings (step `ln 5`, depth 3, slider
21 of 109) unless stated.

## Quaternion side

| # | Claim | Status | Source |
| :-: | :--- | :--- | :--- |
| Q1 | There are 48 integer quaternions of norm 5; up to sign, exactly six have odd real part and even `i, j, k` parts: `1 ± 2i, 1 ± 2j, 1 ± 2k`. | Numeric (complete enumeration) | `check_peel.py` |
| Q2 | Every integer quaternion of norm `5^L` with odd real part and even `i, j, k` parts, not divisible by 5, is ± exactly one reduced word in the six generators. Unique only after this normalization and up to `±5^r`; it is false read literally (e.g. `2 + i` has norm 5 but is not a generator). | Literature; Numeric for `L = 1, 2, 3` (6, 30, 150 words) | Lubotzky–Phillips–Sarnak 1988, §3 (Cor. 3.2, per the fact-check of 30 Oct 2026); `check_peel.py` |
| Q3 | So, modulo `±5^r`, the group they generate is free and its Cayley graph is a 6-regular tree that never closes. | Literature | LPS 1988 |
| Q4 | Each step `1 + 2u` is drawn as a hyperbolic boost of length `ln 5 = 1.6094` along `u`. Over the reals `(1 + 2u)/√5` is a rotation, not a boost; the length `ln 5` matches one edge of the 5-adic tree (eigenvalue ratio 5). | Drawing | Artifact; fact-check of 30 Oct 2026, item 2 |
| Q5 | LPS freeness does **not** prove that the drawn group of boosts is free or discrete. | Caveat (no claim made) | fact-check of 30 Oct 2026, item 2a |
| Q6 | Depth 3 of the six-way tree has `1 + 6 + 30 + 150 = 187` nodes (panel: "187 (his)"). | Numeric | `check_peel.py` |
| Q7 | The `ln 7` option ("Garrett's drawing", step 1.9459) is a drawing choice. With six branches it is **not** the LPS tree for `p = 7`, which is 8-regular. | Drawing | Artifact; fact-check of 30 Oct 2026, item 2d |

## The peel coordinate (VOTKP)

| # | Claim | Status | Source |
| :-: | :--- | :--- | :--- |
| V1 | For a ratio `z > 0`, `Γ = (z − 1)/(z + 1) = tanh(½ ln z)`; at `z = 5`, `Γ = 2/3`. | Lean (`smith_identity`); Numeric | VOTKP Theorem 8.1; [`VOTKP/Smith.lean`](../VOTKP/Smith.lean) |
| V2 | The hyperbolic distance from the centre of the Smith disk is `ln((1 + Γ)/(1 − Γ)) = ln z`, so a ratio-5 step has length `ln 5`. Lean proves the identity `(1 + Γ)/(1 − Γ) = z`; the Poincaré metric itself is not formalized. | Lean (identity only) | VOTKP Corollary 15.2; `hyperbolic_length`; [`LIMITATIONS.md`](../LIMITATIONS.md) |
| V3 | Peel steps add like velocities: `tanh(a + b) = tanh a ⊕ tanh b`. This is a one-dimensional statement. Boosts along **one** axis compose this way; boosts along different axes compose to a boost plus a rotation (Thomas–Wigner). The artifact's "steps compose as boosts (Theorem 15.1)" is literal on one axis only. | Lean (one axis); Numeric (two axes do not give a pure boost) | VOTKP Theorem 15.1; `tanh_add'`, `block_succ` |
| V4 | Reading a quaternion step that multiplies the norm by 5 as a peel step with ratio `z = 5`. | Proposal | This synthesis |

## In the drawing

| # | Claim | Status | Source |
| :-: | :--- | :--- | :--- |
| D1 | Three straight steps add exactly: `3 ln 5 = 4.8283`. | Numeric | Panel; `check_peel.py` |
| D2 | Two steps on one axis then one 90° turn, `(i, i, j)`, have length `4.1757`, shorter by `0.6526`; `cosh d = cosh(2 ln 5)·cosh(ln 5)`. With `ln 7`: `5.8377` and `5.1652`, shorter by `0.6726`. | Numeric | Panel; `check_peel.py` |
| D3 | "A turned path is shorter" holds **only in the drawing**. In the LPS tree every reduced 3-step path has length 3 edges; the saving belongs to the picture. | Drawing | fact-check of 30 Oct 2026, item 2b |
| D4 | The "one 90° turn" path, as the shortened path the panel reports. `(i, j, k)` gives 3.5589, a different path that the panel does not use. | Proposal (observation in the drawing) | Panel; `check_peel.py` |

## Knot side

| # | Claim | Status | Source |
| :-: | :--- | :--- | :--- |
| K1 | A two-bridge knot group has the presentation `⟨a, b \| w a = b w⟩`; the artifact's `a·W·b⁻¹·W⁻¹ = 1` is the same relation with `W = w⁻¹`. The relation has 6 letters for T(2,3) and 10 for T(2,5). | Literature; Numeric (lengths) | Schubert 1956; Riley 1984; panel |
| K2 | "Real peripheral curve" is this atlas's name for the real points of the knot's eigenvalue variety (A-polynomial curve), where `M` and `L` are real. It is not a standard term. | Definition | Cooper–Culler–Gillet–Long–Shalen 1994 |
| K3 | Where `\|M\| ≠ 1` the representation is conjugate into SL(2,R), and the meridians are boosts of length `2x = 2 ln\|M\|`. At the default point `x = 0.440`, `\|M\| = 1.5527`, meridian boost `0.8800`, `tanh x = 0.4136`. At `\|M\| = 1` a meridian is a rotation or parabolic, not a boost. | Literature (standard); Numeric (T(2,3), T(2,5)) | fact-check of 30 Oct 2026, item 4; `check_peel.py` |
| K4 | The longitude commutes with the meridian and is a boost of length `2\|y\|`, `y = ln\|L\|`. For T(2,3), `y = −6x = −2.64` (A-polynomial `L·M⁶ + 1`), boost `5.28`; for T(2,5), `y = −10x = −4.40`, boost `8.80`. The sign depends on orientation and mirror image. | Numeric (from a real SL(2,R) representation, longitude `(ab)ⁿ a⁻²ⁿ`) | Panel; `check_peel.py` |
| K5 | The relation loop closes (panel: distance `0.0e+0`, 6 steps). This is **automatic**: every representation satisfies the relation by definition. It checks the numerics; it is not a finding. | Numeric (residual 8e-16 for T(2,3), 6e-15 for T(2,5)) | `check_peel.py` |
| K6 | These boosts act on the flat disk through the ball's centre, identified with VOTKP's Smith disk. | Drawing / Proposal | Artifact |
| K7 | "The traceless meridian meets L = 1" (Boundary torus view) is claimed for **every knot in this atlas**, not every knot. No general source was found. | Not checked here | Artifact; fact-check of 30 Oct 2026, item 4 |

## The headline

| # | Claim | Status | Source |
| :-: | :--- | :--- | :--- |
| H1 | "The knot's tree closes where his does not." It contrasts a free group with a one-relator group, which is true by algebra, and the closing is automatic (K5). It is an **illustration**, not a theorem and not evidence of a deeper link. | Proposal (illustration) | Artifact |
| H2 | One picture holding the LPS tree, the knot's real meridian and longitude boosts, the relation loop and the one-turn path, with the VOTKP peel coordinate as the shared ruler, shown for the knots in this atlas. | Proposal (the synthesis) | This folder |

## Checked and not checked

- **VOTKP theorem numbers.** Theorem 8.1, Corollary 15.2 and Theorem 15.1 say what the artifact
  uses them for, in both places checked: the Lean docstrings in [`VOTKP/Smith.lean`](../VOTKP/Smith.lean)
  (written from paper v1.1) and the text of paper v2.9 (13 October 2026). Not checked against the
  latest published version of the paper.
- **Prior-work citations.** The bibliographic details below come from a fact-check made for this
  folder; the papers themselves were not re-opened on 30 October 2026.
  - A. Lubotzky, R. Phillips, P. Sarnak, "Ramanujan graphs", *Combinatorica* 8 (1988) 261–277.
  - H. Schubert, "Knoten mit zwei Brücken", *Math. Z.* 65 (1956) 133–170.
  - R. Riley, "Nonabelian representations of 2-bridge knot groups", *Quart. J. Math.* 35 (1984) 191–208.
  - D. Cooper, M. Culler, H. Gillet, D. D. Long, P. B. Shalen, "Plane curves associated to character
    varieties of 3-manifolds", *Invent. Math.* 118 (1994) 47–84.
- **Garrett.** Named only as the artifact names him, for the drawing; not identified further.
- **Other views.** The Knots, Boundary torus, Curve stack and Quaternion ball views, and the 26-knot
  census data, are not checked in this folder.
- **The slider's other points and the other 24 knots** are not checked; `check_peel.py` covers
  T(2,3) and T(2,5) at `x = 0.44` only.
