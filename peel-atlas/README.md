# Peel atlas: a quaternion tree and a knot's tree in one hyperbolic picture

Jeromie Beasley, 30 October 2026. Made with AI assistance (see [`AI_USE.md`](AI_USE.md)).

This folder is a dated public record of a synthesis. It is a **proposal and an observation**,
not a new theorem. What is proved, what was only checked numerically, and what is a drawing
choice is listed claim by claim in [`CLAIMS.md`](CLAIMS.md).

**Interactive version.** *Knot Atlas in 3D*, Peel tree view:
<https://claude.ai/artifact/JVPZneCArPgpfRQ9SFt9PV#peel>. It is hosted on Claude's site
(claude.ai), not in this repository, and that site may change or remove it. This folder records
its text and numbers as of 30 October 2026.

## The idea in plain words

There are two trees.

1. **A quaternion tree.** The six quaternions `1 ± 2i`, `1 ± 2j`, `1 ± 2k` each have norm 5.
   After a standard normalization, every quaternion of norm `5^L` is, up to sign and powers of 5,
   exactly one reduced word in these six (Lubotzky, Phillips and Sarnak). So, read that way, they
   generate a free group, and its picture is a tree that branches six ways and never closes.
2. **A knot's tree.** A two-bridge knot's group has two meridians `a`, `b` and one relation
   `a·W·b⁻¹·W⁻¹ = 1` (Schubert; Riley). Its tree branches four ways (`a`, `b` and their inverses),
   and the relation is a loop that closes.

The synthesis puts both in **one Poincaré ball**, using the peel coordinate of
[VOTKP](https://doi.org/10.5281/zenodo.23011140) as the common ruler:

- A step that multiplies the norm by 5 is read as a peel step with ratio 5. In VOTKP that step has
  Smith step `Γ = 2/3 = tanh(½ ln 5)` and hyperbolic length `ln 5` (Theorem 8.1, Corollary 15.2).
  Each quaternion step is **drawn** as a hyperbolic boost of length `ln 5` along its axis.
- On the knot's side, at real points of the knot's eigenvalue variety (Cooper, Culler, Gillet,
  Long and Shalen), with `|M| ≠ 1`, the meridians really are boosts of length `2x = 2 ln|M|` and
  the longitude a boost of length `2|y| = 2|ln|L||`. They act on the flat disk through the ball's
  centre, which is VOTKP's Smith disk.

What the picture then shows, for the knots in this atlas:

- Three straight steps add exactly: `3 ln 5 = 4.8283`. Two steps on one axis and then **one 90°
  turn** give `4.1757`, shorter by `0.6526`. This saving belongs to the drawing. In the tree
  itself every reduced path of 3 steps has length 3 edges.
- The quaternion tree never closes; the knot's relation loop closes (6 boosts for T(2,3), 10 for
  T(2,5)). That contrast is automatic: one is a free group, the other has a relation that every
  representation satisfies. It is shown as an illustration, not as evidence of a deeper link.

## What is new here, and what is not

**Not new (prior work, credited):**

- The six-generator quaternion tree and its unique reduced words: Lubotzky, Phillips and Sarnak,
  "Ramanujan graphs" (1988).
- The two-bridge knot presentation: Schubert (1956); its representations: Riley (1984).
- Real points of the eigenvalue variety / A-polynomial: Cooper, Culler, Gillet, Long and Shalen
  (1994).
- Boosts in the Poincaré ball: standard hyperbolic geometry.
- The peel coordinate, Smith step and their addition rule: Jeromie Beasley's VOTKP paper; the exact
  parts are proved in Lean in this repository (`VOTKP/Smith.lean`).
- The artifact labels the quaternion tree "His tree (Garrett)" and offers an `ln 7` step as
  "Garrett's drawing". Garrett is credited here for that drawing choice only; the tree itself is
  the LPS construction. Nothing further is claimed about who Garrett is.

**New in this folder (the synthesis):** putting these in one picture. Specifically, using the VOTKP
peel coordinate as the ruler that turns the quaternion tree into boosts of length `ln 5`, placing
the knot's real meridian and longitude boosts on the Smith disk in the same ball, drawing the
knot's relation as a loop beside the free tree, and the observed "one 90° turn" path in that
drawing.

## Contents

| Path | What it is |
| :--- | :--- |
| [`CLAIMS.md`](CLAIMS.md) | Every claim, its status and its source |
| [`checks/check_peel.py`](checks/check_peel.py) | Numeric checks of the panel numbers and small finite cases (Python 3 + numpy) |
| [`checks/check_peel_output.txt`](checks/check_peel_output.txt) | Its output on 30 October 2026: 23 of 23 checks passed |
| [`checks/check_ink.py`](checks/check_ink.py), [`checks/check_ink_output.txt`](checks/check_ink_output.txt) | The first independent check of the path lengths, kept as run |
| [`AI_USE.md`](AI_USE.md) | How AI tools were used |

The artifact also has Knots, Boundary torus, Curve stack and Quaternion ball views (two-bridge knots
through 8 crossings, 26 knots, data from the Atlas straw-man report v2). This folder checks only the
Peel tree view.

A narrated explainer video (about 3 minutes) of the Peel tree view was also made. It is not stored
here, to keep the repository small.

```bash
python3 peel-atlas/checks/check_peel.py
```

Nothing in this folder is formalized in Lean, and nothing here is part of the Lean build or its
proof check.

## Licence

This folder is covered by the repository's [`LICENSING.md`](../LICENSING.md): the scripts and their
outputs under [MIT](../LICENSE), the written text under [CC BY 4.0](../LICENSE-CC-BY-4.0.md).
Copyright (c) 2026 Jeromie Beasley. To credit it: Jeromie Beasley, *Peel atlas*, with a link to
this folder.

Jeromie Beasley · GitHub [dicipler-pixel](https://github.com/dicipler-pixel) · X
[@d1c1pler](https://x.com/d1c1pler) · YouTube [@AtlasMemoriae](https://www.youtube.com/@AtlasMemoriae) ·
[atlas-memoriae.dicipler.workers.dev](https://atlas-memoriae.dicipler.workers.dev) · ORCID
[0009-0006-4645-5643](https://orcid.org/0009-0006-4645-5643)
