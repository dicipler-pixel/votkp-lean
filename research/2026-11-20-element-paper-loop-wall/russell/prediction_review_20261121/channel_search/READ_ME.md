# A state-selected carbon channel and an oxygen fine-structure comparison

**DERIVED.** Six bound final-ion states put an atomic *channel-resolved* ratio between the frozen cutoffs. Five belong to C III and one to O III. All six were found by searching existing spectroscopy. The ground-state ratio remains 2.1654102453 for C and 2.5790114668 for O. These channels supply experimentally identifiable inputs. A physical claim distinguishing the two cutoffs still requires a separately predicted outcome.

## What changes when the outgoing ion is selected

For an atom X, prepare consecutive processes X(g) → X⁺(g) + e⁻ and X⁺(g) → X²⁺(j) + e⁻. Here g means the ground state. The sum of the conventional second removal threshold and the excitation energy of j is the energy threshold for the second channel. For a tabulated level in cm⁻¹,

\[
z_j=\frac{I_2+\tilde\nu_j/8065.543937}{I_1}.
\]

The comparison uses the two positive constants from the ground-state table, \(w=3+2\sqrt2\) and \(c=(7.576234/1.30447+8.15168/1.3895212)/2\). Calling a ratio above a cutoff “outside” specifies a classification. A law for intensity, cross section, or lifetime would be an additional hypothesis.

## Oxygen lets us change J within a term

**MEASURED / EVALUATED.** NIST lists the O III levels below. Pettersson's observations supply an identifying decay line for each triplet member. The wavelengths in the table are the observed vacuum values in UV multiplet 19.23, descending to the 2s²2p3p ³D term. A singlet supplies a reference beyond both cutoffs. **DERIVED.** I₁ = 13.618055(7) eV and I₂ = 35.12112(6) eV give the onsets and ratios. [NIST ASD levels](https://physics.nist.gov/cgi-bin/ASD/energy1.pl?biblio=on&conf_out=on&format=0&j_out=on&lande_out=on&level_out=on&output=0&page_size=15&perc_out=on&spectrum=O+III&submit=Retrieve+Data&term_out=on&unc_out=1&units=0) · [Pettersson, 1982](https://doi.org/10.1088/0031-8949/26/4/007) · [erratum, 1984](https://doi.org/10.1088/0031-8949/29/4/017) · [Moore, 1985, Parts A and B](https://doi.org/10.6028/NBS.NSRDS.3sec11).

| O²⁺ configuration 2s²2p4s, term | Level (cm⁻¹) | Tagged line (Å) | Channel threshold (eV) | Ratio | Geometry | Rival |
|---|---:|---:|---:|---:|---|---|
| ³P°₀ | 356736.30 | 1590.582 | 79.350784 | 5.8268808732 | inside | inside |
| ³P°₁ | 356844.98 | 1591.285 | 79.364259 | 5.8278703392 | inside | inside |
| ³P°₂ | 357117.01 | 1589.973 | 79.397986 | 5.8303470087 | outside | inside |
| ¹P°₁ | 358668.90 | — | 79.590396 | 5.8444760336 | outside | outside |

The three oxygen triplet channels share charge, ionization energies, electron configuration, spin multiplicity and orbital term. Their excitation energy and total angular momentum differ. The closest spacing in the proposed O⁺ photon-onset scan is 0.013475 eV (J=0 versus J=1). The middle-to-upper spacing is 0.033727 eV. Distinct spectral tags can help distinguish channels even when thresholds overlap after instrumental broadening. Relative intensities may also depend on angular-momentum coupling and how the ion was prepared.

## Carbon supplies an optical check

**MEASURED / EVALUATED.** C III has a bound 1s²2p(²P°)3p ¹D₂ level at 333118.21 cm⁻¹. Moore’s multiplet 7 lists Bockasten’s observed decay from that level to 2p3s ¹P°₁ at **4325.560 Å in air**. **DERIVED.** With \(I_1=11.260288(11)\) and \(I_2=24.383143(12)\) eV, the excitation is 41.30139425 eV, the channel onset is 65.68453725 eV and \(z_j=5.8332910537\). This level is more than 6 eV below the C III ionization limit. Four nearby additional C III levels yield the same disagreement, including all three members of 2p3d ³F°. The triplet components share physical origins and should be analyzed as a group. [NIST ASD C III](https://physics.nist.gov/cgi-bin/ASD/energy1.pl?biblio=1&conf_out=1&j_out=1&lande_out=1&level_out=1&perc_out=1&spectrum=C+III&term_out=1) · [Moore, 1970, Parts A and B](https://doi.org/10.6028/NBS.NSRDS.3sec3).

## Uncertainty and scoring

For a rectangular error budget, write \(A=I_1\pm dA\), \(I=I_2\pm dI\), and let \(u\) be a certified two-sided error in the excited level in cm⁻¹. A geometric-outside and midpoint-inside result is safe if

\[
 8065.543937\,[w(A+dA)-(I-dI)] < \tilde\nu-u,\qquad
 \tilde\nu+u < 8065.543937\,[c(A-dA)-(I+dI)].
\]

Neither of the two cited ASD display tables supplies individual uncertainties for the chosen levels. The carbon ¹D₂ case retains its calls for any certified \(u<356.71765\) cm⁻¹. Oxygen J=2 retains its calls for \(u<210.06133\) cm⁻¹. The tighter oxygen J=1 agreement control tolerates \(u<60.34266\) cm⁻¹. Result.csv reports calculated limits on tolerable error. The printed digits facilitate numerical reproduction.

**Operational significance.** Detecting 4325.560 Å or 1589.973 Å in a discharge identifies a decay channel. Its feeding mechanism requires additional measurements. A state-selected threshold measurement would require a ground-state parent-ion beam, calibrated photon energy, and a way to control metastables and cascades or tag the emitted electron at the channel onset. We have not identified a measurement of these particular state-tagged ion-production cross sections. A successful threshold scan would test the spectroscopic energy bookkeeping. A physical wall test also needs the model to specify what independent observable changes, how much, and in which direction before inspecting it. The known fluorescence wavelengths can identify the states whichever cutoff is preferred.

## Search accounting and reproduction

We screened 55 neutral NIST-derived snapshots from a third-party Grotrian compilation. Its coverage emphasizes levels participating in strong lines. We also screened 83 spectroscopic files from CHIANTI for available ions of charges 1–6, across 18 elements. We retained the observed energy column, required positive excitation below that ion's ground ionization threshold, and required both neighboring removal energies. We tried both a bound excited intermediate, \(z=(I_{k+1}-E)/(I_k+E)\), and a bound excited final ion, \(z=(I_{k+1}+E)/I_k\). The 2,452 neutral and 5,244 ionic intermediate contributions gave no matches. Among 5,008 final contributions, six matched. These are channel tests, with levels reused between roles. The NIST references above refine the coarser CHIANTI wavenumbers for the six matches. Many other spectra and states lie outside the screened snapshots. [CHIANTI C III](https://db.chiantidatabase.org/c/c_3.html) · [CHIANTI reference for data columns](https://www.chiantidatabase.org/tech_reports/01_elvlc/chianti_report_1.pdf) · [third-party neutral-level compilation](https://github.com/Muuuun/atom-energy-levels/tree/5fdce8c038db1a92b37faa552f9437633647e2ba).

Given the pinned archive, reproduce the nine primary-data rows offline. Given the H–At thresholds and a download cache, reproduce the broader screen. Each downloaded file is verified against its pinned Git object ID. The search hits retain the source ordering.

    python check.py /path/to/element_thresholds_20261011.json.gz
    python screen_levels.py /path/to/H_to_At_thresholds.csv /path/to/level-cache
