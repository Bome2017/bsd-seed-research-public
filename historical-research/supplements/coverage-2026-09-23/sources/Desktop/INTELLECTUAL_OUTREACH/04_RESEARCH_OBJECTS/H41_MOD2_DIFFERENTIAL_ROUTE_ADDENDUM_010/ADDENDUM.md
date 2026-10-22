# Tenth addendum — the mod-2 differential route `(D1)–(D3)–(E)`, with `(D2)` PROVED and `(D)` unverified

**Tier: ROUTE RECORD + ONE VERIFIED SYMBOLIC STEP + A SOURCE-ABSENCE FINDING.** No research object was
launched, no Codex or Aristotle run, no finite-level computation. Prior objects unmodified and
byte-identical: `ac82f3ad…`, `d5888b62…`, `82b6730f…`, `81ac107b…`, `35f21882…`, `0bfb6b5e…`,
`3eb98a60…`, `da70ec51…`, `c1a6f8ea…`, `b7ebbf00…`, `8af7a2a5…`.

`ADDENDUM_009` withdrew the `ℓ = 2` Vatsal application. This object records the operator's successor
route, which does **not** go through Vatsal's odd-`ℓ` argument, together with what of it is now proved.

## 1. The route, as proposed

    (D)   ARS: for a maximal Hecke ideal of residue characteristic 2 with 2 ‖ N, if U_2 acts by a
          nonzero scalar on the m-part of the regular differentials, then
              dim_{F_2} H^0(X_0(N)_{F_2}, Ω)[m] ≤ 1.
    (D1)  ω̄_η ∈ H^0(X_0(2p)_{F_2}, Ω)   for  ω_η = d log F_p.
    (D2)  W_2^*(ω̄_η) = ω̄_η.
    (D3)  ω̄_η = ω̄_f  as global regular dualizing differentials mod 2.
    (E)   the relevant ordinary Eisenstein étale line is one-dimensional.

with `(D3) + (E)` the candidate route to `(C)`. Tier: **PROPOSED**, except where stated below.

The operator's own caveat is recorded and endorsed: **`(D3)` does not give `(C)`.** In characteristic 2
two 2-torsion classes can share a differential realisation while differing in the étale/unit-root part.
`(C) χ_p = α_p (mod 2)` remains the target; `(X) T_p ∈ π̂(E₀)[2]` from `ADDENDUM_009` §5 is untouched.

## 2. `(D2)` — VERIFIED, symbolically in `p`

`computation/verify_W2_eta.py`, receipt `receipts/W2_ETA_VERIFICATION.txt`. `p` is a symbol throughout;
the family values `n = 5,7,13,17,19,31` appear only as a consistency echo. In the divisor ordering
`(1,2,p,2p)` with `r_F = (2p−1, 2−p, p−2, 1−2p)` and the frozen squarefree cusp matrix:

**(a) The `W₂` exponent shift is exactly as proposed.** Atkin–Lehner `W₂` acts on divisors `d = 2^a p^b`
of `N = 2p` by `a ↦ 1−a`, i.e. the index interchange `1↔2`, `p↔2p`. Then

    r_perm − r_F = (3−3p, 3p−3, 3−3p, 3p−3) = (−3(p−1), 3(p−1), −3(p−1), 3(p−1)),

every entry even because `p` is odd. With `e = 3(p−1)/2`, the vector `r_G = (−e, e, −e, e)` satisfies
`r_F + 2·r_G − r_perm = (0,0,0,0)` identically.

**(b) `G_p` is a genuine modular function on `Γ₀(2p)`.** All four eta-quotient conditions hold:
`Σ r_G = 0` (weight zero); `Σ d·r_G = 3(p²−1)/2` and `Σ (N/d)·r_G = −3(p²−1)/2`, both `≡ 0 mod 24`
since `v₂(3(p²−1)/2) = n ≥ 3` and `3 |` it; and `∏ d^{r_G} = 2^{2e}`, a perfect square, so the character
is trivial.

**(c) The divisor identity.** `div(F_p) = k·(1,0,0,−1)` with `k = (p²−1)/8` reproduced from the matrix;
`div(G_p) = ((p²−1)/16)·(−1,1,−1,1)`, integral since `v₂(p²−1) = n+1 ≥ 6`; and

    div(F_p) + 2·div(G_p) = k·(0, 1, −1, 0).

**(d) The `W₂` cusp action is not assumed — it is forced by the matrix's own rows.** Row 1 is `N/d`
(so `c₁ = [0]`), row 4 is `d` (so `c₄ = [∞]`), and permuting the divisor indices of row 1 gives row 2
exactly, of row 4 gives row 3 exactly. Hence `c₂ = W₂[0]` and `c₃ = W₂[∞]`, which is precisely what (c)
requires. Therefore `W₂^*(div F_p) = div F_p + 2·div G_p`, and since two functions with equal divisors on
a curve differ by a constant,

    F_p|W_2 = c · F_p · G_p²   for some constant c.

**(e) `d log` kills the constant.** So `W₂^*(ω_η) = ω_η + 2·d log G_p`, and reducing mod 2 gives
`W₂^*(ω̄_η) = ω̄_η`. **`(D2)` therefore needs no determination of `c` at all** — the one loose end in the
proposal is not a loose end.

This is uniform in `p`, not a finite check. It rests on the standard eta-quotient modularity criterion and
on the frozen cusp matrix, both already in the record.

Consistent with, and unchanged by, this: the H41 newform has `a₂ = 1`, so `W₂f = −f`, hence
`W₂ω̄_f = ω̄_f` mod 2. Both differentials carry the same `W₂`-symmetry.

## 3. `(D1)` — arithmetic core confirmed, geometry NOT verified

The arithmetic input the local argument needs is confirmed symbolically:
`v₂(p²−1) = v₂(p−1) + v₂(p+1) = 1 + n`, so for `M = (p²−1)/8`,

    v₂(M) = n − 2 = m ≥ 3   for every negative-branch member,

so `2 | M` — indeed `8 | M` — uniformly. Also `v₂(e) = 0`, so `e = 3(p−1)/2` is **odd**.

The three local statements — pole loss at a horizontal cusp because `2 | M`, `2^a` killed by relative
differentiation on a vertical component, and `dx/x` being an allowed generator of the dualizing sheaf at a
node `xy = 2` with `d log F_p = (a−b)dx/x + du/u` — are **not verified here**. They are geometry on the
minimal regular semistable model, not arithmetic this object can check. `(D1)` is recorded as a proposed
elementary lemma with its arithmetic hypothesis discharged. One further ingredient it needs is already in
the frozen record: `F_p` is a modular unit, so its divisor is supported on the cusps and no interior poles
arise.

## 4. `(D)` is UNVERIFIED, and task 4 cannot be executed from frozen material

`computation/audit_source_presence.sh`, receipt `receipts/SOURCE_PRESENCE.txt`.

* **`[Vat99]` is identified**: from Vatsal 2003's own bibliography (line 1903), the étale
  multiplicity-one Theorem 2.7 lives in *V. Vatsal, "Canonical periods and congruence formulae", Duke
  Math. J. 98 (1999), no. 2*. **That paper's text is not in the corpus** — no source file carries that
  title; every hit on the phrase is a citation inside another work. So the proposed task *"retrieve
  [Vat99] Thm 2.7 and determine whether its étale statement allows residue characteristic 2 when `2 ‖ N`
  and `U₂ = 1`"* **cannot be carried out from frozen material.** It is a paywalled 1999 journal article;
  no retrieval was attempted, and none would be within the standing constraints without authorisation.
* **No Agashe–Ribet–Stein text is present.** The only Agashe source in the corpus is the 2018 **solo**
  JTNB paper *Rational torsion in elliptic curves and the cuspidal subgroup*, already audited in
  `ADDENDUM_009` §2 — a different work, containing "Wiles" 0 times, "multiplicity one" 0 times,
  "Lemma 5.17" 0 times, "Proposition 5.10" 0 times.

Therefore **`(D)`, its Lemma 5.17, and its Proposition 5.10 are recorded as handed in by the operator and
UNVERIFIED here**, as is the description of the `2 ‖ N` special fibre as two copies of `X₀(p)_{F₂}` glued
at supersingular points with exceptional components, and the claim that a vanishing `q`-expansion kills
the differential on the component containing `∞`.

**A standing-accuracy note, stated factually.** Of the four literature renderings handed into this
architecture, the three whose sources were present in the corpus — Vatsal Prop 5.3, Byeon–Kim Thm 2.2,
Agashe 2018 — each differed from the source in a load-bearing hypothesis, and one of those differences
invalidated the deduction (`ADDENDUM_009`). `(D)` is the fourth and its source is absent. Nothing follows
about whether `(D)` is true; what follows is that `(D1)–(D3)` must not be advanced past PROPOSED, and no
object may treat `(D)` as established, until the ARS text is read directly.

## 5. What `(D3)` would and would not buy

Granted `(D1)`, `(D2)` and `(D)`, the argument sketched is: `(B) Θ_p ≡ f (mod 2)` — already proved
symbolically and frozen in `ADDENDUM_005` — makes `δ := ω̄_η − ω̄_f` have zero `q`-expansion at `∞`; the
`q`-expansion vanishing kills `δ` on the component containing `∞`; `(D2)` and `W₂`'s interchange of the
two main components carry that to the other; the remaining exceptional `P¹`s are killed the same way.
That would give `(D3)`, a uniform theorem-level step rather than another finite example.

It would **not** give `(C)`. The residual gap is `(E)`, and `(E)` is exactly the étale multiplicity-one
statement whose source is missing. So the route's two ends — `(D)` at the start and `(E)` at the finish —
both currently rest on one unread paper apiece.

## 6. Status

    (D2)   PROVED, uniform in p, here.  Needs no constant c.
    (D1)   arithmetic core confirmed (2 | M, indeed 8 | M); local geometry unverified.
    (D)    UNVERIFIED — no ARS text in the corpus.
    (D3)   PROPOSED, conditional on (D), (D1), (D2) and the special-fibre description.
    (E)    PROPOSED; its source [Vat99] Thm 2.7 is not in the corpus.
    (X)    unchanged from ADDENDUM_009 — T_p ∈ π̂(E₀)[2] still unproved.
    (C)    χ_p = α_p (mod 2) — still the target.
    uniform optimality E_0 = E — still open; the B position with C_2 x C_2 is still live.
    positive branch — still entirely outside this architecture.

**The H41 seed remains unproved.**
