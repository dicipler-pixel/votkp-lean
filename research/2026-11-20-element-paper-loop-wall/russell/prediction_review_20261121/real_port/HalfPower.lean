/- Normalized real-source impedance terminating one lossless power-carrying port.
   x and y are rational resistance and reactance divided by the reference resistance.
   No impedance identification is asserted for an atomic ionization-energy ratio. -/
namespace Beasley.HalfPower

def reflected (x y : Rat) := (x-1)^2 + y^2
def absorbed (x _y : Rat) := 4*x
def incident (x y : Rat) := (x+1)^2 + y^2

theorem fluxBalance (x y : Rat) :
    reflected x y + absorbed x y = incident x y := by
  simp [reflected,absorbed,incident,Rat.pow_succ]
  grind

theorem circleTest (x y : Rat) :
    absorbed x y < reflected x y ↔ 8 < (x-3)^2+y^2 := by
  simp [reflected,absorbed,Rat.pow_succ]
  grind

theorem equalAtComplexBoundary : reflected 5 2 = absorbed 5 2 := by decide +kernel
theorem reactanceFlipsClassification :
    reflected (291/50) 0 < absorbed (291/50) 0 ∧
    absorbed (291/50) (1/4) < reflected (291/50) (1/4) := by decide +kernel

theorem loadSetting : ((300:Rat)*10500/(300+10500))/50=35/6 := by decide +kernel
theorem calibratedEqualFaces :
    reflected (35/6) 0 / incident (35/6) 0 = 841/1681 ∧
    absorbed (35/6) 0 / incident (35/6) 0 = 840/1681 := by decide +kernel

#print axioms fluxBalance
#print axioms circleTest
#print axioms equalAtComplexBoundary
#print axioms reactanceFlipsClassification
#print axioms loadSetting
#print axioms calibratedEqualFaces
end Beasley.HalfPower
