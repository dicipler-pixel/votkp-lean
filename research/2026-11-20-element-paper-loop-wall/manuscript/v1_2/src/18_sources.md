## Appendix E. Sources, reproducibility and credit

**Where it lives.** Everything in this paper — the paper's sources, the threshold archive, the batch records, the Lean files, the check scripts and their outputs, the review exchanges and the failed tests — is on GitHub at `dicipler-pixel/votkp-lean`, branch `element-paper/loop-wall`, folder `research/2026-11-20-element-paper-loop-wall/`, pinned for this edition at commit 02515d0. The interactive *Periodic Table of Elemental Peels* (v1.1) and its data package are deposited on Zenodo (record 24432624).

**What can be checked.** The 85-element inventory and the full threshold table are complete for the stated pins. All 3,655 positive-index removals and all 85 anion slots are in `H_to_At_thresholds.csv`, with missing affinities and missing uncertainty boxes left explicit. The element evidence is frozen at the branch commits named in the record; later amendments to the live branch belong to later editions. Each check script prints its own header and writes its output beside it. The proofs concern mathematical objects and encoded values; a reconstruction checks code against source; a measured comparison needs independent experimental information. Agreement between two scripts reading the same NIST-derived input checks the transformation, not the underlying spectroscopic measurement.

**Coverage boundary.** The companion batch files hold material properties, spectra, nuclear cases and crystal phases with uneven coverage. No claim is made of an exhaustive evaluated handbook of every isotope, phase, pressure, thermal history and optical band for all 85 elements. No universal element-to-knot assignment, nuclear decay rate, bulk transport law or experimental realisation of an elementary knot follows from this edition. Radon onward, the final polonium uncertainty budget and francium's second ionisation energy remain open.

**My own sources.** *The Dirac Time of the Gigantefermion*, long form v3.0.1 (25 September 2026) and v3.1 (26 September 2026); *VOTKP: The Vector of Traits Kept under Peeling*, v2.9 (13 October 2026) and the v3.0–v3.3 editions (12 November 2026); *The Volume of the Knot Potential: Decay and Direction on the Vacuum Disk* (7 November 2026, and v6); *Two Trees in One Ball* v4; *Intrinsic Quantum Geometric Tensor* (v7.3); *Universal Projector Geometry from Electrical Measurements* (v3.2); *Non-Normality Is Connection Energy* (Zenodo concept 10.5281/zenodo.22803572); *The Offset Belongs to the Boundary* (v31); *What Transport Keeps* (edition 3); *The Offset Speed Limit* and *The Weight Between* (v1.1, 26 October 2026); *The Ledger Outlives the Metric* (edition 7); *Matter at a Scale* (v5); *What Russell Saw* and *Russell, Corrected* (November 2026); *A Five-Dimensional Non-Normal Stability Operator with Gradient-Driven Interface Coupling for Zero-Precursor Filamentary Fractures* (17 September 2026); the ball folders on the moving-matrix branch; my November working notes and harness records.

**Data and published sources.**

- NIST Atomic Spectra Database v5.12 (2024), through the archive `data/element_thresholds_20261011.json.gz`.
- C. Ning and Y. Lu, atomic electron affinities (2022); arsenic, *Phys. Rev. Lett.* 134, 043001 (2025); selenium, *J. Chem. Phys.* 164, 054303 (2026); yttrium, *J. Chem. Phys.* 158, 084303 (2023); zirconium, *J. Chem. Phys.* 147 (2017); rhodium, *Chin. Phys. B* 35, 063202 (2026); polonium, preliminary JyvIS photodetachment fits.
- V. A. Yerokhin and V. M. Shabaev (2015); V. A. Yerokhin, V. Patkóš and K. Pachucki (2022): hydrogen-like and helium-like components.
- Crystallography Open Database records 1539039 (β-manganese), 1534711 (trigonal selenium), 2020222 (trigonal tellurium).
- R. G. Parr and R. G. Pearson, *J. Am. Chem. Soc.* 105, 7512 (1983).
- R. G. Parr, L. von Szentpály and S. Liu, "Electrophilicity index", *J. Am. Chem. Soc.* 121, 1922 (1999).
- C. Lyu, C. H. Keitel and Z. Harman, "Periodic table for highly charged ions", *Phys. Rev. Research* 7, L042071 (2025).
- K. Pineda-Urbina, "A ΔSCF-DFT donor–acceptor descriptor map for main-group atoms", *Atoms* 14, 48 (2026).
- J. Washburn, M. Simons and E. Allahyarov, "A noble-gas-centered coordinate for within-period atomic property trends", arXiv:2605.00028 (2026).
- R. Resta and S. Sorella, *Phys. Rev. Lett.* 82, 370 (1999); I. Souza, T. Wilkens and R. M. Martin (2000); R. Resta (2006); Onishi and Fu (2025).
- A. Otero-de-la-Roza, Á. Martín Pendás and E. R. Johnson, *J. Chem. Theory Comput.* 14, 4699 (2018).
- L. D. Barron, *Chem. Phys. Lett.* 123, 423 (1986); T. Furukawa et al., *Nat. Commun.* 8, 954 (2017).
- Z. Zimborás et al., chiral quantum walks (2013).
- N. Shiraishi, K. Saito and H. Tasaki, power–efficiency trade-off (2016); P. Pietzonka and U. Seifert, power, efficiency and constancy (2018).
- G. Nave et al., *Astrophys. J. Suppl.* 94, 221 (1994); H. Kayser, *Astrophys. J.* 32, 217 (1910); C. G. Abbot, *The Sun* (1911); W. Russell, *The Universal One* (1926); N. Bohr (1922).
- A. Müller et al. (2009); Al Shorman et al. (2013); McLaughlin et al. (2017); Crandall et al. (1979): lithium-like resonance strengths.
- Schweiger et al. (2024), holmium–dysprosium Penning-trap ratios; Jung et al. (1992), bound-state beta decay of bare dysprosium-163; storage-ring thallium-205 (2024); bare rhenium-187 lifetime (1996) and rhenium–osmium mass difference (2021).
- Moon et al. (1983); Storm et al. (2026); Laporte et al. (1987); Harvey and Lemmon (2005); Pettersson (1982) and Moore, NBS O III tables (1985); E. Toffoli (2022); KnotInfo database 2026.9.1.

**Credit.** I originated the research programme, both readings of VOTKP, Dirac Time, the ball reading, the loop wall and the questions this paper asks. Elizabeth Johnson co-authored the colour section. The element data passes were run with ChatGPT and Codex (OpenAI); every number was rechecked against the archive and the results formalised in Lean with Claude (Anthropic). The source records keep the individual attributions of each check.

**Licence.** Text CC BY 4.0. Code, Lean, scripts and data files MIT. Credit Jeromie Beasley.
