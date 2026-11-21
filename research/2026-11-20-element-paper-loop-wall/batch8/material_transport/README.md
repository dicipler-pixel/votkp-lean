# Rubidium and krypton at measured crystal geometries

**Question and failure conditions.** Can a material-specific calculation provide the third observable in §5 of Jeromie Beasley’s element paper? The electronic test for ambient bcc Rb fails if its PBE bands give a gap at its electron count or if the converged intraband response vanishes. The contrasting test for fcc solid Kr fails if a band crosses the chemical potential at its closed-shell filling. Crystal temperature labels the source of the lattice parameter. The electronic calculation uses a static periodic crystal without phonons.

## Electronic structures

**Measured inputs.** The bcc Rb cell uses a conventional lattice parameter of 5.700 Å (297 K, COD 9012876, estimated lattice parameter in this refinement). The fcc Kr cell uses 5.721 Å (58 K, COD 9008471). Each primitive cell contains one atom. The Kr comparison concerns a cold crystal; krypton at room temperature and ambient pressure is gaseous. [Rb refinement](https://www.crystallography.net/cod/9012876.html) · [Kr refinement](https://www.crystallography.net/cod/9008471.html).

**Derived.** Ran Quantum ESPRESSO PWSCF 6.7MaX with scalar-relativistic PSLibrary 1.0.0 PBE PAW potentials, one unpolarised channel with spin degeneracy two. Rb uses nine explicit electrons (4s²4p⁶5s¹), Kr eighteen (3d¹⁰4s²4p⁶). The recorded SHA-256 values in [qe_compare.py](qe_compare.py) are checked against each downloaded UPF before running. Rb has no arbitrary onsite staggering in this calculation. The plane-wave basis and atomic potentials, lattice and electron number determine the bands self-consistently. The runs used a 10⁻⁹ Ry electronic threshold, uniform mesh with equal division counts and zero offsets along the primitive reciprocal vectors, and 6–7 electronic iterations. The plane-wave and charge-density cutoffs, smearing and irreducible k counts are in the two CSVs. [Giannozzi et al. (2017)](https://doi.org/10.1088/1361-648X/aa8f79) · [PSLibrary (Dal Corso 2014)](https://doi.org/10.1016/j.commatsci.2014.07.043).

| Observable | Computed result | Numerical sensitivity |
|---|---|---|
| Rb band 5 at 12³ | −0.04579 to 3.19439 eV, chemical potential 1.89188 eV | At 0.01 Ry Fermi–Dirac width, increasing 35/260 to 45/340 Ry changes the width by 0.00004 eV. Absolute energies use the code’s potential zero. |
| Rb band 5 crossing | At least one band crosses at the electron count. Band 4 is completely filled and band 6 begins about 0.78 eV above the 12³ chemical potential. | The same crossing occurs in five SCF variants across 6³–12³, two smearings, two plane-wave cutoffs. |
| Kr indirect Kohn–Sham gap | 7.233378 eV, with both grid extrema at Γ on 8³ | Raising 64/320 to 75/400 Ry changes the gap by 0.000139 eV; four runs across 4³–8³ give a gapped result. |

**Measured comparison.** An exciton-series analysis of low-temperature solid Kr reports a band gap of about 11.61 eV, corroborated by a two-photon measurement. The PBE Kohn–Sham gap here is about 4.38 eV lower. The occupied-band structure gives a stable insulating classification even while the gap magnitude shows this discrepancy. In the independent-particle limit an entirely filled isolated band gives zero intraband Drude response at zero temperature. Disorder, excitons and interband absorption require separate calculations. [Baldini (1962)](https://doi.org/10.1103/PhysRev.128.1562) · [Reininger et al. (1982), discussion on p. 6295](https://doi.org/10.1103/PhysRevB.26.6294).

## Experimental optical comparison

**Measured input and derived descriptive fit.** Smith (1970) measured the complex room-temperature optical constants of bulk Rb. [rb_optics.py](rb_optics.py) reads a pinned public-domain transcription, checks its file hash, converts n+ik to ε, and fits ε(E)=ε_b−Wp²/[E(E+iΓ)] to real and imaginary parts together. Five upper endpoints between 0.85 and 2 eV give Wp=3.570–3.591 eV and Γ=0.0292–0.0300 eV; the input starts at 0.554 eV. The numeric range measures this fit-window dependence. No pointwise errors were available for a statistical uncertainty. Finite-frequency optical response includes background and interband terms; the fitted damping is sample- and model-dependent. [Smith (1970)](https://doi.org/10.1103/PhysRevB.2.2840) · [archived transcription](https://github.com/polyanskiy/refractiveindex.info-database/blob/e6d15e364f70de1cad8a96a20f75689f2fba8b21/database/data/main/Rb/nk/Smith.yml) · [fits](rb_optics.csv).

## Reproducing the SCF and optical tables

Run with Python 3, NumPy, SciPy and a working Quantum ESPRESSO pw.x. The calculation files in WORK contain the SCF inputs, logs, densities and XML from which the tables are extracted.

    python qe_compare.py Rb WORK --pw /path/to/pw.x
    python qe_compare.py Kr WORK --pw /path/to/pw.x
    python rb_optics.py

The executed binary was Debian quantum-espresso 6.7-3+b1 for amd64, pw.x SHA-256 bcd96679f8a8b77d1a26abe8cba9f34a17f8aef7ad2f6688c6d11fb8cf16ec6f. Its MD5 agreed with the binary's entry in the Debian package manifest. [SCF, Rb](Rb_pbe.csv) · [SCF, Kr](Kr_pbe.csv).

## A bulk response with units

**Derived.** Use the highest-cutoff SCF charge density for Rb, then diagonalize that fixed Hamiltonian on denser k grids. Spin degeneracy supplies four completely filled semicore bands and one half-filled band. The sixth band stays clear of the Fermi surface. In the formula below the cell average is over the full primitive Brillouin zone, the band energy ε is in eV, and the Cartesian wave vector is in Å⁻¹:

    D(EF) = 2 ⟨δ(μ−ε)⟩
    Kαβ = 2 ⟨δ(μ−ε) ∂αε ∂βε⟩ = 2 ⟨Θ(μ−ε) ∂α∂βε⟩
    Wp² = [e²/(ε₀ Vcell)] Tr(K)/3.

With the stated units e²/ε₀=180.9513 eV Å and Vcell=5.700³/2 Å³. K has units eV Å², D has units states/(eV·cell), and Wp=ℏωp has units eV. A partially filled smooth band permits both forms for K by integration by parts on the reciprocal torus. The calculation keeps the Fermi charge at one electron per Rb after removing the filled semicore bands. This is an independent-particle response in the clean, collisionless limit. Converting to DC conductivity requires a relaxation rate.

**Derived, two ways.** [rb_tetrahedra.py](rb_tetrahedra.py) slices each linear tetrahedron directly at half filling. Four choices of primitive-cube diagonal probe triangulation error. Its Fermi-plane intersection volume and derivative handle degenerate vertex energies. This is ordinary linear tetrahedron integration. [rb_fermi_surface.py](rb_fermi_surface.py) instead interpolates with Fourier and cubic splines, solves for half filling and integrates a smooth Fermi–Dirac derivative, with broadening 0.025–0.12 eV on 48³, 72³ and 96³ grids. It checks the velocity-squared and occupied-curvature forms of K separately. The electronic SCF occupation smearing and these later quadrature broadenings have different roles. All 48 cubic symmetry images are reconstructed from the irreducible k list, and each orbit multiplicity is checked against its QE integration weight. [Linear tetrahedron integration and its refinements](https://doi.org/10.1103/PhysRevB.49.16223).

At 24³, the zero-width tetrahedra give Wp = 3.710–3.719 eV and D(EF) = 0.918–0.927 states/(eV·cell), depending on tetrahedron orientation. At the same QE grid the 96³ broadened quadrature gives Wp = 3.715–3.718 eV at 0.025 eV width, and 3.708–3.711 eV at 0.05 eV width. The two forms of K in the smooth calculation differ by at most 0.036% across these four entries. The estimated Rb curvature is finite, and the estimate of Wp exceeds the descriptive optical fit by a few percent. Using a free electron with the same cell count gives 3.859 eV. The intrinsic atomic peel angles did not enter these band energies or velocities. [Full mesh and width sensitivity](Rb_fermi_surface.csv) · [zero-width triangulations](Rb_tetrahedra.csv).

## The role of the Fermi-surface shape in the shell test

**Derived, restricted orbital control.** Assign one effective scalar orbital to each primitive Rb site. Give its Bloch states the actual PBE fifth-band dispersion. Occupy the lower half of all k states on each offset grid. Then C=f=½ per spin, the site budget is B=2f(1−f)=½ with spins summed, and X(R)=2|⟨f(k) exp(i k·R)⟩|². Summing over every nonzero direct-lattice displacement on the finite torus must recover B. The code checks that identity and finds the eight shortest R directly from the measured lattice.

On the fine meshes Rb has nearest-shell fraction about 0.455 in this scalar projection, versus 0.533 in the nearest-hopping bcc toy. Both exceed 1/3. This control transfers the Fermi-surface shape from the material calculation, while suppressing the k-dependence of the cell-periodic atomic-orbital content. An energy-ranked fifth band can also touch higher bands away from the Fermi surface. Its scalar translation basis is a defined model choice. An all-orbital spatially resolved PAW projector requires the Bloch wavefunctions, a stated site partition and an overlap convention. A nine-band filled scalar identity for Kr would have B=0 and an undefined shell fraction. [Restricted shell weights and sum-rule residuals](Rb_scalar_shell.csv).

**Reproduce the response.** To replay from the stored irreducible QE data without pw.x, run

    python rb_fermi_surface.py RESULTS --read-bundle Rb_band_inputs.json.gz
    python rb_tetrahedra.py Rb_band_inputs.json.gz RESULTS/Rb_tetrahedra.csv
    python rb_scalar_shell.py Rb_band_inputs.json.gz RESULTS/Rb_scalar_shell.csv

To regenerate the bundle, first run both SCF calls above, then run

    python rb_dense.py WORK --pw /path/to/pw.x
    python rb_fermi_surface.py WORK --save-bundle Rb_band_inputs.json.gz


## A measured light comparison at one Rb surface

**Derived from measured optics.** For a planar vacuum/Rb interface at normal incidence, the nonmagnetic Fresnel amplitude is r=(1−m)/(1+m) with complex optical index m=n+ik. The observed input here is Smith's optical index. This experiment supplies a complex-valued realization of the reflection algebra. For m≠−1 its exact half-power wall is

    |r|² > 1/2 ⇔ |m|²−6 Re(m)+1 > 0 ⇔ |m−3|² > 8.

The positive real axis cuts that circle at the two familiar ratios 3±2√2. Reciprocating m sends r to −r. Each equality holds for every admissible m as algebra. An additional physical identification between m and a free-atom peel ratio would require an independently specified frequency-dependent mapping. The atomic peel uses real removal energies, while r is a surface reflection amplitude.

**Measured input / derived comparison.** Between Smith's samples at 3.2040 and 3.3970 eV, the calculated normal-incidence power falls from 0.587595 to 0.373590 across one half. The two sampled wavelengths are 386.967 and 364.981 nm. This bracket is independent of fitting a damping rate or assuming a shape between tabulated points. Every one of the 24 tabulated rows passed both the circle test and the reciprocal-amplitude check. [Pointwise Rb optical table](Rb_reflectance.csv) · [Smith optical constants (1970)](https://doi.org/10.1103/PhysRevB.2.2840).
