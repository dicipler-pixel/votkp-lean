# Adjacent-element two-face map for all six noble cores in the archive

**DERIVED.** Carbon with nitrogen is the closest pair to ideal tangency in the entire map. The helium-core margin is **+0.003093338**. Its box is [+0.003090764,+0.003095912]. Every other pair stays at least 0.037818076 from zero over its own quoted input box. Thus even permitting independent input movement throughout all the listed intervals leaves this closest-pair identification intact.

**Method and rejection tests.** For core occupancy N, an element of atomic number Z contributes the removal ratio b/a at charge q=Z−N−1 if the archive supplies both consecutive thresholds. Pair it only with Z+1 at the same occupancy. Missing inputs terminate a series; no pair jumps a missing element. Use g=(b−a)/(b+a). For two faces the signed margin is M=g₁²+g₂²−1, positive for open, zero for ideal, negative for closes. The program independently checks its sign with (z₁−1)²(z₂−1)²−16z₁z₂ and with the original geometric intersection criterion for perpendicular disk circles. All three agree for all 427 central pairs. A box spanning zero would suspend the corresponding mixed call. [Pinned input archive](https://github.com/dicipler-pixel/votkp-lean/blob/bcedbd9bba0de5a75fd2a860a912ebc4882f4e8a/data/element_thresholds_20261011.json.gz) · [original disk-circle geometry](https://github.com/dicipler-pixel/votkp-lean/blob/bcedbd9bba0de5a75fd2a860a912ebc4882f4e8a/research/2026-11-20-element-paper-loop-wall/checks/lambert_jump_check_v1.py)

**Why only five pairs test the unequal-side comparison.** Write Sᵢ=2gᵢ²−1 for the one-element self margin. Then Mᵢⱼ=(Sᵢ+Sⱼ)/2 exactly. Equal-side self calls force the central mixed call algebraically. Five adjacent pairs in the map have opposite self signs. In those five, the stronger absolute self margin decides the mixed sign. Across all pairs, 419 have two closing self calls, three have two open self calls, and five have one of each. The map counts repeated applications of the same rule. Its physical use at a real atomic junction would require a separately specified connection.

| Core | Available elements | Faces | Adjacent pairs | Mixed open | Mixed closes | Central upward steps | Ordered falls supported by both endpoints |
|---|---|---:|---:|---:|---:|---:|---:|
| Helium | lithium to lawrencium | 101 | 100 | 4 | 96 | 0 | 100 |
| Neon | sodium to darmstadtium | 100 | 99 | 1 | 98 | 0 | 43 |
| Argon | potassium to darmstadtium | 92 | 91 | 0 | 91 | 4 | 12 |
| Krypton | rubidium to darmstadtium | 74 | 73 | 0 | 73 | 1 | 8 |
| Xenon | caesium to lawrencium | 49 | 48 | 0 | 48 | 16 | 5 |
| Radon | francium to lawrencium | 17 | 16 | 0 | 16 | 3 | 6 |
| **Total** | | **433** | **427** | **5** | **422** | **24** | **174** |

**DERIVED.** The five open mixed pairs are lithium with beryllium, beryllium with boron, boron with carbon, carbon with nitrogen, and sodium with magnesium. No measured or evaluated ratio has been filled in past the archive's stopping points. All 433 central faces are present from each first eligible element through its indicated last element, with no internal holes.

| Core | Adjacent elements near the inward crossing | Left self | Mixed | Right self | Mixed margin with quoted input endpoints |
|---|---|---|---|---|---|
| Helium | Carbon with Nitrogen | open | open | closes | 0.003093338 [0.003090764, 0.003095912] |
| Neon | Sodium with Magnesium | open | open | closes | 0.114273066 [0.114268679, 0.114277453] |
| Argon | Potassium with Calcium | open | closes | closes | -0.037822019 [-0.037825961, -0.037818076] |
| Krypton | Rubidium with Strontium | open | closes | closes | -0.111436975 [-0.111439607, -0.111434343] |
| Xenon | Caesium with Barium | open | closes | closes | -0.175248016 [-0.175276211, -0.175219824] |
| Radon | Francium with Radium | closes centrally; straddles | closes | closes | -0.263879104 [-0.316084207, -0.215870361] |

**DERIVED.** Francium has a central closing self-pair and a straddling self interval. Its ratio ranges from 5.033463694 to 5.966499212 because the second energy is semiempirical. Its mixed pair with radium closes throughout [−0.316084207,−0.215870361]. A central inward crossing on this core cannot be inferred from these first two elements.

**RECOGNISED.** Wall-side robustness is stronger here than a claim of monotone decrease. Among 427 central differences there are 403 falls, 24 rises and no ties. Of the 403 falls, 174 separate across the endpoint boxes. The other 229 falls and all 24 rises permit overlapping endpoints, for 253 adjacent differences whose direction the boxes do not establish. All rise comparisons involve two faces with theoretical energy pairs, except for two tungsten/rhenium comparisons (argon and xenon cores), which compare semiempirical/semiempirical to theoretical/theoretical. The full list and grades are in [output.txt](output.txt). A difference of point estimates is distinct from an interval-resolved directional change.

**Uncertainty convention.** Each ratio lies in [(b−δb)/(a+δa), (b+δb)/(a−δa)] for independent endpoints. For 44 faces the ratio box reaches or includes 1; their squared reflection has a minimum of zero inside the box. The code computes the smaller and larger power over the entire positive interval, then adds the two power ranges. Treating power as ascending across a ratio interval which includes values below one would give an incorrect lower bound. These boxes propagate the reported tolerances and make no assertion about their joint statistical distribution.

Run `python3 adjacent_pairs.py /path/to/data/element_thresholds_20261011.json.gz .`. The [433 faces](opening_faces.csv) preserve the exact ratio, source energies as rational electronvolts, uncertainties, individual grades and NIST reference codes. The [427 adjacent pairs](adjacent_pairs.csv) give both self calls, mixed margins, uncertainty tests and direction comparisons. All rational tests run before display rounding.
