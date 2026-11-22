/- The rational algebra after the normalized 1s overlap integral. The integral,
   sudden preparation and fixed mass are separate analytic/physical hypotheses. -/
namespace Beasley.FaceFidelity

def apex (a b : Rat) := (b-a)/(b+a)
def fidelity (a b : Rat) := (4*a*b/(a+b)^2)^3

theorem halfStep (a b : Rat) (s : a+b ≠ 0) :
    1-(apex a b)^2=4*a*b/(a+b)^2 := by
  simp only [apex, Rat.div_def, Rat.pow_succ, Rat.pow_zero, Rat.one_mul]
  have s' : b+a ≠ 0 := by grind
  have h : (b+a)⁻¹=(a+b)⁻¹ := by rw [Rat.add_comm b a]
  rw [h]
  have hh : (a+b)*(a+b)⁻¹=1 := Rat.mul_inv_cancel _ s
  have hinv : ((a+b)*(a+b))⁻¹=(a+b)⁻¹*(a+b)⁻¹ := by grind
  rw [hinv]
  grind

theorem apexFidelity (a b : Rat) (s : a+b ≠ 0) :
    fidelity a b = (1-(apex a b)^2)^3 := by rw [halfStep a b s]; rfl

theorem reverseIndependent (a b : Rat) : fidelity a b = fidelity b a := by
  simp only [fidelity]
  have a1 : 4*a*b=4*b*a := by grind
  rw [a1,Rat.add_comm a b]

theorem tritiumControl : apex 1 2=1/3 ∧ fidelity 1 2=512/729 := by decide +kernel

theorem distinctFromPeelPower :
    fidelity 1 2 ≠ 1-((4-1:Rat)/(4+1))^2 := by decide +kernel

#print axioms apexFidelity
#print axioms reverseIndependent
#print axioms tritiumControl
#print axioms distinctFromPeelPower
end Beasley.FaceFidelity
