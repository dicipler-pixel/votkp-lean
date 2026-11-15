# SCRIPT: SM-CANCEL-LOCK-01
# CANCEL: R(w) R(w reversed) = I for every word (boost matrices are symmetric, so L(w^R) = L(w)^T = R^T B(p)). KILL: deviation > 1e-60 on any of 500 words.
# LOCK: on a periodic end u u u ..., the own-frame turn per lap converges to the twist theta of L(u), read independently from SL(2,C):
#       tr M(u) = 2 cosh((l + i theta)/2).  KILL: last 5 laps spread > 1e-8, or |limit - |theta|| > 1e-8.
from mpmath import mp, mpf, mpc, matrix, cosh, sinh, sqrt, log, acos, acosh, eye, im, re, pi
import random
mp.dps = 80; R5 = log(5)
AX = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
def boost(nv, eta):
    c, s = cosh(eta), sinh(eta); B = matrix(4,4); B[0,0] = c
    for i in range(3): B[0,i+1] = B[i+1,0] = s*nv[i]
    for i in range(3):
        for j in range(3): B[i+1,j+1] = (1 if i==j else 0) + (c-1)*nv[i]*nv[j]
    return B
def polar(L):
    p = [L[i,0] for i in range(4)]; q = p[1:]; pm = sqrt(sum(x*x for x in q))
    if pm == 0: return eye(4)
    n = [x/pm for x in q]; Bi = boost([-x for x in n], acosh(p[0])); return Bi*L
def Lw(word):
    L = eye(4)
    for w in word: L = L*boost(AX[w], R5)
    return L
def reduced(n):
    out = []
    while len(out) < n:
        w = random.randrange(6)
        if out and (w ^ 1) == out[-1]: continue
        out.append(w)
    return out
random.seed(11); worst = mpf(0)
for t in range(500):
    w = reduced(random.randrange(1, 25)); A = polar(Lw(w)); B = polar(Lw(w[::-1])); D = A*B - eye(4)
    worst = max(worst, max(abs(D[i,j]) for i in range(4) for j in range(4)))
print("CANCEL: max |R(w) R(w reversed) - I| over 500 random words (length 1-24):", mp.nstr(worst, 5), "->", "KILL FIRED" if worst > mpf('1e-60') else "survives")
# SL(2,C): boost along unit n with rapidity r -> cosh(r/2) I + sinh(r/2) (n . sigma)
s1 = [[0,1],[1,0]]; s2 = [[0,-1j],[1j,0]]; s3 = [[1,0],[0,-1]]
def M2(word):
    M = matrix([[1,0],[0,1]])
    for w in word:
        n = AX[w]; c, s = cosh(R5/2), sinh(R5/2)
        S = matrix([[c + s*n[2], s*(n[0] - 1j*n[1])], [s*(n[0] + 1j*n[1]), c - s*n[2]]])
        M = M*S
    return M
from mpmath import acosh as macosh
for name, u in [('i j k', [0,2,4]), ('i j', [0,2]), ('i j -i k', [0,2,1,4]), ('i i j', [0,0,2]), ('i -j k -i j', [0,3,4,1,2])]:
    tr = M2(u)[0,0] + M2(u)[1,1]; lam = 2*macosh(tr/2); ell, th = abs(re(lam)), abs(im(lam)) % (2*pi)
    if th > pi: th = 2*pi - th
    L1 = Lw(u); turns = []; Lk = eye(4); prevR = None
    for k in range(1, 26):
        Lk = Lk*L1; Rk = polar(Lk)
        if prevR is not None:
            D = Rk*prevR.T; trr = D[1,1]+D[2,2]+D[3,3]; turns.append(acos(max(-1, min(1, (trr-1)/2))))
        prevR = Rk
    last = turns[-5:]; spread = max(last) - min(last); lim = turns[-1]
    verdict = "KILL FIRED" if (spread > mpf('1e-8') or abs(lim - th) > mpf('1e-8')) else "survives"
    print(f"LOCK {name:>12}: trace {mp.nstr(tr,10)}  twist |theta| = {mp.nstr(th,15)}  climb l = {mp.nstr(ell,8)}  turn per lap at lap 25 = {mp.nstr(lim,15)}  spread last 5 = {mp.nstr(spread,3)}  -> {verdict}")
