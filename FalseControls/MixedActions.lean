import VOTKP.MultiObserver

open VOTKP.MultiObserver

-- Deliberately false: every pure repetition of A and every pure repetition
-- of B hides this state, but the chronological mixed word [B,A] reads 1.
example : controlRecord (wordMap controlActions [false, true] controlState) = 0 := by
  norm_num [wordMap, controlActions, controlRecord, controlState, controlA, controlB]
