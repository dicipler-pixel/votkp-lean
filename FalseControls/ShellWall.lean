import VOTKP.Smith
-- Deliberately false: at the first shell wall (n = 2) the shell part, the Smith reflection of
-- the ratio 4, is 3/5, not 1/2.
example : ((2 : ℝ) * 2 - 1) / (2 ^ 2 + (2 - 1) ^ 2) = 1 / 2 := by
  norm_num
