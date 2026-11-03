# 2026-06-22_NonNormal_Lattice_Transport_Operators (fileId 1iOkBxMiPd_V2H33l7a-JCcNtAdDwX1Ah) — READ IN FULL (20 pp, nothing truncated). This is the Paper III of the quadralogy (file title ..._20pp_69c4950c.pdf).
Title: "Non-Normal Lattice Transport Operators with Gradient-Controlled Pseudospectra and Effective Inertia Tensors". Jeromie N Beasley, June 22, 2026. (No evidence-grade legend; statements as theorem/proposition/claim.)
## Definitions
- H_N(ε)=A+D0+εE on H_N=⊕R² (2N-dim real), periodic. (AΨ)_n = α_N J(ψ_{n+1}-ψ_{n-1}), J=[[0,-1],[1,0]]. D0: (D0Ψ)_n=B_nψ_n, B_n symmetric 2x2 (local obstruction/Hessian). (EΨ)_n=½[(B_{n+1}-B_{n-1})Jψ_n + J(B_{n+1}-B_{n-1})ψ_n] + lower-order averaging terms; ||E|| ≤ C max||δB_n||, δB_n=B_{n+1}-B_n. Leading part E_lead=(M_nJ+JM_n) block-diagonal, M_n=½(B_{n+1}-B_{n-1}); S_n skew.
- Local anisotropy Δ_n=||δB_n||/sqrt(λmin(B_n)λmax(B_n)). ε-pseudospectrum σ_ε={z: ||(zI-H)^-1|| ≥ 1/ε}. Kreiss constant K(H)=sup Re z>0 Re(z)||(zI-H)^-1||; K=1 for normal.
- Effective obstruction tensor I_n=[[B_n, cδB_n],[c(δB_n)^T, B_{n+1}], c≈1/√2 (R^{4x4}); turning angle Θ_n=arccos<v_max(n),v_max(n+1)>; rigidity R^ε_n=1/(λmin(I^eff_n)+ε).
## Results
- Thm 3.1: A is symmetric (A^T=A) (A=α_N J Δ1, both skew, commute). Sec 6: exact spectrum of A via symplectic Fourier modes: eigenvalues λ_k^± = ∓2α_N sin(2πk/N), purely real (J eigenvalues ±i, eigenvectors ξ±=(1,∓i)).
- H0=A+D0 symmetric hence normal; [H_N(ε),H_N(ε)^T]=O(ε), leading term ∝ δB_n; commutator expansion [H,H^T]=ε·2[E,H0]+O(ε²) (derivation Sec 7.1).
- Pseudospectral bulge vertical extent O(√ε·Δ_n) at obstruction hotspots; Kreiss K(H_N(ε)) ≤ C' max_n Δ_n/√ε (C' with possible mild factors in N, α_N). Numerical validation (Sec 5): N=32,64,128; bulges localize where ||δB_n|| max; uniform B_n ⇒ normal to machine precision; discrete second-difference converges to Laplacian with error O(δ²), δ=2π/N.
- Table 1: eigenvalue shift O(ε); bulge height O(√ε); resolvent norm near spectrum O(1/√ε) within δ~√ε; Kreiss O(max Δ_n/√ε); safe Dunford contour distance ≳ √ε+η.
- Thm 8.1 (Resolvent bound under proper gluing): H_{A∪B}=[[H_A,C],[C*,H_B]], ||C|| ≤ C0 α_N max_{p∈I}||δB(p)||; for Re z ≥ δ, ||(zI-H_{A∪B})^-1|| ≤ C(δ)(max{K(H_A),K(H_B)}+||C||); K(H_{A∪B}) ≤ max{K}+C'||C||. Gluing functional G(A,B)=P(A∪B)-P(A)-P(B) (persistence capacity gain).
- Dunford regularized trace-log: Tr log(H_N(ε)+ηI)=(1/2πi)∮ log(z) Tr[(zI-H-ηI)^-1]dz, contour at distance η ≳ √ε.
- Prop 10.1 (Transport–Obstruction Correspondence): lattice refinement ⇒ A→pullback of intrinsic A_intr; D0 discretizes local transport capacity C(V)=g_Π(V,V); εE realizes tangent variations V=ΠV(I-Π)+(I-Π)VΠ; high-Δ_n sites = lattice analogues of singular features on the Kendall shape sphere (Weyl/Dirac nodes, Euler configurations); metric-curvature inequality |Ω| ≤ 2√(g(V,V)g(W,W)-g(V,W)²) ≤ 2√(C(V)C(W)) sinθ_G.
- Sec 10.3 effective inertia tensors: intermediate-axis (Tennis Racket/Dzhanibekov) analogy; Prop (Localization and Scaling of Pseudospectral Bulges): height ≲ C√(εΔ_n).
- Thm 11.1 continuum limit: ||Δ_δψ-ψ''||_{L²} ≤ δ²√L/12 ||ψ''''||_∞ for smooth compactly supported ψ.
## Open problems: none listed (Conclusion says framework extends to unbounded operators via relative boundedness).
## Flags: non-normality (central); pseudospectral bulges at "rigidity interfaces"/walls; shape-sphere rank-drop; trace-log with shift η (offset-like); Smith disk/census/memory/peel: absent. "Companion paper: Intrinsic Quantum Geometric Tensor on the Grassmannian and Spectral Lower Bounds on Dissipation" (Paper I).
