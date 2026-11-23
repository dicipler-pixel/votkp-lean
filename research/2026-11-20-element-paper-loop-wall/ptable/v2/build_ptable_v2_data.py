# SCRIPT: PERIODIC-TABLE-OF-PEELS-DATA-V2
# Extends the v1 data (ptable_data.json, identical to the v1.1 embedded data) with per-step derived
# readings, threshold grades and uncertainties, radon-to-darmstadtium ladders, three decay pairs,
# the silver-silicon window and neighbouring core-opening pairs. Every number comes from the archive
# data/element_thresholds_20261011.json.gz or from the v1 data; nothing is typed in by hand except
# the three neutral mass anchors, each with its source.
import json, gzip, math
B = '/home/claude/votkp-lean/'
R = B + 'research/2026-11-20-element-paper-loop-wall/'
ZW = 3 + 2*math.sqrt(2)
gam = lambda z: (z-1)/(z+1)
v1 = json.load(open(R + 'ptable/ptable_data.json'))
arc = {r['Z']: r for r in json.load(gzip.open(B + 'data/element_thresholds_20261011.json.gz'))['records']}

def derived(z):
    G = gam(z); g2 = G*G; a = math.tanh(math.log(z)/4)
    d = {'a': a, 'P1s': (1-a*a)**3, 'S': -0.5*math.log(1-g2)}
    if g2 < 0.5:
        RT = g2/(1-g2); c = 1 - 2*RT*RT
        d['theta'] = math.degrees(2*math.acos(max(-1, min(1, c)))); d['K'] = 1/(1-2*g2); d['regime'] = 'turn'
    else:
        d['theta'] = None; d['K'] = 1/(1-2*g2); d['regime'] = 'run'
    return d

NOBLE = {2: 'helium', 10: 'neon', 18: 'argon', 36: 'krypton', 54: 'xenon', 86: 'radon'}
EL = v1['elements']
for e in EL:
    th = arc[e['Z']]['thresholds']
    e['grade'] = [t['grade'] for t in th]; e['unc'] = [t['unc_eV'] for t in th]
    for s in e['steps']: s.update(derived(s['z']))
    if e['steps']:
        k = max(range(len(e['steps'])), key=lambda i: e['steps'][i]['z'])
        e['strongest'] = {'step': k+1, 'z': e['steps'][k]['z'], 'g2': e['steps'][k]['g2']}
    e['heavy'] = False

# period 7 and actinide placement
def place7(Z):
    if Z in (87, 88): return 7, Z-86
    if Z == 89: return 7, 3
    if 90 <= Z <= 103: return 9, Z-90+4
    return 7, Z-104+4
NAMES = {}
for Z in range(86, 119):
    r = arc[Z]; th = r['thresholds']
    if Z == 86: per, col = 6, 18
    else: per, col = place7(Z)
    e = {'Z': Z, 'sym': r['symbol'], 'name': r['name'], 'period': per, 'col': col, 'heavy': True,
         'ie': [t['IE_eV'] for t in th], 'q': [t['q'] for t in th], 'grade': [t['grade'] for t in th],
         'unc': [t['unc_eV'] for t in th], 'complete': [t['q'] for t in th] == list(range(Z)) and len(th) > 0,
         'steps': [], 'cores': [], 'anion': None, 'optic': None, 'tone': None, 'lean': []}
    for i in range(len(th)-1):
        if th[i+1]['q'] == th[i]['q'] + 1:
            z = th[i+1]['IE_eV']/th[i]['IE_eV']; G = gam(z)
            s = {'k': th[i]['q']+1, 'z': z, 'g2': G*G, 'Em': (th[i+1]['IE_eV']-th[i]['IE_eV'])**2,
                 'Ep': (th[i+1]['IE_eV']+th[i]['IE_eV'])**2, 'out': z > ZW}
            s.update(derived(z)); e['steps'].append(s)
    qi = {t['q']: t['IE_eV'] for t in th}
    for N, cn in NOBLE.items():
        q = Z - N - 1
        if N < Z and q in qi and q+1 in qi:
            z = qi[q+1]/qi[q]
            e['cores'].append({'core': cn, 'N': N, 'step': q+1, 'z': z, 'g2': gam(z)**2, 'out': z > ZW})
    fc = e['cores'][-1] if e['cores'] else None
    e['sig'] = ['none', 'none' if not fc else ('out' if fc['out'] else 'in')]
    e['outside'] = sum(s['out'] for s in e['steps'])
    e['ledger'] = math.log(e['ie'][-1]/e['ie'][0]) if e['complete'] else None
    if e['steps']:
        k = max(range(len(e['steps'])), key=lambda i: e['steps'][i]['z'])
        e['strongest'] = {'step': e['steps'][k]['k'], 'z': e['steps'][k]['z'], 'g2': e['steps'][k]['g2']}
    EL.append(e)

# decay pairs: Q(q) = Q0 + sum_{j<=q} (I_H,j - I_L,j)
ie = {e['Z']: e['ie'] for e in EL}
PAIRS = [
 ('Ho-163', 'Dy-163', 67, 66, 2863.2, 'Neutral Q 2863.2(6) eV, as adopted in the element paper decay section.'),
 ('Re-187', 'Os-187', 75, 76, 2470.9, 'Neutral mass difference 2470.9(13) eV, PENTATRAP Penning trap (arXiv 2108.07039).'),
 ('Pb-205', 'Tl-205', 82, 81, 50600.0, 'Neutral Q about 50.6 keV, the anchor that reproduces the element paper 79+ value of +37.545 keV.')]
decay = []
for hn, ln_, H, L, Q0, src in PAIRS:
    n = min(len(ie[H]), len(ie[L])); Q = [Q0]
    for j in range(n): Q.append(Q[-1] + ie[H][j] - ie[L][j])
    flips = [i for i in range(1, len(Q)) if (Q[i] > 0) != (Q[i-1] > 0)]
    decay.append({'heavier': hn, 'lighter': ln_, 'ZH': H, 'ZL': L, 'Q0': Q0, 'Q': Q, 'flips': flips, 'src': src})

# silver-silicon window: forward cutoffs consistent with all labels
an = [(e['anion']['z0'], e['sym'], e['anion']['out']) for e in EL if e.get('anion')]
st = [(s['z'], e['sym'] + ' step ' + str(s['k']), s['out']) for e in EL if not e['heavy'] for s in e['steps'] if s['z'] > 1]
allp = an + st
lo = max(z for z, _, o in allp if not o); hi = min(z for z, _, o in allp if o)
lo_n = [n for z, n, o in allp if not o and z == lo][0]; hi_n = [n for z, n, o in allp if o and z == hi][0]
near = sorted(allp, key=lambda t: abs(math.log(t[0]/ZW)))[:16]
window = {'lo': lo, 'lo_name': lo_n, 'hi': hi, 'hi_name': hi_n, 'near': [{'z': z, 'name': n, 'out': o} for z, n, o in near]}

# neighbouring first-core-opening pairs (same core, consecutive Z, H to At)
faces = []
for cn in ['helium', 'neon', 'argon', 'krypton', 'xenon']:
    pts = [(e['Z'], e['sym'], c) for e in EL if not e['heavy'] for c in e['cores'] if c['core'] == cn]
    for (Za, sa, ca), (Zb, sb, cb) in zip(pts, pts[1:]):
        if Zb == Za + 1:
            faces.append({'core': cn, 'a': sa, 'b': sb, 'ga2': ca['g2'], 'gb2': cb['g2'], 'sum': ca['g2'] + cb['g2'], 'open': ca['g2'] + cb['g2'] > 1})

def rnd(o):
    if isinstance(o, float): return float('%.7g' % o)
    if isinstance(o, list): return [rnd(v) for v in o]
    if isinstance(o, dict): return {k: rnd(v) for k, v in o.items()}
    return o
out = {'wall': ZW, 'elements': EL, 'decay': decay, 'window': window, 'faces': faces, 'source': v1['source'] + '; heavy ladders and grades from the same archive'}
json.dump(rnd(out), open('ptable_v2_data.json', 'w'), separators=(',', ':'))

# report
L = [e for e in EL if not e['heavy']]; Hv = [e for e in EL if e['heavy']]
print('H-At steps', sum(len(e['steps']) for e in L), 'outside', sum(e['outside'] for e in L))
print('anions', sum(1 for e in L if e['anion']), 'outside', sum(1 for e in L if e['anion'] and e['anion']['out']))
print('heavy elements', len(Hv), 'complete', sum(e['complete'] for e in Hv), 'with data', sum(1 for e in Hv if e['ie']))
print('heavy steps', sum(len(e['steps']) for e in Hv), 'outside', sum(e['outside'] for e in Hv))
for e in Hv:
    for s in e['steps']:
        if s['out']: print('  OUT', e['sym'], 'step', s['k'], 'z=%.5f' % s['z'], 'grades', e['grade'][s['k']-1] + e['grade'][s['k']], [c['core'] for c in e['cores'] if c['step'] == s['k']])
for e in Hv[:3]:
    print(e['sym'], [(c['core'], c['step'], round(c['z'], 4), c['out']) for c in e['cores']])
print('window', window['lo'], window['lo_name'], window['hi'], window['hi_name'])
for d in decay: print(d['heavier'], d['lighter'], 'flips', d['flips'], 'bare', round(d['Q'][-1]/1000, 3))
print('faces', len(faces), 'open', [(f['a'], f['b'], round(f['sum'], 4)) for f in faces if f['open']])
print('near-one face pairs', sorted([(round(f['sum'], 4), f['a'], f['b']) for f in faces], key=lambda t: abs(t[0]-1))[:4])
