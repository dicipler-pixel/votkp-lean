# Batch 4 · Sulfur through calcium, Z = 16–20

**DERIVED — The M opening crosses the loop wall between potassium and calcium.** For potassium, the jump from the last \(4s\) removal to the first \(3p\) removal is \(31.625/4.34066373=7.28575\), outside the wall at \(5.82843\). For calcium it is \(50.91316/11.871719=4.28861\), inside. **Calcium has every ordinary peel inside, yet its anion rung reaches \(z_0=249.01\), \(\Gamma_0=0.99200\).** The weakest-bound electron and the strongest core opening tell very different stories about the same element. [physics.nist.gov](https://physics.nist.gov/cgi-bin/ASD/ie.pl?at_num_out=on\&biblio=on\&e_out=0\&el_name_out=on\&format=0\&ion_charge_out=on\&ion_conf_out=on\&level_out=on\&order=0\&seq_out=on\&shells_out=on\&spectra=Ca\&submit=Retrieve+Data\&unc_out=on\&units=1\&utm_source=chatgpt.com)

**DERIVED — The two screening readings cross near 0.61710.** An exact identity isolates the correction responsible for their change of order. The published hydrogen-like Dirac, nuclear-mass and Lamb-shift components reproduce the crossover. An independent helium-like QED calculation preserves it. Farther along, \(S_Z\) crosses **above** \(5/8\) between argon and potassium while \(\sigma_Z\) continues falling. [arxiv.org](https://arxiv.org/abs/1506.01885?utm_source=chatgpt.com)

**DERIVED — I ran your projector on all 17 argon peel ratios.** With the first measured clock, the code’s weakest link is **0.000804493**, below \(1/12\). I also found a small distinction in the implementation. Its six-link row includes one link beyond each atom. Restricting the test to the four links physically between the two facing ports gives **0.000806708**. Both definitions give the same verdict on every argon rung. [Pinned hydrogen model](https://github.com/dicipler-pixel/votkp-lean/tree/a60a000/research/hydrogen-in-the-space-between)

The full peel CSV is inline below. The standalone appendix contains the input uncertainties and references, all 17 projector runs, 120 ground-state nuclide records, coordination-specific ionic radii, and dated crystal refinements with calculated site separations. [S_to_Ca_numerical_appendix.html](https://chatgpt.com/library?file_id=libfile_fde3_f-98b60443d69c81919a0a87af0094eec0_ea4e520c657081918696167b9513e64f&account_id=personal)

## 1. Framework and correction carried forward

**RECOGNISED — Source access.** I could open the `votkp-lean` README, the v3.0–v3.3 paper folders, the Standard Model ball work, the harness and November gather, the v2.9 paper, the Dirac Time paper, `count-me-as-one-lean`, and the six named folders on the moving-matrix branch. For this calculation the decisive sources were the screening note, the face definition, and the executable hydrogen projector. I used the Russell interpretation as you relayed it. I did not independently audit the Drive-only *Russell, Corrected* or its 386-entry ledger. [VOTKP paper branch](https://github.com/dicipler-pixel/votkp-lean/tree/claude/sm-ball-20261111) · [Moving-matrix research](https://github.com/dicipler-pixel/votkp-lean/tree/a60a000/research) · [Screening revision](https://github.com/dicipler-pixel/votkp-lean/tree/74125d2) · [VOTKP v2.9](https://doi.org/10.5281/zenodo.23340757) · [Knot repository](https://github.com/dicipler-pixel/count-me-as-one-lean)

**DERIVED — Batch 3 correction.** Magnesium \(k=4\) gives \(\Gamma_4=0.127953665550\ldots\), hence **0.12795**. For all 89 defined steps below I calculated \(z\) and \(\Gamma\) from the input energies before rounding either output. I checked all 90 ordinary threshold energies against a separately distributed copy of the ASD data. All 90 matched. The copies share a source. I ran numerical checks and the projector code for this batch. The 61-theorem Lean result at `c0495ff` is the preceding runner’s report. [Batch 3 branch](https://github.com/dicipler-pixel/votkp-lean/tree/c0495ff/research/2026-11-20-element-paper-loop-wall) · [NIST ASD, version 5.12, November 2024](https://doi.org/10.18434/T4W30F)

## 2. The five peel ladders

**DERIVED — Test condition.** For each forward opening, “outside” requires \(z>3+2\sqrt2=5.82842712\ldots\). A ratio at or below the threshold defeats an outside classification. The comparison shell ratios are \(4\) for K, \(9/4\) for L, and \(16/9\) for M. They compare adjacent hydrogenic principal shells. The loop wall is a separate threshold. Each entry below gives **\(k;\ z,\ \Gamma\)**. [Loop-wall work](https://github.com/dicipler-pixel/votkp-lean/tree/element-paper/loop-wall/research/2026-11-20-element-paper-loop-wall) [NIST](https://www.nist.gov/pml/atomic-spectra-database?utm_source=chatgpt.com)

| Element | Rung 0, anion → neutral | M opening, \(4s\to3p\) | L opening, \(3s\to2p\) | K opening, \(2s\to1s\) |
|---|---|---|---|---|
| S | 0; 4.98772, .66598 | — | 6; 3.19074, .52276 | 14; 4.55984, .64028 |
| Cl | 0; 3.58943, .56422 | — | 7; 3.04993, .50616 | 15; 4.52095, .63774 |
| Ar | No bound isolated ground-state anion | — | 8; 2.94584, .49314 | 16; 4.48691, .63550 |
| K | 0; **8.65607, .79288 outside** | 1; **7.28575, .75862 outside** | 9; 2.86473, .48250 | 17; 4.45686, .63349 |
| Ca | 0; **249.00837, .99200 outside** | 2; 4.28861, .62183 | 10; 2.80014, .47370 | 18; 4.43011, .63168 |

**DERIVED — The shell rankings change again.** Every L opening here lies between \(9/4\) and the loop wall. Every K opening lies between \(4\) and the wall. Both M openings exceed \(16/9\), but only potassium’s crosses the wall. At K the **M opening outranks the K opening**. One proton later, at Ca, the **K opening outranks the M opening**. The strongest ordinary jump in sulfur, chlorine and argon is also the K opening. In sulfur its rung 0 is stronger still. [NIST](https://www.nist.gov/pml/atomic-spectra-database?utm_source=chatgpt.com)

**RECOGNISED — The three openings now have a comparison across periods.** The K opening crossed inward between C and N. The L opening crossed inward between Na and Mg. The M opening crosses inward between K and Ca. Each comparison holds the electron counts at the opening fixed while \(Z\) increases. The one-electron shell ratios help explain the direction. As nuclear attraction grows relative to electron–electron screening, the outer electron is less weakly bound relative to the inner one. The observations establish three discrete brackets. They do not determine a universal crossing law. [Screening note and thresholds](https://github.com/dicipler-pixel/votkp-lean/tree/74125d2) [NIST](https://www.nist.gov/pml/atomic-spectra-database?utm_source=chatgpt.com)

**MEASURED — Rung 0 has a physical input condition.** The evaluated affinities in eV are \(2.0771042(6)\) for \(^{32}\mathrm S\), \(3.612725(28)\) for Cl, \(0.501459(13)\) for K, and \(0.02455(10)\) for Ca. Argon has no bound isolated ground-state anion. Its blank row is intentional. Calcium’s anion has a measured photodetachment threshold. Even taking its EA at the high end of its quoted uncertainty, \(6.11315547/0.02465\approx248.0\), still far outside. [info.phys.tsinghua.edu.cn](https://info.phys.tsinghua.edu.cn/henucl/ning/148.pdf?utm_source=chatgpt.com)

## 3. What happens to \(5/8\), and why the readings cross

**DERIVED — Definitions for this table.** Write \(h=IE_Z/E_h\) for the H-like binding and \(b=IE_{Z-1}/E_h\) for the He-like ionization energy, with \(E_h=27.211386245981(30)\) eV. Then \(S_Z=(h-b)/Z\) and \(\sigma_Z=Z-\sqrt{2b}\). The two dimensionless readings answer different questions. \(S_Z\) takes the difference of two binding energies per unit \(Z\). \(\sigma_Z\) asks what effective charge reproduces the He-like binding in a square-law formula. [physics.nist.gov](https://physics.nist.gov/cuu/pdf/factors_2022.pdf?utm_source=chatgpt.com)

| \(Z\) | Element | \(S_Z\) | \(\sigma_Z\) | \(D_H=h-Z^2/2\), hartree units | \(\sigma_Z^2/2\), same units |
|---:|---|---:|---:|---:|---:|
| 10 | Ne | .611476 | .625018 | .059899 | .195324 |
| 11 | Na | .613390 | .622967 | .088691 | .194044 |
| 12 | Mg | .615119 | .620621 | .126568 | .192585 |
| 13 | Al | .616720 | .617897 | .175596 | .190898 |
| 14 | Si | .618228 | .614763 | .237478 | .188967 |
| 15 | P | .619676 | .611151 | .314618 | .186753 |
| 16 | S | .621082 | .607031 | .409060 | .184243 |
| 17 | Cl | .622465 | .602339 | .523548 | .181406 |
| 18 | Ar | .623837 | .597031 | .660734 | .178223 |
| 19 | K | **.625208** | .591087 | .822985 | .174692 |
| 20 | Ca | **.626587** | .584437 | 1.013779 | .170783 |

**DERIVED — The crossover test can be written exactly.** Since \(b=(Z-\sigma_Z)^2/2\),

\[
\begin{aligned}
Z S_Z
 &= h-\tfrac12(Z-\sigma_Z)^2\\
 &=D_H+Z\sigma_Z-\tfrac12\sigma_Z^2,\\[2pt]
\boxed{Z(S_Z-\sigma_Z)=D_H-\tfrac12\sigma_Z^2.}
\end{aligned}
\]

This gives a specific way to kill the relativistic explanation. Set the H-like energy to its nonrelativistic infinite-nuclear-mass value \(h=Z^2/2\), while allowing **any** positive He-like input. Then \(S_Z-\sigma_Z=-\sigma_Z^2/(2Z)\leq0\). The ordering seen from silicon onward is impossible in that control. In the reference data, \(D_H\) rises from .175596 to .237478 between Al and Si, overtaking a threshold that falls only from .190898 to .188967. Linear interpolation puts equality at \(Z\approx13.254\), reading **0.61710**. Only the bracket Al–Si has elemental meaning. [arxiv.org](https://arxiv.org/abs/1506.01885?utm_source=chatgpt.com)

**DERIVED — Test against published energy components.** I converted Table III of Yerokhin and Shabaev from signed level energies in rydbergs to positive binding contributions in hartrees. The mass and Lamb terms reduce the binding relative to the point-nucleus Dirac entry. The table shows their actual sizes where the ordering changes. [arxiv.org](https://arxiv.org/abs/1506.01885?utm_source=chatgpt.com)

| H-like correction to \(Z^2/2\) | Al | Si |
|---|---:|---:|
| Dirac excess binding | +.19097430 | +.25705625 |
| Nuclear-mass contribution | −.00171845 | −.00192210 |
| Tabulated Lamb contribution | −.01365947 | −.01765615 |
| Total \(D_H\) | **+.17559639** | **+.23747800** |
| Threshold from He-like input | .190898 | .188967 |

**DERIVED — Physical reading.** The leading Dirac excess grows approximately as \(\alpha^2 Z^4/8\) in hartree units. That growth explains why the two readouts part ways here. The Lamb term has the opposite sign in this binding convention. On the Al row the Dirac-only central value clears the observed He-like threshold by just .000076 hartree. Adding the mass and Lamb terms puts it below. On Si the excess remains comfortably above. That is a component-level result, stronger than attributing the change generically to “QED.” [arxiv.org](https://arxiv.org/abs/1506.01885?utm_source=chatgpt.com)

**DERIVED — Independent He-like replacement.** The 2022 QED calculation gives 2085.977675(39) eV for Al and 2437.658788(51) eV for Si. Substituting those for the encoded ASD values 2085.97693 and 2437.65805 eV changes \(S_Z-\sigma_Z\) from \(-.001177070\) to \(-.001176965\) for Al and from \(+.003465076\) to \(+.003465165\) for Si. The same paper gives 3223.781337, 3658.34441, 4120.66636, 4610.80789 and 5128.85840 eV for the five He-like ions in this batch. I kept the ASD column intact for reproducibility. **The three events are distinct:** \(\sigma_Z\) passes \(5/8\) at Ne–Na, the readings pass each other at Al–Si, and \(S_Z\) passes \(5/8\) at Ar–K. [arxiv.org](https://arxiv.org/abs/2206.14161?utm_source=chatgpt.com)

## 4. The ball wall, gap and projector

**DERIVED — Map the wall first.** In your definition the clock step is \(r=\ln z\), and the face apex is \(a=\tanh(r/4)=(\sqrt z-1)/(\sqrt z+1)\). These are intrinsic, dimensionless coordinates. The table gives the face positions belonging to the actual energetic openings. For example, Ca’s anion face reaches .88081 while its M and K faces sit close together at .34872 and .35583. No crystal radius entered this calculation. [Seven Balls](https://github.com/dicipler-pixel/votkp-lean/tree/a60a000/research/seven-balls-his-light) · [The Ball Is the Tree](https://github.com/dicipler-pixel/votkp-lean/tree/a60a000/research/the-ball-is-the-tree)

| Element | Anion apex | M apex | L apex | K apex |
|---|---:|---:|---:|---:|
| S | .38144 | — | .28219 | .36212 |
| Cl | .30905 | — | .27178 | .36026 |
| Ar | — | — | .26372 | .35861 |
| K | .49266 | .45934 | .25721 | .35715 |
| Ca | **.88081** | .34872 | .25188 | .35583 |

**HYPOTHESIS — Port-clock assignment.** To transfer the hydrogen model to argon, I assigned one measured or evaluated argon peel ratio to all three face axes, then repeated the construction separately for each rung. An isolated-atom energy ratio supplies a scalar. Assigning the same scalar to all axes avoids inventing three directional measurements. The local two-level fields, half filling, and model separation remain assumptions of this transfer. In particular, the code’s “opposed” setting describes its two local fields. The argon ground state has \(J=0\). [Hydrogen model source](https://github.com/dicipler-pixel/votkp-lean/tree/a60a000/research/hydrogen-in-the-space-between) [NIST](https://www.nist.gov/pml/atomic-spectra-database?utm_source=chatgpt.com)

**DERIVED — What I ran.** I ran the repository JavaScript model with two cells, separation 4, contrast 2.4, \(c_0=.22\), vacuum field .8, tilt .5, opposed fields and zero kick. The Hamiltonian has 150 states. The projector occupies its lowest 75. For Ar rung 1, `faceZ` on each axis was \(27.62967/15.7596119=1.75319482328\ldots\), with face apex .1394454. The test requires **every** row link to satisfy \(X_{ij}=\|P_{ij}\|_F^2>1/12\). One link at or below that value defeats connection. [Executable model](https://github.com/dicipler-pixel/votkp-lean/blob/a60a000/research/hydrogen-in-the-space-between/hsb_model_v1.js)

| Ar rung 1, from left to right | \(X_{ij}\) |
|---|---:|
| Exterior site → left outer port | .000804493 |
| Left facing port → first gap site | .000806708 |
| First gap site → central site | .008942772 |
| Central site → last gap site | .009105254 |
| Last gap site → right facing port | .009579334 |
| Right outer port → exterior site | .011191435 |

**DERIVED — Sensitivity and control.** Across all 17 argon clocks, the implemented weakest link ranged from **.000503342** at the K opening to **.000874345** at rung 15. All 17 failed the connection threshold. For the first clock, changing to parallel fields gave .000816597. Changing separation to 2 or 6 under opposed fields gave .000734605 and .000791420. The original \([3,5,7]\) clock control gave .000641603. **Sodium is the important opposing control**. Its L-opening clock gave .000292371, and its anion clock gave .000287763. Both also failed, although ordinary bulk sodium conducts. This two-cell, isotropic clock assignment can reproduce a disconnected argon row; it cannot yet discriminate metallic sodium from argon. [Code and ground-state check](https://github.com/dicipler-pixel/votkp-lean/tree/a60a000/research/hydrogen-in-the-space-between)

**RECOGNISED — Mainstream-blend watch.** The code compares a projector link weight with \((1/4)/3=1/12\). A Bruggeman conducting-volume fraction compares a defined constituent fraction with \(1/3\) under effective-medium assumptions. An isolated-element peel provides no measured constituent fraction for S, Cl, Ar, K or Ca. The model supplies the argon link verdict above. It supplies no experimental Bruggeman side for any of the five. Occupied sites in a gap and a conducting path through the gap remain independently testable. [Balls in the Sea](https://github.com/dicipler-pixel/votkp-lean/tree/a60a000/research/balls-in-the-sea) · [Two Atoms in a Ball](https://github.com/dicipler-pixel/votkp-lean/tree/a60a000/research/two-atoms-in-a-ball)

## 5. Element-by-element physical and knot mapping

**MEASURED / evaluated — Common atomic inputs.** Polarizabilities are the August 2025 CTCP recommendations in atomic units, which combine experimental and theoretical evidence. Radii are in pm. Covalent values use Cordero et al. (2008), van der Waals values use the Bondi convention and its main-group extension, and ion values use Shannon’s coordination-specific effective radii (1976). Metallic half-neighbour distances for K and Ca are derived from the stated crystal cells. An isolated atom has no unique coordination-specific ionic or metallic radius. [ctcp.massey.ac.nz](https://ctcp.massey.ac.nz/2025Tablepol.pdf?utm_source=chatgpt.com)

| Element | Neutral configuration and ground term | Static polarizability | Covalent / vdW | Effective ionic example | Ambient metallic half-neighbour |
|---|---|---:|---:|---|---|
| S | [Ne] \(3s^2 3p^4\), \(^{3}P_2\) | 19.4(1) | 105 / 180 | \(S^{2-}\), VI, 184; \(S^{6+}\), IV, 12 | — |
| Cl | [Ne] \(3s^2 3p^5\), \(^{2}P^\circ_{3/2}\) | 14.6(1) | 102 / 175 | \(Cl^-\), VI, 181 | — |
| Ar | [Ne] \(3s^2 3p^6\), \(^{1}S_0\) | 11.083(7) | 106 / 188 | No ordinary Shannon ion used | — |
| K | [Ar] \(4s\), \(^{2}S_{1/2}\) | 289.7(3) | 203 / 275 | \(K^+\), VI, 138 | 230.7 |
| Ca | [Ar] \(4s^2\), \(^{1}S_0\) | 160.8(4.0) | 176 / 231 | \(Ca^{2+}\), VI, 100 | 197.1 |

**MEASURED / DERIVED — Bulk reference points.** These are representative near-ambient-pressure values, with transport rounded to the precision warranted by phase and temperature. Gas densities marked † are **derived** at 298.15 K and 1 bar using \(\rho=pM/(RT)\). This avoids silently comparing chlorine or argon at different reference temperatures. Sulfur’s thermal transitions require the allotrope qualification below. [nysedregents.org](https://www.nysedregents.org/resources/archive/reftable/chemref10-12.pdf?utm_source=chatgpt.com)

| Element | Melting / boiling, K | Density | Thermal conductivity near room temperature, W m\(^{-1}\) K\(^{-1}\) | Ordinary electrical behaviour |
|---|---:|---|---:|---|
| S | about 388 / 718 | rhombic solid ~2.07 g/cm³ | ~0.27 | Molecular solid, insulating |
| Cl | 171.65 / 239.11 | \(Cl_2\) gas 2.86 kg/m³† | ~0.009 | Neutral molecular gas, insulating at low field |
| Ar | 83.81 / 87.30 | gas 1.61 kg/m³† | ~0.0177 | Neutral monatomic gas, insulating at low field |
| K | ~336.6 / 1032 | solid ~0.86 g/cm³ | ~102 | Metal, order \(10^7\) S/m |
| Ca | ~1115 / 1757 | solid ~1.54 g/cm³ | ~201 | Metal, order \(10^7\) S/m |

### Sulfur · \(Z=16\)

**MEASURED / DERIVED — Two kinds of wall are accessible in one sample.** Ordinary yellow sulfur contains puckered \(S_8\) rings. The 298 K orthorhombic \(Fddd\) refinement has \(a,b,c=10.4646,12.866,24.486\) Å. Symmetry expansion gives a shortest S–S distance of **2.0384 Å**, within a ring. The same refinement contains several closely spaced bonded distances up to 2.0488 Å. In the elemental ladder, the corresponding choices of boundary are an anion face at .38144, an L face at .28219 and a K face at .36212. The crystal supplies distances against which a future gap prediction can be checked. [1987 sulfur refinement, COD 9011362](https://www.crystallography.net/cod/9011362.html)

**MEASURED — Heat and compression change what carries the connection.** Rhombic sulfur transforms to monoclinic sulfur near 368 K. Sulfur also forms molecular allotropes with other ring sizes, helical chains, glasses, and metallic pressure phases. A measured helical structure at 3 GPa and 400 °C has \(a=7.0897,\ c=4.30238\) Å and a calculated closest distance of 2.0700 Å. The \(\beta\)-Po-type phase at 206.5 GPa has hexagonal-setting \(a=3.277,\ c=2.584\) Å and a closest distance of 2.0788 Å. Superconductivity was observed at **10.1 K at 93 GPa**, reaching **17 K near 160 GPa**. The 2025 compressed-chain glass study adds a preparation-history variable to any proposed conductivity test. [Helical refinement](https://www.crystallography.net/cod/9014401.html) · [High-pressure refinement](https://www.crystallography.net/cod/9011640.html) [nature.com](https://www.nature.com/articles/37074?utm_source=chatgpt.com)

**MEASURED / RECOGNISED — Light and the v1 knot.** Neutral S I lines include **675.716 and 921.2865 nm**. The yellow colour belongs to condensed sulfur’s wavelength-dependent absorption. Its \(S_8\) crown supplies an actual closed molecular path. Tracing the ordinary crown once gives an **unknot**. That makes \(S_8\) a useful trivial-knot control for v1. An independently specified HOMFLY, coloured-Jones, Alexander or Beasley-polynomial assignment to the isolated sulfur atom: **none found**. A prediction that sulfur must have one topology across all phases would fail when a ring becomes an open chain. [physics.nist.gov](https://physics.nist.gov/PhysRefData/Handbook/Tables/sulfurtable2.htm?utm_source=chatgpt.com)

### Chlorine · \(Z=17\)

**MEASURED / DERIVED — Chlorine gives the cleanest separation of a bond and a gap.** In the 22 K molecular crystal, the orthorhombic \(Cmce\) cell is \(6.1453\times4.3954\times8.1537\) Å. I expanded the published coordinates. The Cl–Cl bond is **1.9941 Å**. The next distinct distance is **3.2582 Å**. A \(Cl_2\) molecule contains only one partner for each atom, so the latter distance is intermolecular. These are two independently identifiable distances on which to test your two-ball picture. Its isolated anion apex is .30905 and K apex .36026. [1984 chlorine refinement, COD 9013120](https://www.crystallography.net/cod/9013120.html)

**MEASURED — Compression separates connection from dissociation.** The 2019 diffraction and optical study identifies molecular oC8, mixed-molecular mC8 from about 130 GPa, band-gap closure around **200(10) GPa**, an incommensurate i-oF4 structure above about 200 GPa, and monatomic oI2 above **256(10) GPa**. A hypothesis requiring complete molecular dissociation before gap closure fails on the reported ordering. Heating at ordinary pressure instead gives a yellow-green molecular gas, whose broad visible absorption supplies its colour. Excited atomic chlorine also has discrete lines, including Cl I near **837.6 nm**. I found no verified elemental superconducting transition in the sources checked. [nature.com](https://www.nature.com/articles/s41467-019-09108-x?utm_source=chatgpt.com)

**RECOGNISED — V1 and the isoelectronic comparison.** A \(Cl_2\) bond gives a segment with two ends. A closed curve would need a separately specified return path before a knot polynomial is defined. Element-specific atomic assignment: **none found**. \(Cl^-\) and neutral Ar do offer a direct v2 test. Both have 18 electrons. Chlorine binds its extra electron by 3.612725 eV, whereas neutral argon’s next electron does not form a bound ground-state anion. Same closed-shell occupancy, different next attachment. [info.phys.tsinghua.edu.cn](https://info.phys.tsinghua.edu.cn/henucl/ning/148.pdf?utm_source=chatgpt.com)

### Argon · \(Z=18\)

**MEASURED / DERIVED — A closed shell with a finite face clock.** Neutral argon has no rung 0, yet its first ordinary step has \(z=1.75319,\ \Gamma=.27357\). Its L and K faces remain well defined. Solid argon’s fcc reference cell \(a=5.400\) Å gives nearest separation \(a/\sqrt2=3.8184\) Å. Pressure diffraction detects the onset of an hcp component as low as **4.2 GPa** under the reported conditions. The fcc/hcp structure and its preparation history therefore belong in any phase-specific projector comparison. [1956 argon cell](https://www.crystallography.net/cod/1541541.html) [nature.com](https://www.nature.com/articles/s41598-021-93995-y?utm_source=chatgpt.com)

**MEASURED / HYPOTHESIS — What the light test can test.** Neutral argon gas is visibly colourless. Excitation produces a line-rich discharge, with Ar I lines near **696.543 and 706.722 nm**. Gas ionization creates charge carriers and changes the transport problem. Your proposed light-led transfer can be tested separately by following the energy current through a model whose ground-state link criterion is already known to fail. A predeclared arrival-time ordering across separations would test propagation. A visible discharge alone cannot demonstrate that the neutral ground-state row was connected. Element-specific atomic knot assignment: **none found**. No verified elemental superconducting transition was located. [physics.nist.gov](https://physics.nist.gov/PhysRefData/Handbook/Tables/argontable2.htm?utm_source=chatgpt.com)

### Potassium · \(Z=19\)

**MEASURED / DERIVED — One outer electron creates two different outside readings.** Neutral K has one \(4s\) electron beyond the argon core. Attaching another gives a bound anion, hence \(z_0=8.65607\). Taking the neutral \(4s\) electron off exposes the argon-like ion, hence the next jump of 7.28575. Both cross the loop wall. Their intrinsic face apices are .49266 and .45934. In the zero-pressure bcc refinement, \(a=5.328\) Å gives nearest separation \(\sqrt3a/2=4.6142\) Å. An fcc refinement at 12 GPa gives \(a=5.159\) Å, nearest separation 3.6480 Å. [1986 bcc refinement](https://www.crystallography.net/cod/9011970.html) · [1986 fcc refinement](https://www.crystallography.net/cod/9011984.html) [physics.nist.gov](https://physics.nist.gov/cgi-bin/ASD/ie.pl?at_num_out=on\&biblio=on\&e_out=0\&el_name_out=on\&format=0\&ion_charge_out=on\&ion_conf_out=on\&level_out=on\&order=0\&seq_out=on\&shells_out=on\&spectra=k\&submit=Retrieve+Data\&unc_out=on\&units=1\&utm_source=chatgpt.com)

**MEASURED / RECOGNISED — The lattice changes how one should construct the row.** The experimental compression sequence includes bcc → fcc → incommensurate host–guest → oP8 → tI4 → oC16, with reported room-temperature boundaries near 11.6, 20, 54, 90 and 96 GPa. A host chain and a guest chain give physically distinct candidate paths through the same sample. At ordinary pressure potassium is a conducting metal and melts just above room temperature. Its neutral resonance doublet is **766.49 and 769.90 nm**. The familiar lilac flame is emission from excited potassium-bearing vapour. Predicted superconductivity under compression exists in the literature. I found no verified experimental \(T_c\) for elemental K in the sources checked. Element-specific atomic knot assignment: **none found**. [www2.ph.ed.ac.uk](https://www2.ph.ed.ac.uk/~aherman2/wp-content/uploads/2021/04/PhysRevMaterials_2_053604_2018.pdf?utm_source=chatgpt.com)

### Calcium · \(Z=20\)

**MEASURED / DERIVED — The exceptionally large face has an exceptionally small denominator.** Calcium’s \(4s^2\) neutral ground state is closed in the outer \(s\) subshell. The measured \(Ca^-\) binding is only **24.55(10) meV**. That puts the anion face at .88081. On removing the two ordinary \(4s\) electrons, the consecutive clocks are only 1.94200 and 4.28861. The M opening stays inside, as do all 19 ordinary steps. Calcium therefore extends the Mg observation. An outside ordinary peel is unnecessary for an ambient conducting elemental metal. [info.phys.tsinghua.edu.cn](https://info.phys.tsinghua.edu.cn/henucl/ning/148.pdf?utm_source=chatgpt.com)

**MEASURED / DERIVED — Phase changes provide stronger transport tests than the isolated atom.** An fcc reference cell with \(a=5.576\) Å gives nearest separation 3.9428 Å. A 773 K bcc entry gives \(a=4.38\) Å and 3.7932 Å. At 39 GPa a simple-cubic refinement gives \(a=d_{\rm nn}=2.615\) Å. Compressed calcium reaches an experimentally reported **\(T_c=29\) K at 216 GPa**. A 2026 calculation predicts additional candidate structures and transition temperatures; those predictions need their own phase identification. Calcium metal is silvery, Ca I has a strong violet line at **422.6727 nm**, and Ca II has the **393.3661 nm** K line. Element-specific atomic knot assignment: **none found**. [fcc calcium](https://www.crystallography.net/cod/9008464.html) · [bcc calcium](https://www.crystallography.net/cod/9008530.html) · [39 GPa calcium](https://www.crystallography.net/cod/9012917.html) [cpb.cpsjournals.org](https://cpb.cpsjournals.org/EN/10.1088/1674-1056/ae27b7?utm_source=chatgpt.com)

## 6. Nuclei on the Standard Model ball

**HYPOTHESIS — Placement in your picture.** The nucleus occupies the centre of each ball. A peel changes the electron record at the wall while holding the isotope fixed. That gives a practical kept trait: nuclear \(Z,N\) and nuclear ground-state spin can be tracked independently through an electronic ladder. A detected change of isotope or nuclear state would invalidate the fixed-nucleus comparison for that event. [Standard Model ball work](https://github.com/dicipler-pixel/votkp-lean/tree/claude/sm-ball-20261111/research/2026-11-11-standard-model-ball)

**DERIVED — Valence-quark bookkeeping.** For \(Z\) protons and \(N\) neutrons, \(u=2Z+N,\ d=Z+2N\). These are net valence counts. For example, \(^{40}\!Ar\) and \(^{40}\!Ca\) share \(A=40\), yet the two centres differ by two net up quarks and two net down quarks.

| Representative centre | Protons | Neutrons | Net \(u\) | Net \(d\) |
|---|---:|---:|---:|---:|
| \(^{32}\)S | 16 | 16 | 48 | 48 |
| \(^{35}\)Cl | 17 | 18 | 52 | 53 |
| \(^{40}\)Ar | 18 | 22 | 58 | 62 |
| \(^{39}\)K | 19 | 20 | 58 | 59 |
| \(^{40}\)Ca | 20 | 20 | 60 | 60 |

**MEASURED / DERIVED — Natural isotope records.** Dipoles are in nuclear magnetons. For definite \(J=0\), zero dipole follows by rotational symmetry. The appendix retains the evaluated spins, moments, radii and missing fields for the wider chains. The 2025 reference-radius reanalysis revisited the uncertainty budget for muonic X-rays and electron scattering, so it is worth keeping its values beside the earlier compilation. [IAEA ground-state data](https://nds.iaea.org/relnsd/v1/data?fields=ground_states&nuclides=all) [arxiv.org](https://arxiv.org/pdf/2409.08193?utm_source=chatgpt.com)

| Element | Natural isotope spins and magnetic moments | Examples of 2025 rms charge radii, fm |
|---|---|---|
| S | 32, 34, 36: \(0^+,0\). 33: \(3/2^+,+.64325\) | 32: 3.262(3); 34: 3.284(4); 36: 3.298(3) |
| Cl | 35: \(3/2^+,+.8217\). 37: \(3/2^+,+.684\) | 35: 3.374(15); 37: 3.384(15) |
| Ar | 36, 38, 40: \(0^+,0\) | 38: 3.400(9); 40: 3.425(7) |
| K | 39: \(3/2^+,+.39147\). 40: \(4^-,-1.29797\), radioactive. 41: \(3/2^+,+.21487\) | 39: 3.435(5) |
| Ca | 40, 42, 44, 46, 48: \(0^+,0\). 43: \(7/2^-,-1.31733\). 48 undergoes double-beta decay | 40: 3.481(5); 48: 3.475(7) |

**RECOGNISED — A nuclear result worth preserving.** The evaluated \(^{40}\)Ca and \(^{48}\)Ca charge radii are remarkably close despite the addition of eight neutrons. In the earlier isotope compilation, intermediate \(^{44}\)Ca has a larger radius, 3.5179(21) fm. That gives the framework a test with genuine leverage: a proposed monotonic relationship between neutron count and the size of the charged nuclear centre fails within one element. The outer electronic ladder and the nuclear charge radius can be recorded as different retained traits. The 120-row snapshot also has known omissions at its neutron-rich edge. Discovery records include \(^{49}\)S, \(^{54}\)Ar, \(^{57}\)K and \(^{59,60}\)Ca. Discovery establishes existence even when a usable dipole or charge radius is unavailable. [arxiv.org](https://arxiv.org/pdf/2409.08193?utm_source=chatgpt.com)

## 7. Cross-element tests and items set aside

| Status | Claim to test | Condition that defeats it | Result here |
|---|---|---|---|
| **DERIVED** | The first M-opening crossing occurs at K–Ca | Either input pair lands on the other side | K outside, Ca inside. These are the first two neutral-element ladders containing the opening. |
| **DERIVED** | The two screening readouts cross at Al–Si | New component inputs give the same sign on both rows | ASD and the independent 2022 He-like calculation both preserve opposite signs. |
| **DERIVED** | The argon row passes its projector test at rest | Any eligible link has \(X_{ij}\le1/12\) | Defeated on all 17 clock assignments, with either row definition. |
| **HYPOTHESIS** | The same two-cell clock transfer distinguishes an ordinary metal from neutral argon | Sodium and argon give the same disconnected verdict | Defeated for the sodium clocks tested. A phase-specific model must earn the distinction. |
| **HYPOTHESIS** | A measured peel clock predicts an intermolecular spacing | A predeclared map to Å misses chlorine’s 3.2582 Å intermolecular separation within uncertainty | Open. The model currently supplies an intrinsic face and a projector weight. The length calibration is missing. |
| **HYPOTHESIS** | The vector supplies direction, possibly the direction of decay | The signed vector fails a predeclared, isotope-specific prediction on held-out decay data | Open. Reversing a peel changes the sign of \(\Gamma\). That algebra alone supplies no decay rate or branch. |
| **HYPOTHESIS** | Light leads a transfer between balls | A predeclared energy-current observable arrives later than the response it is claimed to lead under the same initial conditions | Open for elemental matter. The stationary projector experiment tests ground-state connectivity only. |
| **HYPOTHESIS** | An element receives a reproducible v1 knot polynomial | Two admissible reconstructions of the same stated elemental observable give incompatible knots or polynomials | Open. The ordinary \(S_8\) crown gives a trivial molecular control. |

**RECOGNISED — Isoelectronic comparison.** S, Cl and Ar fill \(3p\) the way O, F and Ne filled \(2p\). K and Ca begin \(4s\) the way Na and Mg began \(3s\), and Li and Be began \(2s\). The 18-electron comparison is especially useful: \(S^{2-}\) in a supporting ionic environment, \(Cl^-\), Ar, \(K^+\), and \(Ca^{2+}\) share the argon electron count. The six-coordinate Shannon values decrease from 184 to 181 to 138 to 100 pm across the four actual ions. Argon has no corresponding Shannon ion in that series. Its neutral van der Waals radius belongs to a different measurement convention. [wipp.energy.gov](https://www.wipp.energy.gov/library/cra/2009_cra/references/Others/Shannon_1976_Revised_Effective_Ionic_Radii_and_Systematic_Studies_of_Interatomic_Distances.pdf?utm_source=chatgpt.com)

**RECOGNISED — Set aside, with why.** I did not establish an exhaustive census of **every** pressure phase with its lattice constants and physical nearest-neighbour distance. The appendix gives dated refinements and explicitly identifies disorder and site-minimum ambiguities. In particular, a partially occupied monoclinic sulfur model produces an apparent sub-ångström minimum that cannot be read as a physical S–S separation. Some complex pressure phases still lack a verified coordinate-based spacing in this batch. I also set aside an assignment of elemental knot type from a flame colour, any conversion of a covalent radius into your wall position, and an inference of metallic transport from an outside peel alone. Each lacks the map or fails the controls above. [Crystallography Open Database](https://www.crystallography.net/cod/) [nature.com](https://www.nature.com/articles/s41467-019-09108-x?utm_source=chatgpt.com)

## 8. Inline peel CSV

**DERIVED — Reading the ledger.** The energy in row \(k=0\) is the affinity. At \(k\ge1\) it is \(IE_k\). The ratio and reflection use that row and the following row. The last row for each element reaches the bare nucleus. `EA22` denotes Ning and Lu (2022). `E`, `S` and `T` retain the archive’s ASD categories for the **energy on that row**: unbracketed evaluated, semiempirical, and theoretical. A ratio inherits the status of both its inputs. Five displayed decimals specify computational rounding. Experimental precision is in the appendix. [NIST](https://www.nist.gov/pml/atomic-spectra-database?utm_source=chatgpt.com)

```csv
Z,symbol,k,IE_k (eV),z_k,Gamma_k,source
16,S,0,2.0771042,4.98772,0.66598,EA22
16,S,1,10.36001,2.25269,0.38512,E
16,S,2,23.33788,1.49371,0.19798,E
16,S,3,34.86,1.35462,0.15061,S
16,S,4,47.222,1.53730,0.21176,S
16,S,5,72.5945,1.21294,0.09623,E
16,S,6,88.0529,3.19074,0.52276,E
16,S,7,280.954,1.17028,0.07846,E
16,S,8,328.794,1.15525,0.07203,E
16,S,9,379.84,1.17865,0.08200,S
16,S,10,447.7,1.12698,0.05970,S
16,S,11,504.55,1.11864,0.05600,S
16,S,12,564.41,1.15512,0.07198,S
16,S,13,651.96,1.08441,0.04050,S
16,S,14,706.994,4.55984,0.64028,T
16,S,15,3223.78057,1.08388,0.04025,T
16,S,16,3494.188518,,,T
17,Cl,0,3.612725,3.58943,0.56422,EA22
17,Cl,1,12.967633,1.83639,0.29488,E
17,Cl,2,23.81364,1.67131,0.25130,E
17,Cl,3,39.8,1.33769,0.14445,S
17,Cl,4,53.24,1.27122,0.11942,S
17,Cl,5,67.68,1.43233,0.17774,S
17,Cl,6,96.94,1.17806,0.08175,S
17,Cl,7,114.2013,3.04993,0.50616,E
17,Cl,8,348.306,1.15086,0.07014,E
17,Cl,9,400.851,1.13933,0.06513,E
17,Cl,10,456.7,1.16050,0.07429,S
17,Cl,11,530.0,1.11619,0.05490,S
17,Cl,12,591.58,1.10940,0.05186,S
17,Cl,13,656.3,1.14312,0.06678,S
17,Cl,14,750.23,1.07860,0.03781,S
17,Cl,15,809.198,4.52095,0.63774,T
17,Cl,16,3658.34366,1.07871,0.03786,T
17,Cl,17,3946.29179,,,T
18,Ar,0,,,,EA22
18,Ar,1,15.7596119,1.75319,0.27357,E
18,Ar,2,27.62967,1.47432,0.19170,E
18,Ar,3,40.735,1.46262,0.18786,S
18,Ar,4,59.58,1.25613,0.11352,S
18,Ar,5,74.84,1.21980,0.09902,S
18,Ar,6,91.29,1.36280,0.15355,E
18,Ar,7,124.41,1.15310,0.07111,S
18,Ar,8,143.4567,2.94584,0.49314,S
18,Ar,9,422.6,1.13526,0.06335,S
18,Ar,10,479.76,1.12640,0.05944,S
18,Ar,11,540.4,1.14545,0.06779,S
18,Ar,12,619.0,1.10743,0.05098,S
18,Ar,13,685.5,1.10158,0.04833,S
18,Ar,14,755.13,1.13292,0.06232,S
18,Ar,15,855.5,1.07350,0.03545,S
18,Ar,16,918.375,4.48691,0.63550,T
18,Ar,17,4120.66559,1.07415,0.03575,T
18,Ar,18,4426.22407,,,T
19,K,0,0.501459,8.65607,0.79288,EA22
19,K,1,4.34066373,7.28575,0.75862,E
19,K,2,31.625,1.44832,0.18311,E
19,K,3,45.8031,1.32998,0.14162,S
19,K,4,60.917,1.35693,0.15144,S
19,K,5,82.66,1.20300,0.09215,S
19,K,6,99.44,1.18222,0.08350,S
19,K,7,117.56,1.31737,0.13695,E
19,K,8,154.87,1.13526,0.06335,S
19,K,9,175.8174,2.86473,0.48250,S
19,K,10,503.67,1.12296,0.05792,S
19,K,11,565.6,1.11581,0.05473,S
19,K,12,631.1,1.13247,0.06212,S
19,K,13,714.7,1.10018,0.04770,S
19,K,14,786.3,1.09490,0.04530,S
19,K,15,860.92,1.12403,0.05839,S
19,K,16,967.7,1.06907,0.03338,S
19,K,17,1034.542,4.45686,0.63349,T
19,K,18,4610.80714,1.07011,0.03387,T
19,K,19,4934.04979,,,T
20,Ca,0,0.02455,249.00837,0.99200,EA22
20,Ca,1,6.11315547,1.94200,0.32019,E
20,Ca,2,11.871719,4.28861,0.62183,E
20,Ca,3,50.91316,1.32133,0.13843,E
20,Ca,4,67.2732,1.25369,0.11257,S
20,Ca,5,84.34,1.28978,0.12655,S
20,Ca,6,108.78,1.16942,0.07810,S
20,Ca,7,127.21,1.15746,0.07298,S
20,Ca,8,147.24,1.28049,0.12300,E
20,Ca,9,188.54,1.12058,0.05686,S
20,Ca,10,211.275,2.80014,0.47370,S
20,Ca,11,591.6,1.11258,0.05329,S
20,Ca,12,658.2,1.10696,0.05076,S
20,Ca,13,728.6,1.12160,0.05732,S
20,Ca,14,817.2,1.09398,0.04488,S
20,Ca,15,894.0,1.08915,0.04267,S
20,Ca,16,973.7,1.11615,0.05489,S
20,Ca,17,1086.8,1.06526,0.03160,S
20,Ca,18,1157.726,4.43011,0.63168,T
20,Ca,19,5128.8576,1.06649,0.03217,T
20,Ca,20,5469.86358,,,T
```

**Source list**

- Beasley’s framework and executable model. [VOTKP v2.9](https://doi.org/10.5281/zenodo.23340757) · [v3 paper and Standard Model ball branch](https://github.com/dicipler-pixel/votkp-lean/tree/claude/sm-ball-20261111) · [Moving-matrix ball work](https://github.com/dicipler-pixel/votkp-lean/tree/a60a000/research) · [Threshold archive](https://github.com/dicipler-pixel/votkp-lean/blob/74125d2/data/element_thresholds_20261011.json.gz)
- Atomic energies and affinities. [NIST ASD 5.12, 2024](https://doi.org/10.18434/T4W30F) · [Ning and Lu, 2022](https://doi.org/10.1063/5.0080243) · [CODATA 2022 energy equivalents](https://physics.nist.gov/cuu/pdf/factors_2022.pdf)
- Relativistic component checks. [Yerokhin and Shabaev, 2015, Table III](https://arxiv.org/abs/1506.01885) · [Yerokhin, Patkóš and Pachucki, 2022, Table VIII](https://arxiv.org/abs/2206.14161)
- Atomic dimensions and optical data. [CTCP polarizabilities, 2025](https://ctcp.massey.ac.nz/2025Tablepol.pdf) · [Cordero et al., 2008](https://doi.org/10.1039/B801115J) · [Shannon, 1976](https://doi.org/10.1107/S0567739476001551) · [NIST Handbook of Basic Atomic Spectroscopic Data](https://physics.nist.gov/PhysRefData/Handbook/)
- Isotopes and crystal structures. [IAEA LiveChart](https://www-nds.iaea.org/relnsd/vcharthtml/VChartHTML.html) · [Ohayon reference-radius evaluation, 2025 revision](https://arxiv.org/abs/2409.08193) · [FRIB discovery records](https://frib.msu.edu/public-engagement/learning-resources-and-programs/brief-history-of-rare-isotopes/list-of-new-isotope-discoveries) · [Crystallography Open Database](https://www.crystallography.net/cod/)