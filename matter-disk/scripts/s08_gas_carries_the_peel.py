# SCRIPT: MATTER-DISK-S08  a gas carries the VOTKP peel coordinate in density-free combinations (helium)
# WHY THIS CHECK PROVES WHAT IT CLAIMS
# VOTKP v2.9 gives helium the ladder I0 = 24.587389011 eV, I1 = 54.4177655282 eV and the peel coordinate
# Gamma0 = (I1 - I0)/(I1 + I0). In an ideal Saha gas (ground-state weights U = 1, 2, 1) the populations
# n0, n1, n2 change enormously with temperature and density. Each adjacent pair is a point on the disk:
# odds z_q = n_q/n_(q+1), Gamma_pop,q = tanh(ln z_q / 2) (section 1), and half ionization is the centre.
# Two combinations lose the electron density and thermal wavelength exactly:
#   ln(n0 n2 / n1^2)               = -(I1 - I0)/kT - ln 4          (the second difference of the ladder)
#   ln(n0 / (n2 n_e^2 lambda^6))   =  (I0 + I1)/kT - ln 4          (the whole peel, both electrons)
# so their slopes in beta = 1/kT give D = I1 - I0 and B = I0 + I1, and D/B is Gamma0 at any density.
# KILL (written before the run):
#  (a) the populations at 1e22 m^-3 miss the 3 Nov review table (10, 20, 50 kK) by more than 1e-6 percent,
#      or the 20 kK density sweep misses 0.5680% (1e20) and 87.6482% (1e24) at the printed digits;
#  (b) Gamma0 recovered from the gas differs from 0.377575066984 by more than 1e-9 at any density 1e18..1e26;
#  (c) an independent solver (cubic in n_e) disagrees with the root finder by more than 1e-12.
import numpy as np
from scipy.optimize import brentq
h=6.62607015e-34; kB=1.380649e-23; me=9.1093837015e-31; eV=1.602176634e-19
I0,I1=24.587389011,54.4177655282; U=(1.0,2.0,1.0)
G0=(I1-I0)/(I1+I0)
def saha(T,n):
    kT=kB*T; lam3=(h/np.sqrt(2*np.pi*me*kT))**3
    S1=2*(U[1]/U[0])/lam3*np.exp(-I0*eV/kT); S2=2*(U[2]/U[1])/lam3*np.exp(-I1*eV/kT)
    s1,s2=S1/n,S2/n   # charge neutrality in x = ne/n: x(x^2 + s1 x + s1 s2) = s1 x + 2 s1 s2, root in (0, 2)
    g=lambda x: x*(x*x+s1*x+s1*s2)-(s1*x+2*s1*s2)
    ne=n*brentq(g,0.0,2.0,xtol=1e-300,rtol=1e-15,maxiter=2000)
    r1=S1/ne; r2=r1*S2/ne; Z=1+r1+r2
    return np.array([1,r1,r2])/Z, ne, lam3
def saha_cubic(T,n):
    kT=kB*T; lam3=(h/np.sqrt(2*np.pi*me*kT))**3
    S1=2*(U[1]/U[0])/lam3*np.exp(-I0*eV/kT); S2=2*(U[2]/U[1])/lam3*np.exp(-I1*eV/kT)
    # ne(ne^2 + S1 ne + S1 S2) = n(S1 ne + 2 S1 S2)  ->  ne^3 + S1 ne^2 + (S1 S2 - n S1) ne - 2 n S1 S2 = 0
    rts=np.roots([1.0,S1/n,(S1*S2-n*S1)/n**2,-2*S1*S2/n**2])*n
    ne=max(r.real for r in rts if abs(r.imag)<1e-9*abs(r) and r.real>0)
    r1=S1/ne; r2=r1*S2/ne; Z=1+r1+r2; return np.array([1,r1,r2])/Z
print(f'helium ladder (VOTKP v2.9): I0={I0} eV, I1={I1} eV, Gamma0={G0:.12f}')
rev={10000:(99.937400,0.062600,0.000000),20000:(28.978059,71.021940,0.000001),50000:(0.000873,17.146019,82.853108)}
oka=True; okc=True
print('(a) populations at n = 1e22 m^-3, percent [ours | review], and the disk point of each pair')
for T,r in rev.items():
    p,ne,_=saha(T,1e22); pc=saha_cubic(T,1e22); okc&=np.max(np.abs(p-pc))<1e-12
    good=all(abs(100*p[i]-r[i])<1e-6+5e-7 for i in range(3)); oka&=good
    Gp=[np.tanh(0.5*np.log(p[q]/p[q+1])) if p[q+1]>0 else 1.0 for q in range(2)]
    print(f'    T={T:6d} K  He {100*p[0]:10.6f}|{r[0]:10.6f}  He+ {100*p[1]:10.6f}|{r[1]:10.6f}  He2+ {100*p[2]:10.6f}|{r[2]:10.6f}  '
          f'Gamma_pop = ({Gp[0]:+.4f}, {Gp[1]:+.4f})  {"MATCH" if good else "DIFFER"}')
for n,target in [(1e20,0.5680),(1e24,87.6482)]:
    p,_,_=saha(20000,n); good=abs(100*p[0]-target)<5e-5; oka&=good
    print(f'    T=20000 K n={n:.0e}: neutral {100*p[0]:.4f}% | review {target}%  {"MATCH" if good else "DIFFER"}')
print('(a)', 'PASS' if oka else 'DIFFER'); print('(c) cubic solver agrees with the root finder:', 'PASS' if okc else 'FAIL')
# (b) recover Gamma0 from the gas alone at two temperatures, across densities
okb=True; worst=0
print('(b) Gamma0 read back from the gas (two temperatures 30 kK and 32 kK), by density')
for n in [1e18,1e20,1e22,1e24,1e26]:
    vals=[]
    for T in (30000,32000):
        p,ne,lam3=saha(T,n); beta=eV/(kB*T)  # beta in 1/eV
        vals.append((beta,np.log(p[0]*p[2]/p[1]**2),np.log(p[0]/(p[2]*ne**2*lam3**2))))
    (b1,a1,c1),(b2,a2,c2)=vals
    D=-(a2-a1)/(b2-b1); B=(c2-c1)/(b2-b1); Gr=D/B; worst=max(worst,abs(Gr-G0))
    p,_,_=saha(30000,n)
    print(f'    n={n:.0e}: neutral fraction at 30 kK {100*p[0]:9.5f}%   D={D:.9f} eV  B={B:.9f} eV  Gamma0={Gr:.12f}')
okb=worst<1e-9
print(f'(b) worst |Gamma0(gas) - Gamma0(VOTKP)| = {worst:.1e}', 'PASS' if okb else 'FAIL')
