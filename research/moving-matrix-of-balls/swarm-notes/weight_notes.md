# Reader notes: "The Weight Between and the Exit Line" (Jeromie Beasley)

Source: Google Drive file ID 14v2vhY6VioQMoy6JkAm0kPBWTsUQ1w27, file name "weight_between_exit_line_v4 (1).pdf".
Read via Drive text extraction (full text returned, 72,600 characters, 22 page markers, nothing cut off).
Local copy of the extracted text: /tmp/claude-0/-home-claude/f86429e3-e32f-50e6-b1fd-fcadab5264af/scratchpad/swarm/work_weight/paper.txt
Pages read: 22 of 22 (pages 1-11 body, 11-12 references, 12 Appendix A, 12-22 Appendix B scripts and printed outputs).
Not seen: Figure 1 itself (page 10) is an image; only its caption and the plotting script (B.3) were read. FIGURE CONTENT NOT READ as an image.
Extraction note: fractions and superscripts came out broken across lines (e.g. "1 / 4", "C2"). Every formula below marked (rebuilt) was reassembled from the surrounding text, proofs and scripts; where the script confirms the form I say so.

---

## 1. What the paper is

- Title as printed: "The Weight Between and the Exit Line"
- Subtitle as printed: "Cross-block bounds for the boundary census, and where opened matter leaves the disk"
- Author as printed: Jeromie Beasley
- Date as printed: 4 November 2026. (The brief said 5 November 2026; the page says 4 November. No version number is printed in the paper; "v4" is only in the file name. Scripts inside are labelled v2: s15_exit_ladder_v2, s16_weight_between_checks_v2, fig09_exit_ladder_v2, s11_exit_quarter_turn_v2.)
- Disclaimer as printed (under the date, above the abstract): "Prepared with AI assistance (Claude, Anthropic; and OpenAI tools for parts of the formal development). The ideas and research direction are the author's. Computation, drafting, formal checking and typesetting were done with AI tools, and every number is produced by a script printed in Appendix B."
- Grades used by the paper: [T] proved here; [L] also checked in Lean in the author's formal suite; [V] verified numerically with the stated controls; [R] a known result in this coordinate; [C] open.
- Structure: Abstract; 1 Introduction; 2 The chart; 3 The weight between; 4 Opened matter; 5 The exit ladder (5.1 The Hermitian band inside the opened one; 5.2 An operator that commutes with the half-chain block; 5.3 The ladder; 5.4 The exit theorem; 5.5 What the theorem explains, and its scope; "The open step"); 6 Status (grade table); References [1]-[9]; A Conventions; B Scripts (B.1-B.9).
- Two things the paper says it proves (Introduction): (1) about the weight between the two sides of a cut, the cross block X_A = C_AB C_BA: "its order, size, symmetry, stability and information bounds", exact examples "marking where the one-body record stops speaking", and "the speed limit of the signed offset"; (2) "where opened matter leaves the disk".
- Setting is a fermionic system cut into a region A and its complement B, described by its one-body correlation matrix C. Second half is one specific chain: the PT-symmetric Su-Schrieffer-Heeger (SSH) chain.

---

## 2. Objects and definitions (his names, his definitions)

### The chart (Sections 1-2)
- Occupation nu: an eigenvalue ("occupation") of the region's correlation matrix.
- z = (1 - nu)/nu = e^epsilon. (ratio)
- epsilon: the rapidity of a level; epsilon = log((1-nu)/nu).
- Gamma = (z-1)/(z+1) = tanh(epsilon/2) = 1 - 2 nu. "Both readings live on one chart."
- The two readings of a cut: "One is unsigned: it counts how many boundary levels are partially occupied. The other is signed: it says which way each level leans."
- Census: "the gauge without its sign." It "counts levels with nu(1-nu) above a threshold, and is blind to the sign of Gamma."
- Offset: "the clock face". The signed offset tau is the rapidity summed over the levels of the region (eq. 1).
- The disk: |Gamma| < 1. The rim: |Gamma| = 1. (One script comment, B.7, calls it "the Smith disk"; the body text only says "the disk" and "the Cayley unit circle".)
- Leaving the disk: "Leaving needs the real part of the ratio to change sign. In the rapidity this is a quarter turn of the phase."

### The weight between (Section 3)
- C = C* with 0 <= C <= I on H_A (+) H_B, dimensions a, b. Block form (rebuilt): C = [[A_C, B_C],[B_C*, D_C]].
- F_A = A_C - A_C^2 : the local defect.
- T_A = (C - C^2)_AA : the AA block of C - C^2.
- X_A = B_C B_C* : THE WEIGHT BETWEEN (abstract: "X_A = C_AB C_BA is the weight between the two sides"). X_B = B_C* B_C.
- Threshold: fix 0 < eps < 1/2 and theta_thr = eps(1 - eps) (the paper writes this with a script-theta, "vartheta"; I write theta_thr to keep it apart from the ladder phase theta).
- Raw census: N^raw_eps = rank 1_[eps, 1-eps](A_C) (number of eigenvalues of A_C in the window).
- Boundary census: N^d_eps = rank 1_[theta_thr, infinity)(X_A) (number of eigenvalues of X_A at or above the threshold). "Counts include multiplicity and equality at the threshold."
- Boundary coordinate: each eigenvalue lambda in [0, 1/4] of X_A has the radius Gamma_b = sqrt(1 - 4 lambda) in [0, 1].
- N_Y(s) = rank 1_[s, infinity)(Y): count of eigenvalues of Y at or above s.
- eta = ||C - C^2|| (distance from being a projector, Theorem 3.3).
- Projector extension P_A of a positive contraction A (rebuilt): P_A = [[A, sqrt(A - A^2)],[sqrt(A - A^2), I - A]].
- h(x) = -x log x - (1-x) log(1-x).
- I_G = Tr h(A_C) + Tr h(D_C) - Tr h(C): the Gaussian mutual information I_G(A:B).
- For the speed limit: P(t) a smooth family of orthogonal projectors; E an isometry onto the region; C = E^dagger P E with 0 < C < I; g = (1/2)||Pdot||_F^2; S = Tr[(C(I-C))^-1]; W = -(C(I-C))^-1; F = E W E^dagger (note: this F is a different object from F_A).

### Opened matter (Section 4)
- "Opening means a non-Hermitian generator."
- PT-symmetric SSH chain: cells c in Z, two sites a, b per cell.
  h(k) = [[ i u , v + w e^{-ik} ],[ v + w e^{ik} , -i u ]] (rebuilt; confirmed by script B.1 block() and B.8 bands()).
  E(k)^2 = v^2 + w^2 - u^2 + 2 v w cos k.
  Parameters u, v, w > 0, v < w; gap condition E(pi)^2 = (w - v)^2 - u^2 > 0.
  Real space: +/- i u on the a and b sites, v inside a cell, w from (c, b) to (c+1, a). H^T = H but H^dagger != H.
- Biorthogonal projector filling the lower band: P(k) = (1/2)(I - h(k)/E(k)), E > 0 (principal square root).
- C_R: the block of that projector on the half-chain c >= 0.
- Y_A = B E = A - A^2 for an idempotent C = [[A, B],[E, D]] (the non-Hermitian stand-in for X_A; here E is a block, not the energy).
- Radial census: #{ |1 - 2 nu_j| <= r }.
- Petermann factor of the band projectors: K(k) = Tr P^dagger P. Band average <K>.
- The Petermann line / exit line: E(0)E(pi) = u^2, equivalently <K> = 2, equivalently (w^2 - v^2)^2 = 2 u^2 (w^2 + v^2).

### The exit ladder (Section 5)
- E_0 = E(0), E_pi = E(pi); w' = (E_0 + E_pi)/2, v' = (E_0 - E_pi)/2: hoppings of "the Hermitian band hidden in the opened one".
- Modulus k = v'/w' (NOTE: the letter k is used both for momentum and for the elliptic modulus); complementary modulus k' = sqrt(1 - k^2) = sqrt(E_0 E_pi)/w'.
- X: the cell-position operator, X_(c,alpha),(c',beta) = c delta_cc' delta_alpha,beta (a different object from X_A).
- T = (1/2){X + 1/2, H} (anticommutator); T = T_L (+) T_R. T_R is "a linearly weighted operator".
- K = K(k), K' = K(k') complete elliptic integrals of the first kind (NOTE: K is also the Petermann factor; context decides). F(phi | k) incomplete elliptic integral of the first kind, F(phi|k) = integral_0^phi (1 - k^2 sin^2 t)^(-1/2) dt, K(k) = F(pi/2 | k). Scripts call mpmath with parameter m = k^2.
- s = u w / (w^2 - v'^2).
- theta = (pi/K) F(arcsin s | k): the shared phase ("Abel phase", "elliptic (Abel) phase"). Equivalently sn(theta K/pi | k) = s.
- Delta = 2 pi K'/K: the ladder spacing.
- The edge ladder / entanglement ladder: eps_j = log((1 - nu_j)/nu_j) = j Delta + i theta, j in Z.
- Gamma_j = tanh(eps_j / 2).
- Continued endpoint offset: Gamma_end = i gamma, gamma = u / sqrt(E_0 E_pi) ("quarter-turn continuation" 2 arctan(u / sqrt(E_0 E_pi))).
- Census rotation: max over block levels of |Im Log((1 - nu)/nu)| / pi (script definition; exit is where it reaches 1/2).
- Endpoint filter: discards levels with nu within a cutoff (10^-9 by default) of 0 or 1.

### Conventions (Appendix A)
- Logarithms natural. Biorthogonal projector uses the principal square root E(k) > 0, "valid throughout the gapped region". The cut lies between cells -1 and 0; the region is c >= 0; in the scripts it is the left edge of a finite block of 90 cells. Phases Im eps use the principal logarithm.

---

## 3. Equations in order

Only two equations carry a printed number: (1) and (2). Everything else is in-line or in theorem statements. All forms below are rebuilt from broken extraction unless a script is cited as confirming.

Section 1 (chart, unnumbered display):
- Gamma = (z - 1)/(z + 1) = tanh(eps/2) = 1 - 2 nu, with z = (1 - nu)/nu = e^eps.

Section 2:
- Prop 2.1: Gamma = tanh(eps/2) = 1 - 2 nu, and nu(1 - nu) = (1 - Gamma^2)/4. For real nu the window nu in [delta, 1 - delta] maps to the real diameter segment [-1 + 2 delta, 1 - 2 delta], i.e. |Gamma| <= 1 - 2 delta.
  Proof lines: z - 1 = (1 - 2nu)/nu, z + 1 = 1/nu; (e^eps - 1)/(e^eps + 1) = tanh(eps/2); 1 - (1 - 2nu)^2 = 4 nu (1 - nu).
- EQUATION (1): tau = sum over nu of eps_nu = Tr[log(I - C) - log C] = log( det(I - C) / det C ).
  "which for a number-conserving Gaussian state is log P(N_A = 0)/P(N_A = |A|)"; P(0) = product(1 - nu), P(|A|) = product(nu) [T].
- Example: diag(0.2, 0.8) and diag(0.2, 0.2) have the same defect C - C^2 = 0.16 I and offsets 0 and log 16.
- Thm 2.2: for z != -1, |z + 1|^2 - |z - 1|^2 = 4 Re z, so |Gamma| < 1 iff Re z > 0 and |Gamma| = 1 iff Re z = 0. For z = e^W, |tanh(W/2)| < 1 iff cos(Im W) > 0; on the principal branch this is |Im W| < pi/2. Proof: Re e^W = e^{Re W} cos Im W.
- Lean-checked real cases: a positive ratio lands strictly inside; a negative ratio S/(-s) with S > s > 0 lands outside at rim distance 2s/(S - s); z = -1 is the pole. z = 1 - i gamma has |Gamma|^2 = gamma^2/(4 + gamma^2) < 1.

Section 3:
- Definitions: F_A = A_C - A_C^2; T_A = (C - C^2)_AA; X_A = B_C B_C*; X_B = B_C* B_C; theta_thr = eps(1 - eps).
- Thm 3.1(1): F_A = T_A + X_A; with C^2 = C, X_A = A_C - A_C^2. Proof: (C^2)_AA = A_C^2 + B_C B_C*.
- Thm 3.1(2): 0 <= X_A <= F_A <= (1/4) I; 0 <= T_A <= F_A; ||B_C|| <= 1/2, attained by C = (1/2)[[1,1],[1,1]]. Proof step: F_A = (1/4)I - (A_C - 1/2)^2 <= (1/4)I, so ||B_C||^2 = ||X_A|| <= 1/4.
- Thm 3.1(3): N^d_eps(A) = N^d_eps(B) <= rank B_C <= min(a, b); Tr X_A = Tr X_B = ||B_C||_F^2 <= (1/4) min(a, b).
- Thm 3.1(4): N^d_eps <= N^raw_eps, equality when C^2 = C. Proof step: nu(1-nu) - theta_thr = (nu - eps)(1 - eps - nu), so rank 1_[theta_thr, inf)(F_A) = N^raw_eps; lambda_j(X_A) <= lambda_j(F_A).
- Thm 3.1(5): theta_thr N^d_eps <= Tr X_A = sum over i in A, j in B of |C_ij|^2; Tr X_A = 0 iff B_C = 0.
- Boundary coordinate: Gamma_b = sqrt(1 - 4 lambda); for a pure Gaussian (Slater) state lambda = nu(1 - nu), so Gamma_b = |1 - 2 nu|.
- Thm 3.2: with delta = ||C - C~||, ||X_A(C) - X_A(C~)|| <= delta; for delta < theta_thr: N_{X_A(C)}(theta_thr + delta) <= N^d_eps(C~) <= N_{X_A(C)}(theta_thr - delta). If dist(theta_thr, spec X_A(C)) > delta the two counts are equal. Proof step: ||BB* - B~B~*|| <= (||B|| + ||B~||)||B - B~|| <= delta.
- Thm 3.3: with eta = ||C - C^2||, X_A <= F_A <= X_A + eta I; hence N_{F_A}(theta_thr + eta) <= N^d_eps <= N^raw_eps.
- Prop 3.4: |Gamma_b(lambda) - Gamma_b(lambda~)| <= 2 sqrt(|lambda - lambda~|); if both radii are at least g > 0, the bound is (2/g)|lambda - lambda~|. Nonnormal counterexample: [[0,1],[0,0]] and [[0,1],[delta,0]] differ by delta while eigenvalues move by sqrt(delta).
- Prop 3.5: X_A(P_A) = A - A^2; disconnected A (+) (I - A) has the same local block and X_A = 0.
- Prop 3.6: Var(N_A) = Tr F_A; Cov(N_A, N_B) = -Tr X_A; on a pure Slater state Var(N_A) = Tr X_A. Proof: Cov(n_i, n_j) = delta_ij C_ii - |C_ij|^2 (Wick).
- Thm 3.7: 4 Tr X_A <= I_G(A:B), constant sharp. If delta I <= C <= (1 - delta) I then I_G <= Tr X_A / (delta(1 - delta)). No upper constant without a margin.
  Proof ingredients: S = I_A (+) (-I_B), C_0 = (1/2)(C + SCS) = A_C (+) D_C; f = h + 2x^2 with f'' = 4 - 1/(x(1-x)) <= 0; I_G >= 2(Tr C^2 - Tr C_0^2) = 4 Tr X_A; on [delta, 1-delta], h + x^2/(2 delta(1-delta)) is convex. Sharpness: C = (1/2)I + r sigma_x has I_G = 4r^2 + O(r^4) and Tr X_A = r^2.
- Thm 3.8 (offset speed limit): taudot^2 <= 4 g S, with g = (1/2)||Pdot||_F^2, S = Tr[(C(I-C))^-1]; equality iff Pdot proportional to [P,[P,F]], F = E W E^dagger, W = -(C(I-C))^-1. For Pdot = -i[H, P], g = ||P H (1 - P)||_F^2.
  Proof steps: taudot = Tr[W Cdot] = Tr[F Pdot]; Pdot is block off-diagonal; T = [P,[P,F]]; taudot^2 <= ||T||_F^2 ||Pdot||_F^2 ... (as extracted; with g = (1/2)||Pdot||^2 and ||T||_F^2 = 2 Tr[W(I-C)WC] = 2S this gives 4gS. The extracted line reads "taudot^2 <= ||T||^2_F ||Pdot||^2_F"; whether a factor 1/4 from the pairing is printed is NOT RECOVERABLE from the extraction, page 5.)
- Prop 3.9: H = omega sigma_x, P_+-(0) = (1/2)(I +- sigma_y), read through the first basis vector. Both have nu = 1/2, tau = 0, X = 1/4, g = omega^2. tau_+-(t) = -/+ 2 artanh(sin 2 omega t). With s = sin 2 omega t: S = 4/(1 - s^2), taudot^2 = 16 omega^2/(1 - s^2) = 4 g S.
- Remark after 3.9: at t = 0, 2 sqrt(Tr X . S) = 2 while |taudot| = 4 omega.

Section 4:
- h(k) and E(k)^2 as in Section 2 of these notes.
- Thm 4.1: for any idempotent C = [[A,B],[E,D]], Y_A = B E = A - A^2, eigenvalues nu_j(1 - nu_j) with algebraic multiplicity. Counterexample to positivity: C = [[2, 1],[-2, -1]] is idempotent with Y_A = -2. (Script B.9 records for this matrix X_A = -2 and Gamma_b = 3.)
- Prop 4.2: K(k) = Tr P^dagger P = 1 + u^2/E(k)^2; <K> = 1 + u^2/(E(0)E(pi)); <K> = 2 iff E(0)E(pi) = u^2 iff
  EQUATION (2): (w^2 - v^2)^2 = 2 u^2 (w^2 + v^2).
  Proof steps: Tr P^dagger P = (1/2)(1 + sum|d_j|^2/|E|^2) for h = d.sigma; sum|d_j|^2 = |v + w e^{ik}|^2 + u^2, |E|^2 = |v + w e^{ik}|^2 - u^2; (1/2pi) integral dk/(A + B cos k) = (A^2 - B^2)^(-1/2) with A^2 - B^2 = E(0)^2 E(pi)^2; ((v+w)^2 - u^2)((w-v)^2 - u^2) = u^4.
- At w = 1: u_exit = (1 - v^2)/sqrt(2(1 + v^2)) (confirmed by script B.1).

Section 5:
- Lemma 5.1: w' = (E_0 + E_pi)/2, v' = (E_0 - E_pi)/2; v'^2 + w'^2 = v^2 + w^2 - u^2; v'w' = vw; E(k)^2 = |v' + w' e^{ik}|^2; k = v'/w'; k' = sqrt(1 - k^2) = sqrt(E_0 E_pi)/w'. Proof: E_0^2 + E_pi^2 = 2(v^2 + w^2 - u^2), E_0^2 - E_pi^2 = 4vw, w'^2 - v'^2 = E_0 E_pi.
- Thm 5.2: T = (1/2){X + 1/2, H}; [P, T] = 0; T = T_L (+) T_R, no entries across the cut between cells -1 and 0; [C_R, T_R] = 0 entrywise as infinite matrices. T_R tridiagonal and symmetric with entries
  T_R (c,a),(c,a) = i u (c + 1/2); T_R (c,b),(c,b) = -i u (c + 1/2); T_R (c,a),(c,b) = v (c + 1/2); T_R (c,b),(c+1,a) = w (c + 1). (confirmed by script Tmat().)
  Proof steps: [X,P]_cc' = (c - c')P_cc' = (i/2pi) integral e^{ik(c-c')} d_k P(k) dk; [P,{X,H}] = {[P,X],H} <-> -i{d_k P, h} = (i/2){d_k(h/E), h}; (h/E)^2 = I gives {d_k(h/E), h/E} = 0. Entry T_ij = (1/2)(x_i + x_j + 1)H_ij crosses the cut only for i = (-1,b), j = (0,a), where x_i + x_j + 1 = 0. (PT)_RR = C_R T_R + P_RL T_LR = C_R T_R; (TP)_RR = T_R C_R.
- Domain lemma (unnumbered): for 0 <= v < w and 0 < u < w - v, s = uw/(w^2 - v'^2) satisfies 0 < s < 1, s -> 1 at the critical boundary u -> w - v. Proof: dv'/du = (u/2)(1/E_pi - 1/E_0) > 0; v' -> sqrt(vw) at the boundary; v'^2 < vw in the open gapped region; w^2 - v'^2 > w(w - v) > wu > 0.
- Measured statement 5.3: s = uw/(w^2 - v'^2) in (0,1); theta = (pi/K) F(arcsin s | k) in (0, pi); Delta = 2 pi K'/K; sn(theta K/pi | k) = s; eps_j = log((1 - nu_j)/nu_j) = j Delta + i theta, j in Z. "All levels share one phase, and there is no real offset."
- Thm 5.4(a): Gamma_j = tanh(eps_j/2) lies on the circular arc through -1, i tan(theta/2) and 1. All |Gamma_j| < 1, = 1, or > 1 according as theta < pi/2, = pi/2, > pi/2.
- Thm 5.4(b): theta = pi/2 iff E(0)E(pi) = u^2 iff <K> = 2 iff (w^2 - v^2)^2 = 2u^2(w^2 + v^2). theta < pi/2 on the side E(0)E(pi) > u^2, theta > pi/2 on the other.
  Proof: sn(K/2 | k)^2 = 1/(1 + k') [ref 9]; theta = pi/2 iff s^2(1 + k') = 1. With W = w', r = sqrt(E_0 E_pi), k' = r/W:
  F := u^2 w^2 (W + r) - W (w^2 - v'^2)^2 = 0.
  w^2, v^2 are the roots of x^2 - (2W^2 - r^2 + u^2)x + W^2(W^2 - r^2) = 0; delta = u^2 - r^2; D = sqrt(4W^2u^2 + delta^2); w^2 = W^2 + (delta + D)/2; w^2 - v'^2 = (u^2 + r^2 + D)/2.
  F(D)F(-D) = W r^2 u^2 (W + r)^2 (W - r)(u^2 - r^2). (confirmed by sympy output B.4)
  Converse: on u^2 = r^2, delta = 0, D = 2Wu, w^2 = W(W + u), w^2 - v'^2 = u(W + u), s^2 = w^2/(W+u)^2 = W/(W + u) = 1/(1 + k').
- Thm 5.4(c) (dimer limit): at v = 0 the half-chain block has exactly one level off {0,1}, eps = 2i arcsin(u/w); leaves the disk exactly at w^2 = 2u^2.
  Proof: dimer matrix [[-iu, w],[w, iu]], E = sqrt(w^2 - u^2); for the single site (0,a) of the cut dimer nu = (1/2)(1 - iu/E), z = (E + iu)/(E - iu), |z| = 1, eps = 2i arctan(u/E) = 2i arcsin(u/w). At v = 0: v' = 0, k = 0, K = pi/2, F(phi|0) = phi, s = u/w, theta = 2 arcsin(u/w).
- Section 5.5 item 2: Gamma_end = i gamma, gamma = u/sqrt(E_0 E_pi); apex of the arc is i tan(theta/2); the two agree only at v = 0 and on the exit line.
- From script B.8 comments (not in body): <K> = 1 + u^2/(E(0)E(pi)) = sec^2(Im tau_inf / 2) with Im tau_inf = 2 arctan(u/sqrt(E(0)E(pi))); source formula named there: endpoint offset of a gapped chain 2 artanh(v/sqrt(E_min E_max)) from "The Offset Belongs to the Boundary".
- Open-step objects: elliptic curve y^2 = -z(v' + w'z)(v'z + w'); the phase is "the Abel image of the point z = -v/w, where the opened eigenvector (E - iu, -(v + wz)) degenerates."

---

## 4. Results with the grades the paper gives

Grade given at the statement / grade in the Section 6 status table (both listed where they differ in wording).

| Result | Grade |
|---|---|
| Prop 2.1 the bridge | [T][L] |
| Thm 2.2 the Cayley domain | [T]; table: "[T] (real cases also in Lean)" |
| Eq (1) product form P(0)=prod(1-nu), P(|A|)=prod(nu) | [T] |
| Thm 3.1(1) defect split | [T][L] |
| Thm 3.1(2) order and size | [T][L] |
| Thm 3.1(3) two-sided | [T] |
| Thm 3.1(4) comparison and recovery | [T] |
| Thm 3.1(5) trace | [T][L] |
| Thm 3.1(6) local unitaries | [T] |
| Table line for all of 3.1 | "[T][L] (Lean: algebraic subclaim)" |
| Boundary coordinate Gamma_b = |1 - 2nu| on pure Slater states | [T][L] |
| Thm 3.2 stability with a certified count | [T] |
| Thm 3.3 near-projector comparison | [T] |
| Prop 3.4 Holder coordinate | [T] |
| Prop 3.5 projector extension; three exact limit cases | [T] |
| Prop 3.6 number covariance | [T] |
| Thm 3.7 4 Tr X_A <= I_G, sharp; upper bound with margin, none without | [T]; table [T][V] |
| Thm 3.8 offset speed limit | [T]; table (with pair) [T][V] |
| Prop 3.9 opposite-direction saturating pair | [T][V] |
| Section 3 numerical controls (script s16) | [V] |
| Thm 4.1 radial census survives opening; positivity does not | [T][L]; table "(Lean: algebraic subclaim)" |
| Prop 4.2 Petermann line | [T][L]; table "(Lean: algebraic subclaim)" |
| Finite-block census exit on the line (~5e-8), filter audit | [V] |
| Lemma 5.1 hidden Hermitian band | [T] |
| Thm 5.2 commuting operator [C_R, T_R] = 0 | [T] |
| Domain lemma 0 < s < 1 | [T] |
| Measured statement 5.3 ladder form, elliptic spacing, Abel phase (200 random points) | [V] |
| u = 0 limit: elliptic spacing of Hermitian dimerized chain, protected nu = 1/2 edge level at j = 0 | [R] |
| Thm 5.4 (a) one phase one crossing, (b) crossing is the Petermann line, (c) dimer limit | [T]; table: "Conditional ladder crossing (any ladder of the stated form) and exact crossing of the proposed phase on the Petermann line [T]"; "Dimer limit, exact [T]" |
| Numerical confirmation of 5.4 (sympy, s15) | [V] |
| Census rotation of plain blocks equals the Abel phase to 7.2e-7 | [V] |
| Analytic derivation of the ladder from T_R | [C] open |

Key wording on what is and is not proved (abstract and intro):
- "The exact commutation, the simultaneous crossing, the location of the crossing and a closed dimer case are proved. The ladder form and the elliptic phase formula are measured at 200 random points. Deriving them analytically is the remaining step."
- "For this proposed ladder, we prove simultaneous crossing of the Cayley unit circle and show that its phase reaches pi/2 exactly on the band-averaged Petermann line <K> = 2, in both directions, the converse through an explicit factorisation."
- Thm 5.2 scope: "a simple eigenvector of T_R is an eigenvector of C_R. No completeness or diagonalizability of T_R is claimed."
- What the paper says is new relative to refs: "the exact entrywise commutation proof, valid without Hermiticity, the elliptic (Abel) phase tested against the edge levels, and its exact crossing on the Petermann line." The commuting-operator construction itself "is that of Peschel and of Eisler and Peschel for Hermitian chains [1,2,4,5]"; "What is new here is that it uses only h(k)^2 = E(k)^2 I."

Three exact cases "marking the edge of the record" [T]:
1. C = pI has full raw census for p in [eps, 1-eps], and zero boundary census for every p.
2. (1/2)(|10><10| + |01><01|) has C = (1/2)I_2 and X_A = 0, yet covariance -1/4 and mutual information log 2.
3. (|1100> + |0011>)/sqrt(2) split {1,2}|{3,4} has X_A = 0 and entanglement entropy log 2.
Conclusion: "A one-body record does not in general determine correlations outside the quasi-free class."

---

## 5. Numbers (all dimensionless; the paper has no physical units anywhere)

Bounds and constants:
- X_A <= 1/4; ||B_C|| <= 1/2; Tr X_A <= (1/4)min(a,b).
- Information constant 4 (sharp): 4 Tr X_A <= I_G.
- Speed limit constant 4: taudot^2 <= 4 g S.
- Petermann value at exit: <K> = 2. Phase at exit: theta = pi/2 (quarter turn).
- Example offsets: diag(0.2,0.8) -> 0; diag(0.2,0.2) -> log 16; common defect 0.16 I.
- Oblique idempotent [[2,1],[-2,-1]]: Y_A = -2 (script: Gamma_b = 3).

Section 3 controls, script s16_weight_between_checks_v2 (seed 16, a = 4, b = 5):
- 400 random contractions: defect split |F - T - X| max 1.87e-16; max eig X - 1/4 = -5.72e-02 (holds with margin); min eig(F - X) line -2.26e-02 (holds); two-sided |spec X_A - spec X_B| 1.39e-16; ordered lambda_j(X) - lambda_j(F) max -2.54e-02; stability ||X - X~||/delta - 1 max -5.66e-01 (perturbation size 1e-3).
- 64 interior covariances, spectrum in [0.05, 0.95]: min(I_G - 4 Tr X) = 2.106e-03; min(Tr X/(d(1-d)) - I_G) = 3.318e-01.
- Sharp family C = (1/2)I + r sigma_x: I_G/Tr X = 4.000266709 (r = 0.01), 4.000002667 (r = 0.001), 4.000000020 (r = 0.0001). Text quotes 4.00027, 4.0000027, 4.00000002.
- 100 orthogonal projectors (pure Slater states): max |X_A - (A_C - A_C^2)| = 6.80e-16 (text: 6.8e-16).
- Speed-limit pair: max |taudot^2/(4gS) - 1| = 5.9e-15 over 3 omegas (0.5, 1.0, 2.0), 2 signs, 31 times (times with |sin 2 omega t| > 0.95 skipped).
- At t = 0 for the pair: 2 sqrt(Tr X . S) = 2 while |taudot| = 4 omega.

Section 4 exit numbers (w = 1):
- u = 0.5 -> v_exit = 0.4682.
- Predicted from <K> = 2 "before the run": u = 0.25, 0.45, 0.65 -> v = 0.7474014, 0.5291503, 0.2357262.
- Measured census exits, 40-cell block (ring N = 2000, endpoint filter 1e-9): 0.7474015, 0.5291503, 0.2357262. Differences +4.04e-08, -1.53e-09, -3.70e-08 ("about 5e-8 or less in these runs"). Script s05b (with helper s05a; script header names MATTER-PEEL-03c / 03d).

Section 5 ladder evidence, script s15_exit_ladder_v2 (seed 15):
- 200 random points, w = 1, v in (0.02, 0.7), u in (0.02, 0.9), gap E_pi >= 0.2; 16 lie past the exit line. Block 90 cells inside a 6000-momentum chain.
- Eigenvector residual ||C_R r - nu r|| max 8.37e-12 (text: at most 8.4e-12; abstract: below 8e-12 -- NOTE the abstract's "below 8 x 10^-12" is not consistent with the printed 8.37e-12; body says "at most 8.4 x 10^-12") over 600 selected levels, three per point (j = 0, +-1); residual filter (res >= 1e-6) removed 0.
- Relative spacing error max 1.67e-08 (text 1.7e-8; abstract 2e-8) over 400 spacing pairs; 0 skipped by the Delta >= 40 rule.
- Phase error max 4.21e-07 (text 4.2e-7; abstract 4e-7) on j = 0, +-1.
- Inside/outside verdict agrees with sign(E_0 E_pi - u^2) at 200/200.
- Max s over the 200 points: 0.9131 (text 0.913).
- Dimer limit v = 0: max |theta_pred - 2 arcsin(u/w)| over 7 values of u (0.1, 0.3, 0.5, 0.6, 0.7, 0.75, 0.9) = 2.22e-16.
- Exit line: max |theta_pred - pi/2| at 6 values of v (0.05, 0.1, 0.2, 0.3, 0.4, 0.5) = 6.66e-16 (text 6.7e-16).
- Deeper levels have nu within 1e-10 of 0 or 1 and are not used.
- Edge-eigenvector selection in script: 12 smallest-|eigenvalue| eigenvectors of T_R, kept if amplitude in the last 30 components <= 1e-9.

Section 5.5 numbers:
- Filter audit (ring 2000, block 40, v = 0.5, w = 1; script incoming_exit_filter, in which this is the m = 0, t1 = 0.5 setting): massless exit at u = 0.4743416 with <K> = 2.000000002 for filters 1e-6 through 1e-9 (script prints exit_gamma 0.4743416490950296, <K> 2.000000001634376 at cuts 1e-6, 1e-8, 1e-9). At 1e-10: 0.4743414673329256, <K> 1.9999957440096103 (seventh digit). At 1e-12: 0.47422795577696786, <K> 1.9973451918175165 (fourth digit).
- Quarter-turn continuation (script s11_exit_quarter_turn_v2): at nine points (u = 0.3, 0.5, 0.7; v at 60%, 80%, 95% of the way to the exit), plain finite blocks 20/40/80/160 measure a census rotation above the continuation by 4e-6 to 3.4e-2, independent of block size. Per point (u, v, pred, gap): (0.3, 0.4171, 0.22032, +9.81e-03); (0.3, 0.5562, 0.25556, +2.13e-02); (0.3, 0.6604, 0.33867, +3.35e-02); (0.5, 0.2809, 0.36265, +4.90e-03); (0.5, 0.3746, 0.39764, +8.02e-03); (0.5, 0.4448, 0.45733, +6.25e-03); (0.7, 0.0492, 0.49587, +9.73e-06); (0.7, 0.0656, 0.49765, +9.93e-06); (0.7, 0.0779, 0.49936, +3.87e-06). Script verdict printed: "KILLED at the stated bar" (the quarter-turn continuation is NOT the census rotation away from the exit); opposite (Hermitian-form guess 2 arctan(u/E(pi))/pi) "fails as required".
- Census rotation vs Abel phase (script s18, blocks 40 and 80, same nine points): largest |difference| 7.21e-07 (text 7.2e-7). Per-point theta/pi: 0.230133206; 0.276925154; 0.372154620; 0.367545731; 0.405669425; 0.463574889; 0.495879103; 0.497660472; 0.499359218.
- Massive band d = (t1 + cos k, sin k, m + i gamma) (script s06, header MATTER-DISK-S06, "the cone paper's band in 1D"): general Petermann formula K = (1 + |d|^2/|E|^2)/2 worst error 1.49e-13 on 300 random points. Exits: (t1, m) = (0.5, 0.4): gamma 0.1691699, <K> 1.022352 FAIL; (1.5, 0.4): 0.1956728, 1.018838 FAIL; (0.5, 0.0): 0.4743416, 2.000000 PASS; (1.5, 0.8): 0.2518871, 1.015041 FAIL. Printed verdict: "KILLED on the second model at the stated bar." Body text: at m = 0.4 census exits "far earlier, at <K> ~ 1.02".
- Filter dependence on the massive band (m = 0.4, t1 = 0.5): exit gamma 0.2716369 (<K> 1.05797) at cuts 1e-6 and 1e-8; 0.1691699 (<K> 1.02235) at 1e-9 and 1e-10; 0.1227914 (<K> 1.01175) at 1e-12. Text: "from gamma = 0.2716 at 10^-6 to 0.1228 at 10^-12".
- Figure 1 settings (from caption and script fig09): left panel theta vs v at u = 0.3, 0.5, 0.7 (w = 1), measured Im eps_0 from 90-cell block, dashed quarter-turn continuation, stars on the exit line; right panel ladder Gamma_j, j = -3..3, at u = 0.5 for v = 0.30 (inside), v = v_exit (on the rim), v = 0.48 (past the exit).

Script-file inconsistency to know about: B.5 (s18) does exec(open('s15_exit_ladder.py')...), i.e. it loads "s15_exit_ladder.py" without the _v2 suffix, while the listed file is s15_exit_ladder_v2.py.

---

## 6. Limits, failures and open items stated by the paper

1. OPEN [C]: "An analytic derivation of the ladder for the coupled chain remains open." The ladder form eps_j = j Delta + i theta and the elliptic phase formula are measured ([V]) at 200 points on levels j = 0, +-1 only. Suggested route: Wiener-Hopf factorisation of the band symbol on the elliptic curve y^2 = -z(v' + w'z)(v'z + w'). "With it, the exit law on the coupled PT-symmetric chain would be a theorem end to end."
2. Thm 5.4 is conditional: it "turns any ladder of the measured form into the exit law." Parts (a) and (b) are theorems about the proposed ladder, not a proof that the chain has that ladder.
3. Thm 5.2 gives invariant eigenspaces only; "No completeness or diagonalizability of T_R is claimed." The numerical figure is "a residual on selected eigenvectors, not an operator norm of [C_R, T_R]".
4. Deeper ladder levels (nu within 1e-10 of 0 or 1) are not tested: "There the nonnormal eigenproblem is ill-conditioned, and they are not used."
5. Positivity fails after opening: Y_A can be negative (example Y_A = -2). Only the radial census survives. So all Section 3 order/size bounds (0 <= X_A <= 1/4, etc.) are Hermitian-C results and do not carry to the opened chain.
6. Mixed states: "X_A need not commute with A_C, and only the order comparisons remain."
7. No upper bound on I_G in terms of Tr X_A without a spectral margin.
8. One-body record limits: X_A = 0 does not mean no correlation outside the quasi-free class (the three exact cases).
9. "The speed budget does not choose the future": same census, offset, cross weight and coupling, opposite directions.
10. "The cross weight of a fixed cut is not the generator coupling of the moving projector."
11. Eigenvalue stability "does not transfer to nonnormal matrices" (Prop 3.4 example).
12. The exit law <K> = 2 is NOT universal: on the massive band (complex on-site term, m != 0) the census exits far earlier (<K> ~ 1.02) and the exit moves with the filter. Statement 5.3 and Thm 5.4(b) "are stated for real u only, where the on-site term is purely imaginary." "Whether its ladder still carries a single phase is not tested here."
13. The quarter-turn continuation of the endpoint offset (from "The Offset Belongs to the Boundary") fits only at v = 0 and on the exit line; elsewhere the census rotation sits above it by 4e-6 to 3.4e-2, block-size independent. That excess "is the Abel phase."
14. Partition dependence: "The cut runs between cells. With w = 0 every whole-cell block is idempotent and nothing leaves, even where <K> = 2." The level that exits "belongs to a dimer cut in two."
15. Filter: the exit on the PT-symmetric SSH chain is filter-independent from 1e-6 to 1e-9, shifts in the seventh digit at 1e-10 and the fourth at 1e-12.
16. Convention caveat for comparison with ref [6] (Rottoli, Fossati, Calabrese): "their hopping and cut conventions differ from those used here and must be translated before sectors are compared."
17. Lean coverage is partial where the table says "(Lean: algebraic subclaim)"; Cayley domain only "real cases also in Lean".
18. Thm 5.2 scope: needs only h(k)^2 = E(k)^2 I and nearest-cell hopping, "so the commuting operator exists for any such two-band chain."

---

## 7. What in this paper bears on the team's five questions

Plain statement first: the paper contains NO mention of the Sun, planets, bodies, balls, light, photons, energy flow, admittance, impedance, a source, or a hyperbolic field. (Word counts in the extracted text: admittance 0, impedance 0, hyperbolic 0, light 0, energy 0, ball 0, source 0. "Smith" appears once, in a script comment: "the census levels leave the Smith disk".) Everything below is what the paper does say that touches those questions; nothing below is a statement by the paper about suns, planets or balls.

### (a) "Rate is weight"
- The paper has no sentence "rate is weight". What it has is the offset speed limit (Thm 3.8): taudot^2 <= 4 g S, where g = (1/2)||Pdot||_F^2 is the rate of the moving projector (for Pdot = -i[H,P], g = ||P H (1-P)||_F^2, the generator coupling across occupied/empty) and S = Tr[(C(I-C))^-1].
- On a pure Slater state the weight between has eigenvalues lambda = nu(1-nu), and S = sum 1/(nu(1-nu)) = sum 1/lambda. So S is the sum of inverse weights between: the bound on the rate of the offset is 4 x (coupling) x (sum of inverse cross-weights). (This last sentence is my rewriting of his S using his own identity lambda = nu(1-nu); the paper does not write it in this form.)
- The paper explicitly separates the two: "The cross weight of a fixed cut is not the generator coupling of the moving projector. At t = 0, 2 sqrt(Tr X . S) = 2 while |taudot| = 4 omega." So in this paper the weight X is a static record of a cut and the rate involves g separately. Anyone using "rate is weight" in the build needs to know this paper does not identify them; it bounds the rate using both.
- Prop 3.9: the bound does not fix the direction. Two preparations with identical nu = 1/2, tau = 0, X = 1/4, g = omega^2 run tau in opposite directions, both saturating.
- A different sense in which the weight is a rate-like quantity: Prop 3.6, Cov(N_A, N_B) = -Tr X_A and on a pure Slater state Var(N_A) = Tr X_A (number fluctuation across the cut).

### (b) What weight sits between two bodies or two balls
- His definition is for the two sides A and B of one cut of one system: X_A = B_C B_C* (= C_AB C_BA), built from the cross block of the correlation matrix. Facts available:
  - It is two-sided: X_A and X_B have the same positive eigenvalues with multiplicity; Tr X_A = Tr X_B = ||B_C||_F^2 = sum over i in A, j in B of |C_ij|^2. So "the weight between" is one quantity shared by both sides, not one per side.
  - It is bounded: 0 <= X_A <= 1/4 per level; total Tr X_A <= (1/4)min(a, b), so it is capped by the smaller side.
  - It lies below the local defect: X_A <= F_A = A_C - A_C^2, with equality (X_A = F_A) exactly when C is a projector (pure Slater state). For a mixed state the remainder T_A is local, not between.
  - Radius on the chart: Gamma_b = sqrt(1 - 4 lambda); maximum weight 1/4 sits at the centre of the disk (Gamma_b = 0), zero weight at the rim (Gamma_b = 1).
  - It bounds the information across the cut from below: 4 Tr X_A <= I_G(A:B).
  - Same local block, different weight between (Prop 3.5): the local block A alone does not determine the weight; it can be anything from 0 (disconnected A (+) (I - A)) up to A - A^2 (projector extension).
  - Unchanged by local unitaries U_A (+) U_B.
- Nothing in the paper treats more than two sides, three or more units, or a chain of units each handing to the next. Multi-ball weight: NOT IN THIS PAPER.

### (c) The exit line and how light/energy leaves one unit and enters the next
- The paper's exit line is a line in parameter space of the opened (PT-symmetric SSH) chain: E(0)E(pi) = u^2, equivalently <K> = 2, equivalently (w^2 - v^2)^2 = 2u^2(w^2 + v^2); at w = 1, u_exit = (1 - v^2)/sqrt(2(1 + v^2)).
- What exits: the census levels Gamma_j of the half-chain block leave the disk |Gamma| < 1. This happens "inside the gapped phase, before the critical point".
- How: all tested edge levels share one phase theta (eps_j = j Delta + i theta), so they sit on one circular arc through -1, i tan(theta/2), +1 and "cross the rim all at once"; theta reaches pi/2 (a quarter turn) exactly on the exit line. Before: all inside; on the line: all on the rim; past it: all outside.
- Which unit exits: "the level that exits belongs to a dimer cut in two" (dimer limit: the single site (0,a) of the cut dimer, eps = 2i arcsin(u/w), leaves at w^2 = 2u^2). With whole dimers kept intact (w = 0 across the cut) "nothing leaves, even where <K> = 2". So exit is a property of a unit split by the cut, not of whole units.
- Opening keeps the spacing Delta of the hidden Hermitian band (hoppings v', w') and "rotates the whole ladder by one phase".
- The paper does not describe energy or light passing from one unit into the next, nor any re-entry into a neighbouring disk. "Leaves the disk" here means |Gamma_j| crosses 1 as the parameters (u, v, w) are changed. Transfer between units: NOT IN THIS PAPER.

### (d) Admittance and which way it runs outward from a source
- The word admittance does not occur. No direction "outward from a source" is defined. The paper cannot settle this open question.
- What it does fix that the build may lean on: the chart is Gamma = (z - 1)/(z + 1) with ratio z = (1 - nu)/nu = e^eps (empty over filled). With this choice: nu -> 0 (empty) gives z -> infinity, Gamma -> +1; nu -> 1 (full) gives z -> 0, Gamma -> -1; nu = 1/2 gives z = 1, Gamma = 0 (centre, maximal weight 1/4); z = -1 is the pole. Inside the disk iff Re z > 0. Using the inverse ratio nu/(1 - nu) instead flips the sign of Gamma and of eps (and of tau) but not the census, |Gamma|, the weight lambda, or the exit condition. So in this paper the choice of which ratio is "z" is a sign convention for the signed reading (offset), invisible to the unsigned reading (census, weight between).
- The signed quantity that does have a direction is the offset tau = log det(I - C)/det C = log P(N_A = 0)/P(N_A = |A|): positive when the region leans empty, negative when it leans full. Prop 3.9 shows the direction of tau's motion is not determined by census, offset, cross weight and coupling together.
- Rim distance for a negative real ratio S/(-s), S > s > 0: outside at distance 2s/(S - s) (Lean-checked).

### (e) Placing several equal balls on a hyperbolic field
- Nothing on this. The disk in this paper is used only as the chart |Gamma| < 1 with the Cayley map; no hyperbolic metric, distance, tiling or packing is defined. NOT IN THIS PAPER.
- The only "equal spacing" result is the ladder: on the rapidity line the levels are equally spaced, Re eps_j = j Delta, Delta = 2 pi K'(k)/K(k), and under Gamma = tanh(eps/2) they map to points on one circular arc through +-1 crowding toward the two ends. For theta = 0 (Hermitian, u = 0) the arc is the real diameter and the level j = 0 sits at the centre (protected nu = 1/2). This is a statement about entanglement levels of one cut, graded [V] for the opened chain and [R] at u = 0; using it as a placement rule for balls would be the team's step, not the paper's.

### Cross-references to his other papers named inside this one
- "The Offset Belongs to the Boundary" (script B.8 comment): source of the endpoint offset 2 artanh(v/sqrt(E_min E_max)), continued here to Im tau_inf = 2 arctan(u/sqrt(E(0)E(pi))).
- "the cone paper's band in 1D" (script B.7 comment): d = (t1 + cos k, sin k, m + i gamma).
- Script headers MATTER-PEEL-02B, -03c, -03d and MATTER-DISK-S06, -S11-V2 show the lineage of the opened-matter runs.

### References printed (for follow-up questions)
[1] Peschel, J. Phys. A 36 (2003) L205. [2] Peschel, J. Stat. Mech. (2004) P06004. [3] Peschel and Eisler, J. Phys. A 42 (2009) 504003. [4] Eisler and Peschel, J. Stat. Mech. (2013) P04028. [5] Eisler and Peschel, J. Phys. A 50 (2017) 284003. [6] Rottoli, Fossati, Calabrese, J. Stat. Mech. (2024) 063102, arXiv:2402.04776. [7] Chang, You, Wen, Ryu, Phys. Rev. Research 2 (2020) 033069. [8] Herviou, Regnault, Bardarson, SciPost Phys. 7 (2019) 069, arXiv:1908.09852. [9] Byrd and Friedman, Handbook of Elliptic Integrals for Engineers and Scientists, 2nd ed., Springer (1971).
