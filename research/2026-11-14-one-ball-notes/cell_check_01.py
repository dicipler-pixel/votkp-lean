# SCRIPT: ONE-BALL-CELL-CHECK-01
# Object: his placement (Two Trees Def 4.1): six boosts of rapidity ln z along +-i, +-j, +-k acting on o = (1,0,0,0).
# Claims checked, each with why it decides and its kill line (written before the run):
#  C1 The planes halfway to the neighbours (at ln z / 2 along each arm, perpendicular to it), for two perpendicular arms,
#     cross at angle alpha with cos alpha = q, or are apart by delta with cosh delta = q, q = sinh^2(ln z / 2) = (z-1)^2/(4z).
#     Decides: paper Thm 8.4 gives cosh delta = 9/7 at z = 7 by the same planes; the unit normals are n_u = (sinh h, cosh h u).
#     Kill: |<n_i, n_j>| differs from q by more than 1e-12 at any z.
#  C2 The square i j i^-1 j^-1 turns by phi = 4 arccos q inside the wall and runs by tau = 4 arccosh q past it.
#     Decides: paper Thm 5.4 gives cos phi = -527/625 at z = 5; Thm 8.4 gives cosh tau = 23137/2401 at z = 7.
#     Kill: either paper number missed by more than 1e-9, or the 4x law off by more than 1e-9 at any z tested.
#  C3 At q = cos(2 pi / n) the square has order n exactly (c^n = identity).  Kill: |c^n - I| > 1e-8.
#  C4 At q = cos(2 pi / n) the whole six-arm tree closes: distinct points of the orbit of o keep a smallest mutual
#     distance equal to ln z as the depth grows (a lattice), while at z = 3 and z = 5 it keeps falling (paper: 0.4258 at depth 5 for z = 5).
#     Decides: a lattice has a positive smallest distance; a non-discrete group does not.
#     Kill: smallest distance at depth 6 below ln z - 1e-6 for a claimed closing step, or NOT falling for the controls.
import numpy as np, math, itertools
def boost(u,r):
    c,s=math.cosh(r),math.sinh(r); B=np.eye(4); u=np.array(u,float)
    B[0,0]=c; B[0,1:]=s*u; B[1:,0]=s*u; B[1:,1:]=np.eye(3)+(c-1)*np.outer(u,u); return B
AX=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
eta=np.diag([1.,-1,-1,-1])
def q_of(z): return (z-1)**2/(4*z)
def z_of(q): return (math.sqrt(q)+math.sqrt(1+q))**2
print('C1/C2')
for z in (2,3,5,z_of(math.cos(2*math.pi/5)),2+math.sqrt(3),4.6115817893,3+2*math.sqrt(2),7,11):
    r=math.log(z); h=r/2; q=q_of(z)
    n1=np.array([math.sinh(h),math.cosh(h),0,0]); n2=np.array([math.sinh(h),0,math.cosh(h),0])
    ip=abs(n1@eta@n2)
    C=boost(AX[0],r)@boost(AX[2],r)@boost(AX[1],r)@boost(AX[3],r); tr=np.trace(C)
    if q<1-1e-12:
        phi=math.degrees(math.acos(max(-1.0,min(1.0,(tr-2)/2)))); law=4*math.degrees(math.acos(q)); law=law if law<=180 else 360-law
        print(f'z={z:.7f} q={q:.9f} |<n,n>|-q={ip-q:+.1e} alpha={math.degrees(math.acos(q)):.4f} phi={phi:.6f} 4alpha(mod)={law:.6f}')
    else:
        # translation length from the SO(3,1) trace of a pure boost product in a plane: tr = 2 + 2 cosh tau
        tau=math.acosh(max(1,(tr-2)/2)); print(f'z={z:.7f} q={q:.9f} |<n,n>|-q={ip-q:+.1e} delta={math.acosh(max(1,q)):.9f} tau={tau:.9f} 4delta={4*math.acosh(max(1,q)):.9f}')
C5=boost(AX[0],math.log(5))@boost(AX[2],math.log(5))@boost(AX[1],math.log(5))@boost(AX[3],math.log(5))
print('paper z=5: cos phi', (np.trace(C5)-2)/2, 'vs -527/625 =', -527/625)
C7=boost(AX[0],math.log(7))@boost(AX[2],math.log(7))@boost(AX[1],math.log(7))@boost(AX[3],math.log(7))
print('paper z=7: cosh tau', (np.trace(C7)-2)/2, 'vs 23137/2401 =', 23137/2401, ' cosh 4delta =', math.cosh(4*math.acosh(9/7)))
print('C3')
for n in (5,6,7,8,10,12):
    z=z_of(math.cos(2*math.pi/n)); r=math.log(z)
    C=boost(AX[0],r)@boost(AX[2],r)@boost(AX[1],r)@boost(AX[3],r)
    print(n, f'z={z:.10f} Gamma^2={((z-1)/(z+1))**2:.8f} |c^n-I|={np.abs(np.linalg.matrix_power(C,n)-np.eye(4)).max():.1e}')
print('C4  depth: distinct points, smallest mutual distance (ln z in brackets)')
def orbit(z,depth):
    r=math.log(z); G=[boost(u,r) for u in AX]; o=np.array([1.,0,0,0])
    front=[(np.eye(4),-1)]; pts={(0,0,0):o}; out=[]
    for d in range(1,depth+1):
        nx=[]
        for M,last in front:
            for g in range(6):
                if last>=0 and g==(last^1): continue
                M2=M@G[g]; p=M2@o; b=p[1:]/(1+p[0]); k=tuple(np.round(b,7))
                if k not in pts: pts[k]=p; nx.append((M2,g))
        front=nx
        P=np.array(list(pts.values())); m=9.0
        if len(P)<6000:
            IP=P@eta@P.T; np.fill_diagonal(IP,9e9); m=math.acosh(max(1.0,IP.min()))
        out.append((d,len(P),round(m,5),len(front)))
    return out
for name,z,dep in (('n=5',z_of(math.cos(2*math.pi/5)),6),('n=6',2+math.sqrt(3),6),('n=8',4.6115817893,5),('control z=3',3,5),('control z=5',5,5)):
    print(name, f'z={z:.6f} [ln z={math.log(z):.5f}]', orbit(z,dep))
