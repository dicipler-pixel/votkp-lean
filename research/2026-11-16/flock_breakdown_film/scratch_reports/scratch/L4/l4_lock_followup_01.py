# SCRIPT: L4-LOCK-FOLLOWUP-01
# The one cell that met kill lines 1 and 2: N=7, clocks equal, torque 1, gamma 0.1, sign swap, pair (2,5) = balls C (+J arm) and F (-J arm), mirror images of each other.
# KILL LINE (written before the runs): the call stands only if the pair (2,5) meets kill line 1 (rates within 0.02 in both last windows, phase-difference s.d. < 0.5 rad over the last half,
# matching torque-0 run s.d. > 0.5 rad) and both balls carry weight > 0.02 for half the samples, in at least 3 of these 4 variants: (V1) T = 800, (V2) gamma = 0.08, (V3) gamma = 0.12, (V4) kick in ball D (index 3) instead of A.
# Otherwise it is one cell out of 384 and is not called locking. The same four variants are also run with sign asis for contrast.
import subprocess, json
def run(P):
    return json.loads(subprocess.run(['node','l4_sync_02.js',json.dumps(P)],capture_output=True,text=True).stdout)
base=dict(N=7,clocks='equal',torque=1,gamma=0.1,gloss=0,sign='swap',T=400,h=0.005)
variants={'V0 (the original cell)':{}, 'V1 T=800':dict(T=800),'V2 gamma=0.08':dict(gamma=0.08),'V3 gamma=0.12':dict(gamma=0.12),'V4 kick in D':dict(source=3)}
for sign in ('swap','asis'):
    print('SIGN',sign)
    hits=0
    for name,v in variants.items():
        P=dict(base,sign=sign,**v); on=run(P); off=run(dict(P,torque=0))
        po=[q for q in off['pairs'] if q['i']==2 and q['j']==5][0]; pn=[q for q in on['pairs'] if q['i']==2 and q['j']==5][0]
        ok=pn['dr'][0]<0.02 and pn['dr'][1]<0.02 and pn['sd']<0.5 and po['sd']>0.5 and on['heavy'][2]>=0.5 and on['heavy'][5]>=0.5
        if name!='V0 (the original cell)' and ok: hits+=1
        print('  %-24s torque1: rate gaps %.4f %.4f, sd %.3f, heavy C %.2f F %.2f | torque0 sd %.3f | r %.3f surrogate %.3f | %s'%(name,pn['dr'][0],pn['dr'][1],pn['sd'],on['heavy'][2],on['heavy'][5],po['sd'],on['rMean'],on['surMean'],'MEETS' if ok else 'fails'))
    print('  variants V1-V4 meeting the line:',hits,'of 4 ->','call stands' if hits>=3 else 'NOT called locking')
