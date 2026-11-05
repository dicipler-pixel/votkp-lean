"""fig09: the exit ladder. Left: theta(v) from the Abel formula, measured edge phases, quarter-turn continuation.
Right: the ladder Gamma_j = tanh((j*Delta + i*theta)/2) in the disk, inside / on / past the exit line."""
import numpy as np, mpmath as mp, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
exec(open('s15_exit_ladder.py').read().split('out=[]')[0])
plt.rcParams.update({'font.size':9,'axes.spines.top':False,'axes.spines.right':False,'pdf.fonttype':42})
cols=['#2a78d6','#eb6834','#1baf7a']
fig,ax=plt.subplots(1,2,figsize=(9.2,3.9),gridspec_kw={'width_ratios':[1.35,1]})
a=ax[0]
for u,c in zip([0.3,0.5,0.7],cols):
    vmax=1-u-1e-4; vs=np.concatenate([np.linspace(0.0,vmax-0.05,150),vmax-np.geomspace(0.05,1e-4,150)])
    th=[predict(v,1,u)[1] for v in vs]
    gam=[2*np.arctan(u/np.sqrt(np.sqrt((1+v)**2-u*u)*np.sqrt((1-v)**2-u*u))) for v in vs]
    a.plot(vs,th,color=c,lw=2,label=f'$u={u}$, Abel phase $\\theta$')
    a.plot(vs,gam,color=c,lw=1,ls='--')
    vm=np.linspace(0.05,1-u-0.2,5)
    for v in vm:
        lv=measure(v,1,u); e=min(lv,key=lambda x:abs(x[1].real))[1]
        a.plot(v,e.imag,'o',ms=5,mfc='white',mec=c,mew=1.5)
    ve=float(mp.findroot(lambda x:(1-x*x)/mp.sqrt(2*(1+x*x))-u,0.4))
    a.plot(ve,np.pi/2,'*',color='0.15',ms=9,zorder=5)
a.axhline(np.pi/2,color='0.55',lw=0.8); a.text(0.56,np.pi/2-0.13,'rim: $\\theta=\\pi/2$',color='0.35',fontsize=8)
a.set_xlabel('$v$  ($w=1$)'); a.set_ylabel('edge phase  Im $\\varepsilon_j$')
a.set_yticks([0,np.pi/4,np.pi/2,3*np.pi/4,np.pi]); a.set_yticklabels(['0','$\\pi/4$','$\\pi/2$','$3\\pi/4$','$\\pi$'])
a.plot([],[],'o',mfc='white',mec='0.3',label='measured, block 90 cells'); a.plot([],[],'--',color='0.3',lw=1,label='quarter-turn continuation')
a.plot([],[],'*',color='0.15',label='exit line $E(0)E(\\pi)=u^2$')
a.legend(frameon=False,fontsize=7.5,loc='upper left'); a.set_ylim(0,np.pi*1.02); a.set_xlim(-0.02,0.72)
b=ax[1]; t=np.linspace(0,2*np.pi,400); b.plot(np.cos(t),np.sin(t),color='0.3',lw=1)
u=0.5
for v,c,lab in [(0.3,cols[0],'$v=0.30$: inside'),(0.4682,cols[1],'$v=0.468$: on the rim'),(0.48,cols[2],'$v=0.48$: past the exit')]:
    D,th,p=predict(v,1,u); x=np.linspace(-12,12,400)
    G=np.tanh((x+1j*th)/2); b.plot(G.real,G.imag,color=c,lw=1,alpha=0.6)
    j=np.arange(-3,4); Gj=np.tanh((j*D+1j*th)/2)
    b.plot(Gj.real,Gj.imag,'o',color=c,ms=6,mec='white',mew=1,label=lab)
b.set_aspect('equal'); b.set_xlim(-1.15,1.15); b.set_ylim(-0.75,1.25)
b.set_xlabel('Re $\\Gamma$'); b.set_ylabel('Im $\\Gamma$'); b.legend(frameon=False,fontsize=7.5,loc='lower center',ncol=1)
b.set_title('ladder $\\Gamma_j=\\tanh((j\\Delta+i\\theta)/2)$, $u=0.5$',fontsize=9)
plt.tight_layout(); plt.savefig('../figures/fig09_exit_ladder.png',dpi=220); plt.savefig('../figures/fig09_exit_ladder.pdf')
