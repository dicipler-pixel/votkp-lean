# Read record 05 — Non-Normality Is Connection Energy: the statement list (NOT the v15 paper)

Zenodo record 23787997: "Non-Normality Is Connection Energy", Jeromie Beasley, 30 October 2026, paper Version 15 (Zenodo version v5), DOI 10.5281/zenodo.23787997. Files there: v15 HTML (16.0 MB), v15 PDF (3.8 MB), code and sources zip (4.5 MB).
The v15 paper itself is NOT READ: the shell cannot reach Zenodo, and the copy is not on Drive.
Read in full instead: STATEMENTS.md of GitHub dicipler-pixel/nonnormality-connection-energy-lean (covers v7 and the v11 two-books statements; nothing later than v11).

## Setting
- G = (V,E) finite graph; D = diag(D_i), D_i Hermitian r x r; A* = -A, zero off edges, unitary edge blocks, A_ji = -A_ij*; H = D + A; U_ij(X) = A_ij X A_ij*.

## Connection energy (the first book)
- [H,H*] = -2[D,A]; [D,A]_ij = (D_i - U_ij(D_j)) A_ij.
- (1) E_- = (1/8)||[H,H*]||^2 = sum over edges ||D_i - U_ij(D_j)||^2.
- (2) H normal iff D_i = U_ij(D_j) on every edge (D parallel).
- (3) connected G: ker E_- is isomorphic to the Hermitian matrices fixed by the holonomy group at i_0 (commute with every W_C).
- Hermitian D_i is ESSENTIAL (counterexample D_0 = i, D_1 = -i). Reversing a walk of length n gives (-1)^n W*; the sign is invisible to Ad.

## The opposite (the second book)
- H^2 - H*^2 = 2{D,A}; E_+ = (1/8)||H^2 - H*^2||^2 = sum over edges ||D_i + U_ij(D_j)||^2.
- E_+ = 0 iff D is ANTI-parallel: D_i = -U_ij(D_j).
- BUDGET: E_- + E_+ = 2||DA||^2 = 2 sum_i deg(i)||D_i||^2.
- DIFFERENCE: E_- - E_+ = 2 Re Tr((DA)^2) = 4 g(DA), g(X) = (1/2) Re Tr(X^2) — the neutral-signature trace form.
- PRODUCT: E_- E_+ = ||DA||^4 - (Re Tr((DA)^2))^2.
- Bipartite graph: flipping the sign of D on one part swaps E_- and E_+.
- Anti-parallel D is carried along a walk of length n by (-1)^n Ad(W). ker E_+ = the TWISTED fixed set {X : (-1)^{len C} W_C X W_C* = X}. An ODD closed walk with trivial holonomy forces X = 0.
- Double cover: E_-(cover)(S+T, S-T) = 2 E_-(S) + 2 E_+(T).

## Per-edge readings
- Constant shift: [H + cI, (H + cI)*] = [H,H*] (first book blind to c); (H + cI)^2 - ((H+cI)*)^2 = (H^2 - H*^2) + 4cA (second book reads c).
- Trace split: D_i = c_i I + T_i: ||D_i -+ U D_j||^2 = r(c_i -+ c_j)^2 + ||T_i -+ U T_j||^2.
- Duality on an edge: P^2 + V^2 + L^2 = 1, P = (||a||^2 - ||b||^2)/s, V = (||a+b||^2 - ||a-b||^2)/(||a+b||^2 + ||a-b||^2), L^2 = 4(||a||^2||b||^2 - <a,b>^2)/s^2.
- Scalar edge: Gamma = (d_i - d_j)/(d_i + d_j) = tanh(ln(d_i/d_j)/2); (d_i + d_j)^2 - (d_i - d_j)^2 = 4 d_i d_j. Passive (PSD) fields: E_-,e <= E_+,e, |Gamma_e| <= 1.
- Projector fields: ||P - R||^2 + ||P + R||^2 = 4k; E_-,e = 2 sum sin^2(theta_a), E_+,e = 2 sum (1 + cos^2(theta_a)) in principal angles.
- Ring floor (numerical only): sum_k (1 - cos x_k) >= min_w N(1 - cos((d - 2 pi w)/N)) under sum x_k = d mod 2 pi.

## Links to the vacuum-disk puzzle (read off the statements; untested)
1. The scalar edge Gamma = (d_i - d_j)/(d_i + d_j) IS the Smith coordinate. The two books of one edge are |d_i - d_j|^2 and |d_i + d_j|^2: numerator and denominator of the same Gamma. The vacuum disk G = (z - w)/(z - w-bar) has the same shape with d_i = z, d_j = w (numerator) and w-bar (denominator) — but w and w-bar are different points, so it is NOT simply one edge. Whether G is an edge with a transport U that conjugates w is untested.
2. E_- - E_+ = 4 g(DA) with g the NEUTRAL trace form: the same form whose sign wall is Prop 14 of What the Present Must Keep. The sign of the difference of the two books is the sign of that form.
3. The twisted kernel: (-1)^{length} W. On a torus-knot arc the peripheral law is L = (-1)^a M^{-pq} (Dirac Time Thm 13.1(1)). Both carry a parity sign on a loop. Whether a even/odd is the parallel/anti-parallel split is untested.
4. First book blind to a constant, second book reads it (4cA): matches "two readers of a constant".
5. Ring floor with winding w: a constrained minimum over an integer winding — the same shape as "the twist lives in integers".
