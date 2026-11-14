/-
Two Trees in One Ball (Jeromie Beasley). The peel coordinate against Mathlib's own hyperbolic metric.

`Mathlib.Analysis.Complex.UpperHalfPlane.Metric` puts the Poincaré metric on the upper half plane
`ℍ`. This module reads the peel coordinate of `TwoTrees/Core.lean` in that metric, so the paper's
§2 (VOTKP Theorem 8.1 and Corollary 15.2) is stated against a metric that Mathlib defines, not one
written for the paper.

* `smith_identity`: for `z > 0`, `(z − 1)/(z + 1) = tanh(½ ln z)` (VOTKP Theorem 8.1).
* `dist_I_vert`: the points `i` and `z·i` of `ℍ` are at hyperbolic distance `|ln z|`
  (Corollary 15.2: the peel ratio `z` is a hyperbolic length `ln z`).
* `tanh_half_dist_I_vert`: for `z ≥ 1`, `tanh(d(i, z·i)/2) = (z − 1)/(z + 1)`, the peel coordinate.
* `cosh_dist_I_vert`: `cosh d(i, z·i) = (z² + 1)/(2z)`, the time entry of the boost (Theorem 2.6).
* `dist_I_pow`: `d(i, aⁿ·i) = n ln a` for `a ≥ 1`, the norm ladder as equal steps.
* `gam_eq_tanh_half_dist`, `peel_eq_tanh_half_dist`: the rational `PeelTrees.gam` and
  `PeelTrees.peel` of the core module, cast to `ℝ`, are `tanh` of half the Mathlib distance.
-/
import Mathlib
import TwoTrees.Core

namespace TwoTrees.Smith

open Real

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

/-- **VOTKP Theorem 8.1.** For `z > 0`, `(z − 1)/(z + 1) = tanh(½ ln z)`. -/
theorem smith_identity (z : ℝ) (hz : 0 < z) : (z - 1) / (z + 1) = tanh (log z / 2) := by
  rw [tanh_exp]
  have : 2 * (log z / 2) = log z := by ring
  rw [this, exp_log hz]

/-- The point `z·i` of the upper half plane, for real `z > 0`. -/
noncomputable def vert (z : ℝ) (hz : 0 < z) : UpperHalfPlane :=
  UpperHalfPlane.mk ⟨0, z⟩ hz

/-- **Corollary 15.2, in Mathlib's metric.** The points `i` and `z·i` of `ℍ` are at hyperbolic
distance `|ln z|`. -/
theorem dist_I_vert (z : ℝ) (hz : 0 < z) :
    dist UpperHalfPlane.I (vert z hz) = |Real.log z| := by
  have hre : UpperHalfPlane.I.re = (vert z hz).re := by
    first
    | rfl
    | (rw [UpperHalfPlane.I_re]; rfl)
    | simp [vert]
  refine (UpperHalfPlane.dist_of_re_eq hre).trans ?_
  have h1 : UpperHalfPlane.I.im = 1 := UpperHalfPlane.I_im
  have h2 : (vert z hz).im = z := rfl
  rw [h1, h2, Real.log_one, Real.dist_eq]
  first
  | rw [zero_sub, abs_neg]
  | simp

/-- **VOTKP Theorem 8.1, in Mathlib's metric.** For `z ≥ 1`, the peel coordinate `(z − 1)/(z + 1)`
is `tanh` of half the hyperbolic distance from `i` to `z·i`. -/
theorem tanh_half_dist_I_vert (z : ℝ) (hz : 0 < z) (h1 : 1 ≤ z) :
    Real.tanh (dist UpperHalfPlane.I (vert z hz) / 2) = (z - 1) / (z + 1) := by
  rw [dist_I_vert z hz, abs_of_nonneg (Real.log_nonneg h1)]
  exact (smith_identity z hz).symm

/-- **Theorem 2.6, in Mathlib's metric.** `cosh d(i, z·i) = (z² + 1)/(2z)`, the time entry of the
boost of peel ratio `z`. -/
theorem cosh_dist_I_vert (z : ℝ) (hz : 0 < z) :
    Real.cosh (dist UpperHalfPlane.I (vert z hz)) = (z * z + 1) / (2 * z) := by
  rw [dist_I_vert z hz, Real.cosh_abs, Real.cosh_log hz]
  have hz0 : z ≠ 0 := hz.ne'
  rw [div_eq_div_iff two_ne_zero (mul_ne_zero two_ne_zero hz0)]
  have hzz : z⁻¹ * z = 1 := inv_mul_cancel₀ hz0
  linear_combination 2 * hzz

/-- **The norm ladder as equal steps.** For `a ≥ 1`, the point `aⁿ·i` is at hyperbolic distance
`n ln a` from `i`: each factor of `a` is one step of length `ln a`. -/
theorem dist_I_pow (a : ℝ) (ha : 0 < a) (ha1 : 1 ≤ a) (n : ℕ) :
    dist UpperHalfPlane.I (vert (a ^ n) (pow_pos ha n)) = n * Real.log a := by
  rw [dist_I_vert, Real.log_pow,
    abs_of_nonneg (mul_nonneg (Nat.cast_nonneg n) (Real.log_nonneg ha1))]

/-- **The core peel coordinate is the Mathlib one.** For a rational ratio `z ≥ 1`, the rational
`PeelTrees.gam z` of `TwoTrees/Core.lean`, read in `ℝ`, is `tanh` of half the hyperbolic distance
from `i` to `z·i`. -/
theorem gam_eq_tanh_half_dist (z : ℚ) (h0 : (0 : ℝ) < z) (h1 : 1 ≤ z) :
    Real.tanh (dist UpperHalfPlane.I (vert (z : ℝ) h0) / 2) = ((PeelTrees.gam z : ℚ) : ℝ) := by
  rw [tanh_half_dist_I_vert (z : ℝ) h0 (by exact_mod_cast h1), PeelTrees.gam]
  first
  | (push_cast; done)
  | (norm_cast; done)
  | (simp; done)
  | (norm_num; done)
  | (push_cast; ring1)

/-- **Theorem 2.5, in Mathlib's metric.** After `n` peel steps of ratio 5, the core peel walk
`PeelTrees.peel n` (that is, `n` copies of `2/3` combined by Einstein addition), read in `ℝ`, is
`tanh` of half the hyperbolic distance from `i` to `5ⁿ·i`. -/
theorem peel_eq_tanh_half_dist (n : ℕ) :
    Real.tanh (dist UpperHalfPlane.I (vert ((5 : ℝ) ^ n) (pow_pos (by norm_num) n)) / 2) =
      ((PeelTrees.peel n : ℚ) : ℝ) := by
  rw [tanh_half_dist_I_vert ((5 : ℝ) ^ n) (pow_pos (by norm_num) n) (one_le_pow₀ (by norm_num)),
    PeelTrees.peel_ladder, PeelTrees.gam]
  first
  | (push_cast; done)
  | (norm_cast; done)
  | (simp; done)
  | (norm_num; done)
  | (push_cast; ring1)

end TwoTrees.Smith
