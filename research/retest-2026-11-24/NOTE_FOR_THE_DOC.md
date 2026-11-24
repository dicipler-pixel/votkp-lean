# Note for the next version of the 16-matrix doc (24 Nov 2026, evening). The doc itself is not changed yet.

Author: Jeromie Beasley

## What changes
The doc says: at size 2 the largest ratio a nonpositively curved space allows lies between 5/3 and 2.
New: it is exactly 2, and exactly mu at size mu. The space that reaches it is the Euclidean cone over the spherical
building of the general linear group of size 2*mu over the two-element field.

How: send each matrix a to its graph {(x, a x)}, a mu-dimensional subspace of a 2*mu-dimensional space.
Two graphs meet in dimension mu - rank(a - b). In a shared apartment the angle between them has cosine 1 - 2k/mu
for k = rank(a - b), so with cone radius squared mu/4 the squared cone distance is exactly k.

Grade: derived from two standard theorems (a spherical building has curvature at most 1; the Euclidean cone over such a
space is nonpositively curved) plus the algebra above. `building_cone.py` (BUILDING-CONE-01) checks the algebra and runs
the weighted four-point inequalities that any such metric must pass: all 65,536 quadruples at size 2 and 300,000 random
ones at size 3, each on 441 weight pairs; smallest value 0, no violation. Passing those is necessary, not sufficient;
the embedding rests on the two theorems.

## What it means
- The scale now reads: flat 3/2, tree 5/3, building 2, no curvature rule 4.
- A tree is the smallest building. The full ratio needs a building with flat rooms and branching walls together.
- Nonpositive curvature alone can never prove the paper's contracting case. Their open question is strictly about
  which curved spaces are prices. Their own Remark D.3 already uses the metric root-of-rank as a price when the
  contracting case fails; the note here is that it is a nonpositively curved metric with no condition at all.
- The earlier next step ("does squared distance = rank fit a nonpositively curved space") is answered: yes.
- The reader's point stands: products of trees cannot pass 5/3.

## Still open
- Whether 5/3 is the true maximum over trees (search only).
- Whether the building cone's metric is a price over any field. That is the paper's open question in its sharpest form.

## Two one-line identities found while zooming out (`zoom_identities_output.txt`)
- Star in the ball: end to end = 2 x leg - 2 ln(1/sin(half the angle between legs)). At 120 degrees that is ln(4/3).
  This is the census depth of atlas card B16 at 60 degrees, and sin^2(60 degrees) = 3/4 is the threshold of card B77.
- Two ends of one edge with a phase Phi between them: connection energy over its opposite = tan^2(Phi/2).
  These are the dark and bright ports of a two-arm interferometer; a quarter flux quantum balances the two books.
