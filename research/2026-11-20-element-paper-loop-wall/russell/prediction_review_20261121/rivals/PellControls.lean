/-
An exact, pre-indexed sequence of alternating equal-face control settings.
No analysis of a physical instrument is assumed. Core Lean 4.34.1.
-/
namespace Beasley.PellControls

def next (p : Int × Int) : Int × Int := (p.1 + 2*p.2, p.1 + p.2)

def pair : Nat → Int × Int
  | 0 => (1, 0)
  | n+1 => next (pair n)

def defect (p : Int × Int) : Int := p.1^2 - 2*p.2^2

theorem step_flips (p : Int × Int) : defect (next p) = -defect p := by
  rcases p with ⟨u,v⟩
  unfold defect next
  simp
  grind

theorem alternating_defect (n : Nat) : defect (pair n) = (-1 : Int)^n := by
  induction n with
  | zero => decide +kernel
  | succ n ih =>
    change defect (next (pair n)) = (-1 : Int)^(n+1)
    rw [step_flips,ih,Int.pow_succ]
    grind

def ratio (n : Nat) : Rat :=
  let p := pair n
  ((p.1+p.2 : Int) : Rat) / ((p.1-p.2 : Int) : Rat)

def g (z : Rat) : Rat := (z-1)/(z+1)
def power (z : Rat) : Rat := 2*(g z)^2
def trace (z : Rat) : Rat := 2-4*((z-1)^2/(4*z))^2

/-- The first setting has u=v and is singular, so the physical design begins at n=2. -/
theorem settings :
    ratio 2 = 5 ∧ ratio 3 = 6 ∧ ratio 4 = 29/5 ∧ ratio 5 = 35/6 ∧
    ratio 6 = 169/29 ∧ ratio 7 = 204/35 ∧ ratio 8 = 985/169 := by
  decide +kernel

theorem bounded_classes :
    power (ratio 4) < 1 ∧ 1 < power (ratio 5) ∧ power (ratio 6) < 1 ∧
    1 < power (ratio 7) ∧ power (ratio 8) < 1 := by
  decide +kernel

theorem return_margins :
    trace (ratio 4)+2 = 1156/21025 ∧
    trace (ratio 5)+2 = -1681/176400 ∧
    trace (ratio 6)+2 = 39204/24019801 ∧
    trace (ratio 7)+2 = -57121/203918400 ∧
    trace (ratio 8)+2 = 1331716/27710596225 := by
  decide +kernel

#print axioms alternating_defect
#print axioms settings
#print axioms bounded_classes
#print axioms return_margins

end Beasley.PellControls
