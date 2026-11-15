# SCRIPT: BUILD-VOTKP-V33-01
# Builds VOTKP v3.3 from the complete v3.2 page. Nothing is removed from v2.9, v3.0, v3.1 or v3.2 except the sentences
# whose questions were answered on 12 November (twin-chain run, filling of the cap, mean of the band, Lean build);
# each is replaced by its result. Every replacement is asserted to match exactly once.
import sys
src, out = sys.argv[1], sys.argv[2]
t = open(src, encoding='utf-8').read(); n0 = len(t)
def once(old, new):
    global t
    assert t.count(old) == 1, (t.count(old), old[:90]); t = t.replace(old, new)
def M(x): return r'<span class="math inline">\(' + x.replace('<', '&lt;') + r'\)</span>'
def D(x): return r'<p><span class="math display">\[' + x.replace('<', '&lt;') + r'\]</span></p>'
C = lambda s: '<code>' + s + '</code>'

once('Version 3.2 — 12 November 2026 — developed with AI assistance', 'Version 3.3 — 12 November 2026 — developed with AI assistance')

# ---- 25.1: the twin-prime word carried to 10^9
once(' that is still moving; shuffling the arms gives', '; shuffling the arms gives')
once('It has not settled, and a run to ' + M(r'10^9') + ' is the test [Carried: <code>chain_whole_03.py</code>; the last-digit rule is that of the joint Base-10 Prime Pattern report; Open].',
     'Carried on in 40-digit arithmetic the turn is 12.03° at ' + M(r'3\times10^7') + ', 12.20° at ' + M(r'10^8') + ', 12.25° at ' + M(r'3\times10^8') + ' and 12.27° at ' + M(r'10^9')
     + ' (3,424,504 pairs). The steps per decade are 0.45°, 0.13° and 0.065°: each is smaller than the last, by factors 0.29 and 0.49, and the turn is not monotone, the value at '
     + M(r'3\times10^7') + ' lying below that at ' + M(r'10^7') + '. Between ' + M(r'10^7') + ' and ' + M(r'10^9') + ' it moved 0.20°, against a line of 0.1° written before the run. '
     'The axis has settled, moving 0.17° between ' + M(r'3\times10^8') + ' and ' + M(r'10^9') + '; the angle about it has not. The turn per step, the turn per unit of path and the tangent of the half angle show no limit either, and the word read in reverse gives the same angle at every cut-off '
     '[Carried: <code>chain_whole_03.py</code>; values to ' + M(r'10^9') + ' Exact, ' + C('walk.py') + ' with ' + C('sieve_twins.py') + ', double precision agreeing with 40 digits to ' + M(r'4\times10^{-7}') + ' of a degree; '
     'the last-digit rule is that of the joint Base-10 Prime Pattern report; whether the angle converges is Open].')

# ---- 25.2: the third-axis relation written against the wall
once('the third-axis value on 500 ratios.]</p>',
     'the third-axis value on 500 ratios.]</p>\n'
     '<p>Written against the wall, the third-axis relation is</p>\n'
     + D(r'\sin\varphi=\frac{\Gamma}{\Gamma_w},\qquad \Gamma_w=\frac{1}{\sqrt2},') +
     '<p>the sine of an angle equal to a ratio of two coordinates, which is the form of the law of refraction. The angle opens as ' + M(r'\Gamma') + ' rises, lies along the surface at the half line, where ' + M(r'\sin\varphi=1')
     + ', and has no real value beyond it, where the loop no longer turns and each pass shrinks by ' + M(r'e^{-\lambda}') + ' (§25.1 (d)). Read so, the half line is the critical angle of the hypersurface and the run beyond it is the decaying wave behind a surface that reflects everything; '
     'the atlas holds the two halves on B30 and B39. It is a different place from §9, where a refraction rule for the order of filling was tested and failed: here the form belongs to an angle at the wall. The coordinate itself changes sign when the two levels of a step are exchanged, ' + M(r'\Gamma(1/z)=-\Gamma(z)') + ', so two equal levels give ' + M(r'\Gamma=0')
     + ' and no step separates them, which is the form of an exclusion: what changes sign under exchange vanishes on equal entries. '
     '[The identity is Exact below the wall and the sign change is in Lean, ' + C('NewProps.lean') + '; the readings as refraction at the hypersurface and as exclusion are hypotheses of this programme and are Open.]</p>')

# ---- 25.3: how the cap fills
once('How fast the cap fills is not settled: within one of the cap by 2,000 passes was required and was not met in 19 of 144 cases; by 20,000 passes it is met in the frame of the centre and is two short in two cases in the frame of the ball [Exact, <code>check2_capacity.py</code>, <code>check2b_second_setup.py</code>, <code>check2c_three_distance.py</code>; the rate of filling is Open].</p>\n',
     'The cap is not always attained. Write ' + M(r'\delta=2\arcsin\!\big(\sqrt{\varepsilon/2}/\sin\varphi\big)') + ' for the least separation that counts. When ' + M(r'2\pi/\delta') + ' is a whole number there is no slack, the turn is irrational, and '
     + M(r'N\le\text{cap}-1') + ' at every ' + M('n') + ': in 34 such cases carried to 200,000 passes none reached the cap and all reached one below it. In every other case the cap is reached, after a number of passes of order the square of the cap: the median of '
     + M(r'n/\text{cap}^2') + ' is 1.2 in the frame of the centre and 1.9 in the frame of the ball, with a spread from 0.08 to 46 that follows the continued fraction of ' + M(r'\theta/2\pi') + ' and no smooth function of the ratio, the threshold and the direction. Two bounds hold without exception. With '
     + M('g_n') + ' the largest gap between the ' + M('n') + ' visited directions,</p>\n'
     + D(r'N(n,\varepsilon)\ \ge\ m\quad\text{as soon as}\quad (m-1)\,g_n\ \le\ 2\pi-m\,\delta ,') +
     '<p>and the first ' + M('n') + ' with ' + M(r'N\ge m') + ' is at least ' + M(r'1+\max_{1\le r<m} j_{\min}(r)') + ', where ' + M(r'j_{\min}(r)') + ' is the least ' + M(r'\lvert j\rvert') + ' with the fractional part of ' + M(r'j\theta/2\pi') + ' in ' + M(r'[\,r\delta/2\pi,\ r/m\,]')
     + ' (330 targets, no violation). Neither is the exact count: taken as a prediction the first overshoots the measured number of passes by a median factor of 3.9 and the second reaches a median of 0.56 of it, and the first reach falls at the start of a block of the three-gap pattern in only 34 of 330 targets, so the lengths of the gaps do not fix it without their order. '
     'In the atlas the count stands beside B16 and B18, which it would complete at a finite number of passes. [Exact, <code>check2_capacity.py</code>, <code>check2b_second_setup.py</code>, <code>check2c_three_distance.py</code>, ' + C('t3_a_failures.py') + ' to ' + C('t3_d_law_e.py') + ' and the three-gap scripts of Appendix F; the exact number of passes is Open].</p>\n')

# ---- 26.1: which point of the band, and what the mean is
once('at every finite ratio and ' + M(r'K\to2') + ' at the rim.</p>',
     'at every finite ratio and ' + M(r'K\to2') + ' at the rim.</p>\n'
     '<p>Which point of the band a step picks is fixed by one number, ' + M(r'm=\lvert v+we^{ik}\rvert^2/u^2') + ': ' + M(r'm=1/(2\Gamma^2)') + ' below the wall and ' + M(r'm=2\Gamma^2') + ' beyond it, so that ' + M(r'\cos k=(u^2m-v^2-w^2)/(2vw)') + ' and ' + M('K=m/(m-1)')
     + ' on both sides. The two members of a pair across the wall pick the same ' + M('k') + '; the step ' + M('z=3') + ' and the rim pick the point at which ' + M('K') + ' equals its mean over the band. A band with a gap holds only some of the ratios: at ' + M('u=0.5')
     + ' the steps from ' + M('z=5') + ' to ' + M('z=7') + ' fall beyond its end, and every ratio is held only by the family ' + M('w-v=u') + ' in which the gap closes. The mean itself is a statement about the two ends of the band. With ' + M('G_0') + ' and ' + M('G_1')
     + ' the peel coordinates whose obliqueness is that of the band at ' + M('k=0') + ' and ' + M(r'k=\pi') + ',</p>\n'
     + D(r'\langle K\rangle=1+\frac{2G_0G_1}{\sqrt{(1-2G_0^2)(1-2G_1^2)}},\qquad \langle K\rangle=2\iff G_0^2+G_1^2=\tfrac12\iff \frac{1}{K(0)}+\frac{1}{K(\pi)}=1 .') +
     '<p>The exit line of the chain is the half line shared between the two ends of the band; the wall is ' + M(r'\Gamma^2=\tfrac12') + ' for one step and the exit line is the same half for a pair of ends. '
     '[Exact: ' + C('s1_kz.py') + ', ' + M('K') + ' against the loop to ' + M(r'10^{-58}') + ' at twelve ratios on four exit bands; ' + C('s2_readings.py') + ', the identity on 40 random pairs to ' + M(r'10^{-37}') + '.] '
     'Means of ' + M('K') + ' taken evenly in ' + M(r'\Gamma') + ', in ' + M('z') + ', in ' + M(r'\ln z') + ' or in the turn give 2.3 to 3.4 and are not the exit line, and the three perpendicular pairs of steps give one ' + M('K') + ' between them. For the third-axis arm the mean of ' + M('1/K')
     + ' over one turn of the signal of §25.2 equals ' + M('1/K') + ' of the loop [Exact below the wall, ' + C('s3_arm.py') + '; beyond the wall not run].</p>')

# ---- open questions
once('what is the loop whose obliqueness is the mean over the band? ', 'the mean over the band is the half line shared by its two ends (§26.1): which pairs of steps of the tree are the two ends of one band? ')
once('How fast do the passes fill their cap of distinguishable directions? ', 'What is the exact number of passes at which the cap of distinguishable directions is first reached? ')
once('Does the frame turn of the twin-prime word settle? ',
     'The axis of the frame turn of the twin-prime word has settled: does its angle converge? Is the half line the critical angle of a law of refraction at the hypersurface, and is the layer always left between two balls the depth of the run beyond that angle? '
     'A tree on a prime ' + M('p') + ' has ' + M('p+1') + ' arms at every node, six, eight and twelve for 5, 7 and 11: are these the angles of the lattices of six, eight and twelve neighbours? ')

# ---- Lean
once('they were not compiled here. Propositions 22.1 to 22.3, 24.1, 25.1 and 25.2 are not yet in Lean.',
     'they compile under Lean 4.34.1 with Mathlib v4.34.1 built from source, 0 errors, and the repository\'s own ' + C('scripts/verify.py') + ' returns 140 theorems on the three standard axioms and 15 false controls rejected. The five files of <em>Two Trees</em> compile with 159 theorems, and its two controls files fail as they are meant to. '
     'Propositions 22.1 to 22.3, 24.1, 25.1 and 25.2 are in Lean as far as their algebra goes, in ' + C('NewProps.lean') + ', 43 theorems, no <code>sorry</code>: the three readings of the peel; the four edge coefficients and the half line at ' + M(r'z=3+2\sqrt2') + '; the ' + M(r'\oplus') + ' ladder and '
     + M(r'\Gamma(1/z)=-\Gamma(z)') + '; the touch and the split as finite linear algebra; the loop as explicit matrices with ' + M(r'\operatorname{tr}W=-2') + ', ' + M('(W+1)^2=0') + ' and ' + M(r'W+1\ne0') + ' at the wall, the identities for ' + M('K') + ', ' + M(r'\Gamma_5\Gamma_7=\tfrac12') + ' with ' + M('K=9') + ' and ' + M(r'\cos\theta=-527/625')
     + ' at ' + M('z=5') + '; and the arithmetic of the signal of 25.2. Stated in prose only: the ' + M(r'\tanh(\tfrac12\ln z)') + ' form, the module and knot-count parts of 24.1, the picture in the ball, the run beyond the wall, the formula for ' + M('c_n') + ' itself, the cap of §25.3 and the irrationality of the turn.')

# ---- appendices
once('<p><strong>Sections 25 and 26, second round (12 November 2026).</strong>',
     '<p><strong>Third round (12 November 2026).</strong> Each line was written before its run. '
     'Twin-prime word to ' + M(r'10^9') + ': the angle moves no more than 0.1° between ' + M(r'10^7') + ' and ' + M(r'10^9') + ': <strong>not met</strong> (0.197°); steps per decade halving: met (0.4526°, 0.1323°, 0.0648°); the original script unchanged returns 9.87°, 11.62°, 12.07°, 12.08°. '
     'Filling of the cap, each law required to give the first number of passes within a factor of two: the bound of §25.3 used as a prediction, <strong>not met</strong> in 177 of 230 and 138 of 196 on ratios not used to form it; a typical-gap form, not met in 41 of 230 and 28 of 196; the better of two readings in the frame of the centre, not met in 57 of 123, 39 of 104 and 51 of 103; the lower envelope, not met in 110 of 330; two opposite readings from the allowed steps, not met in 268 and 264 of 330. '
     'The class with no slack never reaching the cap: met, 34 of 34. An early run clipped every first reach below 8 passes to 8; it was corrected and every count here is from the rerun. '
     'Mean of the band: the end-pair identity and its two equivalents, line ' + M(r'10^{-10}') + ': met; the mean of ' + M('1/K') + ' over ' + M('dk') + ' (0.680), the sum, product and geometric mean of the end values (9.754, 9.754, 3.123) and the turn-mean of ' + M('K') + ' on seven prepared arms: not the exit line. '
     'Opposites of earlier lines that had fired and had no second setup, each with the line recorded for it beforehand: 24 run; in 11 the opposite met its line (level alone on polarizability 9 of 9; ' + M(r'\lvert\Gamma\rvert') + ' alone on 19 metals 0.977 against 0.743; the frozen thin-film rule on omitted films 11 of 12; the midpoint rule for the real-time charge, ' + M(r'5.5\times10^{-4}') + ' from 1; '
     'random splits at ' + M('K=6') + ', peel above static on 5 of 5 and on 200 further seeds; knots-only length ratios within 2.51 combined standard deviations; the wave against a row mean; the shifted f-block pairing 4 of 14 at most; a random forest on radius and hardness; CIE weights for the stretch toward white; the outer region of the bowl, where a control shows the same signal at every position from 0.2 to 0.6) '
     'and in 13 it did not (ratio-to-neighbour numerator; shape on 1,214 held-out nuclei 0.66 against 0.84; Khovanov rank on the 21 pairs, 0 separated; two rhythm comparisons; the first-to-second ratio 10.3% against 5%; walls split into two kinds, where the s-kind falls to 8.0% or less in every row and the p-kind stays at 22.2%, 16.6% and 26.0% in rows 4 to 6; the depth rule with ' + M('K+1')
     + ', forced by arithmetic; the per-core ladder count 0 of 11; the plasma rank, a sign flip only; no table field separating the 4 never-turners from the 19; shell and screening parts of the element blocks, neither near one half; the hidden level on 11 new links, 10 of 97; 38 new dielectrics, 77.0%). Five could not be run for want of a definition, fresh data or a solver, and four wait on data. '
     'Rerun of the knot scripts: all 28 ran and reproduce the stored outputs, the 11- and 12-crossing scan in pieces; the numerical scan, which omits 104 knots stopped at 60 seconds, counts 353 pairs equal on the three polynomials and 251 separated by volume, against 354 and 253 from the tables, and the pair not reached by the scan has not been identified. The nuclear classification reruns as 0.651 against 0.827 (stored 0.649 against 0.831).</p> '
     '<p><strong>Sections 25 and 26, second round (12 November 2026).</strong>')
once('<p><strong>Sections 25 and 26, second round:</strong>',
     '<p><strong>Third round:</strong> ' + ', '.join(C(s) for s in [
        'v33/twin_turn/walk.py', 'v33/twin_turn/sieve_twins.py', 'v33/twin_turn/orig_chain_whole_03.py',
        'v33/cap_fill/ (laws A, B, E and the reproduction of the 19 cases)', 'v33/cap_word/ (three-gap lower envelope and opposites)',
        'v33/band_mean/s1_kz.py', 'v33/band_mean/s2_readings.py', 'v33/band_mean/s3_arm.py',
        'v33/opposites/items/NN/ (one folder per line, original rerun beside its opposite)',
        'v33/lean/NewProps.lean', 'v33/reports/ (the report of each run, the knot rerun and the build log of the 140 theorems)']) + '.</p> '
     '<p><strong>Sections 25 and 26, second round:</strong>')

open(out, 'w', encoding='utf-8').write(t); print('v3.2 chars', n0, '-> v3.3 chars', len(t))
