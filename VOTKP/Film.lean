/-
VOTKP v1.1: the thinning peel of a metal film.

The film reflection is `r = (Γ + x)/(1 + Γx)` with front-surface reflection `Γ` and echo
`x = r₁₂ e^{4πiNd/λ}`.

* Corollary 15.3: `r` is `Γ ⊕ x`, and its derivative at `x = 0` is `1 − Γ²`, the first-order
  echo coefficient of Theorem 6.1.
* Theorem 6.1: for `|Γx| < 1`, `Σ_{m≥1} (−Γ)^{m−1} x^m = x/(1 + Γx)`, and
  `Γ + (1 − Γ²) x/(1 + Γx) = r`, so `r = Γ + (1 − Γ²) Σ (−Γ)^{m−1} x^m`.
* Theorem 6.2: `|r|² − |a|² = ((1 − |a|⁴)|x|² + 2 Re[ā(1 − a²)x]) / |1 + ax|²`; with
  `A = 1 − |a|⁴ > 0` and `C = ā(1 − a²)`, the film reflects more than its bulk exactly when
  `|x − x_c| > |x_c|` with `x_c = −C̄/A`: outside one circle through the origin.
* Consequence 2 of Theorem 6.2: one radius cannot decide. With `a = 1/2`, the echo `x = 1/5`
  gives `R = 49/121 > 1/4` and `x = −1/5` gives `R = 1/9 < 1/4`.
* Section 15.2: at zero phase a stack telescopes,
  `r₀₁ ⊕ r₁₂ = r₀₂` with `rᵢⱼ = (Nᵢ − Nⱼ)/(Nᵢ + Nⱼ) = tanh(½ ln(Nᵢ/Nⱼ))`, so the inner layer
  drops out.
-/
import VOTKP.Smith

namespace VOTKP.Film

open Complex VOTKP.Smith

/-! ## Corollary 15.3 and Theorem 6.1 -/

/-- The film reflection is `Γ ⊕ x`. -/
theorem film_is_oplus (g x : ℂ) : (g + x) / (1 + g * x) = oplus g x := rfl

/-- **Corollary 15.3.** The first-order echo coefficient is the derivative of `Γ ⊕ x` at
`x = 0`, namely `1 − Γ²`. -/
theorem echo_derivative (g : ℂ) :
    HasDerivAt (fun x : ℂ => (g + x) / (1 + g * x)) (1 - g * g) 0 := by
  have h1 : HasDerivAt (fun x : ℂ => g + x) 1 0 := (hasDerivAt_id (0 : ℂ)).const_add g
  have h2 : HasDerivAt (fun x : ℂ => 1 + g * x) (g * 1) 0 :=
    ((hasDerivAt_id (0 : ℂ)).const_mul g).const_add 1
  have h := h1.div h2 (by simp)
  exact h.congr_deriv (by simp; try ring)

/-- **Theorem 6.1, the series.** For `‖Γx‖ < 1`, `Σ_{m≥0} (−Γ)^m x^{m+1} = x/(1 + Γx)`. -/
theorem echo_series (g x : ℂ) (h : ‖g * x‖ < 1) :
    HasSum (fun m : ℕ => (-g) ^ m * x ^ (m + 1)) (x / (1 + g * x)) := by
  have hg : ‖-(g * x)‖ < 1 := by rwa [norm_neg]
  have hs := (hasSum_geometric_of_norm_lt_one hg).mul_left x
  convert hs using 1
  · funext m
    rw [show -(g * x) = (-g) * x by ring, mul_pow, pow_succ]
    ring
  · rw [sub_neg_eq_add, div_eq_mul_inv]

/-- **Theorem 6.1, the sum.** `Γ + (1 − Γ²) · x/(1 + Γx) = (Γ + x)/(1 + Γx)`. -/
theorem echo_resum (g x : ℂ) (h : 1 + g * x ≠ 0) :
    g + (1 - g * g) * (x / (1 + g * x)) = (g + x) / (1 + g * x) := by
  field_simp
  ring

/-! ## Theorem 6.2: the exact boundary is a circle -/

/-- **Theorem 6.2.** `|r|² − |a|² = ((1 − |a|⁴)|x|² + 2 Re[ā(1 − a²)x]) / |1 + ax|²`. -/
theorem echo_circle (a x : ℂ) (h : 1 + a * x ≠ 0) :
    normSq ((a + x) / (1 + a * x)) - normSq a =
      ((1 - normSq a ^ 2) * normSq x + 2 * ((starRingEnd ℂ) a * (1 - a * a) * x).re) /
        normSq (1 + a * x) := by
  have hn : normSq (1 + a * x) ≠ 0 := by
    intro h0; exact h (normSq_eq_zero.mp h0)
  rw [normSq_div, eq_div_iff hn, sub_mul, div_mul_cancel₀ _ hn]
  simp only [normSq_apply, add_re, add_im, mul_re, mul_im, one_re, one_im, sub_re, sub_im,
    conj_re, conj_im]
  ring

/-- The centre of the circle, `x_c = −C̄/A`, written out in coordinates. -/
noncomputable def centre (A : ℝ) (C : ℂ) : ℂ := ⟨-C.re / A, C.im / A⟩

theorem centre_eq (A : ℝ) (hA : A ≠ 0) (C : ℂ) :
    centre A C = -(starRingEnd ℂ) C / (A : ℂ) := by
  apply Complex.ext <;> simp [centre, div_ofReal_re, div_ofReal_im] <;> field_simp

/-- The circle identity: `A(|x − x_c|² − |x_c|²) = A|x|² + 2 Re(Cx)`. -/
theorem circle_identity (A : ℝ) (hA : A ≠ 0) (C x : ℂ) :
    A * (normSq (x - centre A C) - normSq (centre A C)) = A * normSq x + 2 * (C * x).re := by
  simp only [centre, normSq_apply, sub_re, sub_im, mul_re, mul_im]
  field_simp
  ring

/-- **Theorem 6.2, the criterion.** For `A > 0`, `A|x|² + 2 Re(Cx) > 0` exactly when `x` lies
outside the circle `|x − x_c| = |x_c|`, which passes through the origin. The combined statement,
with `A = 1 − |a|⁴` and `C = ā(1 − a²)`, is `echo_outside_iff`. -/
theorem circle_criterion (A : ℝ) (hA : 0 < A) (C x : ℂ) :
    0 < A * normSq x + 2 * (C * x).re ↔ normSq (centre A C) < normSq (x - centre A C) := by
  rw [← circle_identity A hA.ne' C x]
  constructor
  · intro h
    by_contra hc
    push_neg at hc
    nlinarith
  · intro h
    exact mul_pos hA (by linarith)

/-- `A = 1 − |a|⁴`, the numerator coefficient of Theorem 6.2. -/
noncomputable def echoA (a : ℂ) : ℝ := 1 - normSq a ^ 2

/-- `C = ā(1 − a²)`, the linear coefficient of Theorem 6.2. -/
noncomputable def echoC (a : ℂ) : ℂ := (starRingEnd ℂ) a * (1 - a * a)

/-- **Theorem 6.2.** `|a| < 1` forces `A = 1 − |a|⁴ > 0`. -/
theorem echo_amplitude_pos (a : ℂ) (ha : ‖a‖ < 1) : 0 < echoA a := by
  have hsq : normSq a = ‖a‖ ^ 2 := normSq_eq_norm_sq a
  have h1 : ‖a‖ ^ 2 < 1 := by
    have hn : 0 ≤ ‖a‖ := norm_nonneg a
    nlinarith
  have h2 : (‖a‖ ^ 2) ^ 2 < 1 := by
    have hn : 0 ≤ ‖a‖ ^ 2 := sq_nonneg _
    nlinarith
  rw [echoA, hsq]
  linarith

lemma normSq_one_add_mul (a x : ℂ) :
    normSq (1 + a * x) = 1 + normSq a * normSq x + 2 * (a * x).re := by
  rw [normSq_add, normSq_one, normSq_mul, one_mul, Complex.conj_re]

lemma echo_threshold_algebra (a x : ℂ) (ε : ℝ) :
    (1 - normSq a ^ 2) * normSq x + 2 * ((starRingEnd ℂ) a * (1 - a * a) * x).re -
        ε * (1 + normSq a * normSq x + 2 * (a * x).re) =
      (echoA a - ε * normSq a) * normSq x + 2 * ((echoC a - (ε : ℂ) * a) * x).re - ε := by
  have hlin : ((echoC a - (ε : ℂ) * a) * x).re = (echoC a * x).re - ε * (a * x).re := by
    simp [Complex.sub_re, Complex.mul_re, Complex.ofReal_re, Complex.ofReal_im]
    ring
  simp only [echoA, echoC] at hlin ⊢
  rw [hlin]
  ring

/-- **Theorem 6.2.** For `|a| < 1` and `1 + ax ≠ 0`, the film reflects more than its bulk
exactly outside the circle through the origin with centre `x_c = −C̄/A`. -/
theorem echo_outside_iff (a x : ℂ) (ha : ‖a‖ < 1) (h : 1 + a * x ≠ 0) :
    normSq a < normSq ((a + x) / (1 + a * x)) ↔
      normSq (centre (echoA a) (echoC a)) < normSq (x - centre (echoA a) (echoC a)) := by
  have hA : 0 < echoA a := echo_amplitude_pos a ha
  have hden : 0 < normSq (1 + a * x) := (normSq_pos).mpr h
  rw [← sub_pos, echo_circle a x h, lt_div_iff₀ hden, zero_mul]
  simpa [echoA, echoC] using (circle_criterion (echoA a) hA (echoC a) x)

/-- **Theorem 6.2, detection threshold.** For `ε > 0` and `1 + ax ≠ 0`,
`|r|² − |a|² > ε` if and only if `(A − ε|a|²)|x|² + 2 Re[(C − ε a)x] − ε > 0`. -/
theorem echo_threshold (a x : ℂ) (ε : ℝ) (hε : 0 < ε) (h : 1 + a * x ≠ 0) :
    ε < normSq ((a + x) / (1 + a * x)) - normSq a ↔
      0 < (echoA a - ε * normSq a) * normSq x +
        2 * ((echoC a - (ε : ℂ) * a) * x).re - ε := by
  have hden : 0 < normSq (1 + a * x) := (normSq_pos).mpr h
  have _ := hε
  rw [echo_circle a x h, lt_div_iff₀ hden, normSq_one_add_mul, ← sub_pos, echo_threshold_algebra]

/-- The circle passes through the origin: `|0 − x_c| = |x_c|`. -/
theorem circle_through_origin (A : ℝ) (C : ℂ) :
    normSq (0 - centre A C) = normSq (centre A C) := by
  rw [zero_sub, normSq_neg]

/-- **One radius cannot decide.** With `a = 1/2`, the echo `x = 1/5` raises the reflectance
to `49/121 > 1/4` and `x = −1/5` lowers it to `1/9 < 1/4`. -/
theorem one_radius_cannot_decide :
    ((1 / 2 + 1 / 5) / (1 + 1 / 2 * (1 / 5)) : ℝ) ^ 2 = 49 / 121 ∧ (1 / 2 : ℝ) ^ 2 < 49 / 121 ∧
      ((1 / 2 - 1 / 5) / (1 - 1 / 2 * (1 / 5)) : ℝ) ^ 2 = 1 / 9 ∧ (1 / 9 : ℝ) < (1 / 2) ^ 2 := by
  norm_num

/-! ## Section 15.2: the zero-phase stack telescopes -/

/-- The interface reflection is the Smith coordinate of the index ratio. -/
theorem interface_smith (Ni Nj : ℝ) (hi : 0 < Ni) (hj : 0 < Nj) :
    (Ni - Nj) / (Ni + Nj) = Real.tanh (Real.log (Ni / Nj) / 2) := by
  rw [← smith_identity _ (div_pos hi hj)]
  have : Nj ≠ 0 := hj.ne'
  have : Ni + Nj ≠ 0 := by linarith
  field_simp

/-- **Zero phase.** `r₀₁ ⊕ r₁₂ = r₀₂`: the inner layer drops out. -/
theorem stack_telescopes (N0 N1 N2 : ℝ) (h0 : 0 < N0) (h1 : 0 < N1) (h2 : 0 < N2) :
    oplus ((N0 - N1) / (N0 + N1)) ((N1 - N2) / (N1 + N2)) = (N0 - N2) / (N0 + N2) := by
  have a : N0 + N1 ≠ 0 := by linarith
  have b : N1 + N2 ≠ 0 := by linarith
  have c : (N0 + N1) * (N1 + N2) ≠ 0 := mul_ne_zero a b
  have d : (N0 + N1) * (N1 + N2) + (N0 - N1) * (N1 - N2) ≠ 0 := by
    rw [show (N0 + N1) * (N1 + N2) + (N0 - N1) * (N1 - N2) = 2 * N1 * (N0 + N2) by ring]
    positivity
  have e : N0 + N2 ≠ 0 := by linarith
  unfold oplus
  rw [div_add_div _ _ a b, div_mul_div_comm, one_add_div c, div_div_div_cancel_right₀ c,
    div_eq_div_iff d e]
  ring

/-- Interface reflection of two positive indices. -/
noncomputable def interfaceΓ (Ni Nj : ℝ) : ℝ := (Ni - Nj) / (Ni + Nj)

/-- The zero-phase stack of the first `n` interfaces, `r₀₁ ⊕ ⋯ ⊕ r_{n-1,n}`. -/
noncomputable def stackΓ (N : ℕ → ℝ) : ℕ → ℝ
  | 0 => 0
  | n + 1 => oplus (stackΓ N n) (interfaceΓ (N n) (N (n + 1)))

/-- **§15.2.** For positive real indices the zero-phase stack of `n` interfaces telescopes:
`r₀₁ ⊕ ⋯ ⊕ r_{n-1,n} = (N₀ − Nₙ)/(N₀ + Nₙ) = tanh(½ ln(N₀/Nₙ))`.
Absorbing complex indices are not part of this statement. -/
theorem stack_telescopes_n (N : ℕ → ℝ) (hN : ∀ j, 0 < N j) (n : ℕ) :
    stackΓ N n = (N 0 - N n) / (N 0 + N n) ∧
      stackΓ N n = Real.tanh (Real.log (N 0 / N n) / 2) := by
  induction n with
  | zero =>
    constructor
    · simp [stackΓ]
    · rw [stackΓ, div_self (hN 0).ne', Real.log_one, zero_div, Real.tanh_zero]
  | succ n ih =>
    have hstep := stack_telescopes (N 0) (N n) (N (n + 1)) (hN 0) (hN n) (hN (n + 1))
    have hfrac : stackΓ N (n + 1) = (N 0 - N (n + 1)) / (N 0 + N (n + 1)) := by
      simpa [stackΓ, interfaceΓ, ih.1] using hstep
    exact ⟨hfrac, hfrac.trans (interface_smith _ _ (hN 0) (hN (n + 1)))⟩

end VOTKP.Film
