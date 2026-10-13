import VOTKP.Directed
-- Deliberately false: at τ = 1/2 the gaps 1 and 3 do not share a friction weight
-- (4/5 against 12/13); equality needs d·e = 1/τ² = 4.
example : VOTKP.Directed.wgt (1 / 2) 1 = VOTKP.Directed.wgt (1 / 2) 3 := by
  norm_num [VOTKP.Directed.wgt]
