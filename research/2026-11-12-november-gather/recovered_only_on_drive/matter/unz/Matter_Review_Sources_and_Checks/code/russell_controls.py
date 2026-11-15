import math, cmath, json
# Declared audit predictions, independent of HTML graphics:
# harmonic generator trace form remains negative, center is NOT equal stores;
# imaginary artanh is finite at gamma=1; equatorial/polar analogy requires map.
out={}
# m=k=1: T=[[0,1],[-1,0]]; Herm=0, ||Skew||_F^2=2.
out['oscillator']={'q_generator':-1,'center_x0_p1':{'kinetic':.5,'potential':0,'kinetic_minus_potential':.5},'equal_stores_x_and_p':1/math.sqrt(2)}
out['continuation']=[{'gamma':g,'two_atanh_i_gamma':[ (2*cmath.atanh(1j*g)).real,(2*cmath.atanh(1j*g)).imag],'two_atan_gamma':2*math.atan(g),'K':1+g*g} for g in [.5,1,2]]
assert abs(out['continuation'][1]['two_atanh_i_gamma'][1]-math.pi/2)<1e-14
out['schwarzschild_circular_r5']={'E2':(1-2/5)**2/(1-3/5),'L2_over_M2':5**2/(5-3),'radial_epicyclic_ratio_squared':1-6/5,'exact_circular_exists':True,'stable':False}
out['P1_vs_thermal_origin']={'P1_reflection':(2/math.pi-1/math.sqrt(3))/(2/math.pi+1/math.sqrt(3)),'tanh_thermal_at_zero':0}
print(json.dumps(out,indent=2))
