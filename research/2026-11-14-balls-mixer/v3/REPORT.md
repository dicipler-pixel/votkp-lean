# Balls in One Ball, Mixer v3 — 14 November 2026

Jeromie Beasley. AI-assisted.

Mixer v3 keeps the three eyes of v2 (four balls in one ball; two neighbours, overlap or gap; when the balls close) and adds four tree eyes. The v2 files are unchanged.

## New eyes and what each computes live

| Eye | Draws | Two routes compared on the page |
|---|---|---|
| The tree and its level shells | 937 balls to depth 4, level shells, the tree seen from a neighbour | straight arm against Γ_L = (z^L − 1)/(z^L + 1); tree from a neighbour against tree from the centre |
| One step then another: the frame turns | two steps, the one straight step, the turned frame | turn from the matrices against 2·arctan(Γ₁Γ₂); whole triangle (5, 5 gives 65, 72, 97) |
| Across the line: the turn becomes a run | square, fixed point, ring, line shell | turn against 4·arccos g; fixed point ρ against tanh²(ρ/2) = (1 − s)/(1 + s), s = √(1 − 2Γ²); return counts |
| The twin-prime chain as one path in the tree | first 2 to 2400 twin pairs as true-size steps along the end-digit arm | path length ln(a/11) against distance from the centre |

## Checks (checks/v3_expected.py, 50-digit arithmetic, kill lines written before the run)

None of the six kill lines was hit.

- K1 Thomas turn, 7 pairs: worst difference 5.9e-50; reversed order flips the axis in all 7.
- K2 level shells, z = 2, 3, 5, 7, L = 1 to 5: worst 1.3e-51.
- K3 same tree from a neighbour, z = 5 and 7, depth 3 inside depth 4: worst 6.8e-50.
- K4 fixed point formula, z = 2, 3, 4, 5, 5.5: worst 4.4e-50. z = 3 gives cosh ρ = √2; z = 5 gives cosh ρ = 3.
- K5 return counts at z = 5: 83, 1345, 7594 for 0.1, 0.01, 0.001.
- K6 twin starts from 11 below 400000: 3802.

The page readouts (checks/shot3.out, headless run, no errors) match these values.

## Limits

- Freeness is in Lean at ratios 5 and 7 only; the Lean was not re-run in this session. Freeness is not the same as the balls keeping a spacing.
- The whole-triangle readout, the fixed-point formula and the return counts are for arms at right angles.
- The chain eye is a drawing of the end-digit rule and true-size steps. It tests nothing about the primes.
- The Riley two-bridge knot band, the strip transfer and the never-turn census were gathered and evaluated but are not eyes in v3.

evaluation/ holds the independent evaluator's sixteen check scripts and their outputs.
