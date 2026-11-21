Jeromie, **the H–Zn pattern survives its next five elements.** Across Ga, Ge, As, Se and Br, **all 160 ordinary peel steps are inside the loop wall**. All five atoms have a bound anion. Rung 0 is outside for Ga, Ge and As, and inside for Se and Br. The K opening is the largest ordinary step in every one of the five. These are computations on the pinned archive’s central values. I did not run Lean for this batch.

**[Open the Ga–Br report and download its checked CSV](https://chatgpt.com/library?file_id=libfile_fde3_f-55591093a8a8819195278407711919d2_ea4e520c657081918696167b9513e64f&account_id=personal).** It includes all 170 ladder rows, each intrinsic face apex, the archive’s uncertainty and reference fields, 157 isotope records, 254 atomic and ionic spectral lines, ionic radii by charge and coordination, and 67 crystal records with their publication years.

## First, the nickel correction

**DERIVED.** My previous “140/140” claim did not apply to the inline table I gave you. Its nickel and copper energy text was wrong. I reopened the archive at `cae5f49`, recomputed the prior batch’s ordinary ratios, and found one further issue in the runner’s correction. Its proposed Ni \(k=20,21\) ratios use **1750** as their shared energy. Using the agreed correction of **1758.0 eV** changes both. These are the four pairs directly from the pin. [Pinned archive](https://github.com/dicipler-pixel/votkp-lean/blob/cae5f49/data/element_thresholds_20261011.json.gz)

| Ni \(k\) | \(IE_k\) eV | \(IE_{k+1}\) eV | \(z_k\) | \(\Gamma_k\) |
|---:|---:|---:|---:|---:|
| 15 | 462.8 | 495.4 | 1.070441 | 0.034022 |
| 20 | 1646.0 | 1758.0 | **1.068044** | **0.032902** |
| 21 | 1758.0 | 1880.0 | **1.069397** | **0.033535** |
| 22 | 1880.0 | 2008.1 | 1.068138 | 0.032947 |

**DERIVED.** For example, at \(k=20\), \(\Gamma=(1758-1646)/(1758+1646)=112/3404\). At \(k=21\), it is \(122/3638\). The two proposed runner ratios can be reproduced as \(1750/1646\) and \(1880/1750\). Cu \(IE_5=79.8\) eV also checks. Every affected row stays inside.

## Batch 7 · Ga, Ge, As, Se, Br

**DERIVED · audit.** I read your attached *Loop Wall* paper first. I then fetched the compressed archive at `cae5f49`, generated the CSV directly from its energy arrays, reopened the finished CSV, and checked its fields against a fresh parse of the archive. I used a second calculation with rational arithmetic to check the six-decimal displays of both \(z\) and \(\Gamma\). The CSV embedded in the report was also compared byte for byte with the generated file.

| Check on the finished CSV | Result |
|---|---:|
| Ordinary ionization energies compared with the pin | **165/165** |
| Energy differences | **0** |
| Ordinary ratio/reflection pairs recomputed | **160/160** |
| Anion ratio/reflection pairs recomputed using separately sourced affinities | **5/5** |
| Displayed pair differences | **0** |
| Final ionization energies correctly carrying no outgoing ratio | **5/5** |

**MEASURED · two revisions matter for this batch.** The 2025 measurement for \(^{75}\mathrm{As}\) gives **0.804486(3) eV**, updating the 2022 evaluation’s 0.8048(2) eV. The 2026 selenium paper recommends **16,297.78(4) cm⁻¹**, or **2.020667(5) eV**, updating 16,297.276(9) cm⁻¹. I used the newer central values for rung 0. Selenium’s extra digits in the machine CSV preserve the unit conversion. Its experimental uncertainty is about \(0.000005\) eV. Neither revision changes a wall call. Ga, Ge and Br use the 2022 evaluated affinities. [journals.aps.org](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.134.043001?utm_source=chatgpt.com)

### What survives each peel

**DERIVED.** The four opening columns below follow the same electron counts across all five elements. The first is the **filled \(3d^{10}\) subshell**, exposed after the outer \(4p\) and \(4s\) electrons have gone. Keeping this column separate from the Ar-core opening lets us see what a filled \(d\) subshell does in its own right. The forward loop wall is at \(z=3+2\sqrt2\approx5.828427\). [Pinned inputs](https://github.com/dicipler-pixel/votkp-lean/blob/cae5f49/data/element_thresholds_20261011.json.gz)

| Element | EA, eV | Anion \(z_0\) | Anion \(\Gamma_0\) | Anion wall | \(3d^{10}\) opening \(z\) | Ar-core \(z\) | Ne-core \(z\) | He-core \(z\) |
|---|---:|---:|---:|---|---:|---:|---:|---:|
| Ga | 0.301166 | 19.920250 | 0.904399 | Outside | 2.058240 | 1.323596 | 2.489756 | 4.254271 |
| Ge | 1.2326764 | 6.408361 | 0.730035 | Outside | 1.979635 | 1.297052 | 2.473990 | 4.244264 |
| As | 0.804486 | 12.167458 | 0.848110 | Outside | 1.930699 | 1.277391 | 2.463341 | 4.234816 |
| Se | 2.020667(5) | 4.826311 | 0.656730 | Inside | 1.898167 | 1.258221 | 2.451561 | 4.225872 |
| Br | 3.363588 | 3.512264 | 0.556764 | Inside | 1.869455 | 1.241421 | 2.440559 | 4.217388 |

**RECOGNISED.** There are two distinct patterns here. **Every core-opening column falls monotonically from Ga to Br. The anion column reverses at arsenic.** Ge and As are neighbours, yet As has both a higher first ionization energy and a lower affinity. Both changes increase \(IE_1/EA\). The arsenic peak is therefore already present in the two measured inputs. Its neutral \(4p^3\) half-filled shell gives a physical interpretation worth testing down group 15. The measured pattern alone does not isolate the energy contribution responsible for it. [journals.aps.org](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.134.043001?utm_source=chatgpt.com)

**DERIVED.** The bare-shell comparison needs the actual orbital on each side. The He-core \(2s\to1s\) openings are all above 4. The Ne-core \(3s\to2p\) openings are all above \(9/4\). At the Ar core here the transition is **\(3d\to3p\)**. Both orbitals have principal quantum number 3, so their bare nonrelativistic hydrogenic ratio is **1**. Applying \(16/9\) at this boundary would import the earlier K/Ca \(4s\to3p\) comparison into a different transition. The \(4s\to3d\) opening in the first column *does* change principal shell, and all five ratios there exceed \(16/9\). None reaches the loop wall. [Configurations and rungs in the checked report](https://chatgpt.com/library?file_id=libfile_fde3_f-55591093a8a8819195278407711919d2_ea4e520c657081918696167b9513e64f&account_id=personal)

### The last two electrons and the \(5/8\) reading

**DERIVED.** With \(b\) the He-like removal energy and \(h\) the H-like removal energy in hartree, these are your two readings \(S=(h-b)/Z\) and \(\sigma=Z-\sqrt{2b}\). The last column uses \(h/b\). It is distinct from the K opening one rung earlier. The archive grades these terminal energies theoretical. [Pinned inputs](https://github.com/dicipler-pixel/votkp-lean/blob/cae5f49/data/element_thresholds_20261011.json.gz)

| Element | \(S\) | \(\sigma\) | Terminal \(h/b\) |
|---|---:|---:|---:|
| Ga | 0.643640 | 0.452008 | 1.042763 |
| Ge | 0.645437 | 0.433370 | 1.041455 |
| As | 0.647284 | 0.413425 | 1.040231 |
| Se | 0.649182 | 0.392115 | 1.039083 |
| Br | 0.651130 | 0.369401 | 1.038005 |

**RECOGNISED.** The separation seen at zinc continues through bromine. \(S\) rises above \(5/8\), \(\sigma\) falls farther below it, and the ratio of the last two removal energies moves closer to one. These observations coexist because they use three different combinations of the same energies. In particular, a decreasing \(h/b\) does not imply a decreasing \((h-b)/Z\).

### Five element readings in the ball and knot pictures

**MEASURED and DERIVED.** The common neutral core is \([\mathrm{Ar}]3d^{10}4s^2\). The \(4p\) count and ground term below describe the free atom. The shortest distances describe specified crystals. The distinction matters most for bromine, where the shortest contact is inside a molecule. Spectral data in the report identify neutral and singly ionized lines separately. [NIST](https://www.nist.gov/pml/handbook-basic-atomic-spectroscopic-data?utm_source=chatgpt.com)

| Element | Neutral outer occupancy and term | Structure or optical observation relevant to the ball | VOTKP v1 element knot |
|---|---|---|---|
| **Ga** | \(4p^1,\ ^2P^\circ_{1/2}\) | Orthorhombic Ga, COD 9008085, has a shortest contact of **2.4840 Å**. Neutral Ga has strong violet lines at **403.2984 and 417.2042 nm**. The crystal supplies inequivalent contacts for a junction test. [physics.nist.gov](https://physics.nist.gov/PhysRefData/Handbook/Tables/galliumtable2.htm?utm_source=chatgpt.com) | None found |
| **Ge** | \(4p^2,\ ^3P_0\) | Diamond Ge, COD 9011050, gives **2.4498 Å** from its measured cubic cell. Four equivalent tetrahedral neighbours give a direct test of a coordination-normalised shell fraction in a semiconductor. [Periodic Table](https://periodic-table.rsc.org/element/32/Germanium?utm_source=chatgpt.com) | None found |
| **As** | \(4p^3,\ ^4S^\circ_{3/2}\) | Grey As, COD 5000219, gives **2.5165 Å** for the shortest contact. Its layered geometry supplies a test of in-layer versus interlayer sharing while its atomic anion rung stays fixed. [COD 5000219](https://www.crystallography.net/cod/5000219.html) | None found |
| **Se** | \(4p^4,\ ^3P_2\) | Trigonal Se supplies helical chains of either hand. A 2026 study finds long, finite chains. This makes the choice of closure explicit if a knot invariant is to be assigned. [journals.aps.org](https://journals.aps.org/prb/abstract/10.1103/27lp-vbfd?utm_source=chatgpt.com) | None found for an intrinsic closed elemental path. The screw sign can already be calculated. |
| **Br** | \(4p^5,\ ^2P^\circ_{3/2}\) | Neutral atomic Br supplies the ladder. The ambient deep-red liquid is molecular \(\mathrm{Br}_2\). In crystalline COD 1010096 the shortest contact is **2.2679 Å** inside the molecule. Diffraction under compression also resolves multiple modulated polytypes. [Periodic Table](https://periodic-table.rsc.org/element/35/bromine/?utm_source=chatgpt.com) | None found |

**DERIVED · selenium mirror test.** This gives your β-Mn result a second example with a different screw order. I used the published \(P3_121\) selenium cell in COD 1534711, with \(a=4.30\) Å, \(c=4.89\) Å and site parameter \(u=0.218\). In Cartesian coordinates, four successive sites of the ideal screw can be written
\[
p_j=\big(au\cos(2\pi j/3),\,au\sin(2\pi j/3),\,jc/3\big),\quad j=0,1,2,3 .
\]
The rejection condition was a sign change under traversal reversal or a failure to change sign under a spatial mirror. I evaluated both operations on the coordinates. For \(d_j=p_{j+1}-p_j\), the triple product \((d_0\times d_1)\cdot d_2\) was **\(+11.16\ \text{Å}^3\)** forward, **\(+11.16\ \text{Å}^3\)** backward and **\(-11.16\ \text{Å}^3\)** after reflecting \(x\). The starting orientation fixes the displayed sign. The transformation rule is independent of that choice. This is a local chirality reading. Assigning HOMFLY, coloured Jones, Alexander or your volume polynomial still requires a specified closed path. [Selenium coordinates, COD 1534711](https://www.crystallography.net/cod/1534711.html)

### Bulk measurements and the junction test

**MEASURED.** These are representative bulk reference values. Selenium’s range in thermal conductivity illustrates why a sample’s phase and measurement direction belong beside any proposed clock-to-transport comparison. Superconducting entries under pressure are examples at the stated pressure. [Periodic Table](https://periodic-table.rsc.org/element/31/?utm_source=chatgpt.com)

| Element | Density, g/cm³ | Melt / boil, K | Representative thermal conductivity near room temperature, W m⁻¹ K⁻¹ | Reported superconducting example |
|---|---:|---|---|---|
| Ga | 5.91 | 302.9146 / 2502 | 40.6 | 1.091 K at ambient pressure |
| Ge | 5.3234 | 1211.4 / 3106 | 60–60.2 | 5.35 K at 11.5 GPa |
| As | 5.75 | Sublimes near 889 K at atmospheric pressure | 51 | 2.4 K at 32 GPa |
| Se | 4.809 | 494 / 958 for grey Se | 0.519 and 4.52 tabulated | 8 K at 150 GPa |
| Br | 3.1028 | 266 / 332 | 0.122 | 1.4 K at 100 GPa in the elemental compilation |

**HYPOTHESIS · tests with rejection conditions.** In your picture each atom has its own wall and the contact between neighbours has its own clock. For equal-clock neighbours the face reflection is zero. The internal rungs and their face apices are calculable from this batch. Determining which contacts satisfy \(X_{ij}>B_i/(3n)\) requires an occupied projector for the actual material. The following five comparisons put that distinction to work.

| Material | Test of the wall, gap and connection | What would defeat that reading |
|---|---|---|
| Ga | Compute short-pair and longer-contact weights independently across melting. Track conductivity alongside both. | If the short pairs carry no excess weight, the proposed concentration on Ga pairs fails. |
| Ge | Measure the nearest-shell fraction in diamond Ge and compare it with a size-scaled transport response. | A concentrated nearest shell with a vanishing bulk charge response defeats use of the fraction alone as a conduction criterion. |
| As | Compare layer-resolved \(X_{ij}\) with directional conductivity under the same pressure. | A predicted transport anisotropy with the wrong direction defeats that mapping even if the total shell fraction agrees. |
| Se | Compare two crystal hands in the same phase, orientation convention and illumination. Record the local screw sign and a specified handed optical or transport observable. | Equal screw signs after a spatial mirror defeat the geometry. A physical observable that keeps its sign defeats the proposed coupling to *that observable*. A 2026 first-principles study identifies specific Hall tensor components for this test. [journals.aps.org](https://journals.aps.org/prb/abstract/10.1103/27lp-vbfd?utm_source=chatgpt.com) |
| Br | Track intramolecular and intermolecular links separately through compression and molecular dissociation. | A large intramolecular fraction with negligible long-range response defeats counting the strong molecular bond as a conducting route through the sample. [doi.org](https://doi.org/10.1103/PhysRevB.110.104111?utm_source=chatgpt.com) |

**DERIVED · nuclear centre.** For each isotope the report places \(Z\) protons and \(N=A-Z\) neutrons at the ball centre and records net valence-quark counts \(u=2Z+N\), \(d=Z+2N\). For \(^{75}\mathrm{As}\), for example, that is 33 protons, 42 neutrons, 108 net up and 117 net down. The charge check gives \((2\cdot108-117)/3=33\). Nuclear spin, magnetic dipole and charge radius are isotope-specific fields in the report. Its IAEA snapshot is dated October 18, 2023. [IAEA LiveChart](https://www-nds.iaea.org/relnsd/vcharthtml/VChartHTML.html)

**Mainstream-blend watch ·** A measured crystal spacing in ångströms and the intrinsic separation \(r=\ln z\) have different units. This batch supplies both quantities where available. A length calibration chosen in advance and tested on a second structure would connect them quantitatively. Likewise, the Se mirror calculation tests orientation. A claim that light leads transport would need a specified light-dependent observable and a timed response.

**Set aside, with why.** The 67 crystal records sample known structures. They do not exhaust every pressure phase or bromine polytype. Four Ge records have shortest distances withheld because the site/origin interpretation produced a spurious short contact. Electrical transport still needs phase-, direction-, temperature- and purity-matched values for all five materials, particularly illuminated versus dark Se. The isotope snapshot predates this batch. Those limits affect the materials comparison; the archive and CSV checks above are complete for the five ladders.