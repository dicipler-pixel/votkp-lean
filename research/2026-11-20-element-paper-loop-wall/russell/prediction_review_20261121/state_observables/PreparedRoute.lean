/- State selected oxygen: exact arithmetic on published central inputs.
   The last lemma states explicitly what a measurement conditional only on
   a prepared state can infer about the earlier route. Core Lean 4.34.1. -/
namespace Beasley.PreparedRoute

def cmPerEv : Rat := 8065543937/1000000
def oxygenI : Rat := 13618055/1000000
def oxygenII : Rat := 3512112/100000
def rival : Rat := ((7576234/1000000)/(130447/100000)
                   + (815168/100000)/(13895212/10000000))/2
def ratio (initial final : Rat) : Rat :=
  (oxygenII + final/cmPerEv)/(oxygenI - initial/cmPerEv)
def geometricOutside (z : Rat) : Bool := decide (1 < z ∧ 0 < z*z-6*z+1)
def label (initial final : Rat) : Bool × Bool :=
  let z := ratio initial final
  (geometricOutside z, decide (rival < z))

def finalJ0 : Rat := 35673630/100
def finalJ1 : Rat := 35684498/100
def finalJ2 : Rat := 35711701/100
def initialJ1 : Rat := 158265/1000
def initialJ0 : Rat := 226977/1000

theorem groundTriplet : (label 0 finalJ0, label 0 finalJ1, label 0 finalJ2) =
    ((false,false), (false,false), (true,false)) := by decide +kernel

theorem sameFinalDifferentRoutes :
    (label 0 finalJ0, label initialJ1 finalJ0, label initialJ0 finalJ0) =
    ((false,false), (true,false), (true,true)) := by decide +kernel

theorem noFinalOnlyWall :
    ¬ ∃ readout : Rat → Bool, ∀ initial, readout finalJ0 = (label initial finalJ0).1 := by
  intro ⟨readout,allRoutes⟩
  have one := allRoutes 0
  have two := allRoutes initialJ1
  have h : (label 0 finalJ0).1 ≠ (label initialJ1 finalJ0).1 := by decide +kernel
  exact h (one.symm.trans two)

/-- Applies to state-conditioned probabilities or full outcome distributions.
    Equality here includes all physical preparation variables available to the probe. -/
theorem identicalPreparedResponse {State Outcome : Type} (response : State → Outcome)
    {p q : State} (same : p=q) : response p=response q := congrArg response same

theorem excitationTelescopes (second third excitation : Rat) :
    (second+excitation)+(third-excitation)=second+third := by grind

#print axioms groundTriplet
#print axioms sameFinalDifferentRoutes
#print axioms noFinalOnlyWall
#print axioms identicalPreparedResponse
#print axioms excitationTelescopes
end Beasley.PreparedRoute
