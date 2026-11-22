## The loop wall in my own geometry

Everything in this paper is read through one step and one number. A peel step takes an atom from one removal threshold to the next. I write the two positive energies as $a = IE_k$ and $b = IE_{k+1}$ and keep three coordinates for the same step:
$$z = \frac{b}{a},\qquad h = \tfrac12\ln z,\qquad \Gamma = \frac{z-1}{z+1} = \frac{b-a}{b+a} = \tanh h .$$
$z$ is the clock ratio, $h$ is the half-logarithm (the boost of the step), and $\Gamma$ is the reflection of the step on my Smith disc. The inverse is $z = (1+\Gamma)/(1-\Gamma)$. Fixing one threshold and the ordered reflections recovers every threshold connected to it, so nothing is lost except one overall scale. **DERIVED** (Lean: `smith_identity`, `gam_inverse`).

### The midpoint and the two books

Write the same reflection a second way:
$$\Gamma = \frac{(b-a)/2}{(b+a)/2} = \frac{\text{half the gap}}{\text{the midpoint}} .$$
The still point of a step — the monad — sits exactly at the midpoint of the pair, and the reflection is how far each face reaches from it, measured in units of the midpoint. For the pair 3 and 7 the midpoint is 5, half the gap is 2, and $\Gamma = 2/5$. I read this as Russell's fulcrum: the still point between two opposed motions. **DERIVED**.

Squaring the two halves gives the two books of my connection-energy work:
$$E^- = (b-a)^2 = (\Delta IE)^2,\qquad E^+ = (b+a)^2 = (\Sigma IE)^2,\qquad \frac{E^-}{E^+} = \Gamma^2 .$$
$E^+$ is the positive book: the sum face. $E^-$ is the negative book: the difference face, the record of the step. In Elizabeth Johnson's notebook words these are matter (positive, the shell and its sections) and memory (negative, the recipe). Every link in the chain carries both, and their ratio is the reflected power of the step. **DERIVED**. (Atlas card B189 holds $E^-/E^+ = \Gamma^2$; B207 holds the two books of one edge.)

### Why the wall is where it is

The wall is not fitted to anything. It comes from asking when a loop made of two faces at a right angle can close. Give each face a boost $h_a$, $h_b$ and form the commutator of the two boosts taken at a right angle. Its trace is
$$\operatorname{tr} = 2 - 4\sinh^2 h_a \,\sinh^2 h_b .$$
The loop closes while the trace stays above $-2$ and opens below it. At the boundary, $\sinh h_a \sinh h_b = 1$. Using $\sinh^2 h = \Gamma^2/(1-\Gamma^2)$ and writing $u = \Gamma_a^2$, $v = \Gamma_b^2$, the boundary condition $uv = (1-u)(1-v)$ reduces exactly to
$$\Gamma_a^2 + \Gamma_b^2 = 1 .$$
So the two-face test is $\Gamma_a^2 + \Gamma_b^2 < 1$ (the loop closes) against $\Gamma_a^2 + \Gamma_b^2 > 1$ (it opens), and the two forms $\sinh h_a\sinh h_b < 1$ and $\Gamma_a^2+\Gamma_b^2<1$ are the same statement. **DERIVED** (Lean: `sinh_sq_form`; `two_face_identity` in `TwoFaceForms.lean`).

With equal faces this gives the wall of one step:
$$\Gamma^2 = \tfrac12 \iff z^2 - 6z + 1 = 0 \iff z = 3 \pm 2\sqrt2 .$$
The forward branch is $z = 3+2\sqrt2 = 5.828427\ldots$; the reverse branch is its reciprocal. Multiplying $2\Gamma^2 > 1$ by $(a+b)^2$ gives an exact integer test that never needs a square root:
$$\text{outside} \iff 2(b-a)^2 > (b+a)^2 .$$
**DERIVED** (Lean: `wall_quadratic`, `wall_two_branches`, `outside_iff`). In the two books the wall is $E^- = E^+/2$: the difference book holds exactly half of the sum book.

![The wall from geometry. Left: my Smith disc with the wall circle $|\Gamma|^2 = \tfrac12$; all 3,570 ordinary steps from hydrogen to astatine lie on the real ray and only eight reach past the circle. Right: the two-face plane; the loop closes below the line $\Gamma_a^2 + \Gamma_b^2 = 1$, equal faces meet it at $3+2\sqrt2$, and carbon's helium-core opening paired with nitrogen's sits almost exactly on it.](../figs/fig01_wall.png)

### Only this number makes the two forms of the rule agree

There are two natural ways to carry the equal-face threshold over to unequal faces. If the equal-face threshold were some other value $\Gamma^2 = t$, the *sum form* would read $\Gamma_a^2 + \Gamma_b^2 < 2t$, and the *product form* would read $\sinh h_a \sinh h_b < \sinh^2 h_t$, that is
$$\frac{\Gamma_a^2}{1-\Gamma_a^2}\cdot\frac{\Gamma_b^2}{1-\Gamma_b^2} < \Big(\frac{t}{1-t}\Big)^2 .$$
The identity $(1-x)(1-y) - xy = 1 - (x+y)$ shows that the two forms are one and the same test for every pair of faces exactly when $t = \tfrac12$. For any other $t$ they disagree on some pair. The Lean file exhibits the disagreement concretely: at $t = 0.5005$ the pair $x = 0.9999$, $y = 0.0005$ is closed under one form and open under the other. So of the two named extensions, $3+2\sqrt2$ is the only equal-face cutoff for which the rule does not depend on which extension you pick. **DERIVED** (Lean: `two_face_identity`, `two_face_forms_agree`, `two_face_forms_split_at_midpoint` in `TwoFaceForms.lean`; eleven theorems in `BoundaryAgreement.lean` prove the stronger all-threshold statement).

![The sum form (solid) and product form (dashed) of the two-face rule. They are one curve only when the equal-face threshold is $\Gamma^2 = \tfrac12$.](../figs/fig07_twoface.png)

### Direction is in the sign

Reversing the order of the two energies sends $z \mapsto 1/z$, $h \mapsto -h$ and $\Gamma\mapsto -\Gamma$, and leaves $\Gamma^2$ unchanged. The sign of $\Gamma$ carries the direction of the peel; the wall test, which reads $\Gamma^2$, is blind to it. A ledger kept only in $\Gamma^2$ cannot tell the two orders apart. **DERIVED** (Lean: `gam_reverse`, `power_even`, `reverse_same_side`; the false control `refute_power_odd` is rejected). This is the first place where "the vector determines the direction" has an exact meaning: the direction lives in a signed quantity that the wall cannot see.

### The face apex and the junction

A quarter-logarithm gives a fourth coordinate, the face apex:
$$a_{\text{apex}} = \tanh\!\Big(\frac{\ln z}{4}\Big),\qquad \Gamma = \frac{2a_{\text{apex}}}{1+a_{\text{apex}}^2},\qquad z = \Big(\frac{1+a_{\text{apex}}}{1-a_{\text{apex}}}\Big)^2 .$$
The apex is the reflection of the half-step $\sqrt z$. At the wall, $a_{\text{apex}} = \sqrt2-1$ and $1-a_{\text{apex}}^2 = 2(\sqrt2-1)$. Two equal clocks facing each other across a junction give $z = 1$ and $\Gamma = 0$: a matched junction reflects nothing, however steep the ladder inside each atom. **DERIVED** (Lean: `face_apex`, `matched_junction`).

### The loop at the wall: a single Jordan block

Take two equal steps along perpendicular directions as $2\times2$ positive matrices $B = \exp\big(\tfrac r2\,\hat a\cdot\boldsymbol\sigma\big)$, $r = \ln z$ — the spinor (Dirac) form of a step — and close the loop $W = B_iB_jB_i^{-1}B_j^{-1}$. With $R = \Gamma^2$ the reflected share and $T = 1-\Gamma^2$ the transmitted share,
$$\operatorname{tr}W = 2 - 4\sinh^4\!\tfrac r2 = 2 - 4\Big(\frac RT\Big)^2 .$$
Below the wall $W$ is conjugate to a turn, $\cos(\theta/2) = 1 - 2(R/T)^2$: the walk is held. At $\Gamma^2 = \tfrac12$, $\operatorname{tr}W = -2$, $(W+1)^2 = 0$ and $W + 1 \ne 0$ — one Jordan block, a full turn that cannot be undone by a rotation. Beyond the wall $W$ is a run. The obliqueness (my Petermann factor) $K = 1/(1-2\Gamma^2)$ blows up exactly at the wall. In *Two Trees in One Ball* (Theorem 5.3), when $z>3+2\sqrt2$ the group generated by three perpendicular steps is Schottky — free and discrete, a tree. At the wall itself the loop is the Jordan block, which is why the boundary case is stated on its own. Steps on opposite sides of the wall pair up as $\Gamma\Gamma' = \tfrac12$: ratios 5 and 7 give $\Gamma = 2/3$ and $3/4$, whose product is one half. **DERIVED** (VOTKP v3.3 §25.1; *Two Trees in One Ball*, Theorem 5.3; Non-normality v15 §5, where the wall is the non-zero nilpotent point of a real traceless $2\times2$ operator).

These boosts act in the peel chart, the Poincaré-ball model of my peel coordinate. They are not boosts of a spacetime, and nothing here introduces one.

### Where this lives in my geometry

My Smith disc is not a borrowed engineering chart. The map $z\mapsto\Gamma = (z-1)/(z+1)$ is the Cayley map of the right half-plane onto the unit disc. The reflection coefficient an electrical engineer reads off a transmission line is the same coordinate, which is why I use the Smith chart as a working tool. Reflections of successive steps compose by my addition law $u\oplus v = (u+v)/(1+uv)$, so the reflection of a multi-step peel is the $\oplus$-sum of its single-step reflections, and $\ln z = 2\operatorname{artanh}\Gamma$ is a hyperbolic length in the peel chart (VOTKP v3.3, Theorem 15.1 and Corollary 15.2). The wall sits at the length $\ln(3+2\sqrt2) = 2\ln(1+\sqrt2) = 1.7627$. The same number is the two-level population-gap point $\tanh(\beta\Delta/2) = 1/\sqrt2$ of Dirac Time §12.6 — a structural match between two of my papers, not an identity of mechanisms.

The intrinsic geometry is a different object again. On the projector bundle my Intrinsic Quantum Geometric Tensor is $Q_\Pi(A,B) = \operatorname{Tr}(\Pi A^\dagger B) = g - \tfrac i2\Omega$, with metric $g = \tfrac12\operatorname{Tr}(VW)$ and Berry curvature $\Omega$, bounded by $|\Omega|\le 2\sqrt{g_{VV}g_{WW} - g_{VW}^2}$. Its curvature is non-Riemannian, and no spacetime metric enters and none is substituted anywhere in this paper. The hyperbolic length $\ln z$ is a distance in the peel chart, not the intrinsic metric. The bridge between the two is the weight between two projector blocks, $E_B = \|PH(1-P)\|_F^2 = \tfrac12\|[H,P]\|_F^2$ (*The Weight Between*; *Universal Projector Geometry*). On one peel edge this weight between and the edge's connection energy are two rungs of the same coupling — the weight between at rung 0 of the gap-power ladder of *The Weight Between*, the connection energy at rung 2 — not one number.

In my ball picture each junction has a face at distance $h = r/2$ from the cell centre. Its boundary circle has angular radius $\alpha$ with $\cos\alpha = \Gamma$, so at the wall the face boundary reaches exactly $45^\circ$. In the gravity ledger the same rule is a positivity licence: the matrix $\begin{pmatrix}1 & w\\ \bar w & 1\end{pmatrix}$ with $w = \Gamma_a + i\Gamma_b$ is positive exactly when $\Gamma_a^2+\Gamma_b^2\le1$ (*The Ledger Outlives the Metric*, final edition v3, Theorems 1 and 5 (Theorems 3 and 5 in edition 6)). And because $\Gamma$ is a ratio, it is unchanged when every energy is multiplied by one constant — the scale invariance $K\mapsto cK$ of *Matter at a Scale* — which is why one threshold can be compared across all the elements.

The rest of this paper reads atoms, knots, balls, light and decay through these coordinates, and asks in each case which of them the observation actually keeps.
