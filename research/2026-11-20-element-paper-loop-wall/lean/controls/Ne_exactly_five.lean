import LoopWall
-- False control: must be rejected.
theorem Ne_exactly_five : (1195.8082 / 239.0970 : Rat) = 5 := by
  first | (unfold outside inside Icore Ival; grind) | decide +kernel | grind
