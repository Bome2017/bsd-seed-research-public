# STAGE I — FROZEN VERDICT (written before `STAGE_II_ONLY/` was opened)

Fixed curve

    E' := E^{-7} :  y^2 = x^3 + 159145 x^2 + 5207351716 x
    N' = cond(E') = 2^3 * 3 * 7^2 * 2243 * 4547^2 * 5843
    Delta = 2^8 * 3^2 * 7^6 * 2243 * 4547^3 * 5843^2,   c4 = 2^4*7^2*43*1013*4547
    #E'(Q)_tors = 2,  prod_v c_v = 32 = 2^5

Certified inputs used (not re-derived here): `L(E',1) in [9.054319, 9.054421]`, hence
`L(E',1) != 0`; hence by Gross–Zagier–Kolyvagin `rank E'(Q) = 0` and `Sha(E'/Q)` is finite.

---

## 0. Compliance statement, including one disclosure

* I did **not** open, list, or read anything inside `STAGE_II_ONLY/` before writing and
  committing this file. The Stage-I reasoning below is theorem-first.
* **Disclosure (a leak in the package, not a Stage-II access).** `STATE.json`, which lives at
  the package root *outside* `STAGE_II_ONLY/` and which I read while surveying the package,
  contains the quantities GATE K1b says are withheld: the field `computed_with_PARI.omega_1`
  (the real period) and the block `prediction_NOT_PROVED` (`sha_predicted: 49`,
  `predicted_support: [7]`). So I saw the prediction before freezing, through a Stage-I file.
  I report this rather than claim a blindness I do not have.
  What I can state precisely about influence:
  - Every item in §1–§3 below (model invariants, reduction types, splitness, residual image,
    which theorems have which hypotheses) is derived from the curve equation alone and is
    machine-checked in `RequestProject/TwistSha.lean`; none of it uses the prediction.
  - The identification of `p = 7` as the prime where the available machinery fails comes from
    the reduction type at 7 (additive, Kodaira `I_0*`, forced because `E'` is the twist by
    `-7` of a curve with good reduction at 7). That is a statement about hypotheses, reached
    from the local data, and it would have been reached from the local data alone.
  - I did **not** form the BSD quotient myself, and no step below uses `omega_1` or the
    number 49. Nothing here is inferred from a predicted `#Sha`.
* GATE K1 respected: no bound on `#Sha` below is obtained from the BSD quotient.

---

## 1. Independently re-derived curve data (machine-checked)

`RequestProject/TwistSha.lean`, `sorry`-free, kernel/compiler-evaluated:

| fact | Lean name |
|---|---|
| `c4 = 155281214032`, `c6 = -19291412299579840`, `Delta = 2^8 3^2 7^6 2243 4547^3 5843^2` | `TwistSha.invariants` |
| `Delta ∤ c4^3`, i.e. `j` is not integral, hence `E'` has **no CM** | `TwistSha.j_not_integral` |
| `a_5 = 2, a_11 = -2, a_13 = 4, a_17 = 6, a_19 = -4, a_23 = 0` | `TwistSha.aL_values` |
| `a_3 = 1`, `a_2243 = -1`, `a_5843 = 1` (split / non-split multiplicative) | `TwistSha.aL_at_multiplicative_primes` |
| for every `p` in `{5,7,11,13,17,19,37,43,67,163}` an `l` with `a_l^2-4l` a non-square mod `p` | `TwistSha.irreducibility_witnesses`, `...._zmod` |
| `gcd(#E'(F_5), #E'(F_11)) = 2` | `TwistSha.torsion_gcd` |
| `159145^2 - 4*5207351716 = 4497724161` is not a perfect square | `TwistSha.quadratic_factor_disc_not_square` |

Derived by hand from `(v(c4), v(Delta))` and confirmed against the supplied PARI table:

| `q` | `v_q(c4)` | `v_q(Delta)` | reduction of `E'` | Kodaira | `c_q` |
|---|---|---|---|---|---|
| 2 | 4 | 8 | additive | `I_1*` | 2 |
| 3 | 0 | 2 | split multiplicative (`a_3 = +1`) | `I_2` | 2 |
| 7 | 2 | 6 | additive, potentially good | `I_0*` | 2 |
| 2243 | 0 | 1 | **non-split** multiplicative (`a = -1`) | `I_1` | 1 |
| 4547 | 1 | 3 | additive, potentially good | `III` | 2 |
| 5843 | 0 | 2 | **split** multiplicative (`a = +1`) | `I_2` | 2 |

Model minimal at every bad prime (`v(Delta) < 12`). I independently reproduced the seed's
`a_5, a_7, a_11, a_13 = -2,-2,-2,-4` from the untwisted model
`E : y^2 = x^3 - 22735 x^2 + 106272484 x`, matching the certificate's spot checks, and found
`7 ∤ Delta(E)` with `a_7(E) = -2`: **the seed has good ordinary reduction at 7**; the additive
reduction of `E'` at 7 is exactly the ramified quadratic twist.

**Consequence for `p >= 5` bookkeeping.** `#tors = 2` and `prod_v c_v = 32` are powers of 2,
so for every `p >= 5` these factors are `p`-units and contribute nothing to any `p`-part
formula. The isogeny class matters only through 2-power isogenies (see §2), so the `p`-part
of everything is isogeny-invariant for `p >= 5`.

## 2. Residual Galois representations: an unconditional theorem for this curve

**Claim.** For every prime `p >= 5`, `rhobar_{E',p} : G_Q -> GL_2(F_p)` is **surjective**.
In particular there are no Eisenstein primes `p >= 5`, and `E'` has no rational `p`-isogeny
for any `p >= 5`.

*Proof.* (i) `E'` has multiplicative reduction at `q = 2243` with `v_q(Delta_min) = 1`
(§1, machine-checked). By the theory of the Tate curve, `rhobar_p|_{I_q}` is unipotent and is
non-trivial exactly when `p ∤ v_q(Delta)`; since `v_q(Delta) = 1` this holds for every `p`.
So the image contains an element of order `p`.
(ii) By Dickson's classification, a subgroup of `GL_2(F_p)`, `p >= 5`, containing an element
of order `p` is either contained in a Borel subgroup or contains `SL_2(F_p)`.
(iii) `j(E')` is not an integer (machine-checked), so `E'` has no CM. If `rhobar_p` were
reducible, `E'` would admit a rational `p`-isogeny, so by Mazur's theorem on rational isogenies
of prime degree `p ∈ {5,7,11,13,17,19,37}` (`43,67,163` are CM-only, tested anyway). For each
such `p` the machine-checked witnesses give a good prime `l` with `a_l^2 - 4l` a non-square
mod `p`; a reducible `rhobar_p` has both Frobenius eigenvalues in `F_p^x`, forcing
`a_l^2 - 4l` to be a square mod `p` for every good `l`. Contradiction. Hence `rhobar_p` is
irreducible for all `p >= 5`, so by (i)+(ii) the image contains `SL_2(F_p)`, and
`det rhobar_p = omega` is surjective, so `rhobar_p` is surjective. ∎

Hence also `rho_{E',p}(G_Q) ⊇ SL_2(Z_p)` for all `p >= 5` (standard lifting for `p >= 5`), so
Kato's big-image hypothesis holds at **every** `p >= 5`. Label: *proved here, with the finite
input machine-checked; Mazur's and Dickson's theorems cited, not reproved.*

Two corollaries worth recording:
* the residually **reducible / Eisenstein** branch of the literature (Greenberg–Vatsal;
  Castella–Çiperiani–Skinner–Sprung; the Eisenstein cases in Keller and Keller–Stoll) is
  **not needed and not usable** here for `p >= 5`: there is no Eisenstein prime `>= 5`;
* the Manin constant is a `p`-unit for all `p >= 5` in this isogeny class except possibly at
  `p = 7, 4547` (by Mazur/Edixhoven-type results, `p | c` forces `p^2 | 4N`, i.e.
  `p ∈ {2,7,4547}`) — and 7 and 4547 are already the two additive primes.

## 3. Mechanism-by-mechanism audit (hypotheses checked against this curve)

Throughout, `L^alg := L(E',1)/Omega_{E'}` (rational by Manin–Drinfeld). For `p >= 5` the
BSD quotient's `p`-valuation equals `v_p(L^alg)` because `#tors^2` and `prod c_v` are 2-powers.
**`L^alg` is not evaluated anywhere in Stage I.**

| mechanism | hypotheses for this curve | what it gives here |
|---|---|---|
| **GZK at analytic rank 0** (Kolyvagin; Gross–Zagier; Bump–Friedberg–Hoffstein / Murty–Murty for the auxiliary field) | satisfied (certified `L != 0`) | `rank E'(Q) = 0`, `Sha(E'/Q)` **finite**. Order and support: nothing. |
| **Kolyvagin's Heegner-point bound**, `ord_p #Sha(E'/K') <= 2 ord_p I_{K'}` | needs `rhobar_p` surjective (✓ all `p >= 5`, §2), an imaginary quadratic `K'` with the Heegner hypothesis for `N'` and `L'(E'/K',1) != 0`, `p ∤ 2 disc K'`. **No local hypothesis at `p`** — so it applies at additive `p` too | a genuine bound at every `p >= 5`, but only in terms of the Heegner index `I_{K'}`. Making it explicit needs either the Mordell–Weil generator over `K'` at conductor `~3.2*10^17` (out of computational reach) or an effective height lower bound (Hindry–Silverman: explicit but astronomically weak). **Effective in principle, vacuous in practice.** Excludes no specific prime. |
| **Kato's Euler system** (Kato 2004, Thm 17.4) + Greenberg/Perrin-Riou control ⇒ the `<=` half of the `p`-part of BSD | `p >= 5`; big image ✓ (§2); needs `p` of **good ordinary** or **non-split multiplicative** reduction (so that the MTT `p`-adic `L` exists with unit interpolation factor). Holds at every `p >= 5` with `p ∤ N'`, `a_p ≢ 0`, and at `p = 2243` | `v_p(#Sha(E'/Q)[p^∞]) <= v_p(L^alg)`. **Vanishing at every such `p` not dividing the numerator of `L^alg`** — an explicit finite set *once `L^alg` is computed*. Stage I withholds that computation. |
| **Kobayashi's `±`-Iwasawa theory** (2003) + Kato, good **supersingular** `p` | `p >= 5` good supersingular ⇒ `a_p = 0` automatically (Hasse); `rhobar_p` surjective ✓. Supersingular `p` genuinely occur here (`a_23 = a_29 = 0`) | same inequality `v_p(#Sha) <= v_p(L^alg)` in the supersingular case. So the good-reduction primes are covered uniformly, ordinary and supersingular alike. (This is a statement about **this twist over Q**, cyclotomic; it says nothing about the project's anticyclotomic supersingular interface.) |
| **Skinner–Urban** main conjecture (opposite divisibility) | requires, besides `p >= 3` good ordinary and `rhobar` irreducible + ramified at some `q||N` (✓ at `q = 2243`), a semistability/squarefree-conductor type hypothesis in the stated corollaries. `E'` is **not semistable**: additive at 2, 7, 4547 | **not usable as stated**. Consequence: the *lower* bound half is unavailable, so no theorem here proves `Sha(E'/Q)[p^∞] != 0` either. Both directions are open at `p = 7`. |
| **Split multiplicative `p = 5843`** | `a_{5843} = +1` (machine-checked) ⇒ exceptional/trivial zero of the cyclotomic `p`-adic `L` at the trivial character (Mazur–Tate–Teitelbaum; Greenberg–Stevens) | the naive rank-0 Kato bound is vacuous: `L_p(0) = 0`. A usable bound would need `v_{5843}` of the `L`-invariant. **Not available.** |
| **Additive `p = 7` and `p = 4547`** | no MTT `p`-adic `L`-function of the required kind, no Greenberg control theorem, no `±`-theory: all of these presuppose good or multiplicative reduction at `p` | **no bound at all** from the Iwasawa/Euler-system side. This is the decisive gap (see §4). |
| **Isogeny / isogeny descent** | the isogeny class is 2-power (§2: no odd-degree isogeny) | nothing at `p >= 5`. |
| **Torsion, Tamagawa, local hypotheses** | `#tors = 2`, `prod c_v = 32` | both `p`-units for `p >= 5`: they neither obstruct nor contribute. Any claimed "torsion factor" in a `p >= 5` statement is vacuous. |
| **Explicit `p`-descent / Selmer computation** | `p`-descent over `Q` for `p = 5, 7` is implemented in the literature (Schaefer–Stoll for 3; Fisher for 5 and 7) | would settle `Sha[p] = 0` (⇒ `Sha[p^∞] = 0`, since rank 0 and no `p`-torsion) at a single `p`. At conductor `3.2*10^17`, with the `7`-descent requiring class-group/unit data in large number fields, this is a **computation not performed**, not a missing theorem. Note it is the only route currently visible that could settle `p = 7` in either direction. |
| **Visibility / congruence criteria** (Cremona–Mazur and successors) | need a congruent modular form / an ambient abelian surface | these **construct** `Sha` elements (lower bounds) under congruences; they cannot prove vanishing. Nothing found for this curve; no search performed. |
| **Keller; Keller–Stoll** (`p`-part of BSD at analytic rank 0/1, incl. ordinary Eisenstein primes; complete verification of `#Sha`) | their Eisenstein input is inapplicable (no Eisenstein `p >= 5`, §2); their complete-verification method needs the full BSD-quotient computation *plus* `p`-descents at the remaining primes, at a conductor far beyond the examples treated | reduces the question to the same two ingredients: `v_p(L^alg)`, and a descent at the primes where the Iwasawa input is missing. |

## 4. The per-`p` ledger for `p >= 5`

| class of `p >= 5` | status |
|---|---|
| good reduction, ordinary (`p ∤ N'`, `a_p ≢ 0 mod p`) | `v_p(#Sha) <= v_p(L^alg)` **proved** (Kato + control, hypotheses all verified). Vanishing **proved conditionally on one finite computation** (`v_p(L^alg) = 0`), which Stage I withholds. No hypothesis fails. |
| good reduction, supersingular (`a_p = 0`) | same, via Kobayashi `±` + Kato. Same single missing computation. |
| `p = 2243`, non-split multiplicative | same as good ordinary (interpolation factor `1 + 1/p` is a unit). Same single missing computation. |
| `p = 5843`, split multiplicative | **only finiteness.** Trivial zero; a rank-0 `p`-part bound in the exceptional case, with the `L`-invariant's valuation controlled, was not found. |
| `p = 4547`, additive (`III`) | **only finiteness.** No Euler-system/Iwasawa bound at additive `p`. Kolyvagin applies but is not explicit. |
| `p = 7`, additive (`I_0*`), the twisting prime | **only finiteness.** Same gap, and it is the structurally interesting one: `E' = E ⊗ chi_{-7}` with `E` good **ordinary** at 7 (`a_7(E) = -2`), so `chi_{-7}` is the quadratic character of conductor 7 inside `Q(zeta_7)` and the natural attack is Kato in the `chi_{-7}`-branch over `Q(zeta_{7^∞})` — see §5. |
| any `p >= 5` | no Eisenstein/reducible case occurs (§2); no `p`-isogeny; torsion and Tamagawa contribute nothing. |

Categorisation demanded by the task:

* **proved vanishing** at a specific `p >= 5`: **none** — no prime is currently excluded outright.
* **proved finiteness only**: all `p >= 5` (GZK).
* **reduced to an explicit finite computation** (Kato/Kobayashi, hypotheses fully verified):
  every `p >= 5` except `{7, 4547, 5843}`. The computation is `v_p(L(E',1)/Omega_{E'})`.
* **explicit unresolved finite set** (mechanism missing, not merely uncomputed): `{7, 4547, 5843}`.
* **ineffective/cofinite**: Kolyvagin's Heegner-index bound, which covers all `p >= 5`
  including the three above, but yields no usable explicit set at this conductor.
* **conjectural/BSD-predicted**: everything else. Not used.

## 5. FROZEN VERDICT

    STAGE_I_A = FIRST_MISSING_THEOREM

**The first missing implication, stated precisely.**

> Let `F/Q` be an elliptic curve with `L(F,1) != 0`, let `p >= 5` be a prime at which `F` has
> **additive** reduction, and assume `rhobar_{F,p}` is surjective. Then
>
>     v_p( #Sha(F/Q)[p^∞] )  <=  v_p( L(F,1) * #F(Q)_tors^2 / ( Omega_F * prod_v c_v ) ).
>
> No such theorem is known to me, and I could not locate one; per GATE K2 I report the missing
> statement rather than assert that none exists. Every upper-bound mechanism I verified —
> Kato's divisibility with the Mazur–Tate–Teitelbaum `p`-adic `L`-function, Greenberg's control
> theorem, Kobayashi's `±`-theory, Skinner–Urban — presupposes good (ordinary or supersingular)
> or multiplicative reduction at `p`; at additive `p` the `p`-adic `L`-function on which all of
> them rest is not defined. Kolyvagin's bound does apply at additive `p` but is not explicit.

For the fixed curve this bites at `p = 7` and `p = 4547`, and the companion gap (trivial zero,
Greenberg–Stevens) bites at `p = 5843`.

**Concrete form of the missing theorem at `p = 7`** (the plausible attack, and exactly what is
absent from it). `E' = E ⊗ chi_{-7}`, `chi_{-7}` is the quadratic character of conductor 7,
`Q(sqrt -7) ⊂ Q(zeta_7)`, and `E` has good **ordinary** reduction at 7. For odd `p`,
`Sel_{7^∞}(E'/Q)` is the `chi_{-7}`-eigenspace of `Sel_{7^∞}(E/Q(sqrt -7))`, and Kato's Euler
system over `Q(zeta_{7^∞})` does produce a divisibility in each branch. What is missing is:

1. an **integral control/comparison theorem** identifying the `chi_{-7}`-part of
   `Sel_{7^∞}(E/Q(zeta_7))` with `Sel_{7^∞}(E'/Q)` up to a 7-unit — the local conditions differ
   precisely at the wildly ramified place above 7, where `E'/Q_7` is additive while
   `E/Q_7(zeta_7)` is good ordinary; and
2. an **integrality statement for the interpolated value at a ramified character**: the
   interpolation carries the Gauss sum `tau(chi_{-7}) = sqrt(-7)` (7-adic valuation `1/2`) and
   the comparison of `Omega_E` with `Omega_{E'}` carries a compensating `sqrt 7`; turning the
   resulting 7-adic number into `v_7(L(E',1)/Omega_{E'})` with no loss requires a statement I
   did not find in the literature.

Supply either (a) the additive-`p` bound above, or (b) items 1–2 at `p = 7`, or (c) a certified
`7`-descent on `E'`, and `p = 7` is decided. Absent all three, **nothing unconditional
restricts `7` in or out of the support.**

**What the verdict is *not*.** It is not `TWIST_SHA_PGE5_ZERO` (no prime is excluded).
It is not `TWIST_SHA_EXPLICIT_FINITE_SUPPORT`: the set would be
`{7, 4547, 5843} ∪ {p >= 5 : p | numerator(L(E',1)/Omega_{E'})}`, whose second part is a finite
computation deliberately withheld in Stage I and whose first part is *not* a computation at all
but a missing theorem. It is not `TWIST_SHA_COFINITE_ONLY` either, since the Kato/Kobayashi
statement outside `{7,4547,5843}` is fully effective — only the arithmetic input is withheld.

**Strongest true Stage-I statement, for the record:**

> Unconditionally, and with every hypothesis verified for this curve:
> `v_p(#Sha(E'/Q)[p^∞]) <= v_p(L(E',1)/Omega_{E'})` for every `p >= 5` outside
> `{7, 4547, 5843}`; `Sha(E'/Q)` is finite at every `p`; and no prime `p >= 5` is currently
> proved to lie outside the support, nor is any prime proved to lie inside it.

## 6. Stage I.B — the eigenspace question

    STAGE_I_B = EIGENSPACE_REFINEMENT_UNKNOWN

For odd `p`, `Sha(E/K)[p^∞] = Sha(E/Q)[p^∞] ⊕ Sha(E^{-7}/Q)[p^∞]` under the idempotents
`(1 ± tau)/2`, and that splitting is unproblematic at each finite layer. The obstruction is at
the `Lambda`-level: on `Gamma^- = Gal(K_∞^-/K)`, `tau` acts by inversion, so conjugation by
`tau` is the involution `iota` on `Lambda = Z_p[[Gamma^-]]`, not a `Lambda`-automorphism.
Hence `X_∞` carries a `tau`-semilinear action and does **not** decompose as a direct sum of
`Lambda`-submodules; what `tau` gives is that `Char_p` is `iota`-invariant (a functional
equation), which is a symmetry constraint, not a splitting. The consequence is that
Bertolini–Darmon Thm 2.23's leading term, which computes the order of the whole
`Sha(E/K)[p^∞]`, has no formal eigen-refinement: the natural coefficient ring on which `tau`
acts trivially is `Lambda^{tau} = Z_p`, over which no characteristic ideal argument is available.

Two honest caveats against declaring this `OBSTRUCTED`:
* the derived height pairings themselves *are* `tau`-equivariant in the weak sense
  `<x^tau, y^tau> = -<x,y>` (because `tau` inverts `Gamma^-`), which is exactly what makes the
  first height vanish on `S^+ x S^+`; so partial eigen-information does pass to the pairings,
  and I cannot rule out that a more careful derived-height computation isolates the `+` part;
* an eigen-refinement could plausibly come from outside the anticyclotomic picture entirely —
  e.g. from cyclotomic Iwasawa theory over `Q` for `E` and for `E^{-7}` separately, where the
  two eigenspaces are simply two different curves over `Q` and no splitting problem arises.
  That route is the one §3–§5 above audits, and it is blocked only at `{7, 4547, 5843}`.

First missing input, precisely: a `tau`-equivariant (`iota`-semilinear) refinement of BD Thm
2.23 computing `#(Sha(E/K)[p^∞]^+)` alone, i.e. a leading-term formula for the `iota`-eigen-part
of `Char_p` — equivalently, a characteristic-ideal theory for modules over `Lambda` with
semilinear `tau`-action that is finer than the `iota`-invariance of `Char_p`.

---

**Frozen. Written and committed before `STAGE_II_ONLY/` was opened.**
