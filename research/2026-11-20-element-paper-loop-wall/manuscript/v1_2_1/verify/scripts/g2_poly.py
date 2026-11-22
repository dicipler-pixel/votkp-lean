# SCRIPT: G2_POLY (figure-eight decay-direction polynomial coefficient; lambda normalisation; torus phases)
import mpmath as mp
mp.mp.dps=30
vol=mp.mpf('2.029883212819307250042405108549')  # volume of the figure-eight knot complement
print('2cosh(2 vol/pi)=',mp.nstr(2*mp.cosh(2*vol/mp.pi),8))
print('with 2.02988:',mp.nstr(2*mp.cosh(2*mp.mpf('2.02988')/mp.pi),8))
lam=2j/mp.pi
for CS,V in ((0,vol),(0.7,1.1)):
    V0=-CS+1j*V; u=mp.e**(lam*V0)
    print('|u|',mp.nstr(abs(u),10),'exp(-2Vol/pi)',mp.nstr(mp.e**(-2*V/mp.pi),10),' arg u',mp.nstr(mp.arg(u),8),'-2CS/pi',mp.nstr(-2*CS/mp.pi,8))
    # CS shift by pi^2/2 flips sign; by pi^2 gives identity
    print(' shift pi^2/2 ->',mp.nstr(mp.e**(lam*(V0+mp.pi**2/2))/u,6),' shift pi^2 ->',mp.nstr(mp.e**(lam*(V0+mp.pi**2))/u,6))
    # conj partner 1/conj(u) = holonomy with opposite volume and same CS
    V0p=-CS-1j*V;up=mp.e**(lam*V0p);print(' partner check',mp.nstr(abs(up-1/mp.conj(u)),5))
# 8_19 direction 11/12 and torus: -k^2/(pq) mod 1 are pq-th roots of unity
import itertools
from fractions import Fraction
for p,q in ((2,3),(3,4),(3,5)):
    ph={(-Fraction(k*k,p*q))%1 for k in range(1,p*q)}
    print((p,q),sorted(ph)[:6],'all pq-th roots:',all((x*p*q).denominator==1 for x in ph))
print('figure-eight shape poly roots',mp.polyroots([1,-1,1]),'exp(i pi/3)=',mp.e**(1j*mp.pi/3))
