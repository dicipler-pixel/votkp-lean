# Links between the "VP != VNP over every field" release and existing work

Jeromie Beasley. 24 November 2026. Reading notes and four checks. Nothing here is part of that proof.

Source read: anthropics/formal-math, folder vp-vnp, commit 11b6c7e (README, Statement.lean, Challenge.lean, paper.pdf pages 1 to 11).

How that proof runs, in its own terms:
- A "price" is a distance between parties, read off a spectral point: a wire of dimension q between u and v is worth q to the power d(u,v).
  The log of a spectral point on a network of wires is its "length": the sum over wires of distance times size.
- A tensor of rank at most r across a cut is a restriction of a network with two hubs joined by a wire of dimension r. Ranks become distances.
- Two crossing wires force every price to have nonpositive curvature (the Bruhat-Tits inequality).
- Two cases. Flat: Euclidean configurations are prices; the complete graph has at least 2k^2/9 wires across every balanced cut,
  which forces log(gates) >= l k^(3/2) / 16. Contracting: a Poincare inequality on unitriangular groups over the two-element field,
  rerouting laws, trees, cuts, accelerators, and a diagonal argument.
- The permanent enters only by substitution; the circuit is opened in two places.

Checks (`vp_links.py`, VP-LINKS-01), all passed:
- The hyperbolic ball obeys the four-point curvature rule: 0 violations in 300000 quadrilaterals.
- The tetrahedron's own distance breaks it: 5431 violations in 300000 (worst case 2.58 against 1.60).
- Hamming distance on permutations obeys the rule as written (it is half a squared Frobenius distance):
  0 violations over all 1296 quadrilaterals of Sym(3) and 200000 random ones of Sym(7); no equality with four distinct corners.
- Complete graph: degree-zero constant ceil(k/2); fewest wires across a balanced cut at least 2k^2/9 for k = 4..9;
  degree-one constant with two-element coefficients 2, 5/3, 2 at k = 4, 5, 6 (k/3 missed at k = 4).

Reading: the flat case uses the degree-zero expansion of the complete graph; the k/3 theorem is the degree-one member of the
same family with Sym(3) coefficients. Both proofs turn on whether a flat bound is attained or missed by a fixed factor.
These are structural links, not a dependence in either direction.
