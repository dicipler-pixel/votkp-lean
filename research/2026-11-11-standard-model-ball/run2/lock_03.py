# SCRIPT: SM-LOCK-03
# LOCK with the instrument controlled: digits set so every lap stays resolved (entries ~ e^(l k); need dps > 3 l k / ln 10).
# Prediction and KILL as in SM-CANCEL-LOCK-01: per-lap own-frame turn converges to the twist |theta| from tr M = 2 cosh((l + i theta)/2);
# KILL: spread of laps 16-20 > 1e-8 or |lap 20 - |theta|| > 1e-8.
exec(open('cancel_lock_01.py').read().split('random.seed(11)')[0])
from mpmath import acosh as macosh
mp.dps = 400
def M2(word):
    M = matrix([[1,0],[0,1]])
    for w in word:
        n = AX[w]; c, s = cosh(R5/2), sinh(R5/2)
        S = matrix([[c + s*n[2], s*(n[0] - 1j*n[1])], [s*(n[0] + 1j*n[1]), c - s*n[2]]])
        M = M*S
    return M

for name, u in [('i j k', [0,2,4]), ('i j', [0,2]), ('i j -i k', [0,2,1,4]), ('i i j', [0,0,2]), ('i -j k -i j', [0,3,4,1,2]), ('twin chain, first 6 arms', None)]:
    if u is None:
        N=2000; sv=bytearray(N+3)
        for i in range(2,int((N+2)**.5)+1):
            if not sv[i]: sv[i*i::i]=b'\x01'*len(sv[i*i::i])
        TW=[a for a in range(11,N) if not sv[a] and not sv[a+2]]; u=[{1:0,7:2,9:4}[a%10] for a in TW[1:7]]
    M = M2(u); tr = M[0,0] + M[1,1]; lam = 2*macosh(tr/2); th = abs(im(lam)) % (2*pi)
    if th > pi: th = 2*pi - th
    L1 = Lw(u); Lk = eye(4); prevR = None; out = []
    for k in range(1, 21):
        Lk = Lk*L1; Rk = polar(Lk)
        if prevR is not None:
            D = Rk*prevR.T; trr = D[1,1]+D[2,2]+D[3,3]; out.append(acos(max(-1, min(1, (trr-1)/2))))
        prevR = Rk
    last = out[-5:]; spread = max(last)-min(last)
    v = "KILL FIRED" if (spread > mpf('1e-8') or abs(out[-1]-th) > mpf('1e-8')) else "survives"
    print(f"{name:>26}: twist |theta| {mp.nstr(th,16)}  lap-20 turn {mp.nstr(out[-1],16)}  |diff| {mp.nstr(abs(out[-1]-th),3)}  spread laps 16-20 {mp.nstr(spread,3)}  climb per lap {mp.nstr(abs(re(lam)),8)}  -> {v}")
