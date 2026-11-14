# SCRIPT: BUILD-VOTKP-V31-01
# Builds VOTKP v3.1 from the complete v3.0 page (which holds the whole v2.9 body). Nothing is removed:
# this script inserts sections, figures, ledger rows and contents entries, and rewords three sentences of Sections 22 and 23.
import base64, re, sys
src, out = sys.argv[1], sys.argv[2]
t = open(src, encoding='utf-8').read(); n0 = len(t)
def img(p): return 'data:image/png;base64,' + base64.b64encode(open(p, 'rb').read()).decode()
def once(old, new):
    global t
    assert t.count(old) == 1, (t.count(old), old[:90]); t = t.replace(old, new)
def M(x): return r'<span class="math inline">\(' + x.replace('<', '&lt;') + r'\)</span>'
def D(x): return r'<p><span class="math display">\[' + x.replace('<', '&lt;') + r'\]</span></p>'
def FIG(p, n, cap): return '<figure><img src="' + img(p) + '" alt="Figure %d" style="max-width:100%%" /><figcaption>Figure %d. %s</figcaption></figure>\n' % (n, n, cap)
def TB(head, rows): return '<table><thead><tr class="header">' + ''.join('<th>%s</th>' % h for h in head) + '</tr></thead><tbody>\n' + ''.join('<tr>' + ''.join('<td>%s</td>' % c for c in r) + '</tr>\n' for r in rows) + '</tbody></table>\n'
HL = M(r'\Gamma^2=\tfrac12'); W = M(r'z=3+2\sqrt2')

# ------------------------------------------------------------------ title block, abstract, summary, grades
once('Version 3.0 — 12 November 2026 — developed with AI assistance', 'Version 3.1 — 12 November 2026 — developed with AI assistance')
once('Section 24 reads the walls of the knot layer.',
     'Section 24 reads the walls of the knot layer. Section 25 follows the loop of two perpendicular steps and what it does to a prepared direction of light; Section 26 states the rim and the exit line; '
     'Section 27 sets the colour of the elements beside the ionization ladder; Section 28 gives the volume law near the regular tetrahedron and the census of the invariant ' + M(r'\theta') + '.')
once('<h1 id="summary-of-results">',
     '<p>Five further results join the layers to the tree of steps, to light and to colour. A loop of two perpendicular steps of ratio ' + M('z') + ' is a turn while ' + M(r'\Gamma^2<\tfrac12') + ', one Jordan block at ' + HL + ' and a run beyond it; '
     'at the step ' + M('z=5') + ' its centre of turn lies exactly on the sphere of radius ' + M(r'1/\sqrt2') + '. Carried by that loop, a prepared direction of light gives the signal ' + M(r'c=\tfrac12[1+\sin(n\theta)\sin\varphi]') + ', whose peel coordinate is ' + M(r'\Gamma=1-2c') + '. '
     'The rim ' + M(r'\lvert\Gamma\rvert=1') + ' is reached all at once on the line where the mean obliqueness of a gain-and-loss chain equals 2. Whether an atom has a visible line from its ground state is sorted by its first ionization energy at 6.82 eV. '
     'Near the regular tetrahedron the volume of a knot complement is a closed series in the shape coordinate with a proved remainder.</p>\n'
     '<h1 id="summary-of-results">')
once('<p>Eleven results organize the answer.</p>', '<p>Sixteen results organize the answer.</p>')
once('<p>No element-to-knot correspondence is claimed. Every test ran against a condition fixed beforehand',
     '<p><strong>12. The loop of two perpendicular steps turns, locks and runs.</strong> Its trace is ' + M(r'2-4(R/T)^2') + ' with ' + M(r'R=\Gamma^2,\ T=1-R') + '. Below ' + HL + ' it is a turn about a centre at radius ' + M(r'\rho') + ', '
     + M(r'\rho^2=(1-s)/(1+s)') + ', ' + M(r's=\sqrt{1-2\Gamma^2}') + '; at ' + M('z=5') + ', ' + M(r'\rho^2=\tfrac12') + ' exactly; its obliqueness is ' + M(r'K=1/(1-2\Gamma^2)') + ' (§25.1).</p>\n'
     '<p><strong>13. Light carried by the loop is a peel signal.</strong> A prepared direction at angle ' + M(r'\varphi') + ' to the axis of the loop is read after ' + M('n') + ' passes as ' + M(r'c=\tfrac12[1+\sin(n\theta)\sin\varphi]') + ', ' + M(r'\Gamma=1-2c') + ', '
     + M(r'\dot\Gamma^2\le4g(1-\Gamma^2)') + '; the signal reaches the half line only if ' + M(r'\sin^2\varphi\ge\tfrac12') + ' (§25.2–25.3).</p>\n'
     '<p><strong>14. The rim is reached on the line of mean obliqueness two.</strong> For the gain-and-loss chain, ' + M(r'\langle K\rangle=1+u^2/(E(0)E(\pi))') + '; on ' + M(r'\langle K\rangle=2') + ' the endpoint coordinate is ' + M(r'\Gamma_{\rm end}=i') + ' and a ladder of the stated form crosses the rim all at once (§26).</p>\n'
     '<p><strong>15. The level of the ladder sorts the atoms with a visible ground line.</strong> A threshold of 6.82 eV on the first ionization energy, registered before scoring, separates them with area 0.946 under the curve; the level carries it and the first peel step does not (§27).</p>\n'
     '<p><strong>16. The volume near the regular tetrahedron is a closed series.</strong> ' + M(r'D=V_0-\tfrac{3\sqrt3}{4}\lvert G\rvert^2+\tfrac{\sqrt3}{4}\operatorname{Re}G^3+\tfrac{3\sqrt3}{16}\lvert G\rvert^4+\dots') + ' with every coefficient in closed form and remainder at most ' + M(r'0.70\,\lvert G\rvert^5') + '; '
     'summed over tetrahedra it gives the volume of 12,941 knots to a median 0.107% (§28).</p>\n'
     '<p>No element-to-knot correspondence is claimed. Every test ran against a condition fixed beforehand')
once('<strong>[Open]</strong> not yet computed.</p> <hr />',
     '<strong>[Open]</strong> not yet computed. <strong>[Carried]</strong> a result of a companion paper, repository or dated run by the same author, restated with its source and script named; not rerun for this version.</p> <hr />')

# ------------------------------------------------------------------ three rewordings in Sections 22 and 23
once('<li><strong>the rim</strong>, ' + M(r'\lvert\Gamma\rvert=1') + ': the books are equal, one half each.</li>',
     '<li><strong>the rim</strong>, ' + M(r'\lvert\Gamma\rvert=1') + ': the limit in which one of the two numbers vanishes; the books tend to equality and the share tends to one half without reaching it.</li>')
once('<p>with ' + M(r'\oplus') + ' the addition law of Theorem 15.1. So the static response reads the gap step once and the metric reads it composed with itself. ',
     '<p>with ' + M(r'\oplus') + ' the addition law of Theorem 15.1, for whole ' + M(r'k\ge1') + '; a negative power reverses the sign, ' + M(r'\Gamma(z^{-k})=-\Gamma(z^{k})') + ', and a half power reads the step once in a quantity that goes as the square root, '
     + M(r'\Gamma(z^{1/2})=\tanh(\tfrac14\ln z)') + ', which is the reflection of a matter wave at a step when ' + M('z') + ' is the ratio of kinetic energies and the wave reflects on the ratio of wavenumbers. So the static response reads the gap step once and the metric reads it composed with itself. ')
once('With the ' + M(r'\tfrac58') + ' removed, so that the core electron is unscreened, the crossing moves to ' + M('Z^*=9.47') + ', between fluorine and neon.',
     'With the ' + M(r'\tfrac58') + ' removed, so that the core electron is unscreened at first order, the crossing moves to ' + M('Z^*=9.55') + ' (9.47 if the second-order constant of the core is removed with it), between fluorine and neon.')

# ------------------------------------------------------------------ Section 22.5
S225 = (
 '<h2 id="bounds-on-the-weight-between">22.5 Bounds on the weight between, and what one book cannot see</h2>\n'
 '<p>For a positive contraction ' + M('C') + ' cut into blocks, with ' + M('X_A=C_{AB}C_{BA}') + ' the weight between and ' + M('F_A=C_{AA}-C_{AA}^2') + ' the defect of the retained block,</p>\n'
 + D(r'0\le X_A\le F_A\le\tfrac14 I,\qquad \operatorname{Tr}X_A=\lVert B\rVert_F^2,\qquad 4\operatorname{Tr}X_A\le I_G ,') +
 '<p>where ' + M('I_G') + ' is the Gaussian mutual information across the cut; for an orthogonal projector ' + M('X_A=F_A') + ', and for an oblique idempotent the defect is ' + M('BE') + ' and not ' + M(r'BB^{\dagger}') + ' '
 '[Carried: <em>Matter, Then On Down</em> and its formal edition; Lean <code>MatterGas/Boundary.lean</code>; 64 cases with least margin ' + M(r'9.1\times10^{-6}') + ']. So the number of Proposition 22.1 is bounded above by a quarter per retained mode and by a quarter of an information.</p>\n'
 '<p>The two books of Proposition 22.2 are the scalar edge of a general statement. For ' + M('H=D+A') + ' with Hermitian vertex blocks ' + M('D_i') + ' and unitary edge blocks ' + M('A_{ij}') + ',</p>\n'
 + D(r'E_-=\tfrac18\lVert[H,H^{*}]\rVert_F^2,\qquad E_+=\tfrac18\lVert H^2-H^{*2}\rVert_F^2,') +
 '<p>and the same two forms are the two ends of the pencil ' + M(r'K_\rho(u)=I-uA_\rho+u^2(\mathrm{Deg}-I)') + ' of the twisted graph zeta function: ' + M(r'\langle D,K_\rho(+1)D\rangle=E_-') + ', ' + M(r'\langle D,K_\rho(-1)D\rangle=E_+') + ' '
 '[Carried: <em>Non-Normality Is Connection Energy</em>; Lean <code>norm_sq_selfCommutator_div_eight</code> and companions; checked there to ' + M(r'1.1\times10^{-15}') + ']. On a holonomy eigenvalue ' + M(r'\lambda') + ' the books are '
 + M(r'\lvert1-\lambda\rvert^2') + ' and ' + M(r'\lvert1+\lambda\rvert^2') + ' with sum 4. Both are blind to the sign of the transport, ' + M(r'\mathrm{Ad}(-U)=\mathrm{Ad}(U)') + ': they hold the square of a trace and not the trace. '
 'The sign, the direction, the constant and the order of a route are carried by the odd record, which on a ladder is the directed sum of §19 with its defect ' + M(r'4\min(R_+,R_-)') + '.</p>\n'
 '<p>The friction weight of §19.5 is the same coordinate in a third place. With ' + M(r'u=\chi\tau\Delta') + ' the gap measured against the crossover of the bath and ' + M(r'\Gamma_u=(u-1)/(u+1)') + ',</p>\n'
 + D(r'w(\Delta)=2c(\Delta)\,\Delta=\frac{1}{\chi}\,\frac{2u}{1+u^2}=\frac{1}{\chi}\,\frac{1-\Gamma_u^2}{1+\Gamma_u^2},') +
 '<p>largest at ' + M(r'\Gamma_u=0') + ' [Exact, <code>derived_algebra.py</code>]. On a real ladder the echo weight ' + M(r'1-\Gamma^2') + ' falls as ' + M(r'\lvert\Gamma\rvert') + ' rises, so it orders the steps exactly as ' + M(r'\lvert\Gamma\rvert') + ' does; '
 'test H-01 of §15.2 separated films by the complex reflection of a metal, and on the real diameter the two readings rank alike [Exact, <code>h01_real_gamma.py</code>].</p>\n')
once('<h1 id="the-half-line-on-the-ionization-chart">', S225 + '<h1 id="the-half-line-on-the-ionization-chart">')

# ------------------------------------------------------------------ Section 24.5
S245 = (
 '<h2 id="the-turning-band-and-its-census">24.5 The turning band and its census</h2>\n'
 '<p>For the two meridians ' + M('a,b') + ' of a two-bridge knot on its real curve, with ' + M('s') + ' the eigenvalue of a meridian and ' + M('v') + ' the Riley variable,</p>\n'
 + D(r'\operatorname{tr}[a,b]=2-v\big((s-1/s)^2-v\big),\qquad k=2-\operatorname{tr}[a,b],\qquad 0<k<4\ \Longleftrightarrow\ [a,b]\ \text{turns},') +
 '<p>and ' + M(r'k\le4\sinh^4x') + ' for meridians that are steps of length ' + M('2x') + ', so that crossing axes below ' + HL + ' always give a turn [Carried: <em>Two Trees in One Ball</em>, Theorem 8.6; Lean <code>comm_trace</code>, <code>band_bound</code>]. '
 'Of the 26 two-bridge knots through eight crossings, 19 enter the band and 7 never do: ' + M('T(2,3)') + ', ' + M('T(2,5)') + ', ' + M('T(2,7)') + ', ' + M('6_3') + ', ' + M('7_5') + ', ' + M('8_7') + ', ' + M('8_8') + '. '
 'Through nine crossings, on 50 knots, the same seven and nineteen are reproduced and four more never turn: ' + M('T(2,9)') + ' and the knots of fraction 27/5, 29/9 and 55/21 [Carried: <code>firstx.py</code> at 80 digits; <code>never_turn_02.py</code>; a false entry at 40 digits on 43/5 is removed at 80]. '
 'The torus knots never turn because ' + M(r'\operatorname{tr}(ab)=2\cos((2j-1)\pi/n)<2') + ' [Lean]. The four others share neither their Alexander roots off the circle (4, 0, 4, 4) nor their direction values, which lie inside the spread of the knots that turn. '
 'As the meridian step grows, ' + M('k') + ' tends on each branch to the square of a number ' + M(r'2\cos(j\pi/n)/m') + '; why is open.</p>\n'
 '<p>The trace and the Alexander polynomial are one polynomial read two ways: ' + M(r'\Delta_K(t)=P_m(t+1/t)') + ' with ' + M('P_m') + ' the trace polynomial of the Riley curve, for instance ' + M(r'\Delta_{7_1}(t)=R_7(t+1/t)') + ' [Carried: Two Trees code and the knot handoff of 1 November 2026].</p>\n')
once('<h1 id="what-the-paper-establishes">25. What the paper establishes</h1>', S245 + 'XXNEWSECTIONSXX<h1 id="what-the-paper-establishes">29. What the paper establishes</h1>')

# ------------------------------------------------------------------ Section 25
S25 = (
 '<h1 id="the-loop-of-two-steps-and-light">25. The loop of two steps, and light carried by it</h1>\n'
 '<p>A step of ratio ' + M('z') + ' along an axis is the positive matrix ' + M(r'B=\exp(\tfrac r2\,\hat a\cdot\sigma)') + ', ' + M(r'r=\ln z') + ', whose two eigenvalues stand in the ratio ' + M('z') + '. '
 'Its peel coordinate ' + M(r'\Gamma=\tanh(r/2)') + ' is the radius at which it places the centre of the ball. Steps along one axis compose by ' + M(r'\oplus') + ' and return nothing new; this section takes the smallest word that leaves the line, two perpendicular steps out and back.</p>\n'
 '<h2 id="the-loop">25.1 The loop turns, locks and runs</h2>\n'
 + D(r'W(z)=B_iB_jB_i^{-1}B_j^{-1},\qquad R=\Gamma^2,\quad T=1-R,\qquad \operatorname{tr}W=2-4\sinh^4(r/2)=2-4\,(R/T)^2 .') +
 '<p>Reading one step as a lossless layer that returns ' + M('R') + ' and passes ' + M('T') + ', the loop is a turn while the layer passes more than it returns, and the wall ' + HL + ' is ' + M('R=T') + '.</p>\n'
 '<p><strong>Proposition 25.1 (anatomy of the loop).</strong> (a) For ' + M(r'\Gamma^2<\tfrac12') + ', ' + M('W=SUS^{-1}') + ' with ' + M('S') + ' a positive step and ' + M('U') + ' unitary: the loop is a turn through ' + M(r'\theta') + ', '
 + M(r'\cos(\theta/2)=1-2(R/T)^2') + ', about the third axis, seen from a centre on the bisector of the two arms at radius</p>\n'
 + D(r'\rho^2=\frac{1-s}{1+s},\qquad s=\sqrt{1-2\Gamma^2},\qquad \cosh\eta=\frac1s ,') +
 '<p>with ' + M(r'\eta') + ' the distance of that centre from the centre of the ball. (b) The two eigen-directions of ' + M('W') + ' are not orthogonal; their obliqueness (Petermann factor) is</p>\n'
 + D(r'K=\frac{1}{1-2\Gamma^2}=\frac{1}{T-R}=\cosh^2\eta .') +
 '<p>(c) At ' + HL + ', ' + M(r'\operatorname{tr}W=-2') + ', ' + M('(W+1)^2=0') + ' and ' + M(r'W+1\ne0') + ': one Jordan block, a full turn. (d) For ' + M(r'\Gamma^2>\tfrac12') + ' there is no turn; ' + M('W') + ' carries every direction to one point of the rim, at a rate that tends to '
 + M(r'\lambda=2\operatorname{arccosh}(-\tfrac12\operatorname{tr}W)') + ' per pass. '
 '[(a) for the trace, the turn and the fixed point: Carried, <em>Two Trees in One Ball</em> §5.3 and §8 and <code>BallJoins</code>, Lean <code>comm5_trace</code>, <code>comm5_cos</code>, <code>comm5_fixes_p</code>. The closed forms for ' + M(r'\rho') + ' and ' + M('K') + ', and (c): Exact, '
 '<code>feed_loop_01.py</code>, <code>feed_loop_02.py</code>, residuals below ' + M(r'10^{-11}') + ' on 600 ratios. (d): the limit is Exact; the rate at early passes is Open.]</p>\n'
 '<p>Three values mark the scale (Figure 37).</p>\n'
 + TB(['Step', M(r'\Gamma^2'), 'Turn per pass', M('K'), 'Centre of turn'],
      [[M('z=3'), '1/4', '0.2163 of a turn (77.88°)', '2', M(r'\rho=\sqrt2-1') + '; ' + M(r'\rho\oplus\rho=1/\sqrt2')],
       [M('z=5'), '4/9', '0.5903 of a turn (212.52°, or 147.48° the other way)', '9', M(r'\rho^2=\tfrac12') + ', point ' + M('(3,2,2,0)') + ' of the hyperboloid, distance ' + M(r'\ln(3+2\sqrt2)=1.7627')],
       [W, '1/2', 'one full turn, one Jordan block', 'unbounded', 'on the rim'],
       [M('z=7'), '9/16', 'none; run ' + M(r'\lambda') + ' per pass', '—', '—']]) +
 '<p>At the step ' + M('z=5') + ' the centre of turn lies on the sphere of radius ' + M(r'1/\sqrt2') + ', and its distance from the centre is the length of the step at the wall; ' + M(r'\rho^2=\tfrac12') + ' holds at ' + M('z=5') + ' and at no other ratio, since ' + M(r'\rho') + ' rises with ' + M('z') + ' [Exact]. '
 'The group generated by the three steps of ratio 5 is free and not discrete, and the group of ratio 7 is free and discrete; the dividing line is the wall. The ratio-5 group is not conjugate to the Lubotzky–Phillips–Sarnak group in ' + M(r'\mathrm{PGL}_2(\mathbb Q_5)') + ' (invariant 36/5 against 4/5) '
 '[Carried: Two Trees §5.1–5.3, §8.1–8.4; freeness for every whole ratio by a 2-adic argument written there and not yet in Lean].</p>\n'
 '<p>A single transfer step of trace ' + M(r'\operatorname{tr}=2\cosh\kappa') + ' has ' + M(r'\Gamma^2=(\lvert\operatorname{tr}\rvert-2)/(\lvert\operatorname{tr}\rvert+2)') + ', so the wall is ' + M(r'\lvert\operatorname{tr}\rvert=6') + ' for one step and ' + M(r'\operatorname{tr}=-2') + ' for the loop of two; these are one line read on two words '
 '[Carried: round of 11 November, <code>SNELL-SMITH-TREES-04</code>; the equivalence is arithmetic]. For three axes at once, with ' + M(r'\gamma') + ' the coordinate of the step read as a half-angle, the energy ' + M(r'E_\gamma(X)=\sum_a\lVert X-R_aXR_a^{\dagger}\rVert_F^2') + ' on traceless Hermitian ' + M(r'3\times3') + ' matrices obeys '
 + M(r'E_\gamma\ge\frac{8\gamma^2}{1+\gamma^2}\lVert X\rVert_F^2') + ': 32/13 at ' + M(r'\gamma=2/3') + ' and 72/25 at 3/4; one axis alone has zero modes [Carried: Tree Chain note of 10 November, exact finite checks].</p>\n'
 + FIG('fig37_loop.png', 37, 'The loop of two perpendicular steps. Left: radius of the centre of turn against ' + M(r'\Gamma^2') + ' of one step; it meets the sphere of radius ' + M(r'1/\sqrt2') + ' at ' + M('z=5') + '. Right: the push ' + M(r'P=2\Gamma^2') + ' on one layer and the reciprocal obliqueness ' + M('1/K=T-R') + '; they cross at ' + M('z=3') + ', and ' + M('1/K') + ' reaches zero at the wall.') +
 '<h2 id="light-on-the-peel-disk">25.2 Light on the peel disk</h2>\n'
 '<p>The equal-endpoint witness of the phase record is a two-level exchange: a state ' + M(r'(\lvert01\rangle+e^{i\varphi}\lvert10\rangle)/\sqrt2') + ' under ' + M(r'H=\kappa\sigma_x') + ' is read with share ' + M(r'c(t)=\tfrac12[1+\sin(2\kappa t)\sin\varphi]') + '. '
 'Its occupation ratio ' + M('z=(1-c)/c') + ' has the peel coordinate</p>\n'
 + D(r'\Gamma=\tanh\!\big(\tfrac12\ln\tfrac{1-c}{c}\big)=1-2c=-\sin\varphi\,\sin2\kappa t,\qquad g=\kappa^2\sin^2\varphi,\qquad \dot\Gamma^2=4g\cos^2 2\kappa t\ \le\ 4g\,(1-\Gamma^2),') +
 '<p>with slack ' + M(r'4g\cos^2\varphi\,\sin^22\kappa t') + '. The stored phase sets the reach of the signal: ' + M(r'\max\Gamma^2=\sin^2\varphi') + ', and the half line is touched only if ' + M(r'\sin^2\varphi\ge\tfrac12') + ' [Exact, <code>feed_loop_01.py</code>, 20,000 random states, no violation]. '
 'This is the scalar case of the speed limit of the offset ' + M(r'\tau=\operatorname{Tr}[\log(I-C)-\log C]') + ',</p>\n'
 + D(r'\dot\tau^2\le4gS,\qquad S=\operatorname{Tr}\big[(C(I-C))^{-1}\big],\qquad g=\tfrac12\lVert\dot P\rVert_F^2,\qquad 4gS-\dot\tau^2=\frac{4(\operatorname{Im}\bar b\dot b)^2}{(c(1-c))^2},') +
 '<p>with equality when ' + M(r'\dot P=\lambda[P,[P,F]]') + '; two preparations with one census move the offset in opposite directions at ' + M(r'\dot\tau=\pm3.4915') + ', and the phase spends speed without moving ' + M(r'\tau') + ' [Carried: <em>The Offset Speed Limit</em> v1.1, <code>weight_between_core_checks.py</code>, kill lines C1–C7 written first].</p>\n'
 '<h2 id="the-loop-drives-the-signal">25.3 The loop drives the signal</h2>\n'
 '<p>A prepared direction is a rank-one projector, a point ' + M(r'\hat n') + ' of the rim. The loop carries it to the next point of one circle on the rim, drawn about the line the loop leaves fixed. Seen from the centre of turn the passes are an even turn.</p>\n'
 '<p><strong>Proposition 25.2 (the tree feeds the phase record) [Exact].</strong> For ' + M(r'\Gamma^2<\tfrac12') + ', let ' + M(r'\varphi') + ' be the angle, in the frame of the centre of turn, between the prepared direction and the axis of the loop, and read the share across that turn. After ' + M('n') + ' passes</p>\n'
 + D(r'c_n=\tfrac12\big[1+\sin(n\theta)\,\sin\varphi\big],\qquad \kappa=\tfrac{\theta}{2}\ \text{per pass},\qquad g=\kappa^2\sin^2\varphi .') +
 '<p>For a direction along either arm of the loop ' + M(r'\sin^2\varphi=1') + '; along the third axis ' + M(r'\sin^2\varphi=2\Gamma^2') + '; on the fixed line there is no signal at any step. '
 '[<code>feed_loop_02.py</code>, <code>feed_loop_03.py</code>: residual ' + M(r'3\times10^{-14}') + ' over 40 passes and seven directions; the third-axis value on 500 ratios.]</p>\n'
 '<p>So the witness of §25.2 needs nothing attached by hand: its rate is half the turn of the loop and its stored phase is a direction. At ' + M('z=5') + ' the third-axis signal has ' + M(r'\sin^2\varphi=8/9') + ' and the body diagonal 0.301, which never reaches the half line (Figure 38). '
 'Third-axis light first reaches the half line at ' + M(r'2\Gamma^2=\tfrac12') + ', that is at ' + M('z=3') + ', where ' + M('K=2') + '. The distance of a prepared projector from the projector of the axis is ' + M(r'2\sin^2(\varphi/2)') + ', the measure of §2 of <em>The Price of a Direction</em>, '
 'so the reach of the signal is a statement about how far a direction stands from the loop. How many directions on one circle of passes stay distinguishable after ' + M('n') + ' passes is not computed here [Open].</p>\n'
 + FIG('fig38_signal.png', 38, 'The signal carried by the loop at ' + M('z=5') + ', as the peel coordinate ' + M(r'\Gamma=1-2c') + ' of the read share, for three prepared directions. The dashed lines are the half line.')
 + FIG('fig39_mixer.png', 39, 'The loop at ' + M('z=5') + ' in the ball of the ratio-5 tree. Red mesh: the sphere of radius ' + M(r'1/\sqrt2') + '. Gold circle: the points of the rim through which the loop carries a direction prepared along the third axis; small marks are whole passes. Gold line and point: the fixed line and the centre of turn.') +
 '<h2 id="layers-and-the-push-of-light">25.4 Layers and the push of light</h2>\n'
 '<p>For a thin sheet of sheet parameter ' + M(r'\zeta') + ', ' + M(r'r=-\zeta/(2+\zeta)') + ', ' + M(r't=2/(2+\zeta)') + ' and the absorbed share is ' + M(r'A=4\operatorname{Re}\zeta/\lvert2+\zeta\rvert^2\le\tfrac12') + '. At a threshold of the transverse wave the Smith coordinate is '
 + M(r'\Gamma(D)=(a-\sqrt D)/(a+\sqrt D)') + ', and below it, ' + M(r'D=-\kappa^2') + ', ' + M(r'\lvert\Gamma\rvert=1') + ' with phase ' + M(r'-2\arctan(\kappa/a)') + ': the evanescent wave is on the rim. Across an interface ' + M(r'R_1(E-V_1)\sin^2\theta_1=R_2(E-V_2)\sin^2\theta_2') + ', with a turning barrier '
 '[Carried: <em>Light Keeps the Ledger</em> 7.2 §§5.2, 8.7; Lean <code>refraction_turning_barrier</code>].</p>\n'
 '<p>The pressure of radiation across a wave-front equals the whole energy in unit of volume (Maxwell, <em>Treatise</em>, Art. 792); it is ' + M(r'H^2/8\pi') + ' whatever the permeability, and equals the magnetic energy only at ' + M(r'\mu=1') + ' [Carried: <code>maxwell-lean</code>, <code>art792_radiation_pressure</code>]. '
 'On a lossless layer returned light pushes twice and passed light not at all, so in units of the push on a full absorber</p>\n'
 + D(r'P=2R=2\Gamma^2,\qquad K=\frac{1}{1-P}=1+P+P^2+\cdots,\qquad \sin^2\varphi_{\,\text{third axis}}=P .') +
 '<p>The wall is ' + M('P=1') + ': the layer is pushed as hard as an absorber and the sum of repeated pushes no longer closes. The identities are Exact [<code>feed_loop_03.py</code>]. That ' + M('P') + ' is the pressure of light on the layers of an atom is a reading and is not tested; '
 'no derivation of light held between layers and released further down exists in this programme yet [Open].</p>\n')

# ------------------------------------------------------------------ Section 26
S26 = (
 '<h1 id="the-rim-and-the-exit-line">26. The rim and the exit line</h1>\n'
 '<p>The half line is a circle inside the chart. The rim ' + M(r'\lvert\Gamma\rvert=1') + ' is its edge, the image of ' + M(r'\operatorname{Re}z=0') + '. Three records in this programme reach or pass it, and they are stated here together [all Carried: <em>The Weight Between and the Exit Line</em> v4 and its review ledger; <em>Matter, Then On Down</em> v4; Lean <code>VOTKP/MatterDisk.lean</code>, twelve theorems].</p>\n'
 '<h2 id="the-exit-line">26.1 The exit line of a gain-and-loss chain</h2>\n'
 '<p>For the chain ' + M(r'h(k)=\begin{pmatrix}iu&v+we^{-ik}\\ v+we^{ik}&-iu\end{pmatrix}') + ' with band ' + M('E(k)') + ', the obliqueness of its eigenvectors and its mean over the band are</p>\n'
 + D(r'K(k)=1+\frac{u^2}{E(k)^2},\qquad \langle K\rangle=1+\frac{u^2}{E(0)E(\pi)},\qquad \langle K\rangle=2\iff E(0)E(\pi)=u^2\iff(w^2-v^2)^2=2u^2(w^2+v^2).') +
 '<p>With ' + M(r'\gamma=u/\sqrt{E(0)E(\pi)}') + ', ' + M(r'\langle K\rangle-1=\gamma^2') + ' (worst error ' + M(r'2.8\times10^{-14}') + ' on 20,000 random parameters). The endpoint rapidity is continued from the Hermitian chain by sending its argument to ' + M(r'i\gamma') + ':</p>\n'
 + D(r'\tau_{\rm end}=2\operatorname{artanh}(i\gamma)=2i\arctan\gamma,\qquad \Gamma_{\rm end}=i\gamma,\qquad \langle K\rangle=\sec^2\!\big(\tfrac12\operatorname{Im}\tau_{\rm end}\big).') +
 '<p>On the exit line ' + M(r'\gamma=1') + ', ' + M(r'\tau_{\rm end}=i\pi/2') + ' is finite and ' + M(r'\Gamma_{\rm end}=i') + ' lies on the rim. The real expression ' + M(r'2\operatorname{artanh}\gamma') + ', which grows without bound at ' + M(r'\gamma=1') + ', is the same line in the chart of the Hermitian chain. '
 'For the dimer ' + M('v=0') + ', ' + M(r'\theta=2\arcsin(u/w)') + ' and the exit is at ' + M('w^2=2u^2') + ', that is at ' + M(r'(u/w)^2=\tfrac12') + '.</p>\n'
 '<p><strong>Statement 26.1 (conditional).</strong> If the edge levels form a ladder ' + M(r'\varepsilon_j=j\Delta+i\theta') + ' with ' + M(r'\Delta=2\pi K^{\prime}(k)/K(k)') + ' and ' + M(r'\theta=\pi F(\arcsin s\mid k)/K(k)') + ', ' + M(r's=uw/(w^2-v^{\prime2})') + ', then the whole ladder crosses the rim at once, with ' + M(r'\theta=\pi/2') + ' exactly on ' + M(r'\langle K\rangle=2') + '. '
 'On 200 parameter points, 16 of them past the line, residual ' + M(r'8.4\times10^{-12}') + '; the derivation of the ladder itself is open.</p>\n'
 '<p>What did not hold, each in its own setup: a massive band gives ' + M(r'\langle K\rangle') + ' of 1.015 to 1.022 at exit and not 2, and its exit point moves with the filter (0.2716, 0.1692, 0.1228 at three tolerances) while the massless point is stable (0.4743); the quarter turn is not a law of rotation; the exit is not at the critical point nor at the peak of ' + M('K(k)') + '. '
 'The line ' + M(r'\langle K\rangle=2') + ' is necessary for a spatial exit in this model and not sufficient.</p>\n'
 '<p>In the loop of §25.1 the same number appears as ' + M(r'K=\cosh^2\eta') + ', so that ' + M(r'\sqrt{K-1}=\sinh\eta') + ' stands where ' + M(r'\gamma') + ' stands here, and ' + M('K=2') + ' falls at the step ' + M('z=3') + ' where the doubled radius of the centre of turn meets the half line. '
 'Whether the band of the chain and the loop of the tree are one object is not tested [Open].</p>\n'
 '<h2 id="outside-the-rim">26.2 Outside the rim</h2>\n'
 '<p>A negative ratio lies outside the rim. For a nucleus unbound by ' + M('s') + ' whose next separation energy is ' + M(r'S_{\rm next}') + ', ' + M(r'z=-S_{\rm next}/s') + ' and the distance outside is exactly</p>\n'
 + D(r'\lvert\Gamma\rvert-1=\frac{2s}{S_{\rm next}-s}\qquad(S_{\rm next}>s>0),') +
 '<p>which gives 0.0740621283, 0.2203184706 and 0.0252378072 for ' + M(r'{}^5\mathrm{He}') + ', ' + M(r'{}^5\mathrm{Li}') + ' and ' + M(r'{}^8\mathrm{Be}') + ', the values 1.074, 1.220 and 1.025 of §15.4; the rule there, close to twice the decay energy over the neighbouring step, is this formula at small ' + M('s') + ' [Lean <code>rim_distance</code>, <code>outside_rim</code>, <code>cayley_pole</code>]. '
 'Only ' + M('z=-1') + ' is the pole. Helium’s two thresholds give ' + M(r'\Gamma_0=0.377575') + ', inside.</p>\n'
 '<h2 id="three-places-called-wall">26.3 Three places</h2>\n'
 + TB(['Place', 'On the chart', 'What happens there', 'Section'],
      [['Shell wall', 'the shell part of a core-opening step, ' + M(r'(2n-1)/(n^2+(n-1)^2)'), 'the step splits into shell and screening', '§8.7'],
       ['Half line', HL + ', ' + W, 'one layer returns as much as it passes; a loop of two steps locks; a core line is crossed once', '§§22–25'],
       ['Rim', M(r'\lvert\Gamma\rvert=1') + ', ' + M(r'\operatorname{Re}z=0'), 'evanescent wave; exit of the chain; unbound nuclei beyond', '§15.4, §25.4, §26']]) )

# ------------------------------------------------------------------ Section 27
S27 = (
 '<h1 id="colour-and-the-ionization-ladder">27. Colour and the ionization ladder</h1>\n'
 '<p>The peel record of an element is its ionization ladder; its colour comes from a separate optical record. This section states what the ladder does and does not say about colour [Carried: <em>The Colours of the Elements</em>, 1 November 2026, built on the 118-element table of this paper; <em>Colour Selects the Leader</em> v1.2].</p>\n'
 '<h2 id="the-level-sorts-colour">27.1 The level sorts the visible ground line; the first step does not</h2>\n'
 '<p>A rule registered before scoring: an atom has a visible line from its ground state if its first ionization energy lies below a threshold, set on the elements ' + M('Z=1') + ' to 13 and scored on ' + M('Z=14') + ' to 118. The threshold is 6.82 eV, the area under the curve 0.946 and the accuracy 0.831 against a baseline of 0.569. '
 'The rank correlation of the outcome with ' + M(r'\ln IE_1') + ' is 0.897 in magnitude and with the first peel step ' + M(r'\Gamma_1') + ' only 0.352. This is the division of §8.5 met again: the level carries the response, the shape carries the family.</p>\n'
 '<h2 id="metals">27.2 Metals</h2>\n'
 '<p>Computed from published optical constants at normal incidence, the bulk colours of six metals that are usually called grey are not neutral: calcium ' + M('b^*=+6.6') + ', vanadium ' + M('b^*=-2.8') + ', chromium ' + M('C^*=0.4') + ', copper ' + M(r'C^*\approx18') + ', osmium ' + M('b^*') + ' from −7 to −9, iridium ' + M('b^*=+2.4') + '. '
 'The coinage metals show that the peel order and the colour order differ: by first step, silver, copper, gold; by absorption edge, silver 3.8 eV, gold 2.5 eV, copper 2.1 eV. The gold edge is at 2.46 eV (504 nm). '
 'For thin films the result depends on the data set for zinc, indium, zirconium, molybdenum, platinum and tantalum, and is left open for those six.</p>\n'
 '<h2 id="one-map-two-records">27.3 One map, two records</h2>\n'
 '<p>The balance map of colour, ' + M(r'(m-p)/(m+p)=\tanh(\tfrac12\log(m/p))') + ', is the peel coordinate, and stacked films compose by ' + M(r'\oplus') + '. On the unit circle ' + M(r'\lvert z\rvert=1') + ' the two books ' + M(r'\lvert1-z\rvert^2') + ' and ' + M(r'\lvert1+z\rvert^2') + ' have budget exactly 4: the lossless case is the rim. '
 'Under repeated passes a direction of colour converges at the rate ' + M(r'(\lvert\lambda_2\rvert/\lambda_1)^n') + '; Hilbert’s metric contracts on every pass, and Schrödinger’s line element does not (955 of 20,000 passes stretch, the worst by a factor 4.48). '
 'A match between two lights survives a change of observer exactly when the kernel of the first observer is contained in that of the second. No statement about the half line is made for colour: it does not occur in that record.</p>\n')

# ------------------------------------------------------------------ Section 28
S28 = (
 '<h1 id="volume-near-the-regular-tetrahedron">28. Volume near the regular tetrahedron, and the census of ' + r'<span class="math inline">\(\theta\)</span>' + '</h1>\n'
 '<p>The geometric layer of §13 measured volume by class. This section records what a dated run of eight claims established about volume as a function of the shapes of the tetrahedra, and about the invariant ' + M(r'\theta') + ' of Bar-Natan and van der Veen on the census of §11 '
 '[all Carried: confirmation run of 8 November 2026, second archive; each claim had its rule written in the header of its script before the run; <code>verify_numbers.py</code> recomputes 193 numbers of its report]. Six claims closed, one closed in part and one did not.</p>\n'
 '<h2 id="the-shape-coordinate">28.1 The shape coordinate and the series</h2>\n'
 '<p>With ' + M(r'w=e^{i\pi/3}') + ' the shape of the regular ideal tetrahedron, ' + M(r'G=(z-w)/(z-\bar w)') + ' maps the upper half-plane of shapes to the open unit disk, the real axis of flat shapes to ' + M(r'\lvert G\rvert=1') + ', and the substitution ' + M(r'z\mapsto1/(1-z)') + ' to multiplication of ' + M('G') + ' by a cube root of unity. '
 'The Bloch–Wigner dilogarithm, which is the volume of one tetrahedron, is then</p>\n'
 + D(r'D=V_0-\tfrac{3\sqrt3}{4}\lvert G\rvert^2+\tfrac{\sqrt3}{4}\operatorname{Re}(G^3)+\tfrac{3\sqrt3}{16}\lvert G\rvert^4+O(\lvert G\rvert^5),\qquad V_0=D(w)=1.0149416064096536\ldots') +
 '<p><strong>Proposition 28.1 (sector and closed form).</strong> The series of ' + M('D') + ' in ' + M(r'(G,\bar G)') + ' contains only terms ' + M(r'G^a\bar G^b') + ' with ' + M(r'a\equiv b \pmod 3') + ', all real, and for ' + M(r'a,b\ge1') + '</p>\n'
 + D(r'c_{ab}=\frac{\operatorname{Im}\big[(1-\omega^a)(1-\omega^b)\big]}{2ab},\qquad \omega=e^{2\pi i/3};\qquad c_{11}=-\tfrac{3\sqrt3}{4},\quad c_{22}=\tfrac{3\sqrt3}{16},\quad c_{30}=c_{03}=\tfrac{\sqrt3}{8}.') +
 '<p>The quadratic constant is ' + M(r'\lvert1-\omega\rvert^3/4') + ', the gap of the three-fold symmetry cubed; it is obtained also from the Hessian at ' + M('w') + ' and from ' + M(r'\tfrac14\cot(\pi/3)\sum\lvert c_i\rvert^2') + ' on the three angles of the tetrahedron. '
 'Checked against a ball-arithmetic series on 860 coefficient pairs through degree 40, largest difference ' + M(r'3\times10^{-34}') + '; none off the sector. The remainder after the quartic satisfies ' + M(r'\lvert R\rvert\le0.70\,\lvert G\rvert^5') + ' on ' + M(r'\lvert G\rvert\le0.9999') + ', proved in ball arithmetic on 14,806 cells and 606,204 squares; the true supremum is 0.68557.</p>\n'
 '<h2 id="the-knot-level-sum">28.2 The sum over a knot</h2>\n'
 '<p>Summed over the tetrahedra of a triangulation with nothing fitted, on 12,941 hyperbolic knots through 13 crossings:</p>\n'
 + TB(['Order kept', 'Median error', '90th percentile', 'Worst'],
      [['0: ' + M(r'\sum V_0'), '11.510%', '15.599%', '98.792% (12a803)'], ['2', '0.265%', '0.807%', '19.895% (12a803)'], ['3', '0.524%', '1.132%', '27.208% (13a3143)'], ['4', '0.107%', '0.383%', '11.376% (11a247)']]) +
 '<p>The cubic alone makes the sum worse and the quartic repairs it. The certified bound puts 11,585 of 12,942 knots below 1% and 12,907 below 5%. The error rises with the mean ' + M(r'\lvert G\rvert^2') + ' of the triangulation (rank correlation +0.750 over 198 pairs), '
 'and the canonical triangulation is worse than the default on 52 of 62 knots, against the rule set before that run. The sum is therefore an approximation with error of the order of the mean ' + M(r'\lvert G\rvert^2') + ', not a law. '
 'The median of 0.076% on 12,954 knots given in the companion paper on the vacuum disk is not reproduced by this run; the difference is not explained by the knot set, the denominator or the triangulation, and is open. '
 'Independently, 99.7% of 2,777 tetrahedra of the census lie inside ' + M(r'\lvert G\rvert^2<\tfrac12') + ' [Carried: <code>BOWL-HALF-01</code>]; that circle is on the shape disk and is not the half line of the peel chart (§23.6).</p>\n'
 '<h2 id="solutions-of-the-gluing-equations">28.3 Solutions of the gluing equations</h2>\n'
 '<p>With ' + M(r'S=\sum_j\lvert G_j\rvert^2') + ' over the tetrahedra of one solution: on eleven knots through seven crossings the geometric solution has the strictly smallest ' + M('S') + ' (11 of 11) and is the only solution with every shape inside the disk (11 of 11); every all-real solution has ' + M('S=n') + '; and ' + M('S') + ' falls as volume rises across the solutions of one knot (10 of 10, median rank correlation −0.988). '
 'For ' + M('6_1') + ' the four solutions have ' + M(r'S=0.741,\ 5.100,\ 28.949,\ 47.260') + ' and volumes ' + M(r'3.164,\ 1.415,\ -1.415,\ -3.164') + '. The knot ' + M('7_7') + ' has exactly one genuine flat solution, at ' + M('S=18.113021') + ', four tetrahedra balanced against their mirrors; the point ' + M('S=8=n') + ' on that knot is a degenerate blow-up, with shapes at 0 and infinity, and not a geometry. '
 'Only isolated solutions and one obstruction class were enumerated; that the geometric solution maximises volume is known (Francaviglia; Cho), and the reading by ' + M('S') + ' is a restatement on eleven knots.</p>\n'
 '<h2 id="two-books-of-the-jones-string">28.4 Two books of the Jones polynomial on the circle</h2>\n'
 '<p>For ' + M(r'V_K(e^{i\vartheta})') + ', let the climb be its Mahler measure and the turn the signed area it sweeps over the mean of ' + M(r'\lvert V_K\rvert^2') + '. On 2,970 knots through 12 crossings the climb follows the volume (rank correlation 0.8541; with the determinant, ' + M('R^2') + ' rises from 0.7077 to 0.8091), '
 'the size of the turn follows the size of the signature (0.8300), the signed turn opposes the signed signature (−0.9335), and neither carries the Chern–Simons invariant (−0.031, +0.053). At 13 crossings, on 9,985 knots, the first is 0.8542. A check against the literature on Mahler measure and volume is outstanding.</p>\n'
 '<h2 id="theta-on-the-census">28.5 ' + r'<span class="math inline">\(\theta\)</span>' + ' on the census, mutants and mirrors</h2>\n'
 '<p>On the 12,965 knots of §11, ' + M(r'\theta') + ' vanishes on 78; the census is certified on 66,728 cells with 38,895 comparisons, 12,887 of them nonzero, and its totals are theorems of <code>ThetaCensus.lean</code>. Against the complete tables of mutants through 13 crossings (865 groups, 1,841 positions), with one common evaluation point per group:</p>\n'
 + TB(['Groups', 'Separated', 'Partly', 'Not separated', 'Refuting invariance'],
      [['All 865', '682', '38', '145', '720 (83.2%)'], ['Pairs, 789', '644', '0', '145', '644 (81.6%)'], ['Triples, 43', '21', '22', '0', '43'], ['Four or more, 33', '17', '16', '0', '33'], ['Through 12 crossings, 91', '81', '5', '5', '86 (94.5%)']]) +
 '<p>So ' + M(r'\theta') + ' is not a mutation invariant and is silent on 145 pairs, 124 with equal value and 21 equal up to the sign of a mirror; every silent group is a pair. Both directions are stated by Bar-Natan and van der Veen; the complete count and the list are new. Equality at six points is not equality of the functions, which were not compared symbolically. '
 'The Conway and Kinoshita–Terasaka knots, alike in Alexander polynomial, signature, volume and Jones polynomial, differ in ' + M(r'\theta') + ' at all four points tried (589607/11664 against 251/2 at the first), as those authors record.</p>\n'
 '<p>The mirror rule ' + M(r'\theta(\bar K)=-\theta(K)') + ' holds at every point tested on the two-strand torus knots ' + M('T(2,n)') + ', ' + M(r'n=3,\dots,11') + ': 35 of 35 mirror sums vanish and 35 of 35 same-handed sums do not, with 21 of 21 crossing-switch controls detected; the first evaluator failed its calibration on the trefoil by an omitted term, stopped as declared, and was repaired. '
 'The 21 sign cases of the census reproduce from the original diagrams. Because ' + M(r'\theta') + ' is additive and odd under mirror, it cannot see the shortcut by which ' + M(r'K\#\bar K') + ' unknots faster than its parts, so a bound on unknotting number drawn from it is circular there.</p>\n'
 '<p>The remaining claims of the run: the substitution identities of §28.1 are exact; the circuit polynomial at 1 equals the determinant on 6,729 of 6,729 alternating knots after a correction of the adjacency; and for the windings of the extended dilogarithm the continuous part of the defect is nonzero on 8 of 8 knots while the integers are not verified [Open].</p>\n')

once('XXNEWSECTIONSXX', S25 + S26 + S27 + S28)

# ------------------------------------------------------------------ conclusion, open questions
once('decided in every tabulated case by the module (§24).</p>',
     'decided in every tabulated case by the module (§24). A loop of two perpendicular steps is a turn below the half line, a single Jordan block on it and a run beyond; at the step of ratio 5 its centre of turn lies on the sphere of radius ' + M(r'1/\sqrt2') + ', and the signal of a prepared direction carried by it is a peel coordinate whose reach is set by its angle to the loop (§25). '
     'The rim is reached where the mean obliqueness of the gain-and-loss chain is two, conditionally on the form of its ladder (§26). The level of the ladder sorts the atoms with a visible ground line at 6.82 eV, and the first step does not (§27). Near the regular tetrahedron the volume is a closed series with a proved remainder, and its sum over a knot is an approximation of stated size (§28).</p>')
once('<h2 id="remaining-open-questions">25.1 Remaining open questions</h2> <p>',
     '<h2 id="remaining-open-questions">29.1 Remaining open questions</h2> <p>Is the push ' + M(r'P=2\Gamma^2') + ' the pressure of light on a layer of an atom, and what holds light between layers and releases it further down? Are the exit line ' + M(r'\langle K\rangle=2') + ' of the chain and ' + M('K=2') + ' of the loop one object? '
     'How many directions on one circle of passes remain distinguishable after ' + M('n') + ' passes? What is the rate of the run just past the wall? Can the ladder of Statement 26.1 be derived? Why is the median of the tetrahedral sum 0.107% and not 0.076%? What do the 145 silent mutant pairs share? What do the knots that never turn share? ')

# ------------------------------------------------------------------ appendices D and F, contents
once('<h1 id="appendix-d-test-ledger">Appendix D — Test ledger</h1> ',
     '<h1 id="appendix-d-test-ledger">Appendix D — Test ledger</h1> '
     '<p><strong>Sections 22.5 and 25 (12 November 2026).</strong> Each script states before its run why the check decides the claim and the condition that would kill it. '
     '<code>feed_loop_01.py</code>: ' + M(r'\Gamma=1-2c') + ', the bound and the half-line reach, kill at residual above ' + M(r'10^{-12}') + ' or any violation in 20,000 states: passed. Loop trace, kill at ' + M(r'10^{-10}') + ': passed on 400 ratios. Jordan block at the wall: passed. '
     '<code>feed_loop_02.py</code>: ' + M('K=1/(1-2\\Gamma^2)') + ', the radius of the centre of turn, ' + M(r'\rho^2=\tfrac12') + ' at ' + M('z=5') + ' only, ' + M('W=SUS^{-1}') + ', the loop-fed signal, each with kill at ' + M(r'10^{-9}') + ': passed, worst ' + M(r'5\times10^{-11}') + '. '
     '<code>feed_loop_03.py</code>: ' + M('K=1/(T-R)') + ', the third-axis angle, the side of the half-line sphere, the circle of passes: passed. The rate of the run past the wall against ' + M(r'\lambda') + ' with kill at ' + M(r'10^{-6}') + ' on passes 1 to 4: <strong>not met</strong> (differences ' + M(r'3\times10^{-2}') + ', ' + M(r'5\times10^{-3}') + ', ' + M(r'10^{-4}') + ' at ' + M(r'z=6.5,\ 8,\ 16.8') + '); the rate is stated as a limit only. '
     '<code>derived_algebra.py</code> (32 symbolic and numeric checks) and <code>h01_real_gamma.py</code>: passed. '
     'The scripts behind Sections 23 and 24 were rerun on 12 November and reproduce every printed number; <code>ladder_wall_01.py</code> counts 5,737 steps and 694 closed-core openings where the census of §23 counts 5,714 and 675, the difference being the 23 non-adjacent pairs and the count set, and the eight crossings agree under both. '
     'The helium-sequence constants of §23.4 agree with the values attributed to Baker et al. (1990) and Yan, Tambasco and Drake (1998) in two later papers; the originals were not read. A fit to the thresholds of ' + M('Z=6') + ' to 20 does not fix either constant (0.04 to 0.14 and 0.18 to 0.24 against 0.1577 and 0.2505).</p> '
     '<p><strong>Carried results (Sections 22.5, 24.5 and 25 to 28).</strong> Results graded [Carried] were taken from the files named beside them and were not rerun here. Their own records of what failed: in the offset checks, a central difference missed its ' + M(r'10^{-6}') + ' line at ' + M(r'3.1\times10^{-6}') + ' and was replaced by Richardson extrapolation at ' + M(r'7\times10^{-9}') + '; '
     'in the exit-line scripts the massive band, the quarter-turn law and the independence of nine gap blocks were killed in the setups of §26.1; in the run of 8 November the rule that the canonical triangulation gives the smaller error was not met and the windings closed only in part; in the mirror tests the first evaluator failed calibration and was repaired. '
     'Of the 140 theorems of Appendix B, the Lean sources were read and counted for this version and contain no <code>sorry</code> and no added axiom; they were not compiled here. Propositions 22.1 to 22.3, 24.1, 25.1 and 25.2 are not yet in Lean.</p> ')
once('<h1 id="appendix-f-scripts">Appendix F — Scripts</h1> <p>',
     '<h1 id="appendix-f-scripts">Appendix F — Scripts</h1> <p><strong>Sections 22.5 and 25:</strong> <code>v31/feed_loop_01.py</code>, <code>v31/feed_loop_02.py</code>, <code>v31/feed_loop_03.py</code> (the loop, its centre of turn and obliqueness, the loop-fed signal, the push on a layer), <code>v31/feed_math.js</code> with <code>v31/feed_math_test.js</code> (the same mathematics as run by the interactive page), '
     '<code>v31/derived_algebra.py</code>, <code>v31/h01_real_gamma.py</code>, <code>v31/figs_v31.py</code> (Figures 37 and 38). <strong>Carried, by source:</strong> <em>Two Trees in One Ball</em> code and Lean (<code>band.py</code>, <code>firstx.py</code>, <code>asym.py</code>, <code>PeelTrees3</code>, <code>PeelTrees4</code>, <code>BallJoins.lean</code>); <code>never_turn_01</code> to <code>05</code>; <code>tree_chain_bridge_check.py</code>; <code>SNELL-SMITH-TREES-04</code>; '
     '<em>The Offset Speed Limit</em> (<code>weight_between_core_checks.py</code>, <code>c4_richardson.py</code>); <em>The Weight Between and the Exit Line</em> v4 (<code>s05</code> to <code>s18</code>, <code>g2_b153_exitline.py</code>, <code>VOTKP/MatterDisk.lean</code>); the run of 8 November (<code>c2_*</code>, <code>c3_*</code>, <code>c5</code> to <code>c8</code>, <code>verify_numbers.py</code>, <code>ThetaCensus.lean</code>); the mirror tests of 1 November; <code>maxwell-lean</code>; <code>BOWL-HALF-01</code>.</p> <p>')
TOC = ('<li><a href="#the-loop-of-two-steps-and-light">25. The loop of two steps, and light carried by it</a>\n<ul>\n<li><a href="#the-loop">25.1 The loop turns, locks and runs</a></li>\n<li><a href="#light-on-the-peel-disk">25.2 Light on the peel disk</a></li>\n'
       '<li><a href="#the-loop-drives-the-signal">25.3 The loop drives the signal</a></li>\n<li><a href="#layers-and-the-push-of-light">25.4 Layers and the push of light</a></li>\n</ul></li>\n'
       '<li><a href="#the-rim-and-the-exit-line">26. The rim and the exit line</a>\n<ul>\n<li><a href="#the-exit-line">26.1 The exit line of a gain-and-loss chain</a></li>\n<li><a href="#outside-the-rim">26.2 Outside the rim</a></li>\n<li><a href="#three-places-called-wall">26.3 Three places</a></li>\n</ul></li>\n'
       '<li><a href="#colour-and-the-ionization-ladder">27. Colour and the ionization ladder</a></li>\n<li><a href="#volume-near-the-regular-tetrahedron">28. Volume near the regular tetrahedron, and the census of θ</a></li>\n')
once('<li><a href="#what-turns-and-what-climbs">24.4 What turns and what climbs</a></li>\n</ul></li>\n<li><a href="#what-the-paper-establishes" id="toc-what-the-paper-establishes">25. What the paper establishes</a>\n<ul>\n<li><a href="#remaining-open-questions" id="toc-remaining-open-questions">25.1 Remaining open questions</a></li>',
     '<li><a href="#what-turns-and-what-climbs">24.4 What turns and what climbs</a></li>\n<li><a href="#the-turning-band-and-its-census">24.5 The turning band and its census</a></li>\n</ul></li>\n' + TOC +
     '<li><a href="#what-the-paper-establishes" id="toc-what-the-paper-establishes">29. What the paper establishes</a>\n<ul>\n<li><a href="#remaining-open-questions" id="toc-remaining-open-questions">29.1 Remaining open questions</a></li>')
import re as _re
m=_re.search(r'<li><a href="#what-the-ladder-fixes"[^>]*>22\.4[^<]*</a></li>', t); assert m and t.count(m.group(0))==1
t=t.replace(m.group(0), m.group(0)+'\n<li><a href="#bounds-on-the-weight-between">22.5 Bounds on the weight between, and what one book cannot see</a></li>')
open(out, 'w', encoding='utf-8').write(t); print('v3.0 chars', n0, '-> v3.1 chars', len(t))
