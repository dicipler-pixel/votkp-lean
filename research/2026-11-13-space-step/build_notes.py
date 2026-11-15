# SCRIPT: BUILD-V4-NOTES-01  (assembles the notes page; no computation here)
import base64
img=base64.b64encode(open('fig_space_axis.png','rb').read()).decode()
css="""body{background:#0b0f17;color:#dfe5f2;font:17px/1.6 Georgia,serif;max-width:980px;margin:40px auto;padding:0 22px}
h1{font-size:30px;color:#ffd166;margin-bottom:4px}h2{color:#8fd3ff;border-bottom:1px solid #2a3550;padding-bottom:4px;margin-top:38px}h3{color:#c7b8ff;margin-top:26px}
table{border-collapse:collapse;width:100%;margin:14px 0;font-size:15.5px}th,td{border:1px solid #2a3550;padding:6px 9px;text-align:left;vertical-align:top}th{background:#141b2b;color:#ffd166}
blockquote{border-left:3px solid #ffd166;margin:12px 0;padding:4px 16px;color:#f1e7c9;background:#121826}code{background:#141b2b;padding:1px 5px;border-radius:3px;color:#ffe9a8;font-size:14px}
.g{color:#7be0a4}.o{color:#ffb86b}.r{color:#ff8fa3}.small{font-size:14.5px;color:#aab4cc}img{max-width:100%;border:1px solid #2a3550;border-radius:6px}"""
H=[]; A=H.append
A('<!doctype html><html><head><meta charset="utf-8"><title>VOTKP notes for the next version, 13 November 2026</title><style>'+css+'</style></head><body>')
A('<h1>VOTKP: notes for the next version</h1><p class="small">13 November 2026, version 1. Working notes written by Claude for Jeromie Beasley. Not a paper and not his text, except where his words are quoted with their times. Grades: <span class="g">exact</span> = algebra or a check that ran; <span class="o">seen</span> = noticed in the numbers, no line written first; <span class="r">open</span> = not run. AI-assisted.</p>')

A('<h2>1. What the paper is, in his words</h2>')
A('<p>The next version should be built on these, quoted, as the hypotheses the paper serves. They are his messages of 6 November 2026.</p>')
for t,q in [('07:50','the way the hypersurface peels itself is whre i want to look'),
 ('08:10','the key is conductivity or not in all elelmnts think like this is a elelctric universe set by the electron ;eriod with light the twin friend guiding the whole thing'),
 ('08:18','its the space between thats non conductive this varies why the material structure does the lattice of each element is spaced dif'),
 ('08:19','maybe doestn conduct is like a ground or the vacume'),
 ('08:27','superfluididty and conductivity are worth cheking the heat to cold is the key to matter forming itself into any lattice structure'),
 ('08:37','direction of the leading eigen vector to co vector fight and what else decide it ? time thats the key , so what branch gets cut at the hypersurface determies that?'),
 ('08:48','this is our votkp paper , and that originally tried to measure the elelmnt volume of the knot potential ... now we changed this more into vectors but that may be what creates space and volume as we follow our leader light? keep this as my stance as hypothesis'),
 ('11:46','the vector determines the direction that may be ... decay')]:
    A('<blockquote><b>%s</b> &nbsp; %s</blockquote>'%(t,q))
A('<p>From 12 November: two balls pushed together connect at certain levels but always leave a layer of gap, and that is the spacing of the crystal; some radiate and some absorb, so one size does not fit all; heat, temperature, time and conductivity decide transformations; the electron sea is the ground and the electron follows light; the Snell law at the hypersurface and the Pauli exclusion principle.</p>')

A('<h2>2. The new piece: the space between as one peel step</h2>')
A('<p>The 6 November work measured the space between atoms as <code>E = 1 − (r_cov / r_room)³</code>, one minus the atom\'s own volume over the volume it has in the material. That is a ratio of two volumes, so it is a step in the peel coordinate with no new definition:</p>')
A('<p style="text-align:center;font-size:19px">z<sub>E</sub> = V<sub>room</sub> / V<sub>own</sub> = 1/(1 − E), &nbsp;&nbsp;&nbsp; Γ<sub>E</sub> = (z<sub>E</sub> − 1)/(z<sub>E</sub> + 1) = E/(2 − E).</p>')
A('<p><span class="g">Exact:</span> the line E = 2/3 is the step z = 3, where Γ<sub>E</sub> = 1/2 and K = 2. That step was already singled out three times on 12 and 13 November without any element data: it is where the loop\'s K equals 2, it is the only whole-number solution of the pressure balance P₁ + P₂ = 1 between two facing balls, and it is the point of the exit-line band where K equals its own mean. So the map that was missing between "the 2/3 line" and the disk is this: <b>the 2/3 line is Γ = 1/2 of the space step.</b> It is not Garrett\'s Γ = 2/3, which is the step z = 5.</p>')
A('<img src="data:image/png;base64,'+img+'" alt="Elements and switch points on the space-step axis">')
A('<h3>What the published numbers do on that axis</h3>')
A('<table><tr><th>Line, written before the run</th><th>Result</th></tr>'
  '<tr><td>L1. Every metal has Γ<sub>E</sub> below 1/2 and every non-metal at or above it (41 elements with optical data)</td><td><span class="g">40 of 41.</span> All 35 metals lie at Γ<sub>E</sub> ≤ 0.433 (sodium highest). Non-metals lie at 0.498 to 0.613. Boron is the one on the wrong side, at 0.4977, K = 1.98. Nothing sits between 0.433 and 0.498.</td></tr>'
  '<tr><td>L2. Each measured switch with both sides tabulated straddles Γ<sub>E</sub> = 1/2</td><td><span class="g">Holds for five:</span> silicon melting (0.511 solid, 0.468 liquid metal), germanium melting (0.506, 0.488), tin grey to white (0.497, 0.403), iodine squeezed (0.502 at 9.9 GPa, metal by 0.474 to 0.445), black phosphorus squeezed (0.538, 0.423). <span class="r">Fails for three kinds:</span> mercury is still metal at 0.519 and switches between 0.52 and 0.60; xenon becomes metal only at 0.30; hydrogen and the alkalis switch far out, at 0.83 to 0.90.</td></tr>'
  '<tr><td>L3. Mercury\'s critical density against the wall Γ<sub>E</sub>² = 1/2</td><td><span class="o">One number:</span> the wall gives 33.800 × (3 − 2√2) = 5.799 g/cm³; the published critical density is 5.8. Caesium, rubidium and potassium do not sit there: their critical points are at z = 11.1, 12.6 and 11.4.</td></tr></table>')
A('<h3>Seen, with no line written first</h3><ul>'
  '<li><span class="o">Three families, three steps.</span> Covalent and p-block matter switches at z = 3. Mercury starts leaving at about 3.1 and has its critical point at the wall, z = 5.83. The one-electron atoms switch near z = 11 to 13: caesium, potassium and rubidium at their critical points (11.1, 11.4, 12.6) and fluid deuterium and hydrogen turning metal (11.6 to 13.2; one older hydrogen value at 19.6). This is "one size does not fit all" in numbers. The alkalis are also the one family past the half line in the ionization ladder, and z = 11 is the partner across the wall of the first shell step z = 4.</li>'
  '<li><span class="o">Diamond and the quarter turn.</span> The loop\'s turn is 90° at z = 3.2202. Diamond carbon sits at 3.213 (89.6°) and tellurium at 3.223 (90.1°). Silicon and germanium are at 81°, boron at 77°. Every metal is below 54°.</li>'
  '<li><span class="o">The empty band.</span> Between the last metal and the first non-metal (E from 0.604 to 0.665) there is no element at room conditions. The 60° step falls inside it (E = 0.624).</li></ul>')
A('<p class="small">Cautions. A filled fraction of 1/3 is also the conductor threshold of symmetric effective-medium theory (Bruggeman), and the 6 November ledger records it; so E = 2/3 as a conduction line has prior art, and what is his is the coordinate that puts it on the same disk as the loop, the wall and the neutrino chain. E depends on which radius is called the atom\'s own (Pyykkö covalent radii here); the mercury number moves with that choice. The alkali metal-to-non-metal densities are quoted in the sources only as "around the critical density". The densities, radii and switch points are other people\'s published measurements.</p>')

A('<h2>3. Everything that now has to go in</h2><table><tr><th>Piece</th><th>State</th><th>Where it came from</th></tr>'
  '<tr><td>The whole of v2.9 to v3.3</td><td>Kept word for word</td><td>paper/votkp_v3_3</td></tr>'
  '<tr><td>The space step: Γ<sub>E</sub>, the 2/3 line as Γ = 1/2, the switch table, the three families</td><td class="g">exact map; data lines above</td><td>section 2 of these notes; 6 November ledger and data sheets</td></tr>'
  '<tr><td>Optical record beside the peel: arg N splits metal from non-metal 41 of 41 at 0.661 rad (fitted); arg N against E, +0.785 in 35 metals; handedness of the Smith track, 56 of 59 clockwise</td><td class="o">carried from 6 November, not rerun here</td><td>LEDGER_RAW items 1 to 9</td></tr>'
  '<tr><td>The coinage metals: peel size orders Ag &gt; Cu &gt; Au, the colour edge orders Ag &gt; Au &gt; Cu, and the area of the Smith track orders Ag 24.5 &gt; Au 8.9 &gt; Cu 6.5, the same as the colour edge</td><td class="o">seen: three metals</td><td>colour notes; ledger item 1</td></tr>'
  '<tr><td>Colour as a second record: the paper\'s own section 20.3.4 says ratios of removal energies cannot fix optical numerators</td><td>his text</td><td>v2.9 section 20; the 6.82 eV rule</td></tr>'
  '<tr><td>Level and shape: B102 against polarizability, radius, hardness, conductivity, melting; shape still adds to spacing with the level removed (−0.46, 56 metals)</td><td class="g">ran</td><td>T4, T9, T12 reports</td></tr>'
  '<tr><td>Alkalis: one charge ratio; the only family past the half line; all body-centred; caesium the last one past</td><td class="g">ran</td><td>v3.0 section 23; T9</td></tr>'
  '<tr><td>B99: Pythagorean shell terms; no pure shell step reaches the wall; whole-number pairs across the wall are (5, 7) and (4, 11)</td><td class="g">exact</td><td>T10</td></tr>'
  '<tr><td>Many balls: gap 2/(pⁿ + 1) never zero; six, eight and twelve arms close into simple, body-centred and face-centred cubic; the 13 set does not close; a square of four joins leaves the loop</td><td class="g">exact / ran</td><td>T10, T11</td></tr>'
  '<tr><td>Crystal turns of the loop: 60°, 90°, 120°, 180° at exact steps; the wall is the full turn; hexagonal packing needs the turn between layers</td><td class="g">exact</td><td>T11</td></tr>'
  '<tr><td>Gap and decay: one law; locked step z* = 6.26913</td><td class="g">exact</td><td>T8</td></tr>'
  '<tr><td>Neutrino chain: the speed limit is one law; the two-moment exceptional point is the wall; full-chain wall at κ = 2k/π; order of a history is the loop and is always a run; the door is not a wall crossing</td><td class="g">exact / ran</td><td>T13</td></tr>'
  '<tr><td>Dirac Time: what it already holds of the loop, and what in it to compute</td><td class="r">full read running</td><td>T14</td></tr>'
  '<tr><td>Knots and volume: the original meaning of VOTKP; volume series; silent walls 575 of 575; never-turners</td><td>in v3.1 sections 24 and 28</td><td>needs his call on where it sits</td></tr>'
  '<tr><td>Lean: 140 + 159 + 43 theorems compiled</td><td class="g">ran</td><td>T6, T7</td></tr></table>')

A('<h2>4. A shape for the paper as one argument</h2><p>The versions since v3.0 added sections at the end. To read as one thought the order should follow the peel outward, with nothing removed:</p><ol>'
  '<li><b>What a peel is and what a record keeps.</b> As now. The three disks named once and kept apart, in his own terms from Matter, Gases and VOTKP sections 4.8 and 9.4: the ladder disk (ratios of thresholds), the reflection disk (Γ = (1 − N)/(1 + N) of the optical constant), the space disk (Γ<sub>E</sub>).</li>'
  '<li><b>The ladder.</b> Shape and level; walls and ridges; the shell and screening split; the alkali ratio; the half line on the ladder.</li>'
  '<li><b>The loop.</b> Turn, wall, run; K as the fight between the vector and its covector; pairing; the gap; Snell form and exclusion form; time counting only past the wall. This is where his 07:50 and 08:37 statements are answered.</li>'
  '<li><b>The space between.</b> The space step; ground and conduction; the 2/3 line as Γ = 1/2; switch points under heat and pressure as crossings; three families. This is where 08:10 to 08:27 are answered, and where time and temperature finally enter with measured data.</li>'
  '<li><b>Many atoms.</b> Balls joined with the forced gap; which lattices close; crystal turns; the square of joins; what the alkalis do.</li>'
  '<li><b>Light.</b> The loop-fed signal and its speed limit; push on a layer; the optical record as a second record; colour, the coinage metals, the 6.82 eV rule.</li>'
  '<li><b>Knots and volume.</b> The original VOTKP; his 08:48 hypothesis stated as his.</li>'
  '<li><b>The same wall elsewhere.</b> The neutrino chain; Dirac Time.</li>'
  '<li><b>Ledger, open questions, Lean, scripts.</b></li></ol>')

A('<h2>5. Work to do before writing, in his coordinate</h2><p>Each of these is a computation inside his own objects or a comparison with measured switch points. None is a rank correlation on a property table.</p><table><tr><th>#</th><th>Work</th><th>What it would settle</th></tr>'
  '<tr><td>1</td><td>The space step for all 81 rows of the current-data sheets, with the allotropes (tin, carbon, phosphorus) as pairs</td><td>Whether L1 holds beyond the 41 with optical data; the staircase B, Ge, Si, C, Te at exact turn steps</td></tr>'
  '<tr><td>2</td><td>The three families as a registered line: p-block at z = 3, mercury at the wall, one-electron atoms at one common step; add zinc and cadmium (same family as mercury) and sodium and lithium if critical densities can be found</td><td>Whether "one size does not fit all" is three exact steps or a coincidence of four numbers</td></tr>'
  '<tr><td>3</td><td>Γ<sub>E</sub> against the reflection coordinate for the 35 metals (arg N against E was +0.785)</td><td>The map between the space disk and the reflection disk, which closes the three-disks gap</td></tr>'
  '<tr><td>4</td><td>Compose the space step with the ladder step by ⊕ for each element</td><td>Whether B99\'s "the wall lives in the composition" is the composition of shell, screening and space</td></tr>'
  '<tr><td>5</td><td>Two balls with unequal steps taken from real pairs, cut where the pressure balance holds</td><td>His 12 November picture with real numbers in it</td></tr>'
  '<tr><td>6</td><td>The area of the Smith track for copper, silver and gold again, with the other coinage-like triples</td><td>Whether the optical record resolves the coinage mismatch beyond three points</td></tr>'
  '<tr><td>7</td><td>An operator for the exclusion form</td><td>Whether the Pauli reading is more than a sign change</td></tr>'
  '<tr><td>8</td><td>What Dirac Time says should be computed for the loop</td><td>Comes from the read now running</td></tr></table>')

A('<h2>6. Corrections to carry</h2><ul><li>The gather page row for the 6.82 eV rule says coloured elements; it sorts atoms with a visible line from the ground state.</li><li>Pair count 354 and 253 in the body against 353 and 251 from the rerun; the missing pair is not identified.</li><li>The twin-chain angle is not a constant; 12.08° must not be quoted as one.</li><li>The tree on 11 does not give twelve face-diagonal arms in his normal form; the tree on 7 in his papers has six arms.</li><li>The Space Between page published on 6 November still states two results in their first form.</li><li>Green and Cyan are numbered 2 and 4 in one colour document and 4 and 2 in the other.</li></ul>')

A('<h2>7. Calls that are his</h2><ol><li>Knots and volume at the centre, or one layer beside the elements.</li><li>The velocity and boost wording in the v2.9 body: keep or remove. It came from a September draft Claude wrote.</li><li>How the credit for the last-digit rule should read.</li><li>Whether to rewrite the branch history that carries a name in one early commit.</li><li>Whether the next version may touch the 36 double statements and the Ky Fan range in v2.9\'s own text.</li><li>Whether the 2/π value goes into the neutrino paper.</li><li>Whether the three families of section 2 go in as a result or as an open observation.</li></ol>')
A('<p class="small">Files behind section 2: <code>e_gamma_map_01.py</code>, its output, and <code>fig_space_axis.py</code>, with the data sheets A_41, B_40, C_edges and per_element as supplied on 13 November.</p></body></html>')
open('VOTKP_V4_NOTES_20261113_v1.html','w').write('\n'.join(H)); print(len('\n'.join(H)))
