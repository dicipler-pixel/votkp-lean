import LoopWall
-- False control: must be rejected.
theorem screened_seven_outside : outside (Icore 7 / Ival 7) := by
  first | (unfold outside inside Icore Ival; grind) | decide +kernel | grind
