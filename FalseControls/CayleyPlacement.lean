import VOTKP.Smith
-- False: z = 1/2 > 0 lands at |Γ| = 1/3, not outside the disk.
example : (1 : ℝ) ≤ |(1 / 2 - 1) / (1 / 2 + 1)| := by norm_num
