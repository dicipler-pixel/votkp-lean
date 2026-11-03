# SCRIPT: MATTER-DISK-FIG02  warm census on the disk (raw vs boundary) and the helium gas on the disk
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
import importlib.util, sys, io, contextlib
def load(name):
    spec=importlib.util.spec_from_file_location(name,name+'.py'); m=importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(m)
    return m
b=load('s07_boundary_census_disk'); g=load('s08_gas_carries_the_peel')
fig,ax=plt.subplots(1,2,figsize=(12,5.2))
H=b.ring(1,1); cols={0:'#1b6f8a',0.5:'#c08a2e',2:'#7b5ea7'}
for i,T in enumerate([0,0.5,2]):
    C=b.thermal(H,T); CA,CAB,CBA=b.blocks(C,64); nu=np.linalg.eigvalsh(CA); lam=np.linalg.eigvalsh((CAB@CBA+(CAB@CBA).T)/2)
    G=np.abs(1-2*nu); Gb=np.sqrt(np.clip(1-4*lam,0,1))
    ax[0].scatter(G,np.full_like(G,i+0.15),s=14,color=cols[T],marker='o',label=f'T={T}: raw |Γ| = |1−2ν|')
    ax[0].scatter(Gb,np.full_like(Gb,i-0.15),s=14,color=cols[T],marker='x',label=f'T={T}: boundary |Γ_b|')
ax[0].axvline(0.8,color='0.6',ls=':',lw=1)
ax[0].axvspan(0,0.8,color='0.93',zorder=0)
ax[0].set_xlim(0,1.02); ax[0].set_yticks([0,1,2]); ax[0].set_yticklabels(['T = 0','T = 0.5','T = 2'])
ax[0].set_xlabel('distance from the disk centre  |Γ|   (rim = 1)'); ax[0].set_title('Heat pulls raw levels inward; the boundary census sends them back to the rim\n(uniform ring, 128 sites, half-ring region, shaded = count window ε = 0.1)',fontsize=10)
ax[0].legend(fontsize=7,ncol=3,loc='upper center',bbox_to_anchor=(0.5,-0.13))
Ts=np.linspace(8000,80000,300)
for n,ls in [(1e18,':'),(1e22,'-'),(1e26,'--')]:
    G0s=[];G1s=[]
    for T in Ts:
        p,_,_=g.saha(T,n); G0s.append(np.tanh(0.5*np.log(max(p[0],1e-300)/max(p[1],1e-300)))); G1s.append(np.tanh(0.5*np.log(max(p[1],1e-300)/max(p[2],1e-300))))
    ax[1].plot(Ts/1000,G0s,color='#1b6f8a',ls=ls,label=f'He ↔ He⁺ pair, n = {n:.0e} m⁻³')
    ax[1].plot(Ts/1000,G1s,color='#c08a2e',ls=ls,label=f'He⁺ ↔ He²⁺ pair, n = {n:.0e} m⁻³')
ax[1].axhline(g.G0,color='#7b5ea7',lw=2.2,label=f'Γ₀ read back from the gas = {g.G0:.6f} at every density')
ax[1].axhline(0,color='0.6',lw=0.8)
ax[1].set_xlabel('temperature (thousand K)'); ax[1].set_ylabel('population disk point  Γ_pop = tanh(½ ln n_q/n_(q+1))')
ax[1].set_title('Helium (VOTKP ladder): the gas state sweeps the disk,\nthe peel coordinate Γ₀ stays put',fontsize=10)
ax[1].legend(fontsize=7,loc='lower left'); ax[1].set_ylim(-1.05,1.05)
plt.tight_layout(); plt.savefig('../figures/fig02_boundary_and_gas.png',dpi=150)
