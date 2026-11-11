# Read record 02 — The Dirac Time of the Gigantefermion, long form v3.1 (6 Nov 2026), constructions with formulas

Source read in full: the .md inside Dirac_Time_Gigantefermion_v3_1_Research_Package_20261106.zip (188k characters of text once the embedded figures are removed).
Section and theorem numbers are the paper's own. Tags [T] [C] [H] [OP] are the paper's.

## 1-3. Memory, predictive quotient, record maps
- N_inf = {v : R L^n v = 0 for all n >= 0}; V_pred = V / N_inf; L descends because L N_inf is inside N_inf. [T]
- Finite closure: N_inf = ker O_d, O_d(v) = (Rv, RLv, ..., RL^{d-1}v); dim V_pred = rank O_d; any sufficient summary F has rank F >= dim V_pred. [T]
- The present observation closes iff L(ker R) inside ker R, iff RL = AR for some A. [T]
- Definition 1.1: memory = information absent from the present reduced description but required to distinguish future admitted observations. invariant != history != memory != arrow.
- 3.1: memory hierarchy = nested kernels of declared record maps R_0 -> R_1 -> ... -> R_m.

## 5. Chiral negative control
- Flat torus: D_{alpha,beta} = sigma1(-i d_x + 2 pi alpha) + sigma2(-i d_y + 2 pi beta); block D_mn = 2 pi[(m+alpha) sigma1 + (n+beta) sigma2]; lambda = +-2 pi sqrt((m+alpha)^2 + (n+beta)^2).
- Gamma = sigma3, Gamma D Gamma = -D, so SF(D) = 0.
- 5.1: a = m+alpha, b = n+beta, phi = arg(a + ib); P_+ = (1/2)(I + cos phi sigma1 + sin phi sigma2); Tr(P_+ sigma1) = cos phi, Tr(P_+ sigma2) = sin phi; d phi = (a db - b da)/(a^2 + b^2).
- 5.2: loop (alpha,beta) = r(cos s, sin s): eigenvalues fixed at +-2 pi r, u_+ = (1, e^{is})/sqrt2, i<u,du> = -(1/2) ds, holonomy -1. Equatorial case of the monopole: a_N = (1 - cos theta)/2, loop integral = pi, a_N - a_S = 1.
- 5.3 ONE LAW [T]: if Gamma D(s) Gamma = -D(s): (1) spectrum even; (2) every odd scalar-spectral record (SF, eta, odd traces) vanishes; (3) Gamma P_+ Gamma = P_-, and Tr(P_+ A) = -Tr(P_- A) for Gamma-odd A, unconstrained by the spectrum. The orientation lives only at projector level.

## 6. IQGT inside Dirac Time
- Same Q, g, Omega as IQGT (record 01). 6.2: <n|d_i Pi|m> = <n|d_i Sigma|m>/(lambda_m - lambda_n); the gap enters only as the denominator of a COUPLED pair: "the empty spacing between levels is part of the structure" [T].

## 7. Phase and conditional measurement
- Wilson W(C) = exp(iq loop-integral A). ABL rule P(k|i,f). Weak value A_w = <f|A|i>/<f|i>, with p_0 |A_w|^2 <= <i|A^2|i>. Weak values are instruments, not the writing mechanism.

## 8. Spectral history ledgers
- 8.1 [T]: SF(gamma: x -> y) = n(y) - n(x) for an endpoint function n iff every admitted closed loop has zero SF.
- 8.2 circle odometer: D_a = -i d/dx + a, lambda_k = k + a; SF(a0 -> a1) = floor(a1) - floor(a0); eta(D_a) = 1 - 2{a}; SF = (a1 - a0) + (1/2)(eta_1 - eta_0).
- 8.3 APS: ind = bulk integral - xi(A), xi = (eta + dim ker)/2. 8.4: SF = Maslov(ker Q, Cauchy data).

## 9. One flow, many readouts
- 9.1 [T]: B theta = delta, rank B = n-1 gives theta(s) = theta_0 + v tau(s), v in ker B.
- 9.2 AFFINE PHASE READOUT [T]: x = A + Bs, y = C + Ds, phi = arg(x + iy): phi' = (AD - BC)/(x^2 + y^2). AD - BC = 0 means the readout is SILENT; silence does not mean the progression stopped.
- 9.3 common clock [T]: R^dag H R - i hbar R^dag R-dot = tau-dot H_0 + a(t) I, with tau-dot > 0.
- 9.4: H -> sH keeps projectors, scales gaps: geometry of change != seconds. H -> H + cI changes neither. Offset speed limit: tau_off = log det(I-C) - log det C, C = E^dag P E; tau_off-dot^2 <= 4 g S, g = (1/2)||P-dot||^2, S = Tr[(C(I-C))^{-1}]; for P-dot = -i[H,P], g = ||PH(I-P)||^2.

## 10. Hidden-sector memory
- H = [[A,B],[B^dag,D]]: x-dot = -iAx - iB e^{-iDt} y(0) - integral K(t-s) x(s) ds, K(t) = B e^{-iDt} B^dag. Two carriers: initial hidden source and kernel.
- 10.1: K(0) = B B^dag = PH(I-P)HP = PH^2P - (PHP)^2. Same B, different D: same K(0), different K(t).
- 10.2: B B^dag = sum M_e; Sigma(z) = sum_e M_e/(z - e). The aggregate M does not determine {(e, M_e)}.
- 10.3: J_mu = bI + mu N_0: Tr f(J_mu) = 2 f(b) for all mu, but ||e^{-J t}|| depends on mu.
- 10.4: amplitude kernel (direct sum) is NOT the density kernel (tensor product, partial trace).
- 10.5 neutrinos: L = A + D, A = -ik mu, D = -kappa(I - P); c_l = (l+1)/sqrt((2l+1)(2l+3)); E_B = ||PH(I-P)||^2 = k^2/3; kept population A-dot^2 <= 4 E_B A(1-A); offset ln[(1-G)/G] moves along the rapidity (1/2) ln r, r = kappa2/kappa1, Smith coordinate (r-1)/(r+1).

## 11. Light and path inheritance
- 11.3 quotes VOTKP 5.6, 5.9, 5.10 (beta_min L <= D <= beta_max L, ker D = ker L).
- 11.4 EQUAL-ENDPOINT WITNESS [C]: |Psi> = (|01> + e^{i Phi}|10>)/sqrt2; both marginals I/2 for every Phi; after exchange V = g(|01><10| + h.c.): <Z_P>(t) = sin(2gt) sin Phi. Probe reads sin Phi only; a second probe with local phase e^{-i pi n_E/2} reads cos Phi. The history quotient depends on the probe.

## 12. Thermodynamics
- 12.1 memory engine [C]: p_* = (1-eta)p_h + eta p_m; p_m' = (1-eta)p_m + eta p_h; W_out = (eps_h - eps_c)(p_* - p_c); W_n^(a) - W_n^(b) = (eps_h - eps_c) eta (1-eta)^n [p_m,a - p_m,b].
- 12.6 friction [T]: zeta_mn = 2 c_mn (p_m - p_n)(E_n - E_m) g_mn, c_mn = tau/(1 + k^2 tau^2 (E_m - E_n)^2); two levels zeta_rot = 2c(Delta) Delta tanh(beta Delta/2) g_ss; two-level split zeta = tau beta sech^2(beta Delta/2) r-dot^2 + 2c Delta tanh(beta Delta/2) g_ss; beta W_ex = Sigma + D(rho_f || omega_f); tau_off-dot^2 <= 4 S zeta / w_min.

## 13. Knot exteriors
- 13.1 trefoil: L = -M^{-6}; M = e^{2 pi i alpha}, L = e^{2 pi i beta}: beta = 1/2 - 6 alpha; 6 d theta_M + d theta_L = 0; silence iff 6 eps_mu + eps_lam + 1/2 in Z.
- 13.2 8_19 = T(3,4): G = <X,Y | X^3 = Y^4>, mu = X Y^{-1}, lam = X^3 mu^{-12}; arcs (1,1), (1,3), (2,2) with L = -M^{-12}, -M^{-12}, +M^{-12}; at alpha = 1/4 two branches share M = i, L = -1 but Tr Y = +-sqrt2 (same boundary, different interior).
- THEOREM 13.1 family gearing [T]: G_{p,q} = <x,y | x^p = y^q>, uq + vp = 1, mu = x^u y^v, lam = x^p mu^{-pq}. X has eigenvalues e^{+-i pi a/p}, Y has e^{+-i pi b/q}, 0<a<p, 0<b<q, a = b mod 2; (p-1)(q-1)/2 arcs. On arc (a,b):
  1. L = (-1)^a M^{-pq};
  2. arc covers alpha strictly between alpha_+- = || (1/2)(ua/p +- vb/q) || (distance to nearest integer);
  3. at both ends omega = M^2 = e^{4 pi i alpha_+-} is a root of Delta_{T(p,q)}(t) = (t^{pq}-1)(t-1)/((t^p-1)(t^q-1)); END STEP k = uaq +- vbp, with k = a mod p and k = +-b mod q;
  4. lift beta = a/2 - pq alpha; sector (m,n) has constant phase numerator -[pq(m+eps_mu) + n + eps_lam + a/2]; silence iff pq eps_mu + eps_lam + a/2 in Z.
  Proof of 2 uses (1/2)Tr mu = cos phi1 cos phi2 - sin phi1 sin phi2 cos(vartheta), phi1 = pi ua/p, phi2 = pi vb/q, vartheta the angle between the axes.
- Two-strand: t^{-m} Delta_{T(2,2m+1)}(t) = P_m(x), x = t + 1/t, P_0 = 1, P_1 = x-1, P_{m+1} = x P_m - P_{m-1}. 7_1: P_3 = x^3 - x^2 - 2x + 1.
- THEOREM 13.2 arc = eta window [T]: N(alpha) = (1/2)|rho(S_K, chi_{e^{4 pi i alpha}})| = (1/2)|sigma_K(e^{4 pi i alpha})|; every wall ends exactly one arc. With x = 2 alpha, Theta = {i/p + j/q}, B = {theta - 1 : theta > 1}, D = {theta < 1}: every arc runs from a point of B (lower end) to a point of D (upper end); (1/2) sigma = #(D in (0,x)) - #(B in (0,x)). pq x_+ = +-(Rq + Sp) mod 2pq. rho = -sigma. Trefoil: rho = +2 on (1/12, 5/12). Mirror flips the sign, arcs unchanged.
- 13.5 [C]: 13a3542 and mirror of 13a4018 agree on HOMFLY, Jones, Khovanov, HFK; Alexander roots at alpha = 0.10971 and 0.11522; between them sigma = -2 vs +2. Longitude angle at alpha = 0.11247: theta/2pi = -0.0145345761398 and +0.0171688847270; rates about -4.6 and +6.3 turns per turn. theta invariant (Bar-Natan, van der Veen) nonzero on all 12,887 chiral prime knots to 13 crossings, zero on the 78 amphichiral. 7_1 # 7_1 vs 7_1 # mirror: signature +-12 vs 0.

## 14. Connection energy
- H = D + A, A anti-Hermitian with unitary edge blocks: [H,H^dag] = -2[D,A]; (1/8)||[H,H^dag]||^2 = sum over edges ||D_i - A_ij D_j A_ij^dag||^2. Distinct from the projector metric.

## 15. Maxwell-Dirac gate
- Seed: d = 1 + r^2, psi = d^{-3/2}(1 + iz, ix - y), A = 3N/d, B = 12N/d^2, j_W = N/d^2, so B = 12 j_W; integrals pi^2, 9 pi^2, 9 pi^2; at (1,0,0) curl B = (0,6,-3), j_W = (0,1/4,0).
- Lemma 15.1: Re[psi^dag sigma_k (sigma.pi) psi] = Re(psi^dag pi_k psi) + (1/2)(curl(psi^dag sigma psi))_k. Cor 15.2: a zero mode carries zero Pauli current. Prop 15.3: no static magnetic zero mode is self-consistent; a candidate needs non-constant A_0.
- 15.5: sector reduction needs (I-P)HP = 0; F(H,P) = (I-P)HP + PH(I-P).

## 16. Gigantefermion
- 16.3: V(a;s) = (1/2) mu a^2 + (lambda/4) a^4; H(a) = Delta sigma_x + a sigma_z, E = +-sqrt(Delta^2 + a^2), Tr(P_- sigma_z) = -a/sqrt(Delta^2 + a^2).
- 16.4 [T]: chi = -Tr(Gamma P_-) = n_3 = m/rho; |d-dot|^2 = rho-dot^2 + Delta^2 g_ss; rho^2 chi-dot^2 <= Delta^2 g_ss. eta = -2 kappa chi under coupling alpha = 1/2 + kappa chi [H].

## 17 (to 17.2)
- Stress candidate S_ij = d_i rho d_j rho + Delta^2 g_ij + chi_eta d_i eta d_j eta.
- 17.1: Smith coordinate Gamma_S = (z-1)/(z+1) = tanh(eps/2), z = e^eps; |Gamma_S| < 1 iff Re z > 0, = 1 iff Re z = 0. Exit line E(0)E(pi) = u^2 where the band-averaged Petermann factor is 2. Nuclei outside the disk: 5He 1.074, 5Li 1.220, 8Be 1.025; 4He 0.579.

(Sections 17.3 onward: appended below.)

## 17.3-19
- 17.3: ds^2 = -N(x)^2 dt^2 + dx^2 has R = -2N''/N; a linear lapse has a rate gradient and zero curvature.
- 18: T = (O, F, Theta, M, S). F(s) = g_P(P-dot, P-dot) = (1/2)Tr(P-dot^2). Three bounded records: rho^2 chi-dot^2 <= Delta^2 F; tau_off-dot^2 <= 4 F S; A-dot^2 <= 4 E_B A(1-A). Saturating pair: tau_off(t) = 2 sigma artanh(sin 2 Omega t), sigma = +-1 — same bound, opposite directions: "the metric limits how fast a record can change and never which way it goes."
- Theta = (theta, B); rank B = n-1 means one progression.
- 19.2: Tr((2P - I) P-dot) = 0 — the naive oriented projector scalar is dead by identity.

## 22-23. Tower and well
- Schur well: E_eff(x) = x^dag (A - B D^{-1} B^dag) x, y_* = -D^{-1} B^dag x; positive hidden structure gives a subtractive effective shift.
- mu(s) = mu_0 - chi W(s), W = integral [c_theta |theta-dot|^2 + c_P (1/2)Tr(P-dot^2)] [H].
- Section 23 model: I(r) = I_0 + alpha r; U_J = V + J^2/(2 I(r)); mu_* = mu_0 - b^2/d - g r-bar; lambda_* = lambda - g^2/(2 kappa); H_J-dot = -gamma v^2 - eta_y y-dot^2 - eta_r r-dot^2 <= 0; F_J(s) = c - g R_J(s) + lambda s, F_J' >= lambda_* > 0; two wells at a = +-sqrt(s_*) iff mu_J < 0.
- 23.1: Pi(theta) = (I + cos theta X + sin theta Y)/2, q = (1/2)Tr(Pi-dot^2) = theta-dot^2/4; eta_r r-dot + kappa(r - r-bar) = (g/2)a^2 + 2 alpha q.
- 23.2: e^{-nu u} A(u) <= A_nu(u) <= A(u). 23.3: theta-dot = J/I(r).

## Appendices
- C: Nakajima-Zwanzig exact: sigma-dot = L_0 sigma + integral K(t-s) sigma(s) ds + I(t); K-hat(z) = b(z-d)^{-1}c is the Schur complement of the hidden block of z - L. C.5: nonzero kernel does not imply readable memory.
- D: P1 (tangent geometry), P2 (weak-value bound), P3 (path ledger is a potential iff all loops silent), P4 (common clock; gaps mu_j - mu_k = tau-dot (E_j - E_k)), P5 (return criterion: exists j in 1..d_T^2-1 with R L^j Delta != 0), P5a (witness rho_W(t) = (1/2)[I +- sin(2gt) Z]), P6 (Delta S_S - sum beta_r Q_r = Delta I + sum Delta D(rho_r || tau_r)).
- E: engine numbers eps_h = 3, eps_c = 1, p_h = 2/5, p_c = 1/5, p_m = 3/10, eta = 1/4: p_* = 3/8, W_out = 7/20.
- F: claim lineage table (which claims SURVIVE / FALSE / OPEN). Relevant row: "UPG inverse-smallest-eigenvalue refraction index — FALSE as universal identification; use n = sqrt(g_parallel)".

## What this read gives the vacuum-disk work (constructions already in the paper, not new)
1. The staircase is Theorem 13.1(3): END STEP k = uaq +- vbp, k = a mod p, k = +-b mod q; omega = e^{+-2 pi i k/pq}. Each arc (a,b) has TWO end steps, one from each sign.
2. Theorem 13.2 says which end is which: with x = 2 alpha, the lower end is in B, the upper end in D, and every wall ends exactly one arc. So an arc is an ordered pair (lower step, upper step).
3. The lift beta = a/2 - pq alpha means the longitude phase turns -pq times per turn of meridian phase on every arc. A total turn along an arc is therefore LINEAR in alpha by Theorem 13.1(1). This is the paper's own reason the carried-over item 3 came out linear.
4. Section 9.2 is the affine phase readout: phi' = (AD - BC)/(x^2 + y^2). On an arc the numerator is the CONSTANT -[pq(m+eps_mu) + n + eps_lam + a/2]. A quadratic-in-k quantity cannot come from the numerator; it can only come from integrating over the denominator x^2 + y^2 between the two end steps, or from an end-point term.
5. Section 5.2: holonomy -1 = half the unit monopole flux. Section 18: saturating pair runs the same bound in opposite directions.
