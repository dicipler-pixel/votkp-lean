import VOTKP.Energy
-- False: the one-step reconstruction of 3 from the anchor 2 is not 4.
example : (2 : ℝ) * (1 + (3 - 2) / (3 + 2)) / (1 - (3 - 2) / (3 + 2)) = 4 := by norm_num
