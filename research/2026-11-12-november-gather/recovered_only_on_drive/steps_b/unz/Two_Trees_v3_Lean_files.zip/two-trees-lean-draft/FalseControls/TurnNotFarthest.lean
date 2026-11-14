import TwoTrees.Core
-- Deliberately false: a turned word does not reach as far as the straight path. For +i, +i, +j
-- the scaled time entry is 4069, not the straight path's 7813.
example : (PeelTrees.word PeelTrees.B5 [.pi, .pi, .pj]).a00 = 7813 := by
  decide
