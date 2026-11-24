# SCRIPT: GAPS-FFT-CHECK-01
# Does float64 FFT convolution distort the cap forms? Recompute A on a small grid with exact direct
# convolution (np.convolve, all terms positive) and compare with the FFT version.
# KILL (written before the run): FFT is the culprit if c^T A c differs by more than 1e-6 relative.
import numpy as np, capgram
from capgram import Engine, C_THEIRS
N=6144
E1=Engine(40,N); A1,_=None,None
E1.gram=Engine.gram.__get__(E1)
import types
def fft_exact(a,b,n): return np.convolve(a,b)[:n]
A_fft,B_fft=np.load(f'gram_k40_N{N}.npy')
capgram.fftmul=lambda a,b,n: np.convolve(a,b)[:n]
E2=Engine(40,N); A2,B2=E2.gram()
c=C_THEIRS
print('I fft %.12e exact %.12e rel %.2e'%(c@A_fft@c,c@A2@c,abs(c@A_fft@c-c@A2@c)/abs(c@A2@c)))
print('J fft %.12e exact %.12e rel %.2e'%(c@B_fft@c,c@B2@c,abs(c@B_fft@c-c@B2@c)/abs(c@B2@c)))
