# Two different angle tests for the Be–Rb mixed face

Jeromie Beasley’s elemental peel table · Codex mathematical check · 21 November 2026

**DERIVED.** At the right angle prescribed in the original protocol, the two disk perpendiculars and the four-stage transfer commutator give the same class. Tilting the angle separates them. For the helium-core openings of beryllium and rubidium, taking the comparison-disk angle from 90° to 89.9° closes the disk loop. A direct product of the original four transfer stages still gives a negative-trace hyperbolic return. Its angle response is symmetric about 90°. The disk responds to the sign of the tilt. The original right-angle prediction remains valid. The distinction matters for alignment tolerances and for testing the angular dependence experimentally.

## Disk geometry and the forward sector

Put \(h_a=\frac12\ln a\), \(h_b=\frac12\ln b\), \(x=\tanh h_a\) and \(y=\tanh h_b\). Take forward inputs \(a,b>1\) and let \(0<\theta<\pi\) be the angle between the two forward axes drawn through the disk centre. In Klein coordinates the two supporting faces are \(X=x\) and \(X\cos\theta+Y\sin\theta=y\). Writing \(c=\cos\theta\), the sign of the squared radius of their intersection minus one is the sign of

\[
F(c)=c^2-2xyc+x^2+y^2-1.
\]

A finite intersection requires \(F<0\). Equality gives ideal contact. For the intersection to be inside the forward sector, its two axis coefficients must be positive, equivalently \(x-cy>0\) and \(y-cx>0\). The two ideal contacts have cosines \(xy\pm\sqrt{(1-x^2)(1-y^2)}\). Near 90° the sector test holds for both Be–Rb faces. In radians the derivative of \(F(\cos\theta)\) there is \(2xy=0.9704958472\ldots\). This geometric derivation and the general sector qualification are already on the branch. The new tests below use the selected pair, the transfer model and their angle calibrations together. [Original disk construction](https://github.com/dicipler-pixel/votkp-lean/blob/893bd1018b22fcc575194196975fc9650d2006fb/research/2026-11-20-element-paper-loop-wall/batch8/lambert/mixed_faces.md)

## Four stages with rotated stretching axes

Let \(D(h)=\operatorname{diag}(e^h,e^{-h})\), and let \(R(\phi)\) be a real plane rotation. Define \(A=D(h_a)\), \(B=R(\theta/2)D(h_b)R(-\theta/2)\) and \(W=ABA^{-1}B^{-1}\). This convention maps the 90° comparison-disk setting to a 45° angle between the *expanding eigenvectors* of the transfer stages. Report both angles in any apparatus. The off-diagonal entry of \(B\) is \(b_{12}=\sinh h_b\sin\theta\). Since \(\det B=1\), direct expansion gives

\[
\operatorname{tr}W=2-(e^{h_a}-e^{-h_a})^2 b_{12}^2
=2-4\sinh^2 h_a\sinh^2 h_b\sin^2\theta .
\]

For \(p=\sinh h_a\sinh h_b>1\), the negative-trace hyperbolic interval is \(\arcsin(1/p)<\theta<\pi-\arcsin(1/p)\). At 90° the angular slope vanishes, and the second derivative in radians is \(8p^2\). This even response misses the linear disk change. Equal right-angle classifications follow from \(p^2>1\iff x^2+y^2>1\). The angle-domain equality fails in both directions for Be–Rb, as the 89.9° and 93° rows below show.

## A two-stage transfer realization of the oblique disk test

For each face at axis angle \(\phi\), put \(t=\sinh h\), \(u=\cosh h\cos\phi\), \(v=\cosh h\sin\phi\) and define

\[
N(h,\phi)=\begin{pmatrix}u&t+v\\v-t&-u\end{pmatrix},\qquad E=\operatorname{diag}(1,-1).
\]

The relation \(u^2+v^2-t^2=1\) gives \(N^2=I\) and \(\det N=-1\). Form \(P=N(h_a,0)N(h_b,\theta)\). The two factors \(N(h_a,0)E\) and \(E N(h_b,\theta)\) have determinant +1, and their product is exactly \(P\). This gives a target for a calibrated realization using determinant-one stages. Realizability, gain, loss, alignment and error budgets of a particular apparatus require separate characterization. The matrix product gives

\[
K=\tfrac12\operatorname{tr}P
=\cosh h_a\cosh h_b\cos\theta-\sinh h_a\sinh h_b
=\frac{c-xy}{\sqrt{(1-x^2)(1-y^2)}} .
\]

Expanding shows \((1-x^2)(1-y^2)(K^2-1)=F(c)\). Thus \(|\operatorname{tr}P|<2\) returns the finite supporting-face intersection for every interior axis angle. The sector test above selects the forward intersection. Angle reversal about 90° changes the sign of the \(c\) term, furnishing the missing first-order response. Inverting both positive clocks changes both signed reflections but preserves \(K\) at fixed axes. At 90° specifically, \(\operatorname{tr}W=2-(\operatorname{tr}P)^2\). The two measured traces have different scales even at that angle.

## Pinned elemental inputs and checks

| Face | Earlier energy (eV) | Next energy (eV) | Ratio |
|---|---:|---:|---:|
| Be, removals 2→3 | 18.21115(4), E | 153.896205(4), T | 8.45065825058 |
| Rb, removals 35→36 | 4356.865(10), T | 18305.886(4), T | 4.20161882454 |

Grades and widths are those of the [pinned archive](https://github.com/dicipler-pixel/votkp-lean/blob/893bd1018b22fcc575194196975fc9650d2006fb/data/element_thresholds_20261011.json.gz). These ratios refer to internally calibrated faces; the angle belongs to the chosen comparison construction.

| Disk angle θ | Stretch eigenvector angle θ/2 | Disk margin F | Four-stage trace | Two-stage trace |
|---:|---:|---:|---:|---:|
| 89.0° | 44.5° | −0.01625294 | −2.00524471 | −1.92962558 |
| 89.9° | 44.95° | −0.00131083 | −2.00645282 | −1.99441624 |
| 90.0° | 45.0° | +0.00037996 | −2.00646503 | −2.00161560 |
| 90.1° | 45.05° | +0.00207684 | −2.00645282 | −2.00881497 |
| 93.0° | 46.5° | +0.05391084 | −1.99549111 | −2.21749796 |

The two disk supporting faces first make ideal contact at 14.04529340°. Their intersection enters the open forward sector at 38.67292542°, then reaches the second ideal contact at **89.97755908°**. Its loss under decreasing the angle from the 90° open setting takes only **0.02244092°**. The original commutator’s hyperbolic interval is **(87.69779488°, 92.30220512°)**. The four input widths give [89.97746315°, 89.97765500°] for the upper disk contact and [87.69288110°, 87.70271917°] for the commutator’s lower contact. These are input-range bounds. For the upper disk contact the cosine \(xy-\sqrt{(1-x^2)(1-y^2)}\) increases in both positive reflections. For the commutator the product \(p\) increases in both positive ratios. The bounds therefore occur at endpoint ratios.

At the exact setting \(c=1/1000\), the code checks with rational arithmetic that the disk has \(F<0\), the intersection is forward, and the four-stage transfer remains hyperbolic. It verifies the same disagreement at all 16 energy endpoints. This particular margin is also monotone on the input rectangle because \(x>cy\) and \(y>cx\) throughout it. Angle uncertainty has to be propagated separately.

**A simple instrument control.** Set \(a=9,b=4\), so \(x=4/5,y=3/5\) and \(p=1\). At \(\cos\theta=+3/5\) and \(-3/5\) the four-stage traces both equal \(-14/25\). The two-stage traces are \(+1/2\) and \(-9/2\), respectively. Thus the positive-cosine disk closes in the forward sector and the negative-cosine disk opens, with wide margins. Both are marginal at 90°. This control can establish which angle response an instrument actually implements before using the tighter Be–Rb comparison. It does not provide an atomic measurement.

**Reproduction.** Run `python3 angle_audit.py /path/to/data/element_thresholds_20261011.json.gz`. Without the archive argument, the script uses the same printed rational inputs. The program compares the disk margin with a direct intersection, separate circle centres/radii and matrix multiplications. It also checks the determinant-one factorization, rational controls, constructed interval endpoints and reversal of both clocks. The accompanying text file records the run against the archive. No external software dependencies.

**Exact algebra in Lean.** The standalone `ObliqueFaces.lean` compiles with Lean 4.34.1 and no Mathlib. The thirteen theorems certify the general cleared discriminant, tilt parity and right-angle coincidence, the rational (9,4) control, the archived Be–Rb central rational counterexample, a refutation of universal oblique equivalence, and the rational matrix determinant, product, factorization and commutator trace identities. Each declaration reports only `propext`, `Classical.choice` and `Quot.sound`. The type of these formal statements is rational arithmetic; the note supplies the real trigonometric interpretation and the applicability conditions. Use `lean ObliqueFaces.lean` to recreate `lean_audit.txt`.
