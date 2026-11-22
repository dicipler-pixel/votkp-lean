# SCRIPT: G3-SCREENING-READOUTS
import gzip,json,math,re
B='/home/claude/votkp-lean/'
R=json.load(gzip.open(B+'data/element_thresholds_20261011.json.gz'))['records']
rec={r['Z']:r for r in R}
HA=27.211386245988
S={};G={}
for Z in range(2,86):
    ie=[t['IE_eV']/HA for t in rec[Z]['thresholds']]
    h=ie[Z-1]; b=ie[Z-2]
    S[Z]=(h-b)/Z; G[Z]=Z-math.sqrt(2*b)
    assert abs(Z*(S[Z]-G[Z])-((h-Z*Z/2)-G[Z]**2/2))<1e-9
def cross(f,thr,name):
    out=[]
    for Z in range(3,86):
        a,b=f(Z-1)-thr(Z-1),f(Z)-thr(Z)
        if a*b<0: out.append((Z-1,Z))
    print(name,out)
cross(lambda Z:G[Z],lambda Z:0.625,'sigma=5/8')
cross(lambda Z:S[Z],lambda Z:G[Z],'S=sigma')
cross(lambda Z:S[Z],lambda Z:0.625,'S=5/8')
cross(lambda Z:G[Z],lambda Z:0.5,'sigma=1/2')
cross(lambda Z:G[Z],lambda Z:0.0,'sigma=0')
for Z in (10,11,13,14,17,18,19,28,29,46,47): print(Z,rec[Z]['symbol'],round(S[Z],5),round(G[Z],5))
# compare table
t=open('/home/claude/paper_v12/build/src/17_tables.md').read()
sec=t[t.index('Appendix C'):t.index('Appendix D')]
bad=0;n=0
for m in re.finditer(r'\| (\d+) \| \w+ \| ([-\d.]+) \| ([-\d.]+) \| ([+-][\d.]+) \|',sec):
    Z=int(m.group(1));n+=1
    s,g,d=map(float,m.groups()[1:])
    if abs(round(S[Z],5)-s)>1.1e-5 or abs(round(G[Z],5)-g)>1.1e-5 or abs(round(S[Z]-G[Z],5)-d)>1.1e-5:
        bad+=1;print('MISMATCH',Z,s,g,d,round(S[Z],5),round(G[Z],5),round(S[Z]-G[Z],5))
print('appendix C rows',n,'mismatch',bad)
# asymptotics
print('S=5/8-0.157666/Z at Z=80',0.625-0.157666/80,S[80]); 
a=1/137.035999084
print('Z*',(4*0.617**2/a**2)**.25)
# 0.617 crossing S=sigma Al-Si
print('S,sigma at Al,Si',S[13],G[13],S[14],G[14])
# asymptotic coefficients
c1=0.157666; c2=0.1953125-c1
print('sigma coefficient',c2)
