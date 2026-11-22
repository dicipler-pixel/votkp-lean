# Which coordinate restores the heavy one-electron state?

Jeromie Beasley's signed step r=ln(B₂/B₁) and an independent symmetric scale σ=√(B₁B₂)/(mₑc²) reconstruct the two dimensionless bindings e₁=σ exp(−r/2) and e₂=σ exp(r/2). The scale here is named only for this comparison; it is unrelated to the atomic-screening σ_Z defined in the principal manuscript. Swapping endpoints flips r and leaves the scale fixed. Recording this one absolute energy in addition to r restores the information the scale-only counterexample needs. The pair is equivalent to storing both energies and makes no new experimental degrees of freedom.

In the point-nucleus Dirac 1s model (fixed electron mass and nuclear centre), write gᵢ=1−eᵢ, kᵢ=√[eᵢ(2−eᵢ)], sᵢ=kᵢ/(1+gᵢ), using electron Compton-length units. The large and small reduced-radial components share uᵢ(t)=Nᵢ t^gᵢ exp(−kᵢt) with relative coefficient −sᵢ; Nᵢ=(2kᵢ)^(gᵢ+1/2)/√[(1+sᵢ²)Γ(2gᵢ+1)]. For common angular spinors and orientation the overlap is

    S=N₁N₂(1+s₁s₂) Γ(1+g₁+g₂)/(k₁+k₂)^(1+g₁+g₂).

The Γ with an argument in this expression is Euler's gamma function; its argument is a radial integral exponent. Keep it distinct from the peel reflection. The formula includes both spinor components. The orbital fidelity is S². Under endpoint exchange S is invariant.

**A fixed-ratio counterexample.** Hold B₂/B₁=35/6 exactly. Increasing B₂/(mₑc²) from 0.07 to 0.35 changes the fidelity from 0.551060 to 0.475412. A root solver locates an intervening half-fidelity point at approximately 0.26364446. These are continuous *Coulomb model charges* obtained by inverting the point Dirac energy. They are not extra elements of fractional atomic number. The low and high examples by themselves prove that one value of the ratio cannot assign the side of the half-fidelity line in this model. Physical isotope masses, extended charge distributions and radiative corrections are separate inputs beyond this Hamiltonian. In the weak-binding limit this expression restores the nonrelativistic same-mass 1s formula.

This provides an element-table design decision with a microscopic reason: preserve absolute thresholds or an equivalent common scale, as well as signed ratios and orbital labels. It is not a claim that the registered loop wall changes location. The independent one-electron overlap probes a different function of energy. The script compares the analytic formula with direct numerical radial quadrature at eight input scales.
