# Theta and colour: extending the existing Lean section

Jeromie Beasley's November 2026 theta and colour work extends the existing
VOTKP formalization. The original 140 theorems, the one-action observer,
memory kernels, thin-film identities, and separate Two Trees project remain
the starting point. This extension targets results not already covered there.

## Results selected

| Module | Research result | What must still be supplied in an application |
| --- | --- | --- |
| `VOTKP/ThetaStructure.lean` | A mirror-composite cancellation test is equivalent to mirror antisymmetry under the sum law and a nonzero Alexander weight; conditional factorization of the mirror-composite record through Delta; direct two-branch symmetry witnesses. | The knot invariant, connected-sum and Alexander laws, and any conjectural mirror/reversal laws appear as explicit premises. |
| `VOTKP/ThetaGrid.lean` | Complete rectangular-grid vanishing and equality for bounded bivariate polynomials, including the `(2n+5)(2n+4)` grid. | The actual polynomial, its degree bounds, its relation to theta after clearing denominators, and all exact grid evaluations. |
| `VOTKP/Colour.lean` | When colour matches survive a linear filter; bounded matched inputs that a filter separates; the information lost by normalization and recovered by retaining total amount. | The chosen linear spectral model and its physical calibration. Finite arithmetic is not a measurement of gold or paint. |
| `VOTKP/MultiObserver.lean` | The predictive quotient for several permitted actions, including ordered continuations and a complete finite horizon of `dim(ker R)`. | The actual state, readout, and permitted actions. Restricted word grammars require an explicit model; an abstract quotient does not identify a native palette, knot, or physical system. |

The mathematical statements in the Lean files are authoritative. Their
explicit premises matter as much as their conclusions.

## Theta: three different levels of evidence

The **21 resolved sign cases** are exact rational Python comparisons between
original KnotTheory diagrams and the authors' table at specified admissible
points. They are not Conjecture 21, and those computations have not been
ported into the Lean kernel by this extension.

**Conjecture 21** is the general mirror-antisymmetry assertion. The structural
module proves consequences of that assertion when supplied as a hypothesis;
it does not prove the assertion. The reverse-mirror branch also requires the
appropriate reversal law when zero is deduced from symmetry. Direct
inequalities against both branches provide a separate logical route,
conditional on the observation actually being invariant under knot
equivalence.

The **grid certificate theorem** explains why a complete distinct rectangular
grid suffices after degree bounds are established. A generic theorem does
not validate the claimed degree of an arbitrary theta implementation or
replay the 66,728 reported cells. Alternate braid representatives remain
computational corroboration until their full certificates are imported and
checked.

The conditional record `(Delta(K)^2, 0)` concerns the family `K # mirror(K)`.
It neither proves that theta globally factors through Delta nor establishes
that no function of theta can determine unknotting number. In particular,
the Brittenham–Hermiller self-sum and mirror-sum values are different in the
comparison at hand.

## Colour: keep the actual operation

The current research distinguishes the affine Z/9 labels, the decimal
multiplication-by-3 palette rotation, and normalized additive amounts.
These are different models and operations. This extension does not replace
them with the older claim that Z/10 addition is the complete colour system.

The amount witness uses `(1,1)` and `(2,2)`. Both normalize to `(1/2,1/2)`.
Adding the same absolute amount `(1,0)` produces `(2/3,1/3)` and `(3/5,2/5)`.
The retained total repairs this lost information. Relative-fraction mixing
would be a different operation and needs its own statement.

For optical matching, a finite linear readout is the declared model. A
bounded witness establishes that the hidden direction can be realized
inside the componentwise unit box, rather than only as an unrestricted
signed vector. This does not supply measured spectra, an illuminant,
observer calibration, or optical constants.

## Source record

The extension starts from `dicipler-pixel/votkp-lean` commit
`e3611fe31e3fdcf2a8f132078ab8776135fba541`, with Lean and Mathlib v4.34.1.
The following SHA-256 hashes identify the research inputs read for selection;
they are provenance records, not proof certificates.

| Input | SHA-256 |
| --- | --- |
| `Prime_Colour_Transport_Full_Research_20261101 (2).html` | `fa17e6a49ae2fb58372265bfe26c0c7bd3504bbb0d220e6b1a8e6eb9195041af` |
| `Prime_Colour_Transport_Research_Repository_20261101(1).zip` | `0a5651b75ed985ae309f26118b81fcc25837ce0de6128bf7a73aeff3126b2cd9` |
| `theta_everything (2).pdf` (223-page edition) | `7a125876efd5d0d2de5c9194d7038f77bdb66742b0c5d6613850b412658db93a` |
| `sign_cases_resolved.json` | `c6712a7b2d862ee91a57f91794dd36fdc547c88d840d275939d476fb671424c6` |
| Original `PD4Knots.m` | `7fc6dba63aebddd1de6e0431373d3da260bd416fa04ce002752a2c59c5bcaf3f` |

The colour source edition's `chapters/01_corpus_bridges.md`, section 5.3,
gives the multiple-action extension (OP01); its closing review gives the
normalized-amount witness (CO04). The
surviving-match question also appears in VOTKP v2.9 section 6.2. The theta
source supplies the grid method and structural questions. No source archive
or private correspondence is imported into the public proof project.

The research edition preserves Elizabeth / EJ's native constructions,
palette inputs and drawings, Jeromie's research direction, and the related
Mixin source credit to DarkWolf Modular. The finite linear models selected
here do not replace or claim to exhaust those attributed constructions.

## Reproduction

Use the repository's pinned toolchain and existing verification pipeline:

```sh
lake exe cache get
lake build
python3 scripts/verify.py
python3 scripts/verify_energy_data.py
```

The GitHub workflow additionally runs `lake env leanchecker` for every
configured module and both showcase modules. The audit permits only
`propext`, `Classical.choice`, and `Quot.sound`; it rejects `sorry`, project
axioms, and `native_decide` dependencies. Mathematical false controls are
compiled separately and must be rejected for the intended reason.
