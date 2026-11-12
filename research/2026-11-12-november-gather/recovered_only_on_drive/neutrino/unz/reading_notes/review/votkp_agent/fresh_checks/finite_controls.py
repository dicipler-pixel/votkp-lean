"""Reproducible cross-paper controls and a non-destructive element atlas extension.
Run from the conversation workspace: python output/element_crosspaper_synthesis_20261011/verify_and_extend.py
These are finite mathematical controls, not fits or atomic Hamiltonian calculations.
"""
from pathlib import Path
import json, hashlib, math
from fractions import Fraction as F
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
checks=[]
def check(name, passed, **details):
    checks.append(dict(name=name, passed=bool(passed), **details))
    if not passed: raise AssertionError(name)
def error(a,b): return float(np.linalg.norm(a-b))

# Units in this finite control: hbar=1. Hidden energies and coupling vectors.
D=np.diag([1.,2.,4.])
B=np.array([[.3,.1j,.2],[.1,.25,.1j]],complex)
A=np.array([[1.5,.1],[.1,2.5]],complex)
H=np.block([[A,B],[B.conj().T,D]])
def sigma(z,B=B): return B@np.linalg.inv(z*np.eye(3)-D)@B.conj().T
def kernel(t,B=B): return (B*np.exp(-1j*np.diag(D)*t))@B.conj().T
def contour(center,f,n=1024):
    theta=2*np.pi*(np.arange(n)+.5)/n
    z=center+.22*np.exp(1j*theta)
    # dz/(2 pi i) = r exp(i theta) dtheta/(2 pi).
    return sum(f(zz)*sigma(zz)*(.22*np.exp(1j*tt))/n for zz,tt in zip(z,theta))
residues=[contour(e,lambda z:1) for e in np.diag(D)]
reserr=max(error(r,np.outer(B[:,j],B[:,j].conj())) for j,r in enumerate(residues))
check('Cauchy recovers each matrix channel weight',reserr<1e-12,max_abs_frobenius_error=reserr)
kt=kernel(.7)
ct=sum(contour(e,lambda z:np.exp(-1j*z*.7)) for e in np.diag(D))
check('Weighted contours recover the time kernel',error(ct,kt)<1e-12,error=error(ct,kt))
moment=sum(contour(e,lambda z:z) for e in np.diag(D))
check('Weighted contours recover the first energy moment',error(moment,B@D@B.conj().T)<1e-12,error=error(moment,B@D@B.conj().T))
z=1.1+.7j
full=np.linalg.inv(z*np.eye(5)-H)[:2,:2]
schur=np.linalg.inv(z*np.eye(2)-A-sigma(z))
check('Exact retained resolvent equals the Schur resolvent',error(full,schur)<1e-12,error=error(full,schur))
K0=kernel(0)
check('Coupling footprint is positive and equals commutator norm',np.linalg.eigvalsh(K0).min()>0 and abs(np.linalg.norm(H@np.diag([1,1,0,0,0])-np.diag([1,1,0,0,0])@H)**2-2*np.trace(K0).real)<1e-12)
B2=B[:,[1,0,2]]
check('Same hidden energies and same K(0), different memory',error(kernel(0,B2),K0)<1e-12 and error(kernel(.7,B2),kt)>.01,kernel_difference=error(kernel(.7,B2),kt))
evals,U=np.linalg.eigh(H); P=U[:,:2]@U[:,:2].conj().T
check('A spectral projector of the same Hermitian H has no cross block',np.linalg.norm(P@H@(np.eye(5)-P))<1e-12,cross_block_norm=float(np.linalg.norm(P@H@(np.eye(5)-P))))
check('Positive hidden energy produces a subtractive static correction',np.linalg.eigvalsh(B@np.linalg.inv(D)@B.conj().T).min()>0)

# Light 4.9f: exact conservative redistribution and its countercontrol.
g0=F(1); g1=F(1,8)
def R(gap,y): return 2/(gap*gap-y)
def DD(gap,y0=F(0),y1=F(1,4)): return 2/((gap*gap-y0)*(gap*gap-y1))
loss_g=g0-g1; loss_b=DD(F(1))-DD(F(2))
check('Conserved oscillator-weight upshift lowers metric and divided difference',loss_g==F(7,8) and loss_b==F(38,15),metric_loss=str(loss_g),divided_difference_loss=str(loss_b))
check('Redistribution loss obeys the no-upper-cutoff bound',float(loss_g)**4<=float(loss_b/2)**3)
gaps=list(map(F,[1,2,3,4])); dip0=list(map(F,[2,2,2,2])); dip1=[F(47,24),F(17,6),F(1,8),F(3)]
w0=[t*w for t,w in zip(gaps,dip0)]; w1=[t*w for t,w in zip(gaps,dip1)]
resp=lambda w,y:sum(ww*R(t,y) for ww,t in zip(w,gaps))
metric=lambda w:sum(ww/t**3 for ww,t in zip(w,gaps))
same=all(resp(w0,y)==resp(w1,y) for y in [F(0),F(1,4)])
md=metric(w1)-metric(w0)
check('Four scalar readings plus conservation do not identify the metric without spectral order',sum(w0)==sum(w1) and same and md==F(1,48),metric_difference=str(md),readings={'R0':str(resp(w0,F(0))),'R_quarter':str(resp(w0,F(1,4)))})
e1=np.array([1.,0,0]); v=np.array([1.,1,0]); e3=np.array([0.,0,1]); outer=lambda x:np.outer(x,x)
G0=outer(e1)+outer(v)/2**3+outer(e3)/1.5**3
G1=outer(e1)/3**3+outer(v)/4**3+outer(e3)/1.5**3
BL=(DD(F(1))-DD(F(3)))*outer(e1)+(DD(F(2))-DD(F(4)))*outer(v)
BL=np.asarray(BL,float)
check('Tensor metric and optical losses retain the same dark direction',np.linalg.eigvalsh(G0-G1)[1]>0 and np.linalg.eigvalsh(BL)[1]>0 and np.linalg.norm((G0-G1)@e3)<1e-14 and np.linalg.norm(BL@e3)<1e-14)

# A Jordan cluster: its trace hides structure that weighted Cauchy data retains.
N=np.array([[0.,1.],[0.,0.]])
b=2.; mu=.6; J=b*np.eye(2)+mu*N
theta=2*np.pi*(np.arange(2048)+.5)/2048
jlog=sum(np.log(b+.4*np.exp(1j*t))*np.linalg.inv((b+.4*np.exp(1j*t))*np.eye(2)-J)*.4*np.exp(1j*t)/2048 for t in theta)
exact=np.log(b)*np.eye(2)+(mu/b)*N
check('A weighted matrix contour detects Jordan structure invisible to the trace',error(jlog,exact)<1e-12 and abs(np.trace(jlog)-2*np.log(b))<1e-12,error=error(jlog,exact),off_diagonal=float(jlog[0,1].real))

# Targeted source audits; counterexamples to stronger historical claims.
G=np.diag([.2,.3,.5]); T=np.eye(3)
X=np.diag([1.,-1.,0]); Y=np.array([[0,1,0],[1,0,0],[0,0,0]],float)
AT=lambda V: V@T+T@V-2*np.trace(T@V)*G
inner=lambda V,W:np.trace(np.linalg.solve(G,V)@np.linalg.solve(G,W))
check('Ladder 11.2 traceless counterexample: T=I is selfadjoint without T proportional to inverse G',np.allclose(AT(X),2*X) and np.allclose(AT(Y),2*Y) and abs(inner(AT(X),Y)-inner(X,AT(Y)))<1e-12 and not np.allclose(T,np.linalg.inv(G)/np.trace(np.linalg.inv(G))*3))
def displacement(omega):return 1/np.sqrt((4-omega**2)**2+(.2*omega)**2)
check('Directional phonon formula has nonzero DC response and decaying high-frequency response at fixed drive',displacement(0)==.25 and displacement(100)<displacement(10),dc_displacement=displacement(0),high_frequency_100=displacement(100))
Fflow=lambda K:-2*((K@K.conj().T-K.conj().T@K)@K-K@(K@K.conj().T-K.conj().T@K))
check('FOFT nonnormality flow is inactive on a closed Hermitian atomic operator',np.linalg.norm(Fflow(H))<1e-13)

# Price of a Direction, Appendix B.7: coupling and detuning scale together.
drive=3.; deltaI=2.; gradient=4.
epsilon_star=np.sqrt(deltaI**2+4/drive**2)/abs(gradient)
def wall_link(epsilon):
    e=.5*epsilon*drive*gradient
    return np.array([[drive,1+e],[1-e,drive*(1+deltaI)]])
below=np.linalg.eigvals(wall_link(epsilon_star*.999))
above=np.linalg.eigvals(wall_link(epsilon_star*1.001))
check('Backreaction ratio gate: drive scales detuning and skew coupling together',np.max(abs(below.imag))==0 and np.max(abs(above.imag))>0,finite_drive_onset=float(epsilon_star),large_drive_limit=deltaI/abs(gradient))


Path(__file__).with_name("finite_controls.json").write_text(json.dumps(checks,indent=2))
print(json.dumps({"passed":sum(x["passed"] for x in checks),"total":len(checks)}))
