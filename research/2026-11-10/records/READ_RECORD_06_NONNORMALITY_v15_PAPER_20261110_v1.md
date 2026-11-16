# Read record 06 — Non-Normality Is Connection Energy, and its opposite: the v15 PAPER (94 pages)

**CORRECTED BY v16 (21-22 October): see READ_RECORD_07. Equal books is not the wall outside real traceless 2x2; the flow statement is now a theorem; 47 not 162 Koide preimages; two different coupling blocks B. Read 07 before using anything below.**

Source: Drive file "nonnormality_connection_energy_complete_v1 (1).pdf" (30 Oct 2026), whose Part 1 is the 94 pages of v15 as published (Zenodo 23787997). Read through Drive's text extraction: equations are present but broken across lines; rebuilt here from the surrounding text. Equation numbers are the paper's.

## 1. The operator and its two energies
- H = D + A; U_ij(X) = A_ij X A_ij*. (1) E_- = (1/8)||[H,H*]||^2 = sum_E ||D_i - U_ij D_j||^2. (2) for Hermitian S, skew K: [S+K,(S+K)*] = 2[K,S]. (3) H normal iff D parallel. (4) ker E_- = holonomy-fixed Hermitian matrices. Kernel on Herm(2): 4 on a tree, 2 on one loop, 1 on two loops with holonomies sigma_x, sigma_z.
- (5) E_+ = (1/8)||H^2 - H*^2||^2 = sum_E ||D_i + U_ij D_j||^2.
- BORN READING (6): W_ab = Tr(P_a U_ij(Q_b)) = |<a|A_ij|b>|^2, doubly stochastic. E_-+,e = sum_ab W_ab (lambda_a -+ mu_b)^2; E_- - E_+ = -4 sum W_ab lambda_a mu_b. Balance = zero UNCENTERED cross-moment, not independence.

## 2. One product, two halves
- X = DA: Herm X = (1/2)[D,A], Skew X = (1/2){D,A}; E_- = 2||Herm(DA)||^2, E_+ = 2||Skew(DA)||^2.
- (7) budget E_- + E_+ = 2 sum deg(i)||D_i||^2 = 2||DA||^2: independent of the transport. (8) E_- - E_+ = 2 Re Tr(DA)^2 = -4 sum_E Tr(D_i U_ij D_j).
- (9) E_- E_+ per edge = s^2 - 4<a,b>^2.
- SECTOR FLIP (10)-(11): r = r*, r^2 = I; X = A (crossing, rAr = -A) + B (inside). Herm(rA) = r Skew A, Skew(rA) = r Herm A; Tr X^2 + Tr(rX)^2 = 2 Tr B^2. rA = i U A U*, U = e^{-i pi r/4}: A QUARTER TURN, (rA)^2 = -A^2. Keeps the self-commutator, reverses the trace form. What the flip cannot move is the coupling inside a sector.
- (12) with r = 2P - 1: crossing part = PX(1-P) + (1-P)XP = redistribution.
- RELAXATION FLOW (13): K-dot = -2[[K,K*],K]; d/dt ||K||^2 = -8 S, S = (1/2)||[K,K*]||^2 = 4E_- on the class D + A. Lax flow, keeps the spectrum; total drained = Henrici departure ||K(0)||^2 - sum |lambda|^2. (14) E_-(K) = (1/4)(||K*K||^2 - ||K^2||^2); E_+(K) = (1/4)(||K^2||^2 - Re Tr K^4). E_+ falls too, to 2 sum (Re lambda Im lambda)^2. Dual flow K-dot = -2[C,K*] keeps ||K||^2.

## 3. Zero sets; odd loops frustrate
- (15)-(16) anti-parallel; twisted kernel with (-1)^{length}. An odd loop with trivial holonomy admits NO anti-parallel field.
- (17) bipartite sign flip swaps the books. (18) double cover: E_-(cover) = 2E_-(S) + 2E_+(T). "The two energies are the even and the odd half of one connection energy on the double cover."
- (19) rank-one field in C^2 on an odd cycle: min sum p_e = (N/2)(1 - cos(pi/N)) > 0; in R^3 the floor is zero: AN ODD CYCLE NEEDS A THIRD DIRECTION. Triangle = one complete measurement; pentagon = KCBS, weight sqrt5 > 2.

## 4. One edge
- (20) scalar edge: E_-/E_+ = r_e^2, r_e = (d_i - d_j)/(d_i + d_j) = tanh((1/2) ln(d_i/d_j)); E_+ - E_- = 4 d_i d_j (the transmitted part).
- (21) BOOST: d_i -> e^phi d_i, d_j -> e^{-phi} d_j keeps 4 d_i d_j, shifts rapidity by 2 phi: r_e -> (r_e + tanh phi)/(1 + r_e tanh phi). A boost of the two field values, not of spacetime.
- (22) passive: E_- <= E_+. (23) P^2 + V^2 + L^2 = 1 (Jakob-Bergou): predictability, visibility, concurrence. Scalar edges on the circle, matrix edges fill the disc.
- (24)-(25) projector fields: E_-+,e = 2k(1 -+ p_e), p_e = Tr(ab)/k the Born transition probability. "The two books are the improbability and the probability of the transition on each edge."
- (26) for idempotents of equal rank, orthogonal or not: k - Tr(PR) = (1/2)Tr((P-R)^2). Overlap bends as 1 - q(V)t^2/k, q(V) = (1/2) Re Tr V^2.
- (27) with r = 2P_0 - 1 and Hermitian tangent V: rV is an OBLIQUE idempotent tangent with q(rV) = -q(V). Rotation of E_11 gives overlap cos^2 t; its partner under r gives cosh^2 t, above the cap.
- (28) with a declared transport T and metric eta the overlap is a nonnegative square; the number depends on the declared transport. (29) moving frame: i hbar chi-dot = (R*HR - i hbar R* R-dot) chi.

## 5. The constant
- "The opposite book was introduced to understand the offset and direction. A constant is invisible to the connection energy and is recorded by the opposite; a direction is a signed difference that both books erase and that Section 11 keeps."
- (30) trace split. (31) [H + cI, (H+cI)*] = [H,H*]; (H+cI)^2 - (H+cI)*^2 = H^2 - H*^2 + 4cA.
- (32) one site, J = [[0,1],[-1,0]], M real symmetric: MJ + JM = (Tr M)J; [M,J] = [M_0,J]; ||[M,J]||^2 + ||{M,J}||^2 = 4||M||^2.
- (33) centered projectors D = P - (k/r)I: books 2k(1 - rho) and 2k(1 + rho) - 4k^2/r; centered books balance at rho = k/r, uncentered at rho = 0. THE SCALAR BACKGROUND MUST BE DECLARED before two balance conditions are compared.
- (34) common clock G = tau-dot H_0 + aI: [G,G*] = tau-dot^2 [H_0,H_0*]; G^2 - G*^2 = tau-dot^2(H_0^2 - H_0*^2) + 4 tau-dot a A. No ratio of the books can fix a clock rate.

## 6. The scalar shore
- (35) E_- = d^T L_w d (Laplacian), E_+ = d^T Q_w d (signless Laplacian). lambda_min(Q_w) = 0 iff a bipartite component. On a graph with an odd loop the edge books return every vertex norm. (36) dist(D, ker L_U)^2 <= E_-/lambda_+.

## 7. A twisted ring
- D_k = cos(theta_k) sigma_z + sin(theta_k) sigma_x; x_k = theta_k - theta_{k+1} - phi; sum x_k = -d mod 2 pi.
- (37) min E_- = min_w 4N(1 - cos((d - 2 pi w)/N)); min E_+ = min_w 4N(1 - cos((d + N pi - 2 pi w)/N)). ODD N: the floors interleave by a half turn. At d = pi two windings tie; the floor has a CORNER with slopes +-4 sin(pi/N).
- (38) max sum p_k = (N/2)(1 + cos(delta/N)).
- A single loop never frustrates complex subspace fields. (39) two bow ties with sigma_x, sigma_z: 6 - 3 sqrt3 and 4 - 2 sqrt2.
- Two obstructions kept apart: (i) holonomy not unitarisable (Jordan block); (ii) no common invariant subspace.

## 8. Graph primes between the two books
- (40) twisted zeta = product over primes det(I - rho(P)u^{l(P)})^{-1} = det(I - u B_rho)^{-1}. (41) Bass: det(I - uB) = (1 - u^2)^{(m-n)d} det K(u), K(u) = I - uA_rho + u^2(Deg - I). Needs only rho_ji rho_ij = I.
- (42)-(43) THE TWO ENDS: K(+1) = Deg - A = L_-, K(-1) = Deg + A = L_+; <D, L_-+ D> = E_-+. The u = +1 end of the Bass pencil is the connection-energy operator, the u = -1 end its opposite.
- (44) the sign is the parity of the prime: u -> -u multiplies each prime's holonomy by (-1)^{l(P)}. (45) zeta(cover)(u) = zeta(u) zeta(-u).
- (46) books of a unit holonomy eigenvalue: |1 - lambda|^2 + |1 + lambda|^2 = 4; difference 4 Re lambda. Defect and guard of a relator (UPG torus anchor): clock/shift in dimension d: defect 4 sin^2(pi/d), guard 4 cos^2(pi/d); at d = 2 the guard closes.
- (47)-(49) (q+1)-regular: K(1/(qu)) = (qu^2)^{-1}K(u); zeros off |u| = 1/sqrt q are 2 x #{|lambda| > 2 sqrt q}.
- (50) prime traces: t_l = c t_{l-1} - t_{l-2}, t_0 = 2, t_1 = c = lambda/sqrt q (Chebyshev). (51) continued fraction c - 1/(c - ...) converges to the dominant root iff |c| > 2 (Pincherle).
- (52) companion M = [[c,-1],[1,0]], T = M - (c/2)I: T^2 = (c^2/4 - 1)I; q(T) = c^2/4 - 1. Hermitian half wins off the bound, skew half inside; AT |c| = 2 T IS A NONZERO NILPOTENT — the wall. (53) accumulated stress 4/c^2 rises to 1 at |c| = 2. (54) single eigenline diverges like the inverse gap; the pair projector does not move.
- (55)-(56) Hermitian circulant, eigenvalues d + 2t cos(phi + 2 pi j/3): quadratic data fix d and t; the angle enters only through cos 3 phi at THIRD order.
- THEOREM 2 (57)-(58): triangle with e^{i phi} on each edge: zeta^{-1} = 1 - C_3 u^3 + u^6, C_3 = 2 cos 3 phi; (d, t, C_3) recover the spectrum: det(vI - S) = (v-d)^3 - 3t^2(v-d) - t^3 C_3. A graph prime completes a two-book record.
- Prop 3 (59): a scalar phase is invisible to the induced (adjoint) transport; U = diag(e^{i phi}, 1) keeps it: Tr Ad(U^3) = 2 + C_3. Same field, same two books, different cycle coefficient.
- Climb or swap: around one exceptional point eigenvalues swap in pairs; normal form [[0,1],[delta,0]] swaps after one loop, returns after two.

(Sections 9-13: appended below.)

## 9. Arithmetic primes as connection edges
- (60)-(61) a_p = p + 1 - N_p = 2 sqrt p cos(theta_p); U_p = diag(e^{i theta_p}, e^{-i theta_p}).
- THEOREM 4 (62)-(63) Frobenius edge: books E_- = 4p - a_p^2, E_+ = a_p^2, budget 4p; rho_p = cos^2(theta_p) = a_p^2/(4p).
- Cor 5: at odd p the books never balance (a_p^2 = 2p impossible); Hasse endpoint a_p^2 = 4p never reached.
- Local factor 1 - a_p u + p u^2 is the Ramanujan factor with q = p: c_p = 2 cos(theta_p) strictly inside (-2,2): the skew half wins at every good prime, no minimal solution.
- THEOREM 6 adjoint sign-blindness: Ad(-U) = Ad(U); the books depend on a_p^2 only and cannot recover the sign of a_p. Tr U_p = a_p/sqrt p is the ODD record; rho_p is even.
- (67)-(68) local twist: N_-+ = p + 1 -+ a_p; r_p = a_p/(p+1) = tanh(tau_p/2), tau_p = log(N_+/N_-): the scalar edge again, and it KEEPS the sign.
- Prop 7 (69): global twist a_p(E^(d)) = chi_d(p) a_p(E). (70)-(72) conditional partial-product statement; registered test FAILED as registered (correlation 0.468 < 0.7). Murmurations reproduced by the signed record (correlation -0.985); the even book record cannot carry them.
- (73) normalised local factor 1 - 2 cos(theta_p) z + z^2 = the triangle factor with z = u^3, cos theta_p = cos 3 phi [structural comparison only].

## 10. The wall
- (74) every real traceless 2x2 T: T^2 = q(T) I, q = (1/2)(||Herm T||^2 - ||Skew T||^2). q > 0 grows/decays; q < 0 turns; q = 0 with T != 0: NONZERO NILPOTENT = THE WALL.
- Spinning key (75)-(76): M = [[0,a],[b,0]], h = (a+b)/2, r = (a-b)/2: M^2 = (h^2 - r^2)I; ||[M,M^T]||^2 = 32 h^2 r^2; tumbling rate sqrt(ab) = |Omega| sqrt((I3-I2)(I2-I1)/(I1 I3)). The marked axis is an unsigned line (even record); the angular momentum is signed (odd record). The sector sign turns growth into turning at fixed non-normality.
- Normal envelope; the self-commutator does not measure gain.
- Damped oscillator (77)-(79): T^2 = omega^2(zeta^2 - 1)I; critical damping zeta = 1 is the wall; decay rate alpha peaks only there; at the wall e^{tG} = e^{-omega t}(I + tT). Jordan block [[-b, mu],[0,-b]] grows transiently iff |mu| > 2b; critical damping sits at kappa = 2.
- Many degrees of freedom: fastest asymptotic settling lands on a defective pair (40/40). But q = 0 is a wall ONLY for real traceless 2x2 blocks (80).
- Orbit: [[0,1],[-kappa^2,0]] nilpotent at the ISCO (r = 6M, L^2 = 12M^2).
- Four-body transport: discriminant = 4q(T), a quadratic form with determinant 16 w1 w2 w3 >= 0; (81) normal iff trace-free parts of t and w parallel; at the coplanar wall the Gram-chart block is nilpotent but in the Bures metric the eigenprojector norm stays 1 and the wall is at FINITE distance arcsin x_0. (82) ||P_lambda|| g -> |c|; log det = 2 log lambda with no reference to eigenvectors.
- Leptons (83)-(89): h^2/s^2 = 3Q - 1; Z = h1 sigma_z + h2 sigma_x + sJ, Z^2 = (h^2 - s^2)I; Koide Q = 2/3 iff Z nilpotent iff democratic weight p = 1/(3Q) = 1/2. (86) centered plane books (2(1 - rho_K), 2 rho_K) = (1,1) at Koide. (88) zeta^2 = 3Q - 1: Koide = critical damping [CONDITIONAL]. (89) the cubic record e_3 (sin 3 theta) stays free = C_3. Measured Q - 2/3 = -2.2e-6 (0.43 sigma).
- (90) cooling does not select the wall.

## 11. Records the two books do not keep
- The books are EVEN. For a reversal I: F_even = (F + F.I)/2, F_odd = (F - F.I)/2. "The even half is read exactly... What the even half cannot return is listed exactly: which end is larger, the sign of a_p, the cycle coefficient, the orientation of a loop, the endpoint of a route, the signed curvature, the future of a hidden channel. Each needs its own carrier."
- (91) E_-+(H^T) = E_-+(H): books blind to the direction of an edge; the resolvent sees it.
- (92) log det(M + tE) - log det M = sum log(1 + t^2 omega_j^2) >= 0: a ledger sees a skew transport only at second order. Hermitian coupling lowers log det, skew coupling raises it, same K.
- (93) fermion edge: d_i = 1 - nu, d_j = nu: E_- = (1 - 2 nu)^2, E_+ = 1, tau_nu = log((1-nu)/nu) = 2 artanh(1 - 2 nu).
- (94) g_{1-P} = g_P, Omega_{1-P} = -Omega_P: the metric is the even record of the flip, the curvature the odd one.
- (95) tau = log(det(I-C)/det C) = sum tau_nu_j. C - C^2 = BB*: nu(1-nu) is a coupling weight across the cut, largest at nu = 1/2.
- (96) boundary sets the sign: e^{tau_{B+x}} = e^{tau_B} s_0/s_1; the sign flips when the two Schur residuals trade places.
- Rice-Mele: one self-dual mode nu = 1/2 in every ODD block, none in even; (-1)^n tau -> 2 artanh(v/sqrt(E_min E_max)). Kitaev: two modes approach 1/2 for every length; offset vanishes.
- Synchronising rule: 6 registered predictions, 4 held, 2 failed.
- ROUTE AND ENDPOINT (97)-(98): rapidities r_j = (1/2) ln(E_{j+1}/E_j); L_rec = 2 sum |r_j|; D_end = 2|sum r_j|; L_rec - D_end = 4 min(R_+, R_-). THE BOOKS FIX EVERY |r_j| (the route) BUT NOT THE SIGNS (the endpoint). P_e = tanh 2r_j odd, V_e = sech 2r_j even. Lifts R(b rho) diag(e^{2 rho}, e^{4 rho}) R^T: same spectrum and record for every b, projector moves at speed |b|.
- Smith chart (99): Z_b = Schur complement; I - S_b* S_b = 4 (WV_b)*(Herm L)(WV_b). Positive ratio on the real diameter, w = tanh(tau/2); unit-modulus eigenvalue ON THE CIRCLE. Horizon = matched load at the centre; Sun's trapped modes on the circle. The half-plane map (z - i)/(z + i) and the disk map (z-1)/(z+1) must not be mixed.
- (101)-(103) overlaps beyond the first: rho, F, D with D^{1/k} <= F <= rho; Bargmann triple product Tr P_0 P_1 P_2^+- = (1 +- i)/4 with every pairwise overlap 1/2: THE CUBIC LOOP IS WHERE A SIGNED PHASE SURVIVES A PAIRWISE SUMMARY.
- (104)-(106) hidden channel: C = [H,P]: ||C||^2 = 2 Tr BB* = 2 Tr K(0); q(C) = -Tr BB*; q(-iC) = +Tr BB*. Two-level splitting law gap^2 = (H_11 - H_22)^2 + 2||[H,P]||^2. Compression defect PH^2P - (PHP)^2 >= 0. Two hidden channels have the same kernel iff moments agree for n < q_1 + q_2. Tower and well: self-energy negative below the hidden spectrum, positive above. Stiffening wall: displacement (even) dies like kappa^{-1/2}, phase (signed) keeps counting.

## 12. Penrose and the two books
- Exact: on the isotropic Schwarzschild slice psi = 1 + a/rho, lambda = (1 - a/rho)/(1 + a/rho) = tanh((1/2) log(rho/a)); (107) (1 + lambda)psi/2 = 1, (1 - lambda)psi/2 = a/rho; the inversion rho -> a^2/rho swaps the sheets = the sign flip that swaps the books.
- Structural: fold (108) ds^2 = dX^2/(4c^2 X) = d lambda^2/c^2, X = lambda^2. Reissner-Nordstrom r_+ r_- = Q^2, tau_+ = -tau_-. "A Killing horizon has its kernel along the stratum, while the coplanar wall has it across." Ring floors tie at d = pi with a corner.

## 13 + scope + open
- Origin: the 18-21 June 2026 construction H_N = D + A with skew transport A_{n,n+1} = J; edge term J B_{n+1} - B_n J. "A is time-like transport and D space-like obstruction" (roles, not a signature).
- Open: derive a generator selecting both the cone and C_3; which holonomy probes can be measured; is the rate of E_+ along the relaxation flow never positive; noble gases as a test of the defect 2 Tr B^2 (cross-sector vs same-sector coupling) — NOT RUN; a lower bound on the Born shortfall by distance from a common fixed subspace.

## Appendix A (proofs) and Appendix B (Lean table) — read to p74
- Frobenius edge proof: conjugation by U_p rotates sigma_x by 2 theta_p in the (sigma_x, sigma_y) plane; books 4p sin^2 theta_p and 4p cos^2 theta_p; overlap |<+|U_p|+>|^2 = cos^2 theta_p.
- Twists: N = p + 1 + chi_d(p) sum chi_p(f(x)); log count ratio = 2 artanh(a_p/(p+1)) when chi_d(p) = -1.
- At zeta = 1: I + tT has determinant 1, Frobenius norm^2 = 2 + 4t^2, larger singular value t + sqrt(1 + t^2).
- Stress flow on Z = h1 sigma_z + h2 sigma_x + sJ: C = [Z,Z^T] = 4s(h2 sigma_z - h1 sigma_x); h^2 - s^2 is CONSERVED; on h = s, s(t) = s(0)/sqrt(1 + 32 s(0)^2 t).
- RING CORNER: branches w = 0 and w = 1 of (37) meet at d = pi with derivatives +-4 sin(pi/N).
- Loop with W = [[1,1],[0,1]] preserving a form eta: forces eta_11 = 0 and eta_11 + eta_12 + eta_21 = 0 (a parabolic holonomy forces a null direction of the preserved form).
- (27): rV = P0 V Q0 - Q0 V P0 crosses the sectors; q(rV) = -q(V). Fisher information F_Q = 4 g(V,V)/k. Var(sqrt c_a) is of FOURTH order in the angles.
- (53): right/left eigenvectors of [[c,-1],[1,0]]: (u.v)^2 = (c^2 - 4)/c^2; for rank one B = u v^T, (1/2)||uu^T - vv^T||^2 = 1 - (u.v)^2. At |c| = 2 the right and left eigenvectors are orthogonal.
- (94): Omega_{1-P} = i Tr((1-P)[dP,dP]) = -Omega_P because the trace of a commutator is zero. (96) by Schur complements.
- Oblique pairs: T* eta_0 T = eta; with S = eta_0^{1/2}, (26) applied to S P_0 S^{-1}, S Q S^{-1} gives (28).
- Appendix B: Lean declarations for (1),(3),(4),(5),(7),(8), Cor 1, product E_-E_+ = ||DA||^4 - (Re Tr(DA)^2)^2, (15)-(18),(20),(22),(23),(24),(30),(31),(35),(10),(26),(83). 163 declarations, 17 false controls. NOT formalised: equality case of (22), quarter turn (11), projector forms (25), odd floor (19), ring maximum (38), bow tie (39).
COVERAGE: complete. Pages 75-94 (v15-additions Lean table, cross-library table, Appendix C checks with gates G1-G75, references 1-84) were read from the v15 PDF Jeromie attached on 10 November; the Drive text had stopped at page 74.

## Appendix C (checks) — items that bear on the vacuum-disk work
- G64 CIRCLE ODOMETER: spectral flow floor(a1) - floor(a0) = (a1 - a0) + (1/2)(eta1 - eta0); a and a + 1 share spectrum and eta. This is the same integer-plus-eta bookkeeping as Dirac Time Thm 13.2 (arc count = eta window).
- G38 twisted ring, N = 3..8: two windings tie at d = pi, one-sided slopes -+4 sin(pi/N); G38-OPP at d = 0 the floor is smooth.
- G39b clock and shift in dimension d: (defect, guard^2) = (4 sin^2(pi/d), 4 cos^2(pi/d)); the guard closes at d = 2. (UPGTorusAnchor.unit_defect_add_guard, clock_refused_at_two.)
- G40 companion [[c,-1],[1,0]], |c| > 2: limiting stress = 4/c^2; at c = 2 cumulative stress reaches 1.
- G10 single eigenprojector norm times gap tends to 2 at the wall while the pair projector and det stay.
- A10 around one exceptional point: always a swap (2-cycles only); K4 random gains chain into one orbit.
- M26-M28 triangle: det(I - uB) = 1 - C3 u^3 + u^6; a scalar phase is invisible to Ad, a noncentral one is kept; field sigma_z on the noncentral triangle has books (0,24) for every phi though C3 varies.
- M40 pairwise overlaps all 1/2, triple product (1 +- i)/4.
- G1/G2-OPP same |r_j|, other signs: same books on every edge, D_end 1.0 vs 0.6.
- G63 lifts: same eigenvalues for every b, projector speed b^2.
- G33 q = (1/2) Re Tr D^2 on rank-k idempotent tangents has NEUTRAL signature (2k(n-k), 2k(n-k)).
- Failed/killed as registered: G41 (0.468 < 0.7), G42c (rank 2 does not side with rank 0).
- Exploratory scripts named in the code archive and not yet read: t3b_monodromy_group, t4_zeta_mirror, t5_graph_murmuration, fold_tests, pace_tests.
- Cross-library citations to follow up for the vacuum disk: VOTKP.Directed (cancellation_defect, nonunique_lift, lift_isospectral) on branch claude-finish-lean commit bd4d15a; UPGTorusAnchor; DiracTime.PathLedger.descent_iff; VOTKP.Smith.tanh_add'.

## What v15 gives the vacuum-disk puzzle — read off the text, UNTESTED unless marked
1. EVEN vs ODD is the organising split, and v15 lists exactly what the even half loses. The vacuum-disk direction -k^2/(pq) is EVEN in k. By Section 11 the signed partner needs its own carrier: here the candidates are the sign (-1)^a in L = (-1)^a M^{-pq} and the ordered pair (lower step, upper step) of Dirac Time Thm 13.2.
2. THE CUBIC RECORD. Quadratic data fix (d, t); the angle enters only through cos 3 phi (Theorem 2). The vacuum-disk bowl is quadratic in |G| and its first angular term is G^3 + G-bar^3 = 2|G|^3 cos(3 arg G), the three-fold term of the 120-degree racket. Same structure: two books fix the radius, the primitive 3-cycle carries the angle. A scalar phase is lost to the adjoint transport and kept by a noncentral one (Prop 3) — this is the paper's own statement of why the twist is not in the angles of the pieces.
3. ROUTE vs ENDPOINT (97). The books fix |r_j| and lose the signs. Neumann's integer windings p, q on each tetrahedron are sign/branch data the continuous part does not carry (1 of 79 without them).
4. TWISTED RING FLOOR (37): min over integer winding w of 4N(1 - cos((d - 2 pi w)/N)); small-angle form is 2(d - 2 pi w)^2/N — QUADRATIC IN A STEP OVER N. With N = pq and step k this has the shape k^2/(pq). This is the first place in the corpus where a k^2/(pq)-type quantity comes out of a minimum over windings. Untested as an identification.
5. ODD LOOPS: odd N shifts the opposite floor by a half turn; the torus law carries (-1)^a. Untested.
6. THE WALL IS A NILPOTENT (restricted form, see record 07 item A). At the bound |c| = 2 the companion's traceless part is nilpotent; peripheral holonomies of the geometric representation are parabolic (traces +-2) — parabolic = identity plus nilpotent. So the complete hyperbolic structure sits exactly ON the wall q = 0 of Section 10, and the SU(2) arcs (|trace| < 2) are on the turning side. This is a direct match of statements in two of his papers; it is not tested beyond that.
7. Smith vs half-plane maps must not be mixed (Section 11): G = (z - w)/(z - w-bar) is a HALF-PLANE-type Cayley map (pole at w-bar), not the Smith map (z-1)/(z+1).
