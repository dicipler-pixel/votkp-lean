"""Plot the mass ordering and detailed charge crossing, using existing output CSVs."""
import csv
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np

HERE=Path(__file__).resolve().parent
def load(path):
    with path.open() as f:
        return list(csv.DictReader(f))
raw=load(HERE.parent/'materials/ho_dy_decay.csv')
direct=load(HERE/'direct_trap_bounds.csv')
def values(rows,key):
    return np.array([float(r[key])/1000 for r in rows])
q=np.array([int(r['q']) for r in raw])
mid=values(raw,'Q_Ho_minus_Dy_eV')
lo=values(raw,'Q_lower_eV')
hi=values(raw,'Q_upper_eV')
blue='#215375'
rust='#b44420'
green='#277866'
plt.rcParams.update({'svg.fonttype':'none','svg.hashsalt':'ho-dy-charge-20261121','font.family':'DejaVu Sans','font.size':10})
fig,(left,right)=plt.subplots(1,2,figsize=(10.2,4.7),gridspec_kw={'width_ratios':[1.6,1]},layout='constrained')
for ax in (left,right):
    ax.axhline(0,color='#28332e',linewidth=0.9)
    ax.spines[['top','right']].set_visible(False)
    ax.grid(axis='y',alpha=0.18)
    ax.set_xlabel('Ionic charge q')
    ax.set_ylabel('Ho minus Dy mass energy (keV)')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
left.fill_between(q,lo,hi,color=blue,alpha=.19,label='Published input widths')
left.plot(q,mid,color=blue,lw=2,label='Neutral-mass anchor')
left.scatter([56,57,66],mid[[56,57,66]],s=25,color=rust,zorder=3)
left.annotate('Bare Dy',xy=(66,mid[66]),xytext=(50,-39),arrowprops={'arrowstyle':'->','color':'#405349'},fontsize=9)
left.set_title('All 67 charge states',loc='left')
left.legend(frameon=False,loc='lower left',fontsize=8)
for k in (55,56,57,58):
    right.errorbar(k-.07,mid[k],yerr=[[mid[k]-lo[k]],[hi[k]-mid[k]]],color=blue,fmt='o',capsize=3)
    r=next(r for r in direct if r['q']==str(k) and r['anchor_q']=='40')
    lower=float(r['lower_eV'])/1000
    upper=float(r['upper_eV'])/1000
    right.errorbar(k+.07,(lower+upper)/2,yerr=(upper-lower)/2,color=green,fmt='s',capsize=3)
right.plot([],[],marker='o',color=blue,ls='none',label='Neutral-mass anchor')
right.plot([],[],marker='s',color=green,ls='none',label='Direct trap ratio at 40+')
right.legend(frameon=False,fontsize=8,loc='center right')
right.set_xticks([55,56,57,58])
right.set_title('Change between 56+ and 57+',loc='left')
fig.suptitle('Mass ordering of holmium-163 and dysprosium-163',fontsize=15,fontweight='bold',x=.06,ha='left')
fig.savefig(HERE/'charge_crossing.svg',metadata={'Date':None})
