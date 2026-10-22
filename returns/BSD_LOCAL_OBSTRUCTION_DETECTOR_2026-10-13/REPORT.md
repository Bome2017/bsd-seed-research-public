# The obstruction classes have a two-entry local signature

2026-10-13. Baseline lab commit `257af6888c80fda3b90d481cf2d94f9950701811`.

**EXPLICIT_LOCAL_DETECTOR_DERIVED; GLOBAL_CLASS_GROUP_NOT_NEEDED_FOR_LOWER_BOUND; NO_NEW_SEED_BOUND.**

Remote readback of the submitted report, proof, audit, and equation model succeeded. I then extracted a simpler arithmetic explanation from the actual representatives: their independence modulo rational points is already visible in a two-dimensional local isogeny quotient at 11.

## The calculation

Choose the prime (11,x_K-1), with x_K=(1+sqrt(43737))/2. For a nonzero field element z, record its valuation modulo 5 and the base-2 discrete logarithm modulo 5 of its leading unit residue in F_11. This identifies Q_11^*/Q_11^{*5} with F_5^2.

Exact evaluation gives

| Element | Valuation mod 5 | Leading-unit logarithm mod 5 |
|---|---:|---:|
| epsilon | 0 | 4 |
| alpha11 | 4 | 0 |
| f(P1) | 0 | 0 |
| f(P2) | 0 | 0 |

The obstruction columns have determinant 4 modulo 5. Because P1,P2 span A(Q)/5A(Q) under the retained rank and saturation inputs, the detector kills the entire global rational-point image. It therefore descends to Sha(F)[hatphi] and proves the two classes independent there.

This lower-bound proof does not use a class number, fundamental unit, fifth-root ideal class, L-value, regulator, or previously inferred Sha order. The all-place membership still uses the matched Miller--Stoll theorem. The prior class/unit dimension calculation, if retained, makes the surjective detector an isomorphism; the local computation by itself supplies no upper bound on its kernel.

The detector is NOT a local insolubility test for the genus-one curve. It records the local isogeny-Kummer lift before forgetting the covering structure. The curve remains locally soluble: the mismatch is between the full local point quotient and the image of globally rational points.

## Equations and explicit splitting field

I regenerated the five Pfaffians from Fisher's matrix, verified their syzygies, checked the normalized descent-function norm identity and exact point relation, and independently verified suitable Hensel minors at 5 and 11. I did not rerun the original five-chart Groebner calculation or the rank descent.

For the unit covering, a written calculation also supplies a degree-five splitting field

    M=Q(t),   t^5-5t^3+5t-46846=0.

The polynomial is irreducible modulo 11. In M(sqrt(43737)),

    z=(t+224 sqrt(43737)/(t^4-3t^2+1))/2

satisfies z^5=epsilon. A prime-to-five restriction argument then gives a point on the covering over M. Its nonzero order-five torsor class implies that no extension of degree prime to five can split it. Thus its period, index, and minimum splitting degree are five. No projective coordinates of an M-point were computed.

## Seed relevance and limit

This extracts a concrete arithmetic relation, rather than another experimental sample. It demonstrates how an independently computed local signature detects the supplied positive excess.

It is not a seed vanishing mechanism. For the seed at coefficient prime 17, the full local Kummer group at 11 is zero: the actual finite-field point count is 14. Hence this particular detector has no information there. In general, vanishing of such a localized quotient cannot exclude classes in the kernel; a global upper bound is still required. No rational five-isogeny or quadratic scalar descent is transported to the seed by analogy.

**FIN, ORDER9, Q36 and seed prime coverage are unchanged.** This is a single-assistant written deduction and exact arithmetic check, not independent human or formal review.

## Files and verification

[PROOF.md](PROOF.md) contains the local detector, its cohomological meaning, the splitting field, and the scope of the seed comparison. [SOURCES.md](SOURCES.md) and [SOURCE_BINDINGS.json](SOURCE_BINDINGS.json) specify primary and retained inputs. [checks/verify.py](checks/verify.py) uses only Python's standard library. Run it and compare to [checks/RESULTS.json](checks/RESULTS.json); verify SHA256SUMS separately.

The checker evaluates all 125 exponent combinations on the actual field elements, checks the displayed two-by-two matrix, and rejects inadequate p-adic precision. Finite tests supplement the written proof; they are not a substitute for it. Development timeouts and the repaired polynomial remainder bug are recorded in CHECK_NOTES.md. Original return files and active endpoint claims are not edited by this additive return.
