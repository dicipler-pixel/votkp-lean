import VOTKP.Peel
-- False: the constant predictor 0 misses the outcomes 0 and 1 by max error 1, not < 1/2.
example : max (|(0 : ℝ) - 0|) (|0 - 1|) < (1 : ℝ) / 2 := by norm_num
