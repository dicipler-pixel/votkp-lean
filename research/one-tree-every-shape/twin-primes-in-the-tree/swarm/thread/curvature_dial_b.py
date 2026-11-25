# SCRIPT: TWIN-CURVATURE-DIAL-01b (lam=2 rerun; polar turn read by SVD, stable when d is large)
# Does the wobble zone move with the wall? Scale every rapidity by lam (same chain, curvature lam^2
# times stronger). Find where the walker crosses the wall sphere rho^2 = 1/2 (rho = tanh(d/2)), then
# scramble the end-digit arms (counts kept) in 13-step windows right BEFORE and right AFTER that
# crossing, and in the fixed early window 11..227. Turn runout = sd of the final frame turn at 1e8.
# Kill condition is in CURVATURE_DIAL_PREREG.md (written before this run).
import numpy as np, math, json
tw=np.load('../shapes/twins_1000000000.npy').astype(np.int64); tw=tw[(tw>=11)&(tw<=10**8)]
sg=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]],complex)]
arm={1:0,7:1,9:2}
r0=np.log(tw[1:]/tw[:-1]); s=np.array([arm[int(x)%10] for x in tw[1:]]); N=len(r0); W=13
def turn(L):
    Wl,sv,Vh=np.linalg.svd(L); U=Wl@Vh
    return 2*math.degrees(math.acos(min(1,abs(np.trace(U).real)/2)))
def run(lam):
    r=lam*r0; ch=np.cosh(r/2); sh=np.sinh(r/2)
    mats=[ch[i]*np.eye(2)+sh[i]*sg[s[i]] for i in range(N)]
    def prod(a,b,arms=None):
        M=np.eye(2,dtype=complex)
        for i in range(a,b): M=M@(mats[i] if arms is None else ch[i]*np.eye(2)+sh[i]*sg[arms[i-a]])
        return M
    # wall crossing
    M=np.eye(2,dtype=complex); iw=None
    for i in range(N):
        M=M@mats[i]
        d=math.acosh(max(1,np.trace(M@M.conj().T).real/2))
        if math.tanh(d/2)**2>=0.5: iw=i+1; break
    full=prod(0,N); out={'lam':lam,'turn':turn(full),'wall_index':iw,'wall_start':int(tw[iw]) if iw else None,
        'wall_step_gamma2':float(np.tanh(r[iw-1]/2)**2) if iw else None}
    rng=np.random.default_rng(7)
    wins={'before':(max(0,iw-W),iw),'after':(iw,iw+W),'early_11_227':(0,int(np.searchsorted(tw[1:],227,side='right')))}
    for name,(a,b) in wins.items():
        P=prod(0,a); Q=prod(b,N); vals=[turn(P@prod(a,b,rng.permutation(s[a:b]))@Q) for _ in range(200)]
        out[name]=float(np.std(vals)); out[name+'_starts']=[int(tw[a]),int(tw[b])]
        out[name+'_meanGamma2']=float(np.mean(np.tanh(r[a:b]/2)**2))
    out['ratio_before_after']=out['before']/out['after']
    return out
res=[]
for lam in [1.0,2.0]:
    o=run(lam); res.append(o)
    print('lam %.2f turn %7.3f  wall at twin start %8d (step Gamma^2 %.4f) | runout before %.4g after %.4g ratio %.2f | early(11..227) %.4g'%(
        lam,o['turn'],o['wall_start'],o['wall_step_gamma2'],o['before'],o['after'],o['ratio_before_after'],o['early_11_227']),flush=True)
json.dump(res,open('curvature_dial_b_out.json','w'),indent=1)
far=[o for o in res if o['wall_start']>1e4]
print('lam with wall beyond 1e4:',[o['lam'] for o in far])
if far and all(o['ratio_before_after']<1.5 for o in far): print('KILL: wall is not the bite; big early steps are')
elif far: print('PASS: wobble drop follows the wall where it sits among small steps')
else: print('UNDECIDED: no lam put the wall beyond 1e4')
