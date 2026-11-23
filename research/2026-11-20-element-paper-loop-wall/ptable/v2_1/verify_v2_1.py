# SCRIPT: PTABLE-V2-1-VERIFY
# Independent recount: reads the archive and the page separately, recomputes z1 and the baseline a second way
# (rank-based: best errors = min over split points of the sorted row), and checks the drawers and tiles in the DOM.
import json, gzip, itertools, re, asyncio, os
from playwright.async_api import async_playwright
recs = {r['symbol']: r for r in json.load(gzip.open('../../../../data/element_thresholds_20261011.json.gz'))['records']}
z1 = {s: r['thresholds'][1]['IE_eV'] / r['thresholds'][0]['IE_eV'] for s, r in recs.items() if len(r['thresholds']) > 1}
rows = {'3d': 'Sc Ti V Cr Mn Fe Co Ni Cu Zn', '4d': 'Y Zr Nb Mo Tc Ru Rh Pd Ag Cd', '5d': 'La Hf Ta W Re Os Ir Pt Au'}
mov = set('Cr Cu Nb Mo Ru Rh Pd Ag Pt Au'.split())
def errs(order, S):  # order: symbols sorted by z1; movers predicted = top (n-j)
    n = len(order); return min(sum((i >= j) != (order[i] in S) for i in range(n)) for j in range(n + 1))
html = open('Periodic_Table_of_Elemental_Peels_v2_1_Jeromie_Beasley.html').read()
T = json.loads(re.search(r'd\.moves=(\{.*?\});D=d', html).group(1))
for (nm, ss), r in zip(rows.items(), T['rows']):
    syms = ss.split(); order = sorted(syms, key=lambda s: z1[s]); obs = errs(order, mov)
    k = len(mov & set(syms)); hits = sum(errs(order, set(c)) <= obs for c in itertools.combinations(syms, k))
    tot = len(list(itertools.combinations(syms, k)))
    page_ok = all(abs(p['z1'] - z1[p['sym']]) < 1e-4 for p in r['pts']) and r['errors'] == obs and r['hits'] == hits and r['total'] == tot
    print(nm, 'errors', obs, 'baseline', hits, '/', tot, '| page agrees:', page_ok)
async def dom():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--use-gl=swiftshader'])
        pg = await b.new_page(); errs_ = []
        pg.on('pageerror', lambda e: errs_.append(str(e)))
        await pg.goto('file://' + os.path.abspath('Periodic_Table_of_Elemental_Peels_v2_1_Jeromie_Beasley.html')); await pg.wait_for_timeout(1500)
        marks = await pg.evaluate("[...document.querySelectorAll('#grid .tile .mv, #grid-f .tile .mv, #grid-a .tile .mv')].map(m=>m.closest('.tile').querySelector('.s').textContent+':'+m.textContent).sort()")
        print('tile marks on the main table:', len(marks), marks)
        out = []
        for z in (24, 46, 57, 92, 103, 26):
            await pg.evaluate(f'openEl({z})'); await pg.wait_for_timeout(300)
            out.append((z, await pg.evaluate("[...document.querySelectorAll('#dbody h4')].some(h=>h.textContent==='Where the electron moves')")))
        print('drawer section present (Fe 26 should be False):', out)
        txt = await pg.evaluate('document.body.innerText')
        print('byline:', re.findall(r'Jeromie Beasley[^\n]*', txt)[:1], '| Codex/Claude/Elizabeth in visible text:', [w for w in ('Codex', 'Claude', 'Elizabeth', 'EJ ') if w in txt])
        print('page errors:', errs_ or 'none'); await b.close()
asyncio.run(dom())
