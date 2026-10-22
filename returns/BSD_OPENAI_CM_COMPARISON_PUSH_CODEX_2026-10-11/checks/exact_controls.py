"""Small exact arithmetic controls; no seed CM/Kato value is evaluated."""
import json
from math import gcd


def point_count(q):
    points = [(x, y) for x in range(q) for y in range(q)
              if (y*y - x*x*x + x*x + 66020924*x + 65074271436) % q == 0]
    return 1 + len(points)


def main():
    counts = {q: point_count(q) for q in (5, 13)}
    assert counts == {5: 8, 13: 18}
    eig = {q: q + 1 - counts[q] for q in counts}
    assert eig == {5: -2, 13: -4}
    # A = 2(T5-6) - (T13-14). Degree zero; eigenvalue 2.
    degree = 2*6 - 14 + 2
    scalar = 2*eig[5] - eig[13] + 2
    assert degree == 0 and scalar == 2
    assert gcd(counts[5], counts[13]) == 2
    # A formal alternating specialization can have any even finite length,
    # while its analytic/determinant quotient equals the unit 1.
    alternating = []
    for p in (5, 7, 11):
        for a in (1, 2, 5):
            c = p**a
            determinant = c*c
            assert determinant == p**(2*a)
            alternating.append({'p': p, 'a': a, 'cokernel_length': 2*a,
                                'determinant': determinant, 'quotient': 1})
    return {
        'grade': 'EXACT_FORMULA_CONTROLS_NOT_SEED_BOUND',
        'counts': counts, 'a_q': eig,
        'degree_correction': {'degree': degree, 'eigenvalue': scalar,
                              'single_prime_constants': {'5': -8, '13': -18}},
        'alternating_models': alternating,
        'limitations': ['No CM class or mixed-place scalar computed',
                       'No source theorem or geometric map certified by this script'],
    }


if __name__ == '__main__':
    print(json.dumps(main(), indent=2, sort_keys=True))
