-- deliberately false statements; each must be rejected
theorem c1 : (2:Rat)/3 * (2/3) > 1/2 := by grind
theorem c2 : (7813 : Int) % 5 = 0 := by decide
theorem c3 : (1:Int) + 1 = 3 := by decide
