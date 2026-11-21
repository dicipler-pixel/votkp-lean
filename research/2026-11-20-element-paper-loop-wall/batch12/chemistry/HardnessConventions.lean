/- Realizable finite-decimal inputs are rational here. "Full" refers to the entire
   I − A gap. The scientific convention is a parameter choice, independent of the
   energies' reference source. No database, atoms or fitted parameters enter. -/
namespace ElementPaper.HardnessConventions

def index (chi eta : Rat) : Rat := chi * chi / (2 * eta)

/-- Rescaling the positive denominator by two divides the same quotient by two. -/
private theorem byDouble (x y : Rat) (hy : 0 < y) : x / (2*y) = (x/y)/2 := by
  have h : y ≠ 0 := by grind
  have hd : 2*y ≠ 0 := by grind
  have hxy := Rat.div_mul_cancel (a:=x) h
  have hxd := Rat.div_mul_cancel (a:=x) hd
  have hinv := Rat.mul_inv_cancel y h
  have h1 : (x/(2*y)) * (2*y) * y⁻¹ = (x/y) * y * y⁻¹ := by rw [hxd,hxy]
  grind

/-- With positive half-gap η, using H=2η in the index gives Ω=ω/2. -/
theorem fullIndex (chi eta : Rat) (h : 0 < eta) :
    index chi (2*eta) = index chi eta / 2 := by
  exact byDouble (chi*chi) (2*eta) (by grind)

/-- Keeping ω unchanged and reporting it per full gap gives ω/H=(ω/η)/2. -/
theorem keepOriginalIndex (chi eta : Rat) (h : 0 < eta) :
    index chi eta / (2*eta) = (index chi eta/eta)/2 :=
  byDouble (index chi eta) eta h

/-- Recomputing Ω with the full gap and reporting it per full gap gives Ω/H=(ω/η)/4. -/
theorem recomputeIndex (chi eta : Rat) (h : 0 < eta) :
    index chi (2*eta) / (2*eta) = (index chi eta/eta)/4 := by
  rw [fullIndex chi eta h]
  rw [Rat.div_def (index chi eta / 2), Rat.div_def (index chi eta) eta]
  have e : (2*eta)⁻¹ = (eta⁻¹)/2 := by
    apply Rat.inv_eq_of_mul_eq_one
    have k := Rat.mul_inv_cancel eta (show eta ≠ 0 by grind)
    grind
  rw [e]
  grind

/-- A positive reference gap gives the same strict outside predicate in either convention. -/
theorem sameOutside (chi eta : Rat) (h : 0 < eta) :
    (index chi eta / eta < 1 ↔ index chi eta / (2*eta) < 1/2) ∧
    (index chi eta / eta < 1 ↔ index chi (2*eta) / (2*eta) < 1/4) := by
  rw [keepOriginalIndex chi eta h, recomputeIndex chi eta h]
  grind

/-- At equality the half-gap reading 1 becomes exactly 1/2 or 1/4. -/
theorem sameBoundary (chi eta : Rat) (h : 0 < eta) :
    (index chi eta / eta = 1 ↔ index chi eta / (2*eta) = 1/2) ∧
    (index chi eta / eta = 1 ↔ index chi (2*eta) / (2*eta) = 1/4) := by
  rw [keepOriginalIndex chi eta h, recomputeIndex chi eta h]
  grind

/-- All strict inside labels are preserved as well. -/
theorem sameInside (chi eta : Rat) (h : 0 < eta) :
    (1 < index chi eta / eta ↔ 1/2 < index chi eta / (2*eta)) ∧
    (1 < index chi eta / eta ↔ 1/4 < index chi (2*eta) / (2*eta)) := by
  rw [keepOriginalIndex chi eta h, recomputeIndex chi eta h]
  grind

/-- At the exact wall, chi² = 2η². Encoding the squared coordinate avoids needing
    an irrational chi in Rat. Here η=1, chi²=2 realizes the boundary exactly. -/
theorem boundarySquaredWitness :
    let eta : Rat := 1
    let chiSquared : Rat := 2
    let H := 2*eta
    let omega := chiSquared / (2*eta)
    let fullOmega := chiSquared / (2*H)
    omega/eta = 1 ∧ omega/H = 1/2 ∧ fullOmega/H = 1/4 := by decide +kernel

/-- A false convention can flip a categorical decision at explicit positive inputs:
    chi=3, eta=2. The half-gap ratio is 9/8; misusing a unit cutoff for full/full
    would classify this inside example as outside. -/
theorem falseUnitCutoff :
    1 < index 3 2 / 2 ∧ index 3 4 / 4 < 1 ∧ 1/4 < index 3 4 / 4 := by decide +kernel

#print axioms byDouble
#print axioms boundarySquaredWitness
#print axioms falseUnitCutoff
#print axioms sameInside
#print axioms fullIndex
#print axioms keepOriginalIndex
#print axioms recomputeIndex
#print axioms sameOutside
#print axioms sameBoundary
end ElementPaper.HardnessConventions
