# SCRIPT: c2_arb_enclosure
"""Independent interval-arithmetic check of |R| <= C|G|^5 (python-flint / Arb).
usage: python3 code/votkp/c2_arb_enclosure.py C rho1 [path/to/c2_taylor_S.json]   e.g. 0.70 0.9999
Region A, |G|<=1/2: exact series coefficients as balls, closed-form tail (no Cauchy constant M).
Region B, 1/2<=|G|<=rho1: squares in the G plane, ball value at centre plus ball gradient bound.
Covers the G disk directly, so no z-plane cutoffs. Skip tests carry a 1e-12 float margin."""
import sys,json,time,math
from flint import acb,arb,ctx
from multiprocessing import Pool
ctx.prec=120
pi=arb.pi(); s3=arb(3).sqrt()
w=acb(arb(1)/2,s3/2); wb=w.conjugate(); xi=wb/w; xii=w/wb
I=acb(0,1)
V0=w.polylog(2).imag
C2=3*s3/4;C3=s3/4;C4=3*s3/16
K=40
l0=[acb(0,pi/3)]+[(1-xi**n)/n for n in range(1,K+1)]
l1=[acb(0,-pi/3)]+[(1-xii**n)/n for n in range(1,K+1)]
Ln=[w.polylog(2)]+[ -sum((l1[i]*(n-i)*l0[n-i] for i in range(n)),acb(0))/n for n in range(1,K+1)]
conj=lambda l:[x.conjugate() for x in l]
L0c,L1c,Lc=conj(l0),conj(l1),conj(Ln)
def prod(a,b,n): return sum((a[i]*b[n-i] for i in range(1,n)),acb(0))   # interior i=1..n-1
c={(0,0):acb(V0)}
for a in range(1,K+1):
    c[a,0]=Ln[a]/(2*I)+(prod(l1,l0,a)+l1[0]*l0[a]+l1[a]*l0[0]+l1[a]*L0c[0]-L1c[0]*l0[a])/(4*I)
    c[0,a]=-Lc[a]/(2*I)+(l1[0]*L0c[a]-prod(L1c,L0c,a)-L1c[0]*L0c[a]-L1c[a]*L0c[0]-L1c[a]*l0[0])/(4*I)
for a in range(1,K+1):
    for b in range(1,K+1-a):
        c[a,b]=(l1[a]*L0c[b]-L1c[b]*l0[a])/(4*I)
# collect degree>=5 by k,j
terms={}
for (a,b),v in c.items():
    if a+b>=5: terms.setdefault(a+b,[]).append((a-b,v))
def Bk(k):
    H=sum(1/m for m in range(1,k))
    mixed=4*H/k; pure=2*((2*math.pi/3+4*H)/(2*k)+(8*H/k+4*math.pi/3/k+4*math.pi/3/k)/4)
    return mixed+pure
ctx.prec=80
def f_A(r,e):
    pw={0:acb(1)}
    for j in range(1,K+1): pw[j]=pw[j-1]*e
    ei=1/e
    pn={0:acb(1)}
    for j in range(1,K+1): pn[j]=pn[j-1]*ei
    s=acb(0);rp=arb(1)
    for k in range(5,K+1):
        t=acb(0)
        for j,v in terms[k]: t+=v*(pw[j] if j>=0 else pn[-j])
        s+=t*rp; rp=rp*r
    return s
def region_A(C,rs=arb(1)/2):
    B41=Bk(41); assert all(Bk(k)<=2 for k in (41,50,100,1000))
    n=0;worst=0
    stack=[(0.0,.5,float(2*math.pi*i/90),float(2*math.pi/90)) for i in range(90)]
    while stack:
        r0,r1,t0,dt=stack.pop();n+=1
        rb=arb((r0+r1)/2,(r1-r0)/2);tb=arb(t0+dt/2,dt/2+1e-15)
        e=acb(tb.cos(),tb.sin())
        v=f_A(rb,e)
        tail=2*arb(r1)**36/(1-arb(r1))
        ub=v.real.abs_upper()+tail
        if ub<C:
            if float(ub.mid() if hasattr(ub,'mid') else ub)>worst: worst=float(ub.mid())
            continue
        if n>400000 or dt<1e-7: return ('FAIL: not below C near r,theta',r0,r1,t0,n)
        if (r1-r0)>dt*0.25:
            m=(r0+r1)/2; stack+= [(r0,m,t0,dt),(m,r1,t0,dt)]
        else: stack+= [(r0,r1,t0,dt/2),(r0,r1,t0+dt/2,dt/2)]
    return n,worst
def box(gx,gy,h,C,rho1):
    # returns True if settled
    gm=math.hypot(gx,gy); d=h*1.4142135623731
    if gm+d<.5-1e-12 or gm-d>rho1+1e-12: return True
    G=acb(arb(gx,h),arb(gy,h)); 
    rmaxb=(arb(gx).__abs__()+h)**2+(arb(gy).__abs__()+h)**2
    if not (rmaxb<1): return False
    a=1-G; b=1-xi*G; c_=1-xii*G
    dl0=1/a-xi/b; dl1=1/a-xii/c_
    z=w*b/a; o=wb*c_/a
    if z.abs_lower()<=0 or o.abs_lower()<=0: return False
    lz=(z.abs_upper()).log().abs_upper(); lz2=(z.abs_lower()).log().abs_upper(); ul=max(lz,lz2)
    lo=(o.abs_upper()).log().abs_upper(); lo2=(o.abs_lower()).log().abs_upper(); ul2=max(lo,lo2)
    gD=ul*dl1.abs_upper()+ul2*dl0.abs_upper()
    rm=arb(gm+d)
    if rm>1: rm=arb(1)
    gP=2*C2*rm+3*C3*rm**2+4*C4*rm**3
    g=acb(gx,gy); zc=w*(1-xi*g)/(1-g)
    Dv=zc.polylog(2).imag+(1-zc).arg()*(zc.real**2+zc.imag**2).log()/2
    r2=g.real**2+g.imag**2
    P=V0-C2*r2+C3*(g**3).real+C4*r2*r2
    rlo=max(gm-d-1e-12,.5)
    ub=(Dv-P).abs_upper()+(gD+gP)*arb(d)
    return bool(ub<C*arb(rlo)**5)
def run(q):
    (x0,y0,C,rho1)=q
    n=0;bad=0;minh=1
    st=[(x0+.5,y0+.5,.5)]
    while st:
        x,y,h=st.pop();n+=1
        if box(x,y,h,C,rho1): continue
        if h<2**-30: bad+=1;continue
        minh=min(minh,h)
        h2=h/2
        st+=[(x+s*h2,y+t*h2,h2) for s in(-1,1) for t in(-1,1)]
    return n,bad,minh
if __name__=='__main__':
    C=float(sys.argv[1]);rho1=float(sys.argv[2])
    # check against shipped coefficients
    T=json.load(open(sys.argv[3] if len(sys.argv)>3 else '.scratch/c2_taylor_S.json'))
    m=0
    for key,(re,im) in T['coeffs'].items():
        a,b=map(int,key.split(','))
        m=max(m,float((c[a,b]-acb(float(re),float(im))).abs_upper()))
    print('max diff mine vs shipped coefficients',m,'n',len(T['coeffs']))
    OUT={'coefficient_max_difference_vs_jets':m}
    miss=[(k,float(v.abs_upper())) for k,v in c.items() if f'{k[0]},{k[1]}' not in T['coeffs'] and float(v.abs_upper())>1e-12]
    print('coeffs of mine, non-negligible, absent from shipped file:',len(miss),miss[:5],flush=True)
    t=time.time();A=region_A(arb(C));OUT['region_A_cells'],OUT['region_A_worst']=A;print('region A',A,time.time()-t,flush=True)
    OUT['C']=C;OUT['rho1']=rho1
    t=time.time()
    with Pool(2) as p: res=p.map(run,[(x,y,C,rho1) for x in(-1,0) for y in(-1,0)],chunksize=1)
    print('region B (n,unresolved,minh)',res,'total',sum(r[0] for r in res),time.time()-t)
    OUT['region_B_squares']=sum(r[0] for r in res);OUT['region_B_unresolved']=sum(r[1] for r in res)
    json.dump(OUT,open('.scratch/c2_arb_enclosure.json','w'),indent=1)
