import VOTKP.Peel
open VOTKP.Peel
-- Deliberately false: the shared record T(0) = 1/2 does not fix the later transmission; at
-- x = 1 the two hidden-site signs give 0 and 4/5.
example : T 1 1 = T (-1) 1 := by
  norm_num [T]
