# Notes: "What the Neutrino State Must Keep" v6, 11 November 2026 (Jeromie Beasley)

Reader's working copies (local, extracted from Drive):
- (a) /tmp/claude-0/-home-claude/f86429e3-e32f-50e6-b1fd-fcadab5264af/scratchpad/swarm/dl_neutrino/a/a.pdf , text a/a.txt (pdftotext -layout, 7779 lines, 120 pages)
- (b) /tmp/claude-0/-home-claude/f86429e3-e32f-50e6-b1fd-fcadab5264af/scratchpad/swarm/dl_neutrino/b/b.pdf (12 pages); its embedded attachment Source_and_Data_v6.zip unpacked in dl_neutrino/bzip/ (paper.md = the manuscript source with every equation in TeX, compute.py, extend.py, results.json, run.log, independent_extension_review.md, figures/)

READ STATUS (see section 8 at the end for the exact coverage of (a)'s Appendix B).
- (b): all 12 pages read. The PDF renders equations as images, so pdftotext drops them; every equation below for (b) is taken from the paper's own paper.md source inside the PDF attachment (not rebuilt by me).
- (a): pages 1-27 (whole main text, references, Appendix A proofs A.1-A.15) read in full, line by line. Appendix B (pages 27-120: scripts, run logs, pre-registrations) - coverage stated in section 8. Appendix C (Lean) - the abstract says "machine-checked in Lean (Appendix C)"; see section 8 for whether an Appendix C is physically present.
- pdftotext broke many 2-D fractions/superscripts in (a); where I rebuilt an equation from the surrounding text I say "rebuilt".

---------------------------------------------------------------------
## 1. What each paper is

### (a) What_the_Neutrino_State_Must_Keep_v6_2026-11-11.pdf  (Drive 1k8qnlakJGaFhePfIw8plu6VUBj6H08Dj)
- Title as printed: "What the Neutrino State Must Keep: Hidden Angular Structure, the Flux-Shear Link and the Threshold for Primordial Black Hole Formation"
- Author: Jeromie Beasley. Date line: "11 November 2026 (version 6 of When the Neutrinos Leave)".
- 120 pages, LaTeX/pdfTeX, created Wed Nov 11 14:55:08 2026 CST. 2.4 MB. No embedded files.
- Disclaimer above abstract: "AI-assisted. The ideas and research direction are the author's; AI tools (Claude, Anthropic) were used for literature search, computation, drafting and typesetting. The numbers come from the scripts, run logs and outputs printed in Appendix B. The simulations are runs of S. McCormick's public code on a cloud computer, not experiments."
- Nature: the long, full paper. Sections 1-13 (pp.1-22), References [1]-[21] (pp.22-23), Appendix A Proofs A.1-A.15 (pp.24-27), Appendix B Evidence: scripts, run logs, outputs B.1-B.25 (pp.27-120). It is the continuation of the "When the Neutrinos Leave" v5 body (sections 1-7) plus three new v6 sections: 8 (which hidden directions the future reads - readout Gramian), 9 (the door in the full GR collapse), 10 (McCormick's multigroup physical model as the flux-shear link). It reports NEW RUNS of McCormick's GR code and measured black-hole thresholds.
- Grade tags used in the text: [derived], [computed], [measured], [fit], [reading], [H] (hypothesis/reading), "Lean", "checked, I1..I5" (identity checks in B.1).

### (b) What_the_Neutrino_State_Must_Keep_v6.pdf  (Drive 19qBI1q4ET7xBrBYL3P6bptzz0JLzM6Xb)
- Title: "What the Neutrino State Must Keep"; subtitle "Predictive Quotients, Collision Links, and the Geometry of Angular Memory".
- Author Jeromie Beasley. Date line: "11 November 2026 · When the Neutrinos Leave series · Research manuscript v6.0". Running footer "What the Neutrino State Must Keep · v6.0".
- 12 pages, A4, ReportLab, created Wed Nov 11 08:29:51 2026 CST (about 6.5 hours BEFORE (a)). 738 kB. PDF Subject field: "...; source and data attached". One embedded file Source_and_Data_v6.zip.
- "Scope and provenance. This manuscript contains completed finite-dimensional proofs and reproducible linear calculations. It does not report new general-relativistic collapse simulations. AI assistance was used for analysis, computation, independent mathematical checking and drafting."
- Nature: a short, purely LINEAR, finite-dimensional manuscript: toy constant-rate 12-moment chain; no GR runs; explicitly "without asserting a new primordial-black-hole threshold". Appendix B says "The working v6 label denotes this manuscript's place in the series, not a published DOI revision."

### How (a) and (b) differ (summary; details through the notes)
1. Scope: (a) = full research paper with nonlinear GR threshold runs of McCormick's code (Tests A-D, eleven r-thresholds, eight restart thresholds, multigroup deciding run) + linear chain + proofs + 94 pages of evidence. (b) = 12-page linear-only manuscript; claims no threshold result; says "Until those outputs are checked, this paper makes no claim that hidden angular data change the PBH threshold." (a) by contrast states "the hidden structure moves the threshold itself" with measured differences 3.7e-3, 2.1e-3, 5.5e-3.
2. Status of the 1.11 slope: (a) reports "odd rate = 1.11 +- 0.01" as a measured number [Eq. 11]; (b) says "The earlier measured slope near 1.11 in prescribed split-rate interventions remains an existing result under numerical recheck, not a premise here."
3. Gramian: (a) uses a time-dependent history (McCormick's n=3, eps_dec=2), profile-summed over k and +-k averaged, readout to eps=4, chain L up to 90, top eigenvalues 0.367/0.148/0.040 at decoupling; no output weight W; kernel statement "as T -> infinity is N_inf ∩ Ran Q". (b) uses a constant generator d=12, k=1, kappa_e=0.2, kappa_nu=0.4, T=3, adds a positive-definite output weight W(t) (Theorem 2), proves kernel = N_inf for every finite T>0, eigenvalues 0.15898/0.006973/1.0429e-4/8.17e-7, and adds the rank-r error frontier (Theorem 4) which (a) does not have.
4. Only in (b): Theorem 2 (Gramian realization of the quotient, with weight W), Theorem 4 (best rank-r preparation summary E_r = sqrt(lambda_{r+1})), Table 1 error frontier, IQGT projector metric g(T) vs horizon (Eqs 10-12), VOTKP elimination in general block form with Laplace/Schur form (Eqs 13-15), the transpose "reciprocal blind spot" identity (Eq 16), Proposition 5 (conservative positivity budget optimum), "The Ball" section with boost formula (Eqs 20-22), references to Frank-Seibold 2011, Kalman, Eckart-Young.
5. Only in (a): G definition and McCormick's Table II, sound-speed weight sqrt(E_B)=k/sqrt3, kept-sector propagator g/(1-kappa g), truncated exceptional point, Tests A-D, memory form g and g_2 (w=0.89), matched-pair witness table, speed limit (Adot)^2 <= 4 E_B A(1-A), Smith coordinate / link rapidity, eleven thresholds, odd rate 1.11, shear-only 1.19-1.20, R_nu=0.2 check, intrinsic-ruler check, order-swap pairs under the memory form, closure comparison P1..P5/M1/M2/Chapman-Enskog, restart experiment (eight thresholds), multigroup model (r=1+kappa_n/kappa_e, deciding run 0.51972), annihilation and mean-of-rates tests, Lean (Appendix C claim).
6. Notation: (a) writes L = A + D, A=-ik mu, D=-kappa(I-P), rates kappa_1, kappa_2 (and kappa_e, kappa_n in sec.10), P = projector on isotropic part, Q = I-P or embedding of l>=3. (b) writes L = -ikJ - D with D = diag(0, kappa_e, kappa_e+kappa_nu, ...) (positive D), self-scattering rate "kappa_nu" (not kappa_n), J for the mu-matrix, Q_P = I-P for projector complement, Q for hidden embedding.
7. Citations: (a) cites VOTKP v2.9 Theorem 3.1 [6] and Dirac Time Definition 1.1 [7] for the predictive quotient, connection energy [8], Weight Between [9], Offset Speed Limit [10], IQGT v7.2 [21]. (b) cites Dirac Time v3.0.1 [3] and The Weight Between v1.1 [4] only, and says "A particular VOTKP theorem number is not assigned without checking its version."
8. Positivity/direction ranking: (a) finds the positivity-edge optimal direction on 32 bins gives 2.47x the readout of pure p3 (l=3:0.851, l=5:0.117, l=7:0.010) and in GR moves the threshold 1.47x pure p3. (b), with its conservative weighted-l1 budget, finds the opposite ranking: pure P3 (0.0350135) beats the leading Gramian direction (0.0247717). These are different admissible sets (b says so itself: "not for the larger set of all nonnegative distributions").
9. Order of history: (a) finds reversed-rate pairs differ 33-72% in (density, flux, stress) and 0.06-0.16 in g_2. (b) shows an exact density-return cancellation for a two-stage swap (density difference exactly zero) while the three-moment difference is 0.2819583387, exposed by a common third stage (0.0831015972).
10. McCormick reference: (a) cites both his v1 preprint (Zenodo 23808375) and v1.1 multigroup (commit eb7c4de, Zenodo 24129915); (b) cites only the "supplied 20-page manuscript, reviewed November 2026" with software v1.1.

---------------------------------------------------------------------
## 2. Objects and definitions

### 2A. Whose is what
McCORMICK's (S. McCormick, refs [1],[2],[3] of (a)): the spherical GR angle-resolved transport calculation; the result that free streaming raises the threshold: Delta C_l,c / C_l,c ≃ 0.235 R_nu on the linear compaction C_l, delta_c on the compaction peak rises ≃ 0.15 R_nu; collapse probability beta -> about beta^1.18 above 6e5 Msun (Gaussian fluctuations); gradual decoupling runs kappa = H (eps_dec/eps)^3; his Table II G values; his statement that linear theory "does not determine which diagnostic, if any, predicts the nonlinear threshold" [his Sec. IV C]; the relaxation collision model; plasma equation momentum drag kappa q [his Eq. (6)]; the code (ms_nuc.py, run_nuc.py), thresholds delta_c^fluid = 0.49773, delta_c^inst = 0.52832 (Gaussian), 0.44805 / 0.47747 (alpha=0.3 broad profile); his v1.1 multigroup model (six energy groups per flavour, plasma scattering + neutrino self-scattering, collision term Eq. (C3), first-order and positive common-frame targets), archived thresholds at T_H = 1 MeV 0.519406 +- 0.000156 (with self-scattering), 0.526391 +- 0.000109 (without), perfect fluid 0.49742; his envelope 5.3-6.2% for the annihilation epoch; factor 1.2-8 abundance cost for heavy-tailed statistics.
BEASLEY's: reading the collision operator as a cut; connection-energy link identity; sqrt(E_B)=c_s k; new runs outside McCormick's paper (Tests A-D, controls); memory form g, g_2; matched-pair witness ("the door"); speed limit; split-rate modification of the code and the eleven thresholds; link rapidity law (odd rate 1.11); shear-only test; readout Gramian as weight on the predictive quotient; restart experiment; identification of McCormick's multigroup collision term with the split link; deciding run (r=1 with isotropy history kept); annihilation and mean-of-rates tests.

### 2B. Objects in (a)
- eps = 1/(a H r_m): the Hubble radius in units of the perturbation size (time coordinate). eps_dec: decoupling epoch parameter. eps_0 = 0.1 start. eps_s: restart/planting surface. eps*: readout epoch. tau: conformal-type time used in the linear chain (tau_0 = 0.02 start; a kappa = eps_dec^n / tau^{n+1}).
- R_nu: neutrino fraction of the radiation (0.409 standard; neutrinos carry 41-49% of radiation). C_l: linear compaction. delta_c: threshold on the compaction peak.
- G: "the share of the instantaneous free-streaming shift that survives", Eq (1).
- Collision operator as a cut: L = A + D, A = -ik mu (free streaming, anti-Hermitian), D = -kappa(I-P) (collisions, Hermitian), P projects onto the isotropic part. mu = cosine of angle to the wave vector. Normalised Legendre basis |l>; chain l = 0,1,2,...; streaming couples only neighbours with c_l.
- "Non-normality is connection energy": (1/8)||[L,L*]||_F^2 = sum over links k^2 c_l^2 (D_{l+1}-D_l)^2: "the self-commutator energy of a transport operator is the energy of its Hermitian field failing to be parallel along the links" (scalar case of ref [8]).
- kappa_1: flux relaxation rate (momentum transfer); kappa_2: shear and higher moments' rate; r = kappa_2/kappa_1.
- E_B = ||P H (I-P)||^2 with H = k mu: "the weight between kept and streaming parts"; E_B = k^2 c_0^2 = k^2/3.
- Kept sector: the isotropic part |0> (density). Hidden: h = (v_1, v_2, ...) in sec. 6 elimination; in sec. 8 the hidden sector is l >= 3 with readout R onto l <= 2.
- A(tau): "the population left in |0>", A = |v_0|^2, averaged over the Gaussian profile with weights k^2 e^{-k^2/2} (script: Gauss-Legendre in k on [0.25, 9.0], 36 nodes, L_max=60).
- Memory form g(eps*), Eq (7); two-epoch form g_2 = w g(1.7) + (1-w) g(4.0), w = 0.89 [fit].
- Hidden propagator U_Q, integrated rate Sigma(tau) = -eps_dec^n/(n tau^n), kernel K ("the memory"), source S ("everything the hidden moments held at time s").
- Matched pair: two states with same (v_0,v_1,v_2) = (1, 0.2, 0.1), differing only by +-0.05 in v_3 (or v_4), scaled to unit norm; both positive (f(mu) >= 0.50). Witness R_ret: "the profile-weighted change in (v_0,v_1,v_2), relative to its size"; "the witness is on if R_ret > 1e-3". "The door" = this on/off as a function of planting time.
- Survival factor of the hidden block: exp[-eps_dec^n/(n tau_s^n)]; leakage (k/sigma)^l through damped rungs.
- Link as a reflecting step ("the author's coordinate"): Smith coordinate Gamma_ij = (d_i - d_j)/(d_i + d_j) = tanh((1/2) ln d_i/d_j); rapidity (1/2) ln(d_i/d_j); "exchanging the ends negates Gamma"; "a matched link carries no connection energy". Flux-shear link: Gamma_12 = (r-1)/(r+1). G as a point on the disk: Gamma_G = 1 - 2G, offset tau_G = ln[(1-G)/G].
- Odd rate (of a pair r, 1/r): [tau_G(r) - tau_G(1/r)] / ln r = "the rate at which the offset moves per unit of link rapidity"; even part = the symmetric remainder.
- Admissible window: range of r for which the split collision operator on the angle bins is a Markov generator: 3/4 <= r <= 3/2 (all l >= 2 at kappa_2); 0.6 <= r <= 1.2 (shear alone at kappa_2). [Extraction printed "43 <= r <= 32" and "34 <= r <= 32/23" - rebuilt as 3/4 <= r <= 3/2 from the figure caption "3/4 <= r <= 3/2"-pattern and the listed inside pairs 1.2, 1/1.2, 1.25, 0.8; upper rapidity edge "0.20" = (1/2)ln(1.5)=0.203 confirms 3/2.]
- Endpoint rule: a run moves the bracket only if it ends in a detected horizon (2M/R >= 1 with U < 0) or disperses; trisection (two trial amplitudes per round, bracket shrinks to middle third); failed run repeated once with Courant numbers 0.4 -> 0.3.
- Predictive quotient (a): "For a linear evolution vdot = L(tau) v with readout R, the part of the state no readout can ever see is N_inf = {v : R U(tau,tau_s) v = 0 for all tau}, and the minimal summary that predicts the readout is the quotient V/N_inf (the predictive quotient of VOTKP, Theorem 3.1 [6], and of Dirac Time, Definition 1.1 [7])."
- Readout Gramian of the hidden sector G_T, Eq (12): "weighs each hidden direction h by its integrated squared output, h* G_T h". Snapshot Gramian at the end of the horizon = the witness of Section 6.
- Restart perturbation delta I_ik, Eq (13); p_l = discrete orthogonal polynomial on the 32 angle bins; b = smooth bump vanishing identically for r <= 0.3 r_m and r >= 2 r_m; m_i = cell's positivity margin; f = +-1/2. d_K = 1.65e-4 = measured resolution drift (rerun of decoupling l=3 pair with 48 bins).
- Multigroup: kappa_e plasma scattering rate, kappa_n neutrino self-scattering rate; P_0, P_1 projections onto 1 and mu on the bins; r = 1 + kappa_n/kappa_e; u_eff = 0.831 = energy-weighted link rapidity; T_H, T_b temperatures; kept-share anisotropy 1 - A with A = I_0^2/||I||^2 on the bins; v_L = energy-frame velocity of the neutrino gas.
- Closures compared: P_1..P_5 (moment truncations), M_1, M_2 (entropy closures), viscous (Chapman-Enskog) closure, short-memory correction of optimal-prediction type [Seibold-Frank], exact elimination of l >= 3 (cut at l = 2|3).

### 2C. Objects in (b)
- psi_l(mu) = sqrt(2l+1) P_l(mu), orthonormal for d mu/2 on [-1,1]. J = matrix of multiplication by mu (symmetric tridiagonal), couplings c_l.
- f = coefficient vector; "The first three coefficients encode density, flux and quadrupolar stress, up to their fixed moment normalization. They are not equally scaled physical stress components."
- L = -ikJ - D, D = diag(0, kappa_e, kappa_e + kappa_nu, ...): "the frozen local angular realization" of McCormick's linear collision target (plasma scattering damps flux; neutrino self-scattering preserves a group dipole and damps quadrupole and higher). "It is not the full energy-changing Boltzmann collision operator."
- N_inf, V_pred (predictive quotient), Eq (4). Memory (Dirac Time definition as quoted): "memory is information absent from the present reduced description but needed to distinguish admitted future observations".
- G_T with weight W(t) (Eq 5): output-weighted Gramian. Q: hidden embedding (moments f_3..f_{d-1}); R: selects f_0,f_1,f_2 (in Thm 3, R = e_0^T, density alone).
- K_T (calligraphic): preparation-to-output map (K_T h)(t) = R e^{Lt} Q h; calligraphic G_T = K_T^dagger K_T. Input: Euclidean norm; output: L^2([0,T]; C^3) norm. "Resolved initial data are held fixed; this map describes the contribution of the hidden preparation."
- E_r (adapted summary error), E_r^seq (sequential-moment error, coordinate projection P_r retaining f_3..f_{r+2}).
- Phase transform f = S u, S_ll = (-i)^l: makes the generator real, preserves coefficient norms.
- P(T): orthogonal projector onto the leading simple eigendirection of calligraphic G_T; Q_P = I - P; g(T) projector metric.
- Blocks A(t),B(t),C(t),E(t) (resolved a, hidden h); U_E hidden propagator (time-ordered).
- Stages L_A, L_B, propagators E_A = e^{tau L_A}, E_B = e^{tau L_B} (NOTE: in (b) "E_B" is a stage propagator, NOT the weight across the cut E_B = k^2/3 of (a)).
- I(x,mu) positive-intensity construction with amplitude epsilon and budget b.
- "The Ball": a velocity-ball display using the bulk velocity v_L of the zero-flux frame; "Individual massless momentum directions lie on the null boundary; these are distinct objects." "A retained-share coordinate exceeding one is not a superluminal velocity."

---------------------------------------------------------------------
## 3. Equations in order

### 3A. Paper (a), numbered equations (1)-(15) and the unnumbered displays
(1) G = (delta_c - delta_c^fluid) / (delta_c^inst - delta_c^fluid).  [rebuilt from broken fraction; confirmed by sec. 7 text "G = (delta_c - delta_c^fluid)/(delta_c^inst - delta_c^fluid)"]
(2) d_t f = L f,  L = A + D,  A = -ik mu,  D = -kappa (I - P).
    Unnumbered: <l+1| mu |l> = c_l = (l+1)/sqrt((2l+1)(2l+3)).
    Unnumbered: [L, L*] = 2[A, D]; for diagonal D, [A,D]_ij = A_ij (D_j - D_i).
(3) (1/8) ||[L,L*]||_F^2 = sum_{links l -> l+1} k^2 c_l^2 (D_{l+1} - D_l)^2.   [derived; App. A.1]
(4) (1/8) ||[L,L*]||_F^2 = kappa^2 k^2 / 3.   [derived; checked to 1e-12, I1]
(5) (1/8) ||[L,L*]||_F^2 = k^2 kappa_1^2/3 + (4k^2/15)(kappa_2 - kappa_1)^2.   [derived; checked, I2]  "The energy is stationary in kappa_2 at kappa_2 = kappa_1."
    Unnumbered: E_B = ||P H (I-P)||^2 = k^2 c_0^2 = k^2/3, so sqrt(E_B) = k/sqrt3 = c_s k.   [derived; I3]
(6) <0|(s - L)^{-1}|0> = g/(1 - kappa g),  g = (1/k) arctan(k/(s + kappa)).   [derived; checked, I4]
    Unnumbered: two-moment truncation eigenvalues -kappa/2 +- sqrt(kappa^2/4 - k^2/3), merging at kappa = 2k/sqrt3.  [derived; I5]
(7) g(eps*) = (1 - A_{eps_dec}(eps*)) / (1 - A_inst(eps*)).
    Unnumbered evolution: d_tau v = -(ik mu + a kappa(tau)(I-P)) v, a kappa = eps_dec^n / tau^{n+1}; start in |0> at tau_0 = 0.02.
    Unnumbered: g_2 = w g(1.7) + (1 - w) g(4.0), w = 0.89.  [fit]
    Unnumbered (rejected diffusive-escape form): G = 1/[1 + sqrt15 (eps_dec/eps*)^{3/2}] with D = 1/(3 sigma), conformal rate sigma = eps_dec^3/tau^4 [rebuilt from broken extraction; B.3 pre-registration confirms "G=1/(1+sqrt15 (eps_dec/eps*)^1.5)"; n=6 version "G = 1/(1+sqrt24 (eps_dec/eps*)^3)"].
(8) U_Q(t,r) = e^{-[Sigma(t) - Sigma(r)]} e^{-ik(t-r) M_QQ},  Sigma(tau) = -eps_dec^n/(n tau^n),  Sigma' = sigma.
(9) adot(t) = S(t) - k^2 ∫_s^t K(t,r) a(r) dr,  K = c_0^2 [U_Q(t,r)]_11,  S = -ik c_0 [U_Q(t,s) h(s)]_1.   [derived; App. A.5]
(10) (Adot)^2 <= 4 E_B A (1 - A),  E_B = k^2/3.   [derived; App. A.6; Lean]
    Unnumbered: Gamma_ij = (d_i - d_j)/(d_i + d_j) = tanh((1/2) ln d_i/d_j); Gamma_12 = (r-1)/(r+1); Gamma_G = 1 - 2G; tau_G = ln[(1-G)/G].
    Split collision term in code: kappa(eps/4pi - I) -> kappa_2 (eps/4pi - I) + (kappa_2 - kappa_1) d_mu  (d_mu = dipole part).  Shear-only: kappa_1 (eps/4pi - I) + (kappa_1 - kappa_2) s_mu (s_mu = l=2 projection).
(11) odd rate = 1.11 +- 0.01.   [measured]
(12) G_T = ∫_{tau_s}^{T} Q* U(tau,tau_s)* R* R U(tau,tau_s) Q d tau.
    Unnumbered: (R B^j)_{2,2+j} = k^j c_2 ... c_{j+1} (main text) ; App. A.14 gives (-ik)^j c_2 c_3 ... c_{j+1} != 0 for k != 0.
    Unnumbered: time-integrated connection energy (k^2/3) ∫ sigma^2 d tau (order-blind).
(13) delta I_ik = f b(r_i) m_i (eps_i/4pi) p_l(mu_k).
(14) C = -kappa_e (I - P_0) - kappa_n (I - P_0 - P_1) = -diag(0, kappa_e, kappa_e + kappa_n, kappa_e + kappa_n, ...).
    Unnumbered: connection energy of (14): k^2 (kappa_e^2/3 + 4 kappa_n^2/15) in the continuum; on the bins c_0^2 = 1/3 - Delta mu^2/12, c_1^2 = (4/15)(1 - Delta mu^2).
(15) delta_c (r = 1) = 0.51972 +- 0.00009.   [measured]
    Unnumbered: v_L = 2q / [e + P_r + sqrt((e + P_r)^2 - 4 q^2)].  [rebuilt; identical to (b) Eq 21]
    Unnumbered (sec. 11): f = (1 - c_s)/(1 - 1/sqrt3).
Appendix A displays:
 A.1: [L,L*] = (A+D)(D-A) - (D-A)(A+D) = 2[A,D]; (1/8)||[L,L*]||_F^2 = (1/2) sum_{i != j} |A_ij|^2 (D_i - D_j)^2; |A_{l,l+1}| = k c_l; D = (0, -kappa_1, -kappa_2, -kappa_2, ...); c_0^2 = 1/3, c_1^2 = 4/15.
 A.2: P H (I-P) has the single entry <0|k mu|1> = k c_0; variance of k mu in the isotropic state = k^2 <mu^2> = k^2/3, "the same number".
 A.3: u = (s-L)^{-1}|0>, (s + kappa + ik mu) u = |0> + kappa P u; (1/2)∫_{-1}^{1} d mu/(s + kappa + ik mu) = k^{-1} arctan[k/(s+kappa)] = g; u_0 = g(1 + kappa u_0) -> u_0 = g/(1 - kappa g).
 A.4: on span{|0>,|1>}, L = [[0, -ik/sqrt3],[-ik/sqrt3, -kappa]], char. poly lambda^2 + kappa lambda + k^2/3, discriminant kappa^2 - 4k^2/3 = 0 at kappa = 2k/sqrt3 (not diagonalisable there).
 A.5: d_tau v = -(ik M + sigma(tau) Q) v, Q = I - P; adot = -ik c_0 h_1; hdot = -(ik M_QQ + sigma) h - ik c_0 a e_1; h(t) = U_Q(t,s) h(s) - ik c_0 ∫_s^t U_Q(t,r) e_1 a(r) dr; adot(t) = -ik c_0 [U_Q(t,s) h(s)]_1 - k^2 c_0^2 ∫_s^t [U_Q(t,r)]_11 a(r) dr. "For two states with equal a(s) the difference Delta a obeys the same equation with source S[Delta h(s)] and Delta a(s) = 0; if Delta h(s) = 0 it vanishes identically." Time-independent case e^{t(X - sigma I)} = e^{-sigma t} e^{tX} checked in Lean.
 A.6: d/dtau ||v||^2 = -2 sigma ||Qv||^2 <= 0; v0dot = -ik c_0 v_1; Adot = 2 Re(conj(v_0)(-ik c_0) v_1), |Adot| <= 2 k c_0 |v_0||v_1|; |v_1|^2 <= 1 - A. Core inequality |2 Re(conj(a)(-ih) b)| <= 2|h||a||b| checked in Lean.
 A.7: three moments, L = -ikM - D, D = diag(0, kappa_1, kappa_2); R_00 = <0|(s-L)^{-1}|0> = 1/( s + k^2 c_0^2 / ( s + kappa_1 + k^2 c_1^2/(s + kappa_2) ) ). At k = s = kappa_1 = 1: R_00(kappa_2) = [1 + (1/3)/(2 + (4/15)/(1+kappa_2))]^{-1}, R_00(1) = 32/37, R_00'(1) = -5/1369, while dE/dkappa_2 = (8k^2/15)(kappa_2 - kappa_1) = 0 there. Lean-checked. ("Energy stationarity is not response stationarity.")
 A.8: Gamma(1/r) = -Gamma(r); Gamma(r) = tanh((1/2) ln r).
 A.9: tau_G = ln(delta_i - delta) - ln(delta - delta_f); anchor tau_1 cancels from the odd part; d/d delta_f [tau_G(r) - tau_G(1/r)] = 1/(delta_r - delta_f) - 1/(delta_{1/r} - delta_f); d/d delta_i [...] = -1/(delta_i - delta_r) + 1/(delta_i - delta_{1/r}); coefficients d(rate)/d delta_f ≈ +50, d(rate)/d delta_i ≈ -28 per unit for inner pairs (the +-0.004 common-mode term).
 A.10: c_l^2 = (l+1)^2/((2l+1)(2l+3)): c_0^2 = 1/3, c_1^2 = 4/15, c_2^2 = 9/35; c_0^2/c_1^2 = 5/4, c_1^2/c_2^2 = 28/27 (adjacent weights differ by 1.8% from the second link on). Lean.
 A.11: O(delta) = (delta_i - delta)/(delta - delta_f) = odds (1-G)/G; Q = O(delta_r)/O(delta_{1/r}); odd rate = ln Q/ln r; for r = u/v and rational bound p/q: ln Q/ln r >= p/q <=> Q^q >= r^p <=> [(delta_i - delta_r)(delta_{1/r} - delta_f)]^q v^p >= [(delta_r - delta_f)(delta_i - delta_{1/r})]^q u^p, integers on a common scale; decided exactly by Lean's kernel.
 A.12: bins mu_k weight Delta mu, <f,g> = sum_k f_k g_k Delta mu, m_2 = <mu,mu>, P_2 = mu^2 - m_2/2; d = <mu,I> mu / m_2, s = <P_2,I> P_2/<P_2,P_2>; m_2 = 2/3 - Delta mu^2/6 (0.1% from 2/3 at N_mu = 32). Checked numerically to 1e-16.
 A.13: C I = -kappa_e (I - P_0) I - kappa_n (I - P_0 - P_1) I; (1/8)||[L,L*]||_F^2 = k^2 (c_0^2 kappa_e^2 + c_1^2 kappa_n^2); dipole coefficient c = q/(2 pi sum_k mu_k^2 Delta mu); bin values of c_0^2, c_1^2 "hold to machine precision at N_mu = 32, 64, 128, 1024 and are not proved here". Momentum exchanged with plasma is kappa_e q only.
 A.14: B = -ikM - D; observability matrix rows R B^j; N_inf = {0} for the frozen-time operator; for smooth time-dependent D(tau), G_T positive definite for every T > tau_s (derivative argument: the l=2 component of the (l_0 - 2)-th derivative of y at tau_s is (-ik)^{l_0-2} c_2...c_{l_0-1} h_{l_0} != 0); h* G_T h = ∫ ||R U Q h||^2 d tau; averaging over +-k commutes with parity l -> (-1)^l so eigenvectors can be chosen pure parity.
 A.15: delta I_ik has zero discrete moments of order 0,1,2 in every cell; positivity if |f| b_i m_i |p_l(mu_k)| < 4 pi I_ik/eps_i; m_i = min_k[4 pi I_ik/eps_i]/max_k|p_l(mu_k)|; on an isotropic cell |a| < 1/max_k|p_3(mu_k)| = 1.21498 for l=3, and +2.3509, -1.3885 for l=4.

### 3B. Paper (b), numbered equations (1)-(22) (verbatim from paper.md)
(1) J_{l,l+1} = J_{l+1,l} = c_l,  c_l = (l+1)/sqrt((2l+1)(2l+3)).
(2) fdot = L f,  L = -ikJ - D,  D = diag(0, kappa_e, kappa_e + kappa_nu, ...).
(3) (1/8)||[L, L^dagger]||_F^2 = k^2 (kappa_e^2/3 + 4 kappa_nu^2/15).   [Proposition 1 - two collision links]
(4) N_inf = ∩_{j>=0} ker(R L^j),  V_pred = V/N_inf.   [the predictive quotient]
(5) G_T = ∫_0^T e^{L^dagger t} R^dagger W(t) R e^{Lt} dt;  result ker G_T = N_inf.   [Theorem 2]
(6) (K_T h)(t) = R e^{Lt} Q h,  calG_T = K_T^dagger K_T.
(7) E_r = sqrt(lambda_{r+1}),  0 <= r < m.   [Theorem 4]
(8) E_r^seq = sqrt( lambda_max( (I - P_r) calG_T (I - P_r) ) ).
(9) leading eigenvalues (0.1589825109, 0.0069727910, 0.0001042932, 8.1718927e-7).
(10) g(T) = (1/2)||P'(T)||_F^2 = ||P(T) P'(T) Q_P(T)||_F^2.   (from P^2 = P: P P' P = Q_P P' Q_P = 0)
(11) g(T) = sum_{j>1} |u_j^dagger calG'_T u_1|^2 / (lambda_1 - lambda_j)^2,  calG'_T = K(T)^dagger K(T),  K(T) = R e^{LT} Q.
(12) g(3) = 0.0025469832093.
(13) adot = A(t) a + B(t) h,  hdot = C(t) a + E(t) h.
(14) adot(t) = A(t) a(t) + B(t) U_E(t,t_0) h(t_0) + ∫_{t_0}^{t} B(t) U_E(t,s) C(s) a(s) ds.
(15) [zI - A - B (zI - E)^{-1} C] a_hat = a(0) + B (zI - E)^{-1} h(0).
(16) e_0^T E_B E_A e_0 = e_0^T E_A E_B e_0.
(17) I(x,mu) = 1 + epsilon Re[ e^{ikx} sum_{l>=3} f_l sqrt(2l+1) P_l(mu) ].
(18) epsilon sum_{l>=3} |f_l| sqrt(2l+1) <= b < 1  (guarantees I >= 1 - b).
(19) b max_j ||K e_j|| / w_j.   [Proposition 5]; proof display ||K h|| <= sum_j |h_j| ||K e_j|| <= b max_j ||K e_j||/w_j.
(20) q' = gamma^2 [ (1 + v^2) q - v (e + P_r) ].
(21) v_L = 2q / ( e + P_r + sqrt( (e + P_r)^2 - 4 q^2 ) ).
    Unnumbered: q/e = 4v/(3 + v^2) (boosted isotropic gas only).
(22) d_t (P_{r,+} - P_{r,-}) = -(4/35) e a'(x),  from ∫_{-1}^{1} mu^3 P_3(mu) d mu = 4/35, for I_+- = I_0[1 +- a(x) P_3(mu)] under d_t I = -mu d_x I.

---------------------------------------------------------------------
## 4. Results with the grade the paper gives

### 4A. Paper (a)
Section 2
- All non-normality of the single-rate model lies on the density-flux link: Eq (4) [derived; checked to 1e-12, I1]. "the same channel as the momentum drag kappa q in McCormick's plasma equation".
- Two-rate identity Eq (5) [derived; checked, I2]. Stationary in kappa_2 at kappa_2 = kappa_1.
- Shear link carries 64% (nu_e, ratio 1.5) and 97.5% (nu_mu,tau, ratio 7) of the non-normality [computed, under those assumed ratios].
- sqrt(E_B) = k/sqrt3 = c_s k (radiation sound speed) [derived; I3]. "A rate bound built on E_B therefore sees the root-mean-square streaming speed 1/sqrt3, not the light-speed front that empties the overdensity."
- Kept-sector propagator Eq (6) [derived; checked, I4].
- Exceptional point at kappa = 2k/sqrt3 belongs to the 2-moment truncation [derived; I5]; with 200 moments the least-damped mode turns real only at kappa ≈ 0.646 k; hydrodynamic poles meet a branch cut [computed].
Section 3 [all measured]
- Reproduction: delta = 0.5109, n=3, eps_dec=2 forms a black hole (at eps 6.61), inside McCormick's bracket (0.51074, 0.51109).
- Test A (broad profile alpha = 0.3, n=3): eps_dec=4: delta_c = 0.45337 +- 0.00013, G = 0.181 +- 0.004 (Gaussian 0.190); eps_dec=8: 0.44938 +- 0.00012, G = 0.045 +- 0.004 (Gaussian 0.063). "the collapse time alone does not set the clock" (29% less at eps_dec = 8).
- Tests C, B, D (Gaussian, n = 6): C eps_dec=1: 0.51756 +- 0.00019, G = 0.648 +- 0.006 (n=3: 0.683); B eps_dec=2: 0.50743 +- 0.00011, G = 0.317 +- 0.004 (0.431); D eps_dec=3: 0.50245 +- 0.00019, G = 0.154 +- 0.006 (≈0.30). "The history matters, not only its end point."
- Controls for Test B: cap x10 (5e6): 0.50740 +- 0.00011 (shift -0.00003); finer grid N=600, N_mu=48: 0.50751 +- 0.00006 (shift +0.00008); pre-registered tolerance 0.0005. Cap control only at eps_dec=2 ("at eps_dec = 1 and 3 it is untested").
Section 4 "What does not set the threshold"
 1. First maximum of linear theory: shares 0.86, 0.59, 0.19, -0.05, -0.02, 0.00; largest error 0.50 [computed]. Centre factor 0.944.
 2. Sharp wall / rate ratios: eps_EP = 0.811 eps_dec^{3/4} for k r_m = 2; escape fractions k/(k+kappa), e^{-kappa/k}, 1 - e^{-k/kappa}; 32 combinations; wall variants miss by >= 0.14; with window from horizon entry every one misses by >= 0.17; one (e^{-kappa/k} averaged from eps_0) within 0.077 "selected from 32, it is not counted"; on Test B predicts 0.513 vs 0.317 [computed; measured].
 3. Diffusive escape: matches McCormick's curve to 0.02 with eps* = 4 but built after seeing it; free exponent fit 1.61 +- 0.03 not 3/2; Test A predicted 0.37-0.47 and 0.17-0.24, Test B 0.62: "Both are excluded" [measured].
 4. History-blind: Tests B, D would give 0.431, ≈0.30; got 0.317, 0.154; Test D misses by 0.146 vs kill line 0.08 [measured].
Section 5 memory form
- No fitted number, eps* = 1.7: 0.941, 0.860, 0.671, 0.344, 0.087, 0.013 vs McCormick's G; within 0.02 for eps_dec <= 1; largest error 0.103, "just outside the 0.10 bar set for it in advance" [computed].
- McCormick's curve passes G = 1/2 at eps_dec ≈ 1.67, within 3% of first maximum.
- g_2 with w = 0.89: largest error 0.022 [fit]. Not unique: k r_m = 2 fixed single-epoch misses by 0.093; best single epoch eps* = 1.87 misses 0.065; same w with k r_m = 2 misses by 0.115 (outside the 0.10 bar) [computed]. "The form is a fitted shape with a stated sensitivity, not a derived law."
- Pre-run predictions (file dated 13:47 on 30 October): C 0.663 vs 0.648 (miss 0.014; history-blind 0.683, miss 0.035); B 0.246 vs 0.317 (0.071; hb 0.431, miss 0.114); D 0.118 vs 0.154 (0.037; hb ≈0.30, miss 0.146). All memory-form misses inside the 0.08 kill line; history-blind fails at eps_dec = 3 [measured]. Readout window by neutrino flux and enclosed mass: "untested".
Section 6
- Exact elimination Eq (9) [derived; A.5].
- Matched-pair table R_ret at tau = 4 (eps_dec = 0.5) [computed]: tau_s/eps_dec = 0.1: 7e-15 (n3,l3), 5e-19 (n3,l4), 8e-24 (n6,l3), 5e-31 (n6,l4); 0.25: 6e-10, 6e-11, 2e-15, 7e-20; 0.5: 8.6e-3, 7.9e-3, 3e-6, 3e-6; 1: 0.081, 0.074, 0.094, 0.086; 2: 0.095, 0.085, 0.098, 0.088. "Every call came out as predicted." Survival law quantitative: n=3 ratio of entries at 0.5 and 1 is 0.106 vs e^{-8/3}/e^{-1/3} = 0.097; n=6 at 0.5: law 1.4e-6 vs 1.6e-6 at tau = 1.7. Planted in retained moments deep in coupling: order l = 1 > 2 > 3 > 4, each rung costing about 1e-4 ≈ k/sigma; after decoupling all four same size.
- Checks: 60 -> 120 moments and tighter tolerances change entries by <= 1.4e-5 of value; elimination from closed-form U_Q alone reproduces full difference to 3e-7 - 7e-7 (fourfold drop per step halving); leaving out the kernel misses by 19-234% [computed; B.14].
- Speed limit Eq (10) [derived; A.6; Lean]; largest ratio on computed trajectories 0.87 [computed]. "The bound limits how fast the kept sector can be emptied; it does not set the threshold."
- "No instantaneous closure on density, flux and stress alone can carry this memory." Whether realistic initial data carry such structure and how far it moves the nonlinear threshold: stated "untested" in sec. 6 (sec. 9 then tests the second in engineered form).
Section 7 [measured unless noted]
- r=1 changed code reproduces unchanged: delta = 0.5109 forms BH at eps = 6.61 in both.
- Admissible windows (Markov generator); minimum intensity stayed positive in all runs except one at r = 16 (-2.4e-10).
- Three pre-written readings: (a) frozen memory form predicts Delta G = -0.004 at r = 1/4, +0.003 at r = 4; (b) connection energy -> same-sign shifts; (c) reflection coefficient -> odd shifts. Outcome: shifts +0.183 (r=1/4) and -0.179 (r=4): "(a) fails by a factor of forty and with the wrong sign at r = 4, reading (b) fails on the sign, and reading (c) holds: the two shifts cancel to 0.004".
- Eleven thresholds (step-held rate, as in version 5): r, Gamma_12, (1/2)ln r, delta_c, G, tau_G - tau_G(1):
  1/16, -0.882, -1.386, 0.521485 +- 0.000038, 0.776, -1.547
  1/4, -0.600, -0.693, 0.516498 +- 0.000038, 0.614, -0.763
  1/2, -0.333, -0.347, 0.513656 +- 0.000010, 0.521, -0.384
  1/1.2, -0.091, -0.091, 0.5115145 +- 0.0000003, 0.451, -0.103
  0.8, -0.111, -0.112, 0.5116957 +- 0.0000004, 0.457, -0.127
  1, 0, 0, 0.510741 +- 0.000019, 0.425, 0
  1.2, +0.091, +0.091, 0.5100149 +- 0.0000005, 0.402, +0.098
  1.25, +0.111, +0.112, 0.5098407 +- 0.0000002, 0.396, +0.122
  2, +0.333, +0.347, 0.507973 +- 0.000010, 0.335, +0.385
  4, +0.600, +0.693, 0.505442 +- 0.000038, 0.252, +0.786
  16, +0.882, +1.386, 0.501673 +- 0.000025, 0.129, +1.610
- Line through the matched link: residual 0.014 in tau_G. Odd rates by |(1/2) ln r|: 0.091: 1.1006 [1.1000, 1.1011], even -0.003; 0.112: 1.1128 [1.1124, 1.1131], even -0.003; 0.347: 1.1093 [1.1052, 1.1134], even +0.001; 0.693: 1.1177 [1.1092, 1.1262], even +0.012; 1.386: 1.1384 [1.1332, 1.1436], even +0.032. "The rate is not one."
- Stage-correct reruns (bracket width <= 1e-6; half-widths 3-5e-7): r=1: 0.51077853, G 0.4266, change +3.8e-5; 1.2: 0.51000812, 0.4014, -6.7e-6; 1/1.2: 0.51151594, 0.4507, +1.4e-6; 1.25: 0.50984158, 0.3959, +8.8e-7; 0.8: 0.51169233, 0.4564, -3.4e-6; shear only 1.2: 0.50995463, 0.3996, +4.7e-7; shear only 1/1.2: 0.51157978, 0.4528, +5.0e-6. Stage fix moves BH formation at r=1, delta=0.5109 from eps = 6.6147 to 6.6176. New inner odd rates: 1.1066 [1.1061, 1.1072] (r=1.2 pair), 1.1102 [1.1098, 1.1106] (r=1.25 pair): pairs differ by 0.0036 (0.012 before). Shear-only at 1.2: 1.1928 [1.1922, 1.1933], 0.086 above all-l>=2.
- Error budget: fluid reference +-7.8e-5 (McCormick's archive) moves every rate by +-0.0038 together; joint refinement of r = 1.25 pair (N=600, N_mu=48, Courant numbers and Hubble step factor halved) raises thresholds by 7.5e-5 and 6.4e-5 to 0.50991687 and 0.51175643, rate -> 1.1020 [1.1016, 1.1024], shift -0.0082 "larger than the line of 0.005 set before the run"; budget 0.0097 in quadrature, 0.016 linear. Eq (11) odd rate = 1.11 +- 0.01, "the +-0.01 is now the error budget itself, dominated by resolution, and not a margin around a converged number." Third refinement level (N=900, N_mu=72) "had not finished when this version was closed, and with two levels convergence is untested. The rate is a measured number with no closed form attached."
- Shear only: r=1.2: 0.5099542 +- 0.0000002, G 0.400; r=1/1.2: 0.5115748 +- 0.0000002, G 0.453; odd rate 1.1895 [1.1892, 1.1898] (all l>=2 same pair: 1.1006). r=4: 0.5052350 +- 0.0000037, G 0.245; r=1/4: 0.5170942 +- 0.0000037, G 0.633; odd rate 1.2038 [1.2030, 1.2046] (all l>=2: 1.1177). "The link-weight reading fails by an order of magnitude at both pairs; the shear reading holds at both." "the moments above the shear, relaxed with it, pull the other way."
- Angular resolution (48 bins, r = 4, 1/4): 0.5054959 +- 0.0000082 and 0.5165576 +- 0.0000041 (rise 5.3e-5, 6.0e-5); odd rate 1.1177 -> 1.1170 [1.1156, 1.1184]; moves G by about 0.002.
- r=1 reference: G = 0.4253 +- 0.0006 (tolerance 1e-4), lower edge of McCormick's bracket [0.4253, 0.4367], midpoint 0.431. r = 1/4 with step shrunk fourfold: delta_c unchanged to 3e-6.
- Neutrino fraction R_nu = 0.2 (n=3, eps_dec=2, McCormick's instantaneous threshold 0.51297): 0.50396 +- 0.00003, G = 0.409 +- 0.005; memory form predicted 0.411; vs 0.425 at R_nu = 0.409, difference 0.016. "nearly, not exactly, independent".
- Intrinsic-ruler check [measured; B.17]: principal angle of kept-sector trajectory at first compaction maximum between ratio r and r=1: families' slopes in state angle differ by 5% (6% in rapidity); odd rates spread by 36% vs 3.4%; offsets linear residual 0.13 in the angle vs 0.014 in rapidity; state angle 0.0475 vs 0.0467 at r = 4 while thresholds differ by 8%. Least-damped eigenprojector unavailable: mode isolated only for k <~ 1.4 (about 36% of profile weight). "So the law is a law in the operator's own link rapidity, and not in the displacement of the linear kept state."
- Reading [H]: "The anisotropic stress carries the threshold... The threshold reads the direction of that mismatch, in the rapidity of the collision operator's flux-shear link, and not how much energy sits on the link."
- 3 November review check: step (collisions stop at eps_b = 1) delta_c = 0.513512 bracketed by 0.5132/0.5138; n=3 eps_dec=1.20 at 0.516797 bracketed by 0.5165/0.5171 [measured].
Section 8
- Kernel of G_T is zero; "The predictive quotient of this chain is therefore the whole hidden space, and what carries information is the spectrum of G_T" [derived; A.14]. "The Gramian is the standard observability Gramian of control theory, restricted to the hidden sector; what is used here is its meaning for the predictive quotient and its use in choosing what a reduced state must keep."
- Top three eigenvalues (n=3, eps_dec=2, readout to eps=4, profile-summed, +-k averaged): eps_s = 0.5: 1.1e-7, 9e-12, 1e-15; eps_s = 2: 0.367, 0.148, 0.040; eps_s = 3: 0.147, 0.024, 0.0016 (shorter horizon) [measured; Fig 7]. Leading direction always odd, led by l=3 (weight 0.92-0.99, rest mostly l=5); second always even, led by l=4. Halving time step: <= 3e-6; L = 90: no change at double precision. Coupled-era suppression 2.5e-9 vs survival e^{-42} (leak through conserved l=0 at order (k/sigma)^l); snapshot Gramian follows survival factor to within a factor of ten.
- Direction to plant (positivity edge, 32 bins): odd, weights l=3: 0.851, l=5: 0.117, l=7: 0.010; 2.47x the readout of pure p_3 on the decoupling surface; pure p_4 gives 0.40 [measured].
- Order with opacity fixed: six pairs (single-rate n=3 and 6; split operator r=4 and 1/4): density/flux/stress at readout differ by 33-72%, g_2 by 0.06-0.16 [measured; Fig 7]. "The rate falling late keeps more of the kept population than the rate falling early, in every pair whose window closes before the readout." Matching optical depth between n=3 and n=6 over [0.5, 4] leaves g differing by up to 0.74. "No scalar summary of the history, whether opacity, integrated connection energy or the operator at readout, can carry what the threshold reads; the order is part of the record. Whether the threshold itself separates such a pair is untested."
- Closures at linear order over nine histories [measured]: error to eps=4, worst at eps_dec = 0.25: P1 0.79, P2 0.50, P3 0.28, P5 0.071; linearised M1, M2 are exactly P1, P2; Chapman-Enskog worst (1.39); short-memory optimal-prediction correction beats P2 in all nine; exact elimination of l >= 3 exact to 4.6e-6; freezing kernel to one history costs up to 0.13. At eps* = 1.7 every truncation from P2 up gives memory form within 1e-3; by eps* = 4 miss by up to 0.26.
Section 9 [measured]
- Matched restart states agree: discrete l=0,1,2 to 4.4e-16 of c_0; energy, radial pressure, mass to 9e-16; flux to 1e-16 of energy; lapse 2e-15; constraint Gamma^2 - (1 + U^2 - 2M/R) to 7e-15; fluid and metric arrays bit-identical; hidden component differs by 0.08-0.17 of c_0. Uniform-in-radius perturbation dropped (moved central neutrino density by 91%).
- Unperturbed restart at eps_s = 2: delta_c = 0.5107500 +- 0.0000093.
- Eight thresholds (delta_c(+f), delta_c(-f), difference): eps_s 0.5 l=3: 0.5107685, 0.5107510, +1.75e-5; 0.5 l=4: 0.5107685, 0.5107500, +1.85e-5; 2 l=3: 0.5125833, 0.5088395, +3.744e-3; 2 l=3 N_mu=48: 0.5125134, 0.5090041, +3.509e-3; 2 l=4: 0.5096749, 0.5117726, -2.098e-3; 2 Gramian direction: 0.5134352, 0.5079300, +5.505e-3; 4 l=3: 0.5108796, 0.5106358, +2.44e-4; 4 l=4: 0.5106759, 0.5108241, -1.48e-4. Bracket widths 0.8-1.85e-5. At decoupling: 202, 204, 297 bracket widths, real. Coupled era: agree within two bracket widths "as predicted". Free streaming: 13 and 8 bracket widths but inside drift allowance - "by the rule written first they are not called real".
- +p_3 raises threshold by +1.83e-3 from unperturbed restart, -p_3 lowers by 1.91e-3; +p_4 lowers, at 0.56 of p_3 size (linear Gramian gave 0.40); Gramian direction moves threshold 1.47x pure p_3: "the predictive-quotient ranking of hidden directions carries into the nonlinear collapse, at about 60% of its linear size." Decoupling difference 3.5e-3 = 11% of McCormick's whole free-streaming shift and ten times the flux-shear link effect in his physical model.
- Coupled era not perfectly shut: paired runs separate in compaction by 1e5 times noise floor; ratio 48 vs 32 bins 0.86-0.89 (angular leak would give about 0.44); carries about 0.3-0.5% of the decoupling effect vs linear survival 5e-10; candidate (untested): fluid-frame shear and acceleration terms coupling l=3 to l=2, suppression about S/kappa per rung.
- Reading [H]: "The door is a window centred on decoupling..." "This is an engineered sensitivity, at half each cell's positivity margin, on one profile: whether cosmological initial data carry such structure at decoupling is a separate question, not answered here."
Section 10
- Eq (14) [derived; measured]: operator from his compiled right-hand side matches the diagonal to 3.6e-15, kappa_n part to 4.9e-15.
- r = 1 + kappa_n/kappa_e: 2.43-2.45 (nu_e), 7.69-7.77 (nu_mu,tau) between T_b = 0.3 and 5 MeV; inside the collapse at r = r_m, 1.7 <= eps <= 4, dominant group r = 7.9-8.6 (T_H = 1 MeV), 8.2-12.2 (0.51 MeV); link rapidity 1.03-1.25 vs window edge 0.20; kappa_e/H ≈ 0.02-0.04, kappa_n/H ≈ 0.16-0.27 at T_H = 1 MeV: "a large link rapidity on a weak link" [measured].
- delta_c^inst at T_H = 1 MeV with full equation of state (not in his archive): 0.53313 +- 0.00012 [measured].
- Pre-written readings: timing reading -> threshold stays 0.5194; link reading (frozen law, u_eff = 0.831) -> near 0.5204 +- 0.0003.
- Deciding run Eq (15): 0.51972 +- 0.00009 (T_0 = 10 MeV, six groups, N = 300, N_mu = 32); +0.00031 +- 0.00018 above his self-scattering threshold; strictly above (his 0.5195625 forms BH, here 0.519625 disperses). "neither reading: below the link line, just above the timing band. Most of what self-scattering does to the threshold is timing; the flux-shear split carries a real remainder, +0.0003 in delta_c, about a third of what the frozen law predicted and 4.5% of the whole self-scattering shift in G." Operator checks: -(kappa_e + kappa_n) diag(0,1,1,...) to 5.3e-15; energy conserved to 1.5e-16; momentum balance 1.5e-14; with kappa_n = 0 reproduces his code bit for bit to eps = 0.6.
- Recorder: thresholds with positive common-frame target in [0.51925, 0.51956] (T_H = 1) and [0.52475, 0.52513] (0.51 MeV); kept-share anisotropy 1 - A separates collapsing from dispersing run first, before eps = 3: about 0.85 in eps before peak compaction, 1.2-1.3 before v_L; v_L peaks ≈ 0.11 (1 MeV) and 0.16 (0.51 MeV) near eps ≈ 3.5, turns to infall after eps ≈ 5.3 [measured; Fig 10]. Whether the lead is causal: "what Section 9 tests, in the single-rate model."
Section 11 tests [computed; reading]
- Annihilation: c_s = 0.519 at T = 0.131 MeV; f reaches 1.135 at 1.6e7 Msun (c_s = 0.521); enhancement reading -> 7.5% shift, outside McCormick's envelope 5.3-6.2% ("that reading already fails"); reduction reading -> 5.5-6.3%; differ from unmodified 6.31% by +13.5% and -11.9%. Deciding run (same transport at fixed R_nu with p = e/3 vs full EoS at 3e6-1.6e7 Msun) listed by McCormick as missing.
- Mean of rates: arithmetic mean of group rates reproduces his calibrated decoupling temperatures 1.62 MeV vs 1.6 (e+- only), 1.02 MeV vs 0.93-1.0 (with nu-nu), mass step 2.53 vs 2.5-3; harmonic and geometric fail; mean of squares also passes - "the class of means is identified, not one mean".
Section 12: literature search to October 2026 found no other work on thresholds with free-streaming components, gradual kinetic decoupling in NR, switch-off timing, or shear/flux relaxation ratio. "what is new here is its [the Gramian's] use as the weight on the predictive quotient of VOTKP [6] and Dirac Time [7], and the test of its leading direction in the full collapse."
Lean: "The algebraic identities, the counterexample and every verdict's arithmetic are machine-checked in Lean (Appendix C)."

### 4B. Paper (b) (statuses from its own Appendix B claim table)
- Proposition 1 (two collision links), Eq (3): "Existing v5.1 identity, applied to declared plasma/self-scattering rates"; proof given. Caveats: scalar "does not make the scalar a sufficient predictor of collapse. It is dimensional, depends on k, and contains no ordering information about time-varying rates." Nonnegative self-scattering samples kappa_2 >= kappa_1 only.
- Predictive quotient: "Existing framework in recovered Dirac Time v3.0.1 and The Weight Between v1.1; connected to standard observability here". If a linear summary F determines every future output then ker F ⊆ N_inf, so rank F >= dim V_pred.
- Theorem 2 (Gramian realization of the quotient): ker G_T = N_inf for fixed finite L, any T > 0, W continuous positive-definite. Proved. "Positive weights affect the strength of visibility, not the exact invisible subspace. No convergent infinite-horizon integral is required. A semidefinite weight can discard additional outputs." Restricted kernel for embedding Q: z with Qz in N_inf. Time-varying generator: not covered without further hypotheses.
- Theorem 3 (no exact reduction of a connected finite chain): for (2) with k != 0 and density readout R = e_0^T, N_inf = {0}. "Proof in this manuscript; no numerical rank tolerance required". Limits: k = 0, disconnected chains, infinite hierarchies, nonlinear systems need separate statements.
- Theorem 4 (best rank-r linear preparation summary): E_r = sqrt(lambda_{r+1}); attained by first r Gramian eigenvector coefficients. "standard low-rank approximation principle [Eckart-Young] applied to the declared future readout. It is not an autonomous closure theorem or a wall-time improvement."
- Table 1 / frontier: "Computation here; fixed linear dynamics, norms and horizon".
- IQGT metric vs horizon (Eqs 10-12): "Computation applying established projector identities". Only a one-parameter metric; "No nonzero Berry curvature, flavor phase or gauge charge follows".
- VOTKP elimination (13)-(15): Schur-complement/hidden-response construction; "No identification with the elemental norm tree is required".
- Order cancellation Eq (16) and common continuation: "Exact transpose identity and finite-chain calculation".
- Proposition 5 (positivity-budget optimum): "Proof and computation for a conservative admissible set"; maximizing coordinate l = 3.
- Eq (22): complete local stress does not determine every future stress reading (derived in text).
- "New GR threshold or wall-time gain: Not established or claimed".
- Independent review file (in the zip) reproduces analytic metric 0.0025469832093294505, block-identity residual 8.67e-19, and warns that modes at ~1e-17 - 1e-19 cannot support exact-null claims; truncation convergence "empirical, not a certified infinite-chain error bound".

---------------------------------------------------------------------
## 5. Numbers (beyond those already tabulated in section 4)

### (a)
- PBH mass scale: heavier than about 1e6 Msun form while neutrinos decouple; beta -> beta^1.18 above 6e5 Msun (McCormick).
- McCormick Table II: G = 0.959, 0.867, 0.683, 0.431, 0.190, 0.063 at eps_dec = 0.25, 0.5, 1, 2, 4, 8. (Script B.6 uses 0.960, 0.868, 0.684, 0.431, 0.190, 0.063.)
- Run setup: pure radiation, R_nu = 0.409, N = 400 cells, N_mu = 32 angle bins, eps_0 = 0.1; rate cap kappa/H <= 5e5 (deviation from isotropy relative order H/kappa <= 2e-6); uncapped rate falls below cap at eps ≈ 0.11, 0.22, 0.34 for eps_dec = 1, 2, 3.
- Code line changed (B.2): kap = (1/(2*t))*min((eps_dec/(2*np.sqrt(t*t0)))**nexp, kapcap), nexp default 3, kapcap = 5e5.
- Memory curve (B.5 output; columns: n, eps_dec, g at first max 1.7, two-epoch g_2 with w=0.890): n=3: 0.25: 0.941/0.947; 0.5: 0.86/0.875; 0.75: 0.768/0.792; 1: 0.671/0.705; 1.5: 0.489/0.542; 2: 0.344/0.411; 3: 0.168/0.249; 4: 0.087/0.169; 6: 0.03/0.095; 8: 0.013/0.059. n=6: 0.5: 0.862/0.877; 1: 0.623/0.662; 1.5: 0.352/0.42; 2: 0.159/0.246; 3: 0.026/0.118; 4: 0.005/0.079.
- B.3 pre-registration (written 2026-10-30): Test A law dies if G(4) < 0.30 or G(8) < 0.13; null dies if G(4) > 0.28. Test B: diffusive 0.62, memory model ("Weight Between agent") 0.25, history-blind 0.43; each dies if measured G more than 0.08 away.
- B.4 run logs: reproduction 2026-10-30 ~14:25 CT, BH at eps 6.6146961105642985, 90 s; Test A eps_dec=4 bracket points 0.45325 dispersed / 0.45350 BH; eps_dec=8 0.44925 dispersed / 0.44950 BH; B: 0.50731 dispersed / 0.50754 BH.
- B.1 identity checks: I1-I5 all agree to 12 printed digits (e.g. I2 k=1, k1=0.3, k2=2.0: 0.800666666667).
- McCormick reference thresholds: Gaussian fluid 0.49773, inst 0.52832; broad alpha = 0.3: 0.44805, 0.47747.
- Lean/A.7 counterexample: R_00(1) = 32/37, R_00'(1) = -5/1369.

### (b)
- Model: d = 12 moments, k = 1, kappa_e = 0.2, kappa_nu = 0.4, T = 3 (time in units of inverse streaming frequency), 96-point Gauss-Legendre.
- sqrt(lambda_1) = 0.39872611 (full hidden-response operator norm).
- Gramian eigenvalues (results.json, all nine): 0.15898251090608095, 0.006972791020498613, 0.00010429318541654926, 8.17189269193274e-07, 4.322776920640164e-09, 1.6144573151765818e-11, 4.489525197204629e-14, 9.600195771557201e-17, 4.523762113430138e-19.
- Table 1 (adapted / sequential, % of sqrt(lambda_1)): r=0: 100/100; 1: 20.9425/42.1884; 2: 2.5613/15.6726; 3: 0.2267/4.9246; 4: 0.01649/1.3104; 5: 0.001008/0.2995. (results.json continues: 6: 5.314e-7 / 5.974e-4; 7: 2.457e-8 / 1.0546e-4; 8: 1.687e-9 / 1.6826e-5 as fractions.) Absolute errors: r=1: 0.083503 / 0.168216; r=2: 0.010212 / 0.062491; r=3: 9.0399e-4 / 0.019636; r=4: 6.5748e-5 / 5.2251e-3; r=5: 4.018e-6 / 1.1943e-3.
- Abstract headline: 3 adapted combinations -> 0.227%; 3 sequential -> 4.92%; five sequential needed to fall below 1%.
- Convergence: n=8/quad 96 first four: 0.1589825146802444, 0.006972783821398911, 0.00010429683988683682, 8.161349584419306e-07; n=12/48, n=12/192, n=20/96 agree with (9) to displayed precision.
- IQGT: leading gap lambda_1 - lambda_2 = 0.15200972; g(3) = 0.0025469832093 (analytic); centered finite differences at steps 0.04, 0.02, 0.01: 0.00254787269, 0.00254720560, 0.00254703881.
- Order example: eight moments, k = 1, tau = 0.8, rates A = (0.2, 0.4), B = (2.0, 1.1), initial vector e_0; plasma opacity integral 1.76, self-scattering opacity integral 1.20; final density difference 0 (results.json 0.0); Euclidean difference of first three moments 0.2819583387; third stage C = (0.7, 0.2), duration 0.8 -> density difference 0.0831015972. Densities meet at t = 1.6.
- Positivity: b = 0.25; leading Gramian direction: epsilon = 0.0621270, output norm 0.0247717 (absolute angular bound sum|f_l|sqrt(2l+1) = 4.024015384); pure P_3: epsilon = 0.0944911, output 0.0350135; guaranteed initial intensity >= 0.75. Single-moment signals under budget (l = 3..11): 0.035014, 0.013131, 0.0044852, 0.0013139, 3.2851e-4, 7.0974e-5, 1.3449e-5, 2.2649e-6, 3.4972e-7; best moment 3.
- ∫ mu^3 P_3 d mu = 4/35.
- McCormick increase quoted in (b) intro: "The approximately $0.235R_\nu$ increase concerns linear compaction in the studied pure-radiation regime" (number taken from paper.md; see section 8 note).
- "earlier measured slope near 1.11".

---------------------------------------------------------------------
## 6. Limits, failures and open items (as stated)

### (a)
- Test A changes profile shape together with collapse time: "it does not by itself separate the two, and it does not fix which earlier epoch does."
- Cap control untested at eps_dec = 1 and 3.
- Memory form: "a fitted shape with a stated sensitivity, not a derived law"; unfitted version misses its own 0.10 bar (0.103); weight w does not carry over between weightings (0.115). It "counts slightly too much of the early erasure". It "misses this [flux-shear] effect entirely".
- McCormick-suggested readout window (neutrino flux and enclosed mass between first maximum and apparent horizon): untested.
- Speed limit "does not set the threshold".
- Extreme pairs r = 1/16, 1/4, 4, 16 are "formal interventions on the solver" (outside Markov window); one run at r=16 reached intensity -2.4e-10.
- Odd rate: no closed form; +-0.01 is resolution-dominated error budget; joint-refinement shift -0.0082 exceeded the pre-set 0.005 line; whether the shift is from radial grid or time step: untested; third refinement level unfinished; "with two levels convergence is untested".
- The law measured inside 3/4 <= r <= 3/2 "does not carry linearly to r ≈ 8".
- Intrinsic displacement of the linear kept state does NOT carry the law (a negative result for the IQGT-style intrinsic ruler at linear readout): "the difference between the two collision models is written after the readout epoch, in the nonlinear collapse".
- Order pairs: "Whether the threshold itself separates such a pair is untested."
- Free-streaming restart (eps_s = 4) differences not called real (inside drift allowance). No sign was predicted for the restart thresholds.
- Coupled-era GR leak channel: mechanism candidate untested; radial-resolution dependence untested.
- Section 9 is "an engineered sensitivity ... on one profile"; whether cosmological initial data carry such structure: not answered.
- Deciding run matched neither pre-written reading.
- Bin values of c_0^2, c_1^2: "not proved here".
- Kept-share lead: "Part of the kept share's lead may be that it is second order in the anisotropy".
- Annihilation sign and mean-of-rates: stated as tests, not results.

### (b)
- No GR simulations; no PBH threshold claim; no wall-time gain claim.
- Collision-link scalar is not a sufficient predictor of collapse.
- Theorem 2 only for fixed generator; time-varying needs further hypotheses; several control histories must all be covered.
- Theorem 3: finite connected chain only.
- Theorem 4 is a preparation-summary (reconstruction with the full propagator), "not an autonomous closure theorem"; "A small reconstruction error does not bound a nonlinear collapse threshold." The 1% target "is not a preregistered physical accuracy requirement."
- Output norm weights orthonormal coefficients equally - "not equally scaled physical stress components".
- Eight-moment chain has small discrepancy in fourth eigenvalue; tiny eigenvalues not rank evidence.
- IQGT: one-parameter metric only; parameter is observation horizon, "not physical motion of a neutrino or quantum Fisher information"; small gap does not force divergence.
- Eq (14) "is not automatically an exact autonomous closure" for nonlinear GR.
- Order example "does not exclude all scalar encodings or prove different GR collapse thresholds"; "not a complete reversal of all three stages".
- Positivity guarantee concerns initial data only; (18) can be unnecessarily strict; Prop 5 is for the conservative weighted-l1 budget only.
- q/e = 4v/(3+v^2) only for boosted isotropic gas; one-way null beam has no timelike rest frame. "No particle-generation, SU(3), or flavor-mixing result follows from this transport display alone."
- 1.11 slope "under numerical recheck"; needed: stage-dependent rate evaluation and joint refinement; nonlinear matched-state restart must verify identical stress-energy, constraints, positivity, separated brackets widened by refinement drift. (Paper (a), dated later the same day, reports exactly these as done.)
- Not done: comparisons of actual evolution closures, physical multigroup instrumentation, held-out thresholds, cost benchmarks. "The present manuscript preserves the failed or limited statements with their causes: the reciprocal endpoint, full exact finite-chain observability, and the positivity-induced reversal of the leading-direction ranking."
- No VOTKP theorem number assigned; no fresh Lean build of this manuscript.

---------------------------------------------------------------------
## 7. Bearing on the four team themes

### 7.1 The predictive quotient and Dirac Time
- (b) quotes the Dirac Time organizing definition: "memory is information absent from the present reduced description but needed to distinguish admitted future observations" (Dirac Time v3.0.1, Definition 1.1 and Sections 2-5). "The predictive quotient separates exact indistinguishability from different descriptions of the same future."
- Formal object (b Eq 4): N_inf = ∩_j ker(R L^j), V_pred = V/N_inf; N_inf is L-invariant so "the quotient carries induced dynamics"; any sufficient linear summary F has rank F >= dim V_pred. (a): N_inf = {v : R U(tau,tau_s) v = 0 for all tau}; "the minimal summary that predicts the readout is the quotient V/N_inf (the predictive quotient of VOTKP, Theorem 3.1, and of Dirac Time, Definition 1.1)".
- Key finding for this chain: the quotient is trivial as a reduction - N_inf = {0}; "its exact predictive quotient retains every moment" (b); "The predictive quotient of this chain is therefore the whole hidden space, and what carries information is the spectrum of G_T" (a). So the paper moves from exact quotient to a WEIGHTED quotient: the Gramian spectrum ranks what must be kept at a declared tolerance, horizon and input class.
- "the declared future experiments [are] part of the definition rather than an implicit universal quantifier" (b).
- (a) tests the ranking in GR: Gramian leading direction moves the threshold 1.47x pure p_3; "the predictive-quotient ranking of hidden directions carries into the nonlinear collapse, at about 60% of its linear size."

### 7.2 Output-weighted Gramians (link to his Gram work)
- (b) Eq (5): G_T = ∫_0^T e^{L^dagger t} R^dagger W(t) R e^{Lt} dt with continuous positive-definite output weight W(t); Theorem 2 ker G_T = N_inf; weights change "strength of visibility, not the exact invisible subspace".
- (b) Eq (6): calG_T = K_T^dagger K_T is literally a Gram operator of the preparation-to-output map; singular values of K_T = sqrt of Gramian eigenvalues; Theorem 4 best rank-r summary error sqrt(lambda_{r+1}).
- (a) Eq (12): readout Gramian of the hidden sector (no W, time-dependent U). h* G_T h = ∫ ||R U Q h||^2. Positive definite for every T > tau_s even for time-dependent D (A.14) - (a) proves for the time-dependent case what (b) says needs "further hypotheses" (the hypothesis in (a) is smooth D(tau), tridiagonal streaming with nonzero couplings).
- IQGT link (b sec. 5): the leading Gramian eigenprojector P(T) has projector metric g(T) = (1/2)||P'||_F^2 = ||P P' Q_P||_F^2 (the "projector metric/coupling-block identity used in IQGT and The Weight Between"); eigen-gap formula (11). Parameter = observation horizon.
- The paper does not itself mention his earlier "Gram reduction" papers (e.g. the square-case/N=d+1 Gram work) - no such cross-reference is in either PDF. The link is structural only: G = K^dagger K.

### 7.3 A chain of linked units passing something from one to the next
- The whole model is exactly this: moments l = 0,1,2,... form a chain; "Streaming links each moment to its neighbours; collisions put a rate on each. Non-normality sits only where neighbouring rates differ" (Fig 1 caption). Link couplings c_l = (l+1)/sqrt((2l+1)(2l+3)); c_0^2 = 1/3, c_1^2 = 4/15, c_2^2 = 9/35; from the second link on adjacent weights differ by only 1.8%.
- Connection energy per link: k^2 c_l^2 (D_{l+1} - D_l)^2 - zero on a matched link.
- Each link as "one reflecting step" with Smith coordinate Gamma_ij = (d_i - d_j)/(d_i + d_j) = tanh(rapidity), rapidity (1/2) ln(d_i/d_j); odd under exchange of ends.
- Passing along the chain: observability entry (R B^j)_{2,2+j} = (-ik)^j c_2 c_3 ... c_{j+1} "collects only the path that climbs one rung per step" - product of link weights; (b) Thm 3 proof: column-j entry of e_0^T L^j "is the product of the first j upper off-diagonal entries of L".
- Loss per rung: leakage (k/sigma)^l through damped rungs; "each rung costing about 1e-4 ≈ k/sigma" deep in coupling; survival factor exp[-eps_dec^n/(n tau_s^n)] for the hidden block.
- Speed limit on transfer out of the first unit: (Adot)^2 <= 4 E_B A(1 - A), link weight k c_0 = sqrt(E_B).
- Continued-fraction response A.7: R_00 = 1/(s + k^2 c_0^2/(s + kappa_1 + k^2 c_1^2/(s + kappa_2))) - each link adds one level.
- Negative result relevant to any additive link rule: "A rule in which the offset moves by a sum of link-weight ratios times link rapidities" predicted |rate| < 0.1 for shear-only; measured 1.19-1.20: fails by an order of magnitude.
- Order matters along a time-chain of stages too: (b) Eq (16) two-stage density return is order-blind exactly (transpose symmetry), but the full state is not; (a) reversed-rate pairs differ 33-72%.

### 7.4 Several equal balls on a hyperbolic field with light/energy passing between them
- Neither paper places several balls or uses the word "hyperbolic". What IS present:
  - (b) sec. 9 "The Ball": a single velocity-ball display. Bulk point = subluminal velocity v_L of the zero-flux frame (Eq 21), inside the ball; "Individual massless momentum directions lie on the null boundary; these are distinct objects." "The Ball can therefore display equal initial bulk points alongside different angular data and different subsequent readings. A retained-share coordinate exceeding one is not a superluminal velocity." Boost law Eq (20); q/e = 4v/(3+v^2) only for a boosted isotropic gas; "A purely one-way null beam has no timelike rest frame."
  - (a) the disk language: link Smith coordinate Gamma = tanh(rapidity) in (-1,1); "The surviving share G is itself a point on the disk, Gamma_G = 1 - 2G, with offset tau_G = ln[(1-G)/G]"; measured law: offset tau_G moves 1.11 +- 0.01 per unit of link rapidity (1/2) ln r (not 1). Rapidity/tanh coordinates are the paper's own; calling the disk "hyperbolic" would be the reader's word, not the paper's.
  - (a) v_L measured in McCormick's multigroup runs: peaks ≈ 0.11 (T_H = 1 MeV) and 0.16 (0.51 MeV) near eps ≈ 3.5, turns to infall after eps ≈ 5.3.
  - Energy passing between kept and hidden: weight across the cut E_B = k^2/3, sqrt(E_B) = c_s k; elimination Eq (9)/(14) source + memory kernel; Eq (22) equal stress, different later pressure.
- Constraints these papers would impose on a multi-ball construction (my inference from the stated results, flagged as such): equal bulk points do not determine later readings (hidden l >= 3 data matter, led by l = 3, odd raises / even lowers); matched links pass without connection energy; transfer rate between a kept unit and its neighbour is bounded by 4 E_B A(1-A).

---------------------------------------------------------------------
## 8. Paper (a) Appendix B (evidence) and Appendix C (Lean): coverage and what they add

### 8.0 Coverage statement (exact)
- Pages 1-27 of (a) (a.txt lines 1-1499): read in full.
- Pages 27-118, Appendix B (a.txt lines 1500-7711): read through a FILTER, not line by line. The filter (reader's own script) dropped Python/diff CODE lines, plotting calls, and per-trial run-log lines ("delta=...: BH/dispersed"), and kept: every section heading, every "# SCRIPT:" header and comment line, all pre-registration texts (predictions, kill lines, appended RESULT blocks), printed output tables, and RESULT lines. 6281 lines -> 2283 lines read (file scratchpad/a_appB_prose.txt). So: code bodies of the scripts in B.5-B.25 are NOT READ line by line (B.1, B.2, B.5 scripts were read in full); some prose lines that the filter mistook for code were lost (visible as truncated sentences in B.19-B.23 below - marked "NOT READ (filtered)"). Per-trial bracket logs of the threshold searches: NOT READ except B.4.
- Pages 118-120, Appendix C (Lean statements): read in full.
- Typesetting glitch inside the PDF itself: in B.24 (A5 PREREGISTERED results, p.~112) the literal strings "</content>" and "</invoke>" are printed in the paper and the text just before the results block is cut ("=3 ed=0.25 0.9404/0.9467 vs ... the 0.001.)"). Some A5 result text is therefore missing from the PDF itself.
- The absolute path "/tmp/claude-0/.../a_wb/wb_steve_03_paper_objects.py ... RuntimeWarning: invalid value encountered in divide" is printed in B.6 output (a sandbox path and a numpy warning left in the evidence).

### 8.1 B.6-B.7: mapping "The Weight Between" v1.1 onto McCormick's preprint (scripts WB-STEVE-01..07)
- D2 = memory survival of the kept sector (the form used); D3 = "energy that has crossed into the hidden sector", X = sum_{l>=2} |F_l|^2/(2l+1); opposite runs: kept sector = l in {0,1}, and k r_m fixed at 2. Fitted-epoch scans (diagnostic only): best eps* = 1.87 (max err 0.065); other variants 1.69 (0.095), 1.84 (0.082), 1.77 (0.089); D3: 1.92 (0.112).
- WB-STEVE-07-HISTORY output file written 2026-10-30 13:47:53 -0500; Test B launched about 14:30 CT the same day.
- T0 (McCormick internal consistency): G recomputed from delta_c columns = 0.960, 0.868, 0.684, 0.431, 0.190, 0.063 (brief: 0.959, 0.867, 0.683, 0.431, 0.190, 0.063). shift/R_nu for C_l: 23.0-23.57 (spread 0.9%); for delta_c: 15.6-14.84 (spread 1.7%). Table III ratios 1.171-1.205. beta exponent 1.187-1.192. McCormick's delta_c table used: dec 1: 0.51865; dec 2: 0.51092; dec 4: 0.50354; dec 8: 0.49967; R_nu=.10: 0.50547; .20: 0.51297; .30: 0.52027; .488: 0.53379; alpha .3: 0.47747; alpha .5: 0.49682; alpha 2: 0.56342; alpha 4: 0.59734. Uses his Eq.(15) delta = C - 3C^2/8.
- T1 "Prop 5 / Def 4" of The Weight Between on McCormick's operator: E_B = ||P H (1-P)||_F^2 = k^2/3 = (1/2)||[H,P]||_F^2 = Var_{|0>}(H); connection-energy identity in the form (1/4)||[H',H'^dag]||^2 = ||[D,K]||^2 = S_2 with H' = -L = D + iK. T1 PASS: sqrt(E_B)/k = 0.577350.
- T2 hidden-walk (Schur) formula G_B(z) = [z - E - W (z-F)^{-1} W^dag]^{-1} equals g/(1 - kappa g): worst relative difference 5.29e-16. EP at kappa = 2k/sqrt3 = 2 sqrt(E_B).
- T3 "ladder" S_k (k = -2..2) on the single-rate model: S = {-2: 2.378601, -1: 2.140741, 0: 1.926667, 1: 1.734, 2: 1.5606}; S_0^2 = S_-2 S_2 and S_-1^2 = S_-2 S_0 are equalities (all gaps equal kappa). "rung +1: S_1 = E_B*2*kappa".
- T4 which rung is the effective single rate (power mean M_p, p in {-2..2}): rungs +1 (arithmetic) and +2 pass (both within 15%); mass ratio rung +1: 2.53, rung -1: 3.44 (McCormick 2.5-3). Group energy weights [0.004 0.038 0.229 0.528 0.199 0.003]; six groups x = 0.4..20.
- WB-STEVE-04-CHANNELS: C1 edge energies: relaxation model [1.1267, 0, 0, 0]; nu_e (flux 1, stress 1+1.5): edge 1-2 share 64.3%; nu_mu,tau (1, 1+7): 97.5%; flavour-weighted ratio (stress edge)/(flux edge) = 26.73. E_B for the cut P0 = k^2/3; for the cut P01 (flux kept, neutrinos as own fluid) = 4k^2/15; ratio 0.8000. E1: self-interacting neutrinos with no momentum exchange: first-max shift decreases monotonically with K0, shift*K0 constant to 1.2% between K0 = 100 and 1000 -> PASS (prediction from "rung -1", viscosity weight of the 1-2 edge S_-1 = (4/15) k^2/kappa).
### 8.2 B.8-B.12
- B.8 (OSL-STEVE-B, "Offset Speed Limit" mapping): KB1 |EP(N=2) - 2/sqrt3| = 5.06e-4; KB2 EP(N=200)/(2/sqrt3) = 0.559 -> the claim kappa_EP = 2 sqrt(E_B) does NOT survive in the full operator (kill line was within 10%).
- B.9 annihilation contest table (M_H, T_H, R_nu, c_s, f, baseline 0.15 R G, with f, with 1/f): 3e5: 0.713 MeV, 0.483, 0.5709, 1.015, 5.60%, 5.68%, 5.52%; 1e6: 0.398, 0.474, 0.5591, 1.043, 6.38%, 6.65%, 6.11%; 3e6: 0.240, 0.457, 0.5391, 1.091, 6.85%, 7.47%, 6.28%; 7e6: 0.166, 0.439, 0.5235, 1.128, 6.58%, 7.42%, 5.83%; 1.6e7: 0.118, 0.421, 0.5205, 1.135, 6.31%, 7.16%, 5.56%; 3e7: 0.090, 0.411, 0.5337, 1.103, 6.17%, 6.81%, 5.59%; 7e7: 0.061, 0.406, 0.5642, 1.031, 6.09%, 6.28%, 5.90%. KC0 validation min p/e = 0.2736 at T = 0.167 MeV (McCormick 0.274 at ~0.16) PASS. KC1 (enhancement) max 7.47% > 6.5% -> FAIL. KC2 (1/f) min 5.52% >= 5.3% -> PASS. Baseline (no f) range 5.60-6.85% vs envelope 5.3-6.2. (Main text quotes 7.5% and 5.5-6.3%; the main-text "c_s = 0.519 at T = 0.131 MeV" is not in the filtered table rows - NOT READ in the log.) M_H = 1.5e5 (T/MeV)^-2 (g*/10.75)^-1/2 Msun.
- B.10 linear first maximum (Ma-Bertschinger Newtonian gauge, scripts LIN-FS-01/03): printed rows edec 2: Delta shift -0.285, t_max 1.748; edec 4: -0.145, 1.737; edec 8: -0.022, 1.731.
- B.11 wall/rate-ratio table: EP crossing eps values [0.287, 0.482, 0.811, 1.364, 2.294, 3.859] = 0.811 eps_dec^0.75; 32 combinations with maxerr 0.077 (the one PASS: window 0.1-4, k r_m = 1, B exp(-kappa/k), uniform) up to 0.460.
- B.12 diffusive escape (K6-DIFFUSIVE-LEADER-G-CURVE): "STATUS DISCLOSURE: this model was written AFTER the Table II G column had been read"; l_diff^2 = c tau^5/(15 eps_dec^3); fits: A_fit = 3.811 (c-equivalent 1.03) max err 0.022; e*_fit = 4.043; "KILL (exponent): n=1.5 is 3.4 sd from fitted n".
### 8.3 B.13 (Tests C, D, controls; pre-registration written 2026-10-31T17:09:37Z)
- Frozen predictor: "kept-sector memory model, two-epoch weight w=0.890 (fitted on n=3 only)", values from memory_curve.json (written 2026-10-30 13:47 CDT, never refitted). Test C kill: |G - 0.6625| > 0.08; Test D kill: |G - 0.1176| > 0.08; history-blind 0.683 and 0.30.
- Final brackets: Bcap2 [0.50729, 0.50751]; Bres2 [0.50746, 0.50757]; C [0.51737, 0.51775]; D [0.50226, 0.50264]. Cap released at eps ~0.153 (cap 5e6 run), 0.224, 0.112, 0.337.
- Lean (App. C item 6): G_B = 970/3059, G_C = 1983/3059, G_D = 472/3059.
### 8.4 B.14 witness (pre-registration 2026-10-31T17:12:31Z)
- Model: dv/dtau = -(ikM + sigma(tau)(I-P0)) v, M_{l,l-1} = l/sqrt(4l^2-1), sigma = eps^n/tau^(n+1); 36-node Gauss-Legendre k in [0.25, 9], weight k^2 exp(-k^2/2); eps_dec = 0.5; tau_s in {0.05, 0.125, 0.25, 0.5, 1.0}; positivity checked on 2001-point mu grid (minima 0.501-0.578); delta = 0.05.
- Kill/success conditions K1-K6 (K6: speed bound violated if ratio > 1 + 1e-6). Logged "bound" columns: first number (largest ratio along the pair's trajectories) 0.789-0.872; a second column "bound_worst_N" shows 1.000001/1.000002 and 1.4796 for n=6 at tau_s/eps = 0.1 - the meaning of that second column (normalised variant) is NOT READ (code filtered); main text states the largest ratio is 0.87.
- Kernel check JSON: rel_err 4.7e-6 -> 1.19e-6 -> 2.96e-7 (h = 0.004, 0.002, 0.001) for (n=3, ratio 1, L=3, k=2); src_only_rel (leaving out the kernel) 1.99, 1.26, 2.34, 0.188 -> "19-234%".
- Raw witness rows give R at tau = 1.7 / 4.0 / 6.0 for plants in l = 1,2,3,4 (e.g. n=3, tau_s/eps = 1, l=3: 4.654e-2 / 8.123e-2 / 1.052e-1).
### 8.5 B.15-B.19 (Section 7 evidence)
- Pre-registration file code/v4_runs/PREREGISTERED_V4.txt is "in the archive and on GitHub" (not printed in full). McCormick's ms_nuc.py is MIT-licensed. Run tags: F2_r1o16, F_r025, J_r05, A1_all_r083, K_r08_clean, H1_r1, A1_all_r12, K_r125_clean, J_r2, F_r4, F2_r16.
- Shear-only offsets: r=0.25: G 0.6330, shift -0.8462; r=0.8333: 0.4526, -0.1107; r=1.2: 0.3996, +0.1061; r=4: 0.2453, +0.8227.
- B.17 PREREGISTERED_RULER (written 2026-11-05): the question "are the measured threshold offsets a law in the kept sector's own geometry (IQGT, Paper I Sec. 4: 'the parameter manifold does not generate the geometry') rather than in the parameter" chart. Object: L(r) = -ikM - kappa D_r, 61 moments; Riesz projector Pi_r = |R><L|/<L|R> onto the least-damped eigenvalue. Rulers: (a) arc length of the Hermitian pullback metric g_rr = (1/2)||dPi/dr||_F^2; (b) chord d_HS = ||Pi_r - Pi_1||_F/sqrt2; (c) "his biorthogonal trace form q(V) = (1/2) Re Tr V^2 with V = dPi/dr [cone / B57: may be <= 0]"; (d) principal angle; later (e) principal angle between kept-sector trajectories v_r(tau*) and v_1(tau*). Scale: kappa = eps_dec^3/tau^4 = 8/1.7^4 = 0.958 at eps* = 1.7.
  - RESULT 1: chart baseline all-higher slope 1.1328, rms 0.0142, spread 3.39% (2.90-3.87); shear-only slope 1.2036; ratio 1.0624 (1.058-1.067). Rulers (a),(b),(d): R1 DIES (ratios 1.27, 0.67, 0.73), R2 DIES (spreads 195%, 255%, 201%). Instrument finding: least-damped eigenvalue isolated only for k < 1.4; Petermann factor 374 at the transition; q indefinite along the path (-1e2 .. +4e3). Gamma_12 chart: spread 53%, ratio 0.877.
  - RESULT 2 (ruler e): tau* = 1.7: slope 21.20 rad^-1, rms 0.130; odd rates 16.7 -> 23.4, spread 35.9%; shear-only slope 20.07; ratio 0.9465 -> R1 DIES, R2 DIES. tau* = 4.0: ratio 1.668, spread 22%. Memory-form A0 log-odds as ruler: ratio 0.885/1.84, spread 40%/97%.
  - VERDICT: "R3 for both rulers tried"; "The chart x = (1/2) ln r = (1/2) ln(kappa2/kappa1) remains by far the most linear description"; "the threshold's offset tracks the rapidity of the damping OPERATOR's flux-shear link (B189: ln(kappa2/kappa1) is a property of D, not of a state)"; "other projectors (the full angular moment set of the collapse run, the nonlinear state at the horizon) and other readout epochs remain open and are not run"; "No rate constant is claimed." CORRECTION 2026-11-05: weight share k < 1.4 is 0.362 (not 15%).
- B.19 A1 (written 2026-11-11T14:05Z): Tests S1, S2, S3, control C1, kill lines as in main text. S3 refined pair: one point (0.51175620) "never ended" - reported undecided; 0.4-point 0.51175608 dispersed. Shift corner range [-0.0090, -0.0074]. C1: v5.1 runner at r=1 gives 0.51075683 [0.51075657, 0.51075709]; of +3.78e-5, +2.17e-5 is the stage fix, +1.61e-5 the v5.1 midpoint offset. Solver: McCormick ms_fluid.py at commit 41a0f83; Courant 0.4/0.4, cH = 0.005; "ONE simulation process at a time (house rule)". Several crash-then-retry events logged (min I ~ 1e-9).
### 8.6 B.20-B.22 (Section 10 evidence, tasks A2, A2b, A3; all written 2026-11-11T14:04-14:09Z)
- A2 disclosure: McCormick single-rate thresholds at T_H = 1 MeV: Tdec 0.75: 0.51586; 1.0: 0.52076; 1.5: 0.52583; 2.0: 0.52837; 3.0: 0.53065. Stand-in delta_inst 0.53379 (later measured 0.53313, stand-in high by 0.00066).
- Reading 1 weighting: link rapidity u_s(t) = (1/2) ln r_s(t) averaged over time with the visibility of the flux link g_s = (k_e,s/H) exp(-tau_e,s) per d ln a, and over groups/flavours with background energy weights (flavour 1/3, 2/3). "The rapidity is averaged (not r), because the v5.1 law is linear in the rapidity." Kill: wrong sign or |pred - meas| > 0.5 |meas|.
- Predictions (stand-in d_inst): G(without) = 0.7965; rate 1.11 -> G(with) = 0.6087, shift -0.1878, delta_c(with) = 0.51956 (measured 0.51941 +- 0.00016; miss +0.00015) SURVIVES; rate 1.19-1.20 -> 0.51898-0.51891 SURVIVE. Reading 2 (timing): Tdec_eff = 1.552 MeV without nu-nu, 0.979 MeV with; predicted shift -0.1576 (miss 17.9%) SURVIVES. With measured d_inst = 0.533125: measured G 0.8114 -> 0.6158, shift -0.1956 +- 0.0053; rate 1.11: 0.51995 (miss +0.00054); rate 1.19: 0.51939 (miss -0.00002); timing shift -0.1606.
- Operator check output: k_e = 0.7 test: eigenvalues one at -1.6e-16, one at -0.7, 30 at -(k_e + k_n). Discrete energies at N_mu = 32: 4.589752832 vs continuum 4.60694 (rel 3.7e-3); 64: 9.3e-4; 128: 2.3e-4; 1024: 3.6e-6.
- A2b deciding run: kill lines: > 0.5199 favours link law; 0.5191-0.5197 favours timing; else neither. Log: 0.52000 BH (eps 6.10) | 0.51850 dispersed | 0.51925 dispersed | 0.519625 dispersed (6.23) | 0.5198125 BH (7.20). T_H = 1.0029 MeV. Shift +0.00006 to +0.00056, midpoint +0.00031. G(r1) = 0.6245 vs G(nnmode0) = 0.6158: "r1 undoes 4.5% of the full nu-nu shift in G; it recovers 31% (25% anchored) of the move the link law predicted for r1 (0.5204), and 4.7% of the move given by the tau route (removing u_eff = 0.8313 at rate 1.11 predicts 0.5260)". Run 2 log: 0.533 dispersed | 0.535 BH | 0.534 BH | 0.5335 BH | 0.53325 BH.
- A3 recorder (nnmode = 1, positive target): speed-limit ratio R_SL = (dA/dtau)^2/(4 E_B A(1-A)) with E_B = 1/R(r_m)^2 (k = sqrt3/R(r_m)); "The bound's hypotheses (one Fourier mode, flat space, ||v|| non-increasing) do not hold in the GR model, so R_SL > 1 would not be a violation; it is a reading." Prediction (i) (first 1% separation between eps 3.0 and 5.5, v_L and 1-A within 0.5 of each other): KILLED - 1-A separates before eps = 3.0 at both T_H (2.907, 2.926); v_L 4.095; A itself 4.157; Cmax 3.645; v_L and 1-A separate 1.32 and 1.17 apart. Prediction (ii) (dominant group nu_mu,tau, r outside [0.75, 1.5]): SURVIVES; stated ranges 6-9 and 2.2-2.8 too narrow at T_H = 0.51 (up to 12.1 and 3.39). Runs: T10_lo 0.51925 dispersed eps 6.295; T10_hi 0.5195625 BH eps 6.139; T5_lo 0.52475 dispersed eps 6.052.
### 8.7 B.23 restart test (task A4, written 2026-11-11T14:04Z)
- "PREDICTIONS (from Jeromie's matched-pair witness: survival exp[-(eps_dec/eps_s)^n / n])". P1: at eps_s = 2 |diff| > 3w; P2: at eps_s = 0.5 |diff| <= 2w; opposite reading: collapse washes out l >= 3. "SIGN: Jeromie's corpus does not give the sign of a threshold shift from hidden l=3 structure. The P3 slab result (audit: d/dt (P_r+ - P_r-) = -(4/35) e a') ... NO SIGN IS PREDICTED." (This slab formula is the same as (b) Eq 22.) Magnitude lean: order 1e-4 (measured 3.7e-3).
- Uniform-a linear check: differs by 91% of base at eps 2.5 -> "measures a centre artefact, not the hidden-moment door. It is NOT used for any threshold verdict."
- Design additions D1-D6: third epoch eps_s = 4.0 (survival e^{-1/24} = 0.96, witness R_ret 0.095 (l=3), 0.085 (l=4)); D2 bump perturbation; D3 matched checks; D4 screen at deltas 0.5100 and 0.5115 with selection rule (outcome flip or separation > 10x noise floor); D5 REAL rule (brackets widened by refinement drift); D6 Gramian direction from A5 ("ed2_n3_s2_T4 / Linf_optimal; odd; l-weights 3:0.851 5:0.117 7:0.010; max|d| = 1"), prediction P4 ratio d/p_3 > 1, lean 1.5-3 (A5's linear chain 2.47).
- Screen (2.0, l3): outcomes flip at both deltas; linearised estimate +4.3e-3. Screen d: ratio d/p_3 1.51-1.68; linearised +6.6e-3.
- Trisections with brackets: (2, l3, +f) 0.5125833 [0.5125741, 0.5125926]; (2, l3, -f) 0.5088395 [0.5088313, 0.5088477]; N_mu = 48: +f 0.5125134 (drift 7.0e-5), -f 0.5090041 (drift 1.65e-4); widened brackets disjoint (gap 3.40e-3) -> REAL. "a difference can be REAL only if it exceeds about w + 2 d_K = 3.5e-4." d: +f 0.5134352, -f 0.5079300 (297 w) REAL; ratio 1.47 ("inside the lean 1.5-3 only at its edge"). f = 0: 0.5107500 [0.5107407, 0.5107593]. (0.5, l3): +1.75e-5 = 0.95 w, P2 PASSES, not REAL; "A residual of ~0.5% of the eps_s = 2 shift is consistent with every number here; the survival law alone predicts ~5e-10 of it. At this bracket and drift resolution it cannot be told from zero." (4, l3): +2.438e-4 = 13 w, 6.5% of the eps_s = 2 shift, not REAL; P3 NOT PASSED ("fails only on the drift allowance ... a drift measured on this pair is untested"). (2, l4): -2.098e-3. (0.5, l4): +1.85e-5 = 1.0 w. (4, l4): -1.482e-4 = 8 w, not REAL.
- Summary: P4 PASS; opposite reading KILLED by the eps_s = 2 pairs; "odd directions oriented like +p_3 raise the threshold; +p_4 lowers it."
### 8.8 B.24 Gramian, order swap, closures (task A5, written 2026-11-11T14:10Z)
- Prior-art note inside: "4 web requests spent ... The two papers were NOT read this session." (i.e. the optimal-prediction papers were not read when OP2 was built; "the 'crescendo' form I recall from optimal-prediction closures -- recalled, not read").
- Gramian as computed: G(s,T) = ∫_s^T Q^T Phi(t,s)^T R^T R Phi(t,s) Q dt, R = rows l = 0,1,2, Q = embedding of l >= 3, T = 4; computed per k, parity-symmetrized (G(-k) = P G(k) P, P = diag((-1)^l)), profile-summed; real basis w_l = i^l v_l. Also terminal (snapshot) Gramian = the witness's R_ret object.
- P2a confirmed (Kalman matrix full rank; smallest singular values 1e-29..1e-11; "G eigenvalues below ~1e-19 are round-off"). "There is no exact predictive quotient smaller than the full hidden space; the quotient that matters is numerical (eigenvalues of G above a tolerance)."
- P2b KILLED for the integral Gramian: coupled/transition top ratio 2.5e-9 (n=3, ed=0.5) vs predicted ~e^{-42} = 6e-19; n=6: 5e-27 vs e^{-1365}; cause: leakage (k/sigma)^l into conserved l=0. Terminal Gramian ratio 4.8e-17 within 10^1.1 of the survival factor.
- P2c HOLDS: top eigenvector odd, l=3 weight 0.919, 0.923, 0.918, 0.922, 0.953, 0.990.
- P2d KILLED: effective rank (eigenvalues > 1e-3 of top) free < transition: 8 vs 9 at ed = 0.5, 3 vs 5 at ed = 2 (confounded with shorter horizon).
- Order swap: family R = time reversal inside window W (R5/R6 = split r = 4, 1/4); family S = n=6 vs n=3 rescaled to equal optical depth. P1a-c confirmed (scalar summaries blind). P1d HOLDS for every pair: R_diff 0.33-0.72; |dg| 0.009-0.184; dg_2: R1 -0.064, R2 -0.107, R3 -0.118, R4 +0.161, R5 -0.063, R6 -0.067. Family S: ∫sigma^2 of the n=6 member is 2.09-2.15x the n=3 member's. Two "lean" expectations FAILED (reversed member keeps MORE, not less; family S lean failed in 5 of 6 late-window cases).
- Closures: comparators P1, P2, P3, P5, M1, M2, CE2 (v_2 = -ik c_1 v_1/sigma), OP2 (dv_2/dt += -k^2 c_2^2 theta(t) v_2, theta = ∫ exp(-∫ sigma) dr), MFe (exact block elimination, cut at l = 2|3), MFf (frozen kernel, reference n=3, ed=2). P3a-P3e HOLD (M1 closed moment = 0.3333 eps^2, M2 0.300 eps^2 as eps -> 0; MFe max E_traj 4.6e-6; smallest instantaneous-closure E_traj at ed <= 0.5 is P2 0.433). Lean "OP2 loses for early decoupling" FAILED: OP2 beats P2 in all 9 (ed = 0.25: 0.247 vs 0.496).
### 8.9 Appendix C (Lean statements) - read in full
- Lean 4 with Mathlib (v4.34.1), repository github.com/dicipler-pixel/neutrinos-leave-lean, build at commit c372d3f (4 November 2026): compiles every module, replays every proof in an independent kernel checker, all 100 theorems use only standard axioms (propext, Quot.sound, Classical.choice), all twelve false controls rejected. "Lean checks the finite moment model and the verdict arithmetic. It does not check McCormick's code, the collapse runs, the classification of runs near threshold, the bracket edges (inputs copied from the run logs) or the numerical witness."
- Statements: 1 crossLink, crossLink_sq (A.6). 2 twoMomentConnectionEnergy. 3 splitRateEnergy (three-moment L). 4 shearCounterexample: R_00(1) = 32/37, R_00'(1) = -5/1369, dE/dkappa_2 = 0 at kappa_2 = kappa_1; closed form of the 3x3 resolvent entry 2(15 kappa_2 + 17)/(35 kappa_2 + 39) for kappa_2 > -1. 5 scalarCollisionPropagator e^{t(X - sigma I)} = e^{-sigma t} e^{tX}. 6 testB/C/D verdict (970/3059, 1983/3059, 472/3059). 7 gam_inv, odd_part_free_of_anchor. 8 cSq_zero/one/two, weight_ratio_01, weight_ratio_12. 9 testK_clean_range etc.: at r = 1.25 vs 0.8 the odd rate lies in [1.112, 1.114] over the whole bracket pair; plus controls showing a failed run used as a bracket edge "would have decided wrongly". 10 testJ_straddles: r = 2 odd rate straddles 1.108, at most 1.128. 11 selfScatterEnergy (+_ab, _no_nn) "new in version 6, module Neutrinos.SelfScatter": (1/8)||[L,L*]||_F^2 = a^2 kappa_e^2 + b^2 kappa_n^2 for any streaming weights; discrete weights and diagonalisation of McCormick's operator NOT checked in Lean. 12 testL_rate_ge_six_fifths, testL_rate_le: shear-only odd rate lies in [1.2, 1.21] (the r = 4 pair).
- Note: the Lean build date (4 November) predates v6; the v6 stage-correct numbers (1.1066, 1.1102, 1.1928, restart thresholds, deciding run) are not listed among the Lean verdicts; only item 11 is flagged new in v6.

### 8.10 Cross-check between the two PDFs (reader's observation)
- (b) was created 08:29 CST; the pre-registrations for (a)'s v6 runs are stamped 2026-11-11T14:04-14:10Z = 08:04-08:10 CST, and their results 14:50Z-20:45Z (08:50-14:45 CST); (a) was compiled 14:55 CST. So (b) was written while (a)'s v6 runs had been registered but before their results; (b)'s list of what "must" be verified (stage-dependent rates, joint refinement, matched-state restart with drift-widened brackets) is what (a) then reports.
- Shared items: v_L formula; slab identity -(4/35) e a'; observability by the product of link weights; leading direction led by l = 3; positivity as the limiter of which direction to plant.

### 8.11 Second pass over Appendix B (recovered prose/output lines the first filter dropped)
A second filter recovered 140 further prose/output lines (scratchpad/a_appB_lost.txt), all read. After both passes what remains NOT READ line by line in (a) is: the bodies of the Python scripts and solver copies in B.5-B.25 (code statements only), and the per-trial "delta=...: BH/dispersed/crash" lines of the threshold-search logs outside B.4. All prose, pre-registrations, kill lines, appended results and printed result tables were read.
- B.7 E1 table (self-interacting neutrinos, no momentum exchange): K0 = 3: first-max ratio 0.96022, implied threshold rise 4.1424%, rise*K0 = 12.427; 10: 1.7192%, 17.192; 30: 0.6345%, 19.035; 100: 0.1969%, 19.688; 300: 0.0662%, 19.849; 1000: 0.0199%, 19.918; 3000: 0.0067%, 20.088. With drag on the plasma included (McCormick's relaxation model): 4.2421% (12.726), 1.7488%, 0.6396%, 0.1974% (19.743), 0.0664%, 0.0200% (20.042), 0.0067% (20.210).
- B.8: least-damped eigenvalue becomes real (and stays real) for kappa >= 1.1552 (N=2), 0.7552 (N=10), 0.6719 (N=40), 0.6455 (N=200); N=3 and N=5 print 0.0100 (the scan floor). Least-damped lambda vs diffusion estimate -k^2/(3 kappa): kappa=1.0: N=2 -0.5000+0.2887i, N=200 -0.3579 (estimate -0.3333); kappa=2: -0.1835 / -0.1695 (est -0.1667); kappa=6: -0.0561 / -0.0557 (est -0.0556); kappa=0.5: N=200 -0.4947-0.0078i (est -0.6667).
- B.10: instant-decoupling row "edec None Delta shift 5.962, dpl shift 6.663, tmax 1.711 / 1.744".
- B.12 prediction for alpha = 0.3 from the diffusive law (later excluded): {0.1: 0.995, 1: 0.854, 2: 0.674, 4: 0.422, 8: 0.205, ...}.
- B.14 pre-registered extras: "n=6 suppresses more than n=3 at the same tau_s/eps for tau_s<eps, less (closer to 1) for tau_s>=eps"; "Opposite check: deep in coupling L=1 > L=2 > L=3 > L=4 (one factor k/sigma per rung)".
- B.17: "PRIMARY projector := the Riesz projector onto that pair (rank 2 when complex, rank 1 when real)"; ruler (e) "is Paper I Sec. 10's own instrument (raw data -> intrinsic angles): gauge-free, scale-free, needs no isolated eigenvalue"; sensitivity kappa = 0.3, 3.0 (reported, not used for verdicts); C1 control: theta read in x gives family ratio 1.1455, odd spread 28.00% (tau* = 1.7); 0.7429, 26.67% (tau* = 4.0).
- B.19: regression r = 1, delta = 0.5109: v5.1 runner BH at eps = 6.6147, stage-correct 6.6176 (move +2.9e-3 in eps). S3 refinement: N = 600, N_mu = 48, cH = 0.0025, Courant 0.2/0.2. The expectation "each threshold moves < 2e-5" "FAILED at r = 1 (+3.8e-5); not a kill line (the anchor cancels from the odd rate) but it is flagged". "The stage fix still moves r = 1 more (2.2e-5) than any inner threshold (0.9-6.7e-6). No effect on any odd rate." Shear-only r = 1.2 search: "one point crashed twice".
- B.20: McCormick's archive has instantaneous thresholds (res_eos_fs) only for T0 <= 5 MeV, T_H <= 0.506 MeV; stand-in delta_inst = 0.53379 is his pure-radiation R_nu = 0.488 value; k_e,s is identical in his two runs (with/without nu-nu).
- B.21: Run 2 used "kind 'fs', T0 = 10, his defaults N = 400, K = 32", to +-2e-4, no kill line.
- B.22: recorder runs nnmode=1, mode=phys, G=6, x 0.4-20, N=300, K=32; cells: centre cell i=0 and the cell nearest r = r_m = 1 (i=95); moments p_l, l = 0..4 by Gram-Schmidt on 32 midpoint bins; separation definition: first record where |X_BH - X_disp| > 0.01 * running max |X_disp|; "Caveat fixed now: with nnmode=1 the nu-nu target is a common boosted frame, so k_n leaves only the total momentum alone, not each group's dipole; D=diag(0,k_e,k_e+k_n,...) is exact for nnmode=0 and for the gas as a whole." T5_hi 0.525125 BH eps 6.339. At T_H = 0.51 the metric tripped at the first record (eps = 0.100) where both X = 0 to roundoff - "a definition failure of my metric, reported as such"; that record excluded.
- B.23: restart diagnosis of the uniform-a artefact: "a regular l-th angular moment vanishes like r^l", and at the centre cells streaming across one cell is as fast as collisions, so (k/sigma)^l ~ 1 at grid scale. m_i = min over sign and bins of I_ik/(Ibar_i |p_l(mu_k)|). "Between 2w and 3w at eps_s = 2: inconclusive, reported as such." Screen at delta 0.5100 (2, l3): f=0 dispersed@6.03 (same as no-restart run); +f dispersed@5.47; -f BH@5.55. "at eps_s = 0.5 the separation is ~1e5 x the noise floor, and the estimate (1.3e-5 for l3) is ~3e-3 of" the decoupling shift. p_4/p_3 |shift| ratio 0.56 at equal positivity margin. Gramian direction has code label l = -1.
- B.24: plant epochs for the witness history ed = 0.5: s = 0.125, 0.5, 1.0 (coupled / transition / free); real basis generator kK - D with K real antisymmetric; "P1 truncation at l=1 (v_2 := 0). This is ALSO the linearized M1 closure: Levermore / Minerbo / maximum-entropy"; MFf "Defined here as the analogue of fitting once and freezing"; P3c worst case is the earliest decoupling n=3, ed=0.25 "(longest free streaming)".
- Figure titles in the v6 figure script: "Same density, flux and stress; different hidden angular structure"; "Odd structure raises the threshold, even lowers it"; "Self-scattering lowers the threshold mostly through timing; the flux-shear split carries +0.0003"; "Equal optical depth and equal connection energy, different order: the memory form tells them apart".
- Figures themselves (Figs 1-10 of (a); 3 figures of (b)): captions read; the images were NOT viewed.
