import Std

namespace VOTKP.ScalarShellBound

/-- Independent of how the equal amounts of added and removed occupation are
distributed, if the kernel on their common envelope lies in [lo,hi]. The two
moment hypotheses describe integrals of this kernel over the two pieces. -/
theorem retained_amplitude_lower_bound (reference amplitude added removed moved lo hi : Rat)
    (balance : amplitude = reference+added-removed)
    (addLower : moved*lo ≤ added) (removeUpper : removed ≤ moved*hi) :
    reference-moved*(hi-lo) ≤ amplitude := by grind

private theorem square_monotone {a b : Rat} (ha : 0 ≤ a) (hab : a ≤ b) :
    a^2 ≤ b^2 := by
  have hb := Rat.le_trans ha hab
  have h₁ := Rat.mul_le_mul_of_nonneg_left hab ha
  have h₂ := Rat.mul_le_mul_of_nonneg_right hab hb
  grind

/-- Sufficient enclosure for the 2.2% cubic radial-pocket estimate. The
geometric calculation supplies reference ≥ 0.238, moved ≤ 0.065 and a kernel
range ≤ 0.505. This theorem only needs these rational enclosures. -/
theorem sufficient_shell_concentration (reference amplitude moved width : Rat)
    (referenceLower : 238/1000 ≤ reference) (movedNonnegative : 0 ≤ moved)
    (movedUpper : moved ≤ 65/1000) (widthUpper : width ≤ 505/1000)
    (pocketBound : reference-moved*width ≤ amplitude) :
    (1/3 : Rat) < 8*amplitude^2 := by
  have h₁ := Rat.mul_le_mul_of_nonneg_left widthUpper movedNonnegative
  have h₂ := Rat.mul_le_mul_of_nonneg_right movedUpper (show (0:Rat) ≤ 505/1000 by decide +kernel)
  have hmin : (205175/1000000:Rat) ≤ amplitude := by grind
  have hsq := square_monotone (show (0:Rat) ≤ 205175/1000000 by decide +kernel) hmin
  grind

/-- The volume of the removed portion at 2.2% radial deviation is bounded
by the inner spherical shell's volume relative to the reference volume. -/
theorem inner_volume_enclosure : (1:Rat) - (1-22/1000)^3 < 65/1000 := by decide +kernel

#print axioms retained_amplitude_lower_bound
#print axioms sufficient_shell_concentration
#print axioms inner_volume_enclosure
end VOTKP.ScalarShellBound
