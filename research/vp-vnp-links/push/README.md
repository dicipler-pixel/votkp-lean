# The 16-matrix test from "VP != VNP over every field", run in flat space, in trees and in the ball

> **Status, evening of 24 November 2026 (read this first).** Later work changed four statements below.
> (1) The largest ratio a nonpositively curved space allows at size 2 is exactly 2, not "between 5/3 and 2": the cone over
> the spherical building reaches it (`research/retest-2026-11-24/NOTE_FOR_THE_DOC.md`). (2) "All found the same star" was
> checked for the three-dimensional run only. (3) A uniform placement does exist at 5/3 (the star averaged over the symmetries).
> (4) "Below 2 at every size" is counted for sizes 2 to 5. Also: `ball_search.out` ends in a killed run and
> `star_structured.out` ends in a memory error at size 4.


Jeromie Beasley. 24 November 2026. Exploration; nothing here is part of that proof.

The quantity (their Definition 2.1): on the mu x mu matrices over the two-element field,
ratio = mean squared distance over steps of rank mu / mean squared distance over steps of rank 1.
Their bound for every price: ratio <= mu. Their contracting case: some mu where every price stays a fixed factor below mu.

Results
1. Flat (Euclidean) maximum, exact: 3/2, 7/4, 15/8 at mu = 2, 3, 4, equal to 2 - 2^(1-mu). Reached by a character of rank 1.
   So flat placements stay below 2 at every size while the ceiling is mu. (`exact_flat.py`)
2. Trees beat flat at mu = 2. Exact star: centre = the zero matrix and the six invertible ones; three legs, one for each
   nonzero column vector, each holding its three rank-1 matrices. Ratio exactly 5/3. (`star_search.py`, `star_structured.py`)
3. The same star in the ball (legs at 120 degrees): ratio 1.500 at short legs, the flat value, rising to 1.6624 at leg
   length 40, toward 5/3. Leg end to leg end = twice the leg minus ln(4/3). (`star_in_ball.py`)
4. Free search in the ball and its relatives: best 1.6500 (three dimensions), 1.6487 (six), 1.6475 (fifteen),
   1.6464 and 1.6428 (products of two and three balls). All found the same star. Nothing above 5/3, nothing above 2.
   (`ball_search.py`, `ball_structure.py`: 7 clusters, tree condition met to 0.0009)
5. At mu = 3 no tree placement above the flat 7/4 was found (best star 1.578 after local search). Undecided.
6. Flat Poincare constant on the unitriangular groups (their Theorem F.6, flat targets), h = 2..7:
   0.5000, 1.7071, 3.4397, 4.9886, 6.4019, 7.5848. Still rising at h = 7, steps shrinking. Bounded or not is not decided here.
   (`exact_flat.py`, `poincare_big.py`)

Where it stands at mu = 2: the largest ratio any nonpositively curved space allows is between 5/3 and 2.
Their paper does not know whether prices reach 2. The gap between 5/3 and 2 is that question in its smallest case.

Not results: the first Poincare run used a slow method and was stopped at h = 6; the faster run replaced it.
The uniform target (every rank-1 pair at one distance, every rank-2 pair at another) with ratio above 3/2 was not
found in one ball or a product of two; the 5/3 star is not uniform.
