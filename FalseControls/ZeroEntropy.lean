import VOTKP.Ordinal
-- Deliberately false: zero permutation entropy at delay 2 does not exclude the transposed
-- ladder; its delay-2 pattern is single, so this claim is refuted by evaluation.
example : VOTKP.Ordinal.singlePattern 2 VOTKP.Ordinal.swapped = false := by decide
