# Niobium, molybdenum, technetium, ruthenium and rhodium

**DERIVED.** All 210 ordinary forward peels are inside. Every one of the 215 serialized ionization energies agrees with the pinned archive and the official NIST ASD comparison. Four measured anion rungs are outside. The technetium anion rung also lies outside using the published calculated affinity of 0.636 eV. That estimate has no measured uncertainty.

Claude’s review asked for the opening of the filled 4d¹⁰ subshell alongside the krypton-core opening. There is no such ordinary filled-subshell opening in these five elements. The electron count for [Kr]4d¹⁰ is 46, while a neutral rhodium atom has 45 electrons. A different observable exists in all five: the first opening of a partially filled 4d subshell after 5s removal. The table distinguishes the two.

| Element | Opening of filled 4d¹⁰ along ordinary ladder | First 5s→partially filled 4d rung, z | Last 4d→first 4p (krypton core), z |
|---|---|---:|---:|
| Niobium | Absent | 2.118704 | 2.018259 |
| Molybdenum | Absent | 2.278486 | 1.825416 |
| Technetium | Absent | 1.936435 | 1.704545 |
| Ruthenium | Absent | 2.277019 | 1.621909 |
| Rhodium | Absent | 2.423950 | 1.537111 |

**RECOGNISED.** The krypton-core ratio falls down this sequence. The partial 4d opening changes direction. On the deeper ladder a separate rank swap survives the quoted uncertainty boxes: the krypton-core ratio exceeds the filled 3d¹⁰ opening in molybdenum and falls below it in technetium. The [rank check](ladder/batch9_rank_output.txt) gives the margins.

[All rungs and recheck instructions](ladder/README.md) · [Machine CSV](ladder/batch9_nb_rh.csv) · [Charge-state configuration check](orbitals/opening_labels.txt) · [Independent comparison with official NIST ASD and affinity sources](independent/NIST_AND_AFFINITY_SOURCES.md) · [Core Lean audit](lean/README.md).

The current archive is pinned at 182da01. Five atomic ground-state affinities are external to it. The revised rhodium affinity is 1.14273(5) eV (Chen et al., 2026); the [provenance table](independent/NIST_AND_AFFINITY_SOURCES.md) records the distinction between published measurements, a published evaluation citing unpublished measurements, and the calculated technetium estimate.
