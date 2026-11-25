# Explicit spectral points on the 16 matrices (24 November 2026)

Question: Anthropic's "VP is not VNP over every field" turns on which prices exist on the
matrices Mat_mu(F_2). At the smallest size (16 matrices) the ratio D(2)^2 / D(1)^2 has ceiling 2,
and the contracting case fails exactly when 2 is reached at every size (their Appendix D, Step 7:
squared distance = rank, the building cone of `../retest-2026-11-24/`). What ratio does each
spectral point that can actually be written down give?

Kill line, written before the runs: any explicit point above 5/3.

## What each explicit point is, as a metric on the parties

| Explicit point | Proved for | Metric it puts on the parties |
|---|---|---|
| Rank of a flattening across a split | every field | cut: 1 if the split separates the two ends, else 0 |
| Quantum functional, weights on single-party splits (Christandl, Vrana, Zuiddam, Corollary 3.31) | complex numbers | star: d(u,v) = theta_u + theta_v |
| Strassen support functional | oblique tensors only | same star on wires |
| Quantum functional, nested (laminar) splits that are not single-party | not proved universal; lower version fails (arXiv 2604.18283) | would be general trees |

The star formula d = theta_u + theta_v on a wire is derived here from the entropy definition
(only the two single-party splits at the ends of a wire see any entropy); it is not quoted from
the source. The paper's Definition A.4 makes pull-backs of prices prices, so matrices may share
a leg end and a leg of length 0 is the centre: every star with any grouping and any leg lengths.

## Results

| Class | Largest ratio | How established |
|---|---|---|
| Every cut (32,767 splits) | 3/2 exactly, 69 splits | exhaustive, exact fractions; also follows from the flat bound, since a cut is a two-point Euclidean set |
| Star, one matrix per leg | 3/2 | exhaustive over legs of length 0 or 1; numeric ascent with free lengths; signed bound is 2 |
| Every star (shared leg ends, free lengths) | 5/3 | search: 88 greedy climbs from random groupings, 4 end at 5/3, none above; control recovers the known star exactly |

Kill line did not fire.

## What follows

Over the complex numbers the 5/3 star is an actual price: the quantum functional on four parties
with weights (0, 1/3, 1/3, 1/3), pulled back along "rank-1 matrices to three legs by column space,
everything else to the centre". So over the complex numbers any contracting constant at size 2
must satisfy s^2 >= 5/3, and the open stretch is exactly 5/3 to 2.

Not proved here: that no star exceeds 5/3 (search only), and nothing about nested-split trees.

## Record of an error caught by the control

The first version of `explicit_points_pullback.py` dropped a factor 2 on the cross term and
returned 1.5 for the known star. The control line (known star must return 5/3) exposed it before
any result was read. The file here is the corrected one.

Files: `explicit_points.py` (EXPLICIT-POINTS-01), `explicit_points_pullback.py` (EXPLICIT-POINTS-02), outputs.

## Addition, same night: the edge support functionals (answer to entry B1 of `../TWO_SESSIONS.md`)

The row "Strassen support functional: oblique tensors only" above is out of date. Two 2026 results:
the support functionals equal the quantum functionals over the complex numbers (arXiv 2601.21553),
and the *edge* support functionals, weights (rho, 1-rho, 0) on three parties, are universal over
every field (arXiv 2604.01386, Theorem 1.1).

On wires an edge support functional gives d(1,2) = 1, d(1,3) = rho, d(2,3) = 1-rho: three points
on a straight line. Pulled back, the 16 matrices sit at three collinear points. A collinear set is
Euclidean, so the flat maximum 3/2 applies. `edge_support.py` (EDGE-SUPPORT-01) checks it:
60 climbs, largest ratio 1.5, nothing above.

| Field | Largest ratio from explicit points | Which point |
|---|---|---|
| Every field | 3/2 | cuts; edge support functionals |
| Complex numbers | 5/3 | four-party quantum functional, weights (0, 1/3, 1/3, 1/3) |

The 5/3 star needs three legs, so four parties with single-party weights. Over fields other than
the complex numbers no such point is known. That is the sharpest form of the gap found so far.
