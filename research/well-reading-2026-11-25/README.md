# The well reading at the prime 2 (25 November 2026, Session B)

Queued in entry A3 of `../TWO_SESSIONS.md`. Placement read first from the release itself (anthropics/formal-math,
vp-vnp, commit 11b6c7e, paper.pdf Appendix D.1 and D.2 Step 7): parties = Mat_mu(F_2); D(r)^2 = mean of |a, a+W|^2
over all a and all W of rank r; the limiting price has |a,a'|^2 = rk(a - a').

Construction (`well_reading.py`, WELL-READING-01). Cross block B = the integer difference of the two matrices.
Hidden spectrum = its 2-adic Smith form, levels 2^v_i. Read each level over its own gap:
gap^0 (K(0)) = number of levels, gap^1 (the well) = sum 2^-v_i, gap^2 (the metric) = sum 4^-v_i.
Mod 2 only the v_i = 0 levels survive, so every reading equals the release's rank when nothing is hidden.

Kill lines (both written before the run): (1) the reading is flat (double-centred Gram PSD);
(2) if not flat, it breaks the release's quadrilateral inequality, Lemma C.4(b), on some quadruple.

| mu | reading | D(2)^2/D(1)^2 | D(3)^2/D(1)^2 | flat? | C.4(b) |
|---|---|---|---|---|---|
| 2 | gap^0 | 36/19 = 1.8947 | | no | 0 violations (all 65,536 quadruples) |
| 2 | gap^1, the well | 72/37 = 1.9459 | | no | 0 violations |
| 2 | gap^2, the metric | 144/73 = 1.9726 | | no | 0 violations |
| 3 | gap^0 | 1.7650 | 2.4784 | no | 0 in 400,000 sampled |
| 3 | gap^1 | 1.8705 | 2.7144 | no | 0 in 400,000 sampled |
| 3 | gap^2 | 1.9318 | 2.8500 | no | 0 in 400,000 sampled |

Both lifts (0,1 and +1,-1) give the same ratios. Control: the release's price rk(a - a') gives D(r)^2 = r.

Neither kill line fired. Reading: with the gap read at 2, the 16 matrices are not flat, sit above the tree value 5/3
and below the cone value 2, and pass the one curvature test that every price must pass. What this does NOT show:
that any of these readings is a price. A price comes from a spectral point (Definition A.4); the quadrilateral
inequality is necessary for that, not sufficient, and is not even a full CAT(0) test on more than four points.
Untested: a spectral point that produces this reading; the full CAT(0) embedding; other primes.

## Where the hidden levels sit (checked, 25 Nov, after Jeromie's note linking this to the nilpotent, exceptional
## and degenerate points of the suns and black hole papers)

Over all 256 ordered pairs at mu = 2, the differences of rank 1 mod 2 split as:
idempotent-type mod 2 (trace 1): 96, never a hidden level; nilpotent mod 2 (trace 0): 48, of which 8 carry the
hidden level 2^1 and 40 carry none. So every hidden level sits on a nilpotent: one Jordan block at the prime.
Those 8 are the sign patterns with all entries +-1 and det = +-2, and for them X X^T = 2I exactly
(rows (a,b), (c,d) of +-1 give (ac+bd)^2 + (ad-bc)^2 = 4, so det = +-2 forces the rows orthogonal).
So the same matrix is degenerate (nilpotent, a single Jordan block) mod 2 and is sqrt(2) times an orthogonal
matrix over the 2-adic numbers. The gap the well reading adds is carried only by these points.
