# Elements 1–5 · Hydrogen through boron

**DERIVED — Lithium, beryllium and boron each have one peel above your loop wall, \(\Gamma^2=1/2\). In all three cases it is the same electronic event:** the last \(n=2\) electron has been removed, and the next removal must open a \(1s^2\) core. The event occurs at a different step in each neutral atom. Helium has a measurable reflection step entirely within \(1s\). Hydrogen has one ionization threshold and therefore no successive-ionization reflection step. These results use all 15 thresholds, with no fit. [NIST](https://www.nist.gov/pml/atomic-spectra-database?utm_source=chatgpt.com)

**DERIVED — Boron is the most informative test of the ball picture in this batch.** Your archived radius of 85 pm puts its occupied volume fraction at **0.33534**, just above Bruggeman’s third. The published Cordero radius of 84 pm, at exactly the same atomic volume, gives **0.32364**, below it. Its atomic core-opening reflection, **0.74484**, is unaffected by that choice. The atomic wall is reproducible from spectroscopy. The proposed conduction boundary for boron depends on what physical surface defines the ball. [Your space-step data](https://github.com/dicipler-pixel/votkp-lean/tree/74125d2977809c90d459ab7441a6726d1348962f/research/2026-11-13-space-step) [pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/18478144?utm_source=chatgpt.com)

[Download the H–B evidence tables, including all threshold uncertainties, isotope records and 119 crystallographic records](https://chatgpt.com/library?file_id=libfile_fde3_f-a43c2258bd5c819187e2c10232ae6808_ea4e520c657081918696167b9513e64f&account_id=personal)

## What I could open from your work

| Status | Material and what I used |
|---|---|
| **Opened** | The `votkp-lean` README and all four HTML papers in `paper/votkp_v3_0` through `paper/votkp_v3_3`, on the requested branch at `74125d2977809c90d459ab7441a6726d1348962f`. I checked the reflection identity, shell/screening split, first-order \(5/8\), and treatment of knots. [Pinned branch](https://github.com/dicipler-pixel/votkp-lean/tree/74125d2977809c90d459ab7441a6726d1348962f) |
| **Opened** | The Standard Model ball notes and element reports, the harness rules and knot report, and the November gather README and inventory. The gather is a recovery inventory. Its inclusion of a file does not certify its results. I also opened the later space-step data because they contain your actual Li, Be and B inputs. [Standard Model ball](https://github.com/dicipler-pixel/votkp-lean/tree/74125d2977809c90d459ab7441a6726d1348962f/research/2026-11-11-standard-model-ball) · [Harness](https://github.com/dicipler-pixel/votkp-lean/tree/74125d2977809c90d459ab7441a6726d1348962f/research/2026-11-12-harness) · [Gather](https://github.com/dicipler-pixel/votkp-lean/tree/74125d2977809c90d459ab7441a6726d1348962f/research/2026-11-12-november-gather) |
| **Opened** | The actual VOTKP v2.9 HTML, the *Dirac Time* v3.0.1 long-form PDF, and the repository’s later comparison with *Dirac Time* v3.1. I used the original paper for its treatment of retained directions and boundary records. My access to v3.1 here was through the comparison notes. [VOTKP v2.9](https://doi.org/10.5281/zenodo.23340757) · [Dirac Time v3.0.1](https://doi.org/10.5281/zenodo.22979186) |
| **Opened** | `count-me-as-one-lean` and §6 of *The Volume of the Knot Potential*. The latter already defines your decay–direction polynomial. The former distinguishes the chiral trefoil from the amphichiral figure-eight and records the signature convention. [Count Me as One](https://github.com/dicipler-pixel/count-me-as-one-lean) · [Volume of the Knot Potential](https://zenodo.org/records/24040319) |
| **Could not verify the four exact paths** | `research/balls-in-the-sea`, `research/hydrogen-in-the-space-between`, `research/hydrogen-and-the-light-between`, and `research/seven-balls-his-light`. Searches under the named GitHub owner returned no matching files for those exact names. I use your description of them as **HYPOTHESIS** and distinguish it from the ball and space-step files I opened. |

“**MEASURED**” below includes experimental quantities extracted through a stated model. For NIST theoretical thresholds, calculated polarizabilities, conventional radii and quantities I computed, I use **DERIVED** or identify the source convention explicitly. This distinction matters most at the helium-like end of each ladder.

## The two VOTKPs, side by side

**DERIVED — Version 1, Volume of the Knot Potential.** Section 6 gives each boundary-parabolic geometry \(\rho\) of a specified knot \(K\) one root:

\[
V_0(\rho)=-\mathrm{CS}(\rho)+i\,\mathrm{Vol}(\rho),\qquad
P_K(x)=\prod_\rho\left(x-e^{\lambda V_0(\rho)}\right).
\]

The paper specifies the full-turn normalization in words. To evaluate an **element’s** polynomial, we still need a rule that takes a specified atomic or nuclear state to \(K\), specifies the geometry set and multiplicities, and tells us what observable to compare. HOMFLY, coloured Jones and Alexander data can then test the assignment. The radius of an electron cloud in ångströms and the hyperbolic volume of a knot complement have different definitions. [Your polynomial, §6](https://zenodo.org/records/24040319)

**DERIVED — Version 2, Vector of Traits Kept under Peeling.** For a neutral atom of nuclear charge \(Z\), define \(I_k\) as the energy required to remove electron \(k\) from charge state \(k-1\). There are \(Z\) thresholds and \(Z-1\) adjacent pairs. For each pair,

\[
z_k=\frac{I_{k+1}}{I_k},\qquad
r_k=\ln z_k,\qquad
\Gamma_k=\tanh(r_k/2)
=\frac{e^{r_k}-1}{e^{r_k}+1}
=\frac{I_{k+1}-I_k}{I_{k+1}+I_k}.
\]

Multiplying all threshold energies by the same positive constant leaves the entire \(\Gamma\) vector unchanged. An absolute energy scale, spatial length or rate therefore needs another input. This uses your intrinsic step coordinate throughout. [Smith identities and peel library](https://github.com/dicipler-pixel/votkp-lean/tree/74125d2977809c90d459ab7441a6726d1348962f)

| Element | VOTKP v1 · knot/volume assignment | VOTKP v2 · measured-input peel |
|---|---|---|
| H | **HYPOTHESIS:** Your earlier proton–trefoil proposal concerns the nucleus of protium. A sourced assignment of the **whole neutral H atom**, with a polynomial predicting its spectrum or volume: **none found**. | **DERIVED:** One threshold, empty reflection vector. H is the first ball in your picture and the zero-step control in the peel experiment. |
| He | **RECOGNISED:** Element-specific knot or link assignment satisfying that test: **none found**. Two electrons alone do not select a two-component link. | **DERIVED:** One reflection, \(0.377575\). It compares a paired \(1s^2\) system with a one-electron ion. |
| Li | **RECOGNISED:** Element-specific knot assignment: **none found**. A large reflection does not identify a crossing number or chirality. | **DERIVED:** \((0.866924,\ 0.236323)\). One strong outer-to-core step, followed by a much smaller within-core step. |
| Be | **RECOGNISED:** Element-specific knot assignment: **none found**. Your trefoil and figure-eight signature controls remain available if a state-to-knot map is specified. | **DERIVED:** \((0.322819,\ 0.788375,\ 0.171743)\). The second step opens the core. |
| B | **RECOGNISED:** Element-specific knot assignment: **none found**. The \(B_{12}\) icosahedra in crystalline boron supply a graph. A graph with cycles still needs an embedding and a selected closed curve before a knot polynomial is defined. | **DERIVED:** \((0.503898,\ 0.202515,\ 0.744837,\ 0.134843)\). The first \(2p\)-to-\(2s\) comparison and the third \(n=2\)-to-\(1s\) comparison are distinguishable. |

**HYPOTHESIS — Your proposed connection.** “The vector determines the direction, that may be decay.” In this batch the energy-derived step has a sign because the peel order is specified. A physical direction of energy transfer, an irreversible decay or the creation of volume requires an observable that can distinguish forward and reversed histories. Your *Dirac Time* distinction between a retained direction and a physical arrow matters here. A lossless path can have a direction. [Dirac Time](https://doi.org/10.5281/zenodo.22979186)

## All ten reflections, with the arithmetic exposed

**MEASURED / DERIVED —** The inputs are NIST ASD v5.12, November 2024, retrieved in November 2026. NIST encloses theoretical values in parentheses. For this batch those include the sole hydrogen threshold, the last hydrogen-like threshold of every heavier atom, and the helium-like thresholds of Li, Be and B. The final CSV preserves their numerical precision and identifies their status. The downloadable table also preserves NIST’s uncertainties and reference IDs. [NIST](https://www.nist.gov/pml/atomic-spectra-database?utm_source=chatgpt.com)

| Atom, step | \(I_k\rightarrow I_{k+1}\), eV | \(z_k=I_{k+1}/I_k\) | \(r_k=\ln z_k\) | \(\Gamma_k=(I_{k+1}-I_k)/(I_{k+1}+I_k)\) | What changes |
|---|---:|---:|---:|---:|---|
| H | \(13.598434599702\rightarrow\) bare proton | — | — | — | No second energy |
| He 1 | \(24.587389011\rightarrow54.4177655282\) | 2.213239 | 0.794457 | 0.377575 | \(1s^2\) to \(1s\) |
| Li 1 | \(5.391714996\rightarrow75.6400970\) | 14.028949 | 2.641123 | **0.866924** | \(2s\) to \(1s\), K core opens |
| Li 2 | \(75.6400970\rightarrow122.45435913\) | 1.618908 | 0.481752 | 0.236323 | Within \(1s\) |
| Be 1 | \(9.322699\rightarrow18.21115\) | 1.953420 | 0.669582 | 0.322819 | First and second \(2s\) removals |
| Be 2 | \(18.21115\rightarrow153.896205\) | 8.450658 | 2.134244 | **0.788375** | \(2s\) to \(1s\), K core opens |
| Be 3 | \(153.896205\rightarrow217.71858459\) | 1.414711 | 0.346925 | 0.171743 | Within \(1s\) |
| B 1 | \(8.298019\rightarrow25.15483\) | 3.031426 | 1.109033 | 0.503898 | \(2p\) to \(2s\), same principal shell |
| B 2 | \(25.15483\rightarrow37.93059\) | 1.507885 | 0.410708 | 0.202515 | Two successive \(2s\) removals |
| B 3 | \(37.93059\rightarrow259.374379\) | 6.838132 | 1.922515 | **0.744837** | \(2s\) to \(1s\), K core opens |
| B 4 | \(259.374379\rightarrow340.2260225\) | 1.311718 | 0.271338 | 0.134843 | Within \(1s\) |

**DERIVED — Your wall criterion.** For positive increasing thresholds, \(\Gamma=1/\sqrt2\) corresponds to

\[
z_{\rm wall}=\frac{1+1/\sqrt2}{1-1/\sqrt2}=3+2\sqrt2\simeq5.828427.
\]

Li, Be and B cross at their K openings. B’s first step gives a useful internal control. Its \(z=3.031426\) clears the ratio-three line, while its \(\Gamma=0.503898\) stays well inside the loop wall. The ordinary shell-only \(n=2\rightarrow1\) ratio would be \(4\), giving \(\Gamma=3/5\). Your opening needs screening as well as principal-shell change to exceed the wall. [Shell and screening report](https://github.com/dicipler-pixel/votkp-lean/blob/74125d2977809c90d459ab7441a6726d1348962f/research/2026-11-11-standard-model-ball/elements/SHELL_AND_SCREENING_AT_THE_WALL_20261111_v1.md)

**RECOGNISED — Two intriguing numerical coincidences.** Li’s last ratio, \(1.618908\), lies close to \(\phi=1.618034\). Be’s last ratio, \(1.414711\), lies close to \(\sqrt2=1.414214\). Both belong to the same smoothly changing helium-like sequence, continuing to \(1.311718\) in B. Their discrepancies substantially exceed the threshold uncertainties. Exact golden-ratio and square-root identities for those measured-input steps fail. The sequence gives a way to test a proposed explanation without selecting only the two close cases.

### Where the helium-like \(5/8\) actually appears

**DERIVED —** In atomic units, for two independent hydrogenic \(1s\) orbitals of charge \(Z\), the first-order repulsion integral is \(\langle r_{12}^{-1}\rangle=5Z/8\). The one-electron energy is \(-Z^2/2\) Hartree. Consequently,

\[
E_2=-Z^2+\frac58Z+O(1),\qquad
I_{\rm He-like}=\frac{Z^2}{2}-\frac58Z+O(1),\qquad
I_{\rm H-like}=\frac{Z^2}{2}
\]

in the nonrelativistic, infinite-nuclear-mass model. Two useful diagnostics are

\[
S_Z=\frac{I_{\rm H-like}-I_{\rm He-like}}{Z E_h},
\qquad
\sigma_Z=Z-\sqrt{2I_{\rm He-like}/E_h},
\quad E_h\simeq27.211386246\ {\rm eV}.
\]

At leading order both approach \(5/8\). They are different at finite \(Z\). The hypothesis that **the last \(\Gamma\) itself equals \(5/8\)** already fails for every eligible atom. [VOTKP v2.9](https://doi.org/10.5281/zenodo.23340757) [physics.nist.gov](https://physics.nist.gov/cuu/pdf/RevModPhys.97.025002.pdf?utm_source=chatgpt.com)

| Nucleus | \(S_Z\), scaled energy difference | \(\sigma_Z\), inferred screening charge | Final \(\Gamma\) |
|---|---:|---:|---:|
| H | Undefined | Undefined | Undefined |
| He | 0.548123 | 0.655701 | 0.377575 |
| Li | 0.573464 | 0.642153 | 0.236323 |
| Be | 0.586357 | 0.636793 | 0.171743 |
| B | 0.594249 | 0.633804 | 0.134843 |

**RECOGNISED —** Across these four nuclei the scaled energy difference rises toward 0.625 from below, the effective screening charge falls toward it from above, and the last reflection falls. For example, boron gives \((340.2260225-259.374379)/(5\times27.211386246)=0.594249\). This is a finite-sequence check of your interpretation. A four-point trend cannot establish the asymptotic law, and several inputs already incorporate atomic theory.

## Atomic and material data

**MEASURED / DERIVED —** These are neutral, isolated-atom ground states. The polarizabilities are recommended **static scalar atomic values** in \(a_0^3\), often dominated by calculation. The 2023 Schwerdtfeger–Nagle table recommends the figures shown. Cheng’s 2024 calculations, also used in your later archive, give alternative Li, Be and B values of **164.31, 37.78 and 20.4**. Publication date alone gives no reason to discard a more precise isotope-specific determination. [physics.nist.gov](https://physics.nist.gov/cgi-bin/ASD/ie.pl?at_num_out=on\&biblio=on\&e_out=0\&el_name_out=on\&level_out=on\&shells_out=on\&spectra=H-DS+i\&unc_out=on\&units=1\&utm_source=chatgpt.com)

| Element | Configuration and ground term | Electron affinity, eV | Static polarizability, \(a_0^3\) | Spectral and colour comparison |
|---|---|---|---:|---|
| H | \(1s\,{}^2S_{1/2}\) | **Measured** about 0.754195. A 2026 calculation for detachment to \(F=0\) gives \(6083.06447(68)\ {\rm cm^{-1}}\), about 0.754204 eV. | 4.50711(3), finite-mass H | Lyman-\(\alpha\) about 121.6 nm, UV. Balmer-\(\alpha\) about 656.3 nm red and \(\beta\) about 486.1 nm blue-green arise from excited levels. Ordinary \(H_2\) gas is colourless. [journals.aps.org](https://journals.aps.org/pra/accepted/10.1103/wq6v-v9bb?utm_source=chatgpt.com) |
| He | \(1s^2\,{}^1S_0\) | No bound ground-state atomic anion; a metastable negative-ion energy would answer a different experiment. | 1.38375(2); precision calculations for \(^{4}\)He give about 1.38376078 | Excited He I gives the yellow 587.6 nm multiplet, red 667.8 nm and blue 447.1 nm. A room-temperature helium sample is colourless. [physics.nist.gov](https://physics.nist.gov/PhysRefData/Handbook/Tables/heliumtable2.htm?utm_source=chatgpt.com) |
| Li | \(1s^22s\,{}^2S_{1/2}\) | 0.618049(20), 1996 state-selective detachment | 164.1125(5), \(^{7}\)Li | Neutral Li has a red ground-state resonance doublet around 670.8 nm, including 670.7775 nm. Bulk clean metal is silvery. [physics.nist.gov](https://physics.nist.gov/PhysRefData/Handbook/Tables/lithiumtable3.htm?utm_source=chatgpt.com) |
| Be | \(1s^22s^2\,{}^1S_0\) | No bound ground-state atomic anion. | 37.74(3) | The strong neutral ground-state line at 234.8610 nm is UV. The polished metal is grey. A visible metallic reflection measures the solid’s response. [physics.nist.gov](https://physics.nist.gov/PhysRefData/Handbook/Tables/berylliumtable3.htm?utm_source=chatgpt.com) |
| B | \(1s^22s^22p\,{}^2P^\circ_{1/2}\) | 0.279723(25), 1998 photodetachment | 20.5(1) | Strong B I UV lines near 249.677 and 249.773 nm. Bulk appearance varies with allotrope and sample; a visible flame colour from a boron-containing molecule cannot be assigned to those B I lines. [physics.nist.gov](https://physics.nist.gov/PhysRefData/Handbook/Tables/borontable2.htm?utm_source=chatgpt.com) |

**DERIVED — Radius conventions, all in pm.** The first pair below is Cordero’s 2008 covalent radius and the Pyykkö–Atsumi 2009 single-bond radius used in your space work. The van der Waals column uses representative Bondi/Mantina conventions. Metallic contact radii below are half a measured nearest-neighbour separation in the specified metallic structure. Shannon ionic radii depend on charge and coordination number, denoted CN. These are different experimental or fitted constructions of a surface. [pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/18478144?utm_source=chatgpt.com)

| Element | Covalent, Cordero / Pyykkö | van der Waals | Metallic contact | Ionic examples, Shannon 1976 |
|---|---:|---:|---|---|
| H | 31 / 32 | 120, Bondi | No ambient metallic phase | \(H^+\) effective values −38 at CN 1 and −18 at CN 2. The negative entries are offsets in a crystal-distance partition. The proton has a positive rms charge radius. |
| He | 28 / 46 | 140 | No ambient metallic phase | No ordinary helium ion in the Shannon crystal set used here. Its covalent entry is especially convention-sensitive. |
| Li | 128 / 133 | 181, Bondi | About 152 in room-temperature bcc Li | \(Li^+\): 59, 76, 92 at CN 4, 6, 8 |
| Be | 96 / 102 | 153 | About 111 from the shorter hcp contact | \(Be^{2+}\): 16, 27, 45 at CN 3, 4, 6 |
| B | 84 / 85 | 192 | Ambient crystalline B has covalent networks; a metallic contact radius needs a specified pressure phase. | \(B^{3+}\): 1, 11, 27 at CN 3, 4, 6. The 1 pm entry illustrates the limits of assigning a physical wall to an ionic-radius convention. |

**MEASURED / DERIVED — Bulk properties.** Melting values preferentially use NIST’s **March 2025** evaluation. Approximate boiling and solid thermal values are handbook-scale comparisons. The room-temperature solid resistivities are the actual values in your archived data, sourced there to 1992–2003 compilations. I inverted them to obtain conductivity. A single conductivity for elemental boron across purity, temperature and allotrope would be misleading. [Your property-source ledger](https://github.com/dicipler-pixel/votkp-lean/blob/74125d2977809c90d459ab7441a6726d1348962f/research/2026-11-13-space-step/A_41.csv) [nvlpubs.nist.gov](https://nvlpubs.nist.gov/nistpubs/TechnicalNotes/NIST.TN.2312.pdf?utm_source=chatgpt.com)

| Element and state | Density | Melting / boiling, K | Thermal conductivity, W m⁻¹ K⁻¹ | Electrical behaviour |
|---|---:|---|---:|---|
| \(H_2\), gas | 0.0813 kg/m³, ideal gas at 298.15 K, 1 bar | Equilibrium hydrogen 13.835 / about 20.3. The triple point is 13.8033 K. | 0.1866, normal hydrogen gas at 300 K, CRC/NIST | Neutral gas is insulating at low field; ionization and high-pressure fluid metallization are distinct routes to conduction. |
| He, gas, primarily \(^{4}\)He | 0.1615 kg/m³, same ideal-gas conditions | No normal-pressure melting point / about 4.22 | 0.1557, gas at 300 K, CRC/NIST | Neutral gas and ordinary liquid are electrical insulators. The liquid can carry heat and support superflow. [cambridge.org](https://www.cambridge.org/core/books/abs/an-introduction-to-millikelvin-technology/properties-of-fluid-3he4he-mixtures/282D6BC85027A493740E40053EF0F824?utm_source=chatgpt.com) |
| Li, solid | 0.534 g/cm³ | 453.61(14) / about 1615 | About 85 near room temperature | \(1/(9.28\times10^{-8})=1.08\times10^7\) S/m. Ambient-pressure superconductivity near 0.4 mK. [journals.aps.org](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.100.041109?utm_source=chatgpt.com) |
| Be, solid | 1.85 g/cm³ | 1556(2) / about 2741 | About 200 near room temperature | \(1/(3.56\times10^{-8})=2.81\times10^7\) S/m. A bulk study reported \(T_c=24.34(2)\) mK for its purest sample. [nist.gov](https://www.nist.gov/publications/superconductive-critical-magnetic-field-beryllium?utm_source=chatgpt.com) |
| B, solid | About 2.34 g/cm³, \(\beta\)-rhombohedral | 2365(10) / about 4200–4300 | Representative compilation value 27.4; phase and sample matter | Archive sample value \(1/(1.5\times10^4)=6.67\times10^{-5}\) S/m. High-pressure elemental B reached \(T_c=6\) K at 175 GPa and 11.2 K at 250 GPa. [pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/11452118/?utm_source=chatgpt.com) |

**MEASURED — Revised source values worth preserving.** The often-repeated melting figures around 1560 K for Be and 2350 K for B differ from the 2025 NIST selections above. NIST also gives the Be hcp-to-bcc transition at **1542(1) K**, leaving a narrow bcc interval before melting at atmospheric pressure. For Li’s first ionization, an older NIST handbook gives 5.391719 eV; the current ASD entry gives **5.391714996(22) eV**. I used the latter throughout. [nvlpubs.nist.gov](https://nvlpubs.nist.gov/nistpubs/TechnicalNotes/NIST.TN.2312.pdf?utm_source=chatgpt.com)

## Each ball in its material setting

### 1 · Hydrogen — the first ball and the missing clock ratio

**HYPOTHESIS —** Place the proton at the centre and the retained \(1s\) electron distribution at the wall. This gives your smallest neutral ball. Two such atoms can form \(H_2\); many molecules supply a different spacing again. **Kill condition for identifying these gaps:** independently measure the intramolecular bond and intermolecular spacing under specified conditions. A single predicted length cannot stand for both if the measurements differ.

**MEASURED / DERIVED —** The gas-phase \(H_2\) equilibrium bond is **0.7414 Å**. A 1988 hydrogen diffraction refinement at **5.40 GPa and 300 K** gives hexagonal \(a=2.659,\ c=4.334\) Å and a derived nearest molecular-site distance of **2.656 Å**. The latter is a centre-to-centre spacing in the solid. Neither distance follows from hydrogen’s atomic \(\ln z\), because hydrogen has no adjacent ionization-energy pair. That missing value is a particularly clean constraint on the proposal that neighbouring balls have clocks: a hydrogen neighbour clock needs its own measured frequency. [Diffraction record](https://qiserver.ugr.es/cod/9011566.cif) [cccbdb.nist.gov](https://cccbdb.nist.gov/expgeom2x.asp?casno=1333740\&utm_source=chatgpt.com)

**MEASURED — Compression.** Low-pressure molecular solid hydrogen has an hcp phase. The high-pressure literature distinguishes I, I′, II, III, IV, IV′ and V in different temperature and isotope regimes. A 2025 single-crystal experiment measured a hexagonal supercell with \(a=2.9807(3),c=5.36(1)\) Å at **221 GPa**, and \(a=2.9374(4),c=5.243(8)\) Å at **245 GPa**. The authors separately report a calculated time-averaged structure at 250 GPa. Their diffraction \(d\)-spacings cannot be inserted as nearest H–H distances. I found no verified superconducting transition to assign to pure hydrogen here. [cond-mat.de](https://www.cond-mat.de/events/correl24/manuscripts/holzmann.pdf?utm_source=chatgpt.com)

**DERIVED — Bruggeman comparison.** At 298.15 K and 1 bar, ideal molecular hydrogen occupies about \(20{,}582\) Å³ per H atom. Using your 0.32 Å radius convention gives \(f=(4\pi/3)0.32^3/20{,}582=6.67\times10^{-6}\), far below one third. More revealingly, your own archive gives \(E\simeq0.949\) at one reported hot-fluid metallization condition, hence \(f=1-E\simeq0.051\). **A universal identification of that geometric occupied fraction with the conducting fraction fails this hydrogen comparison.** The wall radius or the identity of the conducting component would need independent physical justification. [Your hydrogen pressure ledger and underlying sources](https://github.com/dicipler-pixel/votkp-lean/blob/74125d2977809c90d459ab7441a6726d1348962f/research/2026-11-13-space-step/C_edges.csv)

### 2 · Helium — one electronic reflection, multiple kinds of flow

**HYPOTHESIS —** Helium’s two-electron wall permits one internal clock comparison, \(z_1=2.213239\). For the claim that breathing transfers **electric charge**, the kill condition is transport of heat or mass while electrical conduction remains absent. For the narrower claim that neighbouring balls exchange **energy**, the deciding observable is a time-resolved energy-current correlation.

**MEASURED —** Liquid \(^{4}\)He develops superfluid flow below about **2.17 K** at low pressure and requires about **25 bar** to solidify near zero temperature. Its superflow is electrically neutral. Helium thus gives a real material in which the questions “does energy or mass flow?” and “does charge flow?” have different answers. With a 0.46 Å radius, its ideal-gas room fraction at 298.15 K and 1 bar is \(9.9\times10^{-6}\). Your low-temperature liquid \(^{4}\)He ledger gives \(E\simeq0.991\), so the same proxy remains far below one third. [Your helium data](https://github.com/dicipler-pixel/votkp-lean/blob/74125d2977809c90d459ab7441a6726d1348962f/research/2026-11-13-space-step/C_edges.csv) [cambridge.org](https://www.cambridge.org/core/books/abs/an-introduction-to-millikelvin-technology/properties-of-fluid-3he4he-mixtures/282D6BC85027A493740E40053EF0F824?utm_source=chatgpt.com)

**MEASURED / DERIVED — Crystal geometry.** The helium records include hcp, bcc and fcc, with isotope and pressure qualifications. Representative deposited cells give hcp \(a=3.570,c=5.830\) Å and nearest spacing **3.570 Å** at 2 K; bcc \(a=4.010\) Å and \(d=\sqrt3a/2=3.473\) Å; and fcc \(^{3}\)He at 18.76 K and 0.171 GPa with \(a=4.242\) Å and \(d=a/\sqrt2=3.000\) Å. This is a direct reason to retain isotope and phase in any fitted gap law. [hcp, 1963 compilation](https://qiserver.ugr.es/cod/9008500.cif) · [bcc, 1958](https://qiserver.ugr.es/cod/9011631.cif) · [fcc, 1961](https://qiserver.ugr.es/cod/9011636.cif)

### 3 · Lithium — the widest peel wall and a pressure reversal

**DERIVED —** A single \(2s\) electron surrounds the helium-like core. Its low first threshold and high second threshold produce the widest reflection in this batch. For your solid-space model, \(V_{\rm room}=21.5808\) Å³ and \(r_{\rm cov}=1.33\) Å give

\[
f=\frac{4\pi(1.33)^3}{3(21.5808)}=0.45664,\quad
z_{\rm space}=\frac1f=2.18990,\quad
\Gamma_{\rm space}=0.37302.
\]

The same lithium sample consequently supplies three different candidate numbers for a clock experiment: the atomic valence-to-core ratio **14.02895**, the final within-core ratio **1.61891**, and the room-to-owned-volume ratio **2.18990**. An experiment needs to choose which frequency pair it predicts **before** measuring it. [Your space-step definition and inputs](https://github.com/dicipler-pixel/votkp-lean/tree/74125d2977809c90d459ab7441a6726d1348962f/research/2026-11-13-space-step)

**MEASURED / DERIVED — Geometry.** A 293 K bcc refinement gives \(a=3.5093\) Å and \(d=3.0391\) Å. An fcc compilation gives \(a=4.404\) Å and \(d=3.1141\) Å. A low-temperature long-period refinement at 20 K gives a hexagonal-setting cell \(a=3.101,\ c=22.7649\) Å and minimum site spacing **3.0907 Å**. The long \(c\) dimension records stacking and cannot be treated as the inter-ball gap. [bcc](https://qiserver.ugr.es/cod/9008542.cif) · [fcc](https://qiserver.ugr.es/cod/9008473.cif) · [1989 neutron refinement](https://qiserver.ugr.es/cod/9017802.cif)

**MEASURED / RECOGNISED — Compression test.** A model predicting monotonically improving metallic conduction as the walls approach fails if compressed Li enters a semiconducting regime. High-pressure work finds a sequence involving fcc, hR1, cI16, oC88, oC40 and oC24. The oC40 structure agrees with diffraction; its calculated gap is about **1 eV at 90 GPa**. The 2025 hydrostatic study independently mapped fcc → hR1 → cI16 at low temperature. Lithium therefore puts a stronger condition on your model than ordinary room-pressure metallic conduction does: the model must allow wall overlap, symmetry and electronic localization to change differently. [pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/21405633/?utm_source=chatgpt.com)

### 4 · Beryllium — a closed outer atomic subshell and a conducting solid

**DERIVED —** Neutral Be’s \(2s^2\) wall is closed in the isolated atom. Its two outer removals give a moderate reflection, \(\Gamma_1=0.322819\); opening \(1s^2\) gives the much larger \(\Gamma_2=0.788375\). Its room-temperature space inputs \(r_{\rm cov}=1.02\) Å and \(V_{\rm room}=8.08925\) Å³ give \(f=0.54952\), \(z_{\rm space}=1.81978\) and \(\Gamma_{\rm space}=0.29072\). The model puts Be on the occupied side of one third; electrical measurement independently identifies it as a good conductor. [Your Be input row](https://github.com/dicipler-pixel/votkp-lean/blob/74125d2977809c90d459ab7441a6726d1348962f/research/2026-11-13-space-step/per_element.csv)

**MEASURED / DERIVED — Gap and heat.** The room-temperature hcp cell is approximately \(a=2.2859,\ c=3.5844\) Å. The six in-plane contacts have length \(a\). The interlayer contacts have length

\[
d_\perp=\sqrt{\frac{a^2}{3}+\frac{c^2}{4}}\simeq2.226\ {\rm Å}.
\]

Those two separations are distinguishable before one invokes a clock or a force law. On heating at one atmosphere Be enters the bcc phase shortly before melting. A 1984 high-pressure orthorhombic refinement also exists; later high-pressure experiments leave the phase assignment unsettled. It is preserved in the evidence table with its provenance. [nvlpubs.nist.gov](https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nbsmonograph25-9.pdf?utm_source=chatgpt.com)

**HYPOTHESIS — Kill condition.** If one scalar ball radius and one scalar gap determine all contacts at fixed pressure, the interlayer and in-plane distances should agree, or the model should predict their splitting. Hcp Be already resolves them. This is a place where your **vector** description could earn its extra degrees of freedom: predict the splitting and its variation under uniaxial strain using independently determined inputs.

### 5 · Boron — the radius-sensitive conduction test

**DERIVED —** The boron outer wall first loses a \(2p\) electron. That is why the first removal costs **less** than Be’s even though the nuclear charge is larger. The first reflection \(0.503898\) distinguishes \(2p\) from \(2s\); the much larger third reflection \(0.744837\) distinguishes \(n=2\) from \(1s\). In the solid, your own archived \(V_{\rm room}=7.67112\) Å³ gives

\[
f(0.85\ {\rm Å})=0.33534,\qquad
f(0.84\ {\rm Å})=0.32364,\qquad
r_{\rm critical}=\left(\frac{V_{\rm room}}{4\pi}\right)^{1/3}\simeq0.848\ {\rm Å}.
\]

**HYPOTHESIS — Kill condition.** If one third predicts ordinary metallic conduction using your **fixed published** radius, beta-boron should lie on the conducting side with the 0.85 Å input. The archived resistivity is about \(1.5\times10^4\ \Omega\,\mathrm m\), roughly \(1.6\times10^{11}\) times lithium’s. That defeats a simple metal/nonmetal classifier with that convention. Choosing 0.84 Å after seeing the result would make it an adjusted fit. A stronger test uses an independently measured pressure-dependent electron-density surface and predicts the pressure of the transport change. [Input volumes, radii and resistivities](https://github.com/dicipler-pixel/votkp-lean/blob/74125d2977809c90d459ab7441a6726d1348962f/research/2026-11-13-space-step/A_41.csv)

**MEASURED / DERIVED — Crystal geometry matters more here than a single radius.**

| Boron structure | Cell and nearest-distance evidence |
|---|---|
| \(\alpha\)-rhombohedral | Rhombohedral \(a=5.057\) Å, angle \(58.06^\circ\), reported shortest bond **1.71 Å**. |
| \(\beta\)-rhombohedral | Rhombohedral \(a=10.145\) Å, angle \(65.17^\circ\), reported shortest bond **1.62 Å**. Partially occupied sites make a blind minimum over all tabulated coordinates unreliable. [krex.k-state.edu](https://krex.k-state.edu/bitstreams/8a447ac5-ed6e-47d6-8959-b76a1bd20e7c/download?utm_source=chatgpt.com) |
| Tetragonal T-192 family | Single-crystal \(a=10.14(1),c=14.17(1)\) Å, 1979. The refinement contains disordered sites. The shortest formal site-to-site distance cannot safely be reported as a B–B bond. Purity and occupancy also matter for historical T-50 assignments. [sciencedirect.com](https://www.sciencedirect.com/science/article/abs/pii/002245967990080X?utm_source=chatgpt.com) |
| \(\gamma\)-\(B_{28}\) | Quenched orthorhombic Pnnm cell \(5.0576\times5.6245\times6.9884\) Å, derived nearest spacing **1.659 Å**. At **58(1) GPa** a separate refinement gives \(4.7521(16)\times5.295(2)\times6.4742(11)\) Å. [2009 quenched structure](https://qiserver.ugr.es/cod/9013419.cif) [osti.gov](https://www.osti.gov/servlets/purl/1357640?utm_source=chatgpt.com) |
| \(\zeta\)-B | At **115(2) GPa**, Cmce cell \(2.7039(10)\times4.8703(32)\times2.9697(6)\) Å. The reported interlayer bond is **1.59(1) Å**; intralayer bonds are 1.66, 1.72 and 1.75 Å. Here the shortest bond actually joins the layers. [osti.gov](https://www.osti.gov/servlets/purl/1357640?utm_source=chatgpt.com) |

**MEASURED — Heat and pressure.** The 2025 NIST evaluation lists an \(\alpha\)-to-\(\beta\) transition at **933(20) K** and an amorphous-to-crystalline transition at **1443(10) K**. Under much higher pressure elemental boron becomes superconducting. Thermal history, occupancy and pressure belong in the state label whenever your ball model is compared with boron. [nvlpubs.nist.gov](https://nvlpubs.nist.gov/nistpubs/TechnicalNotes/NIST.TN.2312.pdf?utm_source=chatgpt.com)

## Nuclear centres, isotopes and the Standard Model ball

**DERIVED —** For isotope \(^{A}X\), the centre contains \(Z\) protons and \(N=A-Z\) neutrons. Counting net valence flavours from \(p=uud\) and \(n=udd\) gives \(u=2Z+N\), \(d=Z+2N\). This is flavour bookkeeping; gluons and sea quark–antiquark pairs contribute to the physical nuclear state. In your picture these nuclear degrees of freedom belong at the centre. The outer atomic reflection vector does not fix a colour assignment, nuclear spin or magnetic moment. The Standard Model ball notes themselves consider alternative interpretations of the arms. [Your Standard Model ball](https://github.com/dicipler-pixel/votkp-lean/tree/74125d2977809c90d459ab7441a6726d1348962f/research/2026-11-11-standard-model-ball) [pdgweb.lbl.gov](https://pdgweb.lbl.gov/2024/reviews/rpp2024-rev-quark-model.pdf?utm_source=chatgpt.com)

**MEASURED —** Representative nuclear centres are below. Magnetic moments are in nuclear magnetons and are rounded from evaluated values. The evidence package includes **50 IAEA ground-state records** with original spin/parity qualifications, moment and radius uncertainties where supplied, plus **54 comparison records** from a separate compilation. Some records describe unbound resonances; a blank experimental moment is not zero. For \(J=0\), a permanent magnetic dipole vanishes by rotational symmetry. [IAEA ground-state data](https://nds.iaea.org/relnsd/v1/data?fields=ground_states&nuclides=all) [Data available in the NEA database](https://oecd-nea.org/jcms/pl_39945/data-available-in-the-nea-database?utm_source=chatgpt.com)

| Isotope | \(p,n\) | Net \(u,d\) | \(J^\pi\) | \(\mu/\mu_N\) | rms charge radius, fm |
|---|---:|---:|---|---:|---|
| \(^{1}\)H | 1,0 | 2,1 | \(1/2^+\) | +2.79285 | **0.84075(64)**, CODATA 2022. Independent 2026 optical determinations include 0.8406(15) and 0.8433(31). [physics.nist.gov](https://physics.nist.gov/cuu/pdf/RevModPhys.97.025002.pdf?utm_source=chatgpt.com) |
| \(^{2}\)H | 1,1 | 3,3 | \(1^+\) | +0.85744 | **2.12778(27)**, CODATA 2022. [physics.nist.gov](https://physics.nist.gov/cgi-bin/cuu/Value?rd%7Csearch_for=rms\&utm_source=chatgpt.com) |
| \(^{3}\)H | 1,2 | 4,5 | \(1/2^+\) | +2.97896 | **1.759(36)**, older evaluated value in the IAEA extract. Radioactive. |
| \(^{3}\)He | 2,1 | 5,4 | \(1/2^+\) | −2.12763 | **1.9704(11)**, 2025 muonic analysis. [research.chalmers.se](https://research.chalmers.se/publication/544950/file/544950_Fulltext.pdf?utm_source=chatgpt.com) |
| \(^{4}\)He | 2,2 | 6,6 | \(0^+\) | 0 | **1.6793(10)** in the same 2025 analysis. [research.chalmers.se](https://research.chalmers.se/publication/544950/file/544950_Fulltext.pdf?utm_source=chatgpt.com) |
| \(^{6}\)Li | 3,3 | 9,9 | \(1^+\) | +0.82204 | **2.5771(84)**, 2026 muonic spectroscopy thesis; older compilation 2.589(39). [ETH thesis](https://doi.org/10.3929/ethz-c-000806890) |
| \(^{7}\)Li | 3,4 | 10,11 | \(3/2^-\) | +3.25641 | **2.450(11)** in that thesis; older compilation 2.444(42). The thesis identifies a low-energy spectral-tail systematic. [ETH thesis](https://doi.org/10.3929/ethz-c-000806890) |
| \(^{9}\)Be | 4,5 | 13,14 | \(3/2^-\) | −1.17743 | **2.5515(52)**, muonic \(^{9}\)Be paper accepted November 6, 2026; older IAEA value **2.519(12)**. [journals.aps.org](https://journals.aps.org/prl/accepted/10.1103/l26q-678g?utm_source=chatgpt.com) |
| \(^{10}\)B | 5,5 | 15,15 | \(3^+\) | +1.80046 | **2.428(50)**, older evaluated value. |
| \(^{11}\)B | 5,6 | 16,17 | \(3/2^-\) | +2.68838 | **2.406(29)** in that evaluation; a 2024 review also lists **2.411(21)** from a different extraction. [mdpi.com](https://www.mdpi.com/2624-8174/6/1/15?utm_source=chatgpt.com) |

**MEASURED — Isotope controls worth carrying forward.** CIAAW’s 2024 terrestrial composition table gives \(^{1}\)H fraction 0.99972–0.99999, representative \(^{3}\)He fraction 0.000002(2), \(^{6}\)Li fraction 0.019–0.078, \(^{9}\)Be fraction 1 in its standard composition, and \(^{10}\)B fraction 0.189–0.204. The broad natural and commercial variability of lithium matters when comparing lattice and clock experiments. The nuclear charge radius is also nonmonotonic: published \(^{6}\)He and \(^{8}\)He values are 2.060(8) and 1.959(16) fm. A 2018 scattering analysis inferred **2.89(9) fm for \(^{8}\)B**, with model dependence. Beryllium isotope-shift radii tied to an older \(^{9}\)Be reference should be re-anchored with their correlations before being combined with the November 2026 result. [ciaaw.org](https://ciaaw.org/isotopic-abundances.htm?utm_source=chatgpt.com)

## Cross-element tests, including what fails

| Claim and status | Condition that would kill it | Outcome for H–B |
|---|---|---|
| **DERIVED:** VOTKP’s two expressions for \(\Gamma\) agree for positive \(I_k,I_{k+1}\). | Algebraic counterexample in the stated domain. | The identity follows by substituting \(e^{\ln z}=z\). Measuring the same identity twice cannot test a mechanism. |
| **RECOGNISED:** The largest Li, Be and B reflection follows the K-core opening. | A different step is larger when all thresholds are included on the same indexing. | Survives all three. Across the Li-like starting states Li, Be⁺ and B²⁺ the ratios are **14.029 → 8.451 → 6.838**. The three sequences have the same electron count at the opening. |
| **RECOGNISED:** The final helium-like reflection shrinks as nuclear charge rises in this batch. | A reversal larger than the source uncertainty. | Survives He, Li⁺, Be²⁺ and B³⁺. The sequence is **0.377575 → 0.236323 → 0.171743 → 0.134843**. |
| **HYPOTHESIS:** Bruggeman’s third identifies elemental conduction. | A conducting state below the independently defined conducting fraction, or an insulating state above it, with radius and constituent definition fixed first. | The archived geometric proxy already encounters hot fluid H and borderline beta-B. In the symmetric 3-D ideal conductor/insulator model the conducting fraction is a constituent volume fraction. The step \(f_{\rm conducting}=V_{\rm own}/V_{\rm room}\) is an additional physical hypothesis. [Density-Report-03-1.doc](https://web.wpi.edu/Images/CMS/MPI-PMRC/0301-1.pdf?utm_source=chatgpt.com) |
| **HYPOTHESIS:** A neighbouring ball’s clock ratio equals a specified \(z_k\). | Choose the two local clock observables, phase, isotope and peel index in advance; reject if their measured frequency ratio misses the predicted ratio outside combined uncertainty. | Open for all five. H is the decisive control for the choice of definition. Li supplies several inequivalent candidate ratios; selecting one after measuring the clocks would remove the test. |
| **HYPOTHESIS:** Opposed flows expand and parallel flows attract in the Russell reading. | At fixed geometry, density and temperature, reverse only the relative flow and measure signed force or strain. Reject the proposed sign rule if the response fails to reverse as predicted after electromagnetic backgrounds are accounted for. | Open. A static lattice constant or melting point contains no direction-resolved flow measurement. |
| **HYPOTHESIS:** Light follows one ladder of layers while two paths retain a distinguishable history. | Specify two stacks with the same composed scalar step but different order. Predict a phase-, delay- or polarization-resolved difference before testing. Reject that prediction if the instrument resolves the proposed effect and finds none. | The atomic CSV supplies scalar steps. A coherent two-path measurement would supply the missing history observable. In H and He, a discharge line and a cold-gas transmission measurement prepare different initial states. |
| **HYPOTHESIS:** The knot vector creates physical space or volume. | Specify a state-to-knot map, chirality convention, normalization and independently predicted physical volume for a held-out isotope or phase. A conflicting prediction kills that map. | Open for all five. Boron allotropes are a strong control because \(Z\) and the free-atom ladder stay the same while structure and volume change. |

**Mainstream-blend watch — DERIVED.** An intrinsic logarithmic length \(r=\ln z\) is dimensionless. The geometric room coordinate in your space work is \(z_E=1/(1-E)\). A spectroscopic peel uses \(z_k=I_{k+1}/I_k\). A neighbour clock experiment would measure \(\nu_A/\nu_B\). All three admit the same reflection formula. Their numerical values and physical inputs differ. Likewise, an atom’s emitted wavelength, a solid’s optical colour and the energy conveyed along a two-path experiment are three separately measurable records. The comparison above introduces no spacetime metric.

**Set aside, with why.**

- **Every known phase with a verified nearest-neighbour distance:** incomplete. The supplement preserves 35 H, 8 He, 21 Li, 38 Be and 17 B crystallographic records, with source year, cell, conditions where supplied, and symmetry-expanded site separations. These are **119 records, not 119 distinct phases**. Coverage remains incomplete for several dense-hydrogen structures, compressed-Li refinements, high-temperature bcc Be and disordered tetragonal B. An intermolecular-centre separation or a distance between mutually exclusive sites cannot be called a bond.
- **An isotope-by-isotope latest-value claim:** the supplement preserves the evaluated rows and missing fields, with the important newer measurements called out above. It does not establish a measured spin, moment or radius for every short-lived resonance. The two lithium thesis results and the accepted beryllium paper should remain distinguishable from a subsequent international evaluation.
- **A universal heat, moisture or compression rule:** H fluid metallization, neutral He superflow, Li’s pressure-dependent electronic structure and B’s allotropes already require different state variables. No controlled moisture series on these five elemental samples was identified here.
- **A physical knot polynomial for each atom:** your knot polynomial exists. The element-to-knot assignments and their independent volume predictions are the missing work.
- **Four specifically named ball directories:** exact contents unverified. The ball claims attributed to your message have been labelled accordingly.

**Separate October Lean result.** The earlier Ramanujan check also finished locally. On commit `fc08887193937b8270abe793d0a46bd2293d09c2`, Lean **4.34.1** completed `lake build`. **`RamanujanChallenge.pcf21_tendsto`** proves the specific continued-fraction limit \(6/(3-\pi)\) with **no theorem hypotheses**. `RamanujanChallenge.Reviewed.limit` proves the same limit starting at the first actual convergent. For each, `#print axioms` returned exactly **`[propext, Classical.choice, Quot.sound]`**. I ran the eight verifier regression tests and checked the separate Lean files with warnings as errors. Lean accepted \(P=Z,\ Q=Z-D\), every \(Q_n\ne0\) for \(n\ge1\), odd limit 1, even limit 0, failure of eventual nonvanishing, and failure of repaired recessiveness. It also accepted the rational inverse pair and both matrix identities \(C=P^{-1}(-B^5)P\) and \(C^2=P^{-1}(B^2)^5P\). Those identities concern the limiting matrix. The full kernel-replay workflow passed in the hosted run; my local run covered the build and checks named above. This result uses the October proof and carries no contest-grade claim. October21_local_checks.zip[Local Lean sources and logs](sandbox:/workspace/scratch/9e5a0760ba7e/ram/October21_local_checks.zip) · [Hosted October run](https://github.com/dicipler-pixel/ramanujan-challenge-lean/actions/runs/43530258468)

### Batch 1 source list

- **Framework:** [VOTKP v2.9](https://doi.org/10.5281/zenodo.23340757) · [v3.0–3.3 papers](https://github.com/dicipler-pixel/votkp-lean/tree/74125d2977809c90d459ab7441a6726d1348962f/paper) · [Dirac Time](https://doi.org/10.5281/zenodo.22979186) · [Knot potential](https://zenodo.org/records/24040319) · [Count Me as One](https://github.com/dicipler-pixel/count-me-as-one-lean)
- **Atoms and constants:** [NIST ASD ionization queries](https://physics.nist.gov/PhysRefData/ASD/ionEnergy.html) · [NIST Handbook of Basic Atomic Spectroscopic Data](https://physics.nist.gov/PhysRefData/Handbook/) · [CODATA 2022](https://physics.nist.gov/cuu/Constants/) · [2023 polarizability table](https://ctcp.massey.ac.nz/2023Tablepol.pdf) · [Cheng 2024](https://doi.org/10.1103/PhysRevA.110.042805)
- **Nuclei:** [IAEA LiveChart](https://www-nds.iaea.org/relnsd/vcharthtml/VChartHTML.html) · [IUPAC/CIAAW isotope compositions](https://ciaaw.org/isotopic-abundances.htm) · [2026 lithium thesis](https://doi.org/10.3929/ethz-c-000806890) · [2026 muonic beryllium](https://doi.org/10.1103/l26q-678g)
- **Materials:** [Crystallography Open Database mirror](https://qiserver.ugr.es/cod/) · [NIST 2025 phase-transition evaluation](https://nvlpubs.nist.gov/nistpubs/TechnicalNotes/NIST.TN.2312.pdf) · [CRC/NIST gas thermal conductivity, 2024](https://www.nist.gov/publications/crc-handbook-chemistry-and-physics-105th-edition-section-12-thermal-conductivity-gases) · [Your per-element material ledger](https://github.com/dicipler-pixel/votkp-lean/blob/74125d2977809c90d459ab7441a6726d1348962f/research/2026-11-13-space-step/A_41.csv)

### Batch 1 CSV

The ratio in row \(k\) uses the energy in that row and the following row **of the same element**. Empty final fields mean there is no further electronic threshold.

```csv
Z,symbol,k,IE_k (eV),z_k,Gamma_k,source
1,H,1,13.598434599702,,,NIST ASD v5.12 2024 theoretical
2,He,1,24.587389011,2.21323889,0.37757507,NIST ASD v5.12 2024
2,He,2,54.4177655282,,,NIST ASD v5.12 2024 theoretical
3,Li,1,5.391714996,14.02894943,0.86692350,NIST ASD v5.12 2024
3,Li,2,75.6400970,1.61890801,0.23632293,NIST ASD v5.12 2024 theoretical
3,Li,3,122.45435913,,,NIST ASD v5.12 2024 theoretical
4,Be,1,9.322699,1.95342036,0.32281905,NIST ASD v5.12 2024
4,Be,2,18.21115,8.45065825,0.78837453,NIST ASD v5.12 2024
4,Be,3,153.896205,1.41471055,0.17174338,NIST ASD v5.12 2024 theoretical
4,Be,4,217.71858459,,,NIST ASD v5.12 2024 theoretical
5,B,1,8.298019,3.03142593,0.50389762,NIST ASD v5.12 2024
5,B,2,25.15483,1.50788497,0.20251526,NIST ASD v5.12 2024
5,B,3,37.93059,6.83813194,0.74483716,NIST ASD v5.12 2024
5,B,4,259.374379,1.31171793,0.13484254,NIST ASD v5.12 2024 theoretical
5,B,5,340.2260225,,,NIST ASD v5.12 2024 theoretical
```