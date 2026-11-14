# SCRIPT: H01-REAL-GAMMA
# WHY: claim = 1-G^2 is strictly monotone in |G| for real G in (0,1) so it ranks like |G|; H-01's kill used complex metal G.
# Step 1 exact (sympy). Step 2 data: take the 171 H-01 cases (same generator, exec'd from the package script unmodified up to the scoring),
# score (a) |1-G^2| with the complex G as H-01 did, (b) 1-|G|^2 i.e. the same weight with G replaced by its REAL modulus.
# KILL LINE: if (b) gives accuracy different from |G| in any split, the monotone-rank claim fails; if (a) equalled |G| the complex-Gamma explanation of H-01 would fail.
import sympy as sp, numpy as np, os
g=sp.symbols('g',positive=True)
print('d/dg (1-g^2) =',sp.diff(1-g**2,g),' <0 on (0,1): strictly decreasing, so 1-g^2 ranks as -g exactly (bijection on (0,1))')
print('real G in (-1,1): |1-G^2| = 1-G^2 (no abs needed). For real |G|>1 (nuclei beyond rim) |1-G^2|=G^2-1 is INCREASING in |G|: not monotone across the rim')
rho,ph=sp.symbols('rho phi',positive=True)
Gc=rho*sp.exp(sp.I*ph); wabs2=sp.simplify(sp.expand((1-Gc**2)*(1-sp.conjugate(Gc)**2)))
print('complex G=rho e^{i phi}: |1-G^2|^2 =',sp.simplify(wabs2.rewrite(sp.cos)),' -> depends on phi; spans [1-rho^2,1+rho^2]: NOT a function of |G|')
T='/home/claude/check_v29/tree/VOTKP_v2_9_Code_Proofs_Data_20261013/work'
src=open(T+'/particles/h01_lorentz_separator.py').read().split("g=np.array([abs(r[3])")[0]
import io,contextlib
ns={'__file__':T+'/particles/h01_lorentz_separator.py'}; os.environ['VOTKP_ROOT']=T
with contextlib.redirect_stdout(io.StringIO()): exec(src,ns)
rows=ns['rows']; o=np.array([r[4] for r in rows]); metal=np.array([r[0] for r in rows]); G=np.array([r[3] for r in rows])
print('cases',len(rows),'bumps',o.sum(),'distinct G',len(set(np.round(G,10))),'always-bump',round(o.mean(),3),'imag parts: max |Im G|=%.3f (G is complex)'%np.abs(G.imag).max())
def best_t(s,y):
    ts=np.unique(s); a=[np.mean((s>=t)==y) for t in ts]; k=int(np.argmax(a)); return ts[k],a[k]
def score(s):
    t,acc=best_t(s,o); pred=np.zeros(len(o),bool)
    for m in np.unique(metal):
        tr=metal!=m; tt,_=best_t(s[tr],o[tr]); pred[~tr]=s[~tr]>=tt
    return acc,np.mean(pred==o)
S={'|G|':-np.abs(G),'|1-G^2| complex G (H-01)':np.abs(1-G**2),'1-|G|^2 (real modulus)':1-np.abs(G)**2}
for k,s in S.items(): print('%-28s in-sample %.3f  leave-one-metal-out %.3f'%((k,)+score(s)))
rk=lambda s:np.argsort(np.argsort(s,kind='stable'))
from scipy.stats import spearmanr
print('Spearman(|1-G^2|, -|G|) on complex G = %.3f ; Spearman(1-|G|^2, -|G|) = %.3f'%(spearmanr(S['|1-G^2| complex G (H-01)'],S['|G|'])[0],spearmanr(S['1-|G|^2 (real modulus)'],S['|G|'])[0]))
# fraction of case pairs ordered differently
a=np.abs(1-G**2); m=np.abs(G); 
d=0;tot=0
for i in range(len(G)):
    for j in range(i+1,len(G)):
        if m[i]!=m[j]: tot+=1; d+= ((a[i]-a[j])*(m[i]-m[j])>0)
print('pairs where |1-G^2| increases with |G| (wrong direction for a monotone decreasing map): %d of %d'%(d,tot))
