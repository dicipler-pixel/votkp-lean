# SCRIPT: FIG-MATTER-PEEL-01  signature map + Smith-disk portraits, NH SSH
import numpy as np, matplotlib
matplotlib.rcParams['pdf.fonttype']=42
import matplotlib.pyplot as plt
exec(open('nhssh_lib_and_s03a_occupations.py').read().split('w=1.0')[0]); w=1.0
M=np.load('sig_u0.5.npy'); ks=np.linspace(0.02,2*np.pi-0.02,180); vs=np.linspace(0.05,1.95,96)
fig=plt.figure(figsize=(12,4.6))
ax=fig.add_axes([0.05,0.12,0.36,0.70])
cm=matplotlib.colors.ListedColormap(['#E0793A','#dddddd','#4FA3C7'])
ax.pcolormesh(ks,vs,M,cmap=cm,vmin=-1,vmax=1,shading='auto')
kk,VV=np.meshgrid(ks,vs); ax.contour(ks,vs,np.abs(VV+w*np.exp(1j*kk))-0.5,[0],colors='k',linewidths=1.2)
ax.plot([np.pi,np.pi],[0.5,1.5],'k*',ms=12)
ax.set_xlabel('momentum k'); ax.set_ylabel('hopping v  (w = 1, gain/loss u = 0.5)')
ax.set_title('band metric signature: orange Lorentzian, blue (-,-)\nblack line: exceptional points; stars: critical points (c<0)',fontsize=9)
cases=[(0.5,0.0,'closed matter (Hermitian)\nc = 0'),(0.5,0.3,'opened, gapped\nc = 0'),(0.5,0.5,'opened, critical\nc < 0')]
for i,(v,u,t) in enumerate(cases):
    a=fig.add_axes([0.46+0.18*i,0.14,0.16,0.64])
    nu=np.linalg.eigvals(corr(v,w,u,2000,80)); G=1-2*nu
    th=np.linspace(0,2*np.pi,300); a.plot(np.cos(th),np.sin(th),'k-',lw=1)
    a.plot(G.real,G.imag,'o',ms=3.5,color='#4FA3C7' if u==0 else ('#79C089' if u<0.5 else '#D8534F'))
    a.set_xlim(-3.4,3.4); a.set_ylim(-3.4,3.4); a.set_aspect('equal'); a.set_title(t,fontsize=9)
    a.set_xlabel('Re Γ'); 
    if i==0: a.set_ylabel('Im Γ')
fig.suptitle('Census levels as peel coordinates Γ = 1 - 2ν: closed matter lives on the real diameter, opened matter leaves the disk at the critical wall',fontsize=10,y=0.985)
fig.savefig('fig_matter_peel.png',dpi=150); print('ok')
