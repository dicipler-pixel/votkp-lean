import Std

namespace VOTKP.RankFlow

/-- Scalar count and overlap premises supplied by the projection argument. -/
structure Fibre where
  source : Rat
  target : Rat
  retained : Rat
  sourceBound : retained ≤ source
  targetBound : retained ≤ target

def charge (f : Fibre) : Rat := max 0 (f.source - f.target)
def loss (f : Fibre) : Rat := f.source - f.retained

theorem fibre_charge_le_loss (f : Fibre) : charge f ≤ loss f := by
  obtain ⟨src, dst, o, hs, ht⟩ := f
  simp [charge, loss]
  grind

theorem total_charge_le_loss (fibres : List Fibre) :
    (fibres.map charge).sum ≤ (fibres.map loss).sum := by
  induction fibres with
  | nil => decide
  | cons head tail ih =>
    have := fibre_charge_le_loss head
    simp only [List.map_cons, List.sum_cons]
    grind

/-- A directed edge counts when an occupied source is shifted to an empty target. -/
def edge (src dst : Bool) : Nat := if src && !dst then 1 else 0

theorem fixed_self_edge (x : Bool) : edge x x = 0 := by cases x <;> decide

/-- An unresolved vertex between opposite fixed neighbours preserves the directed count. -/
theorem opposite_neighbours (x fill : Bool) :
    edge x fill + edge fill (!x) = edge x (!x) := by
  cases x <;> cases fill <;> decide

/-- A translation between identical occupied ranks can still lose orbital overlap. -/
theorem constant_rank_can_lose :
    let f : Fibre := ⟨1,1,0,by decide,by decide⟩
    charge f = 0 ∧ loss f = 1 := by decide +kernel

/-- Symbols 0, 1, 2 mean empty, occupied, or either. -/
def fillings : List Nat → List (List Bool)
  | [] => [[]]
  | n :: ns =>
    let tails := fillings ns
    match n with
    | 0 => tails.map (false :: ·)
    | 1 => tails.map (true :: ·)
    | 2 => tails.map (false :: ·) ++ tails.map (true :: ·)
    | _ => []

def cyclicExits (word : List Bool) : Nat :=
  (word.zipWith edge (word.drop 1 ++ word.take 1)).sum

structure Necklace where
  word : List Nat
  multiplicity : Nat
  exits : Nat

def checkNecklace (c : Necklace) : Bool :=
  !(fillings c.word).isEmpty && (fillings c.word).all (fun w => cyclicExits w == c.exits)

def charged (xs : List Necklace) : Nat := (xs.map (fun c => c.multiplicity*c.exits)).sum

def patterns110 : List Necklace :=
  [⟨[0], 347, 0⟩,
   ⟨[0, 1], 1931, 1⟩,
   ⟨[0, 1, 0, 1], 2, 2⟩,
   ⟨[0, 2, 1, 2], 24, 1⟩]

theorem all_tie_choices_110 :
    patterns110.all checkNecklace = true ∧
    (patterns110.map Necklace.multiplicity).sum = 2304 ∧ charged patterns110 = 1959 := by
  decide +kernel

def patterns200 : List Necklace :=
  [⟨[0], 61, 0⟩,
   ⟨[0, 1], 1685, 1⟩,
   ⟨[0, 1, 0, 1], 542, 2⟩,
   ⟨[0, 2, 1, 2], 8, 1⟩,
   ⟨[0, 2, 1, 2, 0, 2, 1, 2], 8, 2⟩]

theorem all_tie_choices_200 :
    patterns200.all checkNecklace = true ∧
    (patterns200.map Necklace.multiplicity).sum = 2304 ∧ charged patterns200 = 2793 := by
  decide +kernel

def patterns222 : List Necklace :=
  [⟨[0, 1], 559, 1⟩,
   ⟨[0, 1, 0, 1], 927, 2⟩,
   ⟨[0, 1, 0, 1, 0, 1], 794, 3⟩,
   ⟨[0, 1, 0, 2, 1, 0, 1, 2], 24, 3⟩]

theorem all_tie_choices_222 :
    patterns222.all checkNecklace = true ∧
    (patterns222.map Necklace.multiplicity).sum = 2304 ∧ charged patterns222 = 4867 := by
  decide +kernel

theorem equal_neighbours_can_change (x : Bool) :
    edge x (!x) + edge (!x) x ≠ edge x x := by
  cases x <;> decide

def piUpper : Rat := 31415926536 / 10000000000

/-- Per-electron rank term with the 5.700 Å cell and a conservative upper bound on π. -/
def bound48 (exits hklNormSq : Nat) : Rat :=
  (exits : Rat) * (48 * (57/10))^2 / (55296 * 4 * piUpper^2 * hklNormSq)

theorem finite_110_lower : (3358792/100000 : Rat) < bound48 1959 2 := by decide +kernel
theorem finite_200_lower : (2394361/100000 : Rat) < bound48 2793 4 := by decide +kernel
theorem finite_222_lower : (1390781/100000 : Rat) < bound48 4867 12 := by decide +kernel

#print axioms fibre_charge_le_loss
#print axioms total_charge_le_loss
#print axioms fixed_self_edge
#print axioms opposite_neighbours
#print axioms constant_rank_can_lose
#print axioms all_tie_choices_110
#print axioms all_tie_choices_200
#print axioms all_tie_choices_222
#print axioms equal_neighbours_can_change
#print axioms finite_110_lower
#print axioms finite_200_lower
#print axioms finite_222_lower
end VOTKP.RankFlow
