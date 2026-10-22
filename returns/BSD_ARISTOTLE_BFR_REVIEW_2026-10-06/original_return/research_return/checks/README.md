# checks/

All inputs are the seed's own exact integer data (minimal-model coefficients and the retained
points). Nothing is synthetic, fitted or statistical. Plain Python 3 with integers only and no
external libraries.

| script | role | output |
|---|---|---|
| `local_kummer_4547.py` | **producer** (affine coordinates mod `4547⁸`; asserts unit denominators) | `local_kummer_4547.out.json`: `P1` reduces to the singular point; `P2` is non-singular with `v_p(x((p−1)P2) − x(P2)) = 1` |
| `RequestProject/Seed/Local4547.lean` (`chainCert_true`) | **independent checker** (projective coordinates mod `4547³`, no division, unit-denominator flag; kernel-evaluated) | same conclusion; residue `(x_A − x_P)/p ≡ 1274 (mod p)` agrees with the producer |
| `bad_prime_local_types.py` | producer (singular point, tangent cone, `#Ẽ_ns(𝔽_q)` by Euler's criterion) | `bad_prime_local_types.out.json`: `3` non-split node (4), `2243` split node (2242), `4547` cusp (4547), `5843` non-split node (5844) |
| `genus2_quotients.py` | control for candidate M3 (map identities spot-checked at 50 random rationals; they are also immediate by substitution; exact `j`-invariants) | `genus2_quotients.out.json` |

Reproduce with `python3 <script>`. Each run takes a few seconds.

Not run: the delivery folder's `checks/offline_check.py`. Its local/mock receipts are not
observations about this job.
