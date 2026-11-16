# Read record 03 — The Volume of the Knot Potential: Decay and Direction on the Vacuum Disk, v5 (8 Nov 2026)

Source read in full: votkp_vacuum_disk_v5.pdf, 25 pages (text extracted from the PDF; a few display formulas came through broken and are rebuilt here from the surrounding text). v6 not seen.

## The disk
- Bloch-Wigner: D(z) = Im Li2(z) + arg(1-z) log|z|. w = e^{i pi/3}, V_0 = D(w) = 1.0149416064.
- Vacuum disk: G(z) = (z - w)/(z - w-bar).
- Prop 1: (a) G(w) = 0; (b) real z gives |G| = 1 (flat pieces on the rim); (c) G(z-bar) = 1/conj(G(z)) (mirrors outside); (d) T(z) = 1/(1-z) acts as G(Tz) = e^{2 pi i/3} G(z), D(Tz) = D(z). Proof of (d): T is Mobius of order 3 with fixed points w, w-bar; multiplier T'(w) = 1/(1-w)^2 = e^{2 pi i/3}.
- Check point: z = 0.3 + 1.1i, radius 0.1557583601, angles 34.715, 154.715, -85.285 degrees, D = 0.9832288623.

## Decay (the bowl)
- Thm 2: D = V_0 - (3 sqrt3/4)|G|^2 + (sqrt3/8)(G^3 + G-bar^3) + (3 sqrt3/16)|G|^4 + O(|G|^5).
- Knot law, nothing fitted: Vol(K) = sum_j D(z_j). Median errors on 12,954 knots: quadratic 0.21%, + cubic 0.39%, + cubic + quartic 0.076%. Opposite test (hyperbolic distance) 1.3%.
- 1,391 of 2,777 tetrahedra lie within hyperbolic distance 0.5 of the vacuum.

## Every geometry
- 31 knots, 291 solutions of the gluing equations: true geometry = smallest sum |G_j|^2 (31/31) = largest volume (31/31, known).
- All-real solutions: sum |G_j|^2 = n exactly.
- Orientation-aware ladder: eps_j [V_0 - k |G~_j|^2], G~ = 1/conj(G), eps = -1 outside: Spearman 0.995.
- 6_1: sum |G|^2 = 0.74, 5.1, 28.9, 47.3 against volumes 3.164, 1.415, -1.415, -3.164.

## Direction
- Null first: summed three-fold angle of G against CS gives rho = 0.02. The twist is NOT in the angles of the pieces.
- Neumann: w_0 = log z + p pi i, w_1 = log z' + q pi i, w_2 = -w_0 - w_1, z' = 1/(1-z); flattening = every edge and both cusp curves total 0.
- i(Vol + i CS) = sum eps_j R(z_j; p_j, q_j), R(z;p,q) = Li2(z) + (1/2) log z log(1-z) + (pi i/2)(q log z + p log(1-z)) - pi^2/6.
- Relabelling defect: R(z'; q, r) - R(z; p, q) = (1 + 3q) pi^2/6. Fixed by a branching order. CS exact in 454 of 454 runs, modulo pi^2/2.
- Without the windings the continuous part matches 1 of 79.

## Our polynomial
- Cho-Kim-Kim potential: each crossing with sides (a,b,c,d) adds four dilogarithms of side ratios; equations exp(z_k dV/dz_k) = 1; V_0 = V - sum_k (z_k d_k V) log z_k = i(Vol + i CS) at the geometric solution.
- Placement rule: (b,d) is the under-strand pair of PD crossing X[i,j,k,l], same for both signs. Kinked crossing X[i,j,j,l] must be removed.
- Solutions come in continuous families; only V_0 is constant on a family.
- P_K(x) = product over geometries rho of (x - e^{lambda V_0(rho)}), lambda mapping the pi^2 period to a full turn.
- Top root = SnapPy complex volume on 79/79; spectrum the same from three drawings on 13/13.
- Table: 4_1 (2.02988, 0); 5_2 (2.82812, -3.0241), (0, 1.1135); 6_1 (3.16396, 3.0789), (1.4151, 0.211); 6_2 (4.40083, -3.997), (1.53058, 0.3291), (0, 2.4011); 6_3 (5.69302, 0), (0.9243, +-1.8906).
- SnapPy's named manifold is the mirror of the KnotInfo drawing for 42 of 79 knots.
- Torus knots: decay 0, directions as fractions of pi^2 mod 1: 3_1: 5/6; 5_1: 1/10, 9/10; 7_1: 3/14, 5/14, 13/14; 8_19: 11/12; 10_124: 14/15. All fit -k^2/(pq) mod 1. The paper marks this REPRODUCTION (Kirk-Klassen; Dubois-Kashaev; Murakami).

## Light strings, colour, electron
- Jones climb (Mahler measure) vs volume rho = 0.854; turn (swept area) vs |signature| rho = 0.83; no correlation of any of these with CS.
- sl(N) lines v = t^{-N/2}, z = t^{1/2} - t^{-1/2}: climb vs volume 0.60 (N=0), 0.86 (N=2), 0.78-0.86 (N=3..8); all lines + log det R^2 = 0.838.
- Circuit polynomial Q(z): Q(1) = det K on 1,846/1,846 alternating knots; flype-invariant; coarse.
- Colour: Gamma = (1-N)/(1+N); Schottky line |Gamma|^2 = 1/2 splits metals 35/35 from non-metals 0/6; hidden phase rho = 0.64; film winding grows by one per 247 nm; 2/3 vacuum-mix line vs metallization pressure rho = 0.89.
- Electron: SL(2,C) -> PSL(2,C) = Mobius = isometries of H^3. Spin lift closes CS modulo pi^2: 4_1 CS = 0; 5_2 CS = -3.0241284 (= 1.9106738 mod pi^2/2). Peripheral holonomies are parabolic (traces +2, -2): one loop carries no phase while CS != 0. Braiding: B_i = (1 + g_{i+1} g_i)/sqrt2, B_i^2 = g_{i+1} g_i, |B^2 - I| = 1.414.
- Self-assembling knots: 5 of 6 privileged knots are torus knots (zero decay).

## Open problems as the paper lists them
1. Missing torus roots: 2 for 8_19, 3 for 10_124. 2. Rigor of complex Chern-Simons. 3. Arithmetic of P_K. 4. Colour inside the disk. 5. Prior art on circuit polynomial and sl(N) climb. 6. The 61 silent double walls of VOTKP v2.9 Table 6.

## What the Dirac Time read adds here — checked this session (TORUS-DIRS-03)
- Dirac Time Thm 13.1(3) gives both end steps of arc (a,b): k = uaq + vbp and k = uaq - vbp. Their squares differ by 4uvab*pq, a multiple of pq, so -k^2/(pq) mod 1 is the SAME at both ends: the direction belongs to the arc. Checked on every arc of every T(p,q), p < 13, q < 20: zero disagreements.
- Arc by arc: 8_19: arcs (1,1) and (1,3) both give 11/12; arc (2,2) gives 2/3. 10_124: arcs (1,1), (2,4) give 14/15; arcs (1,3), (2,2) give 11/15. T(4,5): 19/20, 11/20, 4/5, 1/5 (six arcs, four values).
- Consequence for open problem 1: the root search should find ONE new direction for 8_19 (2/3), not two, and ONE new direction for 10_124 (11/15), not three. Arcs that share a direction are the plus/minus pairs of Dirac Time 13.2 (same boundary, different interior). Not yet run against the root search itself.
