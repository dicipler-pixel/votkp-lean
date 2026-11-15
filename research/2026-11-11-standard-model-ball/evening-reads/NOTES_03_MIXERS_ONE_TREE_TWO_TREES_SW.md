# NOTES 03 — mixers One Tree/One Ball, Two Trees/One Scale, One Tree/One Ball + Seiberg-Witten; BallJoins.lean; SeibergWitten.lean + harmonic-chains folder

Reader: Sonnet 5.5, 11 Nov 2026. Everything below is what the files print or compute. Items marked (re-computed) were re-run by me in python from the code's own rules (python3 -I, prime sieve plus the same arithmetic); they are not printed in the files. Abbreviations: OTOB = One_Tree__One_Ball.txt; TTOS = Two_Trees__One_Scale.txt; OTOB-SW = One_Tree_One_Ball_Seiberg_Witten__4_.txt; BJ = BallJoins.lean; SW.lean = SeibergWitten.lean.

## 1. COVERAGE

| file | size | read |
|---|---|---|
| /home/claude/in/text/One_Tree__One_Ball.txt | 17,234 B, 60 lines (longest 2,119 chars) | all, in 400-char folds, nothing cut |
| /home/claude/in/text/Two_Trees__One_Scale.txt | 25,510 B, 95 lines | all |
| /home/claude/in/text/One_Tree_One_Ball_Seiberg_Witten__4_.txt | 30,182 B, 303 lines | all; also diffed line by line against OTOB (see 2.1) |
| /mnt/user-data/uploads/1576169b-BallJoins.lean | 5,741 B | all |
| .../original_uploads/SeibergWitten.lean | 10,551 B | all (byte-identical to the copy inside the zip, checked with cmp) |
| .../original_uploads/Seiberg_Witten_Harmonic_Chains_Lean (1).zip | 5 files | unzipped to /tmp, all 5 read: README.md 7,313 B, SeibergWitten.lean, check_chains.py 3,191 B, chain-results.txt 1,364 B, lean-audit.txt 3,032 B |
| .../research/Seiberg_Witten_Harmonic_Chains_Lean (1)/ | 4 files (README.md, check_chains.py, chain-results.txt, lean-audit.txt) | all; identical to the zip contents; no SeibergWitten.lean in that folder (it is in original_uploads and in the zip) |

No other folder under original_uploads or research starts with "Seiberg_Witten_Harmonic_Chains_Lean" (only that zip and that research folder). The 3D library (three.js) is removed from the reading copies; all page text and code are present. No code from the files was executed; I re-implemented the arithmetic. Lean was not run; theorem statements are read from source, and the axiom list is what the folder's own lean-audit.txt reports.

## 2. OBJECTS AND DEFINITIONS

### 2.1 Relation of the three pages
- OTOB-SW = OTOB plus two extra scenes (swCharges, swCusp) and UI additions (zoom buttons, pinch, follow-bead, a select box). Scenes `ride` and `whole` are the same text and code in both. The script header comment in OTOB-SW still reads "SCRIPT: one_tree_one_ball_mixer_v1" (same as OTOB); title still "One Tree, One Ball".
- TTOS is a separate page with different geometry (flat layout, height axis y = ln n), see 2.3.
- Bylines: OTOB/OTOB-SW "The twin-prime chain as a path in the tree of peel steps / Jeromie Beasley · prime chain with Elizabeth Johnson · 3D mixer". TTOS: "VOTKP · Two Trees in One Ball · the twin-prime chain with Elizabeth Johnson / Jeromie Beasley · 3D mixer". TTOS chain label: "Twin-prime chain (E. Johnson and J. Beasley)".

### 2.2 OTOB / OTOB-SW shared model (code "one_tree_one_ball_mixer_v1")
- Ball model: points on the hyperboloid v = (v0,v1,v2,v3), origin O = (1,0,0,0). Boost along axis ax (0,1,2 = i,j,k acting on coordinates 1,2,3), bv(v,ax,r): v0' = cosh r v0 + sinh r v_{ax+1}; v_{ax+1}' = sinh r v0 + cosh r v_{ax+1}. Display map W(v) = RB/(1+v0) * (v1, v3, -v2), RB = 3.4 (Poincare ball).
- Geodesic between hyperboloid points p,q (geoS): ip = -p0q0+p1q1+p2q2+p3q3, d = acosh(max(1,-ip)), point(t) = [sinh((1-t)d) p + sinh(t d) q]/sinh d.
- Peel ratio z (slider P.z), rapidity rap = ln z. Each peel step is a boost by ln z (one edge has length ln z; Gamma = (z-1)/(z+1) in the eq lines).
- Level shells ("Garrett levels"): spheres at ball radius RB*Gamma_L, Gamma_L = (z^L-1)/(z^L+1), L = 1,2,3, labelled "level L: L·ln z". Outer wireframe sphere radius RB (the ball's rim).
- Garrett tree (buildTree): letters k = 0..5; axis = k>>1 (i,j,k), sign + if k even, - if odd, rapidity (+/-)ln z. Node for word w: v=O; for i from last letter to first: v = bv(v, axis(w[i]), sign*rap). Six letters at the root; a letter k is skipped if (k xor 1) equals the previous letter (no step back), so 5 onward. Depth D = 4: edges 6 + 30 + 150 + 750 = 936 (re-computed), each 5 geodesic segments. Edge colour = arm colour (i coral 0xff8d7c, j cyan 0x63d3ff, k gold 0xf2c14e), brightness factor 0.62^depth.
- Twin chain TW: all a from 11 up to N = 400000 with a and a+2 prime (sieve). Starts at 11, not 5. 3,802 pairs (re-computed). First 27: 11, 17, 29, 41, 59, 71, 101, 107, 137, 149, 179, 191, 197, 227, 239, 269, 281, 311, 347, 419, 431, 461, 521, 569, 599, 617, 641; last 399911. End digits (re-computed): 1: 1282, 7: 1269, 9: 1251.
- Arm of a twin start: axOf(a) = {1:0, 7:1, 9:2}[a mod 10] (end digit 1 -> i, 7 -> j, 9 -> k). BJ J6 proves only these three digits occur past 5.
- Connector colour: kapOf(j) = ((TW[j+1] - TW[j] - 2) mod 10)/2, index into EJ = [green 0x3fbf80, black(grey) 0x8e949c, red 0xe8553f, blue 0x4d90ea, white 0xf2eee2]. So connector = start gap minus 2; 0 green, 2 black, 4 red, 6 blue, 8 white (mod 10). Counts over the 3,801 links (re-computed): white 1099, green 982, blue 814, red 495, black 411. The pages call these "Elizabeth Johnson's five connector colours" (TTOS) / "connector classes" (OTOB).
- Ride path (drawPath(k,ax,fr)): future points fut[m] (m = 1..5) = bv applied for i = m down to 1 with axis axOf(TW[k+i]), rapidity +rap, starting at O; past points (up to 5) use i = m-1 down to 0 with axOf(TW[k-i]) and -rap. So the chain step from pair k to k+1 is a boost by ln z (the same z for every step, default 5) along the arm of the NEXT start's end digit. The whole tree is slid by a boost of -fr*rap along that arm (moveTree), so the view stays on the current ball; fr = smoothstep of (t-0.25)/0.75; step time 1.7 s; k runs 6 .. TW.length-NF-3 (= 3794, re-computed) then wraps to 6.
- Whole chain (CH, n = 2400 pairs): G = identity 4x4; for each j: ball position = first column of G; then G <- G * boost(axis = axOf(TW[j+1]), r = ln(TW[j+1]/TW[j])) (right multiplication, applied on every row). Each ring is a boost of its OWN size, ratio a'/a, along the arm of its end digit. Recorded per ball: d_j = acosh(G[0][0]) (distance from the centre ball), len_j = ln(TW[j]/TW[0]) = ln(a/11).
- Tree drawn in scene "whole" is always ratio 5 (buildTree(5)), opacity .3.

### 2.3 TTOS model
- One height axis: y = HS*ln(n), HS = 0.85 world units per unit ln. YMAX = yOf(5^5) = 0.85*ln 3125 (ln 3125 = 8.0472, re-computed). Axis ticks n = 2, 3, 5, 7, 11, 13, 101, 1009 labelled "ln n"; vacuum point at height 0 labelled "vacuum point, ratio 1". Axis text: "height = ln of the number = distance from the vacuum point".
- Garrett's tree (left, x = -3.6): FLAT layout, six directions at angles HEX = [0, pi, 2pi/3, 5pi/3, 4pi/3, pi/3] for +i,-i,+j,-j,+k,-k (three axes 120 degrees apart, both ends), horizontal spacing 1.7*0.42^depth, each step up by HS*ln z. Same no-step-back rule. Depth 4. Balls with depth <= 2 get a star turned by the word's frame. Level lines at d*HS*ln z, labelled "level d · ln z^d". Page text: "The three axes are drawn flat, 120° apart, to lay the tree out; the star on each ball shows the true three-dimensional frame."
- Frame of a word: M = product (in word order, right-multiplied) of sl2(z, axis, sign), sl2 = [(z+1) + sign (z-1) sigma_u]/(2 sqrt z), sigma_u = sigma_x (axis 0: [[p,q],[q,p]]), sigma_y (axis 1: [[p,-iq],[iq,p]]), sigma_z (axis 2: diag(p+q, p-q)), p = (z+1)/(2 sqrt z), q = sign (z-1)/(2 sqrt z). Polar split M = H U (P = M M^dagger, H = (P + I)/sqrt(tr P + 2), U = H^-1 M). Rotation R_ab = tr(sigma_a U sigma_b U^dagger)/2; star orientation from R with world map i = x, j = -z, k = y. Turn angle = 2 acos(|tr U|/2).
- Twin chain (right, x = +3.6): TW = twin starts from 5 up to 5^5 = 3125: 82 pairs (re-computed); first 12 = 5, 11, 17, 29, 41, 59, 71, 101, 107, 137, 149, 179; last 3 = 2969, 2999, 3119. Position of pair a: angle th = 12 degrees * a ("one turn per 30"), height y = HS ln a, radius r = 0.35 + 1.35*hw(log10 a)/117.5, hw = linear interpolation in log10 a of DATA.halfw = [[1, 8.5], [2, 18.0], [3, 27.4], [4, 45.2], [5, 65.8], [6, 89.6], [7, 117.5]] (clamped below 1 and above 7). The page calls this "the measured ring width" / "colour cone from the film"; no script for how the half-widths were measured is in the file (hard-coded).
- Shaft: sh = -1 for a = 5 (the "waist", label "waist (3,5,7)"), else {1:0, 7:1, 9:2}[a mod 10]. Frame: w counts non-waist steps; when w mod 12 = 0, M is reset to identity; then M <- M * sl2(5, sh, +1). Frame U = polar part of M; the ball star is turned by U; "frame turn (last 12 rings)" = turn angle of U. So the chain frames use ratio 5 for every twin step, not the true ratio a'/a.
- Links: tube between consecutive ball positions, colour EJ[kap], kap = ((a' - a - 2) mod 10)/2 (same rule as OTOB); c.g = a'-a-2 ("connector γ to next").
- Gold guide lines at the slots 11, 17, 29 (angle 12*q degrees) along the cone. Gold level rings at d*HS*ln 5, d = 1..5, through both trees.
- Re-computed turn angles for ratio 5 (my port of the frame code), indices 0-14: 0.0, 0.0, 47.92, 75.18, 47.92, 75.84, 53.17, 54.81, 71.61, 84.37, 118.02, 130.26, 127.18, 0.0, 0.0. Index 0 is the waist; index 1 is the first step of a window (U = I); index 13 is a new window; index 14 repeats the same axis (197, 227 both end in 7). Max over the 82 pairs 141.38 deg, mean 62.00 deg. 2 atan(4/9) = 47.925 deg equals the turn of one perpendicular pair at z = 5 (47.92 at index 2), matching the "Thomas turn, tan(θ/2) = Γ² = 4/9" line.

### 2.4 OTOB-SW Seiberg-Witten objects (code)
- Exact integer (BigInt) 2x2 matrices [a,b,c,d]. Charge q = (m,e). Step matrix M(q) = [1+2em, 2e²; -2m², 1-2me] (swMatrix). Pairing <q,r> = m r_e - e r_m (swPair). "Adjacent trace" readout = 2 - 4 pair². Ordered products P_0 = I, P_{k+1} = P_k M(q_k). Recentering: nodes drawn are P_k^{-1} P_j acting on i (Mobius action), so the current vertex P_k sits at i.
- Point of matrix [a,b,c,d]: M·i = ((ac+bd) + i)/(c²+d²): x = (ac+bd)/(c²+d²), y = 1/(c²+d²); to hyperboloid by swH(x,y) = [(x²+y²+1)/(2y), x/y, (x²+y²-1)/(2y), 0], i.e. the H² slice v3 = 0 of the same ball (drawn in the horizontal disc, plus a rim circle of radius RB). Edge geometry: distance d(i, M·i) from cosh d = ||M||_F²/2 (Frobenius), geodesic interpolated between orbit points.
- Families (swFamilies), 7 charges unless stated:
  - wheel "Elizabeth’s wheel → charges": first 27 twin starts, charge from end digit: 1 -> (1,0), 7 -> (1,-1), 9 -> (0,1). Code comment: "Elizabeth's wheel supplies the digit transition. The charge labels are a separate choice, fixed here to close 1 → 7 → 9 projectively." UI text: "Wheel charge labels: 1 ↦ (1,0), 7 ↦ (1,−1), 9 ↦ (0,1)."
  - straight "Straight dyons": (1,-n), n = 0..6.
  - fibonacci: swCF([1,1,1,1,1]); pell: swCF([2,2,2,2,2]); mixed: swCF([1,3,2,5,1]); swCF starts at (1,0),(1,-1) and appends (second-last) + k (last).
  - skip "Skip a dyon · control": (1,-2n), n = 0..6.
  - twins "Literal twin-pair lift · control": (p, p+2) for p = 5, 11, 17, 29, 41 (5 charges).
- Wheel step data (swWheelStep(a,b)): d = a mod 10, next = b mod 10, g = b - a (the START gap), delta = g mod 10, carry = (g - (next - d))/10 ("tens crossed"), palette = delta/2 -> EJN. Readouts: "start gap / full span" = g / g+2; "gap class / tens crossed" = delta · colour / carry.
- Edge colour rule (charge scene): first edge (j=0) cyan 0x71e2ff; wheel edges EJ[palette]; other families gold 0xffcd68 if pairing = +/-1 else coral 0xf28474; the current step is drawn as an opaque tube, others at opacity .58.
- Wheel readout "last three matrices": product M(k-2) M(k-1) M(k); " · closes in the ball" appended when it is scalar (b = c = 0 and a = d).
- Cusp scene: three local frames, each a horocycle s = i + 2·sign·t: plus "Monopole at u = +1" (sign +1, lift "T² in the local frame", coord s = −1/τ), minus "Dyon at u = −1" (sign +1, "T² in the local frame", s = 1/(1−τ)), infinity "Weak coupling at u = ∞" (sign −1, "−T⁻² in the paper’s loop convention", s = τ). Orbit drawn for t in [0,12] windings (13 beads, 181-point tube), bead position swH(s,1). Readouts at k completed windings (exactS = 2·sign·k): "coupling after k windings" = `exactS + i`; "reciprocal after k windings" = (exactS − i)/(exactS²+1); "next winding" = s ↦ s + 2 (finite frames) or s ↦ s − 2 (infinity); "orbit in the ball" = horocycle at Im(s) = 1.
- Animation times: whole 40 s; swCharges 19 s (wheel 54 s); swCusp 24 s; moving the scrub slider stops play in sw scenes.

### 2.5 BallJoins.lean
Header: "BallJoins.lean — the exact joints of the One Ball mixer. Jeromie Beasley. Lean 4.34.1 with Mathlib. No sorry." The only occurrence of the word sorry in the file is that header text (grep count 1). 11 theorems. Definition: gam(z) = (z-1)/(z+1) ("the Smith (peel) coordinate of a ratio"). Header lists joints J1-J8. Statements in 3.2.

## 3. RESULTS (with grade as the source gives it)

### 3.1 Scene by scene, mixers

**OTOB scene 1 "ride": "Ride the chain through the tree."** Grade line: "Exact frame (Lean); the chain is the primes".
- eq: "twin start ends in 1, 7, 9  →  arm i, j, k / one ring = one edge of the tree, length ln z / Γ = (z − 1)/(z + 1)".
- sub: "This is one object. The tree of peel steps fills the ball, and the twin-prime chain is a single path inside it: each twin pair is a ball of the tree, and the next pair is one edge away, along the arm of its end digit. The link is drawn in its connector colour."
- note: "The view always stands on the current pair. When the chain steps, the whole tree slides by that peel step, and what you see from the new ball is exactly the tree you saw from the last one: the connections are the same from ball to ball. Past pairs fall away toward the rim behind; the next five are ahead."
- lean: "Lean: BallJoins J6 (three end digits, three arms) · Two Trees v4 free5, free7 (no path ever returns) · peel_ladder (levels)".
- Control: slider "Peel ratio of the tree", 3..9 step 2 (z in {3,5,7,9}), default 5. Scrub: ride.k = 6 + floor(u*600).
- Readout rows: "this ball" a, a+2; "next ball"; "its end digit → arm" (digit → i/j/k); "link colour (connector C)" with C = next start − a − 2 and colour name; "step in the tree" = "one edge, length ln z"; "seen from this ball" = "the same tree as from every ball"; "shells" = "levels 1, 2, 3 around whichever ball you stand on".
- "no path ever returns" is attributed to Two Trees v4 free5/free7 (not in these files).

**OTOB scene 2 "whole": "The whole chain, at its own size."** Grade: "Computed from exact steps".
- eq: "each ring steps by its own ratio a′/a / path length = Σ ln(a′/a) = ln(a/11)".
- sub: "Here each ring is a peel step of its true size, the ratio of one twin start to the next, still along the arm of its end digit. The path length is then exactly ln a, the height scale, and the chain is drawn whole inside the same ball over the ratio-5 tree and its level shells."
- note: "Because the steps keep changing arm, the chain ends up closer to the centre than its path length; the readout gives the ratio. Colours are the connector classes."
- lean: "Lean: Two Trees v4 gam_mul (ratios multiply, lengths add) · BallJoins J1".
- Readout rows: "twin pairs drawn" n = max(2, floor(2 + u^1.6 (2400-2))); "latest pair" TW[n-1], +2; "path length = ln(a/11)" (4 dp); "distance from the centre ball" (4 dp); "distance / path length" (4 dp, "–" at length 0); "Garrett level reached" = distance/ln 5 (2 dp); "each step" = "ratio a′/a along the arm of its end digit".
- Values of these rows (re-computed; not printed in the file), index j (pair a): path length / distance / ratio / level: j=1 (17): 0.4353 / 0.4353 / 1.0000 / 0.27; j=2 (29): 0.9694 / 0.7016 / 0.7237 / 0.44; j=10 (179): 2.7895 / 1.6820 / 0.6030 / 1.05; j=100 (3929): 5.8782 / 3.5026 / 0.5959 / 2.18; j=500 (32561): 7.9930 / 4.7224 / 0.5908 / 2.93; j=1000 (79697): 8.8881 / 5.2397 / 0.5895 / 3.26; j=2000 (182129): 9.7146 / 5.7172 / 0.5885 / 3.55; j=2399 (228197): 9.9401 / 5.8473 / 0.5883 / 3.63. Ratio distance/length settles near 0.588.

**OTOB-SW scene 3 "swCharges": "Seiberg–Witten · charge chains".** Grade: "Exact matrices · Möbius orbit".
- eq: "Pₖ = M(q₀)⋯M(qₖ₋₁) / tr(M(q)M(r)) = 2 − 4⟨q,r⟩²".
- sub: "One node for each successive product acting on i. The view is recentered by the previous product as you ride."
- note: "For the original charge families, gold marks adjacent trace −2 and coral marks failures. Elizabeth’s wheel uses its own gap colors, keyed to the twin-start gap mod 10. The faint Garrett tree is a reference. These links follow the Möbius orbit on an H² slice of the same ball."
- lean: "Lean · twist_pair_trace · chain_pair_trace · paper_matrices".
- Readout rows: "chain" name; "step" k+1 / n; "charge q = (m, e)"; "step matrix M(q)"; "pairing with previous"; "adjacent trace"; "ordered product through this step"; "ordered product trace"; "view" = "P_k recentered at i"; wheel only: "twin pair", "digit → charge", "wheel transition" (a → b · d → next), "start gap / full span", "gap class / tens crossed", "last three digits", "last three matrices".
- Ordered-product traces after steps 1..n (re-computed; the readout "ordered product trace"): straight 2, -2, -6, 2, 10, -2, -14 (pairings all -1). fibonacci 2, -2, -18, -2, 34, 18, 34 (pairings -1,1,-1,1,-1,1). pell 2, -2, -38, -62, -502, -642, -4558. mixed 2, -2, -18, -98, -958, -15982, -74878. skip 2, -14, 34, -62, 98, -142, 194 (pairings all -2). twins 2, -574, 24194, -2176702, 149066498 (pairings -12, -12, -24, -24). Final values match chain-results.txt.
- Step matrices (re-computed): M(1,0) = [1,0;-2,1]; M(1,-1) = [-1,2;-2,3]; M(1,-2) = [-3,8;-2,5]; M(2,-1) = [-3,2;-8,5]; M(0,1) = [1,2;0,1]; M(5,7) = [71,98;-50,-69].
- Wheel family digit string of the first 27 starts (re-computed): 1 7 9 1 9 1 1 7 7 9 9 1 7 7 9 9 1 1 7 9 1 1 1 9 9 7 1. Product M·M·M over all 27 ordered digit triples from {1,7,9}: only the three cyclic rotations (1,7,9), (7,9,1), (9,1,7) give a scalar matrix, namely [-1,0;0,-1] (= -I, identity as a Möbius map); the other 24 do not (e.g. (1,1,1) -> [1,0;-6,1], (9,9,9) -> [1,6;0,1]). Among the 25 windows of the first 27 starts, 5 close: (11,17,29), (17,29,41), (179,191,197), (311,347,419), (347,419,431). Pairing of consecutive wheel charges: 1->7 gives -1, 7->9 gives +1, 9->1 gives -1; a repeated digit (1->1, 7->7, 9->9) gives pairing 0 and adjacent trace 2, not -2 (re-computed). The page's gold/coral rule applies only to non-wheel families.
- Wheel transition table (re-computed from the page's rule; start a -> b, digits, g = b-a, delta = g mod 10, colour name the page prints, carry): 11→17 (1→7) g6 δ6 blue c0; 17→29 (7→9) g12 δ2 black c1; 29→41 (9→1) g12 δ2 black c2; 41→59 (1→9) g18 δ8 white c1; 59→71 (9→1) g12 black c2; 71→101 (1→1) g30 δ0 green c3; 101→107 (1→7) g6 blue c0; 107→137 (7→7) g30 green c3; 137→149 (7→9) g12 black c1; 149→179 (9→9) g30 green c3; 179→191 (9→1) g12 black c2; 191→197 (1→7) g6 blue c0; 197→227 (7→7) g30 green c3; 227→239 (7→9) g12 black c1; 239→269 (9→9) g30 green c3; 269→281 (9→1) g12 black c2; 281→311 (1→1) g30 green c3; 311→347 (1→7) g36 δ6 blue c3; 347→419 (7→9) g72 δ2 black c7; 419→431 (9→1) g12 black c2; 431→461 (1→1) g30 green c3; 461→521 (1→1) g60 δ0 green c6; 521→569 (1→9) g48 δ8 white c4; 569→599 (9→9) g30 green c3; 599→617 (9→7) g18 δ8 white c2; 617→641 (7→1) g24 δ4 red c3.

**OTOB-SW scene 4 "swCusp": "Seiberg–Witten · harmonic winding".** Grade: "Exact translation · horocycle".
- eq: "sₖ = i ± 2k / wₖ = 1/(i ± 2k)".
- sub: "Each bead is one winding in a local coupling frame. The reciprocal ladder is harmonic and the orbit lies on a horocycle in the same ball."
- note: "The finite frames move by +2. The infinity frame moves by −2 in the paper’s loop convention. These windings act at a fixed base point."
- lean: "Lean · cusp_frames · cusp_translate_add · Seiberg–Witten §§5–6".
- Control: select "Local frame" (three frames).

**TTOS scenes ("eyes"), verbatim text and readout rows:**
1. id both, "Two trees on one scale." Grade "Exact frame; the chain measured". eq: "height = ln n = distance from the vacuum point / Garrett level L at L·ln 5 · twin pair (a, a+2) at ln a". sub: "Garrett's tree on the left and the twin-prime chain on the right grow up the same height axis. Every ball, in both trees, carries the same six-arm star: the three axes i, j, k and their reverses." note: "Gold bands mark Garrett's levels across both trees. A twin pair sits at the same height as the peel step of its own size. The trees share the frame and the scale; whether anything else lines up is what the test eye answers." lean: "Lean: Two Trees v4 (the ladder Γ_L, freeness at ratio 5 and 7) · BallJoins J1, J6". Rows: height (= ln n); Garrett level here (= ln n / ln 5); twin pair here; twin pairs below (k+1); Garrett balls below = 1 + 6(5^L - 1)/4, L = floor(level); "same rule on both" = "each ball: six arms, one frame". Ball counts by level L = 0..5 (re-computed): 1, 7, 37, 187, 937, 4687.
2. id scale, "The shared height." Grade "Proved". eq: "Γ(n) = (n − 1)/(n + 1),  distance from the vacuum = ln n". sub: "One axis for everything: any number n is a peel step of ratio n, at hyperbolic distance ln n from the vacuum point." note: "A twin step from a to a + 2 is a tiny peel step, Γ = 1/(a + 1): the chain climbs in very small steps, Garrett in steps of ln 5." lean: "Lean: Two Trees v4 gam_mul, peel_ladder (core Lean)". Rows: number n = round(exp(u ln 3125)); height ln n; Smith step Γ = (n−1)/(n+1); "distance from vacuum" = "ln n, exact (Two Trees Cor. 2.4)"; "twin pair (a, a+2) step" = "Γ = 1/(a+1), length ln(1+2/a)"; "Garrett level L" = height L ln 5. (re-computed) Γ(2) = 0.3333, Γ(5) = 0.6667, Γ(3125) = 0.9994; Γ of ratio (a+2)/a = 1/(a+1) algebraically.
3. id garrett, "Garrett's tree of balls." Grade "Lean (freeness); layout a display choice". eq: "six arms per ball, five onward (no step back) / level L at height L·ln z". sub: "Each ball branches the same way as every other ball. The star on each ball is turned by its own word's Thomas frame, so balls reached by different turns face different ways." note: "The three axes are drawn flat, 120° apart, to lay the tree out; the star on each ball shows the true three-dimensional frame. Move the ratio between 5 and 7." lean: "Lean: Two Trees v4 free5, free7, thomas5 · BallJoins J7 reverse_turn". Control "Peel ratio (5 or 7)" 5..7 step 2. Rows: peel ratio; "branches per ball" = "6 out, 5 onward (no step back)"; "balls to level 4" = 937; "level height" = "L · ln z = value per level"; "every ball" = "the same six-direction star"; "star turn" = "its word's Thomas frame"; "free for every word" = "Lean (Two Trees v4: free5, free7)".
4. id chain, "The twin chain as a tree of balls." Grade "Lean (three shafts); cone radius measured". eq: "angle 12°·a (one turn per 30) · height ln a · radius from the measured ring width / shaft 1, 7, 9 → axis i, j, k". sub: "Each twin pair is a ball on the colour cone from the film. Its lit arm is the axis of its shaft; the links between balls carry Elizabeth Johnson's five connector colours." note: "The gold guide lines are the three twin-start slots 11, 17, 29 (mod 30). The star on each ball is turned by the frame of its last twelve steps." lean: "Lean: BallJoins.twin_start_digit (J6), first proved by Elizabeth Johnson". Rows: twin pair; height ln a; "shaft → axis" (digit → i/j/k or "waist"); "connector γ to next" (a'-a-2); link colour; "frame turn (last 12 rings)" in degrees; "three shafts" = "Lean (BallJoins J6)".
5. id frame, "One ball, close up." Grade "Computed from exact steps". eq: "M = Π [(z + 1) + (z − 1)σ_u]/(2√z),  M = H·U / turn = angle of U". sub: "The camera rides up the chain one ball at a time. The star turns as the walk changes axis and holds when it goes straight." note: "Frames are taken over windows of twelve rings, as in the test." lean: "Lean: BallJoins.reverse_turn (J7); Two Trees thomas5 for the single turn". Rows: twin pair; "step taken" axis; "frame turn (last 12 rings)"; "why it turns" = "Thomas turn, tan(θ/2) = Γ² = 4/9"; "reverse order" = "reverse turn (BallJoins J7)". Camera follows the first up to 40 pairs.
6. id test, "What the merge shows." Grade "Computed; failed this way where marked". eq: "real chain vs shuffles that keep the step-to-step counts". sub: "Both trees share the scale and the frame exactly. The question was whether the primes put any order into the turning beyond one step back." note: "They do not, at ratio 5 or 7, forward or reversed: the real chain sits inside the band. Digit pairs reach the whole ratios 2, 3, 5 only, never 7, and the census does not prefer them." lean: "Lean: BallJoins J10 (digit pairs); the walk test is a computation". Rows (static text): test = "frame turn of the real chain vs shuffles"; "kept in the shuffles" = "the step-to-step counts"; "ratio 5" = "real 1.2527, band 1.197–1.302"; "ratio 7" = "real 1.3838, band 1.318–1.438"; "reversed" = "the same"; "reading" = "inside the band: no order beyond one step"; "digit pairs on whole ratios" = "(4,1) (8,2) (9,1) (9,4): 3, 3, 2, 5 (J10)"; "rational cells 1→9, 9→1" = "not preferred: failed this way".
   - The numbers 1.2527, 1.197–1.302, 1.3838, 1.318–1.438 are hard-coded here, and among the three .txt readings in my assignment appear only in TTOS. The statistic (what "1.2527" measures, its units, number of shuffles, window) is not defined in these files; the shuffle script is not here.
   - Digit-pair decode (re-computed): pairs (a,b) = (4,1), (8,2), (9,1), (9,4) give Γ² = b/a = 1/4, 1/4, 1/9, 4/9, so Γ = 1/2, 1/2, 1/3, 2/3 and z = (1+Γ)/(1-Γ) = 3, 3, 2, 5, which are the printed "3, 3, 2, 5". The page does not state this rule; it is consistent with BJ garrett_pair (9,4), Γ² = 4/9.

### 3.2 BallJoins.lean — every theorem, plain words
Over an arbitrary field K unless an ordered field is named; gam z = (z-1)/(z+1).
1. book_is_peel (J1): for Wp ≠ 0 and Wm + Wp ≠ 0, (Wm − Wp)/(Wm + Wp) = gam(Wm/Wp). A ratio of two books is a peel step.
2. current_is_peel (J8): for Bk ≠ 0 and F + Bk ≠ 0, (F − Bk)/(F + Bk) = gam(F/Bk). The prime current (forward minus backward over total) is a Smith point; proved from book_is_peel with roles swapped.
3. ceiling_is_peel (J2): in a strictly ordered field, for natural k > 0, gam((k+1)/k) = 1/(2k+1). The equal-gap rung ceilings 1/(2k+1) are the peel steps of ratio (k+1)/k.
4. line_ratio (J3): in an ordered field, if r > 0 and r² = 2 then gam(3 + 2r)² = 1/2. Garrett's line Γ² = 1/2 is the peel ratio 3 + 2√2. (Hand check: gam = (1+r)/(2+r), square (3+2r)/(6+4r) = 1/2.)
5. five_inside_seven_outside: in ℚ, gam(5)² < 1/2 and 1/2 < gam(7)² (4/9 and 9/16). "Norm 5 sits inside the line, Garrett's drawn step 7 outside it."
6. trace_reflect_transmit (J4): c ≠ 0, c² − s² = 1, R := (s/c)²: 2 − 4 s⁴ = 2 − 4 (R/(1−R))². The perpendicular commutator trace 2 − 4 sinh⁴(r/2) in reflect/transmit form (c = cosh(r/2), s = sinh(r/2), R = tanh², T = 1 − R, R/T = s²).
7. euclid_is_thomas (J5): for a ≠ 0: a²(1 − (b/a)²) = a² − b², a²·2(b/a) = 2ab, a²(1 + (b/a)²) = a² + b². Euclid's triple is the Thomas-turn triple with t = b/a.
8. euclid_pythagorean: for integers, (a²−b²)² + (2ab)² = (a²+b²)².
9. garrett_pair: gam(5)² = 4/9 and (9²−4², 2·9·4, 9²+4²) = (65, 72, 97). Garrett's norm-5 step: pair (9,4), triple (65,72,97).
10. twin_start_digit (J6): for naturals a with a and a+2 prime and 5 < a, a mod 10 ∈ {1, 7, 9}. Proof route: a odd; a mod 5 ≠ 0; a mod 5 ≠ 3 (else 5 | a+2); so a mod 5 ∈ {1,2,4}. "Elizabeth Johnson's theorem, re-proved."
11. reverse_turn (J7): in a monoid with a product-reversing involution τ, if τA = A, τB = B, τL = L, R·τR = 1 and A·B = L·R, then B·A = (τR·L·R)·τR and τ(τR·L·R) = τR·L·R. Reversing two symmetric steps gives the inverse turn.
Header map: J1 book_is_peel; J2 ceiling_is_peel; J3 line_ratio (+ five_inside_seven_outside); J4 trace_reflect_transmit; J5 euclid_is_thomas (+ euclid_pythagorean, garrett_pair); J6 twin_start_digit; J7 reverse_turn; J8 current_is_peel.

### 3.3 SeibergWitten.lean — every theorem, plain words
Header: "Algebraic slice of Seiberg–Witten, hep-th/9407087, §§5–6. Periods are columns (a_D,a); charges are rows (n_m,n_e). The paper's analytic continuation results are inputs to the comparison." Core Lean (import Lean; uses grind, decide); README: "Lean 4.24.0, core library only". No sorry (grep 0).
Definitions: Mat (a b c d integers), mul, adj A = [d,-b;-c,a], tr, det, Charge (m,e), pairing q r = q.m r.e − q.e r.m, row q A = (q.m a + q.e c, q.m b + q.e d), twist k q = [1+2k e m, 2k e²; −2k m², 1−2k m e] ("signed rank-one transvection with the paper's width-two normalization"), mono q = twist 1 q, monopole = (1,0), dyon = (1,−1), mPlus = [1,0;−2,1], mMinus = [−1,2;−2,3], mInfinity = [−1,2;0,−1], S = [0,−1;1,0], T = [1,1;0,1], translate n = [1,n;0,1], column, central, straight n = (1,−n), nextCharge q r k = (q.m + k r.m, q.e + k r.e), chainStep, curve u x = (x−1)(x+1)(x−u), disc u = 4(u−1)²(u+1)².
Theorems (33, in file order):
1. twist_det: det(twist k q) = 1.
2. twist_fixes_charge: a charge is fixed by its own twist.
3. twist_add: twist k q · twist l q = twist (k+l) q.
4. det_mul: det(AB) = det A · det B.
5. pairing_covariant: pairing(qA, rA) = det A · pairing(q,r).
6. central_covariant: central(row q (adj A), A p) = det A · central q p (charge transforms contragrediently; polynomial identity, no analytic input).
7. twist_pair_trace: tr(twist k q · twist l r) = 2 − 4 k l (pairing q r)².
8. opposite_order_pair: tr(mono q · mono r) = tr(mono r · mono q).
9. trace_minus_two_iff_neighbors: tr(mono q · mono r) = −2 iff pairing q r = 1 or −1.
10. paper_matrices (decide): mono monopole = mPlus; mono dyon = mMinus; mPlus·mMinus = mInfinity; mMinus·mPlus ≠ mInfinity. "Eqs. (5.12), (5.13) and (6.1), in the paper's loop order."
11. cusp_frames (decide): adj(S)·(mPlus·S) = translate 2; adj(TS)·(mMinus·(TS)) = translate 2; mInfinity = [−1,2;0,−1].
12. cusp_translate_add: translate(2n)·translate(2j) = translate(2(n+j)).
13. infinity_charge_shift: row q mInfinity = (−q.m, −(q.e − 2 q.m)) (§5.5 shift with the overall sign kept).
14. straight_neighbor: tr(mono(straight n) · mono(straight(n+1))) = −2.
15. straight_gap_trace: tr(mono(straight n) · mono(straight(n+j))) = 2 − 4 j².
16. continued_fraction_step: pairing r (nextCharge q r k) = − pairing q r.
17. chain_pairing_sq: after any list of continued-fraction steps the squared pairing of the final pair equals that of the start pair.
18. chain_pair_trace: the trace of the final adjacent pair equals the trace of the starting pair, for any list of steps.
19. twist_charge_action: row q (twist k r) = (q.m + 2k·pairing(q,r)·r.m, q.e + 2k·pairing(q,r)·r.e).
20. twist_conjugation: if det A = 1 then twist k (row q A) = adj A · (twist k q · A).
21. twin_pair_literal_lift: pairing((a,a+2),(b,b+2)) = 2(a − b).
22. twin_pair_literal_lift_fails: for all integers a, b: tr(mono(a,a+2) · mono(b,b+2)) ≠ −2.
23. three_step_negative_control (decide): tr(mono(straight 0) · mono(straight 1) · mono(straight 2)) = −6.
24. discriminant_factor: disc u = 4(u²−1)².
25. cubic_discriminant: the standard cubic discriminant of x³ − u x² − x + u (b = −u, c = −1, d = u) equals disc u.
26. curve_expansion: (x−1)(x+1)(x−u) = x³ − u x² − x + u.
27. picard_fuchs_numerator: (x−u)(3x² − 2u x − 1) − 2·curve u x = (x−u)((x−u)² − (u²−1)).
28. local_recurrence_coefficients: 4((n+1)n b + 2(n+2)(n+1)c) + b = (2n+1)² b + 8(n+2)(n+1)c (operator (z²+2z)d²/dz² + 1/4, cleared of 4).
29. infinity_recurrence_coefficients: ((1−4(n+1))(−1−4(n+1)) + 1)c − (1−4n)(−1−4n)b = 16(n+1)² c − (16n² − 1) b ((u²−1)d²/du² + 1/4 at infinity).
30. central_phase_pairing: (qm dI + qe aI)(rm dR + re aR) − (qm dR + qe aR)(rm dI + re aI) = (qm re − qe rm)(dI aR − dR aI), i.e. Im(Z(q)·conj Z(r)) factors as pairing times Im(a_D·conj a). Source comment: "an alignment criterion; stability still depends on the spectrum."
31. local_log_jump: given i² = −1, invPi·pi = 1: regular + i·invPi·aD·(logValue + 2 pi i) = regular + i·invPi·aD·logValue − 2 aD (§5.4 coefficient and sign).
32. infinity_log_jump: −regular + i·invPi·(−a)(logValue + 2 pi i) = −(regular + i·invPi·a·logValue) + 2a (Eq. (5.3)).
33. effective_vacuum: in a commutative ring with no zero products, if coupling·(M·Mtilde) + perturbation·slope = 0, perturbation·slope ≠ 0 and aD·M = 0, then aD = 0, M ≠ 0 and Mtilde ≠ 0 (§5.6 eq. (5.20) algebra).
End of file: `#print axioms` for 12 theorems. lean-audit.txt lists all 33 (name set identical to the file's, diffed): paper_matrices, cusp_frames, three_step_negative_control depend on no axioms; the other 30 on [propext, Classical.choice, Quot.sound].

### 3.4 Harmonic-chains folder (README.md, check_chains.py, chain-results.txt)
README opening: "First executable formalization of selected algebraic steps in §§5–6 of Seiberg and Witten's 1994 paper, with new chain experiments prompted by Jeromie Beasley's Two Trees in One Ball and the twin-prime chain work of Beasley and Elizabeth Johnson." Reproduce: `lean SeibergWitten.lean`; `python3 check_chains.py` (exact integers and rationals; quadrature in floating point).
- Rule: M(q) = [1+2em, 2e²; −2m², 1−2me]; <q,r> = m r_e − e r_m; q M(r) = q + 2<q,r> r; tr(M(q)M(r)) = 2 − 4<q,r>². Pairing ±1 gives trace −2 "in this integral lift". M(1,0), M(1,−1) reproduce Eqs. (5.12)–(5.13); in Fig. 1's loop order the product is [[-1,2],[0,-1]] (Eq. 6.1); the reversed product differs though the trace agrees.
- chain-results.txt (script output, exact):
  - Straight (1,0)..(1,-6): pairings all -1, traces all -2, full trace -14.
  - Fibonacci [(1,0),(1,-1),(2,-1),(3,-2),(5,-3),(8,-5),(13,-8)]: pairings -1,1,-1,1,-1,1; traces -2; full trace 34.
  - Pell [(1,0),(1,-1),(3,-2),(7,-5),(17,-12),(41,-29),(99,-70)]: same pairings; traces -2; full trace -4558.
  - Mixed [(1,0),(1,-1),(2,-1),(7,-4),(16,-9),(87,-49),(103,-58)]: traces -2; full trace -74878.
  - Skipped [(1,0),(1,-2),...,(1,-12)]: pairings all -2; traces all -14; full trace 194.
  - Literal twin-prime lift [(5,7),(11,13),(17,19),(29,31),(41,43)]: pairings -12, -12, -24, -24; traces -574, -574, -2302, -2302; full trace 149066498.
  - Quadrature: u=1.25: a = 1.504078928770, a_D = i*0.123132888282, errors 2.22e-16, 1.39e-17; u=1.50: a = 1.677609971862, a_D = i*0.242837066949, 2.22e-16, 0.00e+00; u=2.00: a = 1.966685301550, a_D = i*0.473434436536, 2.22e-16, 5.55e-17; u=2.50: a = 2.212804227088, a_D = i*0.694113024191, 0.00e+00, 1.11e-16. Script asserts max error < 1e-10.
- README: three consecutive straight charges already give product trace −6; seven-charge full traces −14, 34, −4558, −74878; "Their neighboring traces all agree."
- Harmonic ladder: in a width-two local frame s -> s+2; w = 1/s gives w -> w/(1+2w), w_n = 1/(s0 + 2n) (script assert at s0 = 3, n = 0..9). Infinity lift is −T⁻², "opposite translation in the paper's loop convention". "The winding ladder concerns analytic continuation at a fixed base point. The physical approach to a cusp concerns changing u. The two operations have different meanings."
- Curve bridge: f = (x−1)(x+1)(x−u), y² = f, λ = (x−u)dx/y locally; affine cubic discriminant 4(u²−1)² "detects the two finite degenerations; the cusp at infinity belongs to the compactified parameter space"; ∂uλ = −dx/(2y), ∂u²λ = −dx/[4(x−u)y]; [(u²−1)∂u² + 1/4]λ = (1/2) d_x(y/(x−u)); period equation (u²−1)Π'' + Π/4 = 0 (analytic step is in the note; numerator algebra in Lean).
- Series: near infinity a(u) = sqrt(2u) Σ c_n u^(−2n), c_0 = 1, c_{n+1}/c_n = (16n²−1)/[16(n+1)²], first 1, −1/16, −15/1024. Near the monopole a_D = (i/2) z Σ b_n z^n, z = u−1, b_0 = 1, b_{n+1}/b_n = −(2n+1)²/[8(n+1)(n+2)], first 1, −1/16, 3/256. Script integrals: a_int = sqrt2/pi * Simpson(sqrt(u − cos t), 0..pi); aD_int = sqrt2/pi * z * Simpson(2cos²t / sqrt(2 + z sin²t), 0..pi/2), 4096 intervals. README: "a numerical cross-check ... It does not certify the general analytic continuation."
- README chain table: Straight (1,−n): pairing −1, trace −2; Fibonacci: pairing alternates ±1, trace −2; Pell: same; Mixed continued fractions: same for every integer list of steps from the same seed; Skip every other (1,−2n): pairing −2, trace −14; Literal twin-prime lift (p,p+2): pairing 2(p−q), always even, "neighboring trace can never be −2".
- Paper-to-Lean boundary table: §5.4 (5.10)–(5.12) and §5.2 (5.3): log-jump algebra, signs, matrix factors / continuation and square-root sign enter as premises. §5.5 and §6 (6.1), (6.7): ordered product, fixed charges, conjugation, determinant, pairing / identifying cycles, based loops, geometric monodromy. §§4–6: central charge covariance and phase-alignment polynomial identity / complex period functions, stability, wall crossing. §6 (6.6), (6.19), (6.22)–(6.23): affine discriminant, numerator, series coefficient algebra / differentiation of periods, holomorphic continuation, convergence, full log coefficients. §5.6 (5.17)–(5.20): conditional F-term implication aD = 0, M ≠ 0, M̃ ≠ 0 / effective superpotential, D-term and gauge quotient, mass gap, physical confinement.
- Limits stated: "The successful alternative chains generate lattice words and candidate matrices. The paper's three punctures and loop choices supply the actual geometric monodromies. The other chains do not imply extra singularities or stable dyons." "Selecting a stable spectrum still requires wall crossing and sign data." The twin-lift test "tests one proposed embedding ... leaves the twin-prime path and direction labels in the original ball model intact."

## 4. FAILED OR SET ASIDE
- Literal twin-pair lift into the charge lattice, (p, p+2) as charge (m,e): fails the neighbour condition always. Failure condition (Lean twin_pair_literal_lift_fails): pairing = 2(a−b) is even, so trace ≠ −2. Numbers: traces −574, −574, −2302, −2302 (chain-results.txt). In the mixer it is "Literal twin-pair lift · control" with coral edges. The wheel map 1,7,9 -> (1,0),(1,−1),(0,1) is the alternative used.
- Skip-a-dyon control: pairing −2, trace −14 (Lean straight_gap_trace with j = 2: 2 − 4·4).
- Trace-only agreement is not enough: three_step_negative_control (product trace −6 for three straight charges); mMinus·mPlus ≠ mInfinity although traces agree (paper_matrices, opposite_order_pair).
- Wheel digit repeats (1→1, 7→7, 9→9): pairing 0, adjacent trace 2, not −2 (my re-computation; the files do not state it).
- TTOS test eye ("failed this way where marked"): twin-chain frame turn vs shuffles inside the band at ratio 5 and 7, forward and reversed; "no order beyond one step". Band lines: ratio 5 real 1.2527 in 1.197–1.302; ratio 7 real 1.3838 in 1.318–1.438. Digit pairs reach whole ratios 2, 3, 5 only; "rational cells 1→9, 9→1" not preferred.
- OTOB scene 2 note: the true-step chain is not a geodesic: distance/path length → about 0.588 (re-computed).
- Seiberg-Witten limits: no analytic continuation certified; quadrature is a numerical cross-check only.

## 5. OPEN QUESTIONS THE SOURCES LIST
- TTOS: "whether anything else lines up is what the test eye answers" (the test eye answers: not beyond one step back).
- README: remaining formalization "starts with the family of smooth curves over the punctured u-plane, transport of the chosen homology cycles, and differentiation of the period map"; the effective F-term result depends on the D-term analysis and the physical confinement argument; stability needs wall crossing; at the other finite cusp "the choice of dyon cycle and normalization left explicit".
- README: physical approach to a cusp (changing u) versus the winding ladder (continuation at a fixed base point) "have different meanings"; not reconciled.
- SW.lean header: analytic continuation results are inputs, not proved.

## 6. ELEMENTS HOOKS
Summary: these files contain no atoms, ionisation ladders, atomic shells, screening, metals/non-metals, colour of matter, 5/8, alkali metals, francium or "space between" (grep over the three .txt files and both Lean files). What touches the listed items:
- Wall Γ² = 1/2 and z = 3 + 2√2: BJ header J3 "Garrett's line Γ² = 1/2 is the peel ratio 3 + 2√2"; theorem line_ratio (r > 0, r² = 2 gives gam(3+2r)² = 1/2); five_inside_seven_outside: gam(5)² = 4/9 < 1/2 < gam(7)² = 9/16 ("Norm 5 sits inside the line, Garrett's drawn step 7 outside it"). The wall is NOT drawn in any of the three mixers. Mixer peel-ratio sliders allow z in {3,5,7,9} (OTOB/OTOB-SW ride) and {5,7} (TTOS garrett), so the wall ratio 5.828 is not selectable. (re-computed) gam(3)² = 1/4 inside, gam(9)² = 16/25 outside.
- Rim: OTOB/OTOB-SW draw the ball boundary as a wireframe sphere of radius RB = 3.4; SW scenes add a rim circle; text "Past pairs fall away toward the rim behind"; code comment in swGeo "close to the rim". No statement |Γ| = 1 in these files; TTOS scale eye gives Γ(n) → 1 (Γ(3125) = 0.9994, re-computed).
- Garrett levels as spheres: Γ_L = (z^L − 1)/(z^L + 1) at radius RB·Γ_L, height L·ln z; at z = 5: Γ_1 = 0.6667, Γ_2 = 0.9231, Γ_3 = 0.9841 (re-computed). Page comment calls them "level shells" (geometric spheres of the tree, not atomic shells).
- BJ J2: "The equal-gap rung ceilings 1/(2k+1) are the peel steps of ratio (k+1)/k" (gam((k+1)/k) = 1/(2k+1)); ladder language with no element named.
- BJ J1/J8: ratio of two books (W₋ − W₊)/(W₋ + W₊) = Γ(W₋/W₊) and the prime current (F − B)/(F + B) = Γ(F/B): the only two-books shape in these files (written W₋, W₊, not E₋/E₊).
- Colour: only the five connector colours (green, black, red, blue, white); no colour-of-matter content.
- TTOS cone: angle 12°·a, "one turn per 30"; slots 11, 17, 29 mod 30 (stated in the page; J6 gives only end digits 1,7,9).
- Garrett norm-5 step: Γ² = 4/9, pair (9,4), triple (65,72,97) (BJ garrett_pair; also the "tan(θ/2) = Γ² = 4/9" Thomas turn line in TTOS).

## 7. CONTRADICTIONS OR SLIPS
1. Connector colour keying differs between scenes in the same OTOB-SW file: ride/whole (and TTOS chain links) use ((a'−a−2) mod 10)/2; the SW wheel scene uses ((a'−a) mod 10)/2 (start gap, not gap−2). Same link, colour shifted by one class: 11→17 ride red, wheel blue; gap 30: ride white, wheel green (re-computed). Over the 3,801 links the counts are rotated: ride white 1099, green 982, blue 814, red 495, black 411; wheel green 1099, black 982, white 814, blue 495, red 411. The page says the wheel "uses its own gap colors, keyed to the twin-start gap mod 10", so it may be deliberate, but scene 1's readout names its colour by "connector (a'−a−2)".
2. "J10" (digit pairs) is cited in the TTOS test eye and its lean line; BallJoins.lean has J1–J8 only (no J9, no J10, no digit-pair theorem). Also cited and not in BJ: free5, free7, thomas5, gam_mul, peel_ladder, "Cor. 2.4" (all attributed to Two Trees v4, which is not in my assignment).
3. TTOS "why it turns: Thomas turn, tan(θ/2) = Γ² = 4/9" is a fixed string for every ball, while the computed "frame turn (last 12 rings)" values run 0 to 141.38 deg (re-computed) because they are products of up to 12 steps; 47.92 deg is the single-pair value only.
4. TTOS label "waist (3,5,7)" but TW starts at a = 5 (pair 5,7); (3,5) is not in the list; only a = 5 gets sh = −1.
5. Step conventions differ across pages: OTOB "ride" uses the same ratio z for every chain step; OTOB "whole" uses true ratios a'/a; TTOS frames use ratio 5 for every step while positions use ln a. TTOS "frame" note does not say which ratio ("Frames are taken over windows of twelve rings, as in the test").
6. README says "Lean 4.24.0, core library only"; BJ says "Lean 4.34.1 with Mathlib": two projects, two toolchains.
7. SW.lean: the comment "Charge transforms contragrediently when periods transform by A. This proves equality of the central-charge pairing for all integer periods." sits above `def column`, ahead of `def central`, not above theorem central_covariant.
8. OTOB-SW keeps the header "SCRIPT: one_tree_one_ball_mixer_v1" and the title "One Tree, One Ball" although it has two more scenes than OTOB; the filename carries "(4)".
9. README states pairing ±1 gives trace −2, and lists no wheel row; the mixer's wheel family has pairing 0 (trace 2) on every repeated digit (re-computed). The wheel charge family exists only in the mixer, not in README, check_chains.py or Lean.
10. In the cusp scene the "plus" and "minus" frames draw identical geometry (sign +1, same orbit); only their labels differ. Labels check against Lean cusp_frames: adj(S) mPlus S = T² gives s = S⁻¹τ = −1/τ; adj(TS) mMinus (TS) = T² gives (TS)⁻¹τ = 1/(1−τ). Consistent.
11. TTOS test-eye numbers (1.2527 etc.) have no script or definition in the delivered files; the grade says "Computed" but the only trace of computation is the string.

## 8. THINGS A LATER READER WOULD WALK PAST
- Wheel charge map closes cyclically: M(1,0)·M(1,−1)·M(0,1) = −I = [-1,0;0,-1] (re-computed); cyclic pairings −1, +1, −1. Among all 27 ordered digit triples from {1,7,9} only the three cyclic rotations of (1,7,9) close. The code comment gives this as why the labels were fixed this way; the readout "· closes in the ball" fires only then (5 of 25 windows in the first 27 starts).
- Digit-pair decode of the TTOS test line: (4,1),(8,2),(9,1),(9,4) -> Γ² = b/a -> z = 3,3,2,5; "never 7" because z = 7 needs Γ² = 9/16 i.e. pair (16,9), not a pair of digits. The page never states the decode.
- OTOB "whole": distance/path length is 0.5883 at pair 228197 (re-computed) and the Garrett level reached by the 2400th pair is 3.63; the page only says "closer to the centre than its path length".
- Counts: 3,802 twin pairs below 400,000 in the OTOB sieve; "whole" uses the first 2400 (latest pair 228197, 228199); "ride" wraps at k = 3794.
- Straight-dyon prefix traces 2, −2, −6, 2, 10, −2, −14: the full-product trace moves while every neighbour trace stays −2 (README gives only −14 and −6).
- chain_pair_trace (Lean) says the neighbour trace is unchanged by any continued-fraction step list: −2 is a property of the seed pair (1,0),(1,−1) (pairing −1), not of the primes; all non-wheel "original" families therefore draw gold; only skip and twins draw coral.
- BJ five_inside_seven_outside and line_ratio are the only wall statements in this assignment.
- TTOS DATA.halfw is the only embedded measurement in the three mixers: r = 0.35 + 1.35·hw/117.5 gives 0.448 at a = 10 and 1.70 at 10^7 (re-computed from the formula). The chain only reaches a < 3125 (log10 about 3.5), so rows 4–7 beyond a ≈ 3162 are never used on screen.
- Ball counts of Garrett's tree (937 to level 4, 4687 to level 5) are independent of z.
- The cusp readout "reciprocal after k windings" is 1/(i + 2k) rationalised: (2k − i)/(4k²+1); at k = 0 it prints "(0 − i) / 1".
- README remark: Fibonacci and Pell chains alternate pairing ±1 exactly like the wheel's digit changes, which is why every one gives trace −2; skip chains break it (trace −14).
