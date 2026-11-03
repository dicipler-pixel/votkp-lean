# What the boundary coordinate on the Smith disk proves

This note integrates the actual incoming `matter-disk` work at commit `881386a0ab00d917af6334a01423fb8b22469f5e`, especially README §7 and `scripts/s07_boundary_census_disk.py`. It preserves the algebraic extension to biorthogonal idempotents while distinguishing it from the positive-covariance interpretation. The new section is an addition to the source record; the incoming files are retained unchanged.

## D1. The positive-contraction boundary coordinate — proved here

Under B1–B2, each eigenvalue \(\lambda\) of \(X_A=C_{AB}C_{BA}=BB^*\) lies in \([0,1/4]\). Therefore

\[
\Gamma_b(\lambda)=\sqrt{1-4\lambda}\in[0,1]
\]

is a real, unsigned coordinate, and

\[
\lambda=\frac{1-\Gamma_b^2}{4}.
\]

For \(0<\varepsilon<1/2\),

\[
\boxed{\lambda\ge\varepsilon(1-\varepsilon)
\iff\Gamma_b(\lambda)\le1-2\varepsilon.}
\]

**Proof.** The square root is real and nonnegative by B2. Both sides of \(\Gamma_b\le1-2\varepsilon\) are nonnegative. Squaring and rearranging proves the equivalence. ∎

For a pure **orthogonal** projector, B4 identifies \(\lambda=\nu(1-\nu)\), hence

\[
\Gamma_b=\sqrt{1-4\nu(1-\nu)}=|1-2\nu|.
\]

The signed occupation coordinate \(\Gamma=1-2\nu\) is recovered only up to sign. This is equality with its modulus, not equality with the original signed disk point. The map forgets the distinction between \(\nu\) and \(1-\nu\).

For mixed positive contractions, \(X_A\) generally does not commute with \(A\). Its eigenvalues cannot in general be paired level by level with \(\nu(1-\nu)\); the order and count comparisons B4/B8 remain valid. The coordinate lies on a real half-diameter of the Smith disk. Its definition alone provides neither a complex phase nor the disk's full geometry.

## D2. What “back to the rim” means — proved here

If \(C=pI\), then \(X_A=0\), so every \(\Gamma_b=1\), although the raw occupation coordinate is \(1-2p\). At \(p=1/2\), all raw coordinates are zero while all boundary coordinates are one. This is the disconnected product-state control.

More generally, a zero boundary count only proves \(\Gamma_b>1-2\varepsilon\) for each level; it does **not** prove \(\Gamma_b=1\) or \(X_A=0\). The original 128-site uniform-ring result at \(T=0.5\) has zero boundary count at \(\varepsilon=0.1\) but \(\operatorname{Tr}X_A\approx0.170835>0\). Its boundary correlations are below that counting threshold, not absent. The warm-state wording must distinguish the exact disconnected control from an interacting or hopping system with small surviving cross correlations.

## D3. The idempotent algebra survives opening — proved here

Now drop Hermiticity and positivity. On a finite complex vector space with a fixed block decomposition, let

\[
C=\begin{pmatrix}A&B\\E&D\end{pmatrix},\qquad C^2=C.
\]

Define the algebraic cross product \(Y_A=BE=C_{AB}C_{BA}\), which need not equal \(BB^*\). Then

\[
\boxed{Y_A=A-A^2.}
\]

If \(\nu_1,\ldots,\nu_a\) are the eigenvalues of \(A\), with algebraic multiplicity, the eigenvalues of \(Y_A\) are

\[
\lambda_j=\nu_j(1-\nu_j),\qquad j=1,\ldots,a,
\]

again with algebraic multiplicity. This statement allows nontrivial Jordan blocks.

**Proof.** The \(AA\) block of idempotence gives \(A^2+BE=A\). Triangularize \(A\) over \(\mathbb C\). A polynomial in that triangular matrix has diagonal entries given by the polynomial evaluated on its diagonal. Taking the polynomial \(p(z)=z-z^2\) proves the spectral multiset statement, without assuming diagonalizability of \(A\). ∎

This is the precise algebraic content that the incoming §7 opened-chain test verifies numerically. It legitimately carries over to a biorthogonal projector. Positivity bounds and Gaussian-state interpretations do not follow from this algebra alone.

## D4. A branch-independent radial census survives too — proved here

For a complex eigenvalue \(\lambda\), define

\[
R_b(\lambda)=\sqrt{|1-4\lambda|}\in[0,\infty).
\]

For every idempotent in D3,

\[
\boxed{R_b(\nu(1-\nu))=|1-2\nu|.}
\]

Consequently, for any \(r\ge0\), the two multisets give the identical radial count

\[
\#\{j:R_b(\lambda_j)\le r\}
=\#\{j:|1-2\nu_j|\le r\}.
\]

**Proof.** The identity \(1-4\nu(1-\nu)=(1-2\nu)^2\) gives

\[
\sqrt{|1-4\nu(1-\nu)|}
=\sqrt{|1-2\nu|^2}=|1-2\nu|.
\]

Apply D3's spectral multiset mapping. ∎

The radial condition is equivalently

\[
\left|\lambda-\tfrac14\right|\le\tfrac{r^2}{4},
\]

a disk in the complex \(\lambda\)-plane. In the positive-contraction case, restricting \(\lambda\) to \([0,1/4]\) reduces this to the one-sided real inequality used in D1. For general non-Hermitian idempotents, there is no ordered comparison \(\lambda\ge\varepsilon(1-\varepsilon)\) for complex \(\lambda\).

Thus the incoming statement can be repaired precisely: **the idempotent spectral relation and the radial disk count carry over unchanged after using \(R_b\); the PSD census, variance interpretation and real-square-root restriction do not.** Taking a principal complex square root of \((1-2\nu)^2\) gives one of \(\pm(1-2\nu)\), not its modulus. Taking its absolute value, or using the branch-independent formula above, gives the radial coordinate.

## D5. Idempotence alone cannot supply positivity — proved here

The real matrix

\[
C=\begin{pmatrix}2&1\\-2&-1\end{pmatrix}
\]

satisfies \(C^2=C\). Its compression is \(A=2\), and its algebraic cross product is \(Y_A=-2\), which is negative. The radial coordinate is \(R_b=3\), outside the unit disk. If one instead substitutes \(BB^*=1\), the projector identity \(Y_A=A-A^2\) is lost. These two cross products cannot be exchanged silently.

More generally, **every** square complex matrix \(A\) is the compression of the idempotent

\[
\mathcal P(A)=\begin{pmatrix}A&I\\A-A^2&I-A\end{pmatrix}.
\]

**Proof.** Multiply blocks. The upper-left block of \(\mathcal P(A)^2\) is \(A^2+A-A^2=A\); the upper-right is \(A+I-A=I\); the lower-left is \((A-A^2)A+(I-A)(A-A^2)=A-A^2\), since all the terms are polynomials in \(A\); the lower-right is \(A-A^2+(I-A)^2=I-A\). ∎

Hence global idempotence places no positivity or spectral-interval restriction on a general compression. A positive-metric reformulation would require its own declared inner product, adjoint, orthogonal partition and physical interpretation. It is not obtained merely by relabeling a biorthogonal projector as a density covariance.

## D6. Cayley-domain statement with the logarithm branch made explicit — proved here

For \(z\in\mathbb C\setminus\{-1\}\), set \(\Gamma=(z-1)/(z+1)\). Then

\[
|z+1|^2-|z-1|^2=4\operatorname{Re}z,
\]

so

\[
|\Gamma|<1\iff\operatorname{Re}z>0,
\quad |\Gamma|=1\iff\operatorname{Re}z=0,
\quad |\Gamma|>1\iff\operatorname{Re}z<0.
\]

For \(z=e^W\ne-1\), the Cayley expression is \(\tanh(W/2)\), and

\[
|\tanh(W/2)|<1\iff\cos(\operatorname{Im}W)>0.
\]

If \(W=\operatorname{Log}z\) is the principal logarithm with imaginary part in \((-\pi,\pi]\), this is equivalent to

\[
|\operatorname{Im}W|<\pi/2.
\]

**Proof.** Expand the squared moduli. Divide their difference by the positive \(|z+1|^2\), then use \(\operatorname{Re}e^W=e^{\operatorname{Re}W}\cos(\operatorname{Im}W)\). On the stated principal branch, cosine is positive exactly in the indicated open interval. ∎

Without the branch restriction, the interval statement is false: the criterion is periodic modulo \(2\pi\). At \(z=-1\) the Cayley coordinate has a pole and is undefined, rather than an ordinary point outside the disk. For a real occupation \(0<\nu<1\), the odds \(z=(1-\nu)/\nu\) give \(\Gamma=1-2\nu\); the endpoints are obtained by continuous limits.

## D7. Coordinate stability and the nonnormal boundary of the estimate — proved here

For \(\lambda,\widetilde\lambda\in[0,1/4]\),

\[
|\Gamma_b(\lambda)-\Gamma_b(\widetilde\lambda)|
\le2\sqrt{|\lambda-\widetilde\lambda|}.
\]

If both radii are at least \(g>0\), the stronger bound is

\[
|\Gamma_b(\lambda)-\Gamma_b(\widetilde\lambda)|
\le\frac{2}{g}|\lambda-\widetilde\lambda|.
\]

**Proof.** For nonnegative \(x,y\), \(|\sqrt x-\sqrt y|\le\sqrt{|x-y|}\). Apply this with \(x=1-4\lambda\), \(y=1-4\widetilde\lambda\). Alternatively, rationalizing gives the exact identity

\[
|\Gamma_b(\lambda)-\Gamma_b(\widetilde\lambda)|
=\frac{4|\lambda-\widetilde\lambda|}{\Gamma_b(\lambda)+\Gamma_b(\widetilde\lambda)},
\]

when the denominator is nonzero, proving the second bound. If both radii vanish the first bound is immediate. ∎

Combining D7 with B7 gives a \(2\sqrt\delta\) coordinate bound for corresponding ordered Hermitian boundary eigenvalues when \(\|C-\widetilde C\|\le\delta\). The square-root loss near the center is real: changing \(\lambda=1/4\) to \(1/4-h\) changes its radius from zero to \(2\sqrt h\).

The scalar radial map \(R_b\) obeys the same one-half Hölder estimate for complex \(\lambda\), by the reverse triangle inequality. However, B7's eigenvalue perturbation step is a Hermitian result and cannot be transferred to nonnormal matrices. For example,

\[
J_0=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
J_\delta=\begin{pmatrix}0&1\\\delta&0\end{pmatrix}
\]

differ in norm by \(\delta\), but their eigenvalues change from \(0,0\) to \(\pm\sqrt\delta\). By D5, these matrices can themselves be embedded as compressions of idempotents. A computed non-Hermitian residual therefore needs a conditioning or pseudospectral analysis before it becomes a certified disk count. Idempotence alone does not supply that analysis.

## What this joins and what it does not identify

The occupation odds, boundary-strength radius and gas-population odds share exact coordinate identities. Their underlying records remain different: an eigenvalue of a local covariance, a cross-boundary singular strength, and a charge-population ratio are distinct observables. These maps create no missing matrix elements, history labels or experimental data. Their value is a precise common language in which the hypotheses and lost information can be written and tested.
