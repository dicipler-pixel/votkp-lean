/- Intentionally false assertion: this file MUST fail elaboration. -/
import MatterGas

example : MatterGas.fourMoment (1/4) (1/4) (1/4) (1/4) 3 =
    MatterGas.fourMoment (7/32) (11/32) (5/32) (9/32) 3 := by
  norm_num [MatterGas.fourMoment]
