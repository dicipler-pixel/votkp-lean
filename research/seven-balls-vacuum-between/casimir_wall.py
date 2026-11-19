# SCRIPT: CASIMIR-WALL-01
# Static Casimir (Lifshitz) energy between two of his faces: two half-spaces of index ratio z (his Gamma=(z-1)/(z+1) is the
# normal-incidence reflection) across an empty gap of width w, T=0, no dispersion (z held fixed at all frequencies: MODEL).
# E/A = -(hbar c / (16 pi^2 w^3)) * F,  F = int_0^{pi/2} cos(phi) [Li4(r_TE^2) + Li4(r_TM^2)] dphi,  perfect mirrors F = 2 zeta(4).
# Checks: (1) direct 2D integral over (k, xi) agrees with the polar formula; (2) z -> infinity gives the perfect-mirror value.
import mpmath as mp
mp.mp.dps=30
ZW=3+2*mp.sqrt(2)
def rTE(phi,eps): s=mp.sqrt(mp.cos(phi)**2+eps*mp.sin(phi)**2); return (1-s)/(1+s)
def rTM(phi,eps): s=mp.sqrt(mp.cos(phi)**2+eps*mp.sin(phi)**2); return (eps-s)/(eps+s)
def F(z):
    eps=z*z
    return mp.quad(lambda p: mp.cos(p)*(mp.polylog(4,rTE(p,eps)**2)+mp.polylog(4,rTM(p,eps)**2)),[0,mp.pi/2])
Fp=2*mp.zeta(4)
def F_direct(z,w=1):
    # E/A * (16 pi^2 w^3/(hbar c)) computed from the raw Lifshitz double integral in (k, xi/c)
    eps=z*z
    def inner(x,k):
        kap=mp.sqrt(k*k+x*x); kb=mp.sqrt(k*k+eps*x*x)
        a=(kap-kb)/(kap+kb); b=(eps*kap-kb)/(eps*kap+kb)
        return k*(mp.log(1-a*a*mp.exp(-2*kap*w))+mp.log(1-b*b*mp.exp(-2*kap*w)))
    I=mp.quad(lambda k: mp.quad(lambda x: inner(x,k),[0,1,mp.inf]),[0,1,mp.inf])
    return -4*I*w**3   # E/A = hbar c/(4 pi^2) I  ->  F = -(16 pi^2 w^3/(hbar c)) E/A = -4 I w^3
print("1. Check: polar formula vs raw double integral (z=3):", mp.nstr(F(3),12), mp.nstr(F_direct(3),12))
print("2. Check: z -> infinity approaches perfect mirrors: F(1e4)/F_perfect =", mp.nstr(F(mp.mpf(10)**4)/Fp,10))
print("3. Force/energy as a share of perfect mirrors (eta = F/F_perfect), and his normal-incidence-only scalar Li4(G^2)/zeta(4):")
for lab,z in [('z=3',3),('z=5',5),('wall 3+2sqrt2',ZW),('z=7',7),('z=16.82 (mu->tau)',mp.mpf('16.818'))]:
    G=(z-1)/(z+1)
    print(f"   {lab:20s} Gamma={mp.nstr(G,6):8s} Gamma^2={mp.nstr(G*G,6):8s} eta={mp.nstr(F(z)/Fp,6):8s} scalar Li4(G^2)/zeta4={mp.nstr(mp.polylog(4,G*G)/mp.zeta(4),6)}")
print("4. At the wall, scalar normal-incidence value exactly Li4(1/2)/zeta(4) =", mp.nstr(mp.polylog(4,mp.mpf(1)/2)/mp.zeta(4),12))
hbarc=197.3269804e-9  # eV*m
for w in [1e-7,1e-6]:
    E0=-(mp.pi**2*hbarc/(720*w**3)); P0=-(mp.pi**2*hbarc/(240*w**4))*1.602176634e-19
    print(f"5. w={w:g} m: perfect-mirror pressure {mp.nstr(P0,5)} Pa; at the wall (z=3+2sqrt2, no dispersion) {mp.nstr(P0*F(ZW)/Fp,5)} Pa")
