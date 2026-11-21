# The Ledger Outlives the Metric × The Loop Wall: connection map

Jeromie Beasley's gravity paper set against his element paper "The Loop Wall" (VOTKP, branch
`element-paper/loop-wall`, page v8). Mapped 21 November 2026. Local only: nothing was written to GitHub or Drive and nothing was committed.

## 0. Which gravity text was used

Three versions were read. Section 7 lists them.

| Version | Date | Pages | Role here |
|---|---|---|---|
| final_v3 (Zenodo deposit 22088625, App A to AF) | 25 Aug 2026 | 62 | His own framing. Its numbering matches the brief: Thm 1 cap, Thm 5 licence locus, Prop 12 wrap, Prop 17 eta, Prop 20 pairing split, Lemma 18 Σ. |
| Full Research Edition 6 (Zenodo 22959910, the current deposit, the one used in the joint paper) | 24 Sep 2026 | 30 | Corrected statements of the same theorems, renumbered. |
| Research Edition 7 (working manuscript, not deposited) | 4 Oct 2026 | 32 | **Newest.** Edition 6 plus a differentiable overlap theorem, Prop 33 (coupling weight) and §22 (source to force). |

Numbering changed between versions. The wall-related theorems map like this:

| Item | final_v3 | Editions 6/7 |
|---|---|---|
| Persistence cap | Thm 1 | Thm 1 |
| Licence (2×2 PSD) | Thm 2, plus §4 | Thm 3, which adds the diagonal condition |
| Codimension | Thm 4 | Prop 12, with transversality stated |
| Licence locus nested inside det g > 0 | Thm 5 | Remark after Thm 3, and §7.1 |
| Reciprocity | Thm 7, Cor 8, eq. (2) for W | Thm 10, Cor 11, narrowed to a single partner (rank zero possible) |
| Contour record | Thm 10, §7 | Thm 13, plus Thm 16 (a moving wall with varying Z) |
| Wrap | Prop 12 | Prop 20 |
| Eta | Prop 17 [C] | Reduced to a scope caveat |
| Σ Gram | Lemma 18, Cor 19 | Prop 19 |
| Exponents and lapses | Result 16, §9.2 [H] | Prop 17, with stronger caveats |
| Pairing split | Prop 20 | Thm 5 |

One correction in Editions 6 and 7 bears directly on "what survives a wall". In GEOWALL-LEDGER-02 every row is evaluated at the base point (t1, t2) = (0, 0). The base matrix and its projector are therefore fixed, and the flat count and trace-log are constant by construction. The moving case is Edition 6 Thm 16: an explicit chart crosses a metric wall without an exceptional point while N = 1 and Z = log(2 + y/10) varies smoothly through it. The "what survives" connection (C5) is graded against that corrected form.

Wording rules followed: element names are written in full, "crossing number" is never shortened, and no letter-pair abbreviations are used. The intrinsic metric is never replaced by a spacetime metric. The only indefinite form used below is the auxiliary quadratic form of the hyperboloid model of the element paper's own disk.

## 1. Summary table

Grades:
- **EXACT**: the same formula, by algebra.
- **STRUCTURAL**: the same shape on different objects (flagged).
- **LEAD**: untested.

"EXACT + STRUCTURAL" means the algebra is identical but setting one paper's object equal to the other's is a construction.

| # | Gravity paper | Loop Wall | Grade | Check |
|---|---|---|---|---|
| C1 | Persistence cap Tr(PR) = Σcos²θ ≤ k (Thm 1) | Two faces close iff Γa² + Γb² < 1 | EXACT + STRUCTURAL | 01 |
| C2 | Licence 4(ac − b²) ≥ ω² (Ed6 Thm 3); nesting inside det g > 0 (final_v3 Thm 5) | The same 2×2 form with a = c = 1, b = Γa, ω = 2Γb. Anion rung: det g = IE·EA | EXACT + STRUCTURAL | 01 |
| C3 | Principal angles in the cap | Γ = cos Π(h), the angle of parallelism. The wall is Π = 45° | EXACT (element side) | 01 |
| C4 | A two-plane det g sign is "a property of the plane" (§5.3, App W) | Loop wall = sign change of a two-plane Gram determinant of an indefinite form; the axis angle chooses the plane | EXACT + STRUCTURAL | 02 |
| C5 | The record crosses the wall (Thm 10; Ed6 Thm 16) | s = sinh ha·sinh hb is cos φ while the loop closes and cosh d once it opens | EXACT + STRUCTURAL | 02 |
| C6 | Wall species and codimension (Thm 4) | The loop wall is a regular codimension-one curve with two sides, far from any coalescence | EXACT (codimension), STRUCTURAL (species) | 02 |
| C7 | Line-element exponents ½ and 1 (Result 16) | The wall is a transverse crossing; √(soft eigenvalue) has exponent ½ | EXACT (computed), STRUCTURAL | 05 |
| C8 | Pairing split, Gram case (Prop 20); Prop 33 (Ed7); F_A (Result 22) | Peel identity = junction sum rule = localization tensor | EXACT | 03 |
| C9 | Area law: gapped saturates, gapless grows as a log (Result 22) | Rubidium spread grows, krypton saturates (§7) | STRUCTURAL | 03 |
| C10 | A semi-definite form can only touch zero (Cor 19) | The real-part (Gram) form never reaches the loop wall | STRUCTURAL | 05 |
| C11 | S = Sᵀ as the laboratory case of Thm 7 (final_v3 §7) | Peel step as a two-port. Power symmetry comes from losslessness; the exact sign flip from reciprocity plus a real S-matrix | EXACT + STRUCTURAL | 04 |
| C12 | W, an out-and-back 2×2 area (eq. 2) | Γ and χ share one reversal law, (−1)^{n(n+1)/2} for an n-step oriented volume | EXACT (law), STRUCTURAL (comparison) | 04 |
| C13 | Metric is a licence, ledger is a record; W lifts linearly (Result 15) | Three-mode loop: energies even in Φ, circulation odd. W lifts linearly; det g = W²‖M‖⁴/(4Δ⁴) at a Hermitian point | EXACT in the model, STRUCTURAL to gravity | 04 |
| C14 | Result 15's mechanism is left open | Gauge control: a removable phase gives isospectral + W linear (slope 0.9995), and W returns to roundoff once the probes are carried along | EXACT in the model; LEAD for the gravity gate | 04 |
| C15 | Scale is invisible to the projector, Z shifts by k log α (Ed6/7 Prop 30) | Every z, Γ and wall call is unchanged by rescaling; the record shifts by n ln α; ln z telescopes | EXACT | 05 |
| C16 | Ledger additive, cap bounded | ln z adds while Γ composes by the tanh (rapidity) addition law and stays inside (−1, 1) | EXACT + STRUCTURAL | 05 |
| C17 | det = exp Tr log discards the wrap (Prop 12) | Γ² discards the sign of Γ | STRUCTURAL | — |
| C18 | Licence local, record global (§8, Results 13/14) | The wall reads one atom's ladder; conduction lives in the junctions | STRUCTURAL | — |
| C19 | Null direction while the projector moves (OP5; Ed6 Thm 16) | At the wall the loop's fourth vertex becomes a null (ideal) point | LEAD | — |
| C20 | Supra-unity persistence only off self-adjointness (§3) | An open loop has no orthogonal rank-one realization; only an oblique one exists | EXACT (no orthogonal realization), LEAD (physical) | 01 |
| C21 | Thomas rotation tan(θ/2) = Γ² (Two Trees) against Ω | No counterpart found in the gravity text | LEAD | — |
| C22 | Wrap licence δ + g² ≤ 4 (Prop 12) | Two Trees ln 5 commutator | tested, **no content** (winding 0) | 05 |
| C23 | Direct textual cross-references | Ed6 §20 cites VOTKP Elemental Peeling 0.8; Ed6/7 Prop 30 note on elemental thin-film work; v8 calls Γ "the half-step of the intrinsic ledger" | textual | — |

## 2. The connections in detail

### C1. The loop test is the persistence cap at rank one. EXACT + STRUCTURAL

**Statement.** Theorem 1 (all versions): for orthogonal projectors with rank P = k, 0 ≤ Tr(PR) ≤ k. Take P = uuᵀ of rank one and R the rank-two orthogonal projector onto two orthonormal face directions e1, e2. Then Tr(PR) = ⟨u,e1⟩² + ⟨u,e2⟩² ≤ 1.

A real unit u with ⟨u,e1⟩ = Γa and ⟨u,e2⟩ = Γb exists in ℝ³ exactly when its third component squared, 1 − Γa² − Γb², is ≥ 0. So:
- "the loop closes" (element paper: Γa² + Γb² < 1) is the same statement as "a rank-one orthogonal projector carries these two overlaps strictly under its rank cap";
- ideal contact is the cap saturated;
- an open loop is the cap exceeded.

The final_v3 abstract already calls the cap "a Cauchy–Schwarz inequality on Gram matrices". The loop test is the same Bessel / Cauchy–Schwarz inequality.

**Why the check proves it.** If the two verdicts are the same inequality, they must agree pair by pair on real data. One disagreement would kill the claim.

**Result** (`check_gravity_01_output.txt`):
```
faces 433 adjacent same-core pairs 427
disagreements loop / licence / rank-one cap / eigenvalue : 0
open pairs: helium 3-4 0.373090752, helium 4-5 0.176316795, helium 5-6 0.069582243,
            helium 6-7 0.003093338, neon 11-12 0.114273066
equal-face disagreements (433 faces): 0
```
The counts (433 faces, 427 pairs, 5 open) and the margins reproduce the element paper's six-core map: lithium with beryllium, beryllium with boron, boron with carbon, carbon with nitrogen (+0.0031), sodium with magnesium. The faces were rebuilt independently from the archive using the opening-map rule q = Z − N − 1.

**Flag.** The identity is exact. Reading the Γ's as projector overlaps is a construction. Γ is a reflection of an energy ratio, not a measured overlap.

### C2. The loop test is the gravity paper's licence form, with the nesting built in. EXACT + STRUCTURAL

**Statement.** Edition 6/7 Thm 3: [[a, b + iω/2],[b − iω/2, c]] is PSD iff a ≥ 0, c ≥ 0 and 4(ac − b²) ≥ ω². Final_v3 §4 states the same on a probe plane: Q is PSD iff 4 det g ≥ Ω².

Put a = c = 1, b = Γa, ω = 2Γb. The form becomes [[1, w],[w̄, 1]] with w = Γa + iΓb. It is PSD iff |w|² = Γa² + Γb² ≤ 1. That is the loop test again: the two faces combined in quadrature behave as one complex reflection, and the loop closes iff that reflection stays inside the unit disk.

The nesting of final_v3 Theorem 5 follows automatically. The "metric" part det g = ac − b² = 1 − Γa² is positive for every real face. So whenever Γb ≠ 0, the licence fails (the loop opens) while the metric is still definite. This is exactly "wherever Ω ≠ 0 the licence locus lies strictly inside det g > 0".

**Chemistry instance at the anion rung.** Take a = c = χ, b = η, ω = 2η:
- the licence reads χ² ≥ 2η², which is ω_Parr ≥ η (the element paper's wall, "electrophilicity = hardness");
- the "metric" determinant is χ² − η² = IE·EA exactly.

So along a family with falling electron affinity, the licence (the wall, z = 3 + 2√2) fails first while IE·EA > 0, and the "metric" degenerates only at EA → 0, where the anion stops binding (z → ∞). Protection is lost first, then the metric degenerates. That is the same order final_v3 §4 measures.

**Why the check proves it.** The PSD criterion is a theorem. Any archive case where the loop verdict and the licence verdict differ, or where an open pair has 1 − Γa² ≤ 0, kills the claim.

**Result:** 0 disagreements on 427 pairs and 433 equal faces; 0 nesting failures among the 5 open pairs. On all 49 anion rungs (hydrogen to neodymium, `batch12/chemistry/anion_chemistry_h_nd.csv`), exactly: Γ0 = η/χ, χ² − η² = IE·EA, licence ⇔ ω ≥ η. 41 of the 49 rungs are outside with IE·EA > 0.

**Flag.** Which Γ plays the metric and which plays the curvature is a choice, and the form is symmetric under swapping them. The inequality is identical; the role assignment is structural.

### C3. Γ is the cosine of the angle of parallelism. EXACT (element side; supports C1)

Lobachevsky's angle of parallelism satisfies cos Π(h) = tanh h = Γ, sin Π = sech h, tan Π = 1/sinh h. The last one is the element paper's circle radius.

Γa² + Γb² < 1 ⇔ cos Π(ha) < sin Π(hb) ⇔ Π(ha) + Π(hb) > 90°. The equal-face wall is Π(h) = 45°: tan(Π/2) = e^{−h} = √2 − 1.

Result: 0 disagreements on 427 pairs; Π = 45.000000000000° at the wall. This is what turns C1 into a literal principal-angle statement: Γ = cos θ with θ = Π(h).

Supporting fact. The coordinate map (X, Y) = 2(x, y)/(1 + x² + y²) in `batch8/lambert/mixed_faces.md` is the standard Poincaré-to-Klein map. Γ = tanh h is the Klein coordinate of a face; the face apex tanh(h/2) is its Poincaré coordinate. In the Klein disk the two perpendiculars are straight lines X = Γa and Y = Γb, so they meet at (Γa, Γb).

### C4. The loop wall is a two-plane determinant sign change of an indefinite form. EXACT + STRUCTURAL

**Statement.** In the hyperboloid model of the element paper's disk (an auxiliary quadratic form with one negative and two positive directions, not a spacetime metric), each face perpendicular has unit normal n = (sinh h, cosh h·u). Two such geodesics:
- meet inside the disk iff the plane spanned by n1, n2 is definite (2×2 Gram determinant 1 − ⟨n1,n2⟩² > 0);
- touch at the rim iff that determinant is zero;
- are ultraparallel iff it is negative (indefinite).

At the right-angled corner, ⟨n1,n2⟩ = −sinh ha sinh hb, and 1 − s² > 0 ⇔ Γa² + Γb² < 1. So the loop wall is precisely a det = 0 crossing of a two-plane restriction of an indefinite form.

That is the event final_v3 §5.3 and Appendix W treat: "the sign of a two-plane determinant is a property of the plane … definiteness is a property of the metric." Rotating the second axis by θ changes the plane. ⟨n1,n2⟩ = cosh a cosh b cos θ − sinh a sinh b, and the sign follows the choice. The forward-sector condition (both intersection coefficients positive) is extra, orientation-odd information that the determinant cannot see.

**Why the check proves it.** The script builds the intersection point directly and compares four verdicts per pair: the Gram determinant, whether the geodesics meet, the element margin, and s < 1. It then finds the sign changes of the plane determinant as θ varies and compares them with the archived carbon-with-nitrogen values.

**Result** (`check_gravity_02_output.txt`):
```
pairs 427 : sign disagreements (Gram det / intersection / margin / s<1): 0
carbon with nitrogen: Gram-det contacts (deg): 1.51888748 89.82270223 | forward-sector closing window starts at 13.11528523
closes at 89.8 deg: True | closes at 90 deg: False
```
This reproduces the archived 1.51888748° and 89.82270223° full-geodesic contacts and the 13.11528523° forward-sector start.

**Flag.** The ambient form here is the hyperboloid model's, not the gravity paper's trace form 1/2 Re Tr(∂P∂P). The shared content is "a two-plane restriction of an indefinite form changes determinant sign, and the sign depends on the plane". Do not compare numbers across the two papers.

### C5. What survives the loop wall: an angle becomes a length. EXACT + STRUCTURAL

**Statement.** The single quantity s = sinh ha·sinh hb:
- equals cos φ, the fourth angle of the Lambert quadrilateral (three right angles), while the loop closes;
- equals cosh d once the loop opens, where d is the common-perpendicular gap of the right-angled pentagon that replaces the quadrilateral.

Both are classical hyperbolic-trigonometry formulas. At the wall, φ → 0 (ideal vertex) and d → 0. The closure, a licence-like yes/no bounded by cos φ ≤ 1, expires. The analytic function s carries straight through and becomes a distance on the far side. So do the ratio z, its log h, and the ladder sum Σ ln z.

This matches the gravity paper's thesis in its corrected form (Ed6 Thm 16). There N and Z = log(2 + y/10) are regular, and Z varies smoothly across the metric wall rather than staying constant. It also matches final_v3 Thm 2: past the wall "the radicand is negative and the bound has no content" while the underlying quantities continue.

**Why the check proves it.** The angle φ is measured at the constructed fourth vertex from tangent vectors, not taken from the formula. The gap d is minimized directly along one geodesic by ternary search, not taken from |⟨n1,n2⟩|.

**Result:**
- closed loops: max |cos φ_measured − s| = 5.8e−15;
- open loops: max |cosh d − s| = 2.2e−16;
- directly minimized distance against d: 3.3e−16.

### C6. Wall species and codimension. EXACT (codimension), STRUCTURAL (species)

F(ha, hb) = sinh ha sinh hb − 1 has gradient (cosh ha sinh hb, sinh ha cosh hb). That gradient is nonzero on F = 0 (minimum |∇F| = 2.000014 on the sampled curve). So the mixed-face wall is a regular codimension-one curve with two sides, which is Ed6 Prop 12's first case and final_v3 Thm 4's "geometric" species. The equal-face wall is its transversal crossing with the diagonal.

The nearest thing to a spectral coalescence on the peel side is z = 1: equal thresholds, Γ = 0, the transparent matched junction. That is the far interior. The archived wall sits at z = 5.83, so the loop wall is a geometric wall with no exceptional point anywhere near it. This parallels Ed6 Thm 16, "a wall without an exceptional point".

### C7. Crossing class: exponent ½. EXACT computation, STRUCTURAL comparison

Final_v3 Result 16: the line-element exponent is n/2. A transverse crossing gives ½ (the indefinite class); a touch gives 1 (the semi-definite class).

At the loop wall:
- d(Γ²)/dz = 0.060660172 ≠ 0, a simple zero with a sign change;
- the soft eigenvalue 1 − |w| of the two-face form vanishes linearly, and its square root has fitted exponent 0.50017;
- the real-part form [[1, Γ],[Γ, 1]] keeps its minimum eigenvalue at 0.2929 at the wall.

So the loop wall belongs to the crossing class. The horizon-lapse reading in final_v3 §9.2 is graded [H] there and is not imported here.

### C8. One identity under four names. EXACT

These are the same algebra:

| Paper | Name | Formula |
|---|---|---|
| Element (`spinor_recovery`) | Peel identity | ι†A²ι − (ι†Aι)² = (QAι)†(QAι), Q = 1 − ιι† |
| Element (§7) | Junction sum rule | Σ_{j≠i} ‖P_ij‖² = Tr(C_i − C_i²) |
| Element (§7) | Localization tensor | Var(X) = Tr(PX(1−P)X) = ½ Σ_ij ‖P_ij‖²(x_i − x_j)² |
| Gravity final_v3 Prop 20 (= Ed6/7 Thm 5) | Pairing split, Gram case | ∂P = X + Y, g = Re ½ Tr(XY + YX); P self-adjoint ⇒ Y = X†, Gram, PSD |
| Gravity Ed7 Prop 33 | Coupling weight | q(C) = −Tr BB†, q(−iC) = +Tr BB† for C = [H, P], B = PH(1−P) |
| Gravity final_v3 Result 22 | Region fluctuation | F_A = Tr Π_A(1 − Π_A) |

The relations:
- The sum rule is the peel identity with A = P and the site isometry.
- The localization tensor is Prop 33's positive (unitary-tangent) form with H set to a site-constant position X. It is also Prop 20's metric on the tangent −i[X, P], where Y = X† makes it a Gram form.
- Prop 33's Tr BB† is the peel defect with A = H on Ran P. It is also the zero-time memory weight 𝒦(0) = BB† of the Universal Projector Geometry paper, which Ed7 itself quotes.
- The sum rule is F_A for a one-site region.

**Why the check proves it.** Both sides of every identity are evaluated on 200 random complex projectors, Hermitian matrices and isometries of random sizes. A false identity fails generically.

**Result** (`check_gravity_03_output.txt`):
```
E1 7.0e-15 | E2=E1(A=P) 2.5e-15 | E3 1.2e-14 | E3=G2 2.3e-14 | G1 Gram 5.4e-15 | G2 sign 7.6e-16 | E2=G3 1.1e-16 | blocks 1.6e-15
half-filled chain nearest share = 0.81057   8/pi^2 = 0.810569
```

Consequence. The element paper's "third reading" (localization tensor) and junction budget are the positive, self-adjoint branch of the gravity paper's tangent form. The gravity paper's negative branch (similarity tangent q([X, P]) = −Var X, checked) has no element-side reading yet. See C14 and the leads.

### C9. Gapped saturates, gapless grows. STRUCTURAL

The quantity F_A from C8 on a 2002-site chain:

| Region size | Gapless F_A | Gapped F_A (dimerized) |
|---|---|---|
| 8 | 0.44047 | 0.50059 |
| 16 | 0.51088 | 0.50064 |
| 32 | 0.58113 | 0.50064 |
| 64 | 0.65124 | 0.50064 |
| 128 | 0.72097 | 0.50064 |

The gapless column grows by 0.0702 per doubling, which is (1/π²)·ln 2, the Widom coefficient for one dimension. The gapped column saturates. This is the shape of final_v3 Result 22, and of the element paper's rubidium spread (5.684 → 12.622 Å² with mesh) against krypton's (≈ 0.067 Å², flat).

**Flag.** Different systems and different observables: a region's fluctuation here, the cell-centre second moment there. Only the growth-against-saturation contrast is shared.

### C10. A semi-definite form cannot carry the wall. STRUCTURAL

Final_v3 Lemma 18 / Cor 19: a Gram form can only touch its null set (exponent 1), so "no geometry built from a spectral-stress Gram form can carry a non-extremal lapse". On the element side the real-part form [[1, Γ],[Γ, 1]] is a Gram matrix. It never reaches zero for |Γ| < 1, at the wall or anywhere. The wall appears only in the Hermitian combination with the second face as the imaginary part (C2), which crosses (C7).

### C11. Reciprocity and the peel step. EXACT algebra + STRUCTURAL

The element paper itself uses transmission-line language (standing-wave ratio, half-power point). Treat the peel step as a two-port S = [[Γ, t],[t, −Γ]] with t = √(1 − Γ²).

- **Losslessness alone** gives |S11| = |S22| for any 2×2 unitary S. That is the element paper's `power_even`. Checked on 1000 random unitaries: residual 6.4e−16.
- **Reciprocity plus a real S-matrix** (S = Sᵀ, S² = I) fixes the off-diagonal condition Γt + tx = 0, so x = −Γ. That is the exact flip `gam_reverse`. Checked: z = 6 gives ±5/7.

Final_v3 §7 names S = Sᵀ ("time reversal makes a scattering matrix symmetric") as the laboratory instance of its Theorem 7. So the element paper's direction law lives inside the reciprocal class of the gravity paper.

The peel's round trip, forward reflection times reverse reflection, is Γ(z)Γ(1/z) = −Γ², a negative perfect square. Theorem 7's reciprocal round trip is also a perfect square (Q = M²/Δ²).

**Prediction from this mapping (untested).** A step that breaks reciprocity, for example under a field, would still keep |S11| = |S22| (losslessness), but the reverse reflection would no longer be exactly −Γ.

### C12. One reversal law for Γ and χ. EXACT law, STRUCTURAL comparison

Reverse a path (d_k → −d_{n−1−k}). An n-step oriented volume det[d0 … d_{n−1}] is multiplied by (−1)^{n(n+1)/2}. A mirror always multiplies it by −1.

- n = 1 is the signed half-step h = ½ ln z: reversal flips it. That is the sign of Γ.
- n = 3 is the screw sign χ = (d0 × d1)·d2: reversal keeps it, a mirror flips it. That is the element paper's `chi_reverse` / `chi_mirror`.

Checked for n = 1 to 7 on random vectors.

Comparison with the gravity obstruction. W = |M_a N_b − M_b N_a|/(‖M‖‖N‖) is an n = 2 area built from the outbound and return amplitudes. Reciprocity (N ∥ M) kills W. What reciprocity can kill is the reversal-odd information: W, the sign of Γ, the circulation in C13. The screw sign is reversal-even and passes through a reciprocal reading untouched. Only a mirror test sees it. This sharpens the element paper's Barron classification (true chirality versus the reversal-odd Γ) in the gravity paper's terms.

### C13. Three-mode loop: the record is even, the direction is odd. EXACT in the model, STRUCTURAL to gravity

The recovered three-mode loop (element folder `spinor_recovery`), with detuned sites ε = (0, 0.3, 0.7), J = 1, flux Φ on one link, and fixed real symmetric probes (B = I). W is computed exactly as final_v3 eq. (2) defines it.

```
Phi = 0: W = 1.56e-16, det g = 7.85e-15 (pinched, rank one: gravity Cor. 8, phase-aligned case)
log-log slope of W against Phi = 0.99703        (gravity Result 15: 1.000 in rotation)
signed Im(M_a M_b*) flips with Phi; max |spec(+Phi) - spec(-Phi)| = 0.0; Z(+Phi) - Z(-Phi) = 0.0
Tr H^3 change at Phi = 1e-2, 2e-2: -3.0e-4, -1.2e-3 (even, second order)
```

The ledger (spectrum, trace-log) is even in Φ, so it is "the same energies". The reciprocity measure W is odd and linear, so it carries "the opposite circulation". This is the element paper's energy-versus-circulation split written as the gravity paper's record-versus-W split.

One new exact statement here (not in either paper). For a Hermitian generator and Hermitian probes, N = M̄, so the pair-form metric is g_ab = Re(M_a M̄_b)/Δ². Its determinant is det g = +(Im M_a M̄_b)²/Δ⁴ = W²‖M‖⁴/(4Δ⁴) ≥ 0. Checked: agreement to 6e−5 relative, limited by cancellation at Φ = 1e−6.

So at a Hermitian point, breaking reciprocity turns the pinched rank-one form into a definite one. That answers, inside this model, final_v3's remark that "breaking reciprocity does not automatically buy definiteness back". At a Hermitian point it does, because Thm 3 forces the round trip to be ≥ 0 and the only obstruction left is phase alignment. On the open horizon generator (non-Hermitian) the sign is not forced, and the gravity paper measures indefinite planes there.

### C14. Gauge control for Result 15's open mechanism. EXACT in the model; LEAD for the gravity gate

Final_v3 §5.3 / App AA measured that rotation is isospectral (trace powers constant to 1e−10) while W lifts linearly, and left the mechanism open. It also notes that every diagonalizable generator is B-symmetric for some B, so "the whole content of Theorem 7 lies in the fixed probes".

The control. Put the same phase on an open chain (no loop). Then it is a pure diagonal-unitary change of basis.
```
open chain (pure gauge): spectral drift = 6.7e-16 ; slope of W vs Phi with fixed probes = 0.99951 ;
W with covariantly carried probes = 1.5e-16
```

So "isospectral + W linear with slope 1" is exactly what a removable change of basis produces when the probes are held fixed. A genuine flux (C13) instead moves the spectrum at second order: Tr H³ shifts by −3Φ², an O(1) coefficient. The gravity gate's trace powers stay constant to 1e−10 up to a = 0.4. That rules out a flux-type shift with an O(1) coefficient. It supports the gravity paper's own suspicion that the advection term acts as a change of basis seen through fixed probes.

**Decisive test (not run; needs the gate script from `gravity_final_v3_complete.zip`):**
1. On GEOWALL-ROT-01, compute the signed antisymmetry Im(M_a N_b − M_b N_a) at +a and −a. Odd means the lift is first order.
2. Construct the similarity S(a) that maps L2 + aD back to L2. Isospectrality says it exists when L is diagonalizable: S = R(a)R(0)⁻¹.
3. Carry the probes covariantly, V → S V S⁻¹.

If W falls back to the instrument floor, Result 15 is a probe-covariance effect, as in the chain. If W stays at 5.5e−2 at a = 0.1, the gate holds information the chain does not have.

### C15. Scale is invisible to the peel. EXACT

Ed6/7 Prop 30: under K → αK the projector and metric are unchanged and Z shifts by k log α. On the element side, rescaling every energy (eV → hartree, ×1000) leaves all Γ and all wall calls unchanged. The ladder record shifts by n ln α. Each half-step is half an increment of the trace-log of the ladder, and Σ ln z_k telescopes to ln(IE_last/IE_first).

```
adjacent steps in archive: 5714 ; outside: 8 ; Gamma or wall call changed by rescaling: 0
record shift residual (n ln alpha): 1.1e-13 ; telescoping residual: 1.8e-15
```
(The 8 outside steps across all 118 archive elements are the 8 first core openings: lithium, beryllium, boron, carbon, sodium, potassium, rubidium and caesium. Francium is centrally inside.)

The element paper's second-hour note already hits Prop 30 from the data side: "a common rescaling of both IE ladders preserves every signed reflection but can erase the crossing; the mass anchor and absolute energies complete the record". That is Prop 30's point: a known energy unit is what breaks the scale ambiguity.

### C16. Additive record, bounded reflection. EXACT + STRUCTURAL

ln z adds under composition of steps. Γ composes by the tanh addition law, Γ(A) ⊕ Γ(B) = (Γa + Γb)/(1 + ΓaΓb) = Γ(AB) (Two Trees `gam_mul`; residual 3.3e−16). Γ stays inside (−1, 1) like a capped quantity, while h grows without bound like a record. Structural parallel to the cap against the ledger.

### C17. Squared readings discard odd information. STRUCTURAL

Final_v3 Prop 12: det = exp Tr log identifies every rung of the 2πi ladder and "discards exactly one wrap". The element paper: "a ledger that keeps only Γ² loses the direction". Both are an even reading (exponential, square) throwing away an odd invariant (integer wrap, sign).

Final_v3 Prop 17 says the asymmetry (eta) travels with the record. The element paper's matching odd quantities are sign(Γ) and χ. No element-side spectral asymmetry of an operator was found. The torus Dirac η = 0 in `spinor_recovery` is a control, not a measurement.

### C18. Local wall, global junctions. STRUCTURAL

Final_v3 §8 (Results 13/14): the metric layer is a local budget per spectral block, and a block's geometry is set from outside it. The record is one global account. Element v8 §2: "The wall reads the atom's own ladder. Conduction is a property of the connections between atoms." The junction budget Tr(C_i − C_i²) is paid entirely by off-site couplings (C8), which has the shape of a block's metric being "assembled from couplings that leave it".

### C19. The null vertex. LEAD

At the wall, the loop's fourth vertex becomes an ideal point, a null vector of the hyperboloid form (C4/C5). Final_v3 OP5 asks whether a null direction of g with a still-moving projector is Carrollian. Ed6 Thm 16 shows a nonzero nilpotent tangent ((∂_y P)² = 0) at its wall. **Test:** build a rank-one idempotent family on the (ha, hb) face plane, for example the hyperboloid-form-orthogonal projector onto n1 along n2, and see whether its trace form has a nilpotent tangent exactly on sinh ha sinh hb = 1.

### C20. An open loop has no orthogonal realization. EXACT that none exists; LEAD for the physics

By C1, an open pair (Γa² + Γb² > 1) cannot be the overlaps of any orthogonal rank-one projector. Only an oblique (biorthogonal) idempotent can carry them. Final_v3 §3 finds supra-unity persistence (Re C = 1.00002372) only off self-adjointness and only where det g < 0.

**Decisive test:**
1. For each of the 5 open adjacent pairs, find the minimally oblique rank-one idempotent with these overlaps.
2. Compute its tangent form q(D) = ½ Re Tr D² along the face plane.
3. Check for a negative direction (Ed6 Cor 9 direction).

If the closed pairs never produce one and the open pairs always do, the cap language is physical. Otherwise it is only formal.

### C21. Thomas rotation. LEAD

Two Trees proves tan(θ/2) = Γ² for the Thomas angle of two peel boosts. The gravity text has curvature Ω and the licence |Ω| ≤ 2√det g, but no holonomy-of-boosts statement. No connection found in the text. Possible test: compare the Thomas angle with the area (Gauss–Bonnet defect) of the element paper's Lambert quadrilateral, which is π/2 − φ.

### C22. Wrap licence on the Two Trees commutator: no content

The ln 5 commutator has cos φ = −527/625, so cos(φ/2) = 7/25. Its eigenvalues are 1, 1, e^{±iφ}, det = 1, winding sum 0. The integer that final_v3 Prop 12 keeps is zero here. Also, Prop 12's hypothesis is unitary U, V, and boosts in SO(3,1) are not unitary. Recorded as tested; nothing carries over.

### C23. Direct textual cross-references

- Edition 6 §20 lists "VOTKP: Elemental Peeling research edition 0.8 as a material measurement check".
- Edition 6/7, after Prop 30: "The elemental thin-film work supplies a material warning: a computable boundary/optical threshold is not external validation without measured reflectance-versus-thickness data, and its failed Snell/film controls remain failures."
- Element v8 abstract: Γ is "the half-step tanh(½ ln z) of the intrinsic ledger" (C15 makes this exact).

## 3. Gravity items with no element counterpart found

These were mapped first; nothing in the element text matches them:
- Newton from the ledger kernel (Result 21);
- the relative-entropy no-go (Ed6/7 Prop 22);
- the conditional Einstein–Hilbert, screen and finite-mode sections (Ed6/7 §§13–14, 19, 22);
- the neutral signature of the full idempotent tangent space (Ed6/7 Thm 6), beyond C8's branch statement;
- the source-insertion tomography (Ed6/7 Thms 26–28).

Lemma 11 (blindness to a scalar baseline) has only the log-space analogue in C15: the peel is blind to multiplicative scale, not to additive shifts.

The element paper's spinor (Dirac) screening events, the opening map's "first opening outside, then inside at once", and the material junction runs have no gravity counterpart in the text.

## 4. The strongest connections, and the decisive tests

1. **C1 + C2: the loop test is the gravity paper's Cauchy–Schwarz licence, with Theorem 5's nesting built in.** EXACT algebra on all 427 pairs, 433 faces and 49 anion rungs, with zero disagreements. The anion-rung version puts the "metric determinant" at IE·EA, so the wall (electrophilicity = hardness) is a licence that lapses while the metric is still definite. Degeneracy comes only when the anion unbinds.
2. **C4 + C5: the loop wall is a two-plane determinant sign change of an indefinite form, and what crosses it is one analytic quantity.** s = sinh ha sinh hb is an angle on one side and a gap length on the other. EXACT hyperbolic geometry, measured independently to 1e−15, with the archived carbon-with-nitrogen angles reproduced. This is the element paper's own instance of "the sign of a two-plane determinant is a property of the plane" and of "the record outlives the licence".
3. **C8: the peel identity, the junction sum rule and the localization tensor are the gravity paper's Prop 20 (Gram case) and Ed7 Prop 33.** EXACT to 1e−14 on random input. The element "third reading" is the self-adjoint branch of the gravity tangent form.

Close behind is **C13 + C14**. The three-mode loop and its gauge control give the gravity paper a solvable model for Result 15 and a decisive test of its open mechanism: carry the probes covariantly on GEOWALL-ROT-01 (C14).

The two decisive tests for leads are C14 (covariant probes on the rotating gate) and C20 (an oblique realization of the 5 open pairs, tested for a negative tangent direction).

## 5. Notes for the main session

- **Versions.** Edition 7 (4 Oct) is the newest gravity text but is a working manuscript, not deposited. Edition 6 is the current Zenodo deposit. Both were read in full. His own framing ("the metric is a licence, the ledger is a record", nesting, eta, lapses) is fullest in final_v3. Editions 6/7 narrow several claims: the fixed-base ledger crossing, the single-partner reciprocity, eta reduced to a caveat, and the lapse identification. Each grade above names the version it rests on.
- **From memory, not from the papers.** Only the version history (final_v3 → Ed6 → joint paper) and the location of the Two Trees material came from memory (`/areas/gravity-paper.md`). Every mathematical statement above was taken from the texts listed in §7 and checked.
- **Element-side fact derived here.** Γ = cos Π(h), the angle of parallelism (C3). It is not stated in the element paper and could go into its §5.
- **Gravity-side fact derived here.** At a Hermitian point with Hermitian probes, det g = W²‖M‖⁴/(4Δ⁴) ≥ 0 (C13). It is not in any gravity version read.
- **Check scripts.** All 5 scripts ran on the pinned archive; outputs are saved beside them. They read the archive as an argument and are run with `python3 -I`.

## 6. Files

- Report: `/home/claude/connections/gravity_connections.md`
- Checks, each beginning with `# SCRIPT: NAME`, with outputs beside them:
  - `/home/claude/connections/checks_gravity/check_gravity_01_cap_licence.py` (C1, C2, C3, C20)
  - `/home/claude/connections/checks_gravity/check_gravity_02_two_plane_wall.py` (C4, C5, C6)
  - `/home/claude/connections/checks_gravity/check_gravity_03_gram_sumrule.py` (C8, C9)
  - `/home/claude/connections/checks_gravity/check_gravity_04_reciprocity_loop.py` (C11, C12, C13, C14)
  - `/home/claude/connections/checks_gravity/check_gravity_05_scale_record.py` (C7, C10, C15, C16, C22)
- Sources downloaded to `/home/claude/connections/src_gravity/` (PDFs, plus pdftotext extractions and the v8 page text).

Run:
```
A=/home/claude/votkp-lean/data/element_thresholds_20261011.json.gz
C=/home/claude/votkp-lean/research/2026-11-20-element-paper-loop-wall/batch12/chemistry/anion_chemistry_h_nd.csv
python3 -I check_gravity_01_cap_licence.py $A $C
python3 -I check_gravity_02_two_plane_wall.py $A
python3 -I check_gravity_03_gram_sumrule.py
python3 -I check_gravity_04_reciprocity_loop.py
python3 -I check_gravity_05_scale_record.py $A
```

## 7. Sources read

**Gravity paper**

| Source | Location | Read |
|---|---|---|
| Research Edition 7, 4 Oct 2026, 32 pp | Drive file 19CY1kNrxxpwo411XjSpwC6TcmI8xXpby, `Gravity_Paper_Edition_7.pdf`; md5 0a0c49b4… | In full |
| Full Research Edition 6, 24 Sep 2026, 30 pp (Zenodo 22959910) | Drive current-papers folder, file 1tVHGGS3fFYJDh-rq_isRfXOpsG-oC5Nd; md5 54d4a176… | In full |
| gravity_final_v3, 25 Aug 2026, 62 pp | Drive file 1F3g29E6Oz0vbagJ7DBWZX38F5g63KJIa; md5 d959f7b1… | Main text (abstract, §§1–12, Scope, References) in full; Appendices A–AF (gate scripts and outputs) skimmed, not read in full |
| Gravity_Version_Comparison.pdf, 4 Oct 2026 | Drive | In full (version lineage) |
| "Gravity Ledger Edition 6 — Fresh Independent Retest", 1 Nov 2026 | Drive HTML | In full |

Not read: `Gravity_Ledger_v4.html` and the Edition 6/final_v3 complete zips (gate code). GitHub could not be listed from this session: the repository-scoped API only, so the private `operator-first` repository was not reached.

**Loop Wall element paper** (local repo `/home/claude/votkp-lean`, branch `element-paper/loop-wall`)

| Source | Read |
|---|---|
| `research/2026-11-20-element-paper-loop-wall/README.md` | In full |
| `QUANTUM_CHEMISTRY_LINKS.md` | In full |
| `CLAUDE_REVIEW.md` | In full |
| `SECOND_HOUR_20261121.md`, `REVIEW_GUIDE_20261121.md` | In full |
| `VOTKP_Element_Paper_Loop_Wall_v8_20261121.html` (text extraction) | In full |
| `lean/LoopWall.lean` | Lines 1–140 read; theorem list and the reversal, mirror, junction, window and chemistry theorems read |
| `batch8/lambert/mixed_faces.md` | In full |
| `spinor_recovery/README.md` | In full |
| `batch10/mixed_map/adjacent_pairs.csv`, `opening_faces.csv` | Headers only (the faces were recomputed independently from the archive) |
| `batch12/chemistry/anion_chemistry_h_nd.csv` | Used as data |
| `two-trees/README.md` | In full |
| `two-trees/lean/PeelTrees.lean`, `PeelTrees3.lean` | Theorem headers only |
| Archive `data/element_thresholds_20261011.json.gz` | Used as data |
