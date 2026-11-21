# SCRIPT: CLAUDE-CHECK-BE-RB-FR-V1
# Independent recompute of Codex's REVIEW_REQUEST items 1-2 from the archive.
# Why this checks it: S = sinh(a)sinh(b) with a = 1/2 ln z_a is computed straight from the archive ladders,
# and the commutator trace 2 - 4 S^2 from the explicit 2x2 matrices, so neither depends on Codex's code.
import gzip, json, hashlib
from mpmath import mp, mpf, sqrt, log, sinh, matrix
mp.dps = 40
arch = '/home/claude/votkp-lean/data/element_thresholds_20261011.json.gz'
print('archive sha256', hashlib.sha256(open(arch,'rb').read()).hexdigest())
d = json.load(gzip.open(arch)); rec = {r['Z']: r for r in d['records']}
def ladder(Z):
    t = {x['q']: x['IE_eV'] for x in rec[Z]['thresholds']}; return [mpf(str(t[q])) for q in sorted(t)]
Be, Rb = ladder(4), ladder(37)
za = Be[2]/Be[1]; zb = Rb[35]/Rb[34]          # Be k=2 (step 2->3), Rb k=35 (step 35->36)
a, b = log(za)/2, log(zb)/2; S = sinh(a)*sinh(b)
from mpmath import exp, cosh
A = matrix([[exp(a),0],[0,exp(-a)]]); B = matrix([[cosh(b),sinh(b)],[sinh(b),cosh(b)]])
W = A*B*A**-1*B**-1; tr = W[0,0]+W[1,1]
print('Be k=2 z_a', za, '| Rb k=35 z_b', zb)
print('S = sinh a sinh b', S, '| trace W', tr, '| 2-4S^2', 2-4*S**2)
print('Gamma_a^2+Gamma_b^2', ((za-1)/(za+1))**2+((zb-1)/(zb+1))**2)
zw = 3+2*sqrt(2); lo, hi = mpf('7.576234')/mpf('1.30447'), mpf('8.15168')/mpf('1.3895212')
for name, c in [('wall', zw), ('window low (Ag)', lo), ('window high (Si)', hi), ('window midpoint in raw z', (lo+hi)/2)]:
    Sc = (c-1)**2/(4*c); print(f'{name:28s} c = {mp.nstr(c,13)}  S_c = sinh^2(1/2 ln c) = {mp.nstr(Sc,13)}  pair outside? {S > Sc}')
IE1 = mpf('4.072741')
print('Fr threshold IE2 (wall)', IE1*zw, '| (midpoint)', IE1*(lo+hi)/2)
# two-period extrapolation of the alkali first openings (Codex quotes 21.8344 eV); one simple version: ratio trend K->Rb->Cs
zs = [ladder(Z)[1]/ladder(Z)[0] for Z in (19,37,55)]
print('alkali openings K, Rb, Cs', [mp.nstr(x,8) for x in zs])
