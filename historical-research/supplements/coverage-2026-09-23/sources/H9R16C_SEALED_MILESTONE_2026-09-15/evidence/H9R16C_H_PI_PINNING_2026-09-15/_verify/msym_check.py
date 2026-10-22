#!/usr/bin/env python3
"""
Exact (mod a large prime) verification of the finite-level modified-pairing compatibility
    varpi_1^* A_r varpi_{1,*} = d_r A_{r+1} N_{r+1,r},   A_s = W_{N p^s}^{-1} (U'_p)^s,
on weight-2 modular symbols (H_1(X_1(L), cusps; Q) via Manin symbols), together with the auxiliary
cycle identities used in the derivation (02/03):
    (i)   varpi_{1,*} varpi_1^*   = p^2                        on MS(M)
    (ii)  varpi_{2,*} U'_p        = p varpi_{1,*}              (KLZ17 Prop 2.4.5, k=0)
    (iii) varpi_2^*  varpi_{1,*}  = U'_p N                     on MS(pM)   <-- norm element identity
    (iv)  varpi_1^* W_M           = W_{pM} varpi_2^*           (Lemma W)
    (v)   varpi_1^* W_M U'^r varpi_{1,*} = W_{pM} U'^{r+1} N   (MPC_r, d_r = 1)
    (vi)  W^2 = 1,  W U' = U W (U = transpose),  varpi_{1,*} U' = U' varpi_{1,*},  N U' = U' N
Conventions (01): varpi_1: tau->tau, varpi_2: tau->p tau; U'_p = classical U_p formula on modular symbols
{a,b} -> sum_b {(a+b)/p,(b+b)/p} (= KLZ17/DR22 U'_p = pi_{1*} pi_2^* on H^1 under Poincare duality);
W_L = [[0,-1],[L,0]]; <d>[c,d'] = [dc, dd'].
"""
import sys, math, random
from fractions import Fraction

# ---------------- basic arithmetic ----------------
def egcd(a, b):
    if b == 0: return (a, 1, 0)
    g, x, y = egcd(b, a % b)
    return (g, y, x - (a // b) * y)

def lift_to_sl2(c, d, L):
    """Return integer matrix [[a,b],[cc,dd]] in SL_2(Z) with (cc,dd) = (c,d) mod L."""
    c0, d0 = c % L, d % L
    for t in range(0, 50):
        for s in range(0, 50):
            cc, dd = c0 + t * L, d0 + s * L
            if math.gcd(cc, dd) == 1:
                g, x, y = egcd(cc, dd)   # x*cc + y*dd = 1
                a, b = y, -x             # a*dd - b*cc = y*dd + x*cc = 1
                assert a * dd - b * cc == 1
                return (a, b, cc, dd)
    raise ValueError("no lift")

# cusps: (num, den) with den >= 0, gcd = 1; infinity = (1,0)
def cusp(n, d):
    if d == 0: return (1, 0)
    if d < 0: n, d = -n, -d
    g = math.gcd(abs(n), d)
    if g == 0: return (0, 1)
    return (n // g, d // g)

def act(mat, cu):
    a, b, c, d = mat
    n, m = cu
    return cusp(a * n + b * m, c * n + d * m)

def matmul(A, B):
    a, b, c, d = A; e, f, g, h = B
    return (a * e + b * g, a * f + b * h, c * e + d * g, c * f + d * h)

# ---------------- Manin symbols ----------------
class ManinSpace:
    def __init__(self, L, ell):
        self.L = L; self.ell = ell
        syms = {}
        reps = []
        for c in range(L):
            for d in range(L):
                if math.gcd(math.gcd(c, d), L) != 1: continue
                key = self.canon(c, d)
                if key not in syms:
                    syms[key] = len(reps); reps.append(key)
        self.syms = syms; self.reps = reps; self.n = len(reps)
        self.build_quotient()

    def canon(self, c, d):
        L = self.L
        c %= L; d %= L
        c2, d2 = (-c) % L, (-d) % L
        return min((c, d), (c2, d2))

    def idx(self, c, d):
        return self.syms[self.canon(c, d)]

    def build_quotient(self):
        """Sparse elimination mod ell of the Manin relations x + x sigma = 0, x + x tau + x tau^2 = 0."""
        ell = self.ell; L = self.L
        pivots = {}   # pivot col -> row dict (col->coef), row normalized with pivot coef 1
        def reduce(row):
            # row: dict col->coef mod ell; eliminate pivot columns
            changed = True
            while True:
                pc = None
                for col in row:
                    if col in pivots: pc = col; break
                if pc is None: return row
                coef = row[pc]; prow = pivots[pc]
                for col, v in prow.items():
                    nv = (row.get(col, 0) - coef * v) % ell
                    if nv: row[col] = nv
                    else: row.pop(col, None)
        def add_relation(cols):
            row = {}
            for col in cols:
                row[col] = (row.get(col, 0) + 1) % ell
            row = {k: v for k, v in row.items() if v}
            row = reduce(row)
            if not row: return
            pc = max(row)   # choose largest column as pivot
            inv = pow(row[pc], ell - 2, ell)
            row = {k: (v * inv) % ell for k, v in row.items()}
            # keep other pivot rows reduced w.r.t. new pivot? not necessary for correctness of reduce(),
            # since reduce() loops until no pivot column remains.
            pivots[pc] = row
        for (c, d) in self.reps:
            x = self.idx(c, d)
            xs = self.idx(d, -c)                 # (c,d) sigma, sigma = [[0,-1],[1,0]]
            add_relation([x, xs])
            xt = self.idx(d, -c - d)             # (c,d) tau, tau = [[0,-1],[1,-1]]
            xt2 = self.idx(-c - d, c)            # (c,d) tau^2
            add_relation([x, xt, xt2])
        self.pivots = pivots
        self.free = [i for i in range(self.n) if i not in pivots]
        self.free_index = {col: k for k, col in enumerate(self.free)}
        self.dim = len(self.free)
        self._reduce = reduce

    def coords(self, formal):
        """formal: dict Manin-index -> coeff. Return coordinate list (len dim) mod ell."""
        row = {k: v % self.ell for k, v in formal.items() if v % self.ell}
        row = self._reduce(row)
        vec = [0] * self.dim
        for col, v in row.items():
            vec[self.free_index[col]] = v
        return vec

    # ---- modular symbols {a,b} -> formal sum of Manin symbols ----
    def modsym0(self, x, acc, sign=1):
        """add {0, x} to acc (dict index->coef)."""
        n, d = x
        if d == 0:   # {0, infinity} = [0,1]
            i = self.idx(0, 1); acc[i] = acc.get(i, 0) + sign; return
        if n == 0: return
        # {0,x} = {0,inf} + sum_k {p_{k-1}/q_{k-1}, p_k/q_k}
        i = self.idx(0, 1); acc[i] = acc.get(i, 0) + sign
        # continued fraction convergents of n/d
        pm1, qm1 = 1, 0
        p0, q0 = None, None
        num, den = n, d
        pk_1, qk_1 = 1, 0      # p_{-1}, q_{-1}
        pk_2, qk_2 = 0, 1      # p_{-2}, q_{-2}
        while True:
            a = num // den
            pk = a * pk_1 + pk_2; qk = a * qk_1 + qk_2
            # symbol {p_{k-1}/q_{k-1}, p_k/q_k}: matrix [[pk, pk_1],[qk, qk_1]] det = pk*qk_1 - pk_1*qk
            det = pk * qk_1 - pk_1 * qk
            if det == 1:
                i = self.idx(qk, qk_1)
            else:
                assert det == -1
                i = self.idx(-qk, qk_1)
            acc[i] = acc.get(i, 0) + sign
            rem = num - a * den
            if rem == 0: break
            num, den = den, rem
            pk_2, qk_2, pk_1, qk_1 = pk_1, qk_1, pk, qk
        assert pk == n and qk == d or pk == -n and qk == -d, (pk, qk, n, d)

    def modsym(self, a, b, acc, sign=1):
        """add {a,b} = {0,b} - {0,a}"""
        self.modsym0(b, acc, sign)
        self.modsym0(a, acc, -sign)

# ---------------- operators ----------------
def path_of_symbol(space, i):
    c, d = space.reps[i]
    a, b, cc, dd = lift_to_sl2(c, d, space.L)
    g = (a, b, cc, dd)
    return act(g, (0, 1)), act(g, (1, 0))   # (g0, g inf)

def operator_matrix(src, tgt, mats, ell):
    """Matrix (list of columns) of x -> sum_beta {beta g0, beta g inf} from src quotient to tgt quotient."""
    cols = []
    for k, i in enumerate(src.free):
        a0, ainf = path_of_symbol(src, i)
        acc = {}
        for beta in mats:
            tgt.modsym(act(beta, a0), act(beta, ainf), acc)
        cols.append(tgt.coords(acc))
    # return as list of rows
    n_rows = tgt.dim; n_cols = src.dim
    M = [[cols[j][i] % ell for j in range(n_cols)] for i in range(n_rows)]
    return M

def diamond_matrix(space, dlist, ell):
    """Matrix of sum_{d in dlist} <d> on the quotient: [c,d'] -> [dc, dd']."""
    cols = []
    for i in space.free:
        c, d0 = space.reps[i]
        acc = {}
        for d in dlist:
            j = space.idx(d * c, d * d0)
            acc[j] = acc.get(j, 0) + 1
        cols.append(space.coords(acc))
    return [[cols[j][i] % ell for j in range(space.dim)] for i in range(space.dim)]

def mmul(A, B, ell):
    n, m, k = len(A), len(B), len(B[0]) if B else 0
    assert len(A[0]) == m
    Bt = list(zip(*B))
    return [[sum(A[i][t] * Bt[j][t] for t in range(m)) % ell for j in range(k)] for i in range(n)]

def madd(A, B, ell, cb=1):
    return [[(A[i][j] + cb * B[i][j]) % ell for j in range(len(A[0]))] for i in range(len(A))]

def mscale(A, c, ell):
    return [[(c * A[i][j]) % ell for j in range(len(A[0]))] for i in range(len(A))]

def is_zero(A):
    return all(v == 0 for row in A for v in row)

def identity(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def rank_mod(A, ell):
    A = [row[:] for row in A]; r = 0; rows = len(A); cols = len(A[0]) if A else 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if A[i][c] % ell: piv = i; break
        if piv is None: continue
        A[r], A[piv] = A[piv], A[r]
        inv = pow(A[r][c], ell - 2, ell)
        A[r] = [(v * inv) % ell for v in A[r]]
        for i in range(rows):
            if i != r and A[i][c] % ell:
                f = A[i][c]
                A[i] = [(A[i][j] - f * A[r][j]) % ell for j in range(cols)]
        r += 1
    return r

def coset_reps_gamma1(M, p):
    """Right coset representatives of Gamma_1(pM) \\ Gamma_1(M): bottom rows (c,d) mod pM, c=0 (M), d=1 (M)."""
    reps = []
    for j in range(p):
        for i in range(p):
            c, d = j * M, 1 + i * M
            a, b, cc, dd = lift_to_sl2(c, d, p * M)
            assert cc % M == 0 and dd % M == 1
            reps.append((a, b, cc, dd))
    return reps

def H_coset_reps(M, p):
    """Right coset reps of H \\ Gamma_1(M), H = {b = 0 (p), d = 1 (pM)} cap Gamma_1(M): [[1,b],[0,1]] delta_d, d in K."""
    reps = []
    K = [1 + i * M for i in range(p)]   # d = 1 mod M, mod pM
    for d in K:
        # delta_d in Gamma_1(M) cap Gamma^0(p) cap Gamma_0(pM) with lower-right = d (mod pM)
        found = None
        for s in range(0, 400):
            dd = d + s * p * M
            if math.gcd(dd, p * M) != 1: continue
            # need a with a*dd = 1 mod p^2 M, then b = (a*dd-1)/(pM) is = 0 mod p
            mod = p * p * M
            g, x, y = egcd(dd % mod, mod)
            if g != 1: continue
            a = x % mod
            for t in range(0, 50):
                aa = a + t * mod
                if aa == 0: continue
                b = (aa * dd - 1) // (p * M)
                assert (aa * dd - 1) % (p * M) == 0
                if b % p == 0:
                    found = (aa, b, p * M, dd); break
            if found: break
        assert found is not None
        a, b, c, dd = found
        assert a * dd - b * c == 1 and b % p == 0 and c % (p * M) == 0 and dd % (p * M) == d % (p * M)
        for bb in range(p):
            reps.append(matmul((1, bb, 0, 1), found))
    return reps

def run_case(Ng, p, r, ell, verbose=True):
    M = Ng * p ** r; pM = p * M
    print(f"=== case N_g={Ng}, p={p}, r={r}: levels M={M} -> pM={pM}, prime={ell}")
    SM = ManinSpace(M, ell); SpM = ManinSpace(pM, ell)
    print(f"  Manin symbols: {SM.n} / {SpM.n};  dim MS(M)={SM.dim}, dim MS(pM)={SpM.dim}")
    I2 = (1, 0, 0, 1)
    alpha = (p, 0, 0, 1)          # tau -> p tau
    alpha_inv = (1, 0, 0, p)      # tau -> tau/p (projective inverse)
    Ubeta = [(1, b, 0, p) for b in range(p)]                 # U'_p (classical formula on symbols)
    Utbeta = [(p, 0, a * M, 1) for a in range(p)]            # transpose U_p at level M
    Utbeta_pM = [(p, 0, a * pM, 1) for a in range(p)]        # transpose U_p at level pM
    wM = (0, -1, M, 0); wpM = (0, -1, pM, 0)

    pi1_push = operator_matrix(SpM, SM, [I2], ell)                     # varpi_{1,*}: pM -> M
    pi1_pull = operator_matrix(SM, SpM, coset_reps_gamma1(M, p), ell)  # varpi_1^*: M -> pM
    pi2_push = operator_matrix(SpM, SM, [alpha], ell)                  # varpi_{2,*}
    pi2_pull = operator_matrix(SM, SpM, [matmul(alpha_inv, g) for g in H_coset_reps(M, p)], ell)  # varpi_2^*
    U_M = operator_matrix(SM, SM, Ubeta, ell); U_pM = operator_matrix(SpM, SpM, Ubeta, ell)
    Ut_M = operator_matrix(SM, SM, Utbeta, ell); Ut_pM = operator_matrix(SpM, SpM, Utbeta_pM, ell)
    W_M = operator_matrix(SM, SM, [wM], ell); W_pM = operator_matrix(SpM, SpM, [wpM], ell)
    K = [1 + i * M for i in range(p)]
    N_pM = diamond_matrix(SpM, K, ell)

    res = {}
    def check(name, A, B):
        ok = is_zero(madd(A, B, ell, -1))
        res[name] = ok
        print(f"  {name:55s} {'PASS' if ok else 'FAIL'}")
        return ok
    # sanity
    check("(vi-a) W_M^2 = 1", mmul(W_M, W_M, ell), identity(SM.dim))
    check("(vi-b) W_pM^2 = 1", mmul(W_pM, W_pM, ell), identity(SpM.dim))
    check("(vi-c) W_M U'_M = U^t_M W_M  (W intertwines U' and U)", mmul(W_M, U_M, ell), mmul(Ut_M, W_M, ell))
    check("(vi-d) varpi_{1,*} U'_pM = U'_M varpi_{1,*}", mmul(pi1_push, U_pM, ell), mmul(U_M, pi1_push, ell))
    check("(vi-e) N U' = U' N on MS(pM)", mmul(N_pM, U_pM, ell), mmul(U_pM, N_pM, ell))
    check("(i)    varpi_{1,*} varpi_1^* = p^2", mmul(pi1_push, pi1_pull, ell), mscale(identity(SM.dim), p * p, ell))
    check("(i')   varpi_{2,*} varpi_2^* = p^2", mmul(pi2_push, pi2_pull, ell), mscale(identity(SM.dim), p * p, ell))
    check("(ii)   varpi_{2,*} U'_pM = p varpi_{1,*}  [KLZ17 Prop 2.4.5]", mmul(pi2_push, U_pM, ell), mscale(pi1_push, p, ell))
    check("(ii')  varpi_{2,*} varpi_1^* = p U^t_M   [02 S2(a)]", mmul(pi2_push, pi1_pull, ell), mscale(Ut_M, p, ell))
    check("(ii'') varpi_{1,*} varpi_2^* = p U'_M   [02 S2(a)]", mmul(pi1_push, pi2_pull, ell), mscale(U_M, p, ell))
    check("(iii)  varpi_2^* varpi_{1,*} = U'_pM N   [NORM ELEMENT]", mmul(pi2_pull, pi1_push, ell), mmul(U_pM, N_pM, ell))
    check("(iv)   varpi_1^* W_M = W_pM varpi_2^*   [Lemma W]", mmul(pi1_pull, W_M, ell), mmul(W_pM, pi2_pull, ell))
    check("(iv')  varpi_2^* W_M = W_pM varpi_1^*   [Lemma W]", mmul(pi2_pull, W_M, ell), mmul(W_pM, pi1_pull, ell))
    # MPC
    Ar = W_M
    for _ in range(r): Ar = mmul(Ar, U_M, ell)          # A_r = W_M U'^r
    Ar1 = W_pM
    for _ in range(r + 1): Ar1 = mmul(Ar1, U_pM, ell)   # A_{r+1} = W_pM U'^{r+1}
    LHS = mmul(pi1_pull, mmul(Ar, pi1_push, ell), ell)
    RHS = mmul(Ar1, N_pM, ell)
    ok = check(f"(v)    varpi_1^* A_{r} varpi_(1,*) = A_{r+1} N_{r+1,r}   [MPC_{r}, d_r = 1]", LHS, RHS)
    print(f"         rank(LHS) = {rank_mod(LHS, ell)}, rank(RHS) = {rank_mod(RHS, ell)}, dim MS(M) = {SM.dim}")
    # exclude other constants: is LHS = c*RHS for some c != 1? (only if RHS != 0)
    if not is_zero(RHS):
        for c in [p, pow(p, ell - 2, ell), p * p, pow(p * p, ell - 2, ell), ell - 1]:
            if is_zero(madd(LHS, mscale(RHS, c, ell), ell, -1)):
                print(f"  WARNING: LHS also equals {c} * RHS")
    # also the U-version on transposes: varpi_1^* varpi_{2,*} = N U^t ? (transpose of iii)
    check("(iii^t) varpi_1^* varpi_{2,*} = U^t_pM N   [transpose of iii]", mmul(pi1_pull, pi2_push, ell), mmul(Ut_pM, N_pM, ell))
    return res

if __name__ == "__main__":
    cases = [(5, 3, 1), (2, 3, 2), (4, 5, 1), (7, 2, 1), (3, 2, 2), (1, 5, 2), (1, 7, 1)]
    if len(sys.argv) > 1:
        cases = [tuple(int(x) for x in arg.split(",")) for arg in sys.argv[1:]]
    allok = True
    for (Ng, p, r) in cases:
        for ell in (1000003, 999983):
            res = run_case(Ng, p, r, ell)
            allok &= all(res.values())
    print("ALL PASS" if allok else "SOME FAIL")
