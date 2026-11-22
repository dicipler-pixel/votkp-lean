# SCRIPT: G2_ARCHIVE (recount thresholds, ladders, pairs, flag pairs, windows from data/element_thresholds_20261011.json.gz)
import gzip,json,math
d=json.load(gzip.open('/home/claude/votkp-lean/data/element_thresholds_20261011.json.gz'))
R=d['records']
print('records',len(R),'max Z',max(r['Z'] for r in R))
tot=sum(len(r['thresholds']) for r in R)
print('thresholds',tot)
comp=sum(1 for r in R if len(r['thresholds'])==r['Z'])
print('complete ladders (len==Z)',comp)
pairs=0;EE=0;TT=0;grades={}
win=0;maxerr=0.0
for r in R:
    th=sorted(r["thresholds"],key=lambda t:t["q"])
    if not th: continue
    qs=[t['q'] for t in th]
    # contiguous runs of q
    runs=[];cur=[th[0]]
    for t in th[1:]:
        if t['q']==cur[-1]['q']+1: cur.append(t)
        else: runs.append(cur);cur=[t]
    runs.append(cur)
    for run in runs:
        n=len(run)
        for i in range(n-1):
            pairs+=1
            g=(run[i]['grade'],run[i+1]['grade'])
            grades[g]=grades.get(g,0)+1
        # windows of 1..10 steps
        for L in range(1,11):
            for s in range(0,n-L):
                win+=1
                I=[run[k]['IE_eV'] for k in range(s,s+L+1)]
                # endpoint composition: Einstein sum of tanh(r/2) vs direct
                G=[(I[k+1]-I[k])/(I[k+1]+I[k]) for k in range(L)]
                u=G[0]
                for g_ in G[1:]: u=(u+g_)/(1+u*g_)
                direct=(I[-1]-I[0])/(I[-1]+I[0])
                maxerr=max(maxerr,abs(u-direct))
print('adjacent pairs',pairs)
print('grade pairs',sorted(grades.items(),key=lambda x:-x[1])[:8])
print('E/E pairs',grades.get(('E','E')))
print('windows 1..10',win,'max abs err',maxerr)
