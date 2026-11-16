# SCRIPT: L4-TAG-SUMMARY-02  tables from sweep2.jsonl and a reproducibility check against the earlier sweep.jsonl (SYNC-01, sign as written).
import json, collections, itertools
rows=[json.loads(l) for l in open('sweep2.jsonl') if l.strip()]
old=[json.loads(l) for l in open('sweep.jsonl') if l.strip()]
# reproducibility
ok=0;worst=0
for o in old:
    m=[r for r in rows if r['P']['N']==o['N'] and r['P']['clocks']==o['clocks'] and r['P']['torque']==o['torque'] and r['P']['gamma']==o['gamma'] and r['P']['gloss']==o['gloss'] and r['P']['sign']=='asis' and r['P'].get('tag')=='grid']
    if m: ok+=1; worst=max(worst,abs(m[0]['rMean']-o['rMean']))
print('sweep.jsonl rows matched in sweep2.jsonl (sign asis): %d of %d ; largest |rMean difference| %.2e'%(ok,len(old),worst))
eps=0.02
def agree(r):  # pairs whose measured rates agree in both windows (kill line 1 first clause), unequal free rates for z
    return [(p['i'],p['j']) for p in r['pairs'] if p['dr'][0]<eps and p['dr'][1]<eps and (r['P']['clocks']=='equal' or p['dfree']>eps)]
T=collections.defaultdict(lambda:collections.Counter())
for r in rows:
    k=(r['P'].get('tag'),r['P']['sign'])
    T[k]['cells']+=1
    a=agree(r)
    if a: T[k]['cells with rate-agreeing pair']+=1
    ha=[p for p in a if r['heavy'][p[0]]>=0.5 and r['heavy'][p[1]]>=0.5]
    if ha: T[k]['... and both heavy']+=1
    if r['P']['gloss']>0 or r['P'].get('sinkRate',0)>0: T[k]['lossy cells']+=1
    if r['rExcess']>3 and max(r['heavy'])>=0.5: T[k]['r > surrogate+3sd with a heavy ball']+=1
    if r['rExcess']>3 and max(r['heavy'])<0.5: T[k]['r > surrogate+3sd, NO heavy ball']+=1
for k in sorted(T,key=str): print(k,dict(T[k]))
ll=[r['lightLeft'] for r in rows if r['P']['gloss']>0 or r['P'].get('sinkRate',0)>0]
print('light left in system at t=400 in lossy cells (min, median, max):',min(ll),sorted(ll)[len(ll)//2],max(ll))
print('lossy cells (gloss, no sink):',sum(1 for r in rows if r['P']['gloss']>0),' sink cells:',sum(1 for r in rows if r['P'].get('sinkRate',0)>0))
# loss rate vs books: lightLeft + lost = 1 is booked inside the script (book); check
print('worst book error incl. lost light: %.2e'%max(r['book'] for r in rows))
# for the grid, the free-rate gap vs measured-rate gap in z cells: do measured rates move toward each other?
mv=[];
for r in rows:
    if r['P']['clocks']!='z': continue
    for p in r['pairs']:
        if r['heavy'][p['i']]>=0.5 and r['heavy'][p['j']]>=0.5 and p['dfree']>eps: mv.append((p['dr'][1],p['dfree']))
print('z cells, heavy pairs: %d ; measured rate gap smaller than free gap in %d (%.2f)'%(len(mv),sum(1 for a,b in mv if a<b),sum(1 for a,b in mv if a<b)/len(mv)))
