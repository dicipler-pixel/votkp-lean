# Independent mathematical review

Prepared 3 November 2026 for the formal Matter–Gases–VOTKP package. This review
checked complete human-readable proofs, independent finite calculations and the
incoming disk-extension scope. It does not substitute for the separate Lean
compilation and axiom manifest.

## Reviewed analytic components

- **B1–B13, boundary theorem file:** exact block decomposition, positive bounds,
  paired spectra, pure-state recovery, trace estimate, local-unitary covariance,
  perturbation margin, near-purity sandwich, projector extension, Gaussian number
  covariance, non-Gaussian counterexamples the fixed-Hamiltonian phase witness and quantitative Gaussian mutual-information bounds.
  No mathematical blocker found.
- **K1–K4, positive moment-matched gas transport:** matching is pointwise in the
  first three moments, the free-streaming contrast has the stated sign and factor,
  and the third derivative exposes the omitted third moment. The reset factor is
  proved for a separate pre-release preparation interval. It is not silently used
  for self-consistent collisions acting simultaneously with streaming.
- **D1–D7, disk extension:** real boundary radius and its lost sign are correctly
  separated from complex radial spectral mapping. The oblique projector identity
  survives, while positivity does not. The logarithm-branch condition is explicit; the scalar radius stability and the nonnormal eigenvalue limitation are correctly distinguished.
- **G1–G7 and R1–R4, gas/response file:** anchored ratio reconstruction, unique
  positive Saha closure, comparative statics, fixed-partition temperature response,
  conditional scaling, exact hidden-source equation and finite response witnesses
  are consistent. The phrase “common increase” was corrected to multiplicative
  threshold scaling; additive shifts do not preserve the Cayley vector.
- **G8–G9, reverse gas inference:** difference and compensated sum identities,
  general ladder reconstruction, temperature-dependent partition bias, corrected
  inverse and deterministic error bounds check. No charge-neutrality assumption is
  needed for the ratio identities themselves.

- **M1–M2, finite records:** the finite-difference weights annihilate exactly the stated lower moments, preserve strict positivity under the given perturbation bound, and yield the explicit characteristic-function difference. The reflected-measure intensity control correctly separates phase-sensitive from intensity-only readout.
- **P1–P2, Petermann scope:** the Pauli projector norm formula and the unbroken SSH band integral are exact under E nonzero and A>|B|, respectively. The manuscript correctly distinguishes the proved average identity from the unproved filtered-exit equivalence.

## Independent finite checks executed

The protocol `ADVERSARIAL_CHECK_PROTOCOL.md` was written before running
`adversarial_checks.py`. All declared checks passed:

| Check | Result |
|---|---|
| Complex positive-contraction pairs | 128 pairs satisfy the spectral-norm Gram bound |
| Threshold comparisons with sufficient margin | 455 count agreements |
| Near-projector order/sandwich checks | 64 cases |
| Gaussian information lower/upper and census bounds | 64 additional covariance cases, separately registered |
| Sharp norm family | Ratio tends to 1; at epsilon 1e-6, ratio 0.999998999994 |
| Absent-margin false control | Counts 0 and 1 at input distance about 2e-9 |
| Four-mode non-Gaussian pure witness | C=0.5 I, cross trace 0, number covariance -1, entropy log 2 |
| Equal-full-spectrum response witness | Same retained block 0 and coupling square 5; survival 0 versus 1/32 |

The separate `GAUSSIAN_INFORMATION_PROTOCOL.md` preceded its new run. The lower information coefficient tends to 4 in the sharp two-mode family; a pure-state counterfamily has information/cross-trace ratios 11.31, 20.42 and 29.63, illustrating why the upper bound needs an occupation margin.

These finite checks support the implementation, while the universal statements
rest on the proofs. The numerical thresholds are not promoted to exact spectral
certificates without validated operator-error bounds.

## Corrections and boundaries retained

The two-mode phase witness has different initial currents; it only matches the
listed local covariance and boundary-strength records. The classical K1–K4
construction is the example that matches density, flow and stress initially.
Neither example matches a complete physical state.

Gauge-invariant Gaussian assumptions are essential to the number-covariance
identity. The four-mode counterexample has even local parity in both branches,
so its non-Gaussian entanglement witness does not rely on a local parity-violating
superposition. One-body data cannot resolve all higher-order state information.

The strongest incoming-data finding is in `incoming_scope_and_exit_audit.md`:
the massive-band exit returned by the source instrument depends materially on
the endpoint filter. Its original universal-average-law rejection is retained,
but no filter-independent physical exit is established. The full numerical table,
protocol and eigenpair diagnostics are supplied. This review also records exact
counterexamples to “complex width implies outside the disk,” arbitrary energy-zero
invariance of eigenenergy ratios, and a negative asymptotic unsigned census.

The physics claims remain narrower than the algebra. A Gaussian lattice covariance,
a classical collisionless gas, a finite amplitude kernel, a Saha equilibrium and
successive relaxed atomic ionization thresholds are distinct models or observables.
The manuscript may connect their coordinate identities and information limits; it
must not identify them as one experimentally established dynamics.

## Conclusion for the manuscript

The reviewed analytic core is mathematically sound under its explicit hypotheses.
The corrected draft should preserve the source observations and failed tests while
using the sharper restrictions above. Machine-checked coverage must be reported
only from the final successful Lean build and axiom inventory. Laboratory gas
preparation, equilibrium attainment, measured threshold inversion and microscopic
memory-kernel inference remain unperformed physical validation tasks.


## Framework-fidelity addendum following the reported implementation dispute

The analytical approvals in this review concern the displayed hypotheses and derivations. They do not certify that a standard model is a source-faithful implementation of the author's full Direction–Spin–Throughput or connection-energy framework. A reported separate ledger-implementation dispute has not been identified with a local named run. See `contamination_dependency_audit.md` for the bounded local dependency search, inherited-review qualifications, and exact language that requires framework-fidelity clarification. No new tests were run for this addendum.
