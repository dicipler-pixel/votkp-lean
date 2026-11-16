# Reading notes: the FOUR-BODY paper (Jeromie Beasley)

Source: Google Drive file "4_Body_Prob (3).pdf", ID 1QCh2wgkoKkZjOWikWVsVmat5erNpzK5r.
Read through the Drive text reader (read_file_content). The text came back complete: page markers 1 to 11, ending with reference [10]. No truncation, so the base64 download was not needed. All 11 of 11 pages read.
Extraction quality: prose is clean; display equations came back broken across lines (fractions, square roots, matrices). Every equation below marked [rebuilt] was reassembled from the broken lines plus the surrounding sentence. Figures: none appear in the extracted text (no captions, no figure references). If the PDF holds images with no caption they were NOT READ (the text reader would not show them).

Convention in these notes: "PAPER" = what the text prints. "READER CHECK" = something I verified by my own algebra on the printed formulas; it is not in the paper.

---------------------------------------------------------------

## 1. What the paper is

- Title as printed: "The 5D Spectral Anatomy of Four-Body Obstructions: Kinematic Transport Geometry on Stratified Shape Manifolds"
- Author line as printed: "Jeromie N. Beasley", affiliation line "Program in Complex Spectral Geometry and Projector Dynamics".
- Date as printed: "(Dated: June 23, 2026)".
- Version: no version number printed in the paper. The Drive filename carries "(3)". It calls itself "Paper IV" and says it "completes the initial quadralogy".
- Length: 11 pages. 10 references.
- Place in his series, as the paper states it (p.1):
  - Paper I: "a coordinate-free spectral geometry of projectors, quantum geometric tensors (QGT), and dissipation bounds ... on abstract Grassmannian manifolds."
  - Paper II: realised that framework "on the 2D Kendall shape sphere (S2(3)) for the three-body problem, defining the 2 x 2 internal transport operator Aintr = J^T P_H T(w) J."
  - Paper III: "extended these transport mechanics to lattice dynamics under non-normal perturbations."
  - Paper IV (this one): lifts "the architectural spine -- transport operator -> spectrum -> admissible motion -- to the four-body problem."
- Stated objective (p.2): "not to solve the four-body equations of motion via traditional celestial mechanics. Instead, we derive the intrinsic 5 x 5 non-normal transport operator Aintr acting on T Sigma4 and map its spectral anatomy across the algebraic horizons of binary and higher-order collisions."

Section list as printed (the numbering is irregular in the source):
- I. INTRODUCTION (p.1-2), containing "Axiom (Reflective Closure of Transport)"
- II. KINEMATIC REDUCTION AND THE SHAPE MANIFOLD Sigma4 (p.2-3)
  - A. Mass-Weighted Binary-Wall Vectors Lij (p.3)
  - [unlettered paragraph "Connection to Refraction at Binary Walls" at top of p.4 -- same wording as subsection K; it appears BEFORE the coupling block C it talks about has been defined]
  - B. Principal Bundle Structure and Mechanical Connection (p.4-5)
  - "sectionThe Intrinsic Transport Operator and Its Non-Normality" (p.5) -- printed with the literal word "section" stuck on the front; it is an unnumbered heading, so the lettering C..L continues under II
  - C. Definition of the Intrinsic Transport Operator (p.5)
  - D. Non-Normality (p.6)
  - E. Orthonormal Tangent Basis for T_W Sigma4 (p.6)
  - F. Derivation of the 5x5 Matrix (p.7)
  - G. Explicit Symbolic Form of the Matrix (p.7-8)
  - H. Spectral Properties of Aintr (p.8)
  - I. Specialization to the Collinear Horizon (w3 = 0) (p.8)
  - J. Jordan Structure at the Boundaries (p.8)
  - K. Connection to Refraction at Binary Walls (p.8-9)
  - L. Derivation of the Block-Triangular Form (p.9), containing Theorem 2
- III. THE COLLINEAR HORIZON AND DIAGONALIZABILITY (p.10) -- Theorem 3
- IV. LINK TO QUANTUM GEOMETRIC TENSOR BOUNDS (p.10) -- two sentences
- V. NUMERICAL TRACKING PROTOCOL (p.10) -- one sentence
- VI. CONCLUSION (p.10-11)
- References [1]-[10] (p.11)

---------------------------------------------------------------

## 2. Objects and definitions (his names, his definitions)

Bodies and coordinates
- q1, q2, q3, q4 in R^3: "position vectors of the four particles with masses m1, m2, m3, m4" (p.2).
- "After center-of-mass removal, the configuration space is nine-dimensional." (p.2)
- rho_k (k = 1,2,3): "mass-weighted Jacobi vectors" (p.2-3). The paper does not print the Jacobi vectors themselves or the order in which bodies are added; it prints only the reduced masses and the L vectors.
- Reduced masses mu1, mu2, mu3: "the standard ones appearing in the Jacobi transformation" -- see equation (R) in section 3.

Configuration and shape
- X = [rho1, rho2, rho3] in R^{3x3}: "the configuration matrix" (columns are the three Jacobi vectors).
- M = X X^T in Sym+(3): "the kinematic inertia matrix is the Gram matrix". Also called (p.2) "the symmetric, positive-semidefinite kinematic inertia matrix M = XX^T ... our fundamental object".
- W = M / Tr(M), with Tr(W) = 1: "the scale-free shape matrix".
- Sigma4: "the manifold of trace-one positive-semidefinite symmetric matrices, stratified by collision type." Called "a five-dimensional stratified shape space" / "5-dimensional stratified manifold".
- T_W Sigma4: "consists of symmetric traceless matrices dW" (3x3; five independent components).
- w1, w2, w3: the eigenvalues of W in "the principal frame" W = diag(w1, w2, w3), with w1 + w2 + w3 = 1.

Collision structure
- sigma_ij(W) = L_ij W L_ij^T: the algebraic constraint function; binary collision of particles i, j (|q_i - q_j| = 0) is sigma_ij(W) = 0.
- L_ij: "mass-weighted binary-wall vectors", six explicit row vectors, eqs (1)-(6), "obtained by inverting the Jacobi reduction chain". "These vectors provide the precise bridge between the physical condition q_i = q_j and the algebraic hypersurface sigma_ij(W) = 0 on Sigma4."
- B_ij: the six "3D binary collision hypersurfaces" / "binary walls". Described as "continuous refraction sheets".
- C_coll: "the 3D collinear horizon", w3 = 0 with w1 + w2 = 1; "generic interior" means w1, w2 > 0.
- Triple collision boundaries: "e.g. w3 = w2 = 0".
- Quadruple collision point: named, no formula.
- N_ij: "the normal vector" to B_ij in T_W Sigma4 (used p.9; no formula printed for it).
- dW_par, dW_perp: decomposition of a tangent vector dW = dW_par + dW_perp relative to a wall; dW_par is defined by L_ij dW_par L_ij^T = 0 ("shape variations that preserve the collision constraint").

Bundle and connection
- P = { X in R^{3x3} | det X X^T > 0 }: "the total space of full-rank mass-weighted configuration matrices".
- pi : P -> Sigma4, X |-> W = X X^T / Tr(X X^T); "SO(3)-equivariant under the left action X |-> R X (R in SO(3))".
- V_X = { Omega X | Omega^T = -Omega }: "the vertical space at X (tangent to the SO(3)-orbit)".
- Inner product on the total space: Frobenius, <A, B> = Tr(A^T B).
- H_X: "horizontal space", the orthogonal complement of V_X; "delta X in H_X <=> X^T delta X is symmetric."
- P_H: "horizontal projector" / "mechanical connection projector" (Theorem 1).
- Omega(X, delta X): "the connection form". Abstract calls the connection "a non-Abelian SO(3) instanton-like connection"; the body calls it the "Mechanical Connection".

Transport
- T(W) (also written T(w)): "the 3 x 3 anisotropic mass-inertia tensor expressed in the principal frame of W". No explicit formula for T(W) is printed anywhere in the paper.
- t1, t2, t3: appear in eqs (10)-(18) and the non-normality formula. The paper never defines them in words; from their use they are the principal-frame diagonal entries of T(W). (This identification is my reading of usage, not a printed definition.)
- K: in X-dot = T(W) X K, "K encodes the driving angular and deformation velocities." No further definition.
- Aintr: "the intrinsic (rotation-free) transport operator on T_W Sigma4", a 5x5 operator, "the horizontal projection of the non-commuting anisotropic mass-inertia tensor" (abstract). Definition in section 3, eq (D1).
- H_T: "raw symmetrized term" (eq D3).
- Omega(H) = skew(H W^{-1}): "connection correction".
- E1..E5: orthonormal basis of T_W Sigma4 under the Frobenius inner product. "E1, E2 control shape deformations while E3, E4, E5 control shear modes."
- A_shape (2x2, indices 1,2), A_shear (3x3, indices 3,4,5), C ("coupling block" / "shear coupling block (refraction terms)"): the blocks of the 5x5 matrix.
- Transport cones: never given a formula. Stated properties: "Its singular values control the local geometry of transport cones" (p.6); "The singular values of Aintr determine the geometry of the transport cones" (p.8); cones "flatten parallel to the wall".
- lambda: "the local mass-density eigenvalue associated with the colliding pair", lambda > 0. 2 lambda is "the inertial squeeze eigenvalue".
- E_shear: "the off-diagonal geometric shear generated by the remaining particles".
- "Directional protection": the mechanism "previously identified on the shape sphere" (Paper II); here realised as suppression of motion normal to a binary collision hypersurface.

Objects imported from Paper I (restated p.2)
- Q_Pi(V, W) = Tr(Pi V W): "the intrinsic tensor ... on the Grassmannian" (here W is a tangent vector, not the shape matrix).
- g_Pi: "unified quantum metric"; Omega_Pi: "Berry curvature".
- C(V) = g_Pi(V, V): "the transport capacity".
- theta_G: "the intrinsic Grassmannian angle".

Axiom (Reflective Closure of Transport) -- verbatim, p.2
"All admissible transport is defined by closure under projection onto the tangent Grassmannian bundle. Any attempted evolution that fails exact closure generates an induced projection defect. The transport dynamics therefore consist not only of the projected motion itself but also of the backreaction generated by this projection defect.
Consequently, transport, obstruction, refraction, and persistence are not independent structures. They arise from a single reflective process in which admissible motion is continually projected back into the allowable tangent geometry."

---------------------------------------------------------------

## 3. Equations in order

Numbered equations in the paper are (1)-(18). Unnumbered displays are given letter tags here (my tags, for reference only).

p.1 (Paper II recalled, inline)
(P2) Aintr = J^T P_H T(w) J   -- the 2x2 internal transport operator of the three-body paper. J is not defined in this paper.

p.2
(I1) M = X X^T   (inline)
(I2) Q_Pi(V, W) = Tr(Pi V W)   (inline)
(I3) [rebuilt] |Omega_Pi(V, W)| <= 2 sqrt( C(V) C(W) ) sin theta_G
     Printed as "|Omega_Pi(V,W)| <= 2 / p / C(V)C(W) sin theta_G" with the root sign extracted as a stray "p". Called "the sharp inequality". C(V) = g_Pi(V,V).

p.3
(S1) X = [rho1, rho2, rho3] in R^{3x3}
(S2) M = X X^T in Sym+(3)
(S3) [rebuilt] W = M / Tr(M),  Tr(W) = 1
(S4) [rebuilt] sigma_ij(W) == L_ij W L_ij^T = 0

Numbered (1)-(6), all [rebuilt] from broken fraction lines; each is a row vector of three entries:
(1) L12 = [ 1/sqrt(mu1), 0, 0 ]
(2) L23 = [ -(m1/(m1+m2)) (1/sqrt(mu1)),  1/sqrt(mu2),  0 ]
(3) L13 = [ (m2/(m1+m2)) (1/sqrt(mu1)),  1/sqrt(mu2),  0 ]
(4) L34 = [ 0,  -((m1+m2)/(m1+m2+m3)) (1/sqrt(mu2)),  1/sqrt(mu3) ]
(5) L24 = [ -(m1/(m1+m2)) (1/sqrt(mu1)),  (m3/(m1+m2+m3)) (1/sqrt(mu2)),  1/sqrt(mu3) ]
(6) L14 = [ (m2/(m1+m2)) (1/sqrt(mu1)),  (m3/(m1+m2+m3)) (1/sqrt(mu2)),  1/sqrt(mu3) ]

(R) [rebuilt] reduced masses:
    mu1 = m1 m2 / (m1 + m2)
    mu2 = (m1 + m2) m3 / (m1 + m2 + m3)
    mu3 = (m1 + m2 + m3) m4 / (m1 + m2 + m3 + m4)

READER CHECK on (1)-(6): with r1 = q2 - q1, r2 = q3 - (centre of mass of 1,2), r3 = q4 - (centre of mass of 1,2,3) and rho_k = sqrt(mu_k) r_k, I get q2-q1, q3-q2, q3-q1, q4-q3, q4-q2, q4-q1 with exactly the coefficients printed in (1)-(6). So the six vectors are mutually consistent with that Jacobi ordering (1, then 2, then 3, then 4). The paper does not print this ordering; it follows from the L vectors.

READER CHECK on (S4): q_i - q_j = X L_ij^T (X has the rho_k as columns, L_ij is a 1x3 row of coefficients on rho1, rho2, rho3). So |q_i - q_j|^2 = L_ij (X^T X) L_ij^T. The matrix that pairs with L_ij is X^T X (the 3x3 matrix of dot products rho_a . rho_b), while the paper defines M = X X^T (which sits in physical space and transforms as R M R^T under rotation). X X^T and X^T X have the same eigenvalues w1, w2, w3 but are different matrices. The paper as printed uses X X^T throughout and applies L_ij to it. Under the left action X -> R X that the paper names, X X^T is not rotation-invariant and X^T X is. This is a printed-text mismatch a follow-up question may hit; it is recorded here, not repaired.

p.4
(B1) P = { X in R^{3x3} | det X X^T > 0 }
(B2) [rebuilt] pi : P -> Sigma4,  X |-> W = X X^T / Tr(X X^T)
(B3) [rebuilt] V_X = { Omega X | Omega^T = -Omega }
(B4) <A, B> = Tr(A^T B)
(B5) [rebuilt] delta X in H_X  <=>  X^T delta X is symmetric
Theorem 1 displays:
(T1a) P_H(delta X) = delta X - Omega(X, delta X) X
(T1b) [rebuilt] Omega(X, delta X) = skew( delta X X^T (X X^T)^{-1} )
      Printed: "Omega(X, delta X) = skew delta X X^T (XX^T)^-1." -- the brackets after skew were lost in extraction; I read skew as acting on the whole product, by analogy with (T1e) where the brackets are printed.
(T1c) delta W = delta X X^T + X delta X^T   "(normalized appropriately)"
(T1d) P_H(delta W) = delta W - [Omega, W]
(T1e) Omega = skew( delta W W^{-1} )
p.5
(T1f) [rebuilt] in the principal frame W = diag(w1, w2, w3):
      Omega_ij = delta W_ij / (w_i - w_j)  (i != j),   Omega_ii = 0
      "This projector defines the unique rotation-free (horizontal) lift of tangent vectors on Sigma4."

p.5
(K1) [rebuilt] X-dot = T(W) X K     ("In the unreduced picture the kinematic evolution takes the form")
(D1) [rebuilt] Aintr(H) = P_H( T(W) H + H T(W) - Tr(T(W) H) W ),  for H in T_W Sigma4 symmetric and traceless.
     Printed with the brackets lost: "Aintr(H) = PH / T(W)H + HT(W) - Tr T(W)H&#1;W". The closing-bracket glyph came through as the entity "&#1;". The grouping is fixed by (D3) and (F1).
(D2) Aintr(H) = H_T - [Omega(H), W]    ("Equivalently, in closed algebraic form")
(D3) [rebuilt] H_T = T(W) H + H T(W) - Tr(T(W) H) W
(D4) Omega(H) = skew( H W^{-1} )

p.6
(N1) [Aintr, Aintr^T] != 0
(N2) [rebuilt] || [Aintr, Aintr^T] || proportional to  sum_{i<j} (t_i - t_j)^2 f(w1, w2, w3)
     "where f is a rational function of the eigenvalues of W arising from the connection terms." f is not given. Whether f sits inside or outside the sum is not recoverable from the print; on p.8 the same formula is printed with a dot: sum_{i<j} (t_i - t_j)^2 . f(w1,w2,w3).
(E0) W = diag(w1, w2, w3),  w1 + w2 + w3 = 1

Numbered (7)-(9) [rebuilt from matrix rows printed one per line]:
(7) E1 = (1/sqrt2) [[1,0,0],[0,-1,0],[0,0,0]]
    E2 = (1/sqrt6) [[1,0,0],[0,1,0],[0,0,-2]]
(8) E3 = (1/sqrt2) [[0,1,0],[1,0,0],[0,0,0]]
    E4 = (1/sqrt2) [[0,0,1],[0,0,0],[1,0,0]]
(9) E5 = (1/sqrt2) [[0,0,0],[0,0,1],[0,1,0]]
(E6) Tr(E_a E_b) = delta_ab

p.7
(F1) [rebuilt] Aintr(dW) = P_H( T(w) dW + dW T(w) - Tr(T(w) dW) W )
(F2) [rebuilt] (Aintr)_ab = Tr( E_a . Aintr(E_b) )    "by direct substitution"
(F3) [rebuilt] (Aintr)_ab = [[ A_shape, C ],[ C^T, A_shear ]]
     Note: the lower-left block is printed as C^T. A matrix with symmetric diagonal blocks and lower-left = C^T is symmetric, which sits against the paper's statement that Aintr is non-normal. The paper does not comment on this. (Reader observation; A_shape is given by A11, A22, A12 only -- no separate A21 is printed.)

Shape block (indices 1, 2), numbered:
(10) A11 = 2(t1 - t2) - (t1 - t2)(w1 - w2)
(11) [rebuilt] A22 = (2/3) [ (t1 + t2 - 2 t3) - (t1 + t2 - 2 t3)(w1 + w2 - 2 w3) ]
(12) [rebuilt] A12 = sqrt(2/3) [ (t1 - t3) w2 - (t2 - t3) w1 ]
     Printed "r2 / 3" for the root; I read sqrt(2/3). It could also be sqrt(2)/3 -- the extraction does not settle which. Flag if this number matters.

Shear block (indices 3, 4, 5), numbered, all [rebuilt]:
(13) S33 = t1 + t2 - (t1 - t2)(w1 - w2) / (w1 + w2 - 2 w3)
(14) S44 = t1 + t3 - (t1 - t3)(w1 - w3) / (w1 + w3 - 2 w2)
(15) S55 = t2 + t3 - (t2 - t3)(w2 - w3) / (w2 + w3 - 2 w1)
     Only the diagonal shear entries are printed. Off-diagonal shear entries (S34, S35, S45): NOT IN PAPER.

Shear coupling block, numbered, [rebuilt]. These are proportionalities, "the leading contributions", not equalities:
(16) C13 proportional to (t1 - t2) . w3 / (w1 + w2 - 2 w3)
(17) C14 proportional to (t1 - t3) . w2 / (w1 + w3 - 2 w2)
(18) C15 proportional to (t2 - t3) . w1 / (w2 + w3 - 2 w1)
     "The off-diagonal entries C_ij are proportional to differences (t_i - t_j) multiplied by geometric factors from the horizontal projection." "These terms generate the triangular structure near binary walls."
     Entries C23, C24, C25: NOT IN PAPER.

READER CHECK on (10): substituting (D3) with E1 and diagonal T = diag(t1,t2,t3), W = diag(w1,w2,w3), the raw term gives Tr(E1 H_T) = (t1 + t2) - (1/2)(t1 - t2)(w1 - w2), not 2(t1 - t2) - (t1 - t2)(w1 - w2). [T E1 + E1 T = sqrt2 diag(t1, -t2, 0); Tr(T E1) = (t1 - t2)/sqrt2; Tr(E1 W) = (w1 - w2)/sqrt2. E1 is diagonal so the connection correction Omega(E1) vanishes in the principal frame.] So (10) as printed does not follow from (D1)-(D3) by direct substitution with a diagonal T. Recorded, not repaired. I did not check (11)-(18) the same way.

READER CHECK on the denominators: with w1 + w2 + w3 = 1, w1 + w2 - 2 w3 = 1 - 3 w3, which is zero at w3 = 1/3, and equals 1 at w3 = 0. Likewise w1 + w3 - 2 w2 = 1 - 3 w2 and w2 + w3 - 2 w1 = 1 - 3 w1. So the printed entries (13)-(18) are singular where one eigenvalue equals 1/3, and are finite at the collinear horizon w3 = 0. The paper (subsection I) says "When w3 = 0 ... several entries in the shear block diverge." The printed (13)-(15) do not diverge there; the divergence at w3 = 0 that the printed formulas do carry is in W^{-1} inside (T1e)/(D4). The connection components (T1f) diverge where two eigenvalues are equal (w_i = w_j).

p.8
(H1) same as (N2), with A^T: || [Aintr, Aintr^T] || proportional to sum_{i<j} (t_i - t_j)^2 . f(w1, w2, w3)

p.9
(L1) L_ij dW_par L_ij^T = 0
(L2) Aintr(dW_par) in T_{W0} B_ij
(L3) [rebuilt] T(w) N_ij + N_ij T(w) = 2 lambda N_ij + E_shear,  lambda > 0
(L4) [rebuilt] Aintr (dW_par ; dW_perp) = [[ A_parpar, E_shear ],[ 0, 2 lambda ]] (dW_par ; dW_perp)
     "The lower-left block vanishes identically on the wall."
     Condition stated just before: "On B_ij the configuration remains non-collinear (det(W0) > 0), so the horizontal projector P_H is smooth and bounded."

No equations in sections III, IV, V, VI.

---------------------------------------------------------------

## 4. Results with the grade the paper itself gives

The paper has no grading scheme (no "proved / checked / conjecture" labels). What it gives is: three items headed "Theorem", an "Axiom", and the verbs "we derive", "we prove", "we demonstrate" in the abstract. Below, "grade in paper" is the paper's own wording; "support printed" is what is actually on the page.

R1. Axiom (Reflective Closure of Transport). Grade in paper: Axiom (assumed). Text in section 2.

R2. Reduction: nine-dimensional configuration space -> five-dimensional stratified shape space Sigma4 = trace-one positive-semidefinite symmetric 3x3 matrices, tangent space = symmetric traceless matrices. Grade in paper: stated as construction ("Thus Sigma4 is ..."). Support printed: the definitions X, M, W.

R3. Six binary walls as algebraic hypersurfaces sigma_ij(W) = L_ij W L_ij^T = 0 with the explicit L_ij of (1)-(6). Grade in paper: explicit, "obtained by inverting the Jacobi reduction chain". Support printed: the vectors; the inversion itself is not shown.

R4. Theorem 1 (Mechanical Connection / Horizontal Projector): P_H(delta X) = delta X - Omega(X, delta X) X with Omega = skew(delta X X^T (X X^T)^{-1}); on the base P_H(delta W) = delta W - [Omega, W], Omega = skew(delta W W^{-1}); principal-frame components Omega_ij = delta W_ij/(w_i - w_j). Grade in paper: Theorem. Support printed: statement only, no proof text.

R5. Definition of Aintr (D1)-(D4) and its 5x5 matrix with blocks A_shape, C, A_shear, entries (10)-(18). Grade in paper: "We derive the explicit 5 x 5 intrinsic transport operator"; matrix elements "by direct substitution". Support printed: final entries only; the diagonal shape and shear entries are equalities, the coupling entries (16)-(18) are proportionalities ("leading contributions"); several entries are not printed (see section 3).

R6. Non-normality: [Aintr, Aintr^T] != 0 "whenever T(w) is anisotropic", with norm proportional to sum (t_i - t_j)^2 f(w); "On the regular stratum the eigenvalues of Aintr are generally complex. Its singular values control the local geometry of transport cones." Grade in paper: asserted with a reason ("Because the inertia tensor T(W) does not commute with a generic shape matrix W, and because the mechanical connection introduces an additional skew-symmetric correction"). Support printed: no computation; f not given.

R7. Theorem 2 (Refraction Law on Binary Hypersurfaces), verbatim: "Let B_ij be any of the six binary collision hypersurfaces. For a tangent vector decomposed as dW = dW_par + dW_perp, the transport operator takes the block-triangular form above. As a trajectory approaches B_ij, incoming transport cones tilt their opening angles parallel to T_W B_ij, forcing continuous kinematic refraction along the wall interface. The normal component is governed by the inertial squeeze eigenvalue 2 lambda."
   Grade in paper: Theorem; abstract says "We prove that the six distinct 3D binary collision hypersurfaces (B_ij) act as continuous refraction sheets where transport cones flatten parallel to the wall face."
   Support printed: subsection L, a two-bullet argument (parallel component maps into the parallel tangent space; normal component gives 2 lambda N_ij + E_shear), giving the block-triangular form (L4). lambda and E_shear are named, not computed.
   Consequences the paper draws (p.9-10): "the normal direction forms an invariant sub-bundle that is strongly suppressed relative to the parallel dynamics"; "motion normal to any binary collision hypersurface is geometrically suppressed"; "Only those trajectories whose incoming parallel component lies in a symmetry of the shear tensor E_shear can maintain a finite normal velocity for appreciable time; all others are forced to skim along the wall." "This constitutes a higher-dimensional instance of the variational refraction across rank-drop interfaces analyzed on the three-body shape sphere."

R8. Collinear horizon specialisation (subsection I): "When w3 = 0 (with w1 + w2 = 1), several entries in the shear block diverge. After regularization, the matrix block-diagonalizes into a finite 2 x 2 collinear block and a 3 x 3 transverse block with large but finite eigenvalues." Grade in paper: stated. Support printed: none; the regularization is not specified.

R9. Jordan structure (subsection J):
   - "Generic collinear horizon (w3 = 0, w1, w2 > 0): The operator is semi-simple (fully diagonalizable). Geometric multiplicity equals algebraic multiplicity."
   - "Triple collision boundaries (e.g. w3 = w2 = 0): Repeated eigenvalues appear in the transverse block and a non-trivial Jordan block of size 2 emerges."
   - "At the quadruple collision point the degeneracy is higher."
   - "True defectiveness is therefore confined to higher-codimension strata."
   Grade in paper: stated. Support printed: none (no eigenvalues, no block shown).

R10. Theorem 3 (Diagonalizability of the Collinear Horizon), verbatim: "On the interior of the collinear horizon C_coll (where w1, w2 > 0), Aintr block-diagonalizes into a 2 x 2 collinear block and a 3 x 3 transverse block. Both blocks are diagonalizable. True Jordan-block defectiveness occurs only at the lower-dimensional strata where w1 -> 0 or w2 -> 0 simultaneously with w3 -> 0."
   Grade in paper: Theorem; abstract says "we demonstrate that the 3D collinear horizon (C_coll) remains semi-simple and fully diagonalizable across its generic interior, meaning true Jordan block defectiveness and Exceptional Points (EPs) are structurally confined to lower-dimensional multi-body collision manifolds."
   Support printed: statement only, no proof text.

R11. Link to QGT bounds (section IV, the whole section): "The 5 x 5 kinematic metric on Sigma4 is the real part of the generalized QGT from Paper I. The dissipation bound remains well-defined on binary walls and forces transverse velocities to vanish on the generic collinear horizon." Also p.7: the non-normality and complex eigenvalues of Aintr "mirror the interplay between the real (metric) and imaginary (curvature) parts of the intrinsic Quantum Geometric Tensor on the Grassmannian"; p.2: the present work "realizes the classical kinematic analogue of this structure".
   Grade in paper: stated identification / analogue ("mirror", "analogue"). Support printed: none; the "5 x 5 kinematic metric" is not written out.

R12. Numerical tracking protocol (section V, the whole section): "A coordinate-free integration scheme using SVD of the transport operator at each step, with manifold projection via SVD after every Runge-Kutta update." Abstract: "present a coordinate-free numerical tracking protocol using Singular Value Decomposition (SVD) to visualize these flattening transport cones in a simulated 5D flow."
   Grade in paper: a protocol description. Support printed: one sentence. No run, no output, no figure, no code, no step size, no Runge-Kutta order.

R13. Conclusion claims: "the structural spine -- transport operator to spectrum to admissible motion -- extends rigorously to the four-body problem"; "The generic collinear horizon ... remains only mildly degenerate, with true defectiveness confined to lower-dimensional strata"; the result "opens a direct route to arbitrary N-body systems through the same Grassmannian and obstruction-theoretic framework."
   The conclusion also mentions "the regularized trace-log functional" ("When combined with the regularized trace-log functional and the SVD-based numerical protocol ..."). This functional is NOT defined or used anywhere in the body of this paper.

---------------------------------------------------------------

## 5. Numbers

The paper contains no measured data, no numerical results, no physical constants and no units. Every number in it is a dimension, a count, or a normalisation:

- 4 bodies, in 3-dimensional physical space.
- 9: dimension of configuration space after centre-of-mass removal.
- 5: dimension of the shape space Sigma4 and of T_W Sigma4; Aintr is 5 x 5.
- 3 x 3: size of X, M, W, T(W).
- 6: number of binary collision hypersurfaces B_ij (pairs 12, 23, 13, 34, 24, 14, in the paper's order).
- 3: Jacobi vectors rho1..rho3; reduced masses mu1..mu3; eigenvalues w1..w3 with w1 + w2 + w3 = 1 (Tr W = 1).
- Block sizes: shape block 2 x 2 (indices 1,2), shear block 3 x 3 (indices 3,4,5); at the collinear horizon a 2 x 2 collinear block and a 3 x 3 transverse block.
- Jordan block of size 2 at triple collision boundaries.
- Basis normalisations: 1/sqrt2 (E1, E3, E4, E5), 1/sqrt6 (E2).
- Coefficients in the matrix entries: 2 in A11; 2/3 in A22; sqrt(2/3) (or sqrt2/3 -- extraction ambiguous) in A12; factor 2 in the bound (I3) and in the squeeze eigenvalue 2 lambda.
- 2 x 2: size of the three-body operator of Paper II, on the 2D shape sphere S2(3).
- Date June 23, 2026. 11 pages. 10 references. 18 numbered equations. 3 theorems. 1 axiom.

No masses are given numerical values. No specific system (no star, planet, moon) is named.

---------------------------------------------------------------

## 6. Limits and open items

Limits the paper states itself
- It does not solve the equations of motion: "not to solve the four-body equations of motion via traditional celestial mechanics".
- P is restricted to full rank, det X X^T > 0; the connection formulas use (X X^T)^{-1} and W^{-1}, so they are stated only off the collinear horizon. On a binary wall the paper requires "the configuration remains non-collinear (det(W0) > 0)" for P_H to be "smooth and bounded".
- At w3 = 0 "several entries in the shear block diverge" and a regularization is needed.
- Coupling entries (16)-(18) are given only as "leading contributions" up to proportionality.
- Defectiveness (Jordan blocks, Exceptional Points) is stated to live only on lower-dimensional multi-body collision strata; at the quadruple collision point "the degeneracy is higher" (not characterised).
- N-body extension is a "direct route" that is opened, not done.

Things the paper uses but does not print (answer "not in the paper" if asked)
- The explicit form of T(W), and any definition of t1, t2, t3.
- K in X-dot = T(W) X K.
- The Jacobi vectors themselves and the ordering convention (only recoverable from L_ij; see reader check).
- The function f(w1, w2, w3) in the non-normality norm.
- Off-diagonal shear entries, coupling entries C2x, and any A21 distinct from A12.
- The normal vector N_ij, the values of lambda and E_shear.
- The regularization at w3 = 0, and the 2 x 2 collinear / 3 x 3 transverse blocks.
- Proofs of Theorem 1 and Theorem 3.
- The "5 x 5 kinematic metric" and the form of the "dissipation bound" on Sigma4.
- The "regularized trace-log functional" (named only in the conclusion).
- A definition of "transport cone" as a formula.
- Any numerical run, figure, code, or table.
- J in the recalled three-body formula Aintr = J^T P_H T(w) J.

Text-level defects in this file version
- The paragraph "Connection to Refraction at Binary Walls" is printed twice: top of p.4 (out of place, before C is defined) and as subsection K on p.8-9.
- The non-normality paragraph and formula are printed twice (D on p.6, H on p.8) and a third short version sits at the top of p.7.
- A heading is printed as "sectionThe Intrinsic Transport Operator and Its Non-Normality" (broken heading command), so section numbers jump from II straight to III with subsections A-L all under II.
- Lost closing brackets in the Aintr definitions (printed as a control character).

Reader checks that found mismatches in the printed mathematics (my algebra, not the paper's words; none repaired here)
1. L_ij pairs with X^T X, not with X X^T as defined (section 3, check on S4).
2. The block form (F3) with lower-left C^T and a single A12 describes a symmetric matrix, against the stated non-normality.
3. A11 in (10) does not come out of (D1)-(D3) by direct substitution with diagonal T (I get (t1 + t2) - (1/2)(t1 - t2)(w1 - w2)).
4. The printed denominators in (13)-(18) vanish at w_k = 1/3, not at w3 = 0, so they do not show the divergence at the collinear horizon that subsection I describes.
5. Theorem 2's block-triangular form (L4) has a zero lower-left block and upper-right E_shear; whether "normal direction forms an invariant sub-bundle" matches that triangle orientation depends on the ordering convention, which the paper does not spell out. With the printed matrix acting on the column (dW_par ; dW_perp), the output's perpendicular part is 2 lambda dW_perp alone, and the parallel part receives E_shear dW_perp.

---------------------------------------------------------------

## 7. What bears on the team's questions

(a) Placing several equal balls on a hyperbolic field so light/energy passes from one to the next
- Nothing in this paper addresses this. The words "hyperbolic", "ball", "light", "energy" (as a transfer quantity) and "photon" do not occur. There is no field in the paper other than the tensor fields on Sigma4.
- The nearest things it does contain, in its own terms:
  - A rule for what happens to transport near a wall: Theorem 2 -- cones "flatten parallel to the wall", normal motion suppressed by 2 lambda, trajectories "forced to skim along the wall" unless the incoming parallel component "lies in a symmetry of the shear tensor E_shear". It is a statement about shape-space motion at a binary collision hypersurface, not about passage between bodies.
  - The word "refraction" is used throughout for this wall behaviour ("continuous refraction sheets", "geometric refraction law", "variational refraction across rank-drop interfaces").
  - The Axiom (Reflective Closure of Transport): admissible motion is "continually projected back into the allowable tangent geometry", with a "projection defect" and its "backreaction".
  - Equal masses: the paper keeps m1..m4 general and never specialises to equal masses. (The three-body paper is the equal-mass one per its title in the team's index; this paper does not say so.)
- Any use of this paper for balls on a hyperbolic field would be an extension the paper does not make.

(b) Sun with four planets (Mercury, Venus, Earth, Mars), or Sun-Earth-Moon
- Not in the paper. No celestial body is named, no mass values, no orbits, no gravitational potential. The paper is purely kinematic: there is no force law in it at all (the only evolution equation is X-dot = T(W) X K with K undefined).
- Count check against what is asked: Sun + four planets is FIVE bodies; this paper is four bodies (three Jacobi vectors, 3 x 3 X). Sun-Earth-Moon is three bodies, which is Paper II's case (2 x 2 Aintr on the shape sphere), not this paper's.
- What it would supply for a four-body system such as Sun + three bodies: the reduced masses (R), the six wall vectors (1)-(6) for general masses, the shape matrix W, and the wall/horizon classification. With strongly unequal masses nothing changes in the formulas; the paper gives no hierarchical (large central mass) limit.
- The only pointer toward more bodies is the conclusion sentence: "opens a direct route to arbitrary N-body systems through the same Grassmannian and obstruction-theoretic framework."

(c) How the four-body case extends the three-body one (the paper's own account)
- Shape space: 2D Kendall shape sphere S2(3) -> 5-dimensional stratified manifold Sigma4 of trace-one positive-semidefinite symmetric 3 x 3 matrices.
- Operator: 2 x 2 Aintr = J^T P_H T(w) J -> 5 x 5 Aintr(H) = P_H( T(W) H + H T(W) - Tr(T(W) H) W ) on symmetric traceless H.
- Connection: now "a non-Abelian SO(3) instanton-like connection" (the rotation group in 3D), given by Theorem 1.
- The spine is kept unchanged: "transport operator -> spectrum -> admissible motion".
- The transition is described as "a clean scaling of tensor fields over a non-Abelian gauge connection".
- Walls: six binary collision hypersurfaces B_ij instead of the three-body collision set; the wall behaviour is "a higher-dimensional instance of the variational refraction across rank-drop interfaces analyzed on the three-body shape sphere" and "a concrete realization, in the four-body setting, of the directional protection mechanism previously identified on the shape sphere".
- New in four bodies: the collinear horizon C_coll (w3 = 0) as a 3D stratum that stays diagonalizable in its interior; defectiveness only at triple (Jordan block of size 2) and quadruple collision strata.
- Block structure new to this case: shape block (E1, E2) / shear block (E3, E4, E5) / coupling block C.

(d) Gram matrices
- This is the central object. "The kinematic inertia matrix is the Gram matrix M = X X^T in Sym+(3)", X = [rho1, rho2, rho3]; called "our fundamental object", used so as to "bypass coordinate-dependent tracking and isolate pure geometric obstructions".
- Normalised Gram: W = M / Tr(M), Tr W = 1. Sigma4 is the space of such W.
- Collision conditions are quadratic forms in the Gram matrix: sigma_ij(W) = L_ij W L_ij^T = 0.
- Rank language: binary walls keep det(W0) > 0; the collinear horizon is w3 = 0 (rank drop); triple collision w3 = w2 = 0.
- See the reader check in section 3: the Gram matrix of the Jacobi vectors in the usual sense (dot products rho_a . rho_b) is X^T X; the paper writes X X^T. Same eigenvalues, different matrix; the L_ij formula needs X^T X.

(e) Leading eigenvectors
- The phrase "leading eigenvector" does not occur, and no eigenvector of anything is singled out or computed.
- What the paper does use: the principal frame of W (its eigenvector frame) with eigenvalues w1, w2, w3; the principal values t_i of T(W); the eigenvalues of Aintr ("generally complex" on the regular stratum); the singular values of Aintr ("control the local geometry of transport cones"); the "local mass-density eigenvalue" lambda and "inertial squeeze eigenvalue" 2 lambda at a wall; geometric vs algebraic multiplicity and Jordan blocks at the strata; SVD of the transport operator at each step in the numerical protocol.
- No ordering of eigenvalues (largest / smallest) is stated, and no "dominant direction" is defined. The only direction singled out is the wall normal N_ij, which Theorem 2 treats as the suppressed direction with eigenvalue 2 lambda.
