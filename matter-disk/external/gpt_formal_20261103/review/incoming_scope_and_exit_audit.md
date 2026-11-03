# Independent audit of the incoming disk extension

This section audits the preserved `matter-disk` sources at commit
`881386a0ab00d917af6334a01423fb8b22469f5e`. Original scripts, outputs and claims
remain unchanged in the incoming record. The findings below qualify their use in
the present formal manuscript; they do not replace the source history.

## Endpoint filtering changes the measured massive-band exit

The incoming second-model experiment uses

\[
h(k)=(t_1+\cos k)\sigma_x+\sin k\,\sigma_y+(m+i\gamma)\sigma_z
\]

and compresses its lower-band biorthogonal projector to a block. Let
\(\nu_j\) be the compressed eigenvalues. For an endpoint filter \(\delta>0\),
the retained set is

\[
\mathcal J_\delta=\{j:|\nu_j|>\delta,\ |1-\nu_j|>\delta\},
\qquad
R_\delta=\max_{j\in\mathcal J_\delta}
\frac{|\operatorname{Im}\operatorname{Log}((1-\nu_j)/\nu_j)|}{\pi}.
\]

The logarithm here is principal. The reported exit is the crossing of
\(R_\delta=1/2\) returned by a geometric scan and bisection, following the source
algorithm. The scan is not a proof of a unique crossing or of the first crossing
over a continuous parameter interval. The filter is part of the instrument.

An independent implementation kept the model, antiperiodic ring \(N=2000\),
block length \(L=40\) unit cells and \(t_1=0.5\) fixed. It constructed each band
projector as \((I-h/E)/2\), with principal \(E=\sqrt{d\cdot d}\), then assembled
the block through Fourier coefficients. This is independent of the source's
left/right eigenvector assembly. Both constructions agree at the checked band
points to floating-point precision. The protocol was recorded before execution.

| Endpoint filter \(\delta\) | Massive \(m=0.4\): returned \(\gamma\) | Massive \(\langle K\rangle\) | Massless \(m=0\): returned \(\gamma\) | Massless \(\langle K\rangle\) |
|---:|---:|---:|---:|---:|
| \(10^{-6}\) | 0.271636929 | 1.057972846 | 0.474341649 | 2.000000002 |
| \(10^{-8}\) | 0.271636929 | 1.057972846 | 0.474341649 | 2.000000002 |
| \(10^{-9}\) | 0.169169932 | 1.022352491 | 0.474341649 | 2.000000002 |
| \(10^{-10}\) | 0.169169932 | 1.022352491 | 0.474341467 | 1.999995744 |
| \(10^{-12}\) | 0.122791366 | 1.011745220 | 0.474227956 | 1.997345192 |

The shipped \(10^{-9}\) massive result is reproduced. Its stability under
increasing block size did not establish stability under changing the endpoint
filter. The large massive-band change between \(10^{-8}\), \(10^{-9}\) and
\(10^{-12}\) prevents identifying that returned number with a filter-independent
physical threshold on the evidence presently available.

The massless result is stable at the displayed precision for filters
\(10^{-6}\) through \(10^{-9}\). At smaller filters it also shifts. The very small
endpoint eigenvalues belong to a nonnormal eigenproblem; neither that shift nor
a small residual alone resolves its exact-arithmetic limit.

At the ten reported parameter values, the maximum normalized eigenpair residual
was \(4.41\times10^{-15}\), using unit eigenvectors and normalization
\(\max(1,\|C_A\|)\). Eigenvector condition numbers ranged from approximately
135 to 575. These diagnostics were added after observing the sensitivity and are
recorded as post-analysis diagnostics, not as prospective decision tests. A small
residual is not a validated eigenvalue-error bound for a nonnormal matrix.

**What remains supported.** The incoming universal statement that all tested
opened bands exit at \(\langle K\rangle=2\) remains falsified at every massive
filter in this table. The restricted massless coincidence has finite numerical
support at specified filters. The exact Petermann identity and its unbroken-SSH
band average are separate analytic results. Neither their derivation nor this
table proves the equivalence between that average and the spatial-census exit.

**What remains open.** A filter-independent massive exit, if one is intended,
needs a definition and a controlled limit involving \(\delta\), ring size, block
size and numerical error. The order of limits must be stated. It should not be
replaced by another fitted constant at a single filter. All failed universal-law
claims and original controls remain part of the record.

Reproduction files are `review/INCOMING_EXIT_FILTER_PROTOCOL.md`,
`review/incoming_exit_filter.py`, `review/incoming_exit_filter_results.json`,
`review/incoming_exit_residuals.py` and `review/incoming_exit_residuals.json`.

## The algebra that survives a biorthogonal projector

For a general idempotent block matrix, the identity
\(C_{AB}C_{BA}=C_A-C_A^2\) and its polynomial spectral mapping survive without
Hermiticity. Therefore the branch-independent radial identity

\[
\sqrt{|1-4\nu(1-\nu)|}=|1-2\nu|
\]

legitimately transfers the complex radial disk count. This is proved in D3–D4.
It is not the same as transferring positivity, singular-value counting or the
Gaussian number-variance interpretation. The exact idempotent

\[
C=\begin{pmatrix}2&1\\-2&-1\end{pmatrix},\qquad C^2=C,
\]

has \(C_A=2\) and \(C_{AB}C_{BA}=-2\). Thus idempotence by itself permits a
negative cross product and radial value 3. Substituting \(C_{AB}C_{AB}^*=1\)
silently changes the observable and loses the identity. A positive metric, if
introduced, must also specify the adjoint and orthogonal partition in that metric.

For a Hermitian positive contraction, the unsigned boundary coordinate
\(\Gamma_b=\sqrt{1-4\lambda}\) is valid and lies in \([0,1]\). In a pure state it
equals \(|1-2\nu|\), not the signed coordinate itself. A zero threshold count means
all strengths are below the chosen threshold; it does not mean the cross block
vanishes. The warm uniform-ring row has zero count but positive trace, making
this distinction observable within the existing calculation.

## Complex poles, coordinate branches and physical interpretations

For \(z\ne-1\), the Cayley coordinate obeys

\[
\left|\frac{z-1}{z+1}\right|<1
\quad\Longleftrightarrow\quad \operatorname{Re}z>0.
\]

Consequently, complex width alone does not imply an outside-disk point. The
explicit family \(z=1-i\gamma\), \(\gamma>0\), gives

\[
\Gamma=\frac{-i\gamma}{2-i\gamma},\qquad
|\Gamma|^2=\frac{\gamma^2}{4+\gamma^2}<1.
\]

An opened or resonant system needs a specified map to \(z\) and a condition on
its real part before an outside-disk conclusion follows. The complex logarithm
also requires a branch: for arbitrary \(W\), the condition is
\(\cos(\operatorname{Im}W)>0\); the interval
\(|\operatorname{Im}W|<\pi/2\) is equivalent only for the principal branch.

Raw Hamiltonian-energy ratios have an additional reference issue. Energies
\((1,2)\) have ratio 2 and coordinate \(1/3\). Shifting both by \(-1.25\) gives
\((-0.25,0.75)\), ratio \(-3\) and coordinate 2, while the energy gap remains one.
This is a counterexample to an energy-zero-independent interpretation of arbitrary
eigenenergy ratios. It is **not** a criticism of VOTKP's explicitly defined removal
energies, whose physical references are part of their definitions.

A negative coefficient inferred from a biorthogonal Rényi-entropy fit likewise
does not establish a negative coefficient for a literal nonnegative channel
cardinality. If \(N(\xi)=a\log\xi+O(1)\) with \(a<0\) as \(\xi\to\infty\), then
\(N(\xi)\) eventually becomes negative, contradicting an unsigned count. A signed
or otherwise redefined observable needs its own definition and proof. The
positive-covariance entropy/count relationship cannot be continued into an
indefinite or nonpositive setting by terminology alone. The actual supplied
Rényi-fit outputs remain preserved as numerical results under their stated
biorthogonal prescription.

## The gas inverse survives with its required state information

The incoming helium difference identity

\[
\log\frac{n_0n_2}{n_1^2}
=-\frac{I_1-I_0}{k_BT}-\log4
\]

is population-only under the declared ground partitions. Its sum identity

\[
\log\frac{n_0}{n_2n_e^2\lambda_e^6}
=\frac{I_0+I_1}{k_BT}-\log4
\]

is also correct, but its evaluation requires \(n_e\lambda_e^3\) for each sample.
It is density-compensated, not obtainable from charge fractions alone. In a pure
neutral species, \(n_e\) may be inferred from fractions **and an absolute nucleus
density**; fractions alone do not provide it. Temperature-dependent partitions
add terms to both slopes. G8–G9 prove the general inverse, its partition correction
and its deterministic error bounds.

Generating synthetic populations from a supplied atomic ladder and reconstructing
that same ladder is an identity and implementation check. It is not independent
experimental confirmation of the threshold prediction. This scope leaves the
inverse construction intact and identifies what a real measurement must supply.
