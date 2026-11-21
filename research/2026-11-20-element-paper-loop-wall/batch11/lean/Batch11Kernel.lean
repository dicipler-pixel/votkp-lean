import Std

namespace ElementPaper.Batch11

def outside (a b : Rat) := decide (2*(b-a)^2 > (a+b)^2)
def separates (z l u : Rat) (out : Bool) :=
  if out then decide (u≤z) else decide (z≤l)

theorem agreesAtAnyCut {z l u c : Rat} {out : Bool} (h : separates z l u out = true)
    (hl : l≤c) (hu : c<u) : decide (c<z)=out := by
  cases out <;> simp [separates] at * <;> grind

/-- A cutoff fits every encoded ordinary crossing when its strict forward
comparison reproduces the archive label at every adjacent pair. -/
def Fits (rs : List (Rat × Rat)) (c : Rat) : Prop :=
  ∀ p ∈ rs, decide (c < p.2/p.1) = outside p.1 p.2

theorem sharpWindow (rs : List (Rat × Rat)) (p q : Rat × Rat)
    (hp : p ∈ rs) (hq : q ∈ rs) (pi : outside p.1 p.2 = false) (qo : outside q.1 q.2 = true)
    (sep : rs.all (fun r => separates (r.2/r.1) (p.2/p.1) (q.2/q.1) (outside r.1 r.2)) = true)
    (c : Rat) : Fits rs c ↔ p.2/p.1 ≤ c ∧ c < q.2/q.1 := by
  constructor
  · intro h
    have a := h p hp
    have b := h q hq
    grind
  · rintro ⟨hl,hu⟩ r hr
    exact agreesAtAnyCut (List.all_eq_true.mp sep r hr) hl hu

def silver := (7.576234 / 1.30447 : Rat)
def silicon := (8.15168 / 1.3895212 : Rat)
def nitrogen := (552.06741 / 97.8901 : Rat)
def carbon := (392.09056 / 64.49352 : Rat)
def cesium := (23.15745 / 3.89390572743 : Rat)

def centralTest (l u : Rat) (e : List Rat) : Bool :=
  (e.zip e.tail).all fun (a,b) =>
    decide (0<a ∧ a<b ∧ 2*(b-a)^2 ≠ (a+b)^2) && separates (b/a) l u (outside a b)

structure Energy where
  e : Rat
  unc : Option Rat
  deriving Inhabited

def ratioBox (a b : Energy) : Option (Rat × Rat) := do
  let da ← a.unc
  let db ← b.unc
  guard (0≤da ∧ 0≤db ∧ 0 < a.e-da ∧ 0 < b.e-db)
  return ((b.e-db)/(a.e+da),(b.e+db)/(a.e-da))

inductive BoxCall where | inside | outside | missing | invalid
  deriving DecidableEq

/-- The inside case needs its upper box edge below silver, the outside case
its lower box edge above silicon. With these exact tests every tested
ratio has the same strict-cutoff call for the whole prior central window. -/
def call (a b : Option Energy) : Option BoxCall := do
  let a ← a
  let b ← b
  let some (lo,hi) := ratioBox a b | return .missing
  if outside a.e b.e then
    return if silicon≤lo then .outside else .invalid
  else
    return if hi≤silver then .inside else .invalid

def labels (e : List (Option Energy)) := (e.zip e.tail).map fun (a,b) => call a b

/-- The exact finite cuts used for the combined and ordinary-only comparisons. -/
theorem orderedEndpoints :
    nitrogen < silver ∧ silver ≤ (7576259/1304450 : Rat) ∧
    (7576259/1304450 : Rat)<(6270500/1068863 : Rat) ∧ (6270500/1068863 : Rat)≤silicon ∧
    silicon < cesium ∧ cesium < 6 ∧ 6 < carbon ∧ outside 3.89390572743 23.15745 = true := by
  decide +kernel

end ElementPaper.Batch11
