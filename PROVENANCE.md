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

The HTML, PDF and package zip used here match their checksums.

**How the Lean files were made.** The four modules were written for this repository from the
statements of v1.1. Every numerical value they assert (the wall fractions, the ladder composites,
the film counterexample, the cumulant witness, the transmissions and the gap
`79,600,000/400,039,601`) was first recomputed in exact rational arithmetic.

Lean v4.34.1, Mathlib v4.34.1. First verified at commit `2342555` (GitHub Actions run
36406349897).


**Version 1.2.** `VOTKP/Ordinal.lean` proves negative control 41 of version 1.2 (§18), restored from
the programme's version 0.1 control list with an explicit witness. The witness was checked by
evaluation before it was written.

**Showcase.** `Showcase.lean` and `Showcase_WithProofs.lean` separate the statements a reader
must trust from the proofs, after the pattern of Gómez-Serrano, Liehr and Taylor's Lean
formalization of their counterexamples to Grad's conjecture
([lukasliehr/Grad-Conjecture](https://github.com/lukasliehr/Grad-Conjecture)). Verified at
commit `b522f2a` (GitHub Actions run 36447512334).
