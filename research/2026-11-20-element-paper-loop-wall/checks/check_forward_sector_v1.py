# SCRIPT: CHECK-FORWARD-SECTOR-01
# Carbon helium-core opening face with nitrogen helium-core opening face at axis angle theta:
# the loop closes only if the two perpendicular geodesics meet inside the forward sector.
import math, numpy as np
zC=392.09056/64.49352; zN=552.06741/97.8901
a,b=0.5*math.log(zC),0.5*math.log(zN)
# hyperboloid model: point at distance d along unit direction u: (cosh d, sinh d u); line normal n=(sinh d, cosh d u)
def closes(th):
    u1=np.array([1,0]); u2=np.array([math.cos(th),math.sin(th)])
    n1=np.r_[math.sinh(a),math.cosh(a)*u1]; n2=np.r_[math.sinh(b),math.cosh(b)*u2]
    # intersection X: <X,n1>=<X,n2>=0, <X,X>=-1, X0>0 ; Minkowski <x,y>=-x0y0+x.y
    J=np.diag([-1,1,1]); X=np.cross(J@n1,J@n2)  # direction orthogonal (Minkowski) to both
    q=X@J@X
    if q>=0: return False
    X=X/math.sqrt(-q); X=X if X[0]>0 else -X
    ang=math.atan2(X[2],X[1])
    return 0<ang<th
ths=np.linspace(0.01,179.9,179900)
res=[closes(math.radians(t)) for t in ths]
edges=[ths[i] for i in range(1,len(res)) if res[i]!=res[i-1]]
print('closes at 90?',closes(math.pi/2),'transitions (deg):',[round(e,3) for e in edges])
