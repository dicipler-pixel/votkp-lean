/- An exact positive four-velocity witness. It proves finite moment statements,
   not a kinetic equation or an experimental prediction. -/
import Mathlib.Basic.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

namespace MatterGas

/-- Four-velocity moment with support (-3,-1,1,3). -/
def fourMoment (w0 w1 w2 w3 : ℝ) (k : ℕ) : ℝ :=
  w0*(-3)^k + w1*(-1)^k + w2*1^k + w3*3^k

/-- The finite-difference null vector annihilates every quadratic polynomial. -/
theorem quadratic_moment_null (a b c : ℝ) :
    -(a*(-3)^2+b*(-3)+c) + 3*(a*(-1)^2+b*(-1)+c)
      - 3*(a*1^2+b*1+c) + (a*3^2+b*3+c) = 0 := by ring

/-- Both distributions have mass one and strictly positive weights. -/
theorem four_moment_weights :
    (1/4:ℝ)+(1/4)+(1/4)+(1/4)=1 ∧
    (7/32:ℝ)+(11/32)+(5/32)+(9/32)=1 ∧
    (0:ℝ)<7/32 ∧ (0:ℝ)<11/32 ∧ (0:ℝ)<5/32 ∧ (0:ℝ)<9/32 := by norm_num

/-- Exact equal zeroth moment. -/
theorem four_moment_zero :
    fourMoment (1/4) (1/4) (1/4) (1/4) 0 =
    fourMoment (7/32) (11/32) (5/32) (9/32) 0 := by norm_num [fourMoment]

/-- Exact equal first moment (zero mean velocity). -/
theorem four_moment_one :
    fourMoment (1/4) (1/4) (1/4) (1/4) 1 =
    fourMoment (7/32) (11/32) (5/32) (9/32) 1 := by norm_num [fourMoment]

/-- Exact equal second moment (the value is five). -/
theorem four_moment_two :
    fourMoment (1/4) (1/4) (1/4) (1/4) 2 = 5 ∧
    fourMoment (7/32) (11/32) (5/32) (9/32) 2 = 5 := by norm_num [fourMoment]

/-- The equal low-moment records do not determine the third moment. -/
theorem four_moment_three_separation :
    fourMoment (7/32) (11/32) (5/32) (9/32) 3 -
    fourMoment (1/4) (1/4) (1/4) (1/4) 3 = (3/2:ℝ) := by norm_num [fourMoment]

end MatterGas
