import VOTKP.Smith
-- Deliberately false: the first shell wall (n = 2) reflects 3/5, not 1/2.
example : ((2 : ℝ) * 2 - 1) / (2 ^ 2 + (2 - 1) ^ 2) = 1 / 2 := by
  norm_num
