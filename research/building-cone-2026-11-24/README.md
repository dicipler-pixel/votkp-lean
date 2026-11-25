# Building cone against the IQGT metric, and the star count (24 November 2026, Session A)

Two queued runs from `../TWO_SESSIONS.md` (A2 NEXT and A1 NEXT), done after the Dirac Time read
(`../required-reading-2026-11-24/NOTES_DIRAC_TIME.md`). Kill lines were written before each run.

## 1. Is the building cone the IQGT metric with the gap removed?

The building cone is the limiting price of the Anthropic release's Appendix D, Step 7: squared
distance = rank(a - b) on Mat_2(F_2), ratio D(2)^2/D(1)^2 = 2. Dirac Time 9.4 says the projector
metric has no gap in it once written on projectors, so "gap removed" means the chordal distance
||P_a - P_b||^2 = 2 sum sin^2(theta).

| Run | Kill line | Outcome |
|---|---|---|
| `graph_projector.py` (GRAPH-PROJECTOR-01): matrix a placed as the projector onto its graph {(x, ax)} over the reals | chord^2 is not a function of rank(a - b) | fired. 13 different values on rank-1 pairs (0.4 to 2.6), 6 on rank-2 pairs. Ratio 1.4648 (entries 0,1), 1.4474 (entries +1,-1) |
| same script, lean angles themselves (geodesic on the Grassmannian) | (read alongside) | ratio 1.4676 and 1.4153 |
| same script, opposite setup: non-compact side, rapidity distance, singular value = tanh(eps/2), scale gamma from 0 to the rim | never above 3/2 | fired. Exactly 3/2 at small gamma, falling toward the rim (1.06 and 1.00 at gamma = 1 - 10^-9) |
| `rank_flatness.py` (RANK-FLATNESS-01): exact, covers every placement by projectors | squared distance = rank is flat | did not fire. Fourier coefficients: -3 on rank-1 characters, +1 on rank-2 characters. In general 1 - 2t and -3 + 2t for t = f(2)/f(1): flat exactly when t <= 3/2 |

Reading. The claim failed this way: every placement of the 16 matrices as projectors, of any rank in
any dimension, gives a flat distance, and a rank-only squared distance is flat only up to 3/2. The
building cone (2) and the tree star (5/3) both lie outside what the chordal IQGT metric can reach.
The flat ceiling 3/2 is the same number the cuts and the edge support functionals give over every
field. The real-number lift is one setup; a placement over the 2-adic numbers was not tried.

## 2. Star count

`star_count.c` (STAR-COUNT-01). All 715,860,651 groupings of the 16 matrices onto a centre and up to
three legs (each grouping once, up to renaming legs), with free leg lengths decided exactly by a
copositivity test (Hadeler's criterion on M = 10 Q_1 - 9 Q_2). Control: the known star must sit
exactly on the line; it does.

| Quantity | Value |
|---|---|
| groupings above 5/3 | 0 |
| groupings that reach 5/3 exactly | 32 |
| largest ratio with unit legs | 5/3 (N2/N1 = 90/81), the same 32 groupings |

Kill line (a star above 5/3) did not fire. "5/3 by search" is now "5/3 by count" for stars with a
centre and up to three legs. Stars with four or more legs, and trees that are not stars, are not
covered. The copositivity test uses floating point with tolerance 10^-9 on whole-number matrices.

Error record: the first run counted 21,523,393 ties because an unused leg gave a zero row; the fix
gives an unused leg weight 1. The count of groupings above 5/3 was 0 in both runs.
