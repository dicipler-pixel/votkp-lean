import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Data.Finset.Max
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

/-! Relative log profiles, with the common scale chosen to minimize the
largest residual. The finite index set may have any positive cardinality. -/

namespace PeelProfile

variable {ι : Type*} (s : Finset ι) (hs : s.Nonempty)

noncomputable def worst (u : ι → ℝ) (t : ℝ) : ℝ :=
  s.sup' hs (fun i => |u i - t|)

noncomputable def middle (u : ι → ℝ) : ℝ := (s.inf' hs u + s.sup' hs u) / 2

noncomputable def radius (u : ι → ℝ) : ℝ := (s.sup' hs u - s.inf' hs u) / 2

/-- Every coordinate is within r of t precisely when the two endpoints are. -/
theorem worst_le_iff (u : ι → ℝ) (t r : ℝ) :
    worst s hs u t ≤ r ↔ s.sup' hs u - r ≤ t ∧ t ≤ s.inf' hs u + r := by
  rw [worst, Finset.sup'_le_iff]
  constructor
  · intro h
    obtain ⟨i, hi, himax⟩ := s.exists_mem_eq_sup' hs u
    obtain ⟨j, hj, hjmin⟩ := s.exists_mem_eq_inf' hs u
    have h₁ := (abs_le.mp (h i hi)).2
    have h₂ := (abs_le.mp (h j hj)).1
    constructor <;> linarith
  · rintro ⟨hmax, hmin⟩ i hi
    have h₁ := s.inf'_le u hi
    have h₂ := s.le_sup' u hi
    exact abs_le.mpr ⟨by linarith, by linarith⟩

theorem radius_le_worst (u : ι → ℝ) (t : ℝ) : radius s hs u ≤ worst s hs u t := by
  have h := (worst_le_iff s hs u t _).mp le_rfl
  unfold radius
  linarith [h.1, h.2]

/-- The midpoint attains the minimum, including when all coordinates coincide. -/
theorem midpoint_attains (u : ι → ℝ) : worst s hs u (middle s hs u) = radius s hs u := by
  apply le_antisymm _ (radius_le_worst s hs u _)
  apply (worst_le_iff s hs u _ _).mpr
  unfold radius middle
  constructor <;> linarith

theorem only_midpoint_attains (u : ι → ℝ) (t : ℝ)
    (h : worst s hs u t = radius s hs u) : t = middle s hs u := by
  have hh := (worst_le_iff s hs u _ _).mp h.le
  unfold radius at hh
  unfold middle
  linarith [hh.1, hh.2]

/-- The exact excess over the optimal error equals the absolute shift from the midpoint. -/
theorem worst_eq_radius_add_offset (u : ι → ℝ) (t : ℝ) :
    worst s hs u t = radius s hs u + |t - middle s hs u| := by
  have h := (worst_le_iff s hs u t _).mp le_rfl
  apply le_antisymm
  · apply (worst_le_iff s hs u t _).mpr
    unfold radius middle
    have hp := le_abs_self (t - (s.inf' hs u + s.sup' hs u) / 2)
    have hn := neg_le_abs (t - (s.inf' hs u + s.sup' hs u) / 2)
    constructor <;> linarith
  · unfold radius middle
    by_cases ht : 0 ≤ t - (s.inf' hs u + s.sup' hs u) / 2
    · rw [abs_of_nonneg ht]
      linarith [h.2]
    · rw [abs_of_neg (lt_of_not_ge ht)]
      linarith [h.1]

/-- One common positive multiplier is fitted to all coordinates of the second profile. -/
noncomputable def scaledError (x y : ι → ℝ) (a : ℝ) : ℝ :=
  s.sup' hs (fun i => |Real.log (x i / (a * y i))|)

noncomputable def logRatios (x y : ι → ℝ) (i : ι) : ℝ := Real.log (x i / y i)

theorem scaledError_eq_worst (x y : ι → ℝ)
    (hx : ∀ i ∈ s, 0 < x i) (hy : ∀ i ∈ s, 0 < y i) {a : ℝ} (ha : 0 < a) :
    scaledError s hs x y a = worst s hs (logRatios x y) (Real.log a) := by
  unfold scaledError worst logRatios
  apply Finset.sup'_congr hs rfl
  intro i hi
  rw [Real.log_div (hx i hi).ne' (mul_pos ha (hy i hi)).ne',
      Real.log_mul ha.ne' (hy i hi).ne', Real.log_div (hx i hi).ne' (hy i hi).ne']
  congr 1
  linarith

/-- The actual error at the positive scale exp(midpoint) equals half the range. -/
theorem optimal_positive_scale (x y : ι → ℝ)
    (hx : ∀ i ∈ s, 0 < x i) (hy : ∀ i ∈ s, 0 < y i) :
    scaledError s hs x y (Real.exp (middle s hs (logRatios x y))) =
      radius s hs (logRatios x y) := by
  rw [scaledError_eq_worst s hs x y hx hy (Real.exp_pos _), Real.log_exp, midpoint_attains]

/-- The maximum is a nonempty finite supremum. IsLeast states a true attained minimum. -/
theorem finite_profile_minimax (x y : ι → ℝ)
    (hx : ∀ i ∈ s, 0 < x i) (hy : ∀ i ∈ s, 0 < y i) :
    IsLeast {r : ℝ | ∃ a : ℝ, 0 < a ∧ scaledError s hs x y a = r}
      (radius s hs (logRatios x y)) := by
  constructor
  · exact ⟨_, Real.exp_pos _, optimal_positive_scale s hs x y hx hy⟩
  · rintro r ⟨a, ha, rfl⟩
    rw [scaledError_eq_worst s hs x y hx hy ha]
    exact radius_le_worst s hs _ _


/-- The optimizing positive multiplier is unique, also for a singleton or a constant profile. -/
theorem unique_positive_scale (x y : ι → ℝ)
    (hx : ∀ i ∈ s, 0 < x i) (hy : ∀ i ∈ s, 0 < y i) {a : ℝ} (ha : 0 < a)
    (he : scaledError s hs x y a = radius s hs (logRatios x y)) :
    a = Real.exp (middle s hs (logRatios x y)) := by
  rw [scaledError_eq_worst s hs x y hx hy ha] at he
  rw [← Real.exp_log ha]
  exact congrArg Real.exp (only_midpoint_attains s hs _ _ he)

/-- Scales whose worst error is within ε of optimal form a closed multiplicative band.
This equivalence even holds for ε < 0, when both sides are impossible. -/
theorem positive_scale_tolerance_iff (x y : ι → ℝ)
    (hx : ∀ i ∈ s, 0 < x i) (hy : ∀ i ∈ s, 0 < y i) {a : ℝ} (ha : 0 < a) (ε : ℝ) :
    scaledError s hs x y a ≤ radius s hs (logRatios x y) + ε ↔
      Real.exp (middle s hs (logRatios x y)) * Real.exp (-ε) ≤ a ∧
      a ≤ Real.exp (middle s hs (logRatios x y)) * Real.exp ε := by
  rw [scaledError_eq_worst s hs x y hx hy ha, worst_eq_radius_add_offset,
      add_le_add_iff_left, abs_le, ← Real.exp_add, ← Real.exp_add,
      ← Real.le_log_iff_exp_le ha, ← Real.log_le_iff_le_exp ha]
  constructor <;> rintro ⟨hl, hu⟩ <;> constructor <;> linarith

/-- Squaring every forward energy ratio doubles its log-step coordinate.
The common multiplier one half therefore gives exactly zero mismatch. -/
theorem squared_ratios_zero (z : ι → ℝ) (hz : ∀ i ∈ s, 1 < z i) :
    scaledError s hs (fun i => Real.log (z i)) (fun i => Real.log ((z i)^2)) (1/2) = 0 := by
  have each (i : ι) (hi : i ∈ s) :
      |Real.log (Real.log (z i) / ((1/2) * Real.log ((z i)^2)))| = 0 := by
    rw [Real.log_pow]
    have hlog := Real.log_pos (hz i hi)
    have half : (1/2 : ℝ) * ((2 : ℕ) * Real.log (z i)) = Real.log (z i) := by
      push_cast
      linarith
    rw [half, div_self hlog.ne', Real.log_one, abs_zero]
  unfold scaledError
  obtain ⟨i, hi, he⟩ := s.exists_mem_eq_sup' hs
    (fun i => |Real.log (Real.log (z i) / ((1/2) * Real.log ((z i)^2)))|)
  exact he.trans (each i hi)

/-- The wall control uses exact forward ratios and the rational wall test. -/
theorem squared_ladder_wall_control :
    ((2 - 1) / (2 + 1) : ℚ)^2 < 1/2 ∧
    ((3 - 1) / (3 + 1) : ℚ)^2 < 1/2 ∧
    ((4 - 1) / (4 + 1) : ℚ)^2 < 1/2 ∧
    1/2 < ((9 - 1) / (9 + 1) : ℚ)^2 := by norm_num

end PeelProfile

#print axioms PeelProfile.worst_le_iff
#print axioms PeelProfile.radius_le_worst
#print axioms PeelProfile.midpoint_attains
#print axioms PeelProfile.only_midpoint_attains
#print axioms PeelProfile.worst_eq_radius_add_offset
#print axioms PeelProfile.scaledError_eq_worst
#print axioms PeelProfile.optimal_positive_scale
#print axioms PeelProfile.finite_profile_minimax
#print axioms PeelProfile.unique_positive_scale
#print axioms PeelProfile.positive_scale_tolerance_iff
#print axioms PeelProfile.squared_ratios_zero
#print axioms PeelProfile.squared_ladder_wall_control
