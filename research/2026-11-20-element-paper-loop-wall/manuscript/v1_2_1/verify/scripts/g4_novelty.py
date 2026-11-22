# SCRIPT: G4_NOVELTY
import re,sys
raw=open('/home/claude/paper_v12/raw_v11b.txt').read().lower()
rawtok=set(re.findall(r'[a-z0-9\.]+',raw))
# also character-ngram approach on words 4-gram
words=re.findall(r'[a-z0-9]+',raw)
grams=set(tuple(words[i:i+4]) for i in range(len(words)-3))
for f in ['06_ball','10_lab','11_tests','12_decay']:
    t=open(f'/home/claude/paper_v12/build/src/{f}.md').read()
    t=re.sub(r'\$\$.*?\$\$','',t,flags=re.S); t=re.sub(r'\$[^$]*\$','',t)
    sents=re.split(r'(?<=[.!?])\s+',t)
    for s in sents:
        w=re.findall(r'[a-z0-9]+',s.lower())
        if len(w)<8: continue
        g=[tuple(w[i:i+4]) for i in range(len(w)-3)]
        hit=sum(1 for x in g if x in grams)/len(g)
        if hit<0.25: print(f'[{f}] {hit:.2f} {s[:230]}')
