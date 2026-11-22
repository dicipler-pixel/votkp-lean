# SCRIPT: G2_WINDOWS (count contiguous windows by step length from the threshold archive)
import gzip,json
d=json.load(gzip.open('/home/claude/votkp-lean/data/element_thresholds_20261011.json.gz'))
cnt={}
for r in d['records']:
    th=sorted(r['thresholds'],key=lambda t:t['q'])
    if not th: continue
    runs=[];cur=[th[0]]
    for t in th[1:]:
        if t['q']==cur[-1]['q']+1: cur.append(t)
        else: runs.append(cur);cur=[t]
    runs.append(cur)
    for run in runs:
        n=len(run)
        for L in range(1,n):
            cnt[L]=cnt.get(L,0)+(n-L)
cum=0
for L in range(1,20):
    cum+=cnt.get(L,0)
    print(L,cnt.get(L,0),cum)
