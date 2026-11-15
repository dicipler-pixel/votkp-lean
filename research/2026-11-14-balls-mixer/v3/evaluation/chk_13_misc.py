# SCRIPT: CHK-13-MISC (orbit return times n(<eps) at z=5; chain displacement vs path length; unequal triples to depth 5; residues mod z at z=2,3,4,6; strip z values; 4_1 limit)
import numpy as np, math
def boost(u,r):
    u=np.array(u,float); c,s=math.cosh(r),math.sinh(r); B=np.zeros((4,4)); B[0,0]=c; B[0,1:]=s*u; B[1:,0]=s*u
    B[1:,1:]=np.eye(3)+(c-1)*np.outer(u,u); return B
# (a) return times, exact Fraction-free float64 with renormalisation
r=math.log(5); A=boost([1,0,0],r); B=boost([0,1,0],r); C=A@B@np.linalg.inv(A)@np.linalg.inv(B)
x=np.array([1.,0,0,0]); thr=[0.1,0.01,0.001]; found={}; eta=np.diag([1,-1,-1,-1.])
for n in range(1,10001):
    x=C@x; x=x/math.sqrt(x@eta@x); d=math.acosh(max(1,x[0]))
    for t in thr:
        if t not in found and d<t: found[t]=(n,d)
print("(a) first n with d(o,c^n o)<eps, z=5 (float64, renormalised):",found,"  R6-23: n=83 (d=3.979e-2), 1345 (2.435e-3), 7594 (5.376e-4)")
# (b) chain displacement vs path length (positions by boosts of ratio a'/a along arm of end digit of a')
def sieve(N):
    s=bytearray([1])*(N+1); s[0]=s[1]=0
    for i in range(2,int(N**0.5)+1):
        if s[i]: s[i*i::i]=bytearray(len(s[i*i::i]))
    return s
S=sieve(100002); TW=[a for a in range(11,100001) if S[a] and S[a+2]]
arm={1:[1,0,0],7:[0,1,0],9:[0,0,1]}
M=np.eye(4); 
for k in (10,50,200,len(TW)-1):
    M=np.eye(4)
    for i in range(k):
        M=M@boost(arm[TW[i+1]%10],math.log(TW[i+1]/TW[i]))
    d=math.acosh(max(1,(M@np.array([1.,0,0,0]))[0])); print("(b) pairs",k,"path length ln(a/11)",round(math.log(TW[k]/11),4),"displacement",round(d,4),"ratio",round(d/math.log(TW[k]/11),4))
# (c) unequal triples
def run3(zs,depth=5):
    gens=[]
    for a in range(3):
        u=[0,0,0]; u[a]=1; rr=math.log(zs[a]); gens+=[boost(u,rr),boost([-v for v in u],rr)]
    o=np.array([1.,0,0,0]); pts={tuple(np.round(o[1:]/(1+o[0]),7)):o}; front=[(np.eye(4),-1)]
    for d in range(1,depth+1):
        nf=[]
        for M,last in front:
            for k in range(6):
                if last>=0 and (k^1)==last: continue
                M2=M@gens[k]; p=M2@o; pts.setdefault(tuple(np.round(p[1:]/(1+p[0]),7)),p); nf.append((M2,k))
        front=nf
    P=np.array(list(pts.values())); G=P[:,0][:,None]*P[:,0][None,:]-P[:,1:]@P[:,1:].T; np.fill_diagonal(G,np.inf); return len(P),math.acosh(max(1,G.min()))
for zs in [(5,5,5),(3,5,7),(2,3,5),(5,7,11),(7,7,7)]:
    n,m=run3(zs); print("(c) triple",zs,"distinct",n,"min dist depth5",round(m,6),"smallest ln z",round(math.log(min(zs)),6),"holds" if m>math.log(min(zs))-1e-6 else "falls")
# (d) residues of the scaled integer boost a00 mod z, depth<=5 (scale 2z)
def Bint(z,d,sg):
    M=[[0]*4 for _ in range(4)]; n=z*z+1; m=z*z-1; M[0][0]=n; M[0][d+1]=sg*m; M[d+1][0]=sg*m
    for i in range(1,4): M[i][i]=2*z
    M[d+1][d+1]=n; return M
mm=lambda A,B:[[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
for z in (2,3,4,6):
    gens=[(d,sg,Bint(z,d,sg)) for d in range(3) for sg in (1,-1)]; fr=[(None,[[1 if i==j else 0 for j in range(4)] for i in range(4)])]; cnt=0; zero=0
    for depth in range(1,6):
        nf=[]
        for last,M in fr:
            for (d,sg,G) in gens:
                if last==(d,-sg): continue
                P=mm(M,G); cnt+=1; zero+= (P[0][0]%z==0); nf.append(((d,sg),P))
        fr=nf
    print("(d) z",z,"words",cnt,"a00 divisible by z:",zero," (R6-11: z=2: 2640, z=4: 762, z=3,6: 0)")
# (e) strip: z from tr=4-mu
for mu in (0,1,1.5):
    tr=4-mu; k=math.acosh(tr/2); z=math.exp(k); print("(e) mu",mu,"tr",tr,"z=e^kappa",round(z,6),"Gamma^2",round(((z-1)/(z+1))**2,6))
print("(e) 2+sqrt3, (3+sqrt5)/2, 2:",2+math.sqrt(3),(3+math.sqrt(5))/2)
