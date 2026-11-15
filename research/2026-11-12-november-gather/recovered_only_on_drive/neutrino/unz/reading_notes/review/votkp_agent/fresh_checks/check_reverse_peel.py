"""VOTKP-RP-01. Assumptions precede each test. Synthetic unless explicitly CSV.
Run: python check_reverse_peel.py [path-to-packaged-NIST-CSV]
Requires numpy, scipy. No external data downloaded. No Lean certification.
"""
import sys,json,csv,math,hashlib
from pathlib import Path
import numpy as np
from scipy.linalg import expm
from scipy.integrate import solve_ivp
R={};checks=[]
def check(name,error,tol=1e-8):
 ok=bool(error<tol);checks.append(dict(name=name,error=float(error),tolerance=tol,passed=ok));assert ok,(name,error)
def gamma(z):return (z-1)/(z+1)
def add(u,v):return (u+v)/(1+u*v)
# A1: positive energies and directed ratios; signed increments may reverse.
rng=np.random.default_rng(20261011);mx=0.;cmx=0.
for j in range(1000):
 e=np.exp(rng.uniform(-4,4,12));r=np.log(e[1:]/e[:-1])/2;v=np.tanh(r);c=0.
 for x in v:c=add(c,x)
 mx=max(mx,abs(c-gamma(e[-1]/e[0])));cmx=max(cmx,abs(np.tanh(r.sum())-c))
check('signed telescoping, 1000 synthetic records',mx);check('composition equals summed rapidity',cmx)
r=np.array([.4,-.4]);R['cancellation']={'net_gamma':float(np.tanh(r.sum())),'endpoint_distance':float(2*abs(r.sum())),'traversed_hyperbolic_length':float(2*abs(r).sum())}
check('forward/reverse identity',abs(add(np.tanh(.4),-np.tanh(.4))))
# A2: packaged NIST central values; preserve stage adjacency, Z<=110.
if len(sys.argv)>1:
 p=Path(sys.argv[1]);rows=list(csv.DictReader(p.open()));E={};grades={};
 for row in rows:
  z=int(row['Z']);q=int(row['ion_charge'])
  if z<=110:E.setdefault(z,{})[q]=float(row['ionization_energy_eV']);grades[z,q]='S' if row['semi_empirical']=='1' else ('T' if row['theoretical']=='1' else 'M')
 n=0;noninc=[];err=0.;windows=0;counts={}
 for z,d in E.items():
  for q in sorted(d):
   if q+1 not in d:continue
   n+=1;counts[grades[z,q]+grades[z,q+1]]=counts.get(grades[z,q]+grades[z,q+1],0)+1
   if d[q+1]<=d[q]:noninc.append([z,q])
   check(f'reversal Z={z} q={q}',abs(gamma(d[q+1]/d[q])+gamma(d[q]/d[q+1])),1e-12)
  for a in sorted(d):
   for b in range(a+1,min(a+11,max(d))+1):
    if not all(q in d for q in range(a,b+1)):continue
    v=0.
    for q in range(a,b):v=add(v,gamma(d[q+1]/d[q]))
    err=max(err,abs(v-gamma(d[b]/d[a])));windows+=1
 R['packaged_csv']={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'stages':sum(map(len,E.values())),'adjacent_pairs':n,'nonincreasing_pairs':noninc,'windows_at_most_10_steps':windows,'max_endpoint_error':err,'pair_grades':counts}
 check('all packaged windows telescope',err,1e-11)
# A3: lift q(rho) into fixed finite-dimensional Hilbert space; no physical atom claim.
# H=U diag(0,e^(2rho), e^(2rho)+e^(4rho)) U*, U rotates first 2 modes by a*rho.
rho=np.linspace(.6,.2,1001);a=.7;h=1e-6
J=np.array([[0.,-1.,0.],[1.,0.,0.],[0.,0.,0.]])
def H(r,b):
 u=expm(b*r*J);return u@np.diag([0.,np.exp(2*r),np.exp(2*r)+np.exp(4*r)])@u.T
def P(r,b):
 _,u=np.linalg.eigh(H(r,b));return u[:,:1]@u[:,:1].T
errs=[]
for r in rho[::50]:
 dp=(P(r+h,a)-P(r-h,a))/(2*h);errs.append(abs(.5*np.trace(dp@dp)-a*a))
check('explicit lifted metric g_rhorho=a^2',max(errs),1e-8)
R['lifts']={'same_reverse_gamma_start':math.tanh(.6),'same_reverse_gamma_end':math.tanh(.2),'constant_projector_length':0.,'rotating_projector_length':a*.4,'arbitrary_rotation_multiplier_allowed':True,'max_metric_error':max(errs)}
# A4: nondegenerate ground projector, T=1 reference action; tau=.5, precession=1, hbar=1.
# U=exp(s A), A has two unequal ground-to-excited amplitudes, .3 and .4.
A=np.array([[0.,-.3,-.4],[.3,0.,0.],[.4,0.,0.]])
def action(gaps):
 weights=2*.5*np.array(gaps)/(1+.25*np.array(gaps)**2);gn=np.array([.09,.16]);return float(weights@gn),weights
for label,gaps in [('equal_weight_multigap',[1.,4.]),('unequal_weight_multigap',[1.,3.])]:
 act,w=action(gaps);L=.5;bound=min(w)*L*L;R[label]={'gaps':gaps,'weights':w.tolist(),'L':L,'leading_action_T1':act,'bound_T1':bound,'slack':act-bound}
 if label.startswith('equal'):check('different gaps can saturate',abs(act-bound),1e-12)
 else:check('unequal active weights strict bound',1e-4/(act-bound),1.)
# A5: rank 2 occupied sector is mathematical only; bath T=0 occupies just level 0.
# E=(0,.5,3,6), drive rotates levels 1 and 2 only, so g=.09 but p1=p2=0.
D4=np.diag([0.,.5,3.,6.]);B=np.zeros((4,4));B[2,1]=.3;B[1,2]=-.3
P2=np.diag([1.,1.,0.,0.]);dP2=B@P2-P2@B;dH4=B@D4-D4@B
g2=float(.5*np.trace(dP2@dP2));p4=np.array([1.,0.,0.,0.]);z2=0.
for m in [0,1]:
 for n in [2,3]:
  gap=D4[n,n]-D4[m,m];gn=abs(dH4[m,n])**2/gap**2
  z2+=2*.5/(1+.25*gap*gap)*(p4[m]-p4[n])*gap*gn
R['rank2_counterexample']={'spectrum':np.diag(D4).tolist(),'g':g2,'zero_temperature_rotation_friction':float(z2)}
check('rank-two moving projector has zero T0 friction',abs(z2)+abs(g2-.09),1e-12)
# A6: test actual bath ODE against leading approximation, Gibbs initial state beta=5.
# Constant spectrum (0,1,4), no populations inferred from transmon shots.
D=np.diag([0.,1.,4.]);beta=5.;tau=.5;om=np.diag(np.exp(-beta*np.diag(D)));om/=np.trace(om)
w=2*tau*np.array([1.,4.])/(1+tau*tau*np.array([1.,4.])**2);pop=np.diag(om);pred=float(np.dot(w*(pop[0]-pop[1:]),[.09,.16]));runs=[]
for T in [20.,80.,320.]:
 def rhs(t,y):
  u=expm((t/T)*A);hs=u@D@u.T;dh=u@(A@D-D@A)@u.T/T;o=u@om@u.T;rr=y[:9].reshape(3,3)
  dr=-1j*(hs@rr-rr@hs)+(o-rr)/tau;return np.r_[dr.ravel(),np.trace(rr@dh)]
 y0=np.r_[om.astype(complex).ravel(),0j];sol=solve_ivp(rhs,(0,T),y0,rtol=2e-9,atol=1e-11)
 W=float(sol.y[-1,-1].real);runs.append({'T':T,'exact_ODE_Wex':W,'leading_Wex':pred/T,'relative_error':abs(W-pred/T)/(pred/T)})
check('bath leading approximation approached at T=320',runs[-1]['relative_error'],.003)
check('error decreases with duration',max(runs[i+1]['relative_error']/runs[i]['relative_error'] for i in range(2)),1.)
R['bath_ODE']={'beta':beta,'tau':tau,'precession':1,'initial_state':'instantaneous Gibbs','delta_F':0.,'runs':runs}
# A7: original IQGT polar family k=3, y0=.6, incidence40 degrees. Independent geodesic ODE.
k=3.;y0=.6;theta=math.radians(40);gp=lambda y:k*k*np.sin(y)**2/4;dg=lambda y:k*k*np.sin(2*y)/4
C=gp(y0)*np.sin(theta)**2;pred_y=np.arcsin(np.sin(y0)*np.sin(theta))
def geo(t,s):
 x,y,vx,vy=s;return [vx,vy,-dg(y)/gp(y)*vx*vy,dg(y)/.5*vx*vx]
def turn(t,s):return s[3]
turn.direction=1;turn.terminal=True
sol=solve_ivp(geo,(0,2),[0.,y0,np.sin(theta)/np.sqrt(gp(y0)),-2*np.cos(theta)],events=turn,rtol=1e-11,atol=1e-13)
yturn=float(sol.y_events[0][0][1]);check('polar turning point analytic versus ODE',abs(yturn-pred_y),1e-9)
R['polar_refraction']={'k':k,'y0':y0,'incidence_degrees':40,'C_squared_convention':float(C),'p_x_unsquared':float(np.sqrt(C)),'predicted_yturn':float(pred_y),'integrated_yturn':yturn,'spectral_gap':2.}
R['checks']={'total':len(checks),'passed':sum(x['passed'] for x in checks),'max_algebra_error':mx};R['assumptions']='Assumptions A1-A7 are specified before test blocks in source. All operator tests synthetic.'
Path(__file__).with_name('reverse_peel_results.json').write_text(json.dumps(R,indent=2)+'\n');print(json.dumps(R,indent=2))
