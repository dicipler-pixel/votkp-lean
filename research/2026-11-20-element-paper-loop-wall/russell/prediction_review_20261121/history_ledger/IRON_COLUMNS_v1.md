# What are the lines in Russell’s three iron columns?

Jeromie Beasley’s *What Russell Saw* explicitly leaves this question open in Appendix C. The original claim record is **U240**. The 1926 plate gives 23 wavelengths in each of three columns. In a comparison of all 69 printed values with observed neutral-iron lines, **21 of 23** in the first column, **20 of 23** in the second and **19 of 23** in the third fall within 0.20 Å. Laboratory transitions of neutral iron occur throughout the purported chronological sequence. Nine entries fall outside this tolerance. [Beasley’s public edition and supplement](https://zenodo.org/records/22986657) · [Russell’s 1926 plate, printed p. 204](https://tile.loc.gov/storage-services/service/gdc/gdclccn/27/00/45/08/27004508/27004508.pdf#page=224)

## The question Russell actually asked

On pp. 202–204 Russell treats colour as a record of material development. He assigns lines to iron’s present state, its immediate associates, and progressively earlier stages. He also connects their position to the atom’s tendency to charge or discharge. The test asks whether an ordinary neutral-iron spectrum supplies lines in all three categories. It does. To test an additional ancestry interpretation, one would need an independently measured history variable and a rule assigning fresh spectra to histories before looking at their labels. No such measurement is reported on these pages. [Russell, pp. 202–204](https://tile.loc.gov/storage-services/service/gdc/gdclccn/27/00/45/08/27004508/27004508.pdf#page=222)

The preceding paragraph and table disagree. Printed p. 203 gives 7817.2, 7392.3 and 6944.8 Å. The heads of the three p. 204 columns give 7181.8, 6916.8 and 6944.8 Å. The table drives the 69-value calculation. All three prose examples separately fall outside ±0.20 Å in our observed Fe I list. A later edition of *The Secret of Light* uses the three table values in the prose as well. Its title matter dates the original work to 1947 and includes a 1971 preface documenting revisions, so the date of that correction remains open. [1926 prose, p. 203](https://tile.loc.gov/storage-services/service/gdc/gdclccn/27/00/45/08/27004508/27004508.pdf#page=223) · [Later edition, Spectrum Analysis](https://avalonlibrary.net/ebooks/Walter%20Russell%20-%20The%20Secret%20of%20Light.pdf)

## Frozen comparison

I read the original plate image and extracted its text by printed column, keeping the one-decimal entries, the order and the intensity stars. Before calculating the hits I recorded the primary tolerance, translation controls, competing spectra and scale sensitivities in [the protocol](iron_protocol_v1.md), SHA-256 `c757ae3537bfb88d0cf84ceccac38aeb41ec87aacdc0b9932be9bade4e7114f0`. I had already seen several possible Fe I matches named by Beasley and examples in reference sources. This is a retrospective test with fixed calculation rules. It provides no prospective element prediction.

The computational reference is an archived NIST extraction at `decde260a4a0eda864f510352ccf5dcea631ac25` (2019). Its source code selects observed wavelengths carrying positive reported relative intensity. The wavelength range is 3400–8100 Å, under the visible/near-infrared air convention. I separately recovered the original measured line list in Nave et al. (1994), Table 4, from the published 239-page article. An independent NIST Handbook compilation supplies a smaller list of strong lines. The sources share underlying laboratory observations, so agreement checks extraction and identification across presentations, without constituting three independent experiments. [Pinned observed line list](https://github.com/astro-data/nist_atomic_lines_package/blob/decde260a4a0eda864f510352ccf5dcea631ac25/nist_library/NIST_ELEMENTS/Fe/Fe_I.dat) · [Nave et al. 1994, Table 4](https://articles.adsabs.harvard.edu/pdf/1994ApJS...94..221N) · [NIST strong lines](https://physics.nist.gov/PhysRefData/Handbook/Tables/irontable2.htm)

| Comparison at ±0.20 Å, zero offset | Reference lines in the window | Iron, out of 23 | Recent, out of 23 | Remote, out of 23 |
|---|---:|---:|---:|---:|
| Fe I, intensity-bearing observations | 3,170 | **21** | **20** | **19** |
| Fe I, extracted lines of Nave et al. Table 4 | 3,160 | **21** | **20** | **19** |
| Fe II | 1,689 | 2 | 4 | 2 |
| Ni I | 150 | 1 | 0 | 1 |
| Ti I | 1,635 | 5 | 5 | 1 |
| NIST Handbook strong Fe I only | 102 | 1 | 4 | 2 |

Each printed number contributes at most one hit per reference, including near blends. All 69 nearest wavelengths agree between the archived Fe I extraction and our Table 4 extraction to better than 0.001 Å. Table 4 also gives a multiplet number for each retrieved counterpart. Our extraction required optical wavelength/wavenumber consistency and may omit unreadable PDF entries. A match specifies wavelength compatibility, and an assignment may still be blended. NIST’s compilation lists *recent* 5227.3 within tolerance of 5227.1509 Å, for example, while the nearest Fe I line in the larger list is 5227.1891 Å. [All 69 values and prose check](iron_wavelengths_v1.csv) · [Laboratory multiplet numbers](iron_nave_v1.csv)

In the translation control, the entire set of 23 values moved together by every integer displacement from −50 to −5 and +5 to +50 Å. This keeps local line densities and wavelength clustering approximately intact. For the 92 translations the Fe I hit medians were 7, 5 and 5, and the maxima were 12, 12 and 10. All three unshifted counts exceed every translated score. With the unshifted case counted the descriptive tail fraction is 1/93 in each column. The translations are dependent. Statistical significance for a general population of possible plates would require a separate sampling model. [Full tolerance, offset and species controls](iron_controls_v1.csv)

## What an observer could have known before 1926

H. Kayser’s 1910 paper reports plate measurements of an iron arc, alongside older Rowland wavelengths on a different scale. There are concrete examples in **every** Russell column where the earlier Rowland entry rounds to the printed tenth. Russell’s acquisition source remains unknown. [Kayser 1910, pp. 217–222](https://articles.adsabs.harvard.edu/pdf/1910ApJ....32..217K)

| 1926 column | Russell, Å | Kayser’s iron arc, Å | Rowland entry in Kayser, Å | Nave et al., Å | Nave multiplet |
|---|---:|---:|---:|---:|---:|
| Iron | 4859.9 | 4859.754 | 4859.928 | 4859.7414 | 692 |
| Recent | 5191.6 | 5191.477 | 5191.629 | 5191.4550 | 792 |
| Remote | 5328.2 | 5328.040 | 5328.236 | 5328.0387 | 88 |

Another entry makes the point without a scale fit. Russell’s remote line at **5269.6 Å** coincides to his printed precision with the solar Fraunhofer E line identified as **iron at 5269.551 Å** in Charles Greeley Abbot’s *The Sun*, published in September 1911, Table III, p. 89. Nave et al. identify 5269.5374 Å in multiplet 88. The same multiplet supplies Russell’s remote 5328.2 Å entry. [Abbot 1911, Table III](https://upload.wikimedia.org/wikipedia/commons/1/10/The_sun_%28IA_cu31924004973628%29.pdf) · [Nave et al. 1994](https://articles.adsabs.harvard.edu/pdf/1994ApJS...94..221N)

**Wavelength conventions matter.** Kayser recommended subtracting roughly 0.19 Å from Rowland-scale wavelengths and documented wavelength-dependent differences. A 1911 analysis adopted −0.16 Å for its own range. We prespecified both as sensitivity tests. At ±0.20 Å, subtracting 0.16 brings all three columns to 21/23; subtracting 0.19 gives 21/23, 20/23 and 21/23. At the tighter ±0.10 Å, subtracting 0.16 gives 20/23, 18/23 and 21/23. With no offset and tolerance ±0.05 Å, just 2/23, 3/23 and 1/23 match. The primary result remains 21, 20 and 19 at ±0.20 with zero shift. We found no stated calibration for Russell’s own table and no evidence for a pole-dependent correction. [Kayser 1910](https://articles.adsabs.harvard.edu/pdf/1910ApJ....32..217K) · [1911 calibration discussion, p. 669](https://articles.adsabs.harvard.edu/pdf/1911MNRAS..71..663S)

## What remains open

The nine unshifted misses are 7181.8 and 4057.9 Å in the iron column; 6827.8, 5455.2 and 4982.7 Å in recent; and 6944.8, 5983.1, 5476.8 and 5415.4 Å in remote. Two miss by especially small amounts, 4982.7 by a residual of 0.2004 Å and 5415.4 by 0.2011 Å. The protocol retains both as misses. This research pass establishes ordinary iron transitions throughout the table. Russell’s column assignment, unique identifications for the remaining values and the physical test of the proposed histories remain open.
