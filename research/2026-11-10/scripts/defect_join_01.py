# SCRIPT: DEFECT-JOIN-01
# Recovery: Two Trees' commutator number k = 2 - tr[a,b] is UPG's relator defect delta = |lambda - 1|^2 (UPGTorusAnchor),
# and the limit values of census 8.8 with m = 1 are the clock-and-shift defects 4 sin^2(pi j/d) (UPG Prop 4.9).
# Why this decides it: (1) the identity is exact for any unit-modulus eigenvalue pair; (2) each printed limit value is
# tested against 4 sin^2(pi j/d) for every d <= 30; a value with no match is reported.  Kill: an m = 1 limit with no match.
import sympy as sp
th=sp.symbols('theta',real=True)
print('identity 2 - 2cos(theta) - |e^{i theta} - 1|^2 =',sp.simplify(2-2*sp.cos(th)-sp.Abs(sp.exp(sp.I*th)-1)**2))
phi=(1+sp.sqrt(5))/2
vals={'1':sp.Integer(1),'2':sp.Integer(2),'3':sp.Integer(3),'phi^2':phi**2,'phi^-2':phi**-2,
      '(2cos pi/7)^2':(2*sp.cos(sp.pi/7))**2,'(2cos 2pi/7)^2':(2*sp.cos(2*sp.pi/7))**2,'(2cos 3pi/7)^2':(2*sp.cos(3*sp.pi/7))**2,
      '1/2':sp.Rational(1,2),'1/4':sp.Rational(1,4),'1/9':sp.Rational(1,9),'phi^2/4':phi**2/4,'phi^-2/4':phi**-2/4}
for name,v in vals.items():
    hit=None
    for d in range(3,31):
        for j in range(1,d):
            if abs(sp.N(4*sp.sin(sp.pi*j/d)**2-v,30))<1e-25: hit=(j,d); break
        if hit: break
    print('  k_inf = %-16s'%name, ('= 4 sin^2(%d pi/%d): relator omega = e^(2 pi i %d/%d), guard^2 = %s'%(hit[0],hit[1],hit[0],hit[1],sp.nsimplify(sp.N(4-v,20),[sp.sqrt(5)])) ) if hit else 'no clock value with d <= 30')
