#!/usr/bin/env python3
"""Acceptance checker for the singleton Ota witness (SINGLETON_SPEC v1.1). Fixes audit findings F2, F3 and F5.

Verdicts and exit codes:
  NONZERO            (0)  every check passed and c2 != 0 (mod p). Ota Thm 1.5/6.4 applies at the audited grade:
                          Sha[p] = 0, hence Sha[p^inf] = 0.
  INCONCLUSIVE_ZERO  (3)  every check passed and c2 == 0 (mod p). Nothing follows; try the next auxiliary prime.
  INVALID            (2)  a binding, integrity, consistency or admissibility check failed (reasons listed). Fails closed.

A Stage-C PASS alone is never a certificate. Only this checker's NONZERO verdict, on a run whose manifest binds the
engine, the parameters and the coefficient receipts, is.
Standard library only; exact rational arithmetic throughout.
"""
import argparse, glob, hashlib, json, os, re, sys
from fractions import Fraction as F
from math import comb, gcd

XB = re.compile(r'XB (\d+) plus \[[^\]]*\] cand (-?\d+)/(\d+) contains (\d+) unique (\d+) '
                r'minus \[[^\]]*\] cand (-?\d+)/(\d+) contains (\d+) unique (\d+)')
COUNT = re.compile(r'COUNT smooth (\d+) pairs (\d+) sum (\d+) T (\d+) identity (\d+)')
ROOT = re.compile(r'AP_SEGROOT_SHA256 ([0-9a-f]{64}) segments (\d+)')
DET = re.compile(r'XB_PLUS_DETERMINED (\d+) of (\d+) \(lattice 1/(\d+) Z\)')


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for block in iter(lambda: f.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def prime_factors(n):
    out, d = [], 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def smallest_primitive_root(l):
    fs = prime_factors(l - 1)
    return next(g for g in range(2, l) if all(pow(g, (l - 1) // q, l) != 1 for q in fs))


def point_count(a, l):
    """#E(F_l) for y^2 + a1 xy + a3 y = x^3 + a2 x^2 + a4 x + a6, by brute force (l small)."""
    a1, a2, a3, a4, a6 = (x % l for x in a)
    n = 1
    for x in range(l):
        for y in range(l):
            if (y * y + a1 * x * y + a3 * y - (x ** 3 + a2 * x * x + a4 * x + a6)) % l == 0:
                n += 1
    return n


def modp(q, p):
    if q.denominator % p == 0:
        raise ValueError(f'denominator {q.denominator} not a {p}-unit')
    return q.numerator * pow(q.denominator, -1, p) % p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--msl', required=True)
    ap.add_argument('--units', required=True, help='the msl work-unit directory (holds PARAMS)')
    ap.add_argument('--manifest', required=True, help='RUN_MANIFEST.json written by the launcher')
    ap.add_argument('--receipts', required=True, help='glob of verifier logs holding the SEG receipts')
    ap.add_argument('--arbcore', required=True, help='path of the arbcore binary that was run')
    ap.add_argument('--curve', required=True, help='"a1 a2 a3 a4 a6"')
    ap.add_argument('--N', type=int, required=True)
    ap.add_argument('--p', type=int, required=True)
    ap.add_argument('--l', type=int, required=True)
    ap.add_argument('--Q', type=int, required=True)
    ap.add_argument('--sign', type=int, required=True)
    ap.add_argument('--T', type=int, required=True)
    ap.add_argument('--segq', type=int, required=True)
    ap.add_argument('--latden', type=int, required=True)
    ap.add_argument('--apdir', required=True)
    ap.add_argument('--pinned-segroot', help='expected AP_SEGROOT (hex), if pinned in advance')
    ap.add_argument('--out', help='write the JSON report here')
    A = ap.parse_args()
    reasons, info = [], {}
    fail = reasons.append
    curve = [int(x) for x in A.curve.split()]
    p, l, LAT = A.p, A.l, A.latden

    # --- admissibility of the singleton S = {l} (spec §2, k = 1 model)
    if not (is_prime(p) and p >= 5):
        fail('p must be a prime >= 5')
    if not is_prime(l):
        fail('l is not prime')
    if l == p or A.N % l == 0:
        fail('l divides pN')
    if (l - 1) % p != 0:
        fail('l is not 1 mod p')
    elif ((l - 1) // p) % p == 0:
        fail('v_p(l-1) > 1: outside the frozen k = 1 model')
    n_l = point_count(curve, l)
    info['E_Fl_order'] = n_l
    if n_l % p == 0:
        fail('p divides #E(F_l): cyclicity of E(F_l)[p] is not decided by this checker (fail closed)')
    if A.Q != A.N:
        fail('Q must equal N for an auxiliary prime not dividing N (M = 1)')

    # --- parameter binding (F3): PARAMS must equal the frozen command line; no stale or foreign outputs
    try:
        params = open(os.path.join(A.units, 'PARAMS')).read().strip()
    except OSError:
        params = None
        fail('PARAMS missing in the unit directory')
    expect = ' '.join(['msl'] + [str(x) for x in curve] + [str(l), str(A.Q), str(A.sign), str(A.T), str(A.segq),
                                                           os.path.realpath(A.apdir), os.path.realpath(A.units), str(LAT)])
    if params is not None:
        toks = params.split()
        if len(toks) != 14:
            fail(f'PARAMS has {len(toks)} fields, expected 14')
        else:
            norm = toks[:11] + [os.path.realpath(toks[11]), os.path.realpath(toks[12]), toks[13]]
            if ' '.join(norm) != expect:
                fail(f'PARAMS mismatch: got "{" ".join(norm)}" expected "{expect}"')
    info['params'] = params

    # --- manifest binding: output bytes, engine bytes and parameters are those that ran
    try:
        man = json.load(open(A.manifest))
    except (OSError, ValueError):
        man = {}
        fail('manifest missing or unreadable')
    msl_sha = sha256_file(A.msl)
    arb_sha = sha256_file(A.arbcore)
    info['msl_sha256'], info['arbcore_sha256'] = msl_sha, arb_sha
    if man.get('msl_output_sha256') != msl_sha:
        fail('manifest msl_output_sha256 does not match the output file')
    if man.get('arbcore_sha256') != arb_sha:
        fail('manifest arbcore_sha256 does not match the engine binary')
    if params is not None and man.get('params') != params:
        fail('manifest params differ from PARAMS')

    # --- output structure and counts (F3): parse exact fields; exactly one of each header record
    lines = open(A.msl).read().splitlines()
    roots = [m for m in (ROOT.fullmatch(x) for x in lines) if m]
    counts = [m for m in (COUNT.fullmatch(x) for x in lines) if m]
    dets = [m for m in (DET.fullmatch(x) for x in lines) if m]
    k_expect = (A.T + 1) // A.segq
    if (A.T + 1) % A.segq != 0:
        fail('T + 1 is not a multiple of SEGQ')
    if len(roots) != 1:
        fail(f'{len(roots)} AP_SEGROOT records (need exactly 1)')
    if len(counts) != 1:
        fail(f'{len(counts)} COUNT records (need exactly 1)')
    else:
        s_, pr_, su_, t_, id_ = (int(x) for x in counts[0].groups())
        if not (s_ + pr_ == su_ == t_ == A.T and id_ == 1 and s_ > 0 and pr_ >= 0):
            fail(f'COUNT fields inconsistent: smooth {s_} pairs {pr_} sum {su_} T {t_} identity {id_} (frozen T {A.T})')
    # --- coefficient receipts: the root over the verifier receipts for exactly segments 0..k-1
    rec = {}
    for fn in glob.glob(A.receipts):
        for x in open(fn):
            t = x.split()
            if t and t[0] == 'SEG':
                s = int(t[1])
                if s in rec and rec[s] != t[-1]:
                    fail(f'conflicting receipts for segment {s}')
                rec[s] = t[-1]
    missing = [s for s in range(k_expect) if s not in rec]
    if missing:
        fail(f'no receipt for {len(missing)} segment(s), e.g. {missing[:3]}')
    else:
        root = hashlib.sha256(b''.join(bytes.fromhex(rec[s]) for s in range(k_expect))).hexdigest()
        info['receipt_root'] = root
        if len(roots) == 1 and (roots[0].group(1) != root or int(roots[0].group(2)) != k_expect):
            fail('AP_SEGROOT does not equal the root of the verifier receipts over segments 0..k-1')
        if A.pinned_segroot and A.pinned_segroot != root:
            fail('receipt root differs from the pinned segment root')

    # --- symbols (F2): the label set must be exactly the units mod l, each exactly once; unique lattice points
    units = {b for b in range(1, l) if gcd(b, l) == 1}
    plus, minus, seen_dup, bad = {}, {}, [], []
    for x in lines:
        if not x.startswith('XB '):
            continue
        m = XB.fullmatch(x)
        if not m:
            bad.append(f'unparseable XB record: {x[:60]}')
            continue
        b, hp, dp, cp, up, hm, dm, cm, um = (int(v) for v in m.groups())
        if b in plus:
            seen_dup.append(b)
        if dp != LAT or dm != LAT or (cp, up, cm, um) != (1, 1, 1, 1):
            bad.append(f'b={b}: not a unique point of (1/{LAT})Z')
        plus[b], minus[b] = F(hp, LAT), F(hm, LAT)
    if seen_dup:
        fail(f'duplicate XB labels: {sorted(set(seen_dup))[:5]}')
    if set(plus) != units:
        fail(f'label set differs from the units mod {l}: missing {sorted(units - set(plus))[:5]}, extra {sorted(set(plus) - units)[:5]}')
    if bad:
        fail('; '.join(bad[:5]))
    if len(dets) != 1 or int(dets[0].group(1)) != len(units) or int(dets[0].group(2)) != len(units) or int(dets[0].group(3)) != LAT:
        fail('XB_PLUS_DETERMINED record missing or inconsistent')
    info['symbols'] = len(plus)

    if not reasons:
        # --- consistency and the witness (spec §3, §5)
        if any(plus[l - b] != plus[b] or minus[l - b] != -minus[b] for b in units):
            fail('symmetry [(l-b)/l]^+ = [b/l]^+ or [(l-b)/l]^- = -[b/l]^- fails')
        g = smallest_primitive_root(l)
        ind, x = {}, 1
        for e in range(l - 1):
            ind[x] = e
            x = x * g % l
        xm = {a: ind[a] % p for a in units}
        c = [sum(comb(xm[a], k) * plus[a] for a in units) for k in range(3)]
        info.update({'generator': g, 'c0': str(c[0]), 'c1': str(c[1]), 'c2': str(c[2])})
        if c[0] != 0:
            fail(f'c0 = {c[0]} != 0 (Hecke relation at l with [0]^+ = 0)')
        try:
            c1p, c2p = modp(c[1], p), modp(c[2], p)
        except ValueError as e:
            fail(str(e))
            c1p = c2p = None
        if c1p not in (None, 0):
            fail(f'c1 = {c1p} != 0 mod {p} (Ota 5.17 forces c1 = 0): computation error')
        info['c1_mod_p'], info['c2_mod_p'] = c1p, c2p

    if reasons:
        verdict, code = 'INVALID', 2
    elif info['c2_mod_p'] != 0:
        verdict, code = 'NONZERO', 0
    else:
        verdict, code = 'INCONCLUSIVE_ZERO', 3
    report = {'verdict': verdict, 'p': p, 'l': l, 'reasons': reasons, **info,
              'meaning': {'NONZERO': 'Ota Thm 1.5/6.4: Sha(E/Q)[p] = 0, hence Sha[p^inf] = 0 (audited grade)',
                          'INCONCLUSIVE_ZERO': 'nothing follows; try the next auxiliary prime',
                          'INVALID': 'no conclusion; investigate'}[verdict]}
    text = json.dumps(report, indent=1)
    if A.out:
        open(A.out, 'w').write(text + '\n')
    print(text)
    sys.exit(code)


if __name__ == '__main__':
    main()
