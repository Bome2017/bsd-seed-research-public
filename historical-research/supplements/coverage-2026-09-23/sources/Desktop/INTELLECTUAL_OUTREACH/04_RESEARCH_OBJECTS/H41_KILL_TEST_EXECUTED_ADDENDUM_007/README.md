# H41_KILL_TEST_EXECUTED_ADDENDUM_007

Executes the `N = 16382` kill test that `ADDENDUM_006` recorded as not executed, by **database lookup
instead of a modular-degree computation**.

**The result:** `a = 0` at `N = 16382`. The kill condition fixed in advance by `ADDENDUM_005` §7 was
`a = 1 ⟹ (C) fails`. It is **not met**, so `(C)` is not refuted — and by the same rule `a = 0` is
**merely another survivor**, not support. The same lookup settles a level never previously tested:
`a = 0` at `N = 262142` (`n = 17`).

**How.** `a = −v₂(Ω₀/Ω_E)` is fixed once the Γ₀(N)-optimal member of the isogeny class is known.
Cremona's `ecdata` records optimality directly. The base's minimal model is `16382b1`, flagged
`opt = 1` — proved optimal — so `E₀ = E`, `h = 1`, `a = 0`. The table also already contains the modular
degree the failed `msinit` job was computing: `degphi = 91008`.

**A correction to `ADDENDUM_006`.** That object closed by saying Sage, Magma, or more memory was what
would execute this. That was wrong and the error was mine: no computation on this host was needed. The
wall was never a compute wall. `ADDENDUM_006` is **not modified** — it stands byte-identical as a true
record of the modular-symbol route and of the operational error inside it.

**Verified, not trusted.** The documented "curve 1 is optimal below 370000, single exception 990h3" was
tested against the data: zero undecided classes below 370000, first `opt>1` at conductor 400002, and
exactly one optimal curve numbered ≠ 1 below 370000 — `990h3`. PARI's `ellisomat` independently
reproduces the isogeny class and its degree matrix, and `ecdata`'s `degree` column independently
reproduces the modular degrees `2,4,8,8` and `24,48,96,96` frozen in `ADDENDUM_005` §6.

**The seed, numerically.** `4L(E,1)/Ω = 1, 3, 9, 117` at `N = 62, 254, 16382, 262142` — all odd, so
`v₂(λ) = −2` wherever it can be checked. Confirmation at four levels, not a proof.

**Reading correction.** The frozen real-period ratios `1 : ½ : ½ : ¼` are correct as a **multiset** and
the inference resting on them is untouched, but the per-index tuple is enumeration-dependent. Do not
identify curves index-wise from it.

**Discipline.** The positive branch is entirely outside this eta-2p architecture — there `N = 2·3·ℓ` and
`F_p` is not even defined. `n = 19` and `n = 31` are outside the database and undetermined. The
determination rests on Cremona's `ecdata` as an external authority, whose digests are recorded here.

    ADDENDUM.md      the nine sections
    computation/     minmodels.gp, lookup.sh, threshold.sh, periods.gp, seed.gp
    receipts/        MINIMAL_MODELS, OPT_MAN_LOOKUP, THRESHOLD_CHECK, PERIODS, SEED_CHECK, ECDATA_PROVENANCE
    MANIFEST.sha256  DIGESTS.md

**The H41 seed remains unproved.**
