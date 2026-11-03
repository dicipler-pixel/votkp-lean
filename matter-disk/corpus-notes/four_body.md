# 4_Body_Prob (3) (fileId 1QCh2wgkoKkZjOWikWVsVmat5erNpzK5r) — READ IN FULL (11 pp; nothing truncated)
Title: "The 5D Spectral Anatomy of Four-Body Obstructions: Kinematic Transport Geometry on Stratified Shape Manifolds" (Paper IV), Jeromie N. Beasley, June 23, 2026. (Byline there is with middle initial and affiliation "Program in Complex Spectral Geometry and Projector Dynamics".)
## Abstract claims
Extends Papers I-III (Paper I: QGT on Grassmannians; Paper II: 3-body S^2, A_intr = J^T P_H T(w) J; Paper III: lattice non-normal). Maps 9-dim config space to 5-dim stratified shape space Σ4 with non-Abelian SO(3) connection; 5x5 intrinsic transport operator A_intr; six binary collision hypersurfaces B_ij act as refraction sheets where transport cones flatten parallel to wall; 3D collinear horizon C_coll semi-simple/diagonalizable generically; Jordan blocks/Exceptional Points confined to lower-dim multi-body collision manifolds; link to QGT dissipation bounds; SVD tracking protocol.
## Definitions
- Axiom (Reflective Closure of Transport): "All admissible transport is defined by closure under projection onto the tangent Grassmannian bundle. Any attempted evolution that fails exact closure generates an induced projection defect..." transport, obstruction, refraction, persistence "arise from a single reflective process".
- Jacobi vectors ρk; X=[ρ1,ρ2,ρ3] in R^{3x3}; M = X X^T in Sym+(3); W = M/Tr M, Tr W=1; Σ4 = trace-one PSD symmetric matrices stratified by collision type; T_W Σ4 = symmetric traceless dW.
- Binary wall: σ_ij(W) = L_ij W L_ij^T = 0. Six explicit mass-weighted row vectors L12..L14 (eqs 1-6) with reduced masses μ1=m1m2/(m1+m2), μ2=(m1+m2)m3/(m1+m2+m3), μ3=(m1+m2+m3)m4/(sum).
- Principal SO(3)-bundle; projection π: X -> XX^T/Tr; vertical V_X={ΩX, Ω skew}; horizontal H_X: X^T δX symmetric.
- Thm 1 (Mechanical connection / horizontal projector): P_H(δX)=δX - Ω(X,δX)X, Ω = skew(δX X^T)(XX^T)^-1; on shape space P_H(δW)=δW - [Ω,W], Ω=skew(δW W^-1); principal frame Ω_ij = δW_ij/(w_i - w_j).
- Intrinsic transport operator: A_intr(H) = P_H( T(W)H + H T(W) - Tr(T(W)H) W ) = H_T - [Ω(H),W]; T = anisotropic mass-inertia tensor, Ẋ = T(W) X K.
- Non-normality: [A_intr, A_intr^T] ≠ 0; ||[A,A^T]|| ∝ Σ_{i<j}(t_i-t_j)^2 f(w); eigenvalues generally complex on regular stratum.
- Orthonormal basis E1..E5 (E1=diag(1,-1,0)/√2, E2=diag(1,1,-2)/√6, E3,E4,E5 off-diagonal symmetric/√2); shape modes E1,E2, shear modes E3-E5.
- 5x5 matrix block form [[A_shape, C],[C^T, A_shear]]. Shape block: A11=2(t1-t2)-(t1-t2)(w1-w2); A22=(2/3)[(t1+t2-2t3)-(t1+t2-2t3)(w1+w2-2w3)]; A12=√(2/3)[(t1-t3)w2-(t2-t3)w1]. Shear: S33=t1+t2-(t1-t2)(w1-w2)/(w1+w2-2w3); S44, S55 cyclic. Coupling C13∝(t1-t2)w3/(w1+w2-2w3), C14, C15 similarly ("refraction terms", proportional only — not exact).
- Collinear horizon w3=0: shear entries diverge; after regularization block-diagonalizes into finite 2x2 collinear block and 3x3 transverse block.
- Jordan structure: generic collinear horizon semi-simple; triple collision boundaries (w3=w2=0) Jordan block size 2; quadruple collision higher. "True defectiveness is therefore confined to higher-codimension strata."
- Block-triangular on B_ij: A(dW∥,dW⊥) = [[A∥∥, E_shear],[0, 2λ]]; lower-left block vanishes identically on wall; normal direction invariant sub-bundle suppressed.
- Thm 2 (Refraction law on binary hypersurfaces): transport cones tilt parallel to T_W B_ij; normal component governed by "inertial squeeze eigenvalue 2λ". (Derivation sketch only.)
- Thm 3 (Diagonalizability of collinear horizon): interior blocks diagonalizable; Jordan defectiveness only at w1→0 or w2→0 simultaneously with w3→0.
- Sec IV: 5x5 kinematic metric = real part of generalized QGT; dissipation bound well-defined on binary walls, forces transverse velocities to vanish on generic collinear horizon (statement only).
- Sec V: SVD numerical tracking protocol with SVD manifold projection after every RK update (described only; no numbers).
## Numerical results: NONE reported in this paper (no figures/numbers).
## Open problems: none enumerated; Conclusion says it "opens a direct route to arbitrary N-body systems".
## Flags
Non-normality (explicit), exceptional points/Jordan blocks and walls (binary walls as refraction sheets) — central. Smith disk/peel/offset/log-odds/census: absent (mentions "regularized trace-log functional" once in conclusion). Memory: none. Theorems are stated without grades; derivations are sketched (e.g. coupling block "proportional to").
Quote: "Aintr is non-normal: [Aintr,A^T_intr] ≠ 0." / "Binary walls function as continuous refraction sheets".
