import VOTKP.ThetaStructure

-- Deliberately false even with nonzero weight: a ring with zero divisors
-- does not support the cancellation used in the mirror equivalence.
example : (3 : ZMod 6) ≠ 0 → (3 : ZMod 6) * (1 + 1) = 0 →
    (1 : ZMod 6) = -1 := by
  decide
