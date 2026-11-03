/- Exact uniqueness core for the three-charge ideal-equilibrium reduction.
   a and b are positive equilibrium coefficient products, not fitted claims. -/
import Mathlib.Basic.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity

namespace MatterGas
noncomputable def meanCharge (a b x : ℝ) : ℝ := (a*x+2*b)/(x^2+a*x+b)

/-- The denominator of the three-charge population model is strictly positive. -/
theorem meanCharge_den_pos (a b x : ℝ) (ha : 0<a) (hb : 0<b) (hx : 0<x) :
    0 < x^2+a*x+b := by positivity

/-- The mean charge decreases strictly with electron density in this model. -/
theorem meanCharge_strictAnti (a b x y : ℝ) (ha : 0<a) (hb : 0<b)
    (hx : 0<x) (hxy : x<y) : meanCharge a b y < meanCharge a b x := by
  have hy : 0<y := lt_trans hx hxy
  unfold meanCharge
  apply (div_lt_div_iff₀ (meanCharge_den_pos a b y ha hb hy)
    (meanCharge_den_pos a b x ha hb hx)).2
  have hprod : 0 < (y-x)*(a*x*y + 2*b*(x+y)+a*b) := by positivity
  have hfactor : (a*x+2*b)*(y^2+a*y+b) - (a*y+2*b)*(x^2+a*x+b) =
    (y-x)*(a*x*y+2*b*(x+y)+a*b) := by ring
  linarith

/-- At most one positive charge-neutral electron density exists.
Existence and a full Saha/LTE derivation are separate manuscript claims. -/
theorem saha_neutrality_unique (a b N x y : ℝ) (ha : 0<a) (hb : 0<b) (hN : 0<N)
    (hx : 0<x) (hy : 0<y) (hxeq : x = N*meanCharge a b x)
    (hyeq : y = N*meanCharge a b y) : x=y := by
  rcases lt_trichotomy x y with hxy | heq | hyx
  · have h := mul_lt_mul_of_pos_left (meanCharge_strictAnti a b x y ha hb hx hxy) hN
    linarith
  · exact heq
  · have h := mul_lt_mul_of_pos_left (meanCharge_strictAnti a b y x ha hb hy hyx) hN
    linarith

/-- At any positive neutral solution the mean charge is strictly between zero and two. -/
theorem meanCharge_bounds (a b x : ℝ) (ha : 0<a) (hb : 0<b) (hx : 0<x) :
    0 < meanCharge a b x ∧ meanCharge a b x < 2 := by
  have hd := meanCharge_den_pos a b x ha hb hx
  unfold meanCharge
  constructor
  · positivity
  · apply (div_lt_iff₀ hd).2
    have hx2 : 0 < x^2 := sq_pos_of_pos hx
    have hax := mul_pos ha hx
    nlinarith

/-- Adjacent population ratios cancel electron density in their quotient. -/
theorem saha_ratio_cancellation (n0 n1 n2 x S0 S1 : ℝ)
    (hn0 : n0 ≠ 0) (hn1 : n1 ≠ 0) (hx : x ≠ 0) (hS0 : S0 ≠ 0)
    (h01 : n1/n0 = S0/x) (h12 : n2/n1 = S1/x) :
    n0*n2/n1^2 = S1/S0 := by
  have h01' := (div_eq_iff hn0).mp h01
  have h12' := (div_eq_iff hn1).mp h12
  rw [h12', h01']
  field_simp [hn0, hx, hS0]

/-- The product of adjacent population ratios supplies the absolute product channel. -/
theorem saha_product_cancellation (n0 n1 n2 x S0 S1 : ℝ)
    (hn0 : n0 ≠ 0) (hn1 : n1 ≠ 0) (hx : x ≠ 0) (hS0 : S0 ≠ 0) (hS1 : S1 ≠ 0)
    (h01 : n1/n0 = S0/x) (h12 : n2/n1 = S1/x) :
    n0/(n2*x^2) = 1/(S0*S1) := by
  have h01' := (div_eq_iff hn0).mp h01
  have h12' := (div_eq_iff hn1).mp h12
  rw [h12', h01']
  field_simp [hn0, hx, hS0, hS1]

end MatterGas
