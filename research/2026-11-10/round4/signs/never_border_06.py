# SCRIPT: NEVER-BORDER-06
# Q3 precision re-check. NEVER-CENSUS-02 (80 digits) flagged three never-turners with a nearly real complex pair inside
# the half band: 37/13, 61/21, 63/13 (relative imaginary part between 1e-6.5 and 1e-15.6). They are re-run at 160 digits.
print('''WHY: if the pair were a real double root blurred by round-off, its imaginary part would shrink with the digits.
If it is a true complex pair, the relative imaginary part is the same at 80 and 160 digits.
KILL (for the verdict NEVER): a real root in the half band at 160 digits at any grid x, or an imaginary part that
drops by more than a factor 10 between 80 and 160 digits.''')
import sys, mpmath as mp
from multiprocessing import Pool
sys.path.insert(0,'/home/claude/work/agent_signs')
from riley_exact_w import *
XS=[0.1*i for i in range(1,16)]+[2.0,2.5,3.0,3.5,4.0]
def run(k):
    p,q=k; by=riley(p,q); bw=to_w(by); out={}
    for dps in (80,160):
        real=0; mins=[]
        for x in XS:
            for b in (by,bw):
                mp.mp.dps=dps; s=mp.e**mp.mpf(x); A=s*s+1/(s*s)-2; hi=A/2 if A*A<=16 else (A-mp.sqrt(A*A-16))/2; co=vcoeffs(b,s)
                roots=mp.polyroots(co,maxsteps=2000+50*len(co),extraprec=6*dps+20*len(co))
                for r in roots:
                    rr=mp.re(r)
                    if 0<rr<hi:
                        im=abs(mp.im(r))/abs(r)
                        if im<=mp.mpf(10)**(-dps//2): real+=1
                        else: mins.append((float(mp.log10(im)),x))
        out[dps]=(real,min(mins) if mins else None)
    return k,out
if __name__=='__main__':
    with Pool(2) as pool:
        for k,out in pool.imap(run,[(37,13),(61,21),(63,13)]):
            print('%d/%d cf %s: 80 digits: real band roots %d, smallest log10 relative |Im| in the half band %s ; 160 digits: real band roots %d, smallest %s'%(k[0],k[1],cf(*k),out[80][0],out[80][1],out[160][0],out[160][1]),flush=True)
