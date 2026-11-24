# SCRIPT: TWIN-PAPER-FIGURES-01
# All figures for the write-up. Data come from the runs recorded on the branch; nothing is invented.
import numpy as np, csv, math, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
BG='#0b0e14'; FG='#e6e1d3'; GOLD='#e8b84a'; BLUE='#4a90e2'; RED='#e0605a'; GREY='#8a8f99'; GREEN='#6cc08b'
plt.rcParams.update({'figure.facecolor':BG,'axes.facecolor':BG,'savefig.facecolor':BG,'text.color':FG,'axes.labelcolor':FG,
 'xtick.color':FG,'ytick.color':FG,'axes.edgecolor':GREY,'font.size':11,'axes.titlesize':12,'legend.facecolor':BG,'legend.edgecolor':GREY})
S='/tmp/claude-0/-home-claude/502f5ad8-acd9-59a2-b5cf-d48e7967cc3a/scratchpad/'
def save(f,n): f.savefig('fig/'+n,dpi=200,bbox_inches='tight'); plt.close(f)

# F1 the chain in the ball (Poincare ball, radius tanh(d/2)), twin starts to 1e6
tw=np.load(S+'swarm/shapes/twins_1000000000.npy'); tw=tw[(tw>=11)&(tw<=1_000_000)].astype(float)
sg=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]],complex)]
ax_of={1:0,7:1,9:2}; L=np.eye(2,dtype=complex); pts=[np.zeros(3)]
for k in range(1,len(tw)):
    r=math.log(tw[k]/tw[k-1]); s=sg[ax_of[int(tw[k])%10]]
    L=L@(math.cosh(r/2)*np.eye(2)+math.sinh(r/2)*s)
    M=L@L.conj().T; v=np.array([np.trace(M@x).real for x in sg])/np.trace(M).real  # Bloch = tanh(d) n
    t=np.linalg.norm(v); d=math.atanh(min(t,1-1e-16)); n=v/t if t>0 else v
    pts.append(math.tanh(d/2)*n)
pts=np.array(pts)
f=plt.figure(figsize=(7,7)); a=f.add_subplot(projection='3d'); a.set_facecolor(BG)
u,vv=np.mgrid[0:2*np.pi:60j,0:np.pi:30j]
a.plot_surface(np.cos(u)*np.sin(vv),np.sin(u)*np.sin(vv),np.cos(vv),color=GOLD,alpha=0.07,linewidth=0)
a.plot(pts[:,0],pts[:,1],pts[:,2],color=BLUE,lw=1.4)
a.scatter(*pts[-1],color=BLUE,s=30)
dg=np.ones(3)/math.sqrt(3); a.plot([0,dg[0]],[0,dg[1]],[0,dg[2]],color=GOLD,lw=1.5,ls='--')
for i,lab in enumerate(['x: end digit 1','y: end digit 7','z: end digit 9']):
    e=np.zeros(3); e[i]=1; a.plot([0,e[0]],[0,e[1]],[0,e[2]],color=GREY,lw=0.8); a.text(*(1.08*e),lab,color=FG,fontsize=8)
a.set_axis_off(); a.view_init(15,-56); a.set_box_aspect((1,1,1))
a.set_title('The twin chain in the ball (twin starts 11 to 10^6)\nblue: the chain; gold: the light sphere and the cube diagonal',color=FG,fontsize=10)
save(f,'f1_chain_ball.png')

# F2 the turn to 1e12, and the readout if the tilt dies
rows=list(csv.DictReader(open(S+'swarm/precision/out/walk_1e12.csv')))
X=np.array([float(r['X']) for r in rows]); T=np.array([float(r['turn_deg']) for r in rows]); R=np.array([float(r['turn_if_tilt_dies_deg']) for r in rows])
m=X>=1e4
f,a=plt.subplots(figsize=(8,4.4))
a.semilogx(X[m],T[m],color=BLUE,lw=1.8,label='measured frame turn')
a.semilogx(X[m],R[m],color=GOLD,lw=1.4,label='readout: turn if the tilt dies')
a.axhline(12.4651,color=GOLD,ls=':',lw=1); a.text(3e10,12.52,'12.4651°',color=GOLD)
for x,t in [(1e9,12.2695),(1e10,12.2969),(1e11,12.3197),(1e12,12.3442)]: a.plot(x,t,'o',color=BLUE,ms=4)
a.set_ylim(9,13); a.set_xlabel('twin starts up to'); a.set_ylabel('degrees'); a.legend(loc='lower right'); a.set_title('The frame turn of the twin chain, measured to 10^12')
save(f,'f2_turn_1e12.png')

# F3 the thread cut prime by prime, and by every prime (digit 1, 1e8-1e9)
P=['5','7','11','13','17','19','23','all\n(≤1000)']; v=[0.675,-0.905,-1.074,-1.158,-0.965,-0.971,-0.741,-0.939]
f,a=plt.subplots(figsize=(8,4.2))
a.axhspan(-0.924-2*0.041,-0.924+2*0.041,color=BLUE,alpha=0.25,label='real twins, 10^8 to 10^9 (±2 se)')
a.plot(range(7),v[:7],'o-',color=GREY,label='screw cut by primes up to P')
a.plot(7,v[7],'D',color=GOLD,ms=9,label='screw cut by every prime (Hardy–Littlewood product)')
a.axhline(0,color=GREY,lw=0.6); a.set_xticks(range(8)); a.set_xticklabels(P); a.set_xlabel('largest prime cutting the thread')
a.set_ylabel('digit-1 tilt × mean gap'); a.legend(fontsize=8,loc='upper right'); a.set_title('Which tooth form makes the tilt')
save(f,'f3_thread_cut.png')

# F4 tilt predicted vs real per decade
dec=['10^5–6','10^6–7','10^7–8','10^8–9','10^9–10','10^10–11','10^11–12']
pred=np.array([[-0.947,0.93,0.016],[-0.942,0.88,0.062],[-0.937,0.842,0.095],[-0.939,0.82,0.119],[-0.945,0.809,0.136],[-0.951,0.806,0.145],[-0.955,0.806,0.15]])
real=np.array([[-1.344,0.654,0.691],[-1.05,0.429,0.621],[-0.83,0.725,0.105],[-0.924,0.839,0.085]]); se=np.array([[0.625,0.955,0.654],[0.246,0.422,0.461],[0.168,0.303,0.233],[0.041,0.034,0.054]])
walk=np.array([[-0.915,0.718,0.198],[-0.957,0.744,0.213],[-0.939,0.73,0.209]])
f,a=plt.subplots(figsize=(8.5,4.6)); x=np.arange(7)
cols=[RED,GREEN,'#b48ee0']; names=['digit 1','digit 7','digit 9']
for j in range(3):
    a.plot(x,pred[:,j],'-',color=cols[j],lw=1.6,label=names[j]+' predicted')
    a.errorbar(x[:4]+0.06*(j-1),real[:,j],yerr=2*se[:,j],fmt='o',color=cols[j],ms=5,capsize=2)
    a.plot(x[4:]+0.06*(j-1),walk[:,j],'s',color=cols[j],ms=5,mfc='none')
a.axhline(0,color=GREY,lw=0.6); a.set_xticks(x); a.set_xticklabels(dec,fontsize=9); a.set_ylabel('tilt × mean gap')
a.set_title('End-digit tilt: every-prime prediction (lines) against twins (dots ±2 se; squares: 10^12 walk)'); a.legend(fontsize=8,ncol=3,loc='upper center',bbox_to_anchor=(0.5,-0.12))
save(f,'f4_tilt_pred_real.png')

# F5 Platonic arm sets: predicted |P| vs measured slope, and the turn
names5=['cube = octahedron','tetrahedron faces','icosahedron vertices','dodecahedron vertex']
gam=[90,109.47,63.43,41.81]; Pp=[0.57735,0.33333,0.79465,0.91117]; meas=[0.57729,0.33271,0.79465,0.91117]; turn=[12.27,19.62,7.45,4.62]
g=np.linspace(20,120,300); Pg=np.sqrt(np.clip((1+2*np.cos(np.radians(g)))/3,0,None))
f,(a,b)=plt.subplots(1,2,figsize=(10,4))
a.plot(g,Pg,color=GOLD,label='|P| = √((1+2cos γ)/3)'); a.plot(gam,meas,'o',color=BLUE,ms=7,label='measured slope d/L to 10^9')
for gg,mm,nn in zip(gam,meas,names5): a.annotate(nn,(gg,mm),textcoords='offset points',xytext=((-105,4) if gg>100 else (5,6)),fontsize=8,color=FG)
a.set_xlabel('angle γ between arms (degrees)'); a.set_ylabel('endpoint slope'); a.legend(fontsize=8)
b.bar(range(4),turn,color=BLUE); b.set_xticks(range(4)); b.set_xticklabels(['cube','tetra','icosa','dodeca']); b.set_ylabel('frame turn at 10^9 (degrees)')
b.set_title('weaker lock, larger turn',fontsize=10)
save(f,'f5_platonic.png')

# F6 the wall at any arm angle
g=np.linspace(1,179,400); G2=1/(1+np.sin(np.radians(g)))
f,a=plt.subplots(figsize=(7,4))
a.plot(g,G2,color=GOLD,lw=2,label='wall: Γ² = 1/(1 + sin γ)')
a.plot(90,0.5,'o',color=GOLD); a.text(92,0.52,'Γ² = ½ (perpendicular arms)',color=FG,fontsize=9)
a.axhline(0.068,color=BLUE,ls='--'); a.text(5,0.08,'largest single twin step: 17→29, Γ² = 0.068',color=BLUE,fontsize=9)
a.set_xlabel('angle γ between the two step directions'); a.set_ylabel('Γ² for equal steps'); a.set_ylim(0,1.05); a.legend()
a.set_title('Where two equal steps stop composing into a rotation')
save(f,'f6_wall.png')

# F7 scaled gaps: the shrinking ruler
q=np.array([[0.341,0.748,1.406,2.168],[0.328,0.735,1.35,2.207],[0.324,0.728,1.38,2.233],[0.319,0.712,1.378,2.242]])
ex=[0.288,0.693,1.386,2.303]; dl=['10^5–6','10^6–7','10^7–8','10^8–9']
f,a=plt.subplots(figsize=(7.5,4))
for j,lab in enumerate(['25%','50%','75%','90%']):
    a.plot(range(4),q[:,j]/ex[j],'o-',color=[BLUE,GREEN,GOLD,RED][j],label=lab+' point')
a.axhline(1,color=GREY,ls=':'); a.text(3.05,1.003,'pure-random limit',color=GREY,fontsize=8)
a.set_xticks(range(4)); a.set_xticklabels(dl); a.set_ylabel('scaled-gap percentile ÷ random limit'); a.legend(fontsize=8)
a.set_title('Gaps in units of the local mean gap: drifting slowly toward the random shape')
save(f,'f7_scaled_gaps.png')

# F8 connection energy between the two views
Xn=[1e5,1e6,1e7,1e8,1e9,1e10,1e11,1e12]; Nv=[0.08863,0.117108,0.124293,0.126319,0.127306,0.127773,0.128146,0.128533]
f,a=plt.subplots(figsize=(7.5,4))
a.semilogx(Xn,Nv,'o-',color=GOLD,lw=1.8); a.axhline(0.130,color=GOLD,ls=':',lw=1); a.text(1.3e5,0.1305,'≈ 0.130 if β levels near 58° (estimate)',color=GOLD,fontsize=9)
a.set_xlabel('twin starts up to'); a.set_ylabel('N = ‖[L,L*]‖ / ‖L‖²'); a.set_ylim(0.08,0.135)
a.set_title('Connection energy between the forward and reversed views')
save(f,'f8_connection_energy.png')
print('ok', len(pts))
