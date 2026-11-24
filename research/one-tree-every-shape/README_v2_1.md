# One Tree, Every Shape v2.1 (Jeromie Beasley, 23 Nov 2026)

v2.1 is v2 with three text changes; every eye, number and drawing is the same.

- The licence is now inside the page (byline, a meta tag and a header comment):
  © 2026 Jeromie Beasley · code MIT · text and figures CC BY 4.0.
- Eye 8 (the end-digit record) names its prior art: Lemke Oliver and Soundararajan (2016),
  the bias in the last digits of consecutive primes; the page counts the same thing for consecutive twin starts.
- Eye 9 (the zeros push apart) keeps the measurement as measured and labels the commuting line
  as a reading, in line with the random-matrix picture of the zeros (Montgomery; Dyson).

Rebuild: `python3 build_v2_1.py One_Tree_Every_Shape_v2.html One_Tree_Every_Shape_v2_1.html`
(v2 is rebuilt from v1 by `build_v2.py`, byte for byte; see REBUILD_v2.md).

Checks run for v2.1: the v2 rebuild is byte-identical to the v2 in this folder; SHAPE-SMITH-01 and
SHAPE-AUDIT-01 rerun to outputs identical to their records; all 12 eyes opened in the icosahedron,
cube and tetrahedron with no page errors (`shot3.py`).
