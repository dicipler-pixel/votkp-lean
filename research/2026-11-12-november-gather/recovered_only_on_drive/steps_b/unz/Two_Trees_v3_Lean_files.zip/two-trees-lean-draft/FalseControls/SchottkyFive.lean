import Mathlib
import TwoTrees.Core
-- Deliberately false: the norm-5 step sits below the Schottky threshold, Γ² = 4/9 < 1/2,
-- not above it.
example : 1 / 2 < PeelTrees.gam 5 * PeelTrees.gam 5 := by
  norm_num [PeelTrees.gam]
