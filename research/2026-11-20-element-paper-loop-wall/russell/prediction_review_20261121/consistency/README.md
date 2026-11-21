# The unique additive/product mixed-face threshold

Let x and y be squared face reflections in (0,1) and let t be the squared reflection at a common forward equal-face boundary. Compare two specific continuations of that boundary. The additive margin is A=x+y−2t. Comparing the product of the odds x/(1−x), y/(1−y) with the square of the cutoff odds gives the cleared product margin P=xy(1−t)²−t²(1−x)(1−y). All cleared denominators are positive. Either margin distinguishes three cases by its sign.

**Exact theorem.** For rational 0<t<1, these three labels agree for every x,y in the rational open unit square if and only if t=1/2. At half, 4P=A. For necessity take x=t² and y=2t−t²; both inputs lie strictly inside the unit interval and A vanishes. The opposing residual is P=t²(1−t)²(2t−1). Universal three-class agreement therefore forces t=1/2. In Beasley’s positive forward-ratio coordinate, this is precisely z=3+2√2. It selects a unique threshold **if agreement of the two stated extensions is required**. The theorem says nothing about a different extension or an experimentally measured threshold.

**Stricter falsifier.** At the same x=t², the additive boundary in y is yA=2t−t² and the product boundary is yP=(1+t)/2. Use their midpoint. Then P=−2t²(1−t) A and 4A=(1−t)(1−2t), so the signs are strictly opposite at each t≠1/2. This removes reliance on an experiment hitting an exact tie. The actual Lean theorem is over rational squared reflections. Its polynomial proof with positive factors applies equally over the reals. For rational programmable forward ratios, any strict example is approachable: rational reflection amplitudes are dense in (0,1), squaring is continuous there, and the inverse ratio is (1+g)/(1−g). These extensions in prose were not formally checked in this file.

## Two settings that identify three candidate rules

The scored models are VOTKP at t=1/2, the rival shifted-additive rule, and the rival shifted-product rule. The shifted t range [0.50051,0.50054] encloses the six empirical calibration variants checked independently. Coordinate errors below specify admissible inputs of a programmable analogue. These are design tolerances, not instrument validations.

| Requested forward ratios | VOTKP | Shifted additive | Shifted product |
|---|---|---|---|
| (35/6, 35/6), with each in [5.832,5.835] | open | closed | closed |
| (3, 13.99), with respective independent errors ±0.0001 | open | closed | open |

The Lean theorem rationalThreeWayControl proves the second row for its nominal rational ratios and every t in the stated interval. The Python script checks both rows with independent input perturbations using exact fractions. Corner sufficiency follows because both margins increase with x,y throughout (0,1), while each rival margin decreases with t. The fixed signs survive every listed input box. A material connection requires an independently observed readout and separate evidence for the mapping.

## Reproduction

Run LEAN=/absolute/path/to/lean ./check.sh in a directory containing the files, or ./check.sh on a configured Lean PATH. Running python control_boxes.py reproduces the two interval controls. The toolchain is Lean 4.34.1 (5045d0056413266e57c625dcd7c365b10e377c52), core only. Eleven theorems were axiom-audited; each prints exactly propext, Classical.choice, Quot.sound. The theorem wrongThird proves the universal agreement claim false at t=1/3. The separate deliberately failing source checks the incorrect three-way equivalence on x=1/9, y=11/18, at t=1/3. Its expected rejection is preserved in full_run.txt.
