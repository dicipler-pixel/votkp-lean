Jeromie, **the frozen prediction passed on both sides**. Rubidium’s Kr-core opening is outside the wall, and strontium’s is inside. I ran those two ratios before computing the rest of the map.

**The weakest proposal is #4.** Measuring \(IE_1\) for a heavy atom is an achievement, but an opening requires two adjacent thresholds. **The idea I’d add is an exact check on the projector itself:** before interpreting a weak link, calculate how much projector weight the site can distribute among its neighbours. I ran that check for a bcc sodium model. Its eight equivalent neighbours make \(1/12\) unattainable for any single link under the one-orbital, two-spin assumptions, even though the model has a partially filled dispersive band. That identifies a reason the sodium test can fail after the clock placement has been corrected.

**Batch 5 gives a second result worth certifying.** All **110 ordinary Sc–Mn peel steps** are inside the wall, including their quoted uncertainty bounds. All four bound-anion rungs are outside. Mn has no bound isolated ground-state anion. The five elements are metals, yet their ordinary isolated-atom peel ladders never cross the wall. [info.phys.tsinghua.edu.cn](https://info.phys.tsinghua.edu.cn/henucl/ning/148.pdf?utm_source=chatgpt.com)

The standalone atlas contains the two plots, all 433 fixed-core ratios, the 300 configuration-resolved switches into \(d\) or \(f\), the ambiguous transitions, the isotope and crystal tables, and the sodium calculation. The complete Sc–Mn CSV is also inline below. [Sc_to_Mn_opening_atlas.html](https://chatgpt.com/library?file_id=libfile_fde3_f-ae973db2321c819195c1d484cc59e41b_ea4e520c657081918696167b9513e64f&account_id=personal)

## 1. The held-out test and the full opening map

**DERIVED.** The frozen test required \(IE_2/IE_1>3+2\sqrt2\) for Rb and \(IE_3/IE_2<3+2\sqrt2\) for Sr. I used the archive pinned to the runner’s commit. The bounds below put the two input energies at opposite ends of their quoted uncertainties. They are sensitivity bounds, not a joint statistical confidence interval. [Pinned threshold archive](https://github.com/dicipler-pixel/votkp-lean/blob/8332fc1/data/element_thresholds_20261011.json.gz)

| Atom | Energies used, eV | \(z\) | \(\Gamma\) | Range of \(z\) | Frozen call |
|---|---|---:|---:|---:|---|
| Rb | \(27.28954/4.1771281\) | **6.533087** | .734505 | 6.533070–6.533103 | Outside, passed |
| Sr | \(42.88353/11.0302765\) | **3.887802** | .590818 | 3.887784–3.887820 | Inside, passed |

**DERIVED — How to index the map.** Let \(N\) be the electron count of the intermediate ion, after one removal and before the next. Then \(k=Z-N\), and the opening is \(IE_{k+1}/IE_k\). This indexing follows an isoelectronic sequence across increasing nuclear charge. It also prevents counting the same ion repeatedly as a new observation merely because one could begin the peel at different charge states. I joined on actual ionic charge; rows on opposite sides of a missing charge never form a ratio. [Pinned data](https://github.com/dicipler-pixel/votkp-lean/blob/8332fc1/data/element_thresholds_20261011.json.gz)

| Intermediate electron count | Available ratios | First eligible element | First central value inside | Increments in \(Z\) | What the rest of the encoded sequence does |
|---:|---:|---|---|---:|---|
| 2, He-like | 101 | Li, 14.029 | N, 5.640 | 4 | Stays inside through Lr |
| 10, Ne-like | 100 | Na, 9.201 | Mg, 5.330 | 1 | Stays inside through Ds |
| 18, Ar-like | 92 | K, 7.286 | Ca, 4.289 | 1 | Stays inside through Ds |
| 36, Kr-like | 74 | Rb, 6.533 | Sr, 3.888 | 1 | Stays inside through Ds |
| 54, Xe-like | 49 | Cs, 5.947 | Ba, 3.583 | 1 | Stays inside through Lr |
| 86, Rn-like | 17 | Fr, 5.500 central | Fr centrally; Ra clearly inside | 0 centrally | Fr straddles the wall; later central values stay inside |
| 118, Og-like | 0 | Element 119 would be first | — | — | No test in this archive |

**DERIVED — Francium is the important brake on the pattern.** Its encoded \(IE_1=4.0727411(11)\) eV is precise, but \(IE_2=22.4(1.9)\) eV is semiempirical. The resulting range is **5.0335–5.9665**, which contains the wall at 5.8284. Radium’s range is **2.8973–3.2127**, entirely inside. I would certify “Fr’s encoded central value is inside” and “Fr’s input interval straddles the wall” as separate statements. The stronger claim that this shell starts inside experimentally remains open. [Pinned inputs, including grades and uncertainties](https://github.com/dicipler-pixel/votkp-lean/blob/8332fc1/data/element_thresholds_20261011.json.gz)

**DERIVED — Archive coverage.** The file has 118 element records and **5,847 threshold entries** out of 7,021 possible ordinary thresholds through \(Z=118\). Elements 111–118 have empty threshold lists. I found **5,714 genuinely adjacent ordinary pairs** across the archive. The plotted noble-core curves are electron-count sequences. A particular orbital interpretation at the heavy end still requires the configuration on that row. [Archive](https://github.com/dicipler-pixel/votkp-lean/blob/8332fc1/data/element_thresholds_20261011.json.gz)

**DERIVED — The \(d\) and \(f\) map needs a different rule.** I expanded the initial and final ground-state occupations and asked which subshell loses one electron in each of two consecutive removals. Of the 5,714 pairs, 4,522 retain the same removal subshell, 1,098 change removal subshell, and 94 have a rearrangement or an unresolved assignment. Among the unambiguous changes, **300 enter a \(d\) or \(f\) subshell**. Their largest central ratio is **2.83576**, the \(5s\to4d\) change in silver. All 300 are inside the wall. This statement has a precise domain: clean changes in the tabulated ground occupations. The 94 unresolved pairs remain in the atlas. [ASD configuration data](https://physics.nist.gov/asd) · [Machine-readable configuration compilation](https://github.com/lmmentel/mendeleev)

**RECOGNISED — A correction to the proposed interpretation.** The six bare hydrogenic shell ratios being inside proves that an observed outside ratio requires a departure from those bare values. It does **not** isolate screening as the only possible cause. The Al–Si calculation in this project already gives an example where relativistic binding changes the ordering of two observables. At high \(Z\), screening, relaxation, correlation, relativistic terms and configuration changes must be distinguished before assigning the departure to one of them. [arxiv.org](https://arxiv.org/abs/1506.01885?utm_source=chatgpt.com)

## 2. Which ideas to keep, and what I would change

### The fingerprint has shape, scale and direction

**DERIVED.** For the ordinary ladder define \(r_k=\ln(IE_{k+1}/IE_k)\), \(L=\sum_k r_k=\ln(IE_Z/IE_1)\), and \(p_k=r_k/L\). Then \(\sum p_k=1\). Two ladders can have the same endpoints and put different fractions of their total log change into a particular opening. For a down-column comparison I aligned the preceding noble-gas core, Ar in period 4 and Kr in period 5. The entries are the fraction \(p_k\) of the **ordinary** ladder at that opening. [Pinned threshold data](https://github.com/dicipler-pixel/votkp-lean/blob/8332fc1/data/element_thresholds_20261011.json.gz)

| Group pair | Period 4 | Period 5 |
|---|---:|---:|
| Sc / Y | 15.94% | 13.32% |
| Ti / Zr | 12.08% | 10.44% |
| V / Nb | 9.66% | 8.62% |
| Cr / Mo | 8.07% | 7.38% |
| Mn / Tc | 7.02% | 6.51% |

**RECOGNISED.** All five fractions fall on moving down a column, and both rows fall on moving across the five groups. That is a fingerprint comparison with a stated alignment. A different alignment, such as the K opening or the half-filled \(d\) configuration, tests a different feature.

**DERIVED — One trap for the Russell interpretation.** Reversing the path sends \(r_k\mapsto-r_{n+1-k}\) and \(L\mapsto-L\). Consequently \(p_k\mapsto p_{n+1-k}\): normalizing by the signed total cancels the overall sign. Keep the ordered signed vector and either \(L\) or its orientation bit alongside the normalized shape. For a comparison that should itself flip sign, use \(r_k/\sum_j|r_j|\). Sorting the normalized entries would also erase where in the ladder the opening occurred.

### The projector needs a coordination check

**DERIVED — The idea I would add.** For an orthogonal occupied-state projector \(P=P^\dagger=P^2\), let \(C_i=P_{ii}\) be the on-site block. Taking the trace of the \(ii\) block of \(P^2=P\) gives

\[
\boxed{\sum_{j\ne i}\|P_{ij}\|_F^2
=\operatorname{Tr}(C_i-C_i^2).}
\]

The right side is the **total off-site weight available to that site**. It can be small because a shell is nearly full, or it can be divided among many neighbours. Those are different physical readings. The identity uses exactly your \(X_{ij}=\|P_{ij}\|_F^2\) and an orthogonal decomposition into sites.

**DERIVED — Sodium control actually run.** I used bcc geometry, one \(3s\) orbital with two spin states per site, one electron per site, equal junction clocks, and spin-independent nearest-neighbour hopping. Symmetry and half filling give \(C_i=\tfrac12 I_2\). Therefore the entire off-site weight is \(1/2\). A bcc site has eight equivalent nearest neighbours, so

\[
8X_{\rm nn}\leq\tfrac12,\qquad
X_{\rm nn}\leq\tfrac1{16}=0.0625<\tfrac1{12}.
\]

This model **cannot** pass the per-link cutoff, even if its nearest neighbours receive the entire off-site weight. Yet its band is partially occupied and disperses through the Fermi energy. That supplies a counterexample to making the raw \(1/12\) rule necessary for metallic-band behaviour across arbitrary coordinations.

| Reciprocal grid I ran | Nearest-neighbour \(X\), two spins |
|---|---:|
| \(32^3\) | .033365474 |
| \(64^3\) | .033305224 |
| \(96^3\) | .033294080 |

**DERIVED — Reproduction.** In primitive reciprocal angles I used \(\epsilon=-2t[\cos u+\cos v+\cos w+\cos(u+v+w)]\), filled the negative energies and calculated \(X=2|\langle e^{iu}\mathbf1_{\epsilon<0}\rangle|^2\). The grid shifts and outputs are in the atlas. This is a controlled band model with sodium’s coordination and valence count. Its output is dimensionless; it supplies no numerical value for sodium’s resistivity.

**HYPOTHESIS — How I would strengthen idea #3.** Keep the original \(X_{ij}\), and also report (i) total off-site weight, (ii) the fraction carried by the first neighbour shell, and (iii) response to a boundary twist as the system grows. Use a filled \(p\) manifold **and accessible empty states** for Ar. If one keeps only completely filled \(p\) states, its occupied projector is the identity on the entire basis; disconnection has then been built into the test. A held-out conducting phase that fails the proposed bulk-response criterion would defeat the transfer. Comparing the spatial decay of the occupied projector offers a separate check. [journals.aps.org](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.82.2127?utm_source=chatgpt.com)

### Heavy atoms and a frozen element-119 call

**MEASURED.** Sato and colleagues reported atom-at-a-time first ionization potentials for Fm, Md, No and Lr. These measurements constrain the neutral-atom end of the ladder. To test an opening one also needs the threshold on the far side, its uncertainty, and the configurations identifying the opening. [pubs.acs.org](https://pubs.acs.org/doi/10.1021/jacs.8b09068?utm_source=chatgpt.com)

**DERIVED.** The archive illustrates the issue directly. Its first two thresholds in eV are Fm \(6.5,12.4\) (S/S), Md \(6.58,12.4\) (S/S), No \(6.62621,12.93\) (E/T), and Lr \(4.96,14.54\) (E/T). All four central adjacent ratios are inside. None of those four archive pairs consists of two unbracketed evaluated entries. In particular, Lr’s weak outer electron above a No-like core gives \(14.54/4.96=2.93\); the second input is theoretical. I would preserve the experimental paper’s values and the archive’s values as separate columns. [Archive](https://github.com/dicipler-pixel/votkp-lean/blob/8332fc1/data/element_thresholds_20261011.json.gz) [pubs.acs.org](https://pubs.acs.org/doi/10.1021/jacs.8b09068?utm_source=chatgpt.com)

**HYPOTHESIS — Frozen November 21, 2026.** My low-confidence prediction for neutral element 119 is

\[
1<IE_2/IE_1<3+2\sqrt2.
\]

The falling first-eligible ratios from K through Cs and the central Fr estimate motivate it. Fr’s uncertainty weakens it, and a bare-shell ratio cannot settle it. A reliable \(IE_2/IE_1\geq5.828427\ldots\) defeats the predicted upper branch classification. An interval that straddles the wall leaves the prediction unresolved. This is a prediction of the **ratio**; calling it an \(8s\)-to-core opening also requires configuration evidence.

## 3. Batch 5 · Scandium through manganese

**DERIVED — What changes at scandium.** K and Ca expose the Ar core by exhausting \(4s\). From Sc through Mn, the last electron above that core is a \(3d\) electron. The next removal is from \(3p\). Both have principal quantum number 3. The Ar-core sequence remains meaningful by electron count, but carrying the label “\(4s\to3p\), hydrogenic floor \(16/9\)” into these five rows would be a physical misidentification. **Chromium’s 1.76852 happens to sit close to \(16/9=1.77778\); the configurations show why the numerical resemblance is misleading.** [math.nist.gov](https://math.nist.gov/DFTdata/atomdata/configuration.html?utm_source=chatgpt.com)

**DERIVED.** Each cell gives \(k;\ z,\Gamma\). The wall is \(z=5.828427\ldots\). The comparison values \(9/4\) for the L opening and \(4\) for the K opening still apply as bare-shell references. Every L and K ratio below exceeds its corresponding bare value. All remain inside the loop wall. [Threshold archive](https://github.com/dicipler-pixel/votkp-lean/blob/8332fc1/data/element_thresholds_20261011.json.gz)

| Element | Anion rung \(0\) | Switch into \(3d\) removal | Ar core, \(3d\to3p\) | L opening | K opening |
|---|---|---|---|---|---|
| Sc | 36.57872, .94678 | 2; 1.93416, .31837 | 3; 2.96845, .49602 | 11; 2.75166, .46690 | 19; 4.40613, .63005 |
| Ti | 90.39079, .97812 | 2; 2.02510, .33886 | 4; 2.29502, .39302 | 12; 2.70213, .45977 | 20; 4.38449, .62856 |
| V | 12.78510, .85492 | 1; 2.16923, .36893, **rearranged** | 5; 1.96265, .32493 | 13; 2.66449, .45422 | 21; 4.36485, .62720 |
| Cr | 10.01070, .81836 | 1; 2.43646, .41801 | 6; 1.76852, .27759 | 14; 2.63326, .44953 | 22; 4.34693, .62595 |
| Mn | **No bound ground-state anion** | 2; 2.15269, .36562 | 7; 1.64006, .24244 | 15; 2.60518, .44524 | 23; 4.33050, .62480 |

**MEASURED — The affinity inputs matter.** Ning and Lu’s evaluated table gives Sc .179380(22), Ti .07554(5), V .52766(20), and Cr .675928(27) eV. These differ from older summaries that still list, for example, .188 for Sc or .666 for Cr. The same evaluation lists Mn as unbound. I used the evaluated values for rung 0. [info.phys.tsinghua.edu.cn](https://info.phys.tsinghua.edu.cn/henucl/ning/148.pdf?utm_source=chatgpt.com)

**DERIVED — Bound on the whole batch.** The largest ordinary ratio is Sc’s K opening, 4.4061282. Even maximizing each ratio over the quoted endpoint uncertainties, the largest upper bound in the entire batch is **4.4061525 rounded upward**. Thus the 110 inside classifications are well separated from the wall. Anion rung 0 contributes four further defined steps, for **114 calculated reflections** from 115 ordinary thresholds and four positive affinities. [Archive](https://github.com/dicipler-pixel/votkp-lean/blob/8332fc1/data/element_thresholds_20261011.json.gz) [info.phys.tsinghua.edu.cn](https://info.phys.tsinghua.edu.cn/henucl/ning/148.pdf?utm_source=chatgpt.com)

### Intrinsic face positions and the He-like check

**DERIVED.** The face coordinates below use your \(a=\tanh(\ln z/4)\). The last two columns extend the same H-like/He-like readings used in batch 4. \(S_Z\) rises farther above \(5/8\), while \(\sigma_Z\) keeps falling. At Mn their difference has grown to **.094728**. The K-opening \(\Gamma\) in the preceding table and \(S_Z\) below describe different transitions and different operations. Their values near .625 should retain their labels. [Ball work](https://github.com/dicipler-pixel/votkp-lean/tree/a60a000/research/seven-balls-his-light) · [Screening inputs](https://github.com/dicipler-pixel/votkp-lean/blob/8332fc1/data/element_thresholds_20261011.json.gz)

| Element | Anion apex | Ar-core apex | L apex | K apex | \(S_Z\) | \(\sigma_Z\) |
|---|---:|---:|---:|---:|---:|---:|
| Sc | .71623 | .26549 | .24778 | .35465 | .627981 | .577030 |
| Ti | .80966 | .20475 | .24352 | .35357 | .629395 | .568838 |
| V | .56290 | .16699 | .24022 | .35259 | .630834 | .559811 |
| Cr | .51969 | .14158 | .23744 | .35169 | .632303 | .549910 |
| Mn | — | .12306 | .23491 | .35086 | .633805 | .539077 |

**RECOGNISED — Rank change.** At Sc the Ar-core opening still exceeds the L opening, \(2.96845>2.75166\). At Ti it has dropped below, \(2.29502<2.70213\), and it stays below through Mn. Meanwhile the K opening remains the largest ordinary step in all five. The Ar-core face shrinks from .26549 to .12306 over this short run while the K face changes only from .35465 to .35086. That is where the fingerprint changes most visibly.

### Atomic properties and visible light

**MEASURED / evaluated.** The configurations and terms are for neutral gas-phase ground states. Static dipole polarizabilities are the CTCP recommended values in atomic units, combining calculation and experiment. The three radii in each row are Cordero covalent (2008), Alvarez van der Waals (2013), and the coordination-12 metallic-radius compilation, in pm. Ionic examples use Shannon’s effective-radius convention (1976). The appendix gives the alternative ionic charge, coordination and spin entries. [pdg.lbl.gov](https://pdg.lbl.gov/2025/reviews/rpp2024-rev-elements-electronic-struct.pdf?utm_source=chatgpt.com)

| Element | Ground configuration and term | Polarizability | Covalent / vdW / metallic, pm | Six-coordinate ion, pm | Representative neutral-atom lines, nm |
|---|---|---:|---:|---|---|
| Sc | [Ar] \(3d4s^2,\ {}^2D_{3/2}\) | 97(10) | 170 / 258 / 162 | Sc³⁺ 74.5 | 390.7484, 391.1812 |
| Ti | [Ar] \(3d^24s^2,\ {}^3F_2\) | 100(10) | 160 / 246 / 147 | Ti⁴⁺ 60.5 | 430.1079, 498.1730 |
| V | [Ar] \(3d^34s^2,\ {}^4F_{3/2}\) | 87(10) | 153 / 242 / 134 | V³⁺ 64 | 437.9230, 438.4710 |
| Cr | [Ar] \(3d^54s,\ {}^7S_3\) | 83(12) | 139 / 245 / 128 | Cr³⁺ 61.5 | 425.44, 427.48 |
| Mn | [Ar] \(3d^54s^2,\ {}^6S_{5/2}\) | 68(9) | 150 / 245 / 127 | high-spin Mn²⁺ 83 | 403.08, 403.31, 403.45 |

**MEASURED — Mainstream-blend watch.** The listed wavelengths are lines of excited neutral atoms, with air wavelengths rounded as displayed. Bulk Sc, Ti, V, Cr and Mn have metallic silver-to-grey appearances and broadband optical responses. A violet V I line does not assign a violet colour to the V crystal, and Ti surface-film interference does not give an isolated Ti atom a new emission line. An optical ball model should specify whether it predicts an atomic transition, a crystal’s reflectance, or a film spectrum. [NIST Handbook, 2005](https://physics.nist.gov/PhysRefData/Handbook/) [physics.nist.gov](https://physics.nist.gov/PhysRefData/Handbook/Tables/scandiumtable2.htm?utm_source=chatgpt.com)

### The five solids, their gaps, and what pressure changes

**MEASURED / DERIVED.** The table gives rounded ambient-pressure reference values. The electrical column is resistivity in \(\mu\Omega\,\mathrm{cm}\); conductivity in MS/m is \(100/\rho\) in those units. Thermal conductivity is in W m\(^{-1}\) K\(^{-1}\). Values vary with temperature, purity and specimen. For Ti the phase-transition compilation gives about 1943 K for melting, while the PubChem compilation gives 1941 K; the reference spread is visible at this precision. The crystal distances below are independently calculated from dated coordinates or lattice parameters. [courses.physics.ucsd.edu](https://courses.physics.ucsd.edu/2025/Spring/physics152b/atomsinsolids.pdf?utm_source=chatgpt.com)

| Element | Density, g/cm³, approx. | Melt / boil, K, approx. | Resistivity → conductivity | Thermal conductivity, approx. | Ambient crystal cell and nearest distance, Å |
|---|---:|---:|---|---:|---|
| Sc | 2.99 | 1814 / 3109 | 51 → 1.96 MS/m | 15.8 | hcp \(a=3.309,\ c=5.2733;\ d=3.2560\) |
| Ti | 4.51 | 1941–1943 / 3560 | 47.8 → 2.09 MS/m | 21.9 | hcp \(a=2.950,\ c=4.686;\ d=2.8966\) |
| V | ~6.1 | 2183 / 3680 | 24.8 → 4.03 MS/m | 30.7 | bcc \(a=3.0241;\ d=2.6190\) |
| Cr | ~7.2 | 2180 / 2944 | 12.9 → 7.75 MS/m | 93.9 | bcc \(a=2.8839;\ d=2.4975\) |
| Mn | ~7.3 | 1519 / 2334 | 139 → 0.72 MS/m | ~7.8 | \(\alpha\)-Mn, cubic \(a=8.9125;\ d_{\min}=2.2435\) |

**RECOGNISED — What that means for the ball mapping.** Each solid has occupied states extending across a lattice, yet conductivity differs by more than a factor of ten between Cr and Mn. All five ordinary ladders stay inside. No measured Bruggeman constituent fraction follows from those five ladders. The appropriate comparison for your sea is between a phase-specific occupied projector, the inequivalent intersite paths, and a transport observable at the same pressure and temperature. The apex coordinates already specify the internal atomic map; the distance in ångströms still needs its own calibration.

**Scandium.** **DERIVED:** Sc is the first case where the Ar core is exposed by removing \(3d^1\). The measured-input ratio is \(73.4894/24.756839=2.96845\). **MEASURED:** the high-purity 1956 hcp refinement supplies a reference gap geometry. Under compression, Sc develops an incommensurate host–guest structure, and elemental superconductivity was measured at **36 K at 260 GPa**. **HYPOTHESIS / kill condition:** a one-row Sc model that predicts the same response for every inequivalent host and guest path would fail if phase-resolved link measurements distinguish them. Atomic v1 knot assignment: **none found**. [Sc refinement](https://www.crystallography.net/cod/9010985.html) [cronfa.swan.ac.uk](https://cronfa.swan.ac.uk/Record/cronfa28287/Download/0028287-11052017155800.pdf?utm_source=chatgpt.com)

**Titanium.** **DERIVED:** Ti’s weak affinity puts its anion apex at .80966, the largest in the batch. Its ordinary Ar-core apex is only .20475. **MEASURED:** the ambient hcp structure and the high-temperature bcc structure give different coordinations; a 1173 K bcc refinement has \(a=3.3065\) Å and \(d=2.8635\) Å. Under pressure Ti also accesses the \(\omega\) phase and further structures. The 2022 transport experiment reported superconducting onset above **26.2 K** and zero resistance at **21 K**. **HYPOTHESIS / kill condition:** if the neutral anion apex alone fixed the solid’s transport, changing phase at fixed element could not produce distinct responses. Use the phase as an explicit input. Atomic v1 knot assignment: **none found**. [Ti bcc refinement](https://www.crystallography.net/cod/9008554.html) [nature.com](https://www.nature.com/articles/s41467-022-33077-3?utm_source=chatgpt.com)

**Vanadium.** **MEASURED:** the neutral atom is \(3d^34s^2\), while \(V^+\) is \(3d^4\). One electron leaves, but two \(4s\) occupations disappear and a \(3d\) occupation appears. **DERIVED:** the \(k=1\) energy ratio remains exactly usable. A label that treats it as a clean single-orbital decrement fails directly against the ground configurations. **MEASURED:** ambient bcc V gives a simple lattice control. A 2025 study reports a shock-induced structural transformation; a March 2026 APS report gives a compressed-state \(T_c\) of **20.9 K at 265 GPa**, with a rhombohedral phase emerging above 200 GPa in that experiment. I treat the latter as a conference result. **HYPOTHESIS:** use V as the control for any model that claims to infer the path of an individual electron from adjacent threshold energies alone. Atomic v1 knot assignment: **none found**. [V reference cell](https://www.crystallography.net/cod/9012770.html) [math.nist.gov](https://math.nist.gov/DFTdata/atomdata/configuration.html?utm_source=chatgpt.com)

**Chromium.** **DERIVED:** neutral Cr has \(3d^54s\), so its first two removals give a clean \(4s\to3d\) switch at \(k=1\). Its Ar-core ratio of 1.76852 is an intra-\(n=3\) subshell transition. **MEASURED:** chromium is the best electrical conductor of these five in the quoted comparison. Its bcc phase supports spin- and charge-density waves, resolved in a 2025 electronic-band study. I found no established bulk elemental \(T_c\) in the sources checked; superconducting Cr compounds are distinct materials. **HYPOTHESIS / kill condition:** a scalar charge-only projector that claimed to distinguish opposite spin arrangements would fail on states with the same scalar density. Spin-resolved blocks provide the relevant observable. Atomic v1 knot assignment: **none found**. [Cr bcc refinement](https://www.crystallography.net/cod/5000220.html) [nature.com](https://www.nature.com/articles/s43246-025-00789-0?utm_source=chatgpt.com)

**Manganese.** **MEASURED / DERIVED:** Mn and Cr both contain a half-filled \(3d^5\) subshell, but Mn has the extra \(4s\) electron and no bound ground-state anion. All 24 ordinary Mn steps are inside. The \(\alpha\)-Mn crystal has inequivalent sites, so its shortest contact cannot describe every gap. The diffraction records give \(\alpha\): \(a=8.9125,\ d_{\min}=2.2435\) Å; \(\beta\): \(a=6.3145,\ d_{\min}=2.3743\) Å; high-temperature fcc \(\gamma\): \(a=3.863,\ d=2.7316\) Å; and bcc \(\delta\): \(a=3.081,\ d=2.6682\) Å in the cited specimen. A high-pressure study followed \(\alpha\)-Mn to 220 GPa. I found no verified bulk elemental superconducting transition in the retrieved references. [α](https://www.crystallography.net/cod/9011068.html) · [β](https://www.crystallography.net/cod/1539039.html) · [γ](https://www.crystallography.net/cod/9008590.html) · [δ](https://www.crystallography.net/cod/9008591.html) [harvest.aps.org](https://harvest.aps.org/v2/journals/articles/10.1103/PhysRevB.103.014101/fulltext?utm_source=chatgpt.com)

**HYPOTHESIS — Mn supplies a physical mirror test for Russell and v1.** The two hands of elemental \(\beta\)-Mn have space groups \(P4_132\) and \(P4_332\). Researchers have assigned the enantiomorphs by diffraction. Both crystals have the same isolated-Mn peel vector. **Spatial mirroring and reversing the peel order are two independently performable operations.** An observable claiming to read the crystal’s hand should change under the first with the peel order held fixed. A test that flips only when the list is reversed measures peel orientation. For the knot side, the missing object is a reproducible closed path in the crystal or projector transport to which Jeromie’s polynomial can be applied. Element-specific atomic polynomial: **none found**. This pair gives a way to test any proposed construction against independently identified handedness. [pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/33990329/?utm_source=chatgpt.com)

### The nuclear centres

**MEASURED / DERIVED.** The isotope moments below are in nuclear magnetons. Definite spin zero gives zero magnetic dipole by rotational symmetry. The charge radii are **Ohayon’s Table 2 reference evaluation** in fm. The separate 2025 Sc spectroscopy paper explicitly uses the older \(^{45}\)Sc anchor 3.5459(25) fm to infer radioactive-isotope radii. Those two reference choices should be labeled if combining tables. The appendix preserves 134 ground-state records from the dated IAEA snapshot, including blanks and tentative assignments. [arxiv.org](https://arxiv.org/pdf/2409.08193?utm_source=chatgpt.com)

| Element | Naturally occurring isotope spin and moment | Selected reference charge radii, fm | Representative nucleus: \(p,n;\ u,d\) net valence |
|---|---|---|---|
| Sc | 45: \(7/2^-,+4.754\) | 45: 3.548(6) | \(^{45}\)Sc: 21,24; 66,69 |
| Ti | 46,48,50: \(0^+,0\); 47: \(5/2^-,-.78814\); 49: \(7/2^-,-1.1037\) | 48: 3.595(4); 50: 3.572(4) | \(^{48}\)Ti: 22,26; 70,74 |
| V | 50: \(6^+,+3.3442\), radioactive; 51: \(7/2^-,+5.1464\) | 51: 3.598(5) | \(^{51}\)V: 23,28; 74,79 |
| Cr | 50,52,54: \(0^+,0\); 53: \(3/2^-,-.47431\) | 50: 3.664(4); 52: 3.644(4); 54: 3.689(4) | \(^{52}\)Cr: 24,28; 76,80 |
| Mn | 55: \(5/2^-,+3.4669\) | 55: 3.705(7) | \(^{55}\)Mn: 25,30; 80,85 |

**RECOGNISED.** In the Standard Model ball picture these quantities label the centre while a peel changes the wall. \(^{51}\)V and \(^{52}\)Cr are a particularly clean comparison: both have 28 neutrons, but adding one proton changes the nuclear ground-state spin from \(7/2\) to zero. Conversely the electronic Cr and Mn ground states both contain \(3d^5\), while their anion binding differs qualitatively. These give two ways to test which trait a proposed vector actually keeps.

**RECOGNISED — Correction to batch 4.** On reopening Ohayon’s Table 2, I found that its entries for \(^{35}\)Cl, \(^{38}\)Ar and \(^{40}\)Ar are **3.388(15), 3.402(7) and 3.427(5) fm**. My earlier batch did not accurately identify those Table 2 values. For the same table the \(^{39}\)K, \(^{40}\)Ca and \(^{48}\)Ca uncertainties are **3.435(3), 3.481(3), 3.475(3) fm**. This correction affects the nuclear reference column only. [arxiv.org](https://arxiv.org/pdf/2409.08193?utm_source=chatgpt.com)

**Set aside, with why.** The phase appendix contains 20 selected refinements. I could not establish an exhaustive coordinate-and-neighbour census of every pressure phase, particularly the complex Sc structures. I also left 94 ambiguous subshell labels open, kept the heavy-ion theoretical thresholds identified, and treated all new map and projector results here as numerical or algebraic work. I made no new Lean build or branch change. The runner’s 81-theorem count at `8332fc1` remains its reported audit. [Runner’s commit](https://github.com/dicipler-pixel/votkp-lean/commit/8332fc1)

## Inline CSV

**DERIVED.** At \(k=0\) the energy column is the EA. At \(k\ge1\) it is \(IE_k\). Each ratio uses the current and next energies. `E`, `S`, and `T` denote the archive’s unbracketed evaluated, semiempirical, and theoretical input grades on that row. `EA22` denotes Ning and Lu. Blanks at the bare nucleus are intentional. All 115 ordinary central energies matched a separately distributed ASD-derived compilation. [ASD](https://doi.org/10.18434/T4W30F) · [Affinity evaluation](https://doi.org/10.1063/5.0080243)

```csv
Z,symbol,k,IE_k (eV),z_k,Gamma_k,source
21,Sc,0,0.179380,36.57872,0.94678,EA22
21,Sc,1,6.56149,1.95074,0.32220,E
21,Sc,2,12.79977,1.93416,0.31837,E
21,Sc,3,24.756839,2.96845,0.49602,E
21,Sc,4,73.4894,1.25120,0.11159,E
21,Sc,5,91.95,1.20370,0.09243,S
21,Sc,6,110.68,1.24675,0.10982,S
21,Sc,7,137.99,1.14559,0.06786,S
21,Sc,8,158.08,1.13885,0.06492,S
21,Sc,9,180.03,1.25079,0.11142,E
21,Sc,10,225.18,1.10933,0.05183,S
21,Sc,11,249.798,2.75166,0.46690,S
21,Sc,12,687.36,1.10233,0.04868,E
21,Sc,13,757.7,1.09964,0.04746,S
21,Sc,14,833.2,1.11198,0.05302,S
21,Sc,15,926.5,1.08861,0.04243,S
21,Sc,16,1008.6,1.08418,0.04039,S
21,Sc,17,1093.5,1.10937,0.05185,S
21,Sc,18,1213.1,1.06171,0.02993,S
21,Sc,19,1287.957,4.40613,0.63005,T
21,Sc,20,5674.9036,1.06324,0.03065,T
21,Sc,21,6033.75643,,,T
22,Ti,0,0.07554,90.39079,0.97812,EA22
22,Ti,1,6.82812,1.98818,0.33070,E
22,Ti,2,13.5755,2.02510,0.33886,E
22,Ti,3,27.49171,1.57383,0.22295,E
22,Ti,4,43.26717,2.29502,0.39302,E
22,Ti,5,99.299,1.20377,0.09246,E
22,Ti,6,119.533,1.17691,0.08127,S
22,Ti,7,140.68,1.21197,0.09583,S
22,Ti,8,170.5,1.12669,0.05957,S
22,Ti,9,192.1,1.12400,0.05838,S
22,Ti,10,215.92,1.22763,0.10219,E
22,Ti,11,265.07,1.09971,0.04749,S
22,Ti,12,291.5,2.70213,0.45977,S
22,Ti,13,787.67,1.09691,0.04621,E
22,Ti,14,864.0,1.09317,0.04451,S
22,Ti,15,944.5,1.10376,0.04932,S
22,Ti,16,1042.5,1.08412,0.04036,S
22,Ti,17,1130.2,1.07972,0.03833,S
22,Ti,18,1220.3,1.10325,0.04909,S
22,Ti,19,1346.3,1.05865,0.02849,S
22,Ti,20,1425.257,4.38449,0.62856,T
22,Ti,21,6249.0226,1.06030,0.02927,T
22,Ti,22,6625.81023,,,T
23,V,0,0.52766,12.78510,0.85492,EA22
23,V,1,6.746187,2.16923,0.36893,E
23,V,2,14.634,2.00295,0.33399,E
23,V,3,29.3111,1.59356,0.22886,E
23,V,4,46.709,1.39762,0.16584,E
23,V,5,65.28165,1.96265,0.32493,E
23,V,6,128.125,1.17635,0.08103,E
23,V,7,150.72,1.15147,0.07040,S
23,V,8,173.55,1.18698,0.08550,S
23,V,9,206.0,1.11893,0.05613,S
23,V,10,230.5,1.10757,0.05104,S
23,V,11,255.3,1.21075,0.09533,S
23,V,12,308.5,1.09003,0.04308,S
23,V,13,336.274,2.66449,0.45422,S
23,V,14,896.0,1.09062,0.04335,E
23,V,15,977.2,1.08770,0.04201,S
23,V,16,1062.9,1.09625,0.04591,S
23,V,17,1165.2,1.08042,0.03865,S
23,V,18,1258.9,1.07570,0.03647,S
23,V,19,1354.2,1.09784,0.04664,S
23,V,20,1486.7,1.05580,0.02714,S
23,V,21,1569.656,4.36485,0.62720,T
23,V,22,6851.3112,1.05763,0.02801,T
23,V,23,7246.12624,,,T
24,Cr,0,0.675928,10.01070,0.81836,EA22
24,Cr,1,6.76651,2.43646,0.41801,E
24,Cr,2,16.486305,1.87786,0.30504,E
24,Cr,3,30.959,1.58791,0.22717,E
24,Cr,4,49.16,1.41294,0.17113,S
24,Cr,5,69.46,1.30485,0.13226,S
24,Cr,6,90.6349,1.76852,0.27759,E
24,Cr,7,160.29,1.15266,0.07092,S
24,Cr,8,184.76,1.06706,0.07709,S
24,Cr,9,215.62,1.16706,0.07709,S
24,Cr,10,244.5,1.10757,0.05104,S
24,Cr,11,270.8,1.09564,0.04564,S
24,Cr,12,296.7,1.19548,0.08904,S
24,Cr,13,354.7,1.08306,0.03988,S
24,Cr,14,384.163,2.63326,0.44953,S
24,Cr,15,1011.6,1.08462,0.04059,S
24,Cr,16,1097.2,1.08276,0.03973,S
24,Cr,17,1188.0,1.08790,0.04240,S
24,Cr,18,1294.8,1.07700,0.03707,S
24,Cr,19,1394.5,1.09297,0.04442,S
24,Cr,20,1524.15,1.05933,0.02882,S
24,Cr,21,1634.1,1.05329,0.02595,S
24,Cr,22,1721.183,4.34693,0.62595,T
24,Cr,23,7481.8624,1.05519,0.02686,T
24,Cr,24,7894.80289,,,T
25,Mn,0,,,,EA22
25,Mn,1,7.434038,2.10384,0.35564,E
25,Mn,2,15.63999,2.15269,0.36562,E
25,Mn,3,33.668,1.52103,0.20667,E
25,Mn,4,51.21,1.41398,0.17149,S
25,Mn,5,72.41,1.32031,0.13805,S
25,Mn,6,95.604,1.24684,0.10986,E
25,Mn,7,119.203,1.64006,0.24244,E
25,Mn,8,195.5,1.13499,0.06323,S
25,Mn,9,221.89,1.12037,0.05677,S
25,Mn,10,248.6,1.15084,0.07013,S
25,Mn,11,286.1,1.09892,0.04713,S
25,Mn,12,314.4,1.09288,0.04438,S
25,Mn,13,343.6,1.17273,0.07950,S
25,Mn,14,402.95,1.07997,0.03845,S
25,Mn,15,435.172,2.60518,0.44524,S
25,Mn,16,1133.7,1.07974,0.03834,S
25,Mn,17,1224.1,1.07859,0.03781,S
25,Mn,18,1320.3,1.08377,0.04020,S
25,Mn,19,1430.9,1.07429,0.03581,S
25,Mn,20,1537.2,1.06896,0.03333,S
25,Mn,21,1643.2,1.08855,0.04240,S
25,Mn,22,1788.7,1.05097,0.02485,S
25,Mn,23,1879.873,4.33050,0.62480,T
25,Mn,24,8140.7864,1.05296,0.02580,T
25,Mn,25,8571.95438,,,T
```

**Source list**

- Framework, clock definitions and exact threshold inputs. [Pinned VOTKP archive](https://github.com/dicipler-pixel/votkp-lean/blob/8332fc1/data/element_thresholds_20261011.json.gz) · [Moving-matrix ball research](https://github.com/dicipler-pixel/votkp-lean/tree/a60a000/research) · [Standard Model ball work](https://github.com/dicipler-pixel/votkp-lean/tree/claude/sm-ball-20261111/research/2026-11-11-standard-model-ball)
- Atomic energies, configurations, spectra and polarizabilities. [NIST ASD 5.12, 2024](https://doi.org/10.18434/T4W30F) · [Ning and Lu, 2022](https://doi.org/10.1063/5.0080243) · [NIST optical handbook](https://physics.nist.gov/PhysRefData/Handbook/) · [CTCP, 2025](https://ctcp.massey.ac.nz/2025Tablepol.pdf)
- Nuclear data. [IAEA LiveChart](https://nds.iaea.org/relnsd/v1/data?fields=ground_states&nuclides=all) · [IUPAC isotope compositions](https://www.ciaaw.org/isotopic-abundances.htm) · [Ohayon reference radii, 2025 revision](https://arxiv.org/abs/2409.08193) · [Sc isotope shifts, 2025](https://doi.org/10.1103/PhysRevLett.134.182501)
- Crystal and transport comparisons. [Crystallography Open Database](https://www.crystallography.net/cod/) · [NIST liquid-metal transport review, 2024](https://www.nist.gov/publications/reference-correlations-density-and-thermal-conductivity-and-review-viscosity) · [Experimental assignment of β-Mn handedness, 2021](https://doi.org/10.1126/sciadv.abg0868) · [Atom-at-a-time heavy-actinide measurements, 2018](https://doi.org/10.1021/jacs.8b09068)