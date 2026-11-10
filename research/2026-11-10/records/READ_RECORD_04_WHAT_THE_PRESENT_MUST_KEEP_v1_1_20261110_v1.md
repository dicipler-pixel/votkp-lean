# Read record 04 — What the Present Must Keep, v1.1 (2 Nov 2026), constructions with formulas

Source read in full: what_the_present_must_keep_v1_1.html (46k characters: abstract, Sections 1-8, Appendix A proofs A.1-A.10, computational record). Grades [T] [C] [N] [M] [H] [L] are the paper's.

## Memory (Thms 1-3)
- N_inf = intersection of ker R L^n; V_pred = V/N_inf. Thm 1: equality for n < dim V decides all n. Thm 2: any predictor F has rank >= dim V_pred. Thm 3: the present needs no memory iff RL = AR; otherwise it must carry dim V_pred - rank R further numbers. "Memory is the gap in Theorem 3."
- (1): x-dot = -i H_PP x - i B e^{-i H_QQ t} y(0) - integral K(t-s) x(s) ds, K(u) = B e^{-i H_QQ u} B^dag, B = PH(1-P).
- (2): Tr K(0) = ||B||^2 = E_B, the WEIGHT BETWEEN.

## The weight between (Prop 4, eq 3)
- Prop 4 holds for EVERY idempotent, orthogonal or not: V = PV(1-P) + (1-P)VP.
- (3): g = (1/2)||P-dot||^2 = (1/2)||[H,P]||^2 = E_B; for a pure state g = Var_psi H. One number = speed of the kept sector = zero-lag memory = energy variance.
- NOTE ON SIGN: this paper writes Omega = 2 Im Q. IQGT writes Omega = -2 Im Tr(XY*) with Q = g - (i/2)Omega. Same bound 4 det g >= Omega^2; the sign convention differs between the two papers.

## The gap ladder (Props 5-6, Cor 7)
- S_k = sum |K_ij|^2 |Delta_ij|^k; log S_k is convex in k (Holder).
- Ground row rungs: k = -2: S_-2 = g_KK (projector metric, memory geometry). k = -1: 2 S_-1 = alpha_0 (static response, light). k = 0: S_0 = Var_0 K (energy variance, speed of time). k = +1: S_+1 = (1/2)<0|[K,[H,K]]|0> = F (oscillator-strength budget; TRK sum q^2 hbar^2/2m).
- Cor 7: alpha_0 <= 2 (g_KK^2 F)^{1/3}, equality iff all coupling sits at ONE gap value. One ladder step (a,b,c) = (-2,-1,1).

## The record and its speed (Thm 8, Cor 9)
- C = E^dag P E, 0 < C < I; C - C^2 = P_12 P_12^dag (the census). tau = log det(I-C) - log det C (log-odds empty vs full). The census loses its sign: diag(0.2,0.8) and diag(0.2,0.2) share a census, offsets 0 and log 16.
- (5): tau-dot^2 <= 4 g S, S = Tr[(C(I-C))^{-1}]. Equality iff P-dot = lambda [P,[P,F]], F = E W E^dag, W = -(C(I-C))^{-1}.
- Cor 9: |tau-dot| <= 2 sqrt(E_B S); if PH(1-P) = 0 the offset is frozen.
- One mode (6): A-dot^2 <= 4 g A(1-A). 2x2 exact gap: 4gS - tau-dot^2 = 4 (Im b-bar b-dot)^2/(c(1-c))^2.

## Two readers of a constant (Prop 10)
- (a) projectors and Q unchanged by H -> sH + cI. (b) a clock reads only c_1 - c_2. (c) contour ledger Z_Gamma(K) = (1/2 pi i) loop-integral log z Tr(z-K)^{-1} dz = sum log lambda_j: Z(K + cI) = Z(K) + sum log(1 + c/lambda_j); Z(alpha K) = Z(K) + k log alpha.
- "The ledger and the clock are the two readers of a weight, and the projector is the reader of a direction." [H]

## The wall (Thms 11-13, Props 14, 16; Thm 15)
- Orthogonal projector: tangent pairing is a Gram form; metric can lose RANK, never SIGN. Oblique idempotent: can do both.
- Thm 11: q(D) = (1/2) Re Tr D^2 has neutral signature (2k(n-k), 2k(n-k)); q = ||U||^2 - ||V||^2 with U = (X + Y^dag)/2, V = (X - Y^dag)/2.
- Thm 12: Re Tr(P(0)P(t)) = k - (1/2) Re Tr(D^2) t^2; a negative direction lifts the overlap above the cap k.
- Chart (8): z = x + iy, w = x + i y^2, P = (1/(1+zw)) [[1, w],[z, zw]], H = (2 + y/10)P + (5 + y/5)(I-P).
- Thm 13: on x = 0, g = (1 - y^3)^{-2} diag(1, -2y); gap stays 3 + y/10; ledger Z = log(2 + y/10) passes through.
- Prop 14: P is self-adjoint iff y = 0; det g = 0 along y = 0 and changes sign across it; d_z P is nilpotent everywhere; on the wall d_y P = i d_z P is a nonzero nilpotent: (1/2) Re Tr(d_y P)^2 = 0 while (1/2)||d_y P||^2 > 0. THE WALL SITS WHERE THE PROJECTOR IS ORTHOGONAL; the null direction is a nilpotent push. det g = -y A B / D^4.
- Thm 15 source insertion: d/dt Z_Gamma(K + tB) at 0 = Tr(P_Gamma K^{-1} B). Polarisation with e_i, e_i + e_j, e_i + i e_j recovers P_Gamma K^{-1}.
- Prop 16: read with phase, the source rebuilds the wall; read through its real part only, the geometry is positive definite and blind to the wall, keeping one trace: positive semidefinite exactly on the wall.

## Neutrinos (Section 7)
- d_eps v = -(ikM + sigma(eps)(I - P_0)) v; M tridiagonal with c_l = (l+1)/sqrt((2l+1)(2l+3)); E_B = k^2 c_0^2 = k^2/3; (1/8)||[L,L*]||^2 = kappa^2 k^2/3.
- (11): a-dot = S(t) - k^2 c_0^2 integral [U_Q(t,r)]_11 a(r) dr, U_Q = e^{-[Sigma(t) - Sigma(r)]} e^{-ik(t-r)M_QQ}.
- (12): A-dot^2 <= 4 E_B A(1-A); free streaming reaches 0.99996 of the bound; gradual decoupling 0.58.
- Measured G: n=6: 0.648, 0.317, 0.154; n=3: 0.683, 0.431, ~0.30. Ledger test K1-K5: K2 FAILS (worst miss 0.101). The ledger of light that has left holds about half the memory (0.0157 against 0.0306); the other half is in light still in transit (hidden moments).

## What this adds to the vacuum-disk puzzle (links read off the text; untested)
1. RANK vs SIGN. On the vacuum disk, real z (flat tetrahedron) is the rim and the mirror shape lies outside. This paper's wall sits exactly where the idempotent becomes orthogonal and the metric changes SIGN beyond it. The vacuum-disk "orientation-aware ladder" (eps = -1 outside the rim) is a sign change of the same kind. Whether the rim of G is a sign wall in the sense of Prop 14 is untested.
2. PHASE-READ vs REAL-PART-READ. Prop 16: a real-part readout is blind to the wall. Vacuum disk Section 5: the twist is NOT in the angles of the pieces (rho = 0.02) and needs the integer windings. Both say the direction book is lost by a real-only reading.
3. THE CENSUS LOSES ITS SIGN; the offset keeps it. Same shape as: k^2/(pq) (direction, even in k) loses what k keeps.
4. ONE GAP SATURATES (Cor 7). Torus knots are the zero-decay, single-direction case; whether "one gap carries all the coupling" is the ladder form of "pure direction" is untested.
5. LEDGER HOLDS HALF. The contour ledger passes through a wall unchanged in kind and holds about half the neutrino memory; the rest is in transit. On the knot side the analogue would be: complex volume (ledger) vs the arc's interior representation (Tr Y = +-sqrt2 at the same boundary). Untested.
