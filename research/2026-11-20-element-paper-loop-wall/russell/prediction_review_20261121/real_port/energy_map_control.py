"""A wave-step control: choose the underlying clock before interpreting flux."""
from math import sqrt
from fractions import Fraction as F
z=F(35,6)
reflection=lambda x: ((x-1)/(x+1))**2
direct=reflection(z)
kinetic=reflection(sqrt(z))
print("linear ratio as wave impedance: R =",direct,"fraction",float(direct))
print("same number as kinetic-energy ratio, equal masses, propagating: R =",kinetic)
print("kinetic-energy ratio at half reflected power =", (3+2*sqrt(2))**2)
assert direct>F(1,2) and kinetic<.5
