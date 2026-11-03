# Non-Normality Is Connection Energy, v15 (read note)

Author: Jeromie Beasley. Facts from his text only; no judgement, no outside physics.
Source dir: /tmp/claude-0/-home-claude/f02ebe36-e50c-5833-b986-4d64a2a87a48/scratchpad/batch2/9963da5e-nonnormality_v15_code_and_sources/nonnormality_v15_code_and_sources/
Date note: tex \date, README and ZENODO_DESCRIPTION_v15.md say 21 October 2026. The brief says v15 = 30 Oct 2026 (Zenodo record 23787997 per the v12 note). Not reconciled in the files.
Read in full: main tex (551 lines), sec_primes, sec_arith, sec_wall, sec_records, sec_penrose, lean_v15, lean_table_v15, refs bibitems, README, ZENODO description, RECONCILIATION_LEDGER_v15 (285 lines), MERGE_LEDGER_v14. The _full.tex inlined copy was only grepped/sampled (duplicates the section files). Scripts/outputs skimmed for kill conditions and verdicts only.

## 1. The operator and its two books
- H = D + A on a finite graph G=(V,E), rank r>=1. D = diag(D_i), D_i Hermitian (obstruction field). A* = -A, unitary edge blocks, A_ji = -A_ij*.
- U_ij(X) = A_ij X A_ij* : induced connection on End(E).
- (1) E_- = (1/8)||[H,H*]||_F^2 = sum_edges ||D_i - U_ij(D_j)||^2.
- (4) E_+ = (1/8)||H^2 - H*^2||_F^2 = sum_edges ||D_i + U_ij(D_j)||^2.
- With X = DA: E_- = 2||Herm(DA)||^2, E_+ = 2||Skew(DA)||^2.
- Budget: E_- + E_+ = 2 sum_i deg(i)||D_i||^2 = 2||DA||^2, independent of transport.
- Difference: E_- - E_+ = 2 Re Tr((DA)^2) = -4 sum_edges Tr(D_i U_ij(D_j)).
- Product: E_- E_+ = ||DA||^4 - (Re Tr (DA)^2)^2.
- Per edge (a = D_i, b = U(D_j), s = ||a||^2+||b||^2): E_-e E_+e = s^2 - 4<a,b>^2 = s^2(P^2 + L^2).
- Verbatim scope: "The budget is an identity of a fixed field, not a conservation law." "The product of the books has a Lorentzian shape and is not a mass."
- Zero sets: ker E_- = holonomy-fixed Hermitian fields; ker E_+ = sign-twisted holonomy-fixed fields (loop sign (-1)^l). Odd loop with trivial holonomy admits no anti-parallel field. Bipartite sign flip sigma swaps E_- and E_+. Double cover: E_-(F) = 2E_-(S) + 2E_+(T).
- Corollary 1: H normal and H^2 Hermitian imply D_i = 0 at every vertex with an edge.

### Born reading
- W_ab = Tr(P_a U(Q_b)) doubly stochastic. E_e^(-/+) = sum W_ab (lambda_a -/+ mu_b)^2; E_- - E_+ = -4 sum W_ab lambda_a mu_b.
- Balance = zero uncentered cross-moment, not independence. Example lambda=(2,-1), mu=(1,2), W=I: 10=10, covariance -3/4.
- Rank-k projector fields: E^(-/+) = 2k(1 -/+ p), p Born transition probability; per-edge budget 4k; principal-angle form 2 sum sin^2 and 2 sum(1+cos^2); sum_e p_e = -Re Tr(DA)^2/(2k).

### Sector flip
- Gamma=Gamma*, Gamma^2=I; crossing part A (Gamma A Gamma = -A), inside part B; Tr(AB)=0. Herm(Gamma A) = Gamma Skew A; Tr X^2 + Tr(Gamma X)^2 = 2 Tr B^2. Quarter turn Gamma A = i U A U*, U = exp(-i pi Gamma/4). Flip keeps whole self-commutator matrix of the crossing part. Redistribution A = P[P,X] - [P,X]P when Gamma = 2P-1. No sign anticommutes with all of sigma_z, sigma_x, J.

### Relaxation flow (new in v15)
- K' = -2[[K,K*],K]; d||K||^2/dt = -8 Phi, Phi = (1/2)||C||^2, C=[K,K*]. On class D+A, Phi = 4E_-. Total drained = Henrici departure ||K0||^2 - sum|lambda|^2.
- E_-(K) = (||K*K||^2 - ||K^2||^2)/4; E_+(K) = (||K^2||^2 - Re Tr K^4)/4.
- E_+ fell in every run, ending at 2 sum (Re lambda Im lambda)^2; rate never positive on 20000 random matrices. Not proved; listed Open.
- Dual flow K' = -2[C,K*] keeps ||K||^2. Flow leaves unitary-edge class: K=[[d1,1],[-1,d2]] gives K'=[[-8delta,-4delta^2],[4delta^2,8delta]].

## 2. One edge: scalar shore, boost, Smith disk
- (15) E_-e/E_+e = Gamma_e^2, Gamma_e = (d_i-d_j)/(d_i+d_j) = tanh((1/2) ln(d_i/d_j)). E_+e - E_-e = 4 d_i d_j. Flux balance (d_i-d_j)^2 + 4 d_i d_j = (d_i+d_j)^2.
- Boost: (d_i+d_j, d_i-d_j) Lorentz vector, invariant 4 d_i d_j. d_i -> e^phi d_i, d_j -> e^-phi d_j shifts tau = ln(d_i/d_j) by 2phi; Gamma -> (Gamma + tanh phi)/(1 + Gamma tanh phi). Verbatim: "It is a boost of the two field values, not of spacetime."
- Smith disk / Cayley w=(z-1)/(z+1): positive ratio on real diameter at w = tanh(tau/2); Gamma_p = w for two point counts. Reactive loads on circle: kappa/y = -tan(theta/2) gives Gamma = e^{i theta}. Matched load z=1 gives Gamma=0 (horizon). Schur-Cayley: Z_b = W*LW, I - S*S = 4 (WV)* Herm L (WV). Signed lapse lambda = (rho-a)/(rho+a) = tanh(1/2 log(rho/a)); rho -> a^2/rho (reflection/inversion) negates it. Hyperbolic metric as optical metric n=1/y with Snell first integral.
- Peel coordinate: directed peel coordinate from VOTKP Prop. 19.1, composition u (+) v = (u+v)/(1+uv); in the Route-and-endpoint paragraph only.
- Grep: "Thomas rotation", "Wigner rotation" and "Schottky" appear NOWHERE in v15 text, README, ledgers or scripts. No Gamma^2=1/2 threshold either.
- Passive fields (D_i PSD): E_- <= E_+, |Gamma| <= 1.
- (17) Duality P^2 + V^2 + L^2 = 1, identified with Jakob-Bergou complementarity.

### Constant and common clock
- Trace split D_i = c_i I + T_i: E^(-/+) = r sum (c_i -/+ c_j)^2 + sum ||T_i -/+ U(T_j)||^2. Constant c: [H+cI,.] unchanged; H^2 - H*^2 gains 4cA.
- Centered projectors: books 2k(1-rho), 2k(1+rho) - 4k^2/r; balance at rho = k/r.
- One site, J: MJ + JM = (Tr M)J; ||[M,J]||^2 + ||{M,J}||^2 = 4||M||^2.
- Common clock: G = tau-dot H0 + aI gives [G,G*] = tau-dot^2 [H0,H0*], G^2-G*^2 = tau-dot^2(H0^2-H0*^2) + 4 tau-dot a A. Born matrices and every ratio (Gamma_e, p_e, V_e) unchanged by D -> sD; books scale as s^2. Verbatim: "No ratio of the books can fix a clock rate." With H0=I, rates 1 and 0 give the same generator.

## 3. Graph primes (sec_primes)
- Twisted Ihara-Bass: det(I-uB) = (1-u^2)^{(m-n)d} det K(u), K(u) = I - uA_rho + u^2(Deg-I)(x)I. Ends K(+1) = L^-, K(-1) = L^+: the two book operators. Zeta has poles at +-1.
- zeta_rho(-u) = zeta_{-rho}(u) (sign = parity of prime). Double cover zeta~(u) = zeta(u)zeta(-u). Mirror K(1/(qu)) = K(u)/(qu^2).
- Zeros off |u|=1/sqrt q: number 2#{|lambda| > 2 sqrt q}.
- Prime-trace recurrence t_l = c t_{l-1} - t_{l-2}, t_l = 2T_l(c/2). Pincherle: minimal solution exists iff |c|>2.
- Companion T: T^2 = (c^2/4 - 1)I; ||Herm T||^2 = c^2/2; ||Skew T||^2 = 2; Phi = 4c^2; Phi_inf = 4/c^2.
- Theorem (Primitive-cycle completion), triangle: C_3 = 2cos3phi; zeta^-1 = 1 - C_3 u^3 + u^6; e_3 = d^3 - 3dt^2 + t^3 C_3.
- Proposition (noncentral rank-two realisation): Tr Ad(U^3) = 2 + C_3; zeta_Ad^-1 = (1-u^3)^4 (1 - C_3 u^3 + u^6)^2. Books of sigma_z are (0,24).
- Climb-or-swap; graph-murmuration null (T5, below).
- Exploratory outputs: T3 kill not met except Petersen with trivial gains (pure swap). T4 mirror survives (7.3e-15; 1000/1000 off-circle counts). T5: NULL for sign det A_s (permutation p 0.25-0.91); real split for parity of frustration index on cubic graphs (z up to 8.9 at n=16, 7.0 at n=20, p=0.005); none on quartic (p=0.41). Fold tests: median fraction on common line 1.0, 40/40 folds; B1 bath toy has no EP at J != 0.

## 4. Arithmetic primes (sec_arith)
- Theorem (Frobenius edge): E_-p = 4p - a_p^2, E_+p = a_p^2, budget 4p; rho_p = cos^2 theta_p = a_p^2/(4p).
- Corollary (Arithmetic restrictions): odd p never balances; Q_p = 4p/(3 a_p^2).
- Theorem (Adjoint sign-blindness): Ad(-U) = Ad(U).
- Local twist record Gamma_p = a_p/(p+1) = tanh(tau_p/2). Proposition (global-twist correction): a_p(E^(d)) = chi_d(p) a_p(E).
- Sato-Tate share of a_p^2 > 2p: 1/2 - 1/pi ~ 0.1817. Share a_p > sqrt(2p): 1/4 - 1/(2pi) ~ 0.091 (37a1 below 5000: 0.079). Partial-product statement graded [conditional].
- 120-pair test: correlation 0.468, KILL vs registered 0.7 (primes_boost_twist_02 printed KILL; sign-agreement kill <0.75). Ledger C-1: reported as computed, per-pair test fails as registered.
- 10,293-class murmuration run: corr -0.985 (kill if > -0.5, passed); book balance -0.300 with 2 of 25 bins apart. Table for 32a2/37a1/389a1.

## 5. The wall (sec_wall)
- Real traceless 2x2: T^2 = q(T) I, q = (1/2)Tr T^2 = (1/2)(||Herm||^2 - ||Skew||^2). q=0, T != 0 is the nonzero nilpotent: the wall.
- Spinning key: q(M) = h^2 - r^2; ||[M,M^T]||^2 = 32 h^2 r^2. Key (3,5,6) with Omega=1 normal and unstable. Generic flip: ab>0.
- Critical damping: T^2 = omega^2(zeta^2-1) I. alpha(zeta) peaks at zeta=1; alpha(1.01)=0.8682 omega. 2% band: t=3.756 (zeta=0.8), t=5.834 (zeta=1). Finite norms 0.0151646 vs 0.0562309. Jordan growth threshold |mu|>2b.
- Many DOF: 40/40 folds; slowest settling gives 0/40 folds.
- Counterexamples to "q=0 means wall": X=[[0,I2],[diag(1,-1),0]]; e^{i pi/4} sigma_z. Balanced books are not a wall: X=DA normal with XX* = I/4.
- Four-body Bures transport: Gram-chart Jordan block is a chart artefact (ledger C-2/C-8); Bures-metric block is normal, wall at finite distance arcsin x0.

### Koide (graded "a conditional reformulation, not a derivation")
- Q = (s^2+h^2)/(3s^2); h^2/s^2 = 3Q-1. Z = h1 sigma_z + h2 sigma_x + sJ, Z^2 = (h^2-s^2)I.
- Koide <=> h=s, Z^2=0, 45 degrees to (1,1,1), Born weight p = 1/(3Q) = 1/2.
- Centered plane books (2(1-rho_K), 2 rho_K) = (1,1) at Koide. Uncentered C^3 gives (1,3); centered C^3 gives (1,5/3).
- p over relative phases: [0.171868, 0.500002]; full dephasing 1/3.
- Brannen circulant Q = (1+2(t/d)^2)/3; Koide at t = d/sqrt2.
- Proposition (Positive phase domain): three roots positive iff cos3phi > 1/sqrt2. Measured |phi| = 0.22222476, near 2/9.
- Compton-wavelength form credited to Caleigh Fisher (@Kali_fissure).
- Damped-oscillator encoding K ~ s[[0,1],[-1,-2h/s]], zeta^2 = 3Q-1. Selector: asymptotic rate maximal at h=s.
- e_3 = s^3/(3 sqrt3) - s h^2/(2 sqrt3) + (h^3/(3 sqrt6)) sin3theta (the cubic C_3 left free). Stress flow Z' = -2[C,Z] keeps h^2-s^2. Cooling does not select the wall.
- Measured Q = 0.6666644634; Q-2/3 = -2.2e-6 = 0.43 sigma; exact Koide needs m_tau = 1776.969 MeV, zeta = 0.9999967. (Ledger S31: Q ~ 0.6666605 with m_tau 1776.86 superseded by PDG.)
- Verbatim: "It fixes the cone. The cubic record C_3 stays free."

## 6. Records the books do not keep (sec_records)
- Books are even, blind to direction: E(H^T) = E(H).
- Signed record: which end larger is Gamma_e. Occupation edge E^- = (1-2nu)^2, E^+ = 1, tau_nu = 2 artanh(1-2nu).
- Phase record: Bargmann invariant Tr(P0 P1 P2^+-) = (1+-i)/4.
- Occupation record: Gaussian offset tau = sum tau_nu; boundary-sets-sign law e^{tau_{B+x}} = e^{tau_B} s0/s1.
- Route record: L_rec = 2 sum|r_j|; D_end = 2|sum r_j|; L_rec - D_end = 4 min(R+,R-).
- Endpoint record needs signs the books erase. Overlaps F, D; Rice-Mele vs Kitaev. Spectral flow (circle odometer). Sync rule: 4 of 6 predictions held.

### Hidden-channel memory
- H = [[A,B],[B*,D]]; self-energy Sigma(z) = B(zI-D)^-1 B*. ||[H,P]||^2 = 2 Tr BB*; q(C) = -Tr BB*, q(-iC) = +Tr BB*.
- Compression: PH^2P - (PHP)^2 = ((1-P)HP)*((1-P)HP).
- Moment horizon: two hidden channels share a kernel exactly when moments agree for n < q1+q2.
- Same footprint, other future: B=(1,1)/sqrt2, spectra (0,2) vs (1,1): K(pi) = +1 vs -1; (|01> +- i|10>)/sqrt2 readouts +-0.531186.

## 7. Penrose section
- Bunting-Masood-ul-Alam doubling = the pair of books of one scalar edge: (1+lambda)psi/2 = 1 and (1-lambda)psi/2 = a/rho; inversion = sign flip. Otherwise graded structural comparison.

## 8. Other results
- Odd loops: C^2 floor (N/2)(1-cos(pi/N)); pentagon KCBS sqrt5 > 2; triangle total 1.
- Ring: (24) floors; ring max (N/2)(1+cos(delta/N)); corner slopes +-4 sin(pi/N) at d=pi.
- Bow tie 6-3sqrt3 ~ 0.804. Shared edge 4-2sqrt2 ~ 1.172 (Zenodo description says analytic proof; tex still says "computed by direct optimisation").
- Born scope (H1-H5), oblique no-go, dimension-two compatibility. Overlap identity k - Tr(PR) = 1/2 Tr((P-R)^2) (Gravity Ledger Thm 8/Cor 9); Mathlib PR #43951.
- "What is classical" section and Scope section present.

## 9. Open (verbatim list from main tex Open paragraph, paraphrased tight)
Selection question (derive a physical generator equivalent to Z - hI); signed traces and quadratic characters to keep; which holonomy probes measurable; why EP points carry two transpositions off |w|=1; whether E_+ rate is never positive; noble-gas test of defect 2 Tr B^2 proposed, not run; when the skew book must vanish; Proposition H constant unstated.

## 10. Lean and checks
- Lean: 163 declarations, 17 false controls; two repos plus cited libraries; VOTKP branch claude-finish-lean commit bd4d15a (ledger V27 FIXED [62], App B p.66).
- Gates 61+13+42+70+33+102 all pass; sixth script G16-G75 with opposite runs. Kill conditions: ce12 error > 1e-10.
- Census outputs list corrected claims (14.13 Hz family, 8_19 claims, CHSH fit found false, left out).

## 11. What changed from v12
- v12: sections 1-10, appendices A-C, equations to ~(42). v15 adds: relaxation flow; Born scope H1-H5; graph-prime recurrence/Bass pencil; arithmetic (Frobenius) edge; records section; hidden-channel memory; Penrose; common clock; Smith/Cayley and peel coordinate.
- Koide: v12 only [CONDITIONAL], no centered-plane books. v15 adds centered books (1,1) and free cubic C_3; v12 link "weight reading assumes one positive phase" is replaced by the Positive phase domain proposition.
- Ledger: 274 rows (IN 193, FIXED 33, LEFT OUT 48); session S1-S172 (122/12/38), GitHub R1-R75 and V1-V27 (71/21/10).
- Fixes: C-1 (120-pair reported as failing as registered); C-2/C-8 (Jordan block chart artefact); S3 (Herm/Skew split is Gravity Ed.6 Prop 15; Thm 6 neutral signature); R1,R5,R11,R23,R24,R75,V19 "not formalised" lines corrected; V18 counts 163/17; V25 origin 18-21 June skew-transport drafts (24 June paper symmetric); S31 superseded; S40 rank-2 correlations -0.048, -0.151 (were -0.008, -0.142).
- Schottky / Thomas rotation: absent in v12 and v15.
