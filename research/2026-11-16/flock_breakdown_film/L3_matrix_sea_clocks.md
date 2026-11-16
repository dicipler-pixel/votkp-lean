# L3 — The matrix between balls, the electron sea, the clocks, and the step to the Flock

Jeromie Beasley · breakdown of the Flock of Balls on the Field · lineage 3 · 16 Nov 2026 · AI-assisted

Paths used below:
- MM = `/home/claude/balls/w/mm/mm_math_v1.js` (byte-identical to `/home/claude/balls/in/81dc35c1-Three_Balls_on_the_Field_v1_Source/mm_math_v1.js`, checked with `diff -q`)
- TB = `/home/claude/balls/w/tb/tb_math_v1.js` (identical to the source copy)
- FL = `/home/claude/balls/w/fl/fl_math_v1.js`
- GCC = `/home/claude/balls/w/tb/gap_clock_check_01.js` and `.out`
- NN-Lean = `/home/claude/gh/nonnormality-connection-energy-lean`
- IQGT-Lean = `/home/claude/gh/iqgt-grassmannian-lean`
- DT-Lean = `/home/claude/gh/dirac-time-lean`
- NN paper text = `/home/claude/text/NN_v15.txt` (Non-normality is connection energy, and its opposite, 21 Oct 2026)
- WPMK = `/home/claude/text/WPMK_v1_1.txt` (What the Present Must Keep, v1.1, 2 Nov 2026)
- CSL = `/home/claude/text/COLOUR_v1_2.txt` (Colour Selects the Leader v1.2; holds Appendix 15.3 and 15.4)
- DT paper = `/home/claude/text/DIRAC_v3_1.clean.md` (Dirac Time long form v3.1)
- Cards = `/home/claude/dicipler-pixel/relational-atlas-lean/atlas/coverage/coverage.json`
- My runs = `/home/claude/balls/breakdown/scratch/L3/l3_run_01.js` … `l3_run_05.js` (run with `node <file>`; all numbers marked RUN below come from these)

Not found on disk: the text of *The Offset Speed Limit* v1.1 and of *The Weight Between* v1.1 as their own files, and the `offset-lean` repository. Their statements are quoted here from the papers that restate them (WPMK, CSL, DT paper). No web request was made.

---

## 1. Summary in plain words

The Moving Matrix puts one small two-level block on every ball and one rotation on every link, and adds them into one matrix H = D + A. The block D_i says which way the ball's field points and how far apart its two levels are. The link A_ij carries a frame from ball j to ball i; because the field is hyperbolic, a frame carried round a triangle comes back turned by the triangle's area. Four papers supply the parts: the connection energy identity says how much the ball fields disagree across the links (LEAN); the IQGT says a projector can only move by crossing between kept and not kept (LEAN); the offset speed limit says a record read from a block of the sea cannot move faster than 2·√(g·S) (PROVED in the papers; LEAN for one mode only); Dirac Time says a rate is a scale on the gaps and is read only against another clock (LEAN). The runs confirm the identity to rounding on 3 and 7 balls, the loop turn = area = Thomas turn to 15 digits, and a speed-limit ratio of at most 0.021 (3 balls) and 0.026 (7 balls). The Flock keeps the placement, the link rotations, the ball levels, the light's torque and the faces; it replaces the instant hop by light that travels and scatters, gives every ball its own level spacing, and holds the faces to rest directions. It drops the sea and with it every sea readout. Two things were found that the sources do not say: the matrix that moves the light is Hermitian, so the connection energy belongs to a companion matrix (same D, hop turned by a quarter turn), and with clocks in the ratio z the Flock's faces carry connection energy at rest (2.204 for three balls) where the three-ball matrix carried none.

---

## 2. The chain, link by link

### 2.1 Where the balls sit, and the link between two balls

**Statement.** Each ball is a point on the hyperboloid, reached from the centre by one peel step (a boost of rapidity r = ln z along an arm). The link between balls i and j has length d_ij (the hyperbolic distance) and Smith coordinate Γ_ij = tanh(d_ij/2).

**Code.** MM:12 `boost(u, r)`; MM:17 `dist = acosh(mink(p,q))`; MM:38–40 `relLorentz`, `linkDistance` (computed in SL(2,C) for stability, MM:27–29); TB:12 `pts` puts A at the centre, B at (cosh r_I, sinh r_I, 0, 0), C at (cosh r_J, 0, sinh r_J, 0); TB:5 "B–C (the third side of the right triangle, cosh d = cosh r_I cosh r_J)".

**Grade.** The peel step and Γ = tanh(r/2): lineage 1 (LEAN / PROVED there). cosh d_BC = cosh r_I · cosh r_J is the hyperbolic Pythagoras theorem: a textbook result, here a reproduction. CHECKED · 0.0e+0 (RUN l3_run_03).

**Flock.** FL:39 (placement), FL:41 (`MMr.linkDistance`). Kept unchanged.

**Why it is there.** The distance between two balls is what later sets both the strength of the link (MM) and the travel time of light (Flock).

### 2.2 The link rotation R_ij and its SU(2) lift U_ij

**Statement.** Carry ball j's frame to ball i along the straight line between them. Read in each ball's own boosted frame, the result is a rotation R_ij (3×3). Its lift U_ij (2×2, unit determinant) acts on the ball's two levels: U (d·σ) U† = (R d)·σ.

**Code.** MM:26–29 (comment: "R_ij = [ L_{q->O} Lambda(A_i^{-1} A_j) ] restricted to space"); MM:39 `linkRotation`; MM:46–51 `su2` ("exp(-i theta/2 n.sigma) = w - i(x sx + y sy + z sz)").

**Grade.** MODEL CHOICE for the construction (own-frame reading of the transport); the SU(2) lift is textbook. That U and R agree is CHECKED · 1.5e-15 by the identity in 2.5 (it can only hold if U (d·σ) U† = (R d)·σ on every link; the control with one U replaced by the identity breaks it by 1–2 %, RUN l3_run_01).

**Flock.** FL:41 `R = MMr.linkRotation(...)`, `U = MMr.su2(R)`; used at the ports FL:79–80 and at every scatterer FL:81. Kept unchanged.

**Why it is there.** Two balls do not share one "up"; the link has to say how one ball's direction looks from the other.

### 2.3 Round a triangle: turn = area = Thomas turn

**Statement.** The product of the three link rotations round A → B → C → A is a rotation by the hyperbolic area of the triangle, and for the right triangle of two perpendicular steps that angle is 2·arctan(Γ_I·Γ_J).

**Why the check proves it.** Three numbers are computed three independent ways: the angle of the matrix product R_AB·R_BC·R_CA (MM:202), the angle defect π − (sum of the three angles from the law of cosines) (MM:203–205), and the closed form (TB:28). Agreement on several unrelated step pairs cannot come from a shared formula, because none is shared.

**RUN (l3_run_04, l3_run_01).**

| steps (r_I, r_J) | turn | area | 2·arctan(Γ_I Γ_J) |
|---|---|---|---|
| τ = 0 of the surprise ball: (1.0986122887, 1.9125468038) | 0.7110545751 | 0.7110545751 | 0.7110545751 |
| (ln 3, ln 5) | 0.6435011088 | 0.6435011088 | 0.6435011088 |
| (0.9, 0.9) | 0.3523076793 | 0.3523076793 | 0.3523076793 |
| (0.3, 2.0) | 0.2258154478 | 0.2258154478 | 0.2258154478 |
| (2.5, 2.5) | 1.2474995467 | 1.2474995467 | 1.2474995467 |

The README value 0.7110545751 (`.../81dc35c1-.../README.md` line 9) is reproduced; differences turn − area 6.7e-16, turn − Thomas 1.7e-15. Seven-ball world: 20 triangles, worst |turn − area| 1.8e-15.

Note on reproduction: `t_tb1.js` cannot be run from `/home/claude/balls/w/tb` because it requires `../surprise/src/lh_math.js`, and `/home/claude/balls/w/surprise/src/` is empty. I took the step formula from `/home/claude/balls/ex_surp_2_light_hypersurface_surprise_v1.js` line 29, `r = max(ln 1.3, ln zbar_a + amp·sin(2π τ/T_a + ph_a))`, with the parameters of `t_tb1.js` line 3. The τ = 0 steps are therefore r_I = ln 3 and r_J = ln 5 + 0.35·sin(2π/3), not (ln 3, ln 5); GCC uses (ln 3, ln 5), which gives 0.6435.

**Grade.** Turn = area: textbook (holonomy of a surface of curvature −1), a reproduction; CHECKED · 2e-15. Thomas turn: LEAN · `thomas5`, `thomas7`, `thomas_half_angle` (`/home/claude/votkp-lean/two-trees/lean/PeelTrees.lean:302`, "tan(theta/2) = sin/(1 + cos) = Gamma^2", exact at z = 5 and 7), `thomas_general` (`PeelTrees2.lean:365`, equal steps, symbolic z); for unequal steps the plan grades it as a numerical check (`PLAN_light_at_the_hypersurface.md` line 320: "Unequal steps and W = L R L⁻¹ R are numerical checks"). So 2·arctan(Γ_I Γ_J) with r_I ≠ r_J is CHECKED · 2e-15, not LEAN.

**Flock.** Not computed in FL. The rotations whose product it is are kept (2.2). TB:28 `loop` is still available but FL never calls it.

**Why it is there.** It is the one number that shows the field between the balls is curved: a frame carried round comes back turned.

### 2.4 The ball's own block D_i = d_i·σ

**Statement.** Each ball has two levels, at −|d_i| and +|d_i|, split along the direction d_i; |d_i| = ω/2.

**Code.** MM:80 "H = blocks D_i = d_i . sigma on each ball (2 levels: ground at -|d|, excited at +|d|; |d| = omega/2 ...)"; MM:88 initial d radial with length ω/2; MM:92–95 the block applied; TB:14 ω = 2.0.

**Grade.** MODEL CHOICE (two levels per ball, ω = 2; TB README line 15: "Model choices: c₀ = 0.5, ω = 2, κ = 0.25"). In the paper's language D_i is a Hermitian vertex block (NN paper line 457 region: "Hermitian vertex blocks Di"); here it is the trace-free 2×2 case.

**Flock.** FL:85–88 (`psi <- exp(-i h d.sigma) psi`); the length is now |d_i| = ω·rate_i/2 (FL:57). Kept in form, changed in size (see 3.2).

**Why it is there.** A ball needs something that can point and something that can tick; a two-level block is the smallest object that does both.

### 2.5 H = D + A and the connection energy identity

**What the paper states.** NN paper lines 457–470 and equation (1): "Let A∗ = −A be block-supported on E: Aii = 0, Aij = 0 for {i, j} ∉ E, and Aij unitary for {i, j} ∈ E, so Aji = −A∗ij. Set H = D + A." Then (1/8)·‖[H, H*]‖² = Σ over edges ‖D_i − A_ij D_j A_ij*‖² (Frobenius norms). Lines 544–545: "Hence the Frobenius self-commutator energy of D + A, the standard measure of non-normality, is exactly the connection energy measuring the failure of its Hermitian obstruction field to be parallel". With weighted edges (lines 517–519): "with weighted edges Aij = √wij Uij, Uij unitary, (1) holds as Σ wij‖Di − UijDjU∗ij‖²".

**What Lean states.** `NN-Lean/NonNormality/SelfCommutator.lean:137–141`, theorem `norm_sq_selfCommutator_div_eight`: for `hA : IsUnitaryConnection G A` and Hermitian `D i`, `‖(diagonal D + A) * (diagonal D + A)ᴴ - (diagonal D + A)ᴴ * (diagonal D + A)‖ ^ 2 / 8 = connectionEnergy G A D`. `connectionEnergy` is defined at line 112 as half the sum over ordered adjacent pairs of `‖D i - A i j * D j * (A i j)ᴴ‖ ^ 2`. Edge form: `norm_sq_selfCommutator_div_eight_eq_sum_edgeFinset` (line 257). Normal ⇔ parallel: `isStarNormal_iff_isParallel` (line 182). Kernel ≅ holonomy-fixed Hermitian matrices: `parallelSectionsEquivHolonomyFixed` (`Holonomy.lean:234`). Statement map: `NN-Lean/STATEMENTS.md` line 34 (row C5, "proved"). Card B137 (grade "theorem"): "⅛‖[H, H*]‖²F = Σ{i,j}∈E ‖Dᵢ − AijDjAij*‖²F".

**What the code does.** MM:206–215 `nnceCheck` builds its own dense matrix: blocks d_i·σ, and on each link the block U_ij one way and −U_ij† the other (MM:210, `Hr[b+s][a+r] -= u[0]; Hi[b+s][a+r] += u[1]`), unit weight. Left side: (1/8)‖[H,H*]‖² (MM:211–213). Right side: Σ_links 2·|d_i − R_ij d_j|² (MM:214). The factor 2 is ‖v·σ‖² = 2|v|², and R enters because U (d_j·σ) U† = (R d_j)·σ.

**Why the check proves it.** The left side knows only the dense matrix; the right side knows only the 3-vectors and the 3×3 rotations. They can agree on random d only if the identity holds and U is the correct lift of R.

**RUN (l3_run_01).**

| world | d | left | right | difference |
|---|---|---|---|---|
| 3 balls (TB, z = 3, 5) | rest | 5.2e-20 | 5.2e-20 | 1.2e-32 |
| 3 balls | random #0 | 4.48386946121 | 4.48386946121 | — |
| 3 balls | 200 random | — | — | worst relative 1.26e-15 |
| 7 balls (MM.makeWorld(1)) | initial radial | 88.5631038472 | 88.5631038472 | 7.1e-14 |
| 7 balls | 200 random | — | — | worst relative 1.49e-15 |
| control: one U replaced by I | random | 11.680 vs 11.447 (3 balls); 92.381 vs 91.149 (7 balls) | | fails by 2.0 % and 1.4 % |

The identity holds to rounding. Note that at the three-ball rest state both sides are zero, so the rest line of `t_tb1.js` (line 8) is a 0 = 0 check; the random-d rows are the real test.

**Match.** The identity in the code is the paper's, in the form the Lean theorem states (unit unitary edge blocks, A_ji = −A_ij*). Grade: LEAN · `norm_sq_selfCommutator_div_eight`; CARD · B137 (theorem); CHECKED · 1.5e-15 on these worlds.

**Does not match (one point, with the smallest repair).** The matrix checked by `nnceCheck` is not the matrix that moves the light. `applyH` (MM:96–99, "y_i += c U x_j ; y_j += c U^dag x_i") is Hermitian (RUN: largest |H − H†| entry 0.0e+0 on both worlds) and its links carry c_ij = c0·sech(d_ij/2), not 1. A Hermitian matrix is normal, so its own self-commutator is zero and it has no connection energy. The header line MM:4 "Non-Normality Is Connection Energy (H = D + A, edge mismatch energy)" and TB:7 "One matrix H = D + A (MM-MATH-V1) moves the light" read as if the two were one matrix. Smallest repair, checked: the paper's H for this world is K = D + i·(hop part of the light matrix). Its off-block part is exactly skew (RUN: 0.0e+0), and (1/8)‖[K,K*]‖² = Σ_links c_ij²·2·|d_i − R_ij d_j|² to 1.1e-15 over 100 random d on 3 and on 7 balls (RUN l3_run_05). This is the paper's weighted form with w_ij = c_ij². In words: same ball blocks, same hop, the hop turned a quarter turn. The comment at MM:206 can say so; nothing in the mathematics needs to change.

**Flock.** FL never calls `nnceCheck`. The right-hand side survives as the face energy (2.6).

**Why it is there.** It turns "the balls disagree" into one number, link by link.

### 2.6 The faces: face energy is the connection energy

**Statement.** The energy held on the faces is κ·Σ_links |d_i − R_ij d_j|². Each ball's field turns about the sum of the pushes on it.

**Code.** MM:147 `faceEnergy`; MM:145–146 `faceGrad` = 2κ·Σ_j (d_i − R_ij d_j); MM:160 `d_i' = G_i × d_i` with G = light spin + sea push + face push (a rotation, so |d_i| is kept).

**Link to the paper, RUN.** faceEnergy = (κ/2) × (right side of the identity): 6.16547097585 against 6.16547097585 on the 7-ball world with random d (l3_run_01). So the face energy is the unit-weight connection energy of the ball fields times κ/2. Grade: the identity LEAN (2.5); taking it as the energy of the faces, with κ = 0.25, is a MODEL CHOICE.

**Small mismatch.** The comment MM:140 says "2 kappa sum_j c-weighted (d_i - R_ij d_j)"; `faceGrad` (MM:146) has no c weight. Code and `faceEnergy` agree with each other; only the comment is off. Repair: drop "c-weighted" from the comment.

**Rest and the holonomy, RUN.** In the three-ball world the rest state is d = (0, 0, 1)·ω/2 on all three balls (l3_run_01) and the face energy is 6.5e-21. That is the paper's kernel statement at work (NN paper equation (4): parallel fields ≅ Hermitian matrices fixed by the holonomy): the triangle lies in the I–J plane, its loop turns about K by 0.64, and the only direction a turn about K leaves alone is K. In the seven-ball MM world no common axis exists; descending the faces alone from the radial start leaves 4.8712401 on the faces (connection energy 38.96992047, both sides equal; residual 9e-12). This is a computed value for that start, not a proved minimum.

**Flock.** FL:58 finds the rest directions with `MMr.restState(... withSea:false ...)`, which uses `MMr.faceGrad`; FL:93 applies the push. Kept, with the change in 3.3.

**Why it is there.** The faces are how one ball feels its neighbours' directions; the identity says that feeling is exactly the non-normality of the companion matrix.

### 2.7 Link strength c_ij = c0·sech(d_ij/2) and the instant hop

**Statement.** The light hops between two balls with amplitude c_ij·U_ij, c_ij = c0·√(1 − Γ_ij²) = c0·sech(d_ij/2).

**Code.** MM:81, MM:85 `c:opts.c0/Math.cosh(d/2)`; TB:6 "Each link is a VOTKP peel step: Γ = tanh(d/2), strength c0·sech(d/2) = c0·sqrt(1 − Γ²)".

**Grade.** √(1 − Γ²) is the amplitude passed by one reflecting step (lineage 1, LEAN `step_matching`, `flux_balance` as cited at FL:6). Using it as the hop amplitude of a link, with c0 = 0.5, is a MODEL CHOICE. Not in any of his papers as a statement about balls: not found.

**What the check found.** GCC.out lines 4–7: ρ_B/t² = 0.1875 = c_AB² at t = 0.001 … 0.03. Light is in B from the first instant: the hop has no travel time. GCC.out lines 18–22: the strengths depend on the centre distance only and do not change when the faces open a gap.

**Flock.** Replaced (3.2). The numbers survive only as a reference: FL:60.

### 2.8 The sea: the projector P and its motion

**What the IQGT states.** IQGT-Lean `IqgtGrassmannian/Rebuild.lean:31` `def IsTangent (P V : R) : Prop := V = P * V + V * P`; `Basic.lean:30` `tangent_offdiag` ("Corollary 3.1. If Π² = Π and V = ΠV + VΠ, then ΠVΠ = 0, (1−Π)V(1−Π) = 0 and V = ΠV(1−Π) + (1−Π)VΠ"); `Basic.lean:67` `def Q (P V W) := trace (P * V * W)`; `Basic.lean:107` `metric_control` ("Theorem 6.1 ... (Im Q(V,W))² ≤ g(V,V) g(W,W) − g(V,W)²"); `Rebuild.lean:112` `two_trace_PVV` (2·Tr(ΠVV) = Tr(VV) for tangent V). DT-Lean `DiracTime/ProjectorBlocks.lean:68–69` `metric_block`: "g(V, W) = ½ Tr(V W) = Re Tr(X Y†)". WPMK lines 180–195, Proposition 4 and equation (3): for Ṗ = −i[H,P], "g := ½‖Ṗ‖²_F = ½‖[H,P]‖²_F = E_B" [T]. DT paper line 761: "for Ṗ = −i[H,P], g = ‖PH(I−P)‖²_F".

**What the code does.** MM:125–129: P is the projector onto the lowest k levels of the whole matrix, with the cut placed in the largest gap near half filling (`chooseCut`, MM:126; "a contour must sit in a gap"). MM:154–159: P' = −i[H, P]. MM:171–175: after each step P is pulled back to the nearest projector (McWeeny, P ← 3P² − 2P³). MM:197–198 `seaSpeed`: g = ½‖P'‖². MM:138–139: the sea pushes ball i with its spin density measured from rest.

**RUN (l3_run_04, three balls, t = 10 after a kick at A).** g from `seaSpeed` 1.71973737797; ‖P H (1−P)‖² computed separately from the dense matrix 1.71973737797; |P² − P| largest entry 1.1e-16; Tr P = 2.000000000000.

**Match.** Projector, tangent (the motion is a commutator with P, so it is off-diagonal), and g agree with the sources. Grade: tangent structure LEAN · `tangent_offdiag`; g = ½Tr(V²) LEAN · `metric_block` / `two_trace_PVV`; g = ‖PH(1−P)‖² PROVED · WPMK Proposition 4 / equation (3), CHECKED · 12 digits here. The sea itself (one Slater-type projector of the whole matrix, rank from `chooseCut`, pushing the balls through its spin density) is a MODEL CHOICE.

**Does not match (three points).**
1. MM:3 lists "IQGT (projector, tangent, metric g, curvature)". No curvature of the sea is computed anywhere in MM. The only curvature in the file is the triangle holonomy of the field (2.3), which is hyperbolic geometry and not the Berry curvature Ω of the projector. Repair: remove "curvature" from the header, or add the readout Ω = i·Tr(P[V,W]) (sign as IQGT; `curvature_block`, DT-Lean ProjectorBlocks.lean:75–76) if it is wanted.
2. MM:124 says "electron sea P (rank N projector ...)". In the three-ball world the rank is 2, not 3 (RUN: `kSea` = 2; levels −1.4696 −1.2700 −0.2605 0.5304 0.7300 1.7395; gaps at cuts 2, 3, 4 are 1.0095, 0.7909, 0.1996, and `chooseCut` takes the largest). In the seven-ball world the rank is 7. Repair: the comment should say "rank from the largest gap near half filling".
3. With the cut at exactly half filling (k = 3) the three-ball sea is a frozen product state: every ball reads ν = (0, 1) (RUN l3_run_02). The cut at 2 is what makes the three-ball sea able to move at all.

**Flock.** Dropped (3.4).

**Why it is there.** The sea is the many-electron background the balls sit in; the projector is the smallest honest object that says which states are filled.

### 2.9 The Weight Between readouts: C, ν, X, τ, S

**What the papers state.** WPMK lines 337–352: "Cut an orthogonal projector P on ℂⁿ by a fixed isometry E: ℂᵐ → ℂⁿ into the accessible block C = E†PE, with 0 < C < I. Then C − C² = P₁₂P₁₂† [T; L], the census of the cut. The offset τ = Tr[log(I−C) − log C] = log det(I−C) − log det C is the log-odds of the block being empty against full". Card B151 (grade "theorem"): "τA = Σi εi = log det(I − CA) − log det CA = log P(NA = 0)/P(NA = L) ... 0 < CA < I". The bridge Γ = 1 − 2ν ↔ tanh(τ/2): CSL cites "offset-lean asymmetry_eq_tanh_half_offset; nonnormality-connection-energy-lean tanh_half_log_odds" (CSL line 610 region); `tanh_half_log_odds` is at `NN-Lean/NonNormality/Admissible.lean:177`.

**What the code does.** MM:189–196 `ballCensus`: E is the embedding of ball i's two components; C_i is the 2×2 block of P; ν its two eigenvalues; Γ = 1 − 2ν; `trX = Tr C − Tr C²` (MM:193–194, "(C^2)_ii = C_ii^2 + X_i -> Tr X_i = Tr C_ii - Tr C_ii^2 for a projector"); τ = log((1−ν₀)(1−ν₁)/(ν₀ν₁)); S = 1/(ν₀(1−ν₀)) + 1/(ν₁(1−ν₁)).

**RUN.** Tr X_i against Σ ν(1−ν): differences 6e-17, 8e-17, 3e-17 (l3_run_04).

**Match.** C, the census Tr X = Tr(C − C²), τ and S are the papers' objects with m = 2. Grade: census identity PROVED · WPMK (and "[L]" there); offset as log-odds CARD · B151 (theorem); Γ bridge LEAN · `tanh_half_log_odds`. One naming point: "weight between" is used for two different numbers in his papers, E_B = ‖PH(1−P)‖² (WPMK line 171–172, "the weight between P and 1−P") and the census block X_A (working notes `/home/claude/text/PATH_NOTES.md` line 101, which are notes and not his paper). MM computes both: g for the whole sea (MM:198) and Tr X_i per ball (MM:194). The film should name which one is on screen.

**Does not match.** The readout is used outside its stated domain 0 < C < I in the three-ball rest state. This is the C4 result; see section 4.

**Flock.** Dropped with the sea (3.4).

**Why it is there.** It is what one ball can know about the sea from its own two levels: how full, how mixed, and which way the odds lean.

### 2.10 The offset speed limit τ̇² ≤ 4·g·S

**What the papers state.** WPMK lines 362–380, Theorem 8: "For a differentiable family of orthogonal projectors, with g = ½‖Ṗ‖²_F and S = Tr[(C(I−C))⁻¹], τ̇² ≤ 4gS. Equality holds if and only if Ṗ = λ[P,[P,F]] for real λ, where F = EWE†, W = −(C(I−C))⁻¹. [T; for rank one a bound of Mandelstam–Tamm type; N: largest ratio 0.911 over 500 driven cases, equality case to 7×10⁻⁹]". Corollary 9 (line 381): "a record moves only as fast as the weight between ... |τ̇| ≤ 2√(E_B·S). If PH(1−P) = 0 the offset is frozen." DT paper lines 757–761 states the same and cites "[T; The Offset Speed Limit, Theorem 1]".

**What Lean states.** One accessible mode only: `/home/claude/src/neutrinos-leave-lean/Neutrinos/Memory.lean:49` `offset_gap_identity` (the exact gap 4gS − τ̇² = 4(Im b̄ḃ)²/(c(1−c))², cleared of denominators), `:56` `offset_gap_nonneg`, `:65` `one_mode_speed`. The general m × m statement: CSL line 2201, "The offset speed limit (Appendix 15.4) has a scalar case in a local Lean build not yet in a public repository; the general equality case is open in Lean." DT-Lean has no offset theorem (search for "offset" in `DiracTime/*.lean` finds only the knot offsets of `PhaseSilence.lean`).

**What the code does.** MM:217–222 `tauDot`: τ' = −Tr[(C(I−C))⁻¹·C'], with C' the ball block of P' (this is the derivative of log det(I−C) − log det C). The ratio τ'²/(4·g·S) is formed in `t_tb1.js` line 14 and GCC line 46, with g from `seaSpeed` (whole sea) and S from `ballCensus` (one ball). Here m = 2 (two components per ball), so the Lean one-mode theorem does not cover it; the paper theorem does.

**Why the check proves it.** τ', g and S come from three separate functions. If any were wrong by a factor, a ratio above 1 would appear somewhere in a long driven run. I also compared `tauDot` with a forward difference of τ.

**RUN (l3_run_02, l3_run_04).**

| world, kick | span | largest τ'²/(4gS), all balls, every step |
|---|---|---|
| 3 balls (ln 3, ln 5), kick A | t ≤ 10 | 0.02055 |
| 3 balls, kick B | t ≤ 10 | 0.01994 |
| 3 balls, kick C | t ≤ 10 | 0.01982 |
| 3 balls at the README steps, kick A | t ≤ 10 | 0.0206 |
| 7 balls (MM.makeWorld(1)), kick ball 0 | t ≤ 3, every 10th step | 0.02570 |

`tauDot` against the forward difference: agreement to 4 digits from t = 0.1 on (for example −4.8262 against −4.8259 at t = 1). At t = 0.01 they disagree (−599 against −6931 for A) because ν₀ ≈ 5.6e-17 there and the difference of logs is rounding noise; this is the domain problem of section 4, not an error in `tauDot`.

**Match.** The bound holds in every run, far from saturated. Grade: PROVED · WPMK Theorem 8 (= The Offset Speed Limit, Theorem 1, as cited); LEAN for one mode only (`offset_gap_nonneg`); CHECKED here, largest ratio 0.026. The ratio is small for a reason visible in the numbers: S is dominated by 1/ν₀ of a nearly empty level (S up to 1.8e16), so the ceiling is very high. The reading "rate is weight" is graded by the papers themselves as a READING, open (CSL line 637 heading "Rate is weight: a reading, with its boundary", ending "[Reading; Open]"; DT paper line 3535, "Rate is weight | OPEN as a reading; identities proved").

**Flock.** Dropped with the sea (3.4).

**Why it is there.** It says a ball's record of the sea cannot change for free: its speed is capped by how strongly kept and not-kept are coupled.

### 2.11 Dirac Time: what "the clock is read from memory: the offset" is, exactly

The words at MM:5, "Dirac Time (the clock is read from memory: the offset)", are not found as a sentence in the Dirac Time paper or in DT-Lean. What the sources do say:

- Memory comes first. DT-Lean `README.md` line 23: "Memory comes before the clock. A present state is worth remembering only as far as some future observation can tell it apart." DT paper line 16: "The Dirac-Time programme begins from memory, not from a metric, a clock, a particle ontology, or an assumed time coordinate."
- Duration is a readout. DT paper line 68: "Physical duration is a calibrated readout".
- A rate is a scale on the gaps and is seen only against another clock. DT-Lean `DiracTime/CommonClock.lean:28` `common_gap_scaling` ("Corollary P4.1. All gaps of the frame generator share the one scale factor τ̇"), `:36` `rate_shift_unique`, `:62` `rescale_same_eigenvectors` ("Rescaling H ↦ s H (s ≠ 0) keeps every eigenvector"), `:67` `rescale_scales_gaps`. DT paper line 755: "A constant is read only as a relative phase ... that is, only against another clock."
- The signed record and its ceiling. DT paper lines 757–761: the offset τ_off = log det(I−C) − log det C of a projector read through a region, with τ̇_off² ≤ 4gS.

So, exactly: in MM the per-ball "offset clock" is τ_i of 2.9, a log-odds record of the sea read on ball i; Dirac Time bounds how fast it can move (2.10). It is a readout. It is not used as any ball's time: MM:150–170 advances every ball with one step h in one shared t, and GCC.out line 32 says so ("no ball uses its own tau as its time"). Grade of the MM header sentence: READING. Grade of the ingredients: LEAN (common clock corollaries), PROVED (speed limit).

**Flock.** The Lean statement that carries over is `rescale_same_eigenvectors` / `rescale_scales_gaps`: scaling ball i's block by rate_i keeps its two eigenvectors (its direction) and scales its gap by rate_i. That is what FL:57 does. That the scale is 1/z is not in Dirac Time; it is the Flock's HYPOTHESIS (3.2).

---

## 3. The honest ledger of the step from the matrix to the Flock

### 3.1 Kept

| Ingredient | MM / TB | FL | Note |
|---|---|---|---|
| Hyperboloid placement, one peel step per arm | MM:12, TB:12 | FL:39 | N = 3, 4, 7 by `ARMS` (FL:26) |
| Link distance d_ij | MM:40 | FL:41, FL:48 | now also the travel time |
| Link rotation R_ij | MM:39 | FL:41 | unchanged function |
| SU(2) lift U_ij | MM:46–51 | FL:41; applied FL:79–82 | unchanged function |
| Ball levels d_i·σ, exact rotation of the two levels | MM:92–95 | FL:85–88 | size changed, see 3.2 |
| Light spin torque on the ball field | MM:141–142 `spinLight`, MM:160 | FL:70 `bloch`, FL:92 | same Bloch vector; FL adds a switch `torque` (FL:37) |
| Face energy as the source of rest directions | MM:145–147, MM-REST MM:227–235 | FL:58 | same `restState`, sea off |
| Field turns by a rotation, |d_i| kept | MM:160 | FL:89–95 | FL uses an exact rotation per step |
| One quantum of light, placed with spin across the source ball's field | MM:130–135 | FL:66–69 | same construction |

### 3.2 Changed

**Instant hop → travelling light with scatterers.** MM:96–99 moves amplitude c·U between balls in the same instant. FL:75–83 gives each link a forward and a backward stream of samples; light enters and leaves a ball through a port (FL:79–80, a rotation by angle √(γ·h) between the ball and the stream), moves one sample per step (speed 1, FL:4–5), and at each mark splits by ρ = Γ = tanh(step/2) and √(1 − ρ²) (FL:81–82). Centre–arm links carry one face at half the step (FL:47). Arm–arm links carry the two faces of the centre cell and, where g = sinh h_a·sinh h_b > 1, a gap mark with ρ = tanh(κ_g·δ) (FL:48–52). Grades as the Flock states them: face step LEAN (lineage 1); gap layer HYPOTHESIS (FL:9); checked by K1, K3, K4 in `fl_check_01.out` lines 1–10. One parameter is new and not graded in the Flock's README: the port rate γ = 0.6 (FL:37). It replaces c0 as the number that sets how fast a ball exchanges light with a link. It is a MODEL CHOICE and should be listed as one.

**One shared level spacing → a rate per ball.** MM:88 gives every ball |d| = ω/2 (GCC.out lines 10–12: spacing 2.000000 on A, B, C). FL:39 sets rate = 1 at the centre and e^(−r) = 1/z one step out; FL:57 sets |d_i| = ω·rate_i/2; FL:88 adds h·rate_i to the ball's own running time. Checked by K5 (`fl_check_01.out` line 11: ratios 3.000000, 5.000000, 7.000000). Grade: HYPOTHESIS, clock ratio z (FL:11). What is LEAN here is only that scaling a block scales its gap and keeps its eigenvectors (2.11).

**Face push against the live neighbour → against the neighbour's rest direction.** MM:146 uses the neighbour's present d_j, in the same instant. FL:93 with `push:'static'` uses `W.dRest[j]`; a neighbour's change reaches a ball only as light. Grade: MODEL CHOICE (FL:14–15). The delayed variant (FL:16–17) is kept for exploring; K6b shows rest is unstable under it (`fl_check_01.out` line 13).

**Consequence found by run, not stated in the Flock files.** With clocks in the ratio z the ball blocks have different sizes, so D cannot be parallel on any link: ‖D_i − U D_j U†‖² ≥ 2·(|d_i| − |d_j|)². The faces therefore hold connection energy at rest. RUN l3_run_05, `MM.nnceCheck(W, W.dRest)` on Flock worlds (both sides of the identity agree in every row):

| Flock world | connection energy at rest | part forced by unequal spacings, 2·Σ(|d_i| − |d_j|)² |
|---|---|---|
| N = 3, clocks z | 2.204444444 | 2.204444444 |
| N = 3, clocks equal | 5.2e-22 | 0 |
| N = 4, clocks z | 3.807954405 | 3.752925170 |
| N = 4, clocks equal | 0.4737377309 | 0 |
| N = 7, clocks z | 8.105871463 | 7.735147392 |
| N = 7, clocks equal | 7.145205479 | 0 |

So "rest: nothing held on any face" (TB README line 10) is true for three balls on one shared clock and no longer true once the clocks differ. For three balls the whole amount is the clock mismatch; for 4 and 7 balls part of it is there even with equal clocks, because the triangles in different planes have no common axis (2.6). By the identity, this is the statement that the companion matrix D + i·hop of the Flock is not normal at rest. This is a computed fact about the model, CHECKED · rounding; no physical reading is claimed for it here.

**Name clash to avoid in the film.** In MM, τ is the offset (log-odds of the sea on a ball, MM:195). In FL, `S.tau[i]` is the ball's own elapsed clock time (FL:88), and `tau` at FL:81 is a scatterer's pass amplitude. Three different things carry one letter.

### 3.3 Kept only as a reference

`FL.modes` (FL:117–119) calls `MMr.denseH` on the Flock's balls with link strengths set at FL:60, c = 0.5·Π√(1 − ρ²) over the marks. For a centre–arm link this equals MM's c0·sech(d/2). For an arm–arm link it is the product of the face (and gap) pass amplitudes, which is not MM's c0·sech(d_BC/2). So the "instantaneous matrix" in `fl_check_01.out` line 24 is a new reference matrix, not the Three Balls matrix; its eigenvalues should not be compared digit for digit with the TB README's.

### 3.4 Dropped

| Dropped | Where it was | In FL |
|---|---|---|
| The sea projector P, its motion P' = −i[H,P], McWeeny purification | MM:125–129, 154–159, 171–175 | absent |
| Sea push on the balls | MM:138–139, 160 | absent |
| C, ν, Γ = 1 − 2ν, Tr X, τ, S per ball | MM:189–196 | absent |
| g = ‖PH(1−P)‖², τ', the speed-limit ratio | MM:197–198, 217–222 | absent |
| Energy ledger (light + sea + faces, work done by breathing steps) | MM:177–180, TB:22–23 | absent; books are light count only (FL:102–103; README line 25) |
| Bond currents, ball powers | MM:181–188 | absent |
| Connection energy check, triangle loop | MM:199–215, TB:28 | not called |
| Breathing steps | TB:21–23 | README line 25–26: "gap lengths are held at the mean steps" |

The Flock README says it plainly (line 25): "Not in this version: the electron sea (it needs its own travel time)".

### 3.5 Open item: what bringing the sea back with travel time would need

Stated as needs, with no result claimed. All of it is untested.

1. **The object.** In MM the sea is a projector on the balls' space ℂ^(2N), and one matrix moves all of it at once (MM:154–159). In the Flock the one-quantum space is larger: two components per ball plus the forward and backward samples of every link (FL:44, FL:63–64). One Flock step with the ball fields held fixed is a unitary map V on that larger space (this is what K2 checks: total 1 to 1e-12). A sea with travel time would be a projector 𝒫 on the larger space, of declared rank, moved by 𝒫 ← V 𝒫 V†. A change made at one ball then reaches another only after the link's crossing time, by the same rule as the light.
2. **The equation for the readouts.** The ball block is still C_i = E_i† 𝒫 E_i with E_i the embedding of ball i's two components, and C − C² = P₁₂P₁₂†, τ = log det(I−C) − log det C and S need nothing else (WPMK lines 337–352). Theorem 8 needs "a differentiable family of orthogonal projectors" (WPMK line 362–364). The Flock moves in finite steps, so either a continuous-time generator for the travelling field is written down (then g = ½‖𝒫̇‖² and the theorem apply as they stand), or a finite-step form of the bound is proved. A finite-step form was not found in the sources.
3. **Which projector.** MM takes the levels below a cut that sits in a gap (MM:125–126). A step map V has phases on a circle, not levels on a line: there is no "lowest". A rest sea must satisfy V 𝒫 V† = 𝒫, so it is a spectral projector of V onto an arc of the circle, and the arc has to be chosen and has to end in gaps. That choice is open.
4. **How many link modes are filled.** Each link holds 4·n samples with n ≈ length/h (FL:44). The number of states in the larger space therefore depends on the step size h. A rank for 𝒫 that does not change when h is halved needs a declared cutoff or a declared filling of the link modes. Open.
5. **The push back on the balls.** MM pushes ball i with s_i(P) − s_i(P_rest) (MM:139). The same formula on C_i would be local and automatically delayed. Whether rest stays still under it must be checked (K6 for the faces holds only because the push is static; the delayed face push is unstable, K6b).
6. **An energy for light in transit.** MM's ledger needs an energy for every part. The Flock books light count only (README line 25). A sea ledger needs the energy of the field in the links first.

His own requirement for it is on record (`/home/claude/balls/w/REQUIREMENTS_v1.md` line 50, P7: "The sea is the shared beam all the balls hang from"; line 79, item 11: "How a shared beam is to respect the travel time of req 6 was not said").

---

## 4. The C4 line: why the per-ball offset reads −Infinity

`gap_clock_check_01.out` lines 25–30 print "tau-tau0 −Infinity" for A, B and C at every time.

**What is infinite.** Not τ at the printed times. It is the reference τ₀, taken at t = 0 (GCC line 44, `C0 = MM.ballCensus(W, S).map(c => c.tau)`), which is +Infinity; a finite τ minus +Infinity prints −Infinity (GCC line 46).

**Which quantity hits 0.** ν₀, the smaller eigenvalue of each ball's block C_i, is exactly 0 at t = 0, so ν₀·ν₁ = 0 in the denominator of MM:195 and τ = log(…/0) = +Infinity; S = 1/(ν₀(1−ν₀)) + … is +Infinity as well. RUN l3_run_01: at t = 0, ν = (0.0000000000000000, 0.6287) on A, (0, 0.6657) on B, (0, 0.7055) on C; τ = Infinity and S = Infinity on all three.

**Why ν₀ = 0, from the code and a run.** At rest all three ball fields point along K: d = (0, 0, 1) (RUN). All three link rotations are turns about K (the triangle lies in the I–J plane), so every U is diagonal (RUN l3_run_02: U_AB = U_AC = identity, U_BC = diag(0.9487 − 0.3162i, 0.9487 + 0.3162i)). The matrix then splits into an "up" half and a "down" half that never mix. The sea has rank 2 (2.8) and both filled levels lie in the down half (rest sea: largest up–up entry 3.4e-20). Every ball's up level is exactly empty.

**After the kick.** The light's torque tips the fields off K, the halves mix, and ν₀ leaves zero: 5.6e-17 at t = 0.01, 5.1e-5 at t = 1, about 1e-3 to 4e-2 later. τ is then finite: about 37 at t = 0.01, 9.4 at t = 1, between 2 and 9 afterwards (RUN l3_run_02). So the offsets exist and move; the printed column hides them.

**Defect of the check or of the readout?** Both, in different senses, and they have different repairs.
- The printed −Infinity is a defect of the check: it subtracts a baseline that is not finite. Smallest repair: print τ_i itself, or take the baseline at the first printed time. The τ' and "limit" columns of the same lines are correct and are reproduced by my run to the printed digits (for example A at t = 1: τ' −4.826, limit 8.054e-4).
- The underlying cause is that the readout is applied outside the domain its theorem states. The offset and the speed limit are stated for 0 < C < I (WPMK line 346; card B151). The three-ball rest sea has C_i with an eigenvalue exactly 0, by symmetry. `ballCensus` (MM:195) does not guard against this. Smallest repair: return "outside 0 < C < I" (not a number) when an eigenvalue is within rounding of 0 or 1. This is not a fault in the theorem.
- The seven-ball MM world does not have the problem: at t = 0, ν = (0.080, 0.912) on the centre ball, all τ₀ finite (0.1006, −0.0172, …), and τ − τ₀ after t = 3 reads −0.32, −0.22, 0.31, 0.53, −0.15, −0.83, 0.55 (RUN l3_run_02).

One more consequence: because S is huge while ν₀ is tiny, the three-ball "limit" values (≤ 0.021) say little about how tight the bound is. They show it is not violated.

---

## 5. Source against code: the list of mismatches

1. **Two matrices under one name** (2.5). The matrix checked for connection energy (skew links, unit weight) is not the matrix that moves the light (Hermitian links, weight c). Repair: say K = D + i·hop; then the paper's weighted identity holds with w = c² (checked, 1.1e-15).
2. **Header lists IQGT curvature; none is computed for the sea** (2.8).
3. **"rank N projector" in the comment; rank is chosen by the largest gap** (2.8): 2 for three balls, 7 for seven.
4. **"c-weighted" in the comment at MM:140; `faceGrad` is not c-weighted** (2.6).
5. **Offset readout used where an eigenvalue of C is 0** (section 4).
6. **Header sentence "the clock is read from memory: the offset"** is not a sentence of Dirac Time (2.11). The sources support: memory first; rate read against another clock (LEAN); offset bounded by 4gS (PROVED). Grade of the sentence: READING.
7. **"Weight between" names two numbers**, E_B and X_A (2.9). MM computes both.
8. **`t_tb1.js` cannot be rerun from `/home/claude/balls/w/tb`** (missing `../surprise/src/lh_math.js`). The README numbers it supports were reproduced another way (2.3): loop 0.7110545751; eigenvalues −1.462 −1.231 −0.307 0.538 0.769 1.693; leading shares 0.381 0.345 0.274; margin 0.864.
9. **Flock reference matrix is not the Three Balls matrix** on arm–arm links (3.3).
10. **Flock port rate γ = 0.6 is an ungraded parameter** (3.2).
11. **Flock with clocks z holds connection energy at rest** (3.2); the Three Balls README line "nothing held on any face" does not carry over.
12. **Curvature sign.** IQGT-Lean `Basic.lean:105` docstring writes Ω = 2·Im Q; `Rebuild.lean:320–321` and DT-Lean `ProjectorBlocks.lean:75` write Ω = −2·Im Q. The proved inequalities are the same either way. Nothing in MM depends on the sign; noted so the film does not show a signed Ω without choosing.

---

## 6. Open or not claimed

- The sea with travel time: open, section 3.5. No result exists.
- The general (m × m) offset speed limit in Lean: open (CSL line 2201). Only one mode is LEAN.
- "Rate is weight": a READING, open, by the papers' own grade.
- Clock ratio 1/z between a ball and the centre: HYPOTHESIS (Flock). Not in Dirac Time.
- The rate between two balls that are not one step apart (B and C): not stated (REQUIREMENTS line 75); FL gives each arm ball 1/z of its own arm.
- Gap layer tunnelling sech(κ_g·δ): HYPOTHESIS (Flock).
- Hop strength c0·sech(d/2) as a law for links between balls: MODEL CHOICE; not found in any paper.
- The sea as one projector with the cut of `chooseCut`: MODEL CHOICE.
- The least face energy of the seven-ball world: the value 4.8712401 is one descent from one start; untested as a global minimum.
- Whether the rest connection energy of the Flock with clocks z has a physical reading: not claimed.
- Thomas turn for unequal steps: CHECKED, not LEAN.
- Not run here: the browser pages; `fl_check_01.js` (its stored output was read, not rerun); the breathing-steps books of `t_tb1.js` line 17–18.

---

## 7. Picture ideas for the film

1. **The carried arrow.** Three balls A, B, C on the field. An arrow leaves A, is carried to B, to C, and home. It comes back turned. The shaded triangle fills as the arrow travels; two numbers count up together and stop equal: turn 0.7110545751, area 0.7110545751. Then the closed form 2·arctan(Γ_I·Γ_J) lands on the same digits.
2. **Faces as springs, one number.** Each ball carries its field arrow d_i. On every link a faint copy of the neighbour's arrow, carried across by R_ij, sits beside the ball's own. The gap between the two arrows glows; the sum of the glows is the counter "connection energy". Scramble the arrows: left and right of the identity tick in step (4.48386946121 = 4.48386946121). Let them relax: three balls go dark with every arrow along K, the axis of the loop.
3. **The quarter turn.** Show the light matrix (balanced, Hermitian, its self-commutator zero). Turn its hop part by a quarter turn (multiply by i): the companion matrix appears and its self-commutator lights up exactly where the faces glow. One line on screen: same D, same hop, turned.
4. **The sea and the empty level.** Each ball shows two bars, ν₀ and ν₁. At rest the lower bar is exactly empty on all three balls and the offset dial sits off the scale (0 < C < I not met). Kick A: the bar lifts from zero (5e-5 at t = 1) and the dial swings in, 37 → 9 → between 2 and 9. Beside it a ceiling gauge shows τ'²/(4gS) staying under 0.021 of the allowed 1.
5. **Instant against travelling.** Split screen, same kick at A. Left (matrix): B brightens from the first frame, ρ_B = 0.1875·t². Right (Flock): a pulse leaves A, meets the face at half the step, a quarter returns (Γ² = 0.25) and three quarters pass, and B stays dark until t = 1.0986.
6. **The flock of clocks loads the faces.** Three balls with clock hands. With equal clocks the faces are dark (0). Switch the clocks to the ratio z: hands run at 1, 1/3, 1/5, the field arrows shrink to match, and the faces light up at rest with 2.204. Caption with the grade on screen: clock ratio z, HYPOTHESIS; the 2.204 is computed.
