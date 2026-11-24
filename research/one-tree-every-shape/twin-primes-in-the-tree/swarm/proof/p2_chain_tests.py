# SCRIPT: TWIN-PROOF-CHAIN-TESTS-01
# Runs the twin chain to X = 1e9 through the EXACT frame-free reduction of REPORT.md Step 1:
#   Y_n = B(e_s, r_n) Y_{n-1}  (body heading u and distance d, no frame needed),
#   R_n = R_{n-1} exp(hat nu_n), nu_n = eps_n (e_s x u)/|e_s x u|, tan(eps/2) = sin th/(coth(d/2)coth(r/2)+cos th).
# Kill conditions, written before the run:
#  K-REC : d - L/sqrt3 at 1e8 and 1e9 must match the earlier direct 4x4 harness (0.1082, 0.1090, +-0.0008 rounding).
#          If off by more than 0.002 the reduction is wrong.
#  K-H2  : if sum of r^2 over twin starts in (1e8, 1e9] exceeds 1e-4, the H2 tail is not settling at this range.
#  K-DEC : if the mean |gap-weighted share - 1/3| over unit path windows L in [14,18) is more than 0.8 x the mean over
#          L in [6,10), the claim "the systematic tilt decays" dies at this range.
#  K-MOD : lattice (mod 30) model predicts weighted-minus-count share  +rho/15, -rho/15, 0  for end digits 1, 7, 9
#          (rho = twin starts per 10 integers). If the measured sign for digit 1 or 7 is opposite in the pooled
#          windows L >= 10, the lattice model of the tilt dies.
#  K-FRM : if the frame moves more between 1e8 and 1e9 than between 1e7 and 1e8, the convergence evidence fails.
#  K-ADV : strawman test. Same gaps, end digits reassigned so every consecutive triple has one of each digit
#          (counts equidistributed to within 1) but the largest gap of the triple goes to digit 1.
#          If this chain's d/L ends within 0.005 of the true chain's d/L, the objection "count equidistribution
#          does not fix the endpoint law" fails.
import numpy as np, math, time
t0 = time.time()
X = 10**9
M = X//2 + 2                       # odd-only sieve: index i <-> 2i+1
s = np.ones(M, dtype=bool); s[0] = False
for i in range(1, int(math.isqrt(2*M+1))//2 + 1):
    if s[i]:
        p = 2*i+1; s[(p*p)//2::p] = False
tw_idx = np.nonzero(s[:-1] & s[1:])[0]
T = 2*tw_idx + 1; T = T[(T > 5) & (T <= X)]
del s
print('sieve done %.0fs, twin starts in (5,1e9]: %d' % (time.time()-t0, len(T)))
arm = np.searchsorted([1,7,9], T % 10)
r = np.log(T[1:]/T[:-1]); a_next = T[1:]; s_next = arm[1:]
L = np.cumsum(r)                    # path after step n
# ---- H2 data
r2 = r*r
for k in range(3,10):
    m = a_next <= 10**k
    print('sum r^2 up to 1e%d = %.7f   max r in (1e%d,1e%d] = %.3e' % (k, r2[m].sum(), k-1, k, r[(a_next>10**(k-1))&m].max() if k>3 else r[m].max()))
tail = r2[a_next > 10**8].sum(); print('H2 tail (1e8,1e9] = %.3e' % tail, 'K-H2', 'PASS' if tail < 1e-4 else 'KILL')
# dyadic block max r  (sufficient condition: sum of block maxima finite)
blocks = np.floor(np.log2(a_next)).astype(int); rho = {}
for b in range(5, int(blocks.max())+1):
    mm = blocks == b
    if mm.any(): rho[b] = r[mm].max()
print('block-max r (dyadic) at 2^10,2^15,2^20,2^25,2^29:', ['%.2e' % rho[b] for b in (10,15,20,25,29)])
print('sum of dyadic block maxima to 2^29: %.4f ; block max * 2^b / b^2 (gap / ln^2 scale):' % sum(rho.values()),
      ['%.2f' % (rho[b]*2**b/(b*math.log(2))**2) for b in (15,20,25,29)])
# ---- windowed shares
print('\nunit-path windows: L, n, weighted share (1,7,9), count share (1,7,9), rho, model (+rho/15,-rho/15,0)')
Lstart = np.concatenate([[0.0], L[:-1]])
wins = []
for k in range(3, int(L[-1])):
    mm = (Lstart >= k) & (Lstart < k+1)
    if mm.sum() < 50: continue
    w = np.array([r[mm][s_next[mm]==j].sum() for j in range(3)]); w = w/w.sum()
    c = np.bincount(s_next[mm], minlength=3)/mm.sum()
    xlo, xhi = T[:-1][mm][0], a_next[mm][-1]
    rho_ = 10*mm.sum()/(xhi-xlo)
    wins.append((k, mm.sum(), w, c, rho_))
    print('L=%2d n=%8d  w=(%.4f %.4f %.4f)  c=(%.4f %.4f %.4f)  w-c=(%+.4f %+.4f %+.4f) rho=%.4f model=(%+.4f %+.4f 0)' %
          (k, mm.sum(), *w, *c, *(w-c), rho_, rho_/15, -rho_/15))
lo = [np.abs(x[2]-1/3).mean() for x in wins if 6 <= x[0] < 10]; hi = [np.abs(x[2]-1/3).mean() for x in wins if 14 <= x[0] < 18]
print('mean |w-1/3| L in [6,10): %.5f   L in [14,18): %.5f' % (np.mean(lo), np.mean(hi)), 'K-DEC', 'PASS' if np.mean(hi) <= 0.8*np.mean(lo) else 'KILL')
pool = [x for x in wins if x[0] >= 10]
wc = np.mean([x[2]-x[3] for x in pool], axis=0); mod = np.mean([x[4]/15 for x in pool])
print('pooled L>=10: measured w-c = (%+.5f %+.5f %+.5f), model = (%+.5f %+.5f 0)' % (*wc, mod, -mod),
      'K-MOD', 'PASS' if (wc[0] > 0 and wc[1] < 0) else 'KILL')
# bias times L^2 (decay law test)
print('weighted share - 1/3 for digit 1, times L^2:', ['L%d:%+.2f' % (x[0], (x[2][0]-1/3)*(x[0]+.5)**2) for x in wins])
# ---- exact reduced recursion
E = np.eye(3); P = np.ones(3)/3; Phat = P/np.linalg.norm(P)
def run(sarr, rarr, marks):
    Y = np.array([1.0, 0, 0, 0]); R = np.eye(3); out = {}; Lp = 0.0
    sum_ra = 0.0; sum_r1t = 0.0; mi = 0
    for n in range(len(rarr)):
        rr = rarr[n]; sv = sarr[n]
        g = Y[0]; d = math.acosh(max(g, 1.0)); sh = math.sinh(d)
        if sh > 0:
            u = Y[1:]/sh; cth = u[sv]; cth = max(-1.0, min(1.0, cth)); sth = math.sqrt(max(0.0, 1-cth*cth))
            if sth > 1e-15:
                eps = 2*math.atan(sth/(1/math.tanh(d/2)/math.tanh(rr/2) + cth))
                ax = np.cross(E[sv], u); ax /= np.linalg.norm(ax)
                K = np.array([[0,-ax[2],ax[1]],[ax[2],0,-ax[0]],[-ax[1],ax[0],0]])
                R = R @ (np.eye(3) + math.sin(eps)*K + (1-math.cos(eps))*K@K)
            alpha = math.acos(max(-1, min(1, float(u@Phat))))
            sum_ra += rr*alpha; sum_r1t += rr*(1-math.tanh(d/2))
        c, shr = math.cosh(rr), math.sinh(rr); t_, x_ = Y[0], Y[1+sv]
        Y[0] = c*t_ + shr*x_; Y[1+sv] = shr*t_ + c*x_
        Lp += rr
        if mi < len(marks) and n+1 == marks[mi][1]:
            d = math.acosh(Y[0]); u = Y[1:]/math.sinh(d)
            out[marks[mi][0]] = (Lp, d, u.copy(), R.copy(), sum_ra, sum_r1t)
            mi += 1
    return out
marks = [(k, int(np.searchsorted(a_next, 10**k, side='right'))) for k in range(4,10)]
t1 = time.time(); out = run(s_next, r, marks); print('\nreduced recursion %.0fs' % (time.time()-t1))
prevR = None; moves = {}
for k in range(4,10):
    Lp, d, u, R, sra, sr1t = out[k]
    ang = math.degrees(math.acos(max(-1, min(1, float(u@Phat)))))
    mv = None if prevR is None else math.degrees(math.acos(max(-1, min(1, (np.trace(R@prevR.T)-1)/2))))
    moves[k] = mv
    print('1e%d: L=%.4f d-L/sqrt3=%.4f d/L=%.5f angle(u,diag)=%.3f deg  sum r*alpha=%.5f sum r(1-tanh(d/2))=%.5f frame moved %s deg since 1e%d'
          % (k, Lp, d-Lp/math.sqrt(3), d/Lp, ang, sra, sr1t, 'n/a' if mv is None else '%.4f' % mv, k-1))
    prevR = R
ok = abs(out[8][1]-out[8][0]/math.sqrt(3)-0.1082) < 0.002 and abs(out[9][1]-out[9][0]/math.sqrt(3)-0.1090) < 0.002
print('K-REC', 'PASS' if ok else 'KILL', '  K-FRM', 'PASS' if moves[9] < moves[8] else 'KILL')
# ---- noise tails (relative to the 1e9 endpoint, so truncated) and the H3' integral
xi = r[:, None]*(np.eye(3)[s_next] - P)       # gap-weighted noise vectors
S = np.cumsum(xi, axis=0); N = S[-1] - S          # tail from n to the 1e9 cut
nN = np.linalg.norm(N, axis=1)
for k in range(4,9):
    i = marks[k-4][1]-1; print("tail |N| at 1e%d (to 1e9 cut) = %.4f ; L=%.2f ; L*|N| = %.3f" % (k, nN[i], L[i], L[i]*nN[i]))
print("H3' integral sum r|N| up to 1e8 = %.4f (truncated tails)" % (r[:marks[4][1]]*nN[:marks[4][1]]).sum())
# ---- strawman K-ADV
nt = (len(r)//3)*3; rr = r[:nt].reshape(-1,3); order = np.argsort(-rr, axis=1)
s_adv = np.empty_like(rr, dtype=int); rows = np.arange(len(rr))[:, None]
s_adv[rows, order] = np.array([0,1,2])[None, :]        # largest gap -> digit 1, middle -> 7, smallest -> 9
s_adv = s_adv.reshape(-1); r_adv = r[:nt]
wa = np.array([r_adv[s_adv==j].sum() for j in range(3)]); print('\nadversarial chain: counts', np.bincount(s_adv), ' gap-weighted shares', np.round(wa/wa.sum(),4))
marks_adv = [(9, nt)]; oa = run(s_adv, r_adv, marks_adv)[9]
Pa = wa/wa.sum(); print('adversarial d/L = %.5f ; true chain d/L = %.5f ; |P_adv| = %.5f ; 1/sqrt3 = %.5f ; angle(u, P_adv) = %.3f deg'
      % (oa[1]/oa[0], out[9][1]/out[9][0], np.linalg.norm(Pa), 1/math.sqrt(3), math.degrees(math.acos(float(oa[2]@Pa)/np.linalg.norm(Pa)))))
print('K-ADV', 'objection SURVIVES (count law does not fix endpoint)' if abs(oa[1]/oa[0]-out[9][1]/out[9][0]) > 0.005 else 'objection KILLED')
print('total %.0fs' % (time.time()-t0))
