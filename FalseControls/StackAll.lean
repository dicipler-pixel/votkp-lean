import VOTKP.Film
-- False: the one-step stack from 2 to 1 is not the step from 3 to 1.
example : ((2 - 1) / (2 + 1) : ℝ) = (3 - 1) / (3 + 1) := by norm_num
