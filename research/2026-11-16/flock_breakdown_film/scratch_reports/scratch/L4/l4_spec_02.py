# SCRIPT: L4-SPEC-02  frame-free check on sweep2.jsonl, clocks z only.
# What it asks: do two balls with DIFFERENT free rates show the same spectral peak (nu_up of the amplitude on the rest-field up state, last half of the run)?
# Locked clocks would share a peak that neither free rate has. Coincidence = |nu_i - nu_j| < 0.03 (the Hann window of 200 time units resolves about 0.03) for both balls heavy (weight > 0.02 for half of the samples).
# KILL LINE (written before the run): z-clock locking is NOT supported if the fraction of heavy pairs that coincide is less than twice the fraction found when the same
# peaks are paired at random across different cells (20000 random pairings, seed 1).
import json, random, itertools
rows=[json.loads(l) for l in open('sweep2.jsonl') if l.strip()]
rows=[r for r in rows if r['P']['clocks']=='z' and r['P'].get('sinkRate',0)==0]
obs=[];peaks=[]
for r in rows:
    n=len(r['free']); hv=[i for i in range(n) if r['heavy'][i]>=0.5]
    for i,j in itertools.combinations(hv,2):
        if abs(r['free'][i]-r['free'][j])>0.02:
            for key in ('up','dn'):
                a=r['spec'][i][key]['nu']; b=r['spec'][j][key]['nu']; obs.append(abs(a-b)<0.03)
    for i in hv:
        for key in ('up','dn'): peaks.append(r['spec'][i][key]['nu'])
random.seed(1); ch=[abs(random.choice(peaks)-random.choice(peaks))<0.03 for _ in range(20000)]
fo=sum(obs)/len(obs); fc=sum(ch)/len(ch)
print('z-clock cells %d, heavy unequal-rate peak pairs %d, coinciding %d (%.4f); chance by random pairing %.4f; ratio %.2f -> %s'%(len(rows),len(obs),sum(obs),fo,fc,fo/fc,'locking supported' if fo>=2*fc else 'NOT supported (killed)'))
