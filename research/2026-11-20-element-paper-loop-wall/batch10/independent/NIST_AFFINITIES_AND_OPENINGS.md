# Palladium through tin: source and opening checks

**DERIVED.** A second reading of five official NIST Atomic Spectra Database v5.12 (2024) output tables agreed with the pinned archive on all 240 central ionization energies, 240 uncertainty fields, 240 bracket-derived source grades and 240 reference strings. The one unreported uncertainty is for the third ionization energy of palladium (32.93 eV, q=2). The final 245-row ladder was independently checked from the saved official rows and separate affinity values. All 235 ordinary steps are inside. Outside steps occur only at the anion rungs of palladium, indium and tin. The measured silver anion rung is inside. Cadmium has no bound ground-state rung. [NIST ASD](https://doi.org/10.18434/T4W30F)

The energy tables were retrieved 21 November 2026. Their printed output dates are November 21 for palladium and November 18 for silver, cadmium, indium and tin. The separate configuration queries in the last column were used for the 240 individual ground configurations and terms in `asd_configurations.csv`. Query by increasing charge q and check each row's isoelectronic atom; q=0 denotes the neutral atom.

| Element | Ionization energies, errors, references | Ground states, energies and isoelectronic sequence |
|---|---|---|
| Palladium | [Official energy rows](https://physics.nist.gov/cgi-bin/ASD/ie.pl?at_num_out=1&biblio=1&e_out=0&el_name_out=1&ion_charge_out=1&spectra=palladium&unc_out=1&units=1) | [Official configurations](https://physics.nist.gov/cgi-bin/ASD/ie.pl?at_num_out=on&biblio=on&e_out=0&el_name_out=on&level_out=on&seq_out=on&shells_out=on&spectra=Pd&unc_out=on&units=1) |
| Silver | [Official energy rows](https://physics.nist.gov/cgi-bin/ASD/ie.pl?at_num_out=1&biblio=1&e_out=0&el_name_out=1&ion_charge_out=1&spectra=silver&unc_out=1&units=1) | [Official configurations](https://physics.nist.gov/cgi-bin/ASD/ie.pl?at_num_out=on&biblio=on&e_out=0&el_name_out=on&level_out=on&seq_out=on&shells_out=on&spectra=Ag&unc_out=on&units=1) |
| Cadmium | [Official energy rows](https://physics.nist.gov/cgi-bin/ASD/ie.pl?at_num_out=1&biblio=1&e_out=0&el_name_out=1&ion_charge_out=1&spectra=cadmium&unc_out=1&units=1) | [Official configurations](https://physics.nist.gov/cgi-bin/ASD/ie.pl?at_num_out=on&biblio=on&e_out=0&el_name_out=on&level_out=on&seq_out=on&shells_out=on&spectra=Cd&unc_out=on&units=1) |
| Indium | [Official energy rows](https://physics.nist.gov/cgi-bin/ASD/ie.pl?at_num_out=1&biblio=1&e_out=0&el_name_out=1&ion_charge_out=1&spectra=indium&unc_out=1&units=1) | [Official configurations](https://physics.nist.gov/cgi-bin/ASD/ie.pl?at_num_out=on&biblio=on&e_out=0&el_name_out=on&level_out=on&seq_out=on&shells_out=on&spectra=In&unc_out=on&units=1) |
| Tin | [Official energy rows](https://physics.nist.gov/cgi-bin/ASD/ie.pl?at_num_out=1&biblio=1&e_out=0&el_name_out=1&ion_charge_out=1&spectra=tin&unc_out=1&units=1) | [Official configurations](https://physics.nist.gov/cgi-bin/ASD/ie.pl?at_num_out=on&biblio=on&e_out=0&el_name_out=on&level_out=on&seq_out=on&shells_out=on&spectra=Sn&unc_out=on&units=1) |

## Bound-anion inputs and the special palladium boundary

**MEASURED.** Ning and Lu's 2022 evaluation supplies palladium 0.56214(12), silver 1.30447(2), indium 0.38392(6), and tin 1.112070(2) eV. These values refer to detachment from the ground-state anion. Its cadmium entry gives a negative affinity sign from electron scattering and accelerator mass spectrometry. Using zero as a denominator would manufacture an undefined rung. [2022 evaluation](https://doi.org/10.1063/5.0080243) · [palladium](https://doi.org/10.1103/PhysRevA.58.2051) · [silver](https://doi.org/10.1088/0953-4075/31/17/013) · [indium](https://doi.org/10.1103/PhysRevA.82.032507) · [tin](https://doi.org/10.1088/0953-4075/46/12/125002)

**DERIVED.** Palladium's ground anion is [Kr]4d¹⁰5s. Its neutral atom is [Kr]4d¹⁰, and its succeeding cations start [Kr]4d⁹ and [Kr]4d⁸. Consequently k=0 compares 5s detachment with 4d removal, z=14.830539, outside. It is simultaneously the anion rung and the filled-4d opening. The first ordinary rung k=1 compares successive 4d removals, z=2.330620, inside. Silver, cadmium, indium and tin expose the filled 4d subshell at ordinary k=1,2,3,4 respectively, each via 5s→4d. An excited anion has a different initial state. [Ground-state palladium-ion study](https://doi.org/10.1021/acs.jpclett.8b03859)

**DERIVED.** Silver's near-wall rung uses z₀=7.576234/1.30447=5.807902, Γ₀=0.706224. Dividing opposite uncertainty endpoints gives [5.807793850,5.808010273], entirely below 5.828427125. At fixed central IE₁ the critical positive EA is 1.299876251 eV. The measured affinity exceeds that critical value, placing silver inside. The weakly bound ground anions of indium and tin give z₀=15.071775 and 6.603827. Each is outside.

## Orbital changes at the deeper openings

**DERIVED.** For each element, an m-electron filled core is exposed after ordinary removal k=Z−m. The ground configurations immediately before, at and after this charge specify both removals. These transitions occur across all five elements:

| Retained electrons | Boundary | Removed orbitals | Bare principal-shell ratio |
|---:|---|---|---:|
| 46 | 4d¹⁰ | 5s → 4d, including the palladium anion case | 25/16 |
| 36 | Krypton core | 4d → 4p | 1 |
| 28 | 3d¹⁰ | 4s → 3d | 16/9 |
| 18 | Argon core | 3d → 3p | 1 |
| 10 | Neon core | 3s → 2p | 9/4 |
| 2 | Helium core | 2s → 1s | 4 |

The bare ratios use only principal quantum numbers. Archive energies determine the actual ratios. Complete ground shells at each charge accompany this note, including indium and tin neutral configurations [Cd]5p and [Cd]5p². The cadmium abbreviation in these shells represents [Kr]4d¹⁰5s².

## Reproduce

```sh
python3 verify_pd_sn.py /path/to/element_thresholds_20261011.json.gz nist_pd_sn_20261121.csv /path/to/batch10_pd_sn.csv
```

The verifier enforces the exact archive digest at bcedbd9bba0de5a75fd2a860a912ebc4882f4e8a, counts every charge, recognizes bound and unbound rows, compares the archive to the separately saved tables, and rederives each printed fraction by integer rounding.
