import VOTKP.Film
-- Deliberately false: with a = 1/2 the echo x = −1/5 lowers the reflectance to 1/9; it does
-- not raise it above the bulk value 1/4.
example : (1 / 2 : ℝ) ^ 2 < ((1 / 2 - 1 / 5) / (1 - 1 / 2 * (1 / 5))) ^ 2 := by
  norm_num
