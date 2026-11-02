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

## Energy extension (11 October 2026)

The archived threshold input is a public-data-only extraction from the VOTKP v2.3 element atlas: element identity, charge, energy, uncertainty, E/S/T label and bibliographic reference. It excludes private cross-paper notes. The parent archive hash is preserved inside the compressed JSON. New Lean identities, exact rational controls and the 5:2 visual accompany section 21. Input values were not refreshed against live NIST in this pass.

## Current paper: version 2.9 (13 October 2026)

*VOTKP: The Vector of Traits Kept under Peeling*, version 2.9, 13 October 2026. Zenodo
[10.5281/zenodo.23340757](https://doi.org/10.5281/zenodo.23340757). Its files, with the MD5
checksums the record lists:

```
6ddfe492cba71521aae3e4f6c77d4e44  VOTKP_ELEMENTAL_PEELING_PAPER_v2_9_20261013.pdf
003026b6532928615d38f063489d28c2  VOTKP_ELEMENTAL_PEELING_PAPER_v2_9_20261013.html
8ca37846dc6819db714e57554763a65d  VOTKP_v2_9_Code_Proofs_Data_20261013.zip
7760d68710e9cc60d407eb52a5c15fc8  VOTKP_Mixer_v1_3_20261013_standalone.html
```

At 31 October 2026, the library held 140 theorems in 15 modules (commit `bbe5b9e`,
checked by GitHub Actions and by an independent cold-clone rebuild on SAIR's Open Math OS). The
folder `two-trees/` (commit `f26efd2`) adds the separate paper *Two Trees in One Ball*, version 4,
with its own core-Lean check.

## Theta and colour extension (November 2026)

The next extension starts from commit
`e3611fe31e3fdcf2a8f132078ab8776135fba541`. It reads the 1 November Prime
Colour Transport research edition, the 223-page theta record, and the
separate resolved-sign-case output. [The extension record](docs/theta-colour-formalization.md)
identifies those inputs by SHA-256 and separates formal statements from
external data checks. It adds conditional theta structure, rectangular-grid
soundness, bounded surviving-match criteria, amount retention, and the
multi-action predictive quotient. These are newly formalized parts of the
research record; no claim of literature novelty follows from formalization.
