# Gate conditions 4 & 5 — source audit. The blocker is not `D`.

Date 2026-09-22. Reading check only, as directed. **No engine launched. Nothing certified.**

Accepted first: `h(-7) = 1` is **not** an obstruction. The construction has no class-number hypothesis, the Gross-point
system lives on orders `O_n = Z + p^n O_K` whose class numbers grow (`h(O_{p^n}) ≈ p^{n-1}(p - (D/p))`), and the
interpolation is stated from `n >= max{1,s}` — positive conductor — rather than from a rich level-0 orbit. Stage 1's
caveat is retired: `H(-7)=1_BASE_DEGENERACY = NOT_AN_OBSTRUCTION`. `D = -7` stays the lead candidate on cost.

---

## 1. Condition 5 — the invoked theorem's hypotheses

Source: *On the Fitting ideals of anticyclotomic Selmer groups of elliptic curves with good ordinary reduction*
(Canadian Mathematical Bulletin). Standing hypotheses as stated:

| hypothesis | our status | size of the excluded set |
|---|---|---|
| `K` imaginary quadratic, **odd discriminant `-D_K < -4`** | `D = -7` ✓ | — |
| `(D_K, Np) = 1` | ✓ by construction | finite |
| **`p` splits in `K`** | **see §2** | **density 1/2 — INFINITE** |
| `p >= 5` | ✓ | finite |
| good **ordinary** reduction at `p` | supersingular excluded | density 0 — **infinite** (Elkies) |
| `p ∤` Tamagawa factors | ✓ for large `p` | finite |
| `a_p(E) ≢ 1 (mod p)` (non-Eisenstein) | ✓ generically | expected finite |
| **(Im)** `ρ̄_p` surjective | ✓ for a.a. `p` (Serre, non-CM) | **finite** |
| **(Ram)** `ρ̄_p` ramified at every `ℓ | N` | ✓ **verified for all `p >= 5`** | none |

**(Ram) checked, not assumed.** `Δ = 2^8·3^2·2243·4547^3·5843^2`. At the multiplicative primes `ℓ = 3, 2243, 5843`
the Tate-curve criterion makes `ρ̄_p` ramified at `ℓ` exactly when `p ∤ v_ℓ(Δ)`, and
`v_ℓ(Δ) = 2, 1, 2` respectively — so `(Ram)` holds at every `ℓ | N` for every `p >= 5`. Not a constraint for us.

Main theorem (Thm 1.1), for `0 <= m <= n`:

    ( θ(E/K_n), ν_{n-1,n}(θ(E/K_{n-1})) )^2  =  Fitt_{Λ_n}( Sel(K_n, E[p^∞])^∨ )

and the three-term relation is stated as

    π_{n+1,n}( θ(E/K_{n+1}) )  =  a_p · θ(E/K_n)  −  ν_{n-1,n}( θ(E/K_{n-1}) )

which **is** H1 in the form `BRANCH_THETA.md` §1 assumes (`pr`, `ν`, same indexing). Condition 4's named target is
therefore met at the level of the relation's shape; what remains unaudited is normalization conventions, which is a
smaller question than the one below and is now moot for the tail (see §3).

## 2. The finding: `p splits in K` cannot be made cofinite by any choice of `D`

For a **fixed** `K = Q(√D)`, `{p : p splits}` has density **1/2** by Chebotarev; `{p : p inert}` has density **1/2**
and is **infinite**. Verified for `D = -7` over `5 < p < 200000`, `p ∤ N`: 8970 split (0.4989) / 9008 inert (0.5010);
first inert primes `5, 13, 17, 19, 31, 41, 47, 59, 61, 73, …`.

By exactly the argument already recorded against ordinary-only coverage, **an infinite exceptional set is not a finite
exceptional set, so no FIN.** And this gap is strictly larger than the one already on the books:

    supersingular, fixed K   : density 0,   infinite
    inert in fixed K         : density 1/2, infinite     <- now the dominant gap

**This is not a defect of `D = -7`.** It holds for every imaginary quadratic field. Stage 1 asked which `D` to pick;
the audit says the choice of `D` is not where this branch is blocked.

**It is also not new to the project — it is the covering obstruction, resurfacing.** `TASK.md` §Q2 already recorded
that `r` independent fixed fields leave uncovered density `2^{-r} > 0` for every finite `r` (computed again here:
`r = 10` still leaves ≈ 0.000977, i.e. infinitely many primes), and that the Klein-four repair forces a **real**
quadratic subfield the machinery cannot use. The definite-theta branch inherits the same wall through a different door.

**Scope, stated precisely.** This does *not* say no inert-prime theory exists — Kobayashi–Ota-type work and
Burungale–He–Kobayashi–Ota Thm 1.3(b) treat `p` inert directly. But per the 2026-09-22 source check, those are in the
**CM / self-dual Hecke character** setting, and `φ_E` is non-CM. So the inert half is *unsupplied here*, not *proved
impossible*.

## 3. Consequence for the gate, and for the run

    condition 4 (theta hypotheses for K = Q(sqrt -7))  = MET in shape; normalization unaudited; moot for the tail
    condition 5 (augmentation -> Selmer corank at K)   = APPLIES to K = Q(sqrt -7), BUT ONLY FOR p SPLIT IN K,
                                                         and that hypothesis CANNOT BE MADE COFINITE BY ANY D

So the corrected ledger:

    DEFINITE_K_FOR_THETA        = CANDIDATES IDENTIFIED (D = -7 lead; h=1 caveat retired)
    DEFINITE_TWIST_RANK0        = NOT CERTIFIED  (and no longer the blocking item)
    FIXED_K_COVERAGE            = STRUCTURALLY INSUFFICIENT — density 1/2 inert gap, any D   <- NEW, blocking
    INERT_PRIME_COMPANION       = UNSUPPLIED in the non-CM setting (exists for CM: BHKO Thm 1.3(b))
    SUPERSINGULAR_COMPANION     = INDICATED_NOT_CONSTRUCTED (density 0, infinite)
    FINITE_LAYER_NONVANISHING   = OPEN
    TAIL_FINITE_SUPPORT         = OPEN

**Recommendation: hold the `L(E^{-7},1)` run.** It is cheap, but it is no longer on the critical path. Certifying
`rank E^{-7}(Q) = 0` would fill one premise of a chain whose *main* term — `FINITE_LAYER_NONVANISHING` — is still open,
and whose *coverage* is now known to top out at density 1/2. It would produce no new `Ш` vanishing. It is also not
needed to pose the question sharply at the workshop: the splitting data alone does that, and we already have it.

The surviving route on this branch is the one `TASK.md` §Q2 direction 2 already named: **let `K` vary with `p`.** That
dissolves the covering problem — for each `p` there are discriminants in which `p` splits — at the price of
(a) uniformity in `D` rather than a fixed `C_i`, and (b) `rank E^D(Q) = 0` for the chosen `D`, which is a
**nonvanishing-in-families** statement rather than one certificate at a time. Both prices land squarely in
Burungale–He–Tian–Ye territory, which reconnects this to the workshop rather than to a local run.

**Nothing certified. No engine launched. FIN, FORMULA open.**
