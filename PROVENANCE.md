# Provenance

**Paper.** *VOTKP: The Vector of Traits Kept under Peeling — Elemental Peeling of Atoms and
Knots: Topology, Field Loading, Geometry, and What Survives Controlled Removal*, version 1.1,
25 September 2026. Zenodo [10.5281/zenodo.23011140](https://doi.org/10.5281/zenodo.23011140).
The paper is labelled "Claude's version, written from Jeromie Beasley's research programme".

The Zenodo record's files, with the MD5 checksums the record lists:

```
f743b39bba31e8e7e5dfcdc61fb29b68  VOTKP_ELEMENTAL_PEELING_PAPER_v1_1_20260925.html
3ab0d62f139e1ae7308c8b0b9b73a262  VOTKP_ELEMENTAL_PEELING_PAPER_v1_1_20260925.pdf
eac2ff97bd0792ce11bca82f00864a0e  VOTKP_Elemental_Peeling_Paper_v1_1_Package_20260925.zip
```

The HTML and PDF copies used here match their checksums. The package zip was not opened for this
repository.

**How the Lean files were made.** The four modules were written for this repository from the
statements of v1.1. Every numerical value they assert (the wall fractions, the ladder composites,
the film counterexample, the cumulant witness, the transmissions and the gap
`79,600,000/400,039,601`) was first recomputed in exact rational arithmetic.

Lean v4.34.1, Mathlib v4.34.1. First verified at commit `2342555` (GitHub Actions run
36406349897).
