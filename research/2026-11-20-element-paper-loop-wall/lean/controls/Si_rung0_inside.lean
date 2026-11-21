import LoopWall
-- False control: must be rejected.
theorem Si_rung0_inside : inside (8.15168 / 1.3895212) := by
  first | (unfold inside; grind) | decide +kernel | grind
