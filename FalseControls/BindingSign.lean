import VOTKP.Energy

-- Deliberately false: the bare-reference bound ground energy has the opposite sign.
example : VOTKP.Energy.ground (fun _ => 1) 3 0 = 3 := by
  norm_num [VOTKP.Energy.ground, VOTKP.Energy.binding, VOTKP.Energy.total,
    VOTKP.Energy.removed, Finset.sum_range_succ]
