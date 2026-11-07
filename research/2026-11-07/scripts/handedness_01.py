# SCRIPT: HANDEDNESS-01
# Why do element tracks wind one way? Candidate: Foster's reactance theorem (lossless passive response: reactance rises
# with frequency, so the Smith locus turns clockwise as frequency rises). With loss it is no longer guaranteed.
# Check on model media: count the direction of the track Gamma(omega) = (1-N)/(1+N), N = sqrt(eps), by its turning sense.
import numpy as np
w=np.linspace(1.5,3.3,400)  # eV, the visible band
def sense(eps):
    N=np.sqrt(eps.astype(complex)); N=np.where(N.imag<0,-N,N); G=(1-N)/(1+N)
    dz=np.diff(G); m=(G[1:]+G[:-1])/2; return np.sign(np.sum(m.real*dz.imag-m.imag*dz.real))  # +1 counter-clockwise as w rises
cases={}
for wp in (5,9,15):
    for g in (0.02,0.2,1.0): cases['Drude wp=%g gamma=%g'%(wp,g)]=1-wp**2/(w*(w+1j*g))
for w0 in (1.0,2.4,4.5):
    for g in (0.05,0.5): cases['Lorentz w0=%g gamma=%g'%(w0,g)]=2.0+3.0/(w0**2-w**2-1j*g*w)
for k,e in cases.items(): print('%-28s  %s'%(k,{1:'counter-clockwise',-1:'clockwise',0:'flat'}[int(sense(e))]),'(as frequency rises)')
