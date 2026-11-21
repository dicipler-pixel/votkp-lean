# Independent check against the public NIST tables

On 21 November 2026, the five NIST Atomic Spectra Database tables below were read independently of the VOTKP archive and the generated ladders. Each table reported version 5.12 (Kramida et al., 2024). The retrieval returned recent rendered public pages. We preserved their energy punctuation and reference IDs, joined on atomic number and ion charge and compared the four fields. This checks data transcription and provenance. The two collections share the same underlying evaluation.

| Public NIST table (eV) | Output date in NIST citation | Rows |
|---|---|---:|
| [Krypton](https://physics.nist.gov/cgi-bin/ASD/ie.pl?at_num_out=1&biblio=1&e_out=0&el_name_out=1&ion_charge_out=1&spectra=krypton&unc_out=1&units=1) | 18 November 2026 | 36 |
| [Rubidium](https://physics.nist.gov/cgi-bin/ASD/ie.pl?at_num_out=1&biblio=1&e_out=0&el_name_out=1&ion_charge_out=1&spectra=rubidium&unc_out=1&units=1) | 18 November 2026 | 37 |
| [Strontium](https://physics.nist.gov/cgi-bin/ASD/ie.pl?at_num_out=1&biblio=1&e_out=0&el_name_out=1&ion_charge_out=1&spectra=strontium&unc_out=1&units=1) | 20 November 2026 | 38 |
| [Yttrium](https://physics.nist.gov/cgi-bin/ASD/ie.pl?at_num_out=1&biblio=1&e_out=0&el_name_out=1&ion_charge_out=1&spectra=yttrium&unc_out=1&units=1) | 21 November 2026 | 39 |
| [Zirconium](https://physics.nist.gov/cgi-bin/ASD/ie.pl?at_num_out=1&biblio=1&e_out=0&el_name_out=1&ion_charge_out=1&spectra=zirconium&unc_out=1&units=1) | 18 November 2026 | 40 |

The checked CSV records these public values in NIST's displayed precision, with only spacing removed. Square brackets identify semiempirical entries (S) and parentheses theoretical entries (T). Other entries use the archive code E. All 190 energies, 190 uncertainty fields, 190 grades and 190 reference strings agree with archive commit `c35b18b1c577bde90eacd3ef7cfa1bb2bb93024f`. Energy and uncertainty comparisons use decimal numbers. For example, `[23.170]` and 23.17 eV agree numerically while the S grade remains visible. One matched uncertainty field is empty. The separate electron affinities fall outside this check. [NIST ASD](https://doi.org/10.18434/T4W30F)

Run the following with the path to the repository's pinned archive and the saved NIST snapshot:

```sh
python3 check_nist_snapshot.py /path/to/data/element_thresholds_20261011.json.gz nist_kr_zr_20261121.csv
```

## Zirconium's two unresolved uncertainty boxes

The official Zr II entry lists **13.13 eV**, reference **L272**, and gives a blank uncertainty. Its footnote explicitly identifies unknown uncertainties. The level table attributes the ionization limit to C. E. Moore (1970), whose Table 2 lists **105900 cm⁻¹** without a row-specific numerical error bar. Moore explains that the two- and one-decimal-place entries have less well-defined accuracy. The separate NIST Handbook gives **106000 cm⁻¹ (13.1 eV)**, citing S. Johansson's unpublished 1998 work. Their difference does not supply a confidence interval. Both affected uncertainty fields stay open pending an evaluation with an explicit error estimate. [Moore's original tables](https://doi.org/10.6028/NBS.NSRDS.34) · [Handbook value](https://physics.nist.gov/PhysRefData/Handbook/Tables/zirconiumtable1.htm) · [Handbook bibliography](https://physics.nist.gov/PhysRefData/Handbook/Tables/zirconiumtable7.htm)

**Derived sensitivity calculation.** Let t = 3 + 2√2 and x = IE₂. The two-sided condition Γ² < 1/2 is 1/t < z < t. For Zr k=1, z=x/IE₁. To stay strictly inside for every allowed IE₁, it suffices and is necessary that IE₁,high/t < x < t·IE₁,low. For k=2, z=IE₃/x, giving IE₃,high/t < x < t·IE₃,low. The joint lower endpoint is the larger lower bound, the upper endpoint is the smaller upper bound. Substituting IE₁=6.634126±0.000005 eV and IE₃=23.170±0.004 eV gives

```
23.174/t < x < 6.634121*t
3.97602981113179… eV < x < 38.6664907852483… eV.
```

Within that window both individual wall labels stay strictly inside throughout the **reported** neighbouring uncertainty ranges. At either exact endpoint one extremal ratio lies on the wall. This calculation describes how far the unknown energy could move before classification becomes sensitive. It assigns no uncertainty to x.
