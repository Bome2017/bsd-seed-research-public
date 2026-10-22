# DEFINITE_FIELD_GATE — stage 1 (congruence + root number). Nothing certified.

Date 2026-09-22. New folder. Master handoff untouched. No engine launched.

Prompted by the backward seam trace: the definite-theta branch says "choose a fixed definite imaginary quadratic `K`"
but **never instantiated one**. `D = -23` is not it — all five bad primes split there, giving the indefinite/Heegner
case with `rank E(K) = 3`.

---

## 1. What `N^-` can be, from the conductor alone

`N = 2^3 · 3 · 2243 · 4547^2 · 5843`.

`B` is the quaternion algebra ramified exactly at the primes of `N^-` and at `∞`; the number of ramified places must be
even, so **`|N^-|` must be odd** for `B` to be definite. And `N^-` must be squarefree with `p || N` (the local
representation must be Steinberg), which excludes `2` (`v = 3`) and `4547` (`v = 2`, additive).

    eligible for N^- : {3, 2243, 5843}
    odd-size subsets : {3}, {2243}, {5843}, {3, 2243, 5843}

This reproduces the Aristotle record's "odd product of inert primes among `{3, 2243, 5843}`" from the conductor
independently, rather than taking it on trust.

Conditions on `D` (fundamental, `D < 0`, `gcd(D,N) = 1`): every `ℓ | N^-` **inert**, every other bad prime **split**.
`2 ∈ N^+` always, so `D ≡ 1 (mod 8)`; `4547 ∈ N^+` always, so `(D/4547) = +1`.

## 2. Admissible `D`, first eight per branch (`|D| < 4000`)

| `N^-` | admissible `D` |
|---|---|
| `{3}` | **-79**, -319, -1255, -1351, -1567, -1999, -2119, -2791 |
| `{2243}` | **-119**, -311, -551, -623, -767, -887, -1151, -1415 |
| `{5843}` | **-167**, -215, -287, -335, -407, -1007, -1079, -1343 |
| `{3, 2243, 5843}` | **-7**, -103, -271, -583, -703, -727, -1951, -2287 |

Control: `D = -23` is admissible for **no** definite `N^-`, as required — it splits everywhere, `|N^-| = 0` is even,
hence indefinite. The seam is confirmed, not merely suspected.

## 3. The root-number condition is automatic — it is not an extra filter

`w(E) = +1` (rank 2), and for `D` coprime to `N`, `w(E^D) = χ_D(-N)·w(E) = -χ_D(N)`. Now

    χ_D(N) = χ_D(2)^3 · χ_D(3) · χ_D(2243) · χ_D(4547)^2 · χ_D(5843)
           = (+1)^3 · (-1)^{|N^-|} · 1
           = (-1)^{|N^-|}

so `|N^-|` odd forces `χ_D(N) = -1` and **`w(E^D) = +1`** for *every* admissible `D`. Confirmed numerically on all
twelve candidates below. The corresponding statement upstream is `w(E/K) = +1`, i.e. `ord L(E/K,s)` even — and since
`ord L(E,s) = 2`, `ord L(E^D,s)` is even, so rank `E^D(Q) ∈ {0, 2, …}`.

**Consequence for the search plan:** root number does *not* narrow the candidate list. The only discriminating test is
the rank-zero certification itself. The user's staging ("only for plausible root-number +1 candidates test rank-zero")
collapses — every candidate is plausible on that criterion.

| `N^-` | `D` | `χ_D(N)` | `w(E^D)` | `h(D)` | `\|D\|·√N` |
|---|---:|---:|---:|---:|---:|
| `{3}` | -79 | -1 | +1 | 5 | 6.37e9 |
| `{3}` | -319 | -1 | +1 | 10 | 2.57e10 |
| `{2243}` | -119 | -1 | +1 | 10 | 9.60e9 |
| `{2243}` | -311 | -1 | +1 | 19 | 2.51e10 |
| `{5843}` | -167 | -1 | +1 | 11 | 1.35e10 |
| `{5843}` | -215 | -1 | +1 | 14 | 1.73e10 |
| **`{3,2243,5843}`** | **-7** | **-1** | **+1** | **1** | **5.65e8** |
| `{3,2243,5843}` | -103 | -1 | +1 | 5 | 8.31e9 |
| `{3,2243,5843}` | -271 | -1 | +1 | 11 | 2.19e10 |

Control `D = -23`: `χ_D(N) = +1`, `w(E^D) = -1`, `h = 3` — odd rank, matching the certified `rank E^{-23}(Q) = 1`.

## 4. `D = -7` is the standout, with one caveat to check

`|D|·√N = 5.65e8`, giving **98× headroom** against the existing corpus `T = 5.5046e10`; it also realises the **full
three-prime** `N^- = 3·2243·5843`. Next best is `D = -103` at 8.3e9. By `D = -271` the headroom is 2.5×, so the corpus
effectively caps `|D| ≲ 500`.

**Caveat, flagged not resolved: `h(-7) = 1`.** `Pic(O_K)` is trivial, so the conductor-1 Gross-point set is a single
point and `Z[Pic(O_c)]` is degenerate at the base level. The anticyclotomic tower itself is unaffected —
`h(O_{p^n}) ≈ p^{n-1}(p - (D/p))` still grows — but a degree-two object whose base level is a one-element set deserves
an explicit check before `D = -7` is adopted. `D = -103` (`h = 5`) is the natural fallback on the same branch.

## 5. Cost of stage 2 (rank-zero certification) — feasibility only, nothing decided

The certification is `L(E^D,1) != 0`, with the weight `exp(-2πn/(|D|√N))` — **not** the `E_1` weight the `D = -23`
derivative required. So it is *strictly cheaper* than a computation this host already completed successfully (~1 GB).
Stage W is again already paid: the prime-coefficient corpus is `D`-independent, and `χ_D` is a table lookup.

Two constraints carried forward, both from recorded incidents:

* **Adequacy of any cutoff is undetermined until the interval exists.** The `D = -23` episode established this: the
  certificate is `|truncated sum| > B(T)`, and no `T` can be called adequate before the truncated value is known.
  No cutoff is recommended here.
* **Table-free traversal only.** The dense path allocates `4·T` bytes — 26 GiB at `T = 7e9` on a 16 GiB host.

## 6. Gate status

| condition | status |
|---|---|
| 1. legitimate definite factorization `N = N^+N^-` | **SETTLED** — four branches, explicit admissible `D` for each |
| 2. root number permits rank 0 | **SETTLED, and automatic** — `w(E^D) = +1` for every admissible `D` |
| 3. `rank E^D(Q) = 0`, hence `rank E(K) = 2` | **OPEN** — requires a certified `L(E^D,1) != 0`; feasible, not run |
| 4. remaining anticyclotomic/theta hypotheses | **NOT AUDITED** — incl. the `h(-7) = 1` degeneracy |
| 5. the theta-augmentation-to-Selmer-corank theorem applies to this `K` | **NOT AUDITED** — not a computational question |

Ledger amendment as the user framed it, with stage 1 filled in:

    D23_HEEGNER_LANE          = CERTIFIED, INDEFINITE, rank E(K) = 3
    DEFINITE_K_FOR_THETA      = CANDIDATES IDENTIFIED (D = -7, -103, -271, -79, -119, -167, ...)
    DEFINITE_TWIST_RANK0      = NOT YET CERTIFIED  (root number +1 automatic; L-value not computed)
    NORM_COHERENCE_ALGEBRA    = PROVED, conditional on H1
    FINITE_LAYER_NONVANISHING = DOWNSTREAM / OPEN

**Nothing certified. No engine launched. `rank E^D(Q)` unknown for every candidate. FIN, FORMULA open.**
