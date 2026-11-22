# SCRIPT: SEA-RUNS-01
# All the balls in the sea, as many ways as possible. Jeromie Beasley. 16 Nov 2026. AI-assisted. The ways and the marks: WAYS_SEA_01.md.
import json, math, sys, itertools, time
import numpy as np, scipy.sparse as sp
from scipy.linalg import expm
GOLD = (1 + 5**0.5)/2
SX = np.array([[0, 1], [1, 0]], complex); SY = np.array([[0, -1j], [1j, 0]]); SZ = np.array([[1, 0], [0, -1]], complex)
dsig = lambda d: d[0]*SX + d[1]*SY + d[2]*SZ
def rot2(d, h): m = np.linalg.norm(d); return np.eye(2) if m < 1e-300 else math.cos(m*h)*np.eye(2) - 1j*math.sin(m*h)*dsig(d)/m
def bloch(C): return np.array([2*C[1, 0].real, 2*C[1, 0].imag, (C[0, 0] - C[1, 1]).real])
_W = {}
def world(tag):
    if tag not in _W:
        w = json.load(open(tag + '.json')); T = w['T']; w['Tm'] = sp.csr_matrix((np.array(T['vr']) + 1j*np.array(T['vi']), (T['rows'], T['cols'])), shape=(w['M'], w['M']))
        w['Am'] = np.array(w['A']['re']) + 1j*np.array(w['A']['im']); _W[tag] = w
    return _W[tag]
def gapped_half(V):
    th = np.angle(np.linalg.eigvals(V)); grid = np.linspace(0, math.pi, 20001)[:-1]; best = (-1, 0)
    for i in range(0, len(grid), 500):
        p = grid[i:i+500]; d = np.abs(np.angle(np.exp(1j*(th[None, :] - p[:, None])))); m = np.minimum(d, math.pi - d).min(1); k = int(np.argmax(m))
        if m[k] > best[0]: best = (float(m[k]), float(p[k]))
    mg, phi = best; Hs = (np.exp(-1j*phi)*V - np.exp(1j*phi)*V.conj().T)/(2j); w, U = np.linalg.eigh(Hs); sel = U[:, w > 0]; return sel @ sel.conj().T, mg, int(sel.shape[1])
_REST = {}
def push_term(w, d, drest, kappa):
    G = [np.zeros(3) for _ in range(w['N'])]
    for l in w['links']:
        R = np.array(l['R']); G[l['i']] += 2*kappa*(d[l['i']] - R @ drest[l['j']]); G[l['j']] += 2*kappa*(d[l['j']] - R.T @ drest[l['i']])
    return G
def run(cfg, _twin=False):
    t0 = time.time(); w = world(cfg['world']); N, h = w['N'], w['h']; ck = w['clocks'][cfg['clocks']]; drest = [np.array(x) for x in ck['d']]; rates = ck['rate']; omega = w['omega']
    arm = list(range(1, N)); far = 2 if N == 3 else 3; lfar = [l for l in w['links'] if l['i'] == 0 and l['j'] == far][0]['d']; mach, ends = cfg['machine'], cfg['ends']; T_end = cfg.get('T', 240.0); nst = int(round(T_end/h))
    th_l = math.sqrt(0.1*h)
    if mach == 'A':
        M = 2*N; H0 = w['Am']; Hd = lambda d: H0 + sum(np.kron(np.diag([1.0 if k == i else 0 for k in range(N)]), dsig(d[i])) for i in range(N))
        key = ('A', cfg['world'], cfg['clocks'])
        if key not in _REST:
            ev, U = np.linalg.eigh(Hd(drest)); gp = np.diff(ev); k = max((N - 1, N, N + 1), key=lambda c: gp[c - 1]); _REST[key] = (U[:, :k] @ U[:, :k].conj().T, float(gp[k - 1]), k)
        Prest, margin, rank = _REST[key]; V0 = None
    else:
        M0 = w['M']; nc = int(round(2.0/h)) if ends == 'container' else 0; M = M0 + len(arm)*4*nc; V0 = sp.lil_matrix((M, M), dtype=complex); V0.setdiag(1); V0[:M0, :M0] = w['Tm']
        if nc:
            E = sp.lil_matrix((M, M), dtype=complex); E.setdiag(1); th = math.sqrt(w['gamma']*h); c, s = math.cos(th), math.sin(th)
            for a, i in enumerate(arm):
                f0 = M0 + a*4*nc; b0 = f0 + 2*nc
                for q in range(2):
                    p = 2*i + q; fo, bo, fn, bn = f0 + q, b0 + q, f0 + 2*(nc - 1) + q, b0 + 2*(nc - 1) + q
                    for j in range(1, nc):
                        E[f0 + 2*(j - 1) + q, f0 + 2*(j - 1) + q] = 0; E[f0 + 2*(j - 1) + q, f0 + 2*j + q] = 1; E[b0 + 2*(j - 1) + q, b0 + 2*(j - 1) + q] = 0; E[b0 + 2*(j - 1) + q, b0 + 2*j + q] = 1
                    E[fn, fn] = 0; E[bn, bn] = 0; E[p, p] = 0
                    E[fn, p] = s; E[fn, bo] = c; E[p, p] = c; E[p, bo] = -s; E[bn, fo] = -1
            V0 = (E.tocsr() @ V0.tocsr())
        V0 = sp.csr_matrix(V0)
        key = ('C', cfg['world'], cfg['clocks'], ends == 'container')
        if mach == 'C' and key not in _REST:
            Vd = V0.toarray(); 
            for i in range(N): Vd[2*i:2*i+2, :] = rot2(drest[i], h) @ Vd[2*i:2*i+2, :]
            _REST[key] = gapped_half(Vd) + (float(np.max(abs(Vd.conj().T @ Vd - np.eye(M)))),)
        if mach == 'C': Prest, margin, rank, udev = _REST[key]
        else:
            Prest = np.zeros((M, M), complex); margin = float('nan')
            for i in range(N):
                ev, U = np.linalg.eigh(dsig(drest[i])); Prest[2*i:2*i+2, 2*i:2*i+2] = np.outer(U[:, 0], U[:, 0].conj())
            rank = N
    P = Prest.copy(); d = [x.copy() for x in drest]; feed = cfg['feed']; push = cfg['push']; Cr = [Prest[2*i:2*i+2, 2*i:2*i+2].copy() for i in range(N)]; srest = [bloch(c) for c in Cr]
    tie0 = float(np.linalg.norm(P[0:2, 2*far:2*far+2])**2); tr0 = float(np.trace(P).real)
    def local(P, i, K): P[2*i:2*i+2, :] = K @ P[2*i:2*i+2, :]; P[:, 2*i:2*i+2] = P[:, 2*i:2*i+2] @ K.conj().T
    u = drest[0]/np.linalg.norm(drest[0]); a = np.array([1.0, 0, 0]) if abs(u[0]) < 0.9 else np.array([0, 1.0, 0]); n = np.cross(u, a); n /= np.linalg.norm(n)
    Kbig = math.cos(math.pi/4)*np.eye(2) - 1j*math.sin(math.pi/4)*dsig(n); Ksm = math.cos(0.05)*np.eye(2) - 1j*math.sin(0.05)*dsig(n)
    if feed == 'kick' and not _twin: local(P, 0, Kbig)
    Tk = math.pi*(GOLD if feed == 'kicks_out' else 1.0); Om = 2*omega*(GOLD if feed == 'squeeze_out' else 1.0); nextk = Tk
    S = np.zeros((nst + 1, N, 3)); dfar = np.zeros(nst + 1); exc = []; trmax = tr0; dmove = 0.0; frames = []
    for i in range(N):
        uu = drest[i]/np.linalg.norm(drest[i]); aa = np.array([0, 0, 1.0]) if abs(uu[2]) < 0.9 else np.array([1.0, 0, 0]); f1 = np.cross(aa, uu); f1 /= np.linalg.norm(f1); frames.append((f1, np.cross(uu, f1)))
    static = (feed in ('kick', 'none')) and not push; Vfix = None
    if mach != 'A' and static:
        Bf = sp.lil_matrix((M, M), dtype=complex); Bf.setdiag(1)
        for i in range(N): Bf[2*i:2*i+2, 2*i:2*i+2] = rot2(drest[i], h)
        Vfix = (Bf.tocsr() @ V0).tocsr(); VfH = Vfix.conj().T.tocsr()
    if mach != 'A': V0H = V0.conj().T.tocsr()
    UA = expm(-1j*Hd(drest)*h) if mach == 'A' and static else None
    for k in range(nst + 1):
        t = k*h
        for i in range(N): S[k, i] = bloch(P[2*i:2*i+2, 2*i:2*i+2]) - srest[i]
        dfar[k] = np.linalg.norm(P[2*far:2*far+2, 2*far:2*far+2] - Cr[far])
        if k % 40 == 0: exc.append(float(np.trace(P).real - np.sum(Prest*P.T).real))
        if k == nst: break
        sc = 1 + 0.1*math.sin(Om*t) if feed.startswith('squeeze') else 1.0
        if mach == 'A':
            U = UA if UA is not None else expm(-1j*Hd([x*sc for x in d])*h); P = U @ P @ U.conj().T
        elif Vfix is not None: P = Vfix @ P; P = (Vfix @ P.conj().T).conj().T
        else:
            P = V0 @ P; P = (V0 @ P.conj().T).conj().T
            for i in range(N): local(P, i, rot2(d[i]*sc, h))
        if ends == 'leak':
            for i in arm: P[2*i:2*i+2, :] *= math.cos(th_l); P[:, 2*i:2*i+2] *= math.cos(th_l)
        if push:
            G = push_term(w, d, drest, w['kappa'])
            for i in range(N):
                g = G[i] + (bloch(P[2*i:2*i+2, 2*i:2*i+2]) - srest[i]); gm = np.linalg.norm(g)
                if gm > 1e-300:
                    uu = g/gm; an = gm*h; d[i] = d[i]*math.cos(an) + np.cross(uu, d[i])*math.sin(an) + uu*np.dot(uu, d[i])*(1 - math.cos(an))
                dmove = max(dmove, float(np.arccos(np.clip(np.dot(d[i], drest[i])/(np.linalg.norm(d[i])*np.linalg.norm(drest[i])), -1, 1))))
        if feed.startswith('kicks') and t + h >= nextk: local(P, 0, Ksm); nextk += Tk
        trmax = max(trmax, float(np.trace(P).real))
    if _twin: return [S, P]
    if feed == 'kick' and (mach == 'B' or ends == 'leak'): dfar = np.linalg.norm(S[:, far, :] - run(cfg, True)[0][:, far, :], axis=1)
    tt = np.arange(nst + 1)*h; kx = int(lfar/h) - 1; before = float(np.max(dfar[:max(kx, 1)])); mv = np.where(dfar > 1e-9)[0]; first = float(tt[mv[0]]) if len(mv) else None
    q = [S[:, i, :] @ frames[i][0] + 1j*(S[:, i, :] @ frames[i][1]) for i in range(N)]
    def main_rate(sig):
        if len(sig) < 8: return 0.0, 0.0
        sig = sig - sig.mean()
        if np.max(abs(sig)) < 1e-12: return 0.0, 0.0
        n = 1 << int(math.ceil(math.log2(len(sig)*8))); F = np.abs(np.fft.fft(sig*np.hanning(len(sig)), n)); wr = np.abs(2*math.pi*np.fft.fftfreq(n, h)); F = np.where((wr >= 0.05) & (wr <= 5.0), F, 0.0); kk = int(np.argmax(F)); y0, y1, y2 = F[kk - 1], F[kk], F[(kk + 1) % n]; dl = 0.5*(y0 - y2)/(y0 - 2*y1 + y2) if (y0 - 2*y1 + y2) != 0 else 0
        f = (kk + dl)/n; f = f - 1 if f > 0.5 else f; return abs(2*math.pi*f/h), float(np.sqrt(np.mean(abs(sig)**2)))
    i40 = int(40/h) if T_end >= 80 else 0; mid = (i40 + nst)//2; halves = [(i40, mid), (mid, nst + 1)]; meas = [[main_rate(q[i][a:b]) for i in range(N)] for a, b in halves]; free = [omega*r for r in rates]
    locks = []; gears = []
    for i, j in itertools.combinations(range(N), 2):
        if abs(free[i] - free[j]) > 0.05*max(free[i], free[j]):
            ok = all(abs(meas[hh][i][0] - meas[hh][j][0]) < 0.02 and meas[hh][i][1] > 1e-6 and meas[hh][j][1] > 1e-6 for hh in (0, 1))
            if ok: locks.append([i, j, meas[0][i][0], meas[1][i][0]])
        if cfg['clocks'] == 'dilation' and all(meas[hh][x][1] > 1e-6 and meas[hh][x][0] > 0 for hh in (0, 1) for x in (i, j)):
            rat = [meas[hh][i][0]/meas[hh][j][0] for hh in (0, 1)]; fr = free[i]/free[j]
            for a in range(1, 8):
                for b in range(1, 8):
                    if math.gcd(a, b) == 1 and all(abs(r/(a/b) - 1) < 0.005 for r in rat) and abs(fr/(a/b) - 1) >= 0.005: gears.append([i, j, a, b, rat[0], rat[1], fr])
    third = (nst + 1)//3; amp = lambda a, b: float(np.sqrt(np.mean(abs(q[far][a:b] - q[far][a:b].mean())**2)))
    out = dict(cfg); out.update(M=int(M), rank=int(rank), cut_margin=margin, tie_at_start=tie0, trace_start=tr0, trace_end=float(np.trace(P).real), trace_max=trmax, proj_dev=float(np.max(abs(P @ P - P))),
        far_change_before_crossing=before, crossing_time=lfar, first_move_time=first, far_swing_mid=amp(third, 2*third), far_swing_last=amp(2*third, nst + 1), lifted_end=exc[-1], lifted_max=float(max(exc)), lifted_mean=float(np.mean(exc)),
        tie_end=float(np.linalg.norm(P[0:2, 2*far:2*far+2])**2), free_rates=free, rates_half1=[m[0] for m in meas[0]], rates_half2=[m[0] for m in meas[1]], swing_half2=[m[1] for m in meas[1]], locks=locks, gears=gears, ball_turn_max=dmove,
        max_sea_change=float(np.max(np.linalg.norm(S, axis=2))), secs=round(time.time() - t0, 1))
    return out
if __name__ == '__main__':
    cfgs = json.load(open(sys.argv[1])); part, of = int(sys.argv[2]), int(sys.argv[3]); outf = open(sys.argv[4], 'a')
    for n, c in enumerate(cfgs):
        if n % of != part: continue
        try: r = run(c)
        except Exception as e: r = dict(c); r['error'] = repr(e)
        outf.write(json.dumps(r) + '\n'); outf.flush()
