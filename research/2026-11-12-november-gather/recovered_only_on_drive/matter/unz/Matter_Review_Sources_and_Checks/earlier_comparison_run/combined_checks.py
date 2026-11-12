"""Finite checks for the comparison; not a full archive rerun or Lean proof.
Predictions: opposite pure preparations saturate the offset bound; the exact
angular gas has impedance/onset 2/pi; moment l reaches stress at order l-2;
Henrici values reproduce the cards; nuclear rim formula is exact.
"""
import json, math
from pathlib import Path
import numpy as np
from scipy.linalg import expm, eigvals
from scipy.integrate import quad
out={}; sx=np.array([[0,1],[1,0]],complex);sy=np.array([[0,-1j],[1j,0]]);I=np.eye(2)
errs=[]; sat=[]
for t in np.linspace(-.6,.6,81):
 for sign in [-1,1]:
  P=(I+sign*sy)/2;U=expm(-1j*t*sx);P=U@P@U.conj().T
  nu=P[0,0].real;pred=(1+sign*np.sin(2*t))/2;errs.append(abs(nu-pred))
  dP=-1j*(sx@P-P@sx);g=np.vdot(dP,dP).real/2;S=1/(nu*(1-nu));dot=-dP[0,0].real*S
  sat.append(abs(dot**2/(4*g*S)-1))
assert max(errs)<1e-12 and max(sat)<1e-12
out['joint_offset_witness']={'samples':162,'max_occupation_error':max(errs),'max_saturation_error':max(sat),'at_t_pi_over_12':{'occupations':[.75,.25],'offsets':[-math.log(3),math.log(3)]},'current_is_not_matched':True}
# Independent angular integral versus the closed propagator, k=1.
err=max(abs(quad(lambda mu:s/(s*s+mu*mu),-1,1)[0]/2-math.atan(1/s)) for s in [.01,.1,.5,2])
assert err<1e-10
out['P1']={'angular_integral_error':err,'zero_frequency_impedance':2/math.pi,'reflection_vs_sound':(2/math.pi-1/math.sqrt(3))/(2/math.pi+1/math.sqrt(3))}
poles=[]
for kap in [.64,.7,.916,1,2]:
 p=1/math.tan(1/kap)-kap; residual=abs(kap*math.atan(1/(p+kap))-1);assert p>-kap and p<0 and residual<1e-12;poles.append([kap,p,residual])
out['P2']={'onset':2/math.pi,'poles':poles,'scope':'real isolated pole to right of branch cut; equality is boundary, not isolated pole'}
n=16;c=np.array([(l+1)/math.sqrt((2*l+1)*(2*l+3)) for l in range(n-1)]);M=np.diag(c,1)+np.diag(c,-1);L=-1j*M
ret=[]
for l in [3,4,5,8]:
 for q in range(l-2):assert abs(np.linalg.matrix_power(L,q)[2,l])<1e-15
 exact=np.prod(c[2:l])/math.factorial(l-2);calc=abs(np.linalg.matrix_power(L,l-2)[2,l])/math.factorial(l-2);assert abs(calc-exact)<1e-15
 ret.append([l,l-2,exact])
out['P3']={'first_stress_return':ret,'density_return_order':'l, not l-2'}
rows=[]
for n in [20,100,200,400]:
 c=np.array([(l+1)/math.sqrt((2*l+1)*(2*l+3)) for l in range(n-1)]);M=np.diag(c,1)+np.diag(c,-1);L=-1j*M-np.diag([0]+[1]*(n-1));adj=L.conj().T
 minus=np.linalg.norm(L@adj-adj@L,'fro')**2/8;plus=np.linalg.norm(L@L-adj@adj,'fro')**2/8
 dep=np.linalg.norm(L,'fro')**2-np.sum(abs(eigvals(L))**2)
 assert abs(minus-1/3)<1e-12
 rows.append({'N':n,'departure_squared':float(dep),'E_minus':float(minus),'E_plus':float(plus)})
out['P4']={'finite_checks':rows,'scope':'finite numerical evidence, not proof of infinite-dimensional convergence'}
out['nuclear_exact_rim']=[2*s/(a-s) for s,a in [(734.8,20577.6),(1966.1,19813.9),(91.8,7366.6)]]
# Explicit false controls against interpreting a changed observable as invariant.
C=np.array([[.5,.35],[.35,.5]]);out['fixed_threshold_dilation_counts']=[int((x[0,1]**2)>=.09) for x in [C,C/2]];assert out['fixed_threshold_dilation_counts']==[1,0]
C=np.array([[.3,.2],[.2,.3]]);out['norm_normalization_offset_counts']=[int(x[0,1]**2>=.1*np.linalg.norm(x,2)**2) for x in [C,C+.2*I]];assert out['norm_normalization_offset_counts']==[1,0]
out['status']='PASS';Path(__file__).with_name('combined_results.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
