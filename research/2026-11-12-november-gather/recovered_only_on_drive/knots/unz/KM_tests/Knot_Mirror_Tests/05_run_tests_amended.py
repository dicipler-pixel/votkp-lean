#!/usr/bin/env python3
"""Exact rational implementation of BN-vdV theta, paper arXiv:2509.18456v4,
Eqs. (2)-(6). Predictions were frozen in 01_PREREGISTRATION.txt first.
Run with Python 3; standard library only.
"""
from fractions import Fraction as F
from collections import Counter
import json, hashlib
from pathlib import Path

HERE=Path(__file__).resolve().parent
CALIBRATION_POINTS=[(2,3),(3,2),(2,5),(5,3)]
POINTS=CALIBRATION_POINTS+[(F(11,5),F(7,3)),(F(13,4),F(11,4)),(F(9,4),F(13,5))]
def inverse_and_det(a):
    n=len(a); a=[row[:] + [F(i==j) for j in range(n)] for i,row in enumerate(a)]
    det=F(1)
    for col in range(n):
        row=next((r for r in range(col,n) if a[r][col]),None)
        if row is None: raise ValueError('singular matrix')
        if row!=col: a[col],a[row]=a[row],a[col]; det=-det
        p=a[col][col]; det*=p; a[col]=[v/p for v in a[col]]
        for r in range(n):
            if r!=col and a[r][col]:
                c=a[r][col]; a[r]=[x-c*y for x,y in zip(a[r],a[col])]
    inv=[row[n:] for row in a]
    return inv,det

def braid(n, mirror=False, damaged=False):
    assert n>0 and n%2==1
    xs=[]
    for k in range(1,n+1):
        i,j=(k,n+k) if k%2 else (n+k,k)
        s=1
        if mirror: i,j,s=j,i,-1
        if damaged and k==1: s=-s
        xs.append((s,i,j))
    rotations={n+1: -1}
    return xs,rotations

def theta_value(n, q1, q2, mirror=False, damaged=False):
    t1,t2=F(q1),F(q2); t3=t1*t2; xs,rot=braid(n,mirror,damaged)
    size=2*n+1; matrices=[]; deltas=[]
    w=sum(s for s,_,_ in xs); phi=sum(rot.values()); exponent=F(-phi-w,2)
    if exponent.denominator!=1: raise ValueError('normalization exponent nonintegral')
    for q in (t1,t2,t3):
        a=[[F(i==j) for j in range(size)] for i in range(size)]
        for s,i,j in xs:
            i-=1; j-=1
            a[i][i+1]-=q**s; a[i][j+1]-=(1-q**s); a[j][j+1]-=1
        inv,det=inverse_and_det(a)
        for i in range(size):
            for j in range(size):
                assert sum(a[i][k]*inv[k][j] for k in range(size)) == int(i==j)
        matrices.append(inv); deltas.append(q**int(exponent)*det)
    def g(z,i,j): return matrices[z-1][i-1][j-1]
    f1=F(0); f2=F(0); f3=F(0)
    for s,i,j in xs:
        q2s=t2**s; q3s=t3**s; q1s=t1**s
        f1+=s*(F(1,2)-g(3,i,i)+q2s*g(1,i,i)*g(2,j,i)-q2s*g(3,j,j)*g(2,j,i)
               -(q2s-1)*g(3,i,i)*g(2,j,i)+(q3s-1)*g(2,j,i)*g(3,j,i)-g(1,i,i)*g(2,j,j)
               +2*g(3,i,i)*g(2,j,j)+g(1,i,i)*g(3,j,j)-g(2,i,i)*g(3,j,j))
        f1+=F(s,1)/(q2s-1)*((q1s-1)*q2s*(g(3,j,j)*g(1,j,i)-g(2,j,j)*g(1,j,i)+q2s*g(1,j,i)*g(2,j,i))
              +(q3s-1)*g(3,j,i)*(1-q2s*g(1,i,i)+g(2,i,j)+(q2s-2)*g(2,j,j)-(q1s-1)*(q2s+1)*g(1,j,i)))
    for s0,i0,j0 in xs:
        for s1,i1,j1 in xs:
            f2+=F(s1,1)*(t1**s0-1)*(t3**s1-1)*g(1,j1,i0)*g(3,j0,i1)/(t2**s1-1)*(t2**s0*g(2,i1,i0)+g(2,j1,j0)-t2**s0*g(2,j1,i0)-g(2,i1,j0))
    for k,v in rot.items(): f3+=(g(3,k,k)-F(1,2))*v
    theta=deltas[0]*deltas[1]*deltas[2]*(f1+f2+f3)
    return theta,deltas

def trefoil_table(S,T):
    S,T=F(S),F(T)
    return -(1-S+S**2-T-S**3*T+T**2+S**4*T**2-S*T**3-S**4*T**3+S**2*T**4-S**3*T**4+S**4*T**4)/(S**2*T**2)

def eval_7_table(S,T):
    # Manually transcribed published 7_1 entry; compare three independent
    # rational points to avoid a point-specific accidental match.
    S,T=F(S),F(T)
    p=(3-3*S+3*S**2-3*S**3+3*S**4-3*S**5+3*S**6-3*T-3*S**7*T+3*T**2+2*S**2*T**2-2*S**3*T**2+2*S**4*T**2-2*S**5*T**2+2*S**6*T**2+3*S**8*T**2-3*T**3-2*S**2*T**3-2*S**7*T**3-3*S**9*T**3+3*T**4+2*S**2*T**4+S**4*T**4-S**5*T**4+S**6*T**4+2*S**8*T**4+3*S**10*T**4-3*T**5-2*S**2*T**5-S**4*T**5-S**7*T**5-2*S**9*T**5-3*S**11*T**5+3*T**6+2*S**2*T**6+S**4*T**6+S**8*T**6+2*S**10*T**6+3*S**12*T**6-3*S*T**7-2*S**3*T**7-S**5*T**7-S**8*T**7-2*S**10*T**7-3*S**12*T**7+3*S**2*T**8+2*S**4*T**8+S**6*T**8-S**7*T**8+S**8*T**8+2*S**10*T**8+3*S**12*T**8-3*S**3*T**9-2*S**5*T**9-2*S**10*T**9-3*S**12*T**9+3*S**4*T**10+2*S**6*T**10-2*S**7*T**10+2*S**8*T**10-2*S**9*T**10+2*S**10*T**10+3*S**12*T**10-3*S**5*T**11-3*S**12*T**11+3*S**6*T**12-3*S**7*T**12+3*S**8*T**12-3*S**9*T**12+3*S**10*T**12-3*S**11*T**12+3*S**12*T**12)
    return -p/(S**6*T**6)

def clean(c): return {k:v for k,v in c.items() if v}
def mul(a,b):
    c=Counter()
    for i,x in a.items():
        for j,y in b.items(): c[i+j]+=x*y
    return clean(c)
def sub(a,b):
    c=Counter(a)
    for i,v in b.items(): c[i]-=v
    return clean(c)
def family_tests():
    x={-1:1,1:1}; fprev={0:1}; f={0:-1,1:1}
    results=[]
    for m in range(1,51):
        direct={j-m:(-1)**j for j in range(2*m+1)}
        # f stores coefficients as powers of x, independently evaluate x=t+t^-1
        val={}; power={0:1}
        for i in range(max(f)+1):
            for e,c in power.items(): val[e]=val.get(e,0)+f.get(i,0)*c
            power=mul(power,x)
        results.append(clean(val)==direct)
        fprev,f=f,sub({i+1:c for i,c in f.items()},fprev)
    expected=results==[True]*50
    false_figure8=clean(sub({0:3,1:-1,-1:-1},{0:-1,1:1,-1:1}))
    wrong_f3=clean(sub({3:1,2:1,1:-2,0:1},{3:1,2:-1,1:-2,0:1}))
    return {'m1_to_50_all_match':expected,'first_failure':next((i+1 for i,v in enumerate(results) if not v),None),'figure8_minus_trefoil_laurent':false_figure8,'wrong_f3_minus_reference_x':wrong_f3}

def stringify(v):
    if isinstance(v,F):return str(v)
    if isinstance(v,dict):return {str(k):stringify(x) for k,x in v.items()}
    if isinstance(v,(list,tuple)):return [stringify(x) for x in v]
    return v

def main():
    protocol=HERE/'01_PREREGISTRATION.txt'
    result={'protocol_sha256':hashlib.sha256(protocol.read_bytes()).hexdigest(),'amendment_sha256':hashlib.sha256((HERE/'04_PROTOCOL_AMENDMENT.txt').read_bytes()).hexdigest(),'sources':['https://arxiv.org/html/2509.18456v4','https://drorbn.net/AcademicPensieve/Projects/Theta/ThetaTable4ChatGPT.txt'],'family':family_tests(),'calibration':{},'tests':{},'damaged':{}}
    calibration=[]
    for n in (3,7):
        for p in CALIBRATION_POINTS:
            try:
                v,d=theta_value(n,*p); ref=(trefoil_table if n==3 else eval_7_table)(*p)
                calibration.append((n,p,v,ref))
            except Exception as e:
                result['calibration']['error']=repr(e)
                result['status']='INVALID - implementation/calibration error'; write(result); return
    for sign in (1,-1):
        if all(v==sign*r for _,_,v,r in calibration): break
    else: sign=0
    result['calibration']['fixed_sign']=sign
    result['calibration']['cases']=[{'n':n,'point':p,'computed':v,'published':r} for n,p,v,r in calibration]
    if not sign:
        result['status']='INVALID - published reference calibration mismatch';write(result);return
    for n in (3,5,7,9,11):
        rows=[]
        for p in POINTS:
            plus,d=theta_value(n,*p); mirror,dm=theta_value(n,*p,mirror=True)
            residual=plus+mirror
            # Eqs (2),(6), Fact 23: use calculated values and delta factors.
            a=plus*d[0]*d[1]*d[2]*2
            b=plus*dm[0]*dm[1]*dm[2]+mirror*d[0]*d[1]*d[2]
            rows.append({'point':p,'theta':plus,'theta_mirror':mirror,'mirror_sum':residual,'delta_match':d==dm,'theta_samehand_sum':a,'theta_mirror_sum':b})
        result['tests'][str(n)]=rows
    for p in POINTS:
        try:
            v,_=theta_value(3,*p,damaged=True)
            result['damaged'][str(p)]={'value':v,'equals_reference':v==sign*trefoil_table(*p)}
        except Exception as e: result['damaged'][str(p)]={'error':repr(e)}
    result['status']='DONE; mirror geometry and normalization require independent validation'
    write(result)

def write(obj):
    text=json.dumps(stringify(obj),indent=2,sort_keys=True)
    (HERE/'06_results_amended.json').write_text(text+'\n')
    print(text)

if __name__=='__main__':main()
