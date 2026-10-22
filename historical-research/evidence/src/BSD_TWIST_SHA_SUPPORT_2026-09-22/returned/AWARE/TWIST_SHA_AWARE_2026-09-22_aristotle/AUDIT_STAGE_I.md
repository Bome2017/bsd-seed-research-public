# STAGE I — hostile referee report on the prime support of `Ш(E^{-7}/Q)`

Fixed curve, prediction-aware run. Frozen before `STAGE_II_ONLY/` was opened.

    STAGE_I_A = TWIST_SHA_COFINITE_ONLY
                (finiteness only; no explicit finite set is proved, and no single prime p >= 5
                 is currently proved to be outside the support)

    FIRST_MISSING_THEOREM (I.A):
        A rigorous determination of the rational number  L(E^{-7},1)/Omega  — equivalently an
        explicit integer D with  D * L(E^{-7},1)/Omega  in Z, together with a certified real
        interval of half-width < 1/(2D).  The package supplies a real interval only, and
        Section 5 below proves that this interval, even combined with every integrality
        statement available here, leaves v_p(L/Omega) undetermined at EVERY prime.

    STAGE_I_B = EIGENSPACE_REFINEMENT_OBSTRUCTED
                (obstruction identified in Section 8; the missing object is an analytic one,
                 not a technical lemma)

## 0. Epistemic ground rules used in this report

* Certified inputs accepted: `L(E^{-7},1) in [9.054319, 9.054421]`, hence `L != 0`; by the
  retained Gross–Zagier–Kolyvagin theorem at analytic rank zero, `rank E^{-7}(Q) = 0` and
  `Ш(E^{-7}/Q)` finite.
* The rank-zero BSD quotient supplied in the package is treated strictly as a prediction. It
  is never used as a premise. Section 6 states what would follow *if* the exact algebraic
  `L`-value were certified, and Section 7 shows that even then the proved support is strictly
  larger than the predicted one — so nothing in this report is downstream of the prediction.
* This host has **no network access and no computer-algebra system**. Every numerical claim
  below was recomputed from scratch here in plain integer/real arithmetic and, where it is a
  finite check, re-verified independently inside Lean (`RequestProject/Main.lean`, theorem
  names quoted inline). Every statement quoted *from the literature* is labelled
  `[cited, not re-read here]`: I could not open the sources, so those citations carry my
  recollection of the statement and its hypotheses, not a source reading. Per gate K2, a
  theorem I could not locate is reported as a missing statement, never as a nonexistent one.

## 1. Independent re-verification of the fixed-curve data

Recomputed here from the model `y² = x³ + 159145 x² + 5207351716 x`, and machine-checked:

| fact | value | Lean |
|---|---|---|
| `c4` | `155281214032 = 2⁴·7²·43·1013·4547` | `TwistSha.invariants`, `TwistSha.c4_factorization` |
| `c6` | `-19291412299579840` | `TwistSha.invariants` |
| `Δ` | `2⁸·3²·7⁶·2243·4547³·5843²` | `TwistSha.disc_factorization` |
| `c4³ - c6² = 1728Δ` | holds | `TwistSha.invariants` |
| conductor factorisation | `2³·3·7²·2243·4547²·5843` | `TwistSha.conductor_factorization` |
| `v_q(Δ) < 12` at all bad `q` | yes, from the factorisation | — |

Consequences I checked rather than assumed:

* **The model is globally minimal** (`v(Δ) < 12` everywhere), so its invariant differential is
  a Néron differential. The "minimal model" `[0,1,0,-3235025292,22326945153120]` quoted in the
  package has the *same* `c4`, `c6`, `Δ` as the given twist model, i.e. the two differ by a
  translation only; the periods therefore agree. (Checked here.)
* **No complex multiplication.** `v_2243(c4) = 0` while `v_2243(Δ) = 1`, so `v_2243(j) < 0` and
  `j` is not an algebraic integer (`TwistSha.j_not_integral_at_2243`). A CM curve has integral
  `j`. This is needed for every residual-image theorem below and was not established in the
  package.
* **Real period.** The cubic has three real roots (`0 > -46039.96… > -113105.03…`), `Δ > 0`, so
  `E(R)` has two components. Recomputing by AGM at 50 digits gives, for the Néron differential
  `ω = dx/2y`, a period over the identity component of
  `0.011548941266157222748917603067…`, matching the package's `omega[1]` to every digit shown,
  so `Ω = ∫_{E(R)}|ω| = 2·omega[1] = 0.0230978825323144454978…`.
  **Methodological objection (upheld):** the package selects `Ω = 2·omega[1]` *because that
  choice makes the BSD quotient a perfect square*. That is a BSD-circular selection rule (it
  uses Cassels' squareness of `#Ш`, which is a statement about the true `#Ш`, to fix an input
  of the formula predicting `#Ш`). The choice happens to be right, but it is right for the
  geometric reason `Δ > 0 ⇒ two real components`, which is what must be recorded.
* **Torsion.** `#E(F_5) = 4`, `#E(F_11) = 14`, `#E(F_13) = 10`, `#E(F_17) = 12`; their gcd is
  `2` (`TwistSha.torsion_divides_two`). Torsion injects into `E(F_ℓ)` at odd good `ℓ`, and
  `(0,0)` is a rational `2`-torsion point, so `E^{-7}(Q)_tors ≅ Z/2` exactly. In particular
  **no `p ≥ 5` divides the torsion**; the package's value is confirmed by an independent route.
* **Tamagawa numbers: only the 2-3-part can matter.** I did not need Tate's algorithm at `2`
  and `3`. For `p ≥ 5` the Kodaira type is determined by `(v(c4), v(Δ))`: at `7`,
  `(2,6) → I_0*`, so `c_7 ∈ {1,2,4}`; at `4547`, `(1,3) → III`, so `c_4547 = 2`; at `2243`,
  `(0,1) → I_1`, so `c_2243 = 1`; at `5843`, `(0,2) → I_2`, so `c_5843 ≤ 2`. At the remaining
  bad primes `2` and `3`, `c_v` divides `4` (additive at 2) resp. `c_3 ≤ 2` (`I_2`). Hence
  **`∏_v c_v` is `{2,3}`-smooth, so `p ∤ ∏ c_v` for every `p ≥ 5`** — independently of the
  package's PARI value `32`, which my constraints are consistent with.
* **Reduction types at the multiplicative primes**, computed here (`-c6` a square mod `q`?):
  `q = 2243` **non-split**, `q = 5843` **split**, `q = 3` split
  (`TwistSha.multiplicative_split_types`). This was *not* in the package and it matters: see
  Section 4.4.

Net effect: for `p ≥ 5` the "easy" hypotheses of every `p`-part theorem — `p ∤ #tors`,
`p ∤ ∏ c_v` — hold. The obstructions are elsewhere.

## 2. The residual representation: no Eisenstein prime at all

This is the one place where the news is good, and it is stronger than anything the package
claims.

* By **Mazur's isogeny theorem** `[cited, not re-read here]`, a rational `p`-isogeny for
  `E/Q`, `p` prime, forces `p ∈ {2,3,5,7,11,13,17,19,37,43,67,163}`. So `ρ̄_p` can only be
  reducible for `p ≥ 5` inside the explicit list `{5,7,11,13,17,19,37,43,67,163}`.
* For each of those ten primes I exhibit a good prime `ℓ` such that `a_ℓ² - 4ℓ` is a **nonzero
  non-square mod p**, so `x² - a_ℓ x + ℓ` is irreducible mod `p` and `ρ̄_p(Frob_ℓ)` has no
  eigenvalue in `F_p`: certificates `(p, ℓ) = (5,17), (7,5), (11,5), (13,17), (17,11), (19,5),
  (37,17), (43,5), (67,5), (163,5)`, machine-checked in
  `TwistSha.irreducible_certificates` (the `a_ℓ` are themselves recomputed there by point
  counting, `TwistSha.ap_small`).
* **Conclusion: `ρ̄_p` is irreducible for every prime `p ≥ 5`.** `E^{-7}` has no Eisenstein
  prime `≥ 5`. The usual reason `p`-part results fail — residual reducibility — does not
  occur here, so the ordinary *Eisenstein* case (Greenberg–Vatsal style, Keller's Eisenstein
  work `[cited, not re-read here]`) is simply not needed.
* Stronger: for every `5 ≤ p ≤ 37` I give certificates killing both Cartan normalisers and all
  exceptional projective images (`A₄, S₄, A₅`), so `ρ̄_p` is **surjective** there
  (`TwistSha.surjectivity_certificates`). For `p > 37`: `E^{-7}` is non-CM and has a rational
  `2`-isogeny, and Lemos' theorem on Serre's uniformity for curves with a rational cyclic
  isogeny of prime degree gives surjectivity for all `p > 37` `[cited, not re-read here — this
  is the one citation the conclusion "surjective for all p ≥ 5" rests on]`. Without it, Mazur
  + Bilu–Parent–Rebolledo still leave the normaliser-of-non-split-Cartan case open for large
  `p` (Serre's uniformity is open in that case), and one falls back on: irreducible for all
  `p ≥ 5` (proved above unconditionally), which is what Kato actually needs.

**Consequence for the audit:** every hypothesis of the Iwasawa-theoretic machinery that is
about the *residual representation* is satisfied at every `p ≥ 5`. Whatever blocks the
conclusion is not the Galois image.

## 3. Ordinary / supersingular / anomalous behaviour

Recomputed here for all good `p < 300`: supersingular exactly at `p = 23, 29, 131, 167, 281`;
all `a_p` are even, so **no anomalous prime** (`a_p = ±1`) occurs in that range
(`TwistSha.supersingular_below_fifty` machine-checks the `p < 50` part). Since `E^{-7}` has a
rational `2`-torsion point, `a_p ≡ p+1 (mod 2)` forces `a_p` even at every odd good `p`:
**`a_p = ±1` is impossible at every odd prime**, so the anomalous case never arises for this
curve. (Elkies: infinitely many supersingular `p` `[cited, not re-read here]`, so the
supersingular case cannot be avoided by a finite exclusion.)

## 4. Route-by-route audit

### 4.1 Kolyvagin / Gross–Zagier–Kolyvagin (the retained input)

Gives: `rank = 0` and `#Ш < ∞`. That is **all** it is used for here, and all it gives without
further work. The quantitative Kolyvagin bound — `#Ш(E/K')[p^∞]` divides the square of the
index of the Heegner point in `E(K')`, for an auxiliary imaginary quadratic `K'` satisfying the
Heegner hypothesis and with `L'(E/K',1) ≠ 0` — is effective *in principle* but requires (i) a
choice of `K'`, (ii) the Heegner point and a generator of `E(K')`, (iii) their heights. At
conductor `3.19·10^17` none of this is computable, and a numerical height comparison would
reintroduce exactly the rationality problem of Section 5. Kolyvagin's hypotheses on `ρ̄_p` are
satisfied here (Section 2); the obstruction is purely the uncomputability of the index.
**Verdict: finiteness only; no explicit prime excluded.**

### 4.2 Kato's Euler system + the cyclotomic main conjecture

`[cited, not re-read here]` Kato's divisibility (Astérisque 295, Thm 17.4) applies to `E/Q`
at an odd prime `p` of **good ordinary or multiplicative** reduction with `ρ̄_p` irreducible
(image containing `SL₂(Z_p)` in the sharp form). Combined with Greenberg's control theorem /
Schneider's formula it yields, at analytic rank zero, the **upper** half of the `p`-part of BSD:

        v_p(#Ш(E/Q)[p^∞])  ≤  v_p( L(E,1)·#E(Q)_tors² / (Ω · ∏_v c_v) ).

Hypothesis check on this curve, `p ≥ 5`:

| hypothesis | status here |
|---|---|
| `p` odd | ok |
| `ρ̄_p` irreducible | **proved above for every `p ≥ 5`** |
| `p` good ordinary or multiplicative | fails at `p ∈ {7, 4547}` (additive) and at the good **supersingular** primes (infinitely many) |
| `p ∤ ∏ c_v`, `p ∤ #tors` | **proved above for every `p ≥ 5`** |
| exact value of the right-hand side | **NOT AVAILABLE** — Section 5 |

So the theorem is available at most `p ≥ 5`, and is *vacuous as applied*, because its
right-hand side is not known at a single prime.

### 4.3 Skinner–Urban, and `p`-converse theorems

`[cited, not re-read here]` Skinner–Urban supply the *reverse* divisibility, which upgrades
Kato's inequality to an equality. Two remarks, both against the package's interests:

* An equality is **not** what one wants for a vanishing statement; it is Kato's `≤` that could
  kill primes. Skinner–Urban can only *create* nonvanishing conclusions.
* Their hypotheses are in any case not clearly met: the standard statement requires `p` good
  ordinary, `ρ̄_p` irreducible (ok here), and a ramification/squarefree-type condition — there
  must be a prime `q ∥ N` at which `ρ̄_p` is ramified, and several versions require `N`
  squarefree. Here `N = 2³·3·7²·2243·4547²·5843` is **not** squarefree. I could not check the
  precise form of the hypothesis at source. Reported as such, not resolved.

`p`-converse theorems (rank `0 ⇔ Selmer corank 0` directions) are also of the wrong shape: they
convert rank information into analytic information, not into `Ш`-order information.

### 4.4 Multiplicative primes, and the exceptional zero at `p = 5843`

`p = 2243` (non-split `I_1`) and `p = 5843` (split `I_2`) are primes `≥ 5` of multiplicative
reduction, so they are inside Kato's reach in principle. But at `p = 5843` the reduction is
**split** (computed here, `TwistSha.multiplicative_split_types`), i.e. `α_p = 1`, and the
interpolation factor `(1 - α_p^{-1})²` of the `p`-adic `L`-function vanishes at the central
point: this is the Mazur–Tate–Teitelbaum **exceptional (trivial) zero**. The passage from the
main conjecture to the finite-level bound then degenerates, and the leading term involves the
Greenberg–Stevens `L`-invariant `[cited, not re-read here]`. I could not locate an
unconditional `p`-part-of-BSD upper bound at a split multiplicative prime; per K2 that is a
**missing statement**, not an absent theorem. `p = 2243` is non-split, so no trivial zero
arises there.

This is an anti-anchoring finding: `5843` is a prime the prediction does not flag at all, and
it is a prime where the standard machinery visibly degenerates.

### 4.5 Supersingular primes

`[cited, not re-read here]` For good supersingular `p ≥ 5` one has `a_p = 0` by Hasse, and
Kobayashi's `±`-Iwasawa theory (Invent. Math. 152, 2003) turns Kato's divisibility into the
same upper bound. Hypotheses (`p ≥ 5`, `a_p = 0`, `ρ̄_p` irreducible) hold here whenever `p` is
good supersingular. So supersingular primes are **not** an obstruction to the shape of the
argument — they are an obstruction only if one insists on the *ordinary* lane. They inherit the
same fatal dependence on the exact algebraic `L`-value.

### 4.6 Additive primes `p = 7` and `p = 4547`

Both are `≥ 5` and both are additive (`I_0*` at 7 — potentially good, since `v_7(j) = 0`;
`III` at 4547). Kato's main conjecture, Greenberg's control theorem and Kobayashi's
`±`-theory are all stated for `p` of good or multiplicative reduction; at additive `p` no
unconditional upper bound for `v_p(#Ш)` was located. `p = 7` is additionally excluded from the
anticyclotomic lane by `p ∤ disc K = -7`, and is the twisting prime. **These two primes are
unreachable by every route audited here, independently of any `L`-value certification.** Note
`4547` is again a prime outside the predicted support.

### 4.7 Descent, isogeny descent, visibility, complete verification

* **Explicit `p`-descent for `p ≥ 5`** requires class-group and unit computations in fields of
  degree `p²-1` over `Q` attached to a curve of conductor `3.19·10^17`: not feasible, and not
  feasible in principle at this size with current algorithms.
* **Isogeny descent** needs a rational `p`-isogeny. Section 2 proves there is none for any
  `p ≥ 5` (irreducibility certificates). So this route is *provably* unavailable — which also
  means the predicted `49 = 7²` cannot be explained by a `7`-isogeny.
* **Visibility / congruence criteria** (Cremona–Mazur and successors) can *exhibit* elements of
  `Ш` coming from congruent modular forms; they cannot prove vanishing. They could in principle
  falsify a vanishing claim; running them needs modular symbols at level `3.19·10^17`.
* **Keller–Stoll-type complete verification** of BSD at analytic rank 0 `[cited, not re-read
  here]` combines (i) exact algebraic `L`-value via modular symbols and (ii) an exact
  computation of `Ш` via descent. Both steps cost at least `O(N)` at level `N ≈ 3·10^17`.
  Infeasible here, on this host or any.

### 4.8 Is there any theorem converting a certified central value into `p`-part information
without BSD?

Only through an Iwasawa-theoretic divisibility, i.e. 4.2/4.5 — and those consume the *algebraic*
`L`-value `L/Ω`, a rational number, not a real approximation. The one classical device that
produces the algebraic `L`-value of a *quadratic twist* in closed form is the
Waldspurger/Kohnen–Zagier/Gross formula, which expresses `L(E^D,1)·√|D|/Ω_E` as (a fixed
rational multiple of) the **square of a coefficient of a weight-3/2 form** attached to the seed
`[cited, not re-read here]`. This is the missing tool that would make the exactness step
rigorous, and it also explains structurally why a perfect square appears — so the package's
"the quotient is a square, therefore the normalisation is right" is a coincidence of the
correct answer, not evidence. Applying it requires the seed curve's level (`≈ 6.5·10^15`) and
the relevant weight-3/2 form, which is out of reach here; the seed is not even in the package.

## 5. The bottleneck, stated precisely and proved

Every surviving route ends at the same demand:

> know `v_p( L(E^{-7},1)/Ω )` exactly.

What is available:

1. `L(E^{-7},1) ∈ [9.054319, 9.054421]` (certified) and `Ω = 0.02309788253231444549783…`
   (recomputed here). Hence `L/Ω ∈ (391.99779, 392.00221)`, half-width `≈ 2.2·10^-3`.
2. `L(E,1)/Ω ∈ Q` (Birch–Manin) `[cited, not re-read here]`.
3. `p`-integrality of the modular symbol at non-Eisenstein `p` `[cited, not re-read here]`:
   since `ρ̄_p` is irreducible for **all** `p ≥ 5` (Section 2), the denominator of `L/Ω` is
   `{2,3}`-smooth. This is the strongest integrality statement I can justify here.

What that does *not* give:

* Two distinct rationals of denominator `≤ B` differ by `≥ 1/B²`, so an interval of width
  `4.4·10^-3` pins the value only among denominators `B ≤ 15`. Since `392` is the unique
  rational of denominator `≤ 15` in the interval, the value is `392` **provided** the
  denominator is `≤ 15`. Nothing proves that.
* The smallest `{2,3}`-smooth denominator `d` with `1/d < 2.21·10^-3` is `d = 486`; from there
  on the interval contains infinitely many admissible candidates. Two explicit ones:
  `200705/512 = 392.001953…` (numerator `= 5·40141`) and `857305/2187 = 392.000457…`
  (numerator divisible by `5`, denominator odd, so not even `2`-integrality would help).
  Both are inside the certified interval and both have `v_5 > 0`.
* In general: **for every prime `p` the certified interval contains a rational with `2`-power
  denominator whose numerator is divisible by `p`.** This is proved, in Lean, as
  `TwistSha.certified_interval_does_not_pin_valuation` (general density statement:
  `TwistSha.exists_p_divisible_dyadic_mem_Ioo`).

So the certified data, plus every integrality statement available, **fail to exclude
`v_p(L/Ω) > 0` at any prime whatsoever**. The step "nearest integer 49" in the package is a
rounding, not a theorem — and per gate K1b it is precisely the step that separates prediction
from proof. Note this is not a quibble about one more digit: pinning the value to a rational
with `{2,3}`-smooth denominator bounded by `D` needs precision `< 1/(2D)`, and no `D` is known.

**First missing implication (the answer to "state the first missing implication"):**

    certified real interval for L(E^{-7},1)   ⟹   the exact rational L(E^{-7},1)/Ω.

Everything downstream (Kato, Kobayashi, the `p`-part bound) is in place, with all hypotheses
verified above, and is waiting on exactly this.

## 6. What would be proved if that gap were closed — and only then

Grant, hypothetically, a certificate that `L/Ω = 392 = 2³·7²` exactly (the label is
*hypothesis*, not prediction-promotion; the same analysis applies to any certified value).
Then, for `p ≥ 5`, `v_p(L·#tors²/(Ω∏c_v)) = v_p(L/Ω)`, because `#tors = 2` and `∏c_v` is
`{2,3}`-smooth (Section 1), and the Kato/Kobayashi upper bound would give

* `Ш(E^{-7}/Q)[p^∞] = 0` for every `p ≥ 5` that is of **good** reduction (ordinary via Kato,
  supersingular via Kobayashi) **or non-split multiplicative** — i.e. for all `p ≥ 5` except
  `p ∈ {7, 4547, 5843}` — *provided* `p ≠ 7` also in the sense `v_p(L/Ω) = 0`, which holds for
  all `p ≥ 5, p ≠ 7`.
* At `p = 7` the bound would read `v_7(#Ш) ≤ 2` and could never give vanishing; and `7` is
  additive, so the bound is not even available.
* At `p = 4547` (additive) and `p = 5843` (split multiplicative, exceptional zero) no bound is
  available at all, in either direction, and `v_p(L/Ω) = 0` is irrelevant without a theorem to
  feed it to.

## 7. Anti-anchoring: where the prediction and the theorems part company

* The predicted support is a **single** prime. The best conceivable outcome of the audited
  machinery, after closing the Section 5 gap, is vanishing outside `{7, 4547, 5843}` — an
  exceptional set containing **two primes the prediction does not flag**, for reasons that have
  nothing to do with the size of `Ш` (additive reduction; a trivial zero of the `p`-adic
  `L`-function). The prediction is therefore *stronger* than anything available.
* Without closing that gap the proved statement is weaker still: **no prime `p ≥ 5` is
  currently known to be outside the support.** The gap between prediction and proof is not a
  handful of primes; it is all of them.
* I searched for obstructions independent of the prediction and found them at `4547` and
  `5843`; conversely I found that the obstructions one would *expect* — Eisenstein primes,
  torsion primes, Tamagawa primes, anomalous primes, CM — do **not** occur on this curve
  (Sections 1–3). That asymmetry is the substance of this report.
* Classification demanded by K1b: the statement `#Ш(E^{-7}/Q) = 49`, and its support `{7}`, is
  **prediction only**. Not proved, at any prime, in either direction: `v_7(#Ш) > 0` is equally
  unproved, since Skinner–Urban's hypotheses are unverified here and `7` is additive.

## 8. Stage I.B — the eigenspace question

**Verdict: `EIGENSPACE_REFINEMENT_OBSTRUCTED`.** The obstruction is analytic, not technical.

1. *Semilinearity.* On the anticyclotomic tower `Γ^- ≅ Z_p`, `τ γ τ^{-1} = γ^{-1}`, so `τ` acts
   on `Λ = Z_p[[Γ^-]]` by the involution `ι` and on a Selmer module `X` semilinearly:
   `τ(λx) = ι(λ)τ(x)`. The eigenspaces `X^±` are therefore **not** `Λ`-submodules; they are
   modules over `R = Λ^{ι=1} = Z_p[[γ+γ^{-1}-2]]`, over which `Λ` is free of rank 2. All that
   semilinearity gives at the level of characteristic ideals is `Char_Λ(X) = Char_Λ(X)^ι`, a
   symmetry, **not** a factorisation. Nothing in this forces `Char` to be a product of two
   ideals matching the `±` parts.
2. *The derived heights are anti-equivariant, so the regulator is an inter-eigenspace
   determinant.* `τ` acts on `I/I²  ≅ Γ^- ⊗ Z_p` by `-1`, hence on `I^k/I^{k+1}` by `(-1)^k`,
   so the `k`-th derived height satisfies `h_k(x^τ, y^τ) = (-1)^k h_k(x,y)`. For odd `k` — in
   particular the first height, which is where the argument lives — `h_k` **vanishes on
   `S^+ × S^+` and on `S^- × S^-`** and is a perfect pairing only *between* the two
   eigenspaces. Its determinant is then an invariant of the pair `(S^+, S^-)` jointly, with no
   factorisation into a `+`-regulator times a `-`-regulator. (Incidentally this is the same
   fact that makes the freeze's own `s^- = 0 ⇒ S^{(2)} = S` step work; it cuts both ways.)
3. *The analytic side does not factor either, and this is decisive.* The anticyclotomic
   `p`-adic `L`-function interpolates `L(E/K, χ)` for anticyclotomic characters `χ`; only at
   `χ = 1` does this factor as `L(E,1)·L(E^{-7},1)`. For `χ ≠ 1` the value is that of a
   `GL₂/K` object with no factorisation into a `Q`-part and a twist-part. An eigenspace-refined
   leading-term formula would need an analytic object interpolating the `+`-part alone; no such
   object exists in the anticyclotomic theory, and manufacturing one is equivalent to replacing
   the anticyclotomic main conjecture by the two **cyclotomic** main conjectures for `E/Q` and
   for `E^{-7}/Q` separately.
4. *Constructive consequence.* Point 3 says the natural home for `Ш(E/Q)[p^∞]` is the
   cyclotomic theory for the seed itself (Kato, with Skinner–Urban if an equality is wanted),
   not a refinement of the anticyclotomic formula. If the seed's cyclotomic data are available,
   the `-`-part — and hence this whole twist question — is bypassed. The freeze is right that
   the exceptional set `{p | #Ш(E^{-7}/Q)}` is an artifact of aiming at the `K`-statement; it
   is wrong to expect the repair to come from splitting `Char_p`.

I did not find, and do not claim the nonexistence of, a `τ`-equivariant (twisted group ring)
main conjecture with a leading-term formula fine enough to isolate the `+`-part. **Missing
statement:** an anticyclotomic main conjecture over `Λ ⋊ ⟨τ⟩` (or over `R = Λ^{ι}`) whose
analytic side is a `+`-part `p`-adic `L`-function, together with a derived-height regulator
refined to `S^+`.

## 9. Summary ledger

    PROVED HERE (unconditional, machine-checked where finite):
      model minimal; c4, c6, Δ, conductor factorisations
      E^{-7} is non-CM (j not integral at 2243)
      E^{-7}(Q)_tors = Z/2; no p ≥ 5 divides the torsion
      ∏_v c_v is {2,3}-smooth; no p ≥ 5 divides it
      ρ̄_p irreducible for EVERY p ≥ 5 (Mazur + explicit Frobenius certificates)
      ρ̄_p surjective for 5 ≤ p ≤ 37 (explicit certificates); for p > 37 modulo Lemos
      no anomalous prime (a_p is even at every odd p)
      2243 non-split multiplicative; 5843 SPLIT multiplicative
      the certified L-interval does not determine v_p(L/Ω) at any prime (Lean)

    PROVED ELSEWHERE, IMPORTED:
      L(E^{-7},1) ≠ 0 (certificate) ⇒ rank 0 and #Ш < ∞ (GZK)

    NOT PROVED, FOR EACH p ≥ 5:
      Ш(E^{-7}/Q)[p^∞] = 0 — at no prime p ≥ 5 is this currently established

    FIRST MISSING IMPLICATION:
      certified real interval for L(E^{-7},1)  ⟹  exact rational L(E^{-7},1)/Ω
      (needs: explicit denominator bound D, plus precision < 1/(2D); or a
       Waldspurger/Gross-type closed form for the twisted algebraic L-value)

    STRUCTURALLY UNREACHABLE EVEN THEN:
      p = 7 (additive, potentially good; also the twisting prime)
      p = 4547 (additive, type III)
      p = 5843 (split multiplicative ⇒ exceptional zero of the p-adic L-function)
