import Std

namespace VOTKP.Element8Intervals

/-- Closed admissible intervals on positive energy inputs. -/
structure Band where
  lo : Rat
  hi : Rat

/-- A sufficient interior bound using endpoints, without division. -/
def SafeInside (s t : Band) : Prop :=
  0 < s.lo ∧ s.hi ≤ t.lo ∧ 2*(t.hi-s.lo)^2 < (s.lo+t.lo)^2

/-- A sufficient exterior bound using endpoints, without division. -/
def SafeOutside (s t : Band) : Prop :=
  0 < s.lo ∧ s.hi ≤ t.lo ∧ (s.hi+t.hi)^2 < 2*(t.lo-s.hi)^2

private theorem sqMono {x y : Rat} (hx : 0 ≤ x) (hxy : x ≤ y) : x^2 ≤ y^2 := by
  have hy : 0 ≤ y := Rat.le_trans hx hxy
  have h₁ := Rat.mul_le_mul_of_nonneg_left hxy hx
  have h₂ := Rat.mul_le_mul_of_nonneg_right hxy hy
  grind

/-- Every pair of energies in a certified inside box obeys the strict wall test. -/
theorem inside_everywhere {s t : Band} {a b : Rat}
    (H : SafeInside s t) (al : s.lo ≤ a) (ah : a ≤ s.hi)
    (bl : t.lo ≤ b) (bh : b ≤ t.hi) :
    0 < a ∧ a ≤ b ∧ 2*(b-a)^2 < (a+b)^2 := by
  obtain ⟨hpos, horder, hedge⟩ := H
  have hdiff : (b-a)^2 ≤ (t.hi-s.lo)^2 := sqMono (by grind) (by grind)
  have hsum : (s.lo+t.lo)^2 ≤ (a+b)^2 := sqMono (by grind) (by grind)
  grind

/-- Every pair of energies in a certified outside box obeys the strict wall test. -/
theorem outside_everywhere {s t : Band} {a b : Rat}
    (H : SafeOutside s t) (al : s.lo ≤ a) (ah : a ≤ s.hi)
    (bl : t.lo ≤ b) (bh : b ≤ t.hi) :
    0 < a ∧ a ≤ b ∧ (a+b)^2 < 2*(b-a)^2 := by
  obtain ⟨hpos, horder, hedge⟩ := H
  have hsum : (a+b)^2 ≤ (s.hi+t.hi)^2 := sqMono (by grind) (by grind)
  have hdiff : (t.lo-s.hi)^2 ≤ (b-a)^2 := sqMono (by grind) (by grind)
  grind

inductive Input where
  | unbound
  | energy (value : Rat) (uncertainty : Option Rat)
  deriving Inhabited

inductive Status where
  | inside | outside | noBoundAnion | missingUncertainty | unresolved
  deriving DecidableEq, Repr

def boxStatus (s t : Band) : Status :=
  if 0 < s.lo ∧ s.lo ≤ s.hi ∧ s.hi ≤ t.lo ∧ t.lo ≤ t.hi then
    if 2*(t.hi-s.lo)^2 < (s.lo+t.lo)^2 then .inside
    else if (s.hi+t.hi)^2 < 2*(t.lo-s.hi)^2 then .outside
    else .unresolved
  else .unresolved

theorem box_inside_sound {s t : Band} (h : boxStatus s t = .inside) : SafeInside s t := by
  unfold boxStatus at h
  unfold SafeInside
  split at h <;> grind (splits := 4)

theorem box_outside_sound {s t : Band} (h : boxStatus s t = .outside) : SafeOutside s t := by
  unfold boxStatus at h
  unfold SafeOutside
  split at h <;> grind (splits := 4)

def classify : Input → Input → Status
  | .unbound, _ | _, .unbound => .noBoundAnion
  | .energy x (some dx), .energy y (some dy) =>
    boxStatus ⟨x-dx, x+dx⟩ ⟨y-dy, y+dy⟩
  | _, _ => .missingUncertainty

def statuses (r : List Input) : List Status :=
  (r.zip r.tail).map fun (s, t) => classify s t

end VOTKP.Element8Intervals
