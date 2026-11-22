# Where does "non-Riemannian" belong? — working notes (22 Nov 2026)
Rule from Jeromie 10:09: take notes, keep all the good math, take every claim out and check it in new ways if needed.

## Read so far
- IQGT June 13 (22), June 13 (28), June 17 (29,35,36), June 19 (142):
  all say g_Π(V,W)=½Tr(VW) "is the intrinsic Hilbert–Schmidt Riemannian metric";
  §4.1 "the intrinsic metric pulls back to a Riemannian metric on M". Ref [3] Provost–Vallée "Riemannian structure".
  NOTE: the June 13 (28) and later already carry the sharpened bound with −g(V,W)² and the "angle safeguard".
- "IQGT not the standard" discussion (28 Oct): intrinsic g is positive definite (C1 ratio 1.000000 over 300 cases),
  Kähler (C2, 1e-14); only PULLBACKS degenerate (fold: det g → 0 while intrinsic g on unit X = 1).
  Curvature half needs no base metric (Chern 1.00003 / 0.99999999 on two charts).

## Every IQGT version read for the word
- June 13 (22),(28); June 17 (29),(35),(36); June 19 (142); June 20 Intrinsic_qm_conj (40); Aug 5 "Intrinsic Quantum Geometric Tensor";
  v7.3.1 html: ALL call g "the intrinsic Hilbert–Schmidt Riemannian metric"; none says non-Riemannian.
- Aug 5 adds: Q_Π(A,A)=‖AΠ‖²≥0, definite on real tangent; pullback degenerate where γ fails to immerse (Prop 4.3).
- June 18 "Spectral Mechanics of Non-Normal Multi-History Operators: Foundations for PREMETRIC Covariance Continuation":
  H_N = D + A non-normal, [H,Hᵀ]=2[A,D]; "explicitly metric-free". = his "premetric" origin (he later stopped using the word).

## Where "non-Riemannian" actually appears in his corpus
1. galaxy_holes_v2 (17 Sep) §11: "the non-Riemannian metric tensor of the refraction sector transforms as
   g̃αβ(θ,I) = gαβ(θ) + χ(I)(∂Fα/∂I θβ + ∂Fβ/∂I θα) + σ_EP δαβ (I−I_c)^(−1/2)" (Bezold–Brücke). Rev 4 (25 Sep) keeps it as [H]
   and cites Bujack et al. PNAS 119 e2119753119 (2022) "The non-Riemannian nature of perceptual color space" and Bujack 2025 CGF.
2. Atlas B15 (FOFT v2 §13.3, COLOR-LEDGER-01): trace-log ledger S(A,B)=log det((A+B)/2) − ½log det A − ½log det B is
   "locally Riemannian, globally subadditive"; √S → d_R/(2√2); accumulated/direct 1.005,1.017,1.062,1.124,1.192 at log κ=1,2,4,6,8;
   Riemannian control 1.000. "Diminishing returns are the shape of the geometry". Closed: "comparison with human colour perception is a cited analogy".
3. Atlas B23 (gates B23-GATE-01/02): non-Hermitian two-band H=[[0,1],[z,0]]: biorthogonal Q=(1/16z²)[[−1,−i],[−i,1]], Ω≡0,
   det g = −|1/16z²|²: "the metric itself has gone indefinite"; 200/200 random two-band families break at γ=0.01.
4. Cone paper v1–v8 (Aug 18–19): measured Lorentzian cone of the non-Hermitian quantum metric; nulls 7.963/172.037 deg;
   his push 19 Aug "we can easily solve the open problem... non riemann curves".
5. A Constant With No Bulk (Sep): "Signature. The metric here is Riemannian on the projector bundle. Pseudo-Hermiticity gives a candidate
   mechanism — one conjugate pair forces a Lorentzian sector".
6. LANL colour fits (24 Oct review / What the Present Keeps §5.4): ledger curve beats log on held-out units, −0.0002 to −0.0003 nats/response.
7. Black Hole v8.4 (B36): oriented quotient "a smooth Riemannian manifold through the wall" — a Riemannian statement, not the word.
## Element paper v1.2.1 still says (02_wall.md §2.7 line 63): "Its curvature is non-Riemannian" — inconsistent with §6 fix. Must settle.

## Checks run (NONRIEMANN-WHERE-01, output in nonriemann_checks_output.txt) — every claim taken out and checked a new way
- C1 Hermitian intrinsic g: g(V,V)/‖X‖² = 1.000000000000 over 300 random cases (tangents built as i[A,P], not from blocks);
  6×6 Gram positive definite. RIEMANNIAN. Its Gaussian curvature on CP¹ = 4.000000 at three angles (ordinary, finite).
  Berry Ω = ½ sinθ dθ∧dφ = Kähler form (2× area form), not the Riemann tensor. => "its curvature is non-Riemannian" is wrong for the Hermitian tensor.
- C2 trace-log ledger (Atlas B15) is the non-Riemannian object: scalar closed form proved numerically to 20 digits
  S = log cosh(½ ln(I/J)) = −½ ln(1−Γ²), Γ = (I−J)/(I+J) = tanh(½ ln(I/J)) = THE PEEL COORDINATE.
  At the peel wall z = 3+2√2: Γ² = ½ and S = ½ ln 2 exactly.  Local √S/d_R = 0.353553390593 = 1/(2√2).
  Not additive: accumulated/direct (scalar) 1.020, 1.074, 1.229, 1.396, 1.555 at ln-contrast 1,2,4,6,8;
  (4×4 family) 1.016, 1.057, 1.179, 1.312, 1.441; Riemannian control 1.000000 every time.
  B15's own numbers (1.005 … 1.192) come from its own family; mine differ in size, agree in kind. NOT reproduced digit-for-digit.
- C3 non-Hermitian: H=[[0,1],[z,0]] biorthogonal Q matches (1/16z²)[[−1,−i],[−i,1]] to 1e-11; Ω = 0 (1e-12);
  det(Re g) = −|1/16z²|² exactly at three z. Hermitian control det>0. Cone point d=(2,0,0.4+0.6i): Re g eigenvalues −1.27e-3, +6.48e-2;
  null directions 7.963 / 172.036 deg (cone paper 7.963/172.037). PSEUDO-RIEMANNIAN (Lorentzian).
- C4 peel step = Lorentz boost: B=exp(½ ln z a·σ) preserves det X (Minkowski, Λᵀ η Λ = η to 1e-13).
  Loop W below wall (Γ²=0.3): eigenvalues 1,1,e^{±iθ}, cos θ = −0.1995 — a Wigner (Thomas) rotation; tr W = 2 − 4(R/T)² exact.
  At wall: tr W = −2, (W+1)²=0, W+1≠0; (Λ−1)³=0, kernel 2-dim, fixed lightlike vector (1, 1/√2, 1/√2, 0)·(−1): a NULL ROTATION.
  Beyond (Γ²=0.7): boost-type, eigenvalues 389.16, 0.00257, 1, 1.
  => the wall is the light cone of the Lorentz group the peel steps live in: Lorentzian = non-Riemannian (pseudo-Riemannian) at the step level.
- C5 pullback fold: det g = 1.79e-2, 1.99e-3, 1.24e-4, 0 while intrinsic g on unit X stays 1 (degenerate, Carrollian-type).

## Prior art (searched 22 Nov)
- Bujack, Teti, Miller, Caffrey, Turton PNAS 119 e2119753119 (2022): diminishing returns cannot exist in a Riemannian geometry
  (geodesic additivity fails); Stark–Turton–Bujack EuroVis 2025 extends to green–pink and blue–orange axes.
- Ye, Vleeshouwers, Heatley, Gritsev, Morais Smith, arXiv:2305.17675: Hermitian quantum geometry is Riemannian; non-Hermiticity
  gives pseudo-Riemannian and complex geometries.

## Answer to "which object does the word belong to"
Not the Hermitian IQGT tensor (all versions + checks: Riemannian, Kähler). Three objects of his carry it, each a different sense:
 (a) the ledger comparison √S (trace-log / log-det) — non-Riemannian in Bujack's sense: locally Riemannian, globally subadditive;
     in scalar form it IS the peel Γ: S = −½ ln(1−Γ²). This is the colour bridge (LANL data, ledger curve beats log).
 (b) the tensor over a NON-HERMITIAN operator (biorthogonal) — pseudo-Riemannian / Lorentzian: B23, the cone paper.
 (c) the peel step itself — a Lorentz boost; the wall is a null rotation (light cone); non-Riemannian (Minkowski) at the spinor level.
 (d) degenerate pullbacks (fold/polar) — semi-Riemannian degenerate, no Levi-Civita connection.
Leftover in v1.2.1: §2.7 (02_wall.md) still says "Its curvature is non-Riemannian" — to be replaced by his choice among (a)–(d).
