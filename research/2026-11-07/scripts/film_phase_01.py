# SCRIPT: FILM-PHASE-01
# Exploratory. P1: bulk metals the eye matches (CIE 1931 2 deg, D65, CIEDE2000) but whose Smith tracks differ in phase
# (arg Gamma). Put the same transparent film (n = 1.5, thickness 10-300 nm) on each and compute the colours.
# Reading: does the film turn the hidden phase difference back into colour? Compare against the phase-track gap.
import sys, numpy as np, colour
sys.path.insert(0,'/home/claude/votkp_research'); import ri_load
S=ri_load.element_sets(); nonmetal={'B','C','Ge','Se','Si','Te'}
lv=np.arange(380,781,5)/1000.0
cmfs=colour.MSDS_CMFS['CIE 1931 2 Degree Standard Observer']; ill=colour.SDS_ILLUMINANTS['D65']
shape=colour.SpectralShape(380,780,5)
def lab_of(R):
    sd=colour.SpectralDistribution(dict(zip((lv*1000).astype(int),R)))
    XYZ=colour.sd_to_XYZ(sd,cmfs,ill,shape=shape)/100
    return colour.XYZ_to_Lab(XYZ,colour.CCS_ILLUMINANTS['CIE 1931 2 Degree Standard Observer']['D65'])
data={}
for el,d in S.items():
    if el in nonmetal: continue
    o=np.argsort(d['lam']); N=np.interp(lv,d['lam'][o],d['n'][o])+1j*np.interp(lv,d['lam'][o],d['k'][o])
    data[el]=N
def film_R(N,dnm,nf=1.5):
    r01=(1-nf)/(1+nf); r12=(nf-N)/(nf+N); delta=2*np.pi*nf*dnm/(lv*1000)
    r=(r01+r12*np.exp(2j*delta))/(1+r01*r12*np.exp(2j*delta)); return np.abs(r)**2
bulk={el:lab_of(np.abs((1-N)/(1+N))**2) for el,N in data.items()}
phase={el:np.angle((1-N)/(1+N)) for el,N in data.items()}
els=sorted(data); pairs=[]
for i,a in enumerate(els):
    for b in els[i+1:]:
        dE=colour.delta_E(bulk[a],bulk[b],method='CIE 2000')
        if dE<2.0:
            dph=np.degrees(np.mean(np.abs(np.angle(np.exp(1j*(phase[a]-phase[b]))))))
            fe=[colour.delta_E(lab_of(film_R(data[a],t)),lab_of(film_R(data[b],t)),method='CIE 2000') for t in np.arange(10,301,10)]
            pairs.append((a,b,dE,dph,max(fe),np.median(fe)))
print('bulk-matched metal pairs (bulk dE2000 < 2):',len(pairs))
print(' pair     bulk dE   mean phase gap (deg)   film dE max   film dE median')
for p in sorted(pairs,key=lambda x:x[3]): print(f' {p[0]:>2}-{p[1]:<2}   {p[2]:6.2f}      {p[3]:8.2f}            {p[4]:8.2f}       {p[5]:8.2f}')
if len(pairs)>3:
    from scipy.stats import spearmanr
    r=spearmanr([p[3] for p in pairs],[p[4] for p in pairs]); print('\nrank link phase gap -> film colour gap (max over thickness): rho =',round(r.correlation,3),' p =',round(r.pvalue,4))
