import VOTKP.Film
-- False: a = 1/2, x = -1/5 lowers the reflectance below the bulk value.
example : ((1 / 2 : ℝ) ^ 2) < ((1 / 2 - 1 / 5) / (1 - (1 / 2) * (1 / 5))) ^ 2 := by norm_num
