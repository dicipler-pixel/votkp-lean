# SCRIPT: TWIN-PAPER-FIGURES-02
# New figures for version 2. Every number is read from the run outputs recorded on the branch.
import numpy as np, json, math, matplotlib, re
matplotlib.use('Agg'); import matplotlib.pyplot as plt
BG='#0b0e14'; FG='#e6e1d3'; GOLD='#e8b84a'; BLUE='#4a90e2'; RED='#e0605a'; GREY='#8a8f99'; GREEN='#6cc08b'
plt.rcParams.update({'figure.facecolor':BG,'axes.facecolor':BG,'savefig.facecolor':BG,'text.color':FG,'axes.labelcolor':FG,
 'xtick.color':FG,'ytick.color':FG,'axes.edgecolor':GREY,'font.size':11,'axes.titlesize':12,'legend.facecolor':BG,'legend.edgecolor':GREY})
S='/tmp/claude-0/-home-claude/502f5ad8-acd9-59a2-b5cf-d48e7967cc3a/scratchpad/'
def save(f,n): f.savefig('fig/'+n,dpi=200,bbox_inches='tight'); plt.close(f)
# F9 the first cut: runout before/after the wall and in the first window, against the curvature dial
res=[o for o in json.load(open(S+'swarm/thread/curvature_dial_out.json')) if o['lam']<2]
b=json.load(open(S+'swarm/thread/curvature_dial_b_out.json')); res.append([o for o in b if o['lam']==2.0][0])
lam=[o['lam'] for o in res]
f,(a1,a2)=plt.subplots(1,2,figsize=(11,4.3))
a1.semilogy(lam,[o['early_11_227'] for o in res],'o-',color=GOLD,label='first steps (twin starts 11 to 227)')
a1.semilogy(lam,[o['before'] for o in res],'s-',color=BLUE,label='13 steps before the wall')
a1.semilogy(lam,[o['after'] for o in res],'^--',color=GREY,label='13 steps after the wall')
a1.set_xlabel('curvature dial  (every rapidity × λ)'); a1.set_ylabel('turn runout, degrees (sd, 200 scrambles)'); a1.legend(fontsize=8.5)
a1.set_title('Scrambling the arms: where the turn is set')
a2.loglog([o['wall_start'] for o in res],[o['ratio_before_after'] for o in res],'o',color=BLUE)
for o in res: a2.annotate('λ %.2g'%o['lam'],(o['wall_start'],o['ratio_before_after']),textcoords='offset points',xytext=(5,4),fontsize=8,color=FG)
a2.axhline(1,color=GREY,lw=0.8); a2.axhline(1.5,color=RED,lw=0.8,ls=':'); a2.text(1.5e5,1.6,'kill line 1.5',color=RED,fontsize=8)
a2.set_xlabel('twin start where the walker crosses the wall'); a2.set_ylabel('runout before / after the wall')
a2.set_title('When the wall sits among small steps, it does not bite')
save(f,'f9_first_cut.png')
# F10 the other prime pairs: turn by decade
txt=open(S+'agent_new/f2_families.out').read()
dec=[1e3,1e4,1e5,1e6,1e7,1e8,1e9]
fam={'twins (gap 2)':[15.1974,6.9955,9.8700,11.6199,12.0725,12.2048,12.2690],'cousins (gap 4)':[7.1911,10.4002,11.3167,14.4066,14.7336,14.8448,14.9926],
     'sexy, cube arms (gap 6)':[6.6008,6.9408,6.6336,8.4706,9.1422,9.9835,10.5305],'sexy, octahedron arms':[8.9135,9.0660,9.0564,8.9999,9.0224,9.0115,8.9931]}
for k,v in fam.items(): assert all(('%.4f'%x) in txt for x in v), k   # every value is in the recorded run output
f,a=plt.subplots(figsize=(8,4.4)); cols=[BLUE,GOLD,GREEN,GREY]
for (k,v),c in zip(fam.items(),cols): a.semilogx(dec,v,'o-',color=c,label=k)
a.set_xlabel('largest pair start'); a.set_ylabel('frame turn, degrees'); a.legend(fontsize=9); a.set_title('The frame turn of each prime-pair family')
save(f,'f10_families.png')
print('figures f9, f10 written')
