import TwoTrees.Riley
-- Deliberately false: off the Riley curve the trefoil relation fails. At s = 1, v = 0 the Riley
-- polynomial is 1, and the top-right entry of A W − W B is 1, not 0.
example : (TwoTrees.Riley.merA (1 : ℤ) * (TwoTrees.Riley.merB 1 0 * TwoTrees.Riley.merA 1) -
    TwoTrees.Riley.merB 1 0 * TwoTrees.Riley.merA 1 * TwoTrees.Riley.merB 1 0) 0 1 = 0 := by
  rw [TwoTrees.Riley.trefoil_relation]
  norm_num
