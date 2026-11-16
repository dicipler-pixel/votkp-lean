# Notes: Jeromie Beasley, three-body paper (three_body_operator_first_v3.pdf)

Source: Google Drive file 1ki75S4LaJw3LyAlx7desUq3uzsVzhlmk, read through the Drive text reader. Text came back complete: page markers 1-9, ends with reference [14]. The reproduction archive (zip 1Zt3cVOgAxxEq5jZzuuYeCve1rJ30WoK7) was NOT opened. The PDF itself was not downloaded, so figures were seen only as their extracted labels/captions, and a few formulas came through scrambled; every rebuilt formula is flagged "REBUILT" below, and what could not be rebuilt is flagged "NOT READ".

## 1. What the paper is

- Title as printed: "The Three-Body Problem, Operator-First". Subtitle: "Spectral anatomy of relational transport on the shape sphere, a spectral record surviving metric degeneracy, and a birefringent reading of the two-sheet geometry".
- Author: Jeromie Beasley. Date printed: August 22, 2026.
- Version: "v3" appears only in the filename; the text does not print a version number. The text refers to "an earlier draft", "my own earlier draft", and "the open problem of the previous version".
- Length: 9 pages, 13 sections, 2 figures, 14 references, 1 numbered display equation set (1) plus (2).
- Scope statement (Sec 1, Sec 12): "No general closed-form solution of the planar three-body dynamics is claimed." It is "a coordinate-free spectral anatomy of relational transport - how much the three mutual distances resist change per unit motion of the shape - together with two quantities that survive the places where that anatomy degenerates."
- Novelty claim is stated as narrow: singular behaviour of side-length coordinates at collinear configurations "is ninety years old (Murnaghan 1936; Lemaitre 1952)"; new is "its statement as a rank drop of an explicit operator, the correct separation of two loci that the literature and my own earlier draft treated as one, and the measurement of a spectral record through them on an actual orbit."
- The setting is the PLANAR three-body problem. Orbit used: the Chenciner-Montgomery figure-eight, equal masses. Unequal masses tested: m=(1,2,3) and m=(1,1,5/2). N-body extension only for the collinear rank law and regular polygons (N=3..8).

Section list: 1 What is and is not being solved; 2 The operator, and why this one; 3 Two degeneracies, of different species; 4 The equilateral degeneracy is not diabolical; 5 The cos^4 law is a fold, not a three-body fact; 6 The transport form is pinched, and by two independent mechanisms; 7 The record along the figure-eight; 8 The symmetry broken: a genuine conical intersection; 9 The shape manifold is a birefringent crystal; 10 The rank drop is the smallest member of a family; 11 Transient amplification under the chosen compression; 12 What is claimed; 13 Open; References.

## 2. Objects and definitions (his names)

- Shape sphere S^2: "the Kendall shape sphere of the planar three-body problem in the coordinates w = (sin th cos ph, sin th sin ph, cos th)". th = polar angle, ph = longitude.
- w3 = "the signed area". Equator w3 = 0 (th = pi/2) = "the collinear (syzygy) locus". Poles (th = 0, pi) = "the equilateral (Lagrange) configurations".
- I = moment of inertia; squared mutual distances are normalised by I.
- Relational map: shape -> its three mutual distances. The three normalised squared distances are affine in (w1,w2), independent of w3. "the relational map is the projection of the shape onto three directions at mutual 120 deg".
- Phi : S^2 -> R^2, Phi(w) = (w1, w2) ("Dropping the constant ... the induced map").
- M = dPhi^T dPhi: "the Gram matrix of its differential, read in an orthonormal frame of the round metric." Called "the Gram operator". Frame {e_th, e_ph}.
- lambda: "Throughout, lambda denotes an eigenvalue of the Gram operator M; the singular values of dPhi are their square roots, |cos th| and 1, and are not used elsewhere." (Note: Sec 8-9 nevertheless speak of "singular values" equal to sqrt2, with lambda1=lambda2=2 given as the equivalent; and the abstract says "its singular values are cos^2 th and 1".)
- lambda_min = cos^2 th, lambda_max = 1.
- Spectral gap = lambda_max - lambda_min = 1 - cos^2 th = sin^2 th.
- Relational rigidity R = lambda_min^(-2) = sec^4 th. Also called "the metric layer". "the cos^4 rigidity law".
- (Notation clash to keep in mind: in Sec 7 "Tr R(z)" is the trace of the resolvent inside a contour integral, not the rigidity R.)
- Earlier-draft object, replaced: weighted tensor T(w) = diag(w1^2, w2^2, w3^2).
- Soft / softest eigendirection = e_th (eigenvalue cos^2 th). "most rigid direction" used for the direction a global choice of which is obstructed (Cor 6).
- Riesz projector: "requires a gap, not invertibility".
- Z2 eigenline monodromy: sign with which the transported eigenvector returns after one circuit (+1 or -1). Also "holonomy".
- Line-field index: winding of the eigenline field at a pole (+1 at each pole here).
- Fold / A2 normal form: Whitney's fold x -> x^2/2. A3 cusp: where the exponent is predicted to differ.
- Square case N = d+1: the shape sphere "is the d = 2 rung of the square case N = d + 1, whose transport operator on the eigenvalue block is A = D_t - g t^T." (D_t, g, t are not defined further in this paper; D_t reads as diag of t. Symbols come from the square-case work; not re-derived here.)
- Bilinear pairing B = diag(t/g) (entries t_i/g_i). Left eigenvectors l_n = B R_n (R_n = right eigenvectors).
- Symmetrisation theorem: D_t - g t^T = S (D_t - u u^T) S^(-1), with B = S^(-2). (u not defined in this paper.)
- W = "the rank measure" of the round-trip form; det g = determinant of the round-trip / transport form (he writes "detg"; this g is the transport form, a different use of the letter from the vector g in A). "cone": the transport form "carries no cone anywhere on the regular stratum".
- Regular stratum; collision divisor (where ||B|| = max_i t_i/g_i diverges); "the boundary".
- Contour Gamma: circle of radius 0.9 about 0.5, "which encloses both eigenvalues with margin".
- Count N = (1/2 pi i) contour-integral of Tr R(z) dz (REBUILT from scrambled text).
- Shifted trace-log Z = (1/2 pi i) contour-integral of log(z + eta) Tr R(z) dz, with eta = 1 (REBUILT). Also "the ledger"; "the record". eta = 0 version = "the unshifted ledger".
- Branch condition: "a branch analytic on and inside Gamma". "It is a branch condition, not a positivity condition, and the shift is what restores it."
- "Two layers": the metric layer (R) and the record (N and Z).
- Index sheets / optic axes: "The two singular values of M are two sheets of an index surface, so a point where they coincide is an optic axis".
- Uniaxial = one axis (equal masses); biaxial = exactly two axes (unequal masses).
- Coordinates a, psi used for the optic-axis locations in Sec 8-9: NOT DEFINED in the paper text (psi behaves as a longitude: pi/2, 3pi/2 is called "the symmetry meridian"; a is a coordinate with a^2 values 1/2, 5/7, 2/7).
- J: "the traceless part of M as a linear map J of the two shape coordinates" near an optic axis.
- Mass-weighted Jacobi coordinates: "where translation and boost are absent by construction and the Euclidean norm is the kinetic-energy norm".
- Compression (Sec 11): the quotient is "an orthogonal complement of the symmetry and integral directions", not flow-invariant, so the measured object is "a compression of the propagator, not a restriction".
- Run labels (script/check names): LAGRANGE-PHASE-01, BODY-RECIP-01, FIG8-LEDGER-01, UNEQUAL-CHECK-01, BIAXIAL-01, CONICAL-RAY-01, LADDER-CHECK-01, TB-TRANSIENT-03.

## 3. Equations in order

(1) [REBUILT: extraction scrambled the fractions; rebuilt using his sentence that the coefficient vectors are unit vectors at 0, 120, 240 degrees]
  r01^2 / I = 1 + w1
  r02^2 / I = 1 - (1/2) w1 + (sqrt3/2) w2
  r12^2 / I = 1 - (1/2) w1 - (sqrt3/2) w2
  "verified to 1.6e-15 over random configurations, with the coefficient of w3 vanishing to 4.6e-16."

(2) M = dPhi^T dPhi.

Theorem 1 display: dPhi(e_th) = (cos th cos ph, cos th sin ph); dPhi(e_ph) = (-sin ph, cos ph);
  M = diag(cos^2 th, 1); lambda_min = cos^2 th, lambda_max = 1. "no dependence on ph and no free constant."
  Proof: cross term = -cos th cos ph sin ph + cos th sin ph cos ph = 0.

Remark 2: earlier tensor T(w) = diag(w1^2, w2^2, w3^2). Its determinant on the sphere: the printed formula is scrambled ("34 sin6 th cos2 th sin 2ph" in extraction) - exact prefactor and exponents NOT READ (p.2, Remark 2). What is readable: it vanishes on the great circles ph = 0 and ph = pi/2 and at w3 = 0; the first two have "no invariant meaning", being axis-dependent; only w3 = 0 is coordinate-free.
  R = lambda_min^(-2) = sec^4 th, "prefactor exactly 1 and no longitude dependence, where the earlier route reported a ph-averaged constant."

Prop 3: gap = 1 - cos^2 th = sin^2 th, maximal on syzygy locus (th = pi/2).
Prop 4: th -> 0, pi: both eigenvalues -> 1; det M -> 1.
Theorem 5: gap/th^2 -> 1.
Cor 6: index +1 + index +1 = 2 = chi(S^2).
Prop 8: th = pi/2 + eps; w1 = cos eps cos ph ~ (1 - eps^2/2) cos ph; fold x -> x^2/2; lambda_min ~ eps^2; R = lambda_min^(-2) gives sec^4.
Sec 6: A = D_t - g t^T.  A^T B = B A, B = diag(t/g).  l_n = B R_n.  D_t - g t^T = S(D_t - u u^T)S^(-1), B = S^(-2).  det g <= 0 with equality when amplitudes are phase-aligned.  ||B|| = max_i t_i/g_i.
Sec 7: N = (1/2 pi i) oint Tr R(z) dz; Z = (1/2 pi i) oint log(z+eta) Tr R(z) dz, eta = 1 (REBUILT).  Z = log(1 + lambda_min) + log 2.  Syzygy times t/T = 0, 1/6, ..., 5/6 (REBUILT from "0, 16,..., 56").
Sec 10 proof: d r_ij^2 / d y_k proportional to (y_i - y_j), vanishing when all y = 0 (REBUILT from scrambled order). Rotation acts as y_i proportional to x_i.
Sec 13: a1^2 + a2^2 = 1 (observed, not derived).

## 4. Results with the paper's own grades

- Theorem 1 (Exact spectrum of the Gram operator). PROVED (direct substitution). M = diag(cos^2 th, 1) in {e_th, e_ph}.
- Remark 2. Replacement of the earlier weighted tensor was "forced": two of its three degeneracy loci were coordinate artefacts. R unchanged = sec^4 th.
- Proposition 3 (Rank drop at syzygy; the gap is maximal there). Stated as proposition, follows from Thm 1.
- Proposition 4 (Degeneracy at the equilateral points; the operator stays invertible). Follows from Thm 1.
  Reading attached: "A Riesz projector requires a gap, not invertibility: it continues real-analytically through syzygy, where the gap is widest, and it is only at the equilateral points that the two spectral subspaces cease to be separable. Any 'diabolical point' or projector-collapse language belongs at the poles, and any regularisation introduced to carry a projector across the equator is unnecessary - there is nothing there to regularise."
- Theorem 5 (Quadratic closing, integer index, no Berry phase). "Proof and verification": analytic (gap = sin^2 th; e_th smooth and single-valued on latitude circles) plus numerical check LAGRANGE-PHASE-01. Monodromy +1; index +1 at each pole; winding 0 in the coordinate frame and +1 as a field on the sphere - "the coordinate frame supplies the whole rotation". Caveat in the statement: "The eigenline is trivially monodromic along every punctured loop, which is not the same as extending through the pole: no globally nonvanishing tangent direction exists there."
- Corollary 6 (The obstruction is topological, not local). "no global smooth choice of 'most rigid direction' on the shape sphere, and the obstruction is the Euler characteristic rather than any stratum."
- Remark 7 (Why the linear term is absent). Z3 relabelling fixes the equilateral configuration; an invariant symmetric 2-tensor at the fixed point is a multiple of the identity to leading order; linear anisotropy forbidden. Prediction: unequal masses break Z3 and are "the place to look for a genuine conical intersection."
- Proposition 8 (A2 normal form). "the exponent 4 is two bookkeeping squarings on top of a simple zero"; invariant content is only "that dPhi has a simple zero on a codimension-one locus." "That converts a recurring coincidence into a theorem and predicts where it should fail: at an A3 cusp, which the equal-mass problem does not have and which unequal masses or four bodies may supply."
- Theorem 9 (Reciprocity). A complex-symmetric w.r.t. B = diag(t/g): A^T B = B A "exactly". Consequences: for B-symmetric probes outbound and return amplitudes coincide, round-trip form is a perfect square, W vanishes, det g <= 0 with equality when phase-aligned. On the regular stratum everything is real so det g = 0 exactly. Checked numerically (BODY-RECIP-01). "The transport form carries no cone anywhere on the regular stratum, and ||B|| diverges exactly on the collision divisor - so the only place the geometry could open is the boundary."
  Note: the section title says "two independent mechanisms" but the text does not number them; what is on the page is (a) the reciprocity pairing and (b) reality of operator, pairing and spectrum on the regular stratum making relative phase zero. I do not assert that this is the intended pair.
- Theorem 10 (Measured: the record outlives the metric). Grade: MEASURED. On the figure-eight: six syzygies per period at exactly T/6 spacing; metric layer collapses at each; count N holds at 2; shifted trace-log Z = log(1+lambda_min)+log 2, finite everywhere, minimum log 2 exactly at each syzygy.
- Remark 11. Convergence under step refinement; residuals at 1e-15 "are at the double-precision floor and are not physical uncertainties."
- Remark 12 (The branch condition is not a technicality). eta = 0 breaks the ledger because the branch point at the origin is inside the contour.
- Proposition 13 (Numerical evidence for a conical intersection at unequal masses). Grade: NUMERICAL EVIDENCE. "The degeneracy is located numerically; no analytic proof of its existence or of the nonvanishing of the local Jacobian is offered here." "The prediction was recorded before the test (UNEQUAL-CHECK-01)." Linear closing, sign flip, Berry phase pi.
- Proposition 14 (Uniaxial, biaxial, and the symmetry plane). Grade: grid search with local refinement (BIAXIAL-01). "A grid search cannot certify that no further coincidences exist; 'two axes' means two found for the tested mass family."
- Remark 15. "the reading is a crystallographic analogue with the same local geometry, not a claim of literal optics." Transferred prediction (Hamilton's): at a biaxial optic axis the sheets meet conically, the surface normal (ray direction) is undefined, "a single incident ray refracts into a hollow cone."
- Proposition 16 (A circle of ray directions). Numerical (CONICAL-RAY-01). "a single point of shape space admits a circle of ray directions rather than one. This is the only statement in the paper about what a trajectory would do rather than what an operator's spectrum is, and it is the natural next computation."
- Proposition 17 (Collinear rank for N bodies). PROVED in one line + verified N = 3..8 (LADDER-CHECK-01). rank dPhi = N-2 at a generic collinear configuration; kernel dimension N-2 in the (2N-4)-dimensional shape space.
- Proposition 18 (Measured). Transient amplification on the figure-eight (TB-TRANSIENT-03).
- Remark 19 (What this is not). Compression, not restriction; eigenvalues are not Floquet multipliers; "only the gain is quoted."
- Sec 12 claim: N and Z are "Not a new integral of motion in the classical sense: N and Z are functions of the shape alone". Claimed: "they are insensitive to the degeneracy that destroys the metric layer, at machine precision, on a real solution, six times per period - and that this is the same ordering measured on synthetic operator families, now realised in celestial mechanics with no dial to turn by hand."

Abstract wording worth keeping: "The record outlives the metric on a real orbit, and the branch condition is doing visible work." (The abstract says "Four results follow" and then lists (i) to (vii).)

## 5. Numbers (all dimensionless unless noted; the paper gives no physical units)

Eq (1) check: residual 1.6e-15 over random configurations; w3 coefficient 4.6e-16.
Thm 5: gap/th^2 = 0.996671, 0.999967, 1.000000, 1.000000 at th = 1e-1, 1e-2, 1e-3, 1e-4. Holonomy +1.000000 at th = 0.3, 0.05, 0.01, zero sign flips. Winding 0 (coordinate frame), +1 (on sphere). Index sum 2 = chi(S^2).
Thm 9 (BODY-RECIP-01): B-symmetric probes W = 1.7e-16, det g = 0.00; generic probes on same operator W = 0.17, det g = -1.5e-4.
Sec 7 protocol: equal masses, "the standard initial data" (values not printed); RK4, step h = 2e-5; period T = 6.32591398; closure |q(T)-q(0)| = 4.1e-5. Contour: circle radius 0.9 centre 0.5. eta = 1.
Thm 10: initial condition collinear, signed area 0.000; six zeros of signed area in [0,T) at t/T = 0, 1/6, ..., 5/6. Closest finite sampled point: lambda_min = 6.3e-9, R = 2.5e16. max|N-2| = 5.1e-15. Z residual 2.2e-15. Z minimum = log 2 = 0.693 at each syzygy; Z ranges between log 2 and 1.045 along the orbit (Sec 12).
Figure 1 (FIG8-LEDGER-01), three panels: signed area w3 (axis about -0.5..0.5) with six zeros; metric layer R on a log axis (labels 1e5, 1e12, 1e19, 1e26, 1e33) "spiking through sixteen orders"; contour count N and shifted trace-log Z flat; t axis 0..6.
Remark 11: h from 2e-4 down to 1.25e-5: max|N-2| 4-5e-15; max|Z - (log(1+lambda_min)+log 2)| 2-3e-15; orbit closure 2.4e-6 at the finest step.
Remark 12: eta = 0 gives measured minimum -0.580 against log 2 = 0.693.
Prop 13: m = (1,2,3); degeneracy at a = 0.845154255, psi = 5.034139535; both singular values = sqrt2; gap closes to 1.5e-14; gap/r = 2.16437, 2.16294, 2.16281, 2.16280 at r = 1e-2, 3e-3, 1e-3, 3e-4; monodromy -1.000000 at every radius tested. (Check: 0.845154255^2 = 0.714286 = 5/7, consistent with Prop 14.)
Prop 14: equal masses: two points, a = 1/sqrt2 at psi = pi/2, 3pi/2 (one axis meeting the sphere twice). m=(1,2,3): four points in two pairs, a^2 = 5/7 and a^2 = 2/7, singular values sqrt2 (lambda1 = lambda2 = 2). m=(1,1,5/2): four points, all at psi = pi/2 or 3pi/2.
Prop 16: det J = -4.463; twelve equally spaced approach directions give ten distinct gradient directions; |grad lambda| from 0.638 to 8.080.
Figure 2: left "equal masses: 1 axis" (2 points on the sphere); centre "m=(1,2,3): 2 axes" (4 points on the sphere); right "one point, a circle of rays": ray direction (axis labels 175..325) against direction of approach 0..300 deg.
Prop 17 (LADDER-CHECK-01): N = 3,...,8: ranks 1,2,3,4,5,6; shape dimensions 2,4,6,8,10,12.
Regular polygons [REBUILT from scrambled text, p.7]: the square gives {sqrt8, 2, 2, 2} "with a threefold degeneracy that splits linearly under perturbation"; the pentagon gives {sqrt(5+sqrt5), sqrt(5+sqrt5), 2, 2, sqrt(5-sqrt5), sqrt(5-sqrt5)} "in three pairs". (Assignment square<->4 values, pentagon<->6 values matches shape dimensions 4 and 6; the pentagon's middle pair "2,2" is read from the scrambled string and is the least certain item.) Sec 13: "The hexagon's spectrum contains the pentagon's values" (hexagon values not printed).
Prop 18 (TB-TRANSIENT-03): amplification 45.7 in energy, 6.8x in amplitude, within one period, returning to 9.6 at the end. Energy conserved to 6.5e-14, angular momentum to 2.2e-14. Mean gain in the quartile of the orbit closest to syzygy 10.58; farthest quartile 26.10. Perturbation eps reaches about 7 eps.
Abstract repeats: gap/th^2 -> 1.000000; R reaches 2.5e16; count holds at 2 to 5.1e-15; trace-log to 2.2e-15; -1.000000.

## 6. Limits, failures, open items

Stated limits:
- No closed-form solution; not a new integral of motion; N and Z are functions of shape alone.
- Planar problem only. Equal masses for the main anatomy.
- Prop 13: no analytic proof of existence of the degeneracy or of nonvanishing local Jacobian.
- Prop 14: grid search cannot certify completeness; "two axes" = two found for the tested mass family.
- Remark 15: crystal reading is an analogue with the same local geometry, "not a claim of literal optics."
- Prop 16 is about ray directions (gradients), not trajectories.
- Sec 11: compression, not restriction; not Floquet multipliers.
- Residuals at 1e-15 are numerical floor, not physical uncertainties.
- Thm 10: counting sign changes of signed area is "ambiguous by one" because the initial condition is itself collinear; roots located directly.
- Stated failure: the unshifted ledger (eta=0) fails, minimum -0.580, because the branch point is enclosed.
- Retired: the earlier weighted tensor T(w) and its two artefact loci; the earlier conflation of the syzygy and equilateral loci; "diabolical point" language for the equal-mass poles; any regularisation to carry a projector across the equator.

Sec 13 Open (verbatim content):
1. "The relation a1^2 + a2^2 = 1 between the two optic axes, and the exact rationals a^2 = 5/7, 2/7 at m = (1,2,3) against a total mass of 6. Observed to the printed digits; not derived."
2. "A closed form for the regular-N-gon spectra. The hexagon's spectrum contains the pentagon's values, which a table of special cases would not do."
3. "Proposition 8 predicts a different exponent at an A3 cusp. The equal-mass shape sphere has folds only; where the first cusp appears is not known."
4. "The ledger on the divisor, where the pairing B of Theorem 9 is undefined and the count is the only surviving object."
5. "A genuinely reduced monodromy for Sec. 11 ... The symplectic complement inside ker dE intersect ker dL would make it one."
6. "Conical refraction at the level of trajectories rather than of ray directions: integrate an orbit into an optic axis and ask what the reduced dynamics does there."

Internal inconsistencies seen on the page (reported, not corrected):
- Abstract: "Four results follow" then seven items; "singular values are cos^2 th and 1" vs Thm 1 (eigenvalues cos^2 th, 1; singular values |cos th|, 1).
- Sec 2 says Z3 protection is "in Sec. 5"; the equilateral degeneracy is treated in Sec 4. Sec 11 says "which is what Sec. 6 requires" (Sec 6 is the pinched transport form - consistent).
- Lemaitre cited as 1952 in Sec 1, reference [6] is dated 1964.
- Thm 1 gives lambda_max = 1 for equal masses, while Prop 14 lists equal-mass coincidence points at a = 1/sqrt2 (not obviously "the poles") and unequal-mass coincident values sqrt2 / lambda = 2: the (a, psi) coordinates and the mass-dependent normalisation are not defined in the text. Would need the reproduction archive (BIAXIAL-01, UNEQUAL-CHECK-01) to pin down. NOT READ.
- Sec 6 symbols t, g, u, S, W and the "round-trip form" are imported without definition.

Not read / not resolved: Remark 2 determinant formula exact form; "standard initial data" values; hexagon spectrum; the figures themselves (only labels); the reproduction zip.

## 7. What bears on the team's questions

(a) Several equal balls on a hyperbolic field, light/energy passing from one to the next:
- The paper contains NO hyperbolic field, no balls, no light passing between bodies. Nothing here states such a construction. What it does offer that could be carried over, in its own terms:
  - Equal masses is the symmetric (uniaxial) case: Z3 relabelling protects the equilateral degeneracy; gap closes quadratically; monodromy +1; no Berry phase. Breaking equality gives a conical intersection, monodromy -1, two optic axes (biaxial). So "equal" versus "unequal" bodies is exactly his uniaxial/biaxial split.
  - The transport operator A = D_t - g t^T with reciprocity pairing B = diag(t/g): for B-symmetric probes "the outbound and return amplitudes coincide, the round-trip form is a perfect square", W = 0, det g = 0. This is the only outbound/return (passing and coming back) statement in the paper. No cone on the regular stratum; "the only place the geometry could open is the boundary" (the collision divisor, where ||B|| diverges).
  - The optics language (index sheets, optic axes, conical refraction, "a single incident ray refracts into a hollow cone", "a circle of ray directions") lives in SHAPE SPACE and is explicitly "not a claim of literal optics".
  - The two layers: metric layer R (fails at syzygy) and the record N, Z (survives). Z = log(1+lambda_min) + log 2 is finite through alignment.
  - N-body: at a generic collinear configuration rank dPhi = N-2; regular polygons carry structured degeneracies (square {sqrt8,2,2,2}; pentagon three pairs; hexagon contains pentagon's values). This is the paper's only statement on more than three bodies arranged regularly.

(b) Sun-Earth-Moon or Sun-planet setting:
- NOT in the paper. No Sun, Earth, Moon, planets, hierarchical or restricted problem, no physical units. Mass cases are only equal, (1,2,3) and (1,1,5/2). The relevant transferable facts: syzygy (collinear alignment, which is what an eclipse-type alignment is geometrically) is where lambda_min = 0, rank drops, R diverges, gap is maximal, the Riesz projector continues analytically, N stays 2 and Z takes its minimum log 2. Strongly unequal masses fall under the biaxial case, but the paper tests no extreme mass ratio; where the optic axes go for such ratios is not stated. Open item 1 (a^2 = 5/7, 2/7 at total mass 6) hints the axis positions are rational in the masses, "not derived".

(c) Shape sphere, collinear / Lagrange configurations:
- Shape sphere coordinates w = (sin th cos ph, sin th sin ph, cos th); w3 signed area; equator = syzygy; poles = equilateral (Lagrange).
- Syzygy: rank drop, lambda_min = cos^2 th = 0, gap = 1 maximal, det M = 0, R = sec^4 th diverges, fold (A2) normal form, nothing to regularise for the projector.
- Lagrange/equilateral poles: both eigenvalues 1, det M -> 1, gap closes as th^2, not diabolical for equal masses, index +1 each, sum 2 = chi(S^2), no global most-rigid direction.
- Figure-eight: six syzygies per period at T/6 spacing; amplification burst "lives on the triangular configurations, not at the wall".
- "Lagrange" here means the equilateral shape (the poles). Lagrange points L1-L5 of a restricted problem are not discussed.

(d) Gram matrices:
- The central object is M = dPhi^T dPhi, "the Gram matrix of the differential of the map that sends a shape to its three mutual distances", read in an orthonormal frame of the round metric; exact form diag(cos^2 th, 1). Eq (1) shows the map is projection onto three unit directions at 120 degrees. Section 6 ties it to "the square case N = d+1" (d = 2 rung). Rank law N-2 at collinear configurations for the N-body dPhi.

(e) Leading eigenvectors:
- Eigenvectors of M are e_th (eigenvalue cos^2 th: the soft / softest direction) and e_ph (eigenvalue 1). The paper tracks the SOFTEST eigendirection: monodromy +1 (equal masses) or -1 (m=(1,2,3)); index +1 at each pole. "Most rigid direction" has no global smooth choice (Cor 6). Near an optic axis the gradient of the lower sheet takes a circle of directions (Prop 16). Left eigenvectors of the transport operator: l_n = B R_n.
