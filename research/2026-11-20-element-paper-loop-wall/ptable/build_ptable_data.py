# SCRIPT: PERIODIC-TABLE-OF-PEELS-DATA-V1
# Every number on the table, computed from the pinned archive data (element_data_v1.js, built from
# data/element_thresholds_20261011.json.gz), the paper's affinity table, the vacuum-disk paper's optical
# data (votkp_data.json) and the LoopWall.lean theorem index.
import json, math, re
ZW = 3 + 2*math.sqrt(2)
s = open('/home/claude/votkp-lean/research/2026-11-20-element-paper-loop-wall/mixer/element_data_v1.js').read()
D = json.loads(s[s.index('{'):s.rindex('}')+1]); EL = D['el']
gam = lambda z: (z-1)/(z+1)
NOBLE = [2, 10, 18, 36, 54]; CORE = {2:'helium', 10:'neon', 18:'argon', 36:'krypton', 54:'xenon'}
# standard layout (period, column 1-18; lanthanides on row 8)
def place(Z):
    if Z == 1: return 1, 1
    if Z == 2: return 1, 18
    starts = [(3,2),(11,3),(19,4),(37,5),(55,6)]
    for z0, p in reversed(starts):
        if Z >= z0: break
    k = Z - z0
    if p in (2, 3):
        return p, (k+1 if k < 2 else k + 11)
    if p in (4, 5):
        return p, k + 1
    # period 6: Cs Ba La | Ce..Lu row 8 | Hf..
    if k < 3: return 6, k + 1
    if Z <= 71: return 8, Z - 58 + 4
    return 6, Z - 71 + 3
ix = json.load(open('/home/claude/atlas/lean_index.json'))
lean = {d['name']: d for d in ix['votkp-lean@element-paper/loop-wall'] if 'LoopWall.lean' in d['file'] or 'OpeningMap.lean' in d['file']}
vd = json.load(open('/home/claude/knots/vd6/votkp_vacuum_disk_v6/mixer_and_film/mixer/votkp_data.json'))
optic = {}
for e in vd['elements']:
    g2 = [abs((1 - complex(n, k))/(1 + complex(n, k)))**2 for n, k in zip(e['n'], e['k'])]
    optic[e['el']] = {'mean_R': sum(g2)/len(g2), 'metal': e['metal']}
OCT = [('helium octave',[3,4,5,6,7,8,9]),('neon octave',[11,12,13,14,15,16,17]),('argon octave',[19,20,31,32,33,34,35]),('krypton octave',[37,38,49,50,51,52,53]),('xenon octave',[55,56,81,82,83,84,85])]
TONES = ['1+','2+','3+','4','3−','2−','1−']
tone = {Z:(nm,TONES[i]) for nm,Zs in OCT for i,Z in enumerate(Zs)}
out = []
for e in EL:
    Z, ie = e['Z'], e['ie']
    steps = []
    for k in range(len(ie)-1):
        z = ie[k+1]/ie[k]; G = gam(z)
        steps.append({'k': k+1, 'z': z, 'g2': G*G, 'Em': (ie[k+1]-ie[k])**2, 'Ep': (ie[k+1]+ie[k])**2, 'out': z > ZW})
    cores = []
    for N in NOBLE:
        if N < Z:
            q = Z - N - 1; z = ie[q+1]/ie[q]
            cores.append({'core': CORE[N], 'N': N, 'step': q+1, 'z': z, 'g2': gam(z)**2, 'out': z > ZW})
    first = cores[-1] if cores else None
    an = None
    if e['ea']:
        I, A = ie[0], e['ea']; z0 = I/A; G0 = gam(z0); eta = (I-A)/2; chi = (I+A)/2; om = chi*chi/(2*eta)
        an = {'EA': A, 'z0': z0, 'g2': G0*G0, 'eta': eta, 'chi': chi, 'omega': om, 'omega_over_eta': om/eta, 'uptake': 1/G0, 'out': z0 > ZW, 'IExEA': I*A}
    sym = e['s']; name = 'Caesium' if e['n'] == 'Cesium' else e['n']
    A_ = 'none' if not an else ('out' if an['out'] else 'in')
    C_ = 'none' if not first else ('out' if first['out'] else 'in')
    th = [{'name': n, 'file': lean[n]['file'], 'line': lean[n]['line']} for n in sorted(lean) if re.search(r'(^|_)' + sym + r'(_|$)', n)]
    p, c = place(Z)
    out.append({'Z': Z, 'sym': sym, 'name': name, 'period': p, 'col': c, 'ie': ie, 'steps': steps, 'cores': cores,
                'anion': an, 'sig': [A_, C_], 'ledger': math.log(ie[-1]/ie[0]), 'outside': sum(s['out'] for s in steps),
                'optic': optic.get(sym), 'tone': tone.get(Z), 'lean': th})
def rnd(o):
    if isinstance(o, float): return float('%.7g' % o)
    if isinstance(o, list): return [rnd(v) for v in o]
    if isinstance(o, dict): return {k: rnd(v) for k, v in o.items()}
    return o
json.dump(rnd({'wall': ZW, 'elements': out, 'source': 'archive data/element_thresholds_20261011.json.gz; affinities as in the element paper; optics from the vacuum-disk paper v6 (refractiveindex.info)'}), open('ptable_data.json', 'w'), separators=(',', ':'))
# checks against the paper's own numbers
print('steps', sum(len(x['steps']) for x in out), 'outside', sum(x['outside'] for x in out))
print('anions', sum(1 for x in out if x['anion']), 'inside', sum(1 for x in out if x['anion'] and not x['anion']['out']))
m = [x for x in out if x['optic']]; print('optic', len(m), 'metals above |G|^2=1/2:', sum(1 for x in m if x['optic']['metal'] and x['optic']['mean_R'] > .5), 'of', sum(1 for x in m if x['optic']['metal']), '; non-metals above:', sum(1 for x in m if not x['optic']['metal'] and x['optic']['mean_R'] > .5), 'of', sum(1 for x in m if not x['optic']['metal']))
from collections import Counter; print(Counter(tuple(x['sig']) for x in out))
for s_ in ['C','N','O','F','Na','Cl']: x = [y for y in out if y['sym'] == s_][0]; print(s_, x['sig'], x['period'], x['col'], [t['name'] for t in x['lean']][:4])
print(sorted(set((x['period'], x['col']) for x in out)) == sorted((x['period'], x['col']) for x in out))
