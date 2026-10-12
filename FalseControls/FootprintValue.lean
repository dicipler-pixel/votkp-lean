import VOTKP.Channels
-- Deliberately false: for B = (0.7, 0.3i) the coupling footprint BB† is 0.49 + 0.09 = 0.58,
-- not 0.59.
example :
    (!![((7 / 10 : ℝ) : ℂ), ((3 / 10 : ℝ) : ℂ) * Complex.I]
      * (!![((7 / 10 : ℝ) : ℂ), ((3 / 10 : ℝ) : ℂ) * Complex.I])ᴴ) 0 0
      = ((59 / 100 : ℝ) : ℂ) := by
  norm_num [Matrix.mul_apply, Fin.sum_univ_two, Complex.ext_iff]
