import VOTKP.Directed
-- Deliberately false: the out-and-back record r₀ = 0.4, r₁ = −0.4 has endpoint distance 0,
-- not its traversed length 1.6. Net change does not record the route.
example : 2 * |∑ j ∈ Finset.range 2, (if j = 0 then (0.4 : ℝ) else -0.4)| = 1.6 := by
  norm_num [Finset.sum_range_succ]
