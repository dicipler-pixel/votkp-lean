/- Intentionally false assertion: this file MUST fail elaboration. -/
import MatterGas

example : MatterGas.meanCharge 1 1 1 < MatterGas.meanCharge 1 1 2 := by
  norm_num [MatterGas.meanCharge]
