# SCRIPT: SM-END-PHASE-01
# A spin carried along an end of the ln5 tree. Each step: boost of rapidity ln 5 along the next arm, in the particle's own frame (L_n = L_{n-1} B_w).
# Polar split L = B(p) R (unique). Rest-frame spin s_n = R_n s_0; travel direction nhat_n = p_n spatial / |p_n|.
# Helicity cosine h_n = s_n . nhat_n.  Prediction (Wigner, massless limit): |h_n - h_{n-1}| shrinks as rapidity grows; the spin rides with the travel direction.
# KILL (written before the run): mean |dh| over the last 10 steps > 0.5 x mean |dh| over the first 10 steps.
from mpmath import mp, mpf, matrix, cosh, sinh, sqrt, log, acos, acosh
import random
mp.dps = 80
R5 = log(5)
def boost(nv, eta):
    c, s = cosh(eta), sinh(eta); B = matrix(4,4)
    B[0,0] = c
    for i in range(3): B[0,i+1] = B[i+1,0] = s*nv[i]
    for i in range(3):
        for j in range(3): B[i+1,j+1] = (1 if i==j else 0) + (c-1)*nv[i]*nv[j]
    return B
AX = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
def stdboost(p):
    E = p[0]; q = [p[1],p[2],p[3]]; pm = sqrt(sum(x*x for x in q)); eta = acosh(E)
    return boost([x/pm for x in q], eta), [x/pm for x in q], eta
def run(word, s0=(0,mpf(1)/sqrt(2),mpf(1)/sqrt(2))):
    L = matrix([[1 if i==j else 0 for j in range(4)] for i in range(4)]); hs=[]; etas=[]; turn=[]; prevn=None
    for k,w in enumerate(word):
        L = L*boost(AX[w], R5); p = [L[i,0] for i in range(4)]
        B, n, eta = stdboost(p); Rm = B**-1 * L      # pure rotation in the rest frame
        s = [sum(Rm[i+1,j+1]*s0[j] for j in range(3)) for i in range(3)]
        h = sum(s[i]*n[i] for i in range(3)); hs.append(h); etas.append(eta)
        if prevn is not None: turn.append(acos(max(-1,min(1,sum(n[i]*prevn[i] for i in range(3))))))
        prevn = n
    dh = [abs(hs[i]-hs[i-1]) for i in range(1,len(hs))]
    first, last = sum(dh[:10])/10, sum(dh[-10:])/10
    return hs, etas, dh, first, last, turn
def reduced(seq):  # forbid immediate backtrack (w then its inverse)
    out=[]; 
    for w in seq:
        if out and (w ^ 1) == out[-1]: continue
        out.append(w)
    return out
# twin-prime chain arms: next pair's end digit 1,7,9 -> i,j,k (all + direction)
N=200000; sv=bytearray(N+3)
for i in range(2,int((N+2)**.5)+1):
    if not sv[i]: sv[i*i::i]=b'\x01'*len(sv[i*i::i])
TW=[a for a in range(11,N) if not sv[a] and not sv[a+2]]
chain=[{1:0,7:2,9:4}[a%10] for a in TW[1:41]]
random.seed(7)
words = {
 'twin-prime chain (40 steps)': chain,
 'random reduced word A': reduced([random.randrange(6) for _ in range(80)])[:40],
 'random reduced word B': reduced([random.randrange(6) for _ in range(80)])[:40],
 'periodic i j k i j k ...': [0,2,4]*14,
 'OPPOSITE: one arm only (i i i ...)': [0]*40,
}
for name,wd in words.items():
    hs, etas, dh, first, last, turn = run(wd[:40])
    verdict = 'KILL FIRED' if last > 0.5*first else 'survives'
    print(f"{name}: rapidity after 40 steps {mp.nstr(etas[-1],5)}  helicity cosine start {mp.nstr(hs[0],5)} end {mp.nstr(hs[-1],8)}")
    print(f"   mean |dh| first 10 = {mp.nstr(first,4)}   last 10 = {mp.nstr(last,4)}   ratio = {mp.nstr(last/first if first else 0,4)}   -> {verdict}")
    if turn: print(f"   travel direction still turning: mean step angle first 10 = {mp.nstr(sum(turn[:10])/10,4)} rad, last 10 = {mp.nstr(sum(turn[-10:])/10,4)} rad")
