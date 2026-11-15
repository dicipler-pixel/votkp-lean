# SCRIPT: CHK-04-TWIN-CHAIN (twin starts, end digits, counts, path length, frame-turn windows at ratio 5 and 7)
import numpy as np, math, cmath
def sieve(N):
    s=bytearray([1])*(N+1); s[0]=s[1]=0
    for i in range(2,int(N**0.5)+1):
        if s[i]: s[i*i::i]=bytearray(len(s[i*i::i]))
    return s
N=400000; S=sieve(N+2)
TW=[a for a in range(11,N+1) if S[a] and S[a+2]]
print("twin starts a>=11, a<=4e5:",len(TW),"(R4 says 3802)")
print("end digits (a>5) set:",sorted(set(a%10 for a in TW)))
TW5=[a for a in range(5,3126) if S[a] and S[a+2]]
print("pairs from a=5 up to 3125:",len(TW5),"(R4 says 82)")
print("path length sum ln(a'/a) over 11..last =", sum(math.log(TW[i+1]/TW[i]) for i in range(len(TW)-1)), " ln(last/11)=", math.log(TW[-1]/11))
print("step a->a+2 : Gamma=1/(a+1)? a=11:",((13/11)-1)/((13/11)+1), 1/12, " length ln(1+2/a)", math.log(13/11))
# frame turn per 12-step window, sl2 matrices as in R4-18
def sl2(z, ax, sg):
    k=1/(2*math.sqrt(z)); p=(z+1)*k; q=sg*(z-1)*k
    if ax==0: return np.array([[p,q],[q,p]],complex)
    if ax==1: return np.array([[p,-1j*q],[1j*q,p]],complex)
    return np.array([[p+q,0],[0,p-q]],complex)
def polarU(M):
    W,S_,Vh=np.linalg.svd(M); return W@Vh
def turn(U): return 2*math.acos(min(1,abs((U[0,0]+U[1,1]).real)/2))
dig={1:0,7:1,9:2}
for z in (5,7):
    angs=[]; M=np.eye(2,dtype=complex); w=0
    for a in TW:
        sh=dig[a%10]
        if w%12==0: M=np.eye(2,dtype=complex)
        M=M@sl2(z,sh,1); w+=1
        angs.append(turn(polarU(M)))
    print("z",z,"mean frame turn (rad) over all pairs",np.mean(angs)," last-in-window only:",np.mean([angs[i] for i in range(11,len(angs),12)]))
# the 82 pair chain from a=5 as in the Two Trees page (sh=-1 waist at 5 skipped)
angs=[]; M=np.eye(2,dtype=complex); w=0
for a in TW5:
    if a==5: continue
    sh=dig[a%10]
    if w%12==0: M=np.eye(2,dtype=complex)
    M=M@sl2(5,sh,1); w+=1; angs.append(turn(polarU(M)))
print("82-pair chain z=5 mean turn",np.mean(angs))
# next-arm shares
cnt={}
for i in range(len(TW)-1):
    k=(TW[i]%10,TW[i+1]%10); cnt[k]=cnt.get(k,0)+1
tot={}
for (a,b),c in cnt.items(): tot[a]=tot.get(a,0)+c
print("next-end-digit shares:",{k:round(v/tot[k[0]],3) for k,v in sorted(cnt.items())})
