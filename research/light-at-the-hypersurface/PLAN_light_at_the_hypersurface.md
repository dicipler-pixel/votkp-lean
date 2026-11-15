# PLAN: Light at the Hypersurface (Mixer v1)

For: Jeromie Beasley. Plan date: 15 Nov 2026. Planner and reviewer: lead designer instance. Builder: main session.

Working title of the page: **Light at the Hypersurface, Mixer v1**. Byline in the page: `JEROMIE BEASLEY · MIXER v1 · 15 NOV 2026 · AI-ASSISTED`.

Paths used below:
- `GH` = `/tmp/claude-0/-home-claude/f86429e3-e32f-50e6-b1fd-fcadab5264af/scratchpad/gh`
- `ATT` = `/mnt/user-data/attachments/f86429e3-e32f-50e6-b1fd-fcadab5264af`
- `WORK` = `/tmp/claude-0/-home-claude/f86429e3-e32f-50e6-b1fd-fcadab5264af/scratchpad/lh_build` (new; all build files go here)
- Exploratory sanity pass already run for this plan: `/tmp/claude-0/-home-claude/f86429e3-e32f-50e6-b1fd-fcadab5264af/scratchpad/plan_sanity/plan_sanity_01.py` (not the final check; see section 7).

---

## 0. The design in one paragraph

One Poincaré ball in the peel coordinate. One feed operator: the peel step `B(u, r)`, a boost of rapidity `r = ln z` along arm `u`, with Smith coordinate `Γ = (z − 1)/(z + 1) = tanh(r/2)`. Everything on the page is computed from that one operator at one clock value `τ`: where the balls sit (`B·O`), where the faces are (the plane halfway, at `h = r/2`), what a face does to light (`R = Γ²`, `T = 1 − Γ²`), how a ray bends at it (`a sin²θ` conserved), when it returns whole (critical angle), how layers stack (`⊕`), what the light pushes with (`P = 2R`), what two steps do to a frame (Thomas turn `2 arctan(Γ_a Γ_b)`), what the four-step square does (turn, lock or run), and what a step does to a light direction on the rim (aberration, which is `⊕` again). One clock drives all of it at once. A ledger recomputes every balance law on every frame.

Two things the builder must hold to throughout:
1. **One object.** There is one shared scene group (`WORLD`) that holds the balls, faces, layers, rays, loop, frames and rim caps. It is added to the stage once and never removed. An "eye" is a camera position, an emphasis (opacity weights) and a readout on that same moving object. No eye builds a separate scene. No side panels with second spheres. No comparison panels. No notes page.
2. **Law and hypothesis are visibly different.** Law items carry a solid grade chip. Hypothesis items carry an amber outlined chip reading `HYPOTHESIS` and are drawn with dashed lines or hollow markers. A hypothesis never appears in a readout row without the word.

---

## 1. Grade vocabulary (use exactly these chips)

| Chip | Meaning |
|---|---|
| `LEAN · <theorem name>` | Lean theorem in his repo. Lean was not re-run in this session; the chip text adds "repo CI" in the tooltip. |
| `PROVED · <paper, theorem>` | Proved in his paper text, no Lean name. |
| `CHECKED · <tol>` | Numerically checked by the final check script to the stated tolerance. |
| `CARD · Bnn (theorem / reading / conjecture)` | The atlas card's own grade, quoted. |
| `READING` | A physical reading of a proved identity. |
| `DRIVE` | A declared schedule for a parameter in time. Not a law. |
| `DRAWING` | A picture convention. |
| `HYPOTHESIS` | His picture, shown as his hypothesis. |

---

## 2. The chosen models (seven laws, one hypothesis layer)

### M1. One face is one reflecting step (R, T, flux balance; matched load and mirror)

Equations and sources:
- Step amplitudes from continuity `1 + r = t` and flux continuity `Y₁(1 − r) = Y₂ t`: `r = (Y₁ − Y₂)/(Y₁ + Y₂)`, `t = 2Y₁/(Y₁ + Y₂)`. `LEAN · step_matching`, `GH/event-horizon-lean/EventHorizon/Edition10.lean:47`.
- Flux balance `r² + (Y₂/Y₁) t² = 1`. `LEAN · flux_balance`, `Edition10.lean:59`.
- Smith form `(Nᵢ − Nⱼ)/(Nᵢ + Nⱼ) = tanh(½ ln(Nᵢ/Nⱼ))`. `LEAN · interface_smith`, `GH/votkp-lean/VOTKP/Film.lean:116`; also `tanh_half_log` `Edition10.lean:108`, `smith_identity` `GH/votkp-lean/VOTKP/Smith.lean:42`.
- Round trip `1 − tanh² t = 1/cosh² t`. `LEAN · round_trip`, `Smith.lean:134`.
- Two books of one edge: `E⁻/E⁺ = Γ²`, `E⁺ − E⁻ = 4 dᵢ dⱼ`. `CARD · B189 (theorem)`.
- Reciprocity `Γ₂₁ = −Γ₁₂`. `LEAN · reciprocity`, `Edition10.lean:69`.
- Extremes: matched load `Γ = 0` (`LEAN · matched_load`, `:77`); mirror `Γ = 1` when the far admittance is zero (`LEAN · polar_mirror`, `:81`). Horizon as matched load: `CARD · B175 (theorem for the identity; horizon reading structural)`.
- Rim and mirror: `Γ(−z) = 1/Γ(z)`; `|G(z̄)| = 1/|G(z)|` for `G(z) = (z − w)/(z − w̄)`. `PROVED · VOTKP vacuum disk v1, Proposition 1` (`GH/votkp-lean/paper/votkp_vacuum_disk_v1/votkp_vacuum_disk_v1.md:47-60`); `LEAN · negative_ratio_leaves_disk` (`Smith.lean:208`).

Declared identification (chip `READING`, source CLAIMS V4, Tree Ball Light v2): the admittance ratio across a face equals the step ratio, `Y₁/Y₂ = z`, so `Γ_face = tanh(r/2)`, `R = Γ²`, `T = 1 − Γ² = 1/cosh²(r/2)`.

Drawn: each face cap (existing `faceGeom`) with opacity tied to `R`. An on-axis beam along each arm. At the face the stream of markers splits: a fraction `R` returns, a fraction `T` goes on. Marker brightness is the flux fraction.
Moves: markers along the arm; the face slides as `h(τ) = r(τ)/2`; `R`, `T` update each frame.
Couples: `R` feeds M4 (each layer boundary), M5 (`P = 2R`), M6 (`sinh²(r/2) = R/T`, loop trace `2 − 4(R/T)²`).

### M2. Refraction at the face (the conserved `a sin²θ`)

Equations and sources:
- `R₁ sin²θ₁ = R₂ sin²θ₂`, from `L = ½R(w)|ẇ|²` with `p∥ = R ẇ∥` and `E = ½R|ẇ|²` conserved. `CARD · B30 (theorem)`; path witness in the card: conserved to 2e-11, 50° in `R = 1` leaves at 22.5210° in `R = 4`.
- Lean algebra of the squared law: `LEAN · three_body_refraction_is_squared_snell` (`GH/square-case-lean/OperatorFirst/HypersurfaceSquareLineage.lean:155`), `snell_implies_squared_snell` (`:40`); with energy and momentum hypotheses `LEAN · refraction_law` (`GH/upg-lean/UPGDiracRefraction.lean:120`, reduces to the card's form when `V₁ = V₂`); barrier `LEAN · turning_barrier` (`:137`).
- Oblique admittance `Y = ω √(a − C)` with `a = g∥` and `C = a₁ sin²θ₁`; the transverse metric drops out. `LEAN · admittance`, `Edition10.lean:35`.
- Clairaut bound `g∥ sin²θ = C`, so `g∥ ≥ C`. `CARD · B74 (theorem)`.
- Speed in a layer from B30's own Lagrangian: `|ẇ| = √(2E/R)`. `PROVED` as a one-line consequence of the card's `E = ½R|ẇ|²`.
- Incidence geometry in the ball (new in this plan, elementary hyperbolic trigonometry): a geodesic from the centre at angle `ψ` to the arm meets the face at distance `h` with `sin θ = cosh h · sin ψ`; it meets the face at all only if `cos ψ ≥ tanh h`. `CHECKED · 1e-10` (sanity pass gave 3e-13). With `h = r/2` this is `sin²ψ = T · sin²θ`.

Declared identification (`READING`): `a = R = n²` with `n` proportional to `Y`, so `a₁/a₂ = z²`. This matches `HypersurfaceSquareLineage.lean`'s own header (`g = n²` is a declared model identification, not an identification with a spacetime metric).

Drawn: a fan of rays from the source, each a true geodesic in the ball. At a face each ray splits into a reflected geodesic and a refracted geodesic. The refracted direction is built from `sin²θ₂ = (a₁/a₂) sin²θ₁` in the plane of incidence. The flux carried by each child is `R(θ)` and `T(θ)` from the oblique admittances.
Moves: the fan turns in azimuth `χ(τ)`; markers run along every segment at the layer speed; faces move, so every hit point and angle is recomputed each frame.
Couples: `C` feeds M3 (critical angle) and the oblique `R(θ)` feeds M5 (`P = 2R cos²θ`).

### M3. Total return past the critical angle, and the gap

Equations and sources:
- `θ_crit = arcsin √(1/κ)`, `κ = R₁/R₂ > 1`; `θ₂ = π/2 + i arccosh(√κ sin θ₁)`; transmission decays as `e^{−|p⊥| w⊥}`. `CARD · B39 (theorem)`; witness `R = 4 → 1` at 45° against critical 30°.
- `|Γ|² = 1` when `Y₂ = iκₑ`. `LEAN · total_reflection`, `Edition10.lean:86`. Turning point `a₂ < a₁ s ⇔ a₂/a₁ < s`. `LEAN · turning_point`, `:102`.
- With the M1 identification `κ = z²`, so `θ_crit = arcsin(1/z)`.
- Phase on return, read off the Lean expression: `arg Γ = −2 arctan(κₑ/y)`, `y = √(a₁ − C)`, `κₑ = √(C − a₂)`. `CHECKED · 1e-12`.
- Decay rate from the model equation `k² = b ω² (a − C)/a` (docstring of `admittance`): `|k⊥| = ω √(b (C − a₂)/a₂)`, penetration depth `ℓ = 1/|k⊥|`. Chip: `PROVED · Event Horizon Ed. 10 §8.3 (model equation)`.
- The gap as an evanescent film: `r = r₀₁ ⊕ (r₁₂ e^{−2|k⊥| w})` with complex steps. `LEAN · film_is_oplus` (`Film.lean:29`, stated over ℂ). `|r|² + |t|² = 1` for equal outer media. `CHECKED · 1e-12`. This is exact for a plane-parallel gap of width `w`.
- Transmission cone `|θ| < arcsin √(1/κ)` and resolvability cone `sin²θ ≥ ε` are different sets. `CARD · B59 (reading)`. Draw the transmission cone only; never label it as the resolvability cone.

Drawn: on each face, the transmission window (a disc about the arm axis) and the total-return annulus outside it, as two tints of the same cap. Rays past the critical angle return whole; a short fading tail of markers past the face shows the penetration depth `ℓ`. Where two faces stand apart (`g > 1`), the common perpendicular of length `δ = arccosh g` is drawn, with the tunnelled fraction along it.
Moves: the window radius changes with `z(τ)`; the tail length changes with `θ` and `ω`.
Couples: uses `C` from M2; the gap film is M4's `⊕` with an imaginary phase; the gap width is the face-pair `δ` of the Balls mixer.

### M4. Layers: echoes and Smith addition (on the arm axis)

Equations and sources:
- `r = (Γ + x)/(1 + Γx) = Γ ⊕ x`, `x = r₁₂ e^{2iφ}`. `LEAN · film_is_oplus`, `Film.lean:29`.
- Echo series `Σ_{m≥0} (−Γ)^m x^{m+1} = x/(1 + Γx)` for `|Γx| < 1`, and `Γ + (1 − Γ²) x/(1 + Γx) = Γ ⊕ x`. `LEAN · echo_series` (`:42`), `echo_resum` (`:53`), `echo_derivative` (`:33`).
- Zero phase: `r₀₁ ⊕ r₁₂ = r₀₂`. `LEAN · stack_telescopes`, `Film.lean:124`. Whole record: `LEAN · directed_composite` (`GH/votkp-lean/VOTKP/Directed.lean:77`), `block_succ` (`Smith.lean:89`), `tanh_add'` (`Smith.lean:72`).
- The echo circle: `|r|² > |a|² ⇔ |x − x_c| > |x_c|`, `x_c = −C̄/A`, `A = 1 − |a|⁴`, `C = ā(1 − a²)`. `LEAN · echo_circle` (`Film.lean:61`), `circle_criterion` (`:90`); witness `one_radius_cannot_decide` (`:108`): `a = ½`, `x = ±⅕` gives `49/121` and `1/9`. `CARD · B100 (theorem)`.
- Thin end as a shunt: `CARD · B101 (theorem)`; `LEAN · thin_end_top` (`GH/votkp-lean/VOTKP/ThinFilm.lean:105`). Readout only.
- Route against endpoint along a chain: `L_rec − D_end = 4 min(R₊, R₋)`. `CARD · B203 (theorem)`.

Scope: this model is exact in one dimension, so it is applied on each arm's axis, where the faces at `(k + ½) r` are all perpendicular to the same geodesic. Layer `k` has hyperbolic thickness `r` and phase `φ_k = ω n_k r`, `n_k = Y_k/Y_0` (`READING` for the phase assignment).

Drawn: along each arm, the faces to tree depth `D` and, between them, two counter-running marker streams with the exact forward and backward amplitudes `|a_k⁺|²`, `|a_k⁻|²` from the stack. A small Smith disc is not drawn separately; instead the composed `r` is shown as a point inside the cap of the first face, using the cap itself as the Smith disk (centre = matched, edge = mirror), with the echo circle drawn on that cap.
Moves: phases advance with `ω` and `r(τ)`; the composed point moves on the cap; streams brighten and dim as layers go in and out of resonance.
Couples: each boundary is an M1 step; the net flux `Y_k(|a_k⁺|² − |a_k⁻|²)` is the same in every layer and equals `T_total`; the per-face push in M5 uses these amplitudes.

### M5. Light pressure and the kick record

Equations and sources:
- A wave front presses with its energy per unit volume: normal stress `= −(E²/8π + H²/8π)`. `LEAN · art792_radiation_pressure_components`, `GH/maxwell-lean/Maxwell/Treatise/RadiationPressure.lean:86`; stress `stress645`, `MagneticStress.lean:266`.
- On a plane tilted by `θ` from the wave front, with `|E| = |H|` and both transverse: normal stress `= −u cos²θ`. Computed from the same stress tensor `σ = (EEᵀ + HHᵀ)/4π − I (E² + H²)/8π`. `CHECKED · 1e-12`.
- Push on a layer in units of the full-absorption push: `P = 2R`; `K = 1/(T − R) = 1/(1 − P)`; `sinh²(r/2) = R/T`. Chip: `CHECKED · FEED-LOOP-03 P1–P3` then `READING · as physical pressure: untested` (the wording already on Tree Ball Light v2).
- Oblique: `P(θ) = 2 R(θ) cos²θ` (`READING`, built from the two lines above).

Drawn: at each face, short normal arrows made of markers whose length is `P_k`. Behind each face a slowly filling ring of markers on the rim (the ground) holds the running record `K_k(τ) = ∫ P_k dτ`.
Moves: arrows follow `R(τ)` and the circulating flux in the layers; the record grows.
Couples: `P_k = 2 R_k (Φ_k⁺ − Φ_k⁻)/Φ_in` with `Φ_k^± = Y_k |a_k^±|²` from M4, so light trapped in a layer pushes both of its faces.

### M6. Rotation within and outside the layers: Thomas turn, and the square that turns, locks or runs

Equations and sources:
- Two perpendicular steps: `B_i B_j = L · Rot_k(θ_T)`, `tan(θ_T/2) = Γ²` for equal steps. `LEAN · thomas5`, `thomas7`, `thomas_half_angle` (`GH/votkp-lean/two-trees/lean/PeelTrees.lean:285, 295, 302`), `thomas_general` (`PeelTrees2.lean:365`); `PROVED · Two Trees v4, Theorem 4.7`. Exact values: `z = 5`: `cos = 65/97`, `sin = 72/97`; `z = 7`: `175/337`, `288/337`.
- Unequal steps: `tan(θ_T/2) = Γ_a Γ_b`. `CHECKED · 1e-9` (not in Lean).
- The square: `W = B_a B_b B_a⁻¹ B_b⁻¹`, SL(2) trace `2 − 4 sinh⁴(r/2) = 2 − 4(R/T)²` for equal steps. `LEAN · comm_trace` (`PeelTrees4.lean:35`); the `sinh⁴` form is `PROVED · Two Trees v4 (sharpness text)` and `CHECKED · FEED-LOOP-01/03`.
- Unequal steps: `g = sinh(h_a) sinh(h_b)`; `g < 1`: a turn with `cos φ = 8g⁴ − 8g² + 1`; `g > 1`: a run of length `4 arccosh g`. `CHECKED · 1e-10` (and already live in Balls mixer v2).
- The wall: `Γ² = ½ ⇔ z = 3 + 2√2 ⇔ R = T`; there the SL(2) trace is `−2` and `W` is one Jordan block (in the 4×4 form the trace is 4 and `W ≠ I`). `LEAN · schottky_five_below`, `schottky_seven_above`, `schottky_ratio` (`PeelTrees.lean:163-166`); `PROVED · Two Trees v4, Theorem 5.3`.
- The account of the two rotations (new in this plan): since `B_j B_i = (B_i B_j)ᵀ = Rᵀ L`, `W = L R L⁻¹ R`. The square is two Thomas turns, one of them carried through the boost `L`. `CHECKED · 1e-8` (sanity pass 3e-10). For small steps `φ ≈ 2 θ_T`.

Drawn: at the corner ball reached by `B_a B_b`, a frame of three short arms turned by `θ_T` against the dotted frame a pure boost would give (rotation within the layers). The gold four-step path of the Balls mixer, and the centre carried round a ring (turn), drifting to one rim point (lock), or running out (run) under repeated squares (rotation outside the layers). A prepared light direction on the rim, carried by the same square (Tree Ball Light v2: `FM.prep`, `FM.labAt`, `FM.kick`).
Moves: the loop phase `n(τ)` advances continuously; `θ_T(τ)` and the regime change as `z(τ)` crosses the wall.
Couples: `R/T` from M1 sets the trace; the rim direction is the M7 object.

### M7. Light on the rim: aberration is `⊕`, the face shadow, the caps

Equations and sources:
- A step acts on a future null vector `(t, x)`; its direction is the rim point `x/t`. Along the arm: `cos ψ′ = (cos ψ + tanh r)/(1 + cos ψ tanh r) = cos ψ ⊕ tanh r`, and `t′/t = cosh r + sinh r cos ψ`; on the axis `t′/t = z`. `CHECKED · 1e-12` (elementary Lorentz algebra). The integer form at `z = 7` is `LEAN · step_plane` (`GH/votkp-lean/two-trees/lean/PingPong7.lean:87`, `t′ = 25t + 24b`, `b′ = 24t + 25b`), `step_lorentz` (`:77`).
- Radar reading: a mirror at speed `Γ` returns the frequency ratio `z`. `LEAN · hyperbolic_length` (`Smith.lean:65`) for the identity `(1 + Γ)/(1 − Γ) = z`; the radar sentence is a `READING` (docstring).
- The cap of letter `u`: null directions with `cos ψ > 1/√2`. Six caps pairwise disjoint: `LEAN · caps_disjoint` (`PingPong7.lean:97`). Ping-pong: every null direction outside the cap of `−u` is sent into the cap of `u`: `LEAN · pingpong_step` (`:179`), ratio 7 only.
- The face's shadow on the rim (new in this plan): the face at distance `h` meets the rim in the circle `cos ψ₀ = tanh h = Γ`. At the wall `Γ = 1/√2`, so the face's rim circle is exactly the cap boundary, and neighbouring caps touch. `CHECKED · 1e-12`.
- The ping-pong inclusion for other ratios (new in this plan, from the aberration law): it holds exactly when `tanh r ≥ 2√2/3`, that is `z ≥ 3 + 2√2`. `CHECKED · zero exceptions in 1e5 directions per ratio`; chip must add "Lean at z = 7 only".

Drawn: the rim sphere carries a dense field of light directions (markers on the sphere). The six cap circles at 45° are fixed thin rings. The six face-shadow circles at `cos ψ₀ = Γ` move with `z(τ)` and pass through the cap rings at the wall. Applying the current step sweeps the directions along meridians toward the arm's rim point; marker colour follows the frequency ratio `t′/t` through the kit's `colour.ramp`.
Moves: all rim markers flow under the continuous step; shadow circles breathe.
Couples: the same `r` as M1; the shadow circle is the rim edge of the M2/M3 face; the carried direction is the M6 loop's object.

### H. The hypothesis layer (his picture, drawn on the same object)

| His statement | What is drawn | Proved pieces it stands on | What stays hypothesis |
|---|---|---|---|
| Light is trapped between layers and kicks itself on the hypersurface | The M4 counter-running streams in a layer, with each bounce flashing the face | `echo_series`, `film_is_oplus` | That the layer walls are electrons |
| Absorbed and re-emitted further down | Two stocks per layer: accessible `x_k` (bright markers) and retained `y_k` (hollow markers held on the face) | `CARD · B182 (theorem, conditional energy model)`: `ẋ = 𝒫 − (κ + a)x + by`, `ẏ = ax − by`; mean residence `(1 + a/b)/κ`; at `b = 0` a share `a/(κ + a)` stays | Which face has which `a`, `b`; that this is what light does at a face |
| Some balls radiate, some absorb | Per-ball switch: `b > 0` (returns all, after a delay) or `b = 0` (keeps a share) | Same card | The assignment |
| The electron sea is ground and follows light, leaving a record of each kick | The rim labelled "rim: the ground" (as in Balls mixer v2); the M5 record ring `K_k(τ)`; a signed running sum of kicks along each arm | `CARD · B203 (theorem)`: route `2Σ|r_j|` against endpoint `2|Σ r_j|`, defect `4 min(R₊, R₋)` | That the sea is the rim and that it stores the record |
| Balls connect at levels but always keep a gap layer (crystal spacing) | For each face pair: crossing circle and angle `α = arccos g` when `g < 1`, common perpendicular and gap `δ = arccosh g` when `g > 1`; the M3 tunnelled fraction across `δ`; the "balls round each edge = 360°/α" count from the Balls mixer's third eye | Two Trees Thm 5.3, 5.4, 8.4; BallJoins J4, J7 (as cited in Balls mixer v2); `film_is_oplus` for the plane-parallel gap | That a minimum gap is enforced |
| "My Snell's law at the hypersurface and Pauli exclusion principle" | Per face an occupation `C = 1/(z + 1) = (1 − Γ)/2`, shown as a filling fraction of a ring on the face; `T = 4C(1 − C)` | `LEAN · fermion_smith`, `fermion_center`, `particle_hole` (`Edition10.lean:183, 194, 213`): `1 − 2/(eˣ + 1) = tanh(x/2)`; with `x = ln z`, `C = 1/(z + 1)` (`CHECKED · 1e-14`); `0 ≤ C ≤ 1 ⇔ |Γ| ≤ 1` | That `x = ln z` is the fermion variable; that exclusion sets the spacing |

Display rule: the layer has one master toggle `Hypothesis layer: shown / hidden`. When hidden, nothing in the law readouts changes. That is itself a final check (K14d).

---

## 3. The shared clock and the feed

### 3.1 Clock

One object `CLOCK = { tau, playing, speed, dtFixed: 1/60 }`.
- `CLOCK.tau` advances by `dt · speed` inside whichever eye's `step(dt, …)` is current. The kit calls exactly one eye per frame, so `tau` is continuous across eye changes. Do not use the kit's `tEye` (it resets on `show`).
- Controls, in a sticky strip that the app appends after `M.run(…)`: `Play / Pause`, `Step` (advance by `dtFixed · speed` once), `Speed` (0.1 to 4), `Reset τ`, `Drive: hold / breathe / sweep`, `Hypothesis layer: shown / hidden`, `Admittance: falls outward / rises outward`, `Run self-test`.
- Reduced-motion users get `playing = false` at load and the Step button.

### 3.2 Feed

`feed(P, tau)` is a pure function. It returns the frozen state `S` for that instant. Everything not listed under "integrated" below is a pure function of `(P, tau)`.

Pure functions of time:

| Quantity | Formula | Chip |
|---|---|---|
| Step rapidity of arm `a ∈ {I, J, K}` | hold: `r_a = ln z̄_a`. breathe: `r_a(τ) = ln z̄_a + A sin(2πτ/T_a + φ_a)`, `T = (8, 13, 21)` s, `φ = (0, 2π/3, 4π/3)`, `A` slider 0 to 0.6. sweep: triangle wave in `r_a` between `ln 1.5` and `ln 13` with the same three periods ×3. Defaults `z̄ = (3, 5, 7)`. | `DRIVE` |
| `z_a, Γ_a, R_a, T_a, P_a, C_a` | `e^{r_a}`, `tanh(r_a/2)`, `Γ²`, `1 − Γ²`, `2R`, `1/(z + 1)` | M1, M5, H |
| Ball positions | `B(u_a, r_a) · O`, and tree nodes to depth `D` | Balls mixer v2 |
| Face planes | unit normal `N_w,u = g_w · (sinh h_u, cosh h_u · u)`, `h_u = r_u/2` | Balls mixer v2 |
| Face pairs | `g_ab = sinh h_a sinh h_b`, `α` or `δ` | Balls mixer v2 |
| Fan azimuth | `χ(τ) = 2π τ/T_χ`, `T_χ = 34` s | `DRIVE` |
| Light frequency | `ω` slider (sets phase and marker colour) | parameter |
| Thomas angle | `θ_T,ab(τ) = 2 arctan(Γ_a Γ_b)` | M6 |
| Loop matrix and regime | `W_ab(τ)` from `FM.boostM`; `kind ∈ {turn, wall, run}` | M6 |
| Ray tree | `traceAll(S)`: every segment, hit, angle, `R`, `T`, flux | M2, M3 |
| On-axis stacks | `stackAxis(S, a)`: `r_total`, layer amplitudes | M4 |
| Marker phase on a segment | `s = (v_k · τ + s₀) mod L`, `v_k = v₀ · Y₀/Y_k` (from `|ẇ| = √(2E/R)`) | M2 |

Integrated quantities (state carried forward, advanced by `advance(S, dτ)`):

| Quantity | Rule | Chip |
|---|---|---|
| Loop phase `n(τ)` | `dn = dτ/T_loop`, `T_loop = 5` s | `DRIVE` |
| Carried rim direction `p(τ)` | `p ← normalise(loopFlow(W(τ), dn) · p)`; `loopFlow` is the one-parameter subgroup through `W` (turn: `cos(dn θ/2) I + sin(dn θ/2)/sin(θ/2) X`; lock: `I + dn X′`; run: the `cosh/sinh` form), `X` the traceless part | M6 |
| Kick record `K_k(τ)` | `dK_k = P_k dτ` | `READING` |
| Stocks `x_k, y_k` | exact 2×2 matrix exponential per layer per step, source `𝒫_k = T`-fraction arriving | `HYPOTHESIS` on B182 |

### 3.3 Why the coupling is consistent

1. **One state per frame.** `scene.update(S)` draws every component from the same `S`. No component keeps its own copy of `z`.
2. **Each frame is a steady state of the instantaneous configuration.** The beams are steady rays; the markers are phase marks on them, with weight equal to the flux of the segment. So `R + T = 1` at every face and "flux in = flux out" at every node of the ray tree hold on every frame, not on average.
3. **The ledger.** `audit(S)` returns the largest residual of each balance law on that frame (list in 5, eye J). It runs every frame and feeds the ledger readout.
4. **What is not claimed** (must be said on the page, in the ledger eye's text): the faces move on a declared schedule; no law of motion for `z(τ)` is claimed; no retardation and no Doppler shift from the motion of a face is modelled. The Doppler factor shown in M7 belongs to the step acting on a light direction, not to the drive.

---

## 4. Code layout and named functions

Files (all in `WORK`; nothing is written into `ATT` or `GH`; every revision gets a new versioned filename):

| File | Marker | Role |
|---|---|---|
| `lh_math_v1.js` | `/* SCRIPT: LH-MATH-V1 */` | Pure maths, no DOM, no three.js. Loadable in node and inlined in the page. |
| `lh_app_v1.js` | `/* SCRIPT: LH-MIXER-V1 */` | The mixer: clock, shared world, eyes, strip, ledger. |
| `lh_selftest_v1.js` | `/* SCRIPT: LH-SELFTEST-V1 */` | Node runner for the page's own self-test list. |
| `lh_check_01.py` | `# SCRIPT: LH-CHECK-01` | Independent recomputation in Python (numpy; mpmath if present). Kill lines in the header, copied from section 7 before the run. |
| `lh_build_v1.py` | `# SCRIPT: LH-BUILD-V1` | Assembles the page: three.js block and `mixer3d_parts_v1` block copied verbatim from Balls mixer v2 (character offsets 201–651869 and 651870–670915 of `ATT/8293df2c-Balls_in_One_Ball__Mixer_v2___Jeromie_Beasley.html`), then `LH-MATH`, then `LH-MIXER`. |
| `lh_shot_v1.py` | `# SCRIPT: LH-SHOT-V1` | Screenshots of every eye at three clock values (model: `scratchpad/tbl_checks/shot_v2.py`). |

Output page: `Light_at_the_Hypersurface_Mixer_v1_20261115.html`.

Reuse verbatim from Balls mixer v2 app script: `boost, mm, mv, I4, mink, hdist, toBall, w3, geo, faceGeom, face, crossing, pairMath, rim, tree, balls, clear`. Reuse verbatim from `scratchpad/tbl_checks/feed_math.js`: `FM` (SL(2) loop, `calc, prep, labAt, kick, boost4`).

`LH-MATH` exports (`window.LH` / `module.exports`):

```
smith(z)                       -> Γ
oplus(u, v)                    -> complex (u+v)/(1+uv)          [complex as [re, im]]
step(Y1, Y2)                   -> {r, t, R, T}                  Y complex allowed
facePlane(g, u, h)             -> N (unit spacelike 4-vector)
hitPlane(X, v, N)              -> s or null      tanh s = −<X,N>/<v,N>, s > 0
geoPoint(X, v, s), geoTangent(X, v, s)
incidence(vHit, N)             -> {cos, sin}     cos = |<v,N>|
reflectDir(v, N)               -> v + 2<v,N>N
refractDir(v, N, sin2)         -> cos2·(−sign<v,N>)N + sin2·t̂ ,  t̂ = (v + <v,N>N)/sin1
splitAtFace(a1, a2, sin1sq, omega, b)
                               -> {C, Y1, Y2, r, R, T, total, sin2sq, theta2 (complex if total),
                                   phase, kappaE, depth}
thetaCrit(a1, a2)              -> arcsin sqrt(a2/a1) or null
nodeAdmittance(word, S)        -> Y0 · Π z_letter^(∓1)   (sign from the orientation toggle)
traceRay(X0, v0, word, flux, S, budget) -> segments[]  (reflect + transmit children; stop at flux < 1e−4 or 6 faces)
traceAll(S)                    -> all segments for the fan
stackAxis(Ys, phis)            -> {r, t, amps:[{ap, am}], flux:[…]}   (recursion by oplus AND transfer matrix)
bounceSum(g, x, M)             -> partial echo series
echoCircle(a)                  -> {A, C, xc}
tunnelGap(Y1, kappaE, w)       -> {r, t, T}
stress(E, H), normalStress(sigma, n)
thomas(ra, rb)                 -> {theta, L, R}     (polar decomposition of the 4×4 product)
loopSL2(ra, rb, ua, ub)        -> W ;  loopFlow(W, dn) ; loopKind(W)
aberrate(cosPsi, r)            -> cosPsi ⊕ tanh r ;  doppler(cosPsi, r)
inCap(v, u)                    -> boolean  (cos ψ > 1/√2)
faceShadow(h)                  -> cos ψ0 = tanh h
stocksStep(x, y, P, kappa, a, b, dt)  -> exact matrix-exponential step
occupation(z)                  -> 1/(z+1)
feed(P, tau)                   -> S
advance(state, S, dtau)        -> integrated quantities
audit(S)                       -> {flux, snell, stackFlux, nullNorm, detW, …}  largest residuals
selftest()                     -> [{id, value, tol, pass}]
```

Layer labelling rule: a ray carries the tree word of the cell it is in. Crossing the face of letter `u` appends `u` (or cancels with the last letter). Candidate faces in cell `w` are the six planes `g_w · N_u`. Below the wall the cells of the tree overlap (the group is free but not discrete there, Two Trees Thm 5.3), so the label belongs to the ray, not to the point; say so in eye C's text.

Marker budget: at most 25,000 points in total; a `Density` control scales it. Use the kit's `points / setPt / flush`, `trail`, `line`, `label`, `shell`, `colour`.

---

## 5. Eyes, in film order (lettered panels)

Each eye: letter, title, section line, grade chips, equation block, one paragraph of plain scientific English, controls it uses, readout rows.

**A. The object: four balls, their faces and the rim.** Feed: `B(u, ln z)`.
Readouts: per arm `z, ln z, Γ, R, T`; `Γ² against ½`; per pair `g`, crossing angle `α` or gap `δ`; clock `τ`; drive mode.

**B. One face is one reflecting step (M1).**
Readouts: `Y₁/Y₂`; `r`, `t`; `R`, `T`; `R + (Y₂/Y₁)t² − 1` (live residual); `E⁻/E⁺`; `Γ` reversed; distance to matched load (`|Γ|`) and to the mirror (`1 − |Γ|`); `Γ(−z)·Γ(z)`.

**C. Refraction at the face (M2).**
Controls: fan half-angle, `ω`. Readouts for the tagged ray: `ψ`; `θ₁` measured from the drawn tangent; `cosh h · sin ψ`; `a₁ sin²θ₁`; `a₂ sin²θ₂` measured from the drawn refracted tangent; their difference; `R(θ)`, `T(θ)`; layer speeds `√(2E/a₁)`, `√(2E/a₂)`; cell word of the ray.

**D. Total return and the gap (M3).**
Readouts: `κ = a₁/a₂`; `θ_crit = arcsin(1/z)` in degrees; transmission window half-angle at the centre `ψ_t = arcsin(1/(z cosh h))`; for the tagged ray: state (crosses / returned whole), `|Γ|`, return phase, `θ₂` (real or `π/2 + i·u`), penetration depth `ℓ`; for the selected pair: `δ`, tunnelled fraction at the chosen incidence.

**E. Layers: echoes and Smith addition (M4).**
Controls: depth `D`, `ω`, selected arm. Readouts: per-face `Γ_k`; phases `φ_k`; composed `r` by `⊕`; composed `r` by the bounce sum (first `M` terms) and the difference; `|r|²`, `T_total`; net flux in each layer (must be one number); zero-phase value `tanh(D r/2)`; echo-circle side (inside / outside) and `x_c`.

**F. Pressure and the kick record (M5).**
Readouts: per face `P = 2R`; oblique `2R cos²θ` for the tagged ray; `K = 1/(1 − P)`; push from circulating light `P_k`; record `K_k(τ)`; Maxwell normal stress on the tilted face `−u cos²θ`.

**G. Rotation within and outside the layers (M6).**
Controls: pair, passes shown. Readouts: `θ_T` (degrees) and `2 arctan(Γ_a Γ_b)`; loop angle or run length; SL(2) trace; regime (turns / locks / runs); `‖W − L R L⁻¹ R‖`; loop phase `n(τ)`; carried direction's angle to the loop axis.

**H. Light on the rim (M7).**
Readouts: face shadow angle `ψ₀ = arccos Γ`; cap angle 45°; shadow minus cap; aberration `tanh r`; frequency ratio on the axis `z`; share of rim directions inside the six caps; ping-pong at this `z` (holds / fails, with the count of exceptions in the live sample); note `Lean: z = 7`.

**I. The hypothesis layer (H).** Every row begins `hypothesis:`.
Controls: `κ, a, b` per ball class (radiating / absorbing). Readouts: per layer `x_k, y_k`; mean residence `(1 + a/b)/κ`; share kept at `b = 0`; ledger `in − out − stored`; occupation `C`, `4C(1 − C)`; route, endpoint and defect of the kick record; gap `δ` and tunnelled fraction; balls round an edge `360°/α`.

**J. Everything at once, and the ledger.**
All components at full emphasis. Readouts: the `audit(S)` residuals (flux at faces, `a sin²θ`, stack flux, node flux of the ray tree, `det W − 1`, null norm of carried directions), each with its tolerance; the list of what is not claimed (3.3 item 4); self-test result line `n of m lines hold` after `Run self-test`.

Text rule for every eye: plain correct scientific English; no slang; no metaphor. The note under the title reads `an explorer of checked formulas, not a test of them` (as on Balls mixer v2). The self-test button is labelled `Run self-test (this page's arithmetic)`.

---

## 6. Open, or must not be claimed

1. Steps compose as one velocity on one axis only (`peel-atlas/CLAIMS.md` V3). Two axes give a boost and a rotation. M4's telescoping is on one arm only.
2. With a phase, the film map `Γ ⊕ x` is not a disk isometry (card B98: a conjugate is needed in the denominator). Do not call the phased stack "velocity addition".
3. The Poincaré metric is not formalised in Lean (CLAIMS V2); only `(1 + Γ)/(1 − Γ) = z` is. Geodesic rays in the ball are elementary geometry, numerically checked here, drawn in the peel ball.
4. Reading a peel step as an admittance step (`Y₁/Y₂ = z`), and `a = n²`, are readings (CLAIMS V4 is a Proposal).
5. PingPong Lean covers ratio 7 only. The statement for `z ≥ 3 + 2√2` is a numerical check from the aberration law made in this build.
6. Card B4 is a conjecture. Do not identify `R sin²θ` with the projector distance `2 sin²θ` (`rank_one_projector_hs_distance_sq`).
7. The `R sin²θ` form came from an earlier model (provenance note in `HypersurfaceSquareLineage.lean`); Lean covers the algebra, not the path integration; `upg.tex` grades the refraction angle as pending.
8. Card B30's `|v⊥| ∝ 1/√(2λ)`: Lean has only the reduced four-body wall map (`four_body_normal_squeeze`, a unit test of a reduced model). The mixer shows `√(2E/R)·cos θ` from the card's Lagrangian and quotes the card line; it does not identify `λ` with the layer rigidity.
9. B175: the horizon reading is structural. No reflection is not full absorption.
10. `P = 2R` as a physical pressure is untested. The momentum carried on by transmitted light inside a layer is not modelled. The Maxwell repo formalises no Poynting vector.
11. No law of motion for `z(τ)`; no retardation; no Doppler from face motion.
12. Thomas: Lean at ratios 5 and 7 and for equal steps. Unequal steps and `W = L R L⁻¹ R` are numerical checks. The turn is of the frame; no claim about polarisation of light.
13. B182 is a conditional energy model. `x = ln z` as the fermion variable is a reading. Exclusion as the cause of spacing is his hypothesis.
14. B59: the transmission cone and the resolvability cone are not identified.
15. Off-axis rays split by flux without phases. Coherent echoes are modelled on the arm axis only. The tunnelled fraction is exact for a plane-parallel gap; the faces here are parallel only along their common perpendicular.
16. Not included: Hawking record as a temperature, photon ring `e^{−π}`, Painlevé–Gullstrand slopes (these live in a declared Schwarzschild model; his intrinsic metric is not to be swapped for a spacetime metric). `light-ledger-lean/Rigidity.lean` (header says not compiled) is not used as law.
17. Lean was not re-run in this session. Chips name the theorem and the file; they do not say "verified here".

---

## 7. Final checks: kill lines, written before any run

Rule: exploration first, with loose tests only. When the build is frozen, copy this table into the header of `lh_check_01.py` and `lh_selftest_v1.js` unchanged, then run once. A line that fails is reported as failed; the corresponding chip is downgraded or the item is set aside into the ledger of the build, never silently dropped. Before any item is called dead, its opposite is run under the same line.

| ID | Statement | Kill if |
|---|---|---|
| K1 | Flux at a step: `|R + (Y₂/Y₁)t² − 1|` over 1e4 random `Y ∈ [1e−2, 1e2]` | > 1e-12 |
| K2 | `|(Y₁ − Y₂)/(Y₁ + Y₂) − tanh(½ ln(Y₁/Y₂))|`; reciprocity; `z = 1 ⇒ Γ = 0`; `Y₂ = 0 ⇒ Γ = 1`; `Γ(−z)Γ(z) = 1`; `|G(z̄)|·|G(z)| = 1` on 1e3 complex pairs | any > 1e-12 |
| K3 | Refraction: `|a₁ sin²θ₁ − a₂ sin²θ₂|` at every transmitted hit, both angles **measured from the drawn tangent vectors by Minkowski products**, not from the formula that built them; and `|sin θ − cosh h sin ψ|` for centre rays | > 1e-10 |
| K4 | Oblique flux with `Y = √(a − C)`: `|R + T − 1|` on 1e4 cases | > 1e-12 |
| K5 | Critical angle: threshold found by bisection on "transmitted branch exists" against `arcsin √(a₂/a₁)`; at `κ = 4` it is 30°; past it `||Γ| − 1|`; `|arg Γ + 2 arctan(κₑ/y)|`; `|sin(π/2 + i arccosh(√κ sin θ₁)) − √κ sin θ₁|` | angle > 1e-9 rad; others > 1e-12 |
| K6 | Film: `⊕` against the explicit bounce sum (400 terms, `|Γx| ≤ 0.9`); recursion against transfer matrix for 2 to 6 layers; net flux equal in every layer; zero-phase telescoping; `D` equal steps at zero phase give `tanh(D r/2)`; echo circle: `sign(|r|² − |a|²) = sign(|x − x_c| − |x_c|)` on 1e4 random complex cases; `a = ½, x = ±⅕` give `49/121`, `1/9` | sum > 1e-10; others > 1e-12; any sign exception; witness > 1e-15 |
| K7 | Gap: `||r|² + |t|² − 1|` (equal outer media); slope of `ln T` against `w` equals `−2κₑ` for `κₑ w ∈ [3, 6]` | > 1e-12; relative slope error > 1e-3 |
| K8 | Wall: at `z = 3 + 2√2`, `|R − ½|`; `|tr_SL(2) W + 2|`; `‖(W + I)²‖`, with `‖W + I‖ > 1e-3` required; `z = 5` gives `R = 4/9 < ½`, `z = 7` gives `9/16 > ½`; trace `= 2 − 4(R/T)²` on 500 ratios | `R`: > 1e-14; trace: > 1e-12; Jordan: > 1e-10; formula: > 1e-12 |
| K9 | Thomas: angle from the polar decomposition against `2 arctan(Γ_a Γ_b)` on 500 random pairs; `z = 5`: `(cos, sin) = (65/97, 72/97)`; `z = 7`: `(175/337, 288/337)` | > 1e-9; exact values > 1e-13 |
| K10 | `‖W − L R L⁻¹ R‖/‖W‖`; `cos φ = 8g⁴ − 8g² + 1` for `g < 1`; run length `4 arccosh g` for `g > 1` | > 1e-8; > 1e-10 |
| K11 | Rim: aberration `= ⊕`; on-axis frequency ratio `= z`; ping-pong with zero exceptions in 1e5 random null directions for `z ∈ {(3 + 2√2)(1 + 1e−6), 7, 9, 13}`; **at `z = 5` at least one exception must be found**; integer check at `z = 7`: step of `(3, 1, 2, 2)` lands in the cap of its letter | residual > 1e-12; any exception above the wall; no exception at 5; integer check false |
| K12 | Face shadow: the face plane meets the rim at `cos ψ₀ = Γ`; at the wall `ψ₀ = 45°` | > 1e-12 |
| K13 | Pressure: Maxwell normal stress on a plane tilted by `θ` equals `−u cos²θ` (transverse, `|E| = |H|`), 500 random frames; FEED-LOOP-03 lines P1, P2, P3 re-run unchanged | > 1e-12; P1–P3 at their own tolerances |
| K14 | **Simultaneous motion.** Run the clock for 2000 fixed steps in `breathe` and 2000 in `sweep` (every arm crosses the wall). On every frame: (a) every face and every ray-tree node: flux residual; (b) `a sin²θ` residual; (c) stack net-flux spread; `|det W − 1|`; null norm of every carried direction. (d) With the hypothesis layer hidden, every law readout is bitwise identical to the run with it shown. (e) Every pure quantity at step `n` equals `feed(P, n·dτ)` computed cold, bitwise. (f) Integrated quantities with `dτ` halved agree | (a)–(c) > 1e-10; (d), (e) any difference; (f) > 1e-6 |
| K15 | B182: impulse total outflow `= 1`; mean residence `(1 + a/b)/κ`: `(1, 1, 0.2) → 6`, `(1, 1, 0.02) → 51`; `b = 0` keeps `a/(κ + a) = 0.5`; network ledger `|in − out − stored|` over the K14 run | > 1e-9 |
| K16 | B203: `2Σ|r_j| − 2|Σ r_j| = 4 min(R₊, R₋)` on 1e3 random chains | > 1e-12 |
| K17 | `1 − 2C = Γ` and `T = 4C(1 − C)` with `C = 1/(z + 1)` | > 1e-14 |
| K18 | Faces: `<N_a, N_b> = sinh h_a sinh h_b`; dihedral angle measured from the two drawn caps `= arccos g`; minimum hyperbolic distance between two separated planes `= arccosh g` | > 1e-12; > 1e-10; > 1e-8 |
| K19 | Page equals script: every self-test value computed in the browser equals the node value | relative difference > 1e-12 |
| K20 | Rendering: no console error in any eye at `τ = 0, 7, 40`; frame time under 33 ms at default density on the sandbox | any error |

Independence rule for `lh_check_01.py`: it must not import or transliterate `lh_math_v1.js`. It recomputes each item from the 4×4 and 2×2 matrices directly.

Note carried from the sanity pass: with signature `(+, −, −, −)`, `<N_a, N_b> = + sinh h_a sinh h_b`. The sanity script printed a non-zero number for this line only because it tested the opposite sign.

---

## 8. Build order

1. Make `WORK`. Copy the two source mixers and `feed_math.js` in as read-only references. Never write into `ATT`.
2. Write `lh_math_v1.js` in this order: Smith and step; hyperboloid ray tracing (`hitPlane` … `refractDir`); `splitAtFace`; `stackAxis` with both routes; Thomas and loop; rim (`aberrate`, `inCap`, `faceShadow`); stocks; `feed`; `advance`; `audit`. After each group, a loose node test (print residuals; no kill lines yet).
3. Write the app shell: `CLOCK`, the control strip, the shared `WORLD` group added to `S3.world` once (take `S3` from the first eye's `make(g, S3)`), `scene.update(S)`. Get eye A moving in all three drive modes.
4. Add components to `WORLD` in film order B to H. After each one: build, screenshot, and look at the screenshot.
5. Add the hypothesis layer (I) with its distinct drawing style and the master toggle.
6. Add eye J, the ledger, and `Run self-test`.
7. Freeze. Copy section 7 into the script headers. Run `lh_check_01.py` and `lh_selftest_v1.js` once each; save `.out` files.
8. Screenshots of all ten eyes at three clock values; view each.
9. Deliverables: the one HTML page; one zip with the scripts, outputs and this plan. No PDF preview.

If the builder thinks a different approach to any model is better, say so before building it and build both where the choice is his (for example the admittance orientation, already a toggle).

---

## 9. What the reviewer will check

1. **One object.** Changing eyes never rebuilds or resets the scene; `τ` does not jump; everything keeps moving in every eye.
2. **One feed.** Search the app for any second source of `z`, `r` or `Γ`. There must be none outside `feed`.
3. **Kill lines unchanged.** Diff the headers of the check scripts against section 7.
4. **Independence.** `lh_check_01.py` shares no code with the page; K3 measures angles from tangents.
5. **Outputs.** Every K line has a number in the `.out` files; none is "skipped".
6. **Chips.** Each equation block's chips match section 2 exactly; no hypothesis has a law chip; every Lean name exists at the cited file (grep).
7. **Words.** No slang or metaphor; no "lab"; no cosmology framing; byline is first and last name only; the AI-assisted line is present; no bar graphs; no second sphere or comparison panel anywhere.
8. **Section 6 is on the page** in eye J's text, in short form.
9. **Wall crossing.** In `sweep`, at the frame nearest each crossing: the face shadow passes the cap ring, the loop changes regime, and `R` passes ½ on the same frame.
10. **Picture.** Rays visibly bend toward the normal on the denser side; the total-return annulus is where the tagged ray says it is; marker density follows flux.
11. **Originals untouched.** Modification times of the files in `ATT` and `GH` are unchanged.
