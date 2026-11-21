import LoopWall
-- False control: must be rejected.
theorem Ca_M_outside : outside (50.91316 / 11.871719) := by
  first | (unfold outside; grind) | decide +kernel | grind
