# Balls in One Ball, Mixer v4 — 14 November 2026

Jeromie Beasley. AI-assisted.

Mixer v4 keeps the seven eyes of v3 and adds two knot eyes. The v3 files are unchanged.

## Eye 8: a knot, its mirror, and what a step can see

The torus knot T(2,n) is drawn round the centre of the ball. With r = ln t and Γ_L = (t^L − 1)/(t^L + 1), its symmetrised Alexander polynomial is shown four ways:

- the polynomial, Σ (−1)^k t^k divided by t^((n−1)/2);
- cosh(n r/2) / cosh(r/2);
- t^(−(n−1)/2) (1 − Γ₁)/(1 − Γ_n), from one step and n steps along one arm of the tree;
- for n = 7, x³ − x² − 2x + 1 at x = t + 1/t (the polynomial R₇ of the Knot Mirror handoff).

All four are unchanged under t → 1/t and under the mirror. On the turn side the same expression is cos(nθ/2)/cos(θ/2), with zeros at θ = (2j+1)·180°/n; the Levine–Tristram signature at angle θ is twice the number of zeros passed, with the sign set by the hand. Each crossing change takes T(2,n) to T(2,n−2).

## Eye 9: knot plus mirror: five, not six

The result is Brittenham and Hermiller, "Unknotting number is not additive under connected sum", arXiv 2506.24088, Theorem 1.2: u(7₁ # mirror 7₁) ≤ 5 < 6. The eye draws the two sums as true connected sums, and the published 20-crossing, 5-strand braid [1, −4, 2, 3, 3, 3, 2, 3, 2, 2, 4, −3, −3, −3, −3, −1, −3, −2, −3, −3] with the two changed crossings marked. The sequence shown is 7₁ # mirror 7₁ → (2 changes) K14a18636 → K15n81556 → K12n412 → unknot.

## Checks (kill lines written before the run; none hit)

- N1 four routes for the Alexander value, n = 3..13, five ratios: worst relative difference 2.4e-31; reversal 6.7e-41.
- N2 R₇ identity at n = 7: 2.8e-41.
- N3 signature from the Seifert matrix against twice the zeros passed: 360 cases, 0 mismatches; the mirror gives the negative in all.
- N4 the published braid: one component, signature 0, determinant 49, Alexander polynomial equal to that of 7₁ squared up to a unit; after changing entries 0 and 1 SnapPy identifies K14a18636.
- N5 7₁ # 7₁: signature 12, determinant 49; 7₁ # mirror 7₁: signature 0, determinant 49.

## Limits

- The last three changes of the sequence (through K15n81556 and K12n412) are as published and were not re-run here.
- The drawing of the braid follows the braid word with one fixed over/under convention; it may be the mirror image of SnapPy's picture. The mirror sum is its own mirror, so the starting picture is unaffected.
- The exact unknotting number of 7₁ # mirror 7₁ is open.
- The link between the knot's Alexander value and the tree is an identity for T(2,n) only. Nothing here ties the closing steps of eye 3 to these knots; that is untested.
