# Tree, Ball and Light — mixer v2 and loop checks (12 November 2026)

- `Tree_Ball_Light_Mixer_v2_20261112.html` — the mixer. One feed: the tree's four-step loop W(z).
- `feed_loop_01/02/03.py` and `.out` — the checks, kill lines in each header.
- `feed_math.js`, `feed_math_test.js` — the page's own mathematics, tested against the Python.
- `build_mixer_v2.py` — builds v2 from the 11 November page; `shot_v2.py` — runtime test.

Checked (exact to 1e-11 or better): Gamma = 1 - 2c; loop trace 2 - 4 (R/T)^2 with R = Gamma^2; inside the wall
W = S U S^-1; Petermann factor K = 1/(1 - 2 Gamma^2); centre of turn rho^2 = (1-s)/(1+s), s = sqrt(1 - 2 Gamma^2);
rho^2 = 1/2 exactly at z = 5; one Jordan block at z = 3 + 2 sqrt 2; loop-fed light c = [1 + sin(n theta) sin(phi)]/2;
arm-k light sin^2(phi) = 2 Gamma^2.

Open: run rate past the wall (missed its 1e-6 line at early kicks); count of distinguishable directions on the
kick circle; P = 2 Gamma^2 as physical light pressure in the layers (reading, untested).
