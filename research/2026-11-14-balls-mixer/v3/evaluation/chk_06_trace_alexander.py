# SCRIPT: CHK-06-TRACE-ALEXANDER (R_7 roots, Delta_7(t)=R_7(t+1/t), recurrence P_m(t+1/t)=D_m(t) m<=50, Delta^2 coefficients, torus Riley roots)
import sympy as sp, numpy as np, math
t,x=sp.symbols('t x')
R7=x**3-x**2-2*x+1
print("roots R_7:",sorted(np.roots([1,-1,-2,1]).real), " 2cos((2j-1)pi/7):",sorted(2*math.cos((2*j-1)*math.pi/7) for j in (1,2,3)))
print("T25 roots:",sorted(np.roots([1,-1,-1]).real)," 2cos((2j-1)pi/5):",sorted(2*math.cos((2*j-1)*math.pi/5) for j in (1,2)))
D=sp.expand(t**-3*sum((-1)**j*t**j for j in range(7)))
print("Delta_7 =",D, " R_7(t+1/t)-Delta_7 =", sp.simplify(sp.expand(R7.subs(x,t+1/t))-D))
Dsq=sp.expand(D**2); print("Delta^2 coeffs t^-6..t^6:",[Dsq.coeff(t,k) for k in range(-6,7)])
P=[sp.Integer(1), x-1]
for m in range(1,50): P.append(sp.expand(x*P[m]-P[m-1]))
bad=0
for m in range(0,51):
    Dm=sp.expand(t**-m*sum((-1)**j*t**j for j in range(2*m+1)))
    if sp.expand(P[m].subs(x,t+1/t)-Dm)!=0: bad+=1
print("recurrence mismatches m=0..50:",bad, " P_3 == R_7:", sp.expand(P[3]-R7)==0)
# control C1: figure-eight Delta must fail trefoil formula
print("control: 3-t-1/t vs t+1/t-1 differ:", sp.simplify((3-t-1/t)-(t+1/t-1))!=0)
