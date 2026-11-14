# SCRIPT: LOOP2-CHECK1-EXACT-RATE
# WHY THIS DECIDES IT: for a Mobius map with fixed points a (attracting) and b (repelling) and multiplier m,
# the coefficient ratio w = B/A in psi = A v_a + B v_b is mapped to m*w EXACTLY (W v_a = mu_a v_a, W v_b = mu_b v_b,
# m = mu_b/mu_a). The chordal distance on the unit (Bloch) sphere is then an exact function of w and the angle alpha
# between the fixed directions:
#     d = 2 sin(alpha/2) |w| / sqrt(1 + |w|^2 + 2 cos(alpha/2) Re w)    (gauge: <v_a|v_b> = cos(alpha/2) real >= 0).
# The "actual" d_n below is computed independently: 2|det(psi_n, v_a)|/|psi_n| with psi_n = W^n psi_0 by plain
# matrix multiplication (no use of w, m or alpha). Agreement to 1e-30 relative over 30 passes is not possible by accident.
# Precision is raised with lambda (50 digits + 30*lambda/ln10 + 20) because d_30 ~ e^{-30 lambda} must stay resolved
# inside a determinant; a second fixed-50-digit run is made on the passes where d_n > 1e-15 to honour the 50-digit setting.
# KILL LINE (before the run): any relative residual |d_actual - d_formula| / d_actual > 1e-30 -> exact law fails.
# Closed-form candidates tested (killed individually if residual > 1e-30 at 50 digits):
#   L1: cosh(lambda/4) = sinh^2(r/2) = Gamma^2/(1-Gamma^2)   (lambda = 4 arccosh(Gamma^2/(1-Gamma^2)), z>wall)
#   L2: sin^2(alpha/2) = 1 - 2 Gamma^2 inside; past the wall candidates cos^2(alpha/2) = 1/(2Gamma^2) and sin^2(alpha/2)=2Gamma^2-1
#   L3: multiplier m = mu_b/mu_a = exp(-lambda)
import mpmath as mp, random, json
def mats(r):
    c,s=mp.cosh(r/2),mp.sinh(r/2); I=mp.mpf(1)
    Bx=mp.matrix([[c,s],[s,c]]); By=mp.matrix([[c,-1j*s],[1j*s,c]])
    Bxi=mp.matrix([[c,-s],[-s,c]]); Byi=mp.matrix([[c,1j*s],[-1j*s,c]])
    return Bx*By*Bxi*Byi
def run(z,nstart=200,N=30,dps=None,tag='adaptive'):
    mp.mp.dps=60; zz=mp.mpf(z); r=mp.log(zz); lam0=2*mp.acosh(-(2-4*mp.sinh(r/2)**4)/2)
    mp.mp.dps = dps if dps else int(60+30*lam0/mp.log(10)+20)
    zz=mp.mpf(z); r=mp.log(zz); G=mp.tanh(r/2); W=mats(r)
    tr=W[0,0]+W[1,1]; lam=2*mp.acosh(-tr.real/2)
    E,V=mp.eig(W)
    ia=0 if abs(E[0])>abs(E[1]) else 1; ib=1-ia
    va=V[:,ia]; vb=V[:,ib]
    nrm=lambda v: mp.sqrt(abs(v[0])**2+abs(v[1])**2)
    va=va/nrm(va); vb=vb/nrm(vb)
    c=va[0].conjugate()*vb[0]+va[1].conjugate()*vb[1]
    vb=vb*(abs(c)/c)  # gauge: <va|vb> real>=0
    c=abs(c); sh=mp.sqrt(1-c*c)   # cos(alpha/2), sin(alpha/2)
    m=E[ib]/E[ia]
    M=mp.matrix([[va[0],vb[0]],[va[1],vb[1]]]); Mi=M**-1
    random.seed(7); worst=mp.mpf(0); nused=0
    for k in range(nstart):
        psi=mp.matrix([mp.mpc(random.gauss(0,1),random.gauss(0,1)),mp.mpc(random.gauss(0,1),random.gauss(0,1))])
        co=Mi*psi; w0=co[1]/co[0]
        p=psi
        for n in range(1,N+1):
            p=W*p
            actual=2*abs(p[0]*va[1]-p[1]*va[0])/nrm(p)
            wn=(m**n)*w0
            form=2*sh*abs(wn)/mp.sqrt(1+abs(wn)**2+2*c*wn.real)
            if dps is not None and actual<mp.mpf('1e-15'): continue
            nused+=1
            worst=max(worst,abs(actual-form)/actual)
    res=dict(z=z,tag=tag,dps=mp.mp.dps,worst_rel=mp.nstr(worst,5),points=nused,
      lam=mp.nstr(lam,20),
      L1=mp.nstr(abs(mp.cosh(lam/4)-G**2/(1-G**2)),5),
      L3=mp.nstr(abs(m-mp.exp(-lam)),5),
      cos2_half_alpha=mp.nstr(c*c,20),sin2_half_alpha=mp.nstr(sh*sh,20),
      cand_cos2_eq_1_over_2G2=mp.nstr(abs(c*c-1/(2*G*G)),5),
      cand_sin2_eq_2G2_minus_1=mp.nstr(abs(sh*sh-(2*G*G-1)),5),
      cand_cos2_eq_2G2=mp.nstr(abs(c*c-2*G*G),5),
      cand_sin2_eq_1_minus_2G2=mp.nstr(abs(sh*sh-(1-2*G*G)),5),
      cand_cos2_eq_1_minus_1_over_2G2=mp.nstr(abs(c*c-(1-1/(2*G*G))),5),
      G2=mp.nstr(G*G,12))
    return res
out=[]
for z in ['5.9','6.5','8','16.8177','206.768']:
    for d in (None,50):
        r=run(z,dps=d,tag='adaptive' if d is None else 'fixed50'); out.append(r); print(json.dumps(r),flush=True)
json.dump(out,open('check1_rate.out','w'),indent=1)
