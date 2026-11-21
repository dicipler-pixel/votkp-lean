import Std

namespace VOTKP.OpticalWall

/-- Normal-incidence power at a vacuum/material boundary. The n+ik sign
convention fixes the phase; using n−ik has the same power. -/
def reflectionPower (n k : Rat) : Rat :=
  ((1-n)^2 + k^2) / ((1+n)^2 + k^2)

/-- Denominator-cleared difference from the half-power boundary. -/
theorem circle_identity (n k : Rat) :
    2*((1-n)^2 + k^2) - ((1+n)^2 + k^2) = (n-3)^2+k^2-8 := by grind

/-- The circle test applies for positive squared denominator. This explicitly
excludes the pole n=−1, k=0. -/
theorem half_power_iff_outside_circle (n k : Rat)
    (h : 0 < (1+n)^2 + k^2) :
    (1/2 : Rat) < reflectionPower n k ↔ 8 < (n-3)^2 + k^2 := by
  unfold reflectionPower
  rw [Rat.lt_div_iff h]
  have hc := circle_identity n k
  grind

/-- Two complex face indices, encoded by four rationals. The outgoing field
is (v−u)/(v+u) at normal incidence. Swapping incident and transmitted indices
negates each amplitude component; the squared amplitude is consequently even.
The common denominator is written explicitly to keep the phase convention visible. -/
def amplitude (ur ui vr vi : Rat) : Rat × Rat :=
  let d := (vr+ur)^2+(vi+ui)^2
  ( ((vr-ur)*(vr+ur)+(vi-ui)*(vi+ui))/d,
    ((vi-ui)*(vr+ur)-(vr-ur)*(vi+ui))/d )

theorem reciprocal_amplitude (ur ui vr vi : Rat) :
    amplitude vr vi ur ui =
      (-(amplitude ur ui vr vi).1, -(amplitude ur ui vr vi).2) := by
  have hd : (ur+vr)^2 + (ui+vi)^2 = (vr+ur)^2 + (vi+ui)^2 := by grind
  have h1 : (ur-vr)*(ur+vr)+(ui-vi)*(ui+vi) =
      -((vr-ur)*(vr+ur)+(vi-ui)*(vi+ui)) := by grind
  have h2 : (ui-vi)*(ur+vr)-(ur-vr)*(ui+vi) =
      -((vi-ui)*(vr+ur)-(vr-ur)*(vi+ui)) := by grind
  simp only [amplitude, hd, h1, h2, Rat.div_def, Rat.neg_mul]

theorem reciprocal_power (ur ui vr vi : Rat) :
    (amplitude vr vi ur ui).1^2+(amplitude vr vi ur ui).2^2 =
    (amplitude ur ui vr vi).1^2+(amplitude ur ui vr vi).2^2 := by
  rw [reciprocal_amplitude]
  grind

/-- The two consecutive photon-energy observations in Smith's room-temperature
rubidium table that bracket half power. Wavelengths 386.967 and 364.981 nm. -/
theorem rubidium_observed_bracket :
    (1/2 : Rat) < reflectionPower (157074/1000000) (429735/1000000) ∧
    reflectionPower (257/1000) (247081/1000000) < 1/2 := by decide +kernel

/-- At 2237.982 nm, dropping the tabulated extinction coefficient reverses
the decision for the very same rubidium specimen and index. -/
theorem rubidium_extinction_false_control :
    (1/2 : Rat) < reflectionPower (172367/1000000) (6306323/1000000) ∧
    reflectionPower (172367/1000000) 0 < 1/2 := by decide +kernel

/-- Transparent crystalline krypton at 546.1 nm, compared at k=0. -/
theorem krypton_transparent_comparison :
    reflectionPower (13674/10000) 0 < 1/2 := by decide +kernel

#print axioms reciprocal_amplitude
#print axioms reciprocal_power
#print axioms circle_identity
#print axioms half_power_iff_outside_circle
#print axioms rubidium_observed_bracket
#print axioms rubidium_extinction_false_control
#print axioms krypton_transparent_comparison
end VOTKP.OpticalWall
