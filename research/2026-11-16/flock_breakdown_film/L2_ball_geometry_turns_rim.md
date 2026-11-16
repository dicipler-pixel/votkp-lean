# L2 — The one ball beyond the single face: geometry, refraction, total return and the gap, pressure, turns, the rim, the hypothesis layer

Lineage 2 of the breakdown of the Flock of Balls on the Field. Jeromie Beasley. 16 Nov 2026. AI-assisted.

Read for this report, in full: `PLAN_light_at_the_hypersurface.md` (M2, M3, M5, M6, M7, H, and sections 3–9), `LEDGER_build_v2.md`, `REVIEW_fable_v1.md`, `lh_math_v1.js`, `fl_math_v1.js`, `fl/README.md`, `fl_check_01.out`, `tb/gap_clock_check_01.out`; the cited Lean files at the cited lines; the ten atlas cards in `coverage.json`. Lean was not compiled here; "LEAN" below means "the theorem is in the file at that line", not "re-verified".

Scratch scripts (all in `/home/claude/balls/breakdown/scratch/L2/`), each run once, outputs saved beside them:

| Script | Command | Output |
|---|---|---|
| `l2_geom_01.py` (`# SCRIPT: L2-GEOM-01`) | `python3 l2_geom_01.py` | `l2_geom_01.out` |
| `l2_flock_01.js` (`// SCRIPT: L2-FLOCK-01`) | `node l2_flock_01.js` | `l2_flock_01.out` |
| `l2_sign_01.js` (`// SCRIPT: L2-SIGN-01`) | `node l2_sign_01.js` | `l2_sign_01.out` |

Path key: `LH/` = `/home/claude/balls/in/367c3aed-Light_at_the_Hypersurface_Mixer_v2_Source/`; `FL/` = `/home/claude/balls/w/fl/`; `TT/` = `/home/claude/votkp-lean/two-trees/lean/`; `ATLAS` = `/home/claude/dicipler-pixel/relational-atlas-lean/atlas/coverage/coverage.json`. Three repos were cloned read-only into `/home/claude/gh/` (square-case-lean, upg-lean, maxwell-lean). No web pages were fetched.

---

## 1. Summary

The one ball is the hyperbolic ball in the peel coordinate. A peel step B(u, r), r = ln z, carries the centre to a ball at hyperbolic distance r along arm u; in the drawn ball that point sits at radius Γ = tanh(r/2) = (z − 1)/(z + 1). The face of that step is the plane of points equally far from the centre and from the new ball; it crosses the arm at r/2. Two faces on perpendicular arms are compared by one number, g = sinh h_a · sinh h_b (h = r/2): they cross at the angle arccos g when g < 1 and stand apart by δ = arccosh g when g > 1. For equal steps g = 1 is the wall Γ² = ½, z = 3 + 2√2, R = T. The centre and two arm balls make a right triangle, cosh d = cosh r_I · cosh r_J, and its area is the Thomas turn 2 arctan(Γ_I Γ_J). All of these were recomputed here independently and hold to rounding (section 3). On top of that geometry the one-ball page puts refraction (a sin²θ kept), total return and an evanescent gap film, the push 2R, the square that turns, locks or runs, and the action of a step on light directions on the rim. The Flock inherits the positions, the faces, the link lengths, the order of the face crossings on a link, the Thomas turn (as the rotation carried by an arm–arm link), g and δ. Its two new hypotheses stand on rows that already exist in the one-ball plan: the "gap layer" is table H row 5 with the M3 film evaluated at one special incidence; the "clock ratio z" is the M7 radar reading of the Lean identity (1 + Γ)/(1 − Γ) = z, moved from a statement about returned light to a statement about a ball's own rate. One real mismatch was found in the Flock code: the sign given to a face on the arm–arm links is opposite to the sign the same face has on the centre–arm links, and the run shows this changes where the light goes (section 4, item 1).

---

## 2. Sources, opened and confirmed

### 2.1 Lean theorems (file:line, exact statement)

| Name | File:line | Exact statement | What it does and does not cover |
|---|---|---|---|
| `thomas5` | `TT/PeelTrees.lean:285` | `theorem thomas5 : M4.mul Lz5 Rz5 = M4.smul 9409 (M4.mul (B5 .pi) (B5 .pj)) := by decide` | Ratio 5 only. `Rz5` (`:284`) is `⟨97,0,0,0, 0,65,72,0, 0,-72,65,0, 0,0,0,97⟩`: rotation about k with cos = 65/97, sin = 72/97. Docstring `:281-282`: "Thomas rotation, exact (peel ratio 5): B_i B_j = L R with L a pure boost (symmetric, Lorentz) and R a rotation about k". |
| `thomas7` | `TT/PeelTrees.lean:295` | `theorem thomas7 : M4.mul Lz7 Rz7 = M4.smul 113569 (M4.mul (B7 .pi) (B7 .pj)) := by decide` | Ratio 7 only; cos = 175/337, sin = 288/337 (`Rz7`, `:294`). |
| `thomas_half_angle` | `TT/PeelTrees.lean:302` | `theorem thomas_half_angle : (72 : Int) * 9 = 4 * (97 + 65) ∧ (288 : Int) * 16 = 9 * (337 + 175) := by decide` | Integer arithmetic saying sin/(1 + cos) = 4/9 and 9/16, that is tan(θ/2) = Γ² at ratios 5 and 7. Docstring `:301`: "Thomas half-angle in the peel coordinate: tan(theta/2) = sin/(1 + cos) = Gamma^2." It is not a statement for general z. |
| `thomas_general` | `TT/PeelTrees2.lean:365` | `theorem thomas_general (z : Int) : M4.mul (Lint z) (Rint z) = M4.smul (Dz z * Dz z) (M4.mul (Qz z .pi) (Qz z .pj))` | Every integer z, **equal steps**, cleared of denominators. `Rint` (`:357`): "D times the rotation about k with cos = 4z(z^2+1)/D, sin = (z^2-1)^2/D", D = z⁴ + 6z² + 1. Unequal steps are not in Lean. |
| `comm_trace` | `TT/PeelTrees4.lean:35` | `theorem comm_trace (s v : R) : (comm s v).tr = 2*(s*s*s*s) - v*(s*s)*((s*s - 1)*(s*s - 1) - v*(s*s))` | The commutator trace of two Riley meridians over any commutative ring: tr[a,b] = 2 − v((s − 1/s)² − v) (docstring `:33-34`). The form 2 − 4 sinh⁴(r/2) is the case v = 2 sinh²(r/2); that case is named only in the docstring of `band_bound` (`:101-103`: "2 − tr[a,b] ≤ (s − 1/s)⁴/4 = 4 sinh⁴ x, with equality at v = 2 sinh² x. When sinh x < 1 (Γ² = tanh² x < 1/2, the Schottky line) this is below 4"). The plan grades the sinh⁴ form `PROVED · Two Trees v4 (sharpness text)` plus `CHECKED`, which is right. Checked here: G8. |
| `schottky_five_below` | `TT/PeelTrees.lean:163` | `theorem schottky_five_below : gam 5 * gam 5 < 1 / 2 := by rw [gam_five]; grind` | 4/9 < ½. |
| `schottky_seven_above` | `TT/PeelTrees.lean:164` | `theorem schottky_seven_above : 1 / 2 < gam 7 * gam 7 := by rw [gam_seven]; grind` | ½ < 9/16. |
| `schottky_ratio` | `TT/PeelTrees.lean:166` | `theorem schottky_ratio : (5 - 3) * (5 - 3) < (8 : Int) ∧ (8 : Int) < (7 - 3) * (7 - 3) := by decide` | 4 < 8 < 16, the integer form of "5 is below and 7 above z = 3 + 2√2". The equivalence Γ² = ½ ⇔ z = 3 + 2√2 itself is not in these three; it is in `line_ratio`, `/home/claude/votkp-lean/research/2026-11-10/BallJoins.lean:59` (`(hs : r ^ 2 = 2) : gam (3 + 2 * r) ^ 2 = 1 / 2`), a research-folder file. |
| `caps_disjoint` | `TT/PingPong7.lean:97` | `theorem caps_disjoint (u w : Dir) (v : V4) (hu : X u v) (hw : X w v) : u = w` | Cap of u (`:64`): "future null with comp u v > 0 and t^2 < 2 (comp u v)^2". No ratio enters; the caps are fixed 45° caps. |
| `pingpong_step` | `TT/PingPong7.lean:179` | `theorem pingpong_step (u : Dir) (v : V4) (hv : Null v) (hout : ¬ X u.inv v) : X u (step u v)` | Ratio 7 only (the step is the integer matrix 7·B_u, `:46`). |
| `step_plane` | `TT/PingPong7.lean:87` | `theorem step_plane (u : Dir) (v : V4) : (step u v).t = 25 * v.t + 24 * comp u v ∧ comp u (step u v) = 24 * v.t + 25 * comp u v` | Ratio 7: cosh = 25/7, sinh = 24/7. |
| `step_lorentz` | `TT/PingPong7.lean:77` | `theorem step_lorentz (u : Dir) (v : V4) : qf (step u v) = 49 * qf v` | Ratio 7. |
| `snell_implies_squared_snell` | `/home/claude/gh/square-case-lean/OperatorFirst/HypersurfaceSquareLineage.lean:40` | `(h : n₁ * Real.sin θ₁ = n₂ * Real.sin θ₂) : n₁ ^ 2 * Real.sin θ₁ ^ 2 = n₂ ^ 2 * Real.sin θ₂ ^ 2` | Squaring ordinary Snell. Algebra only. |
| `three_body_refraction_is_squared_snell` | same file, `:155` | `(hSnell : Real.sqrt R₁ * Real.sin θ₁ = Real.sqrt R₂ * Real.sin θ₂) (hR1 : 0 ≤ R₁) (hR2 : 0 ≤ R₂) : R₁ * Real.sin θ₁ ^ 2 = R₂ * Real.sin θ₂ ^ 2` | Provenance note `:148-153`: "the `R₁ sin² θ₁ = R₂ sin² θ₂` form belongs to the earlier directional-transport/refraction line. This module proves its exact algebraic relation to positive-index Snell once the model coefficient is supplied; it does not re-derive the physical variational principle." File header `:12-15`: "`g = n^2` below is a declared model identification inside this projector/hypersurface construction. It is not an identification of the intrinsic projector metric with a spacetime metric." |
| `refraction_law` | `/home/claude/gh/upg-lean/UPGDiracRefraction.lean:120` | `(hpar : R₁ * v₁ * s₁ = R₂ * v₂ * s₂) (h₁ : E - V₁ = 1 / 2 * R₁ * v₁ ^ 2) (h₂ : E - V₂ = 1 / 2 * R₂ * v₂ ^ 2) : R₁ * (E - V₁) * s₁ ^ 2 = R₂ * (E - V₂) * s₂ ^ 2` | Conditional algebra from kept parallel momentum and energy. With V₁ = V₂ it is R₁ s₁² = R₂ s₂² (`refraction_equal_potentials`, `:128`). |
| `turning_barrier` | same file, `:137` | `(hR₂ : 0 < R₂) (h : R₁ * s₁ ^ 2 = R₂ * s₂ ^ 2) (hs₂ : s₂ ^ 2 ≤ 1) : R₁ * s₁ ^ 2 ≤ R₂` | Docstring: "beyond the critical angle the path returns to its own side." |
| `art792_radiation_pressure_components` | `/home/claude/gh/maxwell-lean/Maxwell/Treatise/RadiationPressure.lean:86` | `{E H n : Vec3} (hn : n ⬝ᵥ n = 1) (hEn : E ⬝ᵥ n = 0) (hHn : H ⬝ᵥ n = 0) : normalStress (stress645 E H H) n = -(electrostaticEnergy631 E ((1 / fourPi) • E) + electrokineticEnergy636 H H)` | Docstring `:82-85`: K = μ = 1, a transverse disturbance; "a pressure across the wave-front equal to `E²/8π + H²/8π`, the whole energy in unit of volume". `stress645` is at `Maxwell/Treatise/MagneticStress.lean:266`. It covers the untilted wave front. It contains no reflection coefficient, so P = 2R is not in it. |
| `hyperbolic_length` (used by the Flock clock) | `/home/claude/votkp-lean/VOTKP/Smith.lean:65` | `theorem hyperbolic_length (z : ℝ) (hz : 0 < z) : (1 + (z - 1) / (z + 1)) / (1 - (z - 1) / (z + 1)) = z` | Docstring `:61-64`: "so the hyperbolic distance `ln((1 + Γ)/(1 − Γ))` from the centre is `ln z`. This is also the radar reading: a mirror at speed `Γ` returns the frequency ratio `z`." Lean proves the identity only; `peel-atlas/CLAIMS.md:32` (V2): "Lean proves the identity `(1 + Γ)/(1 − Γ) = z`; the Poincaré metric itself is not formalized." |

All seventeen named theorems were found at the lines the plan cites. Not one is "not found".

Paper statements used with them (`/home/claude/votkp-lean/two-trees/paper/Two_Trees_in_One_Ball_v4.html`, text extracted): Theorem 4.7 "(half-angle). For two perpendicular steps of equal rapidity r … cos θ = 2γ/(1 + γ²), sin θ = (γ² − 1)/(γ² + 1), tan(θ/2) = Γ². The formula is recognised: for perpendicular boosts Rhodes and Semon give tan(θ/2) = tanh(r₁/2) tanh(r₂/2)". Theorem 5.3: "If the peel ratio satisfies z > 3 + 2√2, equivalently Γ² > 1/2, then the three boosts generate a Schottky group: free, discrete …". Theorem 5.4: at the norm-5 step the commutator "turns about it through an angle φ with cos φ = −527/625"; sharpness text: "tr[A, B] = 2 − 4 sinh⁴(r/2). That is a rotation exactly when sinh(r/2) < 1, i.e. z < 3 + 2√2; it is parabolic at z = 3 + 2√2 and a boost above". Text before Theorem 8.4: "cosh δ = sinh²(ℓ/2) = 9/7" at ln 7. BallJoins J4 and J7: `BallJoins.lean:74` `trace_reflect_transmit` (2 − 4 s⁴ = 2 − 4 (R/(1 − R))²) and `:121` `reverse_turn` (if AB = L·R then BA = (τR·L·R)·τR).

### 2.2 Atlas cards (statement and the card's own grade, from `ATLAS`; line = line of the `"id"` field)

| Card | Line | Title and claim, quoted | Card's own grade (`source_grade`) | Coverage note in the ledger |
|---|---|---|---|---|
| B30 | 842 | "Refraction is kinematics, not force." Claim: "R₁ sin²θ₁ = R₂ sin²θ₂ L = ½R(w)\|ẇ\|² · p∥ = Rẇ∥ and E = ½R\|ẇ\|² conserved · \|v⊥\| ∝ 1/√(2λ) the path turns because the admissible directions turn" | theorem | `external_kernel_mapped` to `upg-lean` `refraction_law`, `refraction_equal_potentials`, `turning_barrier`, `regularized_refraction`; scope "Conditional scalar refraction/turning algebra from conserved quantities; the Lagrangian origin is supplied separately." `full_card_certified: false`. |
| B39 | 1147 | "Past the critical angle nothing gets through." Claim: "θcrit = arcsin√(1/κ) · θ₂ = π/2 + i arccosh(√κ sin θ₁) κ = R₁/R₂ > 1 · transmission decays as e−\|p⊥\|w⊥ the wave is returned whole to the loaded side". Explanation holds the witness: "stiffness falling four to one, incidence forty-five degrees against a critical thirty". | theorem | `local_kernel_mapped` (`critical_angle`, `complex_angle_sin`, `complex_angle_cos`); scope "no derivation of a physical transmission model." |
| B59 | 1763 | "Two cones, deliberately not identified." Claim: "goal scope ≠ admissible continuation any relation arrives as a numbered crossing with hypotheses a word that happens to fit is not a bridge". Explanation ends: "Even two cones drawn from one interface are different sets." | reading | `not_mapped_in_audited_scope`. |
| B74 | 2210 | "A degenerate stratum repels." Claim: "g∥ sin²θ = C and sin²θ ≤ 1 ⇒ g∥ ≥ C Clairaut: the along-interface momentum is conserved · turning point where g∥ = C some walls cannot be reached at all" | theorem | `local_kernel_mapped` (`stratum_repels`, `refraction_turning_barrier`) and `upg-lean`. Audit note: "Clairaut reflection requires the appropriate tangential collapse and conserved momentum." |
| B100 | 2987 | "The echo crosses a circle, not a radius cutoff." Claim: "\|r\|² > \|a\|² ⇔ \|x − xc\| > \|xc\| r = (a + x)/(1 + ax) · xc = −C̄/A, A = 1 − \|a\|⁴, C = ā(1 − a²) the phase of the echo decides the side" | theorem | `external_kernel_mapped` (`echo_circle`, `circle_identity`, `circle_criterion`, `circle_through_origin`, `one_radius_cannot_decide`). |
| B101 | 3026 | "The thin end is a shunt with a reference plane." Claim: "y = −ikd(N² − n₀²) + O(d²) Y = ns + y · r = (n₀ − Y)/(n₀ + Y) first order in thickness, read at a declared plane" | theorem | `not_mapped_in_audited_scope` (the ledger maps no Lean to it; the plan cites `thin_end_top` separately). |
| B175 | 5297 | "A boundary that returns nothing is a matched load; the horizon is one." Claim: "I − Sb*Sb = 4(WVb)* Herm L (WVb) Zb = Lbb − LbiLii⁻¹Lib = W*LW · Sb = (Zb − I)(Zb + I)⁻¹ the power not returned is interior dissipation, pulled back". Closed when: "No reflection is not full absorption, and an impedance says nothing about causality; the horizon reading is structural." | theorem (the plan's chip "theorem for the identity; horizon reading structural" matches the card's own closing line) | `external_kernel_mapped` to `light-ledger-lean/LightBridges/Boundary.lean`; scope "no horizon or general-relativistic boundary realization." |
| B182 | 5482 | "Delay is not trapping: a slow return and no return differ only in the limit." Claim: "ẋ = 𝒫 − (κ + a)x + by, ẏ = ax − by mean residence (1 + a/b)/κ for b > 0 · at b = 0 a share a/(κ + a) stays the limits t → ∞ and b ↓ 0 do not commute". Closed when: "This is a conditional energy model, not a simulation of a star or a black hole." | theorem | `not_mapped_in_audited_scope`. |
| B189 | 5651 | "One scalar edge is one reflecting step." Claim: "E⁻/E⁺ = Γ², Γ = (di − dj)/(di + dj) = tanh(½ ln di/dj) E⁺ − E⁻ = 4didj · boost di ↦ eφdi, dj ↦ e−φdj: Γ ↦ (Γ + tanh φ)/(1 + Γ tanh φ) the ratio of the two books is the squared reflection coefficient" | theorem | `external_kernel_mapped` (`smith_identity`, `round_trip`); scope "book-energy identity and chain thermodynamic interpretation are not part of these declarations." |
| B203 | 6018 | "The book ratios fix the route; the signs fix the endpoint." Claim: "Lrec = 2Σ\|rj\| = 2Σ artanh √(E⁻j/E⁺j) · Dend = 2\|Σrj\| Lrec − Dend = 4 min(R₊, R₋) · rj = ½ ln(Ej+1/Ej) · equality ⇔ every step has one sign" | theorem | `not_mapped_in_audited_scope`. |

Every card carries `witness_status`: "Published card witness only; no fresh numerical replay is claimed by this ledger." Two places where the plan says more than the ledger file shows:
- **B30 path witness.** The plan writes "path witness in the card: conserved to 2e-11, 50° in R = 1 leaves at 22.5210° in R = 4". Those two numbers are **not found** in `coverage.json` or in `/home/claude/atlas_src/atlas_v7_cards_dump.txt` (the card HTML itself is not on disk). The angle follows from the law: arcsin(sin 50°/2) = 22.5210° (G10, run here). "Conserved to 2e-11" is untested here.
- **B59.** The card text in the ledger is about "goal scope ≠ admissible continuation". The plan's wording "transmission cone … and resolvability cone sin²θ ≥ ε are different sets" is **not found** as such in the ledger text; the card's last sentence ("Even two cones drawn from one interface are different sets") is the line it rests on. The use on the page (draw the transmission cone only, never call it the resolvability cone) is consistent with the card's rule.

---

## 3. The chain, link by link

Each link: statement → source → grade → rests on → where the Flock uses it → why it is there. Numbers quoted are from the runs in the table at the top.

### 3.1 The geometry the Flock inherits

**G-a. A ball one peel step out is a point on the hyperboloid at distance r = ln z; in the drawn ball it sits at radius Γ.**
- Source: `LH/lh_math_v1.js:28` (`boost(u, r)`), plan §0 ("the peel step `B(u, r)`, a boost of rapidity `r = ln z` along arm `u`, with Smith coordinate `Γ = (z − 1)/(z + 1) = tanh(r/2)`"); `hyperbolic_length` `Smith.lean:65`.
- Grade: LEAN · hyperbolic_length for the identity (1 + Γ)/(1 − Γ) = z. The Poincaré metric is not formalised (CLAIMS V2), so "distance" is elementary hyperbolic geometry, a reproduction, CHECKED here.
- Check and why it proves it: build B(u, ln z)·O as a 4×4 matrix product, read its distance from O by arccosh of the Minkowski product and its ball radius by |x|/(1 + t). If the three numbers r, Γ and (1 + Γ)/(1 − Γ) = z come out of the matrix itself, the statement is not circular. Result G1: largest residual 5.5e-16 for z = 1.5 … 13.
- Flock use: `FL/fl_math_v1.js:39` (`p:[Math.cosh(rr), Math.sinh(rr)*u[0], …]`).
- Why it is there: it fixes where every ball is, in one ruler that all three generations share.

**G-b. The face is the plane halfway: all points equally far from the centre and the ball; unit normal N = (sinh h, cosh h · u), h = r/2.**
- Source: plan §3.2 table ("Face planes | unit normal `N_w,u = g_w · (sinh h_u, cosh h_u · u)`, `h_u = r_u/2`"); `LH/lh_math_v1.js:35` (`facePlane`).
- Grade: DRAWING for the convention, CHECKED for the geometry (not in Lean).
- Check: the vector from O to the ball is exactly 2 sinh h · N, so the plane ⟨x, N⟩ = 0 is the equal-distance set; random points generated on the plane were tested for equal distance. G2: 7.1e-15.
- Flock use: `FL/fl_math_v1.js:35` (`crossAt`: "arc length along p->q where the geodesic crosses the plane of points equidistant from u and v"), `:47` (centre–arm face at `s:rr/2`), `:49`.
- Why: a face is where one ball's cell ends and the next begins; light meets it there.

**G-c. Two faces on perpendicular arms: g = ⟨N_a, N_b⟩ = sinh h_a · sinh h_b.**
- Source: plan K18 and the note at the end of §7 ("with signature (+, −, −, −), `<N_a, N_b> = + sinh h_a sinh h_b`"); `LH/lh_math_v1.js:170`.
- Grade: CHECKED · 1e-12 (LH self-test K18, re-run here from node: value 0, holds).
- Check G3: 0.0 on 400 random pairs.
- Flock use: `FL/fl_math_v1.js:49` (`g = Math.sinh(balls[a].r/2)*Math.sinh(balls[b].r/2)`), `:52`.
- Why: one number tells whether two neighbouring faces meet or stand apart.

**G-d. g < 1: the faces cross, and the centre cell's angle at that edge is arccos g.**
- Source: plan table H row 5 ("crossing circle and angle `α = arccos g` when `g < 1`"); `lh_math_v1.js:173`.
- Grade: CHECKED · 1e-10 (plan K18).
- Check and why: the angle was measured, not computed from g. A point q on the crossing line was solved for; at q the two directions lying in each face, perpendicular to the line, and pointing to the centre's side of the other face were built from null spaces; the angle between them is the cell's corner angle. G3: largest difference from arccos g on 254 crossing pairs 6.0e-14. Values: z = 3,5: g = 0.5164, α = 58.91°; z = 3,3: 70.53°; z = 5,5: 36.87°. The count 360°/α is 6.11, 5.10, 9.76: not whole numbers at these ratios.
- Flock use: when g ≤ 1 no gap mark is put on the link (`fl_math_v1.js:49-50`, `del = g > 1 ? Math.acosh(g) : 0`); the readout says "faces meet" (`fl_layer_v1.js:140`).
- Why: below the wall neighbouring cells overlap, so there is no gap to tunnel.

**G-e. g > 1: the faces stand apart by δ = arccosh g, the length of their common perpendicular.**
- Source: plan M3 ("the common perpendicular of length `δ = arccosh g`"), K18; Two Trees v4 text before Thm 8.4 ("cosh δ = sinh²(ℓ/2) = 9/7").
- Grade: CHECKED (LH ledger: first run killed by a too-small search window, re-run 4.2e-14; opposite arccosh g² killed). The ratio-7 constant is PROVED · Two Trees v4, Theorem 8.4.
- Check (b), and why it proves the claim: each plane was parametrised by two free coordinates about its foot point, and the Minkowski product of a point on one with a point on the other was minimised over all four coordinates (Nelder–Mead, 12 random starts). The formula for g never enters the search. If the minimum equals arccosh g the formula is the true least distance. G4:

  | z_a, z_b | g | least distance found | arccosh g | arccosh g² (the opposite) |
  |---|---|---|---|---|
  | 5, 7 | 1.014185 | 0.168236118 | 0.168236118 | 0.238480 |
  | 7, 7 | 1.285714 | 0.738997944 | 0.738997944 | 1.088342 |
  | 7, 9 | 1.511858 | 0.972955075 | 0.972955075 | 1.468121 |
  | 9, 13 | 2.218801 | 1.434959913 | 1.434959913 | 2.276603 |
  | 13, 13 | 2.769231 | 1.677395879 | 1.677395879 | 2.726008 |
  | 6, 6 | 1.041667 | 0.287682072 | 0.287682072 | 0.409609 |
  | 5.9, 5.9 | 1.017373 | 0.186133341 | 0.186133341 | 0.263988 |

  Largest difference 3.9e-13. At ratio 7, sinh²(ln 7 / 2) = 1.285714285714 = 9/7. The same four δ values appear in `fl_check_01.out` (K4: 0.1682, 0.9730, 1.4350) and `gap_clock_check_01.out` (C3).
- Flock use: `fl_math_v1.js:49-50` (`del`, the gap mark), `:52` (`links[…].delta`).
- Why: δ is the one length the "gap layer" hypothesis needs.

**G-f. The wall: Γ² = ½ ⇔ z = 3 + 2√2 ⇔ R = T; for equal steps it is g = 1.**
- Source: plan M6 line 126; Two Trees v4 Theorem 5.3; `schottky_five_below`, `schottky_seven_above`, `schottky_ratio`; `line_ratio` (BallJoins.lean:59).
- Grade: PROVED · Two Trees v4, Theorem 5.3; LEAN for the two sides (5 below, 7 above).
- Check G5 at z = 5.828427124746: Γ² − ½ = −1.1e-16; sinh²(r/2) − 1 = 0; (z − 3)² − 8 = −1.8e-15; R − T = −2.2e-16; SL(2) trace + 2 = 0; tanh r − 2√2/3 = −1.1e-16. z = 5: Γ² = 4/9; z = 7: Γ² = 9/16.
- Flock use: `fl_check_01.out` K4 last line (z = 5.828, 5.828: g = 1.0000, "faces meet", passed 0.2500000000 = T² = ¼); the gap mark is continuous through the wall because δ → 0 there.
- Why: it is the one ratio where a face returns exactly half, where the faces of equal steps first separate, and where the square stops turning.
- Note carried from the LH ledger (item 3) and the review (item 9): for unequal steps the pair's regime changes at g = 1, which is not either arm's Γ² = ½.

**G-g. The right triangle: cosh d = cosh r_I · cosh r_J.**
- Source: hyperbolic Pythagoras; `turn5`, `TT/PeelTrees.lean:258` (docstring `:257`: "Two orthogonal steps: cosh d = cosh^2 (ln 5) = 169/25 (hyperbolic Pythagoras)."), `theorem turn5 : pt (word B5 [.pi, .pj]) = [169, 156, 60, 0]`.
- Grade: LEAN · turn5 at ratio 5 (the triangle O, B_i O, B_i B_j O); the general formula is a textbook result, a reproduction, CHECKED here.
- Check G6: 500 random pairs, residual 0; z = 3,5 gives d = 2.1459; z = 5,5 gives cosh d = 6.76 = 169/25.
- Flock use: the arm–arm link length. `fl_math_v1.js:48` (`d = MMr.linkDistance(pa, pb)`); F2 shows `linkDistance` equals arccosh(cosh r_a cosh r_b) on all six test pairs; `fl_check_01.out` K4 link lengths 2.1459, 2.9187, 3.4815, 4.0869, 2.8873 agree.
- Why: it is the travel time of light between two arm balls (speed 1).

**G-h. The Thomas turn equals the area of that triangle: θ_T = 2 arctan(Γ_I Γ_J).**
- Source: plan M6 lines 122–123; `thomas5`, `thomas7`, `thomas_half_angle`, `thomas_general`; Two Trees v4 Theorem 4.7 (which itself calls the formula "recognised", citing Rhodes and Semon for the unequal case).
- Grade: equal steps LEAN (5, 7, and every integer z by `thomas_general`) and PROVED · Two Trees v4, Theorem 4.7. Unequal steps: CHECKED · 1e-9, not in Lean; a recognised textbook formula restated in the peel coordinate (reproduction). "Equals the triangle area" is the classical angle-defect statement; CHECKED here, not in his Lean.
- Check and why: the turn was read from the polar decomposition of the 4×4 product B_a B_b (remove the pure boost to its image point; the remainder is a rotation; read its angle from the trace). The area was computed separately as π minus the three angles of the triangle from the law of cosines. Three independent numbers. G7: polar angle against the formula 2.7e-13; area against the formula 3.7e-14 (500 random pairs). z = 5: cos, sin = 0.670103092784, 0.742268041237 = 65/97, 72/97; tan(θ/2) = 0.444444444444 = Γ²; θ = 47.925°. z = 7: 175/337, 288/337; tan(θ/2) = 0.5625; θ = 58.716°. Unequal: z = 3,5: 36.870°; 5,7: 53.130°; 3,7: 41.112°.
- Flock use: this is where the turn enters the Flock, though the Flock file does not name it. Every link carries a rotation `R = MMr.linkRotation(...)` and its spin form `U = MMr.su2(R)` (`fl_math_v1.js:41`), applied to the light at the ports and faces (`:79-82`). F4 (200 random pairs): the centre–arm rotations are the identity, the arm–arm rotation alone has angle 2 arctan(Γ_a Γ_b) (to 9.4e-8), and the product round centre → a → b → centre has that angle to 8.0e-14.
- Why: light carried round a triangle of balls comes back turned by the triangle's area; the arm–arm link is where that turn is booked.

### 3.2 Refraction (M2)

**R-a. a sin²θ is kept across a face.**
- Source: CARD · B30 (theorem). Lean algebra: `three_body_refraction_is_squared_snell`, `snell_implies_squared_snell`, `refraction_law`, `turning_barrier` (table 2.1). Clairaut bound: CARD · B74 (theorem).
- Grade: CARD · B30 (theorem) for the law; LEAN for the algebra only. The Lean file says in its own words that it "does not re-derive the physical variational principle". The identification a = n², a₁/a₂ = z² is READING (plan line 70).
- Rests on: kept energy and kept momentum along the face (the card's "Carry" and "Check").
- Code: `lh_math_v1.js:46-52` (`splitAtFace`, `sin2sq:Cc/a2`), `:41-44` (`refractDir`), audit `:205-206` (angles re-measured from the drawn tangents).
- Flock use: none. The Flock's links meet each face head-on in the model (one reflecting step, no angle). Oblique incidence is not in `fl_math_v1.js`.
- Why it is there (one ball): it says how a ray bends at a face using only what the face keeps.

**R-b. Incidence in the ball: sin θ = cosh h · sin ψ; the ray meets the face only if cos ψ ≥ tanh h = Γ.**
- Source: plan M2 line 68 ("new in this plan, elementary hyperbolic trigonometry"). Grade: CHECKED · 1e-10.
- Check G9: 2000 random rays, 1.95e-12; 0 cases against the meeting rule.
- Flock use: none directly. Its second half is the face shadow of M7 (cos ψ₀ = Γ), the same circle.
- Why: it turns "angle at the centre" into "angle at the face".

### 3.3 Total return and the gap (M3)

**T-a. Past θ_crit = arcsin √(1/κ) the whole ray returns; with κ = z², θ_crit = arcsin(1/z).**
- Source: CARD · B39 (theorem); `total_reflection` `Edition10.lean:86`, `turning_point` `:102` (both found). κ = z² is the M1/M2 READING.
- Check G10: κ = 4 gives 30.0000°; z = 3, 5, 7 give 19.47°, 11.54°, 8.21°. LH self-test K5 holds (re-run).
- Code: `lh_math_v1.js:50-53`. Flock use: none (no oblique rays).
- Why: beyond that angle a face is a perfect mirror with a phase.

**T-b. The gap as an evanescent film: r = r₀₁ ⊕ (r₁₂ e^{−2|k⊥| w}); |r|² + |t|² = 1.**
- Source: `film_is_oplus` `Film.lean:29` (`theorem film_is_oplus (g x : ℂ) : (g + x) / (1 + g * x) = oplus g x := rfl`); plan M3 line 84.
- Grade: LEAN · film_is_oplus for the composition (it is a definitional identity, `rfl`); CHECKED · 1e-12 for the flux; "exact for a plane-parallel gap of width w" (plan line 84) and "the faces here are parallel only along their common perpendicular" (plan §6 item 15). The decay rate is `PROVED · Event Horizon Ed. 10 §8.3 (model equation)` in the plan; not re-opened here.
- Code: `lh_math_v1.js:73-83` (`tunnelGap`).
- Check F3 and why: for a face whose return has unit size and phase φ, the film formula reduces in closed form to T = sin²φ / (sinh²(k w) + sin²φ). `LH.tunnelGap` was compared against that on 200 random cases: 5.6e-16. At κₑ = Y₁ (φ = π/2) it is sech²(k w): 6.7e-16.
- Flock use: `fl_math_v1.js:50` (`rho:Math.tanh(opts.kgap*del), kind:'gap'`), header `:8-9` ("the light between them only tunnels, amplitude sech(kappa_g delta) (lossless film with |t|^2 = sin^2 phi / (sinh^2 kd + sin^2 phi) at phi = pi/2). [HYPOTHESIS: gap layer]"); checked in `fl_check_01.out` K4.
- Why: it is the rule for how much light gets across a place where it cannot travel.

### 3.4 Pressure (M5)

**P-a. A wave front presses with its energy per unit volume.**
- Source: `art792_radiation_pressure_components` (table 2.1). Grade: LEAN, for the untilted front, K = μ = 1, transverse fields.
- Tilted plane, −u cos²θ: CHECKED · 1e-12, with the condition |E| = |H|, transverse (review must-fix 2, done in v2). LH self-test K13 re-run: 1.4e-17.

**P-b. P = 2R; K = 1/(T − R) = 1/(1 − P); sinh²(r/2) = R/T.**
- Grade (plan line 112): "`CHECKED · FEED-LOOP-03 P1–P3` then `READING · as physical pressure: untested`". The algebra was re-run here (G11, 2.1e-14). z = 3, 5, 7: P = 0.5, 0.8889, 1.125; P = 1 exactly at the wall, where K has its pole.
- Per-face push in a stack: the builder's repair `P_k = 2R_k(Y_k|a_k⁺|² − Y_{k+1}|a_{k+1}⁻|²)/Y_0` (LEDGER item 1, accepted in the review), `lh_math_v1.js:163`. READING.
- Flock use: none as a push. The Flock's "push" (`fl_math_v1.js:13-18`) is the face holding a ball's field toward rest, a MODEL CHOICE; it is not P = 2R. The kick record K_k(τ) is not in the Flock.
- Why (one ball): it is the reading of what returned light does to the face that returned it. It stays untested as a physical pressure.

### 3.5 The Thomas turn and the square (M6)

**S-a. Two perpendicular steps make a boost and a turn**: section 3.1 G-h.

**S-b. The square W = B_a B_b B_a⁻¹ B_b⁻¹: SL(2) trace 2 − 4g² (equal steps: 2 − 4 sinh⁴(r/2) = 2 − 4(R/T)²). g < 1: a turn with cos φ = 8g⁴ − 8g² + 1. g = 1: locks (trace −2, one Jordan block). g > 1: a run of length 4 arccosh g.**
- Source: `comm_trace` (general identity) with the sharpness text of Two Trees v4 after Theorem 5.4; `trace_reflect_transmit` (BallJoins.lean:74) for the R/T form; unequal steps CHECKED · 1e-10 (plan line 125).
- Grade: equal steps PROVED · Two Trees v4 (sharpness text) and LEAN for the general Riley identity; the g-form for unequal steps CHECKED only.
- Check G8: 500 random pairs, turn and run forms, 1.5e-13; the Riley form at v = 2 sinh² against 2 − 4 sinh⁴, 2.2e-14; z = 5 gives g = 0.8 and cos φ = −0.8432 = −527/625, the number of Theorem 5.4 (`comm5_cos`, `TT/PeelTrees3.lean:91`). LH self-test K8, K10 hold.
- W = L R L⁻¹ R (the square is two Thomas turns, one carried through the boost): "new in this plan", CHECKED · 1e-8; LH self-test K10 gives 6.9e-12. `reverse_turn` (BallJoins.lean:121) is the Lean statement of its key step (BA = (τR·L·R)·τR).
- Code: `lh_math_v1.js:98-105`, `:170-174`, `:212`.
- Flock use: not used as such. The Flock has no four-step loop. What it shares with the square is g: the same g that says turn or run says whether the arm–arm link has a gap mark. For N = 7 the Flock has triangles (centre, a, b), whose holonomy is the single turn θ_T (F4), not the square's φ.
- Why (one ball): it shows that going round a closed path of steps does not bring the frame back, and that the wall is where "comes back turned" changes to "does not come back".

### 3.6 The rim and the caps (M7)

**Rim-a. A step acts on a light direction by aberration, and that is ⊕: cos ψ′ = cos ψ ⊕ tanh r; frequency ratio t′/t = cosh r + sinh r cos ψ, equal to z on the axis.**
- Grade: CHECKED · 1e-12 (elementary Lorentz algebra; a reproduction). Integer form at ratio 7: LEAN · step_plane, step_lorentz.
- Check G12: 2000 random cases, 1.1e-13. LH self-test K11 holds.

**Rim-b. Radar reading: (1 + Γ)/(1 − Γ) = z.** LEAN · hyperbolic_length for the identity; the sentence "a mirror at speed Γ returns the frequency ratio z" is a READING (it is in the docstring, not in the statement).

**Rim-c. Six caps of 45°, pairwise disjoint; ping-pong.** LEAN · caps_disjoint (any null vector), LEAN · pingpong_step at ratio 7 only. For other ratios: CHECKED, "zero exceptions" above the wall. Re-run here independently (G12): exceptions in 1e5 directions × 6 steps: z = 5: 25,527; just above the wall: 0; z = 7: 0; z = 13: 0. The integer check at 7: step of (3, 1, 2, 2) is (99, 97, 14, 14), null, inside the +i cap.

**Rim-d. Face shadow: the face meets the rim in the circle cos ψ₀ = Γ; at the wall ψ₀ = 45°, the cap boundary.** "New in this plan", CHECKED · 1e-12 (K12 re-run 1.8e-15; G12). Two Trees v4 says the same of the Dirichlet half-spaces ("caps have angular radius α with cos α = Γ").

- Code: `lh_math_v1.js:107-115`, `:176-177`.
- Flock use: Rim-b only, as the clock ratio (section 5). The caps, the shadow and the aberration field are not in `fl_math_v1.js`; they are on the Mixer-v2 ball page that hosts the Flock.
- Why (one ball): the rim is where every light direction ends; the caps show that above the wall each step owns its own patch of the rim and no two patches overlap.

---

## 4. Where source and code do not match

1. **Flock: the sign of a face on the arm–arm links is opposite to its sign on the centre–arm links.** (`FL/fl_math_v1.js:47, 50-51, 81-82`.)
   - What the code does. In `step` (`:81-82`) light running forward on a link reflects with +ρ and light running backward with −ρ. On a centre–arm link (`:47`) forward is outward and ρ = +tanh(r/2): the centre side sees +Γ, the ball side sees −Γ. That agrees with `step_matching` (`Edition10.lean:47`, r = (Y1 − Y2)/(Y1 + Y2)) with Y falling outward, and with `reciprocity` (`:69`, "Sending the wave from the other side reverses the sign: Γ₂₁ = −Γ₁₂").
   - On an arm–arm link a → b (`:50-51`) forward at the first face is from ball a's side into the centre cell, and ρ = +tanh(r_a/2); at the second face forward is from the centre cell out to b, and ρ = −tanh(r_b/2). So ball a sees its own face as −Γ_a on the link to the centre and as +Γ_a on the link to b; the centre cell sees face b as +Γ_b on one link and −Γ_b on the other. It is the same plane in both cases (`crossAt(pa, pb, d, balls[0].p, pa)` is the centre–a bisector). The comment at `:51` ("the same face seen from inside the centre cell, Gamma_21 = -Gamma_12") gives the minus sign to the direction that the centre–arm links give the plus sign.
   - It is not only a convention. Run `l2_sign_01.js`: a scratch copy with the two signs swapped (first face −Γ_a, second face +Γ_b), original untouched. Books hold in both (≤ 3e-13). The light in the balls differs: N = 3, z = (3, 5, 7), kick A, t = 40: as written 0.1445 0.0135 0.0107; swapped 0.4314 0.1298 0.0515. Kick B, t = 2: ball B holds 0.1136 as written and 0.3250 swapped. First-pass fractions (K3, K4) are the same either way, since they are squares.
   - Smallest repair: in `:50` write `rho:-Math.tanh(balls[a].r/2)` and in `:51` `rho:Math.tanh(balls[b].r/2)`, correct the comment, and re-run `fl_check_01.js` and the exploration table (the shares and the order parameter r will change). If the present signs are intended (each ball taken as the centre of its own cell), that is a different model of the face and should be stated as a MODEL CHOICE; then the centre–arm link needs the same treatment for the ball end. The choice is Jeromie's.

2. **Flock: two different lengths are called the gap.** The light on an arm–arm link spends s₂ − s₁ inside the centre cell (travel time), and separately meets a tunnelling mark of strength set by δ, placed at the midpoint (s₁ + s₂)/2 (`:50`). These are not the same length. F2: z = 7,9: stretch 1.2846, δ = 0.9730; z = 5,7: stretch 0.9781, δ = 0.1682; at the wall, stretch 0.9624, δ = 0. On the whole grid with g > 1 the stretch exceeds δ by at least 0.1284. δ is the least distance between the two face planes, reached on their common perpendicular, which is not the a → b geodesic. The page text ("where two faces stand apart the light between them only tunnels") reads as if the whole in-cell stretch were forbidden; in the code the light travels that stretch freely and is also cut once by sech(κδ). This is inside the HYPOTHESIS; the wording on the page should say which length is which. REQUIREMENTS item 8 already lists "whether the length is the centre-to-centre step d, or only the gap δ" as not stated by him.

3. **Flock: the tunnelling amplitude sech(κδ) is the M3 film at one chosen incidence.** F3 shows sech²(k w) is `LH.tunnelGap` exactly when κₑ = Y₁ (return phase π/2), which is the largest the film can pass. At κₑ = Y₁/2 or 2Y₁ the same film passes 0.3323, against 0.4375 (z = 7,9, k = 1). The one-ball page uses a different setting for the same readout (LEDGER item 4: incidence of the tagged ray or θ_crit + 0.15 rad, admittance 1 in the centre cell and 1/z in the gap). So the two pages show different tunnelled fractions for the same δ. Both are graded hypothesis/plane-parallel; the Flock header states its choice (φ = π/2). κ (`kgap`, default 1) has no source: it is a free parameter.

4. **`comm_trace` is cited for the square's trace, but states the Riley-meridian identity.** The 2 − 4 sinh⁴(r/2) form is its case v = 2 sinh²(r/2), named in the `band_bound` docstring and in the paper's sharpness text, not as a theorem of its own. The plan's chip already splits this correctly (LEAN for `comm_trace`, PROVED for the sinh⁴ form). A film line should not say "Lean proves 2 − 4 sinh⁴".

5. **`thomas_half_angle` is arithmetic at ratios 5 and 7.** tan(θ/2) = Γ² for all equal steps rests on `thomas_general` (integer z) plus the one-line proof in Theorem 4.7. tan(θ/2) = Γ_a Γ_b for unequal steps is CHECKED only, and the paper calls it recognised (Rhodes and Semon). The Flock's arm–arm links use the unequal case (z = 3, 5, 7).

6. **B30 and B59 wording in the plan against the ledger file**: see the two notes under table 2.2 (witness numbers not found; B59 text is about goal scope against admissible continuation).

7. **`art792_radiation_pressure_components` and P = 2R.** The Lean theorem has no reflecting surface in it. The page (v2) now separates the chips; the film should keep "Maxwell: a wave front presses with its energy density" (LEAN) apart from "a face that returns R is pushed by 2R" (READING, untested).

8. **Minor, one-ball code.** `loopKind` (`lh_math_v1.js:105`) labels "wall" only within 1e-9 of g = 1, so the label cannot show in a moving drive (review suggestion 8, not changed in v2). The plan's K18 tolerance for the least distance is 1e-8; the independent run here gives 3.9e-13, so the line has room.

No mismatch was found in the geometry itself: positions, face normals, g, α, δ, the wall, the triangle, the turn, the square, the aberration law and the caps all agree between the plan, `lh_math_v1.js`, the Lean files where they exist, and the independent runs. `LH.selftest()` re-run from node: 24 of 24 lines hold.

---

## 5. Section H: what is theorem-backed and what stays hypothesis; how the Flock's two hypotheses sit on it

### 5.1 Table H, row by row

| Row (his statement) | Pieces that are proved or checked | Their grade | What stays HYPOTHESIS |
|---|---|---|---|
| Light is trapped between layers and kicks itself on the hypersurface | Echo series and Smith addition in a layer: `echo_series`, `film_is_oplus` (`Film.lean:42`, `:29`) | LEAN (one-dimensional, on the arm axis) | That the layer walls are electrons |
| Absorbed and re-emitted further down | Two-stock model ẋ = 𝒫 − (κ + a)x + by, ẏ = ax − by; mean residence (1 + a/b)/κ; at b = 0 a share a/(κ + a) stays | CARD · B182 (theorem; "a conditional energy model", not mapped to Lean); K15 CHECKED after re-run | Which face has which a, b; that this is what light does at a face |
| Some balls radiate, some absorb | Same card (b > 0 against b = 0) | CARD · B182 | The assignment of balls to classes |
| The electron sea is ground and follows light, leaving a record of each kick | Route 2Σ\|r_j\| against endpoint 2\|Σ r_j\|, defect 4 min(R₊, R₋) | CARD · B203 (theorem; not mapped to Lean); K16 CHECKED | That the sea is the rim and that it stores the record. The record K_k = ∫P_k dτ is itself a READING (P = 2R untested as a pressure) |
| Balls connect at levels but always keep a gap layer (crystal spacing) | g, α = arccos g, δ = arccosh g (CHECKED; G3, G4 here); wall and Schottky line (PROVED · Two Trees Thm 5.3, LEAN at 5 and 7); δ at ratio 7 (PROVED · Thm 8.4); non-discreteness below the wall (PROVED · Thm 5.4); BallJoins J4 `trace_reflect_transmit`, J7 `reverse_turn` (LEAN, research folder); `film_is_oplus` for a plane-parallel gap | as listed | **That a minimum gap is enforced.** Nothing proved says balls must keep δ > 0. Below the wall (z = 3, 5) the faces cross; the geometry allows no gap there |
| "My Snell's law at the hypersurface and Pauli exclusion principle" | 1 − 2/(eˣ + 1) = tanh(x/2): `fermion_smith` (`Edition10.lean:183`), `fermion_center` (`:194`), `particle_hole` (`:213`), all found; with x = ln z, C = 1/(z + 1), 1 − 2C = Γ, T = 4C(1 − C) (K17, CHECKED · 1e-14) | LEAN for the identity; CHECKED for the substitution | That x = ln z is the fermion variable; that exclusion sets the spacing. The a sin²θ law beside it is CARD · B30 (theorem) with Lean covering its algebra only |

In every row the mathematics drawn is exact, and the hypothesis is the identification of that mathematics with electrons, the sea, exclusion or an enforced spacing. None of the six "what stays hypothesis" entries is upgraded anywhere in the v2 build (review item 6: "No hypothesis item carries a law chip").

### 5.2 The Flock's "gap layer" hypothesis

- It is table H row 5, moved from one ball's face pairs to the links between balls. The proved pieces are the same: δ = arccosh g is the true least distance between the two faces (G4, independent), the faces first separate at g = 1, and a plane-parallel evanescent film passes sin²φ/(sinh²(kδ) + sin²φ) (`film_is_oplus` plus the M3 model equation; F3).
- What the Flock adds, all inside the hypothesis: (i) the tunnelling is applied to the light on the arm–arm link, at one mark in the middle of its in-cell stretch; (ii) the incidence is fixed at φ = π/2, giving sech²(κδ); (iii) κ = `kgap` = 1 is chosen, not derived.
- What it does not do: it does not enforce a minimum gap. For z = (3, 5, 7) the pairs (I, J) and (I, K) have g = 0.516 and 0.667 < 1, so no gap mark exists on those links; only (J, K) has one (g = 1.014, δ = 0.168). Row 5's hypothesis "always keep a gap layer" is therefore not what the Flock runs; the Flock runs "where the geometry gives a gap, light tunnels it". That distinction should be said in the breakdown.
- What the geometry check (a) settles for it: on every arm–arm link, for all 2,209 ratio pairs on a 0.25 grid from 1.5 to 13, the geodesic from ball a meets face a first, then face b, with 0 < s₁ < s₂ < d (0 violations); the bisection in `crossAt` agrees with a closed form (tanh s = A sinh d / (B + A cosh d), A = cosh r_a − 1, B = cosh d − cosh r_b) to 2.2e-15; each crossing is a single sign change (0 exceptions), so the bisection cannot land on a wrong root; every sample point between the crossings is nearer the centre than either arm ball (0 exceptions). The same order holds on all 12 perpendicular arm pairs at z = (3, 5, 7). The shortest in-cell stretch on the grid is 0.0226, at z = 1.5, 1.5. So the picture "face a, a stretch of the centre cell, face b" is correct over the whole range, including below the wall where the faces cross each other elsewhere.

### 5.3 The Flock's "clock ratio z" hypothesis

- The row it stands on is not in table H; it is M7's radar line: "`LEAN · hyperbolic_length` … for the identity `(1 + Γ)/(1 − Γ) = z`; the radar sentence is a `READING`." REQUIREMENTS S1 records the same grade in the chat: reading the step's z as a clock ratio "is a reading, not a theorem".
- Chain: (1) identity (1 + Γ)/(1 − Γ) = z: LEAN. (2) A mirror moving at speed Γ returns light with frequency ratio z: READING of (1) (two-way Doppler at rapidity r/2). (3) Equivalently, a step of rapidity r multiplies the frequency of light along the arm by z and of light against the arm by 1/z: CHECKED (M7 aberration, G12; F5: e^{−r} = (1 − Γ)/(1 + Γ) = `LH.doppler(−1, r)` to 3.8e-16). (4) A ball one step out runs its own two levels at ω/z (`fl_math_v1.js:10-11`, `:39` `rate: … Math.exp(-rr)`, `:85`): HYPOTHESIS. Step (4) is the new one: it turns a ratio of light frequencies between two frames into the rate of the far ball's own clock as counted in field time.
- What is checked about (4) is only that the code does it: `fl_check_01.out` K5, measured rates 2, 0.6667, 0.4, 0.2857 = ω/z, ratios 3, 5, 7.
- A fact the breakdown should carry, computed in G12: the time-dilation factor of a boost of rapidity r is cosh r (1.667, 2.6, 3.571 for z = 3, 5, 7), not z. The hypothesis picks the light-signal (Doppler/radar) ratio z, not the time-dilation ratio. Both are exact numbers of the same step; which one a ball's clock follows is the hypothesis. Between two arm balls the Flock's ratio is z_b/z_a (`fl_layer_v1.js:142`: "Across an arm–arm gap the ratio is the ratio of the two z"), which is not the radar ratio of the a–b link itself (that would be e^d with cosh d = cosh r_a cosh r_b); REQUIREMENTS item 7 lists this as not stated by him.
- The Flock keeps `clocks:'equal'` beside it for comparison, as his rule on forks asks.

---

## 6. Open, or not claimed

1. The sign of the faces on the arm–arm links (section 4, item 1) is open until he chooses. Every Flock exploration number that depends on phases (shares, sync measure r) depends on it; the kill lines K1–K7 do not.
2. A minimum gap is not enforced and not derived. Below the wall there is no gap at all between equal-step faces.
3. κ in sech(κδ) and the incidence φ = π/2 are free choices. The film is exact only for plane-parallel faces; these faces are parallel only along their common perpendicular (plan §6 item 15).
4. The clock ratio z is a reading made into a model. No source derives a ball's rate from its step. Which of z or cosh r, and what ratio holds between two arm balls, are open.
5. Unequal-step Thomas turn, the g-form of the square, W = L R L⁻¹ R, the face shadow, the incidence formula, and ping-pong for z other than 7 are numerical checks, not Lean. Equal-step Thomas is Lean for integer z.
6. "Turn = triangle area" is a classical statement checked here to 4e-14; it is not in his Lean files.
7. The Poincaré metric is not formalised in Lean (CLAIMS V2). All distances and geodesics in the ball are elementary geometry, checked numerically.
8. a = n², Y₁/Y₂ = z are READINGS (CLAIMS V4 is a Proposal, `peel-atlas/CLAIMS.md:34`). a sin²θ came from an earlier model; Lean covers its algebra, not the path integration; a sin²θ is not identified with the projector distance (card B4, line 138 of the ledger, grade "conjecture").
9. P = 2R as a physical pressure is untested. The Maxwell repo has no reflecting surface and no Poynting vector.
10. No law of motion for z(τ); no retardation and no Doppler from a moving face in the one-ball page. In the Flock the gap lengths are held at the mean steps (README: "gap lengths are held at the mean steps").
11. The Thomas turn is a turn of the frame; no claim about the polarisation of light (plan §6 item 12). In the Flock it acts on the two-component light amplitude through `U`; that use is part of the Flock's model, not a claim of the one-ball plan.
12. B30's "conserved to 2e-11" witness: not found on disk, untested here.
13. Lean was not compiled in this session.
14. From the LH ledger, still standing: K19 and the K20 frame-time line are killed for stated reasons; K14d was killed once and is unexplained.

---

## 7. Picture ideas for the film

1. **The halfway plane.** One ball slides out along an arm as z goes 1.5 → 13. The face follows at half the distance. Numbers shown: z, r = ln z, the ball's radius in the drawing Γ, the face's position r/2. A dotted pair of equal-length threads from any point of the face to the centre and to the ball shows why it is the halfway plane.
2. **Two faces meet, touch, part.** Two perpendicular arms with equal steps; z rises through 3 + 2√2. Below: the two faces cross along a line, the corner angle α = arccos g closes (70.5° at z = 3, 36.9° at z = 5). At z = 5.828: g = 1.0000, they touch at the rim, R = T = ½ appears on both faces at once. Above: a short bar, the common perpendicular, opens between them, labelled δ = arccosh g (0.739 at z = 7). One number, g, counts through 1.
3. **The triangle and its turn.** Centre, ball I, ball J. The link I–J is drawn as the true geodesic; its length d from cosh d = cosh r_I cosh r_J (2.1459 for z = 3, 5). A small three-arm frame is carried centre → I → J → centre and comes back turned. The shaded area of the triangle and the turn angle are the same number: 36.87° for z = 3, 5; 47.93° for z = 5, 5 (65/97, 72/97 on screen).
4. **Light on a link meets two faces.** A pulse leaves ball a toward ball b. Markers: s₁ (face a), the stretch inside the centre cell, s₂ (face b). At each face a share Γ² turns back. For z = 7, 9: d = 3.4815, faces at 1.0448 and 2.3294; beside the link, the bar δ = 0.9730 between the two face planes, drawn where it really is (on the common perpendicular, off the link), so the two lengths are seen to be different. Passed first time: 0.0689.
5. **The square: turns, locks, runs.** The gold four-step path at z = 5 (the centre goes round a ring, cos φ = −527/625), at the wall (it drifts to one rim point), at z = 7 (it runs out, 4 arccosh g per pass). The trace 2 − 4g² counts down through −2.
6. **The rim and the caps.** Six fixed 45° rings on the rim. Six face-shadow circles (cos ψ₀ = Γ) breathe with z and pass exactly through the rings at the wall. A cloud of light directions is swept toward an arm's rim point by one step, coloured by the frequency ratio, z on the axis and 1/z against it; under it the Flock's clock label: "hypothesis: a ball one step out ticks at 1/z" with the two candidate numbers side by side for z = 5: Doppler 5, time dilation 2.6.
