# Reader notes: "Matter, Then On Down" (matter_then_on_down_v4.pdf)

Source: Google Drive file 1jDy6nD8DAOaxZmMETbEBFgCKMMGlzOPP, read through the Drive text extraction (280,092 characters).
Local text copy: /tmp/claude-0/-home-claude/f86429e3-e32f-50e6-b1fd-fcadab5264af/scratchpad/swarm/dl_matter/matter.txt
Coverage: all 86 printed pages read (page markers 1 to 86 all present; text ends with the output of fig08 and page number 86). Nothing truncated.
Figures: only captions and the figure-building scripts were readable; the pictures themselves were NOT SEEN (text extraction only).
Equation extraction: display equations arrived broken across lines (fractions and matrices split). Every equation below marked [rebuilt] was reassembled from the broken lines plus the surrounding prose/proof; none was filled from memory.

---------------------------------------------------------------------

## 1. What the paper is

- Title: "Matter, Then On Down". Subtitle: "One coordinate from bulk matter to the nucleus".
- Author: Jeromie Beasley. Printed date/version line: "4 November 2026 Edition 4". File name says v4.
- AI line printed above the abstract: prepared with AI assistance (Claude, Anthropic; and OpenAI tools for parts of the formal development); ideas and research direction are the author's; "every number is produced by a script printed in Appendix C."
- Length: 86 pages. Body pp. 3 to 27; Sources pp. 27 to 28; Appendix A (proofs) pp. 28 to 31; Appendix B (Lean files) pp. 31 to 39; Appendix C (scripts and outputs) pp. 39 to 86.
- Internal inconsistency worth knowing: the Lean file header comment in Appendix B still reads "Matter, Then On Down (Jeromie Beasley, draft v3, 3 November 2026)". Script s14 says v4 source is 110,959 characters against v3's 41,821, and that v4 merges v3 + the "formal edition" (Matter, Gases and VOTKP: Formal Research Edition, 3 Nov 2026, prepared with OpenAI tools) + "review" items + bridges from Beyond the Event Horizon ed. 10 + new figures.
- One-sentence thesis (abstract): "Matter has no absolute size. The zero and the span of every operator description are free, and the one place scale returns is a logarithmic boundary count whose coefficient is fixed by the central charge, A = 2c/pi^2 for an interval." The paper "follows that boundary downward through one coordinate, Gamma = (z-1)/(z+1) = tanh((1/2) ln z), which reads a ratio at every scale": occupation odds at a cut of bulk matter, successive removal energies of an atom, populations of a gas, separation energies of a nucleus, and the complex odds of opened (non-Hermitian) matter.
- Starting physical reading (from Matter at a Scale): "matter is a gap wearing a boundary. A gapped substrate keeps a finite, area-law census; gas, the gapless phase, floods it."

### Grade key (as printed)
- [T] proved here (or proved in Appendix A from the author's earlier papers)
- [L] checked in Lean (Appendix B)
- [V] verified numerically with stated controls
- [R] a reproduction of a known result in this coordinate
- [C] conjecture
- [H] a reading
- [lit] comparison with other people's published data
- [S] a structural comparison between different objects that share a form, with no identification of the objects

### Section list
1 Matter has no absolute size. 2 The boundary keeps a ledger (2.1 Census, offset and one chart; 2.2 The weight between; 2.3 Stability and a certified count; 2.4 What the local record cannot say; 2.5 Number variance and mutual information; 2.6 The speed of the record; 2.7 Warm matter). 3 One chart for all of it. 4 The disk as a reflection chart (4.1 gap step; 4.2 matched load; 4.3 Hawking fermion pair). 5 The atom. 6 Gas (6.1 One neutral state; 6.2 The gas carries the peel back). 7 The nucleus. 8 Present records and later responses (8.1 to 8.4). 9 Opened matter (9.1 opened chain; 9.2 where it leaves the disk; 9.3 offset as the exit's clock; 9.4 two kinds of wall). 10 The even and odd halves. 11 What is proved, what is measured, what is open. Appendices A, B, C.

---------------------------------------------------------------------

## 2. Objects and definitions (his names, his definitions)

Scale / framework
- Zero and span: "Every instrument needs a zero and a span." Zero is free: difference observables unchanged by K -> K + cI. Span is free: spectral projectors, principal angles and the infrared boundary census unchanged by K -> cK, c > 0. The equivalence is the affine one, K -> cK + dI with c > 0, "carried together with the sector it fills" (a shift moves every eigenvalue, so a fixed numerical Fermi level must move with it).
- Physical zero: a ratio must be taken between quantities that have a physical zero. Removal energies are measured from the continuum, separation energies from the next threshold; a raw eigenenergy ratio does not qualify.
- The invariance belongs to the generator K, not to C: rescaling C is a different operation (cross block scales X -> a^2 X, and a census at a fixed numerical threshold changes).
- Substrate: has correlation length xi, lattice scale a, central charge c. Region A with |dA| boundary points.

The ledger at a cut
- C: one-body correlation matrix of a region; eigenvalues nu in (0,1).
- odds: z = (1 - nu)/nu.
- rapidity: eps = ln z.
- Gamma (the one coordinate): Gamma = (z - 1)/(z + 1) = tanh(eps/2) = 1 - 2 nu.
- Window: nu in [delta, 1 - delta] is the disk |Gamma| <= 1 - 2 delta. Window width enters the census as Lambda = log((1 - eps)/eps) (becomes log(1/eps) only for small eps).
- Census N: number of eigenvalues of the restricted correlation matrix in [eps, 1 - eps]. "The census counts levels inside a window of nu(1 - nu)", and nu(1 - nu) = (1 - Gamma^2)/4 is blind to the sign of Gamma.
- Signed offset tau: summed rapidity, tau = Tr[log(I - C) - log C] = log det(I - C) - log det C; for a number-conserving Gaussian (quasi-free) fermion state it is the log-odds of the region being empty against full. Author's words: "The offset is the clock face; the census is the gauge without its sign."
- Four (then five) names for the same function (credited to The Offset Speed Limit): the Smith-chart reflection (z-1)/(z+1); the two-level Gibbs population gap tanh(beta Delta/2); the asymmetry 1 - 2 nu of an occupation against its log-odds; the peel coordinate of VOTKP; fifth (Section 4): the reflection of a wave at a change of spectral gap.
- Cayley pole: the single ratio z = -1, where Gamma is undefined (not large).
- The disk / rim / centre: disk |Gamma| < 1 iff Re z > 0; rim |Gamma| = 1 iff Re z = 0; outside iff Re z < 0. Centre is z = 1.
- Half-turn / quarter-turn: with z = e^W, a negative real ratio has principal phase Im W = pi (half turn) and lies outside the disk; the rim is |Im W| = pi/2 (quarter turn).

The weight between (Section 2.2)
- Split the space into region A (dim a) and rest B (dim b); C = C*, 0 <= C <= I, with blocks A_C (AA block), B_C (AB block), B_C* (BA), D_C (BB).
- F_A = A_C - A_C^2 (local defect).
- T_A = (C - C^2)_AA (mixing inside the region; Lean name "thermalDefect").
- X_A = B_C B_C* = C_AB C_BA: "the weight between", the cross block. X_B = B_C* B_C.
- theta = eps(1 - eps), with 0 < eps < 1/2.
- Raw census N^raw_eps = rank 1_[eps,1-eps](A_C): counts intermediate local occupations.
- Boundary census N^d_eps = rank 1_[theta,inf)(X_A): counts squared cross-block singular values at or above theta. "Counts include multiplicity and equality at the threshold, and the partition is part of the definition."
- Boundary coordinate Gamma_b(lambda) = sqrt(1 - 4 lambda) in [0,1] for each eigenvalue lambda of X_A; a real, unsigned coordinate.
- "One block, many jobs": the same positive square of an off-diagonal block wherever a space is cut. For an orthogonal projector P = [[C, B],[B^dag, C']]: C - C^2 = B B^dag (boundary census of Light Keeps the Ledger; negative quadratic form of the gravity edition). For a Hamiltonian H = [[A,B],[B^dag,D]]: memory kernel K(t) = B e^{-iDt} B^dag with footprint K(0) = B B^dag; P H^2 P - (PHP)^2 = P H Q H P = B B^dag "is exit and return". On the generator: ||P H (1-P)||_F^2 = E_H, "the coupling energy of The Weight Between". "These are the same functional on different operators and different cuts. They are not one quantity."
- eta = ||C - C^2|| in [0, 1/4] (near-projector parameter). delta = ||C - C~|| (perturbation size).
- N_Y(s) = rank 1_[s,inf)(Y).

Speed of the record (Section 2.6)
- P(t): smooth family of orthogonal projectors on C^n; E an n x m isometry onto the region; C = E^dag P E with 0 < C < I.
- g = (1/2)||P_dot||_F^2. S = Tr[(C(I - C))^{-1}]. W = -(C(I-C))^{-1}; F = E W E^dag.
- E_H = ||P H (1 - P)||_F^2: generator coupling, taken on the moving projector P and generator H; contrasted with the cross weight Tr X_A taken on a fixed spatial cut of C.

Peel / ladder (Sections 3, 5, 7)
- Positive ladder I_0,...,I_n; peel steps Gamma_k = tanh((1/2) ln(I_{k+1}/I_k)).
- Composition u (+) v = (u + v)/(1 + uv) ("peel steps add like velocities"; Einstein addition of collinear velocities; half-rapidities add).
- Smith disk read as the Poincare disk: the peel is a walk along a geodesic diameter whose hyperbolic lengths, 2 artanh|Gamma|, add (VOTKP Corollary 15.2).
- Atom: z_q = I_{q+1}/I_q, ratio of successive relaxed removal thresholds; the index labels successive charge-state removals, not excitations within one fixed-charge Hamiltonian.
- Anchored vector: (I_0, Gamma_0, ..., Gamma_{Z-2}); unanchored ratio vector: (Gamma_0,...,Gamma_{Z-2}) alone. Binding sums B_q = sum_{j>=q} I_j.
- Nucleus: z = S_next/S_first (VOTKP section 15.4 order), S a separation energy. Bound peel: z > 0, inside. Negative separation energy: z < 0, |Gamma| > 1.
- Rim distance: |Gamma| - 1.

Reflection chart (Section 4)
- Pullback metric on a projector family: g = a(y) dx^2 + b(y) dy^2 with a = g_par, b = g_perp. Wave psi = e^{ipx} u(y) of the Laplace-Beltrami operator at frequency omega; Clairaut constant C = a sin^2(theta); admittance Y = omega sqrt(a - C) = omega sqrt(g_par) cos(theta).
- IQGT family used: Sigma = cos 3x sigma_x + sin 3x sigma_y + 2.5 y sigma_z, where g_par Delta^2 = 9 (Intrinsic QGT section 8.6), so sqrt(g_par) proportional to 1/Delta (Delta = spectral gap).
- Passive L: Herm L = (1/2)(L + L*) >= 0. Boundary impedance Z_b = L_bb - L_bi L_ii^{-1} L_ib. S_b = (Z_b - I)(Z_b + I)^{-1}. Matched load: Z_b = I, S_b = 0.
- "The inside of the disk is the passive boundary; the centre is the load that returns nothing; the rim is total reflection."
- Polar stratum: "a perfect mirror", |r| = 1.

Gas (Section 6)
- Model: ideal, nonrelativistic, thermodynamic-equilibrium Saha gas of a pure species. Z >= 1, nucleus density N > 0, positive coefficients S_0..S_{Z-1} (number-density units). n_{q+1}/n_q = S_q/x; sum n_q = N; x = sum q n_q = n_e > 0.
- a_0 = 1, a_q = prod_{j<q} S_j; W(x) = sum a_q x^{-q}; p_q = a_q x^{-q}/W; mu = sum q p_q (mean charge); V = sum (q - mu)^2 p_q. Neutrality: x = N mu(x). y = log x.
- lambda_e = h/sqrt(2 pi m_e k_B T). U_q partition functions. E_q = sum_{j<q} I_j.
- L_q (population-only combination), L_B (density-compensated combination), D_q = I_{q+1} - I_q, B = sum I_q. eps_q here (Thm 6.6) = thermal mean excitation of charge state q.
- "On the disk the gas state is a layer that can be varied freely while an atomic record survives it."

Records and responses (Section 8)
- Present record: a census, an offset, a threshold ladder, a gas state. "A complete state evolves deterministically; what fails is the sufficiency of the summary."
- H = [[A,B],[B^dag,D]] on H_A (+) H_B, psi = (x, y): retained amplitude x, hidden amplitude y.
- Memory kernel K(t) = B e^{-iDt/hbar} B^dag; hidden source J(t) = B e^{-iDt/hbar} y(0); footprint K(0) = B B^dag (total channel mass); channel measure dM(lambda) = B dE_D(lambda) B^dag (positive operator-valued); self-energy Sigma(z) = B (z - D)^{-1} B^dag; retained resolvent G_A(z) = (z - A - Sigma(z))^{-1}.
- Angular gas chain: free streaming in 3D in normalised Legendre moments of the direction cosine; tridiagonal M with M_{l,l+1} = M_{l+1,l} = c_l = (l+1)/sqrt((2l+1)(2l+3)); L = -ikM - kappa(I - P_0), P_0 = e_0 e_0^T; density response G(s) = <e_0,(s - L)^{-1} e_0>. Results are "cards": ANG1 to ANG4. E_- = (1/8)||[L, L^dag]||_F^2; E_+ = (1/8)||L^2 - L^dag 2||_F^2 ("the two books of the chain"). "Henrici departure" = ||L||_F^2 - sum|lambda|^2.

Opened matter (Section 9)
- "Opening matter here means a non-Hermitian effective generator."
- PT-symmetric SSH chain h(k) = [[iu, v + w e^{-ik}],[v + w e^{ik}, -iu]] = d . sigma, d = (v + w cos k, w sin k, iu); s = E(k)^2 = d . d = |v + w e^{ik}|^2 - u^2 with the bilinear dot product.
- Biorthogonal projector C = sum_filled |R_k><L_k|, <L_j|R_k> = delta_jk; restricted to a block. Occupations nu complex; Gamma = 1 - 2 nu complex.
- Y_A = B E = C_AB C_BA for an idempotent C = [[A,B],[E,D]]. Radial coordinate R_b(lambda) = sqrt|1 - 4 lambda|. Radial census #{j : R_b(lambda_j) <= r}.
- Round-trip form (cone paper v8): Q = M_{+-} M_{-+}/(E_+ - E_-)^2, M_ab = <L_a| dh |R_b>. Bilinear two-level metric Q_ab = [s (d_a d . d_b d) - (d . d_a d)(d . d_b d)]/(4 s^2).
- Petermann factor K_+- = Tr P*_+- P_+- ; band average <K>.
- gamma = u / sqrt(E(0) E(pi)); tau_end continued endpoint offset; Gamma_end.
- Exit: where the census levels leave the disk (largest rotation |Im Log((1-nu)/nu)|/pi reaches 1/2). Rotation of a level: |Im tau_nu|/pi with tau_nu = Log((1-nu)/nu). Endpoint filter delta: discards levels with nu within delta of 0 or 1.
- Two kinds of wall (from Beyond the Event Horizon ed. 10, section 8): spectral wall: a real pair turns complex; the unfolding coordinate is real on one side and imaginary on the other; the Jordan block at the wall is a property of the operator in every frame. Geometric wall: spectrum stays real on both sides; the Jordan block lives only in a folded chart.

Parity (Section 10)
- Involution J (J^2 = id): f = f_even + f_odd, f_even = (1/2)(f + f o J), f_odd = (1/2)(f - f o J). "Odd parts vanish at fixed points and under J-symmetric pairing or averaging; they do not become false, and they need not vanish merely because a surface is called a wall. Each claim below names its J."

---------------------------------------------------------------------

## 3. Equations in order

Numbered equations in the paper are (1) to (7). Unnumbered displays are listed with their location.

Section 1
- Shift example [T]: eigenvalues (1,2) have ratio 2 and Gamma = 1/3; shifted by -5/4 they become (-1/4, 3/4), ratio -3 and Gamma = 2, same gap.
- (1) [rebuilt]: N = |dA| (c/pi^2) log(xi/a) log((1 - eps)/eps) + ...
  Two-endpoint interval: A = 2c/pi^2.
- Rails form: spacing Delta = 4 pi K(u~)/K'(u~) of the entanglement ladder, N = 4 Lambda/Delta for two cuts [T] (from The Angle Between the Rails).

Section 2.1
- Prop 2.1 (the bridge): Gamma = tanh(eps/2) = 1 - 2 nu; window nu in [delta, 1-delta] is |Gamma| <= 1 - 2 delta; integral over rapidity of the binary entropy: int_{-inf}^{inf} H(nu(eps)) d eps = pi^2/3. Proof uses nu = 1/(1 + e^eps), d nu = -nu(1-nu) d eps, int = 2 zeta(2).
- (2) [rebuilt]: tau = sum_nu eps_nu = Tr[log(I - C) - log C] = log( det(I - C)/det C ) = log( P(N_A = 0)/P(N_A = |A|) ).
  Last equality only for number-conserving Gaussian (quasi-free) fermion states; otherwise (2) is "read as the trace formula alone".
- nu(1 - nu) = (1 - Gamma^2)/4.
- Thm 2.2 (Cayley domain): |z+1|^2 - |z-1|^2 = 4 Re z; |Gamma| < 1 iff Re z > 0; = 1 iff Re z = 0; > 1 iff Re z < 0. For z = e^W: Gamma = tanh(W/2), |tanh(W/2)| < 1 iff cos(Im W) > 0; on the principal branch Im W in (-pi, pi] this is |Im W| < pi/2.
  Kept apart: z = -2 gives finite Gamma = 3; z = 1 - i gamma gives |Gamma|^2 = gamma^2/(4 + gamma^2) < 1 for every gamma ("a complex ratio does not by itself leave the disk... Leaving needs a ratio whose real part changes sign").

Section 2.2
- Definitions display [rebuilt]: C = [[A_C, B_C],[B_C*, D_C]]; F_A = A_C - A_C^2; T_A = (C - C^2)_AA; X_A = B_C B_C* = C_AB C_BA.
- Thm 2.3 items: (1) F_A = T_A + X_A; (2) 0 <= X_A <= F_A <= (1/4) I_A, 0 <= T_A <= F_A, ||B_C|| <= 1/2 attained by C = (1/2)[[1,1],[1,1]]; (3) Tr X_A = Tr X_B = ||B_C||_F^2 <= (1/4) min(a,b), N^d_eps(A) = N^d_eps(B) <= rank B_C <= min(a,b); (4) N^d_eps <= N^raw_eps, equality when C^2 = C; (5) theta N^d_eps <= Tr X_A = sum_{i in A, j in B} |C_ij|^2, Tr X_A = 0 iff B_C = 0; (6) local unitaries U_A (+) U_B leave both censuses unchanged.
  Used in proof: nu(1-nu) - eps(1-eps) = (nu - eps)(1 - eps - nu); F_A = (1/4)I - (A_C - (1/2)I)^2.
- (3) [rebuilt]: Gamma_b(lambda) = sqrt(1 - 4 lambda) in [0,1]; lambda = (1 - Gamma_b^2)/4; lambda >= eps(1 - eps) iff Gamma_b <= 1 - 2 eps.
  On a pure state lambda = nu(1-nu) and Gamma_b = |1 - 2 nu|.

Section 2.3
- Thm 2.4: ||X_A(C) - X_A(C~)|| <= delta; for delta < theta: N_{X_A(C)}(theta + delta) <= N^d_eps(C~) <= N_{X_A(C)}(theta - delta); equal if dist(theta, spec X_A(C)) > delta.
- Thm 2.5: X_A <= F_A <= X_A + eta I_A; N_{F_A}(theta + eta) <= N^d_eps <= N^raw_eps; if theta + eta <= 1/4 the lower count is N^raw_{eps_eta} with eps_eta = (1/2)(1 - sqrt(1 - 4(theta + eta))), otherwise zero.
- Prop 2.6: |Gamma_b(lambda) - Gamma_b(lambda~)| <= 2 sqrt|lambda - lambda~|; if both radii >= g > 0, <= (2/g)|lambda - lambda~|; ordered boundary coordinates move by at most 2 sqrt(delta). Non-normal failure: J_0 = [[0,1],[0,0]], J_delta = [[0,1],[delta,0]] differ by delta in norm, eigenvalues move 0,0 -> +-sqrt(delta).

Section 2.4
- Prop 2.7 projector extension [rebuilt]: P_A = [[A, sqrt(A - A^2)],[sqrt(A - A^2), I - A]] on H_A (+) H_A; same AA block as C_0 = A (+) (I - A); X_A(P_A) = A - A^2 while X_A(C_0) = 0.

Section 2.5
- Prop 2.8: Var(N_A) = Tr(A_C - A_C^2); Cov(N_A, N_B) = -Tr X_A; Var(N_A) = Tr T_A - Cov(N_A,N_B). Wick: Cov(n_i,n_j) = delta_ij C_ii - |C_ij|^2. Pure Slater state: Var(N_A) = Tr X_A.
- Thm 2.9: h(x) = -x log x - (1-x) log(1-x); I_G(A:B) = Tr h(A_C) + Tr h(D_C) - Tr h(C); 4 Tr X_A <= I_G(A:B) (constant 4 sharp); if delta I <= C <= (1-delta) I, 0 < delta <= 1/2: I_G <= Tr X_A/(delta(1-delta)); N^d_eps <= I_G/(4 eps(1-eps)); within the class I_G = 0 iff X_A = 0. Sharp family C = (1/2)I_2 + r sigma_x: Tr X_A = r^2, I_G = 4 r^2 + O(r^4).

Section 2.6
- (4): tau_dot^2 <= 4 g S. Equality iff P_dot is a real multiple of [P,[P,F]], F = E W E^dag, W = -(C(I-C))^{-1}. If P_dot = -i[H,P] then g = E_H = ||P H (1-P)||_F^2 and |tau_dot| <= 2 sqrt(E_H S).
- Prop 2.11 (hbar = 1, H = omega sigma_x, P_+-(0) = (1/2)(I +- sigma_y), read through the first basis vector): nu_+-(t) = (1/2)(1 +- sin 2 omega t); tau_+-(t) = -+ 2 artanh(sin 2 omega t); both saturate (4) at every time. At t = 0: nu = 1/2, Gamma = 0, tau = 0, X = 1/4, E_H = omega^2, |tau_dot| = 4 omega = 2 sqrt(E_H S), whereas 2 sqrt(Tr X . S) = 2. With s = sin 2 omega t: S = 4/(1 - s^2), tau_dot = -+4 omega cos(2 omega t)/(1 - s^2).

Section 3
- Thm 3.1: Gamma_{j->l} = Gamma_j (+) Gamma_{j+1} (+) ... (+) Gamma_{l-1}, u (+) v = (u+v)/(1+uv); from ln(I_l/I_j) = sum ln(I_{k+1}/I_k) and tanh(a+b) = tanh a (+) tanh b.
- Hyperbolic length of a step: 2 artanh|Gamma|; lengths add.
- Ising ladder: entanglement energies eps_0, 3 eps_0, 5 eps_0, ...; Gamma_{j+1} = Gamma_j (+) tanh(eps_0): one constant peel step.

Section 4
- (5) [rebuilt]: Gamma = (sqrt(a_1 - C) - sqrt(a_2 - C))/(sqrt(a_1 - C) + sqrt(a_2 - C)); sqrt(a_2 - C) -> i sqrt(C - a_2) when C > a_2. g_perp drops out; |Gamma| = 1 exactly beyond the geodesic turning point a_2 = C. Normal incidence C = 0: Gamma = tanh((1/2) ln sqrt(a_1/a_2)).
- (6) [rebuilt]: Gamma = (Delta_2 - Delta_1)/(Delta_2 + Delta_1) = tanh((1/2) ln(Delta_2/Delta_1)).
- Prop 4.1: Z_b = L_bb - L_bi L_ii^{-1} L_ib = W* L W, W = [I ; -L_ii^{-1} L_ib]; Herm Z_b = W*(Herm L)W >= 0; I - S_b* S_b = 4 (W V_b)*(Herm L)(W V_b) >= 0, V_b = (Z_b + I)^{-1}; so ||S_b|| <= 1.
- Prop 4.2 (Dirac pair cos r |00> + e^{i phi} sin r |11>, tan^2 r = e^{-hbar omega/k_B T_H}): outside occupation C = sin^2 r; tau = log(det(I-C)/det C) = log(P(empty)/P(full)) = hbar omega/(k_B T_H); Gamma = 1 - 2C = tanh(hbar omega/(2 k_B T_H)) for every pair phase phi; independent modes: tau = sum_k hbar omega_k/(k_B T_H).

Section 5
- Thm 5.1: I = (I_0..I_{Z-1}) -> (I_0, Gamma_0..Gamma_{Z-2}) is a bijection (0,inf)^Z -> (0,inf) x (-1,1)^{Z-1}; inverse I_q = I_0 prod_{j<q} (1 + Gamma_j)/(1 - Gamma_j). Common scale I -> cI leaves every Gamma_q unchanged.
- Helium-like ion charge Z >= 2, last peel step to first order in electron repulsion: Gamma = 5/(8Z - 5) -> 5/(8Z). (A.10: I_He = Z^2/2 - 5Z/8 Hartree, I_H = Z^2/2, J = (5/8) Z.)
- Thomas-Fermi middle of the peel (cited in VOTKP section 15.11): Gamma_k -> tanh((2/3) ln((k+1)/k)) ~ 2/(3k).

Section 6
- Lemma 6.1: d p_q/dy = p_q(mu - q); d mu/dy = -V; d/dy E[f(q)] = -Cov(f(q), q).
- Thm 6.2: unique positive solution, 0 < x < NZ; unique positive root of P(x) = sum_q a_q x^{Z-q+1} - N sum_q q a_q x^{Z-q}, degree Z+1. Helium (u = x/N, alpha = S_0/N, beta = S_1/N): u^3 + alpha u^2 + (alpha beta - alpha) u - 2 alpha beta = 0, 0 < u < 2. Proof via F(x) = x - N mu(x), F' = 1 + NV/x > 1.
- Thm 6.3: d log x/d log N = mu/(mu + V) in (0,1); d mu/d log N = -mu V/(mu + V) < 0; d log p_q/d log N = (mu - q) mu/(mu + V); every upper tail Pr(q >= r) falls with density. With h_q = d_theta log a_q, C_h = Cov_p(q, h_q): d_theta log x = C_h/(mu+V); d_theta mu = mu C_h/(mu+V); d_theta p_q = p_q[h_q - E h - (q - mu) C_h/(mu+V)]. T-independent partition weights: d log x/d log T = Cov(q, (3/2) q + E_q/k_B T)/(mu + V) > 0. At fixed T,N,U: d mu/d I_r = -mu Cov(q, 1_{q>r})/(k_B T (mu + V)) < 0.
- Physical coefficients [rebuilt]: S_q(T) = (2 U_{q+1}(T)/(lambda_e(T)^3 U_q(T))) e^{-I_q/k_B T}; by Thm 5.1, S_q(T) = (2 U_{q+1}/(lambda_e^3 U_q)) exp[ -(I_0/k_B T) prod_{j<q} (1 + Gamma_j)/(1 - Gamma_j) ]. "Saha with a reconstructed threshold input, not a new ionisation law" [T].
- Thm 6.4: (i) S_q -> c S_q, N -> cN preserves every charge fraction, x -> cx. (ii) m_e -> a m_e, T -> bT, I_q -> b I_q with partition ratios held, N -> (ab)^{3/2} N preserve all populations. (iii) No function of the complete anchored threshold record determines the mean charge for all densities at fixed T,U,m_e; no function of the unanchored ratio vector determines it even at fixed T,N,U,m_e.
- Thm 6.5 [rebuilt]: L_q = log(n_q n_{q+2}/n_{q+1}^2) = log(U_q U_{q+2}/U_{q+1}^2) - beta(I_{q+1} - I_q); L_B = log(n_0/(n_Z (n_e lambda_e^3)^Z)) = log(U_0/(2^Z U_Z)) + beta B, B = sum_q I_q. Two temperatures: D_q = -Delta L_q/Delta beta = I_{q+1} - I_q; B = Delta L_B/Delta beta; I_0 = (1/Z)[B - sum_{r=0}^{Z-2} (Z-1-r) D_r]; I_q = I_0 + sum_{r<q} D_r.
- Helium with U = (1,2,1): log(n_0 n_2/n_1^2) = -beta D - log 4; log(n_0/(n_2 n_e^2 lambda_e^6)) = beta B - log 4; Gamma_0 = D/B.
- Thm 6.6: corrected L~_q = L_q - log(U_q U_{q+2}/U_{q+1}^2), L~_B = L_B - log(U_0/2^Z U_Z); omitting bias: -Delta log(U_q U_{q+2}/U_{q+1}^2)/Delta beta and +Delta log(U_0/(2^Z U_Z))/Delta beta; with d log U_q/d beta = -eps_q helium reads D_app = D + eps_0 + eps_2 - 2 eps_1, B_app = B - eps_0 + eps_2. Slope error <= (eta_1 + eta_2)/|Delta beta|; |D^/B^ - D/B| <= (eta_D + |D/B| eta_B)/(B - eta_B).

Section 7
- Outside-rim identity [rebuilt]: S_first = -s < 0, a = S_next/s > 1, z = -a: Gamma = (a+1)/(a-1); |Gamma| - 1 = 2/(a-1) = 2s/(S_next - s); = 2s/S_next when s << S_next [T][L]. Needs S_next > s. Cayley pole z = -1 is S_first + S_next = 0.
- Half-turn: Gamma = tanh(W/2), W = Log z; negative ratio has Im W = pi exactly.

Section 8
- Thm 8.1 [rebuilt]: x_dot(t) = -(i/hbar) A x(t) - (i/hbar) J(t) - (1/hbar^2) int_0^t K(t - s) x(s) ds. K(t) = int e^{-i lambda t/hbar} dM; Sigma(z) = int dM/(z - lambda); G_A(z) = (z - A - Sigma(z))^{-1}; K(0) = M(R) = B B^dag; Im Sigma(z) <= 0 for Im z > 0; sum_{j,k} u_j^dag K(t_j - t_k) u_k = ||sum_k e^{iDt_k/hbar} B^dag u_k||^2 >= 0.
- Prop 8.2: Lambda = diag(-3,-1,1,3); w^(0) = (1,1,1,1)/4, w^(1) = (3,7,1,5)/16; s = (sqrt w_j), v = e_0 - s, R_w = I - v v^T/(1 - s_0), H_w = R_w Lambda R_w^T. Both: spectrum {-3,-1,1,3}, A = 0, B B^T = 5; survival at t = pi/4: 0 and 1/32. a_0 = (cos 3t + cos t)/2; a_1 - a_0 = (i/2) sin^3 t. B D B^T is 0 and 3. G_0 = (z^3 - 5z)/Q, G_1 = (z^3 - 5z + 3)/Q, Q = (z^2-1)(z^2-9); Sigma_0 = (5z^2 - 9)/(z^3 - 5z), Sigma_1 = (5z^2 + 3z - 9)/(z^3 - 5z + 3).
- Prop 8.3: H = sigma_x, psi_+-(0) = (1, +-i)/sqrt 2: K(t) = 1, |x_+-(t)|^2 = (1/2)(1 +- sin 2t); J_+- = +-i/sqrt 2.
- Thm 8.4: x_j = a + jh, w_j = (-1)^j binom(m,j), q_j = p_j + delta w_j, 0 < |delta| < min p_j/|w_j|: equal moments of every order r < m; sum (q_j - p_j) x_j^m = delta (-1)^m m! h^m; F_q(t) - F_p(t) = delta e^{-iat}(1 - e^{-iht})^m.
- Thm 8.5 (kinetic witness): u = (-3,-1,1,3), d = (-1,3,-3,1), rho(x) = rho_*[1 + eta cos kx], p_+-(v) = sum_j (1/4 +- a d_j) g_sigma(v - v_0 u_j), f_+- = rho(x) p_+-(v). K1: M_0 = rho, M_1 = 0, M_2 = (5 v_0^2 + sigma^2) rho, M_3 = +-48 a v_0^3 rho. K2 (free streaming, q = k v_0 t) [rebuilt]: n_+- = rho_*{1 + eta e^{-sigma^2 k^2 t^2/2}[(1/2)(cos q + cos 3q) cos kx -+ 8a sin^3 q sin kx]}; Delta n = -16 a eta rho_* e^{-sigma^2 k^2 t^2/2} sin kx sin^3(k v_0 t). K3: Delta n and its first two time derivatives vanish at t=0; third derivative = -96 a eta rho_* k^3 v_0^3 sin kx. K4: reset E_s[f] = e^{-nu s} f + (1 - e^{-nu s}) rho p_0 multiplies later contrast by exactly e^{-nu s}.
- ANG1: g_0(s) = (1/2) int_{-1}^{1} d mu/(s + ik mu) = arctan(k/s)/k; Z_b(s) = 1/g_0(s) - s -> 2k/pi as s -> 0+.
- ANG2: G = g/(1 - kappa g), g(s) = g_0(s + kappa); isolated real pole s* > -kappa exists iff kappa > 2k/pi, s* = k cot(k/kappa) - kappa.
- ANG3: a difference planted in moment l > 2 first reaches the stress moment at order l - 2 in t with Taylor coefficient k^{l-2} prod_{j=2}^{l-1} c_j/(l-2)!, and first reaches density at order l, for every kappa >= 0.
- ANG4: E_- = (1/8)||[L, L^dag]||_F^2 = k^2 kappa^2/3 for every truncation N >= 2; E_+ grows with N.

Section 9
- Thm 9.1: for any idempotent C = [[A,B],[E,D]]: Y_A = BE = A - A^2; eigenvalues nu_j(1 - nu_j) with algebraic multiplicity; R_b(nu(1-nu)) = |1 - 2 nu|; radial census survives for every r; condition is the disk |lambda - 1/4| <= r^2/4. Positivity does not survive: C = [[2,1],[-2,-1]] is idempotent with Y_A = -2, R_b = 3. Embedding P(A) = [[A, I],[A - A^2, I - A]].
- Thm 9.2: det Q = -u^2 w^2 cos^2 k/(16 s^3). (Abstract writes the same thing as -u^2 w^2 cos^2 k/(16 E(k)^6).) d . (alpha x beta) = -i u w cos k; Q_vv = (w^2 sin^2 k - u^2)/(4 s^2).
- Prop 9.3: K_+- = Tr P*_+- P_+- = (1/2)(1 + sum|d_j|^2/|E|^2) >= 1; on the PT chain with A = v^2 + w^2 - u^2 > |2vw| = |B|: K(k) = 1 + u^2/E(k)^2; <K> = 1 + u^2/sqrt(A^2 - B^2) = 1 + u^2/(E(0)E(pi)); <K> = 2 iff E(0)E(pi) = u^2.
- (7) [rebuilt]: tau_end = 2 artanh(i gamma) = 2i arctan(gamma); Gamma_end = tanh(tau_end/2) = i gamma; <K> = 1 + gamma^2 = sec^2((1/2) Im tau_end). At <K> = 2, gamma = 1: tau_end = i pi/2 (finite), Gamma_end = i on the rim.
- Closed form it continues (The Offset Belongs to the Boundary): endpoint offset of a gapped chain 2 artanh(v/sqrt(E_min E_max)).
- Spectral wall example: sigma_x + i gamma sigma_z, eigenvalues +-sqrt(1 - gamma^2) turn imaginary at gamma = 1, left-right overlap collapses as sqrt(1 - gamma^2), Petermann factor (1 - gamma^2)^{-1}.

Section 10
- Prop 10.1: (i) under nu -> 1 - nu: nu(1-nu), every census and every Gamma_b are even; Gamma = 1 - 2 nu and tau are odd. (ii) P -> I - P, (V,W) -> (-V,-W) sends Q = Tr(PVW) to its conjugate: quantum metric g = Re Q even, curvature Omega = 2 Im Q odd. (iii) R_{H*}(z) = R_H(z-bar)*; not in general -R_H(z).
- Curvature bound: |Omega(V,W)| <= 2 sqrt(g(V,V) g(W,W) - g(V,W)^2) (A.17).

---------------------------------------------------------------------

## 4. Results with the grades the paper gives

(Statement / grade / where. The Section 11 table is the paper's own summary; body grades agree unless noted.)

1. Zero and span free; a ratio needs a physical zero. [T] (A.1)
2. Census logarithm with A = 2c/pi^2 "given equal spacing and Calabrese-Cardy". [T], [V] at c = 1, 1/2. The derivation is "asymptotic... exact given those two inputs".
3. Prop 2.1: Gamma = tanh(eps/2) = 1 - 2 nu; int H d eps = pi^2/3. [T][L]. He notes the identity 1 - 2 nu = tanh(eps/2) is standard in entanglement-spectrum work; "the reading is the author's".
4. Thm 2.2 Cayley domain with explicit branch; pole only at z = -1. [T][L]
5. Offset = summed rapidity = log-odds empty/full (quasi-free). [T] (A.4; The Offset Belongs to the Boundary v31, Thm 2)
6. Thm 2.3 The weight between: defect split, 0 <= X <= F <= 1/4, two-sided, census comparison, trace estimate, local unitaries. [T][L](core). Item-level: (1) [T][L], (2) [T][L], (3) [T], (4) [T], (5) [T][L], (6) [T].
7. Gamma_b = sqrt(1 - 4 lambda); = |1 - 2 nu| on a pure state. [T][L]
8. "One block, many jobs" (same off-diagonal block functional across papers). [T][S]
9. Thm 2.4 operator-norm stability with certified margin; Thm 2.5 near-projector comparison; Prop 2.6 Holder coordinate. [T], [V]
10. Prop 2.7 same local block, different weight between; three census counterexamples (disconnected thermal state; classical correlation invisible to C; entanglement invisible to C). [T]
11. Prop 2.8 number covariance; Thm 2.9 4 Tr X_A <= I_G <= Tr X_A/(delta(1-delta)); census bound. [T], [V]
12. Thm 2.10 offset speed limit tau_dot^2 <= 4 g S. [T] (A.7; The Offset Speed Limit Thm 1 and Cor. 3)
13. Prop 2.11 equal census, offset and coupling; opposite offsets, both saturating. [T][V]
14. Warm ring: boundary count 2 -> 0 with Tr X_A = 0.170835 > 0. [V]
15. Thm 3.1 peel steps add like velocities (VOTKP Thm 15.1) [T][L]; hyperbolic lengths add (VOTKP Cor. 15.2) [T]; Ising census ladder = constant peel step [V].
16. Gap step reflects with the peel coordinate, eqs (5),(6). [T][V]; black-hole-paper sharp-step and polar-mirror checks [V][S].
17. Prop 4.1 Schur-Cayley boundary: passive inside, matched load at centre. [T]; horizon = centre of chart [S] ("sourced; ed. 10 section 5.2").
18. Prop 4.2 Hawking fermion record tau = hbar omega/k_B T_H, Gamma = tanh(hbar omega/2 k_B T_H). [T][V]; the reading (fixes only omega/T_H, phase never enters) [H][S].
19. Thm 5.1 anchored coordinate equivalence [T][L]; helium Gamma_0 = 0.377575 [lit][V].
20. Scale blindness (VOTKP Thm 15.4) [T] (A.9); last peel step 5/(8Z - 5), Z >= 2 [T][L] (A.10); Thomas-Fermi middle [lit].
21. Lemma 6.1 [T]; Thm 6.2 unique neutral Saha state [T][L](three charges); Thm 6.3 responses [T]; Thm 6.4 scaling and atomic record insufficiency [T]; numerical illustration [V].
22. Thm 6.5 gas carries the peel back [T][L](cancellation); helium read-back [R] ("a model identity and a code check, not an independent measurement of atomic thresholds"); Thm 6.6 partition correction and conditioning [T], synthetic-partition check [V].
23. Unbound nuclei outside; rim distance 2s/(S_next - s); half turn. [T][L], [V][lit]
24. Thm 8.1 reduced equation with hidden source; channel measure. [T]
25. Prop 8.2 equal spectrum and footprint, different survival [T][V]; Prop 8.3 same kernel, different source [T].
26. Thm 8.4 finite moments do not fix response; readout dependence. [T][L](m = 3 witness), [V]
27. Thm 8.5 kinetic witness: same density, flow, stress; Delta n proportional to sin^3; reset factor. [T]
28. ANG1 to ANG3 exact; ANG4 E_- = k^2 kappa^2/3. [T], [V]. "The exact E_-, the growth of E_+ and the numerical convergence trend of the departure are three different statuses; an infinite-dimensional limit of the departure is not claimed."
29. Thm 9.1 opened idempotent: Y_A = A - A^2, radial census survives, positivity does not. [T][L]
30. Thm 9.2 det Q = -u^2 w^2 cos^2 k/16 s^3: Lorentzian iff s > 0, cos k != 0 (and uw != 0); negative definite if s < 0; degenerate on u = 0, w = 0 or cos k = 0; singular (not zero) at s = 0. [T][V]
31. Negative fitted Renyi-2 coefficient is a property of the biorthogonal entropy convention, "not a negative number of channels: a nonnegative census with N(xi) = a log xi + O(1) cannot have a < 0". [T]; the fitted values [V].
32. Prop 9.3 Petermann factor; <K> = 1 + u^2/E(0)E(pi). [T][L]
33. Continued endpoint offset 2i arctan gamma; Gamma_end = i on the rim at <K> = 2. [T] (body: [T][V]). A.15: "The continuation of the closed form to the opened chain is a definition."
34. Opened matter exits before critical at E(0)E(pi) = u^2 (PT class, whole cells, filters to 1e-9). [V]; "why it does is open [C]".
35. Massive-band exit: law fails with a mass term [V]; w = 0, v^2 = 2u^2 counterexample (<K> = 2 exactly yet no block level leaves {0,1}) [T].
36. Whether a biorthogonal form of tau_dot^2 <= 4gS governs the rotation: open [C].
37. Two kinds of wall; opened matter's exit is spectral [S]; ringdown numbers [V][S].
38. Prop 10.1 complement parity: census even, offset odd; metric even, curvature odd. [T][V]
39. "What survives a wall is the even half." [H]; black-hole orientation sign case [S].

Lean coverage (Appendix B)
- VOTKP.MatterDisk (repo dicipler-pixel/votkp-lean, Lean 4 with Mathlib v4.34.1): twelve theorems: bridge, census_square, census_complement, rapidities_add, topleft_sq, idempotent_cross, exit_line, outside_rim, rim_distance, cayley_pole, saha_ratio, last_step. Build record: GitHub Actions run 41729732315 at commit 0e5792a; 152 theorems across the repository; axiom audit finds only propext, Classical.choice, Quot.sound. False controls in FalseControls/, run separately.
- MatterGas (formal suite of the 3 November development): 34 positive declarations under Lean 4.34.1 and Mathlib commit d13f23b723b8a846827a245b89c10fc7d3f11612; no sorry, admit, custom axiom or native_decide; five false controls rejected. Modules: Scalar, Boundary, Saha, Witness. Witness uses weights (7,11,5,9)/32, "a different amplitude of the same construction as the text's (3,7,1,5)/16" (third-moment separation 3/2).
- NOT machine-checked (stated): ordered spectral comparisons, stability, the information bounds, general-Z Saha, the response laws, the kinetic witness and the Petermann statements ("proved by hand in this paper").

Appendix A "does not prove": the [V] numerical statements; the two inputs of A.2; the Saha equation; the 1/Z coefficients and Thomas-Fermi law cited in VOTKP; the IQGT relation g_par Delta^2 = 9; the membrane resistivity of the horizon; NUBASE2020 and NIST data. These are "outside inputs".

---------------------------------------------------------------------

## 5. Numbers (value, units, source)

Census coefficient
- 2/pi^2 = 0.202642 (dimensionless); measured at c = 1: 0.202692. [V] (Matter at a Scale)
- c = 1/2 transverse-field Ising chain: two correction families for the interval entropy coefficient give 0.1693 and 0.1586 (bracket 1/6); census coefficient 0.103689, 2.3% above 1/pi^2 and 41.8 times closer to it than to the c = 1 value. [V] (Matter at a Scale, ISING-A-03 and ROBUST-01)
- Bridge check: 1.1e-16 and 6.7e-15 (script s01; integral 3.2898681336964595 vs pi^2/3).

Offset / census example
- diag(0.2, 0.8) and diag(0.2, 0.2): same defect C - C^2 = 0.16 I; offsets 0 and log 16.

Information bound (script g_gaussian_information_checks)
- 64 random covariances; minimum margins 9.1e-6 (lower), 5.9e-5 (upper); ratio I_G/Tr X_A -> 4.000000020 on the sharp family; pure states p -> 0: upper ratio 11.3, 20.4, (29.6 in output) without bound. Natural-log units.
- s09 independent: min of I_G - 4 Tr X_A over 200 cases = 2.025e-3.

Speed limit example (script s13 K1)
- saturation error 1.4e-13 over three frequencies (0.3, 1, 2), both signs, 31 times; |tau_dot| = 4, 8 > 2 at omega = 1, 2 (at omega = 0.3: 1.2 < 2).

Warm ring (script s07; N = 128 sites, antiperiodic, mu = 0, half-ring region 64, eps = 0.1; T in hopping units)
- Uniform ring: T = 0: raw 2, boundary 2, Tr X_A 0.605657, MI 3.923714. T = 0.5: raw 24, boundary 0, Tr X_A 0.170835, MI 0.949562 (innermost |Gamma| 0.047, innermost |Gamma_b| 0.817). T = 2: raw 64, boundary 0, Tr X_A 0.027779, MI 0.116547.
- Gapped alternating (hoppings 1.5, 0.5): T = 0: raw 0, boundary 0, Tr X 0.029017, MI 0.345837; T = 0.5: raw 10, boundary 0, 0.024935, 0.188891; T = 2: raw 64, boundary 0, 0.006484, 0.028357.
- Disconnected sites C = 0.3 I (region 32): raw 32, boundary 0.
- All rows MATCH a "3 Nov review" table.

Ising peel ladder (script s02)
- xi = 20.5, 50.5, 125.5: eps_0 = 1.9346, 1.6440, 1.4275; peel step tanh(eps_0) = 0.95910, 0.92803, 0.89115; residuals 8.0e-6, 5.5e-6, 3.2e-6; uniformity error 0.022, 0.011, 0.0062.

Reflection chart
- Gap-step matching: 200 random steps, 3.3e-16 (s13 K5). Black-hole paper's sharp-step matching: 1.7e-11 on 400 random steps, 89 beyond the turning point. Its preregistered Richardson gate for smooth steps FAILED (residual 7.4e-4 against 1e-5). Polar stratum |r| = 1 to 2e-16.
- Horizon: surface resistivity 4 pi in Gaussian units = impedance of empty space mu_0 c = 376.73 ohm; normalised Z_b = 1, S_b = 0. [S]
- Hawking record check: six frequencies, seven phases, 5e-16. Fig 3 points: hbar omega/k_B T_H = 0.25, 0.5, 1, 2, 4, 8 -> Gamma = 0.124353, 0.244919, 0.462117, 0.761594, 0.964028, 0.999329. Gap ratios Delta_2/Delta_1 = 1/8, 1/4, 1/2, 3/4 -> Gamma = -0.777778, -0.6, -0.333333, -0.142857.
- Fig 3 right, four readings: occupation nu = 0.2 -> eps = 1.386294, Gamma = 0.6; Hawking eps = 1 -> 0.462117; helium eps = ln(I_1/I_0) = 0.794457 -> 0.377575; gap step ratio 2 -> eps = 0.693147, Gamma = 0.333333.

Atom
- Helium thresholds 24.587389011 eV and 54.4177655282 eV (from VOTKP v2.9 / NIST): Gamma_0 = 0.37757506698375; binding sum 79.0051545392 eV; D = I_1 - I_0 = 29.830376517 eV. [lit][V]
- Sodium: eleven thresholds (NIST ASD, eV, in fig03v4 script): 5.139076, 47.28636, 71.6200, 98.936, 138.39, 172.18, 208.50, 264.18, 299.856, 1465.091, 1648.659; composite peel walk tanh((1/2) ln I_k/I_1) ends at Gamma = 0.9938 (0.9937851227733561). "Shell jumps are the long strides."

Gas (ideal Saha, helium, ground partitions U = (1,2,1))
- Nucleus density 1e22 m^-3: neutral fraction 0.999374, 0.289781, 8.73350e-6 at 1e4, 2e4, 5e4 K; Gamma_0 stays 0.377575. Script s08 percentages: 10 kK: He 99.937400, He+ 0.062600, He2+ 0.000000; 20 kK: 28.978059, 71.021940, 0.000001; 50 kK: 0.000873, 17.146019, 82.853108. Population disk points Gamma_pop = tanh((1/2) ln n_q/n_{q+1}): (+0.9987, +1.0000), (-0.4204, +1.0000), (-0.9999, -0.6571).
- 20 kK density sweep: neutral 0.5680% at 1e20 m^-3, 87.6482% at 1e24 m^-3.
- Read-back at 30,000 K and 32,000 K across 1e18 to 1e26 m^-3: Gamma_0 = 0.37757506698375 to 2e-16 (worst 2.2e-16); D = 29.830376517 eV, B = 79.005154539 eV; neutral fraction at 30 kK: 0.00001%, 0.00267%, 0.26765%, 18.06496%, 82.49125%. [R]
- Synthetic partition U_1(T) = 2 + 4 e^{-10 eV/k_B T} ("not a claimed helium level scheme"): ignoring it returns Gamma_0 = 0.36614943350748, bias -0.0114256 (naive D = 28.927692578698508 eV); correction restores 0.37757506698375 to 1.4e-14. [V] (g01_verify_formal_gas, "specified before its run")
- Constants used in s08: h = 6.62607015e-34, k_B = 1.380649e-23, m_e = 9.1093837015e-31, eV = 1.602176634e-19.

Nucleus (NUBASE2020 via pynucastro; author's script s10; mass excesses n = 8071.31806 keV, 1H = 7288.97061 keV)

| case | S_first (keV) | S_next (keV) | Gamma | |Gamma| | half-life |
|---|---|---|---|---|---|
| 5He: n, then n from 4He | -734.8 | 20577.6 | +1.074062 | 1.074 | 602 ys |
| 5Li: p, then p from 4He | -1966.1 | 19813.9 | +1.220318 | 1.220 | 370 ys |
| 8Be: alpha (12C ladder) | -91.8 | 7366.6 | +1.025238 | 1.025 | 81.9 as |
| 7Li (bound) | 7251.1 | 5664.4 | -0.122852 | 0.123 | stable |
| 4He (bound) | 20577.6 | 5493.5 | -0.578576 | 0.579 | stable |

- 7Li row: remove n, then n from 6Li. 4He row: remove n, then p from 3He. 8Be row: alpha chain 12C -> 8Be -> 2 alpha, S_first the alpha separation from 8Be, S_next that from 12C.
- Rim distances exact: 0.074062, 0.220318, 0.025238; small-s values 2s/S_next: 0.071417, 0.198457, 0.024923 (s12).
- Half-turn check: 4000 random complex z, zero mismatches; z = -28 gives Gamma = 1.0741 (the 5He value) (s04a).

Records and responses
- Survival 0 vs 1/32 at t = pi/4 (numerically 1.2e-32 and 0.03125); footprint B B^T = 5; third moments 0 and 3 (reflected weights (5,1,7,3)/16: -3).
- Moment witness exact rational checks at orders 1 through 12: residuals at most 3.3e-16.
- Kinetic instance: a = 1/24, eta = 1/2, rho_* = v_0 = k = 1, sigma = 0, x = t = pi/2: n_+ = 5/6, n_- = 7/6, Delta n = -1/3.
- ANG1: Z_b(1e-2, 1e-4, 1e-6) = 0.63070, 0.636560, 0.6366192 against 2/pi = 0.6366198.
- ANG2: pole-condition residuals at kappa = 0.64, 0.7, 0.916, 1, 2 below 2e-16; poles s* = -0.6317, -0.5568, -0.3965, -0.3579, -0.1695 (k = 1).
- ANG3: coefficients for l = 3, 4, 5, 8: 0.507092553, 0.127775313, 0.0214031702, 2.2474e-5; lower powers vanish to 1e-15.
- ANG4 at k = kappa = 1: N = 2, 5, 20, 100, 200, 400: E_- = 1/3 throughout; E_+ = 0.333, 3.444, 18.49, 98.50, 198.50, 398.50; ||L||_F^2 - sum|lambda|^2 = 1.0000, 1.0811, 1.1556, 1.1715, 1.173488, 1.174462. (kappa = 0.5: E_- = 1/12.)

Opened matter (w = 1 unless stated)
- Biorthogonal C idempotent to 3e-14; |C^2 - C| <= 2.8e-14; |X_A - C_A(1 - C_A)| <= 1.3e-14 (s07; ring 200 cells, block 40 cells; v = 0.3, 0.5 at u = 0.5).
- det Q: sympy residual identically 0; 2000 random biorthogonal evaluations agree to 4.1e-14 (s13).
- "The 93% of v3's scan is the grid fraction of the region s > 0 off the lines cos k = 0 at u = 0.5, here 0.9304 on a 400 x 400 grid: a property of the chosen window, not a constant." (s03c raw scan: 0.932; fig05 800 x 600 grid prints 0.9355.)
- Renyi-2 coefficient at the critical point: -1.79 -> -1.96 on the v < w side (N = 1000 -> 2000), -0.88 -> -1.09 on the v > w side (not converged); max |Im S_2| = 6.3 at v < w (s03b). Hermitian critical control: +1.007.
- Exit at u = 0.5: v_exit = 0.468 (measured 0.468213; <K> = 2 at v = 0.4682132; critical point at v = 0.5). Critical points at k = pi: v = w -+ u.
- s05a exit line: u = 0.2, 0.3, 0.4, 0.5, 0.6, 0.7 -> v_exit = 0.798752, 0.695189, 0.586649, 0.468213, 0.327358, 0.082016; rotation at critical = 1.00000 pi for every u (level at Im W = pi exactly).
- Petermann formula checked to 3.6e-14 (text); <K> - 1 = gamma^2 to 2.8e-14 over 20,000 random parameters.
- Predicted from <K> = 2 at u = 0.25, 0.45, 0.65: 0.7474014, 0.5291503, 0.2357262; measured 0.7474015, 0.5291503, 0.2357262; differences 4e-8 and below (block 40; block-independence from s04b).
- Second model (cone paper's band in 1D, d = (t_1 + cos k, sin k, m + i gamma)): <K> ~ 1.01 to 1.06 at returned exits. s06 output: (t1,m) = (0.5,0.4): exit gamma 0.1691699, <K> 1.022352 FAIL; (1.5,0.4): 0.1956728, 1.018838 FAIL; (0.5,0.0): 0.4743416, 2.000000 PASS; (1.5,0.8): 0.2518871, 1.015041 FAIL. Script verdict: "KILLED on the second model at the stated bar". Block-independence: exit gamma 0.169170 at blocks 40, 80, 160.
- Filter table (ring 2000, block 40, t_1 = 0.5, principal logarithm; massive m = 0.4):

| filter delta | massive gamma_exit | massive <K> | massless gamma_exit | massless <K> |
|---|---|---|---|---|
| 1e-6 | 0.271636929 | 1.057972846 | 0.474341649 | 2.000000002 |
| 1e-8 | 0.271636929 | 1.057972846 | 0.474341649 | 2.000000002 |
| 1e-9 | 0.169169932 | 1.022352491 | 0.474341649 | 2.000000002 |
| 1e-10 | 0.169169932 | 1.022352491 | 0.474341467 | 1.999995744 |
| 1e-12 | 0.122791366 | 1.011745220 | 0.474227956 | 1.997345192 |

  Eigenpair residuals at most 4.4e-15; eigenvector condition numbers 135 to 575. (Note: the separate script s09 prints slightly different 1e-12 values, 0.122721579 massive and 0.474123961 massless; the table follows g_incoming_exit_filter.)
- Quarter-turn test (s11; u = 0.3, 0.5, 0.7; v at 60%, 80%, 95% of the way to the exit; blocks 20 to 160): measured rotation sits 4e-6 to 3.4e-2 above Im tau_end, independent of block size. Script verdict: "KILLED at the stated bar"; the opposite (Hermitian-form guess 2 arctan(u/E(pi))/pi) "fails as required".
- Ringdown (Beyond the Event Horizon ed. 10, two-mode model): single excitation factors reach 391 with nearly opposite phases while their sum stays fixed.
- Parity check: 200 random projectors to 1.5e-14; minus-sign resolvent law fails on a random control (largest violation 18.9).

Merge audit (s14): v3 83/83, gpt 67/67, review 12/12, bh 9/9, new 6/6 items present; PASS.

---------------------------------------------------------------------

## 6. Limits, failures and open items (as stated in the paper)

Stated limits
- Scale: "The single failure is ultraviolet." A rescaling of the substrate "is registered only as a running, never as a power."
- A.2 derivation is exact only given (i) equally spaced single-particle entanglement spectrum and (ii) Calabrese-Cardy entropy; the level-counting convention must match the entropy convention.
- Offset as log-odds (eq. 2) only for number-conserving Gaussian (quasi-free) fermion states.
- Census: "a statement about the one-body record"; reads correlation faithfully only inside the quasi-free class. A census of zero "is not a certificate of no correlation". A finite census cannot diverge at fixed a, b.
- Mixed states: X_A need not commute with A_C; its eigenvalues cannot be paired level by level with nu(1-nu).
- Information bound holds for fermionic Gaussian states; "it does not transfer a bosonic theorem". No upper constant exists without a spectral margin.
- "A floating-point residual is not by itself an operator-norm error bound; a certified count needs a validated bound and a margin larger than it." Eigenvalue step does not transfer to non-normal matrices; a non-Hermitian residual "needs a conditioning or pseudospectral analysis before it becomes a certified disk count".
- Speed limit: the cross weight Tr X cannot stand in for E_H (they "differ by a factor that grows without bound"). "A frozen offset is a statement about this motion; it does not say the record holds no memory." The speed budget does not choose the future (direction).
- Reflection chart: the three boundary readings "are different normalised impedances on one chart; their relative positions are not a physical identification". The horizon match "belongs to the horizon surface, not to the hole seen from far away: the potential barrier outside reflects long-wavelength radiation". Fermion record needs 0 < C < I: "the bosonic pair has no full state".
- Atom: coordinate "changes conditioning and representation, never information"; it does not know a specimen's temperature, density, partition weights, matrix elements or preparation. Quantum-dot addition spectra have no peel (no physical zero).
- Gas: model is ideal, nonrelativistic, LTE, pure species; "mixtures, external electrons and non-LTE kinetics need other closures". With temperature-dependent partitions positivity of the T response needs an extra condition. Helium read-back "is a model identity and a code check, not an independent measurement". "Close temperatures amplify observational error; rare populations make the logarithms ill-conditioned. Real helium excited-state partitions, continuum lowering and non-LTE populations are separate validation tasks."
- Nucleus: "The placement says no more than the sign of a separation energy"; the author's own caution: a resonance's leak through its barrier "is not a literal atomic or nuclear Smith reflection derived from the threshold coordinate". If both separation energies are negative the ratio is positive and the point is inside.
- Records: kernel properties "do not turn a scalar delay curve into a reconstructed measure". The kinetic reset "is a prescribed preparation map, not the self-consistent collision operator of an isolated gas". ANG1 is "not an electromagnetic reflectance". ANG2 pole "is not the two-moment exceptional point of a truncated chain".
- Opened matter: variance and Gaussian readings of Section 2 need a positive metric and do not come from idempotence. Cone hypothesis must include a Hermitian tangent (h(theta) = sigma_z + i theta sigma_x gives Q = -1/4 at theta = 0). Exit law: the band-average equivalence is separate from the statement that a finite block census crosses the rim at the same parameter, "which carries its block, boundary conditions, filter, error and limit". "The average alone does not force an exit; the coupling and the partition are part of the law." "The massive exit is not yet a filter-independent threshold; the massless exit holds through 1e-9 and shifts below."
- The quarter-turn "is not... a description of the census rotation away from the exit"; "the two meet only at the quarter-turn". The real-argument expression 2 artanh gamma (diverges at gamma = 1) "belongs to a different chart and is not this continuation".
- Parity: the broad reading that what survives a wall's involution is the even part "is a reading of particular cases, each with its own J" [H].

Recorded failures / kills inside the paper
- Black-hole paper's preregistered Richardson gate for smooth steps failed (7.4e-4 against 1e-5).
- s06: exit law <K> = 2 KILLED on the second (massive) model; holds only at m = 0, the SSH class.
- s11: census rotation = continued offset form KILLED at the stated bar.
- Renyi fit on the v > w side has not converged.

Open list (Section 11, verbatim in substance)
1. Why the census rotation meets the offset quarter-turn only at the exit (needs conditioned eigenvalues for the near-endpoint levels).
2. A proof that the exit happens at <K> = 2 on the coupled chain.
3. A definition of the massive exit with a controlled limit in filter, ring and block size and the order of limits stated, using conditioning and error bounds rather than an assumed error expansion.
4. A biorthogonal speed limit for the complex offset.
5. Convergence on the v > w side.
6. The infinite-dimensional limit of the chain's Henrici departure.
7. Placing nuclear resonances with their widths on the chart.
8. A second non-unitary model of a different kind.
9. An empirical gas inverse on a real specimen with measured populations, n_e and partitions.
10. A typed map from the speed limit to the record of a physical system beyond the projector constructions here.

Sources he cites (own): Matter at a Scale v5 (doi 10.5281/zenodo.22019893); VOTKP: The Vector of Traits Kept under Peeling v2.9 (doi 10.5281/zenodo.23340757); The Offset Belongs to the Boundary v31 (doi 10.5281/zenodo.22555919); The Offset Speed Limit v1.1; The Weight Between v2.3; The Angle Between the Rails; A Measured Lorentzian Cone in Non-Hermitian Quantum Geometry v8; Beyond the Event Horizon: What Survives at a Rigidity Wall, edition 10; Intrinsic Quantum Geometric Tensor on the Grassmannian and Spectral Lower Bounds on Dissipation (doi 10.5281/zenodo.20768258); Light Keeps the Ledger research edition 7.2; Matter, Gases and VOTKP: Formal Research Edition 3 Nov 2026 (repository matter-disk/external/gpt_formal_20261103); Physics Atlas v7 (B1 to B207) and Atlas II (W1 to W9) (atlas cards cited in text: W9, B202, B204).
Outside: Calabrese and Cardy 2004; Peschel 2003; Peschel and Eisler 2009; Wolf, Verstraete, Hastings, Cirac 2008; Chang, You, Wen, Ryu 2020; Unsold 1927; Thorne, Price, Macdonald (Membrane Paradigm) 1986; Kondev et al. NUBASE2020; Kramida et al. NIST ASD.

Scripts with a kill condition written before the run: s06, s07, s08, s11, s12, s13 (and s14 merge check). Others are observational scans or figure builders.

---------------------------------------------------------------------

## 7. What bears on the four team topics

Search of the full text: the words "ball", "tree", "Sun", "solar", "planet", "magnetic field" do not occur anywhere in this paper ("magnet" appears only inside "electromagnetic reflectance", and "star" only as figure markers). So anything below is what the paper offers that could be carried to those topics; the paper itself makes none of those applications.

### 7a. The ball/tree picture and its scales from matter downward
- NOT IN THIS PAPER as a ball or a tree. What it has instead is ONE DISK and ONE COORDINATE carried down a list of scales. The scale ladder, in his order, with what is the ratio z at each:
  1. Bulk matter at a cut: z = (1 - nu)/nu, occupation odds of a level of the one-body correlation matrix C (census ladder; Ising levels on both signs of the real diameter).
  2. Warm matter: same, but split into raw (local occupation) and boundary (X_A) coordinates; heat pulls raw levels toward the centre, the boundary coordinate sends them back to the rim.
  3. Atom: z_q = I_{q+1}/I_q, successive removal thresholds measured from the continuum; all on the positive real radius; sodium walks from the centre to 0.9938; helium Gamma_0 = 0.377575.
  4. Gas: population pairs n_q/n_{q+1} are disk points Gamma_pop that sweep the whole disk with T and density while Gamma_0 read back from the gas stays put. Half ionization is the centre (s08 comment).
  5. Nucleus: z = S_next/S_first, separation energies; bound nuclei on the negative half (7Li -0.123, 4He -0.579), unbound mass-5 and mass-8 gaps outside the rim past +1.
  6. Opened (non-Hermitian) matter: complex odds, complex Gamma, off the real diameter; exits the disk before the critical point.
  Figure 2 caption: "One chart, every scale, signed."
- The closest thing to a tree/branching structure is the peel ladder itself: a walk along one geodesic diameter with steps that compose by (+), where "the composite forgets the order of its steps; the resolved ladder keeps it".
- Scale statement that governs any multi-scale picture: only ratios are observable; a common scale leaves every Gamma unchanged (Thm 5.1, scale blindness A.9); the missing absolute anchor is physically consequential (Thm 6.4: the anchored record still does not fix a gas population).

### 7b. Steps r = ln z and walls
- His symbol is eps (rapidity), eps = ln z, not r. Gamma = tanh(eps/2). Summed over levels it is the offset tau.
- Steps: Gamma_k = tanh((1/2) ln(I_{k+1}/I_k)); half-rapidities add; steps compose as u (+) v = (u+v)/(1+uv). Hyperbolic length of a step on the Poincare-disk reading is 2 artanh|Gamma| = |ln z|, i.e. the step length IS |ln z|, and lengths add along the diameter (VOTKP Cor. 15.2). A constant peel step exists on the Ising census ladder: Gamma_{j+1} = Gamma_j (+) tanh(eps_0), levels at odd multiples eps_0, 3 eps_0, 5 eps_0.
- Near the rim the disk compresses differences, "so the informative number is the uniformity error in rapidity".
- Complex steps: z = e^W. Rim = quarter turn |Im W| = pi/2; negative real ratio = half turn Im W = pi (unbound nuclei, and one level at every critical point of the opened chain tested, u = 0.2 to 0.7). Cayley pole z = -1 only.
- Walls (Section 9.4, from Beyond the Event Horizon ed. 10 section 8): spectral wall vs geometric wall, definitions in Section 2 of these notes. Opened matter's exit is spectral. "What grows is the non-orthogonality of single levels, and what crosses the rim is the record of the pair." At such a point a single eigenprojector grows like |A_12|/gap while the pair projector, its contour trace (count 2) and the trace-log ledger stay exact.
- Wall-like features on the reflection chart: |Gamma| = 1 exactly beyond the geodesic turning point a_2 = C (total reflection); a polar stratum is a perfect mirror; the rim is total reflection.
- Section 10: odd parts "need not vanish merely because a surface is called a wall"; the reading "what survives a wall is the even half" is graded [H] only.
- Exit line as a wall-crossing criterion on the PT chain: E(0)E(pi) = u^2, equivalently <K> = 2, equivalently Im tau_end = pi/2, Gamma_end = i.

### 7c. Placing several equal balls on a hyperbolic field so light/energy passes from one to the next
- NOT IN THIS PAPER. No construction of several bodies, no tiling, no field of balls, no transfer of light between bodies.
- Pieces in the paper that a builder of that picture could lawfully draw on (each with the paper's own caveat):
  - The one explicit hyperbolic statement: "On the Smith disk read as the Poincare disk the peel is a walk along a geodesic diameter whose hyperbolic lengths, 2 artanh|Gamma|, add" [T]. Only a diameter walk is treated; no off-diameter geodesics, no two-dimensional hyperbolic placement.
  - Passage/reflection between two regions: gap-step reflection Gamma = (Delta_2 - Delta_1)/(Delta_2 + Delta_1) = tanh((1/2) ln Delta_2/Delta_1) (eq. 6). Equal gaps (Delta_2 = Delta_1) give Gamma = 0: nothing reflected, the matched case. So "equal" neighbours sit at the centre of the chart with respect to each other. With oblique incidence (eq. 5) the Clairaut constant C = a sin^2 theta is conserved and total reflection sets in beyond the turning point a_2 = C.
  - Matched load: Z_b = I gives S_b = 0, "the load that returns nothing"; passive boundary gives ||S_b|| <= 1 with no normality assumed (Prop 4.1).
  - Coupling between two parts: the weight between X_A = C_AB C_BA; two-sided (X_A and X_B share positive eigenvalues, Tr X_A = Tr X_B <= (1/4) min(a,b)); Cov(N_A,N_B) = -Tr X_A; 4 Tr X_A <= I_G(A:B). Disconnected parts: X_A = 0, every boundary coordinate at the rim (Gamma_b = 1).
  - Rate of passage: tau_dot^2 <= 4 g S; with P_dot = -i[H,P], |tau_dot| <= 2 sqrt(E_H S), E_H = ||P H (1-P)||_F^2; "no weight between in the generator, no motion of the record".
  - What is handed on is not fixed by the present record: equal census, offset, coupling can move in opposite directions (Prop 2.11); the memory kernel K(t) = B e^{-iDt} B^dag and hidden source J(t) (Thm 8.1).
  - Free streaming chain: load presented to density Z_b -> 2k/pi; a planted moment l reaches stress at order l - 2 and density at order l (ANG3), i.e. a stated delay law for something passing down a chain.
- Caveat to keep: the three chart readings "are different normalised impedances on one chart; their relative positions are not a physical identification".

### 7d. The Sun, planets, real body shapes and magnetic fields
- NOT IN THIS PAPER. No Sun, no planets, no body shapes, no magnetic fields, no gravity calculation.
- Nearest relevant content:
  - Hot gas (relevant to any stellar-matter use): the ideal Saha section. Helium neutral fractions at 1e22 m^-3 and 1e4 to 5e4 K; the gas populations sweep the disk while the atomic peel Gamma_0 survives; the gas needs four inputs beyond the peel: the absolute thermal ratio I_0/k_B T, the density relative to lambda_e^3, internal partition ratios, and a justified equilibrium. Stated not covered: mixtures, external electrons, non-LTE, continuum lowering, real excited-state partitions.
  - Nuclei 4He, 5He, 5Li, 8Be, 7Li, and the 12C -> 8Be -> 2 alpha ladder appear only as separation-energy peels (table in Section 5 of these notes); no reaction rates, no stellar context.
  - Astrophysical object mentioned: only a black-hole horizon, as a structural comparison [S]: stretched horizon surface resistivity 4 pi (Gaussian) = 376.73 ohm, matched load at the chart centre; Hawking fermion record at Gamma = tanh(hbar omega/2 k_B T_H).
  - Shape/geometry content is limited to the pullback metric g = a(y)dx^2 + b(y)dy^2 on a projector family (his intrinsic metric on the IQGT family, not a spacetime or body-surface metric) and the Lorentzian signature of the opened band metric on the (k, v) plane.
  - "Electromagnetic" appears once, in a disclaimer: ANG1's load is "not an electromagnetic reflectance".

---------------------------------------------------------------------

## 8. Small things a follow-up might ask

- Figures (captions only): Fig 1 warm census (left) and helium gas on the disk (right); Fig 2 one chart, every scale, signed; Fig 3 one disk, three boundary readings + the single curve Gamma = tanh(eps/2) with four readings; Fig 4 equal present records, different futures; Fig 5 angular gas chain (k = 1); Fig 6 opened plane's signature (u = 0.5, w = 1); Fig 7 <K> and continued endpoint phase along v, and exit vs filter. (File names in scripts: fig02_boundary_and_gas, fig03v4_one_chart, fig04_reflection_chart, fig05_metric_signature, fig06_records_and_futures, fig07_exit_and_filter, fig08_angular_chain; file numbering is offset from the printed figure numbers.)
- Fig 2 colour key: blue Ising census ladder; gold sodium peel walk and helium Gamma_0; purple nuclear peels; green and red census levels of the opened non-Hermitian SSH chain (u = 0.5) before (v = 0.30) and past (v = 0.49) its exit.
- Matched-boundary example referenced: C_+- = (1/2)I +- r sigma_y ("B12 of the formal development; here at r = 1/2").
- Internal labels from the formal edition that appear in scripts: B1 to B13 (boundary), D1 to D7 (disk), G1 to G9 (gas), R1 to R4 (reduced/records), M1, M2 (moments), K1 to K4 (kinetic), P1 to P3 (Petermann), ANG1 to ANG4.
- s04a (unwindowed, no endpoint filter) shows rotation ~1.0 pi at every v (near-endpoint levels dominate); s04b (windowed, filter 1e-9) gives the meaningful rotation: at u = 0.5, v = 0.45 rotation 0.4703 pi, in; v = 0.47 rotation 0.5036 pi, max|Gamma| 1.0115, OUT; v = 0.5 rotation 1.0000 pi. On the v > w side: v = 1.52 in, v = 1.51 out (max|Gamma| 1.0009), critical at 1.5. Inside the PT-broken zone (0.5 < v < 1.5) unwindowed max|Gamma| = 1.0000 "in".
- s03a: NH critical |v - w| = u (EP): max|Gamma| = 3.057, max|Im Gamma| = 3.06, c = 3*slope = +1.321, Im S ~ 0.26; NH gapped (v = 0.5, u = 0.3): max|Im Gamma| = 0.42, |Gamma| max 1.000.
