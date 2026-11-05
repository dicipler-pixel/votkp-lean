"""s17: symbolic check of Theorem 5.4(b). W=w', r=sqrt(E0*Epi), D=sqrt(4W^2u^2+(u^2-r^2)^2).
F = u^2 w^2 (W+r) - W (w^2-v'^2)^2 vanishes iff theta = pi/2."""
import sympy as sp
W,r,u,D=sp.symbols('W r u D',positive=True)
d=u**2-r**2
w2=W**2+(d+D)/2; vp2=W**2-r**2
F=sp.expand(u**2*w2*(W+r)-W*(w2-vp2)**2)
prod=sp.expand(sp.expand(F*F.subs(D,-D)).subs(D**2,4*W**2*u**2+d**2))
fac=sp.factor(prod)
target=W*r**2*u**2*(W+r)**2*(W-r)*(u**2-r**2)
lines=[f'F(D)F(-D) factors as: {fac}',
       f'F(D)F(-D) - W r^2 u^2 (W+r)^2 (W-r)(u^2-r^2) = {sp.simplify(prod-sp.expand(target))}',
       f'F on the line u=r (D=2Wu): {sp.simplify(F.subs(D,2*W*u).subs(r,u))}']
# root-check: w^2 is the larger root of x^2-(2W^2-r^2+u^2)x+W^2(W^2-r^2)
x=sp.symbols('x'); q=x**2-(2*W**2-r**2+u**2)*x+W**2*(W**2-r**2)
lines.append(f'w^2 satisfies the quadratic: {sp.simplify(sp.expand(q.subs(x,w2)).subs(D**2,4*W**2*u**2+d**2))}')
print('\n'.join(lines)); open('../outputs/s17_exit_converse_sympy.txt','w').write('\n'.join(lines)+'\n')
