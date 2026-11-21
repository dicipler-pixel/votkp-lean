import LoopWall
-- False control: must be rejected.
theorem Mg_L_outside : outside (80.1436 / 15.035271) := by
  first | (unfold outside; grind) | decide +kernel | grind
