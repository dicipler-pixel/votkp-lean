import BariumNeodymium

namespace ElementPaper.Batch12.Window

open VOTKP.NearestPair
open ElementPaper.Batch11 (Energy)

structure Rung where
  z : Nat
  k : Nat
  a : Energy
  b : Energy

structure Range where
  lo : Rat
  hi : Rat
  outside : Bool
  deriving DecidableEq, Inhabited

/-- Closed input interval, strict comparison with the proposed forward cutoff. -/
def Fits (rows : List Range) (cut : Rat) : Prop :=
  ∀ row ∈ rows, ∀ value : Rat, row.lo ≤ value → value ≤ row.hi →
    decide (cut < value) = row.outside

def separated (x : Range) (l u : Rat) :=
  if x.outside then decide (u ≤ x.lo) else decide (x.hi ≤ l)

theorem sharpRangeWindow (rows : List Range) (p q : Range)
    (hp : p ∈ rows) (hq : q ∈ rows)
    (hpok : p.lo ≤ p.hi ∧ p.outside = false) (hqok : q.lo ≤ q.hi ∧ q.outside = true)
    (sep : rows.all (fun x => separated x p.hi q.lo) = true) (c : Rat) :
    Fits rows c ↔ p.hi ≤ c ∧ c < q.lo := by
  constructor
  · intro h
    have a := h p hp p.hi hpok.1 (by grind)
    have b := h q hq q.lo (by grind) hqok.1
    rw [hpok.2] at a
    rw [hqok.2] at b
    grind
  · rintro ⟨hl,hu⟩ x hx value lo hi
    have h := List.all_eq_true.mp sep x hx
    cases e : x.outside <;> simp [separated, e] at * <;> grind

def rungs (atoms : List (List (Option Energy))) : List Rung :=
  atoms.zipIdx.flatMap fun (atom,i) =>
    (atom.zip atom.tail).zipIdx.filterMap fun ((a,b),k) => do
      return ⟨i+1,k,← a,← b⟩

def point (r : Rung) : Range :=
  ⟨r.b.e / r.a.e, r.b.e / r.a.e, Batch11.outside r.a.e r.b.e⟩

def face? (r : Rung) : Option Face := do
  return ⟨r.a.e, ← r.a.unc, r.b.e, ← r.b.unc⟩

def box (r : Rung) : Option Range := do
  let f ← face? r
  return ⟨endpointLo f, endpointHi f, Batch11.outside r.a.e r.b.e⟩

def stable (r : Rung) : Bool :=
  match face? r with
  | none => true
  | some f => if Batch11.outside r.a.e r.b.e then admitsOutside f else admitsInside f

/-- Global squared-wall stability is a separate check from fitting the central labels with a cutoff. -/
theorem stabilityMeaning {r : Rung} {f : Face} (hf : face? r = some f)
    (ok : stable r = true) {a b : Rat} (h : Admits f a b) :
    (Batch11.outside r.a.e r.b.e = true → (1:Rat)/2 < power a b) ∧
    (Batch11.outside r.a.e r.b.e = false → power a b < (1:Rat)/2) := by
  cases c : Batch11.outside r.a.e r.b.e <;> simp [stable, hf, c] at ok ⊢
  · exact interiorForEveryRealization ok h
  · exact exteriorForEveryRealization ok h

def ofReadings (ea : Reading) (ies : List Reading) : List (Option Energy) :=
  (ea :: ies).map fun (v,u) => some ⟨v, some u⟩

def oldAtom (ea : Option Energy) (ies : List Rat) (us : List (Option Rat)) : List (Option Energy) :=
  ea :: (ies.zip us).map (fun (v,u) => some ⟨v,u⟩)

end ElementPaper.Batch12.Window
