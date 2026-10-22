# Correction to `MANIN_GATE.md` §3 — verdict: `V7_MANIN_BOUND_OPEN`

Date 2026-09-22. **Additive.** Supersedes `MANIN_GATE.md` §3, §6 (the `v_7(c)` row) and §7. Everything else in that
file stands. Edi89 read directly from `websites.math.leidenuniv.nl/edixhoven/publications/1989/phd-thesis.pdf`.

---

## 1. The claimed bound is NOT in Edi89. Confirmed at source.

`MANIN_GATE.md` §3 recorded `v_7(c) BOUND = EXISTS but UNPUBLISHED [Edi89]`, on the strength of ARS's sentence that
Edixhoven "also gives bounds that are independent of `E` on the valuations of `c_E` at 2, 3, 5, and 7."

**The thesis says the opposite.** Introduction, verbatim:

> "It is known that `c` is a positive integer and Mazur proved that only 2 and primes where `E` has additive reduction
> can divide `c`. Our methods show that primes `p > 7` where `E` has additive reduction divide `c` **at most once**,
> and in fact, for most of the possible reduction types (= Kodaira symbols), not (Theorem 4.6.3 and the remarks
> following this theorem). It might well be that a computation involving the period lattices of normalized newforms
> can solve the problem in the case of potentially good, ordinary reduction of type II, III or IV.
> **It should also be tried to get bounds on the exponents of 2, 3, 5 and 7 in `c`.**"

"It should also be tried" is a statement of **open problem**, not of result. ARS's secondary characterization
overstates the thesis. Corrected:

    v_7(c) EXPLICIT BOUND  =  NOT LOCATED / NOT IN EDI89

**Method note for the record:** the ARS sentence was used as evidence for a bound without reading Edi89. That is the
same failure mode as trusting a project summary over a source, and it produced a freeze that was wrong in the
*optimistic* direction. Secondary characterizations of unpublished work are not citations.

## 2. One thing the thesis gives that I had NOT recorded, and it is stronger

For additive `p > 7`: **`v_p(c) <= 1` always**, and `= 0` for most Kodaira types. I had only recorded the `= 0` case.

## 3. Theorem 4.6.3 verbatim, with every hypothesis checked against this curve

> **Theorem 4.6.3** Let `E` be a strong Weil curve. Let `p > 7` be a prime such that:
> 1. `E` has additive reduction at `p`, **not of type `I_0^*` or `I_ν^*`**,
> 2. `E` does not admit an isogeny (over `Q`) of degree `p`.
>
> If `E` has potentially supersingular reduction at `p` then `p` does not divide the (Manin) constant `c` attached to
> `E`. Let `Ẽ` be the strong Weil curve in the isogeny class of the twist of `E` over the quadratic extension of `Q`
> that is ramified only at `p`. Let `c̃` be its Manin constant. If `E` has potentially ordinary reduction then `p`
> divides `c·c̃` at most once.

| hypothesis | at `q = 4547` | at `q = 7` |
|---|---|---|
| `p > 7` | ✓ | **✗** (`7` is not `> 7`) |
| additive, not `I_0^*`/`I_ν^*` | ✓ type **III** | **✗** type **`I_0^*`** |
| no `Q`-isogeny of degree `p` | ✓ (Sage: degrees are `{1,2}`; consistent with Mazur's list `{2,3,5,7,11,13,17,19,37,43,67,163}`) | ✓ |
| potentially supersingular | ✓ (`j ≡ 1728`, `4547 ≡ 3 mod 4`, `a_q = 0`) | ✗ potentially **ordinary** (`j ≡ 4`, `a_7 = 2`) |

    => 4547 ∤ c   CONFIRMED with all hypotheses verified at source.
    => Supp_odd(c) ⊆ {7}   STANDS.

**Robust across the isogeny class.** The theorem is about the *strong Weil* (optimal) curve, which need not be our
minimal model. Computed both curves of the 2-isogeny class:

    curve 0: (0,1,0,-3235025292,22326945153120)      q=7 I0* pot.ORDINARY   q=4547 III pot.SUPERSINGULAR   prod c_v=32
    curve 1: (0,1,0,-29271783872,-1911371041066320)  q=7 I0* pot.ORDINARY   q=4547 III pot.SUPERSINGULAR   prod c_v=64

Identical in every hypothesis-relevant respect, so the optimality subtlety does not bite either way.

## 4. The `I_0^*` lead — chased, and it comes back NEGATIVE, but informatively

The lead was real. Prop 4.2.4's remark, verbatim:

> **Remark.** The condition "`p > 7`" is a bit stronger than we need: the proof also works without change if:
> 1. `E` is of type `I_ν^*` or **`I_0^*`** and **`p > 3`**, 2. `E` is of type III or III\* and `p > 5`, 3. `E` is of
> type IV or IV\* and `p > 3`. If `E` has type `I_ν^*` the proposition is even true for all `p`. One can show for
> `p = 5, 7` that `G` is contained in `ker F^{*2}` or in `ker V^{*2}`.

So Prop 4.2.4 **does** reach `p = 7` at type `I_0^*`. But that does not extend Theorem 4.6.3, because **the `I_0^*`
exclusion in 4.6.3 is a separate structural obstruction, not the `p > 7` condition.** Both branches of the
parametrization analysis exclude it independently:

* supersingular branch: *"...good, supersingular reduction at `p`, that are **not of type `I_0^*`**."*
* ordinary branch (Vertical Weil curves): *"Let `p` and `N` be as before: `p > 7` … **We exclude the reduction types
  `I_0^*` and `I_ν^*`.** According to Proposition 4.2.2 we are left with the strong Weil curves with potentially
  good, ordinary reduction at `p`, that are **not of type `I_0^*`**."*

Prop 4.2.4 is one input (`G ⊂ ker(V)`); relaxing its prime condition does not remove an exclusion that comes from how
the Weil curve sits on the components of the stable model of `X_0(p^2 N)`. **So `p = 7` with type `I_0^*` is doubly
outside 4.6.3, and the lead does not close it.**

`I_0^*` *is* handled elsewhere in the thesis — Remark 2 after 4.6.3, via Stevens: *"the Manin constant `c` of a strong
Weil curve `E` is not divisible by primes `p > 163` where `E` has reduction type `I_0^*` or `I_ν^*`."* Our prime is
`7`, far below 163.

## 5. Verdict

    V7_MANIN_BOUND_OPEN

`v_7(c)` for a strong Weil curve with additive type `I_0^*` and potentially ordinary reduction at `7` is not bounded
by anything located in Edi89, Edi91, ARS, Raynaud, Abbes–Ullmo, or the Stevens-based Remark 2. The later
uniform-boundedness result (additive reduction confined to a fixed finite set `S` bounds `v_p(c)` in terms of `S, p`)
is, as characterized, **existential rather than explicit**, so it does not supply a numerical target either.

**Consequence: do NOT run more `L`-digits.** `MANIN_PRECISION_GATE.txt` is arithmetically correct but currently
useless — without an explicit `v_7(c)` bound no finite precision target is logically sufficient. The 299-segment
rerun is **not** justified.

## 6. Corrected ledger

    MANIN_PRIME_SUPPORT        = SETTLED.  Supp_odd(c) ⊆ {7}.     [ARS Cor 3.7 + Edi89 Thm 4.6.3 at 4547]
    4547_ELIMINATED           = YES, all four hypotheses verified at source, robust across the isogeny class
    v_p(c) <= 1 for additive p > 7 = YES (Edi89 intro) -- newly recorded
    p ∤ c FOR ADMISSIBLE p    = FROZEN
    v_7(c) EXPLICIT BOUND     = NOT LOCATED / NOT IN EDI89          <- CORRECTED from "exists but unpublished"
    I0*_AT_p=7                = doubly outside Thm 4.6.3 (p > 7 AND the I0* exclusion, which is independent)
    PROP_4.2.4_AT_p=7_I0*     = holds (p > 3 suffices) but does NOT extend 4.6.3
    I0*_HANDLED_FOR_p > 163   = yes, via Stevens (Remark 2) -- irrelevant at 7
    MANIN_DENOMINATOR_SIZE    = OPEN, and now genuinely open rather than awaiting a read
    MORE_L_DIGITS             = NOT JUSTIFIED
    ORDINARY_BRIDGE           = NOT CLOSED

## 7. What could still close it

1. A post-Edixhoven **explicit** bound on `v_7(c)` at type `I_0^*` potentially ordinary. Not located; the natural
   place to look is work citing Edi89 §4.6 and the Stevens/Manin-constant literature after 2000.
2. An **effective** form of the uniform-boundedness theorem (explicit constant for `S = {2,3,7,2243,4547,5843}`,
   `p = 7`).
3. A curve-specific argument at `7` avoiding the Manin constant entirely — e.g. anything that bounds
   `v_7(L(E^{-7},1)/Ω)` directly. Note `7` is **excluded from the BLV-admissible lane anyway** (`7 | disc K`), so a
   `7`-specific failure costs nothing downstream; what the lane needs is the *reconstruction* to be valid at the other
   primes, and that is what the `7`-power denominator blocks.
