import VOTKP.ThetaStructure

-- Deliberately false: cancelling a zero Alexander weight is invalid.
-- The vanishing composite factor supplies no mirror-sign information here.
example : (0 : ℚ) * (1 + 1) = 0 → (1 : ℚ) = -1 := by
  norm_num
