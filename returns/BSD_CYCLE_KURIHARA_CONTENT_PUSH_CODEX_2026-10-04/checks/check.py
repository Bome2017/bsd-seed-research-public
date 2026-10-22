#!/usr/bin/env python3
"""Exact controls for this written comparison attempt; no seed witness evaluator."""
import json
import math
from pathlib import Path


def primes(n):
    return [p for p in range(5, n + 1)
            if all(p % d for d in range(2, math.isqrt(p) + 1))]


def add(a, b, p):
    out = a.copy()
    for m, c in b.items():
        out[m] = (out.get(m, 0) + c) % p
    return {m: c for m, c in out.items() if c}


def scale(a, c, p):
    return {m: c * v % p for m, v in a.items() if c * v % p}


def mul(a, b, p, degree=4):
    out = {}
    for (i, j), c in a.items():
        for (h, k), d in b.items():
            m = (i + h, j + k)
            if sum(m) <= degree and m[0] < p and m[1] < p:
                out[m] = (out.get(m, 0) + c * d) % p
    return {m: c for m, c in out.items() if c}


def power(a, e, p, degree=4):
    out = {(0, 0): 1}
    while e:
        if e & 1:
            out = mul(out, a, p, degree)
        a = mul(a, a, p, degree)
        e //= 2
    return out


def rank(rows, p):
    a = [[x % p for x in row] for row in rows]
    r = 0
    for c in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inverse = pow(a[r][c], -1, p)
        a[r] = [x * inverse % p for x in a[r]]
        for i in range(len(a)):
            if i != r:
                factor = a[i][c]
                a[i] = [(x - factor * y) % p for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def mm(a, b, p):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2)) % p
                 for i in range(2) for j in range(2))


def main():
    totals = {key: 0 for key in [
        "integral_operator_coefficients", "cyclic_basis_vectors",
        "borel_commutators", "oldform_scalars", "mixed_grid_basis_vectors",
        "polarized_vectors", "diagonal_differences", "unit_packet_zero_controls",
        "free_mixed_coefficients", "joint_oldform_matrices", "cross_pair_identities"]}
    seed_counts = []
    one = {(0, 0): 1}
    xx = {(1, 0): 1}
    yy = {(0, 1): 1}

    for p in primes(101):
        # Exact integral wraparound coefficients of the composed homology map.
        cs = [((k-2) % p)**2 - 2*((k-1) % p)**2 + k*k for k in range(p)]
        expected = [2-p*p, 2+p*(p-2)] + [2]*(p-2)
        assert cs == expected
        totals["integral_operator_coefficients"] += p

        # Check the full linear identity on a basis, not just random vectors.
        for k in range(p):
            v = [int(j == k) for j in range(p)]
            dv = [v[(j+2) % p]-2*v[(j+1) % p]+v[j] for j in range(p)]
            assert sum(dv) % p == 0
            assert sum(j*dv[j] for j in range(p)) % p == 0
            assert sum(j*j*dv[j] for j in range(p)) % p == 2
            totals["cyclic_basis_vectors"] += 1

        # The same commutator supplies lift surjectivity and prevents the tested
        # extension B -> abelian p-group from sending U nontrivially.
        t = next(t for t in range(1, p) if t*t % p != 1)
        diag = (t, 0, 0, pow(t, -1, p))
        inv_diag = (pow(t, -1, p), 0, 0, t)
        for b in range(p):
            unip = (1, b, 0, 1)
            inv_unip = (1, -b % p, 0, 1)
            comm = mm(mm(mm(diag, unip, p), inv_diag, p), inv_unip, p)
            assert comm == (1, (t*t-1)*b % p, 0, 1)
            totals["borel_commutators"] += 1

        # Exact small seed point counts are normalization controls only.
        count = 1
        for x in range(p):
            rhs = (x*x*x-x*x-66020924*x-65074271436) % p
            legendre = 0 if rhs == 0 else (1 if pow(rhs, (p-1)//2, p) == 1 else -1)
            count += 1 + legendre
        ap = p+1-count
        assert ap % 2 == 0
        assert ap % p not in (1, p-1)
        d = p+1
        inverse = pow((d*d-ap*ap) % p, -1, p)
        A = (-ap*d+d*ap)*inverse
        B = (-ap*ap+d*d)*inverse
        assert A % p == 0 and B % p == 1
        direct = 2*inverse*(d*ap*ap-p*ap*ap-d*d)
        reduced = 2*inverse*(ap*ap-1)
        assert direct % p == reduced % p == p-2
        seed_counts.append({"p": p, "ap": ap, "point_count": count,
                            "supersingular": ap == 0})
        totals["oldform_scalars"] += 1

        # The five degree <=2 constraints have exactly the mixed-coordinate kernel.
        basis = [(0,0), (1,0), (0,1), (2,0), (1,1), (0,2)]
        constraint_rows = [[int(i == j) for i in range(6)] for j in (0,1,2,3,5)]
        assert rank(constraint_rows, p) == 5
        for c in range(p):
            F = {(1, 1): c} if c else {}
            assert all(sum(row[i]*F.get(basis[i], 0) for i in range(6)) % p == 0
                       for row in constraint_rows)
            totals["free_mixed_coefficients"] += 1

        old = [[4]*4 for _ in range(4)]
        assert rank(old, p) == 1
        assert all(sum(w*old[i][j] for i,w in enumerate([1,-1,-1,1])) % p == 0
                   for j in range(4))
        totals["joint_oldform_matrices"] += 1

    for p in primes(19):
        g = add(add(one, xx, p), add(yy, {(1,1): 1}, p), p)
        for k in range(p):
            # v=-e_k has the required finite total -1; apply actual cyclic shifts.
            v = [-int(j == k) for j in range(p)]
            dv = [(v[(j+2) % p]-2*v[(j+1) % p]+v[j]) % p for j in range(p)]
            A = {}
            for j, c in enumerate(dv):
                A = add(A, scale(power(g, j, p, 2), c, p), p)
            assert A == {(2,0): p-1, (1,1): p-2, (0,2): p-1}
            totals["polarized_vectors"] += 1

        # Test coefficient shifts directly on the complete group basis.
        for i in range(p):
            for j in range(p):
                row = {((i-1) % p, (j-1) % p): 1}
                for key, c in [(((i-1) % p, j), -1), ((i,(j-1) % p), -1), ((i,j), 1)]:
                    row[key] = row.get(key, 0) + c
                assert sum(a*b*c for (a,b), c in row.items()) % p == 1
                totals["mixed_grid_basis_vectors"] += 1

        # Even a unit genuine leading packet is killed by the extra differences.
        for c in range(p):
            theta = scale({(1,1): 1}, c, p)
            assert theta.get((1,1), 0) == c
            product = mul({(1,1): 1}, theta, p)
            assert product.get((1,1), 0) == 0
            if c:
                assert product == {(2,2): c}
            totals["unit_packet_zero_controls"] += 1

        F = {(0,0): 3 % p, (1,0): 2, (0,1): 1, (1,1): 4 % p}
        for r in range(p):
            for s in range(p):
                h = mul(power(add(one, xx, p), r, p), power(add(one, yy, p), s, p), p)
                hm1 = add(h, scale(one, -1, p), p)
                out = mul(mul(hm1, hm1, p), F, p)
                assert out.get((1,1), 0) == 2*r*s*F[(0,0)] % p
                assert mul(mul(hm1, hm1, p), {(1,1): 1}, p).get((1,1), 0) == 0
                totals["diagonal_differences"] += 1

        # A small family of determinants controls exact arithmetic algebra,
        # not actual seed prime labels or Tate-pairing factors.
        points = [(1,t) for t in range(p)] + [(0,1)]
        mus = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                det = (points[i][0]*points[j][1]-points[i][1]*points[j][0]) % p
                assert det
                mus.append(det*det % p)
        weights = [(i*i+3*i+1) % p for i in range(len(mus))]
        for Cp in range(p):
            deltas = [Cp*m % p for m in mus]
            lhs = sum(w*d for w,d in zip(weights, deltas)) % p
            rhs = Cp*sum(w*m for w,m in zip(weights, mus)) % p
            assert lhs == rhs
            candidate = (-2*pow(mus[0], -1, p)) % p
            assert candidate*deltas[0] % p == -2*Cp % p
            totals["cross_pair_identities"] += 1

    assert seed_counts[0]["point_count"] == 8
    return {
        "status": "PASS",
        "counts": totals,
        "seed_local_normalization_controls": seed_counts,
        "limits": [
            "No actual seed Kurihara pair was evaluated.",
            "No modular-curve homology matrix or new primary certificate was computed.",
            "The arbitrary mixed coefficients are quotient controls, not claimed seed realizations.",
            "Passing finite controls does not prove the imported arithmetic theorems or the uniform bound."
        ]
    }


if __name__ == "__main__":
    result = main()
    output = Path(__file__).with_name("RESULTS.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "counts": result["counts"]}, sort_keys=True))
