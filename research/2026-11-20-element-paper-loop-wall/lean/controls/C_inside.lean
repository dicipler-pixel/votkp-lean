import LoopWall
-- False control: must be rejected.
theorem C_inside : inside (392.09056 / 64.49352) := by
  first | (unfold outside inside Icore Ival; grind) | decide +kernel | grind
