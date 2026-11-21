# Nb–Rh independent source check

Read on 21 November 2026. The five official eV tables all identify NIST ASD v5.12 (2024). They were collected separately from the pinned archive and the candidate CSV. The dated capture is in `nist_nb_rh_20261121.csv`, with energy brackets/parentheses preserved and thousands spaces removed. The Mo table uses the isoelectronic sequence column, from neutral Mo through H-like Mo, to identify its charge. The other tables explicitly display ion charge. [NIST ASD](https://doi.org/10.18434/T4W30F)

| Official table | Date on the NIST result | Rows |
|---|---|---:|
| [Nb](https://physics.nist.gov/cgi-bin/ASD/ie.pl?at_num_out=1&biblio=1&e_out=0&el_name_out=1&ion_charge_out=1&spectra=niobium&unc_out=1&units=1) | Nov 18 | 41 |
| [Mo](https://physics.nist.gov/cgi-bin/ASD/ie.pl?at_num_out=on&biblio=on&e_out=0&el_name_out=on&level_out=on&seq_out=on&shells_out=on&spectra=Mo&unc_out=on&units=1) | Nov 18 | 42 |
| [Tc](https://physics.nist.gov/cgi-bin/ASD/ie.pl?at_num_out=1&biblio=1&e_out=0&el_name_out=1&ion_charge_out=1&spectra=technetium&unc_out=1&units=1) | Nov 21 | 43 |
| [Ru](https://physics.nist.gov/cgi-bin/ASD/ie.pl?at_num_out=1&biblio=1&e_out=0&el_name_out=1&ion_charge_out=1&spectra=ruthenium&unc_out=1&units=1) | Nov 18 | 44 |
| [Rh](https://physics.nist.gov/cgi-bin/ASD/ie.pl?at_num_out=1&biblio=1&e_out=0&el_name_out=1&ion_charge_out=1&spectra=rhodium&unc_out=1&units=1) | Nov 18 | 45 |

**DERIVED.** The pinned archive and public ASD agree in all 215 numerical energy values, all 215 uncertainty fields, all 215 bracket-derived grades and all 215 reference strings. Seven individual energy uncertainties are unavailable, at Nb IE₂/IE₃, Tc IE₂/IE₃, Ru IE₃ and Rh IE₂/IE₃. Eleven ordinary ratios depend on at least one of these energies. One further unavailable uncertainty interval comes from Tc EA. The uncertainty comparisons count corresponding blank fields as matches.

**DERIVED.** A separate audit read the finished 220-row ladder, checked every energy against the public table or named affinity source and computed both displayed six-place fields from exact fractions. All 210 ordinary ratios are inside. All four measured anion ratios are outside. Tc is also outside conditional on its calculated affinity.

| Element | EA used, eV | Evidence |
|---|---:|---|
| Nb | 0.91740(7) | Ning & Lu (2022), Table I. The original 2016 SEVI study reports 0.91740(6) eV. The slightly wider 2022 uncertainty is carried here. [2016 measurement](https://doi.org/10.1103/PhysRevA.93.020501) |
| Mo | 0.74723(8) | Ning & Lu (2022), Table I, list a SEVI measurement. Their reference 206 is explicitly described as unpublished. The numerical source for this check is the published evaluation. [2022 evaluation](https://doi.org/10.1063/5.0080243) |
| Tc | 0.636, predicted | O’Malley & Beck (2002) predict a 636 meV ground-state binding using relativistic configuration interaction. Ning & Lu list the entry as calculated/semiempirical. No experimental threshold or numerical measurement uncertainty was located. [2002 prediction](https://doi.org/10.1103/PhysRevA.65.064502) |
| Ru | 1.046270(20) | Ning & Lu (2022), Table I, give a SEVI value under the same unpublished reference 206. [2022 evaluation](https://doi.org/10.1063/5.0080243) |
| Rh | 1.14273(5) | Chen et al. (2026) update the earlier evaluated 1.14289(20) eV. Both place the row outside. [2026 measurement](https://doi.org/10.1088/1674-1056/ae5173) |

**Test for Tc.** For a bound anion on the forward branch, an EA below IE₁/(3+2√2) puts rung 0 outside. An independently measured EA above this value but below IE₁ would defeat the predicted outside classification. An unbound ground-state anion would remove the rung entirely. This is an empirical test for the provisional datum.

Run independently of the calculation script:

```sh
python3 verify_nb_rh.py /path/to/element_thresholds_20261011.json.gz nist_nb_rh_20261121.csv /path/to/batch9_nb_rh.csv
```
