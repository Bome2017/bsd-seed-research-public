# Linear-time Brandt Hecke operators: neighbors via right submodules of I/qI + PARI isometry identification.
from sage.all import ZZ, GF, matrix, Matrix, pari, vector, span, VectorSpace
import itertools
class FastBrandt:
    def __init__(self, B):
        self.B = B; self.Is = B.right_ideals(); self.h = len(self.Is); self.R = B.order_of_level_N()
        self.Qalg = B.quaternion_algebra(); self.Rbasis = self.R.basis()
        self.gram = []; self.init = []; self.bucket = {}
        d0 = abs(int(pari.matdet(self._gram(self.Is[0]))))
        self.tb = max(30, int(3 * d0 ** 0.25) + 1)     # theta bound (nrd/N units) scaled to the lattice
        for i, I in enumerate(self.Is):
            G = self._gram(I); self.gram.append(G); self.init.append(pari.qfisominit(G))
            self.bucket.setdefault(self._inv(G), []).append(i)
        self.n_isotests = 0; self.n_ambig = 0
    def _gram(self, I):
        bas = I.basis(); n = I.norm()
        return pari.matrix(4, 4, [ZZ((x * y.conjugate()).reduced_trace() / n) for x in bas for y in bas])
    def _inv(self, G):
        return tuple(int(c) for c in pari.qfrep(G, self.tb, 1))
    def identify(self, J):
        G = self._gram(J); cands = self.bucket.get(self._inv(G), [])
        iso = []
        for c in cands:
            self.n_isotests += 1
            if pari.qfisom(self.init[c], G) != 0: iso.append(c)
        if len(iso) == 1: return iso[0]
        if not iso: raise RuntimeError('no isometric class')
        self.n_ambig += 1
        for c in iso:
            if self.Is[c].is_right_equivalent(J, 0): return c
        raise RuntimeError('ambiguous, none right-equivalent')
    def neighbors(self, I, q):
        bas = I.basis()
        # matrices of right multiplication by R's basis on I's Z-basis, mod q
        from sage.all import QQ
        Bm = Matrix(QQ, [b.coefficient_tuple() for b in bas])
        def coords(x):
            v = Bm.solve_left(vector(QQ, x.coefficient_tuple())); assert all(c.denominator() == 1 for c in v), 'non-integral coords'; return v
        F = GF(q); mats = [Matrix(F, [[F(ZZ(c)) for c in coords(b * r)] for b in bas]) for r in self.Rbasis]
        V = VectorSpace(F, 4); subs = set(); out = []
        if q <= 3:
            witer = (w for w in V)
        else:
            def _rand():
                n = 0
                while len(subs) < q + 1:
                    n += 1
                    assert n < 400 * (q + 1) ** 2, 'neighbor sampling did not converge'
                    yield V.random_element()
            witer = _rand()
        for w in witer:
            if w == 0: continue
            W = V.subspace([w * Mr for Mr in mats] + [w])
            if W.dimension() != 2: continue
            key = tuple(tuple(r) for r in W.echelonized_basis_matrix())
            if key in subs: continue
            subs.add(key)
            gens = [q * b for b in bas] + [sum(ZZ(c) * bas[k] for k, c in enumerate(v)) for v in W.basis()]
            J = self.Qalg.ideal(self._zbasis(gens), right_order=self.R, check=False)
            out.append(J)
        assert len(out) == q + 1, ('neighbor count', len(out), q)
        return out
    def _zbasis(self, gens):
        from sage.all import lcm
        C = [g.coefficient_tuple() for g in gens]
        d = lcm([c.denominator() for row in C for c in row])
        Mz = Matrix(ZZ, [[ZZ(c * d) for c in row] for row in C]).echelon_form()
        rows = [r for r in Mz.rows() if not r.is_zero()]
        assert len(rows) == 4, ('rank', len(rows))
        Q = self.Qalg; e = Q.basis()
        return [sum((r[k] / d) * e[k] for k in range(4)) for r in rows]
    def hecke_rows(self, q, rows):
        return {i: [self.identify(J) for J in self.neighbors(self.Is[i], q)] for i in rows}
    def hecke(self, q, F):
        from sage.all import matrix as mtx
        M = mtx(F, self.h, self.h, sparse=True)
        for i, I in enumerate(self.Is):
            for J in self.neighbors(I, q):
                assert J.norm() == q * I.norm()
                M[i, self.identify(J)] += 1
        return M
