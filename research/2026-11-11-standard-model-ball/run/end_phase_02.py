# SCRIPT: SM-END-PHASE-02
# The opposite reading of END-PHASE-01. Per step n: alpha_n = lab turn of the travel direction (the amplitude side),
# omega_n = rotation angle of R_n R_{n-1}^{-1} in the rest frame (the phase side), eta_n = rapidity.
# PREDICTION (before the run): log alpha_n falls with slope -1 against eta_n (alpha ~ e^-eta); omega_n stays bounded away from 0.
# KILL: mean omega last 10 < 0.1 x mean omega first 10, or fitted slope of log alpha vs eta not negative.
exec(open('end_phase_01.py').read().split('# twin-prime chain arms')[0])
from mpmath import acos, log as mlog, mpf
def run2(word):
    L = matrix([[1 if i==j else 0 for j in range(4)] for i in range(4)]); prevR=None; prevn=None; rows=[]
    for w in word:
        L = L*boost(AX[w], R5); p=[L[i,0] for i in range(4)]; B,n,eta = stdboost(p); Rm = B**-1*L
        R3 = matrix([[Rm[i+1,j+1] for j in range(3)] for i in range(3)])
        if prevR is not None:
            D = R3*prevR.T; tr = D[0,0]+D[1,1]+D[2,2]; om = acos(max(-1,min(1,(tr-1)/2)))
            al = acos(max(-1,min(1,sum(n[i]*prevn[i] for i in range(3)))))
            rows.append((eta,al,om))
        prevR, prevn = R3, n
    return rows
N=200000; sv=bytearray(N+3)
for i in range(2,int((N+2)**.5)+1):
    if not sv[i]: sv[i*i::i]=b'\x01'*len(sv[i*i::i])
TW=[a for a in range(11,N) if not sv[a] and not sv[a+2]]
chain=[{1:0,7:2,9:4}[a%10] for a in TW[1:41]]
random.seed(7)
words={'twin-prime chain':chain,'random reduced A':reduced([random.randrange(6) for _ in range(80)])[:40],'periodic i j k':[0,2,4]*14}
for name,wd in words.items():
    rows=[r for r in run2(wd[:40]) if r[1]>0]
    import numpy as np
    x=np.array([float(r[0]) for r in rows]); y=np.array([float(mlog(r[1])) for r in rows]); slope=np.polyfit(x,y,1)[0]
    om=[float(r[2]) for r in run2(wd[:40])]
    f,l=sum(om[:10])/10,sum(om[-10:])/10
    print(f"{name}: slope of ln(lab turn) vs rapidity = {slope:.4f}  (prediction -1)")
    print(f"   rest-frame turn per step: first 10 mean {f:.4f} rad, last 10 mean {l:.4f} rad, ratio {l/f:.3f}  -> {'KILL FIRED' if (l<0.1*f or slope>=0) else 'survives'}")
