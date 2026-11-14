import TwoTrees.Smith
-- Deliberately false: in Mathlib's metric, tanh(d(i, 5i)/2) is the peel coordinate 2/3 of the
-- ratio 5, not 3/4 (that is the ratio 7).
example : Real.tanh (dist UpperHalfPlane.I (TwoTrees.Smith.vert 5 (by norm_num)) / 2) = 3 / 4 := by
  rw [TwoTrees.Smith.tanh_half_dist_I_vert 5 (by norm_num) (by norm_num)]
  norm_num
