# T8_gap_depth REPORT (2026-11-12)

## Answer to his question
Is the gap forced between two balls the same length as the decay depth past the critical angle? In his coordinate the two decay at the same rate at exactly one step ratio, z* = 6.26912766085231868475884183498070994042359232754037236 (just past the wall at 5.828), and at no other z. For every other z the passes-per-e-fold differ by the factor lambda/ln z (1.519 at z = 7, 2.438 at z = 11). Even at z* the amplitudes agree only in rate: gap/amplitude tends to 2, not 1.

In LENGTH the picture is cleaner and is the stronger half of the answer: measured in his length variable (L = artanh G, one step B has L = r/2), the gap 1 - tanh L = 2/(e^{2L}+1) and the evanescent amplitude e^{-2L} both decay with constant exactly 2, e-fold length 1/2, at every z (c = 2 to 4e-55). So the "same law" is true as a function of length; what differs is how long one pass is. A ball step has length r/2 = ln(z)/2; a pass of the loop W has length L_W = lambda/2 (from the eigenvalues of -W). These two lengths are equal only at z* (difference 0.193 at z = 6.5, 0.505 at z = 7, 1.72 at z = 11, 6.59 at z = 206.768, -3.6e-56 at z*).

## Step 1: Snell past the wall
- Complex angle. sin(phi) = G/G_wall = sqrt2 G > 1 gives phi = pi/2 + i chi with cosh(chi) = sqrt2 G. Tested at 60 digits at z = 5.9, 6.5, 7, 8, 16.8177, 206.768, 1e6 (chi = 0.0927, 0.2715, 0.3466, 0.4434, 0.7004, 0.8676, 0.8814).
- lambda is a closed function of chi but NOT a simple multiple of it. Holds (worst residual over the 7 z): tanh(lambda/8) = sinh(chi) (2e-61); cosh(lambda/4) = cosh^2(chi)/(2 - cosh^2(chi)) (1e-50); cos(alpha/2) = sech(chi) (8e-62), i.e. alpha/2 is the Gudermannian of chi; measured lambda (from eigenvalues of -W) equals 4 arccosh(G^2/(1-G^2)) to 6e-56; K = coth^2(chi). Fail: lambda = 4chi, 2chi, chi, 8chi, chi/2 (residuals 45-52) and lambda/2 = ln K (25.6). Honest status: the three passing forms are algebra consequences of the confirmed loop2 law, so they show closure, not independent evidence.
- Real part, measured. For arms +z and -z in the own frame, with the boost axis (Hermitian part of U) as axis, sin^2(phi_real) = 1 exactly (residual 0) at all 7 z. The inside-wall form 2G^2 and five other candidates fail. The same code, using the rotation axis inside the wall, returns 0.5 at z = 3 and 8/9 at z = 5 (= 2G^2 to 20 digits). So past the wall Re(phi) stays pinned at pi/2 and all the excess of sin(phi) over 1 is the imaginary part chi, as in total internal reflection.
- In peel language: tanh(lambda/8) = sqrt(2G^2 - 1). Inside the wall the same law gives lambda imaginary, e^{-lambda} = e^{i theta}, unit modulus: the passes turn, they do not decay. The Snell picture (oscillation inside, evanescence past) holds in his coordinate.

## Step 2: definitions used
Gap: (a) g_n = 1 - G_n with G_n the n-fold (+) of G; verified = tanh(n r/2) to 1.6e-61 for n <= 30, so g_n = 2/(z^n+1). (b1) two facing identical cut balls, 2 g_n; (b2) composed g (+) g = 2g/(1+g^2). (c1) unequal levels: g1 + g2 and g1 (+) g2; (c2) length reading artanh g1 + artanh g2 = artanh(g1 (+) g2) (identity checked, 4e-62). Note: the length from a cut surface to the rim is infinite, so the only finite length gap is artanh of the coordinate gap. Example, absorber deep (z = 7, n = 3) and radiator shallow (z = 4, n = 1): g1 = 0.005814, g2 = 0.4, sum 0.405814, composed 0.404872, length 0.429463. Identical pairs: (7,3): 2g = 0.011628, composed 0.011628; (4,1): 0.8 and 0.689655.
Depth: (i) 1/lambda passes per e-fold; (ii) profile e^{-n lambda}; (iii) inside the wall, passes per full turn 2 pi/theta (no decay exists there).

## Step 3: comparison
Solve ln z = 4 arccosh((z-1)^2/(4z)). Sign scan over (wall, 3e12]: exactly one root. The hand cubic is confirmed: with y = z^{1/4} + z^{-1/4}, y^3 - 4y - 2 = 0 (residual 0 at 60 digits; y = 2.214319743377535187). Discriminant of the cubic 148 = 4 x 37 (by hand).
z* and companions (each is a root of a small polynomial, findpoly residual < 1e-60, so recognised as a cubic irrational and not as a familiar constant):
- ln z* = lambda* = 1.8356372159148182855434496624549510956693
- G* = 0.72486382227527198292840480115 (root of g^6 + 5g^4 - g^2 - 1)
- G*^2 = 0.52542756084351708734577917764 (root of x^3 + 5x^2 - x - 1)
- K* = 20.663702825333247324632423251508 (root of K^3 - 22K^2 + 28K - 8)
- z* is a root of the palindromic z^6 - 6z^5 - z^4 - 4z^3 - z^2 - 6z + 1; w = z + 1/z satisfies w^3 - 6w^2 - 4w + 8 = 0 (w = 6.42863948675507)
- pair partner G' = 1/(2G*) = 0.68978473560806513535, G'^2 = 0.475802981478 (inside the wall).
At z*: gap/amplitude = 2z^n/(z^n+1) = 1.7249, 1.99979, 2.0 at n = 1, 5, 20.

Ratios (gap e-fold 1/ln z over amplitude e-fold 1/lambda = lambda/ln z), past the wall:
| z | lambda | ln z | lambda/ln z | gap/amp n=1 | n=5 | n=20 |
|---|---|---|---|---|---|---|
| 7 | 2.955991775 | 1.945910149 | 1.519079 | 4.8052 | 312.15 | 1.19e9 |
| 11 | 5.847120315 | 2.397895273 | 2.438439 | 57.706 | 6.18e7 | 1.82e30 |
| z* = 6.2691 | 1.835637216 | 1.835637216 | 1 | 1.7249 | 1.99979 | 2.0 |
Inside the wall there is no decay depth (|multiplier| = 1). Reading (iii), passes per turn 2 pi/theta against the gap e-fold 1/ln z (ratio 2 pi ln z / theta):
| z | G^2 | theta | passes/turn | gap e-fold passes | ratio |
|---|---|---|---|---|---|
| 5 | 0.4444 | 3.70918 | 1.69395 | 0.62134 | 2.7263 |
| 4 (n=2) | 0.36 | 2.38963 | 2.62936 | 0.72135 | 3.6451 |
| 9/4 (n=3) | 0.1479 | 0.69798 | 9.00194 | 1.23315 | 7.2999 |
| 16/9 (n=4) | 0.0784 | 0.34069 | 18.4426 | 1.73803 | 10.6112 |
| 25/16 (n=5) | 0.0482 | 0.20259 | 31.0148 | 2.24071 | 13.8415 |
| 36/25 (n=6) | 0.0325 | 0.13447 | 46.7256 | 2.74241 | 17.0382 |
Inside the wall the "depth" is the turn: one full turn takes 2 pi/theta passes, which is longer than the gap e-fold at every shell step tabulated; no equality there. Gaps at shell steps (n=1 cut): 0.4, 0.6154, 0.72, 0.7805, 0.8197 for z = 4 ... 36/25; z = 5: 0.3333.

## Step 4: opposite reading in length
Kill lines not hit: per-pass lengths r/2 and L_W equal only at z*; both decay constants = 2 (e-fold length 1/2). Cross ratio artanh(g_n)/e^{-2 D_n} with D_n = n L_W: at z* 1.7705, 1.99979, 2.0; at z = 7: 4.909, 312, 1.19e9; z = 11: 58.2, 6.18e7, 1.82e30.

## Step 5: data
Untested: no lattice-constant or nearest-neighbour table on disk (grep and find over /home/claude; master_elements.json has colour, flame and IE1 only). The only spacing data is the metallic radius in work/pmg/periodic_table.json (a proxy for half the nearest-neighbour distance, 77 elements). The registered population (metallic radius AND a ratio z_k > 3+2 sqrt2 in the ionization ladder) holds 6 elements (Li, Be, Na, K, Rb, Cs), under the registered minimum of 25, so no verdict. The printed rho values (+0.83, +1.0, +0.83, -0.83 on n = 6) are not evidence: these are alkali metals ordered by period. A larger population would need a different, newly registered wall filter or step choice; not done.

## Not tested / limits
- The gap-to-lattice-spacing link itself (step 5). The Pauli claim: untested, no operator for it here.
- Two balls were treated by coordinate gap and composition (b, c); no geometric model of two tree-balls actually meeting was built.
- The past-wall arm was tested for +-z only; sin^2 phi_real = 1 there; other arm directions not run past the wall.
- lambda in terms of chi: the three passing forms are algebraic consequences of the loop2 law.
- Convention: his L = artanh G = r/2; standard hyperbolic translation length is twice that.

Files: /home/claude/harness/workers/T8_gap_depth/ (s1_snell.py, s1_out.txt, s3_compare.py, s3_out.txt, s4_length.py, s4_out.txt, s5_data.py, s5_out.txt, STATE.md, REPORT.md)
