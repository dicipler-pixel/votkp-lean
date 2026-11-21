# What the 3,637 original inputs can discriminate

Independent check for Jeromie Beasley, 21 November 2026. The work here is a deterministic mathematical and input-sensitivity audit. No physical instrument or independent atomic outcome was observed.

## Inputs and reproducibility

The script matches all 3,655 positive removal thresholds in the historical CSV directly to the pinned October gzip, SHA-256 `75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c`. The 3,637 positive-to-positive rung ratios are rebuilt from those values and the adopted electron affinities. Of those rungs, 3,614 have both energy widths. Exact fractions, the reported underlying widths, and the unrevised historical pin are used. Widthless entries are fixed at their adopted values for the stated sensitivity checks. The resulting boxes carry no probability interpretation.

The original ZIP `Russell_Peel_Wall_Prediction_Record.zip` contains `H_to_At_thresholds.csv` (SHA-256 `9f7b21e9eba6f76d0cbfa4ffcae65eeac7bf43cd6289bf3205432799ba8c3803`). The archive is in the repo as `data/element_thresholds_20261011.json.gz`. Run the scripts from this directory, supplying paths to those two inputs. The first needs Python 3; the second uses mpmath 1.3.0 for outward-rounded interval differentiation and a mean-value bound on each subdivision.

```sh
python check_rivals.py /path/to/Russell_Peel_Wall_Prediction_Record.zip /path/to/element_thresholds_20261011.json.gz .
python si_ag_dependency.py /path/to/Russell_Peel_Wall_Prediction_Record.zip /path/to/element_thresholds_20261011.json.gz .
```

## An explicit family of competing rules

Let $w=3+2\sqrt2$, $g(z)=(z-1)/(z+1)$ and $h(z)=\log(z)/2$. All tests below concern forward $z>1$. The closed/open diagonal labels in this data came from the original rule itself. A competitor agreeing with them reproduces those recorded classes. It has yet to explain an independent experimental class label.

The greatest inside value $L=5.807902059840\ldots$ is silver's anion rung; the least outside $H=5.866538776091\ldots$ is silicon's. Both are the unique endpoints throughout the available input rectangles. Six choices center the separating interval: arithmetic, geometric, and harmonic means of $L,H$; the arithmetic midpoint in $g$ and in $g^2$ converted back to $z$; and the geometric mean in $\sinh h$ converted back to $z$. Each is a raw/coordinate-based alternative, not an atomic mechanism. Allowing for endpoint uncertainties, their collective range is 5.837006362245 to 5.837286797096.

For each fitted midpoint $c$ evaluate four alternative mixed-face functions $F(a,b;c)$, where positive means open:

1. **Quadrature.** $g(a)^2+g(b)^2-2g(c)^2$.
2. **Product.** $\sinh h(a)\sinh h(b)-\sinh^2 h(c)$.
3. **Log-clock gain.** $g(a^t)^2+g(b^t)^2-1$ with $t=\log(w)/\log(c)$.
4. **Angle sum.** $\arcsin g(a)+\arcsin g(b)-2\arcsin g(c)$.

All four give the original mixed decision *everywhere* when $c=w$, and give diagonal cutoff $c$ when shifted. For the angle rule this follows since both angles are in the first quadrant and $\sin^2 A+\sin^2 B>1$ iff $A+B>\pi/2$. The product identity follows by clearing the positive denominators in $\sinh^2h=g^2/(1-g^2)$. These four rivals are different operational continuations of one proposed geometric perturbation, not independent data replications.

| Pair, evaluated on the same inputs | Verdict of the original law | Box-stable outcomes of the six by four declared rivals |
|---|---|---|
| Be $k=2$ and Rb $k=35$, two He-core openings | Open, $S=1.000379958706$ | **24 closed** |
| Si $k=0$ and Ag $k=0$, two anion rungs | Open, $S=1.001053642566$ | **11 closed, 11 open, 2 exactly ideal** |

For Be/Rb the input scores and fitted cutoffs can be ranged independently. The Si/Ag pair sets the fitted cutoffs itself. Derivatives on 64 two-variable sub-boxes bound the simultaneously varied scores. Treating fit inputs and pair inputs as independent there makes 23 marginal score enclosures straddle zero. The two exact ties are the mean squared reflection used with quadrature and the geometric mean of $\sinh h$ used with the product rule. Neither supplies a new empirical tangency. All 48 rival margins and the dependency-aware 24-case Si/Ag recheck are supplied in the CSV files.

## The Be/Rb result also has a precise failure mode

Use the same arithmetic $z$ midpoint $c$ and replace the root-mean-square reflection with the generalized $p$-mean of $g(a),g(b)$. Every $p$ gives exactly the same diagonal cutoff. At Be/Rb the rival changes from closed to open at $p=2.046143227541\ldots$. With $p=2.05$ the rival agrees with the original Beasley call. A direct perturbation of quadrature shows the scale of the effect. The expression
$$
g(a)^2+g(b)^2+\lambda\,[g(a)-g(b)]^2-2g(c)^2
$$
has an unchanged diagonal for every $\lambda$. The Be/Rb call changes at $\lambda=0.022947258331\ldots$, and is open at the simple exact value $\lambda=1/40$. These perturbations vary the off-diagonal coupling. They test a different degree of freedom from placement of the single-face wall.

## No-go for every historical pairing at once

Even opening *all* historical pair outputs cannot identify the diagonal threshold in the absence of constraints on the shape of the mixed law. Here is an explicit rival for any candidate cutoff $c$ in the open data gap $(L,H)$. On reflection magnitude define a continuous, strictly increasing map $f$ equal to the identity outside $(g(L),g(H))$. Interpolate linearly inside, through
$$
(g(L),g(L)),\qquad (g(c),g(w)),\qquad (g(H),g(H)).
$$
This map fixes every single sampled reflection. Define the symmetric, strictly increasing, idempotent mean
$$
M_f(x,y)=f^{-1}\left(\sqrt{[f(x)^2+f(y)^2]/2}\right).
$$
Use $M_f(x,y)>g(c)$ as the rival wall test. On the diagonal it is $x>g(c)$. For every two sampled inputs, the rival comparison reduces exactly to $x^2+y^2>1$, since $f(g(c))=g(w)=1/\sqrt2$. The rival agrees for all possible pairings from the archive simultaneously, including cross-family pairings and multiplicities. The same construction can use the smaller gap between the highest known inside upper bound and lowest known outside lower bound to fix all points of all complete rectangles. For widthless rungs that extension covers the adopted central inputs.

This counterexample concerns *identification from finite sampled inputs*. The native reflection $g$ itself is retained in the construction; $f$ specifies an alternative way of combining the two observed numbers. Independent physics might rule that combining rule out. Such a physics constraint or genuinely new face inputs do work that more pairings of the same old faces cannot.

## A control immune to off-diagonal tuning

Set both forward faces to $35/6$. This ratio is the smallest-denominator positive rational lying between $w$ and every one of the six fitted midpoint rivals, even at their reported calibration limits. The exact values are
$$
g=29/41,\quad 2g^2=1682/1681>1,\quad \sinh^2 h=841/840,\quad
\operatorname{tr}W=2-4(841/840)^2=-354481/176400=-2.009529478458\ldots .
$$
Every rival with diagonal cutoff at one of those six fitted values must call the pair closed regardless of its mixed extension. The native geometry calls it open. If two *independently measured* gains both land in $[5.832,5.835]$, all coordinatewise-monotone extensions of the six rival cutoffs remain closed, and the native construction remains open. This tolerates unequal actual gains within that box. If a gain is unknown or if the outcome is reconstructed from the already-assumed matrix formula, the intended experimental discrimination has not occurred. A free cutoff as close to $w$ as desired cannot be ruled out by one such setting. This is an engineered discrimination in the gap, not a bound-anion or ionization measurement.

The pair of settings $35/6$ on both faces and the asymmetric archived Be/Rb ratio tests two distinct assumptions. At the diagonal test an independent observed loop return can score cutoff placement without a choice of mixed continuation. At the Be/Rb test it can score the specified off-diagonal rule, with the qualifications above. A third, exactly marginal, unequal pair such as $(9,4)$ gives a useful differential control at the specified orientation. A putative atomic or material response still needs observables within that physical system.

Files: `check_rivals.py`, `si_ag_dependency.py`, `results.txt`, `shared_result.txt`, `rival_boxes.csv`, `si_ag_shared_boxes.csv`.

## Formal check

`FiniteWallGap.lean` builds in core Lean 4.34.1, with no Mathlib import. The main declaration, `Beasley.WallGap.alternative_on_gap`, constructs a strictly increasing piecewise-affine rival on rational squared reflections. For every rational $L<t<H$ and $L<1/2<H$, its diagonal decision is exactly $x>t$. On **every** pair of powers outside the open gap $(L,H)$ its decision equals $x+y>1$. This includes any observed dataset satisfying the gap premise. The squared-power coordinate makes all four breakpoints rational, so the source proof has no floating-point or square-root oracle. The Python reconstruction verifies that the present ledger satisfies the gap premise; the Lean theorem itself is general. The piecewise formula is glued at its interval endpoints, and the proof establishes strict monotonicity there and inside each segment.

The same source proves exact encoded endpoint admissibility, the exact Be/Rb mixed counterexample at $\lambda=1/40$, the $35/6$ numerical certificate including the return trace, the upper-box implication under monotonicity, and rejection of the reversed trace sign. I compiled the standalone file with `lean -j1 FiniteWallGap.lean`. The seven audited declarations each report only `propext`, `Classical.choice`, and `Quot.sound` in `lean_output.txt`.
