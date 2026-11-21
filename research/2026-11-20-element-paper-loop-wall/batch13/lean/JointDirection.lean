import BariumNeodymium

namespace ElementPaper.Batch13

open ElementPaper.Batch12 (Reading)
def low (x : Reading) : Rat := x.1-x.2
def high (x : Reading) : Rat := x.1+x.2

def realizes (xs : List Reading) (ys : List Rat) : Bool :=
  decide (xs.length = ys.length) && (List.range xs.length).all
    (fun i => decide (low (xs[i]!) ≤ ys[i]! ∧ ys[i]! ≤ high (xs[i]!)))

private theorem allowedAt {xs : List Reading} {ys : List Rat} (h : realizes xs ys = true)
    {i : Nat} (hi : i < xs.length) : low (xs[i]!) ≤ ys[i]! ∧ ys[i]! ≤ high (xs[i]!) := by
  simp only [realizes, Bool.and_eq_true] at h
  exact of_decide_eq_true (List.all_eq_true.mp h.2 i (List.mem_range.mpr hi))

def reversal (ys : List Rat) (k : Nat) : Bool := decide (0<k ∧ ys[k]! < ys[k-1]!)
def candidate (xs : List Reading) (k : Nat) : Bool := decide (0<k ∧ low (xs[k]!) < high (xs[k-1]!))

def candidates (xs : List Reading) := (List.range xs.length).filter (candidate xs)
def observed (xs : List Reading) (ys : List Rat) := (List.range xs.length).filter (reversal ys)
def contacts (xs : List Reading) := (List.range xs.length).filter
  (fun k => decide (0<k ∧ low (xs[k]!) = high (xs[k-1]!)))

/-- A shared vector filters only indices whose two input ranges overlap strictly. -/
theorem observedFilter {xs : List Reading} {ys : List Rat} (h : realizes xs ys = true) :
    observed xs ys = (candidates xs).filter (reversal ys) := by
  unfold observed candidates
  rw [List.filter_filter]
  apply List.filter_congr
  intro k hk
  cases hr : reversal ys k
  · simp
  · simp
    simp only [reversal, decide_eq_true_eq] at hr
    have hk' := List.mem_range.mp hk
    have hl := allowedAt h hk'
    have hu := allowedAt (i:=k-1) h (by omega)
    simp only [candidate, decide_eq_true_eq]
    grind

/-- A chain has one shared middle energy. The independent extreme for each edge need
not be available to both edges at once. -/
theorem noConsecutiveReversal {xs : List Reading} {ys : List Rat}
    (hl : 14<xs.length) (sep : high (xs[12]!) ≤ low (xs[14]!))
    (h : realizes xs ys = true) : ¬ (reversal ys 13 = true ∧ reversal ys 14 = true) := by
  have l := allowedAt (i:=12) h (by omega)
  have u := allowedAt (i:=14) h hl
  simp only [reversal,decide_eq_true_eq]
  change ¬ ((0<13 ∧ ys[13]! < ys[12]!) ∧ (0<14 ∧ ys[14]! < ys[13]!))
  grind

def subsequences : List Nat → List (List Nat)
  | [] => [[]]
  | x::xs => let tail := subsequences xs; tail ++ tail.map (x::·)

private theorem filteredMember (s : List Nat) (f : Nat → Bool) : s.filter f ∈ subsequences s := by
  induction s with
  | nil => simp [subsequences]
  | cons x xs ih =>
    cases hx : f x
    · simp [hx, subsequences, ih]
    · simp [hx, subsequences, ih]

def possible (xs : List Reading) := (subsequences (candidates xs)).filter
  (fun ks => decide (¬ (13 ∈ ks ∧ 14 ∈ ks)))

/-- Universal direction of the joint result. No other strict-reversal combination
is compatible with a single assignment of levels to all rungs. -/
theorem onlyPossible {xs : List Reading} {ys : List Rat}
    (hl : 14<xs.length) (sep : high (xs[12]!) ≤ low (xs[14]!))
    (h : realizes xs ys = true) : observed xs ys ∈ possible xs := by
  apply List.mem_filter.mpr
  constructor
  · rw [observedFilter h]
    exact filteredMember _ _
  · apply decide_eq_true
    rintro ⟨h13,h14⟩
    exact noConsecutiveReversal hl sep h ⟨(List.mem_filter.mp h13).2,(List.mem_filter.mp h14).2⟩

/-- For a requested strict reversal, use the left upper and right lower corner.
Other levels stay at their central values. -/
def witness (xs : List Reading) (keys : List Nat) : List Rat :=
  xs.zipIdx.map fun (e,i) =>
    if i+1 ∈ keys then high e else if i ∈ keys then low e else e.1

def realizedAll (xs : List Reading) : Bool := (possible xs).all fun keys =>
  let ys := witness xs keys
  realizes xs ys && decide (observed xs ys = keys)

/-- Converse for every encoded row once the finite constructors have passed the kernel. -/
theorem feasibleIff {xs : List Reading} (hl : 14<xs.length)
    (sep : high (xs[12]!) ≤ low (xs[14]!)) (ok : realizedAll xs = true) (keys : List Nat) :
    (∃ ys, realizes xs ys = true ∧ observed xs ys = keys) ↔ keys ∈ possible xs := by
  constructor
  · rintro ⟨ys,h,rfl⟩
    exact onlyPossible hl sep h
  · intro h
    have w := List.all_eq_true.mp ok keys h
    change (realizes xs (witness xs keys) &&
      decide (observed xs (witness xs keys) = keys)) = true at w
    simp only [Bool.and_eq_true, decide_eq_true_eq] at w
    exact ⟨witness xs keys,w⟩

/-- At the stated common uncertainty multiplier, a gap's first contact is where
the lower edge of level k+1 equals the upper edge of level k. -/
def firstScale (xs : List Reading) (k : Nat) (t : Rat) : Bool :=
  (List.range xs.length).all (fun i =>
    if i = 0 then true else
      let a := xs[i-1]!
      let b := xs[i]!
      decide (0 ≤ a.2 ∧ 0 ≤ b.2 ∧ 0 < a.2+b.2 ∧
        (if k=i then b.1-a.1 = t*(a.2+b.2) else t*(a.2+b.2) < b.1-a.1)))

theorem smallerScaleStrict {a b da db w t : Rat} (positive : 0 < da+db)
    (bound : w*(da+db) ≤ b-a) (earlier : t < w) : a+t*da < b-t*db := by
  have h := Rat.mul_lt_mul_of_pos_right earlier positive
  grind

end ElementPaper.Batch13
