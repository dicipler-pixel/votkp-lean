# SCRIPT: GRAPH-PROJECTOR-01
# Question (entry A2 of research/TWO_SESSIONS.md): is the building cone (squared distance =
# rank(a - b) on the 16 matrices of Mat_2(F_2), ratio D(2)^2/D(1)^2 = 2) the IQGT projector
# metric with the gap removed?
#
# KILL LINE 1 (written in A2 before the run): the squared chordal distance between the graph
# projectors of the 16 matrices is not a function of the rank of their difference.
# KILL LINE 2 (written before the run, for the opposite setup): on the non-compact side
# (rapidity distance, Smith coordinate tanh(eps/2) = singular value), the ratio never rises
# above the flat value 3/2 at any scale gamma.
#
# WHY THE CHECK TESTS THE CLAIM.  The intrinsic metric is g = (1/2) Tr(dP dP); its finite form is
# the chordal distance ||P_a - P_b||^2 = 2 sum sin^2(theta_i).  No gap appears in it (Dirac Time
# 9.4: H -> sH keeps the projectors).  So "the metric with the gap removed" is this distance, and
# the claim says it should equal rank(a - b) up to one constant.  The same pairs are read three ways:
#   chord^2 = 2 sum sin^2 theta      (the IQGT metric, compact side)
#   arc^2   = sum theta^2            (geodesic on the Grassmannian, the lean angles themselves)
#   rapidity^2 = sum eps_i^2 / 4     (non-compact dual: contractions Z, tanh(eps/2) = singular value)
# D(r)^2 = mean of the squared distance over all ordered pairs (a, a + W), rank W = r over F_2.
import numpy as np
from itertools import product
from collections import Counter
mats=[tuple(b) for b in product((0,1),repeat=4)]
def rk(m):
    a,b,c,d=m
    return 0 if not any(m) else (2 if (a*d-b*c)%2 else 1)
def add(x,y): return tuple(p^q for p,q in zip(x,y))
pairs={r:[(a,add(a,W)) for a in mats for W in mats if rk(W)==r] for r in (1,2)}
def proj(m,lift):
    A=lift(np.array(m,float).reshape(2,2)); M=np.vstack([np.eye(2),A])
    return M@np.linalg.inv(M.T@M)@M.T
def angles(P,Q):
    U=np.linalg.svd(P)[0][:,:2]; V=np.linalg.svd(Q)[0][:,:2]
    return np.arccos(np.clip(np.linalg.svd(U.T@V,compute_uv=False),-1,1))
def msqrt(S):
    w,V=np.linalg.eigh(S); return (V*np.sqrt(w))@V.T
def rapid(Z,W):
    I=np.eye(2)
    T=np.linalg.inv(msqrt(I-Z@Z.T))@(W-Z)@np.linalg.inv(I-Z.T@W)@msqrt(I-Z.T@Z)
    s=np.clip(np.linalg.svd(T,compute_uv=False),0,1-1e-15)
    return float(np.sum(np.arctanh(s)**2))
lifts={'entries 0,1':lambda A:A,'entries +1,-1':lambda A:1-2*A}
for name,lift in lifts.items():
    print('=== real lift:',name)
    P={m:proj(m,lift) for m in mats}
    # control: chord^2 must equal 2 sum sin^2 theta on every pair
    err=max(abs(np.sum((P[a]-P[b])**2)-2*np.sum(np.sin(angles(P[a],P[b]))**2)) for r in (1,2) for a,b in pairs[r])
    print('CONTROL chord^2 = 2 sum sin^2(theta): largest error',f'{err:.1e}')
    D={}
    for r in (1,2):
        ch=[round(float(np.sum((P[a]-P[b])**2)),9) for a,b in pairs[r]]
        ar=[float(np.sum(angles(P[a],P[b])**2)) for a,b in pairs[r]]
        D[r]=(np.mean(ch),np.mean(ar))
        print(f'rank {r}: {len(ch)} ordered pairs; distinct chord^2 values and counts:',sorted(Counter(ch).items()))
    print(f'chord: D(1)^2 = {D[1][0]:.6f}  D(2)^2 = {D[2][0]:.6f}  ratio = {D[2][0]/D[1][0]:.6f}')
    print(f'arc:   D(1)^2 = {D[1][1]:.6f}  D(2)^2 = {D[2][1]:.6f}  ratio = {D[2][1]/D[1][1]:.6f}')
    one_value=all(len(set(round(float(np.sum((P[a]-P[b])**2)),9) for a,b in pairs[r]))==1 for r in (1,2))
    print('KILL LINE 1', 'did not fire' if one_value else 'fired: chord^2 is not a function of rank(a - b)')
    smax=max(np.linalg.svd(lift(np.array(m,float).reshape(2,2)),compute_uv=False)[0] for m in mats)
    print(f'non-compact side, Z_a = gamma * a / (largest singular value {smax:.4f}); gamma = 1 is the rim')
    Zc=lambda m,g: g*lift(np.array(m,float).reshape(2,2))/smax
    # controls: symmetry, and d(0,W)^2 = sum artanh^2(singular values)
    g=0.7; a,b=mats[5],mats[11]
    print('CONTROL symmetry d(Z,W)=d(W,Z):',f'{abs(rapid(Zc(a,g),Zc(b,g))-rapid(Zc(b,g),Zc(a,g))):.1e}',
          ' d(0,W):',f'{abs(rapid(np.zeros((2,2)),Zc(b,g))-np.sum(np.arctanh(np.linalg.svd(Zc(b,g),compute_uv=False))**2)):.1e}')
    top=0
    for g in (0.01,0.2,0.5,0.8,0.9,0.99,0.999,0.99999,1-1e-9):
        d={r:np.mean([rapid(Zc(a,g),Zc(b,g)) for a,b in pairs[r]]) for r in (1,2)}
        top=max(top,d[2]/d[1]); print(f'   gamma = {g:<12} ratio = {d[2]/d[1]:.6f}')
    print('KILL LINE 2', 'fired: never above 3/2' if top<=1.5+1e-9 else f'did not fire: largest ratio {top:.6f}')
print('reference values: flat 3/2 = 1.5, tree star 5/3 =',5/3,', building cone 2')
