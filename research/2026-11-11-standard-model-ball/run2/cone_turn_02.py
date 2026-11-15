# SCRIPT: SM-CONE-TURN-02
# Opposite of ITEM 2: the 45-degree cone about (1,1,1) in the TURN book. For every reduced word to depth 6, the own-frame rotation R (polar split)
# has an axis; count axes with cos^2(axis, (1,1,1)) within 1e-10 of 1/2, against windows around 0.45 and 0.55.
# KILL (same as ITEM 2): no exact hits AND 1/2 not singled out.
import numpy as np, math
def boost(n, r):
    c, s = math.cosh(r), math.sinh(r); B = np.eye(4); B[0,0] = c
    for i in range(3):
        B[0,i+1] = B[i+1,0] = s*n[i]
        for j in range(3): B[i+1,j+1] = (1 if i==j else 0) + (c-1)*n[i]*n[j]
    return B
AX = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]; R5 = math.log(5); G = [boost(a, R5) for a in AX]
def polarR(L):
    p = L[:,0]; q = p[1:]; pm = np.linalg.norm(q)
    if pm < 1e-14: return L[1:,1:]
    n = q/pm; return (boost(-n, math.acosh(p[0])) @ L)[1:,1:]
D = np.ones(3)/math.sqrt(3); vals = []; frontier = [(np.eye(4), -1)]
for depth in range(1, 7):
    nf = []
    for L, last in frontier:
        for g in range(6):
            if last >= 0 and g == (last ^ 1): continue
            M = L @ G[g]; nf.append((M, g)); R = polarR(M); ang = math.acos(max(-1, min(1, (np.trace(R) - 1)/2)))
            if ang > 1e-9:
                ax = np.array([R[2,1]-R[1,2], R[0,2]-R[2,0], R[1,0]-R[0,1]])
                if np.linalg.norm(ax) > 1e-12: ax /= np.linalg.norm(ax); vals.append((ax @ D)**2)
    frontier = nf
v = np.array(vals); w = lambda a, h=0.005: int(np.sum(np.abs(v - a) < h))
print(f"turn axes counted: {len(v)};  within 1e-10 of cos^2 = 1/2: {int(np.sum(np.abs(v-0.5) < 1e-10))}")
print("within 0.005 of 0.40, 0.45, 0.50, 0.55, 0.60:", [w(a) for a in (0.40,0.45,0.50,0.55,0.60)], "; on an arm (1/3):", int(np.sum(np.abs(v-1/3)<1e-10)), " on the diagonal (1):", int(np.sum(np.abs(v-1)<1e-10)), " perpendicular to it (0):", int(np.sum(v<1e-10)))
print("->", 'KILL FIRED' if (np.sum(np.abs(v-0.5)<1e-10) == 0 and w(0.5) <= max(w(0.45), w(0.55))) else 'survives')
