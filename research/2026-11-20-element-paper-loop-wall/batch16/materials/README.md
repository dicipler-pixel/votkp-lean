# Material checks for Os, Ir, Pt, Au and Hg

**HYPOTHESIS / falsifiers.** If an atomic scalar were sufficient to predict bulk transport or reflection, changing the crystal axis or a sample's phase while holding its element fixed could not change the corresponding prediction. Use independently measured optical principal axes of Os, phase-resolved transport in Hg and sample-dependent superconductivity in Pt to test this claim. If a neighbor spacing is assigned to a crystal structure, reject a cell that describes a compound, alloy, unverified model or another phase. If a proposed invariant is an actual knot invariant, require a specified closed path and a reproducible invariant under the stated allowed deformations. The tests and data below concern these definitions.

## Heat, charge, phase and the ball picture

**MEASURED / DERIVED.** Near room temperature all five carry electrical current, including liquid mercury. The electrical conductivities below use σ (MS/m)=100/ρ with ρ in µΩ cm. The 295 K resistivities and 300 K thermal conductivities for the four solids are compiled in Ekin, Appendix A. The liquid mercury entry uses Ho, Powell and Liley's 300 K recommendation of 0.0834 W/(cm K) ×100=8.34 W/(m K). Ekin's table displays 83.4; the primary phase-resolved table settles that discrepancy. RSC supplies the near-ambient density and normal boiling temperature. NIST TN 2312 (2025), Table 1, supplies the indicated atmospheric-pressure melting points. [Machine-readable table, source codes and RSC alternatives](material_constants.csv) · [NIST 2025](https://doi.org/10.6028/NIST.TN.2312) · [Ekin, 2006–2011 Appendix](https://www.researchmeasurements.com/figures/ExpTechLTMeas_Apdx_English.pdf) · [Hg thermal conductivity, Ho et al. 1974](https://srd.nist.gov/JPCRD/jpcrdS1Vol3.pdf) · [RSC, accessed 2026](https://periodic-table.rsc.org/)

| Element and room phase | Density (g/cm³) | Melt / boil (K) | ρ (µΩ cm) | σ (MS/m) | Thermal κ (W/m K) | Superconducting observation |
|---|---:|---:|---:|---:|---:|---|
| Os, hexagonal close-packed | 22.5872 | 3328 / 5281 | 9.13 | 10.95 | 87.6 | 0.66 K, solid |
| Ir, face-centered cubic | 22.5622 | 2719 / 4701 | 5.07 | 19.72 | 147 | 0.112 K, solid |
| Pt, face-centered cubic | 21.5 | 2041.9 / 4098 | 10.6 | 9.43 | 71.6 | 0.62–1.38 mK in compressed powder, packing dependent |
| Au, face-centered cubic | 19.3 | 1337.33 / 3109 | 2.23 | 44.84 | 317 | A bulk search found no transition to 60 µK in <1 mG |
| Hg, liquid | 13.5336 | 234.3210 / 629.769 | 95.9 | 1.043 | 8.34 | Solid α-Hg 4.154 K; solid β-Hg about 3.95 K |

**MEASURED.** NIST's melt evaluation differs from the RSC values by +22 K for Os (NIST quotes 30 K uncertainty) and +0.5 K for Pt (NIST quotes 0.5 K). Gold's 1337.33 K is an assigned ITS-90 fixed point. The solid α and β forms of mercury show different critical fields and temperatures. For Pt, powder packing fractions 0.8–0.5 gave the above range, while a later study separated intragranular diamagnetic onset (~1.9 mK) from intergranular response. Neither number establishes an identical transition in a homogeneous Pt single crystal. [Pt compact experiment, 1999](https://doi.org/10.1103/PhysRevLett.82.4528) · [Pt granular study, 2000](https://doi.org/10.1103/PhysRevB.62.14350) · [Au search, 1981](https://doi.org/10.1016/0378-4363(81)90662-8) · [Hg phase-specific experiment, 1961](https://doi.org/10.1103/PhysRev.123.1115)

**DERIVED / HYPOTHESIS.** The measured gas-phase energy ratios provide each element's internal clock changes. Each has its own ball wall and an interatomic junction is a separate object. The K-opening face apex tanh(ln(z)/4) is 0.334112 (Os), 0.333889 (Ir), 0.333664 (Pt), 0.333439 (Au) and 0.333211 (Hg). For the measured anion rungs the apexes are 0.473440, 0.410795, 0.344954 and 0.333119 respectively. No positive Hg anion reference exists. Equal facing clocks give Γ=0 across an ideal identical-neighbor junction. Neither this equality nor an isolated atom's clock specifies a crystal's projector P, Xᵢⱼ, filling or Bruggeman conducting fraction. Placing any of the five elements on a particular side of the 1/3 effective-medium threshold from these data alone remains undetermined. The crystalline Euclidean nearest-neighbor lengths below are measured structural comparators for Jeromie's gap, not a replacement metric. [Internal face calculations, all rungs](../ladder/rungs_detailed.csv) · [Earlier matched-junction study](../../checks)

### Contact lengths, crystal phases and compression

**MEASURED / DERIVED.** These representative cells give distances in Å. For cubic fcc, d=a/√2. In hexagonal Os, the basal six are at a and the three above plus three below are at √(a²/3+c²/4). The shorter shell of six and the longer shell of six give a structural example where assigning a single distance to all twelve faces would discard information. A contact-defined metallic radius for each *solid* is d/2; the corresponding pm values appear below. Its definition depends on the selected phase. Dimensions and atomic coordinates come from the linked COD entries. [31 retained CIFs, with source year and individual links](crystals.csv) · [14 exclusions](set_aside_cells.csv)

| Element | Representative structure and lattice constants (Å) | First two distances (Å) | d/2 (pm) |
|---|---|---:|---:|
| Os | hcp, a=2.7352, c=4.319 | 2.6753, 2.7352 | 133.76 |
| Ir | fcc, a=3.8394 | 2.7149, 3.8394 | 135.74 |
| Pt | fcc, a=3.9231 | 2.7741, 3.9231 | 138.70 |
| Au | fcc, a=4.07825 | 2.8838, 4.07825 | 144.19 |
| Hg solid α | rhombohedral primitive a=3.005, angle 70.52° | 3.0050, 3.4695 | 150.25 |
| Hg liquid near room T | X-ray radial-distribution peaks, average over 0, 30 and 50°C | 3.01, 5.80 | no fixed lattice radius |

- **MEASURED — Os.** Static compression preserved hcp Os even at 770 GPa in a 2015 diffraction experiment. The authors found anomalies in c/a and discussed electronic contributions. Independent single-crystal transport work resolved electrical resistivity anisotropy over 4.2–300 K. Scalar handbook transport data average away the directional comparison. [High compression](https://doi.org/10.1038/nature14681) · [Single-crystal resistivity, 1981](https://pubs.aip.org/aip/ltp/article-abstract/7/9/561/3323729/) · [2013 evaluated cell and thermal expansion](https://doi.org/10.1595/147106713X668541)
- **MEASURED — Ir.** Diffraction in the 2025 Ir pressure/temperature study found fcc wherever a crystalline sample was observed in its investigated range, extending to 101 GPa and 5600 K. A historical suggested 14-layer hexagonal superlattice near 59 GPa lacks confirmation by subsequent experiments; keep it separate from accepted bulk phases. [2025 phase study](https://doi.org/10.1038/s43246-025-00963-4) · [2026 high-pressure review](https://doi.org/10.1088/1361-648X/ae3bc6)
- **MEASURED — Pt.** Shock-compressed platinum retained fcc beyond 380 GPa in 2020 diffraction. Its room-temperature polycrystalline conductivity, its cold compacted powders and its optically characterized thin film have distinct morphologies. [Compression](https://doi.org/10.1103/PhysRevLett.124.235701)
- **MEASURED — Au.** The [1988 temperature series](crystals.csv) expands from a=4.072 Å at 293 K to 4.145 Å at 1324 K in the reported sample. The 2017 hcp record concerns hexagonal nanostructures. Two 2019 shock experiments place the onset of bcc differently; one bracketed 150–176 GPa, the other saw fcc at 169 GPa and bcc evidence at 223 GPa. Their pressure paths and resolution matter. [First shock series](https://doi.org/10.1103/PhysRevLett.123.045702) · [Second shock series](https://doi.org/10.1103/PhysRevLett.123.045701) · [hcp nanostructure CIF](https://qiserver.ugr.es/cod/1545302.cif)
- **MEASURED / DERIVED — Hg.** Liquid Hg has a radial-distribution peak, without a periodic lattice or fixed atom-to-atom spacing. Pressure solidifies Hg at about 1.2 GPa at room temperature. The [four crystalline cells and derived nearest distances](mercury_cells.csv) cover α (rhombohedral); β (I4/mmm, a=3.995, c=2.825 Å, nearest 2.825 Å); γ (C2/m, a=5.179, b=2.797, c=7.964 Å, β=107.96°, at 20.0(5) GPa); and δ (hcp, a=2.612, c=4.284 Å at 193 GPa). γ's two independent sites both have nearest distance 2.797 Å in the 2007 refinement. The older 1993 orthorhombic indexing has been set aside in favor of the 2007 monoclinic refinement. The α/β solid transitions and liquid transport therefore cannot be assigned to one crystalline gap. [Liquid Hg X-ray study, 1968](https://doi.org/10.1080/00319106808083792) · [1993 indexing](https://doi.org/10.1103/PhysRevB.48.14009) · [2007 monoclinic refinement, Table II](https://doi.org/10.1143/JPSJ.76.023601) · [2015 pressure study](https://doi.org/10.1088/2053-1591/2/1/016502) · [Hg phase handbook](https://doi.org/10.1039/9781849735155)

## Light at a surface, light from an atom

**MEASURED / DERIVED.** Measured optical constants supply an element- and sample-specific alternative to substituting an atomic peel for a neighboring clock. For a plane wave at normal incidence from vacuum onto a semi-infinite nonmagnetic material, use the principal complex index n+ik. The intensity reflectance is R=((n−1)²+k²)/((n+1)²+k²). The optical half-intensity condition R>1/2 is (n−3)²+k²>8. Dropping k would change the test. The calculations use exact-point entries or interpolation in wavelength of n and k separately between the printed data brackets. A side face of single-crystal Os with c in the interface plane admits both principal polarizations at normal incidence. The numerical R values below refer to the homogeneous half-space boundary; the 80 nm Pt/quartz film supplied the optical constants, and a full thin-film/substrate reflectance would also require propagation through the film. [Brackets and raw table hashes](optical_brackets.csv) · [Reflectance and attenuation lengths](optics.csv) · [Calculation](optics.py)

| Sample / polarization | R at 450 nm | R at 550 nm | R at 650 nm |
|---|---:|---:|---:|
| Os ordinary | 0.6546 | 0.5814 | 0.4846 |
| Os extraordinary | 0.6438 | 0.5365 | 0.5285 |
| Ir, annealed polycrystal | 0.7014 | 0.7317 | 0.7460 |
| Pt, 2024 film optical constants | 0.6874 | 0.7324 | 0.7614 |
| Au, evaporated film optical constants | 0.4082 | 0.7916 | 0.9565 |
| Hg, room-temperature liquid | 0.7787 | 0.7794 | 0.7814 |

**RECOGNISED.** The same Os crystal crosses the optical half-power condition between polarizations at 650 nm. The indices used are 4.83+1.87i and 2.825+3.055i, respectively. An enriched test of the light-led ball picture would fix the sampled face, optical polarization and frequency before predicting the two signs on a new crystal. Gold has strongly different red and blue return; liquid Hg is nearly flat at these three wavelengths. The Os source's year is misprinted as 1968 by the optical database; the JETP paper itself gives January 1986. The Ir optical numbers are unpublished 1986 ellipsometry supplied privately by E. F. I. Roberts and are weaker evidence than the refereed measurements. [Os primary paper, 1986](https://www.jetp.ras.ru/cgi-bin/dn/e_063_01_0115.pdf) · [Ir tabulation, source details](https://refractiveindex.info/?shelf=main&book=Ir&page=Roberts) · [Pt film, 2024](https://doi.org/10.1103/PhysRevB.110.195130) · [Au, 1972](https://doi.org/10.1103/PhysRevB.6.4370) · [Liquid Hg, 1981](https://doi.org/10.1103/PhysRevB.23.5246)

**MEASURED.** The NIST strong-line compilation gives 840 Os/Ir/Pt/Au/Hg neutral and singly charged transitions. Bright examples in the visible range from the tabulated neutral spectra are Os I 426.085 and 442.047 nm, Ir I 380.012 and 397.631 nm, Pt I 381.86874 and 396.6357 nm, Au I 460.7512 and 479.2583 nm, and Hg I 435.8328 and 546.0735 nm. Preserving relative intensities within their original lists keeps line strengths separate from bulk reflected color. [All 840 entries, medium, line flags, references and source links, NIST Handbook 2007](spectral_lines.csv)

## Radius, polarizability and the nucleus

**MEASURED / EVALUATED.** RSC's empirical covalent/nonbonded distances, Shannon effective ionic radii at specified oxidation state and coordination, and the neutral polarizability are different observables. The September 2025 Schwerdtfeger–Nagle recommendations mix measured and calculated evidence: Os's result is calculation-based, Ir includes an experimental 54.0(6.7), Pt includes an experimental 38(8), Au includes 40(8) among other experimental determinations, and Hg's recommended 33.91(34) matches the experimental entry. No solid-state permittivity follows from a gas-phase static atomic polarizability alone. [RSC data](https://periodic-table.rsc.org/) · [2025 polarizability update, individual sources](https://ctcp.massey.ac.nz/2025Tablepol.pdf) · [Shannon 1976](https://doi.org/10.1107/S0567739476001551) · [All 23 ionic entries](ionic_radii.csv)

| Element | Covalent / nonbonded radius (Å, RSC) | Example ionic radius (pm; CN VI) | α₀ (atomic units) |
|---|---:|---|---:|
| Os | 1.36 / 2.16 | Os⁴⁺ 63 | 57 ± 3 |
| Ir | 1.32 / 2.13 | Ir³⁺ 68 | 54 ± 7 |
| Pt | 1.30 / 2.13 | Pt²⁺ 80 | 48 ± 4 |
| Au | 1.30 / 2.14 | Au³⁺ 85 | 36 ± 3 |
| Hg | 1.32 / 2.23 | Hg²⁺ 102 | 33.91 ± 0.34 |

**MEASURED / DERIVED.** The independent FRIB discovery collection lists 218 nuclides in this batch versus 217 in the IAEA ground-state extract. The difference is ¹⁶⁰Os (fusion evaporation, reported in 2024). The IAEA tables have 192 nonblank spin/parity entries including tentative assignments, and 80 retained charge radii. The two current source tables also retain the naturally abundant isotopes and their abundances. In the Standard Model reading of the ball center the nuclear valence content is u=2Z+N, d=Z+2N. This expresses the conserved net valence counts of Z protons and N neutrons. [FRIB catalogue and paper links for all 218](isotope_discoveries.csv) · [2024 discovery of osmium-160](https://doi.org/10.1103/PhysRevLett.132.072502) · [IAEA isotope table](isotopes.csv) · [IAEA API](https://nds.iaea.org/relnsd/v1/data?fields=ground_states&nuclides=all) · [2013 radius evaluation](https://doi.org/10.1016/j.adt.2011.12.006)

| Representative nucleus | Z, N | net u,d | Iπ | Ground dipole (µN) | Charge radius (fm, IAEA) |
|---|---|---|---|---:|---:|
| ¹⁹²Os | 76,116 | 268,308 | 0⁺ | 0 | 5.4126(15) |
| ¹⁹³Ir | 77,116 | 270,309 | 3/2⁺ | +0.1637 | 5.4032(1061) |
| ¹⁹⁵Pt | 78,117 | 273,312 | 1/2⁻ | +0.60952 | 5.4270(26) |
| ¹⁹⁷Au | 79,118 | 276,315 | 3/2⁺ | +0.145746 | 5.4371(38) |
| ²⁰²Hg | 80,122 | 282,324 | 0⁺ | 0 | 5.4648(33) |

**DERIVED / source check.** Exact spin zero enforces zero ground-state dipole. LiveChart's raw dipole fields of 0.79 for ¹⁹²Os and 1.4 for ²⁰²Hg cannot belong to those 0⁺ ground states. They remain labeled as raw source fields in the ledger. The three nonzero representatives above use isotope-specific entries in the CRC NMR parameter table. Raw API magnetic values for other states require level-resolved verification. [CRC NMR parameters, 91st ed. 2010–2011](https://diverdi.colostate.edu/all_courses/CRC%20reference%20data/NMR%20parameters.pdf) · [IAEA state-resolved moments](https://www-nds.iaea.org/publications/indc/indc-nds-0594.pdf)

## Mainstream-blend watch and limits

**HYPOTHESIS.** Jeromie's “vector determines the direction” has a signed peel observable in the [separate atomic ladder](../ladder/README.md). The crystal spacings, attenuation lengths, DC conductivities, nuclear radii and orbital ionization ratios above have distinct experimental definitions. A link-weight proposal for these materials needs a specified, phase-specific occupied projector and a defined set of neighboring sites. A liquid additionally needs a time- or ensemble-averaging prescription. The half intensity in Os is a statement about its measured complex optical indices and one interface geometry. Treat an identification with the equal-face peel loop as an additional hypothesis requiring a map of those observables. Every listed crystal is centrosymmetric in the bulk exemplar used here; a choice of a directed path could still break that symmetry. No element-specific HOMFLY, coloured Jones, Alexander, or Jeromie-polynomial assignment was found for these structures in the sources checked. No closed path or polynomial has been supplied by this computation.

**Set aside, with why.** The contact radii are geometrical conventions; the mercury liquid peak is not a cell edge. The COD results include alloy, molecule, theory and sparse-coordinate hits; [the exclusion ledger](set_aside_cells.csv) lists them individually. The [31 retained CIFs](crystals.csv) and [four Hg phases](mercury_cells.csv) are sourced exemplars rather than an exhaustive inventory at every temperature, pressure and particle shape. Neither an epoch-wide search for newer level-specific nuclear moments nor a complete angle-resolved optical spectrum for each element was performed.

Reproduce the derived quantities from this directory with `python optics.py`, `python mercury_phases.py` and `python audit.py`. [Run output](audit.txt)
