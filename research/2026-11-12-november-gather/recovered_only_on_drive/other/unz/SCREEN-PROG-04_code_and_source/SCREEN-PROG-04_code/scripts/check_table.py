# SCRIPT: check_table
import numpy as np
from screen04_model import *
for a,b in [(300,400),(250,450),(200,500)]:
    print(a,b,'%.2f'%fit_const(campaign(lambda f: a+(b-a)*f)))
S=lambda f: 200+300*(1-np.exp(-f/0.2)); print('sat0.2 %.2f'%fit_const(campaign(S)))
S=lambda f: 200+300*(1-np.exp(-f)); print('sat1.0 %.2f'%fit_const(campaign(S)))
L=lambda f: 200+300*f
print('fixed %.2f  up %.2f  point %.2f'%(fit_const(campaign(L),fixed=True), fit_const(campaign(L,SCAN[::-1]),SCAN[::-1]), fit_const(campaign(L,point=True))))
