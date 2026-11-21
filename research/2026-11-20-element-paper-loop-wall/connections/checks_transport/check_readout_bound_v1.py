# SCRIPT: WTK-LOOPWALL-READOUT-BOUND-01
"""
Connection: WTK Theorem 3's finite readout-error bound applied to the anion-rung
reflection Gamma_0 = (IE - EA)/(IE + EA) = hardness/electronegativity, and WTK
Theorem 4's coboundary telescoping applied to a peel ladder.

Why this check proves what it claims:
 1. Gamma_0 is a WTK readout: K = p x/(q x) with x = (IE, EA), p = (1, -1), q = (1, 1).
    WTK Theorem 3 bounds the change of the readout under any input error r:
       |p y/q y - K| <= ||p - K q|| ||r|| / (|q x| - ||q|| ||r||).
    With ||r|| at most the Euclidean length of the quoted uncertainties, the bound is a
    guaranteed worst case. If the bound is smaller than the distance |Gamma_0 - 1/sqrt2|
    to the wall, the wall call cannot change anywhere in the uncertainty box, by WTK
    alone. The exact box corners are printed beside it as a cross-check: the bound must
    be at least as large as the true corner excursion.
 2. A peel ladder z_k = IE_{k+1}/IE_k is a one-dimensional coboundary, z_k = U(k+1)/U(k)
    with U = IE. WTK Theorem 4 then says the cumulative transport depends only on the two
    endpoint frames: sum_k h_k = (1/2) ln(IE_last/IE_first). If the summed half-steps of a
    full archive ladder equal the endpoint expression to rounding, the identity is shown
    on data (it is exact algebra). It is why a one-direction ladder carries no curvature,
    and why the loop needs two faces.
"""
import math, gzip, json
ARCH = '/home/claude/votkp-lean/data/element_thresholds_20261011.json.gz'
rec = {r['symbol']: r for r in json.load(gzip.open(ARCH))['records']}
wall = 1/math.sqrt(2)
rows = [('silicon', 'Si', 1.3895212, 0.0000007), ('silver', 'Ag', 1.30447, 0.00002),
        ('iridium', 'Ir', None, None)]
print('1. WTK Theorem 3 bound on Gamma_0 against the distance to the wall')
for name, sym, EA, dEA in rows[:2]:
    t0 = sorted(rec[sym]['thresholds'], key=lambda t: t['q'])[0]
    IE, dIE = t0['IE_eV'], t0['unc_eV']
    K = (IE - EA)/(IE + EA)
    rnorm = math.hypot(dIE, dEA)
    pk = math.hypot(1 - K, -1 - K); qn = math.sqrt(2)
    bound = pk*rnorm/((IE + EA) - qn*rnorm)
    corners = [((IE+a) - (EA+b))/((IE+a) + (EA+b)) for a in (-dIE, dIE) for b in (-dEA, dEA)]
    exc = max(abs(c - K) for c in corners)
    print(f'   {name:8s} Gamma_0 = {K:.8f}, distance to wall = {abs(K-wall):.3e}, WTK bound = {bound:.3e}, '
          f'exact corner excursion = {exc:.3e}, call fixed by the bound: {bound < abs(K-wall)}')
    print(f'            (hardness/electronegativity = {K:.8f}; electrophilicity/hardness = 1/(2 Gamma_0^2) = {1/(2*K*K):.6f})')
print('\n2. WTK Theorem 4 coboundary on full archive ladders')
for sym in ['C', 'Fe', 'Cs']:
    nm = rec[sym]['name']
    ies = [t['IE_eV'] for t in sorted(rec[sym]['thresholds'], key=lambda t: t['q'])]
    s = sum(0.5*math.log(ies[k+1]/ies[k]) for k in range(len(ies)-1))
    print(f'   {nm:9s}: {len(ies)-1:2d} steps, sum h_k = {s:.12f}, (1/2) ln(IE_last/IE_first) = {0.5*math.log(ies[-1]/ies[0]):.12f}')
