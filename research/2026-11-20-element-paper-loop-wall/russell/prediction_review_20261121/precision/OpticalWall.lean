/- Real coherent Jones map against a Stokes-intensity measurement of the
   elemental two-face transfer test. These are rational algebraic identities.
   A real instrument requires separate tests of coherence, phase and calibration.
   No imports beyond Lean core. -/
namespace Beasley.OpticalWall

structure PortMap where
  p : Rat
  q : Rat
  r : Rat
  s : Rat

def tr (k : PortMap) := k.p + k.s
def det (k : PortMap) := k.p*k.s - k.q*k.r
def stokesI (k : PortMap) := (k.p*k.p+k.q*k.q+k.r*k.r+k.s*k.s)/2
def stokesQ (k : PortMap) := (k.p*k.p-k.q*k.q-k.r*k.r+k.s*k.s)/2
def stokesU (k : PortMap) := k.p*k.s+k.q*k.r
def stokesV (k : PortMap) := k.p*k.s-k.q*k.r
def contrast (k : PortMap) := stokesI k + stokesQ k + stokesU k - 3 * stokesV k
def scalar (a : Rat) (k : PortMap) : PortMap := ⟨a*k.p,a*k.q,a*k.r,a*k.s⟩

theorem opticalDiscriminant (k : PortMap) : contrast k = tr k * tr k - 4*det k := by
  simp [contrast, stokesI, stokesQ, stokesU, stokesV, tr, det]
  grind

theorem scaleLaw (a : Rat) (k : PortMap) : contrast (scalar a k) = (a*a)*contrast k := by
  simp [opticalDiscriminant,tr,det,scalar]
  grind

theorem noPhaseSign (k : PortMap) : contrast (scalar (-1) k) = contrast k := by
  rw [scaleLaw]
  grind

/-- A quarter-turn maintains unit intensity for each linear axis and is elliptic. -/
theorem rotationControl : contrast ⟨0, -1, 1, 0⟩ = -4 := by simp [opticalDiscriminant,tr,det] <;> grind

/-- Losing the V channel would assign a false positive to the identity. -/
theorem missingVControl : contrast ⟨1,0,0,1⟩ = 0 ∧
    0 < stokesI ⟨1,0,0,1⟩ + stokesQ ⟨1,0,0,1⟩ + stokesU ⟨1,0,0,1⟩ := by simp [opticalDiscriminant,tr,det,stokesI,stokesQ,stokesU] <;> grind

#print axioms opticalDiscriminant
#print axioms scaleLaw
#print axioms noPhaseSign
#print axioms rotationControl
#print axioms missingVControl
end Beasley.OpticalWall
