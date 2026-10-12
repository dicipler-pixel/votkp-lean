import VOTKP.Channels
-- Deliberately false: an active channel whose pole lies between the probes has c < 0, and
-- c·δs·K with c = -1, δs = 1, K = I is not positive semidefinite. The side condition of 5.6
-- is needed.
example : ((-1 : ℝ) • (1 : Matrix (Fin 1) (Fin 1) ℝ)).PosSemidef :=
  Matrix.PosSemidef.smul Matrix.PosSemidef.one (by norm_num)
