# Occupied pseudo-orbitals in Wigner–Seitz cells

**DERIVED.** For one atom per primitive cell, take a Wigner–Seitz cell Ω and all N distinct translations in a Born–von Kármán supercell. A common twist of an otherwise uniform full k mesh is allowed. Normalize the full Bloch waves φ_kn in the primitive cell. Their restriction to Ω obeys G_kn,km = δ_nm after orthogonalization in the chosen inner product. The supercell wave is φ_kn/√N. The following spin factor of two assumes identical, independent spin copies.

For one spin, the real-space occupied projector restricted from site R to site 0 has kernel
```
P_0R(x,y) = (1/N) Σ_{k,n occupied} φ_kn(x) φ_kn(y)* exp(−ik·R),    x,y in Ω.
G_kn,lm = ∫_Ω φ_kn(x)* φ_lm(x) dx .
```
Squaring the kernel and integrating over both cell coordinates gives
```
X_R = (2/N²) Σ_{kn,lm occupied} exp[i(k−l)·R] |G_kn,lm|² .
```
Complex conjugating this expression yields the same real answer. Thus the sign convention for the Fourier phase is harmless for this scalar. Summing over the N distinct translations enforces k=l. The within-k Gram identity leaves
```
Σ_R X_R = (2/N) Σ_k n_occ(k),          Σ_{R≠0} X_R = B = (2/N) Σ_k n_occ(k) − X_0 .
```
Both equalities refer to a complete translated partition of a one-site primitive lattice. A multi-site unit cell requires site-specific traces and a sum over every other sublattice site as well as cell translations. A spinor or spin-polarized computation requires the actual spin-resolved or spinor projector.

**DERIVED · occupation and norm controls.** For orbital occupations f in [0,1] per spin, replace each ordered-pair factor by f_kn f_lm. Then Σ_R X_R = (2/N) Σ f², while the local charge is (2/N) Σ f. The charge-minus-X0 expression contains an additional (2/N) Σ f(1−f). Use a binary occupied spectral projector for the stated sum rule, or quantify this defect. In a finite rubidium mesh choose the spin-degenerate electron count, check any degeneracy straddling the cutoff, and report twist and size dependence. A full subspace selected at every k can have finite intercell weight; a complete site-localized basis filled in its entirety instead gives X_R=0 for R≠0 and B=0. An effectively zero B makes shell fractions indeterminate.

**DERIVED · numerical controls.**

- Use the full uniformly weighted k grid. Check the actual output k list, grid difference structure, and spin/occupation counts. Symmetry-reduced stars require the corresponding rotated wavefunctions and phases before pair contractions. A band path has a different measure.
- Integrate full Bloch waves over the same physical Ω for every k. For cell-periodic FFT output u_kn, include exp[i(l−k)·x] in G_kn,lm. Translating a wrapped FFT grid point back into the chosen Wigner–Seitz cell requires the correct full-wave translation phase. Recompute X_R under an equivalent cell origin with all coordinates transformed consistently.
- Select the intended eigenstates first. Plain pseudo-L² orthogonalization within each occupied span produces a well-defined pseudo-orbital projector. Mixing selected and excluded states during orthogonalization can change that span. In PAW or ultrasoft datasets the code's generalized eigenvectors have an augmented overlap; the proposed plain pseudo-L² spatial observable and a reconstructed all-electron observable can differ. Report pseudopotential version, basis/cutoff, bands and representation. Compare outer-only with all semicore plus valence *per material* when feasible.
- Require a small within-k Gram defect, full-k sum-rule residual, negligible imaginary leakage, nonnegative X_R and agreement X_R=X_−R. A finite mesh folds real-space translations. Count each *distinct* neighbour and show that all physical nearest neighbours are distinct modulo the supercell. Double the mesh or compare consecutive grid sizes, test at least two twists, converge the real-space representation, and cross-check one shell against an explicit spatial sum. Summing over the full finite supercell is essential for the sum-rule check.
- For n equivalent nearest neighbours the cutoff X_R>B/(3n) is equivalent to a shell share Σ_nn X_R/B>1/3. A finite twist can split symmetry-related values. Then a shell mean passing does not imply every bond passes. Report shell sum, direction range, B, absolute X and the number of contributing neighbours. A bulk transport response is a separate calculation.
- Compare a known synthetic projector and a completely filled local basis before interpreting atomic outputs. Replacing a missing wavefunction with an LDOS, charge density or integrated band character cannot reconstruct the required off-diagonal overlap; these scalars omit the relative phases.

**Executed control.** The accompanying NumPy check uses eight twisted momenta and heterogeneous occupied ranks, forms the complete orthogonal site basis and the full supercell density matrix, and compares every block to the overlap formula. It also checks invariance under independent occupied-unitary rotations, verifies the fractional-occupation deficit analytically and numerically, and verifies that the completely filled local basis returns B=0. These synthetic controls establish normalization and implementation consistency. Material-dependent X_R requires the actual orbital grids.

[Quantum ESPRESSO input documentation](https://www.quantum-espresso.org/Doc/INPUT_PW.html) · [QE user guide, non-SCF uniform meshes](https://www.quantum-espresso.org/wp-content/uploads/2022/03/pw_user_guide.pdf) · [PAW overlap and orthogonalization](https://www.chem.ucla.edu/dept/Faculty/dxn/pdf/p206_opawsgw.pdf).
