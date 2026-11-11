# SCRIPT: SM-CANCEL-LOCK-02
# CANCEL, exact: each boost is an integer matrix over 5 (cosh ln5 = 13/5, sinh ln5 = 12/5). Check 5^n L(w reversed) == (5^n L(w))^T in integers.
#   Why this proves the cancel: boost matrices are symmetric, so L(w^R) = L(w)^T = R^T B(p)^T = R^T B(p) = (R^T B(p) R) R^T,
#   and the polar split is unique, so the rotation of w reversed is R^T = R^-1: the partner's turn undoes the spin's turn exactly.
#   KILL: any word of 2000 fails the integer equality.
# LOCK, debug: print the turn per lap for the two ends that fired, out to lap 60.
import random
AXI = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
def bint(n):
    B = [[5 if i==j else 0 for j in range(4)] for i in range(4)]; B[0][0] = 13
    for i in range(3):
        B[0][i+1] = B[i+1][0] = 12*n[i]
        for j in range(3): B[i+1][j+1] = (5 if i==j else 0) + 8*n[i]*n[j]
    return B
def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
def Lint(w):
    L = [[1 if i==j else 0 for j in range(4)] for i in range(4)]
    for x in w: L = mm(L, bint(AXI[x]))
    return L
random.seed(3); bad = 0
for t in range(2000):
    n = random.randrange(1, 40); w = []
    while len(w) < n:
        x = random.randrange(6)
        if w and (x ^ 1) == w[-1]: continue
        w.append(x)
    A = Lint(w); B = Lint(w[::-1])
    if any(B[i][j] != A[j][i] for i in range(4) for j in range(4)): bad += 1
print("CANCEL exact: words where 5^n L(w reversed) != transpose(5^n L(w)):", bad, "of 2000 (lengths 1-39) ->", "KILL FIRED" if bad else "survives")
exec(open('cancel_lock_01.py').read().split('random.seed(11)')[0])
mp.dps = 120
for name, u in [('i i j', [0,0,2]), ('i -j k -i j', [0,3,4,1,2])]:
    L1 = Lw(u); Lk = eye(4); prevR = None; out = []
    for k in range(1, 61):
        Lk = Lk*L1; Rk = polar(Lk)
        if prevR is not None:
            D = Rk*prevR.T; trr = D[1,1]+D[2,2]+D[3,3]; out.append(acos(max(-1, min(1, (trr-1)/2))))
        prevR = Rk
    print(name, [mp.nstr(x, 10) for x in out[:6]], '...', [mp.nstr(x, 14) for x in out[-4:]])
