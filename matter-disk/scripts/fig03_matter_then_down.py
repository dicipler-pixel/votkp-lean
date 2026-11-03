# SCRIPT: MATTER-DISK-FIG03  one Smith disk, every scale: matter's census ladder, the atom's peel walk,
# the nucleus inside and outside the rim, and opened matter leaving the disk
import numpy as np, csv, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
import importlib.util, io, contextlib
def load(path,cut=None):
    src=open(path).read()
    if cut: src=src.split(cut)[0]
    ns={}; exec(src,ns); return ns
lad=load('s02_ladder.py','op=lambda')
ssh=load('nhssh_lib_and_s03a_occupations.py','w=1.0')
fig,ax=plt.subplots(figsize=(8.6,8.6))
t=np.linspace(0,2*np.pi,400); ax.plot(np.cos(t),np.sin(t),color='0.25',lw=1.4)
for r in (0.25,0.5,0.75): ax.plot(r*np.cos(t),r*np.sin(t),color='0.88',lw=0.7)
ax.axhline(0,color='0.85',lw=0.7); ax.axvline(0,color='0.85',lw=0.7)
# 1 matter: Ising c=1/2 census ladder, Gamma_j = tanh(eps_j/2), shown above the axis
xi,em=lad['ladder'](1.02,8192); lev=em[::2][:6]; G=np.tanh(lev/2)
ax.scatter(G,np.full_like(G,0.10),s=46,color='#1b6f8a',zorder=5,label='matter: Ising census ladder (c = 1/2), Γ = tanh(ε/2)')
# 2 atom: sodium peel walk, composite Gamma from the first removal
rows=[r for r in csv.DictReader(open('/tmp/claude-0/-home-claude/f02ebe36-e50c-5833-b986-4d64a2a87a48/scratchpad/votkp29/zip/VOTKP_v2_9_Code_Proofs_Data_20261013/work/data/nist_asd_ionization_energies_via_mendeleev_1.3.0.csv')) if r['Z']=='11']
seen={}; [seen.setdefault(int(r['ion_charge']),float(r['ionization_energy_eV'])) for r in rows]
IE=np.array([seen[k] for k in sorted(seen)])
walk=np.tanh(0.5*np.log(IE/IE[0]))
ax.plot(walk,np.full_like(walk,-0.10),'-o',color='#c08a2e',ms=5,lw=1,zorder=5,label='atom: sodium peel walk, Γ = tanh(½ ln IEₖ/IE₁)')
ax.scatter([0.377575],[0.0],marker='D',s=70,color='#c08a2e',edgecolor='k',zorder=6,label='atom: helium Γ₀ = 0.378')
# 3 nucleus: his VOTKP 15.4 values (NUBASE2020, rerun here)
inside={'⁴He':0.579,'⁷Li':0.123}; outside={'⁵He':1.074,'⁵Li':1.220,'⁸Be':1.025}
for k,v in inside.items(): ax.scatter([v],[-0.22],marker='s',s=60,color='#7b5ea7',zorder=6); ax.annotate(k,(v,-0.22),(v-0.03,-0.31),fontsize=9)
pos={'⁸Be':(0.97,-0.15),'⁵He':(1.05,-0.33),'⁵Li':(1.19,-0.33)}
for k,v in outside.items(): ax.scatter([v],[-0.22],marker='s',s=60,facecolor='white',edgecolor='#7b5ea7',lw=2,zorder=6); ax.annotate(k,(v,-0.22),pos[k],fontsize=9)
ax.scatter([],[],marker='s',color='#7b5ea7',label='nucleus: bound peels inside, unbound outside (VOTKP §15.4)')
# 4 opened matter: non-Hermitian SSH census levels, u = 0.5, before and after the exit (v_exit = 0.468)
for v,c,lab in [(0.30,'#2a9d55','opened matter, gapped: complex Γ inside'),(0.49,'#d1495b','opened matter past the exit: Γ leaves the disk')]:
    nu=np.linalg.eigvals(ssh['corr'](v,1.0,0.5,2000,40)); nu=nu[(abs(nu)>1e-9)&(abs(1-nu)>1e-9)]
    g=1-2*nu; g=g[abs(g)<1.6]
    ax.scatter(g.real,g.imag,s=10,color=c,alpha=0.8,zorder=4,label=lab)
ax.text(0,1.05,'rim |Γ| = 1: the rapidity has turned a quarter (|Im W| = π/2); negative ratios sit outside',ha='center',fontsize=9,color='0.3')
ax.set_xlim(-1.35,1.35); ax.set_ylim(-1.35,1.35); ax.set_aspect('equal')
ax.set_xlabel('Re Γ'); ax.set_ylabel('Im Γ')
ax.set_title('Matter, then on down: one chart',fontsize=13)
ax.legend(fontsize=7.6,loc='lower left',framealpha=0.95)
plt.tight_layout(); plt.savefig('../figures/fig03_matter_then_down.png',dpi=160)
print('sodium IE count',len(IE),'walk end',walk[-1])
