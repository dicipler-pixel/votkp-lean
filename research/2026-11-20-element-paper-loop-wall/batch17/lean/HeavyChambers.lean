import Batch12Bounds

namespace ElementPaper.HeavyChambers
open VOTKP.NearestPair
open ElementPaper.Batch12 (endpointLo endpointHi ratioBounds admitsInside admitsOutside)

/-- A shell reference of four and the loop wall are distinct decision boundaries. -/
def aboveFour (f : Face) := valid f && decide (4 < endpointLo f)
def belowFour (f : Face) := valid f && decide (endpointHi f < 4)

theorem strictlyAbove {f : Face} (ok : aboveFour f = true) {a b : Rat} (h : Admits f a b) :
    4 < b/a := by
  simp only [aboveFour, Bool.and_eq_true, decide_eq_true_eq] at ok
  have lo := (ratioBounds ok.1 h).1
  grind

theorem strictlyBelow {f : Face} (ok : belowFour f = true) {a b : Rat} (h : Admits f a b) :
    b/a < 4 := by
  simp only [belowFour, Bool.and_eq_true, decide_eq_true_eq] at ok
  have hi := (ratioBounds ok.1 h).2
  grind

theorem descending {f g : Face} (hf : valid f = true) (hg : valid g = true)
    (sep : endpointHi g < endpointLo f) {a b c d : Rat} (h : Admits f a b) (j : Admits g c d) :
    d/c < b/a := by
  have hi := (ratioBounds hg j).2
  have lo := (ratioBounds hf h).1
  grind

/-- Strict proximity, valid for every test value on the first centre's side of the midpoint. -/
theorem nearerOnLeft {y l d : Rat} (order : l<d) (mid : 2*y<l+d) :
    (y-l).abs < (y-d).abs := by
  rw [Rat.abs_of_nonpos (show y-d≤0 by grind)]
  by_cases h : 0≤y-l
  · rw [Rat.abs_of_nonneg h]; grind
  · rw [Rat.abs_of_nonpos (show y-l≤0 by grind)]; grind

def lastDigit : Rat := 1/2000000000

def nearerTest (f : Face) (m : Rat × Rat) : Bool :=
  valid f && decide (m.1+lastDigit < m.2-lastDigit ∧
    2*endpointHi f < (m.1-lastDigit)+(m.2-lastDigit))

theorem nearerAcrossFullBox {f : Face} {m : Rat × Rat} (ok : nearerTest f m = true)
    {a b l d : Rat} (h : Admits f a b)
    (hl : m.1-lastDigit ≤ l ∧ l ≤ m.1+lastDigit) (hd : m.2-lastDigit ≤ d) :
    (b/a-l).abs < (b/a-d).abs := by
  simp only [nearerTest, Bool.and_eq_true, decide_eq_true_eq] at ok
  have upper := (ratioBounds ok.1 h).2
  apply nearerOnLeft <;> grind

def whollyIn (f : Face) (v : Rat) :=
  decide (endpointLo f ≤ v-lastDigit ∧ v+lastDigit ≤ endpointHi f)

def whollyOut (f : Face) (v : Rat) :=
  decide (v+lastDigit < endpointLo f ∨ endpointHi f < v-lastDigit)

structure Forecast where
  z : Nat
  face : Face
  predictedOutside : Bool

def predictionSupported (r : Forecast) :=
  if r.predictedOutside then admitsOutside r.face else admitsInside r.face

/-- Sufficient to add this entire box to any previous silver–silicon cutoff without narrowing it. -/
def leavesWindow (r : Forecast) :=
  if r.predictedOutside then decide (Batch11.silicon ≤ endpointLo r.face)
  else decide (endpointHi r.face ≤ Batch11.silver)

theorem sameCutForEveryInput {r : Forecast} (ok : predictionSupported r = true)
    (keep : leavesWindow r = true) {a b c : Rat} (h : Admits r.face a b)
    (hl : Batch11.silver ≤ c) (hu : c < Batch11.silicon) :
    decide (c < b/a) = r.predictedOutside := by
  cases e : r.predictedOutside
  · simp [predictionSupported,e,admitsInside] at ok
    simp [leavesWindow,e] at keep
    have hi := (ratioBounds ok.1 h).2
    apply decide_eq_false
    grind
  · simp [predictionSupported,e,admitsOutside] at ok
    simp [leavesWindow,e] at keep
    have lo := (ratioBounds ok.1 h).1
    apply decide_eq_true
    grind

def chemistry (f : Face) : Bool :=
  let ea := f.a
  let ie := f.b
  let eta := (ie-ea)/2
  let chi := (ie+ea)/2
  let omega := chi^2/(2*eta)
  decide (0<ea ∧ ea<ie ∧ eta/chi = g ea ie ∧ omega/eta = 1/(2*power ea ie) ∧
      ((1:Rat)/2 < power ea ie ↔ omega < eta))

end ElementPaper.HeavyChambers
