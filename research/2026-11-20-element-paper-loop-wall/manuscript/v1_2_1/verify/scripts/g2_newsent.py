# SCRIPT: G2_NEWSENT (list sentences of 04/05 with low similarity to any sentence of raw_v11b.txt)
import re,difflib,sys
raw=open('/home/claude/paper_v12/raw_v11b.txt',encoding='utf-8').read()
raw=raw.replace('\n',' ')
def norm(s):
    s=re.sub(r'\$[^$]*\$','M',s); s=re.sub(r'[*_`\\]','',s); s=s.lower()
    s=re.sub(r'[^a-z0-9 ]',' ',s); return re.sub(r'\s+',' ',s).strip()
rs=[norm(x) for x in re.split(r'(?<=[.!?])\s+',raw) if len(x)>25]
for f in sys.argv[1:]:
    t=open(f,encoding='utf-8').read()
    t=re.sub(r'\$\$.*?\$\$',' ',t,flags=re.S)
    sents=[x for x in re.split(r'(?<=[.!?])\s+|\n+',t) if len(x.strip())>25]
    print('=====',f)
    for s in sents:
        n=norm(s); 
        if not n: continue
        best=0
        for r in rs:
            if abs(len(r)-len(n))>len(n)*0.8: continue
            q=difflib.SequenceMatcher(None,n,r).quick_ratio()
            if q<0.55: continue
            q=difflib.SequenceMatcher(None,n,r).ratio()
            if q>best: best=q
        if best<0.62: print('%.2f | %s'%(best,s.strip()[:300]))
