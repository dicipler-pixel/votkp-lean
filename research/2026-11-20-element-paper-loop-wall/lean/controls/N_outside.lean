import LoopWall
-- False control: must be rejected.
theorem N_outside : outside (552.06741 / 97.8901) := by
  first | (unfold outside inside Icore Ival; grind) | decide +kernel | grind
