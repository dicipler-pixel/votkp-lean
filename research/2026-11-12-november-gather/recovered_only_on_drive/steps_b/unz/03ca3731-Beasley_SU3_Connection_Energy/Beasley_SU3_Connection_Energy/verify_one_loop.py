from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent / "upstream"))

from fractions import Fraction as F
from collections import defaultdict
import su3_character_certificate as su

original = su.matrix_entries
def test(n, lam, z, steps):
    size, entries = original(n, lam, z)
    extended, block = original(n+steps+1, lam, z)
    states = su.states(n+steps+1)
    rows = [dict() for _ in states]
    for (i,j),v in block.items():
        rows[i][j] = rows[j][i] = v
    start = n*(n+1)//2
    columns=[]
    for i in range(start,size):
        b={j:v for j,v in rows[i].items() if j>=size}
        x={}
        r=b
        for _ in range(steps):
            correction={j:v/rows[j][j] for j,v in r.items()}
            for j,v in correction.items():
                x[j]=x.get(j,F(0))+v
            r=defaultdict(F,b)
            for j,v in x.items():
                for k,w in rows[j].items():
                    if k>=size:
                        r[k]-=v*w
        columns.append((b,x,r))
    for i,(b,x,r) in enumerate(columns):
        for j,(bj,xj,rj) in enumerate(columns[i:],i):
            val=sum(v*xj.get(k,0) for k,v in b.items())+sum(v*xj.get(k,0) for k,v in r.items())
            val+=sum(v*rj.get(k,0)/(su.casimir(*states[k])-z) for k,v in r.items())
            key=(start+i,start+j)
            entries[key]=entries.get(key,F(0))-val
    return size,entries

for n in (14,15,16):
    for z in map(F,('57','579/10','59')):
        if z>=su.tail_floor(n): continue
        out=[su.interval_inertia(n,F(100),z,True)[0]]
        for steps in (1,2,3):
            su.matrix_entries=lambda n,lam,z,schur:test(n,lam,z,steps)
            try: out.append(su.interval_inertia(n,F(100),z,True)[0])
            finally: su.matrix_entries=original
        print(n,z,out,flush=True)

for n, z in ((14, F(387, 10)), (17, F(3859, 100)), (14, F(59))):
    print("Variational inertia", n, z, su.interval_inertia(n, lam=F(100), shift=z)[0])

# Reconstruct the two omitted shells that determine the interface mismatch.
cutoff = 15
n, entries = original(cutoff + 2, F(100), F(0))
retained = len(su.states(cutoff))
first_omitted_end = len(su.states(cutoff + 1))
rows = [dict() for _ in range(n)]
for (i, j), value in entries.items():
    rows[i][j] = rows[j][i] = value

mismatch = defaultdict(F)
for i in range(retained, n):
    for j, value in rows[i].items():
        for k, next_value in rows[j].items():
            if k < retained:
                sign = 1 if j >= retained else -1
                mismatch[i, k] += sign * value * next_value

speed = sum(
    value**2 for row in rows[retained:] for j, value in row.items() if j < retained
)
energy = sum(value**2 for value in mismatch.values())
second_shell = sum(
    value**2 for (i, _), value in mismatch.items() if i >= first_omitted_end
)
print("Interface squared speed, connection energy, second-shell contribution:")
print(speed, energy, second_shell)
if (speed, energy, second_shell) != (80000, F(10581880000, 9), 600000000):
    raise SystemExit("Interface result differs from the recorded run.")
