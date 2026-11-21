/- Finite phase-matching identities and the scalar final inequality.
   Integration, the Bloch Hamiltonian and Jensen's bounds are detailed in CONTACT_MODEL.md. -/
namespace ElementPaper.ContactMoment

def bondLabels : List Nat := [0,1,2,3]
def pairs := bondLabels.flatMap (fun a => bondLabels.map (fun b => (a,b)))
def secondMatches := pairs.filter fun p => p.1 == p.2
def fourthMatches := pairs.flatMap fun p =>
  pairs.filter fun q => (p.1==q.1 && p.2==q.2) || (p.1==q.2 && p.2==q.1)

theorem secondCount : secondMatches.length=4 := by decide +kernel
theorem fourthCount : fourthMatches.length=28 := by decide +kernel

/-- Cross-multiplied middle inequality, with u the squared dimensionless mass. -/
theorem separated (u : Rat) (hu : 0 ≤ u) :
    0 < 4*(u+7) ∧ 4*(u+7)<12*(u+4) := by grind

#print axioms secondCount
#print axioms fourthCount
#print axioms separated
end ElementPaper.ContactMoment
