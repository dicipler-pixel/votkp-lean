"""Create the Fr threshold and relative binding figure from the checked run outputs."""
import csv
import json
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.ticker import MultipleLocator

here=Path(__file__).parent
rad=list(csv.DictReader((here/'allelectron_summary.csv').open()))
md=list(csv.DictReader((here/'model_comparisons.csv').open()))
eom=[json.loads(l) for l in (here/'eom_runs.jsonl').read_text().splitlines()]
def radial(rel,dft):
    return next(r for r in rad if r['atom']=='Fr' and r['dx']=='0.00625' and r['rel']==str(rel) and r['functional']==dft)
def published(starts):
    return float(next(row for row in md if row['source'].startswith(starts))['IE2_eV'])

ground=float(radial(2,'PBE')['IE2_eV']); upper=float(radial(2,'PBE')['upper_threshold_eV'])
pz=float(radial(2,'PZ')['IE2_eV']); pzup=float(radial(2,'PZ')['upper_threshold_eV'])
roots=next(row['IE2_roots_eV'] for row in eom if row['atom']=='Fr' and row['virtual_budget']==60)
frozen=md[0]; wall=float(frozen['IE2_eV'])-float(frozen['margin_wall_eV']); rival=float(frozen['IE2_eV'])-float(frozen['margin_rival_eV'])
navy='#183447'; teal='#00746e'; amber='#a34716'; deep='#324051'; grey='#63727a'
fig,(ax,bx)=plt.subplots(1,2,figsize=(12.4,5.2),gridspec_kw={'width_ratios':[1.57,1]})
fig.subplots_adjust(left=.19,right=.975,bottom=.2,top=.79,wspace=.44)
fig.suptitle('Francium’s ground and excited ionization thresholds',x=.045,y=.973,ha='left',fontsize=19,weight='bold',color=navy)
fig.text(.045,.892,'A future ground-state threshold measurement can test the forecast. All individual points shown below are estimates or calculations.',fontsize=10,color=deep)
ax.set_title('Absolute threshold from Fr⁺ (eV)',loc='left',fontsize=12,weight='bold',color=navy,pad=12)
models=[('NIST semiempirical',22.4,None),('Family continuation',float(frozen['IE2_eV']),None),('de Farias, lattice (2018)',published('de Farias Mendeleev'),None),('de Farias, alkali fit (2018)',published('de Farias Chem'),None),('Groningen X2C (2016)',published('van der Schoor X2C'),None),('Radial PBE',ground,upper),('Radial PZ',pz,pzup),('ECP IP-EOM-CCSD',roots[0],roots[4])]
for i,(name,lo,hi) in enumerate(models):
    y=len(models)-1-i
    if i==0: ax.errorbar(lo,y,xerr=1.9,fmt='none',ecolor=grey,lw=1.6,capsize=4,zorder=2)
    if hi: ax.plot([lo,hi],[y,y],color='#a8b4b6',lw=1.4,zorder=2)
    ax.scatter(lo,y,s=50,c=teal if i>=4 else grey,zorder=4,edgecolor='white',linewidth=.7)
    if hi:ax.scatter(hi,y,s=57,marker='D',c=amber,zorder=4,edgecolor='white',linewidth=.7)
ax.axvspan(wall,rival,color='#ad4f61',alpha=.35,zorder=0)
ax.axvline(wall,color='#8e3650',lw=.8,zorder=1)
ax.set_xlim(19.7,26.4);ax.set_ylim(-.5,len(models)-.4)
ax.set_yticks(range(len(models)),[r[0] for r in models[::-1]])
ax.xaxis.set_major_locator(MultipleLocator(1));ax.grid(axis='x',which='major',color='#dce4e7',linewidth=.7)
ax.set_xlabel('Ionization energy (eV)')
ax.legend(handles=[Line2D([],[],color='#8e3650',lw=4,label='Disagreement interval'),Line2D([],[],marker='D',ls='',color=amber,label='Excited ²P₁/₂ channel')],loc='upper left',bbox_to_anchor=(-.24,-.15),frameon=False,ncol=2,fontsize=8)
bx.set_title('Self-consistent Fr peel ratio',loc='left',fontsize=12,weight='bold',color=navy,pad=12)
for func,col,marker in [('PBE',teal,'o'),('PZ',amber,'s')]:
    zz=[float(radial(i,func)['ratio']) for i in range(3)]
    bx.plot(range(3),zz,color=col,marker=marker,lw=2.5,ms=6,label=func,zorder=3)
bx.axhspan(wall/4.0727411,rival/4.0727411,color='#ad4f61',alpha=.4)
bx.axhline(wall/4.0727411,color='#8e3650',lw=.8)
bx.set_ylim(4.75,6.35);bx.set_xlim(-.20,2.19);bx.set_xticks([0,1,2],['Nonrel.','Scalar rel.','Full Dirac']);bx.grid(axis='y',color='#dce4e7',lw=.7)
bx.set_ylabel('IE₂ / IE₁');bx.legend(frameon=False,loc='lower left',bbox_to_anchor=(-.06,-.26),ncol=2,fontsize=8)
for a in (ax,bx):
    a.spines[['right','top']].set_visible(False);a.spines[['bottom','left']].set_color('#9aa9ad');a.tick_params(axis='both',labelsize=9,color=grey)
fig.savefig(here/'francium_thresholds.png',dpi=160,facecolor='white')
fig.savefig(here/'francium_thresholds.pdf',facecolor='white')
