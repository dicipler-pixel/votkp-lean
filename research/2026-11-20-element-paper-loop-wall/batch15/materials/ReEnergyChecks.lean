/- Integer 10^-5 eV units. Only the shared endpoint is canceled; other widths remain. -/
namespace ElementPaper.ReEnergy

/-- The daughter K binding occurs once in the neutral shell sum and once in
    the final one-electron daughter, so its common error cancels identically. -/
theorem endpointCancel (q re osPartial k : Int) : q+re-(osPartial+k)+k=q+re-osPartial := by omega

/-- For any signed combination within the conservative box margin, the direct
    PENTATRAP Q and pinned widths leave the K channel open while the free
    continuum remains closed. Ring and time data are not needed for this sign. -/
theorem re187ChannelBox (k free : Int)
    (hk : 7051668498 ≤ k) (hf : free ≤ -1056756440) : 0<k ∧ free<0 := by omega

/-- The stable 185Re isotope has a closed K-electron channel even with the most
    favourable quoted sign of all electronic and nuclear input errors. -/
theorem re185ChannelBox (k : Int) (h : k ≤ -94014579440) : k<0 := by omega

/-- Evaluate the uncorrelated error budget before applying the sign tests.
    These are data certificates, not a mechanistic theory of half-lives. -/
theorem endpoints :
    let correction : Int := 7031079529
    let width : Int := 226371031
    let osK : Int := 8561442000
    (247090000 + correction - width - 130000 = 7051668498) ∧
    (-101313930000 + correction + width + 41900000 = -94014579440) ∧
    (247090000 + correction - osK = -1283272471) := by decide +kernel

/-- Starting at charge 29 eliminates the shared contribution of the two 29-electron sums. -/
theorem startAtChargedMass (ionic reLow osLow reHigh osHigh : Int) :
    ionic + osLow-reLow + (reLow+reHigh) - (osLow+osHigh) = ionic+reHigh-osHigh := by omega

/-- Measured ionic shift and the archived high-charge budget, now in 0.01 eV units. -/
theorem excitedKWindow :
    let k : Int := 7276101
    let kw : Int := 118469
    let n : Int := 247090
    let nw : Int := 130
    let e : Int := 975600
    let ew : Int := 1900
    (k-e-(kw+ew)=6180132) ∧ (n-e+(nw+ew) = -726480) := by decide +kernel

#print axioms startAtChargedMass
#print axioms excitedKWindow
#print axioms endpointCancel
#print axioms re187ChannelBox
#print axioms re185ChannelBox
#print axioms endpoints
end ElementPaper.ReEnergy
