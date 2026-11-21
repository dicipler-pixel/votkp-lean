import Std

namespace VOTKP.ScreeningArea

/-- Cleared tangent inequality for f(x)=x/(1+x), before putting m equal to a mean. -/
theorem tangent_remainder (x m : Rat) :
    m*(1+m)*(1+x) + (x-m)*(1+x) - x*(1+m)^2 = (x-m)^2 := by grind

/-- The exact finite two-point Jensen gap, multiplied by its three positive denominators. -/
theorem two_point_gap (x y p : Rat) :
    let m := p*x+(1-p)*y
    m*(1+x)*(1+y)-(1+m)*(p*x*(1+y)+(1-p)*y*(1+x))
      = p*(1-p)*(x-y)^2 := by dsimp; grind

theorem two_point_concavity (x y p : Rat) (hl : 0 ≤ p) (hu : p ≤ 1) :
    let m := p*x+(1-p)*y
    0 ≤ m*(1+x)*(1+y)-(1+m)*(p*x*(1+y)+(1-p)*y*(1+x)) := by
  dsimp
  rw [two_point_gap x y p]
  apply Rat.mul_nonneg (Rat.mul_nonneg hl (by grind))
  by_cases h : 0 ≤ x-y
  · have eq : (x-y)^2 = (x-y)*(x-y) := by grind
    rw [eq]
    exact Rat.mul_nonneg h h
  · have hn : 0 ≤ y-x := by grind
    have eq : (x-y)^2 = (y-x)*(y-x) := by grind
    rw [eq]
    exact Rat.mul_nonneg hn hn

/-- Squaring the positive ratio changes the coefficients of the wall polynomial. -/
theorem square_wall_factor (z : Rat) :
    (z^2)^2-34*z^2+1 = (z^2-6*z+1)*(z^2+6*z+1) := by grind

/-- With positive denominators, successive changes in depolarization factor compose. -/
theorem dressed_composition_cleared (x n d : Rat) :
    (1+n*x)+d*x = 1+(n+d)*x := by grind

theorem sphere_to_long_static_cap (s : Rat) :
    1+s < 3*(1+s/3) := by grind

/-- Uniform shape audit: the complete fitted inverse moment never exhausts its
    static-data allowance under the positive-background hypotheses in the note. -/
theorem shape_inverse_budget (a b s n : Rat) (ha : 0 ≤ a) (hb : 0 ≤ b)
    (hn : 0 ≤ n) (hs : s ≤ a+b) :
    1+n*s ≤ (1+n*a)*(1+n*b) := by
  have hlin := Rat.mul_nonneg hn (show 0 ≤ a+b-s by grind)
  have hquad := Rat.mul_nonneg (Rat.mul_nonneg hn hn) (Rat.mul_nonneg ha hb)
  grind

/-- Necessary cap does not identify threshold opening: a single line at static 36 can open. -/
theorem one_line_six_opens : ((6 : Rat)-1)^2*2 > (6+1)^2 := by decide +kernel

/-- A single line at static 25 stays inside. -/
theorem one_line_five_inside : ((5 : Rat)-1)^2*2 < (5+1)^2 := by decide +kernel

#print axioms tangent_remainder
#print axioms two_point_gap
#print axioms two_point_concavity
#print axioms square_wall_factor
#print axioms dressed_composition_cleared
#print axioms sphere_to_long_static_cap
#print axioms shape_inverse_budget
#print axioms one_line_six_opens
#print axioms one_line_five_inside
end VOTKP.ScreeningArea
