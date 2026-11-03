/- Intentionally false assertion: this file MUST fail elaboration. -/
import MatterGas

example : (3/10:ℝ)*(1-3/10) = 0 := by
  norm_num
