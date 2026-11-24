# Check of the "Gaps and Totals" draft (24 November 2026)

Jeromie Beasley. Independent numerical check, run 23 November 2026 (Central time).

Two scripts, both finite-difference, neither reuses the draft's proofs.

`gaps_totals_check.py` (GAPS-TOTALS-CHECK-01)
- Sum rule: total squared shape-gradient of all pair distances = N(N-2) for N = 3..7. Holds (3, 8, 15, 24, 35).
- Per-pair rule 1/m_i + 1/m_j - d_ij^2 with unequal masses up to N = 8. Holds, worst residual 2.3e-10.
- Three equal bodies: squared singular values sum to 3; product = 12 A^2 / (d12^2 d13^2 d23^2). Holds to 1e-9.
- DISTANCE map at the equilateral shape: gap / distance -> 3 in four directions; holonomy -1.
- SQUARED-distance map (the August operator) at the same point: gap / distance^2 -> 24; holonomy +1.
- Near the collinear locus both maps lose their smaller squared singular value like distance^2.

`squared_map_mass_breaking.py` (SQUARED-MAP-MASS-BREAK-01)
- August prediction: unequal masses give the squared-distance operator a cone with holonomy -1.
- Result: equal masses, one touching point with holonomy +1. Masses (1,1,1.3), (1,1,2), (1,2,3):
  two touching points each, holonomy -1 at each, +1 around the pair. The prediction holds.

Reading: the draft's cone and the August quadratic closing are both right. They are statements about two
different maps (distances, and squared distances). The draft's Remarks 7.4, 7.6 and 7.8 call the August
statements errors; for the August operator they are not.
