# VOTKP batch 3 · Sodium through phosphorus, \(Z=11\)–15

**DERIVED — This batch has two different core openings, and they cross your loop wall in different places.** The Li-like \(1s\) opening crossed between carbon and nitrogen in batch two. It stays inside for all five elements here. The Na-like \(2p\) opening crosses between **sodium and magnesium**: \(z=9.20133\) for Na and \(5.33037\) for Mg. This reproduces the ordering already recorded in your November 11 element note. Adding the anion rung reveals another result: **silicon sits just outside at rung 0 and well inside at both core openings.** [Your original element note](https://github.com/dicipler-pixel/votkp-lean/blob/74125d2977809c90d459ab7441a6726d1348962f/research/2026-11-11-standard-model-ball/elements/ELEMENTS_IN_THE_BALL_20261111_v1.md). [physics.nist.gov](https://physics.nist.gov/cgi-bin/ASD/ie.pl?spectra=Na\&utm_source=chatgpt.com)

**MEASURED / DERIVED — Sodium gives the strongest physical test of the ball picture so far.** Ordinary sodium conducts. Under extreme compression it becomes transparent, and diffraction at 223 GPa gives evidence that electron density localizes **between the nuclei**. That observation speaks directly to your question about what occupies the gap. It also distinguishes two properties your atlas needs to keep: **electrons can occupy the space between nuclei without providing a conducting path through the material.** At still higher pressure the fixed-radius packing calculation fails a numerical bound, as shown below. [pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC12401722/?utm_source=chatgpt.com)

[VOTKP_Na_to_P_evidence.zip](https://chatgpt.com/library?file_id=libfile_fde3_f-4d8a5faa18a8819188efa44149716693_ea4e520c657081918696167b9513e64f) contains **65 successive ionization energies, all 64 defined adjacent reflections, uncertainties, reversed signs, 112 nuclear records, updated charge radii, ionic-radius tables, and 83 candidate diffraction records**. The five ionization ladders are complete through the bare nuclei. The diffraction collection has wider coverage than the selected phases below, but does not establish a complete census of every metastable phase or a physical nearest-neighbour distance for each one.

## 1. What was tested

I started from your November element and screening notes, your archived threshold data, and your per-element space ledger. I used the six recovered moving-ball folders for the meanings of the face, gap, travelling link, occupied projector and tree rung. All 65 ionization energies in your archive matched the separately distributed Mendeleev ionization table at the stored central values. Both draw on NIST, so that agreement checks transcription. I used the 2022 atomic-negative-ion evaluation for the four bound anions. I ran exact rational wall classifications on the encoded decimals and numerical uncertainty checks. **This batch has no new Lean certificate.** [Element source](https://github.com/dicipler-pixel/votkp-lean/tree/74125d2977809c90d459ab7441a6726d1348962f/research/2026-11-11-standard-model-ball/elements) · [Moving-ball source](https://github.com/dicipler-pixel/votkp-lean/tree/a60a000dc41e21be6f1cca3ff9197595a3819ade/research) · [Space ledger](https://github.com/dicipler-pixel/votkp-lean/blob/74125d2977809c90d459ab7441a6726d1348962f/research/2026-11-13-space-step/per_element.csv). [physics.nist.gov](https://physics.nist.gov/cgi-bin/ASD/ie.pl?spectra=Na\&utm_source=chatgpt.com)

| Status | Claim | Condition that would defeat it |
|---|---|---|
| **RECOGNISED**, prediction already in your note | The Na-like core opening crosses the forward wall from Na to Mg. | Either evaluated ratio lands on the opposite side. |
| **RECOGNISED**, prediction already in your note | The largest ordinary ionization step opens a closed core. | A larger ordinary step occurs elsewhere on the same element’s ladder. Adding anion detachment changes the domain and requires a second test. |
| **DERIVED**, uncertainty test | Silicon’s encoded anion rung is outside the wall. | Allow each threshold to vary through its quoted uncertainty. If the resulting interval reaches \(1/\sqrt2\), the side is unresolved at that uncertainty scale. |
| **HYPOTHESIS**, physical test | A fixed neutral-atom sphere represents occupied volume as the sample is compressed. | The assigned sphere exceeds the measured volume available per atom, so \(f>1\). |
| **HYPOTHESIS**, connection test | Interstitial electron accumulation is sufficient for bulk conduction. | Interstitial localization coexists with insulating behaviour. |
| **HYPOTHESIS**, light and direction | Two paths in one tree retain a direction-sensitive record. | Specify an observable, a reversal, and a predicted change before comparing paths. If the change disappears within uncertainty, that directional prediction fails. |

## 2. VOTKP v2 · The directed ladders

**DERIVED.** I retained your four distinct quantities:
\[
I_0=\mathrm{EA},\qquad z_k=\frac{I_{k+1}}{I_k},\qquad
r_k=\ln z_k,\qquad
\Gamma_k=\frac{I_{k+1}-I_k}{I_{k+1}+I_k}.
\]
Reversing the ordered pair sends \(r_k\to-r_k\) and \(\Gamma_k\to-\Gamma_k\), while preserving \(\Gamma_k^2\). The equal-face wall is \(\Gamma^2=1/2\). For the forward ratios here, outside means \(z>3+2\sqrt2=5.828427\ldots\). For a reversed ratio the corresponding outside branch is \(z<3-2\sqrt2\). The CSV at the end shows every forward pair; the download also gives every \(r_k\) and reversed \(\Gamma_k\).

### Three boundaries per element

**DERIVED from evaluated thresholds.** Each entry gives \(z,\Gamma\). “L opens” compares the last \(3s\) removal from a Na-like ion with the first \(2p\) removal from the Ne-like ion it leaves. “K opens” compares the last \(2s\) removal from a Li-like ion with the first \(1s\) removal from the He-like ion it leaves. These are physical labels for the two steps, independent of which ratio is larger. [physics.nist.gov](https://physics.nist.gov/cgi-bin/ASD/ie.pl?spectra=Na\&utm_source=chatgpt.com)

| Element | Anion rung \(k=0\) | L opens, \(k=Z-10\) | K opens, \(k=Z-2\) | Largest ordinary step | Largest step including rung 0 |
|---|---|---|---|---|---|
| Na | **9.37914, .80731 outside** | **9.20133, .80395 outside** | 4.88601, .66021 inside | L | Anion |
| Mg | **No bound ground-state atomic anion** | 5.33037, .68406 inside | 4.79417, .65483 inside | L | L |
| Al | **13.82938, .86513 outside** | 4.21801, .61671 inside | 4.71935, .65031 inside | K | Anion |
| Si | **5.86654, .70873 outside** | 3.69429, .57395 inside | 4.65722, .64647 inside | K | Anion |
| P | **14.04575, .86707 outside** | 3.38992, .54441 inside | 4.60474, .64316 inside | K | Anion |

**DERIVED — Two findings change how to read the atlas.**

1. The strongest **ordinary** step changes identity between Mg and Al. At Mg the L opening is stronger; at Al the K opening is stronger. Both Al openings are inside the wall. The point where two openings exchange rank is a different event from a wall crossing.
2. Your original closed-core result survives for the ordinary ladder in all five cases. On the **extended** ladder, four of five maxima occur at the anion rung. Sodium is particularly informative because its two largest reflections are close: \(0.80731\) at detachment and \(0.80395\) at the L opening. Keeping the physical identity of the rung preserves a difference that a graph of peak height alone nearly hides.

### Silicon’s narrow margin

**MEASURED / evaluated.** Neutral Si has \(I_1=8.15168(3)\) eV. The recommended Si electron affinity is \(1.3895212(7)\) eV. The second number measures binding of the additional electron to an isolated atom; an electrical measurement of a silicon wafer would have different inputs. [physics.nist.gov](https://physics.nist.gov/PhysRefData/Handbook/Tables/silicontable1_a.htm?utm_source=chatgpt.com)

**DERIVED.**
\[
z_0=\frac{8.15168}{1.3895212}=5.866539,\qquad
\Gamma_0=\frac{8.15168-1.3895212}{8.15168+1.3895212}=0.70873244.
\]
The wall is \(0.70710678\). Taking the smaller \(I_1\) and larger EA for the lower endpoint, and reversing those choices for the upper endpoint, gives
\[
0.70873140\leq\Gamma_0\leq0.70873348.
\]
**Silicon stays outside throughout that sensitivity interval.** This uses one quoted uncertainty per input and makes no assumption about a joint probability distribution.

### Screening, the two hydrogenic reference values, and \(5/8\)

**DERIVED.** For an unscreened one-electron shell comparison the energy varies as \(1/n^2\). Hence
\[
z_{3\to2}=(3/2)^2=2.25,\qquad z_{2\to1}=4.
\]
Both limits lie inside your loop wall. Sodium’s L opening gives \(47.28636/5.13907696=9.20133\). Defining effective charges by \(I=\mathrm{Ry}(Z_{\rm eff}/n)^2\), this corresponds to \(Z_{\rm eff,core}/Z_{\rm eff,val}=\sqrt{9.20133/2.25}=2.0223\). Magnesium’s L opening gives \(80.1436/15.035271=5.33037\), or an effective-charge ratio of 1.5392. The wall requires \(1.6095\) for this shell pair. The change in relative screening takes the Na-like sequence through the wall between those two ions. [Your screening analysis](https://github.com/dicipler-pixel/votkp-lean/blob/74125d2977809c90d459ab7441a6726d1348962f/research/2026-11-11-standard-model-ball/elements/SHELL_AND_SCREENING_AT_THE_WALL_20261111_v1.md)

**DERIVED.** On the separate K opening, your stored screened-series formula predicts \(4.88949,4.79769,4.72306,4.66121,4.60910\) from Na through P. The encoded ratios are \(4.88601,4.79417,4.71935,4.65722,4.60474\). All five are above the hydrogenic four and below the wall. They extend the Li-like sequence from Li’s 14.02895, through carbon’s 6.07953 and nitrogen’s 5.63967, down to phosphorus’s 4.60474. [Your screened-series code](https://github.com/dicipler-pixel/votkp-lean/blob/74125d2977809c90d459ab7441a6726d1348962f/research/2026-11-11-standard-model-ball/elements/shell_screen_04.py)

**DERIVED — The last two electrons correct an extrapolation from H–Ne.** Retain both earlier readouts, \(S_Z=(I_Z-I_{Z-1})/(ZE_h)\) and \(\sigma_Z=Z-\sqrt{2I_{Z-1}/E_h}\). The former is the normalized energy gap; the latter is an effective screening charge inferred from the first K-electron removal.

| Readout | Ne, for comparison | Na | Mg | Al | Si | P |
|---|---:|---:|---:|---:|---:|---:|
| \(S_Z\) | .61148 | .61339 | .61512 | .61672 | .61823 | .61968 |
| \(\sigma_Z\) | .62502 | **.62297** | .62062 | .61790 | .61476 | .61115 |
| Final \(\Gamma_{Z-1}\) | .06505 | .05896 | .05393 | .04969 | .04608 | .04297 |

For example, sodium gives \(S_{11}=(1648.702285-1465.0992)/(11\times27.21138625)=0.61339\). **Neon’s \(\sigma\simeq0.62502\) was a crossing near \(5/8\). The next five values continue below it.** The observation through Ne that the two readouts approached \(5/8\) from opposite sides held on that interval. Extending it as a monotonic law fails at Na. The leading \(5/8\) coefficient in the nonrelativistic screened series and the finite-\(Z\) effective charge extracted from evaluated thresholds have different meanings. The highly charged thresholds used here are theoretical NIST entries. [CODATA energy unit](https://physics.nist.gov/cgi-bin/cuu/Value?hrev). [physics.nist.gov](https://physics.nist.gov/cgi-bin/ASD/ie.pl?spectra=Na\&utm_source=chatgpt.com)

## 3. Atomic traits, light and radii

**MEASURED / evaluated.** These are isolated neutral ground states. EA is in eV, and \(\alpha(0)\) is the recommended scalar static dipole polarizability in \(a_0^3\). The polarizability compilation combines measurements and calculations. The selected spectral lines are neutral-atom wavelengths in nm, rounded for identification. [2023 polarizability compilation](https://ctcp.massey.ac.nz/2023Tablepol.pdf) · [NIST atomic spectra handbook](https://physics.nist.gov/PhysRefData/Handbook/index.html). [info.phys.tsinghua.edu.cn](https://info.phys.tsinghua.edu.cn/henucl/ning/148.pdf?utm_source=chatgpt.com)

| Atom | Ground configuration and term | EA | \(\alpha(0)\) | Selected emission or absorption lines |
|---|---|---:|---:|---|
| Na | \([\mathrm{Ne}]3s,\ ^2S_{1/2}\) | 0.547926(25) | 162.7(5) | 588.995 and 589.592, yellow D doublet |
| Mg | \([\mathrm{Ne}]3s^2,\ ^1S_0\) | No bound anion | 71.2(4) | 285.213 in UV; 516.73, 517.27 and 518.36 in green |
| Al | \([\mathrm{Ne}]3s^23p,\ ^2P^\circ_{1/2}\) | 0.43283(5) | 57.8(10) | 394.40 and 396.15 near the violet edge |
| Si | \([\mathrm{Ne}]3s^23p^2,\ ^3P_0\) | 1.3895212(7) | 37.3(7) | 251.61 and 288.16 in UV |
| P | \([\mathrm{Ne}]3s^23p^3,\ ^4S^\circ_{3/2}\) | 0.746609(9) | 25(1) | 213.62 and 253.57 in UV |

**RECOGNISED.** Polarizability falls at each step from Na to P; electron affinity follows a different order. Silicon binds an extra electron more strongly than phosphorus. Attachment to neutral Si leaves a half-filled \(3p^3\) anion, whereas attachment to neutral P starts from \(3p^3\) and makes \(3p^4\). This gives the period-two comparison a concrete extension: C and Si both bind the extra electron that brings them to \(p^3\). N has no bound ground-state anion, while its same-column counterpart P does. Russell’s equal-valence reading groups N and P together; the attachment measurement distinguishes them. [info.phys.tsinghua.edu.cn](https://info.phys.tsinghua.edu.cn/henucl/ning/148.pdf?utm_source=chatgpt.com)

**MEASURED / evaluated — Wall radii in pm.** A covalent radius, an effective ionic radius in a specified coordination, and a van der Waals radius answer different contact questions. The metallic column uses half the measured nearest-neighbour spacing of the ambient metal, so its convention is reproducible. The download also carries tabulated metallic-radius conventions. [Cordero covalent radii, 2008](https://doi.org/10.1039/B801115J) · [Pyykkö single-bond radii, 2009](https://doi.org/10.1002/chem.200800987) · [Bondi van der Waals radii, 1964](https://doi.org/10.1021/j100785a001) · [Main-group extension, 2009](https://doi.org/10.1021/jp8111556) · [Shannon ionic radii, 1976](https://doi.org/10.1107/S0567739476001551)

| Atom | Covalent | Radius in your space calculation | van der Waals | Ambient metallic contact radius, derived | Effective ionic example |
|---|---:|---:|---:|---:|---|
| Na | 166 | 155 | 227 | 185.8, bcc | \(\mathrm{Na}^+\), CN6, 102 |
| Mg | 141 | 139 | 173 | 159.8, shortest hcp contact | \(\mathrm{Mg}^{2+}\), CN6, 72 |
| Al | 121 | 126 | 184, extended table | 143.2, fcc | \(\mathrm{Al}^{3+}\), CN6, 53.5 |
| Si | 111 | 116 | 210 | Ambient solid is covalent | \(\mathrm{Si}^{4+}\), CN4, 26 |
| P | 107 | 111 | 180 | Phase-specific covalent contacts | \(\mathrm P^{5+}\), CN4, 17 |

## 4. The five elements in the ball and knot frameworks

**HYPOTHESIS — Common mapping.** The nucleus sits at the centre. In the outside view, the atomic wall, neighbouring wall and intervening material define a possible connection. In the light’s view, the tree has a parent face, a stretch and a child face. A clock mismatch at the junction is a ratio between specified cells. The measured atomic peel supplies a ratio between successive **thresholds of one ion**. None of the five bulk phases below has an independently measured clock pair identified with its atomic \(z_k\). Your code also has a distinct connection test on the weakest gap link of an occupied-state projector. No element-specific \(P_{ij}\) was supplied or calculated here. [Tree definition](https://github.com/dicipler-pixel/votkp-lean/tree/a60a000dc41e21be6f1cca3ff9197595a3819ade/research/the-ball-is-the-tree) · [Projector definition](https://github.com/dicipler-pixel/votkp-lean/tree/a60a000dc41e21be6f1cca3ff9197595a3819ade/research/hydrogen-in-the-space-between)

**DERIVED — Your geometrical third.** I used \(f=4\pi r_{\rm cov}^3/(3V_{\rm atom})\). The first four rows are in your ledger. Black P is an extension using the eight-atom orthorhombic cell and the same radius convention. This \(f\) is an assigned sphere-volume fraction. The symmetric Bruggeman threshold requires the fraction of a conducting constituent; your projector test requires link weights. Their material inputs still have to be identified. [Your space ledger](https://github.com/dicipler-pixel/votkp-lean/blob/74125d2977809c90d459ab7441a6726d1348962f/research/2026-11-13-space-step/per_element.csv) · [Black-P diffraction record](https://www.crystallography.net/cod/9012486.html)

| Element and phase | \(V_{\rm atom}\), Å³ | \(f\) | Geometrical side of \(1/3\) | V1 · isolated-atom knot assignment | V2 · outside atomic rungs |
|---|---:|---:|---|---|---|
| Na, bcc | 39.438 | 0.39552 | Above | **None found** | Anion and L opening |
| Mg, hcp | 23.222 | 0.48444 | Above | **None found** | None |
| Al, fcc | 16.594 | 0.50494 | Above | **None found** | Anion |
| Si, diamond cubic | 20.016 | 0.32666 | Below | **None found** | Anion, narrowly |
| P, black | 18.972 | 0.30195 | Below | **None found** | Anion |

**HYPOTHESIS — V1 test across all five.** Your volume polynomial needs a specified knot and a set of geometries. Neither an fcc cell, a puckered sheet, a tetrahedral cage, nor a closed walk selected after seeing the data fixes a unique ambient-isotopy class. A testable construction would choose the physical path, its closure and its orientation before comparing HOMFLY, coloured Jones, Alexander or your volume polynomial with a measured phase volume. No such element-specific construction turned up for these five in the checked material. [Your volume-polynomial paper](https://zenodo.org/records/24040319)

### 11 · Sodium — what is in the gap, and can it carry charge?

**MEASURED / DERIVED.** Ambient Na is a silvery bcc metal. A 293 K diffraction record gives \(a=4.2906\) Å, hence eight nearest neighbours at \(d=\sqrt3\,a/2=3.7158\) Å. A 5 K refinement records a close-packed hexagonal structure with \(a=3.767,\ c=6.154\) Å. Near room temperature the density is about 0.968 g/cm³, the thermal conductivity about 140–142 W m\(^{-1}\) K\(^{-1}\), and resistivity about \(4.8\times10^{-8}\ \Omega\mathrm m\), or conductivity near \(2.1\times10^7\) S/m. It melts near 370.94 K and boils near 1156 K at atmospheric pressure. The yellow D doublet belongs to excited or absorbing atomic sodium; bulk metal is silvery. [293 K cell](https://www.crystallography.net/cod/9008545.html) · [5 K cell](https://www.crystallography.net/cod/9011000.html). [webelements.com](https://www.webelements.com/sodium/physics.html?utm_source=chatgpt.com)

**MEASURED.** Pressure takes Na through several structures, including fcc, cI16, oP8, a host–guest regime and transparent hP4. The 2025 single-crystal work measured \(a=2.9028(5),c=4.1386(3)\) Å at 223 GPa and found diffraction evidence favouring interstitial electron localization. At 310 GPa it measured \(a=2.8132(6),c=3.8759(11)\) Å and **6.641(3) Å³ per atom**. A theoretical study estimated a peak superconducting \(T_c\) near 1.2 K for cI16; I found no experimental confirmation of that predicted value. [pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC12401722/?utm_source=chatgpt.com)

**DERIVED — A failure worth preserving.** Holding the ordinary sodium radius at 1.55 Å gives an assigned ball volume of \(4\pi(1.55)^3/3=15.60\) Å³. At ambient pressure \(15.60/39.44=0.396\). At 310 GPa the same operation gives **\(15.60/6.641=2.35\)**. A literal occupied fraction cannot reach 235%. The fixed-radius interpretation fails under this compression. Its failure identifies a measurable question for your model: how does the electronic wall or occupied-state connectivity change as interstitial density localizes?

### 12 · Magnesium — metallic conduction with no outside atomic rung

**MEASURED / DERIVED.** Ambient Mg is a silvery hcp metal. The 1949 measurement at 298.15 K gives \(a=3.2093,\ c=5.2103\) Å. Six same-plane neighbours are 3.2093 Å away. The six adjacent-plane contacts are slightly shorter,
\[
\sqrt{a^2/3+c^2/4}=3.1969\ {\rm Å}.
\]
That small difference supplies two physically distinguishable paths before any light-transfer model is imposed. Representative near-room-temperature values are 1.74 g/cm³, 156 W m\(^{-1}\) K\(^{-1}\), and \(1/(4.39\times10^{-8})=2.28\times10^7\) S/m using your ledger’s resistivity. Mg melts near 923 K and boils near 1363 K. Its isolated-atom green triplet and its bulk metallic reflectance are separate optical observations. [Ambient Mg cell](https://www.crystallography.net/cod/9012001.html). [International Magnesium Association](https://www.intlmag.org/page/basics_phys_prop_ima?utm_source=chatgpt.com)

**MEASURED.** A high-pressure bcc refinement gives \(a=2.953\) Å, \(d=2.557\) Å. At much greater pressure, diffraction records a distorted bcc-like regime and an \(Fmmm\) assignment near 0.56 TPa with \(a=2.58,\ b=2.91,\ c=3.35\) Å. At 0.96 TPa two peaks are consistent with simple hexagonal Mg, \(a=1.87(1), c=1.63(1)\) Å; under that assignment the shortest contact is 1.63 Å. At 1.32 TPa the simple-cubic interpretation gives \(a=d=1.60(1)\) Å. The limited number of peaks constrains how confidently the structures can be identified. A low-temperature experiment cooled elemental Mg to millikelvin temperatures without observing a superconducting transition under its test conditions. [bcc Mg record](https://www.crystallography.net/cod/1538898.html). [pure.ed.ac.uk](https://www.pure.ed.ac.uk/ws/portalfiles/portal/301689200/Mg_nature_phys_resub_resub.pdf?utm_source=chatgpt.com)

**HYPOTHESIS — Magnesium test.** Mg has no bound anion and **every defined atomic rung is inside**, yet the solid conducts well. That single element defeats a proposed requirement that an outside atomic rung must exist before charge can move through a material. An occupied-link version of your hypothesis survives this test and has a sharper task: predict the directional response of the hcp metal from its occupied links.

### 13 · Aluminium — the K opening overtakes the L opening

**MEASURED / DERIVED.** Neutral Al ionizes at 5.985769 eV, below Mg’s 7.646236 eV despite the extra proton. The exposed neutral electron has changed from \(3s\) in Mg to \(3p\) in Al. Conversely, the *second* removal costs 18.82855 eV in Al and 15.035271 eV in Mg. The order reverses when the charge state changes. This is the third-period counterpart of the Be–B first-ionization reversal. [physics.nist.gov](https://physics.nist.gov/cgi-bin/ASD/ie.pl?spectra=Mg\&utm_source=chatgpt.com)

**MEASURED / DERIVED.** Ambient Al is silvery fcc. At 298.15 K the 1949 measurement gives \(a=4.04961\) Å and twelve neighbours at \(a/\sqrt2=2.86351\) Å. Representative bulk values are 2.70 g/cm³, about 237 W m\(^{-1}\) K\(^{-1}\), and \(1/(2.65\times10^{-8})=3.77\times10^7\) S/m using your ledger. It melts at about 933.47 K and boils around 2792 K. Pure bulk Al superconducts near **1.18 K** at zero applied pressure. An experiment under pressure measured a reduction to **0.075 K at 62 kbar**. Compression can suppress the transition even while the metal remains a conductor. [Ambient Al cell](https://www.crystallography.net/cod/9012002.html). [pdg.lbl.gov](https://pdg.lbl.gov/2025/download/db2024.pdf?utm_source=chatgpt.com)

**MEASURED.** Ramp-compression diffraction observed fcc→hcp at \(216\pm9\) GPa and hcp→bcc at \(321\pm12\) GPa, with bcc persisting to 475 GPa. A 2024 molecular-dynamics shock study obtained lower, orientation-dependent transition stresses along its simulated paths. Those are separate protocols and evidence grades. [osti.gov](https://www.osti.gov/servlets/purl/1405327?utm_source=chatgpt.com)

**HYPOTHESIS — Aluminium test.** Use pure Al above and below its measured \(T_c\). Its elemental identity and isolated-atom peel ladder are common to both observations. A bulk law driven solely by that ladder cannot select the transition temperature. A model that includes the neighbour couplings and a declared thermal bath can make a temperature-dependent prediction. The fact that pressure *lowers* the measured \(T_c\) gives that prediction a sign to get right.

### 14 · Silicon — the narrow atomic wall and a sample-dependent bulk response

**MEASURED / DERIVED.** Ordinary crystalline Si is diamond cubic, with \(a=5.430941\) Å at 298.15 K in the 1975 precision measurement. Its four tetrahedral neighbours are \(a\sqrt3/4=2.35167\) Å away. Representative values are 2.3296 g/cm³, about 149 W m\(^{-1}\) K\(^{-1}\), melting near 1687 K and boiling near 3538 K. Bulk crystalline silicon is dark grey with a reflective surface. Its room-temperature indirect band gap of about 1.12 eV gives a characteristic wavelength of \(1240/1.12\simeq1107\) nm, distinct from its atomic UV lines. [Precision cell](https://www.crystallography.net/cod/9011998.html). [pdg.lbl.gov](https://pdg.lbl.gov/2025/download/db2024.pdf?utm_source=chatgpt.com)

**MEASURED — A material correction for the ledger.** Your space ledger gives silicon resistivity \(0.001\ \Omega\mathrm m\). A reference for **intrinsic** Si at 300 K gives \(2.3\times10^5\ \Omega\mathrm{cm}=2.3\times10^3\ \Omega\mathrm m\), corresponding to \(4.35\times10^{-4}\) S/m. The difference is a factor of roughly 2.3 million. I retained your ledger value with its original provenance. A quantitative transport comparison needs sample doping, temperature and carrier concentration before using that row. This matters especially because the calculated packing fraction, 0.32666, is close to one third. [www-pub.iaea.org](https://www-pub.iaea.org/MTCD/Publications/PDF/TE_1681_web.pdf?utm_source=chatgpt.com)

**MEASURED / evaluated — One element supplies a family of rooms.** The 2026 IUCr study gives phase-specific structures. Representative cells are below, in Å. Its table distinguishes directly reported and extrapolated parameters and gives the state conditions. The downloadable COD records supply additional dated refinements and recalculated site distances. [journals.iucr.org](https://journals.iucr.org/b/issues/2026/03/00/tq5036/index.html?utm_source=chatgpt.com)

| Si structure | Representative cell or contact |
|---|---|
| Si-I, diamond | \(a=5.431\), nearest 2.352 |
| Si-II, \(\beta\)-Sn type | \(a=4.760,\ c=2.636\), low-pressure extrapolation in the review |
| Si-III, BC8 | \(a=6.6276\); a separate 2016 refinement at \(a=6.6218\) gives shortest model contact 2.363 |
| Si-IV, hexagonal family | 4H example \(a=3.837,\ c=12.520\); stacking period matters across 2H, 4H and 6H |
| Si-XII, R8 | \(a=5.720,\ \alpha=109.95^\circ\) at 2 GPa |
| Si-V, simple hexagonal | \(a=2.553,\ c=2.382\) at 15.4 GPa; shortest contact 2.382 |
| Si-VI, orthorhombic | \(8.0242\times4.7961\times4.776\) at 38.4 GPa; shortest refined contact about 2.335 |
| High-pressure hcp and fcc | hcp \(a=2.444,\ c=4.152\) at 43 GPa; fcc \(a=3.34\), nearest 2.362, at 87 GPa |
| Open frameworks | \(\mathrm{Si}_{24}\): \(3.8246\times10.700\times12.648\); \(\mathrm{Si}_{136}\): cubic \(a=14.62\) |

**MEASURED / HYPOTHESIS.** Simple-hexagonal silicon showed superconductivity at **8.2 K and 15 GPa**. This gives your framework an unusually clean comparison between ordinary diamond Si and a conducting, superconducting pressure phase of the same element. A rule assigning bulk behaviour from the near-wall anion rung alone would assign the same value to both. A path-based model must say how the altered contacts change the transmitted response. [journals.aps.org](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.54.2375?utm_source=chatgpt.com)

### 15 · Phosphorus — one peel ladder, molecular cages and directional sheets

**MEASURED.** White phosphorus consists of discrete \(\mathrm P_4\) molecules. Red phosphorus includes networks whose ordering varies with preparation. Violet phosphorus is crystalline, and black phosphorus has puckered covalent sheets. The density and thermal transitions therefore need an allotrope label. White P is about 1.82 g/cm³, melts near 317.3 K and boils near 554 K at atmospheric pressure. The black-P cell below implies about 2.71 g/cm³ from eight P atoms per cell. A single melting/boiling pair applied to every phosphorus allotrope would erase transformations on heating. [Black-P cell](https://www.crystallography.net/cod/9012486.html) · [Violet-P cell](https://www.crystallography.net/cod/1569356.html). [nist.gov](https://www.nist.gov/publications/phase-transition-temperatures-solid-elements-atmospheric-pressure?utm_source=chatgpt.com)

**MEASURED / DERIVED.** The black-P refinement gives \(a=3.3133,\ b=10.473,\ c=4.374\) Å, with a shortest refined P–P contact near 2.223 Å. A 2023 violet-P refinement at 300 K gives \(a=9.1997,\ b=9.1235,\ c=21.9062\) Å, \(\beta=97.727^\circ\). A 2023 white-P polymorph refinement at 100 K gives \(18.302\times18.302\times36.441\) Å. In white P the shortest P–P contact is **inside the molecule**. In black P it is a covalent sheet bond. Neither distance, used alone, measures the gap to the next layer or molecule. Under further compression there are rhombohedral, cubic-related, incommensurately modulated, simple-hexagonal and denser phases. In particular, the high-pressure phase once described as bcc was subsequently assigned a cI16 superstructure. [White-P structure](https://www.crystallography.net/cod/1570230.html). [rsc.org](https://www.rsc.org/suppdata/c8/cc/c8cc03013h/c8cc03013h1.pdf?utm_source=chatgpt.com)

**MEASURED — Three paths through one sample.** Room-temperature measurements on passivated black phosphorus found thermal conductivities of **\(86\pm8\)** along zigzag, **\(34\pm4\)** along armchair, and **\(4.0\pm0.5\)** W m\(^{-1}\) K\(^{-1}\) through the layers. A separate historical p-type polycrystalline specimen had room-temperature resistivity around \(1\ \Omega\mathrm{cm}\), or conductivity of order \(100\) S/m. Under pressure, elemental P has shown \(T_c\) around 9.5 K near 32 GPa on a reported experimental path. A 2026 study further examined the dependence of pressure-induced transitions and superconductivity on thickness. [osti.gov](https://www.osti.gov/servlets/purl/1386280?utm_source=chatgpt.com)

**HYPOTHESIS — Phosphorus gives the clearest Two Trees experiment in this batch.** Use the same oriented black-P specimen and compare zigzag and armchair paths at fixed thickness, temperature and excitation. Their measured heat-transport ratio is about \(86/34=2.53\). This tests **axis dependence**. A second measurement reversing propagation along a single axis tests **sign under reversal**. Those experiments ask different questions. Russell’s proposed parallel/opposed-flow rule or a chirality claim would need a predicted reversal-odd observable. The 2.53 ratio alone establishes only anisotropy. A third path through the sheets measures the much larger interlayer suppression.

## 5. Standard Model ball · What the centre keeps during the peel

**DERIVED.** For isotope \(^{A}X\) the centre retains \(Z\) protons and \(A-Z\) neutrons through ordinary electronic ionization. The net valence-flavour counts are \(u=A+Z\) and \(d=2A-Z\). Thus \(^{23}\mathrm{Na}\) carries \(11p,12n;34u,35d\); \(^{24}\mathrm{Mg}\) carries \(12p,12n;36u,36d\); \(^{27}\mathrm{Al}\) carries \(13p,14n;40u,41d\); \(^{28}\mathrm{Si}\) carries \(14p,14n;42u,42d\); and \(^{31}\mathrm P\) carries \(15p,16n;46u,47d\). These are net flavour counts. The measured nuclear charge radius is the size of the central charge distribution and has units of fm. The electronic wall radii above have units of pm.

**MEASURED / evaluated.** The naturally abundant stable nuclei are listed below. Magnetic moments are rounded in nuclear magnetons. The two radius columns deliberately retain the older IAEA snapshot and Ohayon’s 2025 reevaluation, which revisited uncertainty from the nuclear charge distribution. Blank entries in the last column mean that isotope has no separate reference value in the cited Table 2. The evidence package includes available unstable-isotope entries and their qualifications. [IAEA evaluated data](https://nds.iaea.org/relnsd/v1/data?fields=ground_states&nuclides=all) · [CIAAW isotope abundances](https://ciaaw.org/isotopic-abundances.htm). [arxiv.org](https://arxiv.org/pdf/2409.08193?utm_source=chatgpt.com)

| Isotope | Ground \(I^\pi\) | \(\mu/\mu_N\), rounded | Earlier rms charge radius, fm | 2025 reference radius, fm |
|---|---:|---:|---:|---:|
| \(^{23}\mathrm{Na}\) | \(3/2^+\) | +2.218 | 2.9936(21) | **2.992(6)** |
| \(^{24}\mathrm{Mg}\) | \(0^+\) | 0 | 3.0570(16) | **3.056(3)** |
| \(^{25}\mathrm{Mg}\) | \(5/2^+\) | −0.855 | 3.0284(22) | — |
| \(^{26}\mathrm{Mg}\) | \(0^+\) | 0 | 3.0337(18) | **3.030(3)** |
| \(^{27}\mathrm{Al}\) | \(5/2^+\) | +3.641 | 3.0610(31) | **3.061(3)** |
| \(^{28}\mathrm{Si}\) | \(0^+\) | 0 | 3.1224(24) | **3.123(3)** |
| \(^{29}\mathrm{Si}\) | \(1/2^+\) | −0.555 | 3.1176(52) | — |
| \(^{30}\mathrm{Si}\) | \(0^+\) | 0 | 3.1336(40) | — |
| \(^{31}\mathrm P\) | \(1/2^+\) | +1.13 | 3.1889(19) | **3.190(3)** |

**MEASURED — Recent isotope work adds information the snapshot misses.** The 2024 silicon laser-spectroscopy study obtained \(r_c(^{32}\mathrm{Si})=3.153(12)\) fm. A later Al analysis gives \(r_c(^{26m}\mathrm{Al})=3.132(10)\) fm. The superscript \(m\) matters because this datum belongs to an isomer. The IAEA raw export also places nonzero magnetic entries beside some definite spin-zero ground-state records. The derived table sets ground-state magnetic dipoles to zero for definite \(J=0\) and retains the raw records separately. [pureportal.spbu.ru](https://pureportal.spbu.ru/files/119334760/2024_Si_radius.pdf?utm_source=chatgpt.com)

## 6. Running comparisons and claims set aside

- **RECOGNISED — Across all fifteen elements.** H, Li, B, C, O, F, Na, Al, Si and P have a bound isolated ground-state anion. He, Be, N, Ne and Mg do not. Among the ten bound cases, **fluorine alone has an inside rung 0**. Silicon is the nearest outside case to the wall. This pattern is a finite census through P. [info.phys.tsinghua.edu.cn](https://info.phys.tsinghua.edu.cn/henucl/ning/148.pdf?utm_source=chatgpt.com)
- **DERIVED — The Na-like isoelectronic sequence.** \(\mathrm{Na},\mathrm{Mg}^+,\mathrm{Al}^{2+},\mathrm{Si}^{3+},\mathrm P^{4+}\) each start with eleven electrons. Their last \(3s\)-removal energies rise through **5.13908, 15.03527, 28.44764, 45.14179 and 65.02511 eV**. The corresponding first \(2p\)-removal energies also rise, while the ratio falls at every element. The absolute binding strengthens even as your normalized reflection weakens. [physics.nist.gov](https://physics.nist.gov/cgi-bin/ASD/ie.pl?spectra=Na\&utm_source=chatgpt.com)
- **RECOGNISED — Across periods.** Li and Na both have an outside first core opening. Be and Mg both lack a bound atomic anion, but Be’s first core opening is outside and Mg’s is inside. B and Al have strong outside anion rungs. C and Si both bind toward a half-filled \(p^3\) configuration, but Si lands much nearer the wall. N and P share a neutral \(p^3\) term pattern yet disagree on whether an extra electron binds. The directed atlas resolves distinctions hidden by a valence-only octave.
- **HYPOTHESIS — “The vector determines the direction, that may be decay.”** Reversal of ordered thresholds gives an exact odd amplitude and even squared amplitude. Turning this into a prediction about light propagation, a nuclear decay direction or a material current requires an independently specified preparation and observable. The black-P axis and reversal experiments make that distinction experimentally accessible.
- **Mainstream-blend watch.** The \(\ln z\) steps are intrinsic and dimensionless. The Ångström spacings come from crystallography. The resistivities come from particular materials and states. No spacetime metric or conversion from a peel step to crystal distance was introduced.
- **Set aside, with why.** The fixed-radius sodium packing fraction fails under extreme compression. An outside-rung requirement for conduction fails on Mg. Extrapolation of the apparent H–Ne effective-charge approach to \(5/8\) fails at Na. An intrinsic-silicon transport comparison using the unlabeled ledger resistivity is unresolved. A full phase-by-phase catalogue of measured neighbour distances, phase-specific transport, atomic knot assignments, neighbouring clock ratios and elemental \(P_{ij}\) remains incomplete. Some COD candidate rows refer to compounds despite elemental search metadata; the archive flags examples so they can be excluded.

## 7. Full peel CSV

**MEASURED / evaluated input; DERIVED ratios.** At \(k=0\), the energy column holds EA. `EA22` denotes the 2022 anion evaluation. The blank Mg value means no bound ground-state anion. `E`, `S` and `T` are the original NIST-archive grades for an evaluated unbracketed, semiempirical and theoretical threshold respectively. Each ratio uses the energy on its row and the next energy of the same element. The final energy takes the ion to its bare nucleus. Values of \(z\) and \(\Gamma\) below are rounded to five decimals; the side tests used the encoded thresholds before rounding.

```csv
Z,symbol,k,IE_k (eV),z_k,Gamma_k,source
11,Na,0,0.547926,9.37914,0.80731,EA22
11,Na,1,5.13907696,9.20133,0.80395,E
11,Na,2,47.28636,1.51460,0.20465,E
11,Na,3,71.62,1.38140,0.16016,S
11,Na,4,98.936,1.39892,0.16629,S
11,Na,5,138.404,1.24440,0.10889,E
11,Na,6,172.23,1.21061,0.09527,S
11,Na,7,208.504,1.26708,0.11781,S
11,Na,8,264.192,1.13499,0.06323,S
11,Na,9,299.856,4.88601,0.66021,T
11,Na,10,1465.0992,1.12532,0.05896,T
11,Na,11,1648.702285,,,T
12,Mg,0,,,,EA22
12,Mg,1,7.646236,1.96636,0.32577,E
12,Mg,2,15.035271,5.33037,0.68406,E
12,Mg,3,80.1436,1.36337,0.15375,E
12,Mg,4,109.2654,1.29346,0.12800,S
12,Mg,5,141.33,1.32145,0.13847,S
12,Mg,6,186.76,1.20486,0.09291,S
12,Mg,7,225.02,1.18178,0.08332,S
12,Mg,8,265.924,1.23340,0.10450,S
12,Mg,9,327.99,1.12043,0.05679,S
12,Mg,10,367.489,4.79417,0.65483,T
12,Mg,11,1761.8049,1.11401,0.05393,T
12,Mg,12,1962.663889,,,T
13,Al,0,0.43283,13.82938,0.86513,EA22
13,Al,1,5.985769,3.14555,0.51756,E
13,Al,2,18.82855,1.51088,0.20347,E
13,Al,3,28.447642,4.21801,0.61671,E
13,Al,4,119.9924,1.28196,0.12356,E
13,Al,5,153.8252,1.23835,0.10649,S
13,Al,6,190.49,1.26915,0.11861,S
13,Al,7,241.76,1.17737,0.08146,S
13,Al,8,284.64,1.16010,0.07412,S
13,Al,9,330.21,1.20726,0.09390,S
13,Al,10,398.65,1.10875,0.05157,S
13,Al,11,442.005,4.71935,0.65031,T
13,Al,12,2085.97693,1.10459,0.04969,T
13,Al,13,2304.140359,,,T
14,Si,0,1.3895212,5.86654,0.70873,EA22
14,Si,1,8.15168,2.00521,0.33449,E
14,Si,2,16.34585,2.04902,0.34405,E
14,Si,3,33.493,1.34780,0.14814,E
14,Si,4,45.14179,3.69429,0.57395,E
14,Si,5,166.767,1.23093,0.10351,E
14,Si,6,205.279,1.20115,0.09138,S
14,Si,7,246.57,1.23125,0.10364,S
14,Si,8,303.59,1.15709,0.07282,S
14,Si,9,351.28,1.14262,0.06656,S
14,Si,10,401.38,1.18659,0.08533,S
14,Si,11,476.273,1.09898,0.04716,S
14,Si,12,523.415,4.65722,0.64647,T
14,Si,13,2437.65805,1.09662,0.04608,T
14,Si,14,2673.177958,,,T
15,P,0,0.746609,14.04575,0.86707,EA22
15,P,1,10.486686,1.88520,0.30681,E
15,P,2,19.76949,1.52774,0.20878,S
15,P,3,30.20264,1.70329,0.26016,E
15,P,4,51.44387,1.26400,0.11661,E
15,P,5,65.02511,3.38992,0.54441,E
15,P,6,220.43,1.19571,0.08913,S
15,P,7,263.57,1.17464,0.08031,S
15,P,8,309.6,1.20255,0.09196,S
15,P,9,372.31,1.13991,0.06538,S
15,P,10,424.4,1.12969,0.06090,S
15,P,11,479.44,1.16932,0.07805,S
15,P,12,560.62,1.09119,0.04361,S
15,P,13,611.741,4.60474,0.64316,T
15,P,14,2816.90868,1.08979,0.04297,T
15,P,15,3069.842145,,,T
```

**Source list.** [Beasley’s element and core-opening work](https://github.com/dicipler-pixel/votkp-lean/tree/74125d2977809c90d459ab7441a6726d1348962f/research/2026-11-11-standard-model-ball/elements) · [Moving matrix of balls](https://github.com/dicipler-pixel/votkp-lean/tree/a60a000dc41e21be6f1cca3ff9197595a3819ade/research) · [VOTKP v2.9](https://doi.org/10.5281/zenodo.23340757) · [Volume of the Knot Potential](https://zenodo.org/records/24040319) · [NIST ASD](https://doi.org/10.18434/T4W30F) · [Atomic electron affinities](https://doi.org/10.1063/5.0080243) · [NIST 2025 phase evaluation](https://doi.org/10.6028/NIST.TN.2312) · [Crystallography Open Database](https://www.crystallography.net/cod/) · [2025 nuclear-radius reevaluation](https://doi.org/10.1016/j.adt.2025.101732) · [2025 dense sodium diffraction](https://pmc.ncbi.nlm.nih.gov/articles/PMC12401722/) · [2026 silicon phase tables](https://journals.iucr.org/b/issues/2026/03/00/tq5036/index.html) · [2026 pressure and thickness study of black phosphorus](https://doi.org/10.1021/acs.nanolett.6c01210).