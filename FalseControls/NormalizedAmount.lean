import VOTKP.Colour

open VOTKP.Colour

-- Deliberately false: equal normalized colours do not predict addition of
-- the same absolute amount. The original amounts differ by a factor of 2.
example : normalized ((![1, 1] : Fin 2 → ℝ) + ![1, 0]) =
    normalized ((![2, 2] : Fin 2 → ℝ) + ![1, 0]) := by
  ext i
  fin_cases i <;> norm_num [normalized, amount, Fin.sum_univ_two]
