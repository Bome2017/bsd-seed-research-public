# Propositions A and B — the family has a two-condition description

Successor document, 2026-09-10, **v2**.  Conventional (human) proofs, deliberately **not**
formalized; see `RUN013_FAMILY_MINIMISATION_AUDIT.md` §5 for why.

v2 incorporates the exposition corrections from an independent referee pass (a separate model,
which reconstructed Proposition A before reading this document) together with the sharp converse it
contributed.  See `_receipts/PROPOSITIONS_A_B.v1.md` for v1 and
`INDEPENDENT_REFEREE_VERIFICATION.md` for what was checked.

Throughout, `E` is the optimal curve `62a1` / LMFDB `62.a4`,

    E  : v² + uv + v = u³ − u² − u + 1,          minimal discriminant −496 = −2⁴·31,
    E₁ : Y² = X³ − 15X² + 64X = X(X² − 15X + 64),

identified by `X = 4(u+1)`, `Y = 8v + 4u + 4`, and `Ẽ` is the reduction of `E` modulo `q`.

---

## Proposition A

**Let `q` be a prime with `q ≡ 5 (mod 8)` and `(q/31) = −1`.  Then**

    v₂(#Ẽ(F_q)) = 2,     a_q(E) ≡ 2 (mod 8)  (in particular a_q ≠ 0),     q ∤ 372.

*Proof.*

**(i) Excluded primes and good reduction.**  `372 = 2²·3·31`, and `2, 3, 31 ≡ 2, 3, 7 (mod 8)`, so
`q ∤ 372`.  In particular `q ∉ {2, 31}`, the bad primes of `E`, so `E` has good reduction at `q` and
`#Ẽ(F_q)` is the order of an elliptic curve group over `F_q`.

**(ii) The 2-primary part is cyclic.**  Since `2 ∈ F_q^×`, the change of variables above is an
isomorphism `Ẽ ≅ E₁` over `F_q` (see (ii′)), so the two point counts agree.

For **every** odd prime `q ≠ 31`, quadratic reciprocity gives
`(31/q) = (q/31)·(−1)^{15(q−1)/2}`, since `(31−1)/2 = 15` is odd; multiplying by
`(−1/q) = (−1)^{(q−1)/2}` cancels the sign, so

    (−31/q) = (q/31)     for every odd prime q ≠ 31.

No congruence on `q` is needed.  Hence `(−31/q) = −1` here.  Now
`disc(X² − 15X + 64) = 225 − 256 = −31`, so the quadratic factor has no root in `F_q` and

    E₁(F_q)[2] = {O, (0,0)} ≅ Z/2 .

Let `G = E₁(F_q)` and let `S` be its Sylow 2-subgroup.  By the classification of finite abelian
groups `S ≅ ∏_{i=1}^{r} Z/2^{e_i}` with every `e_i ≥ 1`, and each factor contributes exactly two
elements killed by 2, so `|S[2]| = 2^r`.  The odd part of `G` contributes no nonidentity
2-torsion, so `2^r = |G[2]| = 2` and `r = 1`: **`S` is cyclic**.

**(ii′) The model transfer is an isomorphism of elliptic curves.**  With
`F(u,v) = v² + uv + v − u³ + u² + u − 1`, direct expansion gives
`Y² − X³ + 15X² − 64X = 64·F(u,v)` under `X = 4(u+1)`, `Y = 8v + 4u + 4`, whose inverse is

    u = X/4 − 1 ,        v = (Y − X)/8 ,

both denominators being units in odd characteristic.  In projective coordinates the map is
`[U:V:W] ↦ [4(U+W) : 8V + 4U + 4W : W]`, a linear automorphism of determinant `32`, and it sends
`[0:1:0] ↦ [0:8:0] = [0:1:0]`.  So on the smooth projective cubics it is an isomorphism preserving
the identity, and the point counts agree **including the point at infinity**.  At characteristic 2
the map is not invertible; at characteristic 31 both cubics are singular.  Both are excluded by (i).

**(iii) An explicit point of order 4.**  `T = (8,8)` lies on `E₁` over any field, since
`8³ − 15·8² + 64·8 = 512 − 960 + 512 = 64 = 8²`.  It is defined directly over `F_q`; no reduction of
a rational point is used.  Since `q` is odd, `8 ≠ 0`, so `T ≠ (0,0)` and `T` is not 2-torsion.  For
`Y² = X³ + aX² + bX` the duplication formula is

    x(2P) = ( (x(P)² − b) / (2 y(P)) )² ,

independent of `a` — expand `λ² − a − 2x` with `λ = (3x² + 2ax + b)/(2y)` and use `y² = x³+ax²+bx`;
the numerator collapses to `x⁴ − 2bx² + b² = (x² − b)²`.  With `b = 64` and `x(T) = 8`,
`x(2T) = ((64 − 64)/16)² = 0`, so `2T = (0,0) ≠ O`.  Hence `T` has order exactly 4 and `4 ∣ #E₁(F_q)`.

**(iv) `T` is not halved in `E₁(F_q)`.**  Suppose `T = 2P` with `P ∈ E₁(F_q)`.  Then `2P ≠ O`, so
`P ≠ O` and `y(P) ≠ 0`, and the displayed formula exhibits `x(T) = 8` as a square in `F_q`.  But
`q ≡ 5 (mod 8)` gives `(2/q) = −1`, and `(8/q) = (2/q)³ = (2/q) = −1`.  Contradiction.  Hence
`T ∉ 2E₁(F_q)`.

**(v) Conclusion.**  `S` is a **cyclic 2-group** — both hypotheses are needed, see the Remark —
and it contains `T` of order 4, so `|S| = 2^e` with `e ≥ 2`.  Write `S = ⟨g⟩` additively.  Every
element of order 4 has the form `T = 2^{e−2}·u·g` with `u` odd.  If `e ≥ 3` then
`T = 2·(2^{e−3}·u·g)`, so `T ∈ 2S ⊆ 2E₁(F_q)`, contradicting (iv).  Therefore `e = 2`, `|S| = 4`,
and `v₂(#Ẽ(F_q)) = v₂(#E₁(F_q)) = 2`.

> **Remark (both hypotheses in (v) are necessary).**  The implication
> "`S` cyclic, `|T| = 4`, `T ∉ 2S` ⟹ `|S| = 4`" is **false** without the 2-group hypothesis:
> take `S = Z/12` and `T = 3`, which has order 4 and is not in `2S = {even classes}`, yet
> `|S| = 12`.  It is also false without cyclicity: in `S = Z/4 × Z/2` the element `T = (1,0)` has
> order 4 and is not a double, yet `|S| = 8`.  Neither touches the argument above, where `S` is by
> construction the Sylow 2-subgroup and (ii) proves it cyclic — but the lemma must not be quoted in
> isolation without both hypotheses.

**(vi) The trace.**  `#Ẽ(F_q) ≡ 4 (mod 8)` and `q ≡ 5 (mod 8)` give
`a_q = q + 1 − #Ẽ(F_q) ≡ 5 + 1 − 4 = 2 (mod 8)`; in particular `a_q ≠ 0`.  ∎

Step **(iv)** is the load-bearing one.  Without the no-halving argument, (v) proves nothing.

### Corollary A1

    F62(q)  ⟺  F62min(q)      for every q : ℕ,

where `F62min(q)` is `q` prime, `q ≡ 5 (mod 8)`, `(q/31) = −1`.  (`⟹` is `F62.toMin` in
`RequestProject/Run013/Family.lean`; `⟸` is Proposition A.  The equivalence holds on all of `ℕ`, not
merely on primes, because primality is a field of both predicates.)  Hence

    F₆₂ = { q prime : q ≡ 5 (mod 8), (q/31) = −1 }.

---

## Proposition A′ — the sharp finite-field form

Contributed by the independent referee pass, which observed that Proposition A's proof never uses
that `k` is a prime field, nor that `−1` is a square.  Stated for the record; **it is not used
anywhere in the Selmer or BSD chain**, and §"scope" below says why it must not be.

**Let `k` be a finite field of characteristic `∉ {2, 31}` and let `χ_k` be its quadratic character.
Then**

    v₂(#E₁(k)) = 2   ⟺   χ_k(2) = χ_k(−31) = −1.

*Sufficiency* is Proposition A (i)–(v) verbatim, which uses only those two character conditions.

*Necessity.*  If `χ_k(−31) = +1` there are three nonidentity rational 2-torsion points; one of them
lies outside `⟨T⟩`, so together with `T` it generates a subgroup of order 8 and `v₂ ≥ 3`.  Otherwise
suppose `χ_k(−31) = −1` and `2 = s²` is a square.  The halving condition `x(2P) = 8`, i.e.
`(x² − 64)² = 32(x³ − 15x² + 64x)`, factors as

    (x² − 64)² − 32(x³ − 15x² + 64x)
      = (x² − (16 + 4s)x + 64)(x² − (16 − 4s)x + 64),

with discriminants `D_± = 32(1 ± 4s)`, `D₊D₋ = −31·32²`.  Both are nonzero (`1 ± 4s = 0` would force
`32 = 1`), and their product is a nonsquare times a square, so **exactly one** of `D_±` is a square
and the corresponding quadratic has a root `x ∈ k`.  The quartic takes the values `−2048` at `x = 8`
and `2048·31` at `x = −8`, so `x² ≠ 64`; then `y := (x² − 64)/(4s)` is nonzero, satisfies
`y² = (x² − 64)²/32 = x³ − 15x² + 64x`, and

    x(2P) = ((x² − 64)/(2y))² = (2s)² = 4s² = 8 ,

so `2P = ±T`.  Negating if necessary gives a point of order 8, hence `v₂ ≥ 3`.  ∎

**For prime fields** this reads: `q ≡ 3 or 5 (mod 8)` with `(q/31) = −1` implies
`v₂(#Ẽ(F_q)) = 2`.

### Scope — A′ does not enlarge `F₆₂`, and must not be read as doing so

The `q ≡ 3 (mod 8)` half gives the point-count valuation but **not** the trace conclusion: step (vi)
of Proposition A uses `q ≡ 5 (mod 8)`, and for `q ≡ 3 (mod 8)` the same computation yields only
`a_q ≡ 0 (mod 8)`.  The smallest witness is

    q = 11 :   11 ≡ 3 (mod 8),  (11/31) = −1,  #Ẽ(F₁₁) = 12,  v₂ = 2,  a_q = 0.

So `a_q ≠ 0` genuinely fails there.  Independently of that, `q ≡ 5 (mod 8)` is load-bearing for the
**descent** — it fixes both 2-adic local Kummer images, and Lemma 4.2 reduces to the single curve
`E₅/Q₂` via `q = 5s²` in `Q₂`.  `F₆₂` is unchanged.

---

## Proposition B

**`F₆₂` has relative natural density `1/8` among the primes:**

    lim_{x→∞}  #{ q ≤ x : q ∈ F₆₂ } / π(x)  =  1/8.

*Proof.*  By Corollary A1 the family is cut out by `q ≡ 5 (mod 8)` and `(q/31) = −1`.  The first is
one reduced residue class modulo 8; the second is 15 of the 30 nonzero classes modulo 31.  By the
Chinese Remainder Theorem these cut out exactly `1 × 15 = 15` of the
`φ(248) = φ(8)·φ(31) = 4 · 30 = 120` reduced residue classes modulo `248 = 8 · 31`.  By the prime
number theorem for arithmetic progressions with the fixed modulus 248, each reduced class modulo 248
carries relative density `1/120` among the primes.  Hence `15/120 = 1/8`.  ∎

*Citation strength — and Proposition B is not "elementary".*  The CRT count `15/120` is
elementary; the existence of the density is not, and the statement should be called **classical and
unconditional** rather than elementary.  Dirichlet's theorem on primes in arithmetic progressions gives only that each
admissible class is infinite.  Dirichlet's density theorem gives Dirichlet density `1/φ(n)`.  The
prime number theorem for arithmetic progressions gives **relative natural density** `1/φ(n)` among
the primes, and is what the statement above uses; relative natural density implies the corresponding
prime Dirichlet density and not conversely, so these are not interchangeable.  Never shorten the
phrase to "natural density": as a subset of `ℕ` any set of primes has natural density `0`.  The fixed modulus needs no uniform (Siegel–Walfisz) machinery.

---

## Exactly which existing claims these replace

Checked against the frozen, read-only project `/Users/bsm/run013-62a1-bsd2-2026-08-22/`.
**Nothing in that project was edited by this pass.**  This section is a drop-in specification.

| location | current text | disposition |
|---|---|---|
| `TARGET.md:71–79` | the six-field definition of `F₆₂` | **Restate** as the two-condition set, citing Corollary A1.  The six-field form is retained as the audited definition. |
| `src/curves/F62_INFINITY.md` (whole file, 84 lines) | infinitude via the `q = 13` Frobenius witness and Chebotarev in `K = Q(E[8], √31)` | **Retain as historical and independent evidence; it no longer carries the theorem.** Its mechanism is valid and was re-checked by the independent referee: the `q = 13` witness, the Frobenius-class construction, and the Chebotarev density argument all stand. Propositions A + B supersede it as the *primary* proof. Label it accordingly rather than deleting it — an independent route to the same conclusion is worth keeping. |
| `PROOF.md:62–63` | "`F_62` is infinite by the exact `q=13` Frobenius witness and Chebotarev argument in `src/curves/F62_INFINITY.md`" | **Replace** with Proposition B: relative natural density exactly `1/8`. |
| `BSD_CHAIN.md:264–272` (§7, first paragraph) | the same Chebotarev argument, plus "Moreover `q=5 mod 8` and `#E(F_q)=4 mod 8` force `a_q(E)=2 mod 8`, so ordinarity is automatic. Thus `F_62` is infinite." | **Replace** the infinitude sentence with Proposition B.  Keep the `a_q ≡ 2 (mod 8)` sentence — Proposition A (vi) reproves it from weaker input, so it is strengthened, not removed. |
| `evidence/INDEPENDENT_REVIEW.md:299–324` (§7) | the reviewer's independent replay of the Chebotarev argument | **Do not edit.**  This is a review record of the artifact as it stood on 2026-08-22.  Any restatement belongs in a new review. |
| `evidence/DESCENT_DERIVATION.md:486–500` | assumption ledger recording `v2(#E(F_q))=2`, `a_q!=0`, `q!=3` as "not used" | **Unchanged and now sharper**: those fields are not merely unused, they are implied.  Add a forward reference to Proposition A. |

### One substantive improvement, not just a simplification

`src/curves/F62_INFINITY.md` §2–§3 proves that every prime in the Frobenius conjugacy class `C` of
`Frob₁₃` in `Gal(Q(E[8], √31)/Q)` satisfies all six conditions.  That gives `F₆₂ ⊇ C`-primes, hence
positive density `|C|/|Gal(K/Q)|`, a quantity that document does not compute.  What it establishes is
therefore a *containment*: an infinite, positive-density subset of `F₆₂`.  It does not identify all
of `F₆₂`, and containing a positive-density subset does not by itself give the containing set a
density.  (No claim is made here that the subset is strictly smaller; the point is that equality was
never established.)

Proposition A removes the restriction to a single Frobenius class: *every* prime satisfying the two
residue conditions lies in `F₆₂`.  Corollary A1 then identifies the whole family, and Proposition B
computes its relative natural density exactly.  So this is a strengthening together with a
simplification — the `E[8]` division field drops out of the statement entirely.
