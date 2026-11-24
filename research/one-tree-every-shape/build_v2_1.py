# SCRIPT: OTES-BUILD-03  builds One Tree, Every Shape v2.1 from v2 (v2 kept unchanged):
# licence line in the page, Lemke Oliver-Soundararajan credit on the end-digit eye,
# the commuting line labelled as a reading, version 2.1.
import json, sys
v2, out = sys.argv[1:3]
src = open(v2).read()
def rep(old, new, count=1):
    global src
    n = src.count(old); assert n == count, (old[:90], n); src = src.replace(old, new)
LIC = "© 2026 Jeromie Beasley · code MIT · text and figures CC BY 4.0"
rep('<title>One Tree, Every Shape</title>',
    '<title>One Tree, Every Shape</title><meta name="author" content="Jeromie Beasley"><meta name="license" content="Code: MIT. Text and figures: CC BY 4.0. Copyright (c) 2026 Jeromie Beasley.">')
rep('<!doctype html>', '<!doctype html><!-- One Tree, Every Shape v2.1. ' + LIC + '. https://github.com/dicipler-pixel/votkp-lean -->')
rep("Jeromie Beasley · 3D mixer · v2</div>", "Jeromie Beasley · 3D mixer · v2.1<br>" + LIC + "</div>")
a = src.index("window.SCENES=") + len("window.SCENES="); b = src.index(";</script>", a)
sc = json.loads(src[a:b]); hit = {'zero': 0, 'digit': 0}
for s in sc:
    n = s.get('note', '')
    if n.startswith('Points that sit freely are what steps that commute give.'):
        s['note'] = ('Measured: the zeros hold each other apart, 1.0% small gaps against 26% for free points. '
                     'A reading, not a result: free points are what steps that commute give, and points that hold each other apart '
                     'are what steps that do not commute give, in line with the random-matrix picture of the zeros (Montgomery; Dyson).')
        hit['zero'] += 1
    if n.startswith('The same end digit twice in a row is 8 to 9% rarer'):
        s['note'] = n + (' Prior art: Lemke Oliver and Soundararajan (2016) found this kind of bias in the last digits of '
                         'consecutive primes; this is the same count for consecutive twin starts.')
        hit['digit'] += 1
assert hit == {'zero': 1, 'digit': 1}, hit
src = src[:a] + json.dumps(sc, ensure_ascii=False) + src[b:]
open(out, 'w').write(src); print('wrote', out, len(src))
