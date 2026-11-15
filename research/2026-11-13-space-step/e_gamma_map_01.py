# SCRIPT: E-GAMMA-MAP-01
# Why this decides it: E = 1 - (r_cov/r_room)^3 is one minus a ratio of two volumes, so z_E = V_room/V_own = 1/(1-E) is a step
# ratio and its peel coordinate is G_E = (z_E-1)/(z_E+1) = E/(2-E). The check is pure algebra plus his own tabulated E values.
# What would falsify the reading "E = 2/3 is the step z = 3": the algebra (it cannot), so the only content is where the
# measured elements and switch points fall. Nothing is fitted. Lines written before looking at the numbers:
#  L1  every metal of per_element.csv has G_E < 1/2 and every non-metal G_E >= 1/2 except those the 6 Nov ledger already names (B).
#  L2  each measured switch of C_edges.csv with both sides tabulated straddles G_E = 1/2 (Si melt, Ge melt, Sn grey/white, Hg, I).
#  L3  (single number) Hg critical density against the wall G_E^2 = 1/2, i.e. E = 2(sqrt2-1): predicted rho = rho_full*(3-2sqrt2).
import csv, math
def GE(E): return E/(2-E)
def zE(E): return 1/(1-E)
def K(G):
    x=2*G*G
    return 1/(1-x) if x<1 else x/(x-1)
def turn(z):
    q=(z-1)**2/(4*z); c=1-2*q*q
    return math.degrees(2*math.acos(c)) if abs(c)<=1 else float('nan')
print('special steps:  E=2/3 -> z=%.4f G=%.4f K=%.3f ; wall G^2=1/2 -> E=%.5f ; z*=6.26913 -> E=%.5f'%(zE(2/3),GE(2/3),K(GE(2/3)),1-1/(3+2*math.sqrt(2)),1-1/6.26913))
for ang,z in [(60,2.6592271),(72,2.8900536),(90,3.2201934),(120,2+math.sqrt(3)),(180,4.6115818)]:
    print('  loop turn %3d deg at z=%.5f  <->  E=%.5f'%(ang,z,1-1/z))
rows=list(csv.DictReader(open('/home/claude/in_20261113/per_element.csv')))
print('\nel   E      z_E    G_E    G_E^2  K      turn   lattice / nonmetal')
bad=[]
for r in sorted(rows,key=lambda r: float(r['E'])):
    E=float(r['E']); G=GE(E); z=zE(E); nm=r['nonmetal']=='True'
    if (G<0.5)==nm: bad.append(r['el'])
    print('%-3s %.4f %6.3f %.4f %.4f %6.3f %6.1f  %s %s'%(r['el'],E,z,G,G*G,K(G),turn(z),r['lat'][:14],'NONMETAL' if nm else ''))
print('L1 wrong side of G_E=1/2:',bad, ' n=',len(rows))
print('\nSwitch points (E from C_edges.csv computed rows):')
for r in csv.DictReader(open('/home/claude/in_20261113/C_edges.csv')):
    if r['quantity'].startswith('E (computed)'):
        E=float(r['value']); G=GE(E)
        print('%-22s %-3s E=%.3f z=%6.3f G_E=%.3f G^2=%.3f  %s'%(r['case'][:22],r['element'],E,zE(E),G,G*G,r['conditions'][:58]))
w=3-2*math.sqrt(2)
for el,full,meas in [('Hg',33.800,5.8),('Cs',4.219,0.38),('Rb',3.659,0.29),('K',2.058,0.18)]:
    print('L3 %s: wall predicts rho_c = %.3f ; measured %.2f ; z at measured = %.2f'%(el,full*w,meas,full/meas))
