## A criterion for what the observer can keep

**DERIVED.** Let a finite-dimensional state obey $\dot x = Lx$, let $R$ be a fixed linear observation, and let $y = Rx$. An autonomous linear equation $\dot y = My$ for all initial states exists exactly when $L\,\ker R \subseteq \ker R$. Indeed $RL = MR$ implies the inclusion. Conversely, define $M(Rx) = RLx$ on the image of $R$; it is well defined because two lifts differ by a vector in the invariant kernel. Extending $M$ to a complement has no effect on an observed state. A perturbation that stays invisible to the observation for all times lies in
$$\bigcap_{j=0}^{d-1} \ker\!\big(RL^{j}\big)$$
for a $d$-dimensional state; the power series and the Cayley–Hamilton identity prove it. An instantaneous record and a complete time trace can keep different information.

Split the state into a retained part $u$ and a hidden part $v$, with generator blocks $A, B, C, D$. Direct integration gives
$$\dot u(t) = A\,u(t) + B\,e^{tD}\,v(0) + \int_0^t B\,e^{(t-s)D}\,C\,u(s)\,ds .$$
The hidden initial condition and the return through the hidden state both matter. The corresponding resolvent correction is $B(\zeta I - D)^{-1}C$ wherever that inverse exists. This fixes which memory term I am asserting: a static threshold table by itself supplies none of the four generator blocks.

A smaller check shows why the lost information matters for operator-valued traits. Let $J$ include the retained orthonormal subspace, $Q = I - JJ^\dagger$, and $A = A^\dagger$. Then
$$J^\dagger A^2 J - \big(J^\dagger A J\big)^2 = (QAJ)^\dagger\, QAJ .$$
For the two-state swap and a one-coordinate observation, the retained $A$ is zero and the retained $A^2$ is one. This is a falsifier for any rule that multiplies compressed observables without auditing the hidden return. The record closes under this square precisely when $QAJ = 0$.

**RECOGNISED.** This criterion gives my programme one standard of evidence. For each proposed reduction I exhibit the retained map and look for two admissible states with identical retained values. If their target readings differ, extra data are necessary. The same reasoning applies to a knot mirror, a pair of differently normalised ladders, a phase-erasing projector or an isotope change. The witness has to be built inside the domain of the particular claim.

$QAJ$ is the off-diagonal block that couples what is kept to what is eliminated, and $(QAJ)^\dagger QAJ$ is the weight carried across that cut — the weight between of *The Weight Between*. It is never negative, and it vanishes only when nothing leaks. The same block returns below as the second book of the peel (see *Projectors give a second book*).
