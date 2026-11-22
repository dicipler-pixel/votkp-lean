# A signed three-state readout in Jeromie's Coulomb-face comparison

Jeromie Beasley's elemental table keeps directed face ratios and the Dirac Time program asks which independent readout can reveal a path that a reduced record misses. The following application specifies all three pure states and an independent quantum observable in the ideal one-electron model. The same-orbital comparison requires a common Hilbert space, centre, axes and reduced mass. It compares scaled wavefunctions prepared for a measurement. A physical sequence that irreversibly loses electrons does not automatically implement their coherent interference.

## A definite sign before a measurement

Take scales α,β,γ = 1,2,4 in units of a common inverse length. In either 2s or 2p the successive binding-energy ratios are 4,4,1/16 around the cycle. Reversal gives the same eigenvalue-origin data for both choices. Let Pᵢ be the prepared orbital projector and B=Tr(P₁P₂P₃). Then B=〈1|2〉〈2|3〉〈3|1〉. Each state phase cancels. All orbitals here admit real radial representatives, so reversing the traversal complex-conjugates B and preserves its real sign. The negative sign is a gauge-invariant phase of π of the three-state product. It does not measure ordinary spatial chirality.

Let h=8αβγ/[(α+β)(β+γ)(γ+α)], and νᵢⱼ=1−3[(αᵢ−αⱼ)/(αᵢ+αⱼ)]². The previously derived radial overlaps give

| Orbital | Cyclic trace B | At (1,2,4) | Proposed ancilla probability (1+B)/2 |
|---|---|---:|---:|
| 1s | h³ | 32768/91125 ≈ +0.359594 | 0.679797 |
| 2s | h³ ν₁₂ν₂₃ν₃₁ | −262144/20503125 ≈ −0.012786 | 0.493607 |
| 2p | h⁵ | 33554432/184528125 ≈ +0.181839 | 0.590920 |

The negative 2s sign comes from the long 4-to-1 face. Each short edge has a positive radial overlap. All three 2p overlaps are positive. This is a comparison where an oriented set of three projectors yields a *different* sign even though the n=2 ionic binding spectra and energy ratios coincide. At all these scales the nuclear charge ratio and energy ratio have distinct meanings. At the actual ordinary peels these three projectors have not been identified.

**Instrument and scoring.** Prepare the three states simultaneously on three registers with mutually calibrated spatial wavefunction bases. A controlled cyclic permutation on their tensor product and an X-basis ancilla reading yield ⟨X⟩=Re B. Measuring all three pairwise transition probabilities successively generally loses this sign. For a genuinely independent test calibrate the states and permutation gate using other settings, then blind the orbital labels and score a 2s output interval below one half and a 2p output interval above one half. The ideal 2s offset from one half is only 0.006393. Distinguish input preparation and readout uncertainties and provide a positive-identical-state control. A calculation on a simulator whose output is generated directly by these formulas only verifies the software. Physically preparing controlled replicas of isolated atomic orbitals at different Coulomb scales is a distinct experimental problem. This page records predictions for a specified quantum protocol, not a result from such an instrument. [Quantum permutation readout, Ekert et al.](https://arxiv.org/abs/quant-ph/0203016)

**A second, generic control.** Form two 3-by-3 Gram matrices with diagonal one, off-diagonal magnitude 1/3, and product sign respectively plus and minus. Their leading minors are positive and their determinants are 20/27 and 16/27, so normalized real vectors realize both. Every pairwise projector fidelity is exactly 1/9 in both realizations, but the three-state traces are +1/27 and −1/27. This demonstrates what the third-order measurement can add to even *complete pairwise magnitude* data. The equal-magnitude example uses abstract normalized real states; the two Coulomb orbitals above need only share the energy-ratio data and have differing pairwise fidelities.

The calculated sign is borne by specified projectors and their mutual preparation. It does not follow from the half-power cutoff alone and does not discriminate the six comparison atomic cutoffs by itself. The source and numeric integrations, physical protocol and counterexample are given so this claim can be tested or rejected independently.
