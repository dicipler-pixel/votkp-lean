/- Exact comparisons for the two theory-grade pinned ground removals only.
   This file makes no statement about a measured transition or the Dirac overlap. -/
namespace Beasley.HydrogenicScSn

def scandium : Rat := 603375643/100000
def tin : Rat := 35192501/1000
def dSc : Rat := 9/100000
def dSn : Rat := 11/1000
def rival : Rat := ((7576234/1000000)/(130447/100000)
                   + (815168/100000)/(13895212/10000000))/2
def aboveWall (q : Rat) : Prop := 1 < q ∧ 0 < q*q-6*q+1
instance (q : Rat) : Decidable (aboveWall q) := by unfold aboveWall; infer_instance
def low : Rat := (tin-dSn)/(scandium+dSc)
def high : Rat := (tin+dSn)/(scandium-dSc)

theorem endpoints : aboveWall low ∧ low < tin/scandium ∧ tin/scandium < high ∧ high < rival := by
  decide +kernel

theorem wallMonotone (q : Rat) (h : low ≤ q) : aboveWall q := by
  have large : 3 < low := by decide +kernel
  have positive : 0 < low*low-6*low+1 := endpoints.1.2
  have dp : 0 ≤ q-low := by grind
  have ds : 0 ≤ q+low-6 := by grind
  have prod := Rat.mul_nonneg dp ds
  unfold aboveWall
  grind

theorem entireBox (q : Rat) (lo : low ≤ q) (hi : q ≤ high) :
    aboveWall q ∧ q < rival := by
  have top : high < rival := endpoints.2.2.2
  exact ⟨wallMonotone q lo, by grind⟩

theorem nonrelControl : ¬ aboveWall ((50/21:Rat)^2) := by decide +kernel

#print axioms endpoints
#print axioms wallMonotone
#print axioms entireBox
#print axioms nonrelControl
end Beasley.HydrogenicScSn
