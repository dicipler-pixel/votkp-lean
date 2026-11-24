# SCRIPT: TWIN-WALK-COMBINE-01
# Composes chunk outputs of twinwalk (in order) in 40-digit mpmath, adds the boundary steps, and reads off at every
# checkpoint: frame turn (deg), frame axis, distance d, heading, d - L/sqrt3, sum r^2, gap-weighted arm sums S_s.
# Kill (before run): K1 turn at 1e8 != 12.204756 or at 1e9 != 12.269506 (harness 40-digit) beyond 2e-6 deg -> walker wrong.
#                    K3 twin-pair counts at the last start below 1e9 / 1e10 != pi2 - 2 (3424504 / 27412677) -> sieve wrong.
# usage: python3 combine.py out.csv chunk1.txt chunk2.txt ...
import sys, mpmath as mp
mp.mp.dps=40
def B(s,r):
    ch,sh=mp.cosh(r/2),mp.sinh(r/2)
    if s==0: return mp.matrix([[ch,sh],[sh,ch]])
    if s==1: return mp.matrix([[ch,-1j*sh],[1j*sh,ch]])
    return mp.matrix([[mp.exp(r/2),0],[0,mp.exp(-r/2)]])
def arm(a): d=a%10; return 0 if d==1 else 1 if d==7 else 2
def parseM(v): return mp.matrix([[mp.mpc(v[0],v[1]),mp.mpc(v[2],v[3])],[mp.mpc(v[4],v[5]),mp.mpc(v[6],v[7])]])
def readout(M):
    M=M/mp.sqrt(mp.det(M))            # remove the tiny determinant drift
    A=M*M.H; tr=mp.re(A[0,0]+A[1,1]); d=mp.acosh(tr/2)
    adj=mp.matrix([[A[1,1],-A[0,1]],[-A[1,0],A[0,0]]])
    Hinv=(adj+mp.eye(2))/mp.sqrt(tr+2); U=Hinv*M
    c=mp.re(U[0,0]+U[1,1])/2; sgn=1 if c>=0 else -1; U=U*sgn; c=abs(c)
    th=2*mp.acos(min(c,1)); s=mp.sin(th/2) or mp.mpf(1)
    ax=[-mp.im(U[0,1])/s,-mp.re(U[0,1])/s,-mp.im(U[0,0])/s]
    sd=mp.sinh(d) or mp.mpf(1); n=[mp.re(A[0,1])/sd,-mp.im(A[0,1])/sd,mp.re(A[0,0]-A[1,1])/(2*sd)]
    sig=[mp.matrix([[0,1],[1,0]]),mp.matrix([[0,-1j],[1j,0]]),mp.matrix([[1,0],[0,-1]])]
    R=[[mp.re(sum((sig[i]*U*sig[j]*U.H)[k,k] for k in range(2)))/2 for j in range(3)] for i in range(3)]
    m=[1/mp.sqrt(3)]*3; Rm=[sum(R[i][j]*m[j] for j in range(3)) for i in range(3)]
    ang=mp.degrees(mp.acos(max(-1,min(1,sum(n[i]*Rm[i] for i in range(3))))))
    # predicted frame if the arm tilt dies out (Hardy-Littlewood): body heading u=R^T n is carried to m by the minimal
    # rotation, R_inf = R Q with Q m = u (axis m x u, angle acos(m.u)); n held fixed (its motion ~ r/sinh d is negligible)
    u=[sum(R[j][i]*n[j] for j in range(3)) for i in range(3)]
    k=[m[1]*u[2]-m[2]*u[1],m[2]*u[0]-m[0]*u[2],m[0]*u[1]-m[1]*u[0]]; sk=mp.sqrt(sum(x*x for x in k)); al=mp.acos(max(-1,min(1,sum(m[i]*u[i] for i in range(3)))))
    k=[x/sk for x in k] if sk>0 else [0,0,0]
    K=mp.matrix([[0,-k[2],k[1]],[k[2],0,-k[0]],[-k[1],k[0],0]]); Q=mp.eye(3)+mp.sin(al)*K+(1-mp.cos(al))*K*K
    Rp=mp.matrix(R)*Q; trp=Rp[0,0]+Rp[1,1]+Rp[2,2]
    pred=mp.degrees(mp.acos(max(-1,min(1,(trp-1)/2))))
    return mp.degrees(th),ax,d,n,ang,pred
out=open(sys.argv[1],'w')
out.write('X,a,count,steps,L,turn_deg,ax_x,ax_y,ax_z,d,d_minus_L_over_sqrt3,sum_r2,S_x,S_y,S_z,n_x,n_y,n_z,angle_heading_Rm_deg,turn_if_tilt_dies_deg\n')
P=mp.eye(2); last=None; tot=dict(sr=mp.mpf(0),sr2=mp.mpf(0),W=[mp.mpf(0)]*3,cnt=0,steps=0)
for fn in sys.argv[2:]:
    lines=[l.split() for l in open(fn)]
    end=[l for l in lines if l[0]=='END'][0]; first=int(end[1])
    pre=P; bs=dict(sr=0,sr2=0,W=[0,0,0],steps=0)
    if last is not None:
        r=mp.log(mp.mpf(first)/last); s=arm(first); pre=P*B(s,r)
        W=[0,0,0]; W[s]=r; bs=dict(sr=r,sr2=r*r,W=W,steps=1)
    def state(l,off):
        M=pre*parseM(l[off:off+8]); v=[mp.mpf(x) for x in l[off+8:off+13]]
        sr=tot['sr']+bs['sr']+v[0]; sr2=tot['sr2']+bs['sr2']+v[1]
        W=[tot['W'][i]+bs['W'][i]+v[2+i] for i in range(3)]
        return M,sr,sr2,W
    for l in lines:
        if l[0]!='CP': continue
        X=float(l[1]); a=int(l[2]); cnt=tot['cnt']+int(l[3]); st=tot['steps']+bs['steps']+int(l[4])
        M,sr,sr2,W=state(l,5); th,ax,d,n,ang,pred=readout(M); L=mp.log(mp.mpf(a)/11)
        S=[W[i]-sr/3 for i in range(3)]
        out.write(','.join(str(x) for x in [X,a,cnt,st,mp.nstr(L,15),mp.nstr(th,12),*[mp.nstr(x,10) for x in ax],mp.nstr(d,15),
              mp.nstr(d-L/mp.sqrt(3),12),mp.nstr(sr2,12),*[mp.nstr(x,12) for x in S],*[mp.nstr(x,10) for x in n],mp.nstr(ang,8),mp.nstr(pred,10)])+'\n')
    M,sr,sr2,W=state(end,5)
    P=M; last=mp.mpf(int(end[2])); tot=dict(sr=sr,sr2=sr2,W=W,cnt=tot['cnt']+int(end[3]),steps=tot['steps']+bs['steps']+int(end[4]))
print('final: last start',int(last),'count',tot['cnt'],'steps',tot['steps'])
