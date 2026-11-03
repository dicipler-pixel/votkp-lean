/- Intentionally false assertion: this file MUST fail elaboration. -/
import MatterGas

example : (1/2:ℝ)*(1-1/2) ≤ (1/5:ℝ) := by
  norm_num
