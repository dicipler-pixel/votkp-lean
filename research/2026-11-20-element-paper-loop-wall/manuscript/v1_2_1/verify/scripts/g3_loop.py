# SCRIPT: G3-LOOP-LAMBERT-FRANCIUM-GOLDHG
import gzip,json,math
from mpmath import mp,mpf,sinh,log,sqrt,findroot
mp.dps=30
R=json.load(gzip.open('/home/claude/votkp-lean/data/element_thresholds_20261011.json.gz'),parse_float=mpf)['records']
rec={r['Z']:r for r in R}
def ie(Z,k): return rec[Z]['thresholds'][k]['IE_eV']
def zo(Z,N): q=Z-N-1; return ie(Z,q+1)/ie(Z,q)
sh=lambda z: sinh(log(z)/2)
zC=zo(6,2); zN=zo(7,2); zRb=zo(37,36); zSr=zo(38,36)
print('C',zC,'N',zN,'Rb',zRb,'Sr',zSr)
print('both faces: C',sh(zC)**2,'N',sh(zN)**2)
print('C|N', sh(zC)*sh(zN)-1)
bsw=lambda zh:findroot(lambda z: sh(zh)*sh(z)-1, 5.5)
print('C swept root',bsw(zC),'Rb swept root',findroot(lambda z: sh(zRb)*sh(z)-1,5.2))
print('Rb|Sr', sh(zRb)*sh(zSr)-1)
# tangent partner
a=mpf(9); print('b*(9)',((sqrt(a)+1)/(sqrt(a)-1))**2, sh(9)*sh(4))
for a in (mpf(7),mpf(12)):
    b=((sqrt(a)+1)/(sqrt(a)-1))**2; print('b*',a,sh(a)*sh(b))
# gamma identity sinh h = G/sqrt(1-G^2)
z=mpf(6.3);G=(z-1)/(z+1);print(sh(z),G/sqrt(1-G*G))
W=3+2*sqrt(2)
print('wall equal faces sinh^2',sh(W)**2)
# Francium
IE1=ie(87,0); print('IE1 Fr',IE1)
print('wall*IE1',W*IE1)
lo=mpf('5.8079020598');hi=mpf('5.8665387761');print('window*IE1',lo*IE1,hi*IE1)
rival=(mpf('7.576234')/mpf('1.30447')+mpf('8.15168')/mpf('1.3895212'))/2
print('rival',rival,rival*IE1)
# extrapolation
zl=lambda Z: zo(Z,{3:2,11:10,19:18,37:36,55:54}[Z])
for Z,(p,l) in {19:(3,11),37:(11,19),55:(19,37)}.items():
    zn=2*zl(l)-zl(p); print('alkali extrap predicts',Z,zn,'actual',zl(Z),'outside actual?',zl(Z)>W,'pred inside?',zn<=W)
zf=2*zl(55)-zl(37); print('Fr extrap',zf,zf*IE1)
# gold mercury
ZZ=lambda Z: ie(Z,Z-2)/ie(Z,Z-3)  # helium core opening: last removal above core q=Z-3 -> q+1
for Z in (79,80): print(Z,'Heopen',zo(Z,2))
def box(Z):
    q=Z-3;a,b=rec[Z]['thresholds'][q],rec[Z]['thresholds'][q+1]
    return (b['IE_eV']-b['unc_eV'])/(a['IE_eV']+a['unc_eV']),(b['IE_eV']+b['unc_eV'])/(a['IE_eV']-a['unc_eV']),a['grade'],b['grade']
for Z in (79,80): print(Z,box(Z))
bx=[box(Z) for Z in range(3,86)]
print('strict descent of boxes (lo_i > hi_{i+1})',all(bx[i][0]>bx[i+1][1] for i in range(len(bx)-1)),len(bx)-1)
print('first below 4:',[ (Z,zo(Z,2)) for Z in range(70,86) if zo(Z,2)<4][:1])
