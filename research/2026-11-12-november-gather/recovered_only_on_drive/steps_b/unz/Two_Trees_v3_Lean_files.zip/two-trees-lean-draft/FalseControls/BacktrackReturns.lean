import TwoTrees.Core
-- Deliberately false: freeness needs non-backtracking words. The word +i, -i steps out and
-- straight back, its scaled matrix is 25 I, and its time entry 25 IS divisible by 5.
example : (PeelTrees.word PeelTrees.B5 [.pi, .mi]).a00 % 5 ≠ 0 := by
  decide
