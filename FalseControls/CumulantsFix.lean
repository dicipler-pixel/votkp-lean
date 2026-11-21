import VOTKP.Peel
-- False: the padded triples (1,0,0) and (1,1,0) do not share c₁.
example : (1 + 0 + 0 : ℝ) = 1 + 1 + 0 := by norm_num
