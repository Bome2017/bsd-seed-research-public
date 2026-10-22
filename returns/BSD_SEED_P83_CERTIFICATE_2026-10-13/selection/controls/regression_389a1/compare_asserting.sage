# F4 fix: the regression ASSERTS (non-zero exit on any disagreement). usage: sage compare_asserting.sage [tamper]
import re, sys
TAMPER = len(sys.argv) > 1 and sys.argv[1] == 'tamper'
E = EllipticCurve([0, 1, 1, -2, 0]); ms = E.modular_symbol(sign=+1, implementation='eclib'); p = 7
EXPECT = {29: (0, 0, 8), 379: (0, 0, 0)}
for l in (29, 379):
    plus = {}
    for line in open(f"msl_m{l}.txt").read().splitlines():
        if not line.startswith("XB "): continue
        m = re.fullmatch(r'XB (\d+) plus \[[^\]]*\] cand (-?\d+)/(\d+) contains (\d+) unique (\d+) minus .*', line)
        assert m, line
        b, h, d, c, u = (int(v) for v in m.groups())
        assert (d, c, u) == (1024, 1, 1) and b not in plus, (l, b)
        plus[b] = QQ(h) / 1024
    if TAMPER and l == 29: plus[1] += 1                        # negative control: one altered symbol must fail
    units = {b for b in range(1, l) if gcd(b, l) == 1}
    assert set(plus) == units, "label coverage"
    exact = {b: QQ(ms(QQ(b) / l)) for b in units}
    assert all(plus[b] == exact[b] for b in units), f"l={l}: pipeline symbols != exact eclib symbols"
    assert all(plus[b] == plus[l - b] for b in units), "symmetry"
    g = primitive_root(l); ind = {}; x = 1
    for e in range(l - 1): ind[x] = e; x = x * g % l
    c = tuple(sum(binomial(ind[a] % p, k) * plus[a] for a in units) for k in range(3))
    assert c == EXPECT[l], f"l={l}: coefficients {c} != {EXPECT[l]}"
    assert c[0] == 0 and GF(p)(c[1]) == 0, "lower-order vanishing"
    print(f"l={l}: PASS  c = {c}  c2 mod 7 = {GF(p)(c[2])}")
print("REGRESSION PASS")
