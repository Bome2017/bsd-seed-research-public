# ORDINARY LANE — FREEZE, 2026-09-22

Supersedes the ordinary-lane rows of every earlier ledger in this folder and in
`~/BSD_DEFINITE_FIELD_GATE_2026-09-22/`. Prime-local throughout: `[c_2]_p` is a different object at each `p`.

---

## 1. The theorem — canonical statement

    for all p >= 5 with p ∤ 7N and E ordinary at p :    c_2(p) ∈ Z_p^x   ==>   Sha(E/Q)[p^inf] = 0

`c_2(p)` is the `I^2/I^3` coefficient of the stabilized Gross-point square-root theta at `p`; "`[c_2]_p != 0`"
elsewhere in this folder means the same thing (its reduction mod `p` is nonzero). Prime-local: one hypothesis per `p`.

Proof skeleton: `c_2(p)` unit ⟹ (exact augmentation order, given the unconditional lower order; BLV equality) `σ = 4`
with unit leading coefficient ⟹ (BD derived heights,
`s^- = 0`) `Div Sha(E/K)[p^inf] = 0` ⟹ (runs' exponent bound) `v_p #Sha(E/K)[p^inf] <= 2c` ⟹ (odd-`p` descent,
`Sha(E/K)[p^inf] = A ⊕ B`; Cassels–Tate perfect alternating on finite `B`, so `B = ⊕(Z/p^{n_i})^2` and
`v_p #B >= 2c`) `A = 0`. As a by-product, `v_p #B = 2c` forces a single pair: `B = 0` or `(Z/p^c)^2`.

## 2. Status

| item | status |
|---|---|
| `D = -7` central-value certificate, `L(E^{-7},1) ∈ [9.054319, 9.054421]` | **CERTIFIED** (independently re-audited externally: 600 unit hashes, 120 segment hashes, roots, count identity, exact rational recombination, outward containment) |
| `r^- = 0`, `Sha(E^{-7}/Q)` finite | **CERTIFIED** (GZK at analytic rank 0) |
| A0 location: `c_2(p)` is the `I^2/I^3` coefficient of the stabilized Gross-point **square-root** theta `calL_p`, and `L_p = calL_p · calL_p^iota` | **RESOLVED**, line-level from `BRANCH_THETA.md` + BLV |
| A0 lower order: `calL_p ∈ I^2`, `L_p ∈ I^4` | **UNCONDITIONAL** at good ordinary `p` — BD Cor 3 with the certified `(r^+, r^-) = (2, 0)` |
| A0 exact order: `calL_p ∈ I^2 \ I^3`, `L_p ∈ I^4 \ I^5` | **CONDITIONAL on `c_2(p) ∈ Z_p^x`** — this *is* the open witness, not a consequence of A0 |
| BD Annals 2005 Cor 3, definite, good ordinary: `ord_I L_p >= 2 max(r^+, r^-)` | **SOURCE-CHECKED** — supplies the lower-order vanishing that makes degree 2 the *first possible* square-root coefficient. It does **not** establish that `c_2(p)` is nonzero. |
| anomalous-prime interface B | **DEAD** (rational 2-torsion ⟹ `a_p` even at odd good `p`; Hasse for `p >= 7`; `a_5 = -2` directly) |
| BLV ordinary equality `(L_p) = (Char_p)` | theorem statement, Hyp 1.1, Def 1.3 **source-read by the project** (stage 3); Selmer module and local conditions **source-read by two audits only** |
| BLV ↔ BD module comparison | **PROVED BY TWO AUDITS**; not replayed by the project |
| BD Thm 2.18(5) / 2.23 / Lemma 3.1 | **SOURCE-READ BY TWO AUDITS** (both caught Lemma 3.1's chapter-level finiteness assumption and re-derived it without); not replayed by the project |
| runs' `A_2 <= c` step | **REPLAYED** here (τ-rule + bilinearity + `p^c Sel^- = 0`) |
| `A_2 <= c ⟹ v_p #Sha(E/K) <= 2c` | rests on BD 2.18(5) + 2.23; **not** replayed |
| odd-`p` descent `Sha(E/K)[p^inf] = A ⊕ B` | proved for Selmer/`T_pSha` by two audits; standard; **not** replayed |
| Cassels–Tate classification | **REPLAYED** (standard; single-pair consequence verified) |
| A2a: `Sha(E/K)[p^inf]` finite | **CONDITIONAL ON `[c_2]_p != 0`** |
| Cassels–Tate shortcut to `Sha(E/Q)[p^inf] = 0` | **CONDITIONAL ON `[c_2]_p != 0`** |
| `[c_2]_p != 0` | **OPEN**, prime by prime; uniform version is the frontier |
| supersingular analogue A3 | **OPEN** |
| `I_3(13) = F_13` | **`OPEN_TWIST_13_PRIMARY_INPUT`** — separate lane (`K = Q(sqrt -23)`); needs `Sha(E^{-23}/Q)[13] = 0`, unsupplied; `C_1 != 0` not established |

## 3. For this seed, "admissible" means only "ordinary, `p >= 5`, `p ∤ 7N`"

Every other hypothesis of the lane has now been discharged or shown vacuous for this curve:

| hypothesis | status here |
|---|---|
| `p >= 5`, `p ∤ N`, `p ∤ disc K` | excludes exactly `2, 3, 7, 2243, 4547, 5843` |
| `rho-bar_{E,p}` surjective | Sage `non_surjective() = [2]` for the seed — **vacuous for `p >= 3`** |
| `p ∤ h_K` | `h(-7) = 1` — **vacuous** |
| non-anomalous | **vacuous** (interface B dead) |
| (Ram) at `N^-` | `v_l(Delta) = 2, 1, 2` at `3, 2243, 5843` — **vacuous for `p >= 5`** |
| (Ram) + `H^0(G_{Q_q}, E[p]) = 0` at `N^+ = {2, 4547}` | additive, potentially good, `c_q <= 4` — **vacuous for `p >= 5`** |
| `N^-` squarefree | `3 · 2243 · 5843` ✓ |
| BD §1.1 (1)–(4) | "cost no primes beyond BLV's" — **both runs' claim, not replayed** |

So the only thing separating a prime `p >= 5`, `p ∤ 7N` from the lane is **supersingularity**.

## 4. The exact residual, prime by prime

Every prime falls in exactly one row:

| primes | covered by | status |
|---|---|---|
| good ordinary `p >= 5`, `p ∤ 7N` | this lane | `Sha(E/Q)[p^inf] = 0` **conditional on `[c_2]_p`** |
| `2, 3, 5, 7, 11, 13` | fixed-prime certificates | **PROVED** per the current canonical fixed-prime ledger: `0, (Z/3)^2, 0, 0, 0, 0` (5, 11, 13 also lie in the lane) |
| **`2243, 4547, 5843`** | **nothing** — excluded from the lane (`p | N`), not among the certified primes | **UNCOVERED** |
| supersingular: `23, 29, 131, 167, 281, 563, 661, …` (infinite, Elkies) | nothing yet | **A3, OPEN** |

This names what "remaining exceptional primary components" means for this seed: **exactly the three bad primes of
multiplicative-or-additive reduction not already certified.** Note the FIN-threshold logic is unaffected by them —
any one would contribute at least `p^2 >= 2243^2` to `#Sha`, far above `2601` — but FIN itself still needs them.

## 5. Replay status of the six verification items

| # | item | replayed by the project? |
|---|---|---|
| 1 | BLV ordinary equality, exact Selmer module, local conditions | theorem statement **yes**; module/local conditions **no** |
| 2 | BLV ↔ BD identification, `N^-` Tate-curve and `N^+` vanishing | **no** |
| 3 | BD 2.23 / 2.18 / Lemma 3.1, non-circularity of the τ-argument | **no** |
| 4 | `v_p #Sha(E/K)[p^inf] <= 2c` | the `A_2 <= c` step **yes**; the passage via BD 2.18(5) + 2.23 **no** |
| 5 | `Sha(E/K)[p^inf] ≅ A ⊕ B` for odd `p` | **no** (standard) |
| 6 | Cassels–Tate classification | **yes** |

**Replay order** for the next read-only audit — the pieces that rest only on the two Aristotle audits:

    BLV local-module identification  ->  BD 2.18 / 2.23 / Lemma 3.1  ->  odd-p quadratic Selmer decomposition
                                     ->  full A_2 <= c exponent argument (limit passage + BD 2.18(5))

**Do not spend the audit on:** the Cassels–Tate finite-group classification, the finite-level `A_2 <= c` step
(both replayed here), or the anomalous-prime parity facts.

## 6. Off the critical path

The Manin constant of `E^{-7}`, `v_7(c)`, the modular degree, `#Sha_an(E^{-7}) = 49`, exact twist-Sha support, and
Wiersema–Wuthrich. Valid side results; no longer advance the seed implication. Bookkeeping corrections (seed model is
`x = X + 7578`, `u = 1`; twist-period identity needs the full-real-period/cycle convention) are recorded in
`CASSELS_TATE_SHORTCUT.md` §5 and are not regressions.

---

*Finalized 2026-09-22 after external review.* Before finalizing, the A0 row read "theta order 2, full order 4" and the
Cor 3 row read "guarantees `c_2` is the *leading* coefficient". Both stated exact order where only the lower bound is
unconditional. Corrected above: the lower order `calL_p ∈ I^2`, `L_p ∈ I^4` is unconditional; exact order holds only
given the `c_2(p)` unit, which is the open witness itself.
