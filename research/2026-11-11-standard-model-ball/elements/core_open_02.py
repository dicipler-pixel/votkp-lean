# SCRIPT: CORE-OPEN-02
# The step that opens each element's outermost closed core (first step into the noble core),
# by period and valence count v = Z - core. Where does each period cross the wall Gamma^2 = 1/2?
# KILL LINE (before running): if the crossing valence count shows no order across periods
# (non-monotone in period), the "each period crosses the wall at one place" reading fails this way.
import json, sys, math
rows = json.load(open(sys.argv[1]))['rows']
import gzip
d = {r['Z']: r for r in json.load(gzip.open(sys.argv[2]))['records']}
CORES = [2, 10, 18, 36, 54, 86]
def G2(z): return ((z-1)/(z+1))**2
for per, core in enumerate(CORES, start=2):
    nxt = CORES[per-1] if per-1 < len(CORES) else 118
    line = []
    for Z in range(core+1, nxt+1):
        r = d[Z]; ie = {t['q']: t['IE_eV'] for t in r['thresholds'] if t.get('IE_eV')}
        v = Z - core; q = v - 1     # step from removing last valence e (q=v-1) to first core e (q=v)
        if q in ie and q+1 in ie:
            g = G2(ie[q+1]/ie[q]); line.append((v, r['symbol'], ie[q+1]/ie[q], g))
    print(f"period {per} (core {core}):")
    print("   " + "  ".join(f"{s}{v}:{z:.2f}/{g:.3f}{'*' if g>.5 else ''}" for v, s, z, g in line))
    past = [v for v, s, z, g in line if g > .5]
    print(f"   past wall at valence {past}")
