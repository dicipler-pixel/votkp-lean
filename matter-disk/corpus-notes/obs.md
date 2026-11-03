# obs (14).pdf  -  "Spectral Stability Across Obstruction Interfaces in Geometric Transport Systems: Effective Inertia Tensors and Gluing Dynamics"
Author Jeromie N Beasley, dated June 24 2026. 25 pp. fileId 1z6tg_Y7s4pYzmKiBou8WZ_wArLy1kgP5. Read in full (all 3084 lines of extracted text, pp 1-25 incl. Appendix A and reference list). No version number in the text. Figures are images (captions read, not the plots). Math extraction partly garbled but all formulas below were legible.
SAME BODY as 2026-06-24_Spectral_Stability file (see spectral_stability.md): that file differs only in (a) abstract has the duplicated paragraph removed and wording "bounds ... on the Kreiss constant", (b) table-of-contents order of items 7/7.1, (c) it lacks the 7 raw BibTeX reference entries that obs (14) has at the end (Trefethen-Embree 2005; Kreiss 1962; Dunford-Schwartz 1958; Trefethen et al 1993; Kendall 1984; Provost-Vallee 1980). obs (14) abstract states the bulge/Kreiss claim twice (duplicated paragraph).
No [T]/[V]/[C]/[H] grades used. Results are labelled Theorem/Proposition/Lemma/Corollary/Definition. Cross-refs are broken ("Section ??", "Figure ??", "Paper IV [?]").

## Flags for the requested topics
Smith disk / reflection coefficient / peel: none. Offset / log-odds: none (only a shift eta in the trace-log). Census: none. Walls: "rigidity interfaces" (Weyl/Dirac nodes, Euler configurations on the shape sphere), "binary walls" referenced from Paper IV; "refractive surfaces" language. Non-normality: central (see below). Exceptional points: none named. Memory: "transport memory view" and "gauge-equivalent" in 10.4 ("the obstruction geometry view and the transport memory view are gauge-equivalent descriptions of the same underlying anisotropy class").

## Definitions (his)
- H_N(eps) = A + D0 + eps E on H_N = R^{2N} = (+)_{n=1..N} R^2, periodic. psi_n=(x_n,y_n). J=[[0,-1],[1,0]], J^T=-J, J^2=-I2.
- (A Psi)_n = alpha_N J (psi_{n+1} - psi_{n-1}); A = alpha_N J Delta_1.
- (D0 Psi)_n = B_n psi_n, B_n = B_n^T in R^{2x2} ("local obstruction field"; B_n symmetric positive definite in 10.2/10.3).
- (E Psi)_n = (1/2)[(B_{n+1}-B_{n-1}) J psi_n + J (B_{n+1}-B_{n-1}) psi_n] + neighbor averaging terms of lower order (2.1). Constraint ||E|| <= C max_n ||delta B_n||.
- Two gradients: centered delta_c B_n = B_{n+1}-B_{n-1} (in E lead); one-sided delta B_n = B_{n+1}-B_n (in I_n and Delta_n). M_n = (1/2)(B_{n+1}-B_{n-1}); E_lead = diag(E_n), E_n = M_n J + J M_n (block-diagonal, skew-symmetric).
- For symmetric M=[[a,b],[b,d]]: MJ+JM = [[2b, d-a],[d-a, -2b]]. Isotropic part cancels: E_n = 0 whenever B_n = lambda_n I; "E measures only changes in the directional structure (anisotropy) of the obstruction field, not its overall strength."
- E_avg (App A): (E_avg Psi)_n = (1/4)[delta B_n J (psi_{n+1}+psi_n) + delta B_{n-1} J (psi_n+psi_{n-1})]; block-tridiagonal with periodic corner wraps.
- eps-pseudospectrum: sigma_eps = {z : ||(zI-H)^{-1}|| >= 1/eps}.
- Local anisotropy Delta_n = ||delta B_n|| / sqrt(lambda_min(B_n) lambda_max(B_n)).
- Kreiss constant K(H) = sup_{z not in sigma} dist(z,sigma)||(zI-H)^{-1}||; right half-plane form K(H)=sup_{Re z>0} Re(z)||(zI-H)^{-1}||. K=1 for normal. Kreiss Matrix Theorem quoted: ||e^{tH}|| <= e^{t omega} K(H), omega = max Re sigma(H) [as printed].
- Dunford log: log(H+eta I) = (1/2 pi i) oint_Gamma log(z)(zI - H - eta I)^{-1} dz (10.1); Tr log = same with Tr[resolvent] (10.2). Contour placed at distance eta >~ sqrt(eps) from spectrum.
- Effective obstruction tensor I_n^eff = [[B_n, c delta B_n],[c (delta B_n)^T, B_{n+1}]] in R^{4x4}, c ~ 1/sqrt2 ("chosen to balance the two diagonal blocks while preserving positive-definiteness").
- Turning angle Theta_n = arccos<v_max(n), v_max(n+1)> (v_max = unit eigenvector of largest eigenvalue of I_n^eff). Rigidity R_n^eps = 1/(lambda_min(I_n^eff)+eps).
- Gluing functional G(A,B) = P(A u B) - P(A) - P(B), P = "integrated persistence depth" (from "companion obstruction atlas").
- Reporting metrics (Defs 12.1-12.3): C(V)=g_Pi(V,V)=Tr(Pi V^2) = (1/2)Tr([Pi,V][V,Pi]); cos theta_G = g(V,W)/sqrt(C(V)C(W)); sin theta_G = sqrt(1-cos^2); Berry curvature Omega_Pi(V,W) = -i Tr(Pi[V,W]); Locked Participation Index LPI(Psi) = N (sum_n ||psi_n||_R2^4)^{-1}.
- Intrinsic QGT (intro, from Paper I): Q_Pi(V,W)=Tr(Pi V W); metric g_Pi(V,V)=C(V); inequality |Omega_Pi(V,W)| <= 2 sqrt(C(V)C(W) - g(V,W)^2) = 2 sqrt(C(V)C(W)) sin theta_G.

## Results with statements (labels as he gives them)
- Thm 3.1: A^T = A (proof: A = alpha_N J Delta_1; both factors skew, act on independent indices, commute).
- Sec 6 (unlabelled derivation): Fourier modes phi_k(n)=e^{2 pi i k n/N}; (A Psi_k)_n = 2 i alpha_N sin(2 pi k/N) J Psi_k; J eigenvalues +-i with eigenvectors xi_+- = (1, -+i); spectrum lambda_k^+- = -+ 2 alpha_N sin(2 pi k/N), "completely real". (Fig 3 caption: all eigenvalues on real axis.)
- Sec 7: H0 = A + D0 symmetric hence normal [H0,H0^T]=0; [H_N(eps),H_N(eps)^T] = O(eps). Expansion [H,H^T] = eps([H0,E^T]+[E,H0]) + eps^2[E,E^T]; with E^T = -E + O(||E_avg||): [H,H^T] = eps*2[E,H0] + O(eps^2). "Non-normality of H_N(eps) is therefore generated exclusively by the coupling term eps E (together with any spatial variation in the Hessians B_n)." Design goals: uniform B_n -> M_n=0 and E_lead=0; ||E||<=C max||delta B||. Explicit products (7.1) (A D0 Psi)_n = alpha_N J(B_{n+1}psi_{n+1} - B_{n-1}psi_{n-1}); (7.2) (D0 A Psi)_n = alpha_N B_n J(psi_{n+1}-psi_{n-1}).
- Sec 8: first-order resolvent correction localized because E_lead block-diagonal; bulges at sites of largest ||delta B_n||.
- Thm 8.1 (= Thm 10.3, repeated) Resolvent bound under gluing: H_{AuB} = [[H_A, C],[C*, H_B]], ||C|| <= C0 alpha_N max_{p in I}||delta B(p)||; for Re z >= delta>0: ||(zI-H_{AuB})^{-1}|| <= C(delta)(max{K(H_A),K(H_B)} + ||C||), provided ||C|| <= delta/(4 max{K(H_A),K(H_B)}). Proof by Schur complement S = zI - H_A - C(zI-H_B)^{-1}C*, ||C(zI-H_B)^{-1}C*|| <= ||C||^2 K(H_B)/delta < delta/4, Neumann series, ||S^{-1}|| <= (2/delta) max K. (Second proof in 10.3 writes S = H_A - C(zI-H_B)^{-1}C*, a slightly different expression.) Also says bound "continues to hold as delta->0+ with at most a mild logarithmic loss" (no proof).
- Cor 8.2 (= Cor 10.4): K(H_{AuB}) <= C'(delta)(max{K(H_A),K(H_B)} + ||C||). Remark 8.3/10.5: gluing preserves sectorial stability up to first-order interface corrections; analogy with critical layers of Orr-Sommerfeld; "no additional non-normal growth beyond interface scale"; positive G(A,B) enlarges admissible continuation paths without disproportionate non-normal amplification.
- Sec 9.1: K(H0)=1; K(H_N(eps)) <= C' max_n Delta_n / sqrt(eps), C' independent of eps "with possible mild dependence on N and alpha_N" (derived from "numerical range deviates from the spectrum by at most O(eps)" + first-order resolvent perturbation).
- Sec 9.2: ||R0(z)||=1/delta at dist(z,sigma(H0))=delta; ||R(z;eps)|| <= 1/delta + eps C /delta^2 + O(eps^2/delta^3).
- Lemma 9.1: ||(zI-H_N(eps))^{-1} - R0(z)|| <= C eps max_n Delta_n/delta^2 + O(eps^2/delta^3).
- Cor 9.2: with delta = c sqrt(eps), c large, vertical extent of eps-pseudospectrum above sigma(H0) at site n is O(sqrt(eps) Delta_n).
- Table 1 scalings: eigenvalue shift O(eps) everywhere; bulge height O(sqrt(eps) Delta_n) at hotspots; resolvent norm near spectrum O(1/sqrt(eps)) within delta ~ sqrt(eps); Kreiss O(max Delta_n/sqrt(eps)) global; safe Dunford contour distance >~ sqrt(eps)+eta.
- Sec 5 numerics (no tables): periodic lattices N = 32, 64, 128; bulges localize where ||delta B_n|| maximal; "The Kreiss constant grows with system size, consistent with the bound"; uniform B_n -> H_N(eps) normal "to machine precision" and pseudospectrum collapses near the real spectrum; second-difference converges with error O(delta^2), delta = 2 pi/N. Fig 4 caption: bulge height O(sqrt eps), Kreiss O(1/sqrt eps), "transient amplification of size up to O(1/sqrt eps) on intermediate timescales". No tabulated numbers, no fitted exponents reported in text.
- Prop 10.1 (Transport-Obstruction Correspondence): under N->inf, delta=L/N->0: A converges strongly to pullback of A_intr; D0 discretizes C(V); eps E realizes tangent variations V = Pi V (I-Pi) + (I-Pi) V Pi. No proof beyond the narrative.
- 10.3.2 Proposition (Localization and scaling of bulges): height <~ C sqrt(eps) Delta_n; K <= C' max Delta_n / sqrt(eps). "Justification": R ~ R0 + eps R0 E R0, local correction ~ Delta_n/delta^2, set delta~sqrt(eps).
- 10.3.1 statements: "Stable directions: high local rigidity + small Delta_n. Intermediate/unstable directions: large Delta_n." Tennis-racket (Dzhanibekov) analogy for intermediate axis. When all B_n identical Delta_n=0 and operator (near-)normal.
- 10.3.3: continuum limit I^eff(tau) on [0,L]; localized transient growth where ||d_tau I^eff|| large relative to local eigenvalues.
- 10.4: gauge invariance under B_n -> U_n B_n U_n^T, U_n in GL(2): "A is unchanged, while E transforms covariantly. All spectral quantities, the Kreiss bound, the localized bulges..., and the gluing results are gauge-invariant." (Stated, not proved here; note U_n in GL(2) is not orthogonal, text does not address whether D0 stays within the stated class.)
- Thm 11.1: Delta_delta psi_n = (psi_{n+1} - 2 psi_n + psi_{n-1})/delta^2 converges strongly to d^2/dtau^2 in L2 for psi in C_c^inf([0,L],R^2); bound ||Delta_delta psi - psi''||_L2 <= (delta^2 sqrt(L)/12)||psi''''||_inf; proof by Taylor expansion. (Note: the operator A in the paper is the centered FIRST difference; Thm 11.1 is about the second difference, which is not a component of H_N(eps) as defined in Sec 2 -- Prop 10.1 / abstract refer to "the discrete Laplacian component of A"; as defined A has none.)
- Lemma A.1: ||E_avg|| <= max_n ||delta B_n|| (constant C=1), by triangle inequality + Cauchy-Schwarz + periodic shift; E_avg's contribution to [H,H^T] "remains strictly bounded at order O(eps^2)".
- Definition 10.2 dominant transport axis / turning angle (above). Claim: Theta_n is "direct lattice counterpart of the principal-angle hierarchy and variational refraction"; high Delta_n interfaces "act as refractive surfaces that align transport trajectories with the interface normal" (narrative).
- 12.2 LPI claims: delocalized (LPI ~ 1) for uniform field; hotspot locking (LPI ~ 1/N) when Delta_n >> 0, "the transient states of the semigroup e^{-tH_N(eps)} collapse entirely onto the obstruction hotspots" (stated; no numerics shown). Also: pseudospectral bulges "correspond precisely to regions where high geometric chirality (sin theta_G ~ 1) allows intense local curvature flux."

## Open problems / limits
No explicit open-problems section. Text says framework "extends naturally to unbounded operators via relative boundedness and recovers standard geometries with saturation of the metric-curvature bound" (claim, no proof).

## Key verbatim quotes
- "Non-normality is therefore generated exclusively by the coupling term eps E"
- "Sites with large Delta_n act as discrete analogues of rigidity interfaces (such as Weyl/Dirac nodes or Euler configurations) on the shape sphere."
- "the obstruction geometry view and the transport memory view are gauge-equivalent descriptions of the same underlying anisotropy class."
- "instability (non-normality) is curvature of that geometry." (1.1)
- "When delta B_n = 0 everywhere the operator collapses to the normal operator H0 = A + D0"
Companion papers referenced: Paper I (Intrinsic QGT on the Grassmannian, "June 20, 2026 (v2)"), Paper IV (four-body, Sigma_4), "companion obstruction atlas", "companion three-body reduction".
