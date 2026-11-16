# SCRIPT: W2-SWEEP (watcher phase 2). Kill: recount L4 claims from sweep2.jsonl: 384 cells; 192 z cells; 1920 unequal-free-rate pairs; zero agree within 0.02 in both windows; torque/kappa ranges in the 384.
import json, itertools, collections
rows=[json.loads(l) for l in open('/home/claude/balls/breakdown/scratch/L4/sweep2.jsonl')]
print('cells',len(rows)); print('torques',collections.Counter(r['P']['torque'] for r in rows)); print('kappa',collections.Counter(r['P']['kappa'] for r in rows)); print('signs',collections.Counter(r['P']['sign'] for r in rows)); print('tags',collections.Counter(r['P']['tag'] for r in rows))
z=[r for r in rows if r['P']['clocks']=='z']; print('z cells',len(z))
pairs=0; agree=0; close=[]
for r in z:
    fr=r['free']; w=r['rates']; n=len(fr)
    for i,j in itertools.combinations(range(n),2):
        if abs(fr[i]-fr[j])>0.02:
            pairs+=1
            gaps=[abs(w[k][i]-w[k][j]) for k in range(2)]
            if max(gaps)<0.02: agree+=1
            close.append(max(gaps))
print('pairs',pairs,'agree both windows',agree,'smallest max-gap',min(close))
print('rates per row example',z[0]['rates'])
