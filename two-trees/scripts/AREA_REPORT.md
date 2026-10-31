# Why the relator polygon has area 0 at o*: a reflection symmetry (proved)

Grades: **proved** / **computed** / **open**. Scripts: `area_sym.py`, `area_sym2.py` (each starts with `# SCRIPT:` and its kill conditions); outputs `area_sym_out.txt`, `area_sym2_out.txt`.

## Result

**Theorem (proved).** Let K(p,q), q odd, have a real Riley representation a = [[s,1],[0,1/s]], b = [[s,0],[-v,1/s]] (s real, v real, v != 0), with W = g_1...g_{p-1}, g_i = b^{e_i} (i odd), a^{e_i} (i even), e_i = (-1)^{floor(iq/p)}, and relator r = a W b^-1 W^-1. Let P(o) be the geodesic polygon with vertices p_k = h_k.o, h_k the length-k prefixes of r (N = 2m vertices, m = |W|+1), and A(o) its signed (winding-weighted) area.

1. If v > 0, the matrix K = [[0,1],[v,0]] acts on H as the reflection R: z -> 1/(v conj z) in the geodesic l = {|z| = 1/sqrt(v)}, and A(R o) = -A(o) for every o. In particular **A(o) = 0 for every o on l**, whether or not the axes of a and b cross.
2. If v < 0, K is a half-turn, A(K o) = +A(o), and nothing forces A = 0.
3. o* (the crossing point of the axes) lies on l, so A(o*) = 0 on every arm with v > 0 and 0 < v < (s - 1/s)^2 (axes cross). Where the axes do not cross, o* is not on l and A(o*) != 0.

## Proof

**Step 1, an anti-automorphism swapping a and b (proved).** Put D = diag(1,-v) and tau(X) = D X^T D^-1. Then tau(XY) = tau(Y) tau(X), and direct multiplication gives tau(a) = b (the (2,1) entry of a^T is scaled by -v) and tau(b) = a (the (1,2) entry -v is scaled by -1/v, giving 1). So tau(g^{+-1}) swaps the type of the letter and keeps the exponent.

**Step 2, W is palindromic (proved).** For 0 < i < p, iq/p is not an integer, so floor((p-i)q/p) = q - 1 - floor(iq/p); with q odd, e_{p-i} = e_i. Also p is odd, so i and p-i have opposite parity: g_{p-i} has the opposite type to g_i. Hence tau(g_{p-i}) = g_i and tau(W) = tau(g_{p-1})...tau(g_1) = g_1...g_{p-1} = W. (Checked by machine for all odd q, p <= 59: 364 pairs, no failure.)

**Step 3, tau is an inversion in K (proved).** For X in SL2, X^T = J X^-1 J^-1 with J = [[0,1],[-1,0]]. So tau(X) = K X^-1 K^-1 with K = D J = [[0,1],[v,0]], K^2 = v I. As an isometry, K acts by z -> 1/(v z) if det K = -v > 0 (a half-turn about i/sqrt(-v)), and by z -> 1/(v conj z) if v > 0, an orientation-reversing involution whose mirror is |z|^2 = 1/v. Consequences, as exact matrix identities: K a K^-1 = b^-1, K b K^-1 = a^-1, K W K^-1 = W^-1.

**Step 4, the induced map on words (proved).** The substitution phi: a -> b^-1, b -> a^-1 satisfies K h K^-1 = phi(h) for all words h. By Step 2, phi(W) = W^-1 letter for letter (the j-th letter of W^-1 is g_{p-j}^-1, which is the opposite type to g_j with exponent -e_j, which is phi(g_j)). So phi(r) = b^-1 W^-1 a W, as a word.

**Step 5, the half-period shift (proved).** Write r = r1 r2 with r1 = aW (length m), r2 = b^-1 W^-1. Then phi(r) = r2 r1. Since r = 1 in the group, r2 = r1^-1 as matrices. For o on l (R o = o) and each k (indices mod N):

R(p_k) = K h_k K^-1 . R(o) = phi(h_k).o = g.p_{k+m}, g = r1^-1 = (aW)^-1.

Check: for k <= m, phi(h_k) = q_k is a prefix of r2 and p_{m+k} = r1 q_k o, so g p_{m+k} = q_k o. For k > m, phi(h_k) = r2 h_{k-m} = r1^-1 h_{k-m} and k-m = k+m mod N. So Sigma := g^-1 R is an orientation-reversing isometry with **Sigma p_k = p_{k+m}** for all k: it maps the polygon to itself, keeping the cyclic order of the vertices.

**Step 6, the area (proved).** Signed area is A(P) = integral over the boundary of a primitive alpha of the area form, so it depends only on the cyclic edge sequence, not on the starting vertex (equivalently, the fan sum is independent of the apex). An orientation-reversing isometry changes its sign. Since Sigma P = P as a cyclic sequence, A(P) = A(Sigma P) = -A(P), so A = 0. For general o, polygon(R o; r) = R polygon(o; phi(r)) and polygon(o; phi(r)) = g polygon(o; r) re-indexed, so A(R o) = -A(o). For v < 0, K is orientation-preserving and the same argument gives A(K o) = +A(o) only. QED.

**Step 7, o* (proved + computed).** Axis(a) is the line Re z = x_a = s/(1-s^2); axis(b) is the semicircle from 0 to x_b = (1-s^2)/(s v). x_a x_b = 1/v. When the axes cross (x_b < x_a < 0), the crossing point has |z|^2 = x_a^2 + x_a(x_b - x_a) = x_a x_b = 1/v, so it lies on l (R swaps the two axes and so fixes their intersection). When they do not cross, R maps the foot of the common perpendicular on axis(a) to the foot on axis(b), a different point, so o* is not on l.

Why the half-turn J failed: J (orientation-preserving, about o*) inverts a and b but reverses nothing; the true symmetry is the reflection R, composed with the shift g^-1, which is a half-period shift of the cyclic order and not a reversal. The polygon is not a symmetric simple polygon; it is a self-overlapping 2m-gon in which vertices p_k and p_{k+m} are mirror images (Sigma is a reflection in the perpendicular bisector of o and aW.o, checked: Sigma^2 = id to 1e-97), and the signed areas of the two halves cancel.

## Numerical confirmation (computed; kill conditions K1-K12 survived)

mpmath, 50 and 100 digits; knots 3_1, 4_1, 5_2, 6_2, 6_1 (9,7), (13,5); x = 0.7 to 3.5, every real root with |v| > 1e-12 (about 40 branch points).

| check | worst error |
|---|---|
| K1 tau(a) = b, tau(b) = a | 7e-52 |
| K2 tau(W) = W | 1.5e-48 |
| K3 K a^-1 K^-1 = b, K W^-1 K^-1 = W (projective) | 2e-49 |
| K4 K p_k = g p_{k+m}, o on l | 1.3e-34 at x = 3.5 (loss of digits from s^22), < 1e-36 elsewhere |
| K5 A = 0 at 6 points of l (v > 0, all 3_1 rows included, where the axes do NOT cross) | 8e-33 (x = 3.5, 6_2); 1e-96 at 100 digits |
| K6 A(R o) = -A(o) at random o | 4e-31 (x = 3.5), typically < 1e-40 |
| K7 v < 0: A(K o) = +A(o), and A != 0 at random points (4_1 v- arm: 0.08 to 1.3; 6_1 and 6_2 v < 0 arms: 0.07 to 3.5) | 3e-43 |
| K8 o* on l iff axes cross | crossing: ||o*|^2 - 1/v| = 0 to 1e-50, A(o*) < 2e-34; non-crossing: ||o*|^2 - 1/v| = 1e-6 to 0.3, A(o*) = -1.52 (3_1, x = 0.7), -0.52 (x = 2.0), -0.12 (x = 3.5), same on 5_2 and 6_2 v > (s-1/s)^2 arms |
| K9 Sigma p_k = p_{k+m}; Sigma^2 = id | 2e-94 |
| K11 palindrome, 364 (p,q) pairs | 0 failures |
| K12 (13,5), 4 branches: A on l | 2e-90 |

Reading: the zero at o* found earlier is the special case of the reflection fixing l, so it is not an accident of o*. The earlier trefoil value A(o*) -> -pi (x -> 0) is consistent: the trefoil has v > (s-1/s)^2, so o* is off l.

## Idea tests (kill condition stated in the script headers)

1. Orientation-reversing symmetry: **survived; this is the mechanism** (reflection R swapping the axes, R a R = b^-1, R W R = W^-1; it needs o on l, composed with the half-period shift g).
2. Decomposition into congruent triangles of opposite orientation: the same fact in pieces: Sigma pairs the fan triangle (p_0, p_k, p_{k+1}) with (p_m, p_{k+m}, p_{k+m+1}), a mirror pair, with the fan apex moved by a cyclic re-indexing (free by Step 6). Not run separately.
3. Any base point on the line of symmetry: **yes, every point of l** (computed at six angles per branch, proved above), and in addition A is odd under R. Grid scan (17 x 17, 5 branches): A changes sign only across l (0 violations in 53 sign-changing edges); this is **computed on a coarse grid, not proved**, that l is the whole zero set.

## When it fails

- v < 0 (4_1 v- arm, the v < 0 arms of 6_1 and 6_2, the small negative stretch of 6_2 branch 1): K is a half-turn; no reflection exists; A(o) > 0 at all points tested.
- Off l, for any base point (o = i included): A != 0 in general (4_1 at o = i: 0.84 at the fold).
- Where v > 0 but the axes are ultraparallel (v > (s-1/s)^2: the trefoil, the non-crossing 4_1, 5_2, 6_2 arms at large v): the vanishing holds on l but the named point o* is off l, so A(o*) != 0.
- The proof used: q odd (palindrome), real s and v, v > 0. Not covered: q even normal forms, complex branches, elliptic meridians (|s| = 1).

## Open

- Whether l is the entire zero set of A for v > 0 (grid evidence only).
- What A(o) is as a function on H^2 off l (it is odd under R and equals the holonomy angle of the frame around the relator loop).
- Whether the v < 0 half-turn gives a conserved quantity (A(K o) = A(o) is the only constraint found).
