# Independent adversarial checks

Written 3 November 2026 before executing `adversarial_checks.py`.
These are implementation checks and explicit counterexamples, not statistical
confirmation of universal theorems or a new experiment. The universal statements
must stand on the accompanying analytic proofs.

1. For 128 seeded pairs of complex positive contractions, verify the cross-block
   Gram Lipschitz bound with constant one in the spectral norm. Verify invariance
   of every selected threshold count whose spectral margin is strictly larger
   than the input perturbation norm. Tolerance for floating-point inequalities:
   `2e-12`.
2. For 64 seeded mixed perturbations of projectors, verify the positive defect
   ordering and the near-purity threshold sandwich. Use `theta=0.09`, and retain
   threshold distances so proximity is visible. Tolerance `2e-12` for matrix
   inequalities; threshold cases within `1e-11` of an eigenvalue are skipped.
3. Verify two sharp limitations explicitly: the Lipschitz constant tends to one
   along a two-by-two family, and an arbitrarily small perturbation can change a
   threshold count when the spectral margin is absent.
4. Construct a four-mode, two-particle pure state
   `(|1100> + |0011>)/sqrt(2)` using Fock annihilation matrices. Its one-body
   covariance is `0.5 I`, yet the A/B number covariance is `-1` and its bipartite
   entropy is `log(2)`. This must reject unrestricted use of Gaussian Wick
   identities and show that zero one-body cross-correlation does not exclude
   non-Gaussian entanglement. Use covariance convention `<a_j^dagger a_i>`.
5. Independently construct the gas agent's real symmetric Householder witness
   with full spectrum `(-3,-1,1,3)` and spectral weights `(1/4,...,1/4)` versus
   `(3,7,1,5)/16`. Verify identical retained block zero, coupling-square five and
   initial vector, but distinct response: survival probabilities zero and `1/32`
   at time `pi/4`. Check the stated scalar resolvent formulas at nonreal z.

Seed: `2026110307`. No pass threshold will be revised after execution to turn a
failure into a pass. Any correction to the test itself will be recorded.
