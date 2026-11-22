/- Rational values of a three-port orbital trace after inserting the model
   overlaps. The Hilbert-space realization is separately derived in README.md. -/
namespace Beasley.TripleReadout

def scaleTriple (a b c : Rat) := 8*a*b*c/((a+b)*(b+c)*(c+a))
def node (a b : Rat) := 1-3*((a-b)/(a+b))^2
def cyc1s (a b c : Rat) := (scaleTriple a b c)^3
def cyc2p (a b c : Rat) := (scaleTriple a b c)^5
def cyc2s (a b c : Rat) := (scaleTriple a b c)^3*node a b*node b c*node c a

theorem threeWeights :
  cyc1s 1 2 4 = 32768/91125 ∧ cyc2s 1 2 4 = -(262144/20503125) ∧
  cyc2p 1 2 4 = 33554432/184528125 := by decide +kernel

theorem sameClockOppositeCycle : (2/1:Rat)^2=(4/2:Rat)^2 ∧
  cyc2s 1 2 4 < 0 ∧ 0 < cyc2p 1 2 4 := by decide +kernel

theorem realCycleReversesEven (a b c : Rat) :
    cyc2s a b c=cyc2s c b a := by
  have hs : scaleTriple a b c=scaleTriple c b a := by
    unfold scaleTriple
    congr 1 <;> grind
  have hn (x y : Rat) : node x y=node y x := by
    simp only [node,Rat.div_def,Rat.pow_succ,Rat.pow_zero,Rat.one_mul]
    rw [Rat.add_comm y x]
    grind
  unfold cyc2s
  rw [hs,hn a b,hn b c,hn c a]
  grind

theorem equalPairControl :
  ((1/3:Rat)^2 = (-1/3:Rat)^2) ∧
  ((1/3:Rat)*(1/3)*(1/3) = 1/27) ∧ ((1/3:Rat)*(1/3)*(-1/3) = -1/27) := by decide +kernel

#print axioms threeWeights
#print axioms sameClockOppositeCycle
#print axioms realCycleReversesEven
#print axioms equalPairControl
end Beasley.TripleReadout
