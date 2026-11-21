import PromethiumTerbium

namespace ElementPaper.Batch13.SharedError

open ElementPaper.Batch12 (Reading)

/-- Shift E by u*p, where the signed error in units of its reported width has
−1 ≤ p ≤ 1. An adverse neighboring shift increases the left level relative
to the right. The parameter d measures the difference between their errors. -/
def adverse (u v d : Rat) : Rat :=
  if u ≤ v then v-u+u*d else u-v+v*d

theorem adverseBound {u v d p q : Rat} (hu : 0≤u) (hv : 0≤v) (hp : p≤1)
    (hq : -1≤q) (hd : p-q≤d) : u*p - v*q ≤ adverse u v d := by
  unfold adverse
  split <;> rename_i h
  · have a := Rat.mul_le_mul_of_nonneg_left hd hu
    have b := Rat.mul_le_mul_of_nonneg_left (show -q ≤ 1 by grind) (show 0≤v-u by grind)
    grind
  · have a := Rat.mul_le_mul_of_nonneg_left hd hv
    have b := Rat.mul_le_mul_of_nonneg_left hp (show 0≤u-v by grind)
    grind

/-- The upper bound is attained within the two stated standardized intervals. -/
theorem adverseAttained (u v d : Rat) (d0 : 0≤d) (d2 : d≤2) :
    ∃ p q : Rat, -1≤p ∧ p≤1 ∧ -1≤q ∧ q≤1 ∧ p-q=d ∧ u*p-v*q=adverse u v d := by
  unfold adverse
  split
  · exact ⟨d-1,-1, by grind⟩
  · exact ⟨1,1-d, by grind⟩

theorem growsWithDifference {u v d f : Rat} (hu : 0<u) (hv : 0<v) (df : d<f) :
    adverse u v d < adverse u v f := by
  unfold adverse
  split <;> rename_i h
  · have hp := Rat.mul_lt_mul_of_pos_left df hu
    grind
  · have hp := Rat.mul_lt_mul_of_pos_left df hv
    grind

def limit : Rat := 9/7

def atLimit (xs : List Reading) (contact : Option Nat) : Bool :=
  (List.range xs.length).all (fun k =>
    if k=0 then true else
      let a := xs[k-1]!
      let b := xs[k]!
      let bound := adverse a.2 b.2 limit
      decide (0<a.2 ∧ 0<b.2 ∧
        (if contact = some k then bound = b.1-a.1 else bound < b.1-a.1)))

theorem allFive :
    atLimit Promethium none = true ∧ atLimit Samarium none = true ∧
    atLimit Europium (some 14) = true ∧ atLimit Gadolinium none = true ∧
    atLimit Terbium none = true := by decide +kernel

/-- For every checked pair, every smaller differential-error budget leaves a strictly increasing step. -/
theorem strictlyForwardBelow {xs : List Reading} {contact : Option Nat} {k : Nat}
    (ok : atLimit xs contact = true) (h0 : 0<k) (hk : k<xs.length)
    {d p q : Rat} (hd : d<limit) (hp : p≤1) (hq : -1≤q) (diff : p-q≤d) :
    let a := xs[k-1]!
    let b := xs[k]!
    a.1+a.2*p < b.1+b.2*q := by
  have row := List.all_eq_true.mp ok k (List.mem_range.mpr hk)
  simp only [ite_eq_right (show k≠0 by omega), decide_eq_true_eq] at row
  have cut : adverse (xs[k-1]!).2 (xs[k]!).2 limit ≤ (xs[k]!).1-(xs[k-1]!).1 := by
    split at row <;> grind
  have u : 0<(xs[k-1]!).2 := row.1
  have v : 0<(xs[k]!).2 := row.2.1
  have a := adverseBound (show 0≤(xs[k-1]!).2 by grind) (show 0≤(xs[k]!).2 by grind) hp hq diff
  have dec := growsWithDifference u v hd
  grind

theorem atThreshold {xs : List Reading} {contact : Option Nat} {k : Nat}
    (ok : atLimit xs contact = true) (h0 : 0<k) (hk : k<xs.length)
    {p q : Rat} (hp : p≤1) (hq : -1≤q) (diff : p-q≤limit) :
    let a := xs[k-1]!
    let b := xs[k]!
    a.1+a.2*p ≤ b.1+b.2*q ∧ (a.1+a.2*p = b.1+b.2*q → contact=some k) := by
  have row := List.all_eq_true.mp ok k (List.mem_range.mpr hk)
  simp only [ite_eq_right (show k≠0 by omega), decide_eq_true_eq] at row
  have hb := adverseBound (show 0≤(xs[k-1]!).2 by grind) (show 0≤(xs[k]!).2 by grind) hp hq diff
  split at row <;> grind

theorem europiumIsReference : Europium[13]! = ((263,14):Reading) ∧
    Europium[14]! = ((281,14):Reading) := by decide +kernel

/-- The absolute bound |p−q| ≤ d is represented by the two explicit inequalities. -/
theorem sharpEuropium (d : Rat) (_h0 : 0≤d) (h2 : d≤2) :
    (∃ p q : Rat, -1≤p ∧ p≤1 ∧ -1≤q ∧ q≤1 ∧ -d≤p-q ∧ p-q≤d ∧
      281+14*q < 263+14*p) ↔ limit < d := by
  unfold limit
  constructor
  · rintro ⟨p,q,h⟩
    grind
  · intro hd
    exact ⟨d/2,-d/2,by grind⟩

theorem europiumContact : (263:Rat)+14*(9/14) = 272 ∧
    (281:Rat)-14*(9/14) = 272 ∧ (9:Rat)/14 - (-(9:Rat)/14) = limit := by
  decide +kernel

#print axioms adverseBound
#print axioms adverseAttained
#print axioms growsWithDifference
#print axioms allFive
#print axioms strictlyForwardBelow
#print axioms atThreshold
#print axioms europiumIsReference
#print axioms sharpEuropium
#print axioms europiumContact

end ElementPaper.Batch13.SharedError
