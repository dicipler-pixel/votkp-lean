from fractions import Fraction as F
import contextlib,io,importlib.util,json
from pathlib import Path
p=Path(__file__).parent; spec=importlib.util.spec_from_file_location('diagram',p/'theta_diagram.py');m=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):spec.loader.exec_module(m)
pts=[(F(2),F(3)),(F(3),F(2)),(F(1,2),F(2))]
Y=[(1,2*k,(2*k+7)%14) for k in range(7)];R=[0]*15;R[7]=-1
X=[(1,0,3),(1,4,1),(1,2,5)];rot=[0,0,0,-1,0,0,0]
for name,A,B in [('trefoil',X,rot),('seven',Y,R)]:
 for j in range(len(A)):
  c=A[:];s,i,k=c[j];c[j]=(-s,k,i)
  points=[]
  for a,b in pts:
   theta,delta=m.calc(c,B,a,b)
   target=F(1) if name=='trefoil' else a*a-a+1-a**-1+a**-2
   same=theta==m.calc(A,B,a,b)[0]
   points.append({'delta':str(delta),'expected_delta':str(target),'pass':delta==target,'theta':str(theta),'theta_zero':theta==0,'theta_changed':not same})
  print(json.dumps({'knot':name,'crossing':j,'points':points}))
