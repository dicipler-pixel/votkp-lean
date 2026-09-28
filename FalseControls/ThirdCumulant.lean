import VOTKP.Peel
open VOTKP.Peel
-- Deliberately false: the two channel sets share conductance and Fano factor but not the
-- third cumulant (0 against 3/50).
example : pw 1 (1 / 5) (1 / 2) (4 / 5) - 3 * pw 2 (1 / 5) (1 / 2) (4 / 5) +
    2 * pw 3 (1 / 5) (1 / 2) (4 / 5) = 3 / 50 := by
  norm_num [pw]
