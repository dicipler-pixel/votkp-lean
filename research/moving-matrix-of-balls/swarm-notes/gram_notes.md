# GRAM paper notes — "The Square Case" (ladder_v4.pdf)

Source: Google Drive file 18JIlXFlAtZYFmLOoRR5eSgK7fjzmgMGc, "ladder_v4.pdf". Read two ways: Drive text reader (all 18 page markers present, not cut short) and the downloaded PDF run through pdftotext -layout (18 pages, 974 lines). Local copies:
- /tmp/claude-0/-home-claude/f86429e3-e32f-50e6-b1fd-fcadab5264af/scratchpad/swarm/dl_gram/pdf1/ladder_v4.pdf
- /tmp/claude-0/-home-claude/f86429e3-e32f-50e6-b1fd-fcadab5264af/scratchpad/swarm/dl_gram/pdf1/ladder_v4.txt (layout text; line numbers below refer to this)
Pages read: 18 of 18. Companion zip (Square Case v3) NOT opened — the PDF left nothing unclear enough to need it. The scripts VERIFY-LADDER-1/2/3 are named in the paper but their code is NOT in the PDF: NOT READ.
Figures: three figures. Read from caption + extracted labels only; the plotted curves themselves were not inspected as images.

Where I rebuilt broken extraction it is marked [rebuilt].

---

## 1. What the paper is

- Title as printed: "The Square Case: Gram Reduction and Spectral Transport for N = d + 1 Bodies"
- Author as printed: "Jeromie N. Beasley" (the PDF prints the middle initial N.)
- Date as printed: "August 2026". PDF metadata creation date: Sat Aug 8 2026 05:38:29 CDT. pdfTeX, 18 pages, letter.
- Version: NO version number is printed anywhere in the text. "v4" is only the filename. Internally the paper has three verification passes (Appendix B: first pass, "Second pass", "Third pass"), which is the only in-text sign of versions.
- Sections: Abstract; 1 Introduction; 2 The square case and the Gram reduction (2.1 Setup, 2.2 Orientation and the branched double cover, 2.3 d=2: the shape sphere, with its radius, 2.4 Two metrics, and which one is which); 3 Stratification (3.1 Rank strata, 3.2 Collision loci have codimension d); 4 The canonical tangent splitting; 5 The transport operator (5.1 The operator uses no metric, 5.2 The operator is diagonally similar to a symmetric one); 6 The spectrum (6.1 The boundary: pinning and exceptional points); 7 What T is; 8 Where the ladder ends; 9 Reconstruction; 10 Discussion; 11 The volume structure (11.1–11.8); Appendix A Wall vectors at d=3; Appendix B Verification; References [1]–[14].
- One-line thesis (his words, Discussion): "one coincidence, N = d + 1, is doing all of the organising work, and ... once it is made explicit the three-body and four-body constructions stop being analogous and become the same theorem at d = 2 and d = 3."
- Intro: the parameter "is not N but the spatial dimension d".

---

## 2. Objects and definitions (his names)

- q_1..q_N in R^d: body positions; masses m_1..m_N; centre of mass removed.
- rho_1..rho_{N-1}: mass-weighted Jacobi vectors, normalised so kinetic energy = (1/2) sum_k |rho-dot_k|^2 and moment of inertia = sum_k |rho_k|^2.
- X = [rho_1, ..., rho_{N-1}] in R^{d x (N-1)}: "mass-weighted Jacobi configuration matrix". N = d+1 => X in R^{d x d} (square). Square "precisely when ... the bodies form a full d-simplex".
- Rotation acts X -> RX, R in SO(d); scaling X -> mu X.
- G := X^T X: the Gram matrix, "the invariant" (Prop 2.1). XX^T is "the equivariant matrix", NOT invariant (transforms as R XX^T R^T). The two share a spectrum; "only one of them is a function on shape space."
- Sigma_d := {G in Sym(d): G >= 0 (PSD), tr G = 1} (Def 2.2): the trace-one slice; the shape space after O(d) and scale.
- P = {X in R^{d x d}: det X != 0} -> Sigma_d: the principal bundle, SO(d) acting on total space. "There is no horizontal restriction on T_G Sigma_d; every tangent direction of Sigma_d is realised by a motion of the bodies. The connection on P governs reconstruction of the physical rotation, not admissibility of shape velocities."
- D := {det G = 0} = {det X = 0}: the divisor / boundary; configurations that fail to span R^d. Branch locus.
- det X: the orientation coordinate; at d=2, w_3 := det X = signed area. Vol = |det X| = "the simplex volume" (Sec 11).
- r = rank G = rank X: stratifies Sigma_d (rank strata).
- c_(ij) in R^d: fixed vector determined by the masses with q_i - q_j = X c_(ij). Called "wall vectors" (Appendix A title).
- sigma_ij(G) := c_(ij)^T G c_(ij) = |q_i - q_j|^2.
- B_ij: binary collision locus (sigma_ij = 0).
- T_G Sigma_d: tangent space = symmetric traceless d x d matrices (also written Sym_0(d)).
- Principal frame: G = diag(g_1..g_d). g_i = eigenvalues of G (sum = 1).
- Eigenvalue directions (diagonal H: change the g_i; "deforms the shape of the inertia ellipsoid") and eigenframe directions (off-diagonal H: "rotates its principal axes").
- Omega_ij = deltaG_ij / (g_i - g_j): eigenframe rate (Lemma 4.1). "Omega is not the mechanical connection of the bundle P -> Sigma_d: it is a statement about eigenvectors of G, involves no group action, and lives entirely on the base."
- T in Sym(d): positive definite, commuting with G; eigenvalues t_i. Called "one symmetric positive tensor T"; in Remark 6.4 "the mass-inertia tensor". Free parameter until Sec 11.
- A(H) := TH + HT - 2 tr(TH) G: "the intrinsic transport operator" / "transport operator" (Def 5.1), acting on symmetric traceless H.
- D_t = diag(t). M = D_t - g t^T (g, t as column vectors of the g_i, t_i). Eigenvalue block of A = 2 M restricted to {sum h_i = 0}.
- u := sqrt(g ⊙ t) (entrywise), S := diag sqrt(g_i/t_i) (Thm 5.6). <h,k>_S = sum_i h_i k_i t_i/g_i: "the hidden inner product" in which the eigenvalue block is self-adjoint.
- Secular equation: sum_i g_i t_i/(t_i - lambda) = 1. Weights g_i t_i. f(lambda) = sum_i g_i t_i/(t_i - lambda) = "secular function".
- Regular stratum: G positive definite (interior).
- Pin: on the divisor, for k with g_k = 0, eigenvalue of M at t_k (eigenvalue of A "pinned at 2 t_k"). Z = {k: g_k = 0}.
- Branch collision: a root of the reduced secular equation meeting a pin => Jordan block (exceptional point).
- Canonical closure: T = G ("the only choice constructible from the shape alone").
- Frobenius structure: <H,K> = tr(HK) on Sym(d). Kinetic (submersion) metric: induced from the flat metric on X, the physically reduced kinetic energy. Third: affine-invariant metric of SL(d,R)/SO(d).
- Koszul–Vinberg characteristic function: phi(x) = integral over C* of e^{-<x,y>} dy (needs a volume form, no metric). For PD symmetric matrices phi(G) ∝ (det G)^{-(d+1)/2}.
- psi = -log det G: the potential. d psi = "the dual coordinate, a covector"; d^2 psi = "the Koszul–Vinberg metric <H,K>_G" = "the volume metric"; d^3 psi = "the cubic form" C.
- Congruence family: C(H) = S H S - tr(S^2 H) G.
- A_0 (additive / "Lyapunov" canonical operator), C_0 (multiplicative / "congruence" canonical operator): eqs (9),(10).
- M(K) = G^{-1} K G^{-1}: the volume metric read as an operator through the trace pairing (script M; distinct from the matrix M = D_t - g t^T).
- p_i = 1/g_i (Prop 11.5).
- "KV speed" tr((G^{-1} G-dot)^2) [rebuilt: extraction gives "tr (G^-1 Ġ)^2"].
- Smooth part of divisor = rank-(d-1) stratum; corner = where two eigenvalues vanish together (rank <= d-2) = isotropy stratum.
- Taxonomy of degenerations (Remark 11.14): "the pole (kernel along the locus, no genuine stratum)", "the fold (kernel across it, and here two rates)", and the new third entry "the corner, where the divisor itself is singular and the rates merge."
- Off the ladder: N-1 > d. Threefold split: eigenvalues / frame within the support / support-moving.
- Reconstruction holonomy: accumulated SO(d) element from lifting a curve G(t) horizontally in P -> Sigma_d.

---

## 3. Equations in order

Unnumbered displays are given with location. Numbered: (1)–(10).

Intro chain (unnumbered): N d -> (N-1) d -> d(d+1)/2 -> d(d+1)/2 - 1 "closes with no remainder" (after c.o.m.; after rotations; after scale).

Sec 2.1: X = [rho_1..rho_{N-1}] in R^{d x (N-1)}; N = d+1 => X in R^{d x d}.
Prop 2.1 proof: (RX)^T(RX) = X^T R^T R X = X^T X. Conversely Y^T Y = X^T X with X invertible => Q := Y X^{-1} satisfies Q^T Q = I.
Prop 2.3: dim Sigma_d = d(d+1)/2 - 1 = (N-1)d - d(d-1)/2 - 1.
Bundle: P = {X in R^{d x d}: det X != 0} -> Sigma_d.
Thm 2.4: D := {det G = 0} = {det X = 0}. Proof uses det Q = det Y / det X.

Sec 2.3 [rebuilt matrix]: G = [[1/2 + u, v],[v, 1/2 - u]] (general trace-one symmetric 2x2). det G = 1/4 - u^2 - v^2. Sigma_2 = disc u^2+v^2 <= 1/4. With w_3 := det X and det G = (det X)^2:
(1) u^2 + v^2 + w_3^2 = 1/4.
Reduced kinetic metric normalisation: (1/4)(dw_1^2 + dw_2^2 + dw_3^2) [as printed; the w_1,w_2 are not separately defined in the text — it only defines u, v, w_3].
Sec 2.4: at d=2 Frobenius is flat: ||deltaG||_F^2 = 2(du^2 + dv^2).

Sec 3.1: dim of stratum {r <= k} = k(k+1)/2 - 1 + k(d-k).
(2) sigma_ij(G) := c_(ij)^T G c_(ij) = |q_i - q_j|^2.
Prop 3.1: dim B_ij = d(d-1)/2 - 1, codim B_ij = d.

(3) d(d+1)/2 - 1 [dim Sigma_d] = (d-1) [diagonal: change the g_i] + d(d-1)/2 [off-diagonal: rotate the frame]. Instances: 2=1+1, 5=2+3, 9=3+6, 14=4+10, 20=5+15.
Lemma 4.1: Omega_ij = deltaG_ij/(g_i - g_j). Stated equal to "the spectral response formula <m|V|n> = <m|deltaSigma|n>/(lambda_in - lambda_out) of the projector framework, specialised to real symmetric matrices."

(4) A(H) := TH + HT - 2 tr(TH) G.
Lemma 5.2: tr(TH + HT - c tr(TH) G) = (2 - c) tr(TH).
Prop 5.4: on diagonal H = diag(h), sum h_i = 0: A(H) = 2 diag((D_t - g t^T) h), D_t = diag(t).
Thm 5.6: D_t - g t^T = S (D_t - u u^T) S^{-1}, u = sqrt(g ⊙ t), S = diag sqrt(g_i/t_i). <h,k>_S = sum_i h_i k_i t_i/g_i. Proof [rebuilt]: (Su)_i = sqrt(g_i/t_i) sqrt(g_i t_i) = g_i; (u^T S^{-1})_i = sqrt(g_i t_i) sqrt(t_i/g_i) = t_i; so S(uu^T)S^{-1} = g t^T; S commutes with D_t.
Thm 6.1 proof: T E_ij + E_ij T = (t_i + t_j) E_ij (E_ij symmetrised elementary matrix).
(5) sum_{i=1}^d g_i t_i/(t_i - lambda) = 1.
Interlacing: t_(1) < lambda_1 < t_(2) < lambda_2 < ... < lambda_{d-1} < t_(d).
Char. polynomial [rebuilt]: det(D_t - g t^T - lambda I) = prod_i (t_i - lambda) · (1 - sum_i g_i t_i/(t_i - lambda)). lambda = 0 always a root since sum g_i = 1; "it corresponds to the trace direction, which A annihilates."
f'(lambda) = sum_i g_i t_i/(t_i - lambda)^2 > 0.
Thm 6.5: M = D_t - g t^T, A v = 2 M v on traceless subspace. Reduced secular equation: sum_{i not in Z} g_i t_i/(t_i - lambda) = 1. Proof: M v = D_t v - (t·v) g; if t·v != 0 normalise to 1, then v_i = g_i/(t_i - lambda) [THE EIGENVECTOR FORMULA]; if t·v = 0 then t_i v_i = lambda v_i, v supported on {i: t_i = lambda}.
Sec 7: T = G: A(H) = GH + HG - 2 tr(GH) G; t_i = g_i; eigenframe spectrum {g_i + g_j}; weights g_i^2.
Prop 8.1: dim = r(r+1)/2 - 1 + r(n-r) = (r-1) [eigenvalues] + r(r-1)/2 [frame within the support] + r(n-r) [support-moving]. n=4, r=3: 8 = 2+3+3.

Sec 11.1: phi(x) = ∫_{C*} e^{-<x,y>} dy; phi(gamma x) = |det gamma|^{-1} phi(x); phi(G) ∝ (det G)^{-(d+1)/2}; det G = (det X)^2 = Vol^2; log phi = -((d+1)/2) log det G = -(d+1) log Vol.
(6) d psi(H) = -tr(G^{-1} H) — the dual coordinate, a covector.
(7) d^2 psi(H,K) = tr(G^{-1} H G^{-1} K) — the Koszul–Vinberg metric <H,K>_G.
(8) d^3 psi(H,K,L) = -2 tr(G^{-1} H G^{-1} K G^{-1} L) — the cubic form.
Remark 11.1: metric couples index pairs {i,j} with weight ∝ 1/(g_i g_j); cubic form couples index cycles i->j->k->i with weight ∝ 1/(g_i g_j g_k).
Thm 11.2 proof: <TH+HT, K>_G = sum_{i,j} (t_i + t_j) H_ij K_ij/(g_i g_j); trace-removal contribution -2 tr(TH) tr(G^{-1} K). Congruence family C(H) = SHS - tr(S^2 H) G.
(9) A_0(H) = G^{-1} H + H G^{-1} - 2 tr(G^{-1} H) G.
(10) C_0(H) = G^{-1/2} H G^{-1/2} - tr(G^{-1} H) G.
Generator relation [rebuilt]: d/ds|_{s=0} e^{sT/2} H e^{sT/2} = (1/2)(TH + HT).
Eigenframe spectra: 1/g_i + 1/g_j for A_0; 1/sqrt(g_i g_j) for C_0 ("arithmetic against geometric").
Remark 11.4: S = e^{T/2} gives s_i s_j = e^{(t_i+t_j)/2}.
Prop 11.5: eigenvalue block of C_0 is D_p - g p^T, p_i = 1/g_i; secular equation sum_{i=1}^d 1/(1/g_i - lambda) = 1 (every weight g_i p_i = 1); whole spectrum in [1/g_max, 1/g_min].
Thm 11.6: M(K) = G^{-1} K G^{-1}, defined by tr(H M(K)) = <H,K>_G. Square root K -> G^{-1/2} K G^{-1/2}. Positivity: tr(H G^{-1/2} H G^{-1/2}) = ||G^{-1/4} H G^{-1/4}||_F^2 > 0.
Thm 11.8: Gamma_ijk = (1/2) C_ijk. Geodesic equation G-ddot = G-dot G^{-1} G-dot; solution G(t) = G_0^{1/2} e^{tV} G_0^{1/2}, V in Sym(d). Proof: partial_i g_jk = C_ijk; Gamma_ijk = (1/2)(partial_i g_jk + partial_j g_ik - partial_k g_ij) = (1/2) C_ijk; G-dot = G_0^{1/2} V e^{tV} G_0^{1/2}; G-ddot = G_0^{1/2} V^2 e^{tV} G_0^{1/2}.
  NOTE on wording: the Introduction says "the cubic form is exactly twice the Christoffel data"; the theorem says Gamma = (1/2) C. Same statement.
Thm 11.10: lambda_max = 1/eps - 1 + O(eps); eigenframe rate eps^{-1/2} with prefactor 1/sqrt(g_j); finite count (d-1)(d-2)/2 + (d-2). Sketch: lambda = p_k - delta; remaining terms contribute -(d-1)/lambda -> 0, giving 1/delta -> 1.
Cor 11.11: det G = prod_i g_i = Vol^2; g_min ∝ Vol^2 near the divisor; eigenvalue block diverges as Vol^{-2}, eigenframe block as Vol^{-1}.
Prop 11.13: grad det G = adj(G), vanishes iff rank G <= d-2. With g_k = g_l = eps: exact eigenvalue 1/eps on direction e_k - e_l; eigenframe pair (k,l) eigenvalue 1/sqrt(g_k g_l) = 1/eps.

Appendix A (d=3, general masses) [rebuilt from badly broken layout; cross-checked with the Drive text reader output]:
- rho_1 = sqrt(mu_1)(q_2 - q_1), rho_2 = sqrt(mu_2)(q_3 - c_12), rho_3 = sqrt(mu_3)(q_4 - c_123) (c_12, c_123 = partial centres of mass; the paper does not write their formula out).
- mu_1 = m_1 m_2/(m_1+m_2); mu_2 = (m_1+m_2) m_3/(m_1+m_2+m_3); mu_3 = (m_1+m_2+m_3) m_4/(m_1+m_2+m_3+m_4).
- c_(12) = [1/sqrt(mu_1), 0, 0]
- c_(13) = [m_2/((m_1+m_2) sqrt(mu_1)), 1/sqrt(mu_2), 0]
- c_(23) = [-m_1/((m_1+m_2) sqrt(mu_1)), 1/sqrt(mu_2), 0]
- c_(34) = [0, -(m_1+m_2)/((m_1+m_2+m_3) sqrt(mu_2)), 1/sqrt(mu_3)]
- c_(14) = [m_2/((m_1+m_2) sqrt(mu_1)), m_3/((m_1+m_2+m_3) sqrt(mu_2)), 1/sqrt(mu_3)]
- c_(24) = [-m_1/((m_1+m_2) sqrt(mu_1)), m_3/((m_1+m_2+m_3) sqrt(mu_2)), 1/sqrt(mu_3)]
  Confidence: c_(12), c_(13), c_(23), c_(14), c_(24) read cleanly once reassembled. c_(34) second entry: the extraction scrambles numerator; "-(m1+m2)/((m1+m2+m3) sqrt(mu2))" is my reassembly of the fragments "− (m1+m m1+m2 √ 2+m3) µ2" — treat that one entry as rebuilt, verify against the companion zip script before relying on it.

---

## 4. Results with the grade the paper gives

The paper's blanket statement (Abstract): "All statements are verified numerically and the verification script is included." Proved = a proof is printed. Numerical tolerances in Section 5.

Section 2
- Prop 2.1 (The invariant): G = X^T X invariant under X -> RX for every R in O(d), and G determines X up to that action. XX^T not invariant. PROVED (proof printed).
- Def 2.2: Sigma_d.
- Prop 2.3 (Dimension): dim Sigma_d = d(d+1)/2 - 1. Stated; no separate proof (count). Checked d=2..8.
- Thm 2.4 (Branched cover): Sigma_d = P(normalised)/O(d); rotation-reduced shape space (quotient by SO(d)) is the double cover of Sigma_d branched over D. PROVED.
- Cor 2.5: three bodies in the plane — rotation-reduced, scale-fixed shape space is the sphere of radius 1/2, w_3 = det X the signed area, equator w_3 = 0 the collinear locus, two hemispheres the two orientations. "recovered here without choosing a Hopf map." Three binary collision loci sit on the equator, "alternating with the three Euler configurations". Derived in text + numerically checked.
- Sec 2.4: kinetic metric at d=2 is exactly the round metric of the radius-1/2 sphere — NUMERICAL (pushforward Gram = diag(1,1)). Interior of Sigma_d diffeomorphic to SL(d,R)/SO(d) — stated.

Section 3
- Rank strata dimension formula; top boundary r = d-1 has codimension one. Stated.
- Rotation action on P free where r >= d-1; isotropy SO(d-r) where r <= d-2. At d=3 collinear locus r=1 carries SO(2) isotropy, "the genuine singular locus of the reduction." Stated.
- Prop 3.1: sigma_ij(G) = 0 iff c_(ij) in ker G; B_ij inside D; dim B_ij = d(d-1)/2 - 1; codim B_ij = d. PROVED. "collisions are never hypersurfaces, and a generic trajectory does not meet them — the classical fact, recovered here from the rank condition."

Section 4
- Eq (3) tangent split: identity, holds every d.
- Lemma 4.1 (eigenframe rate is the spectral response): Omega_ij = deltaG_ij/(g_i - g_j). First-order perturbation theory; numerically reproduced to ratio 1.000000.

Section 5
- Def 5.1 transport operator.
- Lemma 5.2 (The coefficient is forced): A maps T_G Sigma_d to itself iff c = 2. PROVED (one-line trace identity) + numerical.
- Prop 5.3 (Block structure): block diagonal in the eigenvalue/eigenframe split. PROVED.
- Prop 5.4 (Rank-one form on eigenvalue block). Stated (computation).
- Prop 5.5 (Metric-freeness): A defined using only matrix product and matrix trace; spectrum independent of basis. Stated + numerical.
- Thm 5.6 (Symmetrisation). PROVED + verified. Eigenvalue block: real spectrum, diagonalisable, self-adjoint for <.,.>_S.
- Remark 5.7: S defined only on the interior; on D "self-adjointness is lost"; "the failure is intrinsic."

Section 6 — "the main result" (Intro says Sections 5–6)
- Thm 6.1 (Eigenframe spectrum): eigenvalues t_i + t_j, i<j; "no dependence on G at all." PROVED.
- Thm 6.2 (Secular equation, interlacing, reality): for T, G positive definite, tr G = 1, eigenvalue block of A has spectrum {2 lambda_1..2 lambda_{d-1}}, lambda_k the nonzero roots of (5); exactly one root in each interval (t_(k), t_(k+1)); spectrum of A real on the whole regular stratum; no exceptional points there. PROVED.
- Remark 6.3: the secular equation and interlacing for rank-one modifications are classical (Golub [9]; Bunch–Nielsen–Sorensen [10]) — "We claim none of that. What is claimed here is the identification" plus Thm 5.6.
- Remark 6.4 (Non-normal, but real): A genuinely non-normal; eigenvalue block symmetric only if g and t proportional; ||[A, A^T]|| vanishes when T isotropic and also when G isotropic, nonzero only when both anisotropic — MEASURED. "Non-normality is therefore a joint property of the mass-inertia tensor and the shape, not of T alone."
- Thm 6.5 (Boundary spectrum): (i) pin at 2 t_k with genuine eigenvector; (ii) remaining roots from reduced secular equation; (iii) Jordan block forms precisely when a root of (ii) coincides with a pin t_k; two coinciding pins (t_k = t_l, k,l in Z) is semisimple, two-dimensional eigenspace, no defect. PROVED + verified at d=3.
- Remark 6.6 (Genericity): defective locus has codimension two in combined (G,T) data; generic one-parameter path misses it; generic two-parameter family meets it at isolated points. Stated + numerical perturbation series.

Section 7
- T = G is the canonical closure — "we do not claim it is forced by mechanics." At T = G, A is symmetric (similarity of Thm 5.6 is the identity). "the canonical closure and non-normality are mutually exclusive". "This choice is superseded in Section 11". Status: recorded, not derived.

Section 8
- Three failures off the ladder (constrained G; no determinant; tangent split fails). "We state this as a boundary of validity rather than a conjecture about what replaces it."
- Prop 8.1 (Threefold split): dimension identity "verified for all (n, r) up to n = 8". NUMERICAL/identity.

Section 9: reconstruction — remarks only. Lift obstructed exactly on isotropy strata r <= d-2 (d=3: collinear).

Section 11
- Thm 11.2 (The parameter is the dual coordinate): A self-adjoint for <.,.>_G iff T ∝ G^{-1}; same for congruence family with S^2 ∝ G^{-1}. PROVED + measured asymmetries.
- Remark 11.3: "The non-normality of Section 6 was measured with the wrong form" — at T = G^{-1} Frobenius-asymmetric but KV-self-adjoint with real spectrum; the Sec 7 remark "is correct as stated but is an artefact of which form the question was asked in."
- Prop 11.5 (Spectrum of C_0): block diagonal; eigenframe eigenvalues 1/sqrt(g_i g_j); real, interlaces the p_i; entire spectrum in [1/g_max, 1/g_min]; "one interlacing structure covers all d(d+1)/2 - 1 eigenvalues, which is not the case for A_0." Stated, by Thm 6.2.
- Thm 11.6 (Kinematic selection): C_0's congruence part is the unique positive square root of M. PROVED + verified.
- Remark 11.7: C_0 singled out "with no further choice — a kinematic selection"; A_0 "the logarithmic generator of that congruence, one step removed". "Whether a dynamical principle selects the same operator is a separate question and remains open".
- Thm 11.8: Gamma_ijk = (1/2) C_ijk; geodesics closed form. PROVED + numerical.
- Remark 11.9 (An inversion that must be owned): <H,K>_G is the affine-invariant metric that Sec 2.4 warned against importing; it arrives "by derivation rather than importation: it is the Hessian of the log volume". Tension owned not resolved: "at d = 2 the interior of Sigma_d is hyperbolic in the volume structure and round in the kinetic one."
- Thm 11.10 (Boundary rates) for C_0, g_k = eps -> 0: (i) exactly one eigenvalue diverges, eigenvalue block, lambda_max = 1/eps - 1 + O(eps); (ii) exactly d-1 eigenvalues diverge from eigenframe block at rate eps^{-1/2}, prefactor 1/sqrt(g_j); (iii) remaining (d-1)(d-2)/2 + (d-2) finite; (iv) no Jordan block. Grade printed: "Sketch and verification" (NOT a full proof).
- Cor 11.11: eigenvalue block ~ Vol^{-2}, eigenframe block ~ Vol^{-1}.
- Remark 11.12: Thm 11.10(ii) fails for A_0 (its eigenframe eigenvalues diverge at eps^{-1}); "an exponent is measurable" so A_0 vs C_0 is not convention.
- Sec 11.6 header: "This subsection replaces Section 6.1; it does not extend it. Pinning at a finite value, the branch collision and the Jordan block have no analogue here."
- Prop 11.13 (Corner rates): D smooth exactly on rank-(d-1) stratum, singular exactly on isotropy stratum; at g_k = g_l = eps the two rates collide into one. Part (iii) is MEASURED slopes.
- Remark 11.14: pole / fold / corner taxonomy.

Appendix B verification tallies: VERIFY-LADDER-1 "All fourteen checks pass." VERIFY-LADDER-2: "13 of 14 pass and the one failure is recorded here rather than removed, because it corrected a claim" — the failed check was a drafting prediction that two coinciding pins would produce a Jordan block; "They do not." VERIFY-LADDER-3: "all ten pass."

---

## 5. Numbers (all dimensionless; all from the verification scripts unless noted)

Table 1 (square ladder): d=2,N=3: X 2x2, after c.o.m. 4, after rotations 3, shape dim 2 (Kendall shape sphere). d=3,N=4: 3x3, 9, 6, 5. d=4,N=5: 4x4, 16, 10, 9. d=5,N=6: 5x5, 25, 15, 14. Off ladder d=3,N=5: 3x4, 12, 9, 8 (G singular).
Table 2 (divisor D): d=2 rank 1 collinear; d=3 rank 2 coplanar; d=4 rank 3 confined to a hyperplane. At d=3 collinear = rank 1, codimension three.
- Shape sphere radius 1/2; disc radius 1/2.
- d=2 kinetic metric: off-diagonal 7 x 10^-12 in text (Sec 2.4); table gives 6.7 x 10^-12.
- (u, v, det X) on sphere radius 1/2: max deviation 2.2 x 10^-16.
- dim B_ij: 0 at d=2; 2 at d=3 (in 5-dim space).
- Lemma 4.1: ratio 1.000000 at eps = 10^-4 and 10^-5.
- Lemma 5.2: c=1 leaves tangent space by 0.693; c=2 by 2.8 x 10^-16.
- Block diagonality coupling norm < 10^-13.
- Eigenframe eigenvalues = t_i + t_j: max error 8.9 x 10^-16.
- Spectrum real, d=2..6, 15000 draws: max |Im lambda| = 0.0. One secular root per gap, every draw.
- Spectrum = {t_i + t_j} ∪ {2 lambda_k}: max error 9.2 x 10^-14.
- Metric-freeness: random non-orthonormal basis, same spectrum to 2.1 x 10^-9 across d=3,4,5.
- Thm 5.6: 1.3 x 10^-15 over 10^4 random draws, d=2..6.
- Thm 6.5 example d=3: t = (1.9, 0.5, 1.2), g = (0.6, 0.4, 0): eigenvalue block spectrum {2.12, 2.40}, 2 t_3 = 2.40 pinned. Tuned t_3 so secular root meets pin: normalised eigenvector determinant 6.1 x 10^-16 (defective); table lists boundary EP |det eigvecs| 1.1 x 10^-15 (first pass). g = (1,0,0), t_2 = t_3: 1.000 (semisimple). Generic rank-one boundary not defective: 0.866. Pins checked with 1, 2, 3 vanishing eigenvalues at d=3,4,5.
- Remark 6.6 perturbation amplitudes 0, 10^-6, 10^-4, 10^-2 -> eigenvector determinant 6 x 10^-16, 2.8 x 10^-3, 4.5 x 10^-2, 3.4 x 10^-1.
- Sec 7: ||A - A^T|| = 3 x 10^-16 at T = G (table 3.3 x 10^-16), order unity otherwise (table: 3.75), d=2..5.
- Off-ladder d=3,N=5: Sym(4) dim 10; rank<=3 locus dim 9; shape dim 8 = 2+3+3.
- Remark 11.1: cubic form permutation spread 3 x 10^-16.
- Thm 11.2 asymmetries: A: 84.2 (random T), 14.6 (T=G), 1.8 x 10^-12 (T=G^-1). C: 35.0, 13.3, 3.6 x 10^-12.
- Remark 11.3: at T = G^-1 Frobenius asymmetry 2.74, KV asymmetry 3.6 x 10^-12.
- Thm 11.6: congruence squared = M to 1.4 x 10^-14.
- Thm 11.8: partial_i g_jk = C_ijk to 3.1 x 10^-12; geodesic 5.2 x 10^-7 (second differences); KV speed conserved 1.2 x 10^-11.
- Thm 11.10: d=3, eps = 10^-6: lambda_max = 1000000.000 vs 1/g_min - 1 = 1000000.000. Log-log slopes over eps in [10^-6, 10^-3]: -1.00000 top; -0.49993 (d=3), -0.49996 (d=4) next; predicted -1, -1/2. Min normalised eigenvector determinant over 400 near-boundary draws: 0.87, 0.73, 0.60 at d=3,4,5.
- A_0 slopes: -1.00000 and -0.99980.
- Prop 11.13: exact eigenvalue 1/eps verified relative 1.2 x 10^-16; corner slopes -0.99973, -0.99973, -1.00000; adj(G) check "1.4 x 10^-9 vs 0.25".
- Appendix A: six wall vectors vs random unequal-mass configuration, 3.6 x 10^-15.
- Figure 2: drawn at d=4 (poles t1..t4, lambda axis 0..4, level 1 dashed, circles = roots, square = lambda=0 root).
- Figure 3: d=3, eigenvalues 10^0..10^6 vs g_min ~ Vol^2 from 10^-2 to 10^-6.

There are NO physical units, no physical constants, and no astronomical or laboratory data anywhere in the paper.

---

## 6. Limits and open items (as the paper states them)

1. T has no dynamical derivation (Sec 7): "Any other T — in particular any T carrying velocity or driving data — must be derived from a stated dynamical principle. No such derivation exists in this framework at present". Results are "a statement about the family of operators (4), parametrised by T, rather than about one distinguished dynamical operator." Sec 11 forces T ∝ G^{-1} kinematically only.
2. Dynamical selection open (Remark 11.7, 11.8): "the kinematic selection says which operator the volume structure builds, not which one a mechanical principle would".
3. Off the ladder (N-1 > d): "every statement below fails"; needs "a different construction and not treated here". The support-moving block of Prop 8.1: "the action of any operator above on it is not determined by the interior theory. That block is the precise boundary of what this paper establishes."
4. Frobenius vs kinetic metric relation "established only at d = 2; whether the transport spectrum computed in one is the transport spectrum of the other, for d >= 3, has not been checked." (Mitigated by Prop 5.5: the spectrum of A is metric-free.)
5. Singularity class of the corner in Arnold's hierarchy "is not attempted here."
6. Hyperbolic vs round tension at d=2 "owned rather than resolved".
7. Sec 11.6 replaces Sec 6.1 (pinning / Jordan blocks belong to the general-T Frobenius-form analysis; in the volume structure there is divergence, no defect). The two boundary pictures are both in the paper, each tied to its structure.
8. Thm 11.10 carries only "Sketch and verification".
9. T must commute with G (simultaneously diagonal) in every theorem; non-commuting T is not treated.
10. Interior theorems need all g_i > 0 and all t_i > 0; interlacing as stated orders distinct t_(1) < ... < t_(d) (equal t_i not discussed in Thm 6.2).
11. No equations of motion, no potential energy, no forces appear. It is a kinematic/shape-space paper.

---

## 7. Bearing on the team's questions

### 7a. N equal balls on a hyperbolic field, light/energy passing ball to ball
- The paper contains NO balls, NO light, NO energy transfer, NO "field". It is about N point masses in R^d. Anything said about balls is a mapping the team makes, not something in this paper.
- What Gram matrix placements give, in this paper's construction: remove centre of mass, form the N-1 mass-weighted Jacobi vectors rho_k, stack as X (d x (N-1)), G = X^T X is (N-1) x (N-1), entries rho_a · rho_b. Normalise tr G = 1 (trace = moment of inertia, so this fixes scale). Mutual distances are recovered by sigma_ij(G) = c_(ij)^T G c_(ij) = |q_i - q_j|^2 with the wall vectors c_(ij) (Appendix A gives them for N=4, d=3, general masses; for equal masses set all m_i equal in those formulas — the paper does not print an equal-mass specialisation).
- "Square" means X is d x d, i.e. N = d + 1: balls in a plane (d=2) => N=3; in space (d=3) => N=4. Then G is an unconstrained PSD form, det X exists (orientation / signed volume), shape space = double cover of Sigma_d branched over det X = 0.
- If N-1 > d (e.g. more than 3 balls in a plane, more than 4 in space) the paper is off the ladder: G has rank <= d, lies on a determinantal variety, no determinant, tangent split fails, and only the threefold dimension count (Prop 8.1) survives. First case worked: five bodies in three dimensions, 8 = 2+3+3.
- "Hyperbolic": the only hyperbolic object in the paper is the shape space itself, not the space the bodies sit in. "at d = 2 the interior of Sigma_d is hyperbolic in the volume structure and round in the kinetic one." The volume metric <H,K>_G = tr(G^{-1} H G^{-1} K) is the Hessian of psi = -log det G (log volume); geodesics G(t) = G_0^{1/2} e^{tV} G_0^{1/2}. The bodies themselves are in flat R^d. The paper does not treat bodies placed on a hyperbolic surface.
- Passing "from one to the next": the nearest thing in the paper is the cubic form coupling "index cycles i -> j -> k -> i with weight ∝ 1/(g_i g_j g_k)" versus the metric coupling "index pairs {i,j} with weight ∝ 1/(g_i g_j)" (Remark 11.1) — but the indices there are principal axes of G, not bodies.

### 7b. Secular equation and leading eigenvector
- Secular equation (5): sum_i g_i t_i/(t_i - lambda) = 1, weights g_i t_i > 0; roots lambda_k strictly interlace the t_i; lambda = 0 is the extra root (trace direction, annihilated by A). Eigenvalues of A: {t_i + t_j} (eigenframe) ∪ {2 lambda_k} (eigenvalue block).
- Eigenvector of M = D_t - g t^T for root lambda: v_i = g_i/(t_i - lambda), normalised t·v = 1 (from proof of Thm 6.5). The paper does NOT use the phrase "leading eigenvector" and does not single one out for general T.
- For the canonical C_0: secular equation sum_i 1/(1/g_i - lambda) = 1; whole spectrum inside [1/g_max, 1/g_min]; top eigenvalue near the divisor lambda_max = 1/eps - 1 + O(eps) (eigenvalue block, ~Vol^{-2}); at the corner the exact eigenvalue 1/eps is carried by direction e_k - e_l.
- Symmetrised form: D_t - u u^T with u = sqrt(g ⊙ t); inner product <h,k>_S = sum h_i k_i t_i/g_i.
- T = G: weights g_i^2, eigenframe spectrum {g_i + g_j}. T = G^{-1} (forced by volume structure): A_0 weights g_i · (1/g_i) = 1 [this follows from his weights g_i t_i with t_i = 1/g_i; the paper states "every weight g_i p_i equals 1" for C_0 and says Thm 6.2 applies].

### 7c. Sun and planets
- NOTHING. The words Sun, planet, solar, orbit do not appear. No masses are assigned numerical values except "a random configuration with unequal masses" in a check. Any Sun-planet use is outside this paper.

### 7d. Three- and four-body configurations
- Three bodies in the plane (d=2, N=3): X 2x2; Sigma_2 = disc of radius 1/2 in (u,v) with G = [[1/2+u, v],[v, 1/2-u]]; boundary det G = 0 = collinear; shape space = sphere u^2+v^2+w_3^2 = 1/4 with w_3 = det X signed area; equator collinear; hemispheres = orientations; three binary collision loci B12, B23, B31 are points on the equator "alternating with the three Euler configurations"; kinetic metric round, radius 1/2; tangent split 2 = 1+1 (one eigenvalue direction, one eigenframe direction); transport spectrum: one eigenframe eigenvalue t_1 + t_2 and one eigenvalue-block eigenvalue 2 lambda_1 with t_(1) < lambda_1 < t_(2).
- Four bodies in space (d=3, N=4): X 3x3; shape space five-dimensional; divisor D = coplanar locus (rank 2, codim 1); collinear = rank 1, codim 3, SO(2) isotropy, "the genuine singular locus of the reduction", lift obstructed there; binary collision loci dim 2, codim 3; tangent split 5 = 2+3; six wall vectors in Appendix A; spectrum: three eigenframe eigenvalues t_i + t_j and two eigenvalue-block eigenvalues 2 lambda_1, 2 lambda_2 interlacing t_(1) < lambda_1 < t_(2) < lambda_2 < t_(3).
- Five bodies in a 4-space: d=4, shape dim 9 = 3+6. Six bodies d=5: 14 = 4+10.
- Five bodies in three dimensions: OFF the ladder (see 7a).
- No specific configurations (equilateral/Lagrange, tetrahedron, figure-eight) are computed. The Lagrange/equilateral point is not named; only "Euler configurations" are mentioned once. Chenciner–Montgomery [4] is in the reference list but not discussed in the body.
- The paper says a principal-frame argument "will not detect a confusion between" X^T X and XX^T — the invariant is X^T X.

### Links the paper itself makes to his other work
- Lemma 4.1: "exactly the spectral response formula <m|V|n> = <m|deltaSigma|n>/(lambda_in - lambda_out) of the projector framework, specialised to real symmetric matrices."
- Remark 11.14: "The taxonomy of degenerations running through this programme" (pole, fold, corner).
- No other of his papers is cited in the reference list; all 14 references are external (Kendall; Dryden et al.; Montgomery; Chenciner–Montgomery; Albouy–Chenciner; Moeckel–Montgomery; Kato; Golub–Van Loan; Golub; Bunch–Nielsen–Sorensen; Vinberg; Shima; Koszul; Bhatia). References [5], [6], [7], [8], [13], [14] and [1]–[4] are listed; only [9], [10], [11], [12] are cited by number in the body text that I saw.
