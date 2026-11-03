import VOTKP.MatterDisk
-- Deliberately false: the small-s form 2s/S_next is not exact. At S_next = 3, s = 1 the exact
-- rim distance is 2s/(S_next - s) = 1, not 2/3.
example : VOTKP.MatterDisk.g (3 / (-1)) - 1 = 2 * 1 / 3 := by
  unfold VOTKP.MatterDisk.g
  norm_num
