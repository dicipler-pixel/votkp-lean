# SCRIPT: G1_ARCHIVE_RECOMPUTE
# Recomputes from the threshold archive every count/number quoted in G1 files.
import gzip, json, math, itertools
d = json.load(gzip.open('/home/claude/votkp-lean/data/element_thresholds_20261011.json.gz'))
rec = {r['Z']: r for r in d['records']}
W = 3 + 2*math.sqrt(2)
steps = []  # (Z,name,k,z,G2)
for Z in range(1, 86):
    th = sorted(rec[Z]['thresholds'], key=lambda x: x['q'])
    E = [x['IE_eV'] for x in th if x.get('IE_eV') is not None]
    for k in range(len(E)-1):
        z = E[k+1]/E[k]; G = (z-1)/(z+1)
        steps.append((Z, rec[Z]['name'], k+1, z, G*G, E[k], E[k+1]))
print('ordinary steps', len(steps))
out = [s for s in steps if s[3] > W]
print('outside', len(out), [(s[1], s[2]) for s in out])
near = sorted(steps, key=lambda s: abs(s[4]-0.5))[:5]
print('nearest to G2=0.5:', [(s[1], s[2], round(s[4], 5)) for s in near])
# exact integer test 2(b-a)^2 > (b+a)^2 agrees
dis = sum(((2*(s[6]-s[5])**2 > (s[6]+s[5])**2) != (s[3] > W)) for s in steps)
print('integer-test disagreements', dis)
# composition law on k,k+2 pairs
worst = 0; npair = 0
for Z in range(1, 86):
    th = sorted(rec[Z]['thresholds'], key=lambda x: x['q'])
    E = [x['IE_eV'] for x in th if x.get('IE_eV') is not None]
    for k in range(len(E)-2):
        g = lambda z: (z-1)/(z+1)
        a = g(E[k+1]/E[k]); b = g(E[k+2]/E[k+1]); c = g(E[k+2]/E[k])
        worst = max(worst, abs(c-(a+b)/(1+a*b))); npair += 1
print('pairs', npair, 'worst oplus residual', worst)
# shift/scale invariance of ratio claim: the claim in paper: E -> sE + c changes no z or Gamma
# NOTE: a shift c does NOT leave ratio b/a unchanged in general; test literally
s_, c_ = 1000.0, 0.0
w2 = 0
for st in steps:
    a, b = st[5], st[6]
    g1 = (b-a)/(b+a); g2 = ((s_*b+c_)-(s_*a+c_))/((s_*b+c_)+(s_*a+c_)); w2 = max(w2, abs(g1-g2))
print('pure scale (c=0) worst', w2)
c_ = 5.0
w3 = 0
for st in steps:
    a, b = st[5], st[6]
    g1 = (b-a)/(b+a); g2 = ((s_*b+c_)-(s_*a+c_))/((s_*b+c_)+(s_*a+c_)); w3 = max(w3, abs(g1-g2))
print('scale + shift c=5 worst change in Gamma if shift applied to energies themselves:', w3)
# telescoping
print('=== core sequences')
cores = {'He': (3, 2), 'Ne': (11, 10), 'Ar': (19, 18), 'Kr': (37, 36), 'Xe': (55, 54)}
ends = {'He': 10, 'Ne': 18, 'Ar': 36, 'Kr': 54, 'Xe': 85}
for c, (z0, nz) in cores.items():
    seq = []
    for Z in range(z0, ends[c]+1):
        k = Z - nz  # step index: removing valence electrons count k-1 then core
        S = [s for s in steps if s[0] == Z and s[2] == k]
        if S: seq.append((rec[Z]['symbol'], round(S[0][3], 3), S[0][3] > W))
    flags = [x[2] for x in seq]
    crossings = sum(1 for i in range(1, len(flags)) if flags[i] != flags[i-1])
    print(c, 'n=', len(seq), 'outside-first run:', flags[0], 'crossings', crossings, [x[0]+(':OUT' if x[2] else '') for x in seq][:14])
# scale+shift invariance on charge-state energy ladders
worst = 0
for Z in range(1, 86):
    th = sorted(rec[Z]['thresholds'], key=lambda x: x['q'])
    E = [x['IE_eV'] for x in th if x.get('IE_eV') is not None]
    cum = [0.0]
    for e in E: cum.append(cum[-1]-e)  # charge-state energies relative to neutral
    for s_, c_ in [(37.0, 123.0), (1/27.2114, -7.5)]:
        cum2 = [s_*x + c_ for x in cum]
        IE2 = [cum2[i+1]-cum2[i] for i in range(len(E))]
        for i in range(len(E)-1):
            z1 = E[i+1]/E[i]; z2 = IE2[i+1]/IE2[i]
            worst = max(worst, abs((z1-1)/(z1+1)-(z2-1)/(z2+1)), abs(z1-z2)/z1)
print('E->sE+c worst z-rel / Gamma change', worst)
