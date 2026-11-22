# SCRIPT: G4_HODY_INDEPENDENT_GAIN
import gzip,json
from fractions import Fraction as F
arc='/home/claude/votkp-lean/data/element_thresholds_20261011.json.gz'
recs={r['symbol']:r for r in json.load(gzip.open(arc,'rt'),parse_float=str)['records']}
def lad(s):
    th=sorted(recs[s]['thresholds'],key=lambda t:t['q'])
    return [(F(t['IE_eV']),F(t['unc_eV'])) for t in th]
Ho=lad('Ho');Dy=lad('Dy')
print(len(Ho),len(Dy)); 
Q0=F('2863.2');d0=F('0.6')
res={}
for q in range(0,67):
    # Q_q = Q0 + sum_{k=1}^q (IE_Ho_k - IE_Dy_k); thresholds index q-1 is k-th removal
    U=sum(Ho[k][0] for k in range(q));V=sum(Dy[k][0] for k in range(q))
    dU=sum(Ho[k][1] for k in range(q));dV=sum(Dy[k][1] for k in range(q))
    Q=Q0+U-V; s=1 if Q>0 else -1
    if q==0: continue
    cen=abs(Q)/(U+V)
    num=s*Q-(d0+dU+dV); den=U+V+s*(dV-dU)
    rect=num/den
    res[q]=(Q,cen,rect)
for q in (55,56,57,58):
    Q,c,r=res[q]; print(q,float(Q),f'central {float(c)*100:.6f}%',f'rect {float(r)*100:.6f}%')
b=min(res,key=lambda q:res[q][2]); print('binding rect q',b,float(res[b][2]))
b2=min(res,key=lambda q:res[q][1]); print('binding central q',b2,float(res[b2][1]))
print('signs all consistent?',[q for q in res if (res[q][0]>0)!=(q<=56)])
# false control
eps=F('0.006645')
Qc=F('2862.6')+F('95557.2819')*(1-eps)-F('97139.636067')*(1+eps)
print('false control Q56',float(Qc))
U56=sum(Ho[k][0] for k in range(56));V56=sum(Dy[k][0] for k in range(56));print(float(U56),float(V56))
print('rect eps* digits',float(res[56][2]))
print('--- flips at eps=0.006645')
print([q for q in res if res[q][2]<eps])
print('q1..12 thresholds',[float(res[q][2]) for q in range(1,13)])
print('q55 rect',float(res[55][2]),'> .006645?',res[55][2]>eps)
# Q(q) first row
print('Q0',2863.2)
