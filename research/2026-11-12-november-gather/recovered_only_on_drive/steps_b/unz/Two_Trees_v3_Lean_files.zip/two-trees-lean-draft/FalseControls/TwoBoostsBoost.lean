import TwoTrees.Core
-- Deliberately false: the product of two perpendicular boosts is not a boost (it is not
-- symmetric); the difference is the Thomas rotation.
example : PeelTrees.M4.tr (PeelTrees.M4.mul (PeelTrees.B5 .pi) (PeelTrees.B5 .pj)) =
    PeelTrees.M4.mul (PeelTrees.B5 .pi) (PeelTrees.B5 .pj) := by
  decide
