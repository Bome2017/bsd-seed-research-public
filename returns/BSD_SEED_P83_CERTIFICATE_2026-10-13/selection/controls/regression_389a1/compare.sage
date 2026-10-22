import re
E = EllipticCurve([0, 1, 1, -2, 0]); assert E.label() if hasattr(E, 'label') else True
ms = E.modular_symbol(sign=+1, implementation='eclib'); p = 7
print("Sage real period (Delta>0: 2*omega1):", E.period_lattice().omega(), "; pipeline Omega+ = omega1 = 2.4902125608550550753")
for l in (29, 379):
    txt = open(f"msl_m{l}.txt").read()
    plus = {}
    for line in txt.splitlines():
        if not line.startswith("XB "): continue
        m_ = re.search(r'plus .*? cand (-?\d+)/(\d+) contains (\d) unique (\d)', line)
        b = int(line.split()[1]); h, d, c, u = m_.groups()
        assert c == '1' and u == '1' and int(d) == 1024, (l, b)
        plus[b] = QQ(int(h)) / 1024
    exact = {b: QQ(ms(QQ(b) / l)) for b in range(1, l)}
    ratios = set(plus[b] / exact[b] for b in range(1, l) if exact[b] != 0)
    zeros_agree = all((plus[b] == 0) == (exact[b] == 0) for b in range(1, l))
    g = primitive_root(l)                                   # SPEC: g = smallest primitive root mod l
    ind = {}
    x = 1
    for e in range(l - 1): ind[x] = e; x = (x * g) % l
    xm = {a: ind[a] % p for a in range(1, l)}
    def cs(sym):
        return [sum(binomial(xm[a], k) * sym[a] for a in range(1, l)) for k in range(3)]
    cp, ce = cs(plus), cs(exact)
    print(f"l={l}: g={g}; {len(plus)} symbols identified; pipeline/exact ratio set = {ratios}; zero pattern agrees: {zeros_agree}")
    print(f"   pipeline c0,c1,c2 = {cp}  -> mod 7: {[GF(p)(v) for v in cp]}")
    print(f"   exact    c0,c1,c2 = {ce}  -> mod 7: {[GF(p)(v) for v in ce]}")
    print(f"   symmetry [l-a]=[a]: {all(plus[a] == plus[l - a] for a in range(1, l))};  c0 == 0 exactly: {cp[0] == 0}")
