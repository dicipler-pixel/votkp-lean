import VOTKP.Film
-- False: |a| = 1/2 gives A = 1 - |a|⁴ = 15/16, which is not ≤ 0.
example : (1 - ((1 / 2 : ℝ) ^ 2) ^ 2) ≤ 0 := by norm_num
