"""Check the occupancy implementation against exhaustive small matchings and real rows."""
from collections import Counter
from itertools import product, permutations
from traits import compare, load, DIR

orb=('1s','2s','2p')
n=0
for b in product(range(3),repeat=3):
    for a in product(range(3),repeat=3):
        if sum(b)!=sum(a)+1:
            continue
        before=[o for o,c in zip(orb,b) for _ in range(c)]
        after=[o for o,c in zip(orb,a) for _ in range(c)]
        # All assignments of surviving slots to distinct initial slots, allowing
        # a change of subshell at unit cost. The omitted initial slot is removed.
        best=min((sum(x!=y for x,y in zip(p,after)) for p in permutations(before,len(after))), default=0)
        m=compare(Counter(before),Counter(after))
        assert m['R']==best and m['K']==len(after)-best
        n+=1
print('Exhaustive small pairs agreed with assignment minimum:',n)
ledger=load(DIR/'occupancy_ledger.csv')
def get(z,k):
    return next(r for r in ledger if int(r['Z'])==z and int(r['removal_k'])==k)
assert (get(64,14)['R'],get(64,14)['K'],get(64,14)['lost'],get(64,14)['gained'])==('2','48','4f:3','5s:2')
print('Counterexample to R<=1:',get(64,14)['element'],'removal 14, R=2')
assert get(57,1)['R']=='1' and get(57,57)['K']==get(57,57)['R']=='0'
print('Neutral lanthanum has R=1; final H-like -> bare has K=R=0')
alts=load(DIR/'alternative_configurations.csv')
r=next(a for a in alts if a['symbol']=='Nd' and a['removal_k']=='6' and a['model']=='Carvajal_2024')
assert r['changes_R']=='False' and r['changes_identity']=='True'
print('Same R can lose different orbital identities: neodymium removal 6')
for wrong in [(Counter({'1s':3}),Counter({'1s':2})),(Counter({'1s':2}),Counter())]:
    try:
        compare(*wrong)
    except ValueError:
        print('Rejected invalid pair',dict(wrong[0]),dict(wrong[1]))
    else:
        raise ValueError('Accepted invalid state')
