# SCRIPT: LOOP2-CHECK2B-SECOND-SETUP-AND-GAP-BOUND
# WHY THIS DECIDES IT: check2 passed kill (i) (N never above cap, 0 of 72x2 cases) but kill (ii) "N(2000) within 1 of
# cap" failed in some cases (8 own, 11 lab). The mechanism to test: at finite n the points have a largest gap g_n (three-distance
# theorem), and a covering argument gives a rigorous lower bound  N(n) >= floor((2 pi - g_n)/(delta_min + g_n))  where
# delta_min = 2 arcsin(sqrt(eps/2)/rho): place ideal slots at spacing delta_min+g_n, take the first orbit point at or after each slot.
# So the right finite-n law is   floor((2pi-g_n)/(delta_min+g_n)) <= N(n) <= cap.   Second setup: other start azimuth (1.234 rad),
# indexing k=0..n-1, and n=2000 AND n=20000.
# KILL LINE (before the run): (a) N outside [lower bound, cap] in any case/n -> the gap law is killed;
#   (b) at n=20000 N < cap-1 for any own-frame case -> "reaches the cap" killed even with 10x the passes.
import numpy as np, json
exec(open('check2_capacity.py').read().split('# ---- instrument validation')[0])
exec('def orbit(a,phi,psi0=0.0,k0=1,n=2000):'+open('check2_capacity.py').read().split('def orbit(a,phi,psi0=0.0,k0=1,n=2000):')[1].split('NG=sorted')[0])
def fit_circle(P):
    A=np.hstack([P,-np.ones((len(P),1))]); u,s,vh=np.linalg.svd(A,full_matrices=False); x=vh[-1]; nrm=np.linalg.norm(x[:3]); n=x[:3]/nrm; h=x[3]/nrm
    if h<0: n,h=-n,-h
    res=np.max(abs(P@n-h)); rho=np.sqrt(max(1-h*h,0)); c=h*n
    e1=P[0]-c; e1-=np.dot(e1,n)*n; e1/=np.linalg.norm(e1); e2=np.cross(n,e1)
    t=np.arctan2((P-c)@e2,(P-c)@e1); return n,h,rho,t,res
def gmax(t):
    s=np.sort(np.mod(t,TWO)); g=np.diff(np.concatenate([s,[s[0]+TWO]])); return g.max()
def lowb(t,rho,eps):
    s=np.sqrt(eps/2)/rho
    if s>1: return 1
    dm=2*np.arcsin(min(s,1.0)); g=gmax(t); return max(1,int(np.floor((2*np.pi-g)/(dm+g)+1e-12)))
rows=[]; bad_a=0; bad_b=0; bad_over=0
for setup,(psi0,k0) in {'S1(az0,k=1..n)':(0.0,1),'S2(az1.234,k=0..n-1)':(1.234,0)}.items():
  for z in [2,3,4,5,5.5,5.8]:
    a=anatomy(float(z)); G2=a['G']**2
    for label,s2 in [('1',1.0),('2G^2',2*G2),('0.301',0.301)]:
        phi=np.arcsin(np.sqrt(min(s2,1.0)))
        own,lab,ax,e1,e2=orbit(a,phi,psi0,k0,20000)
        t_own=np.arctan2(own@e2,own@e1); n_l,h_l,rho_l,t_lab,_=fit_circle(lab)
        for eps in [0.5,0.1,0.02,0.005]:
            for frame,t,rho in (('own',t_own,np.sin(phi)),('lab',t_lab,rho_l)):
                cap=cap_formula(rho,eps)
                for n in (2000,20000):
                    N=maxset(t[:n],rho,eps); lb=lowb(t[:n],rho,eps)
                    bad_a+= (N<lb) or (N>cap); bad_over+=(N>cap)
                    if n==20000 and frame=='own': bad_b+=(N<cap-1)
                    rows.append(dict(setup=setup,z=z,label=label,eps=eps,frame=frame,n=n,cap=cap,lower_bound=lb,N=N,gmax=float(gmax(t[:n]))))
print('N above cap:',bad_over,'  N outside [lower bound,cap]:',bad_a,'  own N(20000)<cap-1:',bad_b,' rows',len(rows))
for r in rows:
    if r['n']==20000 and r['N']<r['cap']-1: print('still short at 20000:',r)
sh=[r for r in rows if r['n']==2000 and r['N']<r['cap']-1]
print('short at 2000 (both setups):',len(sh),'; of which lower bound already explains (lb>=cap-1):',sum(r['lower_bound']>=r['cap']-1 for r in sh))
json.dump(rows,open('check2b_second_setup.out','w'))
