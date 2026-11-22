# SCRIPT: G2_FIND (print +-W chars around each match of a pattern in a file)
import sys,re
f,pat=sys.argv[1],sys.argv[2]
W=int(sys.argv[3]) if len(sys.argv)>3 else 200
mx=int(sys.argv[4]) if len(sys.argv)>4 else 4
t=open(f,encoding='utf-8',errors='replace').read()
n=0
for m in re.finditer(pat,t):
    s=max(0,m.start()-W); e=min(len(t),m.end()+W)
    print('['+str(m.start())+']',t[s:e].replace('\n',' '),'\n---')
    n+=1
    if n>=mx: break
if n==0: print('NO MATCH',pat)
