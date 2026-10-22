# Propositions A and B — the family has a two-condition description

Successor document, 2026-09-10.  Conventional (human) proofs, deliberately **not** formalized;
see `RUN013_FAMILY_MINIMISATION_AUDIT.md` §5 for why.

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
isomorphism `Ẽ ≅ E₁` over `F_q`, so the two point counts agree.  As `q ≡ 1 (mod 4)`,
`(−1/q) = +1`; quadratic reciprocity for `q ≡ 1 (mod 4)` gives `(31/q) = (q/31) = −1`; hence
`(−31/q) = −1`.  Now `disc(X² − 15X + 64) = 225 − 256 = −31`, so the quadratic factor has no root in
`F_q` and

    E₁(F_q)[2] = {O, (0,0)} ≅ Z/2 ,

so the 2-Sylow subgroup `S` of `E₁(F_q)` is **cyclic**.

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

**(v) Conclusion.**  `S` is cyclic and contains `T` of order 4, so `|S| ≥ 4`.  If `|S| = 2^k` with
`k ≥ 3`, write `S = ⟨g⟩`; the two elements of order 4 are `g^(2^{k−2})` and its inverse, and
`g^(2^{k−2}) = 2·g^(2^{k−3})` because `k − 3 ≥ 0`.  So `T ∈ 2S ⊆ 2E₁(F_q)`, contradicting (iv).
Therefore `|S| = 4` and `v₂(#Ẽ(F_q)) = v₂(#E₁(F_q)) = 2`.

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

## Proposition B

**`F₆₂` has relative natural density `1/8` among the primes:**

    lim_{x→∞}  #{ q ≤ x : q ∈ F₆₂ } / π(x)  =  1/8.

*Proof.*  By Corollary A1 the family is cut out by `q ≡ 5 (mod 8)` and `(q/31) = −1`.  The first is
one reduced residue class modulo 8; the second is 15 of the 30 nonzero classes modulo 31.  By the
Chinese Remainder Theorem these cut out exactly `1 × 15 = 15` of the
`φ(248) = φ(8)·φ(31) = 4 · 30 = 120` reduced residue classes modulo `248 = 8 · 31`.  By the prime
number theorem for arithmetic progressions with the fixed modulus 248, each reduced class modulo 248
carries relative density `1/120` among the primes.  Hence `15/120 = 1/8`.  ∎

*Citation strength.*  Dirichlet's theorem on primes in arithmetic progressions gives only that each
admissible class is infinite.  Dirichlet's density theorem gives Dirichlet density `1/φ(n)`.  The
prime number theorem for arithmetic progressions gives **natural** density `1/φ(n)` and is what the
statement above uses; natural density implies Dirichlet density and not conversely, so these are not
interchangeable.  The fixed modulus needs no uniform (Siegel–Walfisz) machinery.

---

## Exactly which existing claims these replace

Checked against the frozen, read-only project `/Users/bsm/run013-62a1-bsd2-2026-08-22/`.
**Nothing in that project was edited by this pass.**  This section is a drop-in specification.

| location | current text | disposition |
|---|---|---|
| `TARGET.md:71–79` | the six-field definition of `F₆₂` | **Restate** as the two-condition set, citing Corollary A1.  The six-field form is retained as the audited definition. |
| `src/curves/F62_INFINITY.md` (whole file, 84 lines) | infinitude via the `q = 13` Frobenius witness and Chebotarev in `K = Q(E[8], √31)` | **Superseded** by Propositions A + B. Retain the file: its §2 remains a correct independent derivation, and the `q = 13` witness stays useful as a worked example. |
| `PROOF.md:62–63` | "`F_62` is infinite by the exact `q=13` Frobenius witness and Chebotarev argument in `src/curves/F62_INFINITY.md`" | **Replace** with Proposition B: relative natural density exactly `1/8`. |
| `BSD_CHAIN.md:264–272` (§7, first paragraph) | the same Chebotarev argument, plus "Moreover `q=5 mod 8` and `#E(F_q)=4 mod 8` force `a_q(E)=2 mod 8`, so ordinarity is automatic. Thus `F_62` is infinite." | **Replace** the infinitude sentence with Proposition B.  Keep the `a_q ≡ 2 (mod 8)` sentence — Proposition A (vi) reproves it from weaker input, so it is strengthened, not removed. |
| `evidence/INDEPENDENT_REVIEW.md:299–324` (§7) | the reviewer's independent replay of the Chebotarev argument | **Do not edit.**  This is a review record of the artifact as it stood on 2026-08-22.  Any restatement belongs in a new review. |
| `evidence/DESCENT_DERIVATION.md:486–500` | assumption ledger recording `v2(#E(F_q))=2`, `a_q!=0`, `q!=3` as "not used" | **Unchanged and now sharper**: those fields are not merely unused, they are implied.  Add a forward reference to Proposition A. |

### One substantive improvement, not just a simplification

`src/curves/F62_INFINITY.md` §2–§3 proves that every prime in the Frobenius conjugacy class `C` of
`Frob₁₃` in `Gal(Q(E[8], √31)/Q)` satisfies all six conditions.  That gives `F₆₂ ⊇ C`-primes, hence
positive density — but the density obtained is `|C|/|Gal(K/Q)|`, which is at most `1/8` and is not
computed there.  Proposition A removes the restriction to a single Frobenius class: *every* prime
satisfying the two residue conditions is in `F₆₂`.  So the family is not merely infinite; it is
exactly `1/8` of the primes, and the `E[8]` division field drops out of the statement entirely.
