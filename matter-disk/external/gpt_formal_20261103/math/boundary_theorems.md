# A finite-dimensional boundary census for positive contractions

**Research setting.** This is a theorem-and-proof development prepared for Jeromie Beasley's matter–gas–VOTKP programme on 3 November 2026. The block identities, spectral estimates and Gaussian identities below are standard finite-dimensional mathematics. Their use as a proposed continuation of the paper's pure-projector census is the application developed here; no priority claim is made. A theorem marked **proved here** has a complete mathematical proof below. This label does not mean that the statement has been checked in Lean; the separate formalization inventory is authoritative for that status.

## Definitions and conventions

Let \(\mathcal H=\mathcal H_A\oplus\mathcal H_B\) be a fixed finite-dimensional orthogonal decomposition of a complex Hilbert space, with dimensions \(a,b\). Let \(C=C^*\) satisfy \(0\le C\le I\). Write

\[
C=\begin{pmatrix}A&B\\B^*&D\end{pmatrix},\qquad
T_A=(C-C^2)_{AA},\qquad F_A=A-A^2,\qquad X_A=BB^*.
\]

Here \(B:\mathcal H_B\to\mathcal H_A\); the label \(B\) on this operator is distinct from the subsystem name. Define \(X_B=B^*B\). The norm \(\|\cdot\|\) is the operator norm; \(\|\cdot\|_F\) is the Hilbert–Schmidt norm. Every eigenvalue count below includes algebraic multiplicity (equal to geometric multiplicity for the Hermitian matrices used). At a threshold \(s\), equality is included:

\[
\mathcal N_Y(s)=\operatorname{rank}\mathbf1_{[s,\infty)}(Y).
\]

Fix \(0<\varepsilon<1/2\), put \(\theta=\varepsilon(1-\varepsilon)>0\), and define

\[
N^{\rm raw}_\varepsilon(C;A)=\operatorname{rank}\mathbf1_{[\varepsilon,1-\varepsilon]}(A),
\quad
N^\partial_\varepsilon(C;A)=\mathcal N_{X_A}(\theta).
\]

The first count concerns intermediate local occupations; the second concerns squared cross-block singular values. The partition is part of the definition. There is no partition-independent phase or substance label here.

## B1. Exact defect decomposition — proved here

For every block matrix above,

\[
\boxed{F_A=T_A+X_A.}
\]

**Proof.** The \(AA\) block of \(C^2\) is \(A^2+BB^*\). Hence \(T_A=A-A^2-BB^*\). Rearranging gives the identity. Hermiticity and positivity are not needed for this algebraic calculation if the lower-left block is treated as a general independent block. They become essential for the order statements below. ∎

## B2. Positivity, sharp bounds and singular values — proved here

\[
0\le X_A\le F_A\le \tfrac14 I_A,
\qquad 0\le T_A\le F_A,
\qquad \|B\|\le\tfrac12.
\]

**Proof.** Compression preserves order, so \(0\le A\le I_A\). The finite-dimensional spectral theorem applied to \(C\) gives \(C-C^2\ge0\), because its eigenvalues are \(c(1-c)\ge0\) for \(c\in[0,1]\). Thus \(T_A\ge0\). Also \(X_A=BB^*\ge0\). B1 yields both \(X_A\le F_A\) and \(T_A\le F_A\). Finally,

\[
F_A=\tfrac14 I_A-(A-\tfrac12 I_A)^2\le\tfrac14 I_A.
\]

Therefore \(\|B\|^2=\|BB^*\|\le1/4\). Equality is attained for the two-mode rank-one projector \(C=\frac12\left(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\right)\). ∎

In particular, the eigenvalues of \(X_A\) are the squared singular values of \(B\), with zero padding when \(a>b\). The threshold can equivalently be written \(s_j(B)\ge\sqrt{\varepsilon(1-\varepsilon)}\). Using the unsquared threshold for these singular values would be a different diagnostic.

## B3. Two-sided symmetry and finite-size limits — proved here

The positive eigenvalues of \(X_A=BB^*\) and \(X_B=B^*B\) agree, including multiplicity. Consequently,

\[
N^\partial_\varepsilon(C;A)=N^\partial_\varepsilon(C;B),\qquad
N^\partial_\varepsilon\le\operatorname{rank}B\le\min(a,b),
\]

\[
\operatorname{Tr}X_A=\operatorname{Tr}X_B=\|B\|_F^2
\le\tfrac14\min(a,b).
\]

**Proof.** If \(BB^*u=\lambda u\) with \(\lambda>0\), then \(B^*u\ne0\) and \(B^*B(B^*u)=\lambda B^*u\). The reverse map is \(B/\lambda\), so the eigenspaces have equal dimensions. The remaining statements follow by counting and summing the positive eigenvalues and using B2. ∎

The finite census cannot diverge at fixed finite \(a,b\). A divergent per-boundary or scaling-limit census must specify the sequence of spaces and limits.

## B4. Pure-projector recovery and a universal one-sided comparison — proved here

For every positive contraction,

\[
N^\partial_\varepsilon(C;A)\le N^{\rm raw}_\varepsilon(C;A).
\]

If \(C^2=C\), equality holds exactly.

**Proof.** For \(\nu\in[0,1]\),

\[
\nu(1-\nu)-\varepsilon(1-\varepsilon)
=(\nu-\varepsilon)(1-\varepsilon-\nu),
\]

so \(\nu(1-\nu)\ge\theta\) if and only if \(\nu\in[\varepsilon,1-\varepsilon]\). The spectral theorem therefore gives \(\mathcal N_{F_A}(\theta)=N^{\rm raw}_\varepsilon\). By B2, \(X_A\le F_A\); the min–max principle gives \(\lambda_j(X_A)\le\lambda_j(F_A)\) for each ordered eigenvalue. This proves the inequality. If \(C^2=C\), B1 gives \(T_A=0\), hence \(X_A=F_A\), proving equality. No numerical threshold tolerance is used in this exact statement. ∎

## B5. Trace estimate and its exact meaning — proved here

\[
\boxed{\theta N^\partial_\varepsilon(C;A)\le\operatorname{Tr}X_A=\sum_{i\in A,j\in B}|C_{ij}|^2.}
\]

**Proof.** Each of the counted nonnegative eigenvalues contributes at least \(\theta\) to the trace. The uncounted eigenvalues are nonnegative. The entry formula follows from \(\operatorname{Tr}(BB^*)=\sum_{ij}|B_{ij}|^2\). ∎

This is an upper bound on the count, not an identity determining it from the trace. A count of zero allows nonzero eigenvalues below \(\theta\); it is not a zero-correlation certificate. By contrast, \(\operatorname{Tr}X_A=0\) if and only if \(B=0\).

## B6. Local-unitary covariance — proved here

Let \(U=U_A\oplus U_B\) be block diagonal and unitary, and set \(\widetilde C=UCU^*\). Then

\[
\widetilde A=U_AAU_A^*,\quad \widetilde B=U_ABU_B^*,\quad
\widetilde X_A=U_AX_AU_A^*,\quad \widetilde T_A=U_AT_AU_A^*.
\]

Both censuses and all the displayed spectra and traces are unchanged.

**Proof.** Block multiplication gives the formulas; unitary conjugation preserves eigenvalues and trace. ∎

A unitary that mixes the two regions changes the partition-relative observable and is not covered by this invariance.

## B7. Operator-norm stability and a certified threshold margin — proved here

Let \(C,\widetilde C\) be positive contractions on the same partition and put \(\delta=\|C-\widetilde C\|\). Then

\[
\|X_A(C)-X_A(\widetilde C)\|\le\delta.
\]

For \(\delta<\theta\),

\[
\mathcal N_{X_A(C)}(\theta+\delta)
\le N^\partial_\varepsilon(\widetilde C;A)
\le\mathcal N_{X_A(C)}(\theta-\delta).
\]

In particular, if

\[
\operatorname{dist}(\theta,\operatorname{spec}X_A(C))>\delta,
\]

then \(N^\partial_\varepsilon(C;A)=N^\partial_\varepsilon(\widetilde C;A)\).

**Proof.** Write the cross blocks as \(B,\widetilde B\). Compression gives \(\|B-\widetilde B\|\le\delta\), while B2 gives \(\|B\|,\|\widetilde B\|\le1/2\). Therefore

\[
BB^*-\widetilde B\widetilde B^*
=(B-\widetilde B)B^*+\widetilde B(B^*-\widetilde B^*)
\]

has norm at most \((\|B\|+\|\widetilde B\|)\|B-\widetilde B\|\le\delta\). The Hermitian min–max principle bounds each eigenvalue change by \(\delta\). The threshold inequalities follow by applying those bounds to ordered eigenvalues. The strict distance condition prevents any eigenvalue from reaching or crossing the threshold. ∎

The assumption \(\delta<\theta\) merely keeps the lower comparison threshold positive; the spectral inequalities themselves remain meaningful without it. For floating-point computations, an empirically small residual is not by itself a rigorous operator-norm error bound. A certified numerical count needs a validated error bound and a margin larger than it.

## B8. A near-projector comparison controlled by global mixing — proved here

Put \(\tau=\|C-C^2\|\). Then \(0\le\tau\le1/4\) and

\[
X_A\le F_A\le X_A+\tau I_A.
\]

Consequently,

\[
\boxed{\mathcal N_{F_A}(\theta+\tau)
\le N^\partial_\varepsilon(C;A)
\le\mathcal N_{F_A}(\theta)=N^{\rm raw}_\varepsilon(C;A).}
\]

If \(\theta+\tau\le1/4\), define

\[
\varepsilon_\tau=\frac{1-\sqrt{1-4(\theta+\tau)}}{2}.
\]

Then the lower bound is \(N^{\rm raw}_{\varepsilon_\tau}\), with the endpoint \(\varepsilon_\tau=1/2\) interpreted as the multiplicity of \(1/2\). If \(\theta+\tau>1/4\), the lower comparison count is zero.

**Proof.** Positivity of \(C-C^2\) implies \(0\le C-C^2\le\tau I\). Compressing gives \(0\le T_A\le\tau I_A\). Apply B1 and ordered eigenvalue monotonicity. Solving \(\nu(1-\nu)\ge\theta+\tau\) gives the last assertion. ∎

This quantifies the gap between local occupation counting and cross-boundary counting without assuming that their matrices commute. It recovers B4 when \(\tau=0\).

## B9. Same local covariance, different boundary correlation — proved here

Every positive contraction \(A\) has the projector extension

\[
P_A=\begin{pmatrix}
A&\sqrt{A-A^2}\\
\sqrt{A-A^2}&I-A
\end{pmatrix}
\quad\text{on }\mathcal H_A\oplus\mathcal H_A.
\]

It has the same \(AA\) block as the disconnected positive contraction \(C_0=A\oplus(I-A)\). However,

\[
X_A(P_A)=A-A^2,\qquad X_A(C_0)=0.
\]

**Proof.** The square root exists by the spectral theorem and commutes with \(A\). The diagonal blocks of \(P_A^2\) are \(A^2+(A-A^2)=A\) and \((A-A^2)+(I-A)^2=I-A\). The off-diagonal block is \(A\sqrt{A-A^2}+\sqrt{A-A^2}(I-A)=\sqrt{A-A^2}\). Thus \(P_A^2=P_A=P_A^*\), so it is a positive contraction. The cross blocks give the asserted \(X\)'s. ∎

The local occupation spectrum alone therefore does not determine which part of its defect is boundary correlation and which part is global mixedness. This is a precise limitation of the local record.

## B10. Gaussian number-covariance interpretation — proved here under stated physics assumptions

Let \(a_i,a_i^\dagger\) satisfy the finite fermionic canonical anticommutation relations. Suppose \(\rho\) is a gauge-invariant quasi-free (number-conserving Gaussian) state. Set

\[
C_{ij}=\langle a_j^\dagger a_i\rangle_\rho,
\quad n_i=a_i^\dagger a_i,
\quad N_A=\sum_{i\in A}n_i,\quad N_B=\sum_{j\in B}n_j.
\]

This convention makes one-body evolution under \(H=\sum_{ij}h_{ij}a_i^\dagger a_j\) satisfy \(C(t)=e^{-iht}C(0)e^{iht}\), with \(\hbar=1\). Then

\[
\operatorname{Var}(N_A)=\operatorname{Tr}(A-A^2),\qquad
\operatorname{Cov}(N_A,N_B)=-\operatorname{Tr}X_A,
\]

and hence

\[
\operatorname{Var}(N_A)
=\operatorname{Tr}T_A-\operatorname{Cov}(N_A,N_B).
\]

**Proof.** For \(i\ne j\), Wick factorization and the absence of anomalous pair correlations give

\[
\langle n_i n_j\rangle=C_{ii}C_{jj}-C_{ij}C_{ji}.
\]

For \(i=j\), the CAR give \(n_i^2=n_i\). Thus

\[
\operatorname{Cov}(n_i,n_j)=\delta_{ij}C_{ii}-|C_{ij}|^2.
\]

Sum over \(i,j\in A\) for the variance and over \(i\in A,j\in B\) for the cross covariance. Apply B1 for the last formula. ∎

When \(C\) is a projector, the state is a pure Slater state, and \(\operatorname{Var}(N_A)=\operatorname{Tr}X_A\). For a Gibbs Gaussian state, \(T_A\) is the global thermal occupation defect restricted to \(A\). For a general mixed Gaussian state it is occupation mixedness; calling it thermal requires a thermodynamic preparation. The matrix \(A-A^2\) itself is not a scalar variance; its trace is.

## B11. Counterexamples outside the claimed scope — proved here

**Disconnected thermal state.** If \(C=pI\) with \(\varepsilon\le p\le1-\varepsilon\), then \(N^{\rm raw}_\varepsilon=a\), while \(X_A=0\) and \(N^\partial_\varepsilon=0\). The associated Gaussian state is a product over modes, so its mutual information across the partition is zero. Its local number variance is \(ap(1-p)\).

**Non-Gaussian classical correlations invisible to \(C\).** On two modes, the state

\[
\rho_{\rm cl}=\tfrac12|10\rangle\langle10|+\tfrac12|01\rangle\langle01|
\]

has \(C=\frac12I_2\), hence \(X_A=0\), but \(\operatorname{Cov}(n_1,n_2)=-1/4\) and mutual information \(\log2\). The Gaussian state \(I_4/4\) has the same \(C\), but zero covariance and zero mutual information. This directly disproves B10 without its quasi-free assumption.

**Entanglement invisible to \(C\).** On four modes split as \(A=\{1,2\}\), \(B=\{3,4\}\), let

\[
|\Psi\rangle=\frac{|1100\rangle+|0011\rangle}{\sqrt2}.
\]

It has fixed total particle number two and \(C=\frac12I_4\), so \(X_A=0\). Its reduced state on \(A\) has eigenvalues \(1/2,1/2\), hence entanglement entropy \(\log2\). Each branch has even local parity, so the example does not rely on a local even/odd superposition. The one-body off-diagonal elements vanish because no one-body operator connects the two occupation configurations. Thus the boundary census is not a universal entanglement detector.

## B12. Even the full boundary-strength record does not determine later response — proved here

Consider two modes and

\[
C_\pm=\tfrac12I_2\pm r\sigma_y,
\quad 0<r\le\tfrac12,
\quad h=\omega\sigma_x,\quad \omega>0.
\]

Both matrices are positive contractions. Their local blocks are \(A=D=1/2\), their global eigenvalues are \(1/2\pm r\), and both have \(X_A=X_B=r^2\). Thus both raw and boundary censuses, the full cross-block singular-value list, all occupation spectra, and their Gaussian mutual information agree initially. Under the same number-conserving one-body Hamiltonian,

\[
C_\pm(t)=\tfrac12I_2\pm r\bigl(\cos(2\omega t)\sigma_y+\sin(2\omega t)\sigma_z\bigr),
\]

so

\[
\boxed{\langle n_A\rangle_\pm(t)=\tfrac12\pm r\sin(2\omega t).}
\]

**Proof.** The Pauli matrix \(\sigma_y\) has eigenvalues \(\pm1\), proving positivity and the spectra. Its off-diagonal elements are \(-i,i\), so multiplying each cross block by its adjoint gives \(r^2\). Conjugation by \(e^{-i\omega t\sigma_x}\) gives the stated rotation; alternatively differentiate and use \([\sigma_x,\sigma_y]=2i\sigma_z\). The \(AA\) entry gives the occupation. ∎

The missing datum is a relative phase with respect to the fixed coupling Hamiltonian. The initial currents are **not** matched: the displayed occupations have initial derivatives \(\pm2\omega r\). Thus this is a matched occupation/spectral/boundary-strength example, not the matched density/flow/stress example supplied separately by the kinetic construction. Although a local unitary maps the two initial covariances into each other, using that transformation as a mere change of coordinates would also transform the Hamiltonian. Here the Hamiltonian is held fixed, so the two preparations have physically different phase relative to it. This is an exact observability limitation, not a claim that a census should predict all dynamics.

## B13. Quantitative Gaussian mutual-information bounds — proved here

Define the binary entropy in natural logarithms by

\[
h(x)=-x\log x-(1-x)\log(1-x),\qquad h(0)=h(1)=0.
\]

For the gauge-invariant quasi-free state of B10, its bipartite mutual information is

\[
I_G(A:B)=\operatorname{Tr}h(A)+\operatorname{Tr}h(D)-\operatorname{Tr}h(C).
\]

Then

\[
\boxed{4\operatorname{Tr}X_A\le I_G(A:B).}
\]

If, in addition, \(0<\delta\le1/2\) and

\[
\delta I\le C\le(1-\delta)I,
\]

then

\[
\boxed{I_G(A:B)\le\frac{\operatorname{Tr}X_A}{\delta(1-\delta)}.}
\]

**Proof of the entropy formula.** Diagonalizing the covariance of a gauge-invariant quasi-free state gives independent fermionic occupation modes with probabilities equal to its eigenvalues. Their Bernoulli entropies add, giving \(S(\rho)=\operatorname{Tr}h(C)\). Reduced states remain quasi-free with the compressed covariances \(A,D\), giving the displayed mutual-information formula. Values zero and one follow by continuity, or by including deterministic occupation modes.

**Trace Jensen fact.** If a scalar function \(f\) is concave on an interval and the spectra of Hermitian matrices \(H,K\) lie in it, then

\[
\operatorname{Tr}f(tH+(1-t)K)
\ge t\operatorname{Tr}f(H)+(1-t)\operatorname{Tr}f(K)
\quad(0\le t\le1).
\]

To see this directly, diagonalize \(tH+(1-t)K\) with an orthonormal basis \(u_i\). Apply scalar concavity to the two numbers \(\langle u_i,Hu_i\rangle\) and \(\langle u_i,Ku_i\rangle\). Then scalar Jensen applied to the spectral weights of \(H\) gives \(f(\langle u_i,Hu_i\rangle)\ge\langle u_i,f(H)u_i\rangle\), and likewise for \(K\). Sum over \(i\). For convex \(f\), every inequality reverses. No operator-concavity assumption is being made.

**Proof of the lower bound.** Let

\[
S=I_A\oplus(-I_B),\qquad C_0=A\oplus D=\tfrac12(C+SCS).
\]

The scalar function \(f(x)=h(x)+2x^2\) is concave on \([0,1]\), because in its interior

\[
f''(x)=4-\frac1{x(1-x)}\le0,
\]

and it extends continuously to the endpoints. Trace Jensen and the unitary invariance of trace give \(\operatorname{Tr}f(C_0)\ge\operatorname{Tr}f(C)\). Consequently,

\[
I_G(A:B)\ge2[\operatorname{Tr}C^2-\operatorname{Tr}C_0^2]
=4\operatorname{Tr}(BB^*).
\]

**Proof of the upper bound.** Compression gives the same \([\delta,1-\delta]\) spectral bounds for \(C_0\). On this interval,

\[
g(x)=h(x)+\frac{x^2}{2\delta(1-\delta)}
\]

is convex, since

\[
g''(x)=\frac1{\delta(1-\delta)}-\frac1{x(1-x)}\ge0.
\]

Reversed trace Jensen yields \(\operatorname{Tr}g(C_0)\le\operatorname{Tr}g(C)\). Rearranging and using \(\operatorname{Tr}C^2-\operatorname{Tr}C_0^2=2\operatorname{Tr}X_A\) gives the bound. At \(\delta=1/2\), the only allowed covariance is \(C=I/2\), and both sides vanish. ∎

**Sharpness and consequences.** The lower coefficient 4 is optimal: for \(C=\frac12I_2+r\sigma_x\), with \(r\to0\), one has \(\operatorname{Tr}X_A=r^2\) and

\[
I_G=2\log2-2h(\tfrac12+r)=4r^2+O(r^4).
\]

Combining B5 and B13 gives the rigorous census bound

\[
\boxed{N^\partial_\varepsilon(C;A)\le
\frac{I_G(A:B)}{4\varepsilon(1-\varepsilon)}.}
\]

Within this Gaussian class, \(I_G=0\) if and only if \(X_A=0\): the lower bound gives one direction, and the block-diagonal covariance and entropy formula give the other. This equivalence concerns mutual information, not entanglement. The finite-temperature upper estimate additionally requires a uniform occupation margin \(\delta\); it is not a uniform bound near a pure state.

An independently established Gaussian mutual-information area bound would therefore imply a census area bound with the displayed constant. This conditional implication does not transfer a bosonic theorem to fermions, or establish an area bound by itself. The non-Gaussian counterexamples B11 remain decisive outside the stated class. For entropy measured in bits, divide the natural-log information bounds by \(\log2\).

## Dependency and formalization guide

| Result | Inputs | Proof mechanism | Scope |
|---|---|---|---|
| B1 | Block multiplication | Ring/matrix algebra | No positivity needed |
| B2 | Hermitian positive contraction | Spectral theorem; square completion | Finite-dimensional |
| B3 | Rectangular cross block | Positive-eigenvalue eigenspace correspondence | Finite-dimensional |
| B4 | B1–B2; scalar factorization | Min–max and functional calculus | Exact threshold convention |
| B5 | Nonnegative eigenvalue list | Sum bound | Does not identify MI |
| B6 | Partition-preserving unitary | Matrix conjugation | Partition held fixed |
| B7 | B2; compression norm bound | Product difference; eigenvalue stability | Certified margin required |
| B8 | B1; defect norm | Order and min–max | No commutativity assumption |
| B9 | Positive contraction A | Positive square root | Shows missing global information |
| B10 | CAR; gauge-invariant quasi-free state | Wick factorization | Excludes unmodeled pairing/non-Gaussianity |
| B11 | Explicit density operators | Direct evaluation | Counterexamples to overextension |
| B12 | Explicit Pauli matrices | Exact unitary conjugation | Dynamical phase is extra information |
| B13 | Gauge-invariant quasi-free state; scalar entropy curvature | Trace Jensen and block pinching | Mutual-information bounds, not general entanglement claims |

No result here identifies an ionization threshold with a many-body gap, derives a cosmological mechanism, or proves the original paper's thermodynamic asymptotics. The proposed census can be studied alongside those questions without replacing their missing hypotheses.
