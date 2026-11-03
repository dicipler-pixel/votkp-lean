# Atomic records, finite Saha closure, and resolved response

Formal mathematical supplement for Jeromie Beasley's Matter–Gases–VOTKP project, 3 November 2026. This document proves finite-dimensional and finite-charge statements under explicit hypotheses. It does not identify ionization thresholds with collective gaps, establish local thermodynamic equilibrium in a specimen, or infer a gas memory kernel from the xenon delay table. These are standard mathematical constructions developed into a precise account of the proposed bridge; no priority claim is made.

The original source records are Beasley, *Matter at a Scale*, v5, DOI [10.5281/zenodo.22019893](https://doi.org/10.5281/zenodo.22019893), and *VOTKP*, v2.9, DOI [10.5281/zenodo.23340757](https://doi.org/10.5281/zenodo.23340757). The companion deep-dive archive preserves the original sources, the helium input rows with their grades, and the retrospective xenon source-table reproduction.

## 1. Positive threshold records

Fix an integer $Z\geq1$. A complete positive threshold ladder is $I=(I_0,\ldots,I_{Z-1})\in(0,\infty)^Z$. The index labels successive relaxed charge-state removals. It is not an excitation-energy label within one fixed-charge Hamiltonian. Define, for $0\leq q<Z-1$,

\[
\Gamma_q=\frac{I_{q+1}-I_q}{I_{q+1}+I_q}.
\]

**Theorem G1 — anchored coordinate equivalence.** The map

\[
I\longmapsto (I_0,\Gamma_0,\ldots,\Gamma_{Z-2})
\]

is a bijection from $(0,\infty)^Z$ onto $(0,\infty)\times(-1,1)^{Z-1}$. Its inverse is

\[
I_q=I_0\prod_{j=0}^{q-1}\frac{1+\Gamma_j}{1-\Gamma_j}.
\]

*Proof.* Positivity gives 
$-1<(b-a)/(b+a)<1$ for every $a,b>0$. Direct algebra gives
$(1+\Gamma)/(1-\Gamma)=b/a$. Multiplying adjacent ratios telescopes. Conversely, for any positive anchor and ratios in $(-1,1)$, every factor in the displayed inverse is positive, and the adjacent Cayley transform recovers the supplied ratio. For $Z=1$, the ratio vector is empty and the positive anchor is the whole record. ∎

**Corollary G1a — scale quotient and binding sum.** Positive common scaling $I\mapsto cI$ leaves every $\Gamma_q$ unchanged. Two connected positive ladders have identical ratio vectors if and only if they differ by one positive common scale. The anchored vector determines the remaining electronic binding sums $B_q=\sum_{j=q}^{Z-1}I_j$.

*Proof.* Common scaling cancels in each ratio. Equal ratios give equal adjacent quotients, hence by induction $I'_q/I_q=I'_0/I_0$. The binding sums are functions of the reconstructed ladder. ∎

**Information consequence.** Any function of the complete threshold ladder can be re-expressed as a function of the complete anchored vector, and conversely. A change of coordinates can change numerical conditioning or a chosen statistical representation; it cannot add physical information. Neither representation determines a specimen's temperature, density, partition weights, transition matrix elements, collision rates or preparation. Missing ladder entries remain missing data.

## 2. Finite Saha closure

Fix $Z\geq1$, a nucleus number density $N>0$, and positive coefficients $S_0,\ldots,S_{Z-1}>0$. These coefficients have number-density units. The abstract finite Saha model is

\[
\frac{n_{q+1}}{n_q}=\frac{S_q}{x},\qquad
\sum_{q=0}^{Z}n_q=N,\qquad
x=\sum_{q=0}^{Z}q n_q,
\]

where $x=n_e>0$ is the electron number density. All charge states from 0 to $Z$ are included. The final condition is charge neutrality for a pure species with no imposed background charge. Mixtures, externally supplied electrons and non-LTE kinetics require different closure equations.

Set $a_0=1$, $a_q=\prod_{j=0}^{q-1}S_j$, and for $x>0$ define

\[
W(x)=\sum_{q=0}^{Z}a_qx^{-q},\qquad
p_q(x)=\frac{a_qx^{-q}}{W(x)},\qquad
\mu(x)=\sum_q q p_q(x),\qquad
V(x)=\sum_q(q-\mu(x))^2p_q(x).
\]

Every population is strictly positive. Therefore $0<\mu(x)<Z$ and $V(x)>0$. The population ratios and normalization hold by construction, so neutrality is equivalent to $x=N\mu(x)$.

**Lemma G2 — exponential-family derivative.** Writing $y=\log x$,

\[
\frac{d p_q}{dy}=p_q(\mu-q),\qquad
\frac{d\mu}{dy}=-V.
\]

More generally, for a fixed function $f$ on the charge labels,
\[
\frac{d}{dy}\mathbb E_p[f(q)]=-\operatorname{Cov}_p(f(q),q).
\]

*Proof.* Differentiate the finite sum: $dW(e^y)/dy=-\sum_q q a_qe^{-qy}=-\mu W$. Logarithmic differentiation of $p_q$ gives $\mu-q$. Multiplication by $q$ and summation gives $\mu^2-\mathbb E[q^2]=-V$. The same calculation with $f$ gives the covariance identity. ∎

**Theorem G3 — unique positive charge-neutral state.** The finite Saha model has exactly one positive solution. Its electron density lies in $0<x<NZ$, and its populations are the $p_q(x)$ above.

*Proof.* Let $F(x)=x-N\mu(x)$. It is continuously differentiable and
\[
F'(x)=1+\frac{NV(x)}x>1.
\]
As $x\downarrow0$, the highest-charge weight dominates, so $p_Z\to1$, $\mu\to Z$, and $F\to-NZ<0$. At $x=NZ$, strict positivity of lower charge populations gives $\mu(NZ)<Z$, hence $F(NZ)>0$. The intermediate value theorem gives a root and strict monotonicity gives uniqueness. Ratios and normalization uniquely prescribe the populations for a given $x$; therefore the complete neutral solution is unique. ∎

**Corollary G3a — stable log equation and polynomial form.** The log-neutrality function
\[
g(y)=y-\log N-\log\mu(e^y)
\]
has derivative $g'(y)=1+V/\mu>1$, tends to $-\infty$ as $y\to-\infty$, and is positive at $y=\log(NZ)$. It has the same unique root. Equivalently, $x$ is the unique positive root of
\[
P(x)=\sum_{q=0}^{Z}a_qx^{Z-q+1}
-N\sum_{q=0}^{Z}q a_qx^{Z-q}.
\]
The degree is $Z+1$. This is a uniqueness theorem for the physical positive root, not a claim that all polynomial roots are real.

For helium, $Z=2$, writing $u=x/N$, $\alpha=S_0/N$ and $\beta=S_1/N$, the independent equation is
\[
u^3+\alpha u^2+(\alpha\beta-\alpha)u-2\alpha\beta=0,
\qquad 0<u<2.
\]

## 3. Exact comparative statics

All quantities below are evaluated at the unique neutral solution. Their smooth dependence follows from Theorem G3 and the implicit function theorem, since $F'(x)>1$.

**Theorem G4 — density response and stochastic ordering.** At fixed positive Saha coefficients,
\[
\frac{d\log x}{d\log N}=\frac{\mu}{\mu+V}\in(0,1),
\qquad
\frac{d\mu}{d\log N}=-\frac{\mu V}{\mu+V}<0,
\]
and
\[
\frac{d\log p_q}{d\log N}
=(\mu-q)\frac{\mu}{\mu+V}.
\]
Thus electron density increases with nucleus density, whereas the mean charge decreases. The neutral fraction increases. Every upper-charge tail $\Pr(q\geq r)$, $1\leq r\leq Z$, strictly decreases with nucleus density. Intermediate individual charge populations need not be monotone over an entire density range.

*Proof.* Differentiate $x=N\mu(x)$:
\[
\frac{dx}{dN}=\frac{\mu}{1+NV/x}
=\frac{\mu^2}{\mu+V}>0.
\]
Use $x=N\mu$ to obtain the log derivative and differentiate $\mu=x/N$ to obtain its derivative. Lemma G2 gives the formula for individual probabilities. For an upper-tail indicator $f(q)=\mathbf1_{q\geq r}$, the covariance in Lemma G2 is strictly positive. Indeed, for independent charge labels $q,q'$,
\[
\operatorname{Cov}(f(q),q)
=\frac12\sum_{i,j}p_ip_j\big(f(i)-f(j)\big)(i-j)>0,
\]
because every term is nonnegative and at least one pair straddles the threshold. Since $x$ increases with $N$, the tail decreases. Equivalently, for $x_2>x_1$, the likelihood ratio $p_q(x_2)/p_q(x_1)$ is a positive constant times $(x_1/x_2)^q$, which decreases strictly with $q$. ∎

**Theorem G5 — coefficient and parameter response.** Let $\theta$ vary the positive coefficients smoothly at fixed $N$. Put
\[
h_q=\partial_\theta\log a_q,\qquad
C_h=\operatorname{Cov}_p(q,h_q).
\]
Then
\[
\partial_\theta\log x=\frac{C_h}{\mu+V},\qquad
\partial_\theta\mu=\frac{\mu C_h}{\mu+V},
\]
and
\[
\partial_\theta p_q
=p_q\left[h_q-\mathbb E(h)-(q-\mu)\frac{C_h}{\mu+V}\right].
\]
If $h_q$ is increasing and nonconstant, then $C_h>0$, and mean charge increases strictly. In particular, increasing any one coefficient $S_r$ increases mean charge: for $\theta=\log S_r$, $h_q=\mathbf1_{q>r}$.

*Proof.* At fixed $x$, logarithmic differentiation gives $\partial_\theta p_q=p_q(h_q-\mathbb E h)$, so $\partial_\theta\mu=C_h$. The additional change through $x$ contributes $-V\partial_\theta\log x$ by Lemma G2. Differentiating neutrality at fixed $N$ gives $\partial_\theta\mu=\mu\partial_\theta\log x$, hence $(\mu+V)\partial_\theta\log x=C_h$. Substitution proves the displayed formulas. The covariance sign follows from the pairwise identity used in Theorem G4. ∎

For simultaneous variations of density and coefficients, the same computation gives the differential identity
\[
d\log x=\frac{\mu}{\mu+V}\,d\log N
+\frac{\operatorname{Cov}(q,d\log a_q)}{\mu+V},
\]
\[
d\mu=\frac{\mu}{\mu+V}
\left[\operatorname{Cov}(q,d\log a_q)-V\,d\log N\right].
\]
Here $d\log a_q$ is a charge-indexed differential; its covariance is taken over the current equilibrium populations.

## 4. Physical Saha coefficients and the VOTKP input

For the stated ideal, nonrelativistic, thermodynamic-equilibrium model,
\[
S_q(T)=\frac{2}{\lambda_e(T)^3}\frac{U_{q+1}(T)}{U_q(T)}
\exp[-I_q/(k_BT)],\qquad
\lambda_e(T)=\frac{h}{\sqrt{2\pi m_e k_BT}}.
\]
The factor 2 accounts for electron spin under this partition convention. $U_q$ are positive internal partition weights and must use a consistent truncation and energy reference. The previous numerical helium experiment used ground-state weights $(1,2,1)$, not a complete excited-state equation of state.

Substituting Theorem G1 gives the exact re-expression
\[
S_q(T)=\frac{2}{\lambda_e(T)^3}\frac{U_{q+1}(T)}{U_q(T)}
\exp\left[-\frac{I_0}{k_BT}
\prod_{j<q}\frac{1+\Gamma_j}{1-\Gamma_j}\right].
\]
This is Saha with a reconstructed threshold input, not a new ionization law. It exposes the independent inputs: the absolute thermal energy ratio, density relative to the electron thermal wavelength, internal partition ratios, and a justified equilibrium assumption.

**Theorem G6 — temperature response for fixed partition weights.** Assume $m_e,h,k_B$ fixed, every $I_q>0$, and every $U_q>0$ independent of $T$. Define cumulative removal energies $E_0=0$, $E_q=\sum_{j<q}I_j$. At fixed nucleus density,
\[
\frac{d\log x}{d\log T}
=\frac{\operatorname{Cov}\left(q,\frac32q+\frac{E_q}{k_BT}\right)}{\mu+V}>0,
\qquad
\frac{d\mu}{d\log T}>0.
\]

*Proof.* Telescoping the internal partition ratios gives
$a_q=(2/\lambda_e^3)^q(U_q/U_0)e^{-E_q/(k_BT)}$. Its logarithmic temperature derivative is $h_q=3q/2+E_q/(k_BT)$. Each adjacent increment is $3/2+I_q/(k_BT)>0$. Theorem G5 applies. ∎

This theorem concerns electron density and mean charge. It does not assert monotonicity of every individual charge fraction. With temperature-dependent $U_q(T)$, the derivative includes $d\log(U_q/U_0)/d\log T$; the stated positivity proof then needs an additional condition. It does not follow solely from threshold positivity.

At fixed $T,N,U,m_e$, increasing any threshold $I_r$ decreases mean charge. In fact Theorem G5 gives
\[
\frac{\partial\mu}{\partial I_r}
=-\frac{\mu}{k_BT(\mu+V)}
\operatorname{Cov}(q,\mathbf1_{q>r})<0.
\]
Consequently, common multiplicative scaling of all threshold energies by a factor greater than one at fixed specimen conditions leaves every $\Gamma_q$ fixed but changes the neutral solution. The missing absolute anchor is physically consequential.

**Theorem G7 — complete scaling covariance.** In the abstract finite Saha model, the simultaneous transformation $S_q\mapsto cS_q$, $N\mapsto cN$, $c>0$, preserves every charge fraction and takes $x\mapsto cx$.

*Proof.* The ratios $S_q/x$ and neutrality $x=N\mu$ are preserved by the proposed transformation. Theorem G3 makes the transformed solution unique. Equivalently, the fractions depend only on the dimensionless coefficients $S_q/N$. ∎

For the physical coefficients, take positive scale factors $a,b$ and impose
\[
m_e' = a m_e,\quad T'=bT,\quad I_q'=bI_q,
\quad \frac{U'_{q+1}(T')}{U'_q(T')}=\frac{U_{q+1}(T)}{U_q(T)},
\quad N'=(ab)^{3/2}N.
\]
Then $S'_q=(ab)^{3/2}S_q$, so all populations are invariant. Fixed electron mass gives the density factor $b^{3/2}$. Scaling mass and energy/temperature together by $c$ gives the density factor $c^3$. These are conditional covariances of a specified model. They are not an assertion that fundamental constants or real helium thresholds can be changed arbitrarily, nor a cosmological mechanism.

**Corollary G7a — record insufficiency in the declared model.** No function of the complete anchored atomic threshold record alone determines mean charge for all positive specimen densities at fixed $T,U,m_e$: Theorem G4 makes that mean strictly density-dependent. No function of the unanchored ratio vector alone determines it even at fixed $T,N,U,m_e$: common threshold scaling leaves that vector fixed and changes the mean by Theorem G6's threshold derivative. These are exact non-identifiability statements, not empirical regression findings.

## 5. Retained and hidden amplitudes: the full reduced equation

Let $\mathcal H=\mathcal H_A\oplus\mathcal H_B$ be finite-dimensional complex inner-product spaces with a specified orthogonal split. Let
\[
H=\begin{pmatrix}A&B\\B^\dagger&D\end{pmatrix}=H^\dagger,
\qquad \psi(t)=\binom{x(t)}{y(t)},\quad i\hbar\dot\psi=H\psi,
\]
with $\hbar>0$. The partition is physical data. If it is an invariant spectral subspace of this same undriven $H$, then $B=0$ and the coupling kernel is trivial.

**Theorem R1 — exact reduced equation, including hidden preparation.** Define
\[
K(t)=B e^{-iDt/\hbar}B^\dagger,\qquad
J(t)=B e^{-iDt/\hbar}y(0).
\]
Then the retained amplitude solves
\[
\dot x(t)=-\frac{i}{\hbar}Ax(t)-\frac{i}{\hbar}J(t)
-\frac1{\hbar^2}\int_0^tK(t-s)x(s)\,ds.
\]

*Proof.* Variation of constants in the hidden equation gives
\[
y(t)=e^{-iDt/\hbar}y(0)
-\frac{i}{\hbar}\int_0^te^{-iD(t-s)/\hbar}B^\dagger x(s)\,ds.
\]
Substituting into $\dot x=-i(Ax+By)/\hbar$ gives the formula, including the minus sign in front of the integral. ∎

The specified $A,K,J,x(0)$ uniquely determine the finite-dimensional retained evolution. This can be seen directly from the original finite linear system, or by the uniqueness theorem for a linear Volterra equation with continuous kernel. A kernel without the hidden-source term does not specify evolution when $y(0)\ne0$.

**Theorem R2 — positive channel measure and Schur response.** If $E_D$ is the spectral projection measure of $D$, the finite positive operator-valued measure
\[
d\mathsf M(\lambda)=B\,dE_D(\lambda)\,B^\dagger
\]
satisfies
\[
K(t)=\int e^{-i\lambda t/\hbar}\,d\mathsf M(\lambda),\qquad
\Sigma(z)=B(zI-D)^{-1}B^\dagger
=\int\frac{d\mathsf M(\lambda)}{z-\lambda}.
\]
When the indicated inverses exist, the retained block of $(zI-H)^{-1}$ is
\[
G_A(z)=\big(zI-A-\Sigma(z)\big)^{-1}.
\]
In particular, $K(0)=\mathsf M(\mathbb R)=BB^\dagger$ is only the total channel mass, not the measure's frequency distribution.

*Proof.* The spectral theorem yields the two integral formulas, and each atom of the measure is positive semidefinite because $B E_D(\{\lambda\})B^\dagger\succeq0$. Block Gaussian elimination gives the Schur inverse formula. ∎

For $\operatorname{Im}z>0$,
\[
\operatorname{Im}\Sigma(z)
=-(\operatorname{Im}z)B\big((\operatorname{Re}z-D)^2+(\operatorname{Im}z)^2I\big)^{-1}B^\dagger\preceq0.
\]
Also $K$ is positive definite as an operator-valued function: for any finite times $t_j$ and retained vectors $u_j$,
\[
\sum_{j,k}u_j^\dagger K(t_j-t_k)u_k
=\left\|\sum_k e^{iDt_k/\hbar}B^\dagger u_k\right\|^2\geq0.
\]
These properties constrain admissible channel kernels. They do not turn a scalar delay curve into a fully reconstructed matrix measure.

## 6. Equal full spectra and coupling footprint, unequal later response

The following exact witness is deliberately finite-dimensional. It proves an information limitation for spectral lists and instantaneous coupling footprints, not the existence of a particular gas preparation in a laboratory.

Set $\hbar=1$, fix the retained subspace $\operatorname{span}\{e_0\}\subset\mathbb R^4$, and let
\[
\Lambda=\operatorname{diag}(-3,-1,1,3),\qquad
w^{(0)}=(1,1,1,1)/4,\quad
w^{(1)}=(3,7,1,5)/16.
\]
For either positive unit-sum weight vector $w$, set $s=(\sqrt{w_0},\ldots,\sqrt{w_3})^T$, $v=e_0-s$, and define the explicit Householder matrix
\[
R_w=I-\frac{vv^T}{1-s_0},\qquad H_w=R_w\Lambda R_w^T.
\]
The denominator is nonzero for these weights. Since $v^Tv=2(1-s_0)$, one has $R_w^TR_w=I$, $R_w^T=R_w$, and $R_we_0=s$. Thus $H_w$ is a real symmetric Hamiltonian with the declared eigenvalues and a fixed retained projector $e_0e_0^T$. This is a constructive matrix formula, not merely an existence appeal to a change of basis.

**Theorem R3 — spectral and instantaneous-footprint insufficiency.** Both $H_{w^{(0)}}$ and $H_{w^{(1)}}$ have exactly the spectrum $\{-3,-1,1,3\}$, retained diagonal $A=0$, and $BB^T=5$. With the same initial full state $\psi(0)=e_0$, hence $x(0)=1$ and $y(0)=0$, their retained survival probabilities at $t=\pi/4$ are respectively $0$ and $1/32$.

*Proof.* The unit-sum moments satisfy
\[
\sum_jw^{(0)}_j\lambda_j=\sum_jw^{(1)}_j\lambda_j=0,\qquad
\sum_jw^{(0)}_j\lambda_j^2=\sum_jw^{(1)}_j\lambda_j^2=5.
\]
These give $A=e_0^TH_we_0=0$ and
$BB^T=e_0^TH_w^2e_0-A^2=5$. The retained amplitude is
\[
a_w(t)=e_0^Te^{-iH_wt}e_0=\sum_jw_je^{-i\lambda_jt}.
\]
For $w^{(0)}$, $a_0(t)=(\cos3t+\cos t)/2$. The difference weights are $(-1,3,-3,1)/16$, so
\[
a_1(t)-a_0(t)
=\frac{i}{8}(3\sin t-\sin3t)
=\frac{i}{2}\sin^3t.
\]
At $t=\pi/4$, $a_0=0$ and $a_1=i\sqrt2/8$, whose squared magnitudes are $0$ and $1/32$. Both hidden-source terms are zero because the same initial state is wholly retained. ∎

The weighted third moments are 0 and 3. This identifies the first lost distinction: $BDB^T$ is respectively 0 and 3, and $K'(0)=-iBDB^T$ differs even though $K(0)$ agrees.

The Schur responses are also explicit. With
\[
Q(z)=(z^2-1)(z^2-9)=z^4-10z^2+9,
\]
the retained resolvents are
\[
G_0(z)=\frac{z^3-5z}{Q(z)},\qquad
G_1(z)=\frac{z^3-5z+3}{Q(z)}.
\]
Since $A=0$, $\Sigma=z-G^{-1}$, hence
\[
\Sigma_0(z)=\frac{5z^2-9}{z^3-5z},\qquad
\Sigma_1(z)=\frac{5z^2+3z-9}{z^3-5z+3}.
\]
These meromorphic identities hold away from their poles, with analytic continuation where removable. Both self-energies begin with $5/z$ at large $z$, but their next coefficients differ. The full eigenvalue list supplies possible energies; their spectral weights relative to the fixed retained observable carry additional information.

The same finite-difference null vector appears in the companion classical moment-matching construction. The shared fact is cancellation of the first three moments. Classical streaming density, quantum survival probability and an atomic removal-threshold list remain different observables and must not be equated.

## 7. Same kernel, different hidden initial source

**Proposition R4 — kernel-only evolution is underdetermined.** Take
\[
H=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
\psi_\pm(0)=\frac1{\sqrt2}\binom{1}{\pm i},\quad \hbar=1.
\]
The retained amplitudes at time zero are identical, $A=D=0$, and $K(t)=1$ is identical. Nevertheless
\[
|x_\pm(t)|^2=\frac12\big(1\pm\sin2t\big),
\]
so the retained probabilities at $t=\pi/4$ are 1 and 0.

*Proof.* Here $e^{-iHt}=\cos t\,I-i\sin t\,H$. Its first component gives $x_\pm=(\cos t\pm\sin t)/\sqrt2$. Squaring gives the result. The hidden sources are $J_\pm=\pm i/\sqrt2$, so Theorem R1 predicts the distinction exactly. ∎

This example changes the initial state, whereas Theorem R3 keeps the initial state fixed and changes its resolved spectral weights through the Hamiltonian. They demonstrate two separate omissions. A proposed history experiment must declare which one it varies and which current measurements it matches.

## 8. Evidence and formalization boundary

The incoming matter-disk §8 reverse-recovery construction is developed in `gas_peel_inverse.md`, which supplies Theorems G8–G9: population-combination reconstruction of the threshold ladder, exact partition corrections, and deterministic inversion-error bounds. It is part of this account. Its synthetic excited-partition opposite was specified in a separate prospective addendum before execution. The retained-response theorem labels were changed from M1–M4 to R1–R4 to avoid a collision with the manuscript's separate moment theorem; this administrative relabeling changes no claim, tolerance or test prediction.

Theorem labels G1–G7 and R1–R3, with their corollaries and Proposition R4, are human-readable analytic proofs in this supplement. Machine-checked coverage is only what the project's Lean theorem manifest explicitly lists; a passing numerical script is not a Lean proof. No theorem here assumes a desired physical conclusion under a renamed hypothesis.

`verify_formal_gas.py` executes the prospective checks specified in `PREREGISTERED_FORMAL_CONTROLS.md`, produces `formal_gas_results.json`, and records the protocol SHA-256. Rational ladder reconstruction, manufactured neutrality polynomials and resolvent numerators are checked in exact arithmetic. Finite-difference responses and matrix exponentials are floating-point implementation checks with recorded tolerances. No threshold, temperature or coefficient is fitted to measured populations or delays.

The original helium source grades remain E for 24.587389011 eV and T for 54.4177655282 eV. The archival xenon value remains a retrospective published channel-delay contrast, $114.323\pm35.0164$ as at 75.36 eV, not a matched-history gas experiment or a recovered positive matrix measure. Its raw-scan reconstruction, systematic-error audit and microscopic kernel inference remain separate work.

The next physical test should specify a real specimen, retain its measured preparation variables, choose a justified equilibrium or kinetic model, and predict a new resolved response before inspecting it. The finite proofs above determine which records are sufficient inside their declared models and which proposed summaries necessarily lose information.
