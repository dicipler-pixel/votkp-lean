# SCRIPT: ESR-CHECK-01
# Independent recount of the census numbers printed in "VOTKP: Elemental Structure and Response" (11 Nov 2026)
# from the v2.9 threshold archive. A recount can only confirm or contradict the printed integers; it says
# nothing about the paper's readings. Mismatch = the printed number is not reproduced from this archive.
import gzip, json, sys, math
from fractions import Fraction as F
recs = json.load(gzip.open(sys.argv[1]))['records']
slots = sum(r['Z'] for r in recs)
thr = [(r['Z'], t['q'], t['IE_eV'], t.get('grade'), t.get('unc_eV')) for r in recs for t in r['thresholds'] if t.get('IE_eV')]
by = {}
for Z, q, e, g, u in thr: by.setdefault(Z, {})[q] = (e, g, u)
peels = [(Z, q) for Z in by for q in by[Z] if q+1 in by[Z]]
wins = [(Z, q) for Z in by for q in by[Z] if q+1 in by[Z] and q+2 in by[Z]]
gr = {}
for _, _, _, g, _ in thr: gr[g] = gr.get(g, 0) + 1
complete = [Z for Z in by if len(by[Z]) == Z]
partial = [Z for Z in by if 0 < len(by[Z]) < Z]
none = [r['Z'] for r in recs if r['Z'] not in by]
boxes = sum(1 for Z, q in peels if by[Z][q][2] and by[Z][q+1][2])
ee = [(Z, q) for Z, q in peels if by[Z][q][1] == 'E' and by[Z][q+1][1] == 'E']
def row(name, got, printed): print('%-46s got %-22s printed %-12s %s' % (name, got, printed, 'OK' if str(got) == str(printed) else 'DIFFERS'))
row('charge slots', slots, 7021); row('numeric thresholds', len(thr), 5847); row('adjacent peels', len(peels), 5714)
row('three-threshold windows', len(wins), 5584)
row('grades E / S / T', '%d / %d / %d' % (gr.get('E', 0), gr.get('S', 0), gr.get('T', 0)), '311 / 919 / 4617')
row('complete ladders', len(complete), 103); row('partial ladders', len(partial), 7); row('elements with none', len(none), 8)
row('peels with both margins', boxes, 5691); row('E-to-E pairs', len(ee), 156); row('elements holding an E-to-E pair', len({Z for Z, _ in ee}), 60)
# exact inversion and composition in rational arithmetic on the decimal energies
bad = 0
for Z, q in peels:
    a, b = F(str(by[Z][q][0])), F(str(by[Z][q+1][0])); G = (b-a)/(b+a)
    if (1+G)/(1-G) != b/a: bad += 1
badc = 0
for Z, q in wins:
    a, b, c = (F(str(by[Z][q+i][0])) for i in range(3)); g1 = (b-a)/(b+a); g2 = (c-b)/(c+b)
    if (g1+g2)/(1+g1*g2) != (c-a)/(c+a): badc += 1
row('exact inversions failing', bad, 0); row('exact compositions failing', badc, 0)
# half-line crossings, actual charge indices, at closed-core openings (remaining electrons N -> N-1 with N-1 a noble count)
W = 3 + 2*math.sqrt(2); NOBLE = {2, 10, 18, 36, 54, 86}
cross = [(Z, q) for Z, q in peels if by[Z][q+1][0]/by[Z][q][0] > W]
openings = [(Z, q) for Z, q in peels if (Z - q - 1) in NOBLE]
row('steps past the half line', len(cross), 8); row('  of them at a closed-core opening', sum(1 for c in cross if c in openings), 8)
row('closed-core openings (adjacent, true index)', len(openings), 675)
sym = {r['Z']: r['symbol'] for r in recs}
print('   crossings:', ', '.join('%s q=%d' % (sym[Z], q) for Z, q in cross))
G = lambda Z, q: (by[Z][q+1][0]-by[Z][q][0])/(by[Z][q+1][0]+by[Z][q][0])
row('Li: Gamma across 3 -> 2 electrons', '%.7f' % G(3, 0), '0.8669235'); row('O:  Gamma across 3 -> 2 electrons', '%.7f' % G(8, 5), '0.6851797')
