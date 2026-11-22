# SCRIPT: MAKE_FIGS_WHAT_THE_PEEL_KEEPS_V1_2
import json, math, numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
P='/home/claude/votkp-lean/research/2026-11-20-element-paper-loop-wall/ptable/ptable_data.json'
OUT='/home/claude/paper_v12/figs/'
D=json.load(open(P)); E=D['elements']
W=3+2*math.sqrt(2)
RED='#b8323c'; BLUE='#2b5d9b'; GOLD='#c98a12'; GREY='#7a7a7a'; GREEN='#2f8f5b'; PURP='#6b4c9a'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'savefig.dpi':220})
g=lambda z:(z-1)/(z+1)

# Fig 1: the wall from geometry -- equal faces at right angles; the two-face boundary u+v=1 and the Smith disc
fig,ax=plt.subplots(1,2,figsize=(10,4.6))
a=ax[0]; t=np.linspace(0,2*np.pi,400)
a.plot(np.cos(t),np.sin(t),color=GREY,lw=1); a.plot(np.cos(t)/math.sqrt(2),np.sin(t)/math.sqrt(2),color=RED,lw=2)
a.axhline(0,color='#ccc',lw=.6); a.axvline(0,color='#ccc',lw=.6)
pts=[]
for e in E:
  for s in e['steps']: pts.append(g(s['z']))
pts=np.array(pts)
a.scatter(pts,np.zeros_like(pts),s=4,color=BLUE,alpha=.35,zorder=3)
outs=[(e['sym'],c['z']) for e in E for c in e['cores'] if c['out'] and c['core'] and c['step']==min([cc['step'] for cc in e['cores']])]
for e in E:
  for s in e['steps']:
    if s['out']: a.scatter([g(s['z'])],[0],s=26,color=RED,zorder=4)
a.annotate('wall circle  $|\\Gamma|^2=\\frac{1}{2}$',xy=(0.5,0.5),xytext=(0.15,0.85),color=RED,fontsize=9,arrowprops=dict(arrowstyle='-',color=RED,lw=.7))
a.text(0.72,-0.12,'8 outside',color=RED,fontsize=9); a.text(-0.95,0.08,'3,570 ordinary steps on the real ray',fontsize=8,color=BLUE)
a.set_aspect('equal'); a.set_xlim(-1.08,1.08); a.set_ylim(-1.08,1.08); a.set_xticks([-1,-.5,0,.5,1]); a.set_yticks([])
a.set_title('Smith disc: $\\Gamma=(z-1)/(z+1)$',fontsize=10)
b=ax[1]; u=np.linspace(0,1,200)
b.fill_between(u,0,1-u,color='#e8eef7'); b.plot(u,1-u,color=RED,lw=2)
b.text(0.18,0.2,'loop closes\n$\\Gamma_a^2+\\Gamma_b^2<1$',fontsize=9,color=BLUE); b.text(0.62,0.72,'loop open\n$\\sinh h_a\\,\\sinh h_b>1$',fontsize=9,color=RED)
b.scatter([.5],[.5],color=RED,zorder=4); b.annotate('equal faces: $z=3+2\\sqrt{2}$',xy=(.5,.5),xytext=(.55,.33),fontsize=9,arrowprops=dict(arrowstyle='->',lw=.7))
gc=g(6.079534)**2; gn=g(5.639665)**2
b.scatter([gc],[gn],color=GOLD,zorder=5,s=22); b.annotate('carbon with nitrogen',xy=(gc,gn),xytext=(0.05,0.62),fontsize=8,color=GOLD,arrowprops=dict(arrowstyle='->',lw=.6,color=GOLD))
b.set_xlim(0,1); b.set_ylim(0,1); b.set_xlabel('$\\Gamma_a^2$'); b.set_ylabel('$\\Gamma_b^2$'); b.set_aspect('equal')
b.set_title('Two faces at a right angle',fontsize=10)
fig.tight_layout(); fig.savefig(OUT+'fig01_wall.png'); plt.close(fig)

# Fig 2: all ordinary steps, Gamma^2 vs Z, wall line, eight outside labelled
fig,a=plt.subplots(figsize=(10,4))
for e in E:
  for s in e['steps']:
    a.scatter(e['Z'],s['g2'],s=5,color=RED if s['out'] else BLUE,alpha=.9 if s['out'] else .25,zorder=3 if s['out'] else 2)
    if s['out']: a.annotate(f"{e['sym']}$_{s['k']}$",(e['Z'],s['g2']),xytext=(3,3),textcoords='offset points',fontsize=8,color=RED)
a.axhline(.5,color=RED,lw=1.3); a.text(86,.505,'wall $\\Gamma^2=\\frac{1}{2}$',color=RED,fontsize=9,va='bottom',ha='right')
a.set_xlabel('atomic number $Z$'); a.set_ylabel('$\\Gamma^2$ of each ordinary step'); a.set_xlim(0,86); a.set_ylim(0,.9)
a.set_title('3,570 ordinary steps, hydrogen to astatine: eight cross, every one a first noble-gas core opening',fontsize=10)
fig.tight_layout(); fig.savefig(OUT+'fig02_steps.png'); plt.close(fig)

# Fig 3: anion rung: omega/eta
fig,a=plt.subplots(figsize=(10,4))
for e in E:
  an=e['anion']
  if an and an.get('z0'):
    oe=1/(2*g(an['z0'])**2)
    a.scatter(e['Z'],oe,s=18,color=RED if oe<1 else BLUE,zorder=3)
    if e['sym'] in ('Ag','Si','Au','Pt','Ir','At','Po','O','F','Cl','Br','I','S','Se','Te','Bi','Pb','Os','H','Ca','Sr','Ba'):
      a.annotate(e['sym'],(e['Z'],oe),xytext=(2,3),textcoords='offset points',fontsize=7.5)
a.axhline(1,color=RED,lw=1.3); a.set_yscale('log'); a.text(1,1.05,'wall: electrophilicity = hardness, $\\omega=\\eta$',color=RED,fontsize=9)
a.set_xlabel('atomic number $Z$'); a.set_ylabel('$\\omega/\\eta = 1/(2\\Gamma_0^2)$'); a.set_xlim(0,86)
a.set_title('The anion rung (the stone): red below the line is outside the wall',fontsize=10)
fig.tight_layout(); fig.savefig(OUT+'fig03_anion.png'); plt.close(fig)

# Fig 4: window number line (staggered labels)
fig,a=plt.subplots(figsize=(10,3.6))
lo,hi=5.8079020598,5.8665387761
a.axvspan(lo,hi,color='#f1e7d0'); a.axhline(0,color='#888',lw=.8)
marks=[(lo,lo,'silver anion\n5.80790',GREY,1.0),(hi,hi,'silicon anion\n5.86654',GREY,1.0),
(W,5.8205,'wall $3+2\\sqrt{2}$ = 5.828427',RED,1.55),
(5.8268808732,5.8150,'oxygen O$^{2+}$ 4s $J{=}0$',BLUE,-1.0),(5.8278703392,5.8215,'$J{=}1$',BLUE,-1.6),(5.8303470087,5.8300,'$J{=}2$',BLUE,-1.0),
(5.832602195,5.8395,'scandium–tin hydrogen-like pair',PURP,0.95),(35/6,5.8385,'35/6 bench',GOLD,-1.6),(5.8371,5.8500,'six midpoint rivals',GREY,1.55)]
for x,xl,l,c,y in marks:
  a.scatter([x],[0],color=c,zorder=4,s=20)
  a.annotate(l,xy=(x,0),xytext=(xl,y),color=c,fontsize=8.5,ha='center',va='center',arrowprops=dict(arrowstyle='-',color=c,lw=.8))
a.set_ylim(-2.0,2.0); a.set_xlim(5.803,5.871); a.set_yticks([]); a.spines['left'].set_visible(False)
a.set_xlabel('forward ratio $z$'); a.set_title('Every classification from hydrogen to astatine survives only inside the shaded window; the geometry picks one point in it',fontsize=10)
fig.tight_layout(); fig.savefig(OUT+'fig04_window.png'); plt.close(fig)

# Fig 5: face apex and orbital survival
z=np.linspace(1,12,500); a_=np.tanh(np.log(z)/4); t_=1-a_**2
fig,a=plt.subplots(figsize=(8,4))
a.plot(z,t_**3,color=BLUE,label='1s: $(1-a^2)^3$'); a.plot(z,t_**3*(1-3*a_**2)**2,color=GOLD,label='2s: $t^3(1-3a^2)^2$'); a.plot(z,t_**5,color=GREEN,label='2p: $t^5$')
a.axvline(W,color=RED,lw=1.2); a.axhline(.5,color='#bbb',lw=.8,ls='--'); a.axvline(4,color=GREY,lw=.8,ls=':')
a.text(W+.1,.95,'wall',color=RED,fontsize=9); a.text(4.05,.03,'$z=4$',fontsize=8,color=GREY)
a.set_xlabel('energy ratio $z$'); a.set_ylabel('probability the orbital survives'); a.legend(frameon=False,fontsize=9)
a.set_title('Face apex $a=\\tanh(\\ln z/4)$ as an orbital survival probability',fontsize=10)
fig.tight_layout(); fig.savefig(OUT+'fig05_orbital.png'); plt.close(fig)

# Fig 6: colour line + Elizabeth ladder
fig,ax=plt.subplots(1,2,figsize=(10,4),gridspec_kw={'width_ratios':[1.5,1]})
a=ax[0]; m=[(e['sym'],e['optic']['mean_R'],e['optic']['metal']) for e in E if e['optic']]
m.sort(key=lambda x:x[1])
for i,(s,r,met) in enumerate(m):
  a.bar(i,r,color=GOLD if met else BLUE)
a.axhline(.5,color=RED,lw=1.3); a.set_xticks(range(len(m))); a.set_xticklabels([x[0] for x in m],rotation=90,fontsize=6.5)
a.set_ylabel('visible-average $|\\Gamma|^2$ (reflectance)'); a.set_title('35 metals (gold) above one half, 6 non-metals (blue) below',fontsize=10)
b=ax[1]; zs=[1,2,4,6,8]; 
for zz in zs:
  gg=g(zz)**2; b.scatter([zz],[gg],color=RED if gg>.5 else BLUE,s=30,zorder=3); b.annotate(f'{zz}:1  $\\Gamma^2$={gg:.2f}',(zz,gg),xytext=(4,-10),textcoords='offset points',fontsize=8)
zz=np.linspace(1,9,200); b.plot(zz,g(zz)**2,color=GREY,lw=1); b.axhline(.5,color=RED,lw=1.2); b.axvline(W,color=RED,lw=.8,ls=':')
b.set_xlabel('her ratio, read as a peel step $z$'); b.set_ylabel('$\\Gamma^2$'); b.set_title("Elizabeth Johnson's gap ladder",fontsize=10)
fig.tight_layout(); fig.savefig(OUT+'fig06_colour.png'); plt.close(fig)

# Fig 7: two-face forms agree only at t=1/2
fig,ax=plt.subplots(1,3,figsize=(10,3.4))
for a,tt in zip(ax,(0.4,0.5,0.6)):
  x=np.linspace(0,1,400)
  ys=2*tt-x; k=(tt/(1-tt))**2
  yp=k/(x/(1-x)+k)  # y/(1-y)=k/(x/(1-x))
  a.plot(x,np.clip(ys,0,1),color=BLUE,label='sum form'); a.plot(x[1:],yp[1:],color=RED,ls='--',label='product form')
  a.set_xlim(0,1); a.set_ylim(0,1); a.set_aspect('equal'); a.set_title(f'face threshold $\\Gamma^2={tt}$',fontsize=9)
  a.set_xlabel('$\\Gamma_a^2$')
ax[0].set_ylabel('$\\Gamma_b^2$'); ax[0].legend(frameon=False,fontsize=8)
fig.suptitle('The sum and product forms of the two-face rule are one curve only at $\\Gamma^2=\\frac{1}{2}$',fontsize=10)
fig.tight_layout(); fig.savefig(OUT+'fig07_twoface.png'); plt.close(fig)

# Fig 8: Ho-Dy mass gap
q=np.array([55,56,57,58]); Q=np.array([1869.406439,1951.406439,-4518.593561,-4393.593561])
fig,a=plt.subplots(figsize=(7,3.6))
a.plot(q,Q/1000,'-o',color=BLUE); a.axhline(0,color=RED,lw=1)
for x,y in zip(q,Q): a.annotate(f'{y/1000:+.3f}',(x,y/1000),xytext=(4,6),textcoords='offset points',fontsize=8)
a.set_xlabel('common ionic charge $q$'); a.set_ylabel('$Q(q)=[M_{Ho}-M_{Dy}]c^2$ (keV)')
a.set_title('Holmium-163 and dysprosium-163 swap ground-mass order between 56+ and 57+',fontsize=10)
fig.tight_layout(); fig.savefig(OUT+'fig08_hody.png'); plt.close(fig)
print('ok')

# Fig 9: opening map by core family
fig,a=plt.subplots(figsize=(10,4))
cols={'helium':BLUE,'neon':GREEN,'argon':GOLD,'krypton':PURP,'xenon':'#c0392b'}
for c,col in cols.items():
  xs=[e['Z'] for e in E for cc in e['cores'] if cc['core']==c]; ys=[cc['z'] for e in E for cc in e['cores'] if cc['core']==c]
  a.plot(xs,ys,'-o',ms=3,color=col,lw=1,label=f'{c} core')
  a.annotate(f"{[e['sym'] for e in E for cc in e['cores'] if cc['core']==c][0]} {ys[0]:.2f}",(xs[0],ys[0]),xytext=(4,4),textcoords='offset points',fontsize=8,color=col)
a.axhline(W,color=RED,lw=1.3); a.text(84,W*1.04,'wall $3+2\\sqrt{2}$',color=RED,ha='right',fontsize=9)
a.set_yscale('log'); a.set_xlabel('atomic number $Z$'); a.set_ylabel('core opening ratio $z$'); a.legend(frameon=False,fontsize=8,ncol=5,loc='upper right')
a.set_xlim(0,86); a.set_title('Each core sequence starts outside the wall, crosses inward once, and never comes back out',fontsize=10)
fig.tight_layout(); fig.savefig(OUT+'fig09_openings.png'); plt.close(fig)
print('fig9')
