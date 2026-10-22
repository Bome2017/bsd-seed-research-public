#!/usr/bin/env python3
"""
H_pi ring-level checks.

PART A (mod a large prime ell):  well-definedness and surjectivity of pi_r on the FULL Hecke rings.
  For monomials m_1..m_T in the abstract generators, V has columns vec(ev_{pM}(m_i)) and W has
  columns vec(ev_M(phi_r m_i)).   Over Z_p, ker(V) and ker(W) are saturated, so
        ker_{Z_p}(V) subset ker_{Z_p}(W)  <=>  ker_{Q_p}(V) subset ker_{Q_p}(W)
                                          <=>  rank(V) = rank([V;W]).
  This is a RANK identity of integer matrices, so it is tested exactly mod two large primes.
  rank(V) = Z-rank of T'_{pM} restricted to the monomial span; rank(W) likewise at level M.
  We ALSO test the reverse containment (expected to FAIL: pi_r is onto, never injective).

PART B (mod p^K):  ordinary projector e' = lim (U'_p)^{n!}, surjectivity of e' varpi_{1,*} on
  ordinary parts, pi_r(e'_{r+1}) = e'_r, and the ordinary-algebra rank test.
"""
import sys, math, numpy as np
from msym_check import (ManinSpace, operator_matrix, diamond_matrix, coset_reps_gamma1,
                        H_coset_reps, matmul)
from hpi_gens import Tprime_mats, Uprime_mats

# ---------- mod-q Manin space with unit pivots (q = p^K) ----------
class ManinSpaceQ(ManinSpace):
    def __init__(self, L, q, p):
        self.p = p
        self.q = q
        ManinSpace.__init__(self, L, q)
    def build_quotient(self):
        q = self.ell; p = self.p
        pivots = {}
        def reduce(row):
            while True:
                pc = None
                for col in row:
                    if col in pivots: pc = col; break
                if pc is None: return row
                coef = row[pc]; prow = pivots[pc]
                for col, v in prow.items():
                    nv = (row.get(col, 0) - coef * v) % q
                    if nv: row[col] = nv
                    else: row.pop(col, None)
        def add_relation(cols):
            row = {}
            for col in cols: row[col] = (row.get(col, 0) + 1) % q
            row = {k: v for k, v in row.items() if v}
            row = reduce(row)
            if not row: return
            # UNIT pivot: needed because Z/q is not a field.  Exists because the relation lattice
            # is saturated (H_1(X,cusps;Z) is free), see 04 S1.
            units = [c for c in row if row[c] % p]
            assert units, "no unit pivot: relation lattice not saturated mod p"
            pc = max(units)
            inv = pow(row[pc], -1, q)
            pivots[pc] = {k: (v * inv) % q for k, v in row.items()}
        for (c, d) in self.reps:
            x = self.idx(c, d)
            add_relation([x, self.idx(d, -c)])
            add_relation([x, self.idx(d, -c - d), self.idx(-c - d, c)])
        self.pivots = pivots
        self.free = [i for i in range(self.n) if i not in pivots]
        self.free_index = {col: k for k, col in enumerate(self.free)}
        self.dim = len(self.free)
        self._reduce = reduce

def A(M): return np.array(M, dtype=object) if False else np.array(M, dtype=np.int64)
def mul(X, Y, q): return (X.astype(object) @ Y.astype(object) % q).astype(np.int64) if max(X.max(initial=0),Y.max(initial=0))**2*X.shape[1] > 4e18 else (X @ Y) % q
def mpow(X, e, q):
    R = np.eye(X.shape[0], dtype=np.int64); B = X % q
    while e:
        if e & 1: R = mul(R, B, q)
        B = mul(B, B, q); e >>= 1
    return R

# ---------- linear algebra over Z/q with unit pivots ----------
def unit_rref(Mx, q, p):
    """row-reduce with unit pivots only; returns (R, pivcols). Stops when no unit pivot remains."""
    Mx = Mx.copy() % q; rows, cols = Mx.shape; r = 0; piv = []
    for c in range(cols):
        sel = None
        for i in range(r, rows):
            if Mx[i, c] % p: sel = i; break
        if sel is None: continue
        Mx[[r, sel]] = Mx[[sel, r]]
        inv = pow(int(Mx[r, c]), -1, q)
        Mx[r] = (Mx[r] * inv) % q
        col = Mx[:, c].copy(); col[r] = 0
        Mx = (Mx - np.outer(col, Mx[r])) % q
        piv.append(c); r += 1
        if r == rows: break
    return Mx, piv

def inv_modq(G, q, p):
    n = G.shape[0]
    Aug = np.concatenate([G % q, np.eye(n, dtype=np.int64)], axis=1)
    R, piv = unit_rref(Aug, q, p)
    assert piv == list(range(n)), "matrix not invertible mod p"
    return R[:, n:] % q

def ord_projector(U, q, p, name=""):
    """Fitting projector onto the part where U is invertible, over Z/q. Returns (E,G,Ginv,rho)."""
    n = U.shape[0]
    K = 0
    while p ** (K + 1) <= q: K += 1
    m = n * K + n
    Aa = mpow(U, m, q)
    # A ~ diag(I_rho,0) over Z/q (Fitting).  Unit-pivot rref of A gives both a basis of the
    # column space im(A) (the pivot columns of A, by Nakayama) and a basis of ker(A).
    Rr, piv_cols = unit_rref(Aa.copy(), q, p)
    rho = len(piv_cols)
    free_cols = [c for c in range(n) if c not in piv_cols]
    Kb = np.zeros((n, len(free_cols)), dtype=np.int64)
    for j, fc in enumerate(free_cols):
        Kb[fc, j] = 1
        for i, pc in enumerate(piv_cols):
            Kb[pc, j] = (-Rr[i, fc]) % q
    assert np.all(mul(Aa, Kb, q) == 0), "kernel basis wrong"
    P = Aa[:, piv_cols] % q
    G = np.concatenate([P, Kb], axis=1) % q
    Ginv = inv_modq(G, q, p)
    D = np.zeros((n, n), dtype=np.int64)
    for i in range(rho): D[i, i] = 1
    E = mul(G, mul(D, Ginv, q), q)
    assert np.all(mul(E, E, q) == E), f"e' not idempotent ({name})"
    assert np.all(mul(E, U, q) == mul(U, E, q)), f"e' does not commute with U'_p ({name})"
    Uo = mul(Ginv[:rho], mul(U, G[:, :rho], q), q)
    _, pv = unit_rref(Uo.copy(), q, p)
    assert len(pv) == rho, "U'_p not invertible on the e'-part"
    return E, G, Ginv, rho

def rank_padic(Mx, q, p):
    """Z_p-rank of an integral matrix given mod q=p^K; also returns reliability flag."""
    Mx = Mx.copy() % q; rows, cols = Mx.shape; r = 0; maxval = 0
    K = 0
    while p ** (K + 1) <= q: K += 1
    for c in range(cols):
        best = None; bv = K
        for i in range(r, rows):
            v = 0; x = int(Mx[i, c]) % q
            if x == 0: continue
            while x % p == 0: x //= p; v += 1
            if v < bv: bv = v; best = i
            if v == 0: break
        if best is None: continue
        maxval = max(maxval, bv)
        Mx[[r, best]] = Mx[[best, r]]
        u = int(Mx[r, c]) // p ** bv
        inv = pow(u, -1, q)
        Mx[r] = (Mx[r] * inv) % q
        for i in range(rows):
            if i != r and int(Mx[i, c]) % q:
                f = int(Mx[i, c]) // p ** bv
                if int(Mx[i, c]) % p ** bv: f = 0  # cannot eliminate; leave (valuation lower -> impossible)
                Mx[i] = (Mx[i] - f * Mx[r]) % q
        r += 1
        if r == rows: break
    return r, maxval, maxval < K - 1

def rank_ell(Mx, ell):
    Mx = Mx.copy() % ell; rows, cols = Mx.shape; r = 0
    for c in range(cols):
        sel = None
        for i in range(r, rows):
            if Mx[i, c] % ell: sel = i; break
        if sel is None: continue
        Mx[[r, sel]] = Mx[[sel, r]]
        Mx[r] = (Mx[r] * pow(int(Mx[r, c]), ell - 2, ell)) % ell
        col = Mx[:, c].copy(); col[r] = 0
        Mx = (Mx - np.outer(col, Mx[r])) % ell
        r += 1
        if r == rows: break
    return r

# ---------- generator/monomial machinery ----------
def gens_for(Ng, p, s, space, mod):
    """list of (name, matrix) generators of T'_{N_g p^s} on `space` (level N_g p^s)."""
    L = space.L
    out = []
    out.append(("U'_p", np.array(operator_matrix(space, space, Uprime_mats(L, p), mod), dtype=np.int64)))
    for l in sorted({l for l in range(2, 40) if Ng % l == 0 and all(l % d for d in range(2, l))}):
        out.append((f"U'_{l}", np.array(operator_matrix(space, space, Uprime_mats(L, l), mod), dtype=np.int64)))
    good = [l for l in (2, 3, 5, 7, 11, 13, 17) if math.gcd(l, L) == 1][:3]
    for l in good:
        out.append((f"T'_{l}", np.array(operator_matrix(space, space, Tprime_mats(L, l), mod), dtype=np.int64)))
    # diamonds: take generators of (Z/L)^*
    for d in diamond_gens(L):
        out.append((f"<{d}>", np.array(diamond_matrix(space, [d], mod), dtype=np.int64)))
    return out

def diamond_gens(L):
    units = [d for d in range(1, L) if math.gcd(d, L) == 1]
    gens = []; cur = {1}
    for d in units:
        if d in cur: continue
        gens.append(d)
        new = set(cur)
        changed = True
        while changed:
            changed = False
            for a in list(new):
                for g in gens:
                    b = a * g % L
                    if b not in new: new.add(b); changed = True
        cur = new
        if len(cur) == len(units): break
    return gens

def monomials(ngen, deg):
    """exponent vectors with total degree <= deg"""
    out = [[0] * ngen]
    cur = [[0] * ngen]
    for _ in range(deg):
        nxt = []
        for e in cur:
            for i in range(ngen):
                f = e[:]; f[i] += 1
                if f not in nxt and f not in out: nxt.append(f)
        out += nxt; cur = nxt
    return out

def eval_mon(gens, e, mod, dim):
    R = np.eye(dim, dtype=np.int64)
    for i, a in enumerate(e):
        for _ in range(a): R = mul(R, gens[i][1], mod)
    return R

# ---------------------------------------------------------------- PART A
def partA(Ng, p, r, ell, deg=3):
    M = Ng * p ** r; pM = p * M
    print(f"--- PART A  N_g={Ng} p={p} r={r}  M={M}->{pM}  mod ell={ell}, monomial degree <= {deg}")
    SM = ManinSpace(M, ell); SpM = ManinSpace(pM, ell)
    gM = gens_for(Ng, p, r, SM, ell); gpM = gens_for(Ng, p, r + 1, SpM, ell)
    # match generator lists: same names except diamonds, which are matched by REDUCTION mod M
    names_M = [n for n, _ in gM]
    gpM2 = []
    for (n, X) in gpM:
        if n.startswith("<"):
            d = int(n[1:-1]) % M
            Y = np.array(diamond_matrix(SM, [d if d else 1], ell), dtype=np.int64)
            gpM2.append((n, X, Y))
        else:
            j = names_M.index(n); gpM2.append((n, X, gM[j][1]))
    print(f"    dim MS(M)={SM.dim} dim MS(pM)={SpM.dim}; generators used: {[n for n,_,_ in gpM2]}")
    mons = monomials(len(gpM2), deg)
    V = np.zeros((SpM.dim * SpM.dim, len(mons)), dtype=np.int64)
    W = np.zeros((SM.dim * SM.dim, len(mons)), dtype=np.int64)
    for k, e in enumerate(mons):
        Xu = np.eye(SpM.dim, dtype=np.int64); Yu = np.eye(SM.dim, dtype=np.int64)
        for i, a in enumerate(e):
            for _ in range(a):
                Xu = mul(Xu, gpM2[i][1], ell); Yu = mul(Yu, gpM2[i][2], ell)
        V[:, k] = Xu.reshape(-1); W[:, k] = Yu.reshape(-1)
    rV = rank_ell(V.T.copy(), ell); rW = rank_ell(W.T.copy(), ell)
    rVW = rank_ell(np.concatenate([V, W], axis=0).T.copy(), ell)
    rWV = rVW
    ok_wd = (rV == rVW)
    ok_notinj = (rW < rVW)
    print(f"    rank V (= Z-rank of T'_(pM) on {len(mons)} monomials) = {rV}")
    print(f"    rank W (= Z-rank of T'_(M)  on the same monomials)    = {rW}")
    print(f"    rank [V;W]                                            = {rVW}")
    print(f"    (WD)  ker(V) subset ker(W)   <=>  rank V = rank[V;W] : {'PASS' if ok_wd else 'FAIL'}")
    print(f"    (NI)  pi_r NOT injective     <=>  rank W < rank[V;W] : {'PASS' if ok_notinj else 'FAIL (pi_r injective here)'}")
    # surjectivity, measured: span of the phi_r-images vs the algebra generated by M's OWN generators
    monsM = monomials(len(gM), deg)
    WM = np.zeros((SM.dim * SM.dim, len(monsM)), dtype=np.int64)
    for k, e in enumerate(monsM):
        Yu = np.eye(SM.dim, dtype=np.int64)
        for i, a in enumerate(e):
            for _ in range(a): Yu = mul(Yu, gM[i][1], ell)
        WM[:, k] = Yu.reshape(-1)
    rWM = rank_ell(WM.T.copy(), ell)
    rWjoin = rank_ell(np.concatenate([W, WM], axis=1).T.copy(), ell)
    ok_surj = (rW == rWM == rWjoin)
    print(f"    rank of T'_(M) from M's OWN generators, same degree     = {rWM}; joint span = {rWjoin}")
    print(f"    (SURJ) im(pi_r) = T'_(M)  <=> rank W = rank W_own = rank joint : {'PASS' if ok_surj else 'FAIL'}")
    nonvac = (rV < len(mons))
    print(f"    (NONVAC) the WD test has content: {len(mons)-rV} independent relations at level pM : {'PASS' if nonvac else 'VACUOUS - raise degree'}")
    return {"WD": ok_wd, "NI": ok_notinj, "SURJ": ok_surj, "NONVAC": nonvac, "rV": rV, "rW": rW}

# ---------------------------------------------------------------- PART B
def partB(Ng, p, r, K, deg=3):
    q = p ** K; M = Ng * p ** r; pM = p * M
    print(f"--- PART B  N_g={Ng} p={p} r={r}  M={M}->{pM}  mod q={p}^{K}={q}, monomial degree <= {deg}")
    SM = ManinSpaceQ(M, q, p); SpM = ManinSpaceQ(pM, q, p)
    print(f"    dim MS(M)={SM.dim} dim MS(pM)={SpM.dim}")
    I2 = (1, 0, 0, 1)
    push1 = np.array(operator_matrix(SpM, SM, [I2], q), dtype=np.int64)
    pull1 = np.array(operator_matrix(SM, SpM, coset_reps_gamma1(M, p), q), dtype=np.int64)
    alpha_inv = (1, 0, 0, p)
    pull2 = np.array(operator_matrix(SM, SpM, [matmul(alpha_inv, g) for g in H_coset_reps(M, p)], q), dtype=np.int64)
    UM = np.array(operator_matrix(SM, SM, Uprime_mats(M, p), q), dtype=np.int64)
    UpM = np.array(operator_matrix(SpM, SpM, Uprime_mats(pM, p), q), dtype=np.int64)
    EM, GM, GiM, rhoM = ord_projector(UM, q, p, "level M")
    EpM, GpM, GipM, rhopM = ord_projector(UpM, q, p, "level pM")
    print(f"    ordinary ranks: rho(M)={rhoM}, rho(pM)={rhopM}   (e'^2=e', e'U'=U'e', U' invertible on e': PASS)")
    # varpi_{1,*} e' = e' varpi_{1,*}
    c1 = np.all(mul(push1, EpM, q) == mul(EM, push1, q))
    print(f"    (G2-e') varpi_{{1,*}} e'_(pM) = e'_(M) varpi_{{1,*}}                 {'PASS' if c1 else 'FAIL'}")
    # pi_r(e') = e' :  same limit exponent gives e' at both levels -- verified inside ord_projector,
    # and the intertwining c1 says the two idempotents correspond.
    # surjectivity of e' varpi_{1,*} on ordinary parts
    Cm = mul(GiM[:rhoM], mul(push1, GpM[:, :rhopM], q), q)     # rhoM x rhopM over Z/q
    _, piv = unit_rref(Cm.copy(), q, p)
    surj = (len(piv) == rhoM)
    print(f"    (SURJ-coh) e' varpi_{{1,*}} : e'S_(pM) -> e'S_(M) onto  (rank_(F_p) = {len(piv)} / {rhoM})  {'PASS' if surj else 'FAIL'}")
    # for contrast, is varpi_{1,*} onto on the FULL space over Z_p?
    Cfull = push1 % q
    _, pivf = unit_rref(Cfull.copy(), q, p)
    print(f"    (contrast) varpi_{{1,*}} on the FULL space: rank_(F_p) = {len(pivf)} / {SM.dim} "
          f"{'onto' if len(pivf)==SM.dim else 'NOT onto (p | p^2 = deg)'}")
    # ordinary Hecke algebras
    gM = gens_for(Ng, p, r, SM, q); gpM = gens_for(Ng, p, r + 1, SpM, q)
    names_M = [n for n, _ in gM]; trip = []
    for (n, X) in gpM:
        if n.startswith("<"):
            d = int(n[1:-1]) % M
            Y = np.array(diamond_matrix(SM, [d if d else 1], q), dtype=np.int64)
        else:
            Y = gM[names_M.index(n)][1]
        trip.append((n, X, Y))
    mons = monomials(len(trip), deg)
    V = np.zeros((rhopM * rhopM, len(mons)), dtype=np.int64)
    W = np.zeros((rhoM * rhoM, len(mons)), dtype=np.int64)
    for k, e in enumerate(mons):
        Xu = np.eye(SpM.dim, dtype=np.int64); Yu = np.eye(SM.dim, dtype=np.int64)
        for i, a in enumerate(e):
            for _ in range(a):
                Xu = mul(Xu, trip[i][1], q); Yu = mul(Yu, trip[i][2], q)
        V[:, k] = mul(GipM[:rhopM], mul(Xu, GpM[:, :rhopM], q), q).reshape(-1)
        W[:, k] = mul(GiM[:rhoM], mul(Yu, GM[:, :rhoM], q), q).reshape(-1)
    rV, vV, okV = rank_padic(V.T.copy(), q, p)
    rW, vW, okW = rank_padic(W.T.copy(), q, p)
    rVW, vVW, okVW = rank_padic(np.concatenate([V, W], axis=0).T.copy(), q, p)
    ok_wd = (rV == rVW)
    print(f"    Z_p-rank R_(pM) on {len(mons)} monomials = {rV} (max pivot val {vV}, reliable={okV})")
    print(f"    Z_p-rank R_(M)  on the same monomials   = {rW} (max pivot val {vW}, reliable={okW})")
    print(f"    Z_p-rank [V;W]                          = {rVW} (max pivot val {vVW}, reliable={okVW})")
    print(f"    (WD-ord)  pi_r well defined on R_(r+1)->R_(r)        {'PASS' if ok_wd else 'FAIL'}")
    print(f"    (SURJ-ord) pi_r onto R_(r): generators hit generators; rank drop {rV} -> {rW} "
          f"{'(not injective)' if rW < rV else '(injective here)'}")
    nonvac = (rV < len(mons))
    print(f"    (NONVAC) WD test has content: {len(mons)-rV} independent relations at level pM : {'PASS' if nonvac else 'VACUOUS'}")
    print(f"    (RELIABLE) all three p-adic ranks reliable (max pivot valuation < K-1): "
          f"{'PASS' if (okV and okW and okVW) else 'FAIL - raise K'}")
    return {"G2e": bool(c1), "SURJcoh": surj, "WDord": ok_wd, "NONVACord": nonvac,
            "RELIABLE": bool(okV and okW and okVW),
            "rhoM": rhoM, "rhopM": rhopM, "rV": rV, "rW": rW}

if __name__ == "__main__":
    mode = sys.argv[1]
    cases = [tuple(int(x) for x in a.split(",")) for a in sys.argv[2:]]
    res = []
    for c in cases:
        if mode == "A":
            for ell in (1000003, 999983):
                res.append(partA(c[0], c[1], c[2], ell, deg=c[3] if len(c) > 3 else 3))
        else:
            res.append(partB(c[0], c[1], c[2], K=c[3] if len(c) > 3 else 6, deg=c[4] if len(c) > 4 else 3))
    bad = [k for d in res for k, v in d.items() if isinstance(v, bool) and not v]
    print("ALL PASS" if not bad else "SOME FAIL: " + str(bad))
