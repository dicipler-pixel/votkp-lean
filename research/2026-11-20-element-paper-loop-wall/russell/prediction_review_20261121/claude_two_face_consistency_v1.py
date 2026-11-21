# SCRIPT: CLAUDE-TWO-FACE-CONSISTENCY-V1
# Claim to test: a single-step cutoff c extends to two faces in two natural ways,
#   product form  sinh(a) sinh(b) < sinh^2(h_c)      and   sum form  tanh^2 a + tanh^2 b < 2 tanh^2 h_c,
# both agreeing with the one-step cutoff when a = b = h_c. Claim: the two forms define the SAME region only
# when c = 3 + 2 sqrt 2. Why this checks it: if the regions coincide, every pair gets the same call from both;
# a single pair with opposite calls kills the claim for that c. Kill condition written first: if any c in the
# window other than the wall gives zero disagreements on a dense grid, the claim is wrong.
from mpmath import mp, mpf, sqrt, log, sinh, tanh, acosh
mp.dps = 30
zw = 3 + 2*sqrt(2)
def calls(c, za, zb):
    hc, a, b = log(c)/2, log(za)/2, log(zb)/2
    return sinh(a)*sinh(b) < sinh(hc)**2, tanh(a)**2 + tanh(b)**2 < 2*tanh(hc)**2
import itertools
grid = [mpf(1.5) + mpf(i)/8 for i in range(0, 120)]          # z from 1.5 to 16.4
lo, hi = mpf('7.576234')/mpf('1.30447'), mpf('8.15168')/mpf('1.3895212')
for name, c in [('wall', zw), ('Ag end', lo), ('midpoint', (lo+hi)/2), ('Si end', hi*mpf('0.99999'))]:
    dis = sum(1 for za, zb in itertools.combinations(grid, 2) if calls(c, za, zb)[0] != calls(c, za, zb)[1])
    print(f'{name:9s} c = {mp.nstr(c,10)}  pairs where product and sum forms disagree: {dis} of {len(grid)*(len(grid)-1)//2}')
# exact identity at the wall: sinh a sinh b = 1  <=>  tanh^2 a + tanh^2 b = 1
# (tanh^2 a + tanh^2 b - 1)(cosh a cosh b)^2 = sinh^2 a sinh^2 b - 1 ; check symbolically
import sympy as sp
A, B = sp.symbols('a b', positive=True)
lhs = (sp.tanh(A)**2 + sp.tanh(B)**2 - 1)*(sp.cosh(A)*sp.cosh(B))**2 - (sp.sinh(A)**2*sp.sinh(B)**2 - 1)
print('identity residual:', sp.simplify(sp.expand(lhs.rewrite(sp.exp))))
# Codex's quoted threshold 1.001065717132: which construction gives it?
mid = (lo+hi)/2; G = (mid-1)/(mid+1)
print('2 Gamma_mid^2 =', 2*G**2, '| sinh^2 h_mid =', (mid-1)**2/(4*mid))
