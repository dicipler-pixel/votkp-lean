# SCRIPT: FEED-LOOP-03
# WHY THIS DECIDES IT: his points of 12 Nov (light pressure on the ball, rotation inside and outside the layer,
# direction of the prepared light) are put as exact statements about the same loop W(z). Each is an identity
# in the step ratio z; a false one leaves an order-1 residual.
# KILL LINES (before the run):
#  P1  with R = Gamma^2, T = 1 - R (one lossless layer): sinh^2(r/2) = R/T, loop trace = 2 - 4 (R/T)^2, wall <=> R = T. residual > 1e-10 -> kill
#  P2  K = 1/(T - R) = 1/(1 - P), P = 2R = push on the layer in units of the full-absorption push. residual > 1e-9 -> kill
#  P3  arm along the turn axis (k): sin^2(phi_k) = 2 Gamma^2 = P for every z inside the wall. residual > 1e-9 -> kill
#  P4  centre of turn inside the half-line sphere for z < 5, on it at z = 5, outside for 5 < z < wall. any exception -> kill
#  P5  kicks: n-th lab state stays on one circle of the rim (fixed angle to the eigen-line in the own frame). residual > 1e-9 -> kill
#  P6  past the wall: lab state runs to one rim point; distance falls as exp(-n*lambda), lambda = 2 arccosh(-tr/2). slope error > 1e-6 -> kill
import numpy as np, json, importlib.util
spec=importlib.util.spec_from_file_location('f2','/home/claude/mixer_v2/feed_loop_02.py')
src=open('/home/claude/mixer_v2/feed_loop_02.py').read().split('out={}; k1=k2=k4=0')[0]; exec(src)
out={}; p1=p2=p3=0; p4=True; zs=np.linspace(1.02,ZW-1e-3,500)
for z in zs:
    a=anatomy(z); R=a['G']**2; T=1-R; r=np.log(z)
    p1=max(p1,abs(np.sinh(r/2)**2-R/T),abs(np.trace(a['W']).real-(2-4*(R/T)**2))/max(1,(R/T)**2))
    p2=max(p2,abs(a['K']*(T-R)-1))
    psi=np.linalg.inv(a['S'])@state([0,0,1]); s0=bloch(psi); p3=max(p3,abs(1-np.dot(s0,a['axis'])**2-2*R))
    side=a['rho']**2-0.5
    if (z<5-1e-9 and side>=0) or (z>5+1e-9 and side<=0): p4=False
out.update(P1=p1,P2=p2,P3=p3,P4=p4,wall_R=float(np.tanh(np.log(ZW)/2)**2))
# P5 kicks at z=5
a=anatomy(5.0); Si=np.linalg.inv(a['S']); p5=0
for prep in ([1,0,0],[0,0,1],[1,1,1]):
    lab=state(prep); c0=None
    for n in range(50):
        own=bloch(Si@lab); c=np.dot(own,a['axis'])
        c0=c if c0 is None else c0; p5=max(p5,abs(c-c0)); lab=a['W']@lab; lab/=np.linalg.norm(lab)
out['P5']=p5
# P6 past the wall
rows=[]
for z in [6.5,8,16.8177]:
    r=np.log(z); W=loop(r); w,V=np.linalg.eig(W); i=np.argmax(abs(w)); tgt=bloch(V[:,i]); lam=2*np.arccosh(-(2-4*np.sinh(r/2)**4)/2)
    lab=state([0,0,1]); d=[]
    for n in range(8):
        d.append(np.linalg.norm(bloch(lab)-tgt)); lab=W@lab; lab/=np.linalg.norm(lab)
    d=np.array(d); good=d>1e-12; sl=np.polyfit(np.arange(8)[good][1:5],np.log(d[good][1:5]),1)[0]
    rows.append(dict(z=z,lambda_=lam,fitted_slope=sl,slope_plus_lambda=sl+lam))
out['P6']=rows
# numbers for the page at z=5
out['z5']=dict(R=4/9,T=5/9,P=8/9,K=a['K'],turn_per_loop_over_2pi=a['theta']/(2*np.pi))
print(json.dumps(out,indent=1,default=float)); open('feed_loop_03.out','w').write(json.dumps(out,indent=1,default=float))
