import LoopWall
-- False control: must be rejected.
theorem F_rung0_outside : outside (17.42282 / 3.4011898) := by
  first | (unfold outside inside Icore Ival; grind) | decide +kernel | grind
