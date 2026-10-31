import VOTKP.Energy

-- Deliberately false: matching the first threshold does not match the binding sum.
example : VOTKP.Energy.total VOTKP.Energy.toyA 3 =
    VOTKP.Energy.total VOTKP.Energy.toyB 3 := by
  norm_num [VOTKP.Energy.total, VOTKP.Energy.removed, VOTKP.Energy.toyA,
    VOTKP.Energy.toyB, Finset.sum_range_succ]
