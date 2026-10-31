import VOTKP.Memory
-- Deliberately false: the fifth Markov parameter of the five-site shift is 1, not 0, so
-- vanishing of the first four does not silence the transfer.
example : (VOTKP.Memory.shift5 ^ 4) 4 0 = 0 := by
  decide
