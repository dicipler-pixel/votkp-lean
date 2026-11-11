# SCRIPT: VERIFY-SIGNS-05
# Independent check of the second worker's correction "89/34 TURNS" (earlier today it was recorded as never).
# VERIFY-SIGNS-02 tested the wrong word (even q in an odd-q formula); 03 and 04 bracketed a sign change and then stopped inside
# mpmath's root polisher (division by zero at convergence).  This run uses plain bisection.
# Why this decides it: the group relation w a = b w is built directly from the two-bridge word of 89/55 (the odd-q form of
# 89/34, mirror), sharing no code with the earlier scripts or the second worker's library.  A real v in the band
# (v > 0, tr(ab) > 2, 0 < k < 4) at which ALL FOUR entries of w a - b w vanish is a real representation in the turning band.
# Convention check first: figure-eight 5/3 at v = 0 must satisfy the relation exactly when s^2 is an Alexander root.
# KILL: no bracketed root in the band, or the other entries do not vanish (> 1e-80) at it.
import mpmath as mp
mp.mp.dps=130
def rel(p,q,s,v):
    a=mp.matrix([[s,1],[0,1/s]]); b=mp.matrix([[s,0],[-v,1/s]]); ai=a**-1; bi=b**-1; w=mp.eye(2)
    for i in range(1,p):
        e=(-1)**((i*q)//p); g=(a if e>0 else ai) if i%2==1 else (b if e>0 else bi); w=w*g
    return w*a-b*w
phi=(3+mp.sqrt(5))/2
print('convention: 5/3 at v=0, residual at s^2 = Alexander root %s; at s = 1.3: %s'%(mp.nstr(max(abs(x) for x in rel(5,3,mp.sqrt(phi),0)),3),mp.nstr(max(abs(x) for x in rel(5,3,mp.mpf('1.3'),0)),3)))
def bis(f,lo,hi):
    flo=f(lo)
    for _ in range(420):
        mid=(lo+hi)/2; fm=f(mid)
        if fm==0: return mid
        if (fm>0)==(flo>0): lo,flo=mid,fm
        else: hi=mid
    return (lo+hi)/2
for x in ('0.8','1.2'):
    s=mp.e**mp.mpf(x); dM=2-(s**2+s**-2); top=-dM
    grid=sorted(set([top*mp.mpf(i)/3000 for i in range(1,3000)]+[mp.mpf(i)/100000 for i in range(1,300)]+[top-mp.mpf(i)/100000 for i in range(1,300)]))
    f=lambda v:rel(89,55,s,v)[0,1]; fv=[f(v) for v in grid]; found=[]
    for n in range(len(grid)-1):
        if fv[n]*fv[n+1]<0:
            r=bis(f,grid[n],grid[n+1]); res=max(abs(z) for z in rel(89,55,s,r)); scale=max(abs(z) for z in rel(89,55,s,r*(1+mp.mpf(10)**-6)))
            found.append((r,res,scale))
    print('89/34 (as 89/55), x = %s: sign changes of one entry in the band: %d'%(x,len(found)))
    for r,res,scale in found:
        print('   v = %s  tr(ab)-2 = %s  k = %s  all-entry residual %s (entries are ~%s one part in 1e6 away)'%(mp.nstr(r,18),mp.nstr(top-r,10),mp.nstr(-r*(r+dM),10),mp.nstr(res,3),mp.nstr(scale,3)))
