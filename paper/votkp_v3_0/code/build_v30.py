# SCRIPT: BUILD-VOTKP-V30-01
# Builds VOTKP v3.0 from the complete v2.9 page (13 Oct 2026). The v2.9 body is kept whole;
# this script only inserts new sections, figures, ledger rows and contents entries.
import base64, re, sys

src, out = sys.argv[1], sys.argv[2]
t = open(src, encoding='utf-8').read()
n0 = len(t)

def img(path):
    return 'data:image/png;base64,' + base64.b64encode(open(path, 'rb').read()).decode()

def once(old, new):
    global t
    assert t.count(old) == 1, (t.count(old), old[:80])
    t = t.replace(old, new)

def M(x): return r'<span class="math inline">\(' + x + r'\)</span>'
def D(x): return r'<p><span class="math display">\[' + x + r'\]</span></p>'

# ------------------------------------------------------------------ title block
once('Version 2.9 — 13 October 2026 — developed with AI assistance',
     'Version 3.0 — 12 November 2026 — developed with AI assistance')
once('every numerical result carries the grade stated in the Abstract.</p>\n</div>',
     'every numerical result carries the grade stated in the Abstract. Section 22 places the peel step inside the projector geometry; '
     'Section 23 draws the half line ' + M(r'\Gamma^2=\tfrac12') + ' on the ionization chart of all 118 elements; Section 24 reads the walls of the knot layer.</p>\n</div>')

# ------------------------------------------------------------------ abstract
once('<h1 id="summary-of-results">',
     '<p>Three further results close the gaps between the layers. The peel step is the edge of two books of one coupling: on a single edge '
     + M(r'E_-/E_+=\Gamma^2') + ', the weight across the peel is the zero-lag memory, and the gap powers of projector geometry read the same step composed with itself. '
     'On the ionization chart the half line ' + M(r'\Gamma^2=\tfrac12') + ' is crossed exactly once along each core-opening line; from sodium to caesium the screening part of the first step is one number, '
     'a charge ratio of 2.02 to 2.05, so the alkali metals approach the line by their shell part alone and caesium is the last element past it. '
     'In the knot layer a double root of the signature is a touch or a crossing according to whether the knot’s own turning operator has one Jordan block or two, on all 575 double roots tabulated.</p>\n'
     '<h1 id="summary-of-results">')

# ------------------------------------------------------------------ summary
once('<p>Eight results organize the answer.</p>', '<p>Eleven results organize the answer.</p>')
SUM = (
 '<p><strong>9. A peel step is an edge of two books.</strong> For two positive numbers ' + M('d_i,d_j') + ' on one edge, the connection energy and its opposite are '
 + M(r'E_-=(d_i-d_j)^2') + ' and ' + M(r'E_+=(d_i+d_j)^2') + ', and their ratio is the square of the peel coordinate, ' + M(r'E_-/E_+=\Gamma^2') + '. '
 'The half line ' + M(r'\Gamma^2=\tfrac12') + ' is the edge on which the first book holds one third of the budget; the rim is the edge on which the books are equal (§22).</p>\n'
 '<p><strong>10. The half line sorts the ionization chart.</strong> Eight of 5,714 steps lie past it: the first steps of Li, Na, K, Rb and Cs and the K-shell openings of Be, B and C. '
 'Each core-opening line crosses it once. The screening part of the alkali first step is the same from sodium to caesium, and those five atoms hold five of the six largest optical phases at 1.5, 2.0 and 2.5 eV, '
 'where reflected power does not separate them (§23).</p>\n'
 '<p><strong>11. A wall in the knot layer is a nilpotent.</strong> Of 575 double roots of the signature on the unit circle, 376 touch zero and turn back and 199 are two independent levels; '
 'the split is decided by the second Alexander polynomial in every case, and on 198 Seifert matrices the touch is one Jordan block of size two (§24).</p>\n')
once('<p>No element-to-knot correspondence is claimed. Every test ran against', SUM + '<p>No element-to-knot correspondence is claimed. Every test ran against')

# ------------------------------------------------------------------ new sections 22-24
S22 = (
 '<h1 id="the-peel-inside-the-projector-geometry">22. The peel inside the projector geometry</h1>\n'
 '<p>The peel coordinate of §8 was introduced on a list of thresholds. This section states where it lives in the geometry of a retained subspace, so that the chart of §8, the addition law of §15.2, '
 'the split of §8.7 and the channel record of §20.3 are read as one construction. Every identity below is finite algebra; each is graded.</p>\n'
 '<h2 id="a-peel-is-a-projector-move">22.1 A peel is a projector move</h2>\n'
 '<p>Let ' + M('P') + ' project onto what is retained and ' + M('1-P') + ' onto what is peeled, and write a self-adjoint operator in those blocks,</p>\n'
 + D(r'H=\begin{pmatrix}A&B\\ B^{\dagger}&D\end{pmatrix},\qquad PH(1-P)=B .') +
 '<p><strong>Proposition 22.1 (one number, three readings) [Theorem, elementary].</strong> The following are equal:</p>\n'
 + D(r'E_B=\lVert PH(1-P)\rVert_F^2=\lVert B\rVert_F^2,\qquad \tfrac12\lVert[H,P]\rVert_F^2,\qquad \operatorname{Tr}K(0),\quad K(t)=B\,e^{-iDt}B^{\dagger}.') +
 '<p><em>Proof.</em> ' + M(r'[H,P]=\begin{pmatrix}0&-B\\ B^{\dagger}&0\end{pmatrix}') + ', whose squared Frobenius norm is ' + M(r'2\lVert B\rVert_F^2') + '; and ' + M(r'K(0)=BB^{\dagger}') + '. ∎</p>\n'
 '<p>The first is the weight between a subspace and its complement; the second is the squared speed of the projector when ' + M('H') + ' generates its motion; the third is the zero-lag value of the memory kernel of §20.3.3. '
 'What a peel keeps is therefore stated without reference to a coordinate: the retained block ' + M('A') + ', the projector ' + M('P') + ', and the coupling ' + M('B') + ' through which the peeled part still acts. '
 'The traits of the title are the readings of that triple that survive when ' + M('D') + ' is no longer observed.</p>\n'
 '<h2 id="the-peel-step-is-an-edge-of-two-books">22.2 The peel step is an edge of two books</h2>\n'
 '<p>Take one edge joining two vertices that carry positive numbers ' + M('d_i') + ' and ' + M('d_j') + '. The connection energy of the edge and its opposite are</p>\n'
 + D(r'E_-=(d_i-d_j)^2,\qquad E_+=(d_i+d_j)^2,\qquad E_-+E_+=2\,(d_i^2+d_j^2),\qquad E_+-E_-=4\,d_id_j .') +
 '<p><strong>Proposition 22.2 (the edge coefficient is a peel step) [Theorem, elementary].</strong> With ' + M('z=d_i/d_j') + ' and ' + M(r'\Gamma=\tanh(\tfrac12\ln z)') + ',</p>\n'
 + D(r'\frac{d_i-d_j}{d_i+d_j}=\Gamma,\qquad \frac{E_-}{E_+}=\Gamma^2,\qquad \frac{E_-}{E_-+E_+}=\frac{\Gamma^2}{1+\Gamma^2},\qquad \frac{E_+-E_-}{E_+}=1-\Gamma^2 .') +
 '<p>The last quantity is the echo weight ' + M(r'1-\Gamma^2') + ' met in test H-01 of §15.2; it is the part of the larger book that the smaller does not cancel. With ' + M('d') + ' the successive ionization energies of an element, the reflection atlas of §8 is the atlas of this edge coefficient along the ladder, '
 'and the budget ' + M('E_-+E_+') + ' depends on the two thresholds but not on how it is shared. Two values of the share mark two circles on the chart:</p>\n'
 '<ul>\n<li><strong>the half line</strong>, ' + M(r'\Gamma^2=\tfrac12') + ', ' + M(r'z=3+2\sqrt2') + ': ' + M('E_+=2E_-') + ', the first book holds one third of the budget;</li>\n'
 '<li><strong>the rim</strong>, ' + M(r'\lvert\Gamma\rvert=1') + ': the books are equal, one half each.</li>\n</ul>\n'
 '<p>These are different circles. Statements about the rim (the mass-5 and mass-8 nuclei of §15 lie beyond it) and statements about the half line (§23) are not interchangeable.</p>\n'
 '<h2 id="gap-powers-compose-the-step">22.3 Gap powers compose the step</h2>\n'
 '<p>When the two numbers on the edge are two gaps ' + M(r'\Delta_1<\Delta_2') + ' seen from one retained level with equal coupling, the readings of the projector geometry weight them by powers of the gap: '
 'the metric by ' + M(r'\Delta^{-2}') + ', the static response by ' + M(r'\Delta^{-1}') + ', the commutator norm by ' + M(r'\Delta^{2}') + '.</p>\n'
 '<p><strong>Proposition 22.3 (the gap-power ladder) [Theorem, elementary].</strong> The contrast between the two transitions at gap power ' + M('k') + ' is the peel coordinate of ' + M('z^{k}') + ', and</p>\n'
 + D(r'\Gamma(z^{k})=\tanh\!\big(\tfrac{k}{2}\ln z\big)=\underbrace{\Gamma\oplus\Gamma\oplus\cdots\oplus\Gamma}_{k\ \text{times}} ,') +
 '<p>with ' + M(r'\oplus') + ' the addition law of Theorem 15.1. So the static response reads the gap step once and the metric reads it composed with itself. '
 'The split of Theorem 8.2 is the same statement on charges: an ionization energy goes as the square of an effective charge, so the screening part of a step is the charge step taken twice,</p>\n'
 + D(r'\Gamma^{\rm scr}=r\oplus r,\qquad r=\frac{Z_c-Z_v}{Z_c+Z_v},') +
 '<p>where ' + M('Z_v') + ' and ' + M('Z_c') + ' are the effective charges before and after the step. Checked on every core-opening step of the archive to ' + M(r'2\times10^{-16}') + ' [Exact, <code>shell_screen_04.py</code>].</p>\n'
 '<h2 id="what-the-ladder-fixes">22.4 What the ladder fixes, and what the geometry adds</h2>\n'
 '<p>Proposition 19.3 shows that a positive ladder, even with its full directed record, does not determine the path length of a retained spectral projector: the same eigenvalues are realized by a constant projector and by rotating ones. '
 'Read in the order of this section, that is a statement of priority: the geometry of the retained subspace comes first, and the threshold ladder is the real diameter of its chart. '
 'Order, phase and turning are carried by the parts of the triple ' + M('(A,P,B)') + ' that the diameter cannot hold; §23.5 gives one case in the elements where a phase reading separates what an even reading does not.</p>\n')

S23 = (
 '<h1 id="the-half-line-on-the-ionization-chart">23. The half line on the ionization chart</h1>\n'
 '<p>The circle ' + M(r'\Gamma^2=\tfrac12') + ' is where a loop of two equal perpendicular steps stops closing as a pure turn: its trace is ' + M(r'2-4\sinh^4(\tau/2)') + ', which reaches ' + M('-2') + ' at ' + M(r'z=3+2\sqrt2') + '. '
 'On the ionization chart every step is real and lies on one diameter, so the circle meets the chart in a single point, ' + M(r'\Gamma=1/\sqrt2') + '. This section records which steps of the 118-element archive lie past that point.</p>\n'
 '<h2 id="eight-steps">23.1 Eight steps</h2>\n'
 '<p>Of 5,714 adjacent steps, eight lie past the half line [Exact, <code>esr_check_01.py</code>, <code>ladder_wall_01.py</code>]: the first steps of Li, Na, K, Rb and Cs, and the steps that open the helium core of Be⁺, B²⁺ and C³⁺. '
 'All eight open a closed core. The converse fails: of the 675 adjacent steps that open a closed shell or subshell (remaining electron counts 2, 10, 18, 28, 36, 46, 54, 60, 68, 78, 86), only these eight cross. '
 'The line is selective, and it is not a marker of shell openings.</p>\n'
 '<h2 id="one-crossing-per-core-line">23.2 One crossing on each core line</h2>\n'
 '<p>Follow the step that opens a given core along its isoelectronic line, from the alkali-like atom to higher charge. The registered condition was more than one crossing on any line; no line crosses more than once [Exact, <code>iso_cross_03.py</code>].</p>\n'
 '<table><thead><tr class="header"><th>Core</th><th>Last step past the line</th><th>First step inside</th><th>High-charge limit ' + M('(n/(n-1))^2') + '</th></tr></thead><tbody>\n'
 '<tr class="odd"><td>He</td><td>C³⁺, ' + M('z=6.080') + '</td><td>N⁴⁺, ' + M('z=5.640') + '</td><td>4</td></tr>\n'
 '<tr class="even"><td>Ne</td><td>Na, 9.201</td><td>Mg⁺, 5.330</td><td>2.25</td></tr>\n'
 '<tr class="odd"><td>Ar</td><td>K, 7.286</td><td>Ca⁺, 4.289</td><td>1.78</td></tr>\n'
 '<tr class="even"><td>Kr</td><td>Rb, 6.533</td><td>Sr⁺, 3.888</td><td>1.56</td></tr>\n'
 '<tr class="odd"><td>Xe</td><td>Cs, 5.947</td><td>Ba⁺, 3.583</td><td>1.44</td></tr>\n'
 '<tr class="even"><td>Rn</td><td>none</td><td>Fr, 5.50</td><td>1.36</td></tr>\n</tbody></table>\n'
 '<p>Every high-charge limit is inside the line, so a line that starts past it must cross. Period 2 is the only period in which the crossing falls in the middle of the row, between carbon and nitrogen; in periods 3 to 6 it falls directly after the alkali metal; in period 7 the line is never reached.</p>\n'
 '<figure> <img src="' + img('fig35_core_lines.png') + '" alt="Figure 35. The step that opens each closed core, followed along its isoelectronic line. Each line crosses the half line once and falls toward its high-charge limit." /> '
 '<figcaption aria-hidden="true"><strong>Figure 35.</strong> The step that opens each closed core, followed along its isoelectronic line (log scale). The dashed line is the half line ' + M(r'z=3+2\sqrt2') + '; dotted lines are the high-charge limits ' + M('(n/(n-1))^2') + ' of Theorem 8.2. '
 'Each line crosses once. The helium-core line crosses between C³⁺ and N⁴⁺; the others cross directly after the alkali metal; francium starts inside.</figcaption> </figure>\n'
 '<h2 id="the-alkali-charge-ratio">23.3 The alkali metals reach the line by their shell part alone</h2>\n'
 '<p>By Theorem 8.2 the first step of an alkali metal is its shell part composed with its screening part, and by Proposition 22.3 the screening part is the charge step taken twice. In charges the half line reads</p>\n'
 + D(r'\frac{Z_c}{Z_v}=(1+\sqrt2)\,\frac{n-1}{n},') +
 '<p>a wall ratio that rises with ' + M('n') + ' toward the silver ratio ' + M(r'1+\sqrt2') + '. This restates the line; it predicts nothing by itself. The content is in the measured charge ratios [Exact, <code>shell_screen_04.py</code>]:</p>\n'
 '<table><thead><tr class="header"><th>Element</th><th>' + M('n') + '</th><th>' + M('Z_v') + '</th><th>' + M('Z_c') + '</th><th>' + M('Z_c/Z_v') + '</th><th>Wall ratio</th><th>Margin</th><th>' + M(r'\Gamma^{\rm scr}') + '</th></tr></thead><tbody>\n'
 '<tr class="odd"><td>Li</td><td>2</td><td>1.259</td><td>2.358</td><td>1.873</td><td>1.207</td><td>+0.666</td><td>0.556</td></tr>\n'
 '<tr class="even"><td>Na</td><td>3</td><td>1.844</td><td>3.729</td><td>2.022</td><td>1.610</td><td>+0.413</td><td>0.607</td></tr>\n'
 '<tr class="odd"><td>K</td><td>4</td><td>2.259</td><td>4.574</td><td>2.024</td><td>1.811</td><td>+0.214</td><td>0.608</td></tr>\n'
 '<tr class="even"><td>Rb</td><td>5</td><td>2.770</td><td>5.665</td><td>2.045</td><td>1.931</td><td>+0.113</td><td>0.614</td></tr>\n'
 '<tr class="odd"><td>Cs</td><td>6</td><td>3.210</td><td>6.523</td><td>2.032</td><td>2.012</td><td>+0.020</td><td>0.610</td></tr>\n'
 '<tr class="even"><td>Fr</td><td>7</td><td>3.830</td><td>7.699</td><td>2.010</td><td>2.069</td><td>−0.059</td><td>0.603</td></tr>\n</tbody></table>\n'
 '<p><strong>Result [Exact].</strong> From sodium to caesium the charge ratio is one number: 2.022 to 2.045, a spread of 1.1% against a registered limit of 2%. §8.7 showed that the jump in effective charge grows down the column (1.10, 1.88, 2.31, 2.89, 3.31); '
 'the ratio does not grow. The screening part of the alkali first step is therefore constant, ' + M(r'\Gamma^{\rm scr}=0.607') + ' to ' + M('0.614') + ', and the whole descent of the alkali metals toward the half line is carried by the shell part ' + M(r'\Gamma^{\rm sh}=\tfrac{5}{13},\tfrac{7}{25},\tfrac{9}{41},\tfrac{11}{61}') + '. '
 'A fixed ratio near 2.03 meets the rising wall ratio between ' + M('n=6') + ' and ' + M('n=7') + ': caesium is past the line by 2% in ' + M('z') + ' (' + M(r'\Gamma^2=0.507') + ') and is the last element past it. Lithium stands apart because its core is the two-electron core.</p>\n'
 '<figure> <img src="' + img('fig36_charge_ratio.png') + '" alt="Figure 36. The charge ratio across the first step of each alkali metal against the wall ratio of the half line." /> '
 '<figcaption aria-hidden="true"><strong>Figure 36.</strong> The charge ratio ' + M('Z_c/Z_v') + ' across the first step of each alkali metal (gold) against the wall ratio of the half line (dashed), which rises toward ' + M(r'1+\sqrt2') + '. '
 'Sodium to caesium lie in one band; the wall ratio passes through the band between ' + M('n=6') + ' and ' + M('n=7') + '. The francium point (open) rests on a semi-empirical second threshold and carries its stated margin.</figcaption> </figure>\n'
 '<p><strong>Francium.</strong> The archived second ionization energy of francium is ' + M(r'22.4\pm1.9') + ' eV, semi-empirical, and the half line lies inside that margin: francium is past the line if and only if the ionization energy of Fr⁺ exceeds ' + M(r'(3+2\sqrt2)\,IE_1=23.74') + ' eV. '
 'If francium kept the band of Na to Cs its second threshold would be 22.67 to 23.18 eV, inside the line. That reading is an extrapolation from four atoms, and §8.8 records why the bottom of this column departs from its trend (test T05, the filled f shell and the contraction of the 7s shell); '
 'the archived ratio, 2.010, already sits below the band. A measured ionization energy of Fr⁺ decides it. [Open]</p>\n'
 '<h2 id="the-five-eighths-places-the-crossing">23.4 The five-eighths places the carbon–nitrogen crossing</h2>\n'
 '<p>On the helium-core line both thresholds have the series of §15.10. In Hartree, to second order in ' + M('1/Z') + ',</p>\n'
 + D(r'IE_{\rm core}=\frac{Z^2}{2}-\frac58\,Z+0.157666,\qquad IE_{\rm val}=\frac{Z^2}{8}-\frac{290}{729}\,Z+0.250500 ,') +
 '<p>the first for removing a 1s electron from the two-electron ion, the second for removing the 2s electron from the three-electron ion (' + M(r'\tfrac{290}{729}=2F^0(1s,2s)-G^0(1s,2s)') + '). '
 'With no fitted quantity the ratio of the two reproduces the measured step from boron to neon within 0.55%, and crosses the half line at ' + M('Z^*=6.538') + '; the measured line interpolates to 6.57 [Reproduction, <code>shell_screen_04.py</code>; the second-order constants are cited, not read at source]. '
 'With the ' + M(r'\tfrac58') + ' removed, so that the core electron is unscreened, the crossing moves to ' + M('Z^*=9.47') + ', between fluorine and neon. The first-order terms alone give 7.41. '
 'So the mid-row position of the crossing in period 2 is set by the screening of one 1s electron by the other, the same ' + M(r'\tfrac58') + ' that closes the last step of every ladder in §15.10, together with the second-order terms.</p>\n'
 '<h2 id="the-optical-phase-finds-the-same-five-atoms">23.5 The optical phase finds the same five atoms</h2>\n'
 '<p>The atomic chart carries no phase (Theorem 8.1). The optical record of the same elements does. For the 41 elements with tabulated optical constants covering the visible, take the reflection ' + M(r'\Gamma=(1-N)/(1+N)') + ' at a fixed photon energy and read two things: its angle away from the real axis, and the reflected power ' + M(r'\lvert\Gamma\rvert^2') + '. '
 'The registered condition was a one-sided rank-sum probability above 0.01 for the five atoms past the half line against the rest, or a change of direction between energies [Exact, <code>phase_ladder_02.py</code>].</p>\n'
 '<table><thead><tr class="header"><th>Photon energy</th><th>Phase: Cs, Rb, K, Na, Li (degrees)</th><th>Largest phase among the other 36</th><th>' + M('p') + ', phase</th><th>' + M('p') + ', ' + M(r'\lvert\Gamma\rvert^2') + '</th></tr></thead><tbody>\n'
 '<tr class="odd"><td>1.5 eV</td><td>56.5, 50.0, 44.4, 31.3, 28.5</td><td>28.6 (Ca)</td><td>' + M(r'2.7\times10^{-6}') + '</td><td>0.091</td></tr>\n'
 '<tr class="even"><td>2.0 eV</td><td>78.6, 69.1, 61.2, 42.5, 38.4</td><td>39.5 (Ca)</td><td>' + M(r'2.7\times10^{-6}') + '</td><td>0.099</td></tr>\n'
 '<tr class="odd"><td>2.5 eV</td><td>100.6, 88.8, 77.6, 52.6, 49.2</td><td>52.0 (Ca)</td><td>' + M(r'2.7\times10^{-6}') + '</td><td>0.099</td></tr>\n</tbody></table>\n'
 '<p>The five atoms past the half line on the ladder hold five of the six largest optical phases at each energy, and the reflected power does not separate them. Within the five the order is the order of their margins in §23.3 read backwards: the nearer the first step lies to the line, the larger the phase. '
 'Five atoms is a small set, and these are the free-electron metals with the lowest plasma energies, which is known. What the chart adds is that its half line selects them, and that the odd reading finds them where the even reading is blind. '
 'Whether the phase is a function of the margin is not yet tested. [Open]</p>\n'
 '<h2 id="three-disks">23.6 Three disks</h2>\n'
 '<p>Three coordinates in this programme are drawn as a unit disk: the Smith coordinate ' + M(r'\Gamma=(z-1)/(z+1)') + ' of a ratio, used here and for reflection from a surface; the coordinate of a tetrahedron shape about the regular tetrahedron; and the chiral grading. '
 'A circle of radius ' + M(r'1/\sqrt2') + ' can be drawn on each, and a statement proved on one is not thereby a statement on another. Everything in this section is on the Smith disk: the ladder on its real diameter, the optical reflection in its interior. '
 'The half line is also the Schottky threshold of three perpendicular steps and the first point at which a knot’s meridian pair reaches the top of its turning band; those are statements about loops of steps, and no map from an atom’s ladder to such a loop is claimed.</p>\n')

S24 = (
 '<h1 id="walls-in-the-knot-layer">24. Walls in the knot layer</h1>\n'
 '<p>The knot layer records that an Alexander root of even multiplicity need not change the signature, and that 513 of them change nothing (Figure 21). It does not say why. A wall, in the sense used across this programme, is a nonzero nilpotent: an operator that is not zero and whose square is. This section shows that the silent double roots are of exactly that kind, and records three further results on the knot layer.</p>\n'
 '<h2 id="touch-and-crossing">24.1 Touch and crossing</h2>\n'
 '<p>At a double root the signature can jump by four, or not move. The tabulated signature on the two sides of the root and at the root, with the nullity there, separates two ways of not moving: two levels of the Hermitian form crossing zero in opposite directions (nullity 2), or one level reaching zero and turning back (nullity 1). '
 'On all 575 double roots on the unit circle [Exact, <code>silent_walls_02.py</code>]: 81 jump by four, all with nullity 2; 494 are silent, of which 376 are touches and 118 are opposed crossings. The knot 8<sub>20</sub>, whose polynomial is the square of the trefoil’s, is a touch.</p>\n'
 '<p><strong>Proposition 24.1 (the touch is one Jordan block) [Reproduction of standard module theory; Exact on the tables].</strong> Let ' + M('f') + ' be the factor whose square divides the Alexander polynomial at the root. The root is a touch when the Alexander module has the cyclic summand ' + M(r'\mathbb{Z}[t^{\pm1}]/(f^2)') + ', and it is two independent levels when the module splits as two copies of ' + M(r'\mathbb{Z}[t^{\pm1}]/(f)') + '; the second Alexander polynomial contains ' + M('f') + ' exactly in the split case.</p>\n'
 '<p>The registered condition was any disagreement between the nullity, read from the signature column, and membership in the second Alexander polynomial, an independent column. There is none: 376 roots of nullity 1, none a root of the second polynomial; 199 of nullity 2, all roots of it [Exact, <code>silent_walls_03.py</code>]. '
 'On the 198 double roots whose knot has an invertible Seifert matrix ' + M('V') + ' in the table, the monodromy ' + M(r'h=V^{-1}V^{T}') + ' was built and the kernels of ' + M(r'h-\lambda') + ' and ' + M(r'(h-\lambda)^2') + ' measured: all 121 touches have dimensions 1 then 2, one Jordan block, with ' + M(r'h-\lambda') + ' a nonzero nilpotent on the root space; all 77 split roots have 2 then 2 [Exact, <code>wall_nilpotent_04.py</code>].</p>\n'
 '<p>A defective double root can never jump: every jump of four and every opposed crossing is a split root. Among knots of infinite concordance order there are 61 silent double roots: 45 are touches and 16 are split with opposite signs, so none is left without a reading. What sets the two signs equal (81 roots) or opposite (118) at a split root is open.</p>\n'
 '<h2 id="torus-roots-from-the-arc-ends">24.2 The directions of a torus knot from its arc ends</h2>\n'
 '<p>For a torus knot ' + M('T(p,q)') + ' the ends of the arcs of the meridian phase are integer steps ' + M('k') + ' of a staircase, and the direction attached to an arc is ' + M(r'-k^2/(pq)') + ' modulo 1. The prediction was written before the search: three and four components for ' + M('T(3,4)') + ' and ' + M('T(3,5)') + ', but only two distinct directions each. The registered condition was any non-degenerate rational root outside the predicted set [Exact, <code>torus_roots_01.py</code>].</p>\n'
 '<table><thead><tr class="header"><th>Knot</th><th>Predicted</th><th>Drawing</th><th>Starts</th><th>Found (times)</th></tr></thead><tbody>\n'
 '<tr class="odd"><td>8<sub>19</sub> = ' + M('T(3,4)') + '</td><td>11/12, 2/3</td><td>tabulated</td><td>6,000</td><td>11/12 (881)</td></tr>\n'
 '<tr class="even"><td></td><td></td><td>braid ' + M(r'(\sigma_1\sigma_2)^4') + '</td><td>6,000</td><td>11/12 (579), 2/3 (106)</td></tr>\n'
 '<tr class="odd"><td>10<sub>124</sub> = ' + M('T(3,5)') + '</td><td>14/15, 11/15</td><td>tabulated</td><td>5,000</td><td>14/15 (266), 11/15 (1)</td></tr>\n'
 '<tr class="even"><td></td><td></td><td>braid ' + M(r'(\sigma_1\sigma_2)^5') + '</td><td>5,000</td><td>14/15 (238), 11/15 (45)</td></tr>\n</tbody></table>\n'
 '<p>Both predicted directions were found for each knot and none outside the sets. The same odd integer ' + M('k') + ' appears in three places: as the rotation of the product of the two meridians, ' + M(r'\operatorname{tr}(ab)=2\cos(k\pi/q)') + '; as the direction ' + M(r'-k^2/(pq)') + '; and as the arc end ' + M('k/(2pq)') + ' of the meridian phase [Exact, <code>join_k_01.py</code>, <code>torus_dirs_03.py</code>]. '
 'For torus knots the list of roots reached at a fixed budget depends on the drawing: the tabulated drawing of 8<sub>19</sub> never reaches 2/3.</p>\n'
 '<h2 id="the-commutator-number-is-a-defect">24.3 The commutator number is a defect</h2>\n'
 '<p>For two meridians ' + M('a,b') + ' the number ' + M(r'k=2-\operatorname{tr}[a,b]') + ' measures their commutator. When the commutator is a turn with eigenvalue ' + M(r'\lambda') + ' on the unit circle, ' + M(r'k=\lvert\lambda-1\rvert^2') + ', which is the relator defect ' + M(r'\delta') + ' of the projector geometry, with ' + M(r'\delta+g^2=4') + '; the band ' + M('0<k<4') + ' is its admissible domain. '
 'Every limiting value of ' + M('k') + ' at unit multiplicity in the two-bridge census is a clock-and-shift defect ' + M(r'4\sin^2(\pi j/d)') + ': 1, 2, 3 at ' + M('d=6,4,3') + '; ' + M(r'\varphi^{-2},\varphi^{2}') + ' at ' + M('d=10') + '; ' + M(r'(2\cos(j\pi/7))^2') + ' at ' + M('d=14') + ' [Exact, <code>defect_join_01.py</code>]. The values divided by a squared multiplicity (1/2, 1/4, 1/9) match no clock value and are open.</p>\n'
 '<h2 id="what-turns-and-what-climbs">24.4 What turns and what climbs</h2>\n'
 '<p>Read as words of peel steps, the objects of this paper differ in two respects only: whether the steps lie on one line, and whether the word closes. An ionization ladder is collinear and open: it climbs and keeps no order (§15.2). A film with phase is not collinear: it climbs in ' + M(r'\lvert\Gamma\rvert') + ' and turns in its phase. '
 'A torus knot closes as a pure turn, with vanishing volume form and a rational direction; an amphichiral knot closes as a pure climb, with direction zero; a hyperbolic knot has both. The wall of §24.1 and the half line of §23 are the places where turning becomes possible. No element-to-knot correspondence is claimed; the atomic record with a phase is the optical one (§23.5).</p>\n')

once('<h1 id="what-the-paper-establishes">22. What the paper establishes</h1>',
     S22 + S23 + S24 + '<h1 id="what-the-paper-establishes">25. What the paper establishes</h1>'
     ' <p>The peel coordinate is the edge coefficient of two books of one coupling, and the gap powers of the projector geometry read it composed with itself (§22). '
     'On the ionization chart the half line is crossed once along each core line; the alkali metals reach it by their shell part alone, with one screening value from sodium to caesium; and the five atoms past it are found by the optical phase where reflected power is blind (§23). '
     'In the knot layer a silent double root is a nilpotent wall or a pair of opposed levels, decided in every tabulated case by the module (§24).</p>')
once('<h2 id="remaining-open-questions">22.1 Remaining open questions</h2> <p>',
     '<h2 id="remaining-open-questions">25.1 Remaining open questions</h2> <p>Is the ionization energy of Fr⁺ above or below 23.74 eV? Is the optical phase of the alkali metals a function of their margin from the half line? What sets equal or opposite signs at a split double root? ')

# ------------------------------------------------------------------ open problems (section 17)
once('<li><p><strong>The elemental–knot bridge</strong> itself.</p></li> </ul>',
     '<li><p><strong>The elemental–knot bridge</strong> itself.</p></li> '
     '<li><p><strong>A measured ionization energy of Fr⁺.</strong> The half line lies inside the margin of the archived semi-empirical value; 23.74 eV decides whether francium is past it (§23.3).</p></li> '
     '<li><p><strong>The alkali charge ratio.</strong> Why ' + M('Z_c/Z_v') + ' is one number from sodium to caesium, and whether the second members of each core line (1.54 to 1.58 from Mg⁺ to Ba⁺) hold a second band (§23.3).</p></li> '
     '<li><p><strong>Phase against margin.</strong> Whether the optical phase of the five atoms past the half line is a function of their margin from it (§23.5).</p></li> '
     '<li><p><strong>The elemental angle in projector form.</strong> The principal angles of §9 were taken between model orbital subspaces; the same angles between the retained projectors of §22.1 have not been computed.</p></li> '
     '<li><p><strong>A map between the disks.</strong> No map is stated from a point of the Smith disk to a point of the tetrahedron-shape disk; statements about the circle of radius ' + M(r'1/\sqrt2') + ' on one do not transfer (§23.6).</p></li> '
     '<li><p><strong>Signs at split roots, and the squared multiplicity</strong> in the commutator limits (§24.1, §24.3).</p></li> </ul>')

# ------------------------------------------------------------------ appendices D and F
once('<h1 id="appendix-d-test-ledger">Appendix D — Test ledger</h1> <p>',
     '<h1 id="appendix-d-test-ledger">Appendix D — Test ledger</h1> '
     '<p>Sections 22–24 (kill conditions in each script header, fixed before the run on 10–12 November): '
     'SHELL-SCREEN-04, the alkali charge ratio, kill a spread above 2% among Na, K, Rb, Cs: 1.11%, passed; the helium-core series, kill a crossing outside ' + M('(6,7)') + ' or a miss above 2% for ' + M('Z=5') + ' to 10: crossing 6.538, largest miss 0.55%, passed, and its opposite with the 5/8 removed: crossing 9.47. '
     'ISO-CROSS-03, kill more than one crossing on any core line: none, passed. ELEMENT-BALL-01, largest step at a closed core: 101 of 101, passed; a whole shell composed as one step lies at the half line: killed (median distance 0.404 against 0.297 for random blocks), and killed in the opposite direction (0.296 against 0.338). '
     'LADDER-WALL-01, the half line marks shell openings: killed, 8 of 675 on true charge indices. PLASMA-WALL-01, an optical wall energy follows the ladder: killed (rank correlations +0.06, −0.28, +0.26, 30 elements); its opposite, the phase, led to PHASE-LADDER-02, kill ' + M('p>0.01') + ' or a change of direction: ' + M(r'p=2.7\times10^{-6}') + ' at three energies, passed; the even reading ' + M('p=0.09') + ' to 0.10. '
     'SILENT-WALLS-02, a silent double root is two opposed crossings: killed as stated (376 of 494 are touches) and repaired by SILENT-WALLS-03, kill any disagreement of nullity with the second Alexander polynomial: 575 of 575 agree, passed; WALL-NILPOTENT-04, kill a kernel dimension differing from the nullity: 198 of 198 agree, passed. '
     'TORUS-ROOTS-01, kill a root outside the predicted set: none in 22,000 starts, passed. DEFECT-JOIN-01, kill a unit-multiplicity limit with no clock value: none, passed. NEVER-TURN-01, never-turning knots stand apart in direction: killed (inside the spread of the turning knots); the opposite reading is not yet run. '
     'ESR-CHECK-01 recounts the census of the 118-element archive: 7,021 slots, 5,847 thresholds, 5,714 adjacent steps, 5,584 three-threshold windows, grades 311 / 919 / 4,617, zero failures of exact inversion and composition.</p> <p>')
once('<h1 id="appendix-f-scripts">Appendix F — Scripts</h1> <p>',
     '<h1 id="appendix-f-scripts">Appendix F — Scripts</h1> '
     '<p><strong>Sections 22–23:</strong> <code>v30/shell_screen_04.py</code> (the split in charges, the alkali charge ratio, the helium-core series and its opposite), <code>v30/esr_check_01.py</code> (census and half-line counts in exact rational arithmetic), <code>v30/figs_v30.py</code> (Figures 35 and 36), '
     '<code>elements/element_ball_01.py</code>, <code>elements/core_open_02.py</code>, <code>elements/iso_cross_03.py</code>, <code>round4/ladder_wall_01.py</code>, <code>round4/plasma_wall_01.py</code>, <code>round4/phase_ladder_02.py</code> (reads a local copy of the refractiveindex.info database); each reads <code>element_thresholds_20261011.json.gz</code>. '
     '<strong>Section 24:</strong> <code>silent_walls_02.py</code>, <code>silent_walls_03.py</code>, <code>wall_nilpotent_04.py</code>, <code>torus_roots_01.py</code>, <code>torus_roots_02.py</code>, <code>join_k_01.py</code>, <code>torus_dirs_03.py</code>, <code>defect_join_01.py</code>, <code>never_turn_01.py</code> (need snappy and the KnotInfo tables).</p> <p>')

# ------------------------------------------------------------------ literature
once('<h1 id="appendix-e-literature">Appendix E — Literature</h1> <p>',
     '<h1 id="appendix-e-literature">Appendix E — Literature</h1> '
     '<p><strong>Companion papers of this programme, used in §§22–24:</strong> J. Beasley, <em>The Intrinsic Quantum Geometric Tensor on the Grassmannian</em> (2026); <em>The Weight Between</em> (2026), Proposition 5; <em>Non-Normality Is Connection Energy, and Its Opposite</em> (2026), the scalar edge and §10; '
     '<em>Universal Projector Geometry from Electrical Measurements</em> (2026), §4.4; <em>The Dirac Time of the Gigantefermion</em> (2026), Theorem 13.1; <em>Two Trees in One Ball</em> (2026), Theorems 5.3, 5.4 and 8.6. '
     'The second-order coefficients of the two- and three-electron ' + M('1/Z') + ' series in §23.4 are cited from the standard literature and were not read at source for this version.</p> <p>')

# ------------------------------------------------------------------ contents
TOC = ('<li><a href="#the-peel-inside-the-projector-geometry" id="toc-the-peel-inside-the-projector-geometry">22. The peel inside the projector geometry</a>\n<ul>\n'
       '<li><a href="#a-peel-is-a-projector-move">22.1 A peel is a projector move</a></li>\n<li><a href="#the-peel-step-is-an-edge-of-two-books">22.2 The peel step is an edge of two books</a></li>\n'
       '<li><a href="#gap-powers-compose-the-step">22.3 Gap powers compose the step</a></li>\n<li><a href="#what-the-ladder-fixes">22.4 What the ladder fixes, and what the geometry adds</a></li>\n</ul></li>\n'
       '<li><a href="#the-half-line-on-the-ionization-chart" id="toc-the-half-line-on-the-ionization-chart">23. The half line on the ionization chart</a>\n<ul>\n'
       '<li><a href="#eight-steps">23.1 Eight steps</a></li>\n<li><a href="#one-crossing-per-core-line">23.2 One crossing on each core line</a></li>\n<li><a href="#the-alkali-charge-ratio">23.3 The alkali metals reach the line by their shell part alone</a></li>\n'
       '<li><a href="#the-five-eighths-places-the-crossing">23.4 The five-eighths places the carbon–nitrogen crossing</a></li>\n<li><a href="#the-optical-phase-finds-the-same-five-atoms">23.5 The optical phase finds the same five atoms</a></li>\n<li><a href="#three-disks">23.6 Three disks</a></li>\n</ul></li>\n'
       '<li><a href="#walls-in-the-knot-layer" id="toc-walls-in-the-knot-layer">24. Walls in the knot layer</a>\n<ul>\n'
       '<li><a href="#touch-and-crossing">24.1 Touch and crossing</a></li>\n<li><a href="#torus-roots-from-the-arc-ends">24.2 The directions of a torus knot from its arc ends</a></li>\n'
       '<li><a href="#the-commutator-number-is-a-defect">24.3 The commutator number is a defect</a></li>\n<li><a href="#what-turns-and-what-climbs">24.4 What turns and what climbs</a></li>\n</ul></li>\n')
once('<li><a href="#what-the-paper-establishes" id="toc-what-the-paper-establishes">22. What the paper establishes</a>',
     TOC + '<li><a href="#what-the-paper-establishes" id="toc-what-the-paper-establishes">25. What the paper establishes</a>')
once('id="toc-remaining-open-questions">22.1 Remaining open questions</a>', 'id="toc-remaining-open-questions">25.1 Remaining open questions</a>')

open(out, 'w', encoding='utf-8').write(t)
print('v2.9 chars', n0, '-> v3.0 chars', len(t), 'added', len(t) - n0)
