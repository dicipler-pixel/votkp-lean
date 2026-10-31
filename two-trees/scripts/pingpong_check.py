# SCRIPT: PINGPONG_CHECK
# Exact verification of the (1+i)-adic ping-pong on P^1(Q(i)) for z = 2^k (k>=1), with exact Gaussian rationals.
# Objects: M_u = (z+1) I + (z-1) sigma_u  (sigma_x,sigma_y,sigma_z Pauli);  rho(M)X = M X M^*/|det M| on Hermitian X.
# Check 1 (kill: rho(M_u) != B_u for some u, z  -> the dictionary boosts <-> M_u is wrong and the proof does not apply):
#   rho(M_u) equals the boost matrix B_u of the task (axis u, rapidity ln z).
# Check 2 (kill: a point w violates  f_s( P^1 \ U_{s^-1} ) in U_s  or two U's intersect -> the ping-pong inclusions are false):
#   six sets with v = v_pi(.) = v_2(Norm(.)) :  U_x+ = {v(w+1)>=3}, U_x- = {v(w-1)>=3}, U_y+ = {v(w-i)>=3},
#   U_y- = {v(w+i)>=3}, U_z+ = {v(w)>=1}, U_z- = {v(w)<=-1} u {inf}.   M_x,M_y,M_z act by Moebius maps f_x,f_y,f_z.
#   test on exact points (random + all residue-type points near the centres) the inclusions for all 6 letters.
# Check 3 (kill: a random reduced word w=s_1..s_n and a point p outside U_{s_n^-1} with w(p) outside U_{s_1}):
#   the consequence of the lemma, tested for 3000 random words of length up to 60 -> would show the six-set structure fails.
# Check 4 (kill: any nonempty reduced word with displacement d(w)=0 of the base vertex): d(w)=v(det)-2*min v(entries) of the
#   Z[i]-matrix product of N_u^{+-}=(z+1)+-(z-1)sigma_u over all reduced words up to length 6 and random ones up to 40.
import random, itertools, sys
from fractions import Fraction as Fr
class G:  # Gaussian rational
    __slots__=("a","b")
    def __init__(s,a=0,b=0): s.a=Fr(a); s.b=Fr(b)
    def __add__(s,o): o=g(o); return G(s.a+o.a,s.b+o.b)
    __radd__=__add__
    def __sub__(s,o): o=g(o); return G(s.a-o.a,s.b-o.b)
    def __rsub__(s,o): return g(o)-s
    def __mul__(s,o): o=g(o); return G(s.a*o.a-s.b*o.b,s.a*o.b+s.b*o.a)
    __rmul__=__mul__
    def __neg__(s): return G(-s.a,-s.b)
    def norm(s): return s.a*s.a+s.b*s.b
    def inv(s): n=s.norm(); return G(s.a/n,-s.b/n)
    def __truediv__(s,o): return s*g(o).inv()
    def iszero(s): return s.a==0 and s.b==0
    def __eq__(s,o): o=g(o); return s.a==o.a and s.b==o.b
    def __repr__(s): return "(%s+%si)"%(s.a,s.b)
def g(x): return x if isinstance(x,G) else G(x,0)
def v2(n):  # 2-adic valuation of a positive rational
    n=Fr(n); p,q=n.numerator,n.denominator; c=0
    while p%2==0: p//=2; c+=1
    while q%2==0: q//=2; c-=1
    return c
BIG=10**9
def vpi(x):
    x=g(x)
    if x.iszero(): return BIG
    return v2(x.norm())   # v_pi(x) = v_2(Norm x) since N(pi)=2 and odd primes are units
INF=None
def mob(M,w):
    a,b,c,d=M
    if w is INF:
        return INF if c.iszero() else a/c
    den=c*w+d
    if den.iszero(): return INF
    return (a*w+b)/den
I=G(0,1)
def Mmat(z,u,sg=1):
    zp,zm=z+1,sg*(z-1)
    if u=='x': return (G(zp),G(zm),G(zm),G(zp))
    if u=='y': return (G(zp),G(0,-zm),G(0,zm),G(zp))
    if u=='z': return (G(zp+zm),G(0),G(0),G(zp-zm))
def inU(name,w):
    if name=='x+': return w is not INF and vpi(w+1)>=3
    if name=='x-': return w is not INF and vpi(w-1)>=3
    if name=='y+': return w is not INF and vpi(w-I)>=3
    if name=='y-': return w is not INF and vpi(w+I)>=3
    if name=='z+': return w is not INF and vpi(w)>=1
    if name=='z-': return w is INF or vpi(w)<=-1
names=['x+','x-','y+','y-','z+','z-']
invname={'x+':'x-','x-':'x+','y+':'y-','y-':'y+','z+':'z-','z-':'z+'}
def letter_matrix(z,name): return Mmat(z,name[0],1 if name[1]=='+' else -1)
# For letter s, which set is U_s?  g_x+ (M_x) attracts to -1 : U_{x+} = B(-1,1/8) as in the proof; g_y+ attracts to +i; g_z+ attracts to 0.
def rand_pt(rng):
    t=rng.random()
    if t<0.05: return INF
    # random Gaussian rational with various 2-adic sizes
    def rn():
        return Fr(rng.randint(-40,40),rng.choice([1,1,2,3,4,5,8,16,32,64,7]))
    base=G(rn(),rn())
    ctr=rng.choice([G(0),G(1),G(-1),I,-I,None])
    if ctr is not None:
        sh=rng.choice([1,2,4,8,16,32,64]); pw=Fr(1,sh) if rng.random()<.5 else Fr(sh)
        eps=G(rng.randint(-3,3),rng.randint(-3,3))
        # point near centre at pi-adic distance ~ 2^-j : centre + (1+i)^j * small
        j=rng.randint(0,7); pij=G(1)
        for _ in range(j): pij=pij*G(1,1)
        return ctr+pij*G(rng.randint(-5,5)+rng.choice([0,1]),rng.randint(-5,5))*G(Fr(1,rng.choice([1,3,5,7])))
    return base
def check1():
    # rho(M) X = M X M^*/|det M|, basis X = I, sx, sy, sz ;  coordinates (t,x,y,z): X = t I + x sx + y sy + z sz
    import sympy as sp
    sx=sp.Matrix([[0,1],[1,0]]);sy=sp.Matrix([[0,-sp.I],[sp.I,0]]);sz=sp.Matrix([[1,0],[0,-1]]);I2=sp.eye(2)
    basis=[I2,sx,sy,sz]
    def coords(X):
        return [sp.simplify((X*B).trace()/2) for B in basis]  # tr(X sigma_a)/2 gives coordinate since tr(sa sb)=2 delta
    ok=True
    for z in (2,4,8,16):
        for u,(sig,ax) in {'x':(sx,1),'y':(sy,2),'z':(sz,3)}.items():
            M=(z+1)*I2+(z-1)*sig; det=M.det()
            cols=[]
            for B in basis:
                Y=M*B*M.H/sp.Abs(det)
                cols.append([sp.nsimplify(sp.simplify(c)) for c in coords(sp.simplify(Y))])
            R=sp.Matrix(cols).T   # R[:,j] = image of basis j
            c=sp.Rational(z*z+1,2*z); s=sp.Rational(z*z-1,2*z)
            Bm=sp.eye(4); Bm[0,0]=c;Bm[ax,ax]=c;Bm[0,ax]=s;Bm[ax,0]=s
            same = (R==Bm); ok&=bool(same)
            print("  z=%d axis %s: rho(M_u) == B_u(+ln z): %s"%(z,u,same))
    return ok
if __name__=="__main__":
    print("CHECK 1: rho(M_u)=B_u"); ok1=check1(); print("  ALL OK" if ok1 else "  FAILED (kill)")
    rng=random.Random(12345)
    # Check 2
    print("CHECK 2: disjointness and inclusions")
    bad=0; tested=0
    for z in (2,4,8,16,32):
        for _ in range(4000):
            w=rand_pt(rng)
            mem=[n for n in names if inU(n,w)]
            if len(mem)>1: bad+=1; print("  OVERLAP",w,mem)
            for s in names:
                if not inU(invname[s],w):
                    fw=mob(letter_matrix(z,s),w); tested+=1
                    # which U_s:  letter named 's+' (M_u) maps complement of U_{s-} into U_{s+}, where U_{x+}=B(-1,1/8) etc.
                    if not inU(s,fw): bad+=1; print("  VIOLATION z=%d s=%s w=%s f(w)=%s"%(z,s,w,fw))
    print("  tested inclusions:",tested,"violations/overlaps:",bad)
    # sanity: the points tested are spread over the sets
    cnt={n:0 for n in names}; cnt['none']=0
    for _ in range(4000):
        w=rand_pt(rng); m=[n for n in names if inU(n,w)]
        cnt[m[0] if m else 'none']+=1
    print("  distribution of random test points over the six sets:",cnt)
    # Check 3
    print("CHECK 3: reduced words")
    viol=0
    for z in (2,4,8):
        mats={s:letter_matrix(z,s) for s in names}
        for _ in range(1000):
            n=rng.randint(1,60); w=[rng.choice(names)]
            while len(w)<n:
                s=rng.choice(names)
                if s!=invname[w[-1]]: w.append(s)
            # find a test point outside U_{s_n^-1}
            for _t in range(200):
                p=rand_pt(rng)
                if not inU(invname[w[-1]],p): break
            q=p
            for s in reversed(w): q=mob(mats[s],q)
            if not inU(w[0],q): viol+=1
    print("  words tested 3000, violations:",viol)
    # Check 4
    print("CHECK 4: base-vertex displacement d(w)=v(det)-2 v(content)")
    def mmul(A,B): return (A[0]*B[0]+A[1]*B[2],A[0]*B[1]+A[1]*B[3],A[2]*B[0]+A[3]*B[2],A[2]*B[1]+A[3]*B[3])
    for z in (2,4,8):
        k={2:1,4:2,8:3}[z]; vdet=4+2*k
        mats={s:letter_matrix(z,s) for s in names}
        mind=BIG; cnt=0
        def rec(M,n,last,maxn):
            global mind,cnt
            if n>0:
                d=n*vdet-2*min(vpi(e) for e in M); cnt+=1
                if d<=0: print("   d<=0 for a reduced word!",d); sys.exit(1)
                mind=min(mind,d)
            if n==maxn: return
            for s in names:
                if last is not None and s==invname[last]: continue
                rec(mmul(M,mats[s]) if n>0 else mats[s],n+1,s,maxn)
        rec(None,0,None,5)
        print("  z=%d exhaustive reduced words of length 1..5: %d words, min displacement %d (>0 for all)"%(z,cnt,mind))
        md=BIG
        for _ in range(300):
            n=rng.randint(6,40); w=[rng.choice(names)]
            while len(w)<n:
                s=rng.choice(names)
                if s!=invname[w[-1]]: w.append(s)
            M=mats[w[0]]
            for s in w[1:]: M=mmul(M,mats[s])
            d=n*vdet-2*min(vpi(e) for e in M); md=min(md,d)
            if d<=0: print("   d<=0 random!"); sys.exit(1)
        print("  z=%d 300 random reduced words length 6..40: min displacement %d (>0)"%(z,md))
