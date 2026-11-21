# An ambient-knot and junction test on two measured high-pressure structures

**MEASURED INPUT.** Sm at 175(2) GPa and Tb at 302 GPa have the same reported Fddd structure with eight atoms per conventional cell, origin choice 1 site 8a. Their refined axes differ. The Tb refinements at 302 GPa and the highest observed pressure (308 GPa) are distinct. The lower-pressure terbium structure has *sixteen* atoms per cell with the same space-group symbol. The two refinements and quoted uncertainties are in [pressure_structures.csv](pressure_structures.csv). [Sm diffraction, 2020](https://doi.org/10.1103/PhysRevB.101.174109) · [Tb diffraction, 2025](https://doi.org/10.1103/r3zx-k97x)

## Which edges define the path?

**HYPOTHESIS / failure condition.** Select all and only the contacts at the shortest distance. If the next distance overlaps within the cell-parameter boxes, the construction does not select a robust graph. If two paths meet only after a lattice translation, do not call the path a closed knot in Euclidean space. These are alternative choices to a covalent-bond or all-electron-density graph. Fddd symmetry alone does not select this graph.

| Element at measured pressure | Shortest shell (Å) | Second shell (Å) | Third shell (Å) | Force-separated first-to-second distance across boxes (Å) | Volume per atom (Å³) |
|---|---:|---:|---:|---:|---:|
| Sm, 175(2) GPa | 4 × 2.475825 | 2 × 2.522700 | 4 × 2.602630 | ≥0.046436 | 12.096305 |
| Tb, 302 GPa | 4 × 2.318727 | 2 × 2.389300 | 4 × 2.488071 | ≥0.068761 | 10.203761 |

**DERIVED.** The four F-centering sites and the same sites shifted by (¼,¼,¼) give the eight sites. From the origin the four nearest vectors are (±a,±b,±c)/4 with an even number of minus signs. From the other sublattice they reverse. The squared distances depend linearly on a²,b²,c². Check all corners to exclude reordered shells; a simple lower bound excludes the translations outside the enumeration window. Atomic volume is abc/8. The two measured embeddings differ by a nonsingular positive diagonal map. [Neighbour distances, full intervals and offsets](pressure_contacts.csv) · [reproduce geometry and rings](pressure_rings.py)

**DERIVED, VOTKP v1.** From every site there are zero simple closed three-, four- or five-edge cycles and exactly twelve six-edge cycles up to reversal. Translation and inversion relate all sites. Each of the twelve uses three of the four available tetrahedral directions. Project in the direction of the unused bond in the integer coordinate frame. For every oriented edge, all other four projected vertices are on the same strict side, with consistent sense. The resulting hexagon is strictly convex and hence simple. The 3D loop is therefore a graph of height over a planar simple polygon. Continuously reducing these heights to zero gives an isotopy through embedded loops. The positive diagonal map transports this disk-bounding loop to each measured embedding. **All these shortest cycles are unknots.** For the usual normalized HOMFLY-PT, Jones and Alexander polynomials of a single unknot the value is 1. No fitted knot polynomial was required. [The twelve explicit loops and certificates](shortest_contact_rings.csv) · [Lean check](PressureRingChecks.lean) · [axiom output](pressure_lean_output.txt)

**DERIVED / scope.** The Lean kernel checks the enumerated graph, 24 oriented shortest loops and the finite determinant predicates. The assignment to the measured phases and the ambient knot conclusion use the crystallographic inputs and geometric argument above. Longer cycles, multiple linked cycles and cycles in a larger graph obtained by including the next contact shell are separate questions. A universal atom-specific knot or element-specific Jones polynomial does not follow from this example.

## What can an occupied-space projector distinguish?

**HYPOTHESIS / failure condition.** Probe whether the nearest-contact link distinguishes the two recorded material geometries or a gap. Use one spinless orbital per measured site, only the four shortest links, the same positive hopping magnitude t, and one occupied valence band (half filling). Two unequal values of the normalized projector at fixed reduced Hamiltonian would disprove the scale-invariance statement. A mass with a positive gap and a link above threshold refutes the assertion that passing requires a gapless band. The real metals have more orbitals, including f states. A staggered onsite mass below is a deliberate broken-sublattice-symmetry control.

**DERIVED.** In primitive reciprocal coordinates write

```math
 f=1+e^{ik_1}+e^{ik_2}+e^{ik_3},\quad s=|f|^2,\quad m=\Delta/t,
 \qquad H/t=\begin{pmatrix}m&f\\\bar f&-m\end{pmatrix}.
```

**DERIVED.** Eigenvalues are ±t√(m²+s). The normalized integration measure on the cell's Brillouin zone becomes uniform on three phase angles. The reciprocal Jacobian cancels against the normalized zone volume. At m=0 the zeros of f have measure zero. A pure change in t at m=0, or at fixed Δ/t, leaves the occupied spectral projector unchanged. Changing only from the Sm axes to the Tb axes leaves the function of reduced k unchanged in this model. Differentiating a band energy with respect to *physical* k introduces reciprocal-axis factors again, so identical links do not imply identical group velocities or conductivity.

**DERIVED.** Let ⟨·⟩ denote the zone average and E=√(m²+s). The four individual nearest bonds have equal amplitudes in the continuum by permutation symmetry of the model's four hopping phases. To see this, embed the three relative phases in four independent unit phases; dividing by the first gives the same joint distribution and restores manifest permutation symmetry. Summing the four Fourier coefficients in the occupied projector then gives

```math
 C_A=(1-\langle m/E\rangle)/2,\quad
 B=C_A(1-C_A)=(1-\langle m/E\rangle^2)/4,\quad
 |P_{AB}|=\langle s/E\rangle/8,\quad X=|P_{AB}|^2.
```

**DERIVED, an all-gap test.** The surviving phase terms give ⟨s⟩=4 and ⟨s²⟩=28. For the fourth moment, match two positive phases against two negative ones. Four doubled labels match one way each, and twelve ordered unequal label pairs match two ways each: 4+2·12=28. Apply Jensen's inequality to the convex function u↦(m²+u)⁻¹ᐟ² under the probability weight s/⟨s⟩. Its weighted mean of s is 28/4=7. Thus ⟨s/E⟩≥4/√(m²+7). Apply Jensen again with uniform weight for |m|>0 to get |⟨m/E⟩|≥|m|/√(m²+4). At m=0 use C_A=½ directly. These are scalar inequalities on positive phase averages, independent of any metric assumption about the ball. Hence

```math
 X\geq\frac1{4(m^2+7)} >
 \frac1{12(m^2+4)}\geq\frac{B}{3\cdot4}.
```

**DERIVED.** The strict middle inequality follows from 12(m²+4)−4(m²+7)=8m²+20>0. The criterion passes for every finite m. The band gap is exactly 2|Δ| because f can vanish (take phases −1,1,−1). A nearest-contact link can pass in a model with arbitrarily large gap. At m→∞ both sides tend to zero; replacing the finite-m statement by a strict statement at the atomic limit would fail.

| m | X, 192³ grid | Cutoff B/12 | Four links' share of B | Exact gap/t |
|---:|---:|---:|---:|---:|
| 0 | 0.0505739641 | 0.0208333333 | 0.8091834259 | 0 |
| 1 | 0.0387971774 | 0.0148576427 | 0.8704202105 | 2 |

**DERIVED, numerical check.** Offset grids 24³ through 192³ avoid the m=0 nodes. The smallest *sampled* gap approaches the exact gap from above. The two independent moment checks agree with 4 and 28 to numerical precision on every grid. Finite grids average the four nearly equivalent discrete bonds; continuum symmetry equates each one. [Python/NumPy calculation](contact_projector.py) · [numerical convergence](contact_projector.csv)

**HYPOTHESIS, next experiment.** Use an orbital-resolved electronic Hamiltonian at the actual pressure for each element, with spin, actual orbital filling, further shells and spin–orbit effects. Compare link tails and measured transport only at the same pressure/temperature; a normal-state room-temperature ambient resistivity cannot adjudicate a 175 or 302 GPa insulating gap. Sm and Tb need not then have equal X. Independent data for their pressure-dependent orbital mixing or longer-range hopping would break the present test's exact degeneracy.

**DERIVED, formal scope.** [ContactMomentChecks.lean](ContactMomentChecks.lean) checks the two phase-matching counts in the kernel without axioms and the positive denominator ordering for each nonnegative rational mass-squared using the three standard axioms. The Bloch reduction, scalar Jensen bounds and real-variable extension are analytic arguments above. [Lean axiom log](contact_lean_output.txt)
