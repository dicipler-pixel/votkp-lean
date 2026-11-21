Jeromie, the coordination-normalised cutoff **passes half-filled bcc sodium, fails a dilute metallic band, and passes a filled-band insulator**. It measures something quite specific: how much of a site’s off-site projector weight reaches its nearest neighbours. As a stand-alone test of bulk conduction, it fails in both directions.

For **β-Mn**, I found a screw orbit whose successive steps are actual shortest Mn–Mn contacts. Its natural one-cell torus closure gives an **unknot for both crystal hands**. But the same four-site path gives a signed geometric reading that flips under spatial mirroring and **stays the same when the path is traversed backwards**. That supplies the distinction your Russell test needed.

For **Fe–Zn**, I checked the energy array against `cae5f49` before producing the CSV. **140 of 140 ordinary ionization energies matched. Differences: none.** All **135 ordinary steps are inside** the wall. The four bound-anion steps, Fe, Co, Ni and Cu, are outside. Zn has no bound isolated ground-state anion. The appendix contains the generated CSV, full-precision calculations, uncertainty bounds, projector tests, 160 isotope records and 63 crystal refinements. [Fe_to_Zn_and_junction_tests.html](https://chatgpt.com/library?file_id=libfile_fde3_f-287daa9d6adc8191a60baf9fe65e2f3f_ea4e520c657081918696167b9513e64f&account_id=personal)

## 1. What the normalised junction cutoff measures

**DERIVED.** Start with your occupied projector \(P=P^\dagger=P^2\), local block \(C_i=P_{ii}\), and link weight \(X_{ij}=\|P_{ij}\|_F^2\). The available off-site weight is

\[
B_i=\operatorname{Tr}(C_i-C_i^2)=\sum_{j\ne i}X_{ij}.
\]

For \(n\) equivalent nearest neighbours and \(B_i>0\), the proposed test has an exact interpretation:

\[
X_{\rm nn}>\frac{B_i}{3n}
\quad\Longleftrightarrow\quad
\frac{\sum_{j\in {\rm nearest}}X_{ij}}{\sum_{j\ne i}X_{ij}}>\frac13.
\]

**The question it answers is “Does the first neighbour shell carry more than a third of all off-site weight?”** This is a meaningful observable in the ball picture. It distinguishes short-range concentration from weight spread over more distant shells. If the neighbours are inequivalent, the combined-shell test and a weakest-link test are different experiments. If \(B_i=0\), every off-site weight vanishes and the strict inequality fails.

### Test A · Vary the filling of the same dispersive band

**DERIVED — Failure condition fixed by the claim.** If the cutoff is necessary for metallic-band behaviour, a partially filled dispersive band must not fail it solely because the filling changes. I kept the same bcc nearest-neighbour Hamiltonian, two spin states, eight equivalent neighbours and matched junctions. Only the filling \(f\), quoted **per spin**, changed. I ran \(64^3\), \(96^3\) and \(128^3\) reciprocal grids. The table gives the \(128^3\) results.

| Filling \(f\) | \(X_{\rm nn}\) | Cutoff \(B_i/24\) | Fraction in nearest shell | Verdict |
|---:|---:|---:|---:|---|
| .01 | .000169 | .000825 | .0682 | Fails |
| .03 | .001258 | .002425 | .1729 | Fails |
| .05 | .003004 | .003958 | .2530 | Fails |
| .10 | .008752 | .007500 | .3890 | Passes |
| .20 | .020515 | .013333 | .5129 | Passes |
| .25 | .025104 | .015625 | .5356 | Passes |
| **.50, sodium valence control** | **.033290** | **.020833** | **.5326** | **Passes** |
| .75 | .025104 | .015625 | .5356 | Passes |
| .90 | .008752 | .007500 | .3890 | Passes |
| .95 | .003004 | .003958 | .2530 | Fails |
| .99 | .000169 | .000825 | .0682 | Fails |

**DERIVED — The dilute failure has an analytic explanation.** Per spin, the neighbour matrix element is an average of unit-modulus phases over the occupied region. Hence \(|P_{ij}^{(\mathrm{spin})}|\le f\), giving \(X_{ij}\le2f^2\). Meanwhile \(B_i=2f(1-f)\). Therefore

\[
\frac{nX_{\rm nn}}{B_i}\leq\frac{nf}{1-f}.
\]

For bcc, **every \(f\le1/25\) must fail** the strict one-third criterion under these assumptions. The band remains partially filled for \(0<f<1/25\). This establishes the failure independently of grid resolution. It also explains why simply lowering a fixed numerical tolerance would miss the issue.

### Test B · Fill an entire band and give it a gap

**DERIVED — Failure condition.** If passing the cutoff is sufficient for metallic-band behaviour, a fully occupied lower band separated from an empty upper band by a nonzero gap must fail. I used the same eight-neighbour geometry, alternating site energies \(+\Delta,-\Delta\), hopping \(t\), and two spins. In a two-sublattice cell,

\[
H(\mathbf k)=
\begin{pmatrix}\Delta &g(\mathbf k)\\g(\mathbf k)&-\Delta\end{pmatrix},
\qquad
E_\pm=\pm\sqrt{\Delta^2+g^2}.
\]

I filled the lower band completely. The band gap is \(2|\Delta|\). Both sublattices have the same \(B_i\), even though their on-site occupations differ.

| \(\Delta/t\) | Gap in units of \(t\) | \(X_{\rm nn}\) | Cutoff | Fraction in nearest shell | Verdict |
|---:|---:|---:|---:|---:|---|
| .1 | .2 | .033053 | .020072 | .5489 | Passes |
| 1 | 2 | .027701 | .013619 | .6780 | Passes |
| 4 | 8 | .013136 | .005047 | .8676 | Passes |
| 12 | 24 | .002944 | .001010 | .9717 | Passes |

**DERIVED.** As the gap grows, the absolute link weight **falls**, but an increasing fraction of the surviving off-site weight sits on the closest neighbours. The normalized test therefore passes *more strongly* as this model approaches its atomic limit. At zero hopping exactly, \(B_i=X_{ij}=0\) and the strict test fails. Keeping the absolute weight beside the fraction preserves that distinction.

**DERIVED — A Fe–Zn batch control.** I also ran an fcc copper-valence model with one spin-degenerate \(s\) orbital, one electron per site, matched junctions and 12 nearest neighbours. The mean link weight was .02377890, .02377878 and .02377878 on the three grids. At \(128^3\), even the weakest sampled direction was .02376935, above the cutoff \(1/72=.01388889\). This is an fcc valence-band control. The actual Cu \(d\) bands and measured resistivity were not inputs.

**HYPOTHESIS — What to retain for the paper.** Record three columns: absolute off-site weight \(B_i\), fraction carried by each neighbour shell, and a separate bulk transport response. A boundary-twist calculation with size scaling is one candidate for the third column. The first two already distinguish two concrete ways a gap region can behave: considerable weight shared widely, or very little weight concentrated nearby. A Bruggeman conducting-volume fraction remains a separate observable requiring identified constituents and their volume fractions.

## 2. β-Mn · A real screw path, its closure, and its sign

**MEASURED.** The two crystal hands have space groups \(P4_132\) and \(P4_332\); their absolute structures have been distinguished experimentally. I used the actual coordinates and symmetry operations of β-Mn refinement **COD 1539039**, cubic \(a=6.3145\) Å. This lets the knot question start from identifiable atoms and an identifiable screw operation. [β-Mn coordinates](https://www.crystallography.net/cod/1539039.html) [pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/33990329/?utm_source=chatgpt.com)

**DERIVED — Path selection.** In fractional coordinates, choose the lift

\[
g(x,y,z)=(\tfrac14-y,\ x-\tfrac14,\ z+\tfrac14).
\]

It is a quarter turn around the axis \(x=1/4,y=0\), advancing by \(c/4\). Applying it four times gives \(g^4(x,y,z)=(x,y,z+1)\). For a seed at fractional radial distance \(R\), one straight atom-to-atom step has length \(a\sqrt{2R^2+1/16}\).

| CIF seed | Fractional coordinates | Screw-step length | Physical interpretation |
|---|---|---:|---|
| Mn1 | (.061, .061, .061) | **2.374319 Å** | Matches the shortest site separation in this refinement |
| Mn2 | (.125, .206, .456) | **2.668741 Å** | A longer orbit under the same screw |

**DERIVED — Torus-knot verdict.** The four-step lift ends one unit cell above its start. It closes after imposing axial periodicity. In the resulting solid torus, a smooth helical interpolation winds once longitudinally and once meridionally. With the same upward axis and transverse frame, the mirrored path changes the meridional sign. On the standard unknotted torus in three-space the curves are \(T(1,1)\) and \(T(1,-1)\), up to the order convention. **Both are unknots.** The signed slope is well defined relative to the chosen crystal frame and axial identification. An ordinary unframed knot polynomial of this one-period closure cannot distinguish the hands.

**DERIVED — A sign that distinguishes the hands without choosing a closure.** For four consecutive orbit sites, let \(d_0,d_1,d_2\) be the three displacement vectors in a fixed right-handed laboratory frame. I computed

\[
\chi=(d_0\times d_1)\cdot d_2 .
\]

| Orbit | Original \(\chi\), Å³ | Traverse backwards | Spatial mirror |
|---|---:|---:|---:|
| Mn1 shortest-contact orbit | **+9.930608** | **+9.930608** | **−9.930608** |
| Mn2 orbit | +14.618453 | +14.618453 | −14.618453 |

**DERIVED.** A spatial mirror multiplies the determinant by \(-1\). Reversing a four-site path replaces its three displacement columns by \((-d_2,-d_1,-d_0)\); reversing their order contributes a second minus sign, so \(\chi\) survives. This is a crystallographic comparison in measured coordinates. Its sign can be recorded in the intrinsic ledger without using an ångström ruler to define a peel.

| Operation | Directed atomic peel \(\Gamma\) | β-Mn path \(\chi\) |
|---|---:|---:|
| Reverse the order of the record | Flips | Stays |
| Mirror the crystal while preserving the energy ordering | Stays for the same isolated-atom inputs | Flips |

**HYPOTHESIS — Experimental test.** Preselect the Mn1 screw orbit, the crystallographic axis, and a common right-handed laboratory convention. Compute the sign blind to the diffraction hand assignment, then compare. Failure to separate the independently assigned hands defeats that implementation. My numerical mirror check establishes the transformation law on a refinement and its mirror; it is not a blind validation on two separately measured crystals. For v1, the **framed winding and local sign** are candidates to retain. The unframed one-period knot is a useful negative control. [doi.org](https://doi.org/10.1126/sciadv.abg0868?utm_source=chatgpt.com)

## 3. Fe–Zn · Energy audit and peel ladder

**DERIVED — Audit record.** The Sc–Mn correction is **three mistyped energies, five erroneous displayed pairs, and one rounding tie**. V \(k=11\) and Cr \(k=9\) had correct ratios in the original reply. For Fe–Zn I generated one row array from the independent ASD-derived compilation, compared every ordinary energy by element and charge to the pinned archive, and then generated both the CSV and the appendix from that array. I also verified that the CSV embedded in the appendix matched the generated CSV byte for byte. [Pinned archive at `cae5f49`](https://github.com/dicipler-pixel/votkp-lean/blob/cae5f49/data/element_thresholds_20261011.json.gz) · [ASD-derived comparison database](https://github.com/lmmentel/mendeleev)

| Audit item | Result |
|---|---:|
| Ordinary input energies matched | **140 / 140** |
| Ordinary energy differences | **None** |
| Ordinary adjacent pairs | **135** |
| Bound-anion pairs | **4** |
| Defined reflections | **139** |
| Largest ordinary upper bound using opposite quoted uncertainty endpoints | **4.315376**, rounded upward |
| Smallest bound-anion lower bound | **6.2520**, Cu, rounded |
| CSV SHA-256 | `787e53a88d75ed73e4acb5ab870a8875bb25be2a73f95ea64f5adc050af57ad8` |

**DERIVED.** Classifications were calculated before rounding. The CSV uses decimal half-up to five places, with \(z=y/x\) and \(\Gamma=(y-x)/(y+x)\) evaluated separately from the underlying energies. Since \(4.315376<5.828427<6.2520\), the ordinary and bound-anion calls survive the quoted input uncertainties throughout this batch. The four affinities are external inputs from Ning and Lu; they are excluded from the 140 archive matches. [info.phys.tsinghua.edu.cn](https://info.phys.tsinghua.edu.cn/henucl/ning/148.pdf?utm_source=chatgpt.com)

### Which opening is which?

**DERIVED.** Entries are \(k;\ z,\Gamma\). The Ar-core opening across these five elements is the last \(3d\) removal followed by the first \(3p\) removal. The L and K openings retain their \(3s\to2p\) and \(2s\to1s\) labels. The bare principal-shell comparison \(16/9\) does not describe \(3d\to3p\); both orbitals have \(n=3\). [Pinned energies](https://github.com/dicipler-pixel/votkp-lean/blob/cae5f49/data/element_thresholds_20261011.json.gz) · [Atomic configurations](https://physics.nist.gov/asd)

| Element | Anion rung \(0\) | Ar-core opening | L opening | K opening |
|---|---|---|---|---|
| Fe | 51.57057, .96196 | 8; 1.54641, .21458 | 16; 2.58056, .44143 | 24; 4.31536, .62373 |
| Co | 11.90027, .84496 | 9; 1.47953, .19340 | 17; 2.55622, .43761 | 25; 4.30136, .62274 |
| Ni | 6.60108, .73688 | 10; 1.42190, .17420 | 18; 2.53715, .43457 | 26; 4.28836, .62181 |
| Cu | 6.25223, .72422 | 11; 1.38318, .16079 | 19; 2.52085, .43195 | 27; 4.27624, .62094 |
| Zn | **No bound ground-state anion** | 12; 1.34363, .14662 | 20; 2.50459, .42932 | 28; 4.26490, .62013 |

**RECOGNISED.** All five K openings remain above the bare ratio 4 and are the largest ordinary steps. All five L openings remain above \(9/4\). The Ar-core opening weakens continuously from Sc’s 2.96845 to Zn’s 1.34363. The approaching closure of the *neutral* \(3d\) subshell supplies no new large jump at this *fixed 18-electron* boundary. Those observations refer to different places on the ladder.

### Ball faces, the last pair and the \(5/8\) readings

**DERIVED.** Each apex below is \(\tanh(\ln z/4)\). The last-pair \(\Gamma\) compares the He-like and H-like ionization energies directly. \(S_Z=(h-b)/Z\) and \(\sigma_Z=Z-\sqrt{2b}\) use those energies in hartree units, as in the preceding batches. [Ball definitions](https://github.com/dicipler-pixel/votkp-lean/tree/a60a000/research/seven-balls-his-light) · [Threshold inputs](https://github.com/dicipler-pixel/votkp-lean/blob/cae5f49/data/element_thresholds_20261011.json.gz)

| Element | Anion apex | Ar apex | L apex | K apex | Last-pair \(\Gamma\) | \(S_Z\) | \(\sigma_Z\) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Fe | .7555 | .1086 | .2327 | .3501 | .024826 | .635342 | .527275 |
| Co | .5505 | .0976 | .2304 | .3494 | .023928 | .636917 | .514449 |
| Ni | .4397 | .0878 | .2286 | .3487 | .023096 | .638533 | .500562 |
| Cu | .4286 | .0809 | .2271 | .3481 | .022324 | .640189 | .485553 |
| Zn | — | .0737 | .2256 | .3475 | .021605 | .641891 | .469389 |

**DERIVED.** The trends separate further. The raw final reflection decreases; \(S_Z\) rises farther above \(5/8\); and \(\sigma_Z\) falls through \(1/2\) between Ni and Cu. The established identity \(Z(S_Z-\sigma_Z)=h-Z^2/2-\sigma_Z^2/2\) still applies. A crossing of a round number in one derived column, by itself, provides no new wall criterion.

**RECOGNISED — A limit to last batch’s fingerprint pattern.** Aligning the preceding noble core and computing its share of the total ordinary log ladder gives Fe/Ru **6.17%/5.89%**, Co/Rh **5.48%/5.22%**, Ni/Pd **4.85%/4.89%**, Cu/Ag **4.44%/4.42%**, Zn/Cd **4.11%/4.10%**. The period-5 central value now slightly **exceeds** the period-4 value for Ni/Pd. The uncertainty ranges overlap: **4.793–4.915%** for Ni and **4.721–5.070%** for Pd. The consistent decrease in the five preceding group pairs therefore should not be promoted to a strict down-column law. [Archive](https://github.com/dicipler-pixel/votkp-lean/blob/cae5f49/data/element_thresholds_20261011.json.gz)

## 4. The five elements in the framework

**MEASURED / evaluated — Atomic inputs.** Electron affinities are in eV from the 2022 evaluation. The polarizabilities are recommended scalar values in atomic units. Radii are in pm, ordered as Cordero covalent / Alvarez van der Waals / coordination-12 metallic. The ion examples use Shannon effective radii at coordination six. Spin and coordination can substantially change the ion value; the appendix lists the available alternatives. A 2025 calculation independently recommends **37.95(77)** for Zn polarizability, consistent with the tabulated approximately **38.7(3)** at this precision. [info.phys.tsinghua.edu.cn](https://info.phys.tsinghua.edu.cn/henucl/ning/148.pdf?utm_source=chatgpt.com)

| Element | Neutral configuration and term | EA | Polarizability | Covalent / vdW / metallic | Ionic example |
|---|---|---:|---:|---:|---|
| Fe | [Ar] \(3d^64s^2,\ {}^5D_4\) | .153236(34) | 62(4) | 142 / 244 / 126 | high-spin Fe²⁺ 78 |
| Co | [Ar] \(3d^74s^2,\ {}^4F_{9/2}\) | .662255(47) | 55(4) | 138 / 240 / 125 | high-spin Co²⁺ 74.5 |
| Ni | [Ar] \(3d^84s^2,\ {}^3F_4\) | 1.157368(58) | 49(3) | 124 / 240 / 124 | Ni²⁺ 69 |
| Cu | [Ar] \(3d^{10}4s,\ {}^2S_{1/2}\) | 1.23578(4) | 46.5(5) | 132 / 238 / 128 | Cu²⁺ 73 |
| Zn | [Ar] \(3d^{10}4s^2,\ {}^1S_0\) | Unbound | 38.7(3) | 122 / 239 / 134 | Zn²⁺ 74 |

**MEASURED / DERIVED — Ordinary bulk inputs.** Rounded near-room-temperature conductivities are in MS/m and W m\(^{-1}\) K\(^{-1}\). Thermal and electrical values vary with sample purity, temperature, and orientation. The last column is a site separation calculated from the cited lattice, rather than an assignment of an atomic radius to the intrinsic wall. The phase appendix retains conditions where the original records supply them. [Crystallography Open Database](https://www.crystallography.net/cod/) [nist.gov](https://www.nist.gov/publications/phase-transition-temperatures-solid-elements-atmospheric-pressure?utm_source=chatgpt.com)

| Element | Density, g/cm³ | Melt / boil, K, approx. | Electrical / thermal conductivity | Reference crystal, cell and nearest distance, Å |
|---|---:|---:|---:|---|
| Fe | 7.87 | 1811 / 3134 | ~10 / 80 | bcc \(a=2.8665;\ d=2.4825\) |
| Co | 8.86 | 1768 / 3200 | ~16 / 100 | hcp \(a=2.5071,\ c=4.0686;\ d\approx2.497\) |
| Ni | 8.90 | 1728 / 3186 | ~14.3 / 90.9 | fcc \(a=3.52387;\ d=2.492\) |
| Cu | 8.96 | 1357.77 / 2833 | ~59.6 / 401 | fcc \(a=3.61496;\ d=2.5561\) |
| Zn | 7.13 | 692.68 / 1180 | ~16.9 / 116 | hcp \(a=2.6594,\ c=4.9368;\ d=2.6594\) |

**Fe · Iron.** **DERIVED:** Fe’s small positive affinity produces the largest rung-0 reflection in this batch, .96196. The ordinary outer sequence is \(3d^64s^2\to3d^64s\to3d^6\), followed by a \(d\) removal. **MEASURED:** on heating at atmospheric pressure the bcc metal loses ferromagnetic order near 1044 K, becomes fcc near 1185 K, and returns to bcc near 1667 K before melting. Magnetic and structural boundaries are separately observable. At 61 GPa and 300 K, an \(\epsilon\)-Fe hcp refinement gives \(a=2.347,\ c=3.797\) Å. Superconductivity has been observed in compressed iron near 2 K. Neutral Fe has strong near-UV lines including approximately 371.99 nm; a polished piece of iron is metallic grey. **HYPOTHESIS / kill condition:** a ball model claiming that lattice topology alone fixes magnetic order fails if it gives the same spin state on both sides of the bcc Curie transition. Atomic v1 knot-polynomial assignment: **none found**. [α-Fe](https://www.crystallography.net/cod/9008536.html) · [ε-Fe](https://www.crystallography.net/cod/9006656.html) · [NIST Fe spectrum](https://physics.nist.gov/PhysRefData/Handbook/Tables/irontable2.htm) [srd.nist.gov](https://srd.nist.gov/jpcrdreprint/1.555761.pdf?utm_source=chatgpt.com)

**Co · Cobalt.** **MEASURED / DERIVED:** \(3d^74s^2\to3d^8\) on the first ionization. Two \(4s\) occupations disappear, while one \(3d\) occupation appears. The energy ratio at \(k=1\) is valid; a clean single-subshell path cannot be inferred from it. Cobalt repeats the rearrangement seen in V. Ambient cobalt is a silver-grey, ferromagnetic hcp metal; heating accesses fcc cobalt. An fcc reference has \(a=3.548\) Å, nearest spacing 2.509 Å. Strong neutral Co lines include 345.3510 and 351.3481 nm. **HYPOTHESIS / kill condition:** if a scalar link model is claimed to recover the spin or directional response of Co, compare distinct magnetization directions and hcp versus fcc specimens. A phase-independent scalar assigned from the same atomic ladder cannot distinguish these inputs. I found no established intrinsic bulk elemental \(T_c\) in the references checked. Atomic v1 assignment: **none found**. [hcp Co](https://www.crystallography.net/cod/9008492.html) · [fcc Co](https://www.crystallography.net/cod/9008466.html) [pml.nist.gov](https://pml.nist.gov/PhysRefData/Handbook/Tables/cobalttable2_a.htm?utm_source=chatgpt.com)

**Ni · Nickel.** **MEASURED / DERIVED:** neutral \(3d^84s^2\) becomes \(3d^9\) at \(Ni^+\). This is a second consecutive rearrangement. Its anion still lies outside the wall with \(z_0=6.60108\). Ni is a silvery ferromagnetic fcc metal, with the NIST 2025 compilation listing a Curie reading of 631.43 K. In a 2025 shock experiment its fcc phase persisted to **332 GPa**. Neutral Ni I has strong lines at 351.5052 and 352.4536 nm. **HYPOTHESIS / kill condition:** assigning a new crystal topology whenever bulk magnetic order disappears fails if diffraction retains fcc. The spin projector and structural projector need distinct labels. I found no established intrinsic bulk elemental \(T_c\) in the references checked. Atomic v1 assignment: **none found**. [Ni refinement](https://www.crystallography.net/cod/9008476.html) [physics.nist.gov](https://physics.nist.gov/PhysRefData/Handbook/Tables/nickeltable2.htm?utm_source=chatgpt.com)

**Cu · Copper.** **DERIVED:** \(3d^{10}4s\to3d^{10}\to3d^9\) gives a clean \(4s\)-to-\(3d\) switch at \(k=1\), \(z=2.62638,\ \Gamma=.44849\). Cu has the batch’s nearest bound-anion approach to the loop wall; its entire quoted-input range remains outside. **MEASURED:** it is also the best ambient electrical conductor of the five. Its red bulk appearance comes from wavelength-dependent reflectance and interband absorption. The Cu I resonance line at 324.754 nm belongs to a different optical experiment. Dense Cu is especially useful for the ball map: bcc Cu was observed under hot shock compression, and a 2026 X-ray study also reports a **plausible metastable 9R** structure after quenching. **HYPOTHESIS / kill condition:** apply the same orbital construction at the fcc and bcc coordinations before attributing a change in a raw single-link weight to a change in conduction. The fcc test above already passes without fitting the measured conductivity. I found no established intrinsic bulk elemental \(T_c\) in the checked sources. Atomic v1 assignment: **none found**. [Cu refinement](https://www.crystallography.net/cod/9008468.html) [physics.nist.gov](https://physics.nist.gov/PhysRefData/Handbook/Tables/coppertable2.htm?utm_source=chatgpt.com)

**Zn · Zinc.** **MEASURED / DERIVED:** neutral Zn closes both \(3d^{10}\) and \(4s^2\). It has no bound isolated ground-state anion, yet bulk zinc conducts and becomes a conventional superconductor at about **0.85 K**. Its \(k=2\) switch, after the two \(4s\) removals, is \(z=2.21122,\ \Gamma=.37718\). Zinc gives an unusually clear warning about neighbour counting: the cited hcp crystal has six basal neighbours at **2.6594 Å**, while the six adjacent-layer sites are about **2.9070 Å** away. Choosing six versus twelve changes the normalizing denominator. The phase diagram has been studied to 140 GPa; hcp symmetry persisted to melting in the investigated range. Neutral Zn I has visible lines at 468.0136, 472.2157 and 481.0532 nm, while bulk Zn is bluish silver. **HYPOTHESIS / kill condition:** a claimed Zn junction verdict that changes solely by silently including the second set of six neighbours is a neighbour-definition effect. Predeclare the shells and report both shell sums. Atomic v1 assignment: **none found**. [Zn refinement](https://www.crystallography.net/cod/9012435.html) [physics.nist.gov](https://physics.nist.gov/PhysRefData/Handbook/Tables/zinctable2.htm?utm_source=chatgpt.com)

**Mainstream-blend watch.** The internal apex is calculated in Jeromie’s intrinsic coordinate. The Å-scale distance comes from diffraction; the Bruggeman parameter requires a separately identified volume fraction; the projector cutoff is a statement about weights. For none of these five elements does the gas-phase ladder alone assign a measured “above/below one third” volume fraction. Likewise, the hypotheses that light leads the transfer and that directed peels may encode decay need time-resolved or isotope-resolved tests. Neither follows from metallic appearance or a static ground-state projector.

## 5. Isotope centres and what survives a peel

**MEASURED / DERIVED.** The appendix gives isotope-by-isotope spin/parity, dipole and charge radius where available in the IAEA snapshot. Below are all naturally occurring isotope groups and selected newer reference radii. Magnetic moments are in nuclear magnetons. Definite spin-zero ground states have zero dipole. The quark counts use \(u=2Z+N,\ d=Z+2N\) and label the centre for the named isotope. [IAEA LiveChart](https://www-nds.iaea.org/relnsd/vcharthtml/VChartHTML.html) · [IUPAC isotopic compositions](https://www.ciaaw.org/isotopic-abundances.htm) [arxiv.org](https://arxiv.org/pdf/2409.08193?utm_source=chatgpt.com)

| Element | Natural isotope spin and magnetic moment | Selected reference charge radius, fm | Centre, \(p,n;\ u,d\) |
|---|---|---|---|
| Fe | 54, 56, 58: \(0^+,0\); 57: \(1/2^-,+.09064\) | 54: 3.688(4); 56: 3.733(4) | \(^{56}\)Fe: 26,30; 82,86 |
| Co | 59: \(7/2^-,+4.615\) | 59: 3.786(5) | \(^{59}\)Co: 27,32; 86,91 |
| Ni | 58, 60, 62, 64: \(0^+,0\); 61: \(3/2^-,-.74965\) | 58: 3.773(3) | \(^{58}\)Ni: 28,30; 86,88 |
| Cu | 63: \(3/2^-,+2.2259\); 65: \(3/2^-,+2.3844\) | 65: 3.902(5) | \(^{63}\)Cu: 29,34; 92,97 |
| Zn | 64, 66, 68, 70: \(0^+,0\); 67: \(5/2^-,+.87485\) | 68: 3.964(5) | \(^{64}\)Zn: 30,34; 94,98 |

**RECOGNISED.** \(^{63}\)Cu and \(^{64}\)Zn have the same neutron count. One more proton takes the listed nuclear centre from spin \(3/2\) to zero. On the electronic side, Cu⁻ and neutral Zn have the same 30-electron count, while Zn has no bound next anion. That gives the atlas a matched comparison at both centre and wall without identifying either nuclear spin or electron attachment with the other.

**Set aside, with why.** I did not establish an exhaustive coordinate census of every metastable or high-pressure phase. The 63 records are refinements, not 63 distinct phases. I did not assign element-specific knot polynomials without a reproducible closed path. The β-Mn screw provides such a path under a stated periodic closure, and that closure gives an unknot. The projector results are numerical controls plus the analytic bounds above. I made no Lean or branch changes.

## Generated Fe–Zn CSV

At \(k=0\), the energy column holds EA. At \(k\ge1\), it holds \(IE_k\). The grade belongs to the energy on that row: `E` unbracketed evaluated, `S` semiempirical, `T` theoretical, `EA22` affinity evaluation. Zn’s blank rung 0 and each terminal bare-nucleus ratio are intentional. The downloadable CSV in the appendix is the byte-checked copy.

```csv
Z,symbol,k,IE_k (eV),z_k,Gamma_k,source
26,Fe,0,0.153236,51.57057,0.96196,EA22
26,Fe,1,7.9024681,2.04989,0.34424,E
26,Fe,2,16.19921,1.89213,0.30847,E
26,Fe,3,30.651,1.79146,0.28353,E
26,Fe,4,54.91,1.36587,0.15465,E
26,Fe,5,75.0,1.31980,0.13786,S
26,Fe,6,98.985,1.26249,0.11602,E
26,Fe,7,124.9671,1.20880,0.09453,E
26,Fe,8,151.06,1.54641,0.21458,E
26,Fe,9,233.6,1.12200,0.05749,S
26,Fe,10,262.1,1.10988,0.05208,S
26,Fe,11,290.9,1.13716,0.06418,S
26,Fe,12,330.8,1.09129,0.04365,S
26,Fe,13,361.0,1.08643,0.04142,S
26,Fe,14,392.2,1.16318,0.07544,S
26,Fe,15,456.2,1.07258,0.03502,E
26,Fe,16,489.312,2.58056,0.44143,S
26,Fe,17,1262.7,1.07531,0.03629,S
26,Fe,18,1357.8,1.07527,0.03627,S
26,Fe,19,1460.0,1.07918,0.03808,S
26,Fe,20,1575.6,1.07070,0.03414,E
26,Fe,21,1687.0,1.06603,0.03196,S
26,Fe,22,1798.4,1.08452,0.04055,S
26,Fe,23,1950.4,1.04889,0.02386,S
26,Fe,24,2045.759,4.31536,0.62373,T
26,Fe,25,8828.1864,1.05092,0.02483,T
26,Fe,26,9277.6886,,,T
27,Co,0,0.662255,11.90027,0.84496,EA22
27,Co,1,7.88101,2.16779,0.36865,E
27,Co,2,17.0844,1.96085,0.32452,E
27,Co,3,33.5,1.53045,0.20963,S
27,Co,4,51.27,1.55061,0.21588,S
27,Co,5,79.5,1.28302,0.12397,S
27,Co,6,102.0,1.26373,0.11650,S
27,Co,7,128.9,1.22420,0.10080,S
27,Co,8,157.8,1.17959,0.08240,S
27,Co,9,186.14,1.47953,0.19340,E
27,Co,10,275.4,1.10864,0.05152,S
27,Co,11,305.32,1.10081,0.04799,S
27,Co,12,336.1,1.12615,0.05933,S
27,Co,13,378.5,1.08322,0.03995,S
27,Co,14,410.0,1.07585,0.03654,S
27,Co,15,441.1,1.16064,0.07435,S
27,Co,16,511.96,1.06764,0.03271,S
27,Co,17,546.588,2.55622,0.43761,S
27,Co,18,1397.2,1.07680,0.03698,E
27,Co,19,1504.5,1.06746,0.03263,E
27,Co,20,1606.0,1.07347,0.03544,S
27,Co,21,1724.0,1.06961,0.03363,S
27,Co,22,1844.0,1.06334,0.03070,S
27,Co,23,1960.8,1.08089,0.03887,S
27,Co,24,2119.4,1.04694,0.02293,S
27,Co,25,2218.876,4.30136,0.62274,T
27,Co,26,9544.1817,1.04903,0.02393,T
27,Co,27,10012.1297,,,T
28,Ni,0,1.157368,6.60108,0.73688,EA22
28,Ni,1,7.639878,2.37816,0.40796,E
28,Ni,2,18.168838,1.93667,0.31896,E
28,Ni,3,35.187,1.56080,0.21900,E
28,Ni,4,54.92,1.38492,0.16140,S
28,Ni,5,76.06,1.41993,0.17353,S
28,Ni,6,108.0,1.22222,0.10000,S
28,Ni,7,132.0,1.22727,0.10204,T
28,Ni,8,162.0,1.19259,0.08784,T
28,Ni,9,193.2,1.16304,0.07538,S
28,Ni,10,224.7,1.42190,0.17420,S
28,Ni,11,319.5,1.10047,0.04783,S
28,Ni,12,351.6,1.09357,0.04470,S
28,Ni,13,384.5,1.11651,0.05505,S
28,Ni,14,429.3,1.07803,0.03755,S
28,Ni,15,462.8,1.07095,0.03426,S
28,Ni,16,495.4,1.15275,0.07095,S
28,Ni,17,571.07,1.06295,0.03052,S
28,Ni,18,607.02,2.53715,0.43457,S
28,Ni,19,1540.1,1.06876,0.03324,E
28,Ni,20,1646.0,1.06323,0.03065,S
28,Ni,21,1750.0,1.06569,0.03180,S
28,Ni,22,1880.0,1.06899,0.03335,S
28,Ni,23,2008.1,1.06095,0.02958,S
28,Ni,24,2130.5,1.07749,0.03730,S
28,Ni,25,2295.6,1.04516,0.02208,S
28,Ni,26,2399.259,4.28836,0.62181,T
28,Ni,27,10288.8848,1.04729,0.02310,T
28,Ni,28,10775.3948,,,T
29,Cu,0,1.23578,6.25223,0.72422,EA22
29,Cu,1,7.72638,2.62638,0.44849,E
29,Cu,2,20.29239,1.81551,0.28965,E
29,Cu,3,36.841,1.55750,0.21799,E
29,Cu,4,57.38,1.39073,0.16343,S
29,Cu,5,79.5,1.29073,0.12691,S
29,Cu,6,103.0,1.34951,0.14876,S
29,Cu,7,139.0,1.19424,0.08852,S
29,Cu,8,166.0,1.19277,0.08791,T
29,Cu,9,198.0,1.17273,0.07950,T
29,Cu,10,232.2,1.14268,0.06659,S
29,Cu,11,265.33,1.38318,0.16079,E
29,Cu,12,367.0,1.09264,0.04427,S
29,Cu,13,401.0,1.08728,0.04182,S
29,Cu,14,436.0,1.10803,0.05125,S
29,Cu,15,483.1,1.07369,0.03554,S
29,Cu,16,518.7,1.06574,0.03182,S
29,Cu,17,552.8,1.14418,0.06724,S
29,Cu,18,632.5,1.06025,0.02924,S
29,Cu,19,670.608,2.52085,0.43195,S
29,Cu,20,1690.5,1.06477,0.03137,S
29,Cu,21,1800.0,1.06556,0.03174,S
29,Cu,22,1918.0,1.06569,0.03180,S
29,Cu,23,2044.0,1.06624,0.03206,S
29,Cu,24,2179.4,1.05869,0.02851,S
29,Cu,25,2307.3,1.07446,0.03589,S
29,Cu,26,2479.1,1.04351,0.02129,S
29,Cu,27,2586.954,4.27624,0.62094,T
29,Cu,28,11062.4309,1.04567,0.02232,T
29,Cu,29,11567.6237,,,T
30,Zn,0,,,,EA22
30,Zn,1,9.394197,1.91229,0.31325,E
30,Zn,2,17.96439,2.21122,0.37718,E
30,Zn,3,39.7233,1.49970,0.19990,E
30,Zn,4,59.573,1.38653,0.16196,E
30,Zn,5,82.6,1.30751,0.13326,S
30,Zn,6,108.0,1.23981,0.10707,S
30,Zn,7,133.9,1.29873,0.12995,S
30,Zn,8,173.9,1.16734,0.07721,S
30,Zn,9,203.0,1.17241,0.07937,S
30,Zn,10,238.0,1.15294,0.07104,T
30,Zn,11,274.4,1.13265,0.06220,S
30,Zn,12,310.8,1.34363,0.14662,S
30,Zn,13,417.6,1.08573,0.04110,S
30,Zn,14,453.4,1.08205,0.03941,S
30,Zn,15,490.6,1.10069,0.04793,S
30,Zn,16,540.0,1.07000,0.03382,S
30,Zn,17,577.8,1.06144,0.02980,S
30,Zn,18,613.3,1.13729,0.06424,S
30,Zn,19,697.5,1.05716,0.02778,S
30,Zn,20,737.366,2.50459,0.42932,S
30,Zn,21,1846.8,1.06184,0.02999,S
30,Zn,22,1961.0,1.06323,0.03065,S
30,Zn,23,2085.0,1.06187,0.03001,S
30,Zn,24,2214.0,1.06504,0.03150,S
30,Zn,25,2358.0,1.05662,0.02753,S
30,Zn,26,2491.5,1.07160,0.03456,S
30,Zn,27,2669.9,1.04199,0.02056,S
30,Zn,28,2781.996,4.26490,0.62013,T
30,Zn,29,11864.9401,1.04416,0.02160,T
30,Zn,30,12388.9427,,,T
```

**Source list**

- Framework and input archive. [Pinned VOTKP data](https://github.com/dicipler-pixel/votkp-lean/blob/cae5f49/data/element_thresholds_20261011.json.gz) · [Moving-matrix ball work](https://github.com/dicipler-pixel/votkp-lean/tree/a60a000/research)
- Atomic data. [NIST ASD 5.12, 2024](https://doi.org/10.18434/T4W30F) · [Ning and Lu, 2022](https://doi.org/10.1063/5.0080243) · [CTCP polarizabilities](https://ctcp.massey.ac.nz/2025Tablepol.pdf) · [NIST spectroscopic handbook](https://physics.nist.gov/PhysRefData/Handbook/)
- Solid and nuclear data. [NIST phase-transition evaluation, 2025](https://doi.org/10.6028/NIST.TN.2312) · [Crystallography Open Database](https://www.crystallography.net/cod/) · [β-Mn absolute-hand experiment](https://doi.org/10.1126/sciadv.abg0868) · [IAEA nuclear data](https://www-nds.iaea.org/relnsd/vcharthtml/VChartHTML.html) · [Reference charge-radius evaluation](https://arxiv.org/abs/2409.08193)