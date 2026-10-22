# FINAL REPORT — `p`-primary support of `Sha(E^{-7}/Q)`, fixed-twist hostile audit

Files: `STAGE_I_VERDICT.md` (frozen before Stage II), `STAGE_II_COMPARISON.md`,
`RequestProject/TwistSha.lean` (machine-checked arithmetic, `sorry`-free).

    STAGE_I_A = FIRST_MISSING_THEOREM (additive-prime p-part bound; bites at p = 7)
    STAGE_I_B = EIGENSPACE_REFINEMENT_UNKNOWN
    STAGE_II  = PRIOR_BOUND_CONFIRMED (run A lossy; run B not valid as a general lemma;
                the shared "equivalently A_2 = 0" overstated; exceptional set eliminated)
    CHANGED_STAGE_I_AFTER_READING_STAGE_II = no

Ordering compliance and one disclosure: `STAGE_II_ONLY/` was opened only after the Stage-I
verdict was written and committed. However the package's own root-level `STATE.json` — a
Stage-I file — contains the withheld real period and the prediction `#Sha = 49`, so I had seen
the prediction before freezing. Section 0 of `STAGE_I_VERDICT.md` records exactly which
conclusions are prediction-independent (all of the curve arithmetic, the residual-image theorem,
and the hypothesis audit; none of them uses the period or the number 49).

---

## 1. Frozen Stage-I verdict

**`FIRST_MISSING_THEOREM`.** The missing statement:

> Let `F/Q` be an elliptic curve with `L(F,1) != 0`, let `p >= 5` be a prime at which `F` has
> **additive** reduction, and assume `rhobar_{F,p}` surjective. Then
> `v_p(#Sha(F/Q)[p^∞]) <= v_p( L(F,1)·#F(Q)_tors^2 / (Omega_F · prod_v c_v) )`.

Every upper-bound mechanism that exists — Kato's divisibility with the Mazur–Tate–Teitelbaum
`p`-adic `L`-function, Greenberg/Perrin-Riou control, Kobayashi's `±`-theory, Skinner–Urban —
presupposes good or multiplicative reduction at `p`; at additive `p` the `p`-adic `L`-function
they rest on is not defined. Kolyvagin's Heegner-point bound does apply at additive `p` but is
not explicit at this conductor. Per GATE K2 this is reported as a missing statement, not as a
non-existence claim.

For the fixed curve it bites at `p = 7` (additive `I_0*`, the twisting prime) and `p = 4547`
(additive `III`); the companion trivial-zero gap bites at `p = 5843` (split multiplicative).

## 2. Theorem-by-theorem support table

Notation `L^alg = L(E^{-7},1)/Omega`. For `p >= 5` the factors `#tors^2 = 4` and
`prod_v c_v = 32` are `p`-units, so the `p`-part of the BSD quotient is `v_p(L^alg)`.

| theorem | hypotheses for `E^{-7}` | verdict |
|---|---|---|
| Gross–Zagier–Kolyvagin, analytic rank 0 | certified `L != 0` | ✔ `rank = 0`, `Sha` **finite**; gives nothing about order or support |
| Mazur (rational isogenies) + Dickson + Tate curve at `q = 2243` (`v_q(Delta) = 1`) + machine-checked non-residue witnesses | `j` non-integral (no CM), witnesses verified in Lean | ✔ **`rhobar_p` surjective for every `p >= 5`**; no Eisenstein prime `>= 5`; isogeny class is 2-power |
| Kato (Euler system) + Greenberg/Perrin-Riou control | `p >= 5`, big image ✔, `p` good ordinary or non-split multiplicative | ✔ `v_p(#Sha) <= v_p(L^alg)`; applies at all `p >= 5` except `{7, 4547, 5843}` |
| Kobayashi `±`-Iwasawa theory + Kato | `p >= 5` good supersingular (`a_p = 0` automatic), surjective `rhobar_p` ✔ | ✔ same inequality in the supersingular case (statement about this twist over `Q`, cyclotomic) |
| Skinner–Urban (opposite divisibility) | needs semistability / squarefree conductor in the rank-0 corollaries; `E^{-7}` additive at 2, 7, 4547 | ✘ **not applicable**: no unconditional lower bound on `Sha`, at any `p` |
| Greenberg–Stevens / MTT exceptional zero | `a_{5843} = +1`, split multiplicative (machine-checked) | ✘ trivial zero kills the naive rank-0 bound at `p = 5843` |
| Additive-prime Iwasawa theory | `p = 7` (`I_0*`), `p = 4547` (`III`) | ✘ **no theorem found** — this is the frozen first missing implication |
| Kolyvagin Heegner-index bound | surjective `rhobar_p` ✔; no local hypothesis at `p`, so valid at additive `p` too | ~ bound `v_p(#Sha) <= 2 v_p(I_{K'})`: effective in principle, vacuous in practice at conductor `3.2·10^17` |
| Residually reducible / Eisenstein machinery (Greenberg–Vatsal; Castella–Çiperiani–Skinner–Sprung; Keller's Eisenstein cases) | requires an Eisenstein prime | ✘ vacuous: none exists for `p >= 5` |
| Isogeny descent; torsion; Tamagawa | 2-power isogeny class; `#tors = 2`; `prod c_v = 32` | ✘ all `p`-units for `p >= 5`; contribute nothing either way |
| Explicit `p`-descent (Fisher, `p = 5, 7`) | implemented in the literature | ~ a **computation not performed**; the only visible route that could settle `p = 7` in either direction |

Categorisation demanded: *proved vanishing* — none in Stage I; *proved finiteness only* — all
`p`; *reduced to one explicit finite computation* — all `p >= 5` outside `{7,4547,5843}`;
*explicit unresolved finite set* — `{7, 4547, 5843}`; *ineffective/cofinite* — Kolyvagin;
*conjectural/BSD* — the value `49`, not used in Stage I.

## 3. Explicit exceptional prime set

    unresolved for p >= 5 :  { 7, 4547, 5843 }
      7     additive I_0*, the twisting prime; E itself is good ORDINARY at 7 (a_7(E) = -2)
      4547  additive III
      5843  split multiplicative (a_5843 = +1) -> trivial zero

## 4. Stage-II comparison (summary; details in `STAGE_II_COMPARISON.md`)

* I recomputed the period independently by 50-digit AGM and it agrees with the supplied value to
  37 digits; the packet's normalisation `Omega = 2·omega_1` is correct, and
  `L^alg ∈ [391.9978, 392.0022]`, i.e. `L^alg = 392 = 2^3·7^2`.
* **Upgrade, using Kato and not BSD:** since the only prime `>= 5` dividing `L^alg` is 7,
  `Sha(E^{-7}/Q)[p^∞] = 0` for **every** `p >= 5` outside `{7, 4547, 5843}` — conditional only on
  a certified exact evaluation of `L^alg` (rigorous period error bounds plus a modular-symbol
  denominator bound; neither is supplied in the package).
* **Is the agreement with BSD a proof?** For `p ∉ {7,4547,5843}`: yes, there is now an actual
  proof (Kato's upper divisibility), and BSD's agreement with it is a successful prediction on
  top of a proof. For `p = 7` — where BSD puts all of `#Sha` — it is **prediction only**: the
  upper-bound mechanism does not exist at additive `p`, and the lower-bound mechanism
  (Skinner–Urban) fails its hypotheses for this non-semistable twist. Nothing proves `7` is in
  the support, and nothing proves it is out.
* **The `A_2` bounds: `PRIOR_BOUND_CONFIRMED`.** Both runs' finite-level argument
  (`p^c·S ⊆ S^{(2)}`, hence `A_2 <= c`, hence `v_p(R_der) >= -2c` and
  `v_p(#Sha(E/K)[p^∞]) <= 2c`) is correct. Run A's form is true but lossy (order where the
  argument gives exponent). Run B's form is sharp here but is **not a valid general lemma**: at
  finite level `Sel_{p^n}` differs from `Sha[p^n]` by `E(Q)/p^n`, so the torsion-exponent term
  that run A carries is needed when `p | #tors`; here `#tors = 2` makes it vacuous for `p >= 5`.
* **"Equivalently `A_2 = 0`": overstated,** and the reconciliation's demotion to *sufficient, not
  equivalent* is upheld and strengthened — there are two independent failures of the equivalence
  (determinant cancellation, and the fact that Thm 2.18(5) only *bounds* the denominators).
* **Two further overstatements in the reconciliation itself:** its claim that Mazur allows only
  `2, 3, 5` as torsion primes is false (`Z/7` occurs), and its claim that `p ∤ #Sha` at rank 0
  needs "Kato **plus Skinner–Urban**" is wrong twice over (only Kato is needed, and Skinner–Urban
  does not apply to this non-semistable twist). Its "ordinary Eisenstein" framing is vacuous
  here, since no Eisenstein prime `>= 5` exists for this curve.
* **Exceptional set: smaller — in fact empty inside the admissible lane.** `p = 7` is excluded by
  BLV Hyp 1.1 (`p ∤ disc K`); and — new here — `4547` and `5843` are excluded too, because both
  divide the seed's conductor, so they are not good-ordinary primes for `E`. Every remaining
  admissible `p` is good ordinary for `E^{-7}` with surjective `rhobar_p`, so Kato applies and
  gives `Sha(E^{-7}/Q)[p^∞] = 0`.

## 5. Exact implication for the ordinary anticyclotomic BSD branch

    Conditional on [c_2] != 0 (open, unchanged) and on a certified evaluation L^alg = 392:
        the exceptional set {p admissible : p | #Sha(E^{-7}/Q)} is EMPTY,
        so the prior runs' conclusion Sha(E/K)[p^∞] = 0 — hence Sha(E/Q)[p^∞] = 0 —
        holds at EVERY admissible good-ordinary non-anomalous p, with no exceptions.
    Unconditionally on the twist side: Sha(E/Q)[p^∞] finite at every such p (prior runs' Task 6).

This is **not** `FIN`, `FORMULA` or BSD, and is not claimed to be: `[c_2] != 0` is still open, the
supersingular interface is untouched, and the anomalous `a_p = ±1` set is not known to be finite.
No claim is made about the supersingular branch of the wider project; the only supersingular
statement here is Kato/Kobayashi's cyclotomic upper bound for the fixed twist itself over `Q`,
whose hypotheses I checked for that curve.

## 6. Machine-checked component

`RequestProject/TwistSha.lean` builds without `sorry`: the model invariants and the factorisation
`Delta = 2^8·3^2·7^6·2243·4547^3·5843^2`; non-integrality of `j` (hence no CM); the traces
`a_5, a_11, a_13, a_17, a_19, a_23` and `a_3, a_2243, a_5843` (splitness at the multiplicative
primes); the non-square witnesses `a_l^2 - 4l mod p` for every `p` in Mazur's list; and
`gcd(#E(F_5), #E(F_11)) = 2` with `4497724161` a non-square, confirming `#tors = 2`. These are the
finite inputs to the residual-surjectivity theorem and to the hypothesis audit; the surrounding
arithmetic geometry (Mazur, Dickson, Tate curve, Kato, Kobayashi) is cited, not formalised.
