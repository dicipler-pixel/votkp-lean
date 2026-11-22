"""Check the conditional two-spinor radial inner product and size budgets for Sc/Sn."""
from math import exp,gamma,log,pi,sqrt
from scipy.integrate import quad
a0=1/137.035999177
def orbital(z,alpha):
    # One common radial coordinate in Bohr lengths; point nucleus at the origin.
    g=sqrt(1-(z*alpha)**2)
    b=z*alpha/(1+g)
    norm=(2*z)**(g+.5)/sqrt(gamma(2*g+1)*(1+b*b))
    return g,b,norm
def analytic(za,zb,alpha):
    g,b,n=orbital(za,alpha); h,c,m=orbital(zb,alpha)
    return n*m*(1+b*c)*gamma(1+g+h)/(za+zb)**(1+g+h)
def integrate(za,zb,alpha):
    # Evaluate each of the large and small component contributions separately.
    def rad(z,r,small):
        g,c,n=orbital(z,alpha)
        return n*r**g*exp(-z*r)*(-c if small else 1)
    return [quad(lambda r:rad(za,r,s)*rad(zb,r,s),0,1,epsrel=1e-12,epsabs=1e-13)[0]
            +quad(lambda r:rad(za,r,s)*rad(zb,r,s),1,float('inf'),epsrel=1e-12,epsabs=1e-13)[0] for s in [False,True]]
maxerr=0
for za,zb in ((1,1),(1,2),(21,50),(50,21),(50,50),(50,92),(92,92),(21,110)):
    for alpha in (a0,1e-7,0.0):
        s=analytic(za,zb,alpha)
        direct=sum(integrate(za,zb,alpha))
        maxerr=max(maxerr,abs(s-direct))
        assert abs(s-direct)<1e-10
        if za==zb:assert abs(s-1)<1e-12
        if not alpha:assert abs(s*s-(4*za*zb/(za+zb)**2)**3)<1e-12
print('Quadrature comparisons',24,'max absolute overlap error',maxerr)
parts=integrate(21,50,a0)
print('Sc/Sn large overlap',parts[0],'small overlap',parts[1],'total fidelity',sum(parts)**2)
nr=(4*21*50/71**2)**3
print('nonrel charge-scale fidelity',nr)
base=6033.75643;sn=35192.501
w=3+2*sqrt(2); c=(7.576234/1.30447+8.15168/1.3895212)/2
print('Allowed numerator at archive denominator',w*base,c*base,'margins eV',sn-w*base,c*base-sn)
print('Allowed denominator fixed B(Sn)',sn/c,sn/w)
ratio=sn/base;hyp_apex=(sqrt(ratio)-1)/(sqrt(ratio)+1)
print('nonrel formula forced onto archive energies', (1-hyp_apex**2)**3)
# Source components. Table III units are Rydbergs; Table II FNS separated below.
ry=13.60569312299; mc=510998.95
values=[(21,443.6199488,.0053827,.1416477,.028512),
        (50,2589.25230,.01144,2.63976,.09296)]
results=[]
for z,p,mass,lamb,fns in values:
    size_mev=fns*(a0/pi)*(z*a0)**4*mc
    B=p*ry
    results.append((B,B-mass*ry,B-mass*ry-size_mev,B-(mass+lamb)*ry))
    print('Z',z,'point binding eV',B,'mass correction to signed level eV',mass*ry,'total Lamb eV',lamb*ry,'FNS within Lamb eV',size_mev)
print('point, +mass, +mass+FNS, +mass+entire Lamb ratios:',*[results[1][i]/results[0][i] for i in range(4)])
