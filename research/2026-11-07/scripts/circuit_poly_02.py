# SCRIPT: CIRCUIT-POLY-02
# Repair attempt for CIRCUIT-POLY-01. Tait flyping theorem (Menasco-Thistlethwaite): any two reduced alternating diagrams
# of a knot differ by flypes. So if Q survives flypes, Q read off a reduced alternating diagram is a true invariant of
# alternating knots. Test: for alternating knots, compare Q from KnotInfo's diagram with Q from snappy's own minimal
# alternating diagram, and from redrawn-then-simplified diagrams that come back at minimal crossing number and alternating.
import numpy as np, database_knotinfo as d, snappy, re, random, warnings
warnings.filterwarnings('ignore')
exec(open('circuit_poly_01.py').read().split('# (A) Kirchhoff check')[0])
random.seed(5); alt=[r for r in d.link_list() if r.get('alternating')=='Y' and r['pd_notation'] and re.match(r'^\d',r['name']) and 4<=int(re.match(r'(\d+)',r['name']).group(1))<=11]
tot=same=0; diffs=[]
for r in random.sample(alt,60):
    q0=Q_of(eval(r['pd_notation'])); n0=len(eval(r['pd_notation']))
    try: L=snappy.Link(snapname(r['name']))
    except Exception: continue
    for s in (0,6,12):
        L2=L.copy()
        if s: L2.backtrack(s); L2.simplify('global')
        if len(L2.crossings)!=n0 or not L2.is_alternating(): continue
        q=Q_of(L2.PD_code()); qr=q[::-1]; tot+=1
        ok=(q==q0 or qr==q0); same+=ok
        if not ok: diffs.append((r['name'],q0,q))
print('reduced alternating diagrams compared: %d, Q equal (up to the shading flip): %d'%(tot,same))
for x in diffs[:6]: print('  differs:',x)
