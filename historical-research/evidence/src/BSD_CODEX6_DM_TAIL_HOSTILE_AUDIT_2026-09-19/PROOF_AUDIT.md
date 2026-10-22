# Hostile proof audit: the route through §§3–4

Verdict: **DM_TAIL_THEOREM_FAILS_AT_THEOREM_6_STEP_2_TRACE**.

The decisive result is an invalid inference followed by two false uniform lifting assertions. This is a written mathematical audit, not a formal proof-checker result. The labels below distinguish a fatal defect, a repairable local defect, an argument checked conditional on its inputs, and material not fully verified.

## Dependency map

The claimed path to FIN is:

    integral torsion formulas / normalized traces
      → Theorem 6 (uniform finite set of lifts)
      → §3.5 (one finite auxiliary field K′, degree prime to ell)
      → Proposition 10 (local quotient coverage by E(K′))
      → Proposition 11 and Corollary 10
      → Proposition 12 Step 6 (I ⊆ I′)
      → Proposition 12's Kummer-plus-inflation decomposition
      → Sah vanishing
      → restriction–corestriction
      → Sha[ell] = 0 → Sha[ell^∞] = 0.

The class-field construction and Lemma 8 feed the middle of this chain. They do not independently supply its missing arithmetic comparison.

## §3: torsion traces and auxiliary field

| Item | Grade | Audit finding |
|---|---|---|
| §§3.1–3.3, integrality and Proposition 2's finite set of normalized traces | UNVERIFIED in full | Relevant identities, the conclusion of Proposition 2, and their use were inspected. The entire division-polynomial calculation was not replayed. Granting all of it does not repair the next step. |
| Theorem 6 Step 1 | PASS conditional on standard prime-to-p reduction facts | Reduced ell-power torsion lifts to torsion in an algebraic closure at good p ≠ ell. |
| Step 2 through equation (135) | PASS conditional on the preceding torsion identity | Substitution at one prime gives an error term in that one prime ideal; taking its global trace is legitimate. |
| Step 2, after (135), yielding (137) | **FATAL** | Membership in one prime above p does not imply that the global trace is divisible by p. The trace diagram sums contributions from all primes. See the explicit Q(i), p=17 example in the obstruction proof. |
| Steps 3–4 / Theorem 6 used uniformly in p | **FATAL** | The bounded set of proposed lifts cannot cover reduced ell-primary torsion for all auxiliary primes. A counting argument at completely split division-field primes disproves the statement. |
| Proposition 3's field construction and degree | PASS as a finite construction, with its universal-lifting claim invalid | For any chosen finite C, adjoining finitely many square roots and splitting fields of cubics gives a finite normal extension of degree 2^s3^t. It does not give the asserted universal lift coverage. |
| Proposition 5 and Corollary 8(a) | PASS conditional on standard ramification facts | Radical extensions of degree prime to ell with unit radicands are unramified at ell; the cyclotomic extension is totally ramified. |
| Corollary 8(b) wording | REPAIRABLE | K₃ contains both square-root fields; their intersection with Q(μ_ell) cannot contain both. The intended unique quadratic subfield conclusion follows from the degree bound and the appropriate one of the two roots. |
| Corollary 8(c) | PASS after that repair | The cubic splitting extensions give exponent dividing 6 over K₃; the relevant cyclotomic quotient is cyclic. Combined with the quadratic intersection this bounds its degree by 12. |

The replacements required to fix the fatal assertions are not wording corrections. Both a finite universal lift set and a fixed-field universal local quotient surjection are impossible; proofs are in [TRACE_AND_FIXED_FIELD_OBSTRUCTION.md](/Users/bsm/BSD_CODEX6_DM_TAIL_HOSTILE_AUDIT_2026-09-19/TRACE_AND_FIXED_FIELD_OBSTRUCTION.md).

## §§4.1–4.3: restriction and class fields

Restriction–inflation is used with a normal subgroup acting trivially on E[ell] after adjoining the torsion. This makes restricted cocycles homomorphisms. A global cocycle vanishing on the kernel factors through the finite quotient; its local splitting descends by injectivity of inflation with the appropriate invariant coefficient module. The occasional use of “Hom” before trivializing the action must be read as H¹/cocycles; it is not a source of Sha vanishing.

The local conductor argument has the following independent content. At good residue characteristic different from ell, an ell-Kummer extension attached to a locally split class is unramified. Prime-to-p torsion injects under reduction, and the formal group is ell-divisible. Potentially good reduction becomes good over the torsion field in the stated ell>3 setting. At potentially multiplicative primes different from ell, ramification in an ell-extension is at most tame. At primes over ell, sufficiently deep principal units are ell powers, giving a finite conductor bound.

A ray class field with those conductors therefore gives a finite container for the relevant cocycles for a **fixed ell**. Passing to its maximal exponent-ell quotient is legitimate. In particular this part neither assumes nor proves a uniform bound on the prime support of Sha.

Lemma 7's proof contains a repairable displayed containment: its unit factors away from T need not be ell powers in the S-ideles. They instead belong to I^m, the other factor already killed in the quotient. Replacing that containment by containment in I^m·(I^S)^ell gives the intended inclusion. At primes in T, the conductor choice gives I^m ⊆ N. The S-ideal-class generation property then proves the claimed exponent-ell quotient description. Galois stability gives normality of the resulting class field.

Proposition 9 and Corollary 9 are consistent with this finite-container description and the restriction–inflation sequence. The local conductor references were checked at the level of the used standard facts, not by reconstructing the cited class-field-theory books in full. These steps may be granted without any effect on the fatal defect.

## §4.4: Proposition 10, Proposition 11, Lemma 8, Corollary 10

**Proposition 10 — FATAL.** Its first substantive step uses Theorem 6 to lift a reduced local point into the fixed K′. The subsequent trace-to-the-decomposition-fixed-field operation, formal-group divisibility, and Bezout combination would work if that lift existed. It need not exist. More strongly, for every finite F/Q there are infinitely many primes with zero image of E(F) in a nonzero local quotient E(Q_p)/ell. The same obstruction persists for the semisimple residual type diag(λ₀,1) available from Lemma 9(e).

**Proposition 11 — unproved because of Proposition 10.** Replacing P₀ ∈ E(Q_p) by ξ(P)+ell Q′ with P ∈ E(K′) is precisely its use of Proposition 10. If the replacement were available, choosing an ell-preimage of P and adjusting it by ell-torsion gives the asserted equality of restricted cocycles. The algebraic torsion adjustment does not produce P.

**Lemma 8 — group-theoretic argument checked conditional on the constructed fields.** Its uses are as follows:

1. The exponent-ell abelian kernel permits an order-d₀ lift of σ₀′: raising a lift to ell removes its ell-primary order; because d₀ divides ell−1 this preserves its projection.
2. Maschke's theorem and d₀ | ell−1 decompose the specified invariant subspace into one-dimensional character spaces over F_ell.
3. For a trivial-character line Cν, a nonzero h′ in the line centralizes the order-d₀ lift. Their product has order ell·d₀ and its d₀-th power generates Cν.
4. Chebotarev realizes this product as Frobenius, avoiding any fixed finite set of primes. Compatible restriction and residue degrees give the required projection of decomposition groups.

This creates suitable testing primes. It does not show that a local Kummer point at such a prime comes from E(K′).

**Corollary 10 — unproved.** Its local-to-global matching assertion needs Proposition 11, and hence the false Proposition 10. Lemma 8 alone only supplies the prime.

Scope of the stronger obstruction: prescribing only the residual Frobenius diag(λ₀,1) does not rescue Proposition 10. The obstruction does not assert that every prime chosen with Lemma 8's additional class-field Frobenius constraint fails, or that an independent Selmer-specific replacement is impossible.

## §4.5: Lemma 9, Proposition 12, and the final argument

**Lemma 9 — checked with a small repair.** Full residual image gives commutator SL₂ and maximal abelian quotient the cyclotomic determinant. K₂/Q is actually multiquadratic; use that fact directly in the abelian-intersection argument, rather than an unsupported general inference from abelianness over K₁. The 2-and-3-power field degree rules out a nontrivial quotient of SL₂(F_ell) of that order, placing L∩K′ in Q(μ_ell). Corollary 8 then gives degree dividing 12. Consequently the specified diagonal element, the unipotent element moving its eigenline, and the nonidentity scalar β lie in the required subgroup. Excluding {2,3,5,7,13} ensures the scalar acts with β−1 invertible.

**Proposition 12 — fatal dependency at Step 6, printed page 50.** I′ is built from global Kummer classes over K′; I is built from restricted Selmer classes over Q. The annihilator subspaces H₁,H₂ give I⊆I′ exactly when H₁⊆H₂. On the trivial-character lines of H₁, the proof invokes Corollary 10 for a global Kummer representative. That is the failed arithmetic arrow. Defining I and I′ does not prove their inclusion.

There is also a harmless precision issue in Step 6: annihilation in the quotient E[ell]/X(χ) suffices. For a trivial-character line, equivariance puts its values in X(1), so being in X(χ) forces actual zero. With that justification, the written zero conclusion would follow from the unproved replacement.

Grant the inclusion for the remainder of the argument. A difference h of the Selmer and Kummer cocycles restricts to H′ with values in X(χ). Its image is stable under G′ by equivariance. The unipotent element of Lemma 9 moves X(χ), so the image must be zero. Restriction–inflation then places the remaining class in H¹(G′,E[ell]). This is valid conditional algebra.

**Sah — PASS, conditional on reaching this finite-group cohomology.** An elementary verification avoids any ambiguity about the theorem: for a cocycle c and central z,

    (z−1)c(g) = (g−1)c(z).

If z−1 is invertible on the module, v=(z−1)^(-1)c(z) gives c(g)=(g−1)v, a coboundary. The scalar β from Lemma 9 has exactly this property. Sah does not apply to an arbitrary original Selmer class without the preceding decomposition.

**Descent — PASS in cohomology.** If a class in H¹(Q,E)[ell] restricts to zero over K′, restriction–corestriction kills it by [K′:Q]. This degree is prime to ell, so the class is zero. This is cleaner than the paper's representative-level expressions (210)–(211); changing a representative may otherwise obscure its invariant coefficient field.

**Primary passage — PASS.** If Sha[ell]=0 and x has order ell^n, then ell^(n−1)x would have order ell unless x=0. Thus Sha[ell^∞]=0. This does not assume finiteness of Sha.

## What was established

The requested proof route has been reconstructed far enough to identify and independently refute the essential lifting assertions, while checking the named downstream group and cohomology steps with their hypotheses explicit. This is not a claim that every other line of the preprint has been verified. No repaired proof of Theorem 5 is supplied. No primary component of the seed's Sha is newly controlled.
