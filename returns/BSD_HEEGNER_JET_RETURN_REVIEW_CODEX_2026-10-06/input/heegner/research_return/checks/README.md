# checks/

| File | Kind | Input | Producer / checker |
| --- | --- | --- | --- |
| `supersingular_inert.py` | producer | genuine seed data: the record's original model, `K = ℚ(√−23)` | exact Legendre-symbol point count over 𝔽_ℓ, exact Euler criterion for inertness |
| `supersingular_inert.out.json` | output | `ℓ < 2·10⁴` | `python3 supersingular_inert.py 20000` |
| `supersingular_inert_100000.out.json` | output | `ℓ < 10⁵` | `python3 supersingular_inert.py 100000` |

Independent checker: the Lean kernel re-derives, by enumerating all `ℓ²` pairs, `a_ℓ = 0` for
`ℓ = 281, 661, 839`. It also re-derives their inertness (`RequestProject/Continuation/SeedPointCounts.lean`,
`SeedFinite.lean`). Other entries are checked only by the producer.

There are no synthetic controls in this run. No Heegner points or derived classes were computed.

## Revision 2

| File | Kind | Input | Producer / checker |
| --- | --- | --- | --- |
| `finite_batch_auxiliaries.py` | producer | genuine seed data, same model | first inert `ℓ ≡ −1 (mod p)` with `p ∣ a_ℓ` for `p = 37, 41, 53`; `M_ℓ = gcd(a_ℓ, ℓ+1)` and its factorization; `a_p` and ordinary/supersingular type of the earlier covered primes |
| `finite_batch_auxiliaries.out.json` | output | — | `python3 finite_batch_auxiliaries.py` |

Kernel re-checks (`RequestProject/Continuation/TraceCongruence.lean`): `a_53 = −6`, `a_29 = 0`,
inertness of `3391` and `21089`, `gcd(−74, 21090) = 74`. The values `a_3391 = 0`,
`a_21089 = −74`, `a_100613 = 0`, `a_127591 = 164` are checked only by the producer (and a
separate C implementation run during the session, not delivered).
