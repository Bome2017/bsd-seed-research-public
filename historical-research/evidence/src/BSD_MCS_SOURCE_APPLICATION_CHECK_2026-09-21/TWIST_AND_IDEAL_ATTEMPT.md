# Attempt: suitable twist certificate, and evaluation of the Stark ideal

Date 2026-09-21. Direct attempt at the two remaining items. No compute launched beyond exact integer arithmetic.

## RETURN: `NEITHER_SUPPLIED` — with the twist reduced to one costed computation, and the ideal shown to be
## definitionally equivalent to its own conclusion at the point where it was to be used.

---

# A. The twist

## A.1 The admissible set is explicit and non-empty

Conditions on `K = Q(sqrt D)`: `D < 0` fundamental, odd, `D != -3`, `gcd(D, Np) = 1`, every prime dividing `Np` split
in `K`. Splitting is `D = 1 (mod 8)` at `2` and `(D | l) = +1` at odd `l`. (`2, 3, 2243, 4547, 5843` all confirmed prime.)

Smallest admissible discriminants, all `l | N` split:

    D = -23, -143, -863, -1031, -1055, -1391, -1511, -1847, ...

With `p = 11` (the join's worked admissible prime) additionally split:

    D = -1031, -1055, -1847, -2471, -3071, -3647, -3935, -4391, ...

## A.2 The root number is settled for free — no computation

For `gcd(D, N) = 1` the standard twisting formula gives `w(E^D) = chi_D(-N) w(E)`. Here:

* `w(E) = +1` (analytic rank 2, even);
* `chi_D(N) = prod_{l | N} chi_D(l)^{v_l(N)} = +1`, since **every** `l | N` splits, i.e. `chi_D(l) = +1`;
* `chi_D(-1) = -1`, since `D < 0`.

Hence `w(E^D) = chi_D(-1) chi_D(N) w(E) = -1` **for every admissible `D`**, with no computation. So
`ord_{s=1} L(E^D, s)` is odd, hence `>= 1`, for every candidate in A.1. This is consistent with, and re-derives, the
parity fact used earlier: `ord L(E/K,s) = 2 + ord L(E^D,s)` must be odd.

**What remains is exactly one statement:** `ord_{s=1} L(E^D, s) = 1` rather than `3, 5, ...`. Per the accepted wording
correction W2, that is a single mathematical statement needing a grade, not an extra hypothesis; once it holds at
`PROVED_COMPUTER_ASSISTED`, Gross-Zagier and Kolyvagin give `rank E^D(Q) = 1` and `Sha(E^D)` finite, hence
`rank E(K) = 3` known, which is what the rank-three Fitting shift consumes.

## A.3 The cost of that one statement, exactly

`a_n(E^D) = chi_D(n) a_n(E)`, so the certified coefficient corpus is **reused, not recomputed** — only more of it is
needed. Rigorous evaluation needs `~ sqrt(cond) = |D| sqrt(N)` terms, so the requirement scales **linearly in `|D|`**.
Calibrating against the existing rank-2 certificate (8 444 396 certified `a_q` for `sqrt(N) ~ 8.064e7`, ratio 0.1047):

| `D` | `cond(E^D) = N D^2` | `sqrt(cond)` | est. certified coefficients | multiple of the existing run |
|---|---|---|---|---|
| `-23` | 3.440e18 | 1.855e9 | 1.94e8 | **23x** |
| `-143` | 1.330e20 | 1.153e10 | 1.21e9 | 143x |
| `-863` | 4.843e21 | 6.959e10 | 7.29e9 | 863x |
| `-1031` | 6.913e21 | 8.314e10 | 8.71e9 | 1031x |
| `-1847` | 2.219e22 | 1.490e11 | 1.56e10 | 1847x |

**The cheapest entry point is `D = -23` at 23x the existing certified run.** That is a bounded, well-understood
extension of machinery that already exists in this project — not new mathematics. It is *not* launched here; it is a
costed obligation for the economic gate.

## A.4 A structural limitation of the lane, stated precisely

`D` need not be chosen per prime. A **fixed** `D` serves every `p` with `(D | p) = +1`, a set of density `1/2`. With a
fixed set of `k` discriminants, the primes served are those where at least one `(D_i | p) = +1`, and the uncovered set
has density `2^{-k} > 0` for every finite `k`:

    k = 1: 0.5000    k = 2: 0.2500    k = 3: 0.1250    k = 4: 0.0625    k = 5: 0.0312

**No finite set of twists covers every prime.** This is an arithmetic fact about quadratic characters, not a no-go
theorem about the method: the lane can settle a positive-density set of `p`, and could in principle be combined with
other regimes, but **on its own it cannot reach the uniform tail that FIN requires.** Recorded so that a future run does
not discover it after paying for certificates.

---

# B. The Stark ideal

## B.1 At the point where it was to be used, the identity is an equivalence, not information

Take `n = 1`, `i = 0`, so `R_{1,0} = Z/p = F_p`, and write `V = Sha(E/K)[p]^*`, a finite `F_p`-vector space of some
dimension `d`. Over a field a finite module is free, so the presentation matrix is empty and

    Fitt^i(F_p^d) = 0 for i < d,      = F_p for i >= d.

Hence `Fitt^0(V) = F_p` **iff** `d = 0`. Combined with the rank-three shift `Fitt^i(Sha(E/K)[p^n]^*) = I_{i+3}(ε^Hg_{n,0})`:

    I_3(ε^Hg_{1,0}) = F_p   <=>   Sha(E/K)[p] = 0.

This is an **equivalence**, not a one-way sufficient condition. So "evaluate `I_3`" and "prove `Sha(E/K)[p] = 0`" are
the same problem *unless* `I_3` is computed by a route that never mentions `Sha`. This is why naming the ideal did not
make it easier, made precise.

## B.2 The only Sha-free route, and where it stops

`ε^Hg_{n,m} = ϖ_{n,m}(z^Hg_m)` with `π(z^Hg_∞) = y_∞ (x) y_∞`. So the ideals are determined by where the Λ-basis
`z^Hg_∞` sits relative to the integral lattice `Sel(T)^{(x)2}` — i.e. by the Λ-index `[Sel(T) : Λ y_∞]`, whose
characteristic ideal is exactly what BCK's Heegner point main conjecture equates. Its analytic avatar is the
anticyclotomic `p`-adic `L`-function, whose invariants are computable in principle. **That is the one handle that does
not presuppose `Sha`.**

It requires `y_∞` explicitly: Heegner points of conductor `p^m` on `X_0(N)` with

    N = 6 503 188 012 738 584 ~ 6.5 x 10^15.

That needs the modular parametrization at that level. Nothing in the retained corpus operates at that scale — the
settled primary components at `2, 3, 5, 7, 11` were obtained by Iwasawa/modular-symbol arguments precisely because
direct work on `X_0(N)` is unavailable here. **I have no method for this and am not proposing one.**

## B.3 Not claimed

That no Sha-free evaluation exists; that the anticyclotomic route is impossible; that derived heights cannot contribute
on other Selmer directions. B.2 is a statement about what I could locate and what the corpus can compute, not an
obstruction theorem.

---

# C. Status

Neither deliverable is supplied. What is supplied: the admissible twist set explicitly; the root number settled for
every member with no computation; the remaining twist obligation reduced to a single statement with an exact cost
(**23x the existing certified run at `D = -23`**); the lane's coverage limitation (`2^{-k}` uncovered, so no uniform
tail from twists alone); and a proof that the Stark-ideal target is definitionally equivalent to its own conclusion at
`(i,n) = (0,1)`, which locates the only Sha-free route and its barrier.

FIN, ORDER9, Q36 open. No compute launched, no mechanism proposed, nothing modified.
