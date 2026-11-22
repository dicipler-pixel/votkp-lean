# Which part of Russell’s element table survives a reflection?

**Jeromie’s two Russell papers make a testable distinction.** The size of a normal short-period valence is preserved when lithium and fluorine, beryllium and oxygen, or boron and nitrogen exchange places. Each pair nevertheless falls on opposite sides of Beasley’s helium-core opening wall. We recovered the full underlying Russell ledger, tested exactly which reflection leaves those valences unchanged, and checked a separate iron-spectrum question that the September paper had left open. The historical papers provide both genuine positional successes and controls where the same type of observable gives a wrong reading. [Beasley’s September paper and source deposit](https://zenodo.org/records/22986657) · [Element data and calculations](octave_core_openings_v1.csv) · [Iron results](IRON_COLUMNS_v1.md)

## What was read and counted

I read *What Russell Saw* and *Russell, Corrected*, including the latter’s own statement that Plate II is a reading and that its even/odd split has not been applied to the 386 claims. I recovered `ledger_read3.md`, `laws_uo.py` and `laws_class.py` from the public version-specific September package. I verified the publisher’s zip MD5 `928702b5b738debce6ac43a36f06eb62` and independently hashed all three files. The GitHub Lean repository contains the mathematical checks, while the item-level historical records are in the published supplement. [Versioned package](https://zenodo.org/records/22986657) · [Lean repository, commit `258d89f`](https://github.com/dicipler-pixel/what-russell-saw-lean/tree/258d89f94354d13371b7371d9de5c5b9c1f4433b)

| Original source | Positions checked | Holds | Partly | Fails | No truth value | Cross-reference with no separate grade | Distinct IDs in this review |
|---|---:|---:|---:|---:|---:|---:|---:|
| *Genero-Radiative Concept* claim ledger | 104 | 31 | 35 | 32 | 6 | 0 | 13 |
| *The Universal One* claim ledger | 282 | 94 | 78 | 97 | 10 | 3 | 96 |
| *The Universal One*, appendix laws | 199 | 21 | 46 | 21 | 111 | 0 | 23 |
| Total original positions | 585 | 146 | 159 | 150 | 127 | 3 | **132** |

**These are the author’s grades.** Grouping compound grades such as `T/P` by their first letter reproduces Appendix C exactly. The original qualified grades remain in the row-level crosswalk. The three ungraded references are U222, U273 and U282. Some entries restate others, and U282 explicitly points to the 199-law appendix. Adding the 386 and 199 counts original positions, without implying 585 independent observations. [Source verification log](source_audit_v1.txt) · [Source audit program](audit_sources.py)

**Selection and coverage.** A reproducible screen for unambiguous element names and element, isotope, octave, spectrum, valence, and related terms ran on the claim part of each of the 585 records. We reviewed all **107** literal hits. A further **25** contextual additions include the formula at U54, seven laws associated with a single salt-displacement example, isotope/ionization-adjacent controls and charge-sign cases. This yields **132 unique original IDs** and **133 annotated reading rows**, because G67 contains two distinguishable readings. Some literal matches concern planets or the ordinary word *element*. They are marked as such. The selection is a reproducible element-focused sample with contextual additions. The other **453 positions have no parity grade here**. Relevance is interpretive and this method could miss other pertinent records. No full-corpus parity success rate, precision or recall follows from these counts. [Row-keyed crosswalk](element_crosswalk_v1.csv) · [Human annotations](element_readouts_v1.tsv)

## Give the operation before the sign

Beasley’s atlas B202 concerns the effect of transposition on two matrix-based quantities. For an atomic or historical claim, one must exhibit its directed data and identify how this operation acts on it before assigning an even or odd reading. B199 applies to a real traceless two-dimensional block under a stated quadratic form. A vacancy, a melting point or an independently measured wavelength alone supplies no such matrix. [Beasley’s atlas inventory, B199 and B202](https://github.com/dicipler-pixel/votkp-lean/blob/2b8ea372c7a0d8f2713958bb9c831a127a5c95a5/research/2026-11-11-standard-model-ball/atlas/ATLAS_B97_B207_READ_20261111_v1.md)

| Code in the crosswalk | Defined operation | Readout that exemplifies its effect |
|---|---|---|
| M | Reflect the eight chemical positions about carbon on the cyclic Li–Ne row. | Common normal-valence magnitudes agree on partner elements. |
| S | Exchange the named scalar endpoints of a signed difference. | The difference changes sign. A single isotope mass remains the same under ordinary spatial inversion. |
| A | Exchange the two endpoints naming an otherwise fixed interval of the ordered chemical table. | Existence of an intervening element stays the same whether the claimed slot exists or is spurious. |
| P | Reverse all spatial coordinates, transforming the physical apparatus with the system. | Unpolarized wavelengths, nuclear proton counts, temperatures and ordinary masses are scalar readouts. Chiral or polarization-sensitive observables need their own definition. |
| C, C1 | Change the signs of both point charges, or of only one charge, in the model interaction. | The paired product is even under C and changes sign under C1. C1 changes the physical pair. |
| H | Change the sign of the externally applied magnetic field while retaining stated sample and apparatus conventions. | Zeeman components can exchange or a signed response can change. An unspecified sample and line require further conditions. |
| Peel reversal | Exchange the two energies on the same directed peel step. | Γ changes sign and Γ² stays unchanged. This operation stays within the same atom. |

A grade applies only to the named scalar, count, set or directed difference. For a partly specified mechanism we marked the row *undefined*, *compound* or *unassigned*. This is especially important for the 199-law list: L5–L11 share a reconstructed chemical example, and L148/L171 repeat the same generic statement in the transcribed source. Neither repetition creates a new empirical test. [Source crosswalk](element_crosswalk_v1.csv)

## A precise test of the full short row

Put Li, Be, B, C, N, O, F and Ne at positions $Z=3,\ldots,10$, and use the cyclic involution

$$
 M(Z)=3+\big((9-Z)\bmod 8\big).
$$

The fixed elements are carbon and neon. The other positions form three two-element orbits. For the normal-valence magnitude sequence $(1,2,3,4,3,2,1,0)$, each value equals its partner’s. Plain reversal of the eight-item printed list gives $(0,1,2,3,4,3,2,1)$, which differs from the original. In the pinned Lean repo `RussellRebuild.valence_palindrome` proves the seven-item Li–F list equals its ordinary reverse. These are two compatible, distinct statements. [Lean source](https://github.com/dicipler-pixel/what-russell-saw-lean/blob/258d89f94354d13371b7371d9de5c5b9c1f4433b/lean/RussellRebuild.lean#L244) · [Abegg 1904](https://doi.org/10.1002/zaac.19040390125)

A single-valued odd scalar $s$ on this ring must obey $s(MZ)=-s(Z)$. At a fixed point this gives $s(Z)=0$. A signed valence **±4 at carbon cannot be a single-valued odd scalar on the eight positions**. One can retain the pair of branches $\{+4,-4\}$, exchanged over carbon, while preserving magnitude four. Noble-gas zero is compatible with oddness at the other fixed position. The conventions govern normal valences in a restricted chemical example. Other oxidation states, hydride structure and the reactivity of heavier noble gases require separate measurements. [Beasley’s rows U54, U120, U276 and U277](element_crosswalk_v1.csv) · [1962 xenon tetrafluoride report](https://doi.org/10.1021/cen-v040n041.p039)

**The helium-core openings break this cyclic symmetry.** From the pinned threshold file, for a neutral atom of nuclear charge $Z$, take $a$ as the threshold of its lithium-like ion (charge $Z-3$) and $b$ as that of its helium-like ion (charge $Z-2$). Test the signed polynomial $b^2-6ab+a^2$, which is positive for an outside forward opening. The archive contains measured and calculated inputs with their original grades and precision, so these numbers are derived from the archived reference thresholds. [Pinned thresholds](https://github.com/dicipler-pixel/votkp-lean/blob/2b8ea372c7a0d8f2713958bb9c831a127a5c95a5/data/element_thresholds_20261011.json.gz) · [Executable check](check_octave.py)

| Cyclic orbit | Common normal valence | Helium-core opening $b/a$ in listed order | Wall class |
|---|---:|---|---|
| Li ↔ F | 1 | 14.02894943, 5.15100590 | outside, inside |
| Be ↔ O | 2 | 8.45065825, 5.35282984 | outside, inside |
| B ↔ N | 3 | 6.83813194, 5.63966540 | outside, inside |
| C ↔ C | 4 | 6.07953419 | outside, fixed |
| Ne ↔ Ne | 0 | 5.00135175 | inside, fixed |

All three nonfixed orbits give opposite wall classes. A global even classification fails on the three exchanged pairs. A global odd signed wall score fails at the two fixed points, where the measured scores are nonzero. This tells us exactly which information the octave retains, and exactly where the peel supplies a different reading. It uses historical observations and archived thresholds, so the pattern carries no prospective credit. [Numerical results, both underlying energies and Γ](octave_core_openings_v1.csv)

## Controls that bear on Plate II

1. **Correct and spurious vacancies can have identical parity.** An intervening-slot question on fixed endpoints has the same answer with those endpoints listed in either order. This describes both Russell’s correct Mo–Ru gap and his extra Pt–Au gap. Independent evidence decides occupancy. The 1926 plates also contain the future Pm, At and Fr positions. All four unresolved positions had already appeared by atomic number in Bohr’s 1922 lecture. U103 and U107 show that Beasley’s full source ledger already noticed Tc and Fr even though his main §8 names only Pm, Re and At. [1926 primary plates and 1922 baseline](../RUSSELL_VACANCIES_v1_20261121.md) · [Bohr’s 1922 figure](https://www.nobelprize.org/uploads/2018/06/bohr-lecture.pdf)
2. **A false numerical reading can be an even scalar.** The mass of an atom under P, or the existence of its unpolarized transition at a specified wavelength, carries no spatial sign. U101/U102 contain wrong mass orderings, and the independent CIAAW values put Te above I and Co above Ni. U239 denies intrinsic helium lines, contradicted by the species-specific NIST spectrum. On swapping element endpoints instead, the mass *difference* is automatically odd regardless of its accuracy. [CIAAW standard weights](https://www.ciaaw.org/atomic-weights.htm) · [NIST helium lines](https://physics.nist.gov/PhysRefData/Handbook/Tables/heliumtable2.htm)
3. **A peak need not be a mirror symmetry.** U99 reports a short-period crest. Its printed Li and F temperatures differ, which already excludes equality on this paired orbit. The temperatures on an absolute scale are positive, which excludes equality to one another’s negatives. A rise and fall can be an observable pattern without assigning either exact parity to the full numerical series. [Russell’s short-row table, printed p. 94](https://tile.loc.gov/storage-services/service/gdc/gdclccn/27/00/45/08/27004508/27004508.pdf#page=114)
4. **A physical charge sign is not inherently odd under a spatial mirror.** In G2/U81 the tendency of two point charges to attract or repel depends on $q_1q_2$. That product survives simultaneous reversal of both signs and flips if just one changes. The directional force vector transforms with space, while the attraction-versus-repulsion reading relative to the separation remains unchanged. A source’s physically false force rule can still have this even transformation law. [G2, G25, U81, L50 and L51](element_crosswalk_v1.csv)
5. **Equal line type does not keep a history label.** The separate U240 test locates ordinary neutral-iron transitions in all three of Russell’s columns, with pre-1926 iron line identifications that round to an example from each. The word *history* currently has no specified line-by-line measurable action under a wall. Assigning the label does not create an odd observable. [Iron wavelength audit](IRON_COLUMNS_v1.md)

**Interpretation for the element paper.** The September source’s 386 claims plus 199 laws are now accounted for by ID. The November paper’s strong suggestion that correctness and evenness coincide remains a reading unless a single wall operation, an independent physical verdict and a genuine observability criterion are specified for each eligible row. This audit shows cases where a fixed operation admits both correct and false claims of the same type. It also gives a constructive result: valence, an oriented peel, and the location of its squared wall score retain three different pieces of information. Each can be shown as a separate layer of the periodic table.
