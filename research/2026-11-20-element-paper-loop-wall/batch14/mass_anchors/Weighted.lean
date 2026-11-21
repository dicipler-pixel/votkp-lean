import ShapeScale

namespace ElementPaper.MassAnchors.Weighted

/-- At the same ionic charge, compare the higher-Z and lower-Z next ionization
energies. Its ordering is chosen for Q = M(higher Z)−M(lower Z). -/
def paired (higher lower : Rat) := reflect lower higher

theorem twoSpeciesClock (higher lower : Rat) (h : 0<lower) :
    paired higher lower = reflect 1 (higher/lower) := by
  have eq := scaleReflection 1 (higher/lower) lower h
  rw [Rat.mul_one, anchoredStep lower higher h] at eq
  exact eq

theorem weightedIncrement (higher lower : Rat) (h : higher+lower ≠ 0) :
    paired higher lower * (higher+lower) = higher-lower := by
  exact Rat.div_mul_cancel h

theorem exchange (higher lower : Rat) :
    paired lower higher = -paired higher lower := by
  unfold paired reflect
  grind

theorem signOfIncrement {higher lower : Rat} (h : 0<higher+lower) :
    (0 < paired higher lower ↔ lower < higher) ∧
    (paired higher lower < 0 ↔ higher < lower) := by
  unfold paired reflect
  rw [Rat.lt_div_iff h, Rat.div_lt_iff h]
  grind

/-- The removed-electron rest-energy term cancels at equal charge. -/
theorem chargeCancels (mH mL electronLoss h l : Rat) :
    (mH-electronLoss+h) - (mL-electronLoss+l) = (mH-mL)+(h-l) := by grind

def weightedSum : List (Rat × Rat) → Rat
  | [] => 0
  | (a,b)::rs => paired a b * (a+b) + weightedSum rs

def energyDifference : List (Rat × Rat) → Rat
  | [] => 0
  | (a,b)::rs => a-b + energyDifference rs

/-- Valid for any finite initial segment and any independently supplied mass anchor. -/
theorem anchoredSum (q : Rat) (rs : List (Rat × Rat))
    (h : ∀ r ∈ rs, r.1+r.2 ≠ 0) :
    q+weightedSum rs = q+energyDifference rs := by
  have eq : weightedSum rs = energyDifference rs := by
    induction rs with
    | nil => rfl
    | cons r rs ih =>
      rcases r with ⟨a,b⟩
      have thisRow : a+b ≠ 0 := h (a,b) (by simp)
      have tail := ih (fun x hx => h x (by simp [hx]))
      simp only [weightedSum,energyDifference,weightedIncrement a b thisRow,tail]
  rw [eq]

/-- A single-atom squared-wall crossing is not required for either computed
change of sign of the cumulative archive-based mass ordering. -/
theorem holmiumDysprosiumStep :
    paired 5611 12081 = -3235/8846 ∧
    paired 5611 12081*(5611+12081) = -6470 ∧
    2*(paired 5611 12081)^2 < 1 ∧
    (1951.406439:Rat) + paired 5611 12081*(5611+12081) = -4518.593561 := by
  decide +kernel

theorem leadThalliumStep :
    paired 24938.2 96783.2 = -359225/608607 ∧
    paired 24938.2 96783.2*(24938.2+96783.2) = -71845 ∧
    2*(paired 24938.2 96783.2)^2 < 1 ∧
    (37544.7904516:Rat) + paired 24938.2 96783.2*(24938.2+96783.2) = -34300.2095484 := by
  decide +kernel

/-- The next paired step is positive, while the total same-charge ground-state
mass difference stays negative. Its sign gives a change in Q, not Q itself. -/
theorem leadThalliumLastStep :
    0 < paired 99491.8 98592.12 ∧
    paired 99491.8 98592.12*(99491.8+98592.12) = 899.68 ∧
    (-34300.2095484:Rat) + 899.68 = -33400.5295484 ∧ (-33400.5295484:Rat)<0 := by
  decide +kernel

theorem leadExcitedRelease :
    (33400.5295484:Rat) - 2329 = 31071.5295484 := by decide +kernel

end ElementPaper.MassAnchors.Weighted

#print axioms ElementPaper.MassAnchors.Weighted.twoSpeciesClock
#print axioms ElementPaper.MassAnchors.Weighted.weightedIncrement
#print axioms ElementPaper.MassAnchors.Weighted.exchange
#print axioms ElementPaper.MassAnchors.Weighted.signOfIncrement
#print axioms ElementPaper.MassAnchors.Weighted.chargeCancels
#print axioms ElementPaper.MassAnchors.Weighted.anchoredSum
#print axioms ElementPaper.MassAnchors.Weighted.holmiumDysprosiumStep
#print axioms ElementPaper.MassAnchors.Weighted.leadThalliumStep
#print axioms ElementPaper.MassAnchors.Weighted.leadThalliumLastStep
#print axioms ElementPaper.MassAnchors.Weighted.leadExcitedRelease
