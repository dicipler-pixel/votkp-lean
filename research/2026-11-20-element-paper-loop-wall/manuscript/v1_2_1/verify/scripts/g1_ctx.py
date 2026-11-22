# SCRIPT: G1_CTX
import sys,re
f,pat,w=sys.argv[1],sys.argv[2],int(sys.argv[3])
t=open(f,encoding='utf-8',errors='ignore').read()
n=0
for m in re.finditer(pat,t):
    s=max(0,m.start()-w//4); print('---',m.start()); print(t[s:m.start()+w]); n+=1
    if n>=int(sys.argv[4]) if len(sys.argv)>4 else 3: break
