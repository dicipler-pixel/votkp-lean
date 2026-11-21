import VOTKP.Smith
-- False: at z = -99/100, |Γ| = 199, which is not < 2.
example : |((-99 / 100 : ℝ) - 1) / (-99 / 100 + 1)| < 2 := by norm_num
