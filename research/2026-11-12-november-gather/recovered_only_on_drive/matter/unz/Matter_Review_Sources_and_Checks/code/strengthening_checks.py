from pathlib import Path
import numpy as np, json
from scipy.linalg import expm
from fractions import Fraction as F
out={};n=14;I=np.eye(n);c=np.array([(l+1)/np.sqrt((2*l+1)*(2*l+3)) for l in range(n-1)]);H=np.diag(c,1)+np.diag(c,-1);D=np.diag([0]+[1]*(n-1));rows=[]
for kap in [0,.3,1.]:
 L=-1j*H-kap*D
 for sign in [-1,1]:
  p0=np.zeros(n,complex);p0[0]=1;p0[4]=sign*.2;p0/=np.linalg.norm(p0)
  for t in [.05,.2,.7,1.5,2.5]:
   a=expm(t*L)@p0;psi=a/np.linalg.norm(a);P=np.outer(psi,psi.conj());Pd=L@P+P@L.conj().T-np.trace((L+L.conj().T)@P).real*P
   nu=P[0,0].real;S=1/(nu*(1-nu));dot=-Pd[0,0].real*S;g=np.linalg.norm(Pd,'fro')**2/2;eh=np.linalg.norm(P@H@(I-P),'fro')**2;r=dot**2/(4*g*S)
   assert r<=1+1e-10 and np.linalg.norm(P@P-P)<1e-12
   if kap==0:assert abs(g-eh)<1e-12
   rows.append({'kappa':kap,'sign':sign,'t':t,'ratio':r,'g':g,'hamiltonian_coupling':eh})
out['G1']={'samples':len(rows),'max_ratio':max(r['ratio'] for r in rows),'min_ratio':min(r['ratio'] for r in rows),'max_damped_g_minus_EH':max(abs(r['g']-r['hamiltonian_coupling']) for r in rows if r['kappa']>0),'rows':rows,'scope':'normalized angular state projector only; no identification with original gas ledger'}
rs=[]
for gam in [.2,.7,1.,1.5]:
 tau=2*np.arctanh(1j*gam);theta=2*np.arctan(gam);G=np.tanh(tau/2);assert abs(tau-1j*theta)<1e-12 and abs(G-1j*gam)<1e-12
 assert abs((1+gam*gam)-1/np.cos(theta/2)**2)<1e-12
 rs.append({'gamma':gam,'tau_im':tau.imag,'Gamma_im':G.imag,'K':1+gam*gam})
out['G2']=rs
P=np.diag([1.,0.]);V=np.array([[0,1],[1,0]],complex);W=np.array([[0,-1j],[1j,0]]);Q=np.trace(P@V@W);Qc=np.trace((np.eye(2)-P)@(-V)@(-W));assert abs(Qc-Q.conjugate())<1e-15
A=np.array([[1.,2.],[0.,3.]]);z=5.;R=np.linalg.inv(z*np.eye(2)-A);Ra=np.linalg.inv(z*np.eye(2)-A.T);assert np.allclose(Ra,R.T) and not np.allclose(Ra,-R)
out['parity']={'Q':[Q.real,Q.imag],'Q_complement':[Qc.real,Qc.imag],'resolvent_global_odd_false':True}
exact_checks=0
for rr in [F(1,3),F(2,3),F(3,4)]:
 C=(1-rr*rr)/(1+rr*rr);S=2*rr/(1+rr*rr)
 for u in [F(1,5),F(1,2),F(3,2)]:
  for v in [F(1,4),F(3,4)]:
   w=F(1);e2=v*v+w*w+2*v*w*C-u*u
   if e2==0:continue
   qkk=(e2*w*w-v*v*w*w*S*S)/(4*e2*e2)
   qvv=(e2-(v+w*C)**2)/(4*e2*e2)
   qkv=(-e2*w*S+v*w*S*(v+w*C))/(4*e2*e2)
   assert qkk*qvv-qkv*qkv == -u*u*w*w*C*C/(16*e2**3)
   exact_checks+=1
out['SSH_exact_rational_determinant']={'checks':exact_checks,'formula':'-u^2*w^2*cos(k)^2/(16*(E^2)^3)','general_proof':'bilinear Gram determinant equals squared scalar triple product; d dot (dk cross dv) = -i*u*w*cos(k)','assumptions':'real u,v,w,k; E² nonzero; bilinear biorthogonal metric'}
out['status']='PASS';Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:({a:b for a,b in val.items() if a!='rows'} if isinstance(val,dict) else val) for k,val in out.items()},indent=2))
