import VOTKP.ThetaGrid

open VOTKP.ThetaGrid

-- Deliberately false: the polynomial vanishes at (2,3), (3,2), and (2,5),
-- but those checks do not exhaust its degree-bounded rectangular grid.
-- Its value at (4,5) is 2, not 0.
example : evalXY threePointFalseControl 4 5 = 0 := by
  norm_num [threePointFalseControl, evalXY]
