# SCRIPT: PAPER-FIGURES-01  (figures for "The Centre Is Always in Flux"; every plotted number is computed here or read from a saved output)
import numpy as np, math, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
BG='#0b0f17'; GOLD='#f2c14e'; BLUE='#4aa3ff'; INK='#e8e6df'; DIM='#8a93a3'; RED='#e0705a'
plt.rcParams.update({'figure.facecolor':BG,'axes.facecolor':BG,'savefig.facecolor':BG,'text.color':INK,'axes.edgecolor':DIM,
 'axes.labelcolor':INK,'xtick.color':DIM,'ytick.color':DIM,'font.family':'DejaVu Sans','font.size':11})
# ---- Figure 1: the scale
fig,ax=plt.subplots(figsize=(9,2.6)); ax.set_xlim(1.2,4.3); ax.set_ylim(-1,1.3); ax.axis('off')
ax.plot([1.3,4.2],[0,0],color=DIM,lw=1.5)
for x,lab,sub,c in ((1.5,'3/2','flat space',BLUE),(5/3,'5/3','tree (three-leg star)',BLUE),(2,'2','building\n(curved ceiling)',GOLD),(4,'4','no curvature rule',DIM)):
    ax.plot([x],[0],'o',ms=13,color=c); ax.text(x,0.42,lab,ha='center',fontsize=17,color=c,weight='bold'); ax.text(x,-0.72,sub,ha='center',fontsize=10,color=INK)
ax.text(1.3,1.05,'mean squared rank-2 step  /  mean squared rank-1 step,  on the sixteen 2 by 2 matrices over the two-element field',fontsize=10,color=DIM)
fig.savefig('fig/fig1_scale.png',dpi=170,bbox_inches='tight'); plt.close(fig)
# ---- Figure 2: the star
fig,ax=plt.subplots(figsize=(6.4,5.6)); ax.set_aspect('equal'); ax.axis('off'); ax.set_xlim(-1.9,1.9); ax.set_ylim(-1.75,1.75)
legs=[('(1,0)',90),('(0,1)',210),('(1,1)',330)]
for lab,a in legs:
    t=math.radians(a); x,y=1.15*math.cos(t),1.15*math.sin(t); ax.plot([0,x],[0,y],color=GOLD,lw=2.2)
    for k in (-1,0,1):
        px,py=x+0.16*k*math.cos(t+math.pi/2),y+0.16*k*math.sin(t+math.pi/2); ax.plot([px],[py],'o',ms=10,color=BLUE)
    ax.text(1.5*math.cos(t),1.5*math.sin(t)-(0.22 if a!=90 else 0),'three rank-1 matrices\nwith image '+lab,ha='center',va='center',fontsize=9.5)
for k in range(7):
    t=2*math.pi*k/6; r=0 if k==6 else 0.17; ax.plot([r*math.cos(t)],[r*math.sin(t)],'o',ms=9,color=(GOLD if k==6 else INK))
ax.text(0.28,-0.02,'centre: the zero matrix\nand the six invertible ones',fontsize=9.5,va='center')
ax.text(-1.85,-1.7,'ratio exactly 5/3.  The six invertible matrices permute the legs as Sym(3).',fontsize=9.5,color=DIM)
fig.savefig('fig/fig2_star.png',dpi=170,bbox_inches='tight'); plt.close(fig)
# ---- Figure 3: the disc
fig,ax=plt.subplots(figsize=(6.6,6.4)); ax.set_aspect('equal'); ax.set_xlim(-1.75,1.75); ax.set_ylim(-1.75,1.75); ax.axis('off')
ax.add_patch(Circle((0,0),1,fill=False,ec=DIM,lw=1.6)); ax.plot([-1.6,1.6],[0,0],color=DIM,lw=0.7); ax.plot([0,0],[-1.6,1.6],color=DIM,lw=0.7)
for f in (0.05,0.1,0.15,0.2,0.25,0.29):
    g=-math.tan(math.pi*f); ax.plot([0],[g],'o',ms=8,color=GOLD); ax.text(0.07,g,'flux %.2f'%f,fontsize=8.5,va='center',color=GOLD)
ax.text(0.07,-1.0-0.11,'(a quarter quantum: the rim)',fontsize=8,color=DIM)
ax.plot([-1],[0],'o',ms=13,color=BLUE); ax.text(-1.05,0.13,'cat\nΓ = −1',ha='right',fontsize=10,color=BLUE)
ax.plot([1],[0],'o',ms=13,color=GOLD); ax.text(1.05,0.13,'grin\nΓ = +1',ha='left',fontsize=10,color=GOLD)
ax.plot([-1/3],[0],'s',ms=10,color=INK); ax.text(-1/3,0.12,'plain-light\ntune-out −1/3',ha='center',fontsize=8.5)
ax.plot([1/3],[0],'s',ms=10,color=INK); ax.text(1/3,0.12,'handed\ntune-out +1/3',ha='center',fontsize=8.5)
ax.plot([0],[0],'+',ms=14,color=INK); ax.text(0.06,0.42,'centre:\nboth arms equal',ha='left',fontsize=8.5,color=DIM); ax.plot([0.02,0.06],[0.03,0.38],color=DIM,lw=0.6)
ax.text(-1.7,1.6,'The Smith disc.  Arm shares are (1 − Γ)/2 and (1 + Γ)/2.',fontsize=10)
ax.text(-1.7,-1.72,'Real diameter: strength ratios (handed twists, tune-outs).  Imaginary axis: flux.',fontsize=9,color=DIM)
fig.savefig('fig/fig3_disc.png',dpi=170,bbox_inches='tight'); plt.close(fig)
# ---- Figure 4: the pair wave of the table
import mendeleev, warnings; warnings.filterwarnings('ignore')
from mendeleev import element
E=[element(z) for z in range(1,87)]; Z=np.arange(1,87)
ie=np.log(np.array([e.ionenergies[1] for e in E])); pol=np.log(np.array([e.dipole_polarizability for e in E]))
def m_of(z):
    lo,hi=0.0,40.0
    for _ in range(80):
        mid=(lo+hi)/2
        if mid**3-mid<6*z: lo=mid
        else: hi=mid
    return lo
u=np.array([m_of(z+2) for z in Z])
fig,axs=plt.subplots(2,1,figsize=(9.4,5.6),sharex=True)
for ax,y,lab,c in ((axs[0],ie,'log first ionization energy',GOLD),(axs[1],pol,'log dipole polarizability',BLUE)):
    ax.plot(u,y,'-',color=c,lw=1.3); ax.plot(u,y,'o',ms=3,color=c)
    for zz,nm in ((2,'He'),(10,'Ne'),(18,'Ar'),(36,'Kr'),(54,'Xe'),(86,'Rn')):
        ax.axvline(m_of(zz+2),color=DIM,lw=0.6,ls=':'); 
        if ax is axs[0]: ax.text(m_of(zz+2),ax.get_ylim()[1],nm,ha='center',va='bottom',fontsize=8.5,color=DIM)
    for (a,b) in ((3,5),(7,9)): ax.axvspan(a,b,color='#16202f',zorder=0)
    ax.set_ylabel(lab,fontsize=9.5)
axs[1].set_xlabel('exact pair coordinate m, where 6(Z + 2) = m³ − m   (one period pair = 2 units; alternate pairs shaded)')
fig.savefig('fig/fig4_table.png',dpi=170,bbox_inches='tight'); plt.close(fig)
corr=np.corrcoef(ie,pol)[0,1]; sl=np.polyfit(ie,pol,1); print('raw correlation log IE vs log polarizability %.3f ; slope %.3f'%(corr,sl[0]))
# ---- Figure 5: ghost lines of the primes (numbers read from ghosts_output.txt)
rows=[]
for line in open('ghosts_output.txt'):
    p=line.split()
    if len(p)>=6 and '/' in p[0] and p[3]=='|' and p[0]!='a/q':
        rows.append((p[0],float(p[1]),float(p[2]),float(p[4]),float(p[5])))
keep=['1/2','1/3','1/5','2/5','1/7','2/7','3/7','1/30','1/210','1/4','1/9','1/25']
rows=[r for k in keep for r in rows if r[0]==k]
fig,axs=plt.subplots(2,1,figsize=(9.4,5.2),sharex=True); x=np.arange(len(rows))
for ax,i,j,lab,c in ((axs[0],1,2,'primes',GOLD),(axs[1],3,4,'twin-prime starts',BLUE)):
    ax.bar(x-0.2,[r[i] for r in rows],0.4,color=c,label='measured to 10⁷'); ax.bar(x+0.2,[r[j] for r in rows],0.4,color=INK,alpha=0.55,label='formula')
    ax.set_ylabel('line height\n('+lab+')',fontsize=9.5); ax.legend(frameon=False,fontsize=8.5)
axs[1].set_xticks(x); axs[1].set_xticklabels([r[0] for r in rows]); axs[1].set_xlabel('frequency (turns per integer step)')
fig.savefig('fig/fig5_ghosts.png',dpi=170,bbox_inches='tight'); plt.close(fig)
# ---- Figure 6: the moment ladder of hydrogen
from fractions import Fraction as Fr
S={-1:Fr(2),-2:Fr(9,2),-3:Fr(43,4),-4:Fr(319,12),-5:Fr(9673,144),-6:Fr(297541,1728)}
ks=[-1,-2,-3,-4,-5,-6]; q=[float(S[k-1]/S[k]) for k in ks[:-1]]
fig,ax=plt.subplots(figsize=(8.4,3.4)); ax.plot(range(len(q)),q,'o-',color=GOLD,lw=1.6); ax.axhline(8/3,color=BLUE,ls='--',lw=1.2); ax.text(4.02,8/3+0.01,'8/3',color=BLUE)
ax.set_xticks(range(len(q))); ax.set_xticklabels(['S(−2)/S(−1)','S(−3)/S(−2)','S(−4)/S(−3)','S(−5)/S(−4)','S(−6)/S(−5)'],fontsize=9)
ax.set_ylabel('rung quotient'); ax.text(0.05,2.6,'hydrogen, exact fractions.  The tensor at rung −3:  81/16  ≤  43/8  ≤  6',fontsize=9.5)
fig.savefig('fig/fig6_ladder.png',dpi=170,bbox_inches='tight'); plt.close(fig)
print('figures written')
