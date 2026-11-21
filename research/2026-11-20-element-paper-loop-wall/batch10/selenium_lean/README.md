# Arithmetic certificate for the β-monoclinic cyclooctaselenium ring

The verifier checks the exact bytes of COD 2204812, matches all 24 fractional coordinates and their 24 quoted standard uncertainties to the Lean literals, and checks the eight reported bonds and the four coordinate symmetries. This is the eight-site Se1→Se2→…→Se8→Se1 bond polygon in that crystallographic setting. Coordinates are scaled by 100000, so the displayed integer determinant is divided by 10¹⁰ for fractional-coordinate units squared.

Project along fractional x onto the yz plane. The kernel verifies all 48 oriented edge/off-edge-vertex checks, each strictly positive throughout the rectangular ±1-standard-uncertainty intervals, with smallest certified lower bound 44414721/10¹⁰ = 0.0044414721. Generic interval multiplication proves the corner enclosure for every rational realization. Intervals containing either sign are allowed. A test exchanging vertices 3 and 6 gives a strictly negative determinant even at its interval upper endpoint. The positive source proves this and an alternate false claim is rejected.

The four published symmetry images have computed integer box-shift windows for their fractional-coordinate hulls. For any lattice translation (three arbitrary integers, no truncation of the search), compatibility of all three axes implies the identity operation with shift (0,0,0). A separate theorem verifies that the bounding boxes contain each site's uncertainty box. Thus even before measuring bond lengths one has coordinate separation from every distinct translated symmetry image. The boxes use the observed coordinate setting; crystallographic uncertainty intervals are model inputs, not probability guarantees.

**Topological interpretation in prose.** Strict positive determinants put all nonincident projected vertices strictly to the left of each oriented edge. The projected ring is a simple convex octagon. Each spatial edge is a graph of fractional x above its projected edge. One can extend that boundary height function piecewise linearly across the convex octagon and to its exterior, and shear the ambient x-coordinate to flatten the spatial polygon. This provides an ambient isotopy to a planar polygon. Equivalently its bounded disk can be built inside the hull by coning to a point above the polygon centre. Distinct rings have disjoint bounding boxes, so those disks can be chosen disjointly for this periodic model. The Lean modules certify the interval arithmetic and integer separation, not the ambient-isotopy extension, crystal-field dynamics, or an element-wide knot assignment. Use the original CIF study's cell and convention for comparisons.

Run from the repository root with the pinned Lean 4.34.1:
```sh
base=research/2026-11-20-element-paper-loop-wall/batch10
python3 "$base/selenium_lean/verify_selenium.py" "$base/knot/COD_2204812.cif"
```
