# Barium through neodymium — element ladders

**DERIVED.** On the 21 November 2026 run, all 285 ordinary peel ratios in this batch fall inside the loop wall. All five bound-anion rungs fall outside. All 290 classifications survive the independent rectangular input boxes formed from the reported uncertainties. The largest ordinary upper bound is 4.096071445 for barium’s helium-core opening. The smallest anion lower bound is 9.227472817 for cerium. Each of the seven comparator cutoffs frozen in batch 11 (5 through 6) gives the same labels across every box in this batch. These five elements add stringent source and shell-assignment checks, while leaving the earlier empirical window on the cutoff intact.

**SOURCE RECORD.** The public ladder contains 295 rows including the five terminal energies, each with blank outgoing ratio. Its 290 ionization energies come directly from the immutable [threshold archive](https://github.com/dicipler-pixel/votkp-lean/blob/8e5d44f1d9e36f242e6522bbe70cea18fb315c7a/data/element_thresholds_20261011.json.gz). SHA-256 is `75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c`. The archive grades are 9 E (experimental), 28 S (semiempirical) and 253 T (theoretical). Input boxes are conditional sensitivity intervals. A theoretical estimate with an uncertainty stays labelled T. The 2022 Ning–Lu recommendations supply the five measured extra-electron binding energies. “EA22” labels that separate input in the CSV. [Ning and Lu, Table 3](https://doi.org/10.1063/5.0080243)

[Full requested CSV](batch12_ba_nd.csv) · [Detailed wall, face and configuration rows](rungs_detailed.csv) · [Anion chemistry](anion_chemistry.csv) · [Named openings](asg_openings.csv) · [Fresh public ASD extract](asd_states_20261121.csv) · [Independent audit](audit.txt) · [Source substitutions](source_variants.csv)

## Where current ASD differs from the archive

**MEASURED.** All 290 archive energy values match the generated ladder. In the separate comparison with fresh public ASD, 289 of 290 energies, 289 of 290 uncertainties, 290 of 290 grades and 289 of 290 reference strings agree. Every difference belongs to neutral neodymium. The archive gives 5.525 ± 0.0006 eV (L4277). ASD now gives 5.52475 ± 0.00005 eV (L23155, Miyabe et al., 2024). The central shift is −0.00025 eV and the reported uncertainty is twelve times smaller. The seven-column file preserves the pin. [Current NIST ground shells and energies](https://physics.nist.gov/cgi-bin/ASD/ie.pl?at_num_out=on&biblio=on&e_out=0&el_name_out=on&level_out=on&seq_out=on&shells_out=on&spectra=Nd&unc_out=on&units=1) · [2024 measurement](https://doi.org/10.1016/j.sab.2024.107036)

**DERIVED.** Holding the primary EA fixed, substituting the current IE1 changes neodymium’s k=0 pair from (56.678293, 0.965325) to (56.675728, 0.965323). The k=1 pair changes from (1.951674, 0.322418) to (1.951763, 0.322439). Their endpoint classifications survive both substitutions. A later source can falsify the classification by pushing either input box across the wall.

## Extra-electron chemistry and a historical control

**MEASURED.** All five species have bound ground-state anions. In barium the extra electron occupies 6p in the reported leading configuration. In lanthanum and cerium the extra orbital occupation is 5d. Praseodymium and neodymium gain a 6p electron. The assignments and inputs are recorded in [affinities.csv](affinities.csv). [Ning and Lu 2022](https://doi.org/10.1063/5.0080243)

**DERIVED.** For positive EA and IE1>EA, the chemistry columns use the Pearson finite differences η=(IE1−EA)/2, χ=(IE1+EA)/2 and ω=χ²/(2η). The ratio ω/η=1/(2Γ₀²). Each of the five ratios is below one even at the upper endpoint.

| Element | EA (eV) | z₀ | Γ₀ | η (eV) | χ (eV) | ω/η |
|---|---:|---:|---:|---:|---:|---:|
| Barium | 0.14462(6) | 36.036956 | 0.946000 | 2.5335223 | 2.6781423 | 0.558712 |
| Lanthanum | 0.557546(20) | 10.002583 | 0.818224 | 2.509677 | 3.067223 | 0.746836 |
| Cerium | 0.600160(26) | 9.228539 | 0.804469 | 2.469220 | 3.069380 | 0.772595 |
| Praseodymium | 0.10923(46) | 50.079648 | 0.960845 | 2.680485 | 2.789715 | 0.541580 |
| Neodymium | 0.09748(31) | 56.678293 | 0.965325 | 2.71376 | 2.81124 | 0.536566 |

**MEASURED.** Fu et al. (2020) print the neodymium affinity as both 786.3(26) cm⁻¹ and 0.09748(31) eV. Ning and Lu (2022) retain both reported forms. Direct conversion of the displayed reciprocal-centimetre digits gives 0.0974887752 ± 0.0003223589 eV using hc=1.2398419843320×10⁻⁴ eV cm. Fu’s body, Table IV and conclusion give 0.09749(32) eV, consistent with nearest rounding of these digits. One secondary compilation displays 0.09749(33) eV. Its central value follows the converted digits, and 0.00033 conservatively rounds the displayed uncertainty upward. The last digits do not identify a second measurement. All three eV renderings and both source choices for IE1 are carried in the sensitivity CSV. [Primary photoelectron measurements](https://doi.org/10.1103/PhysRevA.101.022502) · [Compilation displaying the alternative](https://en.wikipedia.org/wiki/Electron_affinity_(data_page))

**SET ASIDE — historical affinity.** Davis and Thompson’s 0.926(24) eV for praseodymium, published online in 2001 and in the 2002 volume, would give z₀=5.90734. Its input box spans 5.75768–6.06497 and crosses the wall. The later Fu measurement, 0.10923(46) eV, puts the entire box at 49.86599–50.29512. Ning and Lu discuss possible line misassignment in the earlier determination and leave the discrepancy’s cause open. Treating the older value as a near-wall discovery would be unsupported. [Earlier measurement](https://doi.org/10.1088/0953-4075/35/1/102) · [Fu et al. 2020](https://doi.org/10.1103/PhysRevA.101.022502)

## Which shell actually opened?

**SOURCE RECORD.** The orbital columns use three consecutive leading ground-shell configurations as tabulated by ASD. They show differences of occupations after relaxation. When several occupations change, + denotes population lost and − denotes population gained, with net loss one. Each comparison checks the electron counts. These are source assignments, including theoretical entries, and a revised assignment changes the interpretation even if the scalar energy ratio survives. See the batch discussion of competing Nd VII assignments.

| Element | k at 54 electrons | z | Configurations indicate |
|---|---:|---:|---|
| Barium | 2 | 3.583009 | 6s removal followed by 5p removal from 5p⁶ |
| Lanthanum | 3 | 2.604642 | 5d removal followed by 5p removal from 5p⁶ |
| Cerium | 4 | 1.776134 | 4f removal followed by 5p removal from 5p⁶ |
| Praseodymium | 5 | 1.425343 | 4f removal, then 5p⁶ → 4f5p⁴ in the ASD configuration model |
| Neodymium | 6 | 1.178571 | ASD assigns 4f²5p⁵ → 4f²5p⁴ → 4f²5p³; the middle state has the electron count of xenon |

**RECOGNISED.** The 54-electron ratios decrease through all five central inputs. The same number of electrons accommodates several different sequences of orbitals. The simple comparator (6/5)² is tied to the first row’s change in principal quantum number. Orbital changes 5d→5p and 4f→5p need their own assignments. For these five ions the argon-count pair is 3d→3p and the krypton-count pair 4d→4p. Blindly applying the (4/3)² and (5/4)² labels would use the wrong initial principal shells. The true 2s→1s pairs give the largest ordinary ratios for all five (4.096048 in barium down to 4.078835 in neodymium). The 3s→2p opening likewise remains present.

**DERIVED.** The closed helium-core opening remains distinct from the *terminal* readout using He-like and H-like ionization energies. Let b and h be those energies in Hartrees, with 1 Hartree=27.211386245981 eV (2022 CODATA). [screening.csv](screening.csv) gives S=(h−b)/Z and σ=Z−√(2b). From barium to neodymium S increases from 0.706285 to 0.720403, and σ decreases from −0.534200 to −0.826734. Both continue away from the low-Z 5/8 value in the opposing directions already found. These rows retain archive isotope/nuclear and spinor terms in the input energies. Extrapolating a single 5/8 screening constant to these charges fails.

**DERIVED.** The weakest assertion about direction needs an endpoint qualification here. For neodymium k=10 the theoretical estimates are 152±8 and 168±8 eV. Their lower ratio is (168−8)/(152+8)=1, although the central ratio is 1.105263. Its reflection can therefore vanish at one allowed corner while the entire box remains inside. No independence probabilities or distribution for the two quoted errors were used.

## Reproduction

Run from the repository root with Python 3.11 or newer. The normal path reads the committed NIST snapshot. The optional fetch queries current ASD, which can change.

```sh
d=research/2026-11-20-element-paper-loop-wall/batch12/ladder
a=data/element_thresholds_20261011.json.gz
python3 "$d/batch12_ladder.py" "$a"
python3 "$d/verify_batch12.py" "$a"
python3 "$d/sensitivity.py" "$a"
python3 "$d/test_false_controls.py" "$a"
# Optional public fetch, to compare the stored snapshot with a future release
python3 "$d/fetch_asd_states.py" /tmp/batch12_current_asd.csv
```

**Falsifiers.** The checker fails on a changed archive digest, missing or repeated charge, mismatched printed energy/grade, last-place ratio error, or an interval that changes side. The frozen ASD comparison fails if the list of source differences changes. The orbital checker verifies counts and flags rearrangements, leaving the spectroscopic assignment open to independent correction. Passing the numerical tests establishes an energy-ladder classification. Bulk transport and crystal topology require the separate observables in this batch.
