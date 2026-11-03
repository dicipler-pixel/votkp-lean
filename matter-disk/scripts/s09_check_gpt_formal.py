# SCRIPT: MATTER-DISK-S09  independent checks of the GPT formal edition's new claims
import numpy as np, importlib.util, io, contextlib, sys
sys.path.insert(0,'/home/claude/votkp-lean/matter-disk/scripts')
spec=importlib.util.spec_from_file_location('s06','/home/claude/votkp-lean/matter-disk/scripts/s06_second_model_exit_law.py')
src=open('/home/claude/votkp-lean/matter-disk/scripts/s06_second_model_exit_law.py').read().split('# check the general Petermann formula')[0]
ns={}; exec(src,ns)
# (1) endpoint filter sensitivity of the massive exit (claim: 0.2716 at 1e-8, 0.16917 at 1e-9, 0.12279 at 1e-12)
def exit_g(t1,m,d):
    rot=lambda g: ns['rotation'](t1,m,g,d=d)[0]
    lo,hi,g=0.0,None,0.05
    while hi is None and g<4:
        if rot(g)>=0.5: hi=g
        else: lo=g; g*=1.4
    for _ in range(28):
        mid=(lo+hi)/2
        if rot(mid)<0.5: lo=mid
        else: hi=mid
    return (lo+hi)/2
print('(1) massive band t1=0.5 m=0.4, exit gamma by endpoint filter:')
for d in [1e-6,1e-8,1e-9,1e-10,1e-12]:
    print(f'    filter {d:.0e}: exit gamma {exit_g(0.5,0.4,d):.9f}')
print('    massless t1=0.5 m=0, filters 1e-8 and 1e-12:', f'{exit_g(0.5,0.0,1e-8):.9f}', f'{exit_g(0.5,0.0,1e-12):.9f}')
# (2) P3: w=0, v^2=2u^2 -> <K>=2 yet compressed projector idempotent (eigenvalues 0,1)
lib=open('/home/claude/votkp-lean/matter-disk/scripts/nhssh_lib_and_s03a_occupations.py').read().split('w=1.0')[0]; ns2={}; exec(lib,ns2)
u=0.5; v=np.sqrt(2)*u
C=ns2['corr'](v,0.0,u,400,40); nu=np.linalg.eigvals(C)
print('(2) P3 w=0, v^2=2u^2: max distance of block eigenvalues from {0,1} =',f'{np.max(np.minimum(abs(nu),abs(1-nu))):.1e}','; band <K> = 1+u^2/(E0 Epi) =',1+u**2/(v**2-u**2))
# (3) D5 idempotent
C=np.array([[2,1],[-2,-1]]); print('(3) D5: C^2==C', np.allclose(C@C,C), ' Y_A =',C[0,1]*C[1,0], ' A-A^2 =',2-4)
# (4) B13: 4 Tr X_A <= I_G on random Gaussian covariances; sharp family
rng=np.random.default_rng(3); h=lambda x: -np.sum(x*np.log(x)+(1-x)*np.log(1-x))
worst=np.inf
for _ in range(200):
    n=10; M=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); U,_=np.linalg.qr(M); ev=rng.uniform(0.02,0.98,n)
    C=U@np.diag(ev)@U.conj().T; A=C[:4,:4]; D=C[4:,4:]; B=C[:4,4:]
    IG=h(np.linalg.eigvalsh(A))+h(np.linalg.eigvalsh(D))-h(ev); worst=min(worst,IG-4*np.trace(B@B.conj().T).real)
print('(4) B13 lower bound: min of I_G - 4 Tr X_A over 200 random cases =',f'{worst:.3e}','(>=0 required)')
# (5) G9 partition bias: U1 = 2+4exp(-10eV/kT), naive inversion at 30/32 kK
kB=8.617333262e-5; I0,I1=24.587389011,54.4177655282
def logs(T,U1):
    b=1/(kB*T); return b, -b*(I1-I0)+np.log(1*1/U1**2), b*(I0+I1)+np.log(1/(4*1))  # L_q and L_B with U0=U2=1
U1=lambda T: 2+4*np.exp(-10/(kB*T))
(b1,a1,c1),(b2,a2,c2)=logs(30000,U1(30000)),logs(32000,U1(32000))
Dn=-(a2-a1)/(b2-b1); Bn=(c2-c1)/(b2-b1)
print('(5) G9 naive Gamma with synthetic U1(T):',f'{Dn/Bn:.14f}','(claim 0.36614943350748); exact',f'{(I1-I0)/(I1+I0):.14f}')
