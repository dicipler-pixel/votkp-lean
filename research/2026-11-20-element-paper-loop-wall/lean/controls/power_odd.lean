import LoopWall
-- False control: must be rejected.
theorem power_odd : ∀ z : Rat, 0 < z → gam (1 / z) * gam (1 / z) = - (gam z * gam z) := by
  first | (unfold outside inside Icore Ival; grind) | decide +kernel | grind
