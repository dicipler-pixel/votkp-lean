"""Independent checks of formulas printed in Beasley BH v2 (August 2026).

This is a new audit script, not an edit to the author's originals.
Run from the workspace root with Python 3 and sympy.
"""
import json
from pathlib import Path
import sympy as s

w1, w2 = s.symbols('w1 w2', positive=True)
w3 = 1-w1-w2
t1, t2, t3 = s.symbols('t1 t2 t3', real=True)
G = s.Matrix([
    [(1/w1+1/w2)/8, (1/w1-1/w2)/(8*s.sqrt(3))],
    [(1/w1-1/w2)/(8*s.sqrt(3)), (1/w1+1/w2+4/w3)/24],
])
A = s.Matrix([
    [t1+t2-(t1-t2)*(w1-w2), ((t1-t2)-(t1+t2-2*t3)*(w1-w2))/s.sqrt(3)],
    [s.sqrt(3)*(t1-t2)*w3, 2*t3+w3*(t1+t2-2*t3)],
])
physical_adjoint_residual = s.simplify(G*A-A.T*G)
assert physical_adjoint_residual == s.zeros(2)
example = {w1:s.Rational(1,2), w2:s.Rational(3,10), t1:2, t2:1, t3:s.Rational(13,10)}
euclidean_commutator = s.simplify((A*A.T-A.T*A).subs(example))
assert euclidean_commutator != s.zeros(2)

q, a = s.symbols('q a', positive=True)
weights = [a*(1-q), (1-a)*(1-q), q]
radial_g = s.simplify(sum(s.diff(w,q)**2/(4*w) for w in weights))
assert s.simplify(radial_g - 1/(4*q*(1-q))) == 0

time, omega, velocity0 = s.symbols('time omega velocity0', positive=True)
position = velocity0*s.sin(omega*time)/omega
velocity = s.diff(position,time)
assert s.simplify(s.diff(position,time,2)+omega**2*position) == 0
assert position.subs(time,0) == 0
assert velocity.subs(time,0) == velocity0

jordan = s.simplify(A.subs({w1:s.Rational(7,10), w2:s.Rational(3,10), t1:2,t2:1,t3:s.Rational(13,10)}))
nilpotent = jordan-s.Rational(13,5)*s.eye(2)
assert nilpotent != s.zeros(2) and nilpotent**2 == s.zeros(2)
results = {
    'physical_adjoint_residual':str(physical_adjoint_residual),
    'euclidean_commutator_example':str(euclidean_commutator),
    'radial_metric':str(radial_g),
    'finite_boundary_path_length':'arcsin(sqrt(q0)); 0 < q0 < 1',
    'oscillator_position':str(position),
    'oscillator_velocity':str(velocity),
    'jordan_matrix':str(jordan),
    'jordan_nilpotent_square':str(nilpotent**2),
    'scope':'Formula checks only; no black-hole simulation or empirical gravity validation.',
}
dest = Path('analysis/sun_blackholes/blackhole_independent_checks.json')
dest.write_text(json.dumps(results,indent=2))
print(json.dumps(results,indent=2))

