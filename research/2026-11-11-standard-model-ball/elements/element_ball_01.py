# SCRIPT: ELEMENT-BALL-01
# Every element's ionisation ladder run through the ball (11 Nov 2026).
# Step q: z_q = IE_{q+1}/IE_q, Gamma = (z-1)/(z+1) = tanh(1/2 ln z), wall Gamma^2 = 1/2 (z = 3+2sqrt2).
# Shell block: all steps inside one noble-gas shell composed into one boost (rapidities add):
#   r = IE_last/IE_first in the block, Gamma_block^2 = ((r-1)/(r+1))^2.
# KILL LINES (written before running):
#  K1 closure: the largest step of each element (>=2 shells of data) sits at a noble-core boundary
#     in >= 90% of elements. Fails this way if < 90%.
#  K2 shell at the wall: whole-shell blocks (>=3 electrons) have median |Gamma_block^2 - 1/2| at most
#     half that of random contiguous blocks of the same length from the same ladders, with p < 0.01
#     (5000 shuffles). Fails this way otherwise. Opposite tried too: is the shell block past the wall
#     (converted as a whole) more often than random blocks?
#  K3 books: per step E-/E+ = Gamma^2. Count the elements whose ladder has a step on the wall to 2%.
import gzip, json, math, random, sys
d = json.load(gzip.open(sys.argv[1]))['records']
W = 3 + 2*math.sqrt(2)
NOBLE = {0, 2, 10, 18, 36, 54, 86, 118}
def G2(z): return ((z-1)/(z+1))**2
rows, blocks, allsteps, ladders = [], [], [], {}
for r in d:
    Z, s = r['Z'], r['symbol']
    ie = {t['q']: t['IE_eV'] for t in r['thresholds'] if t.get('IE_eV')}
    qs = sorted(ie)
    lad = [ie[q] for q in qs if q < Z]
    # contiguous from q=0 only
    n = 0
    while n < len(qs) and qs[n] == n: n += 1
    lad = [ie[q] for q in range(n)]
    ladders[s] = lad
    full = (n == Z)
    steps = []
    for q in range(len(lad)-1):
        z = lad[q+1]/lad[q]
        left = Z - q - 1           # electrons left after removing electron q
        steps.append(dict(q=q, z=z, g2=G2(z), bnd=(left in NOBLE)))
        allsteps.append((s, Z, q, z, G2(z), left in NOBLE))
    # shell blocks: electron indices q .. between boundaries (electron q removed from ion with Z-q e)
    cuts = [q+1 for q in range(len(lad)-1) if (Z-q-1) in NOBLE]
    edges = [0] + cuts + [len(lad)]
    for a, b in zip(edges, edges[1:]):
        if b - a >= 3:
            rr = lad[b-1]/lad[a]
            blocks.append(dict(s=s, Z=Z, a=a, n=b-a, r=rr, g2=G2(rr)))
    big = max(steps, key=lambda x: x['z']) if steps else None
    near = min(steps, key=lambda x: abs(x['g2']-.5)) if steps else None
    rows.append(dict(Z=Z, s=s, n=len(lad), full=full, nsh=len(cuts)+1,
        big_q=big and big['q'], big_z=big and big['z'], big_g2=big and big['g2'], big_bnd=big and big['bnd'],
        near_q=near and near['q'], near_g2=near and near['g2'],
        past=[x['q'] for x in steps if x['g2'] > .5],
        eta_tot=math.log(lad[-1]/lad[0]) if len(lad) > 1 else 0))
print(f"elements {len(rows)}, full ladders {sum(r['full'] for r in rows)}, steps {len(allsteps)}")
# K1
el = [r for r in rows if r['nsh'] >= 2 and r['big_q'] is not None]
hit = [r for r in el if r['big_bnd']]
print(f"\nK1 largest step at a noble-core boundary: {len(hit)}/{len(el)} = {len(hit)/len(el):.3f}  -> {'PASSES' if len(hit)/len(el)>=.9 else 'FAILS THIS WAY'}")
print("   misses:", ' '.join(f"{r['s']}(q={r['big_q']},z={r['big_z']:.2f})" for r in el if not r['big_bnd']))
# K2
random.seed(1)
dev = sorted(abs(b['g2']-.5) for b in blocks)
med = dev[len(dev)//2]
pool = [l for l in ladders.values() if len(l) >= 3]
def rand_block(n):
    while True:
        l = random.choice(pool)
        if len(l) >= n:
            a = random.randrange(len(l)-n+1); return G2(l[a+n-1]/l[a])
meds, pasts = [], []
past_obs = sum(b['g2'] > .5 for b in blocks)/len(blocks)
for _ in range(5000):
    g = [rand_block(b['n']) for b in blocks]
    dv = sorted(abs(x-.5) for x in g); meds.append(dv[len(dv)//2]); pasts.append(sum(x>.5 for x in g)/len(g))
p = sum(m <= med for m in meds)/len(meds)
cm = sorted(meds)[len(meds)//2]
print(f"\nK2 shell blocks n={len(blocks)}: median |G2-1/2| = {med:.4f}, random median {cm:.4f}, ratio {med/cm:.3f}, p = {p:.4f}")
print("   ->", 'PASSES' if (med <= cm/2 and p < .01) else 'FAILS THIS WAY')
pp = sum(x >= past_obs for x in pasts)/len(pasts)
print(f"   opposite: shell blocks past the wall {past_obs:.3f} vs random {sorted(pasts)[len(pasts)//2]:.3f} (p of >= observed {pp:.4f})")
# shell block table by shell size
from collections import defaultdict
bys = defaultdict(list)
for b in blocks: bys[b['n']].append(b)
print("   by shell size n: count, median Gamma_block^2, fraction past wall")
for n in sorted(bys):
    g = sorted(x['g2'] for x in bys[n]); print(f"     n={n:2d}  {len(g):3d}  {g[len(g)//2]:.4f}  {sum(x>.5 for x in g)/len(g):.2f}")
# K3
on = [r for r in rows if r['near_g2'] is not None and abs(r['near_g2']-.5) <= .01]
print(f"\nK3 elements with a step within 0.01 of the wall: {len(on)}:", ' '.join(f"{r['s']}(q={r['near_q']},G2={r['near_g2']:.4f})" for r in on))
# per-element table
print("\nZ  sym  steps shells  biggest(q,z,G2,at core)   nearest-wall(q,G2)  past-wall  eta_total")
for r in rows:
    if r['big_q'] is None: print(f"{r['Z']:3d} {r['s']:3s} {r['n']:3d}  -"); continue
    print(f"{r['Z']:3d} {r['s']:3s} {r['n']:3d}{'*' if r['full'] else ' '} {r['nsh']:2d}   q={r['big_q']:3d} z={r['big_z']:7.3f} G2={r['big_g2']:.3f} {'core' if r['big_bnd'] else 'IN-SHELL'}   q={r['near_q']:3d} {r['near_g2']:.4f}   {r['past'] or ''}  {r['eta_tot']:.3f}")
json.dump(dict(rows=rows, blocks=blocks), open(sys.argv[2], 'w'))
