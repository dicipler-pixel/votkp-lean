import VOTKP.Curvature
-- Deliberately false: with μ_b = δ = c = 1 the curvature vanishes at r_c = 1, not at the
-- half-filled r = 1/2, where μ_eff = 1.
example : VOTKP.Curvature.μeff 1 1 1 (1 / 2) = 0 := by
  norm_num [VOTKP.Curvature.μeff]
