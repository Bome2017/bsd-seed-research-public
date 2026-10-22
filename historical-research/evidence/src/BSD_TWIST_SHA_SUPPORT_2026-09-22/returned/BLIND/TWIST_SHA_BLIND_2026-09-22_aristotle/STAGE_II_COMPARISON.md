# STAGE II — adversarial comparison (opened only after `STAGE_I_VERDICT.md` was committed)

    CHANGED_STAGE_I_AFTER_READING_STAGE_II = no
    STAGE_II = PRIOR_BOUND_CONFIRMED (with two refinements and three overstatements recorded)

Ordering compliance: `STAGE_I_VERDICT.md` was written and committed (`git` commit
"Stage I: frozen verdict…") before any file in `STAGE_II_ONLY/` was read. The one disclosure
is the package-side leak of the withheld period and prediction through the root-level
`STATE.json`, reported in §0 of the Stage-I verdict.

---

## 1. The prediction versus the frozen Stage-I verdict

`BSD_QUOTIENT_PREDICTION.txt`: `Omega = 2*omega_1 = 0.0230978825…`, `prod c_v = 32`,
`#tors = 2`, giving `#Sha(E^{-7}/Q) = L*#tors^2/(Omega*prod c_v) ∈ [48.99972, 49.00028]`,
predicted `49 = 7^2`, predicted support `{7}`.

I recomputed the period independently (50-digit AGM on the real roots
`0 > -46039.9629613… > -113105.0370386…`):

    2*pi/AGM(sqrt(e1-e3), sqrt(e1-e2)) = 0.02309788253231444549783520613454076…
    half of it = 0.01154894126615722274891760306727038…  = the supplied omega_1 (agrees to 37 digits)

So the supplied `omega_1` is the period of the Néron differential `dx/(2y)` over one real
component, `Omega = 2*omega_1` is the full real period (two components, `Delta > 0`), and the
packet's "square-check" normalisation argument is correct. With the certified `L`-interval,

    L^alg := L(E^{-7},1)/Omega  ∈  [391.99779, 392.00221],   and  392 = 2^3 * 7^2 .

**Comparison of verdicts.** My frozen Stage-I verdict is `FIRST_MISSING_THEOREM`, which is
*weaker* than the prediction: the prediction names the support exactly (`{7}`), Stage I names
no prime at all. But the gap is narrower than "prediction versus nothing", and in one direction
it is now closed by a theorem rather than by BSD — see §2.

## 2. What the revealed period actually buys, without BSD (GATE K1 respected)

Stage I §3 proved, with every hypothesis checked for this curve: for every `p >= 5` at which
`E^{-7}` has good (ordinary or supersingular) or non-split multiplicative reduction — i.e. every
`p >= 5` except `{7, 4547, 5843}` — Kato's Euler-system divisibility together with the
Greenberg/Perrin-Riou control theorem (supersingular case: Kobayashi's `±`-theory) gives the
**upper half** of the `p`-part of BSD:

    v_p( #Sha(E^{-7}/Q)[p^∞] )  <=  v_p( L^alg )        (`#tors^2` and `prod c_v` are 2-powers).

This is a proved theorem, not BSD: it is one divisibility, and the opposite one
(Skinner–Urban) is *not* available here (§4(c)). Feeding in the arithmetic input
`L^alg = 392 = 2^3 * 7^2`, whose only prime factor `>= 5` is 7:

> **Stage-II upgrade (conditional only on a certified exact evaluation of `L^alg`):**
> `Sha(E^{-7}/Q)[p^∞] = 0` for **every** prime `p >= 5` with `p ∉ {7, 4547, 5843}`.
> Hence `supp(#Sha(E^{-7}/Q)) ∩ {p >= 5} ⊆ {7, 4547, 5843}`.

Labels, explicitly:
* *proved theorem*: the inequality `v_p(#Sha) <= v_p(L^alg)` at those `p` (Kato; Kobayashi;
  hypotheses verified in Stage I §2–§3, residual surjectivity machine-checked);
* *p-integrality of `L^alg` at `p >= 5`*: holds because no `p >= 5` is Eisenstein for this curve
  (Stage I §2), so the modular symbol is `p`-integral;
* *isogeny/Manin caveat discharged*: the isogeny class is 2-power (no odd-degree isogeny,
  Stage I §2), so for `p >= 5` the `p`-parts of `L^alg` and of `#Sha` are isogeny-invariant
  (Cassels), and `p | ` Manin constant would force `p^2 | 4N`, i.e. `p ∈ {2, 7, 4547}`;
* *numerical input still to be certified*: that `L^alg` is **exactly** `392` and not merely
  within `4.5·10^{-3}` of it. That needs (i) the real period with rigorous error bounds — my
  AGM computation is high-precision but not interval-certified, and the packet's is a PARI
  float — and (ii) a denominator bound for the modular symbol. Both are routine; neither is
  done in this package. Until they are, the upgrade is *proved modulo one certified
  computation*, which is a strictly weaker status than "proved".

At `p = 7` nothing changes: the mechanism itself is missing (additive reduction), so even
`v_7(L^alg) = 2` cannot be converted into `v_7(#Sha) <= 2`. At `p = 4547` (additive) and
`p = 5843` (split multiplicative, trivial zero) likewise.

**Is the agreement with the prediction a proof?** Partly, and it is important to separate the
two halves:
* "no prime `p >= 5` other than 7 divides `#Sha(E^{-7}/Q)`" — for `p ∉ {4547, 5843}` this is now
  **proof** (Kato + the numerical `L^alg`), not merely a successful prediction;
* "`7` *does* divide `#Sha`, and `#Sha = 49` exactly" — this remains **prediction only**. No
  unconditional lower bound is available: the Skinner–Urban divisibility, which would supply
  `v_p(#Sha) >= v_p(L^alg)`, fails its hypotheses here (§4(c)), and no descent was performed.
  So BSD's agreement with the theorem-first result at `p ∉ {7,4547,5843}` is a successful
  prediction plus an independent proof; at `p = 7` it is a prediction and nothing else.

## 3. Audit of the `A_2` bounds (Stage-II item 2)

Both runs prove `p^c · S ⊆ S_p^{(2)}` and conclude `A_2 <= c`. I checked the derivations line by
line and re-derived them.

* The finite-level step is **correct**. With `e^± = (1±tau)/2` (`p` odd) and the finite-layer
  form of BD Lemma 3.1, `<,>_{1,n}` vanishes on `Sel^+ x Sel^+` and on `Sel^- x Sel^-`; writing
  `m` for the exponent of `Sel_{p^n}(E/K)^- ≅ Sel_{p^n}(E^{-7}/Q)` and `z = x+y`, `z' = x'+y'`,
  one has `<mz, z'> = m<x,x'> + <x, m y'> = 0`. Bilinearity is used correctly in both runs
  (run A's displayed line is a compressed but valid rearrangement). Hence `m·Sel_n ⊆ Sel_n^{(2)}`,
  and in the limit `p^c S ⊆ S^{(2)}`, so `A_2 <= c` since `S̄^{(2)} ⊆ S`.
* The consequence `v_p(R_der) >= -2A_2` and `v_p(#Sha(E/K)[p^∞]) <= 2A_2` is correct: `R_der` is
  the determinant of the `2 x 2` Gram matrix of `⟪,⟫_2`, i.e. `⟪P_1,P_2⟫_2^2` (the `k = 2`
  pairing is alternating), each entry with denominator at most `p^{A_2}` by Thm 2.18(5).

**Refinement 1 — run A is valid but lossy.** Run A states
`A_2 <= v_p(#Sha(E^{-7}/Q) · #E^{-7}(Q)_tors)`. The argument it gives actually yields the
*exponent*, not the order. Orders dominate exponents, so the statement is true; it is simply not
sharp.

**Refinement 2 — run B is sharp here but overstated as a general lemma.** Run B states
`A_2 <= c` with `p^c` the exponent of `Sha(E^{-7}/Q)[p^∞]`, dropping run A's torsion factor. The
argument needs `p^c` to kill `Sel_{p^n}(E^{-7}/Q)` at **finite** level, and
`0 -> E^{-7}(Q)/p^n -> Sel_{p^n} -> Sha[p^n] -> 0` shows the exponent of `Sel_{p^n}` can exceed
that of `Sha[p^∞]` by the `p`-part of the torsion exponent. So the correct general statement is

    A_2  <=  v_p( exp Sha(E^{-7}/Q)[p^∞] )  +  v_p( exp E^{-7}(Q)_tors[p^∞] ) ,

i.e. run A's shape with exponents. For *this* curve the second term vanishes for every `p >= 5`
(`#tors = 2`, machine-checked twice in `RequestProject/TwistSha.lean`), so run B's bound is
correct as applied, and the reconciliation's conclusion that the two bounds have the same support
`{p : p | #Sha(E^{-7}/Q)}` is right.

**Verdict on item 2: `PRIOR_BOUND_CONFIRMED`.** Neither bound is refuted; run A is lossy, run B
is not a valid general lemma but is valid for this curve; the exceptional set they derive is the
right one *as the set where their `K`-statement fails*.

## 4. Overstatements found (Stage-II item 5)

**(a) "equivalently `A_2 = 0`" — the reconciliation's demotion is correct, and there are two
distinct failures of equivalence, not one.**
Both runs wrote that `v_p(R_der) >= 0` is "equivalently" `A_2 = 0`. Adjudication: `A_2 = 0` is
*sufficient only*, and for two independent reasons.
1. `R_der = ⟪P_1,P_2⟫_2^2` is a determinant. Entries of valuation `-A_2` can produce a
   determinant of non-negative valuation by cancellation; in the `2 x 2` antisymmetric case
   `R_der` is a single entry squared, so here the obstruction is milder but still real: what is
   needed is `v_p(⟪P_1,P_2⟫_2) >= 0` for the *specific* basis, not saturation of `S^{(2)}`.
2. Even `A_2 > 0` does not force `⟪,⟫_2` to be non-integral: Thm 2.18(5) gives an **upper bound**
   `p^{A_k}` on the denominators, not an exact denominator. So `A_2 = 0` is sufficient for
   integrality, and integrality is sufficient for `v_p(R_der) >= 0`, and neither arrow reverses.
The reconciliation states one of these two; I confirm it and add the second.
`NEEDED: v_p(R_der) >= 0`, with `A_2 = 0` a sufficient structural criterion, is the correct freeze.

**(b) A factual error in the reconciliation, §3.** It asserts: *"By Mazur the only primes that
could ever appear in torsion are 2, 3, 5."* That is wrong: Mazur's theorem allows `Z/7Z`, so 7 is
a possible torsion prime. The error is harmless here (`#tors = 2` exactly, which I verified
independently: the quadratic factor's discriminant `4497724161` is not a square, and
`gcd(#E(F_5), #E(F_11)) = 2`), but in a document whose purpose is to grade other runs' rigour it
should be corrected — the more so since the prime it wrongly excludes is 7.

**(c) An overstatement in the reconciliation, §5, route 2.** It writes that `p ∤ #Sha(E^{-7}/Q)`
at rank zero is "the `p`-part of BSD at rank 0 — Kato's divisibility **plus Skinner–Urban** for
good ordinary non-Eisenstein `p`". Two corrections:
  * only **Kato's** divisibility is needed for the direction that matters (an upper bound on
    `Sha`); Skinner–Urban supplies the opposite divisibility, which is needed only to prove
    `Sha` non-trivial;
  * Skinner–Urban is **not applicable to this twist** in the form quoted: its rank-zero BSD
    corollaries carry a semistability / squarefree-conductor hypothesis, and `E^{-7}` has
    additive reduction at 2, 7 and 4547 (`N' = 2^3·3·7^2·2243·4547^2·5843`). So the lower half of
    the `p`-part of BSD is unavailable here at every `p`.
  Also, the "ordinary **Eisenstein** case" flagged as the relevant Keller input is vacuous for
  this curve: there is **no Eisenstein prime `p >= 5`** (Stage I §2, machine-checked witnesses).
  The relevant Keller/Keller–Stoll input is the *complete-verification* method, not the
  Eisenstein one.

**(d) Not an error, but an anchoring risk worth recording.** `STATE.json`, a Stage-I-visible
file, contains both the withheld period and the prediction `#Sha = 49`. Any run that reads the
package root before `GATE.md` is no longer blind. The blinding of this experiment is broken at
the packaging level.

## 5. Does Stage I make the prior exceptional set smaller, larger or unchanged? (item 4)

**Smaller — and, within the admissible lane, empty.**

The prior runs' exceptional set is `X = {p admissible : p | #Sha(E^{-7}/Q)}`. Admissible means
(BLV Hyp 1.1 + BD): `p >= 5`, `p ∤ disc K = -7`, `p` good ordinary and non-anomalous for the
seed `E`, `rhobar_{E,p}` surjective.

1. `p = 7` is outside the lane already (`p ∤ disc K`), as the prediction file notes.
2. `p = 4547` and `p = 5843` — my two other unresolved primes — are **also outside the lane**:
   both divide the seed's conductor `N = 2^3·3·2243·4547^2·5843`, so `E` does not have good
   reduction there. This observation is new here and it matters: it means *every one of the three
   primes at which my Stage-I audit finds no mechanism is already excluded from the ordinary
   anticyclotomic lane on independent grounds.*
3. For every remaining admissible `p`: `p >= 5`, `p ∤ N`, `p ≠ 7`, so `E^{-7}` also has good
   reduction at `p` (a quadratic twist by `-7` changes reduction only at 2 and 7) and is ordinary
   there (`a_p(E^{-7}) = ±a_p(E)`). Stage I §2 gives `rhobar_{E^{-7},p}` surjective. Hence Kato's
   bound applies and `v_p(#Sha(E^{-7}/Q)) <= v_p(L^alg) = 0`.

> **Therefore `X = ∅`** — conditional only on the certified exact evaluation `L^alg = 392`, and
> **not** on BSD. The prior runs' exceptional set is eliminated, not merely bounded.

## 6. Exact implication for the ordinary anticyclotomic BSD branch

Combining the prior runs' chain (which I did not re-derive from BLV/BD source; I audited their
`A_2` step only) with §5:

    conditional on [c_2] != 0, and on the certified evaluation L^alg = 392:
        Sha(E/K)[p^∞] = 0   at EVERY admissible good-ordinary non-anomalous p,
        with NO exceptional set;
        in particular Sha(E/Q)[p^∞] = 0 at every such p.

and unconditionally on `[c_2]`, from the prior runs' Task 6, `Sha(E/Q)[p^∞]` is finite at every
such `p`.

What this does **not** do:
* it does not prove `[c_2] != 0`, which remains the standing open hypothesis;
* it does not touch the supersingular interface for the seed, nor the anomalous `a_p = ±1`
  primes; the reconciliation's §4 point stands — "cofinite" still means the complement of two
  sets that are not known to be finite, so this is not `FIN`;
* it does not prove the `p`-part of BSD for the twist at any `p`: only the upper divisibility;
* it says nothing about `p = 7`, `4547`, `5843` for the twist itself — and the first of these is
  exactly where the BSD quotient predicts all of `#Sha(E^{-7}/Q)` to live.
* No claim of `FIN`, `FORMULA` or full BSD is made anywhere in this audit.

## 7. Stage-II freeze

    STAGE_II = PRIOR_BOUND_CONFIRMED
      - run A's bound: correct, lossy (order where exponent suffices);
      - run B's bound: correct for this curve, but not a valid general lemma (the torsion
        exponent term is needed when p | #tors);
      - the shared "equivalently A_2 = 0": OVERSTATED, the reconciliation's demotion to
        "sufficient, not equivalent" is upheld and strengthened (two independent failures);
      - the reconciliation's own Mazur-torsion claim (§3) and its Skinner–Urban / Eisenstein
        framing (§5) are overstated; corrected above;
      - the derived exceptional set is the right set, and my Stage-I audit plus the revealed
        period shows it to be EMPTY inside the admissible lane.

    CHANGED_STAGE_I_AFTER_READING_STAGE_II = no
      Stage I asked what is proved without the withheld arithmetic input; Stage II supplies that
      input. The Stage-I verdict FIRST_MISSING_THEOREM (the additive-p bound, biting at p = 7)
      is untouched by everything in STAGE_II_ONLY/: nothing there supplies a theorem at an
      additive prime, and the prediction of `#Sha = 49 = 7^2` in fact places the entire predicted
      Sha at precisely the prime where the machinery is missing.
