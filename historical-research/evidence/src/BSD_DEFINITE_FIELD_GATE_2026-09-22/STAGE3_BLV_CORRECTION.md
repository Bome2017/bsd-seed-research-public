# Stage 3 — correction to the stage-2 audit, and the answer to question #3

Date 2026-09-22. **Additive.** Supersedes §2–§3 of `GATE_STAGE2_AUDIT.md`; that file is preserved unedited.
No engine launched. Nothing certified.

---

## 0. My error, plainly

`GATE_STAGE2_AUDIT.md` recorded

    INERT_PRIME_COMPANION = UNSUPPLIED in the non-CM setting
    FIXED_K_COVERAGE      = STRUCTURALLY INSUFFICIENT

**Both are wrong.** The density-1/2 computation was correct *about Chan-Ho Kim's finite-layer Fitting theorem*, which
does assume `p` split and ordinary. What was not correct was extrapolating from one theorem's hypothesis to a
structural property of the branch. That is precisely the failure the standing rule
`kill-verdicts-must-not-outrun-the-theorem` names — absence of a comparison is not impossibility — and I applied the
rule to Fable's verdicts earlier in this project while breaking it here. The stage-2 conclusion is withdrawn.

## 1. BLV, verified at source

**Bertolini–Longo–Venerucci, *The anticyclotomic main conjectures for elliptic curves*, arXiv:2306.17784,
Math. Ann. 395 (2026).** Hypothesis 1.1:

| hypothesis | excluded set | our status |
|---|---|---|
| `p >= 5`, `p ∤ N`, `p ∤ disc(K)` | finite | ✓ |
| **`p ∤ h_K`** | finite | **vacuous for `D = -7`** (`h = 1`) |
| `ρ̄_{E,p}` **surjective** | finite (Serre) | ✓, and see §2 |
| `N^-` squarefree | structural | ✓ (`3·2243·5843`) |
| **anomalous:** ordinary case — `a_p ≢ ±1 (mod p)` if `p` **inert**; `a_p ≢ 1 (mod p)` if `p` **split** | see §3 | see §3 |
| ramification at `N^+`, certain `N^-` | — | partially checked |

**`p` may be split OR inert. Reduction may be good ordinary OR supersingular.** All four combinations are treated.

**Theorem A:** `(L_p^ε(f)) ⊆ (Char_p^ε(f))`, with **equality in the non-exceptional case**.
**Definition 1.3 — exceptional** means: `E` supersingular at `p`, `p` **inert** in `K`, and `ε = +`. Only that one case
gets a single divisibility.

So the corrected ledger, as the user framed it:

    CHANHO_KIM_FINITE_LAYER_THEOREM  = SPLIT + ORDINARY ONLY            (stage-2 density-1/2 criticism stands here)
    FIXED_K_ANTICYCLOTOMIC_COVERAGE  = REOPENED BY BLV / BBL            (all four cases, non-CM)

Burungale–Büyükboduk–Lei independently treat supersingular `p` inert in `K` with signed anticyclotomic main
conjectures and the one-sided inclusion, also not restricted to CM.

## 2. A point in our favour that stage 1 read backwards

BLV assume `ρ̄_{E,p}` **surjective**. A CM curve never has surjective mod-`p` image, so Hypothesis 1.1 *excludes* CM
curves — BLV is built for exactly our kind of curve. Combined with the 2026-09-22 source check, the picture inverts:
the Burungale–He program is CM-only and unusable for us, while BLV is non-CM and usable.

And `p ∤ h_K` is **vacuous for `D = -7`** because `h(-7) = 1`. The class-number-one property that stage 1 flagged as a
possible degeneracy is, for BLV's hypotheses, an **asset** — it removes a hypothesis rather than creating a problem.
`D = -7` strengthens as the lead candidate.

## 3. Repair 1 — the anomalous primes. My "expected finite" was wrong.

For `p >= 7`, Hasse gives `|a_p| <= 2√p < p-1`, so `a_p ≡ ±1 (mod p)` ⟺ `a_p = ±1` exactly. Lang–Trotter predicts
`#{p <= x : a_p = t} ~ C_t √x / log x`, i.e. **conjecturally infinite, density 0**. So the set is:

* **not proved finite** — my stage-2 entry "expected finite" is withdrawn;
* **not proved infinite** either — unlike the supersingular primes, where Elkies gives infinitude unconditionally.

Measured for this curve: **no prime `5 <= p < 30000` with `a_p = ±1`.** Empirically empty so far; theoretically
unresolved in both directions.

One refinement worth keeping: the hypothesis is **case-dependent**. A split `p` only needs `a_p ≢ 1`, so `a_p = -1` at
a split prime is *permitted*. The excluded set is therefore smaller than a naive reading suggests.

## 4. Repair 2 — `(Ram)` completed at the additive places

Stage 2 checked only the multiplicative places `3, 2243, 5843` and then asserted every `ℓ | N`. The gap is repaired:

`v_q(j) < 0` only at `q = 3, 2243, 5843`, so `j` is **integral** at `2` and `4547` — those places have **potentially
good** reduction, not potentially multiplicative. Inertia at such `ℓ` acts on `T_p(E)` through a finite group of order
`e | 24`; for `p >= 5` we have `p ∤ 24`, so reduction mod `p` is injective on that group and `ρ̄_p` **is** ramified at
`2` and `4547` for every `p >= 5`. Together with the Tate-curve argument at the multiplicative places
(`v_ℓ(Δ) = 2, 1, 2`), `(Ram)` now genuinely covers **all** `ℓ | N`.

## 5. Question #3, answered: the rank-two leading term is NOT in BLV

This is the decisive finding of stage 3. BLV contains **no** derived `p`-adic height formula, **no** leading-term
analysis in powers of the augmentation ideal, and **no** statement for the trivial character when the `L`-value
vanishes. Its results are about Selmer structure over Iwasawa algebras, not about analytic ranks or leading
coefficients.

Moreover BLV **flag the trivial character themselves**, in Remark 1.4:

> "The presence of a local zero in the exceptional case prevents us to treat the trivial character on the same ground
> as the other characters."

Our problem lives exactly there: for the definite field, `ord_{s=1} L(E/K,s) = 2`, hence `L(E/K,1) = 0`, i.e. the
trivial character with a vanishing `L`-value. Theorem B's `Sel` finite ⟺ `L(E/K,χ,1) ≠ 0` therefore returns only
"`Sel` is infinite", which we already know from `rank E(K) = 2`.

    BLV_RANK2_LEADING_TERM = NOT PRESENT IN BLV, AND NOT AN IMMEDIATE COROLLARY

So the user's prediction is confirmed: **this, not the split/inert coverage, is the first unproved theorem.**

## 6. Remaining non-finite exclusions under BLV — honest tally

| exclusion | status |
|---|---|
| `a_p = ±1` | conjecturally infinite (Lang–Trotter), density 0, **unproved both ways**; empty below 30000 here |
| exceptional case: supersingular + inert + `ε = +` | supersingular is **proved** infinite (Elkies); whether infinitely many are *also* inert in a fixed `K` is expected but **not asserted here** |

**The exceptional case may not be fatal, and this is worth checking at source.** Theorem A still gives
`(L_p^ε) ⊆ (Char^ε)` there, i.e. `Char | L_p` — which is the direction that bounds the Selmer group *above* by the
`L`-function, and an upper bound on `Ш` is what we want. If that reading is right, the exceptional case costs
sharpness, not applicability. **Not confirmed — inferred from a summarised statement, flagged for source check.**

## 7. Corrected recommendation

**Agreed: do not vary `K` yet.** Stage 2's "surviving route is `K` varies with `p`" was premature. Two live options:

1. **Fixed `K`**, using BLV/BBL for all four split/inert × ordinary/supersingular cases, then derive the rank-two
   leading-term consequence. **Cheaper to audit, and now the priority.**
2. **Vary `K` with `p`** — still available, but it buys the uniform-in-`D` rank-zero-twist problem.

**Hold the `L(E^{-7},1)` run** — but for the user's reason, not stage 2's. The blocker is the rank-two leading-term
arrow, not coverage, so the run still fills a premise of a chain whose first unproved theorem lies elsewhere.

Remaining questions from the proposed `BLV_RANK2_LEADING_TERM_AUDIT`, with #3 now answered:

1. definite, good ordinary, inert `p` — does BLV's theta object/relation match the one manipulated in `BRANCH_THETA`? **open**
2. definite supersingular, split and inert — which signed theta class replaces it; exceptional `+` inert behaviour? **open, see §6**
3. can the finite-layer ε-BSD formulas be specialized at the augmentation ideal to give `I²/I³ ≠ 0 ⟹ Ш(E/K)[p] = 0` at `rank E(K) = 2`? **ANSWERED: not in BLV; Remark 1.4 sets the trivial character apart**
4. which hypotheses leave possibly-infinite prime sets? **ANSWERED in §6**

**Nothing certified. No engine launched. FIN, FORMULA open.**
