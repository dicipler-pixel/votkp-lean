from pathlib import Path
import json
import sympy as s
import numpy as np
from scipy.linalg import expm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out=Path('output/sun_blackholes'); out.mkdir(parents=True,exist_ok=True)
z,a,b,k=s.symbols('z a b k',positive=True)
L=s.Matrix([[-(k+a),b],[a,-b]])
T=s.factor(k*((z*s.eye(2)-L).inv())[0,0])
expected=k*(z+b)/(z*z+(k+a+b)*z+k*b)
assert s.simplify(T-expected)==0
assert s.simplify(T.subs(z,0)-1)==0
assert s.simplify(-s.diff(T,z).subs(z,0)-(1+a/b)/k)==0
assert s.simplify(sum(L*s.Matrix(s.symbols('x y')))+k*s.Symbol('x'))==0
assert s.simplify(T.subs(b,0)-k/(z+k+a))==0
I,alpha,eta,p=s.symbols('I alpha eta p',positive=True)
rate=I/(I+alpha*eta*a*p/(k*b))
assert s.simplify(s.diff(rate,b)-I*alpha*eta*a*p*k/(I*k*b+alpha*eta*a*p)**2)==0
checks={'symbolic_assertions':6,'transfer_function':str(T),'mean_dwell':str(s.simplify(-s.diff(T,z).subs(z,0))),'model_only':True}

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'figure.facecolor':'#081321','axes.facecolor':'#081321','text.color':'#eef4fb','axes.labelcolor':'#eef4fb','xtick.color':'#bdcad8','ytick.color':'#bdcad8','axes.edgecolor':'#617589','savefig.facecolor':'#081321'})
fig,ax=plt.subplots(figsize=(12.5,5))
ts=np.linspace(0,40,1000)
checks['examples']=[]
for ret,col in [(1.,'#5dd5f5'),(.1,'#f9cd70'),(0.,'#f08ca8')]:
 M=np.array([[-2.,ret],[1.,-ret]])
 vals=np.array([expm(M*t)@np.array([1.,0.]) for t in ts])
 assert np.min(vals)>-1e-13
 ax.plot(ts,vals[:,1],lw=2.5,color=col,label=f'return rate b = {ret:g}')
 checks['examples'].append({'return_rate':ret,'retained_at_t40':float(vals[-1,1]),'eventual_escape_fraction':1. if ret>0 else .5})
ax.set(xlabel='Time (model units)',ylabel='Retained energy / incoming energy',ylim=(-.015,.56),xlim=(0,40))
ax.set_title('The return channel separates delayed release from permanent retention',loc='left',pad=16,fontsize=14)
ax.grid(alpha=.13);ax.legend(frameon=False,loc='upper right',labelcolor='#eef4fb')
ax.text(.99,.035,'Conditional two-stock model; a = κ = 1. No astronomical data fitted.',transform=ax.transAxes,ha='right',fontsize=9,color='#bdcad8')
fig.tight_layout()
fig.savefig(out/'retention_response.png',dpi=190)
fig.savefig(out/'retention_response.pdf')
(out/'retention_checks.json').write_text(json.dumps(checks,indent=2))
print(json.dumps(checks,indent=2))

