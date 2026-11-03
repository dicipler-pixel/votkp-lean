# SCRIPT: MATTER-PEEL-02B2  branch-safe Renyi-2 at the NH SSH EP critical point
import numpy as np
exec(open('nhssh_lib_and_s03a_occupations.py').read().split("w=1.0")[0])
w=1.0
def run(v,u,N,Ls):
    S2=[];Sv=[]
    for Lc in Ls:
        nu=np.linalg.eigvals(corr(v,w,u,N,Lc)).astype(complex)
        S2.append(-np.sum(np.log(nu**2+(1-nu)**2)))
    x=np.log(N/np.pi*np.sin(np.pi*np.array(Ls)/N))
    S2=np.array(S2); sl=np.polyfit(x,S2.real,1)[0]
    return 4*sl, np.max(np.abs(S2.imag)), S2.real
for (v,u,tag) in [(1.0,0.0,'Hermitian critical control'),(0.5,0.5,'EP critical, v<w'),(1.5,0.5,'EP critical, v>w'),(0.5,0.3,'NH gapped control')]:
    for N in (1000,2000):
        c,im,S=run(v,u,N,[10,20,40,80,160])
        print(f'{tag:28s} N={N}: c from Renyi-2 = {c:+.3f}   max|Im S2|={im:.1e}   S2={np.round(S,3)}')
