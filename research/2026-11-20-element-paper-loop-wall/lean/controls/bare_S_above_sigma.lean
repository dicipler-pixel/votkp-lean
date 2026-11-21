import LoopWall
-- False control: must be rejected. With the bare hydrogenic H-like energy, S cannot exceed sigma.
theorem bare_S_above_sigma : (16 * 16 / 2 - (16 - (607:Rat)/1000) * (16 - (607:Rat)/1000) / 2) / 16 - (607:Rat)/1000 > 0 := by
  first | grind | decide +kernel
