# SCRIPT: VERIFY-SIGNS-02
# Second setup for VERIFY-SIGNS-01 part (2), which scanned only 0 < v < 0.02 on one matrix entry and found nothing.
# k = -v(v + dM) = 0.0083 has TWO real v: one near 0 and one near -dM (there tr(ab) - 2 is the small one).  Scan the whole
# band 0 < v < -dM (that is exactly v > 0 and tr(ab) > 2), on every entry of w a - b w, both ends on a fine grid.
# KILL as before: a bracketed root counts only if all four entries vanish there to 1e-80.
import mpmath as mp
mp.mp.dps=120
def rel(p,q,s,v):
    a=mp.matrix([[s,1],[0,1/s]]); b=mp.matrix([[s,0],[-v,1/s]]); ai=a**-1; bi=b**-1; w=mp.eye(2)
    for i in range(1,p):
        e=(-1)**((i*q)//p); g=(a if e>0 else ai) if i%2==1 else (b if e>0 else bi); w=w*g
    return w*a-b*w
s=mp.e**mp.mpf('0.8'); dM=2-(s**2+s**-2); top=-dM
grid=[top*mp.mpf(i)/4000 for i in range(1,4000)]+[mp.mpf(i)/100000 for i in range(1,400)]+[top-mp.mpf(i)/100000 for i in range(1,400)]
grid=sorted(set(grid)); found=[]
for (i,j) in ((0,0),(0,1),(1,0),(1,1)):
    f=lambda v:rel(89,34,s,v)[i,j]; fv=[f(v) for v in grid]
    for n in range(len(grid)-1):
        if fv[n]*fv[n+1]<0:
            r=mp.findroot(f,(grid[n],grid[n+1]),solver='anderson',tol=mp.mpf(10)**-100); res=max(abs(x) for x in rel(89,34,s,r))
            if res<mp.mpf(10)**-80 and not any(abs(r-x)<mp.mpf(10)**-50 for x,_ in found): found.append((r,res))
print('89/34, x = 0.8, -dM = %s: real band roots of the full relation: %d'%(mp.nstr(top,12),len(found)))
for r,res in sorted(found): print('   v = %s   tr(ab)-2 = %s   k = %s   residual %s'%(mp.nstr(r,20),mp.nstr(top-r,12),mp.nstr(-r*(r+dM),12),mp.nstr(res,3)))
