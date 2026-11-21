"""Exact engineered control; requires Python 3 standard library only."""
from fractions import Fraction as Q

z = Q(35, 6)
g = (z - 1) / (z + 1)
sinh_sq = (z - 1)**2 / (4*z)
power = 2*g*g
trace = 2 - 4*sinh_sq**2
assert power == Q(1682,1681)
assert trace == Q(-354481,176400)
assert 2*g*g > 1
# Prove the location of the probe at every lower possible denominator.
# The narrowest rival listed in the companion report exceeds 5.835.
# The broader cap 5.84 here also admits no denominator below 6.
for den in range(1,6):
    for num in range(5*den, 6*den+1):
        q=Q(num,den)
        assert not (q*q-6*q+1>0 and 5<q<Q(584,100))
lo,hi=Q(5832,1000),Q(5835,1000)
assert lo < z < hi and lo*lo-6*lo+1>0
print(f'z={z}, reflection={g}, power={power}, trace={trace} ({float(trace):.12f})')
