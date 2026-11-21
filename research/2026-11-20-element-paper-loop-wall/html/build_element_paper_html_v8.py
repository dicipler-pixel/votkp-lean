# SCRIPT: VOTKP-ELEMENT-PAPER-HTML-V8
# Builds the element-paper breakdown page (hydrogen to astatine) from Jeromie's threshold archive, the evaluated
# electron affinities, and the Lean inventory. Every number in the tables is computed here.
import gzip, json, math, html, sys, re
import csv
import hashlib
from pathlib import Path
ARCH = sys.argv[1]; LEANDIR = sys.argv[2]; OUT = sys.argv[3]
d = json.load(gzip.open(ARCH)); rec = {r['Z']: r for r in d['records']}
W = 3 + 2 * math.sqrt(2)
# Use the same affinity inputs and evidence categories as the reviewed element packets.
PAPER = Path(__file__).resolve().parents[1]
if hashlib.sha256(Path(ARCH).read_bytes()).hexdigest() != '75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c':
    raise ValueError('Ionization archive differs from the pin')
def records(path):
    with path.open(newline='') as source:
        return list(csv.DictReader(source))

EA, status_text = {}, {}
for source_row in records(PAPER/'batch12/chemistry/anion_chemistry_h_nd.csv'):
    symbol = source_row['symbol']
    EA[symbol] = float(source_row['EA_eV'])
    status_text[symbol] = 'estimated' if source_row['EA_status']=='estimated' else ''
for source_row in records(PAPER/'batch12/chemistry/no_bound_anion_h_nd.csv'):
    status_text[source_row['symbol']] = 'no bound ground-state anion in adopted ledger'
for batch in range(13,18):
    for source_row in records(PAPER/f'batch{batch}/ladder/affinities.csv'):
        symbol, status = source_row['symbol'], source_row['status']
        if source_row['EA_eV']:
            EA[symbol] = float(source_row['EA_eV'])
        if status == 'measured-lower-bound':
            label = 'bound; EA > ' + source_row['lower_bound_eV'] + ' eV'
        elif status == 'experimental-upper-limit-no-established-bound-anion':
            label = 'no established bound anion; experimental upper limit ' + source_row['upper_bound_eV'] + ' eV'
        else:
            label = {'theory-only':'theory only; no adopted measured EA',
                     'preliminary-measurement':'preliminary measurement',
                     'evaluated-AMS-estimate':'estimated affinity',
                     'evaluated-AMS-estimate-disputed':'disputed estimate',
                     'evaluated-no-stable-ground-anion':'no stable ground anion in evaluation',
                     'no established bound ground anion':'no established bound ground anion',
                     'observed-preliminary-systematics-outstanding':'bound; preliminary threshold, systematics outstanding'}.get(status,'')
        if symbol not in EA and not label:
            raise ValueError(f'Unrendered missing-point status for {symbol}: {status}')
        status_text[symbol] = label
if set(status_text) != {rec[i]['symbol'] for i in range(1,86)}:
    raise ValueError('Incomplete anion source coverage')
def th(Z): return {t['q']: t['IE_eV'] for t in rec[Z]['thresholds']}
def gam(z): return (z - 1) / (z + 1)
def cell(z, label=''):
    if z is None: return '<td class="na">—</td>'
    cls = 'out' if z > W else 'in'
    return f'<td class="{cls}">{z:.4f}<span class="g">Γ {gam(z):.4f}</span></td>'
# opening for a core of N electrons: IE(q+1)/IE(q), q = Z-N-1
def opening(Z, N):
    t = th(Z); q = Z - N - 1
    return t[q+1] / t[q] if q >= 0 and q in t and q+1 in t else None
rows = []
for Z in range(1, 86):
    s = rec[Z]['symbol']; t = th(Z)
    r0 = (t[0] / EA[s]) if s in EA else None
    K = opening(Z, 2) if Z >= 3 else None
    L = opening(Z, 10) if Z >= 11 else None
    M = opening(Z, 18) if Z >= 19 else None
    N4 = opening(Z, 36) if Z >= 37 else None
    N5 = opening(Z, 54) if Z >= 55 else None
    rows.append((Z, s, rec[Z]['name'], r0, K, L, M, N4, N5, s in EA))
def row_html(r):
    Z, s, name, r0, K, L, M, N4, N5, bound = r
    annotation = html.escape(status_text[s])
    if bound:
        r0c = cell(r0)
        if annotation:
            r0c = r0c.replace('</td>', f'<span class="g">{annotation}</span></td>')
    else:
        r0c = f'<td class="na">{annotation}</td>' 
    return f'<tr><td class="el"><b>{s}</b> <span class="zz">{Z}</span></td>{r0c}{cell(K)}{cell(L)}{cell(M)}{cell(N4)}{cell(N5)}</tr>'
table = '\n'.join(row_html(r) for r in rows)
# opening-map SVG: ratio vs Z for each noble core, log scale, wall line
cores = [(2,'He core','#e8c46a'),(10,'Ne core','#f0a050'),(18,'Ar core','#7fc8ff'),(36,'Kr core','#9fe08a'),(54,'Xe core','#d79bff'),(86,'Rn core','#ff8a8a')]
Wd, Ht, ml, mr, mt, mb = 900, 420, 60, 20, 20, 50
def X(Z): return ml + (Z - 1) / 117 * (Wd - ml - mr)
lo, hi = math.log(1.0), math.log(16.0)
def Y(z): return mt + (hi - math.log(z)) / (hi - lo) * (Ht - mt - mb)
svg = [f'<svg viewBox="0 0 {Wd} {Ht}" class="plot" role="img" aria-label="Opening ratio against atomic number for each noble core">']
for v in (1, 2, 4, 8, 16):
    svg.append(f'<line x1="{ml}" x2="{Wd-mr}" y1="{Y(v):.1f}" y2="{Y(v):.1f}" class="grid"/><text x="{ml-8}" y="{Y(v)+4:.1f}" class="ax" text-anchor="end">{v}</text>')
for zt in (1, 20, 40, 60, 80, 100, 118):
    svg.append(f'<text x="{X(zt):.1f}" y="{Ht-mb+18}" class="ax" text-anchor="middle">{zt}</text>')
svg.append(f'<text x="{(ml+Wd-mr)/2}" y="{Ht-8}" class="ax" text-anchor="middle">atomic number Z</text>')
svg.append(f'<line x1="{ml}" x2="{Wd-mr}" y1="{Y(W):.1f}" y2="{Y(W):.1f}" class="wall"/><text x="{X(72):.1f}" y="{Y(W)+17:.1f}" class="wallt" text-anchor="middle">loop wall z = 3 + 2√2</text>')
for N, lab, col in cores:
    pts = [(Z, opening(Z, N)) for Z in range(N+1, 119)]; pts = [(Z, z) for Z, z in pts if z]
    if not pts: continue
    path = ' '.join(f'{X(Z):.1f},{Y(z):.1f}' for Z, z in pts)
    svg.append(f'<polyline points="{path}" fill="none" stroke="{col}" stroke-width="1.8"/>')
    Z0, z0 = pts[0]
    svg.append(f'<circle cx="{X(Z0):.1f}" cy="{Y(z0):.1f}" r="4" fill="{col}"/><text x="{X(Z0)+6:.1f}" y="{Y(z0)-(16 if z0<6.5 else 6):.1f}" class="lab" fill="{col}">{lab}: {rec[Z0]["symbol"]} {z0:.2f}</text>')
svg.append('</svg>')
svg = '\n'.join(svg)
first = []
for N, lab, col in cores:
    pts = [(Z, opening(Z, N)) for Z in range(N+1, 119)]; pts = [(Z, z) for Z, z in pts if z]
    outs = [rec[Z]['symbol'] for Z, z in pts if z > W]
    first.append(f'<tr><td>{lab}</td><td>{len(pts)}</td><td>{rec[pts[0][0]]["symbol"]} {pts[0][1]:.3f}</td><td>{", ".join(outs) if outs else "none (Fr straddles)"}</td></tr>')
first = '\n'.join(first)
# screening readouts
Eh = 27.211386245981; sr = []
for Z in range(2, 86):
    t = th(Z); h = t[Z-1]/Eh; b = t[Z-2]/Eh; S = (h-b)/Z; sg = Z - math.sqrt(2*b)
    sr.append(f'<tr><td>{rec[Z]["symbol"]}</td><td>{S:.5f}</td><td>{sg:.5f}</td><td class="{"out" if S > sg else "in"}">{S-sg:+.5f}</td></tr>')
sr = '\n'.join(sr)
# chemistry table: hardness over electronegativity at every bound anion rung
chem = []
for Z in range(1, 86):
    sy = rec[Z]['symbol']
    if sy not in EA: continue
    I = th(Z)[0]; A = EA[sy]; z = I/A; g = (I-A)/(I+A)
    grade = html.escape(status_text[sy])
    name = html.escape(rec[Z]['name']) + (f' <small>({grade})</small>' if grade else '')
    chem.append((1/(2*g*g), f'<tr><td>{name}</td><td class="{"out" if z > W else "in"}">{z:.4f}</td><td>{g:.5f}</td><td class="{"out" if z > W else "in"}">{1/(2*g*g):.4f}</td></tr>'))
chem = '\n'.join(r for _, r in sorted(chem, reverse=True))
# Lean inventory
def thms(f): return len(re.findall(r'^theorem ', open(f).read(), re.M))
nLW = thms(f'{LEANDIR}/LoopWall.lean'); nOM = thms(f'{LEANDIR}/OpeningMap.lean')
page = open(f'{sys.argv[4]}').read()
page = page.replace('%%TABLE%%', table).replace('%%SVG%%', svg).replace('%%FIRST%%', first).replace('%%SR%%', sr).replace('%%CHEM%%', chem)
page = page.replace('%%NLW%%', str(nLW)).replace('%%NOM%%', str(nOM)).replace('%%NT%%', str(nLW + nOM))
open(OUT, 'w').write(page)
print('written', OUT, nLW, nOM)
