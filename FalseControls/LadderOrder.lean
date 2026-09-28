import VOTKP.Smith
-- Deliberately false: the ladders 1, 2, 6 and 1, 3, 6 share a composite but not their first
-- step (1/3 against 1/2).
example : ((2 : ℝ) - 1) / (2 + 1) = (3 - 1) / (3 + 1) := by
  norm_num
