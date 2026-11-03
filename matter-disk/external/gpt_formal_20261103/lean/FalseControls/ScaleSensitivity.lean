/- Intentionally false assertion: this file MUST fail elaboration. -/
import MatterGas

example : MatterGas.gamma (2*1) (2*3) ≠ MatterGas.gamma 1 3 := by
  norm_num [MatterGas.gamma]
