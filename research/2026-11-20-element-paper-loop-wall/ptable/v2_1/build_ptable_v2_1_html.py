# SCRIPT: PERIODIC-TABLE-OF-PEELS-HTML-V2-1
# Builds v2.1 from the v2 page (read only, never written): adds the view "Where the electron moves",
# marks the 20 elements on their tiles and in their drawers, and embeds moves_test.json.
import json
SRC = '../v2/Periodic_Table_of_Elemental_Peels_v2_Jeromie_Beasley.html'
s = open(SRC).read()
T = json.load(open('moves_test.json')); js = open('moves.js').read()
def rep(old, new, cnt=1):
    global s
    n = s.count(old); assert n == cnt, (n, old[:90]); s = s.replace(old, new)
rep('<title>Periodic Table of Elemental Peels v2 · Jeromie Beasley</title>', '<title>Periodic Table of Elemental Peels v2.1 · Jeromie Beasley</title>')
rep('hydrogen to darmstadtium · v2, 22 November 2026', 'hydrogen to darmstadtium · v2.1, 22 November 2026')
rep('@media (max-width:900px)', '.tile .mv{position:absolute;bottom:3px;right:4px;font:600 9px var(--mono);color:#0a0f16;background:#c9b6ff;border-radius:3px;padding:0 3px}.tile .mv.t{background:#9fe0c0}\n@media (max-width:900px)')
rep('<a href="#tests">Tests and predictions</a>', '<a href="#moves">Where the electron moves</a><a href="#tests">Tests and predictions</a>')
sec = '''<section class="view" id="v-moves"><p class="note">Twenty atoms do not fill in the plain order. In ten, the electron moves into the d shell of its own row; in ten more, an n + l tie between two shells is broken toward d, and at lawrencium toward 7p. Tiles carry a small mark: d for a move in the d row, t for a tie. The strips show each d row's first peel step z₁ = IE₂/IE₁, movers filled.</p>
<div class="classes" id="movesclasses"></div><figure><svg class="chart" id="movessvg" viewBox="0 0 1300 510" role="img" aria-label="First peel step by d row, movers filled"></svg></figure><div class="cards" id="movescard" style="margin-top:14px"></div></section>
'''
rep('<section class="view" id="v-tests">', sec + '<section class="view" id="v-tests">')
# tile mark
rep('<span class="z">${e.Z}</span><span class="s">${e.sym}</span>${spark(e)}', '<span class="z">${e.Z}</span><span class="s">${e.sym}</span>${spark(e)}${MOVES[e.sym]?`<span class="mv ${MOVES[e.sym][0]}" title="${MOVES[e.sym][0]===\'d\'?\'the electron moves to d\':\'an n + l tie, broken toward d (Lr: 7p)\'}">${MOVES[e.sym][0]}</span>`:\'\'}')
# data
rep(';D=d;EL=d.elements;', ';d.moves=' + json.dumps(T, separators=(',', ':')) + ';D=d;EL=d.elements;')
rep("drawHeavy();drawDecay();drawWindow();drawFaces();corpus();", "drawHeavy();drawDecay();drawWindow();drawFaces();corpus();drawMoves();")
rep("'faces','corpus','tests','about'];", "'faces','corpus','moves','tests','about'];")
rep('/* hash routing */', js + '\n/* hash routing */')
open('Periodic_Table_of_Elemental_Peels_v2_1_Jeromie_Beasley.html', 'w').write(s)
print('written', len(s))
