import TwoTrees.Riley
-- Deliberately false: at s = 1 the meridian is parabolic (discriminant 0), not hyperbolic, so the
-- hypothesis s² ≠ 1 cannot be dropped.
example : Matrix.IsHyperbolic !![(1 : ℝ), 1; 0, 1 / 1] := by
  show (0 : ℝ) < Matrix.discr !![(1 : ℝ), 1; 0, 1 / 1]
  rw [TwoTrees.Riley.meridian_discr]
  norm_num
