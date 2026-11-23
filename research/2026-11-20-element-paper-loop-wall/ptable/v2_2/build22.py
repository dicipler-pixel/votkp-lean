# SCRIPT: PT-V22-BUILD  Periodic Table of Elemental Peels v2.2: v2.1 plus the Shapes view
src = open('/tmp/claude-0/-home-claude/502f5ad8-acd9-59a2-b5cf-d48e7967cc3a/scratchpad/pt_v21.html').read()
def rep(o, n, c=1):
    global src
    k = src.count(o); assert k == c, (o[:70], k); src = src.replace(o, n)
rep('<title>Periodic Table of Elemental Peels v2.1 · Jeromie Beasley</title>', '<title>Periodic Table of Elemental Peels v2.2 · Jeromie Beasley</title>')
rep('href="#moves">Where the electron moves</a>', 'href="#moves">Where the electron moves</a><a href="#shapes">Shapes</a>')
section = '''<section class="view" id="v-shapes"><p class="note">The same table read on other shapes. The disk is one choice of shape; here every removal step and anion rung is carried onto a triangle, square, diamond or hexagon, by a chart that keeps angles (Schwarz–Christoffel) or one stretched out to the faces. Below, each element's two books (anion rung and first core opening) sit on the diamond, one edge per book; and a table gives how well each shape groups the columns.</p>
<div class="ctl"><label for="shapepick">shape</label><select id="shapepick"><option value="disk">disk (as now)</option><option value="triangle">triangle</option><option value="square">square</option><option value="diamond">diamond</option><option value="hexagon">hexagon</option></select><label for="shapetype">chart</label><select id="shapetype"><option value="angles">keeps angles</option><option value="stretch">stretched to the faces</option></select></div>
<p class="note" id="shapedisknote"></p><figure><svg class="chart" id="shapedisk" viewBox="0 0 900 900" style="max-width:820px" role="img" aria-label="Every step on the chosen shape"></svg></figure>
<h3 style="font:600 15px var(--body);margin:18px 0 4px">The address on the diamond</h3><p class="note" id="addrnote"></p><figure><svg class="chart" id="addrsvg" viewBox="0 0 640 640" style="max-width:640px" role="img" aria-label="Anion rung against first core opening on the diamond"></svg></figure>
<h3 style="font:600 15px var(--body);margin:18px 0 4px">Which shape groups the columns</h3><p class="note">Each element's first 8 removal steps are its books; on each shape, its nearest element is found by that shape's own distance. Hydrogen to astatine, 77 elements with 8 steps. Every shape groups the columns far better than the raw energies do (0.05). The triangle family, which reads only the shape of the ladder, scores highest, but no shape beats the circle by more than its bootstrap spread. Script PT-SHAPES-01B on the element-paper/loop-wall branch.</p><div id="shaperecall"></div></section>
'''
rep('<section class="view" id="v-moves"', section + '<section class="view" id="v-moves"')
js = open('shapes_view.js').read()
rep("/* hash routing */", js + "\n/* hash routing */")
rep("VIEWS=['standard','signature','cores','disk','stone','colour','octaves','spiral','heavy','decay','window','faces','corpus','moves','tests','about'];",
    "VIEWS=['standard','signature','cores','disk','stone','colour','octaves','spiral','heavy','decay','window','faces','corpus','moves','shapes','tests','about'];")
rep("if(v==='spiral')drawSpiral();else if(S3){S3.stop();S3=null;}}", "if(v==='shapes')drawShapes();if(v==='spiral')drawSpiral();else if(S3){S3.stop();S3=null;}}")
rep("$('spiralmode').onchange=drawSpiral;", "$('spiralmode').onchange=drawSpiral;$('shapepick').onchange=drawShapeDisk;$('shapetype').onchange=drawShapeDisk;")
src = src.replace('· v2.1, 22 November 2026', '· v2.2, 23 November 2026', 1).replace('· v2.1, ', '· v2.2, ', 1)
open('Periodic_Table_of_Elemental_Peels_v2_2_Jeromie_Beasley.html', 'w').write(src)
print('ok', len(src))
