# L1 — The peel step, the face, Smith addition and layers

Lineage 1 of the breakdown of the Flock of Balls on the Field. Jeromie Beasley. Report written 16 Nov 2026. AI-assisted.

Scratch scripts and their outputs (all runs quoted below come from these):

- `/home/claude/balls/breakdown/scratch/L1/l1_gap_check_01.js` → `l1_gap_check_01.out` (`node l1_gap_check_01.js`)
- `/home/claude/balls/breakdown/scratch/L1/l1_sign_check_02.js` → `l1_sign_check_02.out` (`node l1_sign_check_02.js`)
- `/home/claude/balls/breakdown/scratch/L1/fl_check_01_rerun.out` (`node fl_check_01.js` run again from `/home/claude/balls/w/fl/`; `diff` against `fl_check_01.out` is empty: the stored check output reproduces line for line)

Lean status, stated once for the whole report. `grep -rn "sorry"` over `votkp-lean/VOTKP/*.lean`, `votkp-lean/two-trees/lean/*.lean` and `event-horizon-lean/EventHorizon/*.lean` finds the word only in header comments ("no sorry") and README badges; no proof uses it. No `axiom` or `native_decide` in the five files of this lineage. Imports: `Edition10.lean` imports Mathlib only (line 24); `Smith.lean` Mathlib only (line 21); `Film.lean` imports `VOTKP.Smith` (line 20); `Directed.lean` imports Mathlib and `VOTKP.Smith` (lines 21–22); `ThinFilm.lean` Mathlib only (line 16). So no theorem below has a `sorry` anywhere in its dependency inside these repositories. The repositories' READMEs state that every push is built against Lean v4.34.1 and Mathlib v4.34.1 with a kernel replay and an axiom audit (`votkp-lean/README.md:72–77`, `event-horizon-lean/README.md:56–58`). Lean is not installed on this machine, so the build was **not re-run here: untested locally**; what was done here is reading each statement and the grep.

---

## 1. Summary in plain words

One operator feeds everything: the peel step B(u, r), a boost of length r = ln z along an arm u. Its Smith coordinate is Γ = (z − 1)/(z + 1) = tanh(r/2). A face stands halfway along the step, at r/2. At a face, light splits: Γ² goes back, 1 − Γ² goes on, and seen from the other side the reflection has the opposite sign. Steps along one line add like velocities (Smith addition ⊕), which is the same statement as "a layer plus its echo is Γ ⊕ x". All of this is proved in Lean in his two repositories, with no `sorry`. The Flock uses exactly this at each face: a lossless two-way scatterer with ρ = Γ and τ = √(1 − Γ²), checked by K3 to 1e-12. Where two faces stand apart the Flock adds one more element, ρ = tanh(κδ). That element is the modulus of his film theorem (`film_is_oplus`) applied to a gap whose two walls each return everything (`total_reflection`), evaluated at one chosen wall phase φ = π/2. At that phase the gap is, in modulus, exactly one more peel step of length 2κδ, with ratio z_gap = e^{2κδ} (checked here to 1e-12). The theorem part is the film law and the wall being a perfect mirror; the choices are φ = π/2, κ = 1, no dependence on frequency, and the real signs given to the gap and to the faces on the arm–arm links. Those signs are not fixed by any source and they change the run (section 3).

---

## 2. The chain, link by link

Format of each link: plain statement → source and quote → grade → what it rests on → where the Flock uses it → why it is there.

Short names for files:

- **Ed10** = `/home/claude/gh/event-horizon-lean/EventHorizon/Edition10.lean`
- **Smith** = `/home/claude/votkp-lean/VOTKP/Smith.lean`
- **Film** = `/home/claude/votkp-lean/VOTKP/Film.lean`
- **Directed** = `/home/claude/votkp-lean/VOTKP/Directed.lean`
- **ThinFilm** = `/home/claude/votkp-lean/VOTKP/ThinFilm.lean`
- **FL** = `/home/claude/balls/w/fl/fl_math_v1.js`; **K** = `/home/claude/balls/w/fl/fl_check_01.js` and `.out`
- **PLAN** = `/home/claude/balls/in/367c3aed-Light_at_the_Hypersurface_Mixer_v2_Source/PLAN_light_at_the_hypersurface.md`

### 2.0 The peel step B(u, r) itself

- **Says.** A ball one step out sits at B(u, r)·O = (cosh r, sinh r · u) on the hyperboloid, r = ln z.
- **Source.** PLAN:17: "One feed operator: the peel step `B(u, r)`, a boost of rapidity `r = ln z` along arm `u`, with Smith coordinate `Γ = (z − 1)/(z + 1) = tanh(r/2)`." Integer form at z = 7: `step_lorentz`, `/home/claude/votkp-lean/two-trees/lean/PingPong7.lean:77`: `qf (step u v) = 49 * qf v`; `step_plane`, same file :87: `(step u v).t = 25 * v.t + 24 * comp u v ∧ comp u (step u v) = 24 * v.t + 25 * comp u v`.
- **Grade.** LEAN · step_lorentz, step_plane for z = 7 only (7·cosh ln 7 = 25, 7·sinh ln 7 = 24). The general boost is elementary Lorentz algebra (PLAN:136 grades the general rim action CHECKED · 1e-12).
- **Rests on.** Core Lean, no Mathlib (file header line 3: "no Mathlib, no sorry, no native_decide").
- **Flock.** FL:38–39: `r = opts.z.map(Math.log)` and each arm ball `p:[Math.cosh(rr), Math.sinh(rr)*u[0], Math.sinh(rr)*u[1], Math.sinh(rr)*u[2]]`. Default z = [3, 5, 7] (FL:37).
- **Why.** It places every ball; every later number (face position, Γ, link length, gap) is computed from these positions.

### 2.1 tanh_half_log — the Smith coordinate is a half-step tanh

- **Statement, Ed10:108.** `theorem tanh_half_log (q : ℝ) (hq : 0 < q) : Real.tanh (Real.log q / 2) = (q - 1) / (q + 1)`
- **Says.** For any positive ratio q, tanh(½ ln q) = (q − 1)/(q + 1).
- **Grade.** LEAN · tanh_half_log.
- **Rests on.** Mathlib's definitions of tanh, sinh, cosh, exp, log only. It is the first lemma of the "gap form" block; `normal_incidence` (:122), `gap_form` (:135) and `fermion_smith` (:183) call it.
- **Flock.** FL:47 `rho:Math.tanh(rr/2)` with rr = ln z. K3 (K:21) compares against `G = (3-1)/(3+1)`: the two forms of the same number.
- **Why.** It lets a ratio z be read as a length r = ln z, so reflections can be added as lengths.

### 2.2 smith_identity — the same identity in the VOTKP file

- **Statement, Smith:42.** `theorem smith_identity (z : ℝ) (hz : 0 < z) : (z - 1) / (z + 1) = tanh (log z / 2)`
- **Says.** VOTKP Theorem 8.1. Same content as 2.1, proved independently.
- **Grade.** LEAN · smith_identity.
- **Rests on.** `tanh_exp` (Smith:31), `tanh t = (exp (2 * t) - 1) / (exp (2 * t) + 1)`.
- **Flock.** As 2.1. Peel-atlas claim V1 (`/home/claude/votkp-lean/peel-atlas/CLAIMS.md:31`) records it: "at `z = 5`, `Γ = 2/3`".
- **Note.** This is the textbook Smith-chart / rapidity identity written in his coordinate; as a formula it is a reproduction. What is his is using the peel ratio z as the thing that is charted.

### 2.3 hyperbolic_length — the ratio is the length from the centre

- **Statement, Smith:65.** `theorem hyperbolic_length (z : ℝ) (hz : 0 < z) : (1 + (z - 1) / (z + 1)) / (1 - (z - 1) / (z + 1)) = z`
- **Says.** (1 + Γ)/(1 − Γ) = z, so ln((1 + Γ)/(1 − Γ)) = ln z = r.
- **Grade.** LEAN · hyperbolic_length for the identity. The words "hyperbolic distance" and "radar reading: a mirror at speed Γ returns the frequency ratio z" (docstring, Smith:62–64) are READING: `votkp-lean/LIMITATIONS.md:18` says "the Poincaré metric itself is not formalized".
- **Rests on.** Field algebra only.
- **Flock.** Link length d is the hyperboloid distance (FL:42 `MMr.linkDistance`); for a centre–arm link d = r, which K1 prints: "link length d = 1.0986" (= ln 3) and "1.6094" (= ln 5), `fl_check_01.out:1–2`. The clock rate 1/z (FL:39, `rate: Math.exp(-rr)`) uses the same z; that use is HYPOTHESIS (clock ratio z) and belongs to another lineage.
- **Why.** It is what allows "the link is a stretch of field of length r" and "the face is at r/2" to be the same r that gives Γ.

### 2.4 step_matching — what a sharp step does to a wave

- **Statement, Ed10:47.** `theorem step_matching (Y1 Y2 r t : ℂ) (hs : Y1 + Y2 ≠ 0) (hu : 1 + r = t) (hF : Y1 * (1 - r) = Y2 * t) : r = (Y1 - Y2) / (Y1 + Y2) ∧ t = 2 * Y1 / (Y1 + Y2)`
- **Says.** If the wave is continuous (1 + r = t) and the flux is continuous (Y₁(1 − r) = Y₂ t), then the reflected and passed amplitudes are fixed: r = (Y₁ − Y₂)/(Y₁ + Y₂), t = 2Y₁/(Y₁ + Y₂). The admittances are complex, so an evanescent far side is included (docstring :44–46).
- **Grade.** LEAN · step_matching.
- **Rests on.** Nothing earlier; two lines of linear algebra (`linear_combination`).
- **Flock.** FL:6 names it. FL:81–82 is the scatterer. Written for one face with forward stream f (from the left) and backward stream b (from the right):
  - f_out = τ f − ρ U b
  - b_out = ρ U† f + τ b, with τ = √(1 − ρ²)
  
  That is the matrix [[τ, −ρU], [ρU†, τ]]. U is the SU(2) frame turn of the link (FL:42); it is unitary and does not change any modulus.
- **Why.** The face is not given a made-up strength. Its two numbers come from requiring the wave and its flux to match across the step.
- **Match between the Lean amplitudes and the code amplitudes.** The Lean t = 2Y₁/(Y₁ + Y₂) is the field amplitude; the code τ is the flux amplitude, τ = √(Y₂/Y₁) · t. By `flux_balance` this is √(1 − Γ²), the same from both sides. Checked: T4 in `l1_gap_check_01.out`, 2000 random steps, worst error 5.0e-16.

### 2.5 flux_balance — nothing is lost at the face

- **Statement, Ed10:59.** `theorem flux_balance (Y1 Y2 : ℝ) (h1 : 0 < Y1) (h2 : 0 < Y2) : ((Y1 - Y2) / (Y1 + Y2)) ^ 2 + Y2 / Y1 * (2 * Y1 / (Y1 + Y2)) ^ 2 = 1`
- **Says.** Γ² + (Y₂/Y₁) t² = 1: returned plus passed flux is the whole.
- **Grade.** LEAN · flux_balance.
- **Rests on.** The formulas of `step_matching` (it restates them; it does not call the theorem).
- **Flock.** τ² + ρ² = 1 in FL:81, which makes each scatterer an exact rotation; that is why the books close. **K3** (`fl_check_01.out:5`): "returned 0.250000000000 (Gamma^2 = 0.250000000000), passed 0.750000000000 (1 - Gamma^2 = 0.750000000000)", kill line 1e-12. **K2**: "largest |balls + gaps - 1| to t = 200: 1.0e-12" (N = 3) and 8.3e-13 (N = 7).
- **Why.** It is the reason "light in the balls + light in the gaps = 1" can be exact.

### 2.6 reciprocity — the other side sees the opposite sign

- **Statement, Ed10:69.** `theorem reciprocity (Y1 Y2 : ℂ) : (Y2 - Y1) / (Y2 + Y1) = -((Y1 - Y2) / (Y1 + Y2))`
- **Says.** Γ₂₁ = −Γ₁₂.
- **Grade.** LEAN · reciprocity.
- **Rests on.** Ring algebra.
- **Flock.** Two places. (i) Inside every scatterer: light from the left returns with +ρ, light from the right with −ρ (FL:82). (ii) The second face of an arm–arm link is entered with ρ = −tanh(r_b/2), FL:51, with the comment "entering b's side: the same face seen from inside the centre cell, Gamma_21 = -Gamma_12".
- **Why.** A face is one object with two sides; without the sign flip the scatterer would not conserve light.
- **Open point.** Reciprocity fixes the sign of one side relative to the other. It does not say which side is "1". See section 3, item A.

### 2.7 matched_load and polar_mirror — the two ends of the scale

- **Statements.** Ed10:77 `theorem matched_load (Y : ℂ) : (Y - Y) / (Y + Y) = 0`. Ed10:81 `theorem polar_mirror (Y : ℂ) (h : Y ≠ 0) : (Y - 0) / (Y + 0) = 1`.
- **Says.** Equal admittances return nothing (Γ = 0, the centre of the disk). A far side of zero admittance returns everything (Γ = 1, the rim).
- **Grade.** LEAN · matched_load, LEAN · polar_mirror. The sentence "this is the class of the horizon" (docstring :75–76) is a reading; atlas card B175 carries it (grade: theorem for the identity, per PLAN:51).
- **Rests on.** `simp`.
- **Flock.** Limits of the same scatterer: z → 1 gives ρ = 0 (the face vanishes); z → ∞ gives ρ → 1. The gap element reaches the mirror limit as δ → ∞ (ρ = tanh κδ → 1). Not separately tested by a K line; K4's row at the wall ("z = 5.828,5.828 g = 1.0000, faces meet … passed first time 0.2500000000") is the δ = 0 end, where the gap element is absent.
- **Why.** They tell the viewer what the centre and the edge of the Smith disk mean.

### 2.8 total_reflection and turning_point — the wall of a gap is a perfect mirror

- **Statements.** Ed10:86 `theorem total_reflection (y κ : ℝ) (hy : 0 < y) : Complex.normSq (((y : ℂ) - κ * Complex.I) / ((y : ℂ) + κ * Complex.I)) = 1`. Ed10:102 `theorem turning_point (a1 a2 s : ℝ) (ha1 : 0 < a1) : a2 < a1 * s ↔ a2 / a1 < s`.
- **Says.** If the far side cannot carry the wave (its admittance is imaginary, Y₂ = iκ), then |Γ|² = 1 exactly: everything returns, with a phase. The far side stops carrying the wave exactly when sin²θ > a₂/a₁ (the critical angle).
- **Grade.** LEAN · total_reflection, LEAN · turning_point.
- **Rests on.** `total_reflection` is the `step_matching` formula with Y₂ = iκ; the proof is |y − iκ| = |y + iκ|. `turning_point` is one line of ordered-field algebra.
- **Flock.** This is the |r₀| = 1 that the gap formula needs (section 2.16). `turning_point` is not used in the Flock: the Flock has no angles, only light along the link. It is used in the one-ball page (PLAN:80).
- **Why.** It is what makes "the light between the faces only tunnels" a statement with a formula behind it: each wall alone returns all of it, and only the thinness of the gap lets some through.

### 2.9 admittance — the cross metric drops out

- **Statement, Ed10:35.** `theorem admittance (a b C ω : ℝ) (ha : 0 < a) (hb : 0 < b) (hC : C ≤ a) (hω : 0 ≤ ω) : √(a / b) * √(b * (ω ^ 2 * (a - C) / a)) = ω * √(a - C)`
- **Says.** With a = g∥, b = g⊥ and Clairaut constant C = a sin²θ, the admittance is Y = ω√(a − C); b cancels.
- **Grade.** LEAN · admittance for the identity. The model equation k² = bω²(a − C)/a is in the docstring (:32–34) and is graded in PLAN:83 as "PROVED · Event Horizon Ed. 10 §8.3 (model equation)".
- **Rests on.** `Real.sqrt_mul`, `Real.sqrt_sq`.
- **Flock.** Not used directly. Two things follow from it that bear on the Flock: at normal incidence (C = 0) Y = ω√a, so the ratio Y₁/Y₂ is free of ω — the face reflection does not depend on frequency. That agrees with the Flock's frequency-independent faces. In a region where C > a the same formula gives an imaginary Y with |Y| proportional to ω, and a decay rate |k⊥| = ω√(b(C − a₂)/a₂) (PLAN:83) that grows with ω. The Flock's gap uses a fixed κ = 1 instead. That is the model choice (section 2.16).
- **Why.** It says what number a face compares on its two sides.

### 2.10 fermion_smith — the same coordinate for an occupation

- **Statement, Ed10:183.** `theorem fermion_smith (x : ℝ) : 1 - 2 * (1 / (Real.exp x + 1)) = Real.tanh (x / 2)`
- **Says.** With Fermi–Dirac occupation C = 1/(eˣ + 1), 1 − 2C = tanh(x/2): the occupation's Smith coordinate, with z = eˣ (`fermion_impedance`, :174).
- **Grade.** LEAN · fermion_smith. (The identity 1 − 2f = tanh(x/2) is textbook; in his coordinate it is a reproduction. The reading of it as the fermion record's Smith coordinate is his, Ed. 10 Sec. 7.1.)
- **Rests on.** `tanh_half_log` (:184).
- **Flock.** Not used in `fl_math_v1.js`. It is used in the one-ball page (`lh_math_v1.js:247`, a selftest of `1 − 2C = Γ`). Not claimed for the Flock.
- **Why (for the film).** It shows the same tanh(½ ·) coordinate serving a second kind of ratio; it is background, not a working part of the Flock.

### 2.11 round_trip — what goes on, as a sech

- **Statement, Smith:134.** `theorem round_trip (t : ℝ) : 1 - tanh t ^ 2 = 1 / cosh t ^ 2`
- **Says.** T = 1 − Γ² = 1/cosh²(r/2).
- **Grade.** LEAN · round_trip (Corollary 15.3).
- **Rests on.** `cosh_sq_sub_sinh_sq`.
- **Flock.** τ = √(1 − ρ²) = sech(r/2) for a face (FL:81), and τ = sech(κδ) for the gap element — the "sech(κ_g δ)" of FL:9 and the "sech²" of K4 (K:27: "(1-Ga^2)(1-Gb^2) sech^2(k_g delta)"). Also FL:60, the reference link strength `l.c = 0.5*t` with t the product of the τ's.
- **Why.** It is the bridge between "ρ = tanh" in the code and "passes sech²" on the page.

### 2.12 tanh_add' and block_succ — steps add like velocities

- **Statements.** Smith:28 `noncomputable def oplus {K : Type*} [Field K] (u v : K) : K := (u + v) / (1 + u * v)`. Smith:72 `theorem tanh_add' (a b : ℝ) : tanh (a + b) = oplus (tanh a) (tanh b)`. Smith:89 `theorem block_succ (IE : ℕ → ℝ) (hpos : ∀ j, 0 < IE j) (k m : ℕ) : blockΓ IE k (m + 1) = oplus (blockΓ IE k m) (stepΓ IE (k + m))`, with `stepΓ IE k := tanh (log (IE (k + 1) / IE k) / 2)` (:82) and `blockΓ IE k m := tanh (log (IE (k + m) / IE k) / 2)` (:85).
- **Says.** tanh(a + b) = tanh a ⊕ tanh b, with u ⊕ v = (u + v)/(1 + uv). So the reflection of a block of peel steps is the ⊕-sum of the steps (VOTKP Theorem 15.1).
- **Grade.** LEAN · tanh_add', LEAN · block_succ.
- **Rests on.** `tanh_add'`: Mathlib `sinh_add`, `cosh_add`. `block_succ`: `tanh_add'` plus `log_div`.
- **Limit of the statement.** One axis only. CLAIMS V3 (`peel-atlas/CLAIMS.md:33`): "This is a one-dimensional statement. Boosts along **one** axis compose this way; boosts along different axes compose to a boost plus a rotation".
- **Flock.** Each link is one line, so the one-axis law applies on it. The code never calls ⊕; it runs the scatterers in time and the echoes do the adding. Checked here (T5 in `l1_gap_check_01.out`, a separate time-domain cascade of the same real scatterers, z_a = 7, z_b = 9, with the gap): first-pass amplitude 0.2625000000 = τ_a τ_g τ_b (squared 0.0689062500, the K4 number); the sum of all echoes back is 0.6896551724 = tanh(r_a/2 + δ − r_b/2); the sum of all echoes on is 0.7241379310 = sech(r_a/2 + δ − r_b/2); errors ≤ 2.7e-15. So what K4 measures is the first arrival; what ⊕ gives is the total after every echo, at zero phase.
- **Why.** It is why a stack of faces can be thought of as one longer step: lengths add, reflections ⊕-add.

### 2.13 film_is_oplus, echo_series, echo_resum — a layer plus its echo

- **Statements.** Film:29 `theorem film_is_oplus (g x : ℂ) : (g + x) / (1 + g * x) = oplus g x := rfl`. Film:42 `theorem echo_series (g x : ℂ) (h : ‖g * x‖ < 1) : HasSum (fun m : ℕ => (-g) ^ m * x ^ (m + 1)) (x / (1 + g * x))`. Film:53 `theorem echo_resum (g x : ℂ) (h : 1 + g * x ≠ 0) : g + (1 - g * g) * (x / (1 + g * x)) = (g + x) / (1 + g * x)`.
- **Says.** A film with front reflection Γ and echo x (the back reflection times the round-trip factor) reflects r = (Γ + x)/(1 + Γx) = Γ ⊕ x. The bounce-by-bounce sum Σ (−Γ)^m x^(m+1) converges to x/(1 + Γx) when |Γx| < 1, and Γ + (1 − Γ²)·(that sum) is the same r. All over the complex numbers.
- **Grade.** LEAN · film_is_oplus, echo_series, echo_resum. `film_is_oplus` is true by definition (`rfl`): it names the film formula as ⊕. The content is in `echo_series` + `echo_resum`: the bounces really sum to it. (The film formula is the textbook Airy formula; identifying it with ⊕, the same law as the peel record, is VOTKP Corollary 15.3 / card B98.)
- **Rests on.** `oplus` (Smith:28); Mathlib's geometric series `hasSum_geometric_of_norm_lt_one`.
- **Flock.** Between two marks of a link the light bounces exactly this way: each pass through FL:81–82 produces the next term. And it is the law from which the gap element is derived (2.16).
- **Limit.** PLAN:310: "With a phase, the film map `Γ ⊕ x` is not a disk isometry (card B98: a conjugate is needed in the denominator). Do not call the phased stack 'velocity addition'."
- **Why.** It is the whole of "light trapped between layers": not a new rule, the same addition with the echo as the second term.

### 2.14 echo_circle and circle_criterion — when a film returns more than its bulk

- **Statements.** Film:61 `theorem echo_circle (a x : ℂ) (h : 1 + a * x ≠ 0) : normSq ((a + x) / (1 + a * x)) - normSq a = ((1 - normSq a ^ 2) * normSq x + 2 * ((starRingEnd ℂ) a * (1 - a * a) * x).re) / normSq (1 + a * x)`. Film:90 `theorem circle_criterion (A : ℝ) (hA : 0 < A) (C x : ℂ) : 0 < A * normSq x + 2 * (C * x).re ↔ normSq (centre A C) < normSq (x - centre A C)`.
- **Says.** |r|² − |a|² has the sign of (1 − |a|⁴)|x|² + 2 Re[ā(1 − a²)x], and that is positive exactly outside one circle through the origin, centre x_c = −C̄/A.
- **Grade.** LEAN · echo_circle, LEAN · circle_criterion; card B100 (theorem). The docstring is exact about what is not joined: "that combined statement is not proved here" (Film:88–89) — the two theorems are proved separately, the one-line combination is not a Lean theorem.
- **Rests on.** `circle_criterion` rests on `circle_identity` (Film:80) and `centre` (:73).
- **Flock.** Not used. The Flock has no phase per unit length in a link (light there is a pure delay), so the echo x is real and the circle question does not arise. Used on the one-ball page (PLAN:97, K6 there).
- **Why (for the film).** It belongs to the one-ball generation; in the Flock breakdown it should be shown as "where the layers came from", not as a working part.

### 2.15 interface_smith, stack_telescopes, directed_composite — the middle drops out

- **Statements.** Film:116 `theorem interface_smith (Ni Nj : ℝ) (hi : 0 < Ni) (hj : 0 < Nj) : (Ni - Nj) / (Ni + Nj) = Real.tanh (Real.log (Ni / Nj) / 2)`. Film:124 `theorem stack_telescopes (N0 N1 N2 : ℝ) (h0 : 0 < N0) (h1 : 0 < N1) (h2 : 0 < N2) : oplus ((N0 - N1) / (N0 + N1)) ((N1 - N2) / (N1 + N2)) = (N0 - N2) / (N0 + N2)`. Directed:77 `theorem directed_composite (E : ℕ → ℝ) (hpos : ∀ j, 0 < E j) (m : ℕ) : blockΓ E 0 m = (E m - E 0) / (E m + E 0)`.
- **Says.** An interface reflection is the Smith coordinate of the index ratio. At zero phase, r₀₁ ⊕ r₁₂ = r₀₂: the inner layer drops out. For a whole record of positive values in any order, the ⊕-sum of all steps is (E_m − E_0)/(E_m + E_0): only the ends remain.
- **Grade.** LEAN · interface_smith, stack_telescopes, directed_composite.
- **Rests on.** `interface_smith` ← `smith_identity`. `stack_telescopes` ← `oplus` and field algebra. `directed_composite` ← `block_smith` (Smith:101) ← `smith_identity`; its docstring says the sum is "built step by step by `Smith.block_succ`".
- **Flock.** An arm–arm link with the faces touching (g ≤ 1) is a two-step stack: +tanh(r_a/2) then −tanh(r_b/2) (FL:50–51). Checked here (T5d): the sum of all echoes back is −0.1250000000 = (z_a − z_b)/(z_a + z_b) for z = 7, 9, error 1.9e-16. The centre cell has dropped out, as `stack_telescopes` says. K4's first row is the first-pass side of the same link: "z = 3.000,5.000 … faces meet … passed first time 0.4166666667 (formula 0.4166666667)" = (1 − ¼)(1 − 4⁄9).
- **Why.** It tells the viewer the difference between what arrives first (the product of what each face passes) and what the link is as a whole (one step between the two outer balls).

### 2.16 The gap element — derivation from film_is_oplus with |r₀| = 1

**What the code does.** FL:49–50: g = sinh(r_a/2)·sinh(r_b/2); if g > 1, δ = arccosh g, and a mark `rho:Math.tanh(opts.kgap*del), kind:'gap'` is placed midway between the two face crossings. Header FL:8–9: "the light between them only tunnels, amplitude sech(kappa_g delta) (lossless film with |t|^2 = sin^2 phi / (sinh^2 kd + sin^2 phi) at phi = pi/2). [HYPOTHESIS: gap layer]". Default κ_g = 1 (FL:37 `kgap:1.0`).

**Why the derivation proves the formula.** The film law is an identity in complex numbers (2.13). If the two inputs — the wall reflection and the round-trip factor — are put in for a gap that cannot carry the wave, the modulus of the output is forced. Nothing else is assumed. The numerical check then compares the formula with a second route that does not use ⊕ at all (matching the wave and its flux in the three regions directly).

**Derivation, step by step.**

1. Set-up: medium of admittance Y₁ (real) | gap of width δ in which the wave cannot run | the same medium Y₁. In the gap the admittance is imaginary, Y_g = iκₑ, and the wave decays as e^(−κx).
2. Front wall, from `step_matching` with Y₂ = iκₑ: r₀ = (Y₁ − iκₑ)/(Y₁ + iκₑ). By `total_reflection`, |r₀| = 1. Write r₀ = e^(iφ); then φ = −2·arctan(κₑ/Y₁). (PLAN:82 gives the same phase: "arg Γ = −2 arctan(κₑ/y)".)
3. Back wall, seen from inside the gap, by `reciprocity`: r₁₂ = −r₀.
4. Round trip in the gap: the usual phase factor e^(2ikδ) with k = iκ becomes the real number q = e^(−2κδ).
5. Echo: x = r₁₂·q = −r₀ q.
6. Film law, `film_is_oplus`: r = r₀ ⊕ x = (r₀ − r₀ q)/(1 − r₀² q) = r₀ (1 − q)/(1 − q e^(2iφ)).
7. Modulus of the denominator: |1 − q e^(2iφ)|² = 1 − 2q cos 2φ + q² = (1 − q)² + 2q(1 − cos 2φ) = (1 − q)² + 4q sin²φ.
8. So |r|² = (1 − q)² / ((1 − q)² + 4q sin²φ). Divide top and bottom by 4q and use (1 − q)²/(4q) = ((e^(κδ) − e^(−κδ))/2)² = sinh²κδ:
   - |r|² = sinh²κδ / (sinh²κδ + sin²φ)
9. Lossless, equal media on both sides, so |t|² = 1 − |r|²:
   - |t|² = sin²φ / (sinh²κδ + sin²φ)
   
   This is the formula quoted in FL:9.
10. Choose φ = π/2 (that is r₀ = −i, which by step 2 means κₑ = Y₁). Then sin²φ = 1, and 1 + sinh² = cosh²:
    - |t| = sech κδ, |r| = tanh κδ.
    - In full, from step 6 with r₀² = −1: r = r₀ (1 − q)/(1 + q) = r₀ · tanh κδ.

**Numerical check** (`l1_gap_check_01.out`; 2000 random cases each; the comparison route is direct three-region wave matching, function `filmByMatching`, which never calls ⊕):

- T1a |r₀| = 1: worst 4.4e-16.
- T1b r₀ ⊕ (−r₀ e^(−2κδ)) equals r from direct matching: worst 1.3e-15.
- T1c |t|² = sin²φ/(sinh²κδ + sin²φ): worst 1.2e-15. T1d the |r|² form: worst 1.1e-15.
- T2a at φ = π/2, r = r₀ tanh κδ: worst 2.2e-16. T2b |t| = sech κδ: worst 3.3e-16.
- Sample κδ = 0.7: film r = (0, −0.604368), t = (0.796705, 0); tanh 0.7 = 0.604368, sech 0.7 = 0.796705.
- T3 the Flock's own marks, read out of `makeWorld`: gap ρ = tanh(δ) to 1.1e-16; for z = 5,7: δ = 0.1682, ρ = 0.166667; z = 7,9: δ = 0.9730, ρ = 0.750000; z = 9,13: δ = 1.4350, ρ = 0.892679.

**Which K-check confirms it in the Flock.** K4 (`fl_check_01.out:6–10`), kill line 1e-12 on the first-pass fraction (1 − Γ_a²)(1 − Γ_b²)·sech²(κ_g δ): 0.2363040123 (z = 5, 7), 0.0689062500 (7, 9), 0.0194005102 (9, 13), and at the wall g = 1 (z = 3 + 2√2 both) 0.2500000000 with no gap element. K4 confirms that the code applies sech²(κδ) and that it joins on continuously at g = 1. K4 does not confirm that sech²(κδ) is the right law for the gap; that is the hypothesis.

**What is theorem and what is choice.**

| Part | Status |
|---|---|
| Film law r = r₀ ⊕ x, and that the bounces sum to it | LEAN · film_is_oplus, echo_series, echo_resum |
| Each wall of a non-carrying gap returns everything, \|r₀\| = 1 | LEAN · total_reflection |
| Back wall has the opposite sign | LEAN · reciprocity |
| \|t\|² = sin²φ/(sinh²κδ + sin²φ) | Follows from the three above by the algebra of steps 6–9. CHECKED · 1e-11 here (T1). Not itself a named Lean theorem. PLAN:84 grades the same film `CHECKED · 1e-12` and adds "This is exact for a plane-parallel gap of width `w`." As a formula it is the textbook result for tunnelling through a barrier (frustrated total reflection), reproduced in his coordinate. |
| φ = π/2 (κₑ = Y₁: the gap's admittance has the same size as the medium's) | MODEL CHOICE. No source fixes it. It is the phase at which the most gets through. |
| κ_g = 1 (decay per unit of hyperbolic length) | MODEL CHOICE. |
| No dependence on frequency | MODEL CHOICE. Ed. 10's own model equation gives a decay rate proportional to ω (PLAN:83). |
| The gap element entered as a real scatterer [[τ, −ρ],[ρ, τ]] with ρ = +tanh κδ | MODEL CHOICE; see section 3, item B. |
| The gap width is δ = arccosh g, the common perpendicular of the two faces, while the link runs along the geodesic between the two balls | MODEL CHOICE. PLAN:323: "The tunnelled fraction is exact for a plane-parallel gap; the faces here are parallel only along their common perpendicular." |
| That the region between two faces standing apart cannot carry the light at all | HYPOTHESIS: gap layer (FL:9; README). |

### 2.17 The nice fact: the gap is one more peel step of length 2κδ — true in modulus

- **Check, on paper.** A peel step of length r has Γ = tanh(r/2) (2.1). The gap element has ρ = tanh(κδ) = tanh((2κδ)/2). So it is the Smith coordinate of a step of length r_gap = 2κδ, ratio z_gap = e^(2κδ) = 1/q, where q is the round-trip decay of step 4. Directly from step 10: r = r₀ (1 − q)/(1 + q) = r₀ (z_gap − 1)/(z_gap + 1).
- **Check, numerically.** T2c: tanh κδ = (z_gap − 1)/(z_gap + 1), z_gap = e^(2κδ), worst 2.2e-16. T2d: ln((1 + ρ)/(1 − ρ)) = 2κδ (`hyperbolic_length` read backwards), relative error ≤ 8.3e-15 for κδ up to 4.
- **So.** At φ = π/2 the gap is, in modulus, exactly one more peel step, of length equal to the round trip across the gap in units of 1/κ. Its ratio z_gap is the factor by which one round trip in the gap weakens the light, turned upside down. Grade: CHECKED · 1e-12 for the identity; the reading "the gap is a peel step" is a READING on top of the MODEL CHOICE φ = π/2. Away from φ = π/2 it is not a peel step of that length: |r| = sinh κδ / √(sinh²κδ + sin²φ), which is larger than tanh κδ.
- **What "in modulus" leaves out.** The true film has r = r₀ tanh κδ with r₀ = −i, and the same r from both sides (a film between equal media is symmetric). A peel step has a real Γ with opposite signs from the two sides. The two agree after a fixed phase of +45° is put on one port and −45° on the other (algebra: e^(iπ/2)·(−i) = 1, e^(−iπ/2)·(−i) = −1, product of the two port phases = 1 so t stays real). The Flock uses the real, peel-step form. See section 3, item B.
- **Second nice fact, at κ = 1.** sech(arccosh g) = 1/g. So the gap passes the amplitude 1/g exactly, with g = sinh(r_a/2)·sinh(r_b/2), and ρ_gap = √(1 − 1/g²). Since sinh²(r/2) = R/T for a face (PLAN:58: "`sinh²(r/2) = R/T`"), the gap passes the fraction 1/g² = (T_a/R_a)(T_b/R_b), and the first-pass fraction of the whole link is (T_a T_b)²/(R_a R_b). Run (`l1_sign_check_02.out`): z = 7, 9: g² = 2.2857142857 = (R_a/T_a)(R_b/T_b), gap passes 0.4375000000, first pass 0.0689062500; z = 5, 7: 0.9722222222 and 0.2363040123; z = 9, 13: 0.2031250000 and 0.0194005102 — the K4 numbers, from the two faces' R and T alone. At κ = 1 the gap is therefore not a new number: it is fixed by the two faces. (For z = 7, 9 this is why ρ_gap comes out as exactly 0.75.) Grade: CHECKED · 1e-10 (printed digits), under MODEL CHOICE κ = 1.

### 2.18 thin_end_top — the thin end of a film

- **Statement, ThinFilm:105.** `theorem thin_end_top (n0 nb N k : ℂ) (hN : N ≠ 0) (hsum : n0 + nb ≠ 0) : rTop n0 nb N k 0 = rShuntTop n0 nb N k 0 ∧ HasDerivAt (fun d : ℝ => rTop n0 nb N k d) (2 * I * k * n0 * (N ^ 2 - nb ^ 2) / (n0 + nb) ^ 2) 0 ∧ HasDerivAt (fun d : ℝ => rShuntTop n0 nb N k d) (2 * I * k * n0 * (N ^ 2 - nb ^ 2) / (n0 + nb) ^ 2) 0`
- **Says.** VOTKP Theorem 6.3. For a very thin film the exact reflection and the "shunt" law Y = n_b − ikd(N² − n_b²) agree at thickness 0 and have the same first derivative in the thickness. `thin_end_top_remainder` (:216) adds that the difference is O(d²).
- **Grade.** LEAN · thin_end_top; card B101 (theorem).
- **Rests on.** `rTop_zero` (:43), `hasDerivAt_rTop` (:46), `hasDerivAt_rShuntTop` (:69). The film outputs B, C (:23, :26) are taken from Born & Wolf (header :5).
- **Flock.** Not used. PLAN:98 already marks it "Readout only" for the one-ball page. For the Flock it bears on one thing: the thin end of the gap. As δ → 0 the gap element goes to ρ = tanh κδ ≈ κδ, first order in δ, and vanishes at the wall g = 1, which K4's last row shows (0.2500000000 with and without). No claim is made that the Flock's thin gap equals the shunt of Theorem 6.3; that comparison is **untested**.
- **Why (for the film).** Background only.

### 2.19 negative_ratio_leaves_disk and the vacuum disk paper, Proposition 1 — the rim and outside it

- **Statement, Smith:208.** `theorem negative_ratio_leaves_disk (z : ℝ) (hz : z < 0) (h1 : z + 1 ≠ 0) : 1 < |(z - 1) / (z + 1)|`
- **Says.** A negative ratio gives |Γ| > 1: it lands outside the disk (VOTKP Section 15.4).
- **Grade.** LEAN · negative_ratio_leaves_disk. Rests on `abs_div`, `sq_lt_sq`, `nlinarith`.
- **Proposition 1.** `/home/claude/votkp-lean/paper/votkp_vacuum_disk_v1/votkp_vacuum_disk_v1.md:47–55` (heading at :47, parts (a)–(d) at :49–55), for G(z) = (z − w)/(z − w̄), w = e^(iπ/3) (defined :45): "(a) $G(w)=0$: the regular tetrahedron is the vacuum point. (b) Real $z$ (a flat tetrahedron, $D=0$) gives $|G|=1$: flat pieces lie on the rim. (c) The mirror shape $\bar z$ gives $|G(\bar z)| = 1/|G(z)|$: mirrors lie outside the disk. (d) The axis switch $T(z) = 1/(1-z)$ … acts on $G$ as an exact rotation, $G(T z) = e^{2\pi i/3}\,G(z)$, while $D(Tz)=D(z)$." Proof at :57–65. The paper's own status line (:67): "(a)–(c) are elementary; (d) is a new reading of a classical symmetry; the racket interpretation is ours."
- **Grade.** PROVED · VOTKP vacuum disk v1, Proposition 1 (a paper proof; it is not in Lean — no file under `votkp-lean/VOTKP/` states it; searched by name, not found).
- **What it shares with the peel coordinate.** The same picture with a different map: centre = matched / vacuum, rim = everything returns, outside the rim = the mirror image. For the peel coordinate the matching facts are Γ(1) = 0, |Γ| → 1 as z → 0 or ∞, and Γ(1/z) = −Γ(z) (`directed_reverse`, Directed:48). PLAN:52 also writes "Γ(−z) = 1/Γ(z)": that is one line of algebra ((−z − 1)/(−z + 1) = (z + 1)/(z − 1)); it is not a named Lean theorem — `negative_ratio_leaves_disk` proves only the weaker |Γ| > 1.
- **Flock.** Not used in `fl_math_v1.js`. Every ρ in the Flock is inside the disk (all z > 1, and tanh κδ < 1). Its place in the breakdown is the meaning of the disk: centre, rim, outside.
- **Why.** It is where the words "vacuum at the centre, mirror at the rim" come from.

---

## 3. What does not match between source and code

**A. The sign of the faces on the arm–arm links is the reverse of the centre–arm links.** (Smallest repair given below.)

- Centre–arm link, FL:47: `mk(0, k, [{ s:rr/2, rho:Math.tanh(rr/2), kind:'face' }])`. Ball i is the centre. By FL:82, light from the left (leaving the centre cell) returns with +Γ; light entering the centre cell returns with −Γ.
- Arm–arm link, FL:50–51: first mark `rho:Math.tanh(balls[a].r/2)`: ball i is the outer ball a, so light **entering** the centre cell returns with +Γ_a. Last mark `rho:-Math.tanh(balls[b].r/2)`: light **leaving** the centre cell toward b returns with −Γ_b.
- So the same kind of face is given +Γ for leaving the centre on one kind of link and −Γ for leaving the centre on the other. The comment at FL:51 calls the second face "the same face seen from inside the centre cell, Gamma_21 = -Gamma_12"; on the centre–arm link "from inside the centre cell" is the + side.
- Within each link the code is consistent with `reciprocity` (the two faces of the arm–arm link have opposite signs, and the stack telescopes, T5d). What differs is which side is called side 1. The source for that is the declared identification in PLAN:54 ("the admittance ratio across a face equals the step ratio, `Y₁/Y₂ = z`"), graded READING there, from CLAIMS V4 (a Proposal). Under that reading the centre–arm sign (+Γ leaving the centre) is the one that follows, and the arm–arm link should be (−Γ_a, gap, +Γ_b).
- **Why a check decides whether this matters.** K3 and K4 measure squared first-pass fractions, which cannot see a sign. If the light in the balls changes when only the signs change, the sign is physical. Run (`l1_sign_check_02.out`, kick B, z = 7, 9, 11, light in B at t = 3, with `torque:0` so the run is linear): as built 0.03254; faces negated 0.42116. At t = 20, light in A, B, C: as built 0.02818, 0.15717, 0.12524; faces negated 0.01925, 0.10479, 0.01143. Books stay 1.000000000000 in every variant. So the sign changes the run strongly, and no K line constrains it. (Reason: the sign sets whether the echo from the near face comes back to the ball in step or out of step with the light still in the ball.)
- **Smallest repair.** In FL:50–51 use `rho:-Math.tanh(balls[a].r/2)` for the first face and `rho:+Math.tanh(balls[b].r/2)` for the last, so that "leaving the centre cell" is + on every link; correct the comment; add one kill line that compares the signed echo returned by a face on an arm–arm link with the one on a centre–arm link. Or keep the present signs and state the convention as a MODEL CHOICE. Either way the exploration table in `fl_check_01.out` (order parameter, shares) was produced with the present signs. This is a call for the owner; it is reported, not changed.

**B. The gap element's sign and phase are a choice, and they also change the run.** The film theorem gives r = r₀ tanh κδ with r₀ = −i, the same from both sides (2.17). The code uses a real ρ = +tanh κδ from the a side and −tanh κδ from the b side. Moduli agree (K4, T2). The difference is a fixed ±45° at the two ports of the gap; with echoes between the gap and the faces this is not removable. Run (same file): "gap negated" gives light in B at t = 10 of 0.37572 against 0.02311 as built. Also the present form treats a and b differently (which side gets +) although a gap between two faces has no preferred side. Smallest repair: none needed for K4; for the model, either state the real form as MODEL CHOICE in the header next to φ = π/2, or carry the film's own symmetric element (r = −i tanh κδ both sides, t = sech κδ), which the complex amplitudes already in the code can hold.

**C. Header wording.** FL:6 writes "t = sqrt(1 - Gamma^2) (LEAN step_matching, flux_balance, …)". The Lean t is 2Y₁/(Y₁ + Y₂); √(1 − Γ²) is that t times √(Y₂/Y₁) (T4, 5.0e-16). Nothing is wrong in the code; the smallest repair is the word "flux amplitude" in the comment.

**D. Travel time through a gap.** The gap mark is a point scatterer at the midpoint (FL:50, `s:(s1+s2)/2`); the light crosses the stretch between the faces at speed 1 like the rest of the link and is weakened once. The film derivation has no travel inside the gap (the decay is the whole of it). Not a contradiction with any source — `REQUIREMENTS_v1.md:76` already lists "whether the length is the centre-to-centre step d, or only the gap δ between faces, is not stated" — but it should be shown as a choice.

**E. `Gam:Math.tanh(d/2)` on every link (FL:46)** is stored but not used by the stepper; for a centre–arm link it equals the face Γ, for an arm–arm link it is not any face's reflection. Harmless; noted so no one reads it as the link's reflection.

Nothing else was found that disagrees: face position r/2 (FL:47), ρ = Γ, τ² + ρ² = 1, opposite sign from the far side, and the first-pass products all match the Lean statements and K3/K4 to the stated tolerances.

---

## 4. Open or not claimed

1. The Lean build was not re-run here (no Lean on this machine). Statements were read and grepped; **compile untested locally**.
2. |t|² = sin²φ/(sinh²κδ + sin²φ) is derived and checked numerically; it is not a named Lean theorem. A one-line Lean corollary of `film_is_oplus` + `total_reflection` would close that; not written.
3. φ = π/2, κ = 1 and frequency independence are choices; no test here compares other φ or κ in the Flock. **Untested.**
4. The gap layer itself (that light between faces standing apart only tunnels) is HYPOTHESIS, as the code and README say. Not upgraded.
5. Signs on the arm–arm links (3A, 3B): open, and they change the run.
6. ⊕ is a one-line law (CLAIMS V3). The Flock respects this — each link is one line — but a path through two links (B to A to C) is not a ⊕-sum, and nothing here claims it is.
7. With a phase the film map is not "velocity addition" (PLAN:310, card B98). The gap derivation uses ⊕ with complex r₀; it is the film law, not a boost.
8. `echo_circle`, `circle_criterion`, `thin_end_top`, `fermion_smith`, `turning_point`, `admittance` and Proposition 1 are not used by `fl_math_v1.js`. They belong to the one-ball generation or to the meaning of the disk. The combined echo-circle statement is not proved in Lean (Film:88–89).
9. The Poincaré metric is not formalised (LIMITATIONS.md:18); "length r = ln z" rests in Lean only on (1 + Γ)/(1 − Γ) = z.
10. The identities 2.1, 2.2, 2.11, 2.12 and the barrier formula are textbook results in his coordinate: reproductions. What is his in this lineage: the peel ratio as the charted quantity, the face at half the step, one addition law shared by the peel record and the film (Theorem 15.1 with Corollary 15.3), the echo-circle criterion, and the use of one operator to feed all of it.

For the main session: nothing in this report came from memory; every statement is from the files cited or from the runs listed at the top.

---

## 5. Picture ideas for the film

1. **One step, three readings.** A point slides out from the centre of a disk along one arm. Three numbers move together: z (1 → 7), r = ln z (0 → 1.946), Γ = (z − 1)/(z + 1) (0 → 0.75). At z = 3 freeze: Γ = 0.5, "a quarter returns, three quarters go on" (K3: 0.250000000000 and 0.750000000000). The face is drawn as a plate standing at half the step.
2. **The face has two sides.** A pulse meets the plate from the left: +Γ returns. The same pulse from the right: −Γ returns (the returned pulse is drawn flipped). Bars underneath show returned + passed = 1 each time.
3. **Echoes add up to one step.** Two plates on one line. A pulse enters; the bounces appear one by one, each smaller; a running total climbs to Γ₁ ⊕ Γ₂. Then the two plates slide together and become one plate for the combined step: "lengths add, reflections ⊕-add". Numbers: steps 1/3 and 1/2 give 5/7 (ladders 1, 2, 6 and 1, 3, 6, `ladders_same_composite`, Smith:127).
4. **First arrival against the whole.** The arm–arm link for z = 7, 9: the first pulse through carries 0.0689 of the light (K4). Then the echoes keep arriving; the total amplitude on settles at 0.7241 and back at 0.6897 (T5). Two counters side by side.
5. **The gap as one more step.** Two plates move apart. While they overlap (g < 1) nothing new appears. At g = 1 they just touch (z = 5.828, K4 row five). Past it a faint third plate grows between them, with its own ratio z_gap = e^(2κδ) and its own Γ = tanh κδ; label it HYPOTHESIS. Show 1/g as the amplitude that gets through: at z = 7, 9, g² = 16/7 and the gap passes 7/16 = 0.4375.
6. **The disk's three places.** Centre: matched, nothing returns (`matched_load`). Rim: everything returns (`polar_mirror`, `total_reflection`). Outside the rim: the mirror image (`negative_ratio_leaves_disk`; Proposition 1(c)). One point is carried from the centre to the rim as δ grows, to show the gap element approaching a perfect mirror.
