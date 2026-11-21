/-
VOTKP: The Vector of Traits Kept under Peeling (Jeromie Beasley, v1.1, 25 September 2026).
The reflection coordinate and its addition law.

* Theorem 8.1: for a ratio `z = IE_{k+1}/IE_k > 0`, `(z − 1)/(z + 1) = tanh(½ ln z)`, and
  every `z > 1` lands on the positive real radius `0 < Γ < 1`. Any `Γ ∈ (−1, 1)` is reached by
  `z = (1 + Γ)/(1 − Γ)`, so the chart alone constrains no dynamics.
* Theorem 15.1: `tanh(a + b) = tanh a ⊕ tanh b` with `u ⊕ v = (u + v)/(1 + uv)`, so the
  reflection of a block of removals is the `⊕`-sum of its steps.
* Corollary 15.2: `ln((1 + Γ)/(1 − Γ)) = ln z`, the hyperbolic distance from the centre.
* `⊕` is commutative and associative, so the composite carries no order: the ladders
  `1, 2, 6` and `1, 3, 6` have different steps and the same composite `5/7`.
* Corollary 15.3: `1 − tanh² t = 1/cosh² t`, the round-trip factor as `1/γ²`.
* Theorem 8.2: with `IE_k = Ry Z_k²/n_k²`, the step splits into screening and shell parts,
  `Γ = tanh(Δ ln Z) ⊕ tanh(−Δ ln n)`, and at a shell wall the shell part is
  `(2n − 1)/(n² + (n − 1)²)`: `3/5, 5/13, 7/25, 9/41, 11/61, 13/85` for `n = 2, …, 7`,
  the odd leg over the hypotenuse of a Pythagorean triple (Euclid's form).
* Theorem 15.4, the ratio part: scaling every energy by `λ > 0` leaves each ratio unchanged.
* Section 15.4: a negative ratio (a negative separation energy) gives `|Γ| > 1`.
-/
import Mathlib

namespace VOTKP.Smith

open Real

/-- Einstein's addition law `u ⊕ v = (u + v)/(1 + uv)`. -/
noncomputable def oplus {K : Type*} [Field K] (u v : K) : K := (u + v) / (1 + u * v)

/-- `tanh t = (e^{2t} − 1)/(e^{2t} + 1)`. -/
theorem tanh_exp (t : ℝ) : tanh t = (exp (2 * t) - 1) / (exp (2 * t) + 1) := by
  have h2 : exp (2 * t) = exp t * exp t := by rw [← exp_add]; ring_nf
  have hn : exp (-t) = (exp t)⁻¹ := exp_neg t
  have he : 0 < exp t := exp_pos t
  rw [tanh_eq_sinh_div_cosh, sinh_eq, cosh_eq, h2, hn]
  have h1 : exp t + (exp t)⁻¹ ≠ 0 := by positivity
  have h3 : exp t * exp t + 1 ≠ 0 := by positivity
  field_simp
  try ring

/-- **Theorem 8.1.** For `z > 0`, `(z − 1)/(z + 1) = tanh(½ ln z)`. -/
theorem smith_identity (z : ℝ) (hz : 0 < z) : (z - 1) / (z + 1) = tanh (log z / 2) := by
  rw [tanh_exp]
  have : 2 * (log z / 2) = log z := by ring
  rw [this, exp_log hz]

/-- Every ratio `z > 1` lands on the positive real radius: `0 < Γ < 1`. -/
theorem positive_radius (z : ℝ) (hz : 1 < z) : 0 < (z - 1) / (z + 1) ∧ (z - 1) / (z + 1) < 1 := by
  constructor
  · apply div_pos <;> linarith
  · rw [div_lt_one (by linarith)]; linarith

/-- The chart constrains nothing by itself: any `Γ ∈ (−1, 1)` is reached by
`z = (1 + Γ)/(1 − Γ) > 0`. -/
theorem any_target (g : ℝ) (h1 : -1 < g) (h2 : g < 1) :
    0 < (1 + g) / (1 - g) ∧ ((1 + g) / (1 - g) - 1) / ((1 + g) / (1 - g) + 1) = g := by
  have hne : (1 - g) ≠ 0 := by linarith
  refine ⟨div_pos (by linarith) (by linarith), ?_⟩
  field_simp
  try ring

/-- **Corollary 15.2.** For `Γ = (z − 1)/(z + 1)`, `(1 + Γ)/(1 − Γ) = z`, so the hyperbolic
distance `ln((1 + Γ)/(1 − Γ))` from the centre is `ln z`. This is also the radar reading:
a mirror at speed `Γ` returns the frequency ratio `z`. -/
theorem hyperbolic_length (z : ℝ) (hz : 0 < z) :
    (1 + (z - 1) / (z + 1)) / (1 - (z - 1) / (z + 1)) = z := by
  have h : z + 1 ≠ 0 := by linarith
  field_simp
  try ring

/-- **Theorem 15.1, one step.** `tanh(a + b) = tanh a ⊕ tanh b`. -/
theorem tanh_add' (a b : ℝ) : tanh (a + b) = oplus (tanh a) (tanh b) := by
  have ca : cosh a ≠ 0 := (cosh_pos a).ne'
  have cb : cosh b ≠ 0 := (cosh_pos b).ne'
  have hc : cosh a * cosh b ≠ 0 := by positivity
  have hs : cosh a * cosh b + sinh a * sinh b ≠ 0 := by rw [← cosh_add]; exact (cosh_pos _).ne'
  rw [tanh_eq_sinh_div_cosh, tanh_eq_sinh_div_cosh, tanh_eq_sinh_div_cosh, sinh_add, cosh_add,
    oplus]
  rw [div_add_div _ _ ca cb, div_mul_div_comm, one_add_div hc, div_div_div_cancel_right₀ hc]

/-- The reflection of one removal step. -/
noncomputable def stepΓ (IE : ℕ → ℝ) (k : ℕ) : ℝ := tanh (log (IE (k + 1) / IE k) / 2)

/-- The reflection of the block of removals from `k` to `k + m`. -/
noncomputable def blockΓ (IE : ℕ → ℝ) (k m : ℕ) : ℝ := tanh (log (IE (k + m) / IE k) / 2)

/-- **Theorem 15.1.** Peel steps add like velocities:
`Γ_{k→k+m+1} = Γ_{k→k+m} ⊕ Γ_{k+m}`. -/
theorem block_succ (IE : ℕ → ℝ) (hpos : ∀ j, 0 < IE j) (k m : ℕ) :
    blockΓ IE k (m + 1) = oplus (blockΓ IE k m) (stepΓ IE (k + m)) := by
  unfold blockΓ stepΓ
  rw [← tanh_add']
  congr 1
  have h1 := (hpos k).ne'
  have h2 := (hpos (k + m)).ne'
  have h3 := (hpos (k + m + 1)).ne'
  rw [← add_assoc, log_div h3 h1, log_div h2 h1, log_div h3 h2]
  ring

/-- The block reflection is the Smith reflection of the overall ratio `IE_l/IE_k`. -/
theorem block_smith (IE : ℕ → ℝ) (hpos : ∀ j, 0 < IE j) (k m : ℕ) :
    blockΓ IE k m = (IE (k + m) / IE k - 1) / (IE (k + m) / IE k + 1) := by
  rw [blockΓ, smith_identity _ (div_pos (hpos _) (hpos _))]

section Group

variable {K : Type*} [Field K]

/-- `⊕` is commutative. -/
theorem oplus_comm (u v : K) : oplus u v = oplus v u := by
  unfold oplus; rw [add_comm u v, mul_comm u v]

/-- `⊕` is associative wherever the denominators are nonzero, so a composite reflection
carries no information about the order or grouping of its steps. -/
theorem oplus_assoc (u v w : K) (h1 : 1 + u * v ≠ 0) (h2 : 1 + v * w ≠ 0) :
    oplus (oplus u v) w = oplus u (oplus v w) := by
  unfold oplus
  rw [div_add' _ _ _ h1, div_mul_eq_mul_div, one_add_div h1, div_div_div_cancel_right₀ h1,
    add_div' _ _ _ h2, mul_div_assoc', one_add_div h2, div_div_div_cancel_right₀ h2]
  rw [show u + v + w * (1 + u * v) = u * (1 + v * w) + (v + w) by ring,
    show 1 + u * v + (u + v) * w = 1 + v * w + u * (v + w) by ring]

end Group

/-- **Order drops out of the composite.** The ladders `1, 2, 6` and `1, 3, 6` have different
first steps, `1/3` and `1/2`, and the same composite `5/7`. -/
theorem ladders_same_composite :
    oplus ((2 - 1) / (2 + 1) : ℝ) ((3 - 1) / (3 + 1)) = (6 - 1) / (6 + 1) ∧
      oplus ((3 - 1) / (3 + 1) : ℝ) ((2 - 1) / (2 + 1)) = (6 - 1) / (6 + 1) ∧
      ((2 - 1) / (2 + 1) : ℝ) ≠ (3 - 1) / (3 + 1) := by
  refine ⟨?_, ?_, ?_⟩ <;> norm_num [oplus]

/-- **Corollary 15.3.** The round-trip factor `1 − Γ²` at `Γ = tanh t` is `1/cosh² t`. -/
theorem round_trip (t : ℝ) : 1 - tanh t ^ 2 = 1 / cosh t ^ 2 := by
  have hc := (cosh_pos t).ne'
  rw [tanh_eq_sinh_div_cosh]
  field_simp
  linarith [cosh_sq_sub_sinh_sq t]

/-! ## Theorem 8.2: screening and shell -/

/-- **Theorem 8.2, the log step.** With `IE = Ry Z²/n²`,
`½ ln(IE'/IE) = (ln Z' − ln Z) − (ln n' − ln n)`. -/
theorem split_log (Ry Z Z' n n' : ℝ) (hR : 0 < Ry) (hZ : 0 < Z) (hZ' : 0 < Z') (hn : 0 < n)
    (hn' : 0 < n') :
    log ((Ry * Z' ^ 2 / n' ^ 2) / (Ry * Z ^ 2 / n ^ 2)) / 2 =
      (log Z' - log Z) - (log n' - log n) := by
  have e : (Ry * Z' ^ 2 / n' ^ 2) / (Ry * Z ^ 2 / n ^ 2) = (Z' / Z) ^ 2 * (n / n') ^ 2 := by
    field_simp
    try ring
  rw [e, log_mul (by positivity) (by positivity), log_pow, log_pow,
    log_div hZ'.ne' hZ.ne', log_div hn.ne' hn'.ne']
  push_cast
  ring

/-- **Theorem 8.2.** The step splits exactly: `Γ = tanh(Δ ln Z) ⊕ tanh(−Δ ln n)`. -/
theorem split_step (Ry Z Z' n n' : ℝ) (hR : 0 < Ry) (hZ : 0 < Z) (hZ' : 0 < Z') (hn : 0 < n)
    (hn' : 0 < n') :
    tanh (log ((Ry * Z' ^ 2 / n' ^ 2) / (Ry * Z ^ 2 / n ^ 2)) / 2) =
      oplus (tanh (log Z' - log Z)) (tanh (-(log n' - log n))) := by
  rw [split_log Ry Z Z' n n' hR hZ hZ' hn hn', ← tanh_add']
  ring_nf

/-- **The shell wall.** For `n > 1`, the ratio `z = (n/(n − 1))²` has
`(z − 1)/(z + 1) = (2n − 1)/(n² + (n − 1)²)`. -/
theorem shell_wall (n : ℝ) (hn : 1 < n) :
    ((n / (n - 1)) ^ 2 - 1) / ((n / (n - 1)) ^ 2 + 1) = (2 * n - 1) / (n ^ 2 + (n - 1) ^ 2) := by
  have h1 : n - 1 ≠ 0 := by linarith
  have h2 : n ^ 2 + (n - 1) ^ 2 ≠ 0 := by positivity
  rw [div_pow]
  field_simp
  try ring

/-- The wall values for `n = 2, …, 7`. -/
theorem shell_wall_values :
    ((2 : ℝ) * 2 - 1) / (2 ^ 2 + (2 - 1) ^ 2) = 3 / 5 ∧
      ((2 : ℝ) * 3 - 1) / (3 ^ 2 + (3 - 1) ^ 2) = 5 / 13 ∧
      ((2 : ℝ) * 4 - 1) / (4 ^ 2 + (4 - 1) ^ 2) = 7 / 25 ∧
      ((2 : ℝ) * 5 - 1) / (5 ^ 2 + (5 - 1) ^ 2) = 9 / 41 ∧
      ((2 : ℝ) * 6 - 1) / (6 ^ 2 + (6 - 1) ^ 2) = 11 / 61 ∧
      ((2 : ℝ) * 7 - 1) / (7 ^ 2 + (7 - 1) ^ 2) = 13 / 85 := by
  norm_num

/-- The wall fractions are odd leg over hypotenuse of a Pythagorean triple:
`(2n − 1)² + (2n(n − 1))² = (n² + (n − 1)²)²`. -/
theorem pythagorean (n : ℤ) :
    (2 * n - 1) ^ 2 + (2 * n * (n - 1)) ^ 2 = (n ^ 2 + (n - 1) ^ 2) ^ 2 := by ring

/-- Euclid's form: `tanh(ln(p/q)) = (p² − q²)/(p² + q²)` for `p, q > 0`. -/
theorem euclid_form (p q : ℝ) (hp : 0 < p) (hq : 0 < q) :
    tanh (log (p / q)) = (p ^ 2 - q ^ 2) / (p ^ 2 + q ^ 2) := by
  have hz : 0 < (p / q) ^ 2 := by positivity
  have e : log (p / q) = log ((p / q) ^ 2) / 2 := by rw [log_pow]; push_cast; ring
  rw [e, ← smith_identity _ hz, div_pow]
  have : q ^ 2 ≠ 0 := by positivity
  field_simp
  try ring

/-! ## Changing the particles -/

/-- **Theorem 15.4, the ratio part.** Scaling every energy by `λ > 0` leaves each ratio, and so
the peel coordinate, unchanged. -/
theorem scale_blind (l a b : ℝ) (hl : l ≠ 0) : (l * a) / (l * b) = a / b :=
  mul_div_mul_left a b hl

/-- **Section 15.4.** A negative ratio, from a negative separation energy, leaves the disk:
`|(z − 1)/(z + 1)| > 1` for `z < 0`, `z ≠ −1`. -/
theorem negative_ratio_leaves_disk (z : ℝ) (hz : z < 0) (h1 : z + 1 ≠ 0) :
    1 < |(z - 1) / (z + 1)| := by
  rw [abs_div, one_lt_div (abs_pos.mpr h1)]
  apply sq_lt_sq.mp
  nlinarith

/-- **Section 15.2, matter waves.** At a potential step,
`(k₁ − k₂)/(k₁ + k₂) = −tanh(½ ln(k₂/k₁))`. -/
theorem matter_wave (k1 k2 : ℝ) (h1 : 0 < k1) (h2 : 0 < k2) :
    (k1 - k2) / (k1 + k2) = -tanh (log (k2 / k1) / 2) := by
  rw [← smith_identity _ (div_pos h2 h1)]
  have : k1 + k2 ≠ 0 := by linarith
  have : k2 + k1 ≠ 0 := by linarith
  field_simp
  try ring

/-! ## Corollary 15.2: the peel coordinate is a Poincaré length -/

/-- **Corollary 15.2.** For `0 < IE_k < IE_l` and `w = (IE_l − IE_k)/(IE_l + IE_k)`,
the Poincaré distance from the disk centre is `d(0, w) = 2 artanh|w| = ln(IE_l/IE_k)`. -/
theorem poincare_distance (Ek El : ℝ) (hk : 0 < Ek) (hl : Ek < El) :
    let w := (El - Ek) / (El + Ek)
    2 * artanh |w| = log ((1 + |w|) / (1 - |w|)) ∧ 2 * artanh |w| = log (El / Ek) := by
  intro w
  have hwpos : 0 < w := by
    apply div_pos <;> linarith
  have hwlt : w < 1 := by
    rw [div_lt_one (by linarith)]
    linarith
  have habs : |w| = w := abs_of_pos hwpos
  have hmem : |w| ∈ Set.Icc (-1) 1 := by
    rw [habs]
    exact ⟨by linarith, by linarith⟩
  have hlen := hyperbolic_length (El / Ek) (div_pos (by linarith) hk)
  have hwz : w = (El / Ek - 1) / (El / Ek + 1) := by
    field_simp
    ring
  have hratio : (1 + w) / (1 - w) = El / Ek := by
    rw [← hwz] at hlen
    exact hlen
  refine ⟨?_, ?_⟩
  · rw [artanh_eq_half_log hmem, habs]
    ring
  · rw [artanh_eq_half_log hmem, habs, hratio]
    have : 2 * (1 / 2 * log (El / Ek)) = log (El / Ek) := by ring
    exact this

/-! ## Section 15.4: Cayley placement of every real ratio -/

/-- **§15.4.** For real `z ≠ −1`, `|Γ(z)| < 1` if and only if `z > 0`; a negative ratio
leaves the disk, and `z = 0` sits at `Γ = −1`. -/
theorem cayley_placement (z : ℝ) (hz : z ≠ -1) :
    (|(z - 1) / (z + 1)| < 1 ↔ 0 < z) ∧
      (z < 0 → 1 < |(z - 1) / (z + 1)|) ∧
      (z = 0 → (z - 1) / (z + 1) = -1) := by
  have hz1 : z + 1 ≠ 0 := by
    intro h
    exact hz (by linarith)
  refine ⟨?_, fun hz0 => negative_ratio_leaves_disk z hz0 hz1, fun hz0 => by simp [hz0]⟩
  have hden : 0 < |z + 1| := abs_pos.mpr hz1
  rw [abs_div, div_lt_one hden, ← sq_lt_sq]
  constructor <;> intro h <;> nlinarith

/-- **§15.4.** As `z → −1`, `|Γ(z)| → ∞`. -/
theorem cayley_pole :
    Filter.Tendsto (fun z : ℝ => |(z - 1) / (z + 1)|)
      (nhdsWithin (-1) {z | z ≠ -1}) Filter.atTop := by
  rw [Filter.tendsto_atTop]
  intro M
  let δ : ℝ := 1 / (max M 1 + 1)
  have hδ : 0 < δ := by positivity
  rw [eventually_nhdsWithin_iff, Metric.eventually_nhds_iff]
  refine ⟨δ, hδ, ?_⟩
  intro z hz hne
  have hclose : |z + 1| < δ := by
    simpa [Real.dist_eq] using hz
  have hne1 : z + 1 ≠ 0 := by
    intro h
    exact hne (by linarith)
  have hpos : 0 < |z + 1| := abs_pos.mpr hne1
  have hδ1 : δ < 1 := by
    unfold δ
    rw [div_lt_one (by positivity)]
    linarith [le_max_right M (1 : ℝ)]
  have hlower : 1 < |z - 1| := by
    have htri : (2 : ℝ) - |z + 1| ≤ |2 - (z + 1)| := by
      simpa using abs_sub_abs_le_abs_sub (2 : ℝ) (z + 1)
    have : |2 - (z + 1)| = |z - 1| := by
      rw [show (2 - (z + 1) : ℝ) = -(z - 1) by ring, abs_neg]
    linarith [hclose, hδ1]
  have hbig : 1 / δ < |z - 1| / |z + 1| := by
    rw [lt_div_iff₀ hpos, one_div, inv_mul_lt_iff₀ hδ]
    nlinarith
  have hM : M < 1 / δ := by
    unfold δ
    rw [one_div_div]
    linarith [le_max_left M (1 : ℝ)]
  rw [abs_div]
  linarith

/-! ## Section 15.11: Thomas–Fermi peel -/

/-- The Thomas–Fermi ratio `((k+1)/k)^{4/3}`. -/
noncomputable def tfZ (k : ℝ) : ℝ := ((k + 1) / k) ^ ((4 : ℝ) / 3)

/-- **§15.11.** `Γ_k = tanh(⅔ ln((k+1)/k)) = ((k+1)^{4/3} − k^{4/3})/((k+1)^{4/3} + k^{4/3})`. -/
theorem thomas_fermi_peel (k : ℝ) (hk : 1 ≤ k) :
    (tfZ k - 1) / (tfZ k + 1) = tanh ((2 / 3) * log ((k + 1) / k)) ∧
      (tfZ k - 1) / (tfZ k + 1) =
        ((k + 1) ^ ((4 : ℝ) / 3) - k ^ ((4 : ℝ) / 3)) /
          ((k + 1) ^ ((4 : ℝ) / 3) + k ^ ((4 : ℝ) / 3)) := by
  have hk0 : 0 < k := by linarith
  have hratio : 0 < (k + 1) / k := div_pos (by linarith) hk0
  have hz : 0 < tfZ k := Real.rpow_pos_of_pos hratio _
  refine ⟨?_, ?_⟩
  · have hlog : log (tfZ k) / 2 = (2 / 3) * log ((k + 1) / k) := by
      unfold tfZ
      rw [Real.log_rpow hratio]
      ring
    rw [← hlog, smith_identity _ hz]
  · unfold tfZ
    have hdiv : ((k + 1) / k) ^ ((4 : ℝ) / 3) =
        (k + 1) ^ ((4 : ℝ) / 3) / k ^ ((4 : ℝ) / 3) :=
      Real.div_rpow (by linarith) hk0.le _
    have hkp : 0 < k ^ ((4 : ℝ) / 3) := Real.rpow_pos_of_pos hk0 _
    rw [hdiv]
    field_simp [hkp.ne']

/-! ## §20.3.1: frequency ratios carry the same Γ -/

/-- **§20.3.1.** Dividing two positive energies by `h > 0` does not change `Γ`,
and that coordinate is `tanh(½ ln(f_{q+1}/f_q))`. -/
theorem gamma_of_frequency (h Iq Iq1 : ℝ) (hh : 0 < h) (hi : 0 < Iq) (hs : Iq < Iq1) :
    (Iq1 - Iq) / (Iq1 + Iq) =
        ((Iq1 / h) - Iq / h) / ((Iq1 / h) + Iq / h) ∧
      (Iq1 - Iq) / (Iq1 + Iq) =
        tanh (log ((Iq1 / h) / (Iq / h)) / 2) := by
  have h1 : 0 < Iq1 := by linarith
  have hz : 0 < (Iq1 / h) / (Iq / h) := by positivity
  constructor
  · field_simp [hh.ne', hi.ne', h1.ne']
  · rw [← smith_identity _ hz]
    field_simp [hh.ne', hi.ne', h1.ne']

end VOTKP.Smith
