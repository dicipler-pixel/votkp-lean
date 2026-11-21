# How far does the occupied projector reach in rubidium and solid krypton?

**DERIVED.** The two crystals each pass Jeromie Beasley's one-third nearest-neighbour test. We used their original occupied wavefunctions to ask how far the remaining weight reaches. The site-centre result per electron grows with system size in rubidium. In krypton it stabilizes. Resolving coordinates *inside* each cell gives substantial extra spread in krypton. Files below report finite periodic systems at zero-temperature outer-band occupation.

**MEASURED input / model used.** The conventional crystal parameters are 5.700 Å for body-centred cubic rubidium (297 K structure) and 5.721 Å for face-centred cubic krypton (58 K). The occupation and Hamiltonian are those of the static structures. A site owns the **geometric Wigner–Seitz region in real space**, the points closest to its lattice point. This specifies what the junction weighs. Each normalized outer-band projector counts both spins. The numbers of electrons included per primitive cell are one for rubidium and eight for krypton. Crystal inputs, frozen cores, potentials and benchmarks are pinned in the earlier calculation. [Original norm-conserving setup](../../batch8/nc_control/README.md) · [original smooth PAW setup](../../batch8/ws_control/README.md)

### Three readings from the same branch

| Material | Nearest-shell share (NC, 6³) | Site-centre mean square per direction, 4³ → 6³ (Å²) | Microscopic phase response, 4³ → 6³ (Å²) | Transport comparator from batch 8 |
|---|---:|---:|---:|---|
| Rubidium | 0.47755844 | 5.704361 → 7.995186 | 2.786833 → 4.247212 | finite intraband response, plasma energy 3.71377–3.71588 eV on the 48³ zero-width mesh |
| Solid krypton | 0.99095841 | 0.073224 → 0.073270 | 0.238159 → 0.245570 | filled isolated valence bands, zero independent-particle intraband weight |

**DERIVED.** The first two columns use exactly the same atom-to-atom weights. The third uses the actual plane-wave coordinates at the shortest nonzero reciprocal wavevectors of each finite system. The last uses band energies and velocities. The old smooth PAW spatial calculation gives rubidium 5.6844, 7.9743, 10.3788 and 12.6220 Å² on meshes 4³, 6³, 8³ and 10³. Krypton gives 0.066924, 0.066972 and 0.066972 Å² on 4³, 6³ and 8³. All these new PAW readouts use 28³ spatial quadrature. The earlier 10³ rubidium shell fraction 0.473866891 used 26³ spatial quadrature. At 28³ the same electronic mesh gives 0.473891910. [All site tensor components and quadrature controls](site_moments.csv) · [phase shell means](phase_shell_means.csv) · [transport details and sources](../../batch8/material_transport/README.md)

### Distance, direction and normalization

**DERIVED.** For each supercell translation class $R$, let $X_R=\|P_{0R}\|_F^2$, including both spin copies. With $\nu$ occupied electrons per primitive cell, $\sum_R X_R=\nu$. The offsite budget is $B=\nu-X_0$, and the first-shell reading is $\sum_{\mathrm{near}}X_R/B$. The centre-position second moment per electron is

$$
\Lambda^{c}_{ab}=\frac{1}{2\nu}\sum_R X_R\,\langle R_aR_b\rangle_{\mathrm{shortest}}.
$$

Here $R$ is in Å. The brackets average dyads of every tied shortest Cartesian image. A bound using the smallest singular value of the primitive lattice matrix ensures all shortest images are included. The table gives $\operatorname{Tr}(\Lambda^c)/3$. The CSV includes the six independent tensor components. A single shifted mesh has finite anisotropy. The spatial weight at $R=0$ enters the sum rule with zero contribution to the centre moment.

**DERIVED.** For the microscopic position phase set $U_q=e^{i q\cdot r}$ and $L(q)=\|(1-P)U_qP\|_F^2/(N_e |q|^2)$. The connected structure factor per electron is $|q|^2 L(q)$ for this Slater state. Let $r_k$ be the occupied rank per spin at $k$, $N_o=\sum_k r_k$, and $M_k$ the plane-wave overlap from $k$ to $k+q$ with reciprocal-lattice wrapping. The two spin copies cancel between numerator and denominator. Then

$$
L(q)=\frac{\sum_k |r_k-r_{k+q}|/2}{N_o |q|^2}
+\frac{\sum_k [\min(r_k,r_{k+q})-\|M_k\|_F^2]}{N_o |q|^2}.
$$

Both terms are nonnegative. The first counts an exact loss of dimension on crossing the Fermi surface. On the shortest reciprocal star it accounts for 4.046325 of rubidium's 4.247212 Å² at 6³. Krypton has constant occupied rank four, so this term vanishes. Using the phase at each cell centre gives $L_c(q)=\sum_R X_R[1-\cos(q\cdot R)]/(\nu |q|^2)$. Comparing $L_c$ and $L$ at the same $q$ isolates the effect of assigning all points in a cell the same coordinate. The earlier spatial tensor uses a minimum-image distance. Both finite periodic distance conventions appear in the CSVs. [Each direction and both contributions](phase_directions.csv) · [independent controls](../controls/README.md) · [Onishi and Fu (2025)](https://doi.org/10.1103/PhysRevResearch.7.023158)

**DERIVED.** A Slater determinant gives another test at the same $q$. Its many-body twist overlap is a determinant with k-blocks permuted by translation. A sector of larger dimension than its target forces the determinant to vanish exactly. Around a finite permutation, unequal ranks force such a sector. The CSV reports this rank obstruction and gives infinity for the corresponding negative-log spread. When all blocks have equal source and target rank and are nonsingular, the spread is $-2\sum_k \ln|\det M_k|/(N_o |q|^2)$. Every tested rubidium direction has a rank obstruction. The krypton blocks are nonsingular, giving 0.249604 → 0.250885 Å² on the shortest star from 4³ to 6³. The logarithmic reading lies above the structure-factor reading because $-\ln t\geq 1-t$ for squared singular values $0<t\leq1$. The two approach each other as $q$ decreases for krypton. [Resta and Sorella (1999)](https://doi.org/10.1103/PhysRevLett.82.370) · [Souza, Wilkens and Martin (2000)](https://doi.org/10.1103/PhysRevB.62.1666)

**HYPOTHESIS / scope.** The growth or saturation of long-range sharing is the part of Jeromie's junction picture tested here. These are outer-band pseudo-wavefunctions at fixed material parameters and electron count. The numeric moments use squared lengths in the measured crystal used for this comparison. An identification with the full intrinsic IQGT or a model of the junction based solely on an atom's peel ratios would require additional hypotheses. Growth on a finite list of cells supplies a test of the trend. The thermodynamic divergence of this specific microscopic rubidium calculation has not been established by finite-size sampling alone.

### Falsifiers and reproduction

- **DERIVED.** Wrong supercell-image handling can change direction-resolved tensor components. The direct checker re-enumerates nearest images. Reject material weights if their spin sum, nonnegativity or reversal symmetry fails. [Independent checks](../controls/README.md)
- **DERIVED.** An incorrect sign for reciprocal-zone wrap can give plausible overlaps. The independent real-space FFT comparison exercises ten wrap links on the 4³ meshes and rejects the reversed sign on all ten. Gauge rotations of the occupied bands preserve principal angles. An exactly soluble half-filled chain gives $L=N/(2\pi^2)$ for unit spacing. A filled isolated bonding orbital gives positive microscopic spread with its centre spread exactly zero. [Test implementation](phase_controls.py) · [actual output](phase_controls.txt)
- **DERIVED.** The default electronic setup is norm-conserving at 75/300 Ry, full shifted mesh, common real quadrature of 28³. A 60/240 Ry control and alternate mesh twist test material sensitivity. Increasing the real quadrature to 32³ tests only the spatial partition. The microscopic estimator uses native plane-wave coefficients and needs no real-space quadrature.
- **DERIVED.** Use Python with SciPy/NumPy. Recreate densities with the earlier NC/PAW instructions. For each desired mesh, generate the full shifted NSCF output with the earlier script. W is the NC work folder, P is the path to this folder, and E is Rb or Kr. The common reciprocal twist is (0.137,0.271,0.389) in mesh units. The alternate twist is (0.411,0.097,0.233). Direction labels are conventional Cartesian Miller indices in units $2\pi/(aM)$ for mesh side M. Shortest-star means use six unoriented directions for rubidium and four for krypton. Axial means use three.

```sh
OPENBLAS_NUM_THREADS=1 python3 "$P/../../batch8/ws_control/qe_full_mesh.py" \
  "$W/$E-scf" "$W/ws" "$E" "$M" --pw /path/to/pw.x
OPENBLAS_NUM_THREADS=1 python3 "$P/site_tensor.py" \
  "$W/ws/$E-$M/out/system.save" "$E" "$M" 28 --weights "/tmp/$E-$M.csv"
OPENBLAS_NUM_THREADS=1 python3 "$P/microscopic_response.py" \
  "$W/ws/$E-$M/out/system.save" "$E" "$M" --weights "/tmp/$E-$M.csv"
OPENBLAS_NUM_THREADS=1 python3 "$P/phase_controls.py" "$W"
```

**DERIVED.** The [weights](weights/) directory contains all default spatial translations as round-trip-safe CSV. Each file begins with mesh, electron count and three primitive lattice vectors in Å, followed by i,j,k,X in primitive mesh coordinates. Prefix NC denotes the norm-conserving 75/300 Ry family. Prefix PAW denotes the orthonormalized smooth PAW span. Convert any file to an equivalent compressed NumPy archive with `python3 weight_io.py weights/NC-Rb-6.csv /tmp/NC-Rb-6.npz`. The converter checks every float64 value after conversion.
