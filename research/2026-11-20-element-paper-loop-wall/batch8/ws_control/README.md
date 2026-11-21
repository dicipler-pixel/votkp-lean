# Nearest-neighbour sharing in two material-specific occupied projectors

Jeromie Beasley's question is whether the nearest neighbours of a crystal carry a third of the shareable weight, and how that relates to conduction. Here the occupied states come from self-consistent periodic rubidium and krypton calculations at measured conventional lattice spacings. Each atom owns its Wigner–Seitz cell (all points closest to it). A single site per primitive cell avoids an arbitrary choice of orbital centres. The assignment of a spatial region to the atom remains a modelling choice.

## Operator and experiment

**DERIVED.** For the site at the origin let its spatial projection be Π₀ and let P be the orthogonal projector onto a specified occupied subspace. Write C₀=Π₀PΠ₀ on that site and X(R)=‖Π₀PΠᴿ‖² including both spins. Since P²=P,

    B = Tr(C₀−C₀²) = ∑(R≠0) X(R).
    S₁ = ∑(nearest R) X(R) / B, when B>0.

The quoted per-link mean is the sum over all nearest neighbours divided by their number. Per-direction minima and maxima are retained because a finite twisted mesh can split symmetry-related values. The strict shell-concentration test is S₁>1/3. Fix the following failure conditions before interpreting it: a negative X beyond numerical noise, failure of ∑X=Tr C₀, or a classification that changes under modest refinement invalidates the numerical classification; passage by a gapped crystal defeats the proposal that passage alone establishes a metal.

**DERIVED · computation.** The SCF parameters and potential hashes appear in the [material-specific band calculation](../material_transport/README.md). Freeze the PBE charge density and compute the wavefunctions on the full, un-reduced M³ mesh with offsets (0.137,0.271,0.389) in grid units. At each k take the selected *occupied* smooth PAW pseudo-wavefunctions as a span. Symmetrically orthonormalize this span at k in ordinary L². This defines a genuine projector on the smooth pseudo-wavefunctions. The all-electron PAW projector, with augmentation inside the atom, is a distinct operator. Within the chosen span a unitary rotation of the occupied band basis leaves the result invariant.

The default rubidium span uses the lowest half of the outer-band levels over the entire finite mesh (one spin-degenerate electron per primitive site), ranked at zero temperature. Levels from the four occupied semicore bands are omitted. Krypton uses the outer 4s and 4p occupied bands (eight electrons per site); the five 3d semicore bands are omitted. The separately labelled semicore control adds those bands before orthonormalization. It is important to use binary occupations. With fractional occupations the additional term Tr(P−P²) enters the budget.

**DERIVED · real-space integration.** Define wₐ as the cell-normalized smooth Bloch wave of occupied state a=(k,n) restricted to the origin Wigner–Seitz cell. Include the Bloch phase in the cell integral. On converting a primitive parallelepiped grid point to its nearest periodic image, use that *image's* coordinate in the phase. Let Gₐᵦ = ⟨wₐ,wᵦ⟩. For N=M³,

    X(R) = (2/N²) ∑ₐᵦ exp[i(kₐ−kᵦ)·R] |Gₐᵦ|².
    Tr C₀ = (2/N) ∑ₖ noccupied(k).

Quoting ∑X only after evaluating every finite-torus block checks the normalization and Fourier sign convention up to R↔−R; the even weights alone cannot determine an orientation. A separate [direct supercell test](../transport/normalization/Wigner_Seitz_projector_check.md) compares with the explicit block matrix, including phase and occupation controls. The geometry, spin and normalization here match that comparison.

## Reproduce

Python needs NumPy and SciPy. Quantum ESPRESSO 6.7 was run using one spin-degenerate channel and its standard binary wavefunction output. The reader expects those scalar, non-gamma-only Fortran records. From this directory, with the sibling material SCFs already generated into an absolute work directory W:

```sh
python qe_full_mesh.py "$W/Rb-45-340-12-0.01" "$W/full" Rb 6 --pw pw.x
python pseudo_projector.py "$W/full/Rb-6/out/system.save" Rb 6 28
python qe_full_mesh.py "$W/Kr-75-400-8-0" "$W/full" Kr 6 --pw pw.x
python pseudo_projector.py "$W/full/Kr-6/out/system.save" Kr 6 26
```

See [results.csv](results.csv) for the actual inputs and outputs. Real grids are per primitive lattice direction. The quadrature offset used by default is (0.213,0.367,0.479) in grid units. The second krypton 6³ real grid uses (0.711,0.133,0.837). The 4³ k meshes used the lower 35/260 Ry (rubidium) and 64/320 Ry (krypton) SCFs in the companion equipment table; subsequent meshes use 45/340 and 75/400 Ry. Data are comparisons in this declared PBE PAW smooth-span model. No experimental X has been inferred.

## Results

| Outer smooth span, 8³ full k points | Off-site budget per site | Mean nearest link | Nearest shell share | Independent band check |
|---|---:|---:|---:|---|
| Body-centred cubic rubidium | 0.790748 | 0.046949 | 0.474985 | Partly occupied outer band crossing the Fermi level |
| Face-centred cubic krypton | 0.193066 | 0.015948 | 0.991271 | Filled outer bands, with a 7.233 eV PBE gap on the companion 8³ Γ-centred band mesh |

**DERIVED.** Rubidium has the larger absolute weight on each nearest link on average. Krypton localizes a much higher fraction of a much smaller budget on its nearest shell. Both exceed one third. The independent electronic responses separate the metallic and insulating cases. The results survive changes of mesh, real-space quadrature, and including the semicore bands in the 4³ test. The electronically calculated quantities concern the stated occupied spans and cell partition. An experimental dc conductivity would additionally require a response and relaxation model. Independent measured optical data and the PBE gap discrepancy are in the [band comparison](../material_transport/README.md).
