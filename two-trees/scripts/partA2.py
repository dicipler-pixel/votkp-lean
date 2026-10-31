# SCRIPT: LN7_PARTA_COMMUTATOR
# Exact translation length of the commutator [B_i, B_j] = B_i B_j B_-i B_-j and other short periodic words.
import sympy as sp, mpmath as mp, itertools
mp.mp.dps = 50
def Q(axis, sign):
    M = sp.diag(7,7,7,7); M[0,0]=25; M[axis,axis]=25; M[0,axis]=M[axis,0]=24*sign; return M
L = {'i':Q(1,1),'-i':Q(1,-1),'j':Q(2,1),'-j':Q(2,-1),'k':Q(3,1),'-k':Q(3,-1)}
inv = {'i':'-i','-i':'i','j':'-j','-j':'j','k':'-k','-k':'k'}
x = sp.symbols('x')
delta = mp.acosh(mp.mpf(9)/7)
def specrad(M):
    A = mp.matrix([[mp.mpf(int(sp.numer(M[r,c])))/mp.mpf(int(sp.denom(M[r,c]))) for c in range(4)] for r in range(4)])
    E, _ = mp.eig(A)
    return mp.log(max(abs(e) for e in E))
def transl(word):
    M = sp.eye(4)
    for a in word: M = M*L[a]
    M = M/sp.Integer(7)**len(word)
    p = sp.factor(M.charpoly(x).as_expr())
    return specrad(M), p, M.trace()
tau, p, tr = transl(['i','j','-i','-j'])
print('commutator charpoly:', p)
print('trace =', tr, ' tau =', mp.nstr(tau,20), ' tau/4 =', mp.nstr(tau/4,20), ' delta =', mp.nstr(delta,20))
print('cosh(tau) candidates: cosh(4 delta)=', mp.nstr(mp.cosh(4*delta),20))
# minimum per-letter translation over cyclically reduced periodic words up to period 6, first letter i
names=list(L)
res=[]
for P in range(1,7):
    for w in itertools.product(names, repeat=P-1):
        w=('i',)+w
        ok=all(w[(m+1)%P]!=inv[w[m]] for m in range(P))
        if not ok: continue
        M=sp.eye(4)
        for a in w: M=M*L[a]
        t=specrad(M)-P*mp.log(7)
        res.append((t/P,' '.join(w)))
res.sort()
for r in res[:8]: print(mp.nstr(r[0],15), r[1])
