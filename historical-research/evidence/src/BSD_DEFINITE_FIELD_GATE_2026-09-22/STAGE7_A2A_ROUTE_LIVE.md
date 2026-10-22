# Stage 7 — Stage 6 was too pessimistic. A2a route is LIVE, and the held run returns to the critical path.

Date 2026-09-22. **Additive.** Supersedes `STAGE6_A2_SPLIT.md` §4 and the Stage-5/6 "hold the run" recommendation.
No engine launched. Nothing certified.

---

## 1. The diagnosis is right: my toy model discarded the τ-structure

Stage 6's four-`Λ/(T)` example is valid *as an abstract Λ-module statement* but it worked with Mordell–Weil ranks and
forgot complex conjugation. BD's derived-height machinery runs on the **pro-`p` Selmer group itself**,

    S = S_p(E/K) = lim_n Sel_{p^n}(E/K),     0 -> E(K) ⊗ Z_p -> S -> T_p Sha(E/K) -> 0

so a divisible `Sha` is *already inside* `s^± = rank_{Z_p} S^±`. The first anticyclotomic height vanishes on
`S^+ × S^+` and `S^- × S^-`, its nullspace has rank `>= |s^+ − s^-|`, and the filtration gives

    sigma := ord_I char(X_inf)  >=  rank S + rank S^(2)  >=  (s^+ + s^-) + |s^+ − s^-|  =  2·max(s^+, s^-).

Same inequality as Stage 5/6, but on `S` rather than `E(K)` — and that is exactly the difference that makes it bite on
`Div Sha`. Truncation clause is fine: `p >= 5` and `sigma = 4 < p`.

**A1 dissolves at ordinary `p`.** BLV's exceptional case is supersingular + inert + `ε = +`; at ordinary `p` it cannot
occur, so Theorem A gives **equality** `(L_p) = (Char_p)`. Hence `[c_2] ≠ 0` ⟹ `L_p ∈ I⁴\I⁵` with unit leading
coefficient ⟹ `sigma = 4` with unit algebraic leading coefficient. The old A1 lower-bound problem is replaced by a
**module-identification** problem: is BLV's `Char_p(f)` the characteristic ideal of the *same* `X_∞` BD's theorem
applies to (same local conditions)?

## 2. Refinement — what actually kills the Stage-6 counterexample

With `p` odd the `1±τ` idempotents split cleanly: `s^+ = 2 + d^+` (since `rank E(K)^+ = rank E(Q) = 2`) and
`s^- = r^- + d^-`, where `d^±` are the coranks of `Div Sha(E/K)[p^∞]^±` and `d = d^+ + d^-`. Enumerating **every**
configuration with `2·max(s^+,s^-) <= 4`:

| `d^+` | `r^-` | `d^-` | `s^+` | `s^-` | `2·max` | `d = Div Sha` | survives? |
|---:|---:|---:|---:|---:|---:|---:|---|
| 0 | 0 | 0 | 2 | 0 | 4 | **0** | ✓ |
| 0 | 0 | 1 | 2 | 1 | 4 | 1 | needs certificate |
| 0 | 0 | **2** | 2 | 2 | 4 | **2** | needs certificate |
| 0 | 1 | 0 | 2 | 1 | 4 | **0** | ✓ |
| 0 | 1 | 1 | 2 | 2 | 4 | 1 | needs certificate |
| 0 | 2 | 0 | 2 | 2 | 4 | **0** | ✓ |

**`d^+ = 0` is forced by the inequality alone** — `rank E(Q) = 2` already fills `s^+`, so no room remains for
`T_p Sha^+`. That is precisely what the Stage-6 toy model missed, and it is free.

**But `d^- ∈ {0,1,2}` survives the inequality.** So the τ-structure alone does *not* give `Div Sha = 0`. My Stage-6
counterexample had `d = 2`; under the τ-structure it must be `(d^+, r^-, d^-) = (0, 0, 2)` — and that row is
**consistent with `sigma = 4`**. It is not defeated by τ-equivariance.

**It is defeated by the certificate.** `L(E^{-7},1) ≠ 0` gives, by Gross–Zagier–Kolyvagin at analytic rank 0, both
`rank E^{-7}(Q) = 0` **and** `#Sha(E^{-7}/Q) < ∞` — i.e. `r^- = 0` *and* `d^- = 0`, hence `s^- = 0`. Only the first
row remains, and `Div Sha(E/K)[p^∞] = 0`.

    Stage-6 counterexample dies to:  tau-structure + CERTIFICATE.   Not tau-structure alone.

## 3. Operational consequence — reverse the hold

Stages 4, 5 and 6 recorded "hold the `L(E^{-7},1)` run; it is off the critical path." **That is now wrong, and the
reversal is the most actionable item here.** The certificate is not tidying: GZK at analytic rank 0 is what supplies
`d^- = 0`, and nothing else in the route does. It is the step that removes the last configuration the inequality
permits.

    HOLD_L_E_MINUS_7_RUN = WITHDRAWN.  The run is back on the critical path, for A2a's minus side.

Stage 1 already established it is cheap: `exp` weight not `E_1`, `|D|·√N = 5.65e8`, 98× corpus headroom, stage W
already paid. Constraints unchanged — cutoff chosen **from** the computed interval, never in advance; table-free
traversal only.

## 4. A2b follows formally, as claimed

BD Remark 2.21 makes `R_der` integral once `Sha[p^∞]` is finite; Thm 2.23 then gives the leading coefficient as
`#Sha(E/K)[p^∞] · R_der` up to a unit. With the left side a unit and both factors of non-negative valuation whose
product has valuation zero, `v_p(#Sha) = 0` and `v_p(R_der) = 0`, so `Sha(E/K)[p^∞] = 0`. A2b is not an independent
wall — **conditional on A2a**.

## 5. Parity bookkeeping — accepted, and it is an error in the record

`w(E^{-7}) = +1` forces the **analytic** rank even. Earlier files (Stage 1 §3, Stage 6 §3) used it to assert
`r^- ∈ {0,2,4,…}` with `r^-` the **Mordell–Weil** rank. That step needs a parity theorem with its own hypotheses,
which is not installed in the project record. **Withdrawn.** Harmless for this route, since the certificate gives
`rank E^{-7}(Q) = 0` unconditionally through GZK — but it must not be reused as stated.

## 6. Honest scoping

* **BD Theorems 2.7, 2.18, 2.23 and Remark 2.21 were not read at source here.** Their characterization is accepted as
  given. Checking BD Cor 3 at source mattered two stages ago; the same reservation applies, and the prompt correctly
  instructs the run to use them at source.
* **The whole route is conditional on `[c_2] ≠ 0`.** `sigma = 4` *exactly* is what drives it, and that comes from the
  witness. So A2a is **not eliminated** — it is **reduced** to `[c_2] ≠ 0` + the `D = -7` certificate + module
  identification. That is still a large gain: A2a stops being an independent wall and becomes a consequence of the
  target the branch was already chasing.

## 7. Freeze

    A2a_DERIVED_HEIGHT_ROUTE   = LIVE       (replaces "A2a = recurring Sha-finiteness wall")
    A2a_MINUS_SIDE             = REQUIRES the D = -7 certificate; tau-structure alone leaves d^- in {0,1,2}
    A2a_PLUS_SIDE              = FREE from the inequality (d^+ = 0, since rank E(Q) = 2 fills s^+)
    A1_ORDINARY                = reduced to MODULE IDENTIFICATION (BLV equality holds; no exceptional case)
    A2b                        = FORMAL, conditional on A2a
    HOLD_L_E_MINUS_7_RUN       = WITHDRAWN — back on the critical path
    MW_RANK_PARITY_FROM_SIGN   = WITHDRAWN — sign gives analytic parity only
    EXACT_M4 <== [c_2] != 0    = OPEN, and now carries A2a as well
    A3 (supersingular)         = still separate; BD Cor 3 and BLV equality are both good-ordinary here

One addition to the proposed prompt: it should carry the §2 enumeration explicitly, so the run cannot wave at the
minus side. The τ-inequality gives `d^+ = 0` for free and `d^- ∈ {0,1,2}` **not** for free; a run that reports
`ORD4_FORCES_SHA_FINITE` without invoking the certificate has skipped three live rows.

**Nothing certified. No engine launched. FIN, FORMULA open.**
