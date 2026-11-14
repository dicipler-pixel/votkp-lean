# SCRIPT: ONE-BALL-FIG-CELLS-01 (draws the checked law: angle between neighbour walls inside the wall, gap layer past it)
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt, math
z=np.linspace(1.001,13,2000); q=(z-1)**2/(4*z); W=3+2*math.sqrt(2)
fig,ax=plt.subplots(figsize=(11,5.2),facecolor='#0b0f17'); ax.set_facecolor('#0b0f17')
ins=z<W; ax.plot(z[ins],np.degrees(np.arccos(q[ins])),color='#ff6fae',lw=2.4,label='inside the wall: walls of neighbouring cells cross at angle α, cos α = q')
ax2=ax.twinx(); ax2.plot(z[~ins],np.arccosh(q[~ins]),color='#f2f2f2',lw=2.4,label='past the wall: gap layer δ between the cells, cosh δ = q')
ax.axvline(W,color='#63d3ff',ls='--',lw=1); ax.text(6.9,60,'gold: n cells meet round each edge',color='#f2c14e',fontsize=9.5); ax.text(W+0.08,86,'wall  z = 3 + 2√2',color='#63d3ff',fontsize=10)
zof=lambda c:(math.sqrt(c)+math.sqrt(1+c))**2
for n,ok in ((5,1),(6,1),(8,1),(7,0),(10,0),(12,0)):
    zz=zof(math.cos(2*math.pi/n)); a=360/n
    ax.plot([zz],[a],'o',ms=9,color='#f2c14e' if ok else 'none',mec='#f2c14e',mew=1.6)
    ax.annotate(f'n = {n},  z = {zz:.4f}',(zz,a),xytext=(zz-1.75,a-6.5),color='#f2c14e',fontsize=8.5)
for zz,nm in ((3,'z = 3'),(5,'z = 5'),(7,'z = 7'),(11,'z = 11')):
    qq=(zz-1)**2/(4*zz)
    if zz<W: ax.plot([zz],[math.degrees(math.acos(qq))],'s',color='#8fd3ff',ms=6); ax.annotate(f'{nm}: α = {math.degrees(math.acos(qq)):.2f}°',(zz,math.degrees(math.acos(qq))),xytext=(zz+0.2,math.degrees(math.acos(qq))+4),color='#8fd3ff',fontsize=8.5)
    else: ax2.plot([zz],[math.acosh(qq)],'s',color='#8fd3ff',ms=6); ax2.annotate(f'{nm}: δ = {math.acosh(qq):.4f}',(zz,math.acosh(qq)),xytext=(zz+0.15,math.acosh(qq)-0.12),color='#8fd3ff',fontsize=8.5)
ax.set_xlabel('step ratio z of one edge of the tree',color='#dfe5f2'); ax.set_ylabel('angle α between neighbour walls (degrees)',color='#ff6fae'); ax2.set_ylabel('gap layer δ (hyperbolic length)',color='#f2f2f2')
ax.set_ylim(0,95); ax2.set_ylim(0,1.9); ax.set_xlim(1,13)
for a in (ax,ax2):
    a.tick_params(colors='#aab4cc'); [s.set_color('#2a3550') for s in a.spines.values()]
h1,l1=ax.get_legend_handles_labels(); h2,l2=ax2.get_legend_handles_labels()
ax.legend(h1+h2,l1+l2,loc='center right',facecolor='#141b2b',edgecolor='#2a3550',labelcolor='#dfe5f2',fontsize=9)
ax.set_title('One ball, six arms: overlap inside the wall, gap past it.  Filled gold: lattice confirmed to depth 5.  Open gold: order of the square confirmed only.',color='#ffd166',fontsize=10)
plt.tight_layout(); plt.savefig('fig_cells.png',dpi=130,facecolor='#0b0f17')
