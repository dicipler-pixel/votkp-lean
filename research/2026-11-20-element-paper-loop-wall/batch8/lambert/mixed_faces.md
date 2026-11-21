# Two different peel faces at a right-angled corner

**DERIVED.** Claude's disk construction provides a way to combine two distinct intrinsic peel faces. The faces are assigned to the perpendicular axes of the element paper's comparison disk. This calculation tests a geometric closure in that construction. Assigning either coordinate to a material junction or calibrating a physical distance would require additional input.

## Where the two perpendiculars meet

Let the two forward ratios be \(a,b>1\). For one face with ratio \(z\), define \(h=\tfrac12\log z\), \(u=\tanh(h/2)\), and \(g(z)=\tanh h=(z-1)/(z+1)\). In the Poincaré disk, Claude's geodesic perpendicular to the horizontal axis has centre \(c=(1+u^2)/(2u)\), radius \(R\), and \(c^2-R^2=1\). Its equation expands to

\[
2cx=1+x^2+y^2.
\]

Use the coordinates \((X,Y)=2(x,y)/(1+x^2+y^2)\). On the open unit disk this is a bijection to the open unit disk, since the radial function \(2t/(1+t^2)\) increases strictly from 0 to 1 for \(0\le t<1\). The horizontal face's perpendicular now has constant \(X=1/c=2u/(1+u^2)=g(a)\). The vertical face gives \(Y=g(b)\). Therefore the prospective intersection has coordinates exactly \((g(a),g(b))\).

| Location of the prospective intersection | Classification |
|---|---|
| \(g(a)^2+g(b)^2<1\) | The perpendiculars meet at an interior point, and the loop closes. |
| \(g(a)^2+g(b)^2=1\) | They have one common ideal endpoint. |
| \(g(a)^2+g(b)^2>1\) | They have no intersection in the closed disk, and the loop is open. |

The same comparison follows from \(\sinh^2h=g^2/(1-g^2)\). Clearing the positive denominators of the product leaves \(g(a)^2g(b)^2-(1-g(a)^2)(1-g(b)^2)=g(a)^2+g(b)^2-1\). For equal faces this is the paper's \(2g^2-1\). These equations also specify the one-face-zero case \(z=1\) by continuity, where the circle-centre formula becomes singular.

**DERIVED.** Fixing \(a>1\) gives an analytic threshold for its partner. Set \(t=\sqrt a\). Then \(g(a)=(t^2-1)/(t^2+1)\), so at tangency \(g(b)=\sqrt{1-g(a)^2}=2t/(t^2+1)\). Inverting the reflection gives

\[
 b_*(a)=\left(\frac{\sqrt a+1}{\sqrt a-1}\right)^2.
\]

In particular, \(a=9, b=4\) gives \(g(a)=4/5, g(b)=3/5\), an exact unequal-face tangency. The strict reading “open at equality” fails here. For the archive's carbon face the critical partner is 5.59115620. The original script used shortened carbon energies and printed 5.591162. Nitrogen is on the same side in both evaluations. The construction takes place on the paper’s auxiliary disk and makes no claim about a spacetime metric.

## Tests and observations

**Rejection tests.** The exact rule would fail this comparison if its strict classification disagreed with the original disk-circle code away from tangency. The threshold formula would fail if a rational Pythagorean pair gave nonzero margin, or a positive and a negative perturbation went to the same side. A quoted uncertainty would defeat a definite historical mixed call if either endpoint crossed the wall.

**DERIVED.** The runnable check exhausts all unordered pairs with replacement within each named opening in Kr through Zr, treating the neutral affinity step as a separate family. These are comparisons of two internal clocks. The rubidium and strontium row uses the Kr-core opening of each atom; an equal-clock external junction must be specified separately. Each of the three lighter core families gives 15 closing pairs. Of the ten Kr-core comparisons, only rubidium and rubidium opens. Each of the ten bound-anion pairs opens. Krypton has no bound ground anion. The exact and disk classifications agree on all 65 pairs. The script also checks 19 exact tangencies and their 38 strict perturbations. An ideal point does not enter the strict-open or the finite-closing count.

**RECOGNISED.** Across the five previously observed inward crossings, pairing the last outside face with the first inside face produces two different outcomes. carbon and nitrogen and sodium and magnesium remain open. potassium and calcium, rubidium and strontium and caesium and barium close. All five retain their calls at the quoted lower and upper endpoints of the archive energies. The classification in the most finely balanced case, carbon and nitrogen, has the signed power margin +0.00309334. This is a comparison of these five pairs. Evidence for a change in atomic or material behaviour at this bound would have to come from a separate observable.

The first element and the next element in each row open the **same core**, starting with one electron above it. If the core contains \(N\) electrons, the charge before the first removal is \(q=Z-N-1\) for each element. Their absolute charge indices differ by one. Every first element also gives a strict-open self-pair and every second element a finite-closing self-pair. For an energy ratio \(v/u\) the quoted endpoint range is \([(v-\delta v)/(u+\delta u),(v+\delta v)/(u-\delta u)]\). Both squared reflections increase with each forward ratio, so simultaneous low and simultaneous high enclose the margin. This interval propagates the quoted uncertainties without assigning them a joint probability.

| Core | Last outside / next inside | Mixed margin | Margin interval using reported input uncertainties | Result |
|---|---|---:|---|---|
| He | carbon and nitrogen | +0.00309334 | [+0.00309076, +0.00309591] | open |
| Ne | sodium and magnesium | +0.11427307 | [+0.11426868, +0.11427745] | open |
| Ar | potassium and calcium | -0.03782202 | [-0.03782596, -0.03781808] | closes |
| Kr | rubidium and strontium | -0.11143697 | [-0.11143961, -0.11143434] | closes |
| Xe | caesium and barium | -0.17524802 | [-0.17527621, -0.17521982] | closes |

## Reproduction

Run from this directory with the checkout root as the first argument:

```sh
python3 mixed_faces.py /path/to/votkp-lean --csv mixed_faces.csv
```

The program checks the pinned archive's SHA-256 before computing with exact rational energies. It loads the original disk implementation and compares its floating-point result for each strict pair. The CSV records both exact ratios and the exact signed margin \(g(a)^2+g(b)^2-1\). The text output gives the earlier brackets and their endpoint controls.

- [Original disk-circle implementation at c35b18b](https://github.com/dicipler-pixel/votkp-lean/blob/c35b18b1c577bde90eacd3ef7cfa1bb2bb93024f/research/2026-11-20-element-paper-loop-wall/checks/lambert_jump_check_v1.py)
- [NIST-derived pinned thresholds](https://github.com/dicipler-pixel/votkp-lean/blob/cae5f49/data/element_thresholds_20261011.json.gz)
- [Ning & Lu, 2022, evaluated electron affinities](https://doi.org/10.1063/5.0080243)
- [Zhang et al., 2023, Y affinity](https://pubmed.ncbi.nlm.nih.gov/36859075/)

The independent Lean file proves the rational power comparison, its ideal case, and the unequal-face control. Its scope is rational algebra. The coordinate argument above supplies the connection to Claude's disk geometry.

Checked on the repository’s pinned Lean 4.34.1. All nine declarations report only `propext`, `Classical.choice` and `Quot.sound`. The exact axiom listing is in [mixed_faces_lean_output.txt](mixed_faces_lean_output.txt). Run `lean MixedFaces.lean` to repeat the check.

## How much does the right angle matter?

**DERIVED, auxiliary-disk control.** Keep carbon’s and nitrogen’s measured peel ratios fixed and rotate the second *axis through the disk centre* by a chosen angle θ relative to the first. The original construction prescribes 90°. This deliberately perturbs that assumption. θ is neither an angle between crystal bonds nor a measured orientation of an ion.

In the disk coordinates above, write g and h for the two reflections. The face equations become X = g and X cos θ + Y sin θ = h. For 0 < θ < 180°, the intersection has squared radius g² + (h − g cos θ)² / sin² θ. Its signed difference from one has the sign of

    F(c) = c² − 2ghc + g² + h² − 1,     c = cos θ.

The two ideal contacts therefore have cosines gh ± √((1−g²)(1−h²)). Between the two contact angles the **complete supporting geodesics** intersect inside the disk. For closure in the sector bounded by the two forward axes there is an additional orientation condition. At either contact the intersection is ideal. Beyond either contact, within the stated angle domain, the loop opens. This reduces exactly to the original signed margin at 90°.

At the archive central values, carbon with nitrogen has contacts at **1.51888748° and 89.82270223°**. At 89.8° the loop closes. At 90° it opens. Thus a rotation of about **0.17730°** from orthogonality reaches the nearer contact. Sodium with magnesium takes about 6.67065° in the same direction. This quantifies what “barely” means for one specified perturbation of the mathematical construction. The original orthogonal classification is stable to the quoted energy uncertainties. No angular measurement enters that result.

[Five archived opening pairs](angle_control.csv) · [Reproducible angle and ideal-contact checks](angle_control.py)

For an oriented loop, write the intersection vector as α times the first unit axis plus β times the second. Then α=(g−h cos θ)/sin² θ and β=(h−g cos θ)/sin² θ. Both must be positive for a nondegenerate loop in the forward sector. For carbon with nitrogen this requires θ>13.11528523°. A 2° test gives an interior intersection of the complete geodesics on the wrong side of the forward sector. Thus the oriented, finite carbon-with-nitrogen loop closes for 13.11528523…° < θ < 89.82270223…°. The near-parallel contact previously listed describes the complete supporting geodesics. The 89.8° and 90° conclusions retain their original sectors and signs.
