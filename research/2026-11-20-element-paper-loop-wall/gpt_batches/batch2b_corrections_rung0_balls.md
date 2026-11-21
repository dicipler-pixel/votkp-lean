Jeromie, all six ball folders opened on `claude/moving-matrix-of-balls`. My earlier H–Ne mapping missed a distinction your code makes explicit: **the reflection between successive peels of one atom and the reflection at the junction between two neighbouring atoms are different observables.** Hydrogen makes this especially clear. Its anion rung gives \(\Gamma_0=0.894905\). Two identical resting hydrogen cells in your light-between model give \(\Gamma_{\rm junction}=0\). Both results follow from your formula. They use different pairs of inputs.

Adding rung 0 also changes a conclusion from batch two. **Carbon alone among C–Ne crosses the loop wall at the opening of the \(1s\) core. Oxygen also crosses it, earlier, at its anion rung.** So the atlas needs to record *which* boundary crossed the wall. A single outside/inside label per element loses that information.

[VOTKP_H_to_Ne_corrected_ladders.csv](https://chatgpt.com/library?file_id=libfile_fde3_f-8e7ab053e4e481918fe688a54c269f1e_ea4e520c657081918696167b9513e64f) contains the complete corrected H–Ne ledger: all 55 ordinary ionization thresholds, six bound-anion thresholds, four explicit unavailable rung-zero records, and all 51 defined adjacent reflections in both directions.

## 1. Rung 0, from hydrogen through neon

**DERIVED.** In the extended ladder the first two energy costs are
\[
X^-\longrightarrow X+e^- \quad (I_0=\mathrm{EA}),\qquad
X\longrightarrow X^++e^- \quad (I_1).
\]
For a bound ground-state anion,
\[
z_0=\frac{I_1}{\mathrm{EA}},\qquad
\Gamma_0=\frac{I_1-\mathrm{EA}}{I_1+\mathrm{EA}}.
\]
The EA column uses measured detachment energies for the six bound cases. The ionization column uses NIST ASD v5.12, whose recommended thresholds include theoretical values where indicated in the downloadable ledger. For H I used the **measured** affinity \(0.754195(18)\) eV so the provenance of that first result is explicit. [webbook.nist.gov](https://webbook.nist.gov/cgi/cbook.cgi?ID=C12184882\&Mask=1A8F\&utm_source=chatgpt.com)

| Element | \(I_1\), eV | Ground-state atomic EA used, eV | \(z_0\) | \(\Gamma_0\) | Rung 0 versus the loop wall |
|---|---:|---:|---:|---:|---|
| H | 13.598434599702 | 0.754195 | 18.03040 | 0.894905 | Outside |
| He | 24.587389011 | No bound anion | — | — | Undefined |
| Li | 5.391714996 | 0.618049 | 8.72377 | 0.794318 | Outside |
| Be | 9.322699 | No bound anion | — | — | Undefined |
| B | 8.298019 | 0.279723 | 29.66513 | 0.934779 | Outside |
| C | 11.2602880 | 1.2621226 | 8.92171 | 0.798422 | Outside |
| N | 14.53413 | No bound anion | — | — | Undefined |
| O | 13.618055 | 1.4611136 | 9.32033 | 0.806208 | Outside |
| F | 17.42282 | 3.4011898 | 5.12257 | 0.673340 | Inside |
| Ne | 21.564541 | No bound anion | — | — | Undefined |

**MEASURED / evaluated.** **Helium, beryllium, nitrogen and neon have no bound ground-state atomic anion** under this definition. A metastable negative-ion state, a temporary scattering resonance, or an anion stabilized in a compound answers a different question. Those four records carry an explicit status with blank numerical fields. Substituting zero for EA would manufacture an infinite ratio and a fictitious wall crossing. [info.phys.tsinghua.edu.cn](https://info.phys.tsinghua.edu.cn/henucl/ning/148.pdf?utm_source=chatgpt.com)

**DERIVED — Hydrogen checks your number.**
\[
z_0=\frac{13.598434599702}{0.754195}=18.030396,\qquad
\Gamma_0=\frac{13.598434599702-0.754195}{13.598434599702+0.754195}
=0.894905.
\]
Hydrogen therefore has a real two-threshold comparison even though its ordinary neutral-to-bare ladder has just one threshold. At the other end of this table, fluorine binds the extra electron most strongly, yet has the *smallest* rung-zero reflection among the six. Boron’s weak binding gives it the **largest** rung-zero reflection. What survives in \(\Gamma_0\) is the contrast across neutrality.

## 2. Following the same \(1s\) opening from Li to Ne

**DERIVED.** Compare the same electronic event in every row. Start from a Li-like ion \(1s^22s\). The first removal costs \(I_{Z-2}\) and leaves \(1s^2\). The next costs \(I_{Z-1}\) and opens the closed \(1s\) core. Thus
\[
z_K=\frac{I_{Z-1}}{I_{Z-2}},\qquad
\Gamma_K=\frac{z_K-1}{z_K+1}.
\]
Hydrogen and helium have no such pair on their ground-state ladders. Hydrogen’s large rung-zero result is therefore **not a \(2s\)-to-\(1s\) core opening**. [NIST](https://www.nist.gov/pml/atomic-spectra-database?utm_source=chatgpt.com)

| Element | Starting Li-like ion | Last \(2s\) removal → first \(1s\) removal, eV | \(z_K\) | \(\Gamma_K\) | Wall |
|---|---|---:|---:|---:|---|
| Li | Li | 5.391715 → 75.640097 | 14.02895 | 0.866923 | Outside |
| Be | \(\mathrm{Be}^+\) | 18.21115 → 153.896205 | 8.45066 | 0.788375 | Outside |
| B | \(\mathrm B^{2+}\) | 37.93059 → 259.374379 | 6.83813 | 0.744837 | Outside |
| C | \(\mathrm C^{3+}\) | 64.49352 → 392.09056 | **6.07953** | **0.717496** | **Outside** |
| N | \(\mathrm N^{4+}\) | 97.8901 → 552.06741 | **5.63967** | **0.698780** | **Inside** |
| O | \(\mathrm O^{5+}\) | 138.1189 → 739.32697 | 5.35283 | 0.685180 | Inside |
| F | \(\mathrm F^{6+}\) | 185.1868 → 953.8983 | 5.15101 | 0.674850 | Inside |
| Ne | \(\mathrm{Ne}^{7+}\) | 239.0970 → 1195.8082 | 5.00135 | 0.666742 | Inside |

**DERIVED — Why the wall is there in your tree.** Your note gives the two-face boundary as \(\sinh h_a\,\sinh h_b=1\). For an equal-step comparison, \(h_a=h_b=\tfrac12\ln z\). Then
\[
\sinh h=1,\qquad e^h=1+\sqrt2,\qquad
z_*=3+2\sqrt2=5.828427\ldots,\qquad \Gamma_*=\frac1{\sqrt2}.
\]
This is the equal-face criterion. For unlike neighbouring faces, the general test retains both \(h_a\) and \(h_b\). [Your tree note and implementation](https://github.com/dicipler-pixel/votkp-lean/tree/a60a000dc41e21be6f1cca3ff9197595a3819ade/research/the-ball-is-the-tree)

**DERIVED — Why the sequence crosses on its way toward four.** With the same effective nuclear charge for both removals, the hydrogenic energy factors give
\[
z_{\rm hydrogenic}=\frac{Z^2/2}{Z^2/8}=4,\qquad
\Gamma_{\rm hydrogenic}=\frac35.
\]
At low \(Z\), the two inner electrons screen the outer \(2s\) electron strongly. The valence-removal cost is consequently small compared with the first core-removal cost. To see the effect directly in the data, define the two effective charges by matching each threshold to its own hydrogenic energy. Then
\[
z_K=4\left(\frac{Z_{\rm eff,core}}{Z_{\rm eff,val}}\right)^2.
\]
The wall requires an effective-charge ratio of \((1+\sqrt2)/2=1.207107\). Carbon gives \(\sqrt{6.07953/4}=1.23284\); nitrogen gives \(\sqrt{5.63967/4}=1.18740\). **The ratio of effective charges passes through the wall value while both elements still have an intact \(1s^2\) core before the opening.** As nuclear attraction increasingly dominates the relative screening correction in the nonrelativistic isoelectronic expansion, the energy ratio tends toward four.

**DERIVED — Screening control.** I recalculated the crossing with your stored expansion, in Hartree,
\[
I_{\rm core}\simeq Z^2/2-(5/8)Z+0.157666,\qquad
I_{\rm val}\simeq Z^2/8-(290/729)Z+0.250500.
\]
Solving \(I_{\rm core}/I_{\rm val}=3+2\sqrt2\) gives **\(Z_*=6.53850\)**. Linear interpolation of the evaluated C and N *ratios* gives **6.571**. I also checked exactly what the code removes in its unscreened control. It replaces the whole core numerator by \(Z^2/2\), giving **9.47002**. Removing only the linear \(5Z/8\) correction while retaining \(+0.157666\) gives **9.54777**. Both controls shift the crossing to F–Ne. That isolates the importance of the leading core-screening term without attributing the entire numerical shift to it. [Your screening script](https://github.com/dicipler-pixel/votkp-lean/blob/74125d2977809c90d459ab7441a6726d1348962f/research/2026-11-11-standard-model-ball/elements/shell_screen_04.py)

## 3. What the six ball folders change

I opened all six at commit `a60a000dc41e21be6f1cca3ff9197595a3819ade`. Two checks below are fresh local runs. The other results are identified as archived checks or model definitions.

| Folder | Source-grounded correction |
|---|---|
| [Balls in the Sea](https://github.com/dicipler-pixel/votkp-lean/tree/a60a000dc41e21be6f1cca3ff9197595a3819ade/research/balls-in-the-sea) | **HYPOTHESIS / model definition.** The sea is represented by an occupied projector \(P\) on balls and link sites. A ball’s local state is its \(2\times2\) block \(C_i\). The sweep distinguishes an all-at-once matrix from travelling models and tests whether the far ball changes before the link crossing time. A covalent packing fraction cannot supply that information. |
| [Hydrogen in the Space Between](https://github.com/dicipler-pixel/votkp-lean/tree/a60a000dc41e21be6f1cca3ff9197595a3819ade/research/hydrogen-in-the-space-between) | **DERIVED in the model, fresh run.** The gap contains actual model sites. The code reads link weight \(X_{ij}=\lVert P_{ij}\rVert_F^2\) and declares a chain connected when every tested gap link exceeds \((1/4)/3=1/12\). At separation 4 the minimum was \(6.416\times10^{-4}\), well below that mark. The ground sea was still; after a kick the far atom responded later at larger separations. The page explicitly disclaims a hydrogen bond-energy curve because the number of sites changes with separation. |
| [Hydrogen and the Light Between](https://github.com/dicipler-pixel/votkp-lean/tree/a60a000dc41e21be6f1cca3ff9197595a3819ade/research/hydrogen-and-the-light-between) | **DERIVED in the model.** With room \(s\) and empty fraction \(E\), the drawing uses \(r_c=(s/2)(1-E)^{1/3}\), gap \(\delta=s-2r_c\), and gap power transmission \(\operatorname{sech}^2(\kappa_g\delta)\). Equal resting H clocks give zero face reflection even when a finite gap still attenuates transmission. An archived moving-wall test missed its fixed-wall control by \(1.7\times10^{-3}\). |
| [Seven Balls, His Light](https://github.com/dicipler-pixel/votkp-lean/tree/a60a000dc41e21be6f1cca3ff9197595a3819ade/research/seven-balls-his-light) | **DERIVED in the model, fresh run.** All seven radii stay fixed at one in v4. The six neighbours move. At the wall, a neighbour’s near point agrees with the face apex \(\tanh(r/4)\). The centre ball’s intrinsic light and the external room-light tracer obey different path rules. The intrinsic comparison exercised 31 interior segments and **zero first-transmitted directions** in that test. Interior agreement therefore leaves that transmitted-direction check open. |
| [The Ball Is the Tree](https://github.com/dicipler-pixel/votkp-lean/tree/a60a000dc41e21be6f1cca3ff9197595a3819ade/research/the-ball-is-the-tree) | **HYPOTHESIS / model definition.** From the light’s viewpoint there is one tree. A rung comprises the parent face, the intervening stretch or junction, and the child face. The faces carry opposite orientations. Ground leaves retain a record \(K\). The archived depth-two run conserved the ledger, but equal-schedule twins differed by \(7.0\times10^{-5}\) against a \(10^{-10}\) criterion. That numerical equality test failed. |
| [Two Atoms in a Ball](https://github.com/dicipler-pixel/votkp-lean/tree/a60a000dc41e21be6f1cca3ff9197595a3819ade/research/two-atoms-in-a-ball) | **DERIVED in the model, archived run.** Two inner cells and a surrounding rim carry a work ledger. A moving wall can give energy to light or take it back. The closed-rim check registered outside energy of \(7.884\times10^{-5}\), and total wall work changed with step size. The model declares no bath, so the deposited work has no calibrated temperature. |

**Mainstream-blend watch.** Three quantities appeared under “one third” in the earlier mapping: an assigned geometric packing fraction, a conducting-constituent fraction in an effective-medium model, and your normalized weakest-link projector test. They have different inputs. Graphite defeats the simple *packing-fraction* conductivity classifier. It does **not** by itself defeat the projector test, because graphite’s directional \(P_{ij}\) was never calculated. Conversely, the hydrogen simulation’s failed connectivity mark does not measure the DC conductivity of physical hydrogen.

## 4. Revised ball mapping for each element

**HYPOTHESIS — element applications.** Hydrogen has a direct implementation in the recovered folders. For He–Ne the entries below are mappings and tests using those source definitions. I found no calibrated element-specific sea projector in these six folders for those nine elements, so their projector connection status remains **unmeasured**. The peel and loop-wall classifications in the middle column are calculated.

| Element | What the directed ladder keeps | Revised ball mapping and the test that can defeat it |
|---|---|---|
| **H** | Bound outer anion rung outside; no Li-like core opening. | Use the implemented pair of H cells and the gap sites. Equal resting cells give zero clock mismatch, while the atomic anion rung is strongly reflecting. An identification of those two reflections already fails numerically. The distinct gap-transmission prediction can be tested by varying separation at fixed face clocks. |
| **He** | No bound anion rung. Its two ordinary thresholds give \(\Gamma_1=0.377575\); both removals start in the \(1s\) shell. | Two equivalent resting He cells provide an equal-clock control. The model permits a finite intervening stretch with a transparent junction. A rule assigning a finite anion rung to represent that stretch fails the binding test. A neutral–neutral transport model still needs its own link state. |
| **Li** | Both rung 0 and the \(1s\) opening lie outside. The core opening is stronger, \(0.866923\) versus \(0.794318\). | For metallic Li, compare the outer-electron connected paths with the large inner-shell reflection. A rule that treats the strongest atomic reflection as blocking all bulk charge transport fails here. The stronger test is whether an occupied-state projector predicts connected paths in the conducting phase. |
| **Be** | No bound anion rung; core opening outside. | Metallic link transport can coexist with an unavailable isolated-atom rung 0. This rules out any requirement that a neutral atom must bind an extra isolated electron before its bulk material can conduct. In the ball picture, a state shared across links is a separate object. |
| **B** | Rung 0 is the largest of all H–Ne, \(\Gamma_0=0.934779\); core opening also outside. | For crystalline boron, label bonds inside a cluster separately from links between clusters. In the earlier geometry ledger, changing the assigned radius from 0.85 to 0.84 Å moved the packing fraction from 0.33534 to 0.32364, across one third. A conductivity grade that changes with that convention alone fails. The weakest-link test instead requires the intercluster \(P_{ij}\). |
| **C** | Rung 0 and core opening both outside. The larger reflection on the extended ladder is now the anion rung, \(0.798422\), rather than the core opening, \(0.717496\). | Diamond and graphite share the isolated C ladder. In graphite, compare paths along a sheet and across the sheets; in diamond, compare equivalent tetrahedral paths. A model with only the atomic input cannot distinguish them. A directional connection model can make a separate prediction for each path. |
| **N** | No bound anion rung; core opening inside. | In molecular nitrogen, distinguish transfer across the two faces within \(\mathrm N_2\) from transfer to the next molecule. Changing molecular orientation changes the latter path even with the same isolated-atom ladder. A single path assigned to both must reproduce both observations to survive. |
| **O** | **Anion rung outside, core opening inside.** \(0.806208\) versus \(0.685180\). | Oxygen is the cleanest counterexample to assigning one wall side to an entire element. In condensed \(\mathrm O_2\), record the molecular orientation and magnetic state as separate inputs. A sign-sensitive transport claim should predict what reverses when the selected orientation reverses. |
| **F** | Anion rung and core opening both inside, and unusually close: \(0.673340\) and \(0.674850\). | These similar amplitudes arise from very different threshold pairs: \(3.40119\to17.42282\) eV and \(185.1868\to953.8983\) eV. Any rule reconstructing the physical layer from \(\Gamma\) alone is ambiguous here. Keep the rung identity. In solid \(\mathrm F_2\), also keep intramolecular bonds distinct from gaps between molecules. |
| **Ne** | No bound anion rung; core opening inside. | Monatomic fcc Ne removes the intramolecular path ambiguity. Compare symmetry-equivalent paths at the same pressure, then compare the same path under compression. A measured change in transmission alongside a fixed atomic ladder tests the contribution from the intervening stretch. A claimed directional split between equivalent paths needs an independently identified source of broken symmetry. |

## 5. What the Russell connection establishes for the elements

**DERIVED.** Let \(R\) reverse an *ordered pair* of positive thresholds. Then
\[
R:z\mapsto z^{-1},\qquad
\ln z\mapsto-\ln z,\qquad
\Gamma\mapsto-\Gamma,\qquad
\Gamma^2\mapsto\Gamma^2.
\]
For the same H threshold pair, the forward record is \(+0.894905\) and the reverse record is \(-0.894905\). A ledger retaining only the returned power \(\Gamma^2\) gives the same entry both ways. **The direction is already present in VOTKP if the atlas retains the sign and the ordered pair.** That is an exact elemental example of the distinction you describe in *Russell, Corrected*.

**RECOGNISED.** The octave has a related but slightly more specific symmetry. Across Li–Ne, \(1,2,3,4,3,2,1,0\) pairs Li with F, Be with O, and B with N across carbon. Neon’s zero pairs with the preceding closed shell, helium, if both endpoints are included. The extended sequence He–Ne is then \(0,1,2,3,4,3,2,1,0\). **The anion ladder breaks that octave symmetry in a directly checkable way:** Be and O both receive valence two, but only O has a bound rung 0. B and N both receive valence three, but B has the strongest rung-zero reflection of this set and N has no bound rung 0 at all. Here the peel ledger recovers information that the octave actually discards. [info.phys.tsinghua.edu.cn](https://info.phys.tsinghua.edu.cn/henucl/ning/148.pdf?utm_source=chatgpt.com)

**Set aside, with why.** Reversing threshold order, mirroring a spatial path, and mirroring a knot are distinct operations. The first sign reversal is proved above. Connecting it to either of the other two requires an explicit map that respects the reversal. I used your account of the Russell papers for that comparison; I did not independently grade Plate II or the 386 entries. For the element work, the narrower conclusion already holds: **keep the ordered thresholds, signed amplitude, returned power, and physical identity of the rung as separate fields.**

**Carry-forward for batches 3–5.** Each element will get an explicit bound-anion status and rung 0, its Li-like \(1s\) opening compared with both \(3+2\sqrt2\) and four, and a phase-specific ball mapping grounded in these six folders. Atomic peel, neighbouring-clock junction, gap transmission and projector connectivity will each retain their own inputs and evidence status.