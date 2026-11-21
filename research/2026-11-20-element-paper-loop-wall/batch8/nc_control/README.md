# Norm-conserving control for the rubidium and krypton spatial projectors

**Question.** Does the nearest-neighbour shell still carry over a third of each site's off-site projector weight if the wavefunctions come from independently generated norm-conserving PBE potentials? The earlier calculation used smooth PAW occupied subspaces. Here the plain pseudo-wavefunction inner product agrees with the eigenproblem's norm. The resulting observable is still defined on pseudo-orbitals partitioned into Wigner–Seitz cells.

**MEASURED inputs.** Body-centred cubic rubidium uses conventional a=5.700 Å from the 297 K structure (estimated lattice parameter in the deposited record). Face-centred cubic krypton uses a=5.721 Å at 58 K. Temperature labels the crystallographic input. Both electronic calculations use a static crystal. [Rubidium COD 9012876](https://www.crystallography.net/cod/9012876.html) · [Krypton COD 9008471](https://www.crystallography.net/cod/9008471.html)

## Electronic and spatial inputs

**DERIVED.** Quantum ESPRESSO PWSCF 6.7MaX, scalar-relativistic, nonmagnetic PBE, one atom per primitive cell. The two UPF headers identify ONCVPSP 3.3.0, `pseudo_type="NC"`, `is_paw="F"`, `is_ultrasoft="F"` and PBE. Rubidium explicitly includes nine electrons (4s²4p⁶5s¹); krypton includes eight (4s²4p⁶). These are the nc-sr-04/PBE/standard UPF files. Each file's SHA-256 is verified before the run. [PseudoDojo](https://www.pseudo-dojo.org/about.html) · [Hamann (2013)](https://doi.org/10.1103/PhysRevB.88.085117) · [Pinned rubidium UPF](https://github.com/Quantum-MultiScale/KSPP/blob/33528761f31e0e3a5d6c875f6174a17e69eb86e9/norm-conserving/nc-sr-04/PBE/standard/upf/Rb.upf) · [Pinned krypton UPF](https://github.com/Quantum-MultiScale/KSPP/blob/33528761f31e0e3a5d6c875f6174a17e69eb86e9/norm-conserving/nc-sr-04/PBE/standard/upf/Kr.upf)

| File | SHA-256 |
|---|---|
| Rb.upf | b40d0424cd413a24da3396b6fb62081bbb13be49acbf1fc666ca976c239ed736 |
| Kr.upf | 42d25c77ed07bf438be5b8543f4afd66f10ae46f90d1b80155b6519f4c9bb8c3 |

**DERIVED.** SCF uses a 12³ unshifted mesh and 0.01 Ry Fermi–Dirac width for rubidium, an 8³ unshifted mesh and fixed occupations for krypton, 75/300 Ry wavefunction/density cutoffs and a 10⁻⁹ Ry electronic convergence tolerance. An independent 60/240 Ry SCF plus a 4³ NSCF serve as a cutoff control. Each full NSCF mesh uses the same offsets (0.137,0.271,0.389) in mesh units. Krypton has four fully occupied bands; the indirect gap is checked before retaining bands 1–4. Rubidium contains four fully occupied semicore bands. Rank eigenvalues over all higher bands at all N k-points, select the lowest N/2 levels for the outer subspace and verify a positive finite-mesh separation at the rank boundary. The lowest partially occupied band crosses the chemical potential. This calculation uses a zero-temperature spectral projector after the metallic SCF. The additional rubidium semicore control includes bands 1–4 as well. Absolute Kohn–Sham energies use a pseudopotential-dependent zero. [SCF inputs for rubidium](Rb.scf.in) · [SCF inputs for krypton](Kr.scf.in) · [actual SCF diagnostics](scf_summary.csv) · [band diagnostics](bands.csv)

**DERIVED.** At each wave vector the unadjusted orbital Gram matrix in plain pseudo-L² must differ from the identity by less than 10⁻⁷ in every entry before the spatial integration. The test uses the translated Wigner–Seitz partition, full Bloch phases, full finite reciprocal mesh, two spin copies and the complete finite-torus sum rule. Rubidium has eight nearest neighbours and krypton twelve. Uniform real grids use offset (0.213,0.367,0.479) in sampling-grid units. The packet records absolute weight, on-site budget, extrema among nearest directions and the normalized shell fraction separately. The value of a filled crystal's shell fraction can approach one with a small absolute off-site budget. [Projector implementation](nc_projector.py) · [raw numeric results](results.csv)

## Sensitivity already resolved by the 4³ runs

**DERIVED.** At 75/300 Ry on the 28³ spatial grid, the rubidium nearest shell holds 0.496956 of its off-site budget and the krypton shell holds 0.991023. Their mean absolute link weights are respectively 0.0490595 and 0.0174273. Every individual nearest direction exceeds its per-link cutoff in both materials. Exchanging the 4³ k-mesh twist moves the rubidium fraction to 0.491526 and the krypton fraction to 0.991007. Lowering both plane-wave cutoffs to 60/240 Ry at the original twist shifts those fractions by less than one part in a million in absolute fraction units. Including rubidium’s four semicore bands raises its fraction to 0.501521 on the original 4³ mesh. The material with the insulating band occupation has the more concentrated shell, while the metallic material has the larger absolute connection on a nearest bond. This is a finite-mesh test of an electronic-structure model. [Numerical controls](results.csv)

## Reproduction

The calls below create independent densities, unconstrained full NSCF meshes and projector results. Larger density and wavefunction files are generated under the specified work directory. The same SCF wavefunction cutoff is used for both materials. Reuse the work directory for the second mesh of a material. The 60 Ry control should use its own work directory. To reproduce the semicore test, append `--include-semicore` on a rubidium call. The spatial grid parameter in the examples is 28; 32 reproduces the quadrature refinements.

```sh
python3 fetch_nc.py /path/to/nc_pps
python3 run_nc.py /path/to/nc_work /path/to/nc_pps Rb 4 28 --pw /path/to/pw.x
python3 run_nc.py /path/to/nc_work /path/to/nc_pps Kr 4 28 --pw /path/to/pw.x
python3 run_nc.py /path/to/nc_work /path/to/nc_pps Rb 6 28 --pw /path/to/pw.x
python3 run_nc.py /path/to/nc_work /path/to/nc_pps Kr 6 28 --pw /path/to/pw.x
python3 run_nc.py /path/to/nc_work/lower /path/to/nc_pps Rb 4 28 --cutoff 60 --pw /path/to/pw.x
python3 run_nc.py /path/to/nc_work/lower /path/to/nc_pps Kr 4 28 --cutoff 60 --pw /path/to/pw.x
python3 summarize_bands.py /path/to/nc_work
```

The mesh utility lives in the sibling `ws_control` folder. Private work directories should be on a filesystem with space for binary wavefunctions. Python needs NumPy and SciPy for the projector readout.

**DERIVED · additional controls.** The independent alternate 4³ reciprocal mesh replaces the shift by (0.411,0.097,0.233) in sampling-grid units. The real-space quadrature offset and all SCF settings remain the same. Use the optional mesh script shown below, writing into a fresh NSCF directory; rerunning on an existing default-shift mesh would reuse the wrong Fourier components. With W set to the main working directory:

```sh
python3 qe_alternate_twist.py "$W/Rb-scf" "$W/alternate" Rb 4 --pw /path/to/pw.x
python3 nc_projector.py "$W/alternate/Rb-4/out/system.save" Rb 4 28
python3 qe_alternate_twist.py "$W/Kr-scf" "$W/alternate" Kr 4 --pw /path/to/pw.x
python3 nc_projector.py "$W/alternate/Kr-4/out/system.save" Kr 4 28
```

The PAW comparison replays the sibling smooth projector on the previously generated PAW wavefunctions, using the *same* full reciprocal mesh, shift, outer subspace definition and 28³ Wigner–Seitz quadrature as the corresponding NC control. The original PAW semicore treatment and cutoff settings are documented in the sibling packet. A cutoff check within the NC family isolates the NC basis sensitivity. Differences between potential families also include different frozen-core treatments. [Cross-family readouts](paw_comparison.csv) · [PAW calculation](../ws_control/README.md).

**DERIVED · six-by-six-by-six result.** At 75/300 Ry with a 6³ full reciprocal mesh and a 28³ real grid, the outer rubidium projector gives B = 0.792878973, mean nearest link = 0.047330756 and nearest-shell fraction = 0.477558444. The krypton projector gives B = 0.211074390, mean nearest link = 0.017430495 and fraction = 0.990958408. Under the same k twist and spatial quadrature the earlier PAW smooth-span fractions are 0.478460388 and 0.991270600. Increasing the NC real grid to 32³ shifts the two fractions to 0.477554247 and 0.990957236. At 6³ the NC krypton indirect gap is 7.331576 eV. Rubidium band 5 spans 0.007417–3.116506 eV, containing the finite-grid half-filling estimate of 1.916210 eV. A change in potential representation leaves both shell calls and electronic classifications intact across these tests. The rubidium fraction shows substantially greater k-mesh dependence; the decimal digits provided support reproduction of these specific finite-mesh runs. [Two representations side by side](paw_comparison.csv) · [NC numerical results](results.csv) · [independent band readout](bands.csv)
