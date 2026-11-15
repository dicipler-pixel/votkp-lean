# SCRIPT: BUILD-VOTKP-V32-01
# Builds VOTKP v3.2 from the complete v3.1 page. Nothing is removed from v2.9 or v3.0; four passages of Sections 25 and 26
# that v3.1 left open are replaced by their results, one subsection and ledger rows are added.
import sys
src, out = sys.argv[1], sys.argv[2]
t = open(src, encoding='utf-8').read(); n0 = len(t)
def once(old, new):
    global t
    assert t.count(old) == 1, (t.count(old), old[:90]); t = t.replace(old, new)
def M(x): return r'<span class="math inline">\(' + x.replace('<', '&lt;') + r'\)</span>'
def D(x): return r'<p><span class="math display">\[' + x.replace('<', '&lt;') + r'\]</span></p>'
HL = M(r'\Gamma^2=\tfrac12'); W = M(r'z=3+2\sqrt2')
once('Version 3.1 — 12 November 2026 — developed with AI assistance', 'Version 3.2 — 12 November 2026 — developed with AI assistance')

# ---- 25.1 (d): the exact law past the wall
once('(d) For ' + M(r'\Gamma^2>\tfrac12') + ' there is no turn; ' + M('W') + ' carries every direction to one point of the rim, at a rate that tends to '
     + M(r'\lambda=2\operatorname{arccosh}(-\tfrac12\operatorname{tr}W)') + ' per pass. ',
     '(d) For ' + M(r'\Gamma^2>\tfrac12') + ' there is no turn; ' + M('W') + ' carries every direction to one point of the rim. With ' + M('w') + ' the coordinate of a direction between the two fixed points of the rim and ' + M(r'\alpha') + ' the angle between them, each pass multiplies ' + M('w') + ' by ' + M(r'e^{-\lambda}') + ' exactly, and the distance to the far point is '
     + M(r'd_n=2\sin(\alpha/2)\lvert w_n\rvert/\sqrt{1+\lvert w_n\rvert^2+2\cos(\alpha/2)\operatorname{Re}w_n}') + ', where '
     + M(r'\cosh(\lambda/4)=R/T') + '. (e) The angle between the fixed directions is ' + M(r'\cos^2(\alpha/2)=2\Gamma^2') + ' below the wall and ' + M(r'1/(2\Gamma^2)') + ' beyond it, and ' + M(r'K=1/\sin^2(\alpha/2)') + ' on both sides, so beyond the wall ' + M(r'K=2\Gamma^2/(2\Gamma^2-1)') + ', which falls from unbounded at the wall to 2 at the rim. ')
once('(d): the limit is Exact; the rate at early passes is Open.]', '(d) and (e): Exact, <code>check1_rate.py</code>, residual below ' + M(r'10^{-35}') + ' at 50 digits on five ratios, 200 directions and 30 passes.]')
once('<tr><td>' + M('z=7') + '</td><td>9/16</td><td>none; run ' + M(r'\lambda') + ' per pass</td><td>—</td><td>—</td></tr>',
     '<tr><td>' + M('z=7') + '</td><td>9/16</td><td>none; run with ' + M(r'\cosh(\lambda/4)=9/7') + '</td><td>9</td><td>none; fixed directions at the same angle as for ' + M('z=5') + '</td></tr>')
once('<p>At the step ' + M('z=5') + ' the centre of turn lies on the sphere of radius ',
     '<p>Two steps whose coordinates multiply to one half are paired across the wall: ' + M(r'\Gamma\Gamma^{\prime}=\tfrac12') + ' gives ' + M(r'PP^{\prime}=1') + ', the same angle between fixed directions and the same ' + M('K') + '. The steps of ratio 5 and 7 are such a pair, ' + M(r'\tfrac23\cdot\tfrac34=\tfrac12') + ', with ' + M('K=9') + ' for both; '
     'one turns and the other runs, and ' + M(r'\cosh(\lambda/4)=9/7') + ' is the constant of the ratio-7 group in Two Trees §8.4.</p>\n'
     '<p>At the step ' + M('z=5') + ' the centre of turn lies on the sphere of radius ')
once('one axis alone has zero modes [Carried: Tree Chain note of 10 November, exact finite checks].</p>\n',
     'one axis alone has zero modes [Carried: Tree Chain note of 10 November, exact finite checks]. Along the word of ratio-5 steps written by the twin primes, with the arm chosen by the last digit of each pair, the frame turn of the whole product is 9.87°, 11.62°, 12.07° and 12.08° at ' + M(r'10^5') + ', ' + M(r'10^6') + ', ' + M(r'10^7') + ' and ' + M(r'2\times10^7') + ' (107,405 pairs), about an axis near ' + M('-j') + ' that is still moving; '
     'shuffling the arms gives 23° to 29° about other axes, so the turn belongs to the order of the word. It has not settled, and a run to ' + M(r'10^9') + ' is the test [Carried: <code>chain_whole_03.py</code>; the last-digit rule is that of the joint Base-10 Prime Pattern report; Open].</p>\n')

# ---- 25.3: the count of directions
once('How many directions on one circle of passes stay distinguishable after ' + M('n') + ' passes is not computed here [Open].</p>\n',
     'On the circle of passes the turn never repeats: ' + M(r'\cos\theta=-527/625') + ' at ' + M('z=5') + ', and a rational cosine other than ' + M(r'0,\pm\tfrac12,\pm1') + ' is no rational part of a turn. The gaps between the first ' + M('n') + ' passes take at most three lengths, the largest the sum of the other two. '
     'The number of directions among them that are pairwise distinguishable at threshold ' + M(r'\varepsilon') + ' in the measure ' + M(r'\lVert P-Q\rVert_F^2') + ' is capped:</p>\n'
     + D(r'N(n,\varepsilon)\ \le\ \Big\lfloor \frac{\pi}{\arcsin\!\big(\sqrt{\varepsilon/2}\,/\sin\varphi\big)}\Big\rfloor ,') +
     '<p>with no exception in 144 cases over six ratios, three directions and four thresholds, in the frame of the centre of turn and in the frame of the ball. In the frame of the ball the circle is carried to a smaller one and the cap falls with it: at ' + M('z=5') + ' the third-axis circle goes from ' + M(r'\sin^2\varphi=8/9') + ' to 8/17, and its cap at ' + M(r'\varepsilon=0.02') + ' from 29 to 21. '
     'So a direction buys a bounded number of channels and the bound is set by its angle to the loop. How fast the cap fills is not settled: within one of the cap by 2,000 passes was required and was not met in 19 of 144 cases; by 20,000 passes it is met in the frame of the centre and is two short in two cases in the frame of the ball [Exact, <code>check2_capacity.py</code>, <code>check2b_second_setup.py</code>, <code>check2c_three_distance.py</code>; the rate of filling is Open].</p>\n')

# ---- 26.1: the loop is one point of the band
once('Whether the band of the chain and the loop of the tree are one object is not tested [Open].</p>\n',
     'The two are one matrix. Taking ' + M('-W') + ', which moves directions as ' + M('W') + ' does, its logarithm is ' + M(r'(a+ib)\cdot\sigma') + ' with ' + M(r'a\cdot b=0') + ' at every ratio, which is the form of ' + M('h(k)') + ' at one ' + M('k') + ': below the wall</p>\n'
     + D(r'E=2\arccos\frac{R}{T},\qquad \frac{u}{E}=\sinh\eta=\frac{\sqrt2\,\Gamma}{\sqrt{1-2\Gamma^2}},\qquad \frac{\lvert v+we^{ik}\rvert}{E}=\cosh\eta,\qquad K_h=1+\frac{u^2}{E^2}=K_W ,') +
     '<p>to ' + M(r'10^{-59}') + ' at thirteen ratios on both sides of the wall; the wall of the loop is the exceptional point ' + M(r'u=\lvert v+we^{ik}\rvert') + ' of the chain, and ' + M('K=2') + ' is ' + M('u=E') + ', the step ' + M('z=3') + ' [Exact, <code>check3_exit_line.py</code>]. '
     'The loop is one point of the band and not its mean: ' + M(r'\langle K\rangle') + ' equals ' + M('K_W') + ' only when ' + M('E(k)') + ' does not vary across the band. Beyond the wall the loop has ' + M('K>2') + ' at every finite ratio and ' + M(r'K\to2') + ' at the rim.</p>\n')

# ---- 25.5: where the atlas holds the parts
S255 = (
 '<h2 id="where-the-atlas-holds-the-parts">25.5 Where the atlas holds the parts</h2>\n'
 '<p>The atlas of this programme (cards B1 to B207, and W1 to W9) holds the pieces of this section under other headings. They are named here so that the same result is not carried twice.</p>\n'
 '<table><thead><tr class="header"><th>Here</th><th>On the cards</th><th>Not on a card</th></tr></thead><tbody>\n'
 '<tr><td>The step and its addition law</td><td>B97, ' + M(r"\Gamma=(I'-I)/(I'+I)=\tanh(\tau/2)") + '; B189, the scalar edge with ' + M(r'E_-/E_+=\Gamma^2') + '; B100 and B101, a layer composing by ' + M('(a+x)/(1+ax)') + '</td><td>—</td></tr>\n'
 '<tr><td>Turn, Jordan block, run</td><td>the real, Jordan and complex cases of a ' + M(r'2\times2') + ' on B70, B19, B140, B199, B122; the unitary commutator and its budget on B128; a loop turning in proportion to its area on B67</td><td>the loop of two perpendicular steps, its trace, and ' + HL + ' as its Jordan point</td></tr>\n'
 '<tr><td>Centre of turn</td><td>B149 shares the unit: ' + M(r'(1+\sqrt2)^4=(3+2\sqrt2)^2') + '</td><td>the centre, its radius, and the sphere of radius ' + M(r'1/\sqrt2') + ' at ' + M('z=5') + '</td></tr>\n'
 '<tr><td>Obliqueness</td><td>B148, ' + M(r'S=1-\kappa^{-2}') + ' for an oblique idempotent, with ' + M('1-S') + ' multiplying under tensor product; B140, ' + M(r'\lVert P_\pm\rVert=1/\lvert\langle L\vert R\rangle\rvert') + '; B129, ' + M(r'\det G=1-\lvert v\rvert^2') + '; B73, the divergence</td><td>' + M(r'K=1/(1-2\Gamma^2)') + ' and its value 2 at ' + M('z=3') + '</td></tr>\n'
 '<tr><td>The signal and its bound</td><td>B211, ' + M(r'\dot\tau^2\le4gS') + ' on a scalar cut; B108, an imbalance ' + M(r'\pm\sin2gt') + '</td><td>the signal driven by the loop</td></tr>\n'
 '<tr><td>The layer</td><td>B189 and B175 for ' + M('R') + ' and ' + M('T') + '</td><td>the wall as ' + M('R=T') + ', the push ' + M('P=2R') + '; no card treats the pressure or momentum of light</td></tr>\n'
 '<tr><td>The exit line</td><td>B153, the rapidity ' + M(r'\gamma') + ' of the chain; W1 and W6</td><td>the line ' + M(r'\langle K\rangle=2') + '</td></tr>\n'
 '</tbody></table>\n'
 '<p>With ' + M(r'S=2\Gamma^2') + ' the relation of B148 is ' + M('K=1/(1-P)') + ' of §25.4. On a scalar edge equal books are the rim (B189), and B199 records that equal books on a graph are not a wall; the half line is neither of these. No card states the contrary of anything in this section.</p>\n')
once('<h1 id="the-rim-and-the-exit-line">26. The rim and the exit line</h1>', S255 + '<h1 id="the-rim-and-the-exit-line">26. The rim and the exit line</h1>')
once('<li><a href="#layers-and-the-push-of-light">25.4 Layers and the push of light</a></li>', '<li><a href="#layers-and-the-push-of-light">25.4 Layers and the push of light</a></li>\n<li><a href="#where-the-atlas-holds-the-parts">25.5 Where the atlas holds the parts</a></li>')
# speed bound: name the card beside the paper
once('[Carried: <em>The Offset Speed Limit</em> v1.1, <code>weight_between_core_checks.py</code>, kill lines C1–C7 written first].', '[Carried: <em>The Offset Speed Limit</em> v1.1 and card B211, <code>weight_between_core_checks.py</code>, kill lines C1–C7 written first].')

# ---- summary, conclusion, open questions
once('its obliqueness is ' + M(r'K=1/(1-2\Gamma^2)') + ' (§25.1).</p>', 'its obliqueness is ' + M(r'K=1/(1-2\Gamma^2)') + '. Steps with ' + M(r"\Gamma\Gamma'=\tfrac12") + ' are paired across the wall, as 5 and 7 are; the loop is one point of the band of the gain-and-loss chain (§25.1, §26.1).</p>')
once('the signal reaches the half line only if ' + M(r'\sin^2\varphi\ge\tfrac12') + ' (§25.2–25.3).</p>', 'the signal reaches the half line only if ' + M(r'\sin^2\varphi\ge\tfrac12') + ', and the number of distinguishable directions on its circle of passes is capped by that angle (§25.2–25.3).</p>')
once('Are the exit line ' + M(r'\langle K\rangle=2') + ' of the chain and ' + M('K=2') + ' of the loop one object? '
     'How many directions on one circle of passes remain distinguishable after ' + M('n') + ' passes? What is the rate of the run just past the wall? ',
     'The loop is one point of the band of the chain: what is the loop whose obliqueness is the mean over the band? How fast do the passes fill their cap of distinguishable directions? Does the frame turn of the twin-prime word settle? ')

# ---- appendices
once('<h1 id="appendix-d-test-ledger">Appendix D — Test ledger</h1> ',
     '<h1 id="appendix-d-test-ledger">Appendix D — Test ledger</h1> '
     '<p><strong>Sections 25 and 26, second round (12 November 2026).</strong> <code>check1_rate.py</code>: the exact law of the run, kill at relative residual ' + M(r'10^{-30}') + ': passed (' + M(r'3\times10^{-36}') + ' at 50 digits). The fit of the first round, which missed its line, measured the slope of ' + M(r'\log d_n') + ' over passes 1 to 4 while the denominator of ' + M('d_n') + ' was still changing; the law was not at fault. '
     'Candidate closed forms for the angle between fixed directions beyond the wall that failed: ' + M(r'\cos^2(\alpha/2)=2\Gamma^2') + ', ' + M(r'\sin^2(\alpha/2)=2\Gamma^2-1') + '. <code>check2_capacity.py</code>: the count never above the cap, kill on any excess: passed in 144 cases; within one of the cap by 2,000 passes: <strong>not met</strong> in 19 cases; second setup at 20,000 passes: met in the frame of the centre, two short in two cases in the frame of the ball. '
     '<code>check3_exit_line.py</code>: ' + M(r'a\cdot b=0') + ' and ' + M('K_h=K_W') + ', kill at ' + M(r'10^{-40}') + ': passed at thirteen ratios. The unswapped pairing of the two parts of the logarithm gives a negative ' + M('K') + ' below the wall and is not the map. '
     'The atlas was read in full for this section, cards B1 to B207 with B212 and B213 and W1 to W9; the bodies of B208 to B211 were available only in a rebuilt form and B214 to B216 not at all.</p> ')
once('<h1 id="appendix-f-scripts">Appendix F — Scripts</h1> <p>',
     '<h1 id="appendix-f-scripts">Appendix F — Scripts</h1> <p><strong>Sections 25 and 26, second round:</strong> <code>v32/check1_rate.py</code>, <code>v32/check1b_inside_alpha.py</code>, <code>v32/check2_capacity.py</code>, <code>v32/check2b_second_setup.py</code>, <code>v32/check2c_three_distance.py</code>, <code>v32/check3_exit_line.py</code>; <code>chain_whole_03.py</code>, <code>chain_turn_01.py</code>, <code>chain_turn_02.py</code> (carried).</p> <p>')
open(out, 'w', encoding='utf-8').write(t); print('v3.1 chars', n0, '-> v3.2 chars', len(t))
