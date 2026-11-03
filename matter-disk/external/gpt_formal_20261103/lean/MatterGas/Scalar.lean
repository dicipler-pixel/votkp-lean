/-
Finite scalar core for Matter, Gases and VOTKP.
Prepared for Jeromie Beasley, 2026-11-03, with AI assistance.
All statements below are algebra/order facts, not empirical laws.
-/
import Mathlib.Basic.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Algebra.Order.BigOperators.Group.Finset

namespace MatterGas

/-- The positive-threshold Cayley coordinate. -/
noncomputable def gamma (a b : ℝ) : ℝ := (b - a) / (b + a)

/-- Positive common rescaling leaves the coordinate unchanged. -/
theorem gamma_scale (a b c : ℝ) (hc : c ≠ 0) :
    gamma (c*a) (c*b) = gamma a b := by
  unfold gamma
  rw [← mul_sub, ← mul_add, mul_div_mul_left _ _ hc]

/-- A positive threshold pair has a coordinate strictly between -1 and 1. -/
theorem gamma_bounds (a b : ℝ) (ha : 0 < a) (hb : 0 < b) :
    -1 < gamma a b ∧ gamma a b < 1 := by
  have hden : 0 < b + a := by linarith
  unfold gamma
  constructor
  · apply (lt_div_iff₀ hden).2
    linarith
  · apply (div_lt_iff₀ hden).2
    linarith

/-- The coordinate together with its positive absolute anchor reconstructs b. -/
theorem gamma_inverse (a b : ℝ) (ha : 0 < a) (hb : 0 < b) :
    (1 + gamma a b) / (1 - gamma a b) = b / a := by
  have ha0 : a ≠ 0 := ne_of_gt ha
  have hden : b+a ≠ 0 := ne_of_gt (add_pos hb ha)
  have hm : 1 - gamma a b ≠ 0 := ne_of_gt (sub_pos.mpr (gamma_bounds a b ha hb).2)
  unfold gamma at hm ⊢
  field_simp [ha0, hden, hm]
  ring_nf
  calc
    a*b*a⁻¹ = b*(a*a⁻¹) := by ring
    _ = b := by rw [mul_inv_cancel₀ ha0, mul_one]

/-- The ratio coordinate alone loses an absolute common scale. -/
theorem gamma_anchor_reconstruction (a b : ℝ) (ha : 0 < a) (hb : 0 < b) :
    a * ((1 + gamma a b) / (1 - gamma a b)) = b := by
  rw [gamma_inverse a b ha hb]
  field_simp [ne_of_gt ha]

/-- Scalar polynomial behind the pure-projector census equivalence. -/
theorem census_factorization (nu eps : ℝ) :
    nu*(1-nu) - eps*(1-eps) = (nu-eps)*(1-eps-nu) := by ring

/-- Threshold equivalence, including endpoints. No spectral theorem is assumed here. -/
theorem census_threshold_iff (nu eps : ℝ) (he : eps < (1:ℝ)/2) :
    eps*(1-eps) ≤ nu*(1-nu) ↔ eps ≤ nu ∧ nu ≤ 1-eps := by
  constructor
  · intro h
    constructor
    · by_contra hn
      have hn' : nu < eps := lt_of_not_ge hn
      have hp : 0 < 1-eps-nu := by linarith
      have hnprod := mul_neg_of_neg_of_pos (sub_neg.mpr hn') hp
      nlinarith [census_factorization nu eps]
    · by_contra hn
      have hn' : 1-eps < nu := lt_of_not_ge hn
      have hp : 0 < nu-eps := by linarith
      have hnprod := mul_neg_of_pos_of_neg hp (by linarith : 1-eps-nu < 0)
      nlinarith [census_factorization nu eps]
  · rintro ⟨hlo,hhi⟩
    have h := mul_nonneg (sub_nonneg.mpr hlo) (by linarith : 0 ≤ 1-eps-nu)
    nlinarith [census_factorization nu eps]

/-- On [0,1] the scalar covariance defect lies in [0,1/4]. -/
theorem scalar_defect_bounds (nu : ℝ) (hlo : 0 ≤ nu) (hhi : nu ≤ 1) :
    0 ≤ nu*(1-nu) ∧ nu*(1-nu) ≤ (1:ℝ)/4 := by
  constructor
  · exact mul_nonneg hlo (sub_nonneg.mpr hhi)
  · nlinarith [sq_nonneg (nu - (1:ℝ)/2)]

/-- A thresholded count is bounded by the sum, for any finite nonnegative list.
This is the scalar counting ingredient; spectral identification is separate. -/
theorem threshold_count_trace_bound {ι : Type*} [Fintype ι]
    (lambda : ι → ℝ) (h : ∀ i, 0 ≤ lambda i) (theta : ℝ) (_ht : 0 < theta) :
    theta * ((Finset.univ.filter (fun i => theta ≤ lambda i)).card : ℝ)
      ≤ ∑ i, lambda i := by
  classical
  calc
    theta * ((Finset.univ.filter (fun i => theta ≤ lambda i)).card : ℝ)
      = ∑ i ∈ Finset.univ.filter (fun i => theta ≤ lambda i), theta := by simp [mul_comm]
    _ ≤ ∑ i ∈ Finset.univ.filter (fun i => theta ≤ lambda i), lambda i := by
      apply Finset.sum_le_sum
      intro i hi
      exact (Finset.mem_filter.mp hi).2
    _ ≤ ∑ i, lambda i := by
      apply Finset.sum_le_sum_of_subset_of_nonneg
      · exact Finset.filter_subset _ _
      · intro i _ _
        exact h i

/-- Raw mixed occupation persists in a disconnected example. -/
theorem disconnected_occupation_witness :
    (0:ℝ) < (3/10:ℝ)*(1-3/10) ∧ (3/10:ℝ)*(1-3/10) = 21/100 := by norm_num

end MatterGas
