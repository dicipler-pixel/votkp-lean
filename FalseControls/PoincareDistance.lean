import VOTKP.Smith
-- False: w = 1/3 gives (1+w)/(1-w) = 2, not 3.
example : (1 + (1 / 3 : ℝ)) / (1 - 1 / 3) = 3 := by norm_num
